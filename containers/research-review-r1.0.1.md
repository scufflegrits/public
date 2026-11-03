# Container platform research: independent review r1.0.1

Review revision: **r1.0.1**. Baseline: the unversioned research bundle, recorded
as **r1.0.0** for preservation bookkeeping only
([manifest](research-baseline-r1.0.0.manifest.json)). Research cutoff:
**2026-10-30** (unchanged). Review date: **2026-10-30**. Governing inputs:
[request r1.0.2](request-container-comparison-r1.0.2.md) and
[review handoff r1.0.0](review-handoff-r1.0.0.md).

Review mode: **historical verification at the original cutoff**. The review
happened on the cutoff date, so no newer developments were separated out and
no cutoff refresh was needed. Web pages fetched during the review are dated
2026-10-30 snapshots of the same baseline period.

## Scope and method

- One coordinator (this session) did the review sequentially. No subagents
  were started. `ListAgents` showed two unrelated peer sessions, both started
  seven days earlier; neither owns files in this project.
- Every claim group in the ledger was checked against the primary source text:
  a saved local PDF (text layer, with page renders where a table needed column
  headers) or a public web page saved under `reference/web/` on 2026-10-30.
- Claim IDs, locators, source pages, hashes and verdicts are in
  [research-claim-audit-r1.0.1.tsv](research-claim-audit-r1.0.1.tsv). A claim
  repeated across reports has one ledger row that lists every location.
- At the user's request, every local PDF also got a MarkItDown extraction saved
  beside it as `reference/<name>.pdf.md`. Web snapshots have Trafilatura
  extractions (`.html.md`). These derived files make the sources searchable;
  the original PDF or HTML stays the citable evidence. MarkItDown flattens PDF
  tables, so every table-dependent claim was checked against the PDF layout or
  a rendered page.

## Verdict summary

33 ledger rows: **26 verified**, **6 partly supported**, **1 not verified**,
**0 contradicted**, **0 temporal drift**. No version, release date, price or
lifecycle date in the baseline was wrong. The corrections fix entitlement
statements, status labelling and internal consistency.

### Corrections that affect selection or procurement

1. **Red Hat OVE includes OADP (RH-LIC-01).** The report's own entitlement
   source, the January 2026 self-managed OpenShift subscription guide (R1, PDF
   p29), lists OpenShift APIs for Data Protection as included for OVE, OKE,
   OCP and Platform Plus. The baseline left this as an open procurement
   question because the Operator life-cycle page names only OKE/OCP/Plus.
   That page names OVE for no Operator at all, so its omission is not a
   conflicting exclusion. All four reports now state the documented inclusion,
   subject to order confirmation.
1. **OpenShift product types cannot be mixed in one cluster (RH-LIC-02).** R1
   p7 requires every node in a cluster to carry the same product type (OVE,
   OKE, OCP or Plus). Neither report mentioned this. It changes the
   mixed-workload recommendation: OVE for VMs plus OCP/Plus for application
   pods means separate clusters, or one product type for the whole cluster.
   The Red Hat licensing section and the comparison's licensing table and
   recommendations now say so.
1. **VMware SRM and Live Recovery Cloud are add-ons (VM-REC-01).** The 2026-10-14
   feature comparison has three columns: VVF, VCF Edge and VCF. It lists Site
   Recovery Manager and Live Recovery Cloud under *Advanced Services (Add-ons)*
   for all three, and footnote 13 says those are separate purchases not included
   in core VCF or VVF. Footnote 14 says Any-to-vSAN Replication requires an SRM
   license. The baseline treated VVF recovery rights as unresolved. The open
   question narrows to SKUs and RPO tiers in the quote.

### Accuracy and consistency corrections

1. **NSX routed multicast is documented for IPv4 only (VM-NET-01).** The VCF
   9.1 manual (printed p3509) scopes tier-0/tier-1 multicast to "an IPv4
   network". The IPv6 cell remains **not verified** but now says the feature
   is documented for IPv4 only. Two documented limits were added: ESX hosts
   and NSX Edge only, and up to four VTEP segments.
1. **Proxmox OCI-image containers relabelled (PX-SUP-01).** The baseline marked
   the technology preview **documented unsupported**. The evidence (guide p329
   and §14; agreement: previews "not supported in production environments")
   excludes production support but does not declare the capability
   unsupported. The status is now **conditional**: preview, non-production
   only.
1. **Proxmox package-freshness inconsistency (PX-PKG-01).** Limitations item 1
   and the unresolved-reference row still said the public index could not be
   read. The baseline section reports later unauthenticated HTTP observations.
   Both now say: HTTPS failed hostname validation, HTTP observations exist but
   were not retained or signature-checked, and the signed enterprise set
   remains unverified.
1. **Minor precision fixes:** Ceph Tentacle 20.2.1 named at the VE 9.2 launch.
   The RHEL 10.2 notes contain both "buildah rebased to 1.41.8-1" (PDF p89) and
   Container Tools Buildah 1.43.1 (p90), so the installed package should be
   checked. Proxmox reference P13 is unassigned, which is recorded rather than
   renumbered.

### Not verified in this review

- **RH-NV-01:** WMCO 10.22.0 with Windows Server 2022/2025, OCP 4.22 tested
  maxima (2,000 nodes and 150,000 pods), and the three-worker recommendation.
  Direct requests to docs.redhat.com returned HTTP 403 on 2026-10-30, and no
  bypass was attempted. These claims keep their baseline qualifications and
  are listed as unresolved U11 in the Red Hat report.
- The Oct 28 SDDC Manager security advisory (VMware V13) was not re-read.

## Effect on the conditional recommendations

- **VM-only Red Hat:** stronger. OVE plus OADP is a documented commercial
  starting point. Containerized applications later need core-pair entitlement
  of those VMs, a whole-cluster product change, or a separate cluster.
- **Mixed VM/container (Red Hat):** must plan cluster boundaries around product
  types, not node roles.
- **VMware site recovery:** site recovery is an add-on purchase for VVF and VCF
  alike. That narrows the VVF-versus-VCF difference for recovery and puts the
  remaining question in the quote.
- **Multicast:** unchanged in substance. The NSX routed path is now explicitly
  IPv4. No recommendation was promoted.
- **Proxmox:** unchanged. The OCI-preview label change doesn't alter the
  recommended VM-hosted application-container path.

## Coverage by report section

"Evidence-verified" means a ledger row ties the section's consequential claims
to primary source text. "Consistency-reviewed" means the content was read in
full and checked against the verified facts and the other reports. Those
sections are explanatory or labelled technical inference or recommendation,
and they make no version, entitlement or support claim of their own.

| Section (platform reports)              | VMware                                                                 | Proxmox                                                                                               | Red Hat                                                                   |
| --------------------------------------- | ---------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| Summary and fit                         | consistency-reviewed                                                   | consistency-reviewed                                                                                  | consistency-reviewed                                                      |
| Verified product baseline               | evidence-verified (VM-BASE-01, VM-VKS-02, VM-LIC-02)                   | evidence-verified (PX-BASE-01, PX-ARM-01, PX-PKG-01)                                                  | evidence-verified (RH-BASE-01, RH-LC-01)                                  |
| Architecture and workload support       | evidence-verified (VM-POD-01, VM-VKS-02, PX-CAND-01)                   | evidence-verified (PX-SUP-01, PX-CAND-01)                                                             | evidence-verified (RH-RT-01, RH-BASE-01); RH4 row RH-NV-01                |
| Centralized and multi-host management   | evidence-verified (VM-HA-01, VM-VKS-01, VM-MGMT-01)                    | evidence-verified (PX-HA-01, PX-PDM-01)                                                               | consistency-reviewed; scale para RH-NV-01                                 |
| Provisioning and orchestration          | consistency-reviewed                                                   | consistency-reviewed                                                                                  | consistency-reviewed                                                      |
| Networking and multicast                | evidence-verified (VM-NET-01, VM-NET-02, VM-VKS-01, NET-UP-01)         | evidence-verified (NET-UP-01); end-to-end rows remain labelled inference                              | evidence-verified (RH-NET-01, RH-RT-01, NET-UP-01)                        |
| Availability, failover, and maintenance | evidence-verified (VM-HA-01, VM-HA-02, VM-RISK-01)                     | evidence-verified (PX-HA-01)                                                                          | evidence-verified (RH-HA-01); topology RH-NV-01                           |
| Backup, restore, and DR                 | evidence-verified (VM-REC-01, VM-VKS-01)                               | evidence-verified (PX-BKP-01; PBS WORM/protected-flag text in guide §10.7 and client docs)            | evidence-verified (RH-LIC-01); ODF DR terms remain 2024-sourced           |
| Other capabilities and operations       | consistency-reviewed                                                   | consistency-reviewed                                                                                  | consistency-reviewed                                                      |
| Licensing, subscriptions, and support   | evidence-verified (VM-LIC-01, VM-LIC-02, VM-MGMT-01)                   | evidence-verified (PX-LIC-01, PX-LIC-02, PX-PDM-01)                                                   | evidence-verified (RH-LIC-01, RH-LIC-02, RH-LIC-03)                       |
| Modules, add-ons, and integrations      | partly (VM-REC-01); advanced-service catalog rows consistency-reviewed | partly (PX-BKP-01; Offline Mirror free-eligibility text checked); ecosystem rows consistency-reviewed | partly (RH-BASE-01 companion versions); catalog rows consistency-reviewed |
| Limitations, risks, open questions      | consistency-reviewed and corrected                                     | consistency-reviewed and corrected                                                                    | consistency-reviewed and corrected                                        |
| References                              | links checked by audit; new review snapshots added (V20, P32, R58)     | same                                                                                                  | same; U11 added                                                           |

The comparison's 14 sections were reviewed after the platform reports and
corrected wherever a platform finding applied: the licensing table, the NSX
multicast row, the backup paragraph, the mixed-workload and VM-only Red Hat
recommendations, open questions, and the unresolved table.

Claim classes not independently re-verified against a primary source in this
review: the vendor-neutral Kubernetes and Linux operational explanations
(drain, PodDisruptionBudgets, etcd, generic RTO/RPO definitions); the ecosystem
directory rows (NAKIVO, Vinchin, Lightbits, Zabbix, NVIDIA and others); the
VMware ACC SPD contents; the Red Hat ACM, AAP and Satellite capability
statements; and the R25 certified-guest list. All of them already carry
"not verified" or "conditional" status, or "separate entitlement" qualifiers,
in the reports. No recommendation depends on them being stronger than stated.

## Readiness assessment

| Use          | Assessment                                                                                                                                                                                                         |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Shortlisting | **Ready**, as conditional desk research. Versions, prices, lifecycle dates and the main support and entitlement boundaries are verified at the cutoff.                                                             |
| Procurement  | **Not ready without quotes.** VMware SRM/Live Recovery SKUs and RPO tiers, ODF Advanced/DR metrics, OVE OADP order confirmation, the Proxmox 24/7 contract wording and Veeam build pairing must come from vendors. |
| Deployment   | **Not ready.** No hardware, guest, CNI/CSI, multicast application or recovery requirements were supplied. No platform, multicast, failover, backup or restore test was performed or is claimed.                    |
