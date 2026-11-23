#!/usr/bin/env python3
"""Extract fenced Mermaid blocks and render SVG/PNG pairs with a chosen CLI."""
import argparse
import json
import re
import shutil
import subprocess
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('sources', nargs='+', type=Path)
    parser.add_argument('--output-dir', required=True, type=Path)
    parser.add_argument('--renderer', default=shutil.which('mmdc'))
    parser.add_argument('--node', type=Path, help='Run the renderer JavaScript entrypoint with this Node executable')
    parser.add_argument('--browser-config', type=Path,
                        help='Config for the chosen CLI: Puppeteer or Playwright, not interchangeable')
    parser.add_argument('--background', default='#0b1120')
    parser.add_argument('--scale', type=int, default=2)
    parser.add_argument('--mermaid-version', default='unknown',
                        help='Library version observed separately; CLI version may be a wrapper version')
    args = parser.parse_args()
    if not args.renderer:
        parser.error('mmdc not on PATH; provide --renderer /path/to/mmdc')
    if args.scale < 1:
        parser.error('--scale must be positive')
    if len({p.stem for p in args.sources}) != len(args.sources):
        parser.error('source filename stems must be distinct within one run')
    args.output_dir.mkdir(parents=True, exist_ok=True)
    renderer = ([str(args.node)] if args.node else []) + [args.renderer]
    version = subprocess.run([*renderer, '--version'], capture_output=True, text=True)
    manifest = {'renderer': args.renderer, 'renderer_version': version.stdout.strip(), 'node': str(args.node) if args.node else None,
                'reported_mermaid_version': args.mermaid_version,
                'background': args.background, 'results': []}
    failures = 0
    for source in args.sources:
        blocks = re.findall(r'^```mermaid\n(.*?)^```', source.read_text(encoding='utf-8'), re.M | re.S)
        if not blocks:
            print(f'{source}: FAILED: no fenced Mermaid blocks')
            failures += 1
            continue
        for index, block in enumerate(blocks, 1):
            mmd = args.output_dir / f'{source.stem}-{index}.mmd'
            mmd.write_text(block, encoding='utf-8')
            for ext in ('svg', 'png'):
                output = mmd.with_suffix('.' + ext)
                cmd = [*renderer, '-i', str(mmd), '-o', str(output), '-b', args.background]
                if args.browser_config:
                    cmd += ['-p', str(args.browser_config)]
                if ext == 'png':
                    cmd += ['-s', str(args.scale)]
                result = subprocess.run(cmd, capture_output=True, text=True)
                output.with_suffix(f'.{ext}.log').write_text(result.stdout + result.stderr, encoding='utf-8')
                ok = result.returncode == 0 and output.exists()
                manifest['results'].append({'source': str(source.resolve()), 'block': index,
                                            'output': str(output.resolve()), 'ok': ok})
                print(f'{mmd.stem} {ext}: {"OK" if ok else "FAILED (see log)"}', flush=True)
                failures += not ok
    (args.output_dir / 'render-manifest.json').write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    return int(bool(failures))


if __name__ == '__main__':
    raise SystemExit(main())
