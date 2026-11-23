"""Historical draft generator, retained for review rather than maintenance.

Its original logic is encapsulated below and never called automatically. The final
Markdown contains later edits; running this draft would not reproduce that final file.
Use the rendering/checking helpers to maintain the current documents instead.
"""


def original_draft():
    from pathlib import Path
    import re
    original=Path('mermaid-best-practices-r1.0.5.md').read_text()
    s=original.replace('# Mermaid code conventions','# Mermaid code conventions — embedded CSS edition',1)
    intro='''
    This is the **CSS r1.0.5 edition**, derived from
    [the original r1.0.5 guide](mermaid-best-practices-r1.0.5.md). It is a separate
    alternative: the original file is unchanged. For new diagrams governed by this
    edition, put all custom appearance rules in embedded `config.themeCSS`; do not
    write `classDef`, inline `style`, or numeric `linkStyle` statements. Keep Mermaid
    `class` statements to attach semantic classes to nodes and subgraphs.

    The selector recipes and starter template below target **flowcharts with
    `look: classic`**, checked with Mermaid **12.2.0** in Chromium. YAML configuration
    requires Mermaid 10.5 or newer, but that minimum does not guarantee these SVG
    selectors or named-edge features. Other diagram types, looks, and viewer versions
    need their own inspected selectors and render tests. Do not copy flowchart selectors
    into a mind map, sequence diagram, or block diagram and assume they match.

    '''
    pos=s.index('## For AI agents:')
    s=s[:pos]+intro+s[pos:]
    s=s.replace('A diagram you have not rendered is unverified, however correct the source looks.', '''A diagram you have not rendered is unverified, however correct the source looks.
    Record both the renderer and the Mermaid library version. A command named `mmdc`
    can be an unrelated Python wrapper: `mmdc --version` alone does not identify the
    Mermaid library. The npm Mermaid CLI uses Puppeteer; a Python wrapper may use
    Playwright and different configuration keys. Check `--help` before passing browser
    configuration. On this workstation the available wrapper is
    `/home/sysadmin/.venv/bin/mmdc` (wrapper 0.1.3), using Playwright and a CDN-loaded
    Mermaid library. Its `-p` file uses `executable_path`, not Puppeteer's
    `executablePath`. Report this implementation accurately.''')
    s=s.replace('1. `classDef` declarations, grouped by node role, status, edge role, and group style.\n1. `class` assignments, grouped to match those definitions.', '''1. `class` assignments for node roles, statuses, and subgraphs at the bottom.

    The CSS definitions are already in the front matter's `themeCSS: |` block. Group
    those rules by node role, status, edge meaning, subgraph, and layout helper. Edge
    rules target stable named-edge attributes directly; they do not need `class`
    assignments.''')
    s=s.replace('''- **Omit statement semicolons.** Mermaid treats them as optional terminators. Do not
      mix styles within a block. Quoting every label (see below) prevents a `;` in label
      text from ending a statement early.''','''- **Omit semicolons on Mermaid statements.** Inside `themeCSS`, use ordinary CSS:
      one property per line, a semicolon after every declaration, and braces on separate
      rule lines. This is an intentional distinction between the two languages.
    - Use YAML's literal block scalar `themeCSS: |`, not its folded scalar. Indent the
      CSS two spaces under `themeCSS`, and each declaration two more spaces.
    - Inside that literal scalar, comments are CSS `/* comments */`, not YAML `#`
      comments or Mermaid `%%` comments. Outside it, front matter uses YAML comments.''')
    s=s.replace('''- **Quote hex colors.** `background: #0b1120` parses as an empty value followed by a
      comment. Named CSS colors such as `white` need no quotes.''','''- **Quote hex values in YAML settings.** `background: #0b1120` parses as an
      empty value followed by a comment. Named CSS colors such as `white` need no
      quotes. Inside the `themeCSS: |` literal, write normal CSS, such as
      `fill: #172b46;` or `fill: lavender;`; CSS hex values there need no quotes.''')
    s=s.replace('without an external `--configFile` or theme JSON file.', 'without an external `--configFile`, theme JSON file, or stylesheet.')
    s=s.replace('  theme: base\n  layout: elk\n  themeVariables:', '  theme: base\n  # Keep the SVG structure consistent with the CSS recipes.\n  look: classic\n  layout: elk\n  themeVariables:',1)
    s=s.replace('assign `class layout_* layoutOnly` (`classDef layoutOnly opacity:0`) if global\n  strokes make them visible.', 'hide them with `.flowchart-link[data-id^="layout_"]` in embedded CSS if global\n  strokes make them visible. Do not assign CSS classes to layout edges.')
    s=s.replace('''classDef layoutOnly opacity:0
    class layout_course_01_03,layout_course_03_05,layout_course_05_07 layoutOnly
    class layout_course_02_04,layout_course_04_06,layout_course_06_08 layoutOnly''','''%% Hide named layout edges with the themeCSS selector shown below; no classDef.
    '''.rstrip())
    needle='''For eight courses in the orientation guide, one chain measured'''
    s=s.replace(needle,'''Put this rule in the diagram's existing `themeCSS: |` block:

    ```css
    .flowchart-link[data-id^="layout_"] {
      opacity: 0 !important;
      visibility: hidden !important;
    }
    ```

    '''+needle)
    s=s.replace('''  classDef groupWrapper fill:white,stroke:none
      class SG_BRACKET groupWrapper''','''  class SG_BRACKET groupWrapper''')
    s=s.replace('''  These links connect groups rather than nodes and are usually left unnamed;
      comment them.''','''  These links connect groups rather than nodes and are usually left unnamed;
      comment them. Keep them invisible and inspect the final SVG.''')
    s=s.replace('''  hides the box while giving its contents a solid background.''','''  hides the box while giving its contents a solid background. Define that class
      with `.cluster.groupWrapper rect { fill: white !important; stroke: none !important; }`
      in embedded CSS.''')
    s=s.replace('''A `groupWrapper` class with `stroke:none` and a fill matching the canvas''','''A `groupWrapper` class with a CSS stroke of `none` and a fill matching the canvas''')
    start=s.index('## Styles\n');stop=s.index('## Starter template\n',start)
    s=s[:start]+'''## Styles

    ### Embed the stylesheet; retain semantic class assignments

    Use **one `themeCSS: |` block per diagram** inside its own YAML `config`. Use
    `theme: base` and `look: classic`. Put palette defaults in `themeVariables`, and
    custom shape, text, status, edge, and subgraph rules in embedded CSS. CSS named
    colors and hex colors are both valid CSS values. A stylesheet never requires a
    separate file in this edition.

    **Do not create `classDef`, inline `style`, `linkStyle`, or inline `:::` statements.**
    Use bottom-of-block `class` statements for node roles, statuses, and subgraph groups.
    A class need not have a `classDef`: Mermaid emits its name into the SVG, where
    embedded CSS can select it. Define every assigned class in the stylesheet. Use one
    assignment per role/status, for example `class BACKUP_SERVER nodeServer` and
    `class BACKUP_SERVER statePending`. A comma-separated list is for element IDs,
    not class names: `class SERVER_01,SERVER_02 nodeServer`.

    Keep classes semantic (`nodeServer`, `statePending`, `groupSite`), not paint-based
    (`greenBox`). Mermaid element IDs remain uppercase; classes retain the naming table's
    camelCase prefixes. Preserve existing diagrams unless asked to convert them.

    ### Selector recipes for classic flowcharts

    These selectors address Mermaid's generated SVG. They are not a universal DOM API.
    Recheck their matches and computed styles when changing Mermaid versions or looks.

    | Purpose | Selector pattern | Properties |
    | --- | --- | --- |
    | Node shape | `.node.nodeServer .label-container` | `fill`, `stroke`, `stroke-width` |
    | Node HTML label | `.node.nodeServer .nodeLabel` | `color` |
    | Node SVG label | `.node.nodeServer text` | `fill` |
    | Status border | `.node.statePending .label-container` | `stroke-dasharray` |
    | Site box | `.cluster.groupSite rect` | `fill`, `stroke`, `stroke-width` |
    | Site title HTML label | `.cluster.groupSite .nodeLabel` | `color` |
    | Site title SVG text | `.cluster.groupSite text` | `fill` |
    | Site title size | `.cluster.groupTitleLarge .cluster-label` | `font-size`, `font-weight` |
    | Named edge path | `.flowchart-link[data-id="edge_server_switch_data"]` | `stroke`, `stroke-width`, `stroke-dasharray` |
    | Named invisible helper | `.flowchart-link[data-id^="layout_"]` | `opacity`, `visibility` |

    Use both HTML-label and SVG-text selectors in role rules so text and fill remain
    paired. The `.label-container` selector covers tested rectangles and cylinder
    outlines without accidentally filling the small empty rectangle inside `.label`.
    For an unfamiliar shape, inspect its SVG and add an explicit selector if needed.
    Do not paint every descendant `path`: that can color icons and unrelated details.

    Use descendant (space) selectors and attribute selectors. **Do not use the `>`
    child combinator** in `themeCSS`; the inherited guide observed configurations being
    dropped with it. Do not confuse that restriction with YAML's scalar syntax: use
    `themeCSS: |`, never `themeCSS: >`.

    ### CSS precedence, role, and status

    Mermaid generates its own scoped CSS and sometimes inline styles. Put `!important`
    on each custom appearance declaration in this edition, and keep semantic selectors
    specific (for example `.node.nodeServer .label-container`, rather than `rect`).
    This is a tested convention, not a guarantee against arbitrary host CSS. Do not
    combine these rules with legacy `classDef` or inline styles; their inline important
    values can win. Inspect computed styles if the expected appearance does not apply.

    A role owns fill, text color, border color, and border width. A status owns the dash
    pattern and still requires visible text such as `PLANNED`. Keep these property sets
    separate so CSS order does not silently change the role palette. Keep the stylesheet
    in role, status, edge, subgraph, then layout order. Do not rely on class-assignment
    order to resolve CSS conflicts.

    CSS declaration semicolons are required by this convention. Mermaid statement
    semicolons remain omitted. Give each property its own line, including `!important`:

    ```css
    .node.statePending .label-container {
      stroke-dasharray: 6 4 !important;
    }
    ```

    ### Named edges and arrowheads

    **Do not rely on `class edge_name edgeData` for embedded CSS.** Mermaid can consume
    an edge class assignment without retaining that class on the SVG path. Name an edge
    in its Mermaid connection and select `.flowchart-link[data-id="edge_name"]` in CSS.
    The path qualifier avoids styling the separate edge-label element, which can share
    that `data-id`. Group several explicit selectors with commas when paths share a style.
    If the target SVG does not retain `data-id`, inspect it and document a tested selector
    for that viewer; do not silently substitute a numeric edge index.

    Edge CSS colors the path, **not automatically the arrowhead marker**. Keep the theme's
    `lineColor` readable so shared arrowheads remain visible. Do not recolor a shared
    marker to fix one edge: it can alter unrelated arrows. Preserve direction and patterns
    in the connection syntax, and inspect arrowheads, labels, and path styles separately.
    Do not claim matching colored markers unless actually verified.

    ### Choosing a palette and legends

    Choose either a dark canvas with light text, or a light card with dark text. Pair
    shape fills and text colors in the same role's CSS. Set the background in front matter
    and pass the same background to the renderer (`-b '#0b1120'` for the starter). The
    background variable alone does not reliably paint the export canvas. A light card
    on a dark page needs white-filled group boxes or a white wrapper to keep its labels
    and connectors readable. A theme change will not redesign explicit CSS colors.

    Do not communicate status or connection meaning only through color. Use labels,
    line patterns, and a prose edge legend. With more than four node-role classes, build
    a `SG_LEGEND` subgraph whose swatches have the same `class` assignments as the real
    nodes. Style that group through embedded CSS as well. This keeps the key and drawing
    synchronized without duplicating color rules.

    ''' +s[stop:]
    start=s.index('## Starter template\n');stop=s.index('## Review before sharing\n',start)
    # Reuse the original topology and role/status assignments, replacing definitions.
    origblock=re.search(r'^```mermaid\n(.*?)^```',original,re.M|re.S).group(1)
    body=origblock[origblock.index('%% Two sites'):]
    body=body[:body.index('  %% 5. Layout helpers:')]
    roles=[('nodeNetwork','darkslateblue','lightskyblue','aliceblue'),('nodeServer','darkslategray','aquamarine','honeydew'),('nodeStorage','indigo','plum','lavender'),('nodeOperator','midnightblue','cyan','lightcyan')]
    css=''
    for role,fill,stroke,text in roles:
        css+=f'''    .node.{role} .label-container {{
          fill: {fill} !important;
          stroke: {stroke} !important;
          stroke-width: 2px !important;
        }}
        .node.{role} .nodeLabel,
        .node.{role} text {{
          color: {text} !important;
          fill: {text} !important;
        }}
    '''
    css+='''    /* Status changes the border pattern, not the server's role colors. */
        .node.statePending .label-container {
          stroke-dasharray: 6 4 !important;
        }
        /* Data paths share a rule; named paths do not need edge classes. */
    '''
    dataedges=['edge_site_a_app_sw_data','edge_site_a_db_sw_data','edge_site_a_sw_fw_data','edge_site_a_fw_carrier_data','edge_site_b_fw_carrier_data','edge_site_b_sw_fw_data']
    css+=',\n'.join(f'    .flowchart-link[data-id="{edge}"]' for edge in dataedges)+' {\n      stroke: lightslategray !important;\n      stroke-width: 2px !important;\n    }\n'
    css+='''    .flowchart-link[data-id="edge_site_a_admin_fw_management"] {
          stroke: cyan !important;
          stroke-width: 2px !important;
          stroke-dasharray: 3 3 !important;
        }
        .flowchart-link[data-id="edge_site_b_backup_sw_planned"] {
          stroke: gold !important;
          stroke-width: 2px !important;
          stroke-dasharray: 6 4 !important;
        }
        .cluster.groupSite rect {
          fill: #111827 !important;
          stroke: lightslategray !important;
          stroke-width: 1px !important;
        }
        .cluster.groupSite .nodeLabel,
        .cluster.groupSite text {
          color: aliceblue !important;
          fill: aliceblue !important;
        }
        .cluster.groupTitleLarge .cluster-label {
          font-size: 20px !important;
        }
        /* Hide named helpers even if a broad edge rule is added later. */
        .flowchart-link[data-id^="layout_"] {
          opacity: 0 !important;
          visibility: hidden !important;
        }
    '''
    front='''---
    config:
      # Base supports explicit theme defaults beneath the CSS overrides.
      theme: base
      # The selector recipes below target classic flowchart shapes.
      look: classic
      # Keep owned nodes within their site boxes where supported.
      layout: elk
      # Supply readable defaults, including neutral arrowhead markers.
      themeVariables:
        darkMode: true
        background: "#0b1120"
        primaryTextColor: "#e6edf7"
        textColor: "#e6edf7"
        lineColor: "#94a3b8"
        edgeLabelBackground: "#111827"
        clusterBkg: "#111827"
        clusterBorder: "#475569"
        titleColor: "#e6edf7"
      # Leave space between nodes, ranks, and the site titles.
      flowchart:
        nodeSpacing: 35
        rankSpacing: 55
        subGraphTitleMargin:
          top: 8
          bottom: 12
      # All custom appearance travels with this diagram as ordinary CSS.
      themeCSS: |
    '''
    assign='''  %% Assign semantic classes; all definitions are in themeCSS above.
      class SITE_A_SW_01,SITE_A_FW_01,SITE_B_FW_01,SITE_B_SW_01,WAN_CARRIER nodeNetwork
      class SITE_A_APP_01,SITE_B_BACKUP_01 nodeServer
      class SITE_A_DB_01 nodeStorage
      class SITE_A_ADMIN_01 nodeOperator
      class SITE_B_BACKUP_01 statePending
      class SG_SITE_A,SG_SITE_B groupSite
      class SG_SITE_A,SG_SITE_B groupTitleLarge
    '''
    starter=front+css+'---\n'+body+assign
    s=s[:start]+'''## Starter template

    This self-contained flowchart shows two sites, data connections, a management
    request, and a planned backup server. It is an illustrative topology, not a claim
    about access policy, actual backup operation, speed, or redundancy. Copy the complete
    fenced block. Its CSS selector contract is `look: classic`, Mermaid 12.2.0; also
    verify the viewer in which the Markdown will be presented.

    ```mermaid
    '''+starter+'''```

    **Legend:** solid double arrows show bidirectional data connectivity. The dotted cyan
    arrow shows management initiation; the dashed gold line shows a planned connection.
    Arrowheads retain the neutral theme color. The backup server's dashed border and
    `PLANNED` label identify its status. Site boxes group ownership, not isolation.

    To adapt this template:

    1. Replace quoted labels and actual relationships before adjusting layout.
    1. Retain stable node and named-edge IDs. On edge renames, update `data-id` selectors
       in `themeCSS` as well as the connection statement.
    1. Add or remove node and group assignments at the bottom. A second status needs its
       own `class` statement and its own CSS rule; do not merge its palette into a role.
    1. Remove the planned label, status assignment, and planned connection pattern
       together when commissioning the backup server.
    1. Render SVG and PNG with matching background `-b '#0b1120'`. Check rule retention,
       selector matches, computed styles, labels, containment, and arrowheads.

    '''+s[stop:]
    s=s.replace('- Check that every class assignment names an existing element and defined class.', '''- Check that every class assignment names an existing node or subgraph and a class
      addressed by `themeCSS`. Check each edge selector against an existing named path.
    - Confirm one embedded `themeCSS: |` block, `theme: base`, and `look: classic` for
      the flowchart selector recipes. No external CSS dependency is needed.
    - Confirm no `classDef`, inline `style`, or `linkStyle` Mermaid statements were added.
    - Verify CSS uses semicolons, one property per line, and `!important` for appearance.
    - Check HTML-label `color` and SVG-text `fill`; checking shape fill alone is insufficient.''')
    s=s.replace("- Confirm the front matter is the block's first line and every hex color in it is quoted.","- Confirm front matter starts the block and hex values in YAML settings are quoted.\n  Hex values inside the CSS literal use normal unquoted CSS syntax.")
    s=s.replace('- Confirm styles and `themeCSS` rules in the rendered SVG rather than by eye; see', '- Confirm CSS rule retention in the SVG and computed browser styles, not only appearance; see')
    start=s.index('### Verify a render\n');stop=s.index('## Appendix: Emoji vocabulary',start)
    s=s[:start]+'''### Verify a render

    A successful render proves accepted syntax, not successful styling. Verify all of:

    1. **Rule retention:** custom selectors and declarations appear in the SVG's style
       element. A dropped YAML scalar can otherwise leave an apparently valid diagram.
    1. **Selector matches:** each required selector matches its intended SVG element.
       An edge path and its label can share `data-id`; keep `.flowchart-link` in the selector.
    1. **Computed appearance:** load the SVG in a browser and inspect `getComputedStyle`.
       This proves the CSS cascade selected the intended values. Inline `style` attributes
       can be empty when embedded CSS works correctly; do not use the old inline-edge-style
       procedure as the CSS edition's success test.
    1. **Visual result:** open the browser-rendered PNG. Check wrapping, contrast, glyphs,
       arrowheads, legends, group containment, and invisible helpers.

    For example, in the browser console with the rendered SVG open:

    ```javascript
    const svg = document.querySelector('svg');
    const edge = svg.querySelector('.flowchart-link[data-id="edge_site_a_admin_fw_management"]');
    if (!edge) throw new Error('Named management path selector matched nothing');
    const edgeStyle = getComputedStyle(edge);
    console.log(edgeStyle.stroke, edgeStyle.strokeWidth, edgeStyle.strokeDasharray);
    const server = svg.querySelector('.node.nodeServer.statePending .label-container');
    if (!server) throw new Error('Pending server shape selector matched nothing');
    console.log(getComputedStyle(server).strokeDasharray);
    const label = svg.querySelector('.node.nodeServer .nodeLabel');
    if (label) console.log(getComputedStyle(label).color);
    ```

    For the starter, expect management stroke `rgb(0, 255, 255)` (cyan), width `2px`,
    and dash array equivalent to `3px, 3px`. Expect the pending server border dash array
    `6px, 4px`. Browser serialization can use commas, spaces, RGB values, or pixel units;
    compare normalized values rather than requiring a literal source spelling.

    Check **each** custom role and status, the site box and title, every named-edge rule,
    and any layout helper. Inspect shared arrowheads separately: path colors do not
    propagate to markers. A stylesheet rule appearing in the SVG does not establish that
    it matched or won the cascade. A successful computed-style test does not replace
    opening the PNG. Report the renderer, Mermaid library version, exact checks run,
    and anything unverified. Re-render after the last change.

    ''' +s[stop:]
    # Keep inherited history clearly separate from claims about the CSS edition.
    s=s.replace('## Revision history\n','''## Revision history

    **CSS r1.0.5 (Oct. 25, 2026).** Separate embedded-CSS edition. Replaced authoring
    instructions and the starter's `classDef` rules with readable `themeCSS: |` rules;
    retained semantic node/subgraph `class` assignments. Added classic-flowchart selector
    recipes, named-edge attribute selectors, CSS precedence, arrowhead limits, and
    computed-style verification. The original guide is unchanged. Validation evidence
    for this edition is recorded in the companion evaluation document.

    ### Inherited source history

    The entries below describe the original guide's development and earlier renders;
    they are provenance, not claims that those versions tested this CSS edition.

    ''',1)
    # Remove remaining current instructions that make edge classes sound like CSS targets.
    s=s.replace('| Edge class            | `edge` followed by the connection meaning in camelCase                      | `edgeData`, `edgeManagement`, `edgeEncrypted`         |','| Edge CSS rule         | Select the named path by `data-id`; describe its meaning in a CSS comment | `.flowchart-link[data-id="edge_server_switch_data"]` |')
    s=s.replace('| Layout class          | Use `layoutOnly` for invisible layout helpers                               | `class layout_course_01_03 layoutOnly`                |','| Layout CSS rule       | Hide paths named with the `layout_` prefix | `.flowchart-link[data-id^="layout_"]` |')
    Path('mermaid-best-practices-CSS-r1.0.5.md').write_text(s)
    print('Created CSS edition:',len(s.splitlines()),'lines')


if __name__ == '__main__':
    raise SystemExit('Archived draft only; no files written. See scripts/README.md.')
