#!/usr/bin/env python3
"""Preview existing SVGs over white/dark hosts with Chromium, preserving HTML labels."""
import argparse
import asyncio
import json
from pathlib import Path
from playwright.async_api import async_playwright


async def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('sources', nargs='+', type=Path)
    parser.add_argument('--output', required=True, type=Path)
    parser.add_argument('--no-sandbox', action='store_true')
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    results = []
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(args=['--no-sandbox'] if args.no_sandbox else [])
        page = await browser.new_page(viewport={'width':1600, 'height':1000})
        await page.route('**/*', lambda route: route.abort())
        for source in args.sources:
            await page.set_content('<body style="margin:0">' + source.read_text() + '</body>')
            info = await page.evaluate('''() => {
              const svg = document.querySelector('svg'), v = svg.viewBox.baseVal;
              svg.style.maxWidth = 'none'; svg.style.width = v.width + 'px'; svg.style.height = v.height + 'px';
              const canvas = svg.querySelector('[data-mermaid-canvas="opaque"]');
              return {background:getComputedStyle(svg).backgroundColor,
                canvas:canvas ? {fill:getComputedStyle(canvas).fill,width:canvas.getAttribute('width'),height:canvas.getAttribute('height')} : null};
            }''')
            for name, color in [('light','white'), ('dark','#0d1117')]:
                await page.evaluate('(c)=>{document.body.style.backgroundColor=c}', color)
                await page.locator('svg').screenshot(path=str(args.output/f'{source.stem}-{name}.png'))
            results.append({'source':str(source.resolve()), **info})
        await browser.close()
    (args.output/'previews.json').write_text(json.dumps(results, indent=2))

if __name__ == '__main__':
    asyncio.run(main())
