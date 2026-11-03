# Installed tools and package usage

Inventory verified: 2026-10-30, in
`/home/sysadmin/projects/guides/containers`.

This inventory combines the user's installation output with local version,
package, executable, and browser-file checks. Updating this document did not
install or upgrade packages.

## Installed inventory

| Tool/package            | Verified version    | Installation scope                   |
| ----------------------- | ------------------- | ------------------------------------ |
| Node.js                 | 24.22.1             | Existing NVM runtime.                |
| npm / npx               | npm 12.2.1          | Existing Node.js tooling.            |
| markdownlint-cli2       | 0.24.0              | Global npm package under NVM.        |
| markdownlint            | 0.42.0              | Library used by markdownlint-cli2.   |
| @mermaid-js/mermaid-cli | 12.0.0              | Global npm package; command: `mmdc`. |
| playwright              | 1.64.1              | Project npm development dependency.  |
| playwright-core         | 1.64.1              | Dependency of `playwright`.          |
| Tesseract OCR           | 5.5.0               | Debian package `tesseract-ocr`.      |
| Poppler utilities       | 25.03.0             | Debian package `poppler-utils`.      |
| curl                    | 8.14.1              | Existing Debian package.             |
| Python                  | 3.13.5              | Existing Debian package `python3`.   |
| codex-source-extract    | No version assigned | Existing local Python helper.        |

Node/npm, Poppler, curl, Python, and the HTML helper were already available.
The user reported installing the Markdown, Mermaid, Playwright, and OCR tools;
their installed versions have now also been checked locally.

## Installation records and reproduction commands

The exact Tesseract installation command is preserved in the user's console
output. Exact original npm installation commands were not captured here.
The npm commands below reproduce the verified package versions and scopes;
they are not presented as a recovered shell history.

### Markdownlint CLI

Reproduce the installed global package:

```bash
npm install --global markdownlint-cli2@0.24.0
```

It checks Markdown formatting, including headings, lists, spacing, code fences,
and tables. Use it on the reports and progress file before handoff, following
the repository's configuration. It does not establish factual correctness or
whether external links resolve. See the [official CLI documentation][lint-docs].

Example:

```bash
markdownlint-cli2 research-vmware.md research-proxmox.md research-rhel.md \
  research-vm-comparison.md research-progress.md
```

`markdownlint-cli2 --version` prints the installed versions, but this version
also treats `--version` as a file pattern and reports zero linted files. That
output confirms a version, not a successful check of the reports.

### Mermaid CLI

Reproduce the installed global package:

```bash
npm install --global @mermaid-js/mermaid-cli@12.0.0
mmdc --version
```

`mmdc` converts Mermaid definitions into SVG, PNG, or PDF diagrams. Use it to
render the architecture, management, and lifecycle diagrams, identify syntax
errors, and inspect readability, clipping, and layout. Successful rendering
does not verify the technical relationships in a diagram.
See the [official Mermaid CLI documentation][mermaid-docs].

Example, after extracting a Mermaid block to a temporary `.mmd` file:

```bash
mmdc -i /tmp/platform-architecture.mmd -o /tmp/platform-architecture.svg
```

Mermaid CLI uses Puppeteer for browser rendering. Its browser setup is separate
from Playwright's; installing Playwright browsers does not automatically
configure Mermaid CLI. A version check has passed; diagram rendering was not
tested during this inventory update.

### Playwright and Chromium

`package.json` records `playwright` as a development dependency with range
`^1.64.1`; `package-lock.json` and the installed CLI confirm 1.64.1.
Reproduce the current package version:

```bash
npm install --save-dev playwright@1.64.1
```

Previously recommended browser setup command; the exact original invocation
was not captured:

```bash
npx playwright install --with-deps chromium
npx playwright --version
```

The browser installer downloads Chromium and installs required Linux libraries;
the dependency step may require administrator access. See
[browser installation][playwright-browsers]. Chromium, its headless shell, and
FFmpeg cache directories are present under `~/.cache/ms-playwright/`, and the
Chromium executable exists. Browser launch was not tested during this update.

Playwright drives browsers, runs page JavaScript, interacts with pages, and
captures screenshots. Use it for rendered documentation checks and collecting
accessible page content that requires JavaScript. The installed package is
the automation library; `@playwright/test` is a separate test-runner package.
See the [library documentation][playwright-docs].

Example screenshot:

```bash
npx playwright screenshot --browser chromium --full-page \
  https://example.com /tmp/source-page.png
```

### Tesseract OCR

Confirmed installation command from the user's console output:

```bash
sudo apt install tesseract-ocr
```

Installed Debian packages:

| Package           | Installed package version |
| ----------------- | ------------------------- |
| tesseract-ocr     | 5.5.0-1+b1                |
| libtesseract5     | 5.5.0-1+b1                |
| libleptonica6     | 1.84.1-4                  |
| tesseract-ocr-eng | 1:4.1.0-2                 |
| tesseract-ocr-osd | 1:4.1.0-2                 |

Tesseract recognizes text in images. `libtesseract5` provides the recognition
engine; Leptonica provides image processing. The `eng` data supports English
recognition, and `osd` supports orientation/script detection. Both data sets
are installed; other recognition languages were not listed.

Use OCR on scanned source pages or screenshots when ordinary text extraction
does not expose the content. Review OCR against the original image, especially
tables, version numbers, prices, and licensing language.
See [Tesseract command-line usage][tesseract-docs].

```bash
tesseract --version
tesseract --list-langs
tesseract /tmp/source-page.png /tmp/source-page -l eng
```

The last command writes `/tmp/source-page.txt`. For a searchable PDF instead:

```bash
tesseract /tmp/source-page.png /tmp/source-page -l eng pdf
```

For scanned PDF input, first render pages as images using Poppler, then OCR
the images. For example, to process the first page:

```bash
pdftoppm -f 1 -l 1 -r 300 -png -singlefile \
  reference/source.pdf /tmp/source-page
tesseract /tmp/source-page.png /tmp/source-page -l eng
```

## Supporting tools already available

The original installation commands for these system packages were not recorded.
The following is a reproduction command for their Debian package names:

```bash
sudo apt install poppler-utils curl python3
```

### Poppler utilities

- `pdfinfo` checks PDF readability and reports metadata and page count.
- `pdftotext` extracts an existing text layer for source review and search.
- `pdftoppm` renders PDF pages to images for visual inspection or OCR.

Use text extraction first; image-only scans may require the OCR workflow above.
Command syntax and options are available in the installed manual pages:
`man pdfinfo`, `man pdftotext`, and `man pdftoppm`.

```bash
pdfinfo reference/source.pdf
pdftotext -layout reference/source.pdf /tmp/source.txt
```

### curl

Downloads public source documents and retrieves HTTP headers or HTML. Check
downloaded file content as well as HTTP status; an HTML login/error page saved
with a `.pdf` filename is not a valid PDF.

```bash
curl -L --fail --max-time 60 \
  https://example.com/source.pdf -o /tmp/source.pdf
pdfinfo /tmp/source.pdf
```

The URL is illustrative. Use actual source URLs from the research references.
Installing browser/OCR tools does not remove authentication restrictions or
establish missing vendor support/entitlement evidence.

### Python and local HTML extraction helper

Python supports local parsing, file checks, reference inventories, and Markdown
anchor/local-link checks. The existing helper
`/home/sysadmin/.local/bin/codex-source-extract` uses only Python's standard
library; no separate pip package was required. It was created locally during
earlier authorized work, rather than installed through npm or apt.

The helper reads saved HTML from standard input and emits text or links. It
can filter output with `--match` and inspect Debian package-index records using
`--deb-packages`. It does not fetch web pages or execute their JavaScript.

```bash
/home/sysadmin/.local/bin/codex-source-extract < /tmp/source.html
/home/sysadmin/.local/bin/codex-source-extract --links < /tmp/source.html
```

Its earlier creation and approval history remains in `prompt.md`. The original
creation command was not recorded in this package inventory.

## Node tools in noninteractive sessions

The global npm commands are installed under
`/home/sysadmin/.nvm/versions/node/v24.22.1/bin/`. That directory is not on this
agent session's inherited PATH; the tools are installed even when a plain
command lookup cannot find them.

For an individual shell session, expose the existing installation with:

```bash
export PATH="/home/sysadmin/.nvm/versions/node/v24.22.1/bin:$PATH"
```

This changes only that shell's environment. Global npm tools belong to this
NVM runtime; switching Node versions can change their availability. Run local
Playwright commands from the project directory so the installed dependency is
used. Node/npm's original installation commands were not captured here.

## Recommended additions

Recommendations reviewed: 2026-10-30. These are proposed additions, not confirmed
installations. The commands below have not been executed as part of this
documentation update.

Start with OCRmyPDF, MarkItDown, and Trafilatura, using pipx to manage the Python
command-line applications. Evaluate Docling if simpler conversion loses too
much structure in technical manuals.

| Package     | Priority           | Research role                                  |
| ----------- | ------------------ | ---------------------------------------------- |
| pipx        | Install first      | Isolate Python command-line applications.      |
| OCRmyPDF    | Recommended        | Add searchable text to scanned PDFs.           |
| MarkItDown  | Recommended        | Convert PDFs and Office documents to Markdown. |
| Trafilatura | Recommended        | Extract web content and metadata.              |
| ripgrep     | Recommended        | Search extracted text and Markdown using `rg`. |
| sqlite3     | Optional initially | Query a persistent document/search index.      |
| Docling     | Evaluate as needed | Extract complex layouts, tables, and OCR.      |

### Package selection and purpose

- **pipx** installs Python applications in separate environments, avoiding
  dependency conflicts between command-line tools. Use a dedicated Python
  virtual environment instead when writing scripts that import their libraries.
  See the [pipx documentation][pipx-docs].
- **OCRmyPDF** processes whole PDFs and adds an OCR text layer using Tesseract.
  It complements the installed image-level OCR tooling and supports page
  correction. See [installation][ocrmypdf-install] and
  [usage examples][ocrmypdf-docs].
- **MarkItDown** converts PDF, Word, PowerPoint, and Excel content to Markdown
  for review, searching, and indexing. Start with its format-specific extras
  rather than installing every optional integration. See
  [Microsoft's documentation][markitdown-docs].
- **Trafilatura** extracts main page content, links, and metadata while reducing
  navigation clutter. It exports Markdown or structured formats such as JSON.
  See the [command-line documentation][trafilatura-docs].
- **ripgrep** searches local extracted content quickly. `rg` is available in
  this agent environment through bundled tooling; installing Debian's package
  makes it available independently of that tool bundle. See
  [ripgrep documentation][ripgrep-docs].
- **sqlite3** provides a CLI for a persistent document catalog and full-text
  index using FTS5. Python's existing SQLite build already passed an in-memory
  FTS5 availability check, so the CLI is optional. Indexing still requires a
  schema and an ingestion script; installation alone does not index documents.
  See [SQLite FTS5][sqlite-fts5].
- **Docling** provides layout analysis, table extraction, OCR, and Markdown or
  structured JSON export. Evaluate it on representative technical manuals when
  simpler conversion loses structure. Compare the output with the originals
  before choosing a converter for the whole collection. See the
  [project documentation][docling-docs].

### Suggested installation commands

For Debian, install the system tools and isolated Python CLI manager:

```bash
sudo apt install pipx ocrmypdf ripgrep sqlite3
pipx ensurepath
pipx install 'markitdown[pdf,docx,pptx,xlsx]'
pipx install trafilatura
```

Open a new shell afterward if the installed commands are not on PATH. Install
Docling separately if needed:

```bash
pipx install docling
```

Record actual versions and successful commands in the installed inventory
after installation. Distribution packages may differ from the latest upstream
versions; verify the installed command's help before using advanced options.

### Example collection and conversion workflow

Keep original source PDFs intact and store derived files separately. The
filenames and URL below are examples; replace them with actual sources.

```bash
mkdir -p reference/derived

# Convert a PDF with an existing text layer.
markitdown reference/manual.pdf \
  -o reference/derived/manual.md

# Add searchable text to scanned pages, preserving the original.
ocrmypdf --skip-text reference/scanned.pdf \
  reference/derived/scanned-searchable.pdf

markitdown reference/derived/scanned-searchable.pdf \
  -o reference/derived/scanned.md

# Extract a public web page into Markdown with metadata.
trafilatura -u "https://example.com" \
  --markdown --with-metadata > reference/derived/page.md

# Search the collected material.
rg -n -i 'multicast|licensing|failover' reference/derived
```

The conversion, OCR, and extraction examples follow the documented interfaces
for [MarkItDown][markitdown-docs], [OCRmyPDF][ocrmypdf-docs], and
[Trafilatura][trafilatura-docs]. They have not been run on the research sources
during this update.

### Web discovery and indexing

The existing web-search integration supplies URL discovery. Trafilatura
extracts discovered pages; Playwright handles accessible pages requiring
browser execution. For unattended research scripts, use a search-provider API
or search integration for discovery and these local tools for extraction.

For every indexed source, preserve:

- The original PDF or saved web page and its source URL.
- Title/publisher, access date, and original-file checksum.
- Converter/version and the path to derived Markdown, text, or JSON.
- Page references or other locators linking extracted content to the original.

Review converted tables, version numbers, and licensing language against the
source before using them as evidence. Markdown conversion can lose structure
and reliable page boundaries; the original remains the reference for checking
extracted passages. Use `rg` for immediate file searches and add a SQLite FTS5
index when the collection needs persistent cataloging and ranked text search.

## Verification scope and documentation

This update checked tool versions, Debian package versions, Tesseract language
data, Node package records, executable locations, and Playwright browser-file
presence. `packages.md` itself passed a `markdownlint-cli2` check. This update
did not launch browsers, render diagrams, OCR documents, or lint the research
reports. Those checks belong to the research workflow; their results should
be recorded in `research-progress.md`.

Appendix A's shell and JavaScript examples passed syntax checks. Its Node
package-discovery, Python metadata, and in-memory SQLite FTS5 examples were
also executed successfully. No installation commands were run.

Official usage documentation below was accessed on 2026-10-30. The installed
versions above come from local checks and user output, not online version
labels.

- [Markdownlint CLI documentation][lint-docs]: installation and lint usage.
- [Mermaid CLI documentation][mermaid-docs]: diagram rendering and browser setup.
- [Playwright library][playwright-docs]: automation library versus test runner.
- [Playwright browsers][playwright-browsers]: browser/dependency installation.
- [Tesseract usage][tesseract-docs]: image recognition and output formats.
- [pipx][pipx-docs]: isolated installation of Python applications.
- [OCRmyPDF installation][ocrmypdf-install]: Debian package installation.
- [OCRmyPDF cookbook][ocrmypdf-docs]: searchable PDFs and OCR behavior.
- [MarkItDown][markitdown-docs]: conversion, CLI usage, and format extras.
- [Trafilatura][trafilatura-docs]: web extraction, Markdown, and metadata.
- [ripgrep][ripgrep-docs]: local text search and installation.
- [SQLite FTS5][sqlite-fts5]: full-text indexing and search.
- [Docling][docling-docs]: document layout, OCR, and structured exports.

## Appendix A: Agent discovery and use of research tools

Use this appendix when starting or resuming research. The inventory above is a
dated record, not a guarantee that every tool is available in the current
shell, Python environment, Node runtime, or remote workspace. Recommended
packages must not be treated as installed until checked.

### A.1 Discover the current environment

Read applicable repository instructions, this document, and the task's scope.
Start in the project directory. Perform local discovery before deciding that
another installation is needed; discovery does not require network access.

Check commands on the inherited PATH:

```bash
for research_tool in \
  node npm npx markdownlint-cli2 mmdc \
  python3 pipx uv markitdown trafilatura docling ocrmypdf \
  tesseract pdfinfo pdftotext pdftoppm curl rg sqlite3 jq \
  codex-source-extract
do
  if research_tool_path="$(command -v "$research_tool")"; then
    printf '%-22s %s\n' "$research_tool" "$research_tool_path"
  else
    printf '%-22s %s\n' "$research_tool" 'not on PATH'
  fi
done
```

If a command is missing, check relevant known installation locations rather
than searching the entire filesystem:

- Existing NVM runtimes under `~/.nvm/versions/node/`; inspect `.nvmrc` or other
  project runtime declarations when present. This inventory's Node path is a
  starting point, not a requirement to use that exact version forever.
- Project `node_modules/.bin/`, `package.json`, and `package-lock.json`.
- `~/.local/bin/`, the project virtual environment, and any environment
  explicitly identified by the task or existing configuration.
- `pipx list` when pipx is available, or `uv tool list` for existing uv-managed
  tools. Use the application's installed entry point, not an unrelated Python
  interpreter.

Use an absolute executable path or a temporary PATH adjustment for an existing
runtime, as shown above. Do not source arbitrary shell startup files, change
system configuration, or run `pipx ensurepath` merely to discover tools.

### A.2 Check package records and execution environments

On Debian, query package status and versions. Missing packages may make the
command exit nonzero; inspect the individual results instead of abandoning
the remaining checks. A package record must say `installed` to establish an
installed Debian package.

```bash
dpkg-query -W \
  -f='${Package}\t${db:Status-Status}\t${Version}\n' \
  tesseract-ocr tesseract-ocr-eng tesseract-ocr-osd \
  poppler-utils curl python3 pipx ocrmypdf ripgrep sqlite3
```

For Node tools, first select an existing compatible Node runtime and make it
available to child processes. Then inspect global and project packages without
downloading anything:

```bash
node --version
npm --version
npm list --global --depth=0
npm list --depth=0
```

`package.json` describes requested dependencies; the lockfile records resolved
versions. Neither proves that the dependency currently exists on disk. From
the project directory, check the installed Playwright package records:

```javascript
// Run using node, for example: node /tmp/check-node-packages.cjs
const fs = require('node:fs');
const path = require('node:path');

for (const name of ['playwright', 'playwright-core']) {
  try {
    const file = require.resolve(`${name}/package.json`, {
      paths: [process.cwd()],
    });
    const metadata = JSON.parse(fs.readFileSync(file, 'utf8'));
    console.log(`${name}\t${metadata.version}\t${path.dirname(file)}`);
  } catch (error) {
    console.log(`${name}\tunresolved\t${error.code || error.message}`);
  }
}
```

An unresolved package can indicate the wrong project/runtime or an incomplete
installation. Do not use bare `npx` or `npm exec` as a discovery probe: they can
download a missing package. Use an existing local entry point, or invoke its
CLI script with the selected Node executable. For this project's installation:

```bash
node node_modules/playwright/cli.js --version
```

Check Python distribution metadata without requiring pip or importing packages
that might initialize models or other resources:

```bash
python3 - <<'PY'
import sys
from importlib import metadata

print('Interpreter:', sys.executable)
for name in ('markitdown', 'trafilatura', 'docling', 'ocrmypdf'):
    try:
        print(name, metadata.version(name))
    except metadata.PackageNotFoundError:
        print(name, 'not in this Python environment')
PY
```

Repeat using an identified virtual environment's interpreter where relevant.
A missing distribution in system Python does not mean a pipx-installed CLI is
missing. Conversely, metadata alone does not prove all optional dependencies
or system libraries are usable. Check an installed tool's `--help` or version
option before choosing flags; not every CLI implements `--version` identically.

### A.3 Verify the capability needed by the task

Separate discovery from a functional check. Only test capabilities needed for
the task, using small known local inputs and separate temporary outputs. Do
not modify original references or run network, infrastructure, or failover
tests merely to check whether research software works.

- **Playwright:** Check package resolution and browser executable presence,
  then, if browser use is needed, launch the selected browser against a local
  page or `about:blank`. Confirm it closes cleanly. Package installation and a
  browser file on disk do not prove launch succeeds in the current sandbox.
- **Mermaid CLI:** Render a small known Mermaid definition, then the actual
  diagram, into a temporary directory. Inspect the result. Playwright's browser
  cache does not establish Puppeteer's runtime readiness.
- **Tesseract:** Check `tesseract --list-langs`; confirm the language required
  by the source. If OCR is needed, recognize a small known image and review the
  result rather than treating successful process exit as accurate extraction.
- **PDF utilities and converters:** Run `pdfinfo` on a known local PDF. Try
  text or Markdown extraction into a separate file; review headings, reading
  order, tables, and missing content. A blank extraction may mean image-only
  pages rather than a broken parser.
- **Docling:** Check the selected pipeline's dependencies and required model
  assets before conversion. First-use model downloads are additional setup;
  do not trigger them silently while claiming to perform offline discovery.
- **Trafilatura and the HTML helper:** Extract a saved local HTML page first.
  Fetch live pages only within the research task's authorized scope.
- **SQLite:** Check FTS5 in memory if indexing is needed. Python's built-in
  SQLite can support indexing even when the `sqlite3` command is absent.

An in-memory FTS5 check creates no persistent database:

```bash
python3 - <<'PY'
import sqlite3

with sqlite3.connect(':memory:') as connection:
    connection.execute('CREATE VIRTUAL TABLE docs USING fts5(body)')
    connection.execute('INSERT INTO docs(body) VALUES (?)', ('multicast',))
    rows = connection.execute(
        'SELECT body FROM docs WHERE docs MATCH ?', ('multicast',)
    ).fetchall()
    assert rows == [('multicast',)]
    print('SQLite', sqlite3.sqlite_version, 'FTS5 works')
PY
```

If a functional check fails, record the command, error, and affected capability.
Distinguish package absence from PATH problems, missing browser/model/language
assets, incompatible dependencies, and sandbox restrictions. Follow the
session's approval mechanism when required; do not bypass it by disabling
security controls or switching tools solely to evade an approval boundary.

### A.4 Choose available tools and fallbacks

Use the smallest available tool that handles the source correctly. Refer to
the examples earlier in this document for commands.

| Research activity               | Available-tool selection                           |
| ------------------------------- | -------------------------------------------------- |
| Discover public sources         | Use the configured web-search integration.         |
| Retrieve static documents       | Use the browser/source tools or curl.              |
| Extract static HTML             | Trafilatura; otherwise the local helper or Python. |
| Read JavaScript-dependent pages | Playwright when browser launch works.              |
| Inspect PDFs                    | Poppler metadata, text, and page-rendering tools.  |
| Convert text PDFs to Markdown   | MarkItDown; evaluate output quality.               |
| Handle complex layouts/tables   | Docling if its pipeline is usable.                 |
| OCR scanned PDFs                | OCRmyPDF; otherwise Poppler images plus Tesseract. |
| Search extracted files          | ripgrep; otherwise available text-search tools.    |
| Persist a text index            | SQLite FTS5 through Python or the SQLite CLI.      |
| Check report formatting         | markdownlint-cli2 with repository rules.           |
| Check Mermaid diagrams          | mmdc rendering plus visual review.                 |

If no Markdown converter is usable, retain Poppler's plain-text extraction and
page images for research; label the output format accurately. Do not relabel
raw text as structured Markdown or claim an unavailable tool was used. Inspect
complex tables visually if conversion loses important relationships.

Installation, upgrade, browser/model download, or configuration changes require
authorization within the current task. The presence of installation examples
in this document is not an instruction to execute them. Continue independent
research with available tools and describe any specific unmet capability.

### A.5 Record results and preserve progress

For tools actually selected, record the check date, executable path, runtime or
environment, version, capability tested, result, and limitations. Use these
status distinctions:

- **Usable:** The relevant functional check passed in this environment.
- **Present, unverified:** Executable/package found; relevant function untested.
- **Installed, off PATH:** Found in a known environment; use its explicit path.
- **Blocked:** Present, but a dependency or execution restriction prevents use.
- **Not found in checked scope:** State which environments were examined.

Save the inventory and next steps in the task's progress record, such as
`research-progress.md`. In a delegated run, workers report their checks to the
coordinator; only the assigned owner edits shared progress files. Do not
rewrite the confirmed package inventory based on assumptions or an incomplete
PATH lookup. Repeat checks after environment changes or relevant failures,
rather than rediscovering the entire stack for every source.

Preserve original files, source URLs, access dates, checksums, conversion
commands/versions, derived paths, and source locators. Report incomplete or
unverified output honestly and resume from the saved state after interruption.

### A.6 Paste-ready prompt for a research agent

```text
Before starting or resuming the assigned research task, read applicable
AGENTS.md instructions and packages.md in full, including Appendix A.
Use packages.md as a dated tool inventory and usage guide. Its recommended
packages and installation examples are not proof of installation or permission
to install them. Follow the task's scope and execution boundaries.

Discover existing tools using local PATH checks, known NVM/project locations,
Debian package records, and relevant Python/Node environments. Account for
pipx isolation and tools installed outside PATH. Inspect actual installed
packages; do not rely only on manifests or old version records. Avoid probes
that can automatically download packages, browsers, or models.

For tools needed by the task, check versions/help and perform a small local
functional check where appropriate. Distinguish presence from readiness,
including browser launch, OCR language data, converter dependencies/model
assets, and SQLite FTS5 support. Record paths, environments, versions, checks,
results, and limits in the assigned progress record. In delegated work,
respect file ownership and send findings to the coordinator.

Use available tools: search integration for discovery; curl/browser tools for
retrieval; Trafilatura or the HTML helper for static content; Playwright for
pages requiring JavaScript; Poppler for PDF inspection; MarkItDown for Markdown;
Docling for complex layouts when usable; OCRmyPDF or Tesseract for scans;
ripgrep/SQLite for local search; and markdownlint-cli2/mmdc for report checks.

Use documented fallbacks when tools are absent. Request additional setup only
when necessary and not already authorized. Respect sandbox and approval rules.
Preserve source originals and provenance, inspect converted tables and critical
claims, and save work incrementally. Continue the assigned research rather
than stopping after environment discovery. Report exactly which capabilities
were verified, unavailable, or left untested.
```

## r1.0.1 review session inventory — 2026-10-30

Checked in this session; no packages were installed or upgraded.

| Tool                                     | Path / environment                     | Version                                                      | Check                                                                                                 | Status                                                                                                                               |
| ---------------------------------------- | -------------------------------------- | ------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| MarkItDown                               | `~/.local/bin/markitdown` (pipx venv)  | 0.1.9                                                        | Converted reference PDFs to `reference/<name>.pdf.md`; output spot-checked against the PDF text layer | Usable; flattens PDF tables, so verify tables against the PDF                                                                        |
| Trafilatura                              | `~/.local/bin/trafilatura` (pipx venv) | 2.3.1                                                        | Extracted `reference/web/*.html.md`                                                                   | Usable; `--precision` dropped some page sections, so later snapshots used `--recall` and claims were read from the saved HTML        |
| Docling                                  | `~/.local/bin/docling` (pipx venv)     | 2.145.0 (distribution metadata)                              | Not run: first use may download models, which needs approval                                          | Present, unverified                                                                                                                  |
| ripgrep                                  | `/usr/bin/rg`                          | system                                                       | Command lookup                                                                                        | Present                                                                                                                              |
| Poppler `pdftotext`/`pdftoppm`/`pdfinfo` | `/usr/bin`                             | 25.03.0 (baseline record)                                    | Text-layer searches, page render of feature-comparison p3                                             | Usable                                                                                                                               |
| markdownlint-cli2                        | NVM Node 24.22.1 global                | 0.24.0 / markdownlint 0.42.0                                 | Linted r1.0.1 Markdown                                                                                | Usable                                                                                                                               |
| Mermaid CLI                              | NVM Node 24.22.1 global                | 12.0.0                                                       | Rendered 3 diagrams via `/opt/brave.com/brave/brave`                                                  | Usable                                                                                                                               |
| mdformat                                 | `~/.venv/bin/mdformat`                 | 1.0.0 with mdformat_frontmatter 2.2.0 and mdformat-gfm 1.0.0 | Version check; formatted r1.0.1 Markdown                                                              | Usable. `mdformat-frontmatter` 2.2.0 (with ruamel-yaml 0.19.1) installed by the user on 2026-10-30 after the review found it missing |
| Helper `codex-source-extract`            | `~/.local/bin`                         | unversioned                                                  | HTML-to-text for saved snapshots                                                                      | Usable                                                                                                                               |

### User installation on 2026-10-30 (after the review)

- `pip install mdformat-frontmatter` into `~/.venv`: mdformat-frontmatter 2.2.0
  and ruamel-yaml 0.19.1. That cleared the mdformat blocker.
- `pip install docling` into `~/.venv`: a second Docling 2.145.0 alongside the
  existing pipx copy (`~/.local/bin/docling`). It pulled in torch 2.15.0,
  torchvision and the CUDA 13 libraries; `~/.venv` measured 6.4 GB afterward.
  Recommendation given to the user: uninstall the `~/.venv` copy and the
  packages that install added, and keep the isolated pipx copy. Neither copy has
  been run, so no Docling models have been downloaded.

[docling-docs]: https://github.com/docling-project/docling
[lint-docs]: https://github.com/DavidAnson/markdownlint-cli2
[markitdown-docs]: https://github.com/microsoft/markitdown
[mermaid-docs]: https://github.com/mermaid-js/mermaid-cli
[ocrmypdf-docs]: https://ocrmypdf.readthedocs.io/en/latest/cookbook.html
[ocrmypdf-install]: https://ocrmypdf.readthedocs.io/en/latest/installation.html
[pipx-docs]: https://github.com/pypa/pipx
[playwright-browsers]: https://playwright.dev/docs/browsers
[playwright-docs]: https://playwright.dev/docs/library
[ripgrep-docs]: https://github.com/BurntSushi/ripgrep
[sqlite-fts5]: https://www.sqlite.org/fts5.html
[tesseract-docs]: https://tesseract-ocr.github.io/tessdoc/Command-Line-Usage.html
[trafilatura-docs]: https://trafilatura.readthedocs.io/en/latest/usage-cli.html
