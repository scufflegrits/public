#!/usr/bin/env python3
"""Add a real background rectangle to an exported SVG without rewriting its content."""
import argparse
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from xml.sax.saxutils import quoteattr


def paint(source, color='#ffffff'):
    root = ET.fromstring(source)
    if root.tag.rsplit('}', 1)[-1] != 'svg':
        raise ValueError('Input root must be svg')
    values = [float(v) for v in re.split(r'[\s,]+', root.attrib.get('viewBox', '').strip()) if v]
    if len(values) != 4 or values[2] <= 0 or values[3] <= 0:
        raise ValueError('A positive four-number SVG viewBox is required')
    if not re.fullmatch(r'#[0-9a-fA-F]{3}(?:[0-9a-fA-F]{3})?|white|black', color, re.I):
        raise ValueError('Use white, black, or an opaque 3/6-digit hex color')
    if color.lower() in ('none', 'transparent', 'inherit', 'currentcolor'):
        raise ValueError('Use a concrete opaque color')
    if 'data-mermaid-canvas="opaque"' in source:
        raise ValueError('An opaque canvas marker already exists')
    match = re.search(r'<svg(?:"[^"]*"|\x27[^\x27]*\x27|[^\x27">])*>', source)
    if not match:
        raise ValueError('Unprefixed Mermaid svg root not found')
    x, y, width, height = values
    rect = (f'<rect xmlns="http://www.w3.org/2000/svg" data-mermaid-canvas="opaque" '
            f'x="{x:g}" y="{y:g}" width="{width:g}" height="{height:g}" '
            f'fill={quoteattr(color)} style="fill:{color} !important;stroke:none;"/>')
    return source[:match.end()] + rect + source[match.end():]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path)
    parser.add_argument('--output', required=True, type=Path)
    parser.add_argument('--color', default='#ffffff')
    args = parser.parse_args()
    if args.source.resolve() == args.output.resolve():
        parser.error('Use a separate output file; source is preserved')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(paint(args.source.read_text(), args.color))

if __name__ == '__main__':
    main()
