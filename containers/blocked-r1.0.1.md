# Research blockers and access limitations

Research cutoff and log date: 2026-10-30. Research continues where accessible evidence is available.

| Issue                                                                   | Observed effect                                                                                                                                                            | Recovery / next step                                                                                                                                                               | Status                                                              |
| ----------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| Sandbox network restriction during source downloads                     | Platform agents encountered DNS/download failures in sandboxed curl.                                                                                                       | Retry using required command approval; `curl -L --fail` prefix was approved during this session.                                                                                   | Workaround available; not a task-wide blocker.                      |
| Some Broadcom technical documentation returns HTTP 403 in browser       | Browser view unavailable for some release details.                                                                                                                         | Authorized direct public curl retrieved full VKS release-note HTML successfully; other unresolved URLs retained in report. No authentication/access-control bypass.                | Partial recovery; final remaining limitations in VMware references. |
| Some docs.redhat.com PDF requests return HTTP 503 even after escalation | Initial RHEL10.2 release-note download failed.                                                                                                                             | Authorized retry recovered the PDF; now saved as reference/rhel-10.2-release-notes.pdf. Other transient endpoints continue to be checked and any unresolved URLs remain in report. | RHEL10.2 download resolved; not a task-wide blocker.                |
| Proxmox package index TLS validation                                    | `https://download.proxmox.com/debian/pve/dists/trixie/pve-no-subscription/binary-amd64/Packages.gz` returned curl60, certificate hostname mismatch, even after escalation. | No TLS bypass attempted. Release train9.2 verified; exact newest enterprise patch remains unverified.                                                                              | Evidence limitation; agent recording source.                        |
| Veeam older migration whitepaper URL returns HTML                       | `https://www.veeam.com/whitepapers/veeam-hypervisor-migration-guide-vmware-proxmox-ve_wp.pdf?pdfViewer=` returned landing/redirect HTML rather than PDF.                   | Invalid artifact moved out of reference/. Use current migration/support documentation; retain unresolved PDF URL in Proxmox report.                                                | Not a valid downloadable PDF at this endpoint.                      |

No missing deployment inventory or pricing quote is treated as a blocker to writing conditional research. No platform installation or live testing is authorized.

## Research agent usage limit — 2026-10-30

All three platform agents returned a usage-limit error before final handoffs. Saved drafts and PDFs remain on disk. Coordinator is continuing sequentially from those artifacts, reviewing saved primary evidence and completing unfinished sections/references. No duplicate agents or report writers will be started. VMware report has the largest remaining writing gap; Proxmox/Red Hat substantive sections were saved before the failure. This blocks additional agent work, not the coordinator's remaining research/writing.

## Curl approval interruption — resolved configuration

Repeated approval prompts were caused by agents using `curl -sSL` while the saved rule matched only `curl -L --fail`. User requested permanent approval for curl in all sessions. On2026-10-30 the coordinator appended `prefix_rule(pattern=["curl"], decision="allow")` to `/home/sysadmin/.codex/rules/default.rules` using the required one-time configuration-write escalation. Existing rules were backed up. `codex execpolicy check` returned `allow` for both flag forms. This session's agents retain the already loaded `curl -L --fail` form; future startups load the broader rule. Details and approval text are preserved in prompt.md.

A later curl/Python pipeline still prompted because its Python segment was a separate escalated command. Interrupted and corrected to separate download and sandbox parsing. User authorized that operation class; reusable read-only `/home/sysadmin/.local/bin/codex-source-extract` and exact-path global allow rule were installed/verified with approved config write at17:00:22UTC. No broad Python execution rule. Future sessions may pipe curl to that helper; current agents continue split calls. See prompt.md.

Package-index follow-up: official public HTTP endpoints for VE/PBS/PDM were successfully fetched and parsed by coordinator; public patch observations recorded in Proxmox baseline/P31. Enterprise-channel authenticity/latest patch remains unverified; signed repository metadata was not validated. User authorized gzip/exact-parser pipeline; persistent rules/helper mode saved. Markdownlint/Mermaid binaries located under the Node installation; no longer a PATH-related tool blocker.

Mermaid render check: all three sandboxed mmdc attempts failed because Chromium crashpad socket setup returned `Operation not permitted` (setsockopt). Render input/configuration is prepared in /tmp; retrying the single combined Markdown render with required sandbox escalation. No package missing and no infrastructure configuration change required.

Final resolution: all3 report diagrams rendered to SVG and PNG; visual review
passed. The exact Mermaid CLI rule is saved globally and validates allow.
The initial OVE overview503 resolved on retry; valid historical PDF retained.
All51 PDFs validate. Final corrected live link results are in
research-link-checks.tsv:175 HEAD successes plus2 GET recoveries,39 unresolved.
Unresolved endpoint/entitlement/support questions remain in report references.
No missing tool or agent failure prevents delivery of the saved reports.

## r1.0.1 independent review — 2026-10-30

| Issue                                                | Observed effect                                                                                                                              | Recovery / next step                                                                                                                 | Status                         |
| ---------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------ |
| docs.redhat.com HTML returns HTTP 403 to direct curl | WMCO 10.22.0, OCP 4.22 tested maxima and bare-metal topology pages could not be re-read; Red Hat U11                                         | No bypass attempted. Retry through normal browser access or a downloadable PDF; claims keep baseline qualifications                  | Open evidence gap              |
| `mdformat-frontmatter` missing from `~/.venv`        | Repository CLAUDE.md requires both mdformat plugins and says to stop rather than format without one; mdformat was not run on r1.0.1 Markdown | User to install with `~/.venv/bin/pip install mdformat-frontmatter`, then run mdformat; markdownlint (the project's own lint) passes | Waiting on user                |
| Large-PDF MarkItDown conversion runtime              | The 11,511-page Veeam guide and 9,085-page VCF manual take a long time to convert to `.pdf.md`                                               | Conversion ran in the background without overwriting existing files; the audit reports any PDF still missing an extraction           | Tracked in verification record |

No platform, network or system configuration was changed. No commits or
publication occurred.
