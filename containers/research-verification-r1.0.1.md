# Container comparison verification r1.0.1

Revision **r1.0.1**. Research cutoff **2026-10-30**; review and check date
**2026-10-30** (link probes ran 2026-10-31 01:03–01:04 UTC). Specification:
`request-container-comparison-r1.0.2.md`. Baseline verification record:
`99_Archive/research-verification.md` (historical, unchanged). These are
document and evidence checks, not platform, multicast, failover, backup or
performance tests.

## Results

| Check                  | Command / tool                                                                                                                        | Target                                                                                      | Result                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Structure, links, PDFs | `python3 -B research-audit-r1.0.1.py` (Python 3.13.5, poppler pdfinfo, `../tools/check_anchors.py`)                                   | four r1.0.1 reports, 51 PDFs, `reference/web/` snapshots                                    | Final run after all extractions finished: **exit 0, no issues**. Headings 13/13/13/14 in required order; cutoff and r1.0.1 revision headers present; table cell counts consistent; all anchors, local links and source-reference definitions resolve; 51 PDFs valid, unique, linked; all web snapshots linked. 51/51 PDFs have a `.pdf.md` extraction (an earlier run, before conversion finished, reported only the 14 missing extractions). Raw output: [research-verification-r1.0.1.json](research-verification-r1.0.1.json) |
| Markdown lint          | markdownlint-cli2 0.24.0 / markdownlint 0.42.0, `--config research-markdownlint-r1.0.1.json` (identical to baseline config)           | four reports, progress, TODO, review log (also verification and packages records: 0 issues) | Exit 0, 0 issues in 7 files. `blocked-r1.0.1.md` has 7 MD013 findings, all in text copied unchanged from the baseline (outside the request's lint scope); its r1.0.1 section is clean. Four line-length and list-numbering findings in new text were fixed by rewrapping; no rule was disabled                                                                                                                                                                                                                                   |
| Mermaid                | `python3 -I -B research-mermaid-render-r1.0.1.py <outside dir>`; Mermaid CLI 12.0.0, Node 24.22.1, Brave `/opt/brave.com/brave/brave` | 3 blocks (VMware, Proxmox, Red Hat; comparison has none)                                    | 3/3 SVG and PNG rendered; PNGs inspected: labels readable, no clipping, edges match the described layers. Previews kept outside the project                                                                                                                                                                                                                                                                                                                                                                                      |
| External links         | curl HEAD `-L --max-time 20`, ranged GET `--max-time 30` on failure, 8 parallel                                                       | 216 unique URLs in the four reports                                                         | 140 HEAD 2xx; 9 GET 2xx; 67 unresolved, of which 54 are docs.redhat.com HTTP 403 to scripted requests (access observation; local PDFs remain valid), 1 Ansible 429, 2 developers.redhat.com 403, HTTPS Proxmox index timeout, and known discovery 404s. Log: [research-link-checks-r1.0.1.tsv](research-link-checks-r1.0.1.tsv)                                                                                                                                                                                                  |
| Baseline preservation  | SHA256 re-hash against [manifest](research-baseline-r1.0.0.manifest.json)                                                             | 13 copied sources, 7 inputs, 51 PDFs                                                        | 71/71 unchanged. Edits confined to r1.0.1 files and new evidence (`reference/*.pdf.md`, `reference/web/`)                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Formatting convention  | `~/.venv/bin/mdformat`                                                                                                                | r1.0.1 Markdown                                                                             | Run after the user installed `mdformat-frontmatter` 2.2.0 (mdformat 1.0.0, mdformat-gfm 1.0.0) on 10 r1.0.1 Markdown files, request revisions excluded. Changes: table padding, list renumbering to `1.`, one code span rejoined (then rewrapped for MD013). Lint rerun: 0 issues                                                                                                                                                                                                                                                |
| Claim evidence         | manual review                                                                                                                         | 33 claim groups                                                                             | 26 verified, 6 partly supported, 1 not verified; see [review](research-review-r1.0.1.md) and [ledger](research-claim-audit-r1.0.1.tsv)                                                                                                                                                                                                                                                                                                                                                                                           |

## PDF text extractions

At the user's request, each PDF gets a MarkItDown 0.1.9 extraction at
`reference/<name>.pdf.md`, generated without overwriting any existing file.
All **51 of 51** exist; none is empty (smallest are ~750-word press releases;
the VCF manual extraction is ~3.37 million words).

Spot-check against facts already verified from the PDFs: the SPD values
(16-core minimum, 0.25 TiB), the OpenShift subscription-guide OADP row
(four "Yes" cells), the Proxmox agreement prices, and the NSX multicast
limitations are all present and readable. **Limitation:** the VCF/VVF feature
comparison extraction drops the column headers (VVF, VCF Edge, VCF) and splits
some rows from their marks (for example, "vSphere Pod Service"). Use the PDF
(rendered page 3) for edition/column questions. The extractions are derived
search aids: MarkItDown flattens tables, so the review
read table-dependent claims from the PDF layout or a rendered page.

## Limits

- Lint, rendering and link checks establish document integrity, not factual
  truth; the claim review is separate.
- An HTTP 403/404/timeout does not invalidate previously read content or valid
  local PDFs. A 2xx response does not show that gated content was read.
- No live platform, multicast, failover, restore or performance test was
  performed, and none is claimed.
- No active writer other than this session touched project files. An unrelated
  user file, `conversation.md`, appeared during the session and was preserved.
