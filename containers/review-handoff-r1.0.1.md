# Container platform research: review and revision handoff

Instruction document revision: **r1.0.1**, created **2026-10-30**, revised
**2026-11-01** to name the research tools guide (supersedes
[r1.0.0](review-handoff-r1.0.0.md)).
Workspace: `/home/sysadmin/projects/guides/containers`.
Existing research cutoff: **2026-10-30**.

Use this document when instructed to review and revise this project. Creating
this handoff does not start that review or revise the existing reports.
No clarification is needed to begin a document/evidence review. Record unknown
deployment requirements and continue work that does not depend on them.

## Mission and governing material

Independently assess the research, correct consequential errors, close
accessible evidence gaps, and produce a coherent next revision. Test the
existing conclusions against primary evidence; do not assume they are correct
because the reports are extensive or passed document checks.

Read applicable `AGENTS.md` files, then read the complete authoritative
[execution request](request-container-comparison-r1.0.2.md). Also read:

- [prompt.md](prompt.md), including later validation instructions and the
  approval history. Existing command examples are not instructions to run
  configuration changes again.
- [research-progress.md](99_Archive/research-progress.md),
  [TODO.md](99_Archive/TODO.md), [blocked.md](99_Archive/blocked.md), and the
  full [packages.md](99_Archive/packages.md) inventory.
- All four reports: [VMware](99_Archive/research-vmware.md),
  [Proxmox](99_Archive/research-proxmox.md),
  [Red Hat](99_Archive/research-rhel.md), and
  [comparison](99_Archive/research-vm-comparison.md).
- [Verification methods](99_Archive/research-verification.md),
  [audit results](99_Archive/research-verification.json),
  [external-link log](99_Archive/research-link-checks.tsv),
  [audit utility](99_Archive/research-audit.py), and
  [lint configuration](99_Archive/research-markdownlint.json).
- The shared [research tools guide](../research/research-tools-r1.0.2.md)
  for source discovery, retrieval, PDF/HTML extraction and validation tools.

The r1.0.1 review moved the unversioned baseline files above to `99_Archive/`
(gitignored, so those links resolve only in the local workspace). Their
hashes are recorded in the
[baseline manifest](research-baseline-r1.0.0.manifest.json).

The request revisions are immutable inputs. Do not revise their requirements
to make the reports pass. Follow current user instructions where they amend
the work. Preserve unrelated files and any user edits discovered on recovery.

## Understand the starting point

The current reports are conditional desk research intended to support
shortlisting. They do not certify a deployable stack or establish measured
availability, multicast behavior, recovery times, or total cost.

Three platform agents performed research, but reached usage limits before
formal final handoffs. The coordinator completed VMware and the synthesis
from saved artifacts. An independent final claim-by-claim review has not yet
been performed; that is the main purpose of this assignment.

Recorded baseline claims include VCF/VVF9.1.1 with asynchronous VKS3.8;
Proxmox VE9.2/PBS4.2/PDM1.1; and RHEL10.2 with OpenShift4.22 and matching
Virtualization. These are claims to verify, not assumptions to carry forward.
Likewise, the recorded51 PDFs,47 tables,216 URLs and39 unresolved live probes
are historical counts. Recount the actual artifacts when reviewing them.

Structural checks establish document integrity and traceability. A valid PDF,
HTTP200 response, working link, rendered diagram, or complete heading does
not establish that a consequential claim is true or supported commercially.

## First action: inventory and recover

Before editing any existing project file:

1. Inspect files and revision names, repository status, references and saved
   progress. Read changed content and identify user edits. Do not reset,
   discard, rename or overwrite existing work.
1. Check for active agents and assignments if management tools exist. Recover
   their actual ownership/status; do not start duplicate writers or assume
   historical agents are still running.
1. Reconcile the progress log with the reports and artifacts. Identify what
   is complete, pending review, partly revised, or missing evidence.
1. Establish the review date, original research cutoff, selected paths and
   evidence rules. Record whether this is historical verification, a current
   research refresh, or both.
1. Inventory existing revision bundles before choosing a new revision. If a
   prior review was interrupted, resume its saved draft after verifying its
   baseline and ownership instead of creating another conflicting bundle.

Read-only inspection and creation of a new baseline manifest may precede
revision copies. Changes to existing reports, logs, tools and validation data
must wait until the next-revision copies have been created.

## Mandatory revision protocol

### Revision scheme

The unversioned research deliverables have no declared document revision.
Treat that existing bundle as **r1.0.0 for preservation bookkeeping only**.
This does not certify its correctness and is independent of request r1.0.2.

For the first review, use **r1.0.1** if no later research revision exists.
If later revisions exist, identify the authoritative baseline from saved
progress and manifests, then increment its patch number. Never overwrite an
existing destination. Use a minor revision for an explicit scope/structure
change, or a major revision for incompatible scope changes; document why.
Do not choose the report revision from the request or this handoff's version.

### Copy before editing

Create a complete next-revision working bundle before modifying its content.
Retain the original filenames and bytes as the historical baseline.

For an initial r1.0.1 review, the mapping is:

| Existing baseline            | New working copy                    |
| ---------------------------- | ----------------------------------- |
| `research-vmware.md`         | `research-vmware-r1.0.1.md`         |
| `research-proxmox.md`        | `research-proxmox-r1.0.1.md`        |
| `research-rhel.md`           | `research-rhel-r1.0.1.md`           |
| `research-vm-comparison.md`  | `research-vm-comparison-r1.0.1.md`  |
| `research-progress.md`       | `research-progress-r1.0.1.md`       |
| `TODO.md`                    | `TODO-r1.0.1.md`                    |
| `research-verification.md`   | `research-verification-r1.0.1.md`   |
| `research-verification.json` | `research-verification-r1.0.1.json` |
| `research-link-checks.tsv`   | `research-link-checks-r1.0.1.tsv`   |
| `research-audit.py`          | `research-audit-r1.0.1.py`          |
| `research-markdownlint.json` | `research-markdownlint-r1.0.1.json` |

Also copy `blocked.md`, `prompt.md`, `packages.md`, or this handoff to
revision-suffixed files before changing them. Leave shared originals intact.
Do not copy dependency directories or duplicate unchanged source PDFs.

Create a new `research-baseline-r1.0.0.manifest.json` recording source paths,
sizes, SHA256s, source-to-copy mappings, cutoff and review date. Inventory
relevant reference hashes too. Use the actual baseline revision in its name
on later passes. Create files without clobbering existing destinations; an
existing manifest or destination requires recovery inspection, not replacement.

Verify each initial copy matches its source hash. Only then edit the working
copies. Mark their review/verification state **draft, not yet revalidated**;
copied verification results remain historical until checks are rerun.

Add document revision, baseline, review date, research cutoff and review status
near the top of each revised report. Preserve the required main headings.
Record changes in the review log rather than adding incompatible main sections.

Keep all four reports at the same bundle revision. Update their relative links
to revised peers and revised logs/results. Links to immutable request inputs
and unchanged shared source PDFs may remain unchanged. Do not replace originals
with symlinks, redirects, or rewritten copies unless separately instructed.

### Preserve evidence

Keep source PDFs immutable. A changed download gets a new descriptive,
collision-safe filename with the platform prefix and useful date/version.
Compare hashes and reuse identical local copies instead of duplicating them.
Record original URL, publication/update date, access date and local path.

When a source is superseded, preserve it and label its historical role. Retain
failed-source history and document replacements; do not silently delete gaps.

## Independent evidence review

Create `research-review-r1.0.1.md` and
`research-claim-audit-r1.0.1.tsv`, using the actual working revision.
Audit every consequential claim or table row; do not infer complete coverage
from a sample. A shared claim may have one ledger entry listing all locations.
Identify any section or claim class not yet reviewed.

For each claim, record:

- Stable claim ID, report/revision, heading or row locator, and the claim.
- Exact product/version, execution path and relevant support/entitlement scope.
- Primary source title, publisher, URL, document version and dates.
- Precise section/table/page locator. Distinguish printed page from PDF page
  where they differ, and identify the local file/hash when used.
- What content was actually read and how it supports or limits the claim.
- Verdict: verified, partly supported, contradicted, not verified, or temporal
  drift. Keep this review verdict separate from the report's support status.
- Required correction, affected comparison conclusions and remaining action.

Use primary vendor/upstream release notes, compatibility/lifecycle matrices,
support policies, licensing terms and catalogs. Search results and secondary
articles can identify leads; inspect the actual primary material before using
it to substantiate a support or entitlement conclusion.

Do not treat a newer source as historical proof without checking effective
dates. Distinguish GA from preview, announcement from availability, current
component from compatible stack, feature catalog from license grant, and
upstream feasibility from commercial support.

Prioritize claims whose correction could change selection or procurement:

| Area               | Questions to challenge                                                                                                                                                                  |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Versions/lifecycle | Are releases real, GA by cutoff, supported and compatible? Are optional products and asynchronous components independently qualified?                                                   |
| Workload support   | Where does the workload execute, what kernel/runtime does it use, and who supports each layer? Is guest support being extended without evidence?                                        |
| Management         | Are host, cluster, site and vendor scopes distinct? Does a dashboard control lifecycle or merely show inventory? What fails with the manager?                                           |
| Multicast          | Are endpoint pair, same/cross-host/LAN path, IP family, CNI/mode, physical dependencies and support owner explicit? Is application multicast confused with discovery or fabric traffic? |
| Availability       | Are restart, replicas, live migration, FT and site recovery distinguished? Are quorum, fencing, storage and management-plane restrictions supported?                                    |
| Backup             | What is captured/excluded? Are consistency, external mounts, PVC data, keys, control-plane state and restore dependencies actually covered?                                             |
| Commercial         | Are bundle rights, support levels, metrics/minimums, order availability, recovery rights and add-ons evidenced by applicable terms?                                                     |
| Recommendations    | Does the conclusion follow from verified capabilities and stated unknowns, without invented performance, recovery or cost guarantees?                                                   |

Review VMware recovery/VVF/SRM/ACC rights and management-plane restrictions;
Proxmox previews, signed enterprise package freshness, PDM eligibility and
support-contract wording; and Red Hat OVE guest/OADP rights, ODF DR terms,
update-channel differences and gated matrices. Verify these independently.

For multicast, explicitly inspect IGMP/MLD membership, default versus secondary
networks, IPv4/IPv6, physical switching/routing, security-policy exceptions and
behavior after migration or rescheduling. A VM's multicast support does not
prove the runtime/CNI path; IPv6 neighbor discovery does not prove arbitrary
IPv6 application multicast. Clearly label technical inference.

## Cutoff and refresh rules

A historical review may retain the2026-10-30 cutoff while stating its actual
review date and testing what was supported then. Newer findings must be
identified as later developments, not silently inserted into that baseline.

If conducting fresh research under the execution request, use the actual new
execution cutoff. Revalidate all affected time-sensitive claims across the
four revised reports. Keep historical evidence and change notes, align shared
stacks, and distinguish latest components from a supported combination. Do not
update one platform to today while silently leaving others on the old cutoff.

Unknown inventory, quotes and unavailable source bodies do not prevent useful
review. Record bounded conclusions and exact dependencies. Never invent a
supported combination or mark missing documentation as unsupported.

## Correct and reconcile

1. Save findings incrementally in the new review/claim logs before large edits.
1. Correct the revised standalone reports first, citing applicable evidence
   near the changed claims and preserving their standalone explanations.
1. Finish and review all three platform reports before revising the comparison.
   Propagate changes to recommendations, matrices, assumptions and diagrams.
1. Reconcile terminology, versions, provider responsibilities and entitlements.
   A stronger finding in one report must not lose its qualifications elsewhere.
1. Update the versioned TODO, blocker and unresolved-reference records. Close
   items only when the supporting evidence/result is saved; a documented
   unknown remains open.

If delegation is authorized in the active task, use at most three platform
reviewers with exclusive ownership of their revised report and new prefixed
PDFs. The coordinator owns synthesis, shared logs, manifest and validation.
Check live assignments first; use no nested agents. Review handoffs or recover
their actual artifacts before synthesizing. Agent agreement is not independent
source evidence. Do not spawn agents merely because this file was opened.

## Validation of the new revision

Inspect installed tools using packages.md and the
[research tools guide](../research/research-tools-r1.0.2.md); use existing
runtimes and avoid implicit downloads during discovery. Previous version/tool
results are dated records, not proof of readiness in a new session.

The existing audit hardcodes unversioned report names and cutoff and imports
the sibling `../tools/check_anchors.py`. Adapt the **versioned copy** to audit
the intended revised files/cutoff and verify that dependency. Print the actual
targets. Running the old script successfully would not certify new revisions.

For example, after adapting the new audit:

```bash
python3 -B research-audit-r1.0.1.py

markdownlint-cli2 --config research-markdownlint-r1.0.1.json \
  research-vmware-r1.0.1.md research-proxmox-r1.0.1.md \
  research-rhel-r1.0.1.md research-vm-comparison-r1.0.1.md \
  research-progress-r1.0.1.md TODO-r1.0.1.md \
  research-review-r1.0.1.md
```

Keep raw audit output distinct from the broader verification summary; do not
overwrite copied results with incomplete output and retain an old success
claim. Record command, target revision, date, tool version, exit status and
limitations for each check.

Required checks:

- Templates, all required topics/tables/workflows and common cutoff/terminology.
- Claim-ledger coverage, unresolved evidence and comparison consistency.
- Markdown, source-reference definitions, anchors and all local links, including
  revised peer links. Preserve established lint rules; do not suppress errors
  merely to get a passing result.
- Actual PDF signatures/parser readability, hashes, duplicate detection and
  original/local links. Validate fetched content, not its filename alone.
- External URL checks with bounded timeouts and final process results. Poll
  yielded sessions to completion. Separate HEAD/GET availability from access
  to article content and from prior valid local evidence.
- Every Mermaid block rendered with mmdc, then visually inspected for labels,
  clipping and correct relationships. Keep derived previews separate from
  source reports and record reproducible rendering commands/configuration.
- Baseline hashes unchanged and all intended edits confined to new revisions
  and new evidence artifacts. Ensure no active writer remains unaccounted for.

Technical/document checks supplement the evidence review. Do not claim live
platform, multicast, failover, restore or performance tests from these checks.

## Execution boundaries and durable progress

Authorized review work consists of reading, public-source research, reference
downloads, versioned report corrections and document validation. Do not
provision platforms, change production/network configuration, buy products,
commit or publish without separate authorization. Do not contact vendors or
other people through messaging tools unless explicitly instructed.

Reuse available approved commands within their actual scope. Do not assume a
saved prefix covers piped Python, decompression or another executable. Prefer
downloading to a local file, then parsing it in the sandbox. Inspect existing
rules and approval history without rewriting them just to enable research.
Never bypass authentication, TLS checks or required approval mechanisms.

Record system/tool/access blockers in the versioned blocked log, genuinely
needed tools in the versioned packages record, and any required user prompts
in the versioned prompt log. Ask only for information or authority genuinely
needed after checking available context; continue independent work meanwhile.

Checkpoint the versioned progress file after review milestones, handoffs,
corrections and checks. Include current owners, files saved, reviewed sections,
claim IDs, evidence gaps, blockers and next concrete actions. On interruption,
reread the request, manifest, progress and actual working artifacts. Preserve
the chosen revision and resume unfinished work; do not restart blindly.

## Completion and handoff

Deliver the four revised reports plus the versioned review/claim ledger,
progress/TODO, verification outputs and any new references. Summarize:

- Baseline and new revision, research cutoff and review date.
- Major corrections and their effect on the platform recommendations.
- Scope actually reviewed, evidence strengthened and unresolved findings.
- Checks performed, exact failures and any unmet specification requirements.
- Files generated and baseline-preservation results.
- Readiness for shortlisting, procurement and deployment, assessed separately.

Qualify or remove unsupported conclusions rather than promoting them to fact.
Do not describe the review as complete if material claims were skipped or
required corrections/checks remain. Where accessible research is complete but
entitled evidence or deployment validation is pending, state those limits
precisely. Keep the original baseline available for comparison and rollback.
