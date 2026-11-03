# Container comparison research progress

## Evidence follow-up (2026-11-02)

Using the official web versions of Red Hat and Broadcom documentation, and
Veeam's official web PDF extraction, I revisited three open evidence items:

- Red Hat U11: updated the WMCO release reference to10.22.1 (issued July28,
  2026), kept the detailed platform/build table qualified because it is labeled
  for10.20.0, and confirmed hybrid OVN-Kubernetes as the supported WMCO
  networking mode and dual NIC as unsupported. The OCP4.22 tested scale values
  (2,000 nodes/150,000 pods) and bare-metal OpenShift Virtualization worker/HA
  requirements were also reread. The exact detailed matrix still needs a
  version-matched entitlement check before deployment.
- VMware V13: reread VMSA-2026-0008.1 for CVE-2026-111497. The advisory rates
  SDDC Manager9.1.1.x Critical (CVSS9.8), and9.0.x/9.1.0/5.2.x Important
  (CVSS7.5). Patches remain listed as pending, with version-specific
  workarounds. No remediation was performed.
- Veeam: read its version1.0 VMware-to-Proxmox guide via the official web PDF
  extraction. It describes full recovery/on-the-fly conversion and says that
  cross-hypervisor on-the-fly conversion only works with Proxmox as the source.
  Direct downloads still return HTML, so there is no valid local PDF copy.
- Red Hat cadence: checked the policy note last updated2026-09-28 and the
  release-date table last updated2026-05-21. RHEL errata are event-driven, not
  issued on a fixed monthly schedule; minor releases are planned about every
  six months during Full Support and include cumulative qualified errata.
  RHEL10.2 and9.8 were both listed as GA2026-05-19. This does not verify the
  latest supported patch or entitlement for each optional operator/add-on.

Updated the affected reports and TODO. These are later-dated research
supplements; the frozen report cutoff remains2026-10-30. The baseline source
link-check ledger says67 unresolved URLs (216 total; 140 HEAD 2xx and9 GET
recoveries), while the TODO previously said39. The counts conflict and the bulk
URL recheck remains open; do not treat39 as the verified count. Entitled
Broadcom/Red Hat matrices, signed Proxmox enterprise metadata, selected add-on
patch/lifecycle checks, and procurement/PoC items also remain open.

## Supplemental clarification (2026-11-02)

At the user's request, added plain-language VKS multi-network explanations to
the VMware report and comparison. Clarifies that VCF 9.1/VKS 3.6 node-level
secondary interfaces create a separate path but do not automatically route pod
traffic; pod-level multi-NIC is a separate configuration. Cited the official
June 2, 2026 VMware overview (accessed2026-11-02). The research cutoff and
selected VKS 3.8 comparison stack remain unchanged. The report also states the
primary network is immutable after cluster creation and secondary interfaces
cannot be removed without recreating the cluster. This targeted wording/source
addition has not had the full independent review and document-check workflow
rerun; see the updated report references for the source.

Also added a Proxmox networking clarification: VM-level multiple NICs are
documented, while the selected Kubernetes/Multus/CNI end-to-end path remains
unverified. Described Multus in plain terms and recorded its Apache-2.0 license
and upstream source in both the Proxmox report and comparison. Research cutoff
and selected stack remain unchanged; this is also a targeted addition without a
full review/check rerun.

## r1.0.1 independent review (current)

Revision **r1.0.1**; baseline unversioned bundle = r1.0.0 (bookkeeping only).
Research cutoff **2026-10-30** (unchanged); review date **2026-10-30**. Mode:
historical verification at the original cutoff. Governing inputs: request
r1.0.2 and [review handoff r1.0.0](review-handoff-r1.0.0.md).

### Owners and agents

Single coordinator (Claude Code session). No subagents. `ListAgents` showed only
two unrelated peer sessions started seven days earlier; no writer owns these
files. Historical Codex platform agents (`/root/vmware`, `/root/proxmox`,
`/root/rhel`) are not running.

### Files saved

- [Baseline manifest](research-baseline-r1.0.0.manifest.json): sizes, SHA256s,
  source-to-copy mapping for 13 copies (all verified byte-identical before
  editing), unchanged inputs and 51 reference PDFs.
- Revised reports: [VMware](research-vmware-r1.0.1.md),
  [Proxmox](research-proxmox-r1.0.1.md), [Red Hat](research-rhel-r1.0.1.md),
  [comparison](research-vm-comparison-r1.0.1.md).
- [Review log](research-review-r1.0.1.md) and
  [claim ledger](research-claim-audit-r1.0.1.tsv) (33 rows).
- Versioned [TODO](TODO-r1.0.1.md), [blocked log](blocked-r1.0.1.md),
  [packages record](packages-r1.0.1.md),
  [verification summary](research-verification-r1.0.1.md),
  `research-verification-r1.0.1.json`, `research-link-checks-r1.0.1.tsv`,
  `research-audit-r1.0.1.py`, `research-markdownlint-r1.0.1.json`.
- New evidence: `reference/<name>.pdf.md` MarkItDown extractions beside each
  PDF (requested by the user); `reference/web/` 2026-10-30 HTML/text
  snapshots, each with a Trafilatura `.html.md` extraction.

### Review status

- All four reports read in full. Platform reports corrected first; comparison
  revised afterwards.
- Ledger: 26 verified, 6 partly supported, 1 not verified, 0 contradicted.
  Major corrections: OVE includes OADP per R1 p29; OpenShift product types
  cannot be mixed per cluster; VMware SRM/Live Recovery Cloud are add-ons for
  VVF and VCF; NSX routed multicast is IPv4-only; Proxmox OCI preview
  relabelled conditional; Proxmox package-freshness wording made consistent.
- Evidence gaps: docs.redhat.com HTML returned 403 to curl (WMCO, tested
  maxima, bare-metal topology); SDDC Manager advisory not re-read; signed
  Proxmox enterprise package set; quotes/SKUs for every vendor.

### Checks so far

- Audit (`research-audit-r1.0.1.py`): templates, revision headers, tables,
  anchors, local links and 51 PDFs pass; remaining issues are only PDFs whose
  `.pdf.md` extraction was still being generated.

- markdownlint-cli2 0.24.0: 0 issues in 7 r1.0.1 Markdown files.

- Mermaid CLI 12.0.0 via Brave: 3/3 diagrams rendered and visually inspected.

- Baseline: 71 manifest-listed files re-hashed, none changed.

- mdformat not run: `mdformat-frontmatter` missing (see blocked log).

- An unrelated user file `conversation.md` (13,909 bytes, created 19:58 during
  this session) appeared in the directory; it was preserved and not edited.

- External links: 216 probed; 140 HEAD 2xx, 9 GET 2xx, 67 unresolved (54
  docs.redhat.com 403 to scripted requests). Results in
  `research-link-checks-r1.0.1.tsv`; reports note the rerun.

- Verification summary and raw audit JSON written for r1.0.1.

### Status

Evidence review and corrections are complete for the claim groups in the
ledger; one claim group (RH-NV-01) is not verified because of 403 responses.
The revision is **reviewed, with document checks rerun**. It is not certified
for procurement or deployment (see the review's readiness table).

### Baseline archived

On the user's instruction, the 13 baseline files that have r1.0.1 copies were
moved, unchanged, into `99_Archive/` (gitignored): the four reports,
`research-progress.md`, `TODO.md`, `research-verification.md/.json`,
`research-link-checks.tsv`, `research-audit.py`, `research-markdownlint.json`,
`blocked.md` and `packages.md`. Their SHA256s still match
`research-baseline-r1.0.0.manifest.json`. That manifest records their original
top-level paths. Request revisions, `prompt.md`, the review handoff and
`reference/` stay in place. The historical sections of this file mention the
old top-level names as they were at the time.

### Next actions

1. Done: all 51 `.pdf.md` extractions exist; the final audit run exits 0 with
   no issues; the verification JSON/summary are updated. The feature-comparison
   extraction loses its column headers (use the PDF for edition questions).
1. Done: the user installed `mdformat-frontmatter`; `~/.venv/bin/mdformat` was
   run on the r1.0.1 Markdown (request revisions excluded), then re-linted.
1. Open evidence items in [TODO-r1.0.1.md](TODO-r1.0.1.md).

## r1.0.0 progress record (historical, preserved from the baseline)

Request: `request-container-comparison-r1.0.2.md`, read in full.
Research cutoff: **2026-10-30**. Started and finalized on the same date.
No later-date resumption or cutoff refresh occurred.

## Current state

All four research deliverables are written and reviewed. They are complete as
conditional desk-research reports, with explicitly unverified evidence and
procurement items below. They are not deployment certifications. No platform
installation, purchases, network changes, live failover/multicast tests,
commits or publication were performed.

- `research-vmware.md`: all13 required sections written and reviewed.
- `research-proxmox.md`: all13 required sections written and reviewed.
- `research-rhel.md`: all13 required sections written and reviewed.
- `research-vm-comparison.md`: all14 required sections synthesized after the
  three standalone reports were completed/reviewed.
- `reference/`:51 relevant public PDFs retained, with original/local links.
- `research-link-checks.tsv`:216 unique external URLs and probe results.
- `research-verification.json`: structural/local-link/PDF audit and SHA256s.
- `research-verification.md`: final verification methods and qualifications.
- `TODO.md`: prioritized follow-ups and selection/validation checklist.
- `blocked.md`, `packages.md`, `prompt.md`: access/tool/approval records.

## Recovery and preservation

Initial inspection found no reports, progress file, references or applicable
AGENTS.md in this workspace or its ancestors. No live platform agents existed.
The request revisions and unrelated files were left unchanged. Initial hashes
of all three request revisions were rechecked and match.

During execution, `prompt.md` acquired additional validation instructions and
`packages.md` expanded into a detailed installed-tool inventory. These changes
were reread and preserved. Coordinator approval records are appended to
prompt.md; its original input block was not replaced. Its current block hash
differs from the initial snapshot because of the added validation instructions;
do not claim a byte-identical prompt. Package installation/manifests from
other work were not modified by this research.

## Shared baseline and scope

No inventory, hardware/host count, sites, budget, entitlement, support level,
multicast specification or recovery targets were supplied. Recommendations
remain conditional. Assume certified x86-64 hardware for the main comparison;
alternate Arm/edge/cloud paths have separate qualifications.

- VMware: VCF/VVF9.1.1, ESX/vCenter9.1.1.0100. Independently current
  VKS3.8/VKr1.37.1 is distinguished from the older GA BOM Kubernetes pair.
  Supervisor prerequisites, CNI/CSI and service entitlements are explicit.
- Proxmox: VE9.2, PBS4.2, PDM1.1. Public-channel observations include
  pve-manager9.2.24, PBS4.2.8-1 and PDM1.1.9. Signed enterprise patch set is
  not verified. LXC is native; guest Docker/Kubernetes support is separate.
- Red Hat: RHEL10.2/Podman5.8.2 as host/guest path; OCP4.22.18 plus
  Virtualization4.22.9 as mixed-workload path, with compatible optional
  OADP1.6/ODF4.22/ACM2.17. OVE is VM-only; guest rights differ by edition.

Status vocabulary: documented supported, conditional, documented unsupported,
not verified. Capability, support provider, entitlement and evidence strength
are separate. Missing documentation is not proof of unsupported behavior.
System containers, application runtimes, Kubernetes, VMs and applications are
separate layers. Restart, continuity, live migration, backup and site recovery
are separate mechanisms. Multicast matrices preserve endpoints, physical
scope, IPv4/IPv6, components, conditions and support/inference distinctions.

## Assignments and saved handoffs

The user authorized three platform agents; no nested agents were created.
Exclusive ownership was respected while each agent was active.

- `/root/vmware`: VMware report and vmware-prefixed PDFs. Initial668-word
  draft and extensive current primary PDFs/HTML saved; final messages
  established VKS3.8/VKr1.37.1, compatible BOM, multicast alternatives and
  management-plane restrictions. Usage limit prevented final report/handoff.
- `/root/proxmox`: Proxmox report and proxmox-prefixed PDFs. Full8,941-word
  draft, all substantive sections/references/unresolved sources saved before
  usage limit. Main findings: PBS S3 now supported, PDM current, OCI/import
  previews, Premium24/7 from Oct19, PDM subscription threshold and support
  contract wording conflict. Formal handoff unavailable.
- `/root/rhel`: Red Hat report and rhel-prefixed PDFs. Full8,974-word draft
  and references saved before usage limit. Main findings: current release
  lines, OVE restrictions, RHEL guest rights, OVN multicast policy exception,
  SR-IOV path, recovery/fencing and gated support matrices. Handoff unavailable.

Coordinator reconciled actual files after all agents failed, assumed ownership
and completed VMware sequentially. No duplicate writers were started. The
comparison was written only after standalone completion/review. Public package
metadata and an initially inaccessible OVE PDF were subsequently recovered.

## Verification completed

- Templates:13/13/13/14 required main headings in correct order; all sections
  substantive, no draft placeholders. Common cutoff and terminology reviewed.
- Content: support/execution/provider/rights distinctions, management domains
  and outages, lifecycle workflows, availability/failback, backup consistency,
  add-on inventories and endpoint/IP-family multicast matrices reviewed.
- PDFs:51 files pass PDF magic and pdfinfo parsing, linked from reports, with
  no byte-identical duplicates. SHA256/page counts retained in audit JSON.
  Invalid HTML responses were excluded. OVE overview retry is now a valid
  historical2025 PDF; current2026 rights still rely on subscription guide.
- Links: all local files, heading anchors and source-reference definitions
  checked.216 unique external URLs probed with curl.175 successful HEAD
  responses plus2 successful GET recoveries;39 remain live-unresolved.
  Every failed endpoint is retained in the TSV and affected report reference
  sections. Prior valid local PDFs are not invalidated by later503/timeouts.
- Corrected probe handling: slow exec commands were initially returned as
  running sessions. Those provisional failures were rerun with session polling;
  uncollected preliminary GET results are labeled, not used as final evidence.
- Markdown: markdownlint-cli2 0.24.0 / markdownlint0.42.0 checks all four
  reports and this progress file. Final scoped configuration is
  `research-markdownlint.json`: prose80, code120, wide comparison tables
  exempt from line width because Markdown rows cannot be soft-wrapped.
  MD013 remains active; other default rules remain active. Reference anchors
  were converted to Markdown headings, so no HTML rule exception is needed.
- Diagrams: mmdc12.0.0 with Chromium rendered every fenced Mermaid block
  (3 total) into temporary SVG and PNG outputs. PNGs visually inspected:
  labels readable, no clipping, execution/management relationships consistent.
  Headless launch required sandbox escalation; no platform configuration changed.
- Tools located explicitly under Node24.22.1 because inherited PATH omitted
  NVM binaries. Installed package inventory preserved in packages.md. No new
  converter/OCR/browser package was installed by coordinator.

Reproducible checks:

```bash
python3 -B research-audit.py
```

The saved audit script uses existing repository anchor logic plus table,
reference, local-link and PDF checks; durable results are in the JSON artifact.
The lint command uses the installed Node executable and CLI script:

```bash
markdownlint-cli2 --config research-markdownlint.json \
  research-vmware.md research-proxmox.md research-rhel.md \
  research-vm-comparison.md research-progress.md
```

Mermaid inputs/outputs are temporary files under `/tmp/container-diagrams*`
and `/tmp/container-diagram-review*`. Rendering used the installed Mermaid
CLI through Node, with `/tmp/container-puppeteer.json` selecting Chromium.

## Remaining evidence gaps and next steps

The actionable checklist is maintained in
[TODO.md](99_Archive/TODO.md). Created on
2026-10-30 from the saved gaps and validation plan; no new research or live
testing was performed for that documentation update.

These prevent unconditional procurement/deployment assurances, not the saved
conditional architectural comparison:

1. Obtain exact hardware/guest/add-on certification and every optional-service
   latest patch/lifecycle/support schedule. Broadcom portal lookups and some
   Red Hat matrices are gated; deployment inventory is unknown.
1. Confirm signed Proxmox enterprise package set; public HTTP observations
   were parsed without signed-metadata authentication. Resolve current support
   wording against January agreements and newest Veeam build/plug-in pairing.
1. Confirm VMware VVF recovery/SRM/ACC/RPO-tier rights, OVE OADP entitlement,
   current ODF Advanced/DR metrics and bundle/node/guest rights in quotes.
1. Recheck architecture/update-channel errata where Red Hat sources differ;
   stable manifests verified4.22.18, but later MicroShift reference is retained.
1. Obtain multicast groups/ports/family/source semantics/topology/throughput.
   Qualify IPv6, Windows, external-LAN and secondary-interface paths; do not
   generalize component support into end-to-end commercial app certification.
1. Run the proposed application-specific multicast, failure/maintenance,
   backup/restore and site recovery/failback proof of concept after separate
   deployment authorization. No such tests were executed in this task.
1. Retry live-unresolved source endpoints normally or obtain entitled material.
   Veeam migration-PDF lead still returns HTML; no invalid PDF was retained.

## Persistent command permissions

User-requested global rules were saved with backups and validated using
`codex execpolicy check`: curl; read-only source extractor; gzip -dc; exact
package-parser literals; exact Node24.22.1 plus Mermaid CLI script prefix.
No arbitrary Python or Node prefix was allowed. Helper mode supports HTML
text/links and Debian package-version extraction. Rules load at startup;
existing sessions can retain queued approval state. Full prompts/outcomes and
paths are preserved in prompt.md. All required configuration writes used the
session's approval mechanism.
