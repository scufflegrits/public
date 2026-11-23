"""Archived evidence-dependent report draft; the checked-in audit is authoritative."""


def original_draft():
    from pathlib import Path
    import json
    root=Path('/tmp/mermaid-audit-r1.0.7/final')
    data=json.loads((root/'audit.json').read_text())
    hashes=json.loads(Path('/tmp/mermaid-audit-r1.0.7/source-hashes.json').read_text())
    fixture=[r for r in data['results'] if 'DoDAF' in r['document'] and r['variant']=='original']
    rows=[]
    for r in fixture:
     failures=sum(c['status']=='FAIL' for c in r['dark']['cssChecks'])
     low=sum(c['status']=='FAIL' for c in r['dark']['contrast'])
     dims=' × '.join(r['light']['viewBox'].split()[2:])
     note='Transparent root; intended white-root rule does not match'
     if r['block'] in [13,14]: note+='; legacy ER selectors unmatched; dark connectors weak'
     if r['block']==17: note+='; message text nearly invisible on dark host'
     if r['block'] in [1,3]:note+='; wide overview needs natural-width/scroll review'
     if r['block'] in [5,7,9,11]:note+='; selected LR direction preserved'
     rows.append(f"| {r['block']} | {r['section']} | {dims} | {failures} | {low} | {note} |")
    report='''# Mermaid guide audit — r1.0.7

    Date: October 25, 2026.

    ## Executive summary

    Created [the standard r1.0.7 guide](mermaid-best-practices-r1.0.7.md) and
    [the embedded-CSS r1.0.7 guide](mermaid-best-practices-CSS-r1.0.7.md) from their
    respective r1.0.6 baselines. The standard edition retains `classDef`/`class`; the CSS
    edition retains embedded `themeCSS`, semantic assignments, and classic flowchart
    selectors. The baselines and the DoDAF regression document are unchanged.

    The new guidance distinguishes theme-engine color calculations from CSS color
    values, and palette configuration from actual SVG paint. It supplies tested minimal
    light flowchart, ER, and sequence examples; qualifies layout/host claims; and adds
    reusable offline validation and explicit opaque-SVG export helpers.

    **Results:** all 32 source diagrams (eight guide examples and 24 DoDAF diagrams)
    parsed and rendered. Including explicit Dagre/ELK copies, there were **90 successful
    SVG renders and 90 transparent PNG renders**, each with separate light/dark opaque
    host PNGs. Successful rendering is not an all-PASS styling result: the unchanged
    DoDAF fixture still has inactive background rules and stale ER selectors. Its
    OV-6c message text has poor dark-host contrast. These defects were reported, not
    silently corrected in the architecture document.

    All new guide examples passed their required explicit CSS/class property checks
    and source lint; sampled text contrast passed in the tested surfaces. Their native
    palette sequence example has no custom CSS to assert in the standard edition;
    computed contrast and manual PNG review cover it instead. Optional unused helper
    rules remain NOT TESTED when there is no helper, rather than being called PASS.

    **Host limitation:** actual VS Code and GitHub previews were not exercised. Local
    browser light/dark simulations do not certify those hosts. Native ER grouping and
    the current ER selectors require the stated version; older hosts need a separately
    verified recipe or opaque SVG/PNG exports.

    ## Source review and evidence categories

    Both complete r1.0.6 baselines were reviewed. The authoritative requested task was
    `request-update-guide.md`. The available local `DoDAF_Guide_r1.0.8.md` supplied all
    24 regression blocks. The cited historical `../DoDAF/DoDAF_Guide_r1.0.7-mod.md` was
    also read; its DIV-1 and DIV-3 blocks were extracted into a temporary diagnostic,
    without rewriting that source.

    Official sources consulted:

    - [Theme configuration and color calculations](https://mermaid.js.org/config/theming.html).
    - [Configuration](https://mermaid.js.org/config/configuration.html) and
      [configuration schema](https://mermaid.js.org/config/schema-docs/config.html).
    - [Flowchart syntax](https://mermaid.js.org/syntax/flowchart.html),
      [ER syntax/configuration](https://mermaid.js.org/syntax/entityRelationshipDiagram.html),
      and [sequence syntax/styling](https://mermaid.js.org/syntax/sequenceDiagram.html).
    - [Current layout/build guidance](https://mermaid.js.org/intro/syntax-reference.html#selecting-layout-algorithms).
    - [Mermaid 12.2.0 release notes](https://github.com/mermaid-js/mermaid/releases/tag/mermaid%4012.2.0),
      which include an ELK terminal-routing fix and other renderer-specific changes.
    - [GitHub's diagram documentation](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams).

    The guides distinguish official contracts, local versioned findings, actual editor
    observations, authoring conventions, and unverified behavior. No editor-specific
    observation was invented. Inherited lessons remain labeled historical rather than
    being re-certified by the current tests.

    ## Issues discovered and established causes

    | Issue | Evidence / established cause | Revision or disposition |
    | --- | --- | --- |
    | Named colors recommended in theme variables | Official theme docs specify hex for color calculations; YAML validity is a different check | Both guides default to quoted six-digit hex for color-related `themeVariables` |
    | Current implementation more permissive than documentation | Local 12.2.0 rendered both `primaryColor: red` and quoted `#ff0000` as red | Reported as a local/documented discrepancy; did not promote names to a portable theme contract |
    | Unquoted YAML hex | `primaryColor: #ff0000` parsed as null and rendered the default light fill | Explicit quoting rule, lint check, and negative test |
    | CSS syntax confused with Mermaid class grammar | Named colors and short/long hex worked in class definitions; an unescaped `fill:rgb(240,248,255)` failed at function syntax | Document supported tested subset; leave escaped/function variants unverified |
    | Palette background mistaken for canvas paint | Root computed background stayed transparent despite a white theme background | Separate palette, shapes, root CSS, CLI export, alpha, and host surfaces |
    | Plain `svg` CSS assumed to paint the root | Scoped rule became `#audit_svg svg` and matched zero elements | Removed that recipe as a guaranteed fix; document matched-selector and pixel checks |
    | Alternative root selectors assumed to work | `:root` also matched nothing; `&` was rewritten into a nonmatching doubled root selector | Do not recommend these as cross-renderer workarounds |
    | Stale ER CSS selectors | `.er.entityBox`, `.er.attributeBoxEven/Odd`, `.er.relationshipLine`, and `.er text` matched zero elements in 12.2.0 | Added separately tested modern ER selectors and compatibility limits |
    | Recognized ER options treated as proof of effect | Accepted `er.fill`/`er.stroke` did not establish the requested header/outline appearance in the fixture | Require effective-style/visual checks; config acceptance alone is insufficient |
    | Native sequence text exposed to host background | OV-6c root was transparent and message text remained dark; sampled dark-host ratio about 1.06:1 | Added explicit actor/signal/note palettes and a native white message region |
    | Engine/host defaults overgeneralized | Full local build loaded both engines; official docs distinguish full and tiny builds; GitHub docs do not promise ELK | Version/build-qualified recommendations and explicit engine-copy tests |
    | Flowchart rules presented as general diagram grammar | ER has its own current class and grouping support; sequence has native controls | Added per-type guidance and qualified historical flowchart class-syntax claims |
    | Standard starter had five roles without its required swatch legend | Existing legend convention and starter were inconsistent | Added role swatches reusing classes; layout-only links remain invisible |
    | Tiny inherited renderer printed failure but could exit successfully | Source review of the embedded helper | Added missing-block and failure exit handling; parser helper also sets failure exit status |

    The historical DIV-1 had several named theme variables. Those violate the corrected
    contract convention but did not make every node fail in this local release. Its
    root was still transparent. Historical DIV-3 used hex variables but also had a
    transparent canvas. Therefore unsupported named-color guidance cannot by itself
    explain both reported cases. The local evidence supports missing root paint and,
    for the newer ER fixture, stale selectors. The exact original VS Code preview
    remains unverified without that editor/extension version and its webview CSS.

    ## Exact sections revised

    | Section | Standard edition | CSS edition |
    | --- | --- | --- |
    | For AI agents: verify before you deliver | Linked full audit workflow; qualified npm CLI/browser identity; fixed simple renderer/parser exit handling | Same shared changes, retaining wrapper provenance as historical |
    | Configuration / Front matter | Hex-only default for theme color calculations; YAML acceptance and version minimum qualified | Same, separately explaining literal CSS syntax |
    | Layout engine: ELK or dagre | Full/tiny/custom build distinction, retained ELK recommendation, practical Dagre fallback, runtime tests | Synchronized shared guidance |
    | Labels and relationships | Group-level edge does not imply physical bonding or fan-out | Same correction |
    | Styles / palette / class syntax | Retains class-based architecture; scopes color formats and historical flowchart grammar | Keeps CSS/semantic assignments; scopes flowchart recipes separately from ER/sequence |
    | Color formats and background decisions (new) | Decision table, actual backing shapes, alpha, export, and host surfaces | Identical shared rules |
    | Renderer identity and evidence (new) | CLI/library/browser/build/extension distinctions | Identical shared rules |
    | Reusable audit workflow (new) | Parser, render, class/CSS properties, contrast, explicit statuses and limits | Same, including scoped-selector verification |
    | Diagram-type styling and minimal light examples (new) | Native palettes and class-based flowchart/ER styling | Independently tested flowchart, ER, and sequence CSS recipes |
    | Starter template | Preserved network meaning/direction; pinned classic look and added a compact role legend | Retained base/classic/themeCSS and corrected invisible-helper selector |
    | Review / Verify a render | Clarified scope of old inline-edge checks and missing-rule searches | Retained computed-style verification; new shared workflow supplies per-type checks |
    | Revision history / provenance | Concise r1.0.7 entry; older policy explicitly superseded | Current counterpart/baseline links corrected; historical evaluation links retained as history |

    ## Testing environment

    | Component | Observed identity |
    | --- | --- |
    | Primary renderer | `scripts/audit_mermaid.py` with local Mermaid ESM and Python Playwright; **not mmdc** |
    | Mermaid library | Full npm `mermaid` **12.2.0**, local `node_modules/mermaid/dist/mermaid.esm.min.mjs` |
    | ESM entrypoint SHA-256 | `dae3440dd5a4adecf76cfd2951c7a69523df3237f110dd186bebbd55f6038c9d` |
    | Python | `/home/sysadmin/.venv/bin/python`, Python **3.13.5**, PyYAML **6.0.3** |
    | Browser automation | Python Playwright **1.64.0** |
    | Browser | Chromium **156.0.8078.4**, `/home/sysadmin/.cache/ms-playwright/chromium-1248/chrome-linux64/chrome` |
    | Layout evidence | Explicit config and geometry recorded; both Dagre and ELK dynamic modules actually loaded |
    | Local default | `defaultConfig.layout` observed as `elk` in this full build |
    | Official CLI cross-check | `/home/sysadmin/projects/guides/mermaid/node_modules/@mermaid-js/mermaid-cli/src/cli.js`, npm CLI **12.0.0** |
    | CLI runtime | `/home/sysadmin/.nvm/versions/node/v24.22.1/bin/node`, Node **v24.22.1**, Puppeteer **25.16.0**, local Mermaid **12.2.0** |
    | CLI browser | Explicit Puppeteer `executablePath` selecting the same Chromium binary; `-b white` |
    | Older wrapper | `/home/sysadmin/.venv/bin/mmdc` 0.1.3 identified as a Playwright/CDN wrapper; not the primary r1.0.7 renderer |
    | VS Code / relevant extension | **NOT TESTED**; actual preview version/extension ID not established |
    | GitHub renderer | **NOT TESTED**; no assumption of a particular deployed library/build |

    ## Compatibility matrix

    | Environment / technique | Flowchart | ER | Sequence | Status and scope |
    | --- | --- | --- | --- | --- |
    | Local full Mermaid 12.2.0, classic look | Role/classes and CSS tested | Modern selectors, attributes, groups, labels and markers tested | Native palette/region and CSS tested | PASS for new examples in the stated browser |
    | Local explicit ELK and Dagre copies | Both rendered and recorded | Both rendered and recorded | Not a flowchart-layout choice | PASS render; visual fallback sampling, not certification of every route |
    | White source-only content backing | Native wrapper rect | Native ER group in tested version | Native white message region and light actors | PASS local light/dark composites; outer margins can remain transparent |
    | Official npm CLI 12.0.0 + Mermaid 12.2.0 | New minimal CSS example exported | New minimal CSS example exported | New minimal CSS example exported | PASS SVG/PNG export with explicit white canvas |
    | Actual root background rectangle | Applicable to exported SVG | Tested on DIV-3 export | Applicable to exported SVG | PASS tested DIV-3 browser previews; not a source-architecture rewrite |
    | Current GitHub Markdown | Version/build must be identified | Group/class support must be checked | Must be checked | NOT TESTED |
    | Actual VS Code dark/light preview | Record extension/webview styles | Record extension/webview styles | Record extension/webview styles | NOT TESTED |
    | Tiny/custom/older Mermaid builds | ELK may be omitted or need registration | Grouping/selectors can differ | Native grammar/version can differ | NOT TESTED; do not inherit the local PASS |
    | Unescaped RGB function in classDef | Rejected by tested parser | Not separately tested | Not a sequence control | NOT SUPPORTED in the tested flowchart form |

    ## Tests executed

    - Ten deterministic Python tests passed: section extraction excludes YAML comments,
      front matter survives extraction, named/unquoted theme colors are flagged, valid
      hex/boolean settings pass, duplicate IDs/missing classes/invalid references and
      unmatched subgraphs are found, and opaque-SVG content and transparency rejection
      behave as intended.
    - Eight new guide examples parsed/rendered, with required explicit style declarations
      checked against browser-normalized computed values. Standard native class border,
      status, data/management/planned edge and invisible-helper properties were checked;
      CSS edition role, text, group, ER compartment/marker, and sequence rules were checked.
    - All 24 DoDAF source blocks parsed/rendered. There were 23 graph-like diagrams with
      explicit Dagre/ELK copies and one native sequence, producing 70 regression renders.
      The guide examples added 20 renders, for 90 total in the final aggregate.
    - Natural dimensions were retained for screenshots. The DoDAF LR choices in blocks
      5, 7, 9, and 11 were preserved; all graph directions and original block bytes were
      compared against the extracted source. No architecture content was rewritten.
    - Original guide PNGs were visually inspected on the intended palette; the minimal
      light examples were also inspected on white hosts. Both starter Dagre fallbacks
      were inspected. DoDAF contact sheets surveyed all 24 originals; DIV-1/2/3, OV-6c,
      overview and large viewpoint trees received additional original-resolution review.
    - Known failures were retained as failures. Positive named/short-hex class controls
      passed; RGB-function grammar, unsupported-key, unquoted-hex, and scoped root-CSS
      controls demonstrated distinct parser, policy, configuration, and style outcomes.
    - Both cited historical DIV cases were rendered as temporary extracts. The real
      white rectangle export was inspected over a dark host. Its root CSS background
      remained transparent but its full-viewBox backing shape computed to white, while
      the CLI's `-b white` export computed a white root CSS background. These are different
      verified mechanisms.

    ### DoDAF source-block regression ledger

    All rows below have PASS parsing and SVG/PNG rendering. Style failure counts are
    conservative automated screens, not a count of separate architectural defects.
    For example, an unused edge-label rule in a diagram with no labels is inconclusive
    (NOT TESTED in manual interpretation), not evidence of broken labels. The root
    `svg` rule is intended to apply in every fixture block and fails in all 24.

    | Block | Source section | Natural dimensions | Explicit CSS screen failures | Low dark-host text samples | Review note |
    | ---: | --- | --- | ---: | ---: | --- |
    '''+ '\n'.join(rows)+'''

    The DIV-2/3 entity text itself remained readable in the local screenshot, but the
    requested blue/gray CSS palette was not applied and dark relationship strokes were
    weak against the host. OV-6c message text visibly failed on the dark host. DIV-1's
    nodes/label backings remained readable locally despite the absent white canvas;
    this distinction prevents attributing every visible dark margin to a text failure.

    ## Tests not executed and known limitations

    - Actual VS Code dark/light previews, their extension IDs/versions, actual GitHub
      Markdown, other browsers/fonts, and the tiny build were not tested. No NOT TESTED
      result is promoted to PASS.
    - Not every Dagre/ELK variant was manually inspected at reading scale. Automated
      rendering/geometry evidence is not a blanket visual approval of all 90 layouts.
    - Large DoDAF overview trees are wide/tall at natural size. A host's max-width rule
      may compress labels; the audit does not certify readability after arbitrary host
      scaling. Use scrolling or appropriately sized exports before changing direction.
    - The contrast screen uses computed leaf text, HTML backgrounds and covering shape
      geometry. It is not pixel segmentation, a complete contrast audit of every
      connector/cardinality, or accessibility certification. Manual review caught weak
      relationship strokes; those must not be hidden by a clean text-only ratio count.
    - Config-default/schema checks identify unknown keys, but do not prove that every
      recognized option affects every diagram. The report explicitly leaves complete
      configuration-effect testing NOT TESTED. Scoped selector checks likewise do not
      certify an unrelated host stylesheet or arbitrary nested CSS/at-rules.
    - Current ER SVG selectors and native ER groups are version-specific. HTML-label
      disabled mode, other looks, optional newer actor forms, and all legacy ER renderers
      were not separately tested. The guides retain explicit opaque-export fallbacks.
    - Test artifacts are under `/tmp/mermaid-audit-r1.0.7/` and may be removed by system
      cleanup. The scripts, negative/positive fixtures, versions, findings, and ledger
      are preserved in the repository for reproducible reruns.

    ## Outstanding concerns and future revisions

    The unchanged DoDAF r1.0.8 fixture is not an all-PASS appearance baseline. A later,
    separately authorized revision should replace its ineffective root rule with a
    verified backing technique, update ER selectors for its selected renderer, and
    protect sequence message contrast. Its architecture statements and LR choices
    must remain intact during any such change.

    Capture an actual VS Code reproduction with editor/extension versions, `info`
    output where supported, generated SVG, compiled selector matches, effective styles,
    and a screenshot. Repeat in the actual GitHub destination. If a viewer lacks native
    ER groups or rejects custom CSS, publish tested opaque SVG/PNG assets instead of
    claiming the source recipe is universally portable.

    For future library upgrades, rerun both engine copies and the diagnostic fixtures,
    review release notes, update selector contracts, and record the installed dependency
    and browser versions. Preserve the distinction between the two authoring editions.

    ## Saved workflow and evidence

    [Scripts and usage](scripts/README.md) document the offline auditor, browser checks,
    CLI wrapper support, background-rectangle helper, SVG previews, contact sheets,
    fixtures, deterministic tests, and archived construction drafts.

    Temporary detailed evidence:

    - [Final per-block JSON](/tmp/mermaid-audit-r1.0.7/final/audit.json) and
      [automated ledger](/tmp/mermaid-audit-r1.0.7/final/audit.md).
    - [Official CLI manifest](/tmp/mermaid-audit-r1.0.7/cli/render-manifest.json).
    - [Saved diagnostic control results](/tmp/mermaid-audit-r1.0.7/controls-final/audit.json).
    - [Opaque/transparent/CLI background comparison](/tmp/mermaid-audit-r1.0.7/opaque-previews/previews.json).
    - [Historical DIV reproduction](/tmp/mermaid-audit-r1.0.7/historical/audit.json).

    ## Preservation checks

    The following source SHA-256 values were recorded before revision and compared
    again after the new guide examples and regression renders:

    | Preserved source | SHA-256 |
    | --- | --- |
    '''+ '\n'.join(f'| `{name}` | `{digest}` |' for name,digest in hashes.items())+'\n'
    Path('mermaid-guide-audit-r1.0.7.md').write_text(report)
    print('Audit report written:',len(report.splitlines()),'lines')


if __name__ == '__main__':
    raise SystemExit('Archived report draft only; see the final audit and reusable helpers.')
