#!/usr/bin/env python3
"""Offline, browser-based Mermaid parsing/render/style/contrast audit.

Requires PyYAML and Playwright with Chromium. Uses a local installed Mermaid ESM
build via intercepted HTTP routes; no CDN or external HTTP requests are allowed.
Outputs per-block sources, SVG/PNG and light/dark host previews plus JSON/Markdown.
Source lint is deliberately conservative, not a replacement for Mermaid's parser.
"""
import argparse
import asyncio
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlparse

import yaml


def extract(path):
    text = path.read_text(encoding='utf-8')
    fenced = [(m.start(),m.end()) for m in re.finditer(r'^```[^\n]*\n.*?^```\s*$',text,re.M|re.S)]
    headings = [(m.start(), m.group(0).lstrip('# ')) for m in re.finditer(r'^#{1,6} .+$', text, re.M) if not any(a<=m.start()<b for a,b in fenced)]
    for index, match in enumerate(re.finditer(r'^```mermaid\s*\n(.*?)^```\s*$', text, re.M | re.S), 1):
        section = next((title for pos, title in reversed(headings) if pos < match.start()), '(preamble)')
        yield index, section, match.group(1)


def configuration(code):
    match = re.match(r'^---\n(.*?)\n---\n', code, re.S)
    cfg = (yaml.safe_load(match.group(1)) or {}).get('config', {}) if match else {}
    if not isinstance(cfg, dict):
        raise ValueError('config must be a YAML mapping')
    return cfg


def lint(code, cfg):
    issues = []
    for key, value in cfg.get('themeVariables', {}).items():
        if re.search(r'color|bkg|background|border|fill|stroke', key, re.I):
            if not isinstance(value,str) or not re.fullmatch(r'#[0-9a-fA-F]{3}(?:[0-9a-fA-F]{3})?', value):
                issues.append({'status':'FAIL','check':'theme-color-format','key':key,'value':value})
    if re.search(r'^\s*%%\s*$', code, re.M):
        issues.append({'status':'FAIL','check':'bare-comment'})
    if re.search(r'^(?:flowchart|graph)\b', code, re.M):
        if len(re.findall(r'^\s*subgraph\b', code, re.M)) != len(re.findall(r'^\s*end\s*$', code, re.M)):
            issues.append({'status':'FAIL','check':'subgraph-balance'})
        declarations = re.findall(r'^\s*([A-Za-z][\w]*)\s*(?:\[|\(|\{)', code, re.M)
        for node in set(declarations):
            if declarations.count(node)>1:
                issues.append({'status':'FAIL','check':'duplicate-node-declaration','id':node})
        known = set(declarations) | set(re.findall(r'^\s*subgraph\s+([A-Za-z]\w*)', code, re.M))
        known |= set(re.findall(r'\b((?:edge_|layout_)\w+)@', code))
        defs = set(re.findall(r'^\s*classDef\s+(\w+)', code, re.M))
        css = cfg.get('themeCSS', '')
        for ids, role in re.findall(r'^\s*class\s+([\w,]+)\s+(\w+)\s*$', code, re.M):
            for node in ids.split(','):
                if node not in known:
                    issues.append({'status':'FAIL','check':'invalid-class-reference','id':node})
            if role not in defs and not re.search(r'\.'+re.escape(role)+r'\b', css):
                issues.append({'status':'FAIL','check':'missing-class-definition','class':role})
    return issues


async def run(args):
    from playwright.async_api import async_playwright
    args.output.mkdir(parents=True, exist_ok=True)
    dist = args.mermaid_dist.resolve()
    package = json.loads((dist.parent/'package.json').read_text())
    metadata = {'renderer':'offline local Mermaid ESM + Python Playwright (not mmdc)',
                'mermaid_version':package['version'],'mermaid_dist':str(dist),
                'esm_sha256':hashlib.sha256((dist/'mermaid.esm.min.mjs').read_bytes()).hexdigest(),
                'vscode_preview':'NOT TESTED','github_preview':'NOT TESTED'}
    results = []
    async with async_playwright() as pw:
        options = {'headless':True}
        if args.no_sandbox: options['args']=['--no-sandbox']
        if args.browser_executable: options['executable_path']=args.browser_executable
        browser = await pw.chromium.launch(**options)
        metadata['browser_version'] = browser.version
        metadata['browser_executable'] = args.browser_executable or pw.chromium.executable_path
        page = await browser.new_page(viewport={'width':1600,'height':1000}, device_scale_factor=1)
        loaded_layouts = set()
        async def route(request):
            path = unquote(urlparse(request.request.url).path)
            if path=='/index.html':
                await request.fulfill(content_type='text/html',body='<body style="margin:0"><div id="diagram"></div></body>')
                return
            target = (dist/path.removeprefix('/mermaid/')).resolve()
            if path.startswith('/mermaid/') and target.is_relative_to(dist) and target.is_file():
                if target.name.startswith(('elk-','dagre-')): loaded_layouts.add(target.name)
                await request.fulfill(path=target,content_type='application/javascript')
            else:
                await request.abort()
        await page.route('**/*', route)
        await page.goto('http://audit.local/index.html')
        await page.evaluate("async()=>{window.mermaid=(await import('/mermaid/mermaid.esm.min.mjs')).default}")
        await page.add_script_tag(content=Path(__file__).with_name('mermaid_audit_browser.js').read_text())
        warnings = []
        page.on('console', lambda msg: warnings.append(msg.text) if msg.type in ['warning','error'] else None)
        for source in args.sources:
            source = source.resolve()
            blocks=list(extract(source))
            if not blocks:
                results.append({'document':str(source),'block':0,'section':'(document)','parse':'NOT TESTED','svg':'NOT TESTED','lint':[{'status':'FAIL','check':'no-mermaid-blocks'}]})
            for index,section,code in blocks:
                try: cfg=configuration(code)
                except Exception as exc:
                    results.append({'document':str(source),'block':index,'section':section,'yaml':'FAIL','error':str(exc)})
                    continue
                is_graph=bool(re.search(r'^(flowchart|graph|erDiagram)\b',code,re.M))
                variants=['original']+(['dagre','elk'] if args.engines and is_graph else [])
                for variant in variants:
                    altered=code
                    if variant!='original':
                        if re.search(r'^  layout:.*$',altered,re.M):
                            altered=re.sub(r'^  layout:.*$',f'  layout: {variant}',altered,flags=re.M)
                        else:
                            if 'config:\n' in altered:
                                altered=altered.replace('config:\n',f'config:\n  layout: {variant}\n',1)
                            elif not altered.startswith('---\n'):
                                altered=f'---\nconfig:\n  layout: {variant}\n---\n'+altered
                            else:
                                raise ValueError('Engine copies require a canonical config mapping in existing front matter')
                    item={'document':str(source),'block':index,'section':section,'variant':variant,
                          'lint':lint(altered,configuration(altered)),'visual':'NOT TESTED'}
                    stem=f'{source.stem}-{index:02}-{variant}'
                    (args.output/f'{stem}.mmd').write_text(altered)
                    warnings.clear()
                    try:
                        parsed=await page.evaluate('async(code)=>{mermaid.initialize({startOnLoad:false});return await mermaid.parse(code)}',altered)
                        item['parse']='PASS'
                        item['parsed_config']=parsed.get('config',{}) if isinstance(parsed,dict) else {}
                        outcome=await page.evaluate('''async(code)=>{
                          document.querySelector('#diagram').innerHTML='';
                          mermaid.initialize({startOnLoad:false});
                          const parsed=await mermaid.parse(code);
                          const {svg}=await mermaid.render('audit_svg',code,document.querySelector('#diagram'));
                          document.querySelector('#diagram').innerHTML=svg;
                          const root=document.querySelector('svg');
                          const v=root.viewBox.baseVal;
                          root.style.maxWidth='none';root.style.width=v.width+'px';root.style.height=v.height+'px';
                          return {svg,parsed,defaults:mermaid.mermaidAPI.defaultConfig};
                        }''',altered)
                        item['parse']='PASS';item['svg']='PASS'
                        (args.output/f'{stem}.svg').write_text(outcome['svg'])
                        defaults=outcome['defaults'] or {}
                        observed=configuration(altered)
                        unknown=[]
                        for key,value in observed.items():
                            if key not in defaults: unknown.append(key)
                            elif key!='themeVariables' and isinstance(value,dict) and isinstance(defaults[key],dict):
                                unknown.extend(key+'.'+k for k in value if k not in defaults[key])
                        item['unknown_config']={'status':'NOT SUPPORTED' if unknown else 'PASS','keys':unknown,
                            'scope':'Compared with this installed build defaultConfig; absence is a warning, not universal rejection'}
                        item['default_layout']=defaults.get('layout')
                        item['configuration_effect']={'status':'NOT TESTED','detail':'Recognized keys require type-specific visual/effective-style checks; retention alone does not prove effect'}
                        for host,color in [('light','#ffffff'),('dark','#0d1117')]:
                            await page.evaluate('(color)=>{document.body.style.backgroundColor=color}',color)
                            inspection=await page.evaluate('window.inspectMermaid',{'css':cfg.get('themeCSS',''),'config':observed,'classDefs':{role:dict(part.strip().split(':',1) for part in body.split(',') if ':' in part) for role,body in re.findall(r'^\s*classDef\s+(\w+)\s+([^\n]+)',altered,re.M)},'assignments':re.findall(r'^\s*class\s+([\w,]+)\s+(\w+)\s*$',altered,re.M)})
                            item[host]=inspection
                            bounds=await page.locator('#diagram svg').bounding_box()
                            if max(bounds['width'],bounds['height'])>16000:
                                item['png']='NOT SUPPORTED';item['png_reason']='natural dimension exceeds 16000px'
                            else:
                                await page.locator('#diagram svg').screenshot(path=str(args.output/f'{stem}-{host}.png'))
                                item['png']='PASS'
                        await page.evaluate("()=>{document.body.style.backgroundColor='transparent'}")
                        if item['png']=='PASS':
                            await page.locator('#diagram svg').screenshot(path=str(args.output/f'{stem}.png'),omit_background=True)
                        item['warnings']=list(warnings)
                    except Exception as exc:
                        item['parse']=item.get('parse','FAIL');item['svg']=item.get('svg','FAIL');item['error']=str(exc)
                    results.append(item)
                    print(source.name,index,variant,item.get('svg'),section[:65],flush=True)
        metadata['loaded_layout_modules']=sorted(loaded_layouts)
        await browser.close()
    data={'environment':metadata,'results':results}
    (args.output/'audit.json').write_text(json.dumps(data,indent=2))
    lines=['# Automated Mermaid audit','',f"Renderer: {metadata['renderer']}; Mermaid {metadata['mermaid_version']}; Chromium {metadata['browser_version']}.",'',
           '| Document | Block | Section | Variant | Parse | SVG | PNG | Source lint | CSS checks | Low contrast samples (light / dark) | Visual |',
           '| --- | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- |']
    for item in results:
        css=item.get('light',{}).get('cssChecks',[])+item.get('light',{}).get('classChecks',[])
        css_status='FAIL' if any(r['status']=='FAIL' for r in css) else ('PASS' if css else 'NOT TESTED')
        low=[sum(r['status']=='FAIL' for r in item.get(host,{}).get('contrast',[])) for host in ['light','dark']]
        lines.append(f"| {Path(item['document']).name} | {item['block']} | {item['section']} | {item.get('variant','original')} | {item.get('parse','NOT TESTED')} | {item.get('svg','NOT TESTED')} | {item.get('png','NOT TESTED')} | {'FAIL' if item.get('lint') else 'PASS'} | {css_status} | {low[0]} / {low[1]} | NOT TESTED |")
    (args.output/'audit.md').write_text('\n'.join(lines)+'\n')
    return int(any(r.get('parse')=='FAIL' or r.get('svg')=='FAIL' or r.get('lint') or any(c['status']=='FAIL' for c in r.get('light',{}).get('cssChecks',[])+r.get('light',{}).get('classChecks',[])) for r in results))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('sources',nargs='+',type=Path)
    parser.add_argument('--output',required=True,type=Path)
    parser.add_argument('--mermaid-dist',type=Path,default=Path('node_modules/mermaid/dist'))
    parser.add_argument('--browser-executable')
    parser.add_argument('--no-sandbox',action='store_true')
    parser.add_argument('--engines',action='store_true',help='Render temporary Dagre/ELK copies without changing orientation')
    args=parser.parse_args()
    for source in args.sources:
        if not source.is_file(): parser.error(f'Source does not exist: {source}')
    raise SystemExit(asyncio.run(run(args)))

if __name__=='__main__': main()
