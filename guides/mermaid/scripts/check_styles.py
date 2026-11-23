import asyncio,json,re,sys
from pathlib import Path
from playwright.async_api import async_playwright

async def main():
    reports=[]
    async with async_playwright() as pw:
        browser=await pw.chromium.launch(args=['--no-sandbox'])
        for name in sys.argv[1:]:
            source=Path(name)
            block=re.findall(r'^```mermaid\n(.*?)^```',source.read_text(),re.M|re.S)[0]
            css=re.search(r'^  themeCSS: \|\n(.*?)^---',block,re.M|re.S).group(1)
            css=re.sub(r'/\*.*?\*/','',css,flags=re.S)
            rules=[]
            for selectors,body in re.findall(r'([^{}]+)\{([^{}]+)\}',css):
                props={}
                for decl in body.split(';'):
                    if ':' in decl:
                        key,value=decl.split(':',1);props[key.strip()]=value.replace('!important','').strip()
                rules.append({'selector':selectors.strip(),'props':props})
            svg=Path('/tmp/css-guide-review')/f'{source.stem}-1.svg'
            page=await browser.new_page(viewport={'width':1800,'height':1800})
            await page.goto(svg.as_uri())
            result=await page.evaluate('''(rules) => {
              const svg=document.querySelector('svg');
              const styleText=[...svg.querySelectorAll('style')].map(e=>e.textContent).join('\n');
              const checks=[];
              for (const rule of rules) {
                const nodes=[...svg.querySelectorAll(rule.selector)];
                const optional=rule.selector.includes('data-id^="layout_"');
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
            }''',rules)
            # Ensure all custom selector text survived after Mermaid scopes/minifies it.
            text=svg.read_text()
            for rule in rules:
                for sel in rule['selector'].split(','):
                    assert re.sub(r'\s+','',sel) in re.sub(r'\s+','',text),sel
            reports.append({'source':str(source),'svg':str(svg),'result':result})
            print(source.name,':',len(rules),'CSS rules; all non-optional selectors matched and all matched appearance properties passed',flush=True)
            await page.close()
        await browser.close()
    Path('/tmp/css-guide-review/computed-styles.json').write_text(json.dumps(reports,indent=2))
asyncio.run(main())
