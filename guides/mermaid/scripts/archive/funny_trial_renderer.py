"""Archived one-off renderer; use scripts/render_mermaid_blocks.py instead."""


def original_trial():
    from pathlib import Path
    import subprocess
    root=Path('/tmp/funny-mermaid-review')
    failed=[]
    for mmd in [root/f'block-{i:02}.mmd' for i in [12]]:
        for ext in ['svg','png']:
            cmd=['/home/sysadmin/.venv/bin/mmdc','-i',str(mmd),'-o',str(mmd.with_suffix('.'+ext)),'-b','midnightblue','-p',str(root/'browser.json')]
            if ext=='png': cmd+=['-s','2']
            r=subprocess.run(cmd,capture_output=True,text=True)
            print(mmd.stem,ext,'OK' if r.returncode==0 else r.stdout+r.stderr,flush=True)
            if r.returncode: failed.append((mmd.stem,ext))
    if failed: raise SystemExit(1)

    import urllib.request
    with urllib.request.urlopen('https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js') as response:
        print('Rendered library version (CDN header):', response.headers.get('x-jsd-version'), flush=True)


if __name__ == '__main__':
    raise SystemExit('Archived trial only; use scripts/render_mermaid_blocks.py.')
