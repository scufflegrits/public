"""Archived one-off renderer; use scripts/render_mermaid_blocks.py instead."""


def original_trial():
    from pathlib import Path
    import re,subprocess,json,sys
    root=Path('/tmp/css-guide-review')
    (root/'browser.json').write_text(json.dumps({'args':['--no-sandbox']}))
    for source in map(Path,sys.argv[1:]):
        for i,b in enumerate(re.findall(r'^```mermaid\n(.*?)^```',source.read_text(),re.M|re.S),1):
            mmd=root/f'{source.stem}-{i}.mmd';mmd.write_text(b)
            for ext in ['svg','png']:
                cmd=['/home/sysadmin/.venv/bin/mmdc','-i',str(mmd),'-o',str(mmd.with_suffix('.'+ext)),'-b','#0b1120','-p',str(root/'browser.json')]
                if ext=='png':cmd+=['-s','2']
                r=subprocess.run(cmd,capture_output=True,text=True)
                print(mmd.stem,ext,'OK' if r.returncode==0 else r.stdout+r.stderr,flush=True)
                if r.returncode:raise SystemExit(1)


if __name__ == '__main__':
    raise SystemExit('Archived trial only; use scripts/render_mermaid_blocks.py.')
