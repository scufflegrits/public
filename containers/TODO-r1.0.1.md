# Project TODO

Revision: **r1.0.1** (copied from the baseline `TODO.md`, then updated after the
independent review). Updated: **2026-11-02**. Research baseline: **2026-10-30**.
Review findings: [research-review-r1.0.1.md](research-review-r1.0.1.md).

The four reports are delivered as conditional desk research. This checklist
tracks the work needed to resolve evidence gaps and prepare a platform
decision. Detailed evidence stays in the reports; execution history stays in
[research-progress.md](research-progress-r1.0.1.md), and access problems stay in
[blocked.md](blocked-r1.0.1.md).

## Research follow-ups

- [ ] Reconcile and recheck the URLs listed as unresolved by the 2026-10-31
  probe (67 in the TSV; the prior TODO said39) in
  [research-link-checks.tsv](research-link-checks-r1.0.1.tsv). Distinguish transient
  failures, obsolete discovery URLs and gated sources; retain valid local
  evidence and document replacements in the affected reports.
- [ ] Obtain the missing Broadcom hardware/guest/lifecycle lookups and Red Hat
  support matrices through normal entitled access. Record the exact supported
  combinations and affected conclusions.
- [ ] Verify the signed Proxmox enterprise package set. Public HTTP package
  observations do not establish authenticated enterprise-channel freshness.
- [ ] Verify the latest supported patch/lifecycle of optional services actually
  selected for use. The general RHEL distinction is now recorded: package
  errata are released when available (no fixed monthly schedule); minor
  releases are planned about every six months during Full Support and include
  cumulative qualified errata. This does not establish current operator/add-on
  patch levels or their subscription-specific support channels.
- [x] Re-read the Red Hat HTML-only claims through normal public browser
  access. The 4.22 docs now list WMCO 10.22.1 (issued July 28, 2026); the
  Windows Server support table is explicitly labeled WMCO 10.20.0, so do not
  present its detailed platform/build rows as a 10.22.1 matrix. The docs also
  confirm tested maxima of 2,000 nodes and 150,000 pods, with workload and
  configuration caveats, and three worker nodes recommended for OpenShift
  Virtualization live migration. See Red Hat U11 in the report.
- [x] Re-read the 2026-10-28 SDDC Manager security advisory (VMware V13).
  CVE-2026-111497 remains patch-pending for listed affected versions; the
  advisory provides version-specific workarounds. No remediation was performed.
- [x] Read Veeam's VMware-to-Proxmox migration guide through the official web
  PDF extraction. It describes full recovery with on-the-fly conversion and
  notes a version 1.0 limitation: cross-hypervisor on-the-fly conversion only
  works with Proxmox as the source. The vendor endpoint still returns an HTML
  page to direct download attempts, so a valid local PDF is not retained.

Platform details: [VMware gaps](research-vmware-r1.0.1.md#limitations-risks-and-open-questions),
[Proxmox gaps](research-proxmox-r1.0.1.md#limitations-risks-and-open-questions),
[Red Hat gaps](research-rhel-r1.0.1.md#limitations-risks-and-open-questions).

## Before platform selection or procurement

- [ ] Gather workload/OS inventory, hardware, CPU/core/socket counts, storage,
  sites, growth, existing entitlements, budget, skills and support requirements.
- [ ] Define per-application recovery time/recovery point objectives, tolerated
  restart/session loss, retention, independent-copy and failback requirements.
- [ ] Specify multicast IP families, groups, source semantics, ports, topology,
  throughput, external endpoints and acceptable loss/rejoin behavior.
- [ ] Quote VMware SRM/Live Recovery Cloud SKUs, RPO tiers and ACC rights. The
  r1.0.1 review established that SRM and Live Recovery Cloud are separately
  purchased Advanced Services for VVF and VCF (feature comparison footnote 13).
- [ ] Confirm in the order the OADP inclusion for OVE documented in the January
  2026 subscription guide (p29), current ODF Advanced/DR terms and applicable
  OpenShift bundle, node and guest rights. Plan cluster boundaries knowing one
  cluster cannot mix OVE with OKE/OCP/Plus nodes.
- [ ] Reconcile Proxmox support-transition wording with the agreement and
  confirm the supported Veeam build/plug-in pairing.
- [ ] Validate the complete proposed hardware/guest/runtime/CNI/CSI/application
  stack and obtain comparable quotes. Update conditional recommendations using
  those verified requirements rather than choosing a universal winner.

## Proof of concept — requires separate deployment authorization

- [ ] Validate multicast in both directions for same-host, cross-host,
  VM-to-container and external-LAN endpoints, IPv4/IPv6 separately. Repeat
  after migration, failure, rescheduling and membership aging.
- [ ] Test manager/control-plane loss, host failure, quorum/fencing,
  storage/network failure and planned maintenance. Measure application
  recovery and traffic restoration against the agreed targets.
- [ ] Restore representative VMs, excluded mount data, Kubernetes resources
  and persistent application data; recover keys and verify independent copies.
  Exercise site recovery and controlled failback without competing writers.

Use the existing [validation plan](research-vm-comparison-r1.0.1.md#open-questions-and-proposed-validation);
these tests have **not** been performed.

## Maintenance and closure

- [x] Finish the `reference/<name>.pdf.md` extractions: 51 of 51 done on
  2026-10-30 (the VCF manual finished last). Earlier note: 50 of 51 done on
  2026-10-30 (none empty; smallest are ~750-word press releases). The 9,085-page
  `vmware-cloud-foundation-9-1-technical-documentation.pdf` was still converting
  in the original background run. Do not start a second conversion of that file
  while the first is running.
- [x] After all 51 extractions exist, rerun `python3 -B research-audit-r1.0.1.py`
  and save its output to `research-verification-r1.0.1.json`. Confirm the
  `.pdf.md` issues are gone and no other issue appeared.
- [x] Spot-check the new extractions: none empty; key verified values present.
  The feature-comparison extraction loses its column headers, so use the PDF
  for edition questions (recorded in the verification summary).
  The feature comparison, SPDs and FAQs are table-heavy, and MarkItDown
  flattens tables. Record any extraction that is not a usable search aid in
  `research-verification-r1.0.1.md`; the PDF remains the cited source.
- [x] Update `research-verification-r1.0.1.md` (PDF text extractions section,
  now "51 of 51") and the progress checkpoint with the final count.
  No report or claim-ledger change is needed: every claim was checked against
  the PDFs themselves, not against the `.pdf.md` files.
- [x] Save reproducible diagram extraction/render configuration alongside the
  audit utility: `research-mermaid-render-r1.0.1.py` (r1.0.1 review).
- [x] Install `mdformat-frontmatter` in `~/.venv` (repository convention) and
  then run `~/.venv/bin/mdformat` on the r1.0.1 Markdown files. Done 2026-10-30
  after the user installed the plugin (request revisions excluded).
- [ ] On a later research pass, assess whether the cutoff needs refreshing.
  If it changes, revalidate affected evidence and align all four reports.
- [ ] After substantive changes, run the revision's audit script (currently
  `research-audit-r1.0.1.py`), lint the reports and progress file, render
  changed diagrams, and update the verification records.

Close an item only when its answer or validation result is recorded in the
relevant report and progress log. An explicitly documented unknown remains
open; it does not mean the platform is unsupported.
