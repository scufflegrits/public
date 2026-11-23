# Mermaid authoring helpers

Run these commands from the repository's `mermaid/` directory. The helpers require Python 3.
Rendering also requires a working Mermaid CLI and its browser. CSS inspection
requires Python's `playwright` package and an installed Chromium browser.

## Render every embedded block

`render_mermaid_blocks.py` extracts fenced Mermaid blocks into numbered `.mmd`
files, renders each to SVG and PNG, and writes logs plus `render-manifest.json`.
It returns a failure status if a render fails or a document has no Mermaid blocks.
The output directory is explicit; Markdown sources are never rewritten.

```bash
/home/sysadmin/.venv/bin/python scripts/render_mermaid_blocks.py \
  mermaid-best-practices-CSS-r1.0.5.md \
  --renderer /home/sysadmin/.venv/bin/mmdc \
  --browser-config scripts/fixtures/playwright-browser.json \
  --output-dir /tmp/css-guide-review \
  --background '#0b1120' \
  --mermaid-version 12.2.0
```

The version argument records an independently observed Mermaid library version;
it does not detect that version. The manifest records the CLI's reported version
separately because a Python wrapper version is not a Mermaid library version.
The trial used wrapper 0.1.3 with Playwright and CDN-reported Mermaid 12.2.0.

For the official npm CLI, select that executable and provide its **Puppeteer**
configuration instead. The supplied JSON is for the trial's Playwright wrapper.
If specifying a browser path, Playwright uses `executable_path` while Puppeteer
uses `executablePath`. The supplied `--no-sandbox` browser option was necessary
for this test environment; omit it where your environment can use the sandbox.

Use `--background midnightblue` for section 12 of `mermaid-engineering-examples.md`; most other examples
use `#0b1120`. One invocation uses one background for all extracted diagrams.
Inspect the PNGs separately: rendering does not establish readable layout.

## Check embedded CSS in a browser

`check_mermaid_css.py` opens the corresponding rendered SVG for **every** block,
checks custom selector retention, verifies selector matches, and compares computed
appearance against browser-normalized expected values. It writes a JSON report
and fails if an expected selector or property does not match. It does not render
missing SVGs or judge layout.

```bash
/home/sysadmin/.venv/bin/python scripts/check_mermaid_css.py \
  mermaid-best-practices-CSS-r1.0.5.md \
  --render-dir /tmp/css-guide-review \
  --report /tmp/css-guide-review/computed-styles.json \
  --allow-no-match 'path[data-id^="layout_"]' \
  --no-sandbox
```

The starter declares an optional invisible-helper rule but has no layout helpers.
The explicit `--allow-no-match` above permits that one selector to match nothing;
other selectors must match. The fixture `fixtures/css-layout-helper.md` actually
contains a named invisible edge and tests that its opacity and visibility are hidden.
Pass it to both helpers in the same way as any other Markdown source.

The CSS checker supports this guide's flat selector/declaration rules and simple
values. It intentionally does not support at-rules, nesting, CSS custom-property
expressions, or values containing semicolons. It expects two-space YAML indentation
and a `themeCSS: |` setting. Use browser developer tools for more complex styles.
SVGs and source blocks must correspond; rerender after changing a diagram.
Source files must have distinct filename stems within one invocation.

## Archived construction scripts

`archive/` retains the one-off guide/example generators and renderers written during
this session. They contain intermediate draft logic, not the final documents.
Their original bodies are encapsulated in uncalled functions; running an archived
file exits without writing anything. Use the reusable tools above for maintenance.

The pre-existing `check_styles.py` and `zta-render-from-terminal.sh` were preserved.
`check_mermaid_css.py` is the reusable checker for this CSS-guide trial.

## Version r1.0.7 technical audit

The reusable `audit_mermaid.py` and `mermaid_audit_browser.js` use the **local full
Mermaid ESM build** with Python Playwright and Chromium. They are an independent
browser renderer, not an invocation of `mmdc`. PyYAML and Playwright are required.
No CDN access is needed; external requests are blocked.

```bash
/home/sysadmin/.venv/bin/python -B scripts/audit_mermaid.py \
  mermaid-best-practices-r1.0.7.md mermaid-best-practices-CSS-r1.0.7.md \
  DoDAF_Guide_r1.0.8.md --mermaid-dist node_modules/mermaid/dist \
  --output /tmp/mermaid-r1.0.7-review --engines --no-sandbox
```

This preserves original blocks and creates separate temporary engine copies. It
writes section-numbered SVGs, transparent/light/dark PNGs, and JSON/Markdown reports.
Parser, renderer, lint, explicit CSS/class properties, selector matches, estimated
text contrast, and unknown configuration are separate checks. Visual inspection
and actual GitHub/VS Code previews remain **NOT TESTED** until performed separately.
Nonzero exit status indicates parser/render/source-lint/explicit-style failures;
contrast warnings and unsupported settings also need review in the report. The
DoDAF fixture currently contains known style failures, so it is not expected to
produce an all-PASS report. Contrast estimates are geometric screens, not pixel
segmentation or an accessibility certification. CSS inspection supports flat rules;
at-rules and complex host styling need separate inspection.

The diagnostic fixtures in `fixtures/audit-r1.0.7/` intentionally include negative
controls: named theme colors outside the documented contract, unquoted YAML hex,
an unsupported configuration key, an unescaped RGB function rejected by Mermaid's
classDef grammar, and root CSS selectors which do not paint the root canvas in
the audited build. Do not use those controls as production examples. The separate
`class-colors.md` is the positive named/short-hex control.

For the official npm CLI with a Node executable outside PATH, the existing renderer
also accepts `--node /path/to/node --renderer node_modules/@mermaid-js/mermaid-cli/src/cli.js`.
Use a Puppeteer config and record CLI version separately from its installed Mermaid
dependency; `--mermaid-version` is recorded evidence, not automatic discovery.

`opaque_svg.py input.svg --output output-opaque.svg --color white` adds a real
viewBox-sized background rectangle while preserving source SVG content. It accepts
white, black, or 3/6-digit hex and refuses source/output identity or transparent
colors. `render_svg_previews.py` previews existing SVGs on light/dark hosts using a
browser so foreignObject labels are retained. `mermaid_contact_sheet.py` assembles
already-rendered PNGs for overview review; open full-size images for small labels.
All browser helpers support `--no-sandbox` for environments which require it.

Run deterministic helper checks with:

```bash
/home/sysadmin/.venv/bin/python -B scripts/test_mermaid_audit.py
```

These tests exercise extraction/section mapping, color-format violations, duplicate
IDs, missing classes, invalid references, unmatched groups, and opaque-SVG content
preservation. They do not establish visual correctness. See the
[r1.0.7 audit](../mermaid-guide-audit-r1.0.7.md) for actual render results and limits.
