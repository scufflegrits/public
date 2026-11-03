"""Render every fenced Mermaid block in the r1.0.1 reports for review.

Usage: python3 -I -B research-mermaid-render-r1.0.1.py OUTPUT_DIR

Writes NAME-N.mmd, NAME-N.svg and NAME-N.png into OUTPUT_DIR, which must be
outside the report sources. Report files are only read. Uses the existing
Mermaid CLI under the NVM Node runtime and the installed Brave browser,
because Mermaid's bundled headless shell is not installed on this host.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPORTS = [
    'research-vmware-r1.0.1.md',
    'research-proxmox-r1.0.1.md',
    'research-rhel-r1.0.1.md',
    'research-vm-comparison-r1.0.1.md',
]
MMDC = Path('/home/sysadmin/.nvm/versions/node/v24.22.1/bin/mmdc')
BROWSER = '/opt/brave.com/brave/brave'

out = Path(sys.argv[1]).resolve()
if out == ROOT or ROOT in out.parents:
    sys.exit('OUTPUT_DIR must be outside the project directory')
out.mkdir(parents=True, exist_ok=True)
config = out / 'puppeteer.json'
config.write_text(json.dumps({'executablePath': BROWSER, 'args': ['--no-sandbox']}))

failures = 0
for name in REPORTS:
    text = (ROOT / name).read_text()
    blocks = re.findall(r'^```mermaid\n(.*?)^```', text, re.M | re.S)
    print(f'{name}: {len(blocks)} Mermaid block(s)')
    for n, block in enumerate(blocks, 1):
        stem = f'{Path(name).stem}-{n}'
        src = out / f'{stem}.mmd'
        src.write_text(block)
        for ext in ('svg', 'png'):
            cmd = [str(MMDC), '-p', str(config), '-i', str(src),
                   '-o', str(out / f'{stem}.{ext}'), '-b', 'white']
            if ext == 'png':
                cmd += ['-s', '2']
            result = subprocess.run(cmd, capture_output=True, text=True)
            status = 'ok' if result.returncode == 0 else f'FAILED ({result.returncode})'
            print(f'  {stem}.{ext}: {status}')
            if result.returncode:
                failures += 1
                print(result.stderr.strip()[-800:])
sys.exit(1 if failures else 0)
