#!/usr/bin/env python3
"""Check computed appearance for the guide's flat embedded-CSS rules in Chromium.

This intentionally supports ordinary selector/declaration rules, not @rules, nested
CSS, custom-property expressions, or values containing semicolons. It checks every
Mermaid block. It is not a substitute for PNG inspection or structural source review.
"""
import argparse
import asyncio
import json
import re
from pathlib import Path
from playwright.async_api import async_playwright

async def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('sources', nargs='+', type=Path)
    parser.add_argument('--render-dir', required=True, type=Path)
    parser.add_argument('--report', required=True, type=Path)
    parser.add_argument('--browser-executable', help='Optional installed Chromium executable')
    parser.add_argument('--no-sandbox', action='store_true', help='Only when the environment requires it')
    parser.add_argument('--allow-no-match', action='append', default=[], metavar='SELECTOR',
                        help='Exact selector explicitly allowed to match no elements')
    args=parser.parse_args()
    if len({p.stem for p in args.sources}) != len(args.sources):
        parser.error('source filename stems must be distinct')
    reports=[]
    async with async_playwright() as pw:
        options={}
        if args.no_sandbox: options['args']=['--no-sandbox']
        if args.browser_executable: options['executable_path']=args.browser_executable
        browser=await pw.chromium.launch(**options)
        for source in args.sources:
            blocks=re.findall(r'^```mermaid\n(.*?)^```',source.read_text(),re.M|re.S)
            if not blocks: raise ValueError(f'{source}: no fenced Mermaid blocks')
            for index,block in enumerate(blocks,1):
                match=re.search(r'^  themeCSS: \|\n(.*?)(?=^  [A-Za-z]|^---)',block,re.M|re.S)
                if not match: raise ValueError(f'{source} block {index}: expected literal themeCSS')
                css=match.group(1)
                if '@' in css or css.count('{')!=css.count('}') or '{{' in css:
                    raise ValueError('Only flat CSS rules are supported; inspect complex styles manually')
                css=re.sub(r'/\*.*?\*/','',css,flags=re.S)
                if re.sub(r'[^{}]+\{[^{}]+\}', '', css).strip():
                    raise ValueError('Unparsed or nested CSS remains; only flat rules are supported')
                rules=[]
                for selectors,body in re.findall(r'([^{}]+)\{([^{}]+)\}',css):
                    props={}
                    for decl in body.split(';'):
                        if ':' in decl:
                            key,value=decl.split(':',1);props[key.strip()]=value.replace('!important','').strip()
                    if not props: raise ValueError('CSS rule has no property declarations')
                    rules.append({'selector':selectors.strip(),'props':props})
                if not rules: raise ValueError('No CSS rules found')
                svg=(args.render_dir/f'{source.stem}-{index}.svg').resolve()
                page=await browser.new_page(viewport={'width':1800,'height':1800})
                await page.goto(svg.as_uri())
                result=await page.evaluate(r'''({rules,allowed}) => {
                  const svg=document.querySelector('svg');
                  const styleText=[...svg.querySelectorAll('style')].map(e=>e.textContent).join('\n');
                  const checks=[];
                  for (const rule of rules) {
                    for (const [p,v] of Object.entries(rule.props)) {
                      if (!CSS.supports(p,v)) throw Error('Unsupported CSS declaration: '+p+': '+v);
                    }
                    const nodes=[...svg.querySelectorAll(rule.selector)];
                    const optional=allowed.includes(rule.selector);
                    if (!nodes.length && !optional) throw Error('No matches: '+rule.selector);
                    if (!nodes.length) {checks.push({selector:rule.selector,optional:true,matches:0});continue;}
                    for (const node of nodes) {
                      const actual=getComputedStyle(node);
                      const ref=document.createElementNS('http://www.w3.org/2000/svg','rect');
                      for (const [p,v] of Object.entries(rule.props)) ref.style.setProperty(p,v,'important');
                      svg.appendChild(ref);const expected=getComputedStyle(ref);
                      for (const [p,v] of Object.entries(rule.props)) {
                        if (actual.getPropertyValue(p)!==expected.getPropertyValue(p))
                          throw Error(rule.selector+' '+p+': got '+actual.getPropertyValue(p)+' expected '+expected.getPropertyValue(p));
                      }
                      ref.remove();
                    }
                    checks.push({selector:rule.selector,matches:nodes.length,properties:Object.keys(rule.props)});
                  }
                  const pending=[...svg.querySelectorAll('.node.statePending .label-container')].map(n=>({fill:getComputedStyle(n).fill,dash:getComputedStyle(n).strokeDasharray}));
                  const markers=[...svg.querySelectorAll('marker path')].map(n=>({fill:getComputedStyle(n).fill,stroke:getComputedStyle(n).stroke}));
                  return {checks,pending,markers,ruleTextPresent:styleText.includes('!important'),nodes:svg.querySelectorAll('g.node').length};
                }''',{'rules':rules,'allowed':args.allow_no_match})
                # Ensure all custom selector text survived after Mermaid scopes/minifies it.
                text=svg.read_text()
                for rule in rules:
                    for sel in rule['selector'].split(','):
                        assert re.sub(r'\s+','',sel) in re.sub(r'\s+','',text),sel
                reports.append({'source':str(source.resolve()),'block':index,'svg':str(svg),'result':result})
                print(source.name,'block',index,':',len(rules),'CSS rules; all non-optional selectors matched and all matched appearance properties passed',flush=True)
                await page.close()
        await browser.close()
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(reports,indent=2), encoding='utf-8')
if __name__ == '__main__':
    asyncio.run(main())
