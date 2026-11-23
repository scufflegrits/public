#!/usr/bin/env python3
"""Assemble labeled browser-rendered PNGs into a contact sheet using Chromium."""
import argparse
import asyncio
import base64
import html
from pathlib import Path
from playwright.async_api import async_playwright

async def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('images',nargs='+',type=Path)
    parser.add_argument('--output',required=True,type=Path)
    parser.add_argument('--columns',type=int,default=2)
    parser.add_argument('--cell-width',type=int,default=640)
    parser.add_argument('--cell-height',type=int,default=520)
    parser.add_argument('--no-sandbox',action='store_true')
    args=parser.parse_args()
    if min(args.columns,args.cell_width,args.cell_height)<1:parser.error('dimensions must be positive')
    cells=[]
    for source in args.images:
        data=base64.b64encode(source.read_bytes()).decode()
        cells.append(f'<section><p>{html.escape(source.stem)}</p><img src="data:image/png;base64,{data}"></section>')
    document=f'''<style>body{{margin:0;background:#dce2ea;font:13px sans-serif;display:grid;grid-template-columns:repeat({args.columns},{args.cell_width}px)}}
      section{{width:{args.cell_width}px;height:{args.cell_height}px;box-sizing:border-box;padding:8px}}p{{margin:0;height:24px}}
      img{{width:100%;height:calc(100% - 24px);object-fit:contain;object-position:left top}}</style>'''+''.join(cells)
    async with async_playwright() as pw:
        browser=await pw.chromium.launch(args=['--no-sandbox'] if args.no_sandbox else [])
        page=await browser.new_page(viewport={'width':args.columns*args.cell_width,'height':800})
        await page.set_content(document)
        await page.evaluate('async()=>{await Promise.all([...document.images].map(i=>i.decode()))}')
        args.output.parent.mkdir(parents=True,exist_ok=True)
        await page.screenshot(path=str(args.output),full_page=True)
        await browser.close()

if __name__=='__main__':asyncio.run(main())
