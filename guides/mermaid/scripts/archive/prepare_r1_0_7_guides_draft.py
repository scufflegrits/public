"""Archived r1.0.7 construction draft. Later corrections are in the final guides.

The intermediate body below is retained for audit, not invoked automatically.
"""


def original_draft():
    from pathlib import Path

    color='''## Color formats and background decisions

    **Official behavior:** Mermaid's [theme documentation](https://mermaid.js.org/config/theming.html#color-and-color-calculation)
    limits its color-calculation contract to hex values. **Convention:** use quoted
    six-digit `"#RRGGBB"` values for color-related `themeVariables`. YAML accepting
    `white` only proves valid YAML; it does not prove Mermaid can derive the intended
    palette. Named inputs may happen to work in a tested release without being a
    portable theming contract. Non-color settings such as `darkMode` remain booleans.

    **CSS convention:** prefer readable named colors in `themeCSS`, or supported
    `classDef` properties in the standard edition. Keep exact hex shades where needed.
    These values are consumed as CSS, unlike theme color calculations. CSS hex values
    are unquoted. For `classDef`, this guide's tested subset is CSS named colors and
    3/6-digit hex; other CSS formats require parser and renderer tests (commas in
    `rgb()`/`hsl()` can conflict with Mermaid's property separators).

    | Context / intention | Choice | Reason / verification |
    | --- | --- | --- |
    | Color-related `themeVariables` | Quoted `"#RRGGBB"` | Official color-calculation contract; YAML validity alone is insufficient |
    | Embedded `themeCSS: |` | Named CSS color; unquoted hex for precision | Normal CSS declarations, semicolons, and this edition's selectors/precedence rules |
    | Standard-edition `classDef` color | Named CSS color or unquoted hex | Keep semantic role/status classes; test other color-function syntax before use |
    | CLI export canvas | `-b white` or `-b '#0b1120'` | CLI explicitly sets the export background; record implementation and inspect output |
    | Source-only light flowchart on dark UI | White-filled wrapper containing all nodes and edges | An actual SVG shape backs the content; outside margin may remain transparent |
    | Light ER card on dark UI | Tested native ER grouping with white group fill | Version-specific; older hosts may lack ER subgraphs or have different selectors |
    | Light sequence on dark UI | Light actors plus a native white `rect` message region | Protect messages and notes; check lifelines and arrows outside the region |
    | Portable opaque SVG asset | Add a viewBox-sized background rectangle | Actual SVG paint survives inline and image embedding; inspect the resulting asset |
    | Transparent SVG / PNG | Explicit transparent export plus light/dark composites | Host background will show through; it is not an opaque light card |

    ### What paints the background

    `themeVariables.background` participates in palette derivation. It does **not**
    guarantee a painted root SVG canvas. SVG shapes (`rect`, node/entity backgrounds)
    paint their own areas; CSS `background-color` paints the element it actually matches.
    The host editor's page background is a separate surface visible through transparent
    parts of an inline SVG or transparent image. An SVG can have an opaque content card
    and transparent outer margins. PNG may also retain alpha: it is opaque only when
    rendered/composited onto an opaque background, not merely because it is PNG.

    **Local finding, Mermaid 12.2.0/classic:** `themeCSS`'s `svg { background-color: white; }`
    is scoped to `#diagram-id svg`, which does not match the root SVG. The rule can be
    present in the SVG while doing nothing. Neither `:root` nor `&` solved root paint
    in the audited build. Do not prescribe these as cross-renderer fixes. Match the
    compiled selector and check the root's computed background, then inspect pixels.

    For CLI images, set `-b white` and inspect SVG plus PNG. For a portable SVG, use
    `scripts/opaque_svg.py input.svg --output output-opaque.svg --color white`: it adds
    a real background rectangle first in paint order without changing diagram source.
    Broad host CSS can still affect an inline SVG; embedding the opaque asset with
    Markdown image syntax isolates it from the page's selectors. This is the fallback
    when a host cannot render the source-only light-card example correctly.

    ### Renderer identity and evidence

    Distinguish **official documentation**, **versioned local observations**, **actual
    editor-extension observations**, **authoring conventions**, and **unverified claims**.
    The tests for r1.0.7 use the locally installed full Mermaid 12.2.0 ESM distribution
    and Python Playwright/Chromium, not the older CDN wrapper. The official npm CLI
    12.0.0 is identified and tested separately. A name such as `mmdc` or its version
    string does not establish which JavaScript library or browser ran.

    Record executable path, CLI implementation/version, Mermaid library version and
    build, requested and observed layout evidence, browser engine/version, and editor
    extension ID/version where tested. The official npm CLI uses Puppeteer; independent
    wrappers may use Playwright (`executablePath` versus `executable_path` in their
    browser config). Never label an offline browser render an npm CLI render.

    No actual GitHub or VS Code preview was run for this audit. Browser dark/light
    host simulations are useful regression checks, not certification of those hosts.
    Use GitHub's documented `info` diagram to identify its Mermaid version. VS Code
    requires the actual preview implementation/extension and its version to be recorded.

    '''
    layout='''### Layout engine: ELK or dagre

    **Recommendation:** request `layout: elk` for hierarchical flowchart architectures
    when the host provides it. Use explicit `layout: dagre` for compatibility or a
    verified local-direction requirement. Preserve the author's LR/TB/TD orientation.
    ELK is a preference, not a guarantee against overlapping labels or escaped groups.

    The current [official layout documentation](https://mermaid.js.org/intro/syntax-reference.html#selecting-layout-algorithms)
    describes ELK as bundled/default in the full build and Dagre as the fallback for
    the tiny build. Older/custom integrations may need a loader registered; do not
    infer availability or defaults from an `mmdc` major version. Sequence diagrams
    use their own renderer, not this flowchart engine choice. ER also supports layout
    selection in the audited release; check its native documentation and version.

    In the locally installed Mermaid 12.2.0 full build, both engines were actually
    loaded and rendered. This does not establish a GitHub/VS Code installation's
    capabilities. GitHub's official diagram documentation does not promise ELK support;
    older community reports are not a current compatibility guarantee.

    Test copies with **both** front-matter settings. Change the copy's own `layout`
    value rather than relying on a CLI config override. Preserve nodes, labels, edges,
    and direction; render both copies and inspect dimensions, containment, title
    clearance, and named-edge geometry. Record warnings/fallbacks. Identical output
    or a requested configuration string alone does not prove that an engine executed.
    The audit runner records loaded Dagre/ELK module evidence and node geometry.

    **Inherited local observations:** older bracket renders ignored local subgraph
    direction under ELK; Dagre's documented flowchart limitation applies when group
    members connect outside their group. Treat these as reasons to test, not universal
    proof that a particular drawing silently switched engines. In the audited ELK
    routes, `flowchart.curve` did not determine the orthogonal route shape. Dagre offers
    `basis`, `linear`, `monotoneX`, and `step` options; inspect their actual bends and
    arrowheads. The inherited `elk.mrtree` cross-group crash was a versioned observation;
    this collection continues to recommend plain `elk`, without certifying other variants.

    '''
    validation='''## Reusable audit workflow

    From this repository's `mermaid/` directory, with Python Playwright, PyYAML,
    Chromium, and a local full Mermaid install available:

    ```bash
    /home/sysadmin/.venv/bin/python -B scripts/audit_mermaid.py \\
      mermaid-best-practices-r1.0.7.md mermaid-best-practices-CSS-r1.0.7.md \\
      DoDAF_Guide_r1.0.8.md \\
      --mermaid-dist node_modules/mermaid/dist \\
      --output /tmp/mermaid-r1.0.7-review --engines --no-sandbox
    ```

    The final browser option is environment-specific; omit it when Chromium's sandbox
    works. The runner reads local assets through intercepted requests and blocks
    external network requests. It extracts every fenced block with front matter,
    records block number and enclosing document section, invokes Mermaid's parser,
    renders SVG and transparent/light/dark PNGs at natural dimensions, and writes
    `audit.json` plus `audit.md`. Its metadata identifies the local library and browser;
    its results separately record CLI/editor checks as untested unless actually run.

    The statuses are **PASS**, **FAIL**, **NOT TESTED**, and **NOT SUPPORTED**. Do not
    collapse an absent preview or an unmatched optional selector into PASS. The scanner
    flags color-format violations, duplicate flowchart declarations, invalid/missing
    class references, and unbalanced subgraphs. These are deterministic conservative
    checks for this collection's syntax, not a general Mermaid grammar. The actual
    Mermaid parser remains authoritative for syntax acceptance.

    CSS checks examine retained rules, the **compiled/scoped** selector matches, and
    computed declarations. Check the root background independently of node fills.
    Unknown configuration keys are compared with this build's defaults and reported
    as unsupported/unverified, not silently accepted. Recognized settings can still be
    ignored by a diagram type or host; inspect requested versus effective appearance.
    The contrast check estimates foreground/background pairs from computed leaf text,
    HTML backgrounds, and covering shapes in both host modes. Its 4.5:1 threshold is
    a conservative text screening convention, not a full accessibility certification.
    Gradients, opacity, nested graphics, and geometry-based background choices require
    manual review. Absence of a flagged sample does not prove the drawing is accessible.

    Open each changed PNG, including full-resolution wide/tall diagrams. Record visual
    review separately: automation leaves it **NOT TESTED**. Do not declare a diagram
    visually correct from parsing, CSS retention, selector counts, or contrast estimates
    alone. Browser host simulations do not reproduce an unknown extension's CSS.

    '''
    for css in [False,True]:
     src=Path('mermaid-best-practices'+('-CSS' if css else '')+'-r1.0.6.md')
     s=src.read_text()
     s=s.replace('**CSS r1.0.6 edition**','**CSS r1.0.7 edition**')
     s=s.replace('[the original r1.0.5 guide](mermaid-best-practices-r1.0.5.md)', '[the standard r1.0.7 guide](mermaid-best-practices-r1.0.7.md)')
     s=s.replace('It is a separate\nalternative: the original file is unchanged.', 'It is a separate\nalternative, revised from the CSS r1.0.6 baseline; both r1.0.6 files are unchanged.')
     s=s.replace('''- **Prefer CSS named colors** when they provide the intended appearance, for
      readability and maintainability. Use hex colors when precise colors are necessary.''','''- **Use quoted hex for color-related `themeVariables`.** Prefer readable CSS named
      colors only in CSS-consuming contexts; see the color/background decision table.''')
     s=s.replace('Named CSS colors such as `white` need no quotes.', 'A named color can be valid YAML while outside the supported theme-color contract.')
     s=s.replace('''  empty value followed by a comment. Named CSS colors such as `white` need no
      quotes. Inside the `themeCSS: |` literal, write normal CSS, such as''','''  empty value followed by a comment. YAML accepting a name does not establish
      theme-engine support. Inside the `themeCSS: |` literal, write normal CSS, such as''')
     s=s.replace('''Use CSS named colors when they provide the intended appearance, for readability
    and maintainability. Retain hex colors where precise colors are necessary, such as
    an exact brand palette or the starter template's custom dark palette. Apply this
    rule to theme variables, class definitions, and export backgrounds.''','''Use quoted hex colors in `themeVariables`; prefer readable CSS named colors in
    `classDef` where they provide the intended appearance. Retain precise hex colors
    for the starter's custom palette. Export backgrounds are an explicit rendering
    choice, separate from palette calculation; see the color/background decision table.''')
     s=s.replace('''custom shape, text, status, edge, and subgraph rules in embedded CSS. Use CSS named
    colors when they provide the intended appearance, for readability and
    maintainability. Retain hex colors where precise colors are necessary. Apply this
    rule to embedded CSS, theme variables, and export backgrounds.''','''custom shape, text, status, edge, and subgraph rules in embedded CSS. Prefer named
    CSS colors there when they provide the intended appearance; retain hex for exact
    shades. Color-related `themeVariables` use quoted hex instead. Choose export
    backgrounds explicitly, separately from theme calculation.''')
     s=s.replace('''  provide the intended appearance; use hex for precise custom colors and quote
      them in YAML.''','''  provide the intended appearance in CSS/class definitions; theme-variable
      colors use quoted hex.''')
     s=s.replace('''Pin `background: white`, use named CSS colors''','''Use `background: "#ffffff"` in theme variables, use named CSS colors''')
     a=s.index('### Layout engine: ELK or dagre\n');b=s.index('## Labels and relationships\n',a)
     s=s[:a]+layout+s[b:]
     s=s.replace('''If a dagre-pinned diagram suddenly renders stacked, it has fallen back to ELK:''','''A changed arrangement alone does not establish a fallback:''')
     s=s.replace('''A subgraph ID used as an edge endpoint draws one bulk connection, meaning "this
    connects to the whole group," such as a switch to a set of hosts on bonded links.''','''A subgraph ID used as an edge endpoint denotes a group-level relationship.
    It does not imply fan-out to every member, bonded physical links, or access policy.''')
     s=s.replace('''in either engine.''','''in the historically tested renderers.''')
     s=s.replace('''**Chromium is what `mmdc` already uses.** `mmdc` launches headless Chrome through
    Puppeteer, so you do not need to drive Chromium yourself.''','''**The official npm CLI drives Chromium through Puppeteer.** Independently packaged
    commands named `mmdc` may use Playwright instead. Identify the implementation before
    choosing browser options.''')
     s=s.replace('''A diagram you have not rendered is unverified, however correct the source looks.''','''A diagram you have not rendered is unverified, however correct the source looks.
    See [renderer identity and evidence](#renderer-identity-and-evidence) and the
    [reusable audit workflow](#reusable-audit-workflow) for the r1.0.7 verification path.''',1)
     # Make the inherited tiny renderer fail honestly rather than merely print failures.
     s=s.replace("blocks = re.findall(r'^```mermaid\\n(.*?)^```', text, re.S | re.M)\nfor i", "blocks = re.findall(r'^```mermaid\\n(.*?)^```', text, re.S | re.M)\nif not blocks:\n    sys.exit('No Mermaid blocks found')\nfailures = 0\nfor i")
     s=s.replace("        print(f'block {i} {ext}: {status}')\n```", "        print(f'block {i} {ext}: {status}')\n        failures += result.returncode != 0\nsys.exit(1 if failures else 0)\n```",1)
     s=s.replace('''for (const f of process.argv.slice(2)) {''','''let failed = false;
    for (const f of process.argv.slice(2)) {''',1)
     s=s.replace("    console.log(f, 'FAILED', e.message.split", "    failed = true;\n    console.log(f, 'FAILED', e.message.split",1)
     s=s.replace("  }\n}\n```\n\nA parse proves", "  }\n}\nprocess.exitCode = failed ? 1 : 0;\n```\n\nA parse proves",1)
     s=s.replace('''Never use the `>` child combinator.''','''Convention: avoid the `>` child combinator in this collection.''')
     s=s.replace('''**Do not use the `>`\nchild combinator**''','''**Convention: avoid the `>`\nchild combinator**''')
     s=s.replace('''  theme: base\n  # ELK keeps nodes inside their subgraphs. It ignores flowchart.curve,''','''  theme: base\n  # Stabilize the selector/shape contract for this tested template.\n  look: classic\n  # ELK keeps nodes inside their subgraphs. It ignores flowchart.curve,''')
     s=s.replace('''## Starter template\n''',color+validation+'## Starter template\n',1)
     # Do not imply the new cross-type recipes have been tested in the historical trial.
     if css:
      s=s.replace('''Other diagram types, looks, and viewer versions
    need their own inspected selectors and render tests.''','''The r1.0.7 diagram-type section adds separately tested ER and sequence examples;
    other looks and viewer versions still need inspected selectors and render tests.''')
     s=s.replace('## Revision history\n', '''## Revision history

    **'''+('CSS ' if css else '')+'''r1.0.7 (Oct. 25, 2026).** Corrected theme-variable color scope, separated
    palette and canvas handling, added type-specific light examples and selector
    contracts, qualified layout/host claims, and added reproducible parser/render,
    computed-style, contrast, and engine checks. See
    [the r1.0.7 audit](mermaid-guide-audit-r1.0.7.md) for actual results and limitations.
    Older entries below record historical policy; r1.0.7 supersedes their broad
    recommendation of named colors inside theme variables.

    ''',1)
     dst=Path('mermaid-best-practices'+('-CSS' if css else '')+'-r1.0.7.md')
     dst.write_text(s)
    print('Created both versioned guides; baselines retained')


if __name__ == '__main__':
    raise SystemExit('Historical draft only; use the audited guides and validation helpers.')
