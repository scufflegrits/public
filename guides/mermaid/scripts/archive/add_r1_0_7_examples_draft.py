"""Archived r1.0.7 construction draft. Later corrections are in the final guides.

The intermediate body below is retained for audit, not invoked automatically.
"""


def original_draft():
    from pathlib import Path

    intro='''## Diagram-type styling and minimal light examples

    The following examples were rendered with the local full Mermaid 12.2.0 build and
    Chromium. They are source-level light cards/regions on simulated white and dark
    hosts, not claims about an untested VS Code extension or GitHub's current build.
    All color-related theme variables use quoted hex. Export with `-b white`, or add
    an actual SVG background rectangle, when the **whole canvas** must be opaque.

    | Type | Configuration and contrast controls | Background and compatibility |
    | --- | --- | --- |
    | Flowchart | `theme: base`, classic shapes, explicit layout; role fill/text and edge color | White-filled wrapper contains nodes and edges; verify label/title clearance in both engines |
    | ER | Native `erDiagram`, entity/attribute palettes, relationship labels/lines, cardinality markers | Native ER group provides a light card in tested 12.2.0; older versions need an opaque export fallback |
    | Sequence | Actor, signal, note and lifeline palette; native `sequence` options | Native white message `rect` plus light actors; outer margins remain transparent; ELK/Dagre do not lay out sequences |

    The [flowchart](https://mermaid.js.org/syntax/flowchart.html),
    [ER](https://mermaid.js.org/syntax/entityRelationshipDiagram.html), and
    [sequence](https://mermaid.js.org/syntax/sequenceDiagram.html) syntax references
    have different grammars and controls. A flowchart class recipe is not a sequence
    actor-styling API. In particular, ER supports its own classes in current versions;
    older renderers may not support the same class/subgraph syntax.

    ### Flowchart: actual white backing shape

    The wrapper is intentionally presentational. Its label is a space, all semantic
    connections stay inside it, and its white fill is real SVG paint. It does not
    represent ownership or network isolation. Direction remains LR.

    '''
    flow_front='''---
    config:
      theme: base
      look: classic
      layout: elk
      # Hex values participate in Mermaid's color calculations.
      themeVariables:
        darkMode: false
        background: "#ffffff"
        primaryTextColor: "#191970"
        lineColor: "#475569"
        edgeLabelBackground: "#ffffff"
    '''
    flow_css='''  themeCSS: |
        .cluster.groupLight rect {
          fill: white !important;
          stroke: none !important;
        }
        .node.nodeService .label-container {
          fill: aliceblue !important;
          stroke: steelblue !important;
        }
        .node.nodeService .nodeLabel,
        .node.nodeService text {
          color: midnightblue !important;
          fill: midnightblue !important;
        }
    '''
    flow_body='''---
    %% A source-only light card; wrapper has no domain meaning.
    flowchart LR
      subgraph SG_LIGHT[" "]
        CLIENT_APP["Client"]
        SERVICE_API["API"]
        CLIENT_APP -->|"Request"| SERVICE_API
      end
    '''
    flow_def='''  classDef nodeService fill:aliceblue,stroke:steelblue,color:midnightblue
      classDef groupLight fill:white,stroke:none
    '''
    flow_assign='''  class CLIENT_APP,SERVICE_API nodeService
      class SG_LIGHT groupLight
    '''
    er_front='''---
    config:
      theme: base
      look: classic
      layout: elk
      # Explicit header, attribute, text, and backing-card palette.
      themeVariables:
        darkMode: false
        background: "#ffffff"
        primaryColor: "#f0f8ff"
        primaryTextColor: "#191970"
        textColor: "#191970"
        lineColor: "#64748b"
        clusterBkg: "#ffffff"
        clusterBorder: "#ffffff"
        attributeBackgroundColorOdd: "#ffffff"
        attributeBackgroundColorEven: "#f1f5f9"
    '''
    er_css='''  themeCSS: |
        .cluster rect {
          fill: white !important;
          stroke: none !important;
        }
        .node .outer-path path[fill]:not([fill="none"]) {
          fill: aliceblue !important;
        }
        .node .outer-path path[fill="none"] {
          stroke: steelblue !important;
        }
        .row-rect-odd path[fill]:not([fill="none"]) {
          fill: white !important;
        }
        .row-rect-even path[fill]:not([fill="none"]) {
          fill: whitesmoke !important;
        }
        .row-rect-odd path[fill="none"],
        .row-rect-even path[fill="none"],
        .divider path {
          stroke: slategray !important;
        }
        .node .nodeLabel,
        .node text {
          color: midnightblue !important;
          fill: midnightblue !important;
        }
        .edgeLabel span,
        .edgeLabel text {
          color: midnightblue !important;
          fill: midnightblue !important;
          background-color: white !important;
        }
        .relationshipLine {
          stroke: slategray !important;
        }
        marker.er path {
          stroke: slategray !important;
          fill: none !important;
        }
        marker.er circle {
          stroke: slategray !important;
          fill: white !important;
        }
    '''
    er_body='''---
    %% ER grouping is native syntax in the tested 12.2.0 build.
    erDiagram
      subgraph SG_LIGHT[" "]
        ACCOUNT ||--o{ REQUEST : submits
        ACCOUNT {
          int account_id PK
          string name
        }
        REQUEST {
          int request_id PK
          int account_id FK
        }
      end
    '''
    er_def='''  classDef nodeEntity fill:aliceblue,stroke:steelblue,color:midnightblue
      class ACCOUNT,REQUEST nodeEntity
    '''
    seq_front='''---
    config:
      theme: base
      # Sequence uses its native renderer, not flowchart layout settings.
      themeVariables:
        darkMode: false
        background: "#ffffff"
        actorBkg: "#f0f8ff"
        actorTextColor: "#191970"
        actorBorder: "#64748b"
        actorLineColor: "#64748b"
        signalColor: "#64748b"
        signalTextColor: "#191970"
        noteBkgColor: "#ffffff"
        noteTextColor: "#191970"
    '''
    seq_css='''  themeCSS: |
        rect.actor {
          fill: aliceblue !important;
          stroke: slategray !important;
        }
        text.actor,
        text.actor tspan {
          fill: midnightblue !important;
        }
        .messageText {
          fill: midnightblue !important;
        }
        .actor-line,
        .messageLine0,
        .messageLine1 {
          stroke: slategray !important;
        }
        .note {
          fill: white !important;
          stroke: slategray !important;
        }
        .noteText {
          fill: midnightblue !important;
        }
    '''
    seq_body='''---
    %% White backing for messages; actors have their own opaque fills.
    sequenceDiagram
      participant CLIENT as Client
      participant API as API
      rect rgb(255,255,255)
        CLIENT->>API: Submit request
        API-->>CLIENT: Accepted
        Note over CLIENT,API: Messages have a white backing
      end
    '''
    er_note='''
    ### ER: headers, compartments, relationships, and markers

    Do not reuse `.node .label-container` or old `.er.entityBox` recipes blindly.
    The 12.2.0 classic ER renderer in this audit uses `.node .outer-path` for entity
    outlines, `.row-rect-odd` / `.row-rect-even` for attributes, `.divider` for cell
    boundaries, `.relationshipLine` for connectors, and `marker.er` for cardinalities.
    The older `.er.entityBox`, `.er.attributeBoxEven`, `.er.relationshipLine`, and
    `.er text` selectors matched nothing in the regression fixture. Accepted config
    keys such as `er.fill`/`er.stroke` also did not establish that the requested
    header/outline colors were actually used; inspect the rendered styles.

    These are **versioned SVG observations**, not permanent Mermaid selector APIs.
    Keep header and attribute fills distinguishable, pair text with each fill, and
    check relationship labels, row dividers, crow's-foot paths, and open cardinality
    circles independently. Theme defaults are useful even when CSS overrides are used.

    '''
    seq_note='''
    ### Sequence: native controls and tested CSS

    The native palette controls actor boxes/text, lifelines, signals, and notes.
    In the audited build, `rect.actor` and `text.actor tspan` are distinct targets;
    using a broad `.actor { fill: ... }` rule can accidentally affect text. The
    [documented sequence classes](https://mermaid.js.org/syntax/sequenceDiagram.html#styling)
    include `.actor-line`, `.messageLine0`, `.messageLine1`, `.messageText`, `.note`, and
    `.noteText`; their matches and computed styles still need checking in the actual
    renderer. Sequence messages and participant order are semantic, so do not change
    them to imitate a flowchart orientation. Native `rect rgb(...)` syntax is a
    sequence-region color, not a `themeVariables` value or a `classDef` declaration.

    '''
    for css in [False,True]:
     p=Path('mermaid-best-practices'+('-CSS' if css else '')+'-r1.0.7.md')
     types=intro+'```mermaid\n'+flow_front+(flow_css if css else '')+flow_body+( '' if css else flow_def)+flow_assign+'```\n'
     types+=er_note+'```mermaid\n'+er_front+(er_css if css else '')+er_body+('' if css else er_def)+'```\n'
     types+=seq_note+'```mermaid\n'+seq_front+(seq_css if css else '')+seq_body+'```\n\n'
     if css:
      types+='The ER/sequence selectors above are independent of the flowchart role selectors.\nNo flowchart `classDef`, inline `style`, or `linkStyle` statements are introduced.\n\n'
     else:
      types+='The flowchart and ER examples retain this edition\'s `classDef`/`class` conventions;\nsequence styling uses its native supported palette and region syntax.\n\n'
     s=p.read_text().replace('## Starter template\n',types+'## Starter template\n',1)
     p.write_text(s)
    print('Added three minimal type examples to each guide')


if __name__ == '__main__':
    raise SystemExit('Historical draft only; use the audited guides and validation helpers.')
