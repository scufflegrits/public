# Mermaid documentation

Start with the guide for the task you are doing:

| Document | Purpose |
| -- | -- |
| [Code conventions and starter template](mermaid-best-practices-r1.1.0.md) | Naming, source organization, classes, labels, worked examples, and review standards for new diagrams |
| [Installation and setup](mermaid-install.md) | Node.js, CLI, Puppeteer browser, fonts, verification, linter, and installation troubleshooting |
| [Authoring and export reference](mermaid-reference.md) | Syntax, infrastructure examples, layout, styling, export options, and official reference links |
| [Lessons learned](mermaid-lessons-r1.0.6.md) | Observed renderer limitations, layout experiments, and review evidence |
| [Text diagram tools](diagrams-reference.md) | Graph-Easy and PlantUML examples, plus comparison with Mermaid image output |

Worked diagrams live in [architecture/](architecture/) and [flowchart/](flowchart/).
For a large, multi-section diagram (nested subgraphs with their own directions, an
in-diagram rules row, and a legend built from sample nodes), see the
[2026 MLB playoff bracket](flowchart/mlb-playoff-2026.md). It pins Dagre
rather than ELK, for the reason given in the
[code conventions](mermaid-best-practices-r1.1.0.md#layout-engine-elk-or-dagre).
Each diagram carries its own palette and layout engine in its own YAML front
matter ([configuration](mermaid-best-practices-r1.1.0.md#configuration)); see the
[export reference](mermaid-reference.md#match-a-github-or-vs-code-dark-appearance).
The [Puppeteer configuration](puppeteer-config.json) disables browser sandboxing;
use it only under the conditions described in
[browser troubleshooting](mermaid-install.md#chromium-fails-to-start).

Installation procedures belong in `mermaid-install.md`; other guides link to them.
The former `mermaid-setup.md` has been consolidated there, and the links from
`mermaid-reference-links.md` are included in the authoring reference's Further reading section.
