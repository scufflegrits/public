# VM and Container Platform Research

This project compares VMware, Proxmox, and Red Hat options for running and
managing virtual machines and containers. It is a source-backed decision aid:
it explains where workloads run, how they are managed and protected, what
networking and recovery depend on, and which support or entitlement questions
still need answers.

## Start here

1. Read the [platform matrix](research-matrix.md) for a quick stack-by-stack
   view, then the [platform comparison](research-vm-comparison-r1.0.1.md) for
   detailed evidence and conditional fit guidance.
2. Read the standalone reports for platform-specific evidence:
   [VMware](research-vmware-r1.0.1.md),
   [Proxmox VE and PBS](research-proxmox-r1.0.1.md), and
   [Red Hat](research-rhel-r1.0.1.md).
3. Check the [research TODO](TODO-r1.0.1.md) for unresolved evidence and
   decision inputs.

## Research baseline and limits

The reports use a **2026-10-30 research cutoff**. Targeted evidence notes were
added on **2026-11-02**; those additions are dated in the reports and do not
change the stated baseline. The selected product paths include VMware VCF/VVF
9.1.1 with VKS, Proxmox VE 9.2 with PBS 4.2, and RHEL 10.2 / OpenShift 4.22.
Each report explains where independently current components differ from a
tested or documented compatible bundle.

No hardware or workload inventory, network specification, subscription
entitlements, budget, or recovery targets were supplied. The recommendations
are therefore conditional. The work is desk research: no platform deployment,
live multicast or failover testing, measured recovery, purchase, or production
change was performed.

In the reports, **not verified** means the available evidence did not establish
the particular support claim. It does not by itself mean the capability is
impossible or unsupported. Hardware-specific certification, entitled support
matrices, signed Proxmox enterprise package freshness, selected add-on
lifecycles, and proof-of-concept testing remain follow-up items.

## Research records

- [Claim audit](research-claim-audit-r1.0.1.tsv) — evidence status by claim.
- [Review notes](research-review-r1.0.1.md) and
  [progress log](research-progress-r1.0.1.md) — review history and dated
  supplements.
- [Verification summary](research-verification-r1.0.1.md) and
  [verification data](research-verification-r1.0.1.json) — document checks and
  their scope. These are not deployment tests.
- [Link-check ledger](research-link-checks-r1.0.1.tsv) — URL probe results.
  Its 2026-10-31 results list 67 unresolved URLs; an older progress note says
  39, so that count must be reconciled before the link-check follow-up closes.
- `reference/` — retained source PDFs, text extractions, and dated web snapshots
  where available. The cited original source remains authoritative; an
  extraction is a reading aid.
- [Request specification](request-container-comparison-r1.0.2.md) — scope and
  questions that guided the research. Earlier request revisions are retained
  for history.

## Project files

The audit helper is [research-audit-r1.0.1.py](research-audit-r1.0.1.py).
Mermaid render settings are in
[research-mermaid-render-r1.0.1.py](research-mermaid-render-r1.0.1.py). The
project also includes [blocked-access notes](blocked-r1.0.1.md), package and
tool observations ([packages](packages-r1.0.1.md)), and a
[baseline manifest](research-baseline-r1.0.0.manifest.json) used to track
preserved inputs.

## Status language

- **Documented supported** — a vendor source documents the stated path under
  the listed conditions.
- **Conditional** — the capability is documented, but depends on requirements
  such as a supported version, network setup, hardware, or entitlement.
- **Documented unsupported** — a vendor source explicitly excludes the path.
- **Not verified** — the research did not establish whether the path is
  supported.

Do not treat these desk-research reports as product certifications, a bill of
materials, a deployment design, or a substitute for current vendor support and
licensing confirmation.
