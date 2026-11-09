# Storage Capability Comparison: VMware and Proxmox with Dell or NetApp

**Version:** r1.4.0 (initial capability comparison)  
**Research baseline:** 2026-11-08  
**Status:** First substantive comparison draft. Product-specific support still requires exact model/version confirmation and interoperability checks.  
**Purpose:** Compare capabilities for a three-server cluster using VMware or Proxmox VE with Dell or NetApp external storage. Cost is not a ranking criterion; entitlements and support requirements are included when they gate a capability.

## Table of contents

- [1. Decision to be made](#1-decision-to-be-made)
- [2. Scenario, boundaries, and terms](#2-scenario-boundaries-and-terms)
- [3. Requirements before products](#3-requirements-before-products)
  - [3.1 Workload profile](#31-workload-profile)
  - [3.2 Capacity model](#32-capacity-model)
  - [3.3 Performance objectives](#33-performance-objectives)
  - [3.4 Availability and recovery objectives](#34-availability-and-recovery-objectives)
  - [3.5 Three-server cluster baseline](#35-three-server-cluster-baseline)
  - [3.6 One array versus two arrays](#36-one-array-versus-two-arrays)
- [4. Failure scenarios and expected service](#4-failure-scenarios-and-expected-service)
- [5. Four reference designs](#5-four-reference-designs)
  - [5.1 VMware with Dell storage](#51-vmware-with-dell-storage)
  - [5.2 VMware with NetApp storage](#52-vmware-with-netapp-storage)
  - [5.3 Proxmox VE with Dell storage](#53-proxmox-ve-with-dell-storage)
  - [5.4 Proxmox VE with NetApp storage](#54-proxmox-ve-with-netapp-storage)
  - [5.5 Availability tier: one array or two](#55-availability-tier-one-array-or-two)
- [6. Hypervisor capability matrix](#6-hypervisor-capability-matrix)
  - [6.1 VMware editions and features](#61-vmware-editions-and-features)
  - [6.2 Proxmox storage backends and feature maturity](#62-proxmox-storage-backends-and-feature-maturity)
  - [6.3 Migration, HA restart, and maintenance](#63-migration-ha-restart-and-maintenance)
  - [6.4 Snapshots, backups, and granular recovery](#64-snapshots-backups-and-granular-recovery)
- [7. Array capability matrix](#7-array-capability-matrix)
  - [7.1 Dell family and reference model](#71-dell-family-and-reference-model)
  - [7.2 NetApp family and ONTAP personality](#72-netapp-family-and-ontap-personality)
  - [7.3 Protocols and host integration](#73-protocols-and-host-integration)
  - [7.4 Availability, data services, and recovery](#74-availability-data-services-and-recovery)
- [8. Host storage layout and filesystem layers](#8-host-storage-layout-and-filesystem-layers)
  - [8.1 VMware: VMFS and NFS](#81-vmware-vmfs-and-nfs)
  - [8.2 Proxmox: shared LVM and NFS](#82-proxmox-shared-lvm-and-nfs)
  - [8.3 Guest filesystems](#83-guest-filesystems)
- [9. Separate comparison: ZFS and Btrfs architectures](#9-separate-comparison-zfs-and-btrfs-architectures)
  - [9.1 Dedicated storage server or appliance](#91-dedicated-storage-server-or-appliance)
  - [9.2 Filesystem on a SAN LUN](#92-filesystem-on-a-san-lun)
  - [9.3 Guest filesystem](#93-guest-filesystem)
  - [9.4 Shared access, fencing, and failure domains](#94-shared-access-fencing-and-failure-domains)
- [10. Workload capability and acceptance testing](#10-workload-capability-and-acceptance-testing)
  - [10.1 VM and database activity](#101-vm-and-database-activity)
  - [10.2 Packet capture and security analytics](#102-packet-capture-and-security-analytics)
  - [10.3 Media options](#103-media-options)
  - [10.4 Common proof-of-concept tests](#104-common-proof-of-concept-tests)
- [11. Kubernetes and container storage](#11-kubernetes-and-container-storage)
- [12. Conditional findings](#12-conditional-findings)
- [13. Open inputs and verification gates](#13-open-inputs-and-verification-gates)
- [Appendix A: Filesystem and storage-layer notes](#appendix-a-filesystem-and-storage-layer-notes)
- [Appendix B: Source guides and version records](#appendix-b-source-guides-and-version-records)
- [Appendix C: Verification reference register](#appendix-c-verification-reference-register)
- [Appendix D: Acronyms and Terms](#appendix-d-acronyms-and-terms)
  - [Acronyms and abbreviations](#acronyms-and-abbreviations)
  - [Key terms](#key-terms)

## Comparison at a glance

| Design question | VMware | Proxmox VE |
| --- | --- | --- |
| Shared block SAN datastore | Supported through VMFS on compatible LUNs/namespaces and transports | Supported through shared LVM on compatible SAN block devices |
| Shared file datastore | Supported NFS datastore | Supported NFS backend |
| Planned VM migration | vMotion when compute, network, device, and entitlement prerequisites are met | Live migration when node compatibility and storage accessibility/prerequisites are met |
| Restart after one host fails | vSphere HA can restart eligible VMs if storage remains available and admission/resource conditions are met | HA manager can restart eligible guests if quorum, fencing, storage, and remaining-node capacity are available |
| Shared SAN VM snapshot position | Mature hypervisor snapshots for supported VMFS VMDKs; use short retention and monitor/consolidate deltas | Shared thick-LVM volume-chain snapshots exist in VE 9 but remain a technology preview in the documentation reviewed |
| Array-aware recovery | Depends on array and integration; SnapCenter VMware workflows exist for supported ONTAP combinations | Depends on array and integration; Dell PowerStore and NetApp publish Proxmox continuity workflows, each with exact prerequisites |
| vVols for new deployments | Deprecated in VCF/VVF 9.0; Broadcom says removal in VCF 9.1. Treat as legacy for a new 9.x design | Not applicable |

This is a capability map, not an overall winner. The table describes platform-level paths; exact support remains subject to the selected hardware, release, protocol, plugin, and entitlement. Section 6 gives the fuller matrix, and Appendix C records sources and the claims they support.

## 1. Decision to be made

Compare four ways to run the stated workloads on three clustered servers with shared external storage, then evaluate a second array as an optional availability tier:

| Hypervisor | Dell array | NetApp array |
| --- | --- | --- |
| VMware vSphere | VMware + Dell | VMware + NetApp |
| Proxmox VE | Proxmox + Dell | Proxmox + NetApp |

The comparison asks which combination provides the required data path, operational features, and recovery behavior. It must compare **complete, version-pinned designs**, not vendor names in isolation. The four primary pairings use a three-server compute cluster and one shared array; each is then assessed with a second, replicated array as a separate resilience tier. ZFS and Btrfs are assessed separately because they are filesystem/storage-stack choices, not peer hypervisor choices or turnkey shared-array backends.

The intended outcome is a capability matrix and conditional recommendation based on demonstrated requirements. No single winner should be named until the workload profile, recovery objectives, and exact product configurations are fixed.

## 2. Scenario, boundaries, and terms

The working baseline is three powerful physical servers in a cluster connected to one external shared array. Workloads include approximately 100 VMs, databases, shared files, backups, containers/Kubernetes, packet capture, Snort-like inspection, and Splunk-like indexing/search. An optional second array provides a distinct array-failure protection tier. The earlier 130 TB raw capacity estimate remains a planning reference and must specify whether it applies per array or across both. HDD, hybrid, SSD, and NVMe media are in scope. Cost is not a concern for ranking.

“Dell SAN” is not a sufficiently precise product description. Dell's product families expose different protocols and services. The final comparison must either select an exact family/model/software release or compare explicit categories with model-dependent claims marked unresolved. **PowerStore can be used as an initial Dell reference only if stated as an assumption; it must not stand in for PowerMax or all Dell storage.**

“NetApp” also requires a pinned family and personality. Unified ONTAP on AFF/FAS supports NAS and SAN. Classic ASA is SAN-only. ASA r2 is SAN-only with a different storage model. The report must not attribute a feature of one personality to all NetApp arrays. See [NetApp's ONTAP platform comparison](https://docs.netapp.com/us-en/asa-r2/learn-more/hardware-comparison.html).

Keep “array capability” separate from “hypervisor capability.” The array presents block or file storage and may provide controller failover, snapshots, replication, and management integrations. The hypervisor formats or consumes the presented storage, manages VM disks, performs migration, and restarts VMs after host loss. The exact support boundary depends on versions, hardware, plugins, and contracts.

Cost does not determine the ranking. However, a capability that requires a particular VMware edition, subscription, NetApp license, integration product, or support agreement must be identified as **entitlement-dependent**. Do not assume that technical possibility means supported entitlement.

## 3. Requirements before products

Record measurable requirements before filling in vendor comparisons. If a value is unknown, carry a labeled scenario range through the evaluation instead of silently assuming one.

### 3.1 Workload profile

Separate occupied capacity and I/O for VM disks, databases, file shares, backups, containers, packet captures, inspection logs, and Splunk indexes. Record VM count and footprint distributions, not only the 100-VM average. Identify which systems are latency-sensitive and which can be restarted or restored later.

### 3.2 Capacity model

The baseline is **130 decimal TB raw installed capacity**. Show the protected usable capacity after the chosen layout, then subtract system overhead, required free-space/rebuild reserve, snapshots, and backup allocation to estimate space for live workloads. A second replicated array does not double unique workload capacity: it holds another protected copy. The unresolved detail is whether 130 TB raw refers to each array or the total raw media across the pair. Use decimal TB for drive-market figures and show TiB conversions where useful. Do not count data-reduction savings unless measured on representative data.

Produce two capacity views: (1) equal raw media for comparing efficiency and (2) equal usable workload capacity for comparing the hardware needed to satisfy the requirement. Neither view alone captures performance or failure behavior.

### 3.3 Performance objectives

For each workload define sustained and peak throughput, random IOPS, block-size mix, read/write mix, queue depth/concurrency, and acceptable p95/p99 latency. For capture and indexing, record retained ingest rate, search concurrency, and retention. Report performance at expected occupancy and with caches saturated, not only short burst results.

### 3.4 Availability and recovery objectives

Set separate objectives for planned migration, server failure, storage-controller failure, array-wide failure, accidental deletion, application corruption, and site loss. Specify interruption and data-loss limits per workload. Define what “recovered” means: storage path online, VM booted, database consistent, service healthy, or user traffic restored.

### 3.5 Three-server cluster baseline

Use three full compute nodes as the reference baseline. Define the required service level after losing one node and size the two survivors for CPU, memory, network, and device needs. State reservations and any lower-priority workloads that may be paused. The third node improves quorum and gives another placement target; it does not guarantee that two nodes can carry the full workload.

For Proxmox, upstream guidance recommends at least three nodes for reliable HA quorum, matching node versions, and resilient low-latency Corosync networking. A third node provides a vote and placement target; it does not guarantee two nodes have enough CPU/RAM for the required workload. For VMware, specify vCenter, vSphere HA admission control, and the capacity policy. In both cases, planned maintenance while preserving N+1 protection must be evaluated separately from recovery after a single failure. Do not claim VMware HA inherently requires three hosts; three is this design's chosen baseline.

### 3.6 One array versus two arrays

**One array** means one storage system with its configured internal redundancy. It can address supported drive, controller, and path failures, but array-wide outage remains a shared failure domain.

**Two arrays** means two separate storage systems with a documented protection relationship and a defined host failover procedure. Compare two distinct layouts: (1) both arrays in one site for array/device failure, and (2) arrays in separate sites for site recovery. State whether the systems are the same model/family, which one serves writes, whether replication is synchronous or asynchronous, the RPO/RTO, and how hosts discover and access the surviving copy. Place a witness/mediator in a third failure domain when required. This witness is a separate service; do not count it as one of the compute servers unless the supported design explicitly does so.

Do not assume that a second array alone provides automatic failover or zero data loss. Replication can copy deletion or corruption; pair it with independent, recoverable backup points. If cross-vendor replication (for example Dell to NetApp) is proposed, verify that the exact models and software support the intended relationship and recovery process. Otherwise compare matched array pairs within each vendor column.

As a model-specific example, NetApp SnapMirror active sync requires supported ONTAP configurations and a mediator for automated unplanned failover; its network, protocol, and model prerequisites are version dependent. [SnapMirror active sync prerequisites](https://docs.netapp.com/us-en/ontap/snapmirror-active-sync/prerequisites-reference.html). This is an example of a capability to verify, not an assumption that equivalent Dell behavior uses the same design.

## 4. Failure scenarios and expected service

Use one matrix for all four reference designs. For every event, record: data availability; affected workloads; automatic versus manual action; interruption; risk of data loss; dependencies; and proof-of-concept evidence. For a two-site design, model compute quorum, storage quorum, mediator placement, and host-to-array paths together: surviving storage alone does not preserve service if the surviving compute partition cannot form quorum or run the VMs.

| Event to test | Questions to answer |
| --- | --- |
| One compute server fails | Can the two surviving hosts run the required VM set? Which VMs restart, and how long until applications are ready? |
| One server is in maintenance | Can planned work proceed on two hosts while retaining the stated failure protection? Which services lose redundancy? |
| One storage path, switch, or fabric fails | Do hosts continue I/O over independent paths? Are multipathing and network failover configured end to end? |
| One array controller fails | Does the partner continue serving data? What changes in path state and performance? |
| Drive/shelf failure or rebuild | Does data remain available? What latency and throughput degradation occurs during repair? |
| Entire array or array software is unavailable | With one array, what independent copy can restore service? With two arrays, does replication preserve the required data and can hosts fail over safely? |
| Replication link or mediator/witness fails | Does I/O continue, pause, or run without protection? Is automatic failover still safe? |
| Deletion, ransomware, or application corruption | Are clean recovery points retained outside the compromised failure domain? Can one VM/application be recovered without rolling back unrelated data? |
| Replicated deletion or corruption | Can a clean point-in-time copy be recovered without promoting the corrupted replica? |
| Site/network loss | Is this a single-site array pair or stretched design? Can the surviving compute and storage quorums agree on one active site, and what consistency/RPO/failover procedure applies? |

Do not describe controller takeover as VM failover, snapshots as backups, live migration as host-failure recovery, or quorum as compute capacity.

## 5. Four reference designs

Before populating these sections, record exact product/version assumptions. Each design uses the same three-server compute cluster, workload, failure scenarios, data set, and test procedure. First compare it with one array; then add a second array from the same vendor family as a distinct replication/failover tier. If the chosen array offers both block and file services, compare the relevant access paths as alternatives inside that design. Keep the primary 2 × 2 matrix intact; array count is a second comparison dimension.

Each reference design will state:

- Three-server cluster configuration, quorum, surviving-host capacity, and workload placement after one host fails.
- For the one-array tier: array model, controller configuration, drives, firmware/OS, and usable capacity.
- For the two-array tier: both array models, replication relationship, mediator/witness, usable capacity at each site, and how hosts access each copy.
- Host protocol, switches/fabrics, adapters, multipath configuration, and datastore backend.
- Snapshot, replication, backup, and application-integration products and versions.
- Supported operations, known limits, failure behavior, and test evidence.

### 5.1 VMware with Dell storage

For a concrete unified-array example, use **Dell PowerStore** as a provisional reference, while retaining PowerMax as a separate candidate if the intended purchase is a high-end block-only system. Dell documents PowerStore VMFS on block storage and NFS datastores. The exact model, PowerStoreOS release, protocols, VMware build, and interoperability entries must be pinned. PowerStore is an all-flash family; do not use it as evidence for Dell HDD/hybrid options. [Dell PowerStore VMware best practices](https://infohub.delltechnologies.com/en-au/t/dell-powerstore-vmware-vsphere-best-practices-2/).

For a one-array layout, compare VMFS on supported block paths with NFS 4.1 unless a requirement selects another NFS version. For two arrays, Dell PowerStore Metro Volumes are a documented synchronous block design with Metro Witness; failover depends on the selected uniform/non-uniform host connectivity, witness state, and PowerStoreOS. Dell also publishes a Proxmox Metro Volumes example; do not transfer its Proxmox configuration details to ESXi without checking the VMware-specific guide. [Dell Metro Volume overview](https://www.dell.com/en-us/infohub/articles/dell-powerstore-metro-volume-1).

### 5.2 VMware with NetApp storage

Use **unified ONTAP on AFF** as the all-flash mixed-protocol reference. If HDD/hybrid capacity is required, evaluate FAS as a separate media/platform variant. Compare SAN protocols on VMFS against NFS only for NAS-capable unified ONTAP; classic ASA and ASA r2 are SAN-only. NetApp's documented VMware paths include FC, iSCSI, NVMe/FC, NVMe/TCP, NFSv3, and NFSv4.1, subject to the exact system and release. [ONTAP VMware datastore protocol overview](https://docs.netapp.com/us-en/ontap-apps-dbs/vmware/vmware-vsphere-datastores-top.html).

Use ONTAP snapshots for array-level recovery and SnapCenter/compatible VMware tooling when application coordination or VM-granular restore is required. For a second array, compare the exact SnapMirror active sync or other supported design, including mediator and host behavior. A snapshot of a VMFS LUN may contain multiple VMs; it is not inherently a single-VM restore point.

### 5.3 Proxmox VE with Dell storage

Compare shared LVM on supported SAN block devices with NFS. Dell publishes a three-host Proxmox VE + PowerStore Metro Volumes implementation using two PowerStore 5200T systems, iSCSI multipathing, shared LVM, and a witness. Its example pins Proxmox VE 8.3.0 and PowerStoreOS 4.1; use it as a vendor-documented example, not blanket support for Proxmox VE 9, other PowerStore models, or other Dell families. Verify the exact stack with Dell and Proxmox before relying on it. [Dell Proxmox Metro Volumes guide](https://www.dell.com/en-us/infohub/articles/proxmox-with-dell-powerstore-metro-volumes).

For NFS, record supported VM/container content types and the chosen disk image format. Shared-LVM volume-chain snapshots remain a preview in the Proxmox documentation reviewed; that does **not** mean online VM backup is unavailable. Proxmox live VM backup uses its backup mechanism and guest-agent freeze/thaw where configured. Validate backup and restore separately from VM snapshot capability.

### 5.4 Proxmox VE with NetApp storage

Compare NFS with shared LVM on supported block protocols, with each transport and plugin pinned to the exact Proxmox/ONTAP combination. NetApp publishes Storage Manager for Proxmox workflows and business-continuity designs. The continuity guide requires the exact ONTAP, MetroCluster or SnapMirror active sync, mediator, and Proxmox versions to appear together in the NetApp Interoperability Matrix Tool. It includes multi-site designs whose Corosync, QDevice, storage paths, and site placement are coordinated; do not infer that three nodes in one site provide the same site-failure behavior. [NetApp Proxmox business continuity](https://docs.netapp.com/us-en/netapp-solutions-virtualization/proxmox/proxmox-business-continuity.html).

Record restore scope and consistency by backend. NetApp's current Storage Manager for Proxmox documentation describes differences between NFS and iSCSI workflows; for example, iSCSI backups are crash-consistent and storage-level restore can affect all VMs on the volume/LUN. Verify current release behavior before making this a product ranking claim. [NetApp Storage Manager for Proxmox](https://docs.netapp.com/us-en/netapp-solutions-virtualization/proxmox/proxmox-smp.html).

### 5.5 Availability tier: one array or two

For each of the four pairings, first document one array with its internal drive, controller, and path protections. Then add a second array, preferably a matched model/family pair, with the supported replication and failover mechanism. Compare asynchronous replication, synchronous replication, or active/active only where the exact product and host combination supports it. Record the witness/mediator, replication network, consistency groups, host mappings, failover/failback steps, RPO/RTO, and degraded-mode performance.

| Availability tier | What it protects | What must also be present |
| --- | --- | --- |
| Three compute hosts + one HA array | Host, path, controller, and protected drive failures within the array's supported design | Two surviving hosts with enough capacity after one host fails; independent backup for array-wide loss |
| Three compute hosts + two arrays in one site | Array failure where synchronous replication and host access/failover are supported | Independent witness/mediator where required; separate power/network failure domains; preserve backup points |
| Compute and arrays split across sites | Site failure only if compute quorum, storage quorum, host paths, and application placement all survive coherently | Site-aware cluster design, inter-site network, witness in a third failure domain, sufficient compute at surviving site, tested RPO/RTO |

Treat the second array as a separate failure-domain option, not as a fifth hypervisor pairing. A remote replica alone does not make the compute cluster site-resilient. For example, a three-voter Proxmox cluster split 2+1 can lose quorum if the two-node site fails. Do not assume cross-vendor replication is supported or transparent. If Dell-to-NetApp replication is of interest, make it a separate explicitly verified design and identify which vendor owns support for the complete path.

## 6. Hypervisor capability matrix

The matrix below describes broad platform capabilities, not certification of the proposed system. Dell and NetApp support depends on the exact array model, firmware, host build, protocol, and integration software. Proxmox source references are moving upstream documentation; confirm the released manual and support position for the chosen VE version.

| Capability | VMware vSphere | Proxmox VE | Design implication |
| --- | --- | --- | --- |
| Shared block SAN datastore | VMFS on supported FC/iSCSI/NVMe-oF devices | Shared LVM on supported SAN LUNs; configure multipath on every node | Both can use shared block storage; Proxmox backend/content behavior differs from VMFS |
| Shared NFS datastore | Supported NFS datastores; version and array support matter | NFS backend is shared; supported content/image formats matter | NFS is a file-service path, not VMFS on a LUN |
| VM snapshots on shared block | Established VMFS/VMDK delta snapshots for supported disk modes | Thick shared-LVM volume-chain snapshots are currently marked technology preview | Snapshot maturity differs; do not equate array snapshots to VM-aware snapshots |
| VM snapshots on NFS | Supported VM configurations; delta growth/consolidation still needs monitoring | qcow2 can provide VM snapshots; snapshot operations can be slow/blocking on network storage | Verify image format and snapshot operation under expected write load |
| Planned live migration | vMotion for eligible VMs; shared datastore avoids disk copy | Live migration for compatible nodes; shared storage avoids disk copy | CPU vendor/feature compatibility, network, devices, and destination capacity still apply |
| Storage migration | Storage vMotion for eligible configs and entitlements | Storage migration for supported source/destination backends | Separate from compute-only migration; verify snapshots/device restrictions |
| HA restart after host failure | vSphere HA can restart eligible VMs on remaining hosts if admission control/resources/storage allow | HA manager can restart eligible guests if quorum, fencing, storage, network, and node eligibility allow | Planned migration is not failure recovery; application restart time must be measured |
| Local ZFS backend | No native ESXi ZFS datastore management | Available as local storage; not shared by default | Local ZFS needs separate replication or shared-storage architecture |
| Local Btrfs backend | No native ESXi Btrfs datastore management | Available but still marked technology preview in current storage matrix | Do not base primary availability design on the preview without explicit acceptance |
| vVols | Deprecated in VCF/VVF 9.0; Broadcom states removal in VCF 9.1 | Not applicable | Treat as a legacy migration path, not a preferred new 9.x baseline |
| VM backup | Through supported backup products and APIs | Proxmox live VM backup is available independently of shared-LVM snapshot support; PBS is integrated option | Backup/restore capability must be tested separately from VM snapshot support |

Status labels in the completed support matrix: **documented**, **documented with prerequisites**, **preview**, **unsupported**, **not verified**. Add exact release, source, and interoperability result to every model-specific assertion. VMware entitlement remains a gate where the feature/operation is edition-dependent.

### 6.1 VMware editions and features

Pin the VMware offering, vCenter/ESXi versions, and support entitlement. Map only capabilities relevant to external storage: VMFS, NFS, vMotion, Storage vMotion, HA, backup APIs/integrations, and optional data services. vVols are now a legacy topic: Broadcom deprecated vVols and VASA capabilities beginning in VCF/VVF 9.0 and discontinued new 9.0 certifications; Broadcom documentation says removal in VCF 9.1. Verify the final lifecycle statement against release-specific documentation. Keep vSAN separate; it consumes host storage devices and is not one of the four external-array pairings. [Broadcom vVol deprecation notice](https://knowledge.broadcom.com/external/article/401070), [removal notice](https://knowledge.broadcom.com/external/article/407058).

### 6.2 Proxmox storage backends and feature maturity

The current Proxmox storage matrix lists shared NFS, shared LVM on SAN block storage, local ZFS, and local Btrfs as different backends (sources checked 2026-11-08). It marks Btrfs as technology preview. Proxmox VE 9 introduced the shared-LVM volume-chain snapshot option; Proxmox documentation explicitly labeled it a technology preview in a documentation patch announced on 2025-08-29, and the current documentation still labels it preview. No published stable-release date or commitment was found in the sources checked, so this comparison does not estimate when it may leave preview. This preview concerns that VM snapshot mechanism; Proxmox live VM backup is a separate capability. NFS snapshot/clone behavior depends on qcow2; Proxmox warns that snapshot creation/deletion can block a running VM and be slow on network storage. Recheck the released VE guide at publication. [Storage matrix](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc), [LVM backend](https://github.com/proxmox/pve-docs/blob/master/pve-storage-lvm.adoc), [NFS backend](https://github.com/proxmox/pve-docs/blob/master/pve-storage-nfs.adoc), [backup/restore](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc).

### 6.3 Migration, HA restart, and maintenance

Compare online VM migration when storage is shared, VM migration when storage must also move, automatic restart after host loss, and maintenance of one host while two hosts carry the workload. State which operations need common CPU compatibility, sufficient destination resources, supported device state, and additional entitlement. Test the combined case of one host already in maintenance plus another host failure; N+1 capacity only promises to tolerate one host failure from the normal three-host state.

### 6.4 Snapshots, backups, and granular recovery

| Mechanism | VMware | Proxmox VE | Array contribution |
| --- | --- | --- | --- |
| Hypervisor VM snapshot | Delta disks on supported VMDKs/datastores; useful as a short-term checkpoint, not a backup | Backend-dependent; shared thick-LVM volume chains remain preview; NFS/qcow2 behavior differs from raw/shared LVM | Array can provide low-level snapshots, but it does not change hypervisor snapshot semantics |
| Array snapshot | Possible on both Dell and NetApp arrays; consistency depends on host/application integration | Possible on both array families; exact VM/application integration differs | Provides array-level point-in-time state; shared LUN snapshot may cover multiple guests |
| Application-consistent capture | Guest quiescing or vendor/application integration, with supported guest tools | Guest-agent/application integration or supported storage manager workflow | AppSync/SnapCenter and other tools may coordinate selected supported workloads |
| Independent backup | Compatible backup product/API and target required | Proxmox Backup Server or compatible product/target; verify VM/container restore behavior | A second array replica is not an independent backup if it mirrors unwanted changes |

For each method, record scope, consistency, maturity, retention, space behavior, and restore granularity. Demonstrate one-VM restore from a shared datastore without rolling back unrelated VMs. Also restore with the primary array unavailable, including recovery of backup catalogs and management dependencies.

## 7. Array capability matrix

The array matrix is separate from the hypervisor matrix. This first-pass matrix uses PowerStore as a Dell reference and unified ONTAP/AFF as a NetApp reference. These products are not the entire Dell or NetApp catalog. Verify every cell against the exact product family, model, release, and host combination.

| Capability | Dell PowerStore reference | NetApp ONTAP reference | Scope/caveat |
| --- | --- | --- | --- |
| Block VM storage | PowerStore volumes over supported FC/iSCSI/NVMe-oF; VMware VMFS and Proxmox shared-LVM examples exist | ONTAP LUNs/namespaces over supported FC/iSCSI/NVMe-oF; VMFS for VMware, shared LVM paths documented for Proxmox | Protocol support and array model must match host release and adapter configuration |
| File VM storage | NFS file service, including VMware NFS datastore guidance | Unified ONTAP provides NFS; classic ASA and ASA r2 are SAN-only | NFS is not available on every NetApp personality or Dell product family |
| Controller availability | Dual-controller appliance design; host multipathing and model-specific failover handling required | HA pair takeover/giveback and host path failover, depending on protocol/platform | Controller HA does not protect array-wide or site-wide loss |
| Local array snapshots | PowerStore snapshots/clones; crash consistency unless application coordination is used | ONTAP volume snapshots, with file/LUN recovery capability | Snapshot object scope and application consistency differ; test granular restore |
| Application/VM integration | Dell AppSync and VMware integrations for selected supported workloads | SnapCenter for VMware and applications on selected supported combinations | Do not score basic snapshots as application-consistent backup |
| Two-array protection | PowerStore Metro Volumes provide a synchronous block design with witness; PowerStoreOS and host connectivity constrain behavior | SnapMirror active sync or MetroCluster options depend on platform/personality, protocol, ONTAP version, mediator/tiebreaker, and topology | These are different implementations; compare actual failure outcomes, not feature names |
| Proxmox-specific continuity evidence | Dell publishes a three-host, two-PowerStore Metro Volumes example using iSCSI/shared LVM and witness | NetApp publishes Proxmox business-continuity designs and requires exact stack validation in IMT | Vendor solutions guide examples are not universal certifications |
| Media choice | PowerStore reference is all-flash; use a separate Dell family for HDD/hybrid | AFF is all-flash; FAS is a distinct hybrid option | Do not compare media types as if selectable within one model |
| Efficiency/QoS/management | Available features depend on PowerStoreOS/model and configuration | ONTAP data services vary by personality and release | Record feature, entitlement, and failure behavior rather than broad vendor claims |

This first-pass matrix establishes useful candidates, not exact compatibility. If the intended Dell system is PowerMax rather than PowerStore, rework the Dell column around PowerMax-specific protocols, integration, and Metro configuration. If NetApp is intended to be SAN-only, replace unified AFF with ASA/ASA r2 and remove NFS claims.

Describe what happens during failure, not just whether a feature appears in a product list. Separate array-local protection from second-array or second-site protection.

### 7.1 Dell family and reference model

PowerStore is the provisional Dell reference because it offers both block and file services and has published VMware and Proxmox integration guidance. It is not the assumed purchase. Pin its exact model and PowerStoreOS version. PowerStore is flash-based; if HDD or hybrid capacity is a core requirement, compare a different Dell family as a separate design rather than implying PowerStore can be configured with spinners. PowerMax is a plausible block-focused alternative and needs its own matrix.

### 7.2 NetApp family and ONTAP personality

Use unified ONTAP on AFF as the provisional all-flash reference. Add FAS as a distinct HDD/hybrid variant if capacity media matter. Distinguish classic ASA and ASA r2 as SAN-only variants; ASA r2 also uses storage availability zones rather than the aggregate model used by AFF/FAS/classic ASA. Record NAS availability, SAN transports, provisioning, replication and recovery workflows by exact model and ONTAP release.

### 7.3 Protocols and host integration

Compare protocol paths only when supported by both the exact array and host release. Record independent adapters/switches, multipathing, failover state, zoning/networking, and the host plugin or integration tools. Ethernet bonding is not a substitute for block multipathing.

### 7.4 Availability, data services, and recovery

Compare takeover and giveback, performance headroom during takeover, snapshots, replication, application integrations, and restore granularity. For the second-array tier, specify sync mode, mediator/witness requirements, distance/latency limits, quorum behavior, host path changes, failover/failback, and out-of-sync behavior. Identify whether a snapshot covers a VM disk, datastore, LUN, volume, or consistency group. Do not imply that array snapshots alone produce application-consistent or single-VM recovery.

## 8. Host storage layout and filesystem layers

Show what each hypervisor actually consumes. The term “filesystem on the SAN” is too vague: block arrays present LUNs/namespaces, while NFS arrays present exported files. The array also has internal data structures that are not the same as a host datastore filesystem.

### 8.1 VMware: VMFS and NFS

For block storage, show a supported LUN/namespace formatted as VMFS for shared VM datastores. For NFS, show the array export mounted as a VMware datastore without VMFS formatting on the host. Record guest filesystems as a separate layer. Validate any vVol use against the pinned array and VMware releases.

### 8.2 Proxmox: shared LVM and NFS

For SAN block devices, show multipathed LUNs managed as shared LVM for VM disks; this is block-volume management, not a shared directory filesystem. For NFS, show the shared file datastore and its content/image-format limits. Record snapshot maturity and backup behavior by release/backend.

### 8.3 Guest filesystems

NTFS, ext4, XFS, ZFS, Btrfs, or database-specific layouts inside a guest are guest/application design choices. They do not replace the hypervisor datastore or array's internal storage layer.

## 9. Separate comparison: ZFS and Btrfs architectures

Do not insert ZFS/Btrfs as if they were another hypervisor or another SAN vendor. Compare them separately as complete storage designs or guest filesystems. The comparison below evaluates the storage architecture needed to meet the same shared access, failover, capacity, and recovery objectives.

| Role | What must be compared | Key limitation to make explicit |
| --- | --- | --- |
| Dedicated storage server/appliance | Directly visible disks, ZFS/Btrfs layout, export protocol, dual-server/HA design, fencing, support, backup | A single server is a service failure domain; filesystem redundancy does not add compute or controller failover |
| Filesystem on one SAN LUN | Single owning host, filesystem features, LUN/array protection overlap, recovery and failover process | Not a concurrently mounted shared datastore for both cluster servers |
| Guest filesystem | Guest data services, application consistency, backup, performance | Does not provide shared hypervisor storage or array management |

### 9.1 Dedicated storage server or appliance

| Architecture | Capability profile | Comparison with an enterprise array |
| --- | --- | --- |
| ZFS server exporting NFS or iSCSI | Checksums, snapshots, replication, and flexible vdev layouts; NFS can be consumed as a shared datastore | Can provide strong data integrity and useful recovery features, but requires a separately engineered and supported server HA, controller, path, and failover design |
| Btrfs server exporting NFS or iSCSI | Checksums, snapshots, send/receive, and flexible filesystem management | Same service-availability caveat; verify RAID/profile and workload limitations for the exact kernel and tools |
| Enterprise Dell or NetApp array | Integrated controllers, supported host protocols, array management, and vendor-defined replication/failover features | Provides an integrated storage service; exact behavior, data services, and support still depend on model and release |

Specify who owns physical disks and redundancy, how storage is exported, how the service fails over, and how the hypervisors reconnect. Compare against array-controller availability using the same failure test. Distinguish a self-built server from a supported HA appliance. ZFS or Btrfs alone does not provide a redundant head node or transparent storage service failover.

### 9.2 Filesystem on a SAN LUN

This can add host-visible checksums and filesystem snapshots on top of array-protected block storage, but also adds a filesystem layer and its capacity/operational overhead. It retains the array's controller, media, and site failure domains. Use one owner at a time; require fencing and tested ownership transfer before claiming service failover. For VM datastores, compare this single-owner approach with VMFS, shared LVM, or NFS designed for multi-host access.

### 9.3 Guest filesystem

Include only where guest application behavior or portability makes ZFS/Btrfs relevant. Identify the guest's virtual-disk backing, guest-level redundancy assumptions, and application-aware backup path.

### 9.4 Shared access, fencing, and failure domains

Ordinary ZFS and Btrfs filesystems do not become cluster filesystems because their backing LUN is shared. Never compare simultaneous read/write mounting as a normal configuration. Any single-owner failover design must prevent dual ownership and be tested through fencing, failover, and recovery. Compare all architectures across disk/media failure, server/head failure, path/switch failure, array/controller failure, site loss, corruption, and backup restore.

## 10. Workload capability and acceptance testing

Use the same representative data set, virtual-machine mix, concurrency, retention, and test sequence for every reference design. Establish pass/fail targets before running tests. Vendor benchmark claims are context, not substitutes for tests on the proposed configuration.

### 10.1 VM and database activity

Test mixed small random I/O, synchronous writes, database checkpoints, boot storms, snapshots, backup, and migration concurrently. Capture guest/application latency and host/array queueing.

### 10.2 Packet capture and security analytics

Measure average/peak retained capture rate, capture drops, packet size distribution, filtering, retention, and write concurrency. Separately measure Snort/log output and Splunk ingest/index/search. Account for application replication and retained backups. A 10 Gb network link is not a statement that 10 Gb/s of packet data is written continuously.

Use `decimal TB/day ≈ retained Gbit/s × 10.8` before overhead/compression. Examples:

| Average retained rate | Raw retained data per day | Days for a 30 TB capture allocation |
| --- | ---: | ---: |
| 100 Mbit/s | 1.08 TB | 27.8 days |
| 500 Mbit/s | 5.40 TB | 5.6 days |
| 1 Gbit/s | 10.80 TB | 2.8 days |
| 10 Gbit/s | 108.00 TB | 6.7 hours |

These are raw arithmetic examples, not forecasts. Size retention, protection, snapshots, and independent backup separately. For Splunk, use measured daily ingest, retention, searchable/raw data size, and replication/search factors instead of assuming one compression ratio. Test sustained writes beyond cache, simultaneous searches, normal VM I/O, and degraded array/server operation.

### 10.3 Media options

Compare HDD, hybrid, SATA/SAS SSD, and NVMe only within configurations supported by the chosen product. Evaluate capacity, endurance, sustained writes, latency under mixed load, rebuild effect, and performance during controller takeover. Media type alone does not identify host protocol.

### 10.4 Common proof-of-concept tests

| Test | Measurements and pass condition |
| --- | --- |
| Normal mixed workload | Throughput, p95/p99 latency, queue depth, packet drops, application health |
| Cache-saturated steady state | Sustained results after short-term cache advantage is exhausted |
| Single path/switch failure | I/O continuity, pauses, error recovery, and path-state evidence |
| Storage controller takeover | Application impact, latency, throughput, and return-to-normal behavior |
| One compute host failure | Time to restart and application readiness; surviving host CPU/RAM capacity |
| Host in maintenance plus another host failure | Quorum outcome, workload set remaining, and whether HA guarantees are intentionally relaxed |
| Disk rebuild/resilver | Duration and foreground workload impact |
| Snapshot and expiration | Creation, growth, deletion/consolidation, free-space recovery |
| Single-VM/application restore | Restore correctness without reverting unrelated workloads |
| Primary array unavailable, one-array design | Recovery from independent copy and time to restore service |
| Array unavailable, two-array design | Failover time, data currency/RPO, path recovery, application readiness, and return/failback procedure |
| Replication or mediator interruption | Data protection state, application I/O behavior, alerts, and safe recovery when connectivity returns |
| Controller failure during replication outage | Whether paths remain available, which copy can serve writes, and how split-brain is prevented |
| Corruption/deletion replicated to secondary | Ability to select a clean earlier recovery point and restore only intended workloads |
| Stale array returns | Resynchronization/failback behavior, host path state, and prevention of stale writes |
| Management/backup services after array loss | Whether control plane, credentials, catalogs, and independent backup remain reachable |
| Planned maintenance | What continues, what loses redundancy, and whether workloads must stop |

## 11. Kubernetes and container storage

Identify whether Kubernetes workers are VMs, bare metal, or both. Compare storage provisioned through the hypervisor with storage provisioned directly through CSI. Pin Kubernetes and CSI versions, supported access modes, block/file semantics, topology, and recovery owner for Dell and NetApp. Do not infer CSI support from array protocol support alone. Include persistent data restore and worker-node failure tests.

## 12. Conditional findings

These are conditional findings from the current evidence, not a final product selection:

- VMware with Dell or NetApp is a strong candidate where the organization needs VMware's mature VMFS-based shared-storage workflows, vMotion/HA operations, and established backup integrations. Choose the array only after pinning model, protocol, release, and recovery integration.
- Proxmox VE with Dell or NetApp is a viable candidate for shared NFS or supported shared-LVM SAN designs. Shared-LVM volume-chain VM snapshots remain preview in the documentation reviewed; live backup remains a separate supported workflow. Require a proof of concept for the exact storage backend and restore granularity.
- A second array adds array-failure protection only when replication, host connectivity, quorum/witness, and failover behavior are supported together. It does not replace an independent backup or solve compute-site failure by itself.
- A stretched two-site Proxmox design needs coordinated compute and storage quorum and a witness/mediator in a third failure domain. Three voters split 2+1 do not preserve quorum if the two-node site is lost.
- ZFS and Btrfs are appropriate to compare as guest filesystems or as complete storage-server designs. They are not a safe shared SAN filesystem simply by placing them on a shared LUN.

Do not give a general-purpose vendor winner. The best fit remains conditional on workload measurements, exact compatibility, and demonstrated recovery outcomes.

## 13. Open inputs and verification gates

Before completing product matrices, resolve or bound:

| Input | Needed for |
| --- | --- |
| Exact Dell family/model and software release | Protocol, data services, integrations, and support claims |
| NetApp family/personality, model, and ONTAP release | Unified NAS/SAN versus SAN-only capabilities and workflow limits |
| Whether the second array is a matched same-vendor pair or cross-vendor | Replication support, compatibility, failover orchestration, and support ownership |
| Array locations and replication-link latency/bandwidth | Synchronous/asynchronous feasibility, RPO, and site-failure behavior |
| Witness/mediator placement | Safe automatic failover and independent failure-domain requirements |
| Whether 130 TB raw is per array or total across the pair | Protected usable capacity, replica sizing, backup space, and growth |
| VMware release/edition and vCenter design | Feature and entitlement availability |
| Proxmox VE release and subscription/support assumptions | Backend maturity, snapshots, cluster support |
| Three-server CPU/RAM, adapters, firmware, and device passthrough | Migration compatibility and N+1 compute feasibility after losing one host |
| Switch/fabric speeds and redundant topology | Path design, throughput, and failure isolation |
| Actual VM/storage footprint and growth | Usable capacity sizing |
| Capture and Splunk ingest/retention/search rates | Capacity and sustained performance |
| RPO/RTO/service interruption per workload | Protection and recovery architecture |
| Kubernetes versions and CSI/storage requirements | Provisioning and persistent-data support |
| Independent backup destination and scope | Array-loss and corruption recovery |

For each claim, retain the exact official documentation and compatibility-matrix result for the selected versions. Label claims as vendor-documented, tested in the proof of concept, inferred, or unresolved.

## Appendix A: Filesystem and storage-layer notes

### A.1 “Filesystem on the SAN” can mean different layers

A block SAN generally presents a LUN or namespace. VMware commonly places VMFS on a supported block device; Proxmox can use shared LVM over a supported SAN device. These are host/hypervisor storage layers. With NFS, the array exports a filesystem and the hypervisor mounts the share as a datastore; the host does not format the export with VMFS.

The array has its own internal data layout. Unified NetApp ONTAP on AFF/FAS uses WAFL internally and can present LUNs, NVMe namespaces, and file shares. The host may then place VMFS on an ONTAP LUN. Those are two different layers. Dell arrays also have internal storage implementations; describe them only for the selected Dell family and software release.

### A.2 ZFS/Btrfs over a SAN LUN is a single-owner design

Putting ZFS or Btrfs on a SAN LUN does not make the filesystem safe for both cluster hosts to mount read/write concurrently. A single host can own the LUN and filesystem, but failover requires exclusive ownership, fencing, and recovery procedures. This is not equivalent to VMFS, shared LVM, or NFS used as a supported cluster datastore.

### A.3 Protection mechanisms cover different failures

Array redundancy, controller failover, array snapshots, host VM snapshots, guest/filesystem checksums, application-aware backups, replication, and independent backups protect different layers. A snapshot of a shared datastore may contain many workloads; a datastore/LUN rollback can revert unrelated VMs. Replication can faithfully copy unwanted changes, so it is not a substitute for retained recovery points or independent backup. Require a granular recovery demonstration.

Checksums can detect corruption only within the data visible to that layer. Repair requires an accessible valid copy. Two LUNs from one array may still share controllers, shelves, software, and site failure domains.

## Appendix B: Source guides and version records

Repository background guides:

- [Btrfs Administration Reference r1.2.4](README-BTRFS-Guide_r1.2.4.md)
- [NetApp ONTAP Guide r1.0.1](README-NetApp-Guide_r1.0.1.md) (proposed guide outline)
- [VMware Virtualization and Storage](README-vmware-storage.md)
- [ZFS Guide r1.0.1](README-ZFS-Guide_r1.0.1.md)

Initial primary references:

- [Proxmox storage backends](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc) and [shared LVM snapshots](https://github.com/proxmox/pve-docs/blob/master/pve-storage-lvm.adoc).
- [Proxmox VE cluster guide](https://pve.proxmox.com/pve-docs/pve-admin-guide.html), including QDevice guidance for small clusters.
- [Broadcom vSphere HA admission-control guidance](https://knowledge.broadcom.com/external/article/396016).
- [Dell PowerStore VMware best practices](https://infohub.delltechnologies.com/en-au/t/dell-powerstore-vmware-vsphere-best-practices-2/) (PowerStore-specific; do not generalize to other Dell families).
- [NetApp ONTAP platform/personality comparison](https://docs.netapp.com/us-en/asa-r2/learn-more/hardware-comparison.html).
- [NetApp VMware datastore protocols](https://docs.netapp.com/us-en/ontap-apps-dbs/vmware/vmware-vsphere-datastores-top.html).
- [NetApp SnapMirror active sync prerequisites](https://docs.netapp.com/us-en/ontap/snapmirror-active-sync/prerequisites-reference.html) and [architecture](https://docs.netapp.com/us-en/ontap/snapmirror-active-sync/architecture-concept.html) (NetApp-specific example; verify the selected model and release).

These links are starting evidence, not a completed compatibility audit. At publication, record exact hardware, software, protocol, plugin/driver, and entitlement versions. Distinguish current product documentation from the local guides' dated or planned content.


## Appendix C: Verification reference register

Use this register to trace claims to authoritative material and revisit them when product versions change. The upstream Proxmox links below point to moving documentation; the research check date is 2026-11-08. Record the selected release's archived/manual version and Interoperability Matrix Tool (IMT) result before procurement. “Scope” describes what the source can support; it does not imply blanket certification.

| ID | Reference and source | Version/date checked | Use in this comparison | Scope and caveat |
| --- | --- | --- | --- | --- |
| C-01 | [Proxmox VE storage: backend matrix](https://github.com/proxmox/pve-docs/blob/master/pvesm.adoc) | Upstream current; checked 2026-11-08 | Backend availability and maturity labels, including Btrfs preview | Moving master branch; confirm against the chosen released VE manual |
| C-02 | [Proxmox VE storage: LVM](https://github.com/proxmox/pve-docs/blob/master/pve-storage-lvm.adoc) and [documentation patch marking volume-chain snapshots as preview](https://lore.proxmox.com/pve-devel/s8o1pom2vhn.fsf%40proxmox.com/T/) | Patch dated 2025-08-29; current docs checked 2026-11-08 | Shared LVM, volume-chain snapshot behavior, and date the preview status was explicitly documented | Current maturity can change; no stable-release date/commitment identified in reviewed sources |
| C-03 | [Proxmox VE storage: NFS](https://github.com/proxmox/pve-docs/blob/master/pve-storage-nfs.adoc) | Upstream current; checked 2026-11-08 | NFS backend and image/snapshot behavior | Validate chosen server, NFS version, content type, and image format |
| C-04 | [Proxmox VE backup and restore](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc) | Upstream current; checked 2026-11-08 | Live backup distinction from VM snapshot features | Test guest consistency, retention, and restore with the selected release/PBS version |
| C-05 | [Proxmox VE cluster administration guide](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) and [HA manager](https://pve.proxmox.com/pve-docs/pve-admin-guide.html#chapter_ha_manager) | Current online guide; checked 2026-11-08 | Cluster quorum, Corosync, HA and QDevice design | Pin node count, site topology, fencing, and release; a third voter does not itself establish site resilience |
| C-06 | [Dell PowerStore VMware vSphere best practices](https://infohub.delltechnologies.com/en-au/t/dell-powerstore-vmware-vsphere-best-practices-2/) | Product guide; checked 2026-11-08 | PowerStore VMware NFS/block datastore practices | PowerStore-specific; verify model/PowerStoreOS and VMware interoperability |
| C-07 | [Dell PowerStore Metro Volumes](https://www.dell.com/support/manuals/en-us/powerstore-5000/pwrstr-metro-volumes-guide) | Guide; checked 2026-11-08 | Synchronous block replication, host connectivity, witness and failure behavior | Exact model, PowerStoreOS, host mode, and topology determine behavior; do not generalize to all Dell arrays |
| C-08 | [Dell Proxmox VE with PowerStore Metro Volumes](https://www.dell.com/en-us/infohub/articles/proxmox-with-dell-powerstore-metro-volumes) | Example pins PVE 8.3.0 and PowerStoreOS 4.1; checked 2026-11-08 | Three-host Proxmox, iSCSI multipath, shared LVM, dual-array witness example | Vendor solution example, not blanket certification for later PVE or all PowerStore models |
| C-09 | [Broadcom vVol deprecation notice](https://knowledge.broadcom.com/external/article/401070) and [removal notice](https://knowledge.broadcom.com/external/article/407058) | KBs; checked 2026-11-08 | vVol/VASA lifecycle statements for VCF/VVF 9.x | Verify product-specific lifecycle and release notes before migration planning |
| C-10 | [Broadcom vSphere HA admission-control guidance](https://knowledge.broadcom.com/external/article/396016) | KB; checked 2026-11-08 | Capacity/admission-control considerations for HA | VMware HA is not asserted to require exactly three hosts; design depends on workload and policy |
| C-11 | [NetApp ONTAP VMware datastore protocols](https://docs.netapp.com/us-en/ontap-apps-dbs/vmware/vmware-vsphere-datastores-top.html) | Online documentation; checked 2026-11-08 | ONTAP VMFS/block and NFS options | Exact ONTAP platform, transport, ESXi/vCenter release, and host utilities must be checked |
| C-12 | [NetApp platform/personality comparison](https://docs.netapp.com/us-en/asa-r2/learn-more/hardware-comparison.html) | Online documentation; checked 2026-11-08 | AFF/FAS/classic ASA/ASA r2 distinction | Product personality and supported protocol differ; do not treat “NetApp” as a single configuration |
| C-13 | [NetApp SnapMirror active sync prerequisites](https://docs.netapp.com/us-en/ontap/snapmirror-active-sync/prerequisites-reference.html) and [architecture](https://docs.netapp.com/us-en/ontap/snapmirror-active-sync/architecture-concept.html) | Online documentation; checked 2026-11-08 | Mediator, latency/topology and active-sync behavior | Confirm exact platform, ONTAP release, protocol, and IMT result |
| C-14 | [NetApp Proxmox business continuity](https://docs.netapp.com/us-en/netapp-solutions-virtualization/proxmox/proxmox-business-continuity.html) | Online solution guide; checked 2026-11-08 | Multi-site Proxmox/ONTAP continuity patterns | Solution-specific; site quorum and storage quorum must be designed together |
| C-15 | [NetApp Storage Manager for Proxmox](https://docs.netapp.com/us-en/netapp-solutions-virtualization/proxmox/proxmox-smp.html) | Online product guide; checked 2026-11-08 | Proxmox integration, backup consistency and restore scope | Behavior is release-specific; validate granularity and any all-VM impact before relying on it |
| C-16 | [Btrfs documentation](https://btrfs.readthedocs.io/en/latest/) | Current online docs; checked 2026-11-08 | Btrfs filesystem features and operational constraints | Kernel/userspace and RAID profile matter; this is not a cluster-filesystem claim |
| C-17 | [OpenZFS documentation](https://openzfs.github.io/openzfs-docs/) | Current online docs; checked 2026-11-08 | ZFS features, hardware/layout and administration concepts | Does not certify a hypervisor datastore or multi-host shared-LUN use |
| C-18 | Local [Btrfs guide](README-BTRFS-Guide_r1.2.4.md), [NetApp guide](README-NetApp-Guide_r1.0.1.md), [VMware guide](README-vmware-storage.md), and [ZFS guide](README-ZFS-Guide_r1.0.1.md) | Repository copies; check each document's own revision/date | Background context and terminology | Internal working guides; not substitutes for current vendor support matrices |

### Evidence status for each statement

For final review, classify every material capability statement as **vendor-documented**, **interoperability-confirmed**, **tested**, **inferred**, or **unresolved**. A product guide establishes documented behavior only within its stated configuration. The selected models, firmware, host build, protocol, plugins, licenses/entitlements, and support agreements require their own compatibility records. Capture the document title, URL or local path, product release, publication/update date, access date, verified claim, and any limitation when adding references.

## Appendix D: Acronyms and Terms

### Acronyms and abbreviations

| Acronym or abbreviation | Full form | Meaning in this document |
|---|---|---|
| AFF | All Flash FAS | NetApp all-flash storage family used as the provisional unified ONTAP example. |
| ASA | All SAN Array | NetApp SAN-focused storage personality; distinguish classic ASA from ASA r2. |
| Btrfs | B-tree filesystem | Linux filesystem considered as a guest filesystem or as part of a separate storage-server design. |
| Corosync | Cluster engine for cluster messaging and membership | Proxmox cluster communication layer; its network and quorum behavior matter to HA. |
| CSI | Container Storage Interface | Kubernetes interface used by storage drivers to provision and attach storage. |
| FC | Fibre Channel | Block-storage transport considered for SAN connectivity. |
| FAS | Fabric-Attached Storage | NetApp storage family, commonly considered for HDD or hybrid capacity configurations. |
| HA | High availability | Ability of eligible workloads to restart or continue after specified failures; not a guarantee of zero interruption. |
| IMT | Interoperability Matrix Tool | NetApp compatibility tool used to verify exact product and software combinations. |
| iSCSI | Internet Small Computer Systems Interface | SCSI block storage transported over IP networks. |
| LUN | Logical unit number | A block-storage device presented by an array to a host. |
| Mbit/s, Gbit/s | Megabits per second, gigabits per second | Network or data-rate units; not interchangeable with megabytes or gigabytes per second. |
| NAS | Network-attached storage | File-based storage accessed through protocols such as NFS. |
| NFS | Network File System | File-sharing protocol used here as a shared hypervisor datastore option. |
| N+1 | N plus one | Capacity planning that can tolerate one additional component failure while serving the required workload. |
| NVMe | Non-Volatile Memory Express | Storage command/interface family; NVMe-oF transports it over a fabric or network. |
| ONTAP | NetApp ONTAP storage operating system | NetApp storage software whose features depend on platform, personality, and release. |
| PBS | Proxmox Backup Server | Proxmox backup product; considered separately from hypervisor snapshot capability. |
| PVE | Proxmox Virtual Environment | Proxmox's virtualization platform; also abbreviated VE in product/version names. |
| QDevice | Quorum device | External vote used by a Proxmox cluster in supported small-cluster designs. |
| QoS | Quality of Service | Controls or policies that influence resource allocation or performance; exact implementation is product-specific. |
| RPO | Recovery Point Objective | Maximum acceptable amount of data loss, expressed as time or an equivalent recovery point. |
| RTO | Recovery Time Objective | Target time to restore a service after a disruption. |
| SAN | Storage Area Network | Network and storage system presenting block devices to hosts. |
| SVM | Storage Virtual Machine | ONTAP logical storage server that provides data services and protocol endpoints. |
| TB | Terabyte | Decimal capacity unit in this report: 1 TB = 10¹² bytes, unless a source explicitly uses another convention. |
| VCF/VVF | VMware Cloud Foundation / VMware vSphere Foundation | VMware product offerings referenced in the vVol lifecycle discussion. |
| VE | Virtual Environment | Short form used in Proxmox VE product/version references. |
| VM | Virtual machine | Software-defined computer hosted by a hypervisor. |
| VMFS | Virtual Machine File System | VMware datastore filesystem used on supported shared block devices. |
| VMDK | Virtual Machine Disk | VMware virtual-disk format. |
| WAFL | Write Anywhere File Layout | NetApp ONTAP's internal filesystem/layout layer; distinct from a host filesystem such as VMFS. |
| ZFS | Zettabyte File System | Filesystem and volume-management system considered here as a guest filesystem or separate storage-server design. |

### Key terms

| Term | Plain-language definition | How it applies here |
|---|---|---|
| Array | A purpose-built storage system that presents data to servers. | Dell and NetApp are compared as external arrays; exact family and model determine capabilities. |
| Array snapshot | A point-in-time copy or reference maintained by the storage system. | May protect a volume, LUN, datastore, or consistency group; it is not automatically a VM-aware backup. |
| Backend | The storage type and management method a hypervisor uses for VM or container data. | Examples include VMFS, shared LVM, NFS, local ZFS, and local Btrfs. |
| Backup | A separately retained copy intended to restore data after loss, corruption, or unwanted change. | Must be tested independently; snapshots and replicas alone may share failure modes or copy corruption. |
| Capacity: raw vs usable | Raw is the sum of drive capacity before protection and overhead; usable is space available to store workload data after those factors. | The 130 TB scenario is stated as raw capacity; usable capacity and whether it applies per array or to the pair remain open. |
| Crash-consistent | A copy that reflects storage as if power were lost at that instant, without application-level coordination. | This may require application recovery and should not be presented as application-consistent protection. |
| Data path | The route data takes between a workload and storage, including host software, adapters, switches, and array interfaces. | Used to compare FC, iSCSI, NVMe-oF, and NFS designs and their failure points. |
| Failure domain | A component or location whose failure can affect multiple systems at once. | Hosts, fabrics, arrays, power zones, and sites must be considered separately when assessing resilience. |
| Failback | Returning service or ownership to the preferred system after a failover. | Must include resynchronization, host path state, and protection against stale writes. |
| Failover | Moving service or storage access to a surviving component after a failure. | Its trigger, automation, interruption, and recovery steps depend on the exact host-array design. |
| Fencing | Forcibly preventing a failed or isolated system from accessing a resource it must no longer own. | Prevents two hosts or sites from writing to a single-owner filesystem or storage service during failover. |
| Granular recovery | Restoring one selected object, such as a VM or application, without reverting unrelated data. | The report asks whether array snapshots and integrations can restore at the required level. |
| Live migration | Moving a running VM from one host to another with little or no planned interruption. | Requires compatible hosts and network/device setup; it is different from restarting a VM after host failure. |
| Multipathing | Using multiple independent paths between a host and block storage, with path selection and recovery. | Needed for resilient FC/iSCSI designs; redundant Ethernet alone does not configure block multipathing. |
| NFS datastore | A shared directory exported by a storage system and mounted by hypervisor hosts. | A file-based alternative to presenting a block LUN and formatting it with VMFS or managing it with LVM. |
| Quorum | The minimum set of votes or members required for a cluster to make coordinated decisions. | Compute-cluster quorum and storage-system quorum are distinct and both matter in stretched designs. |
| Replication | Copying data changes from one storage system or location to another. | Can improve recovery from array/site failure, but may also copy deletion or corruption. |
| Shared storage | Storage accessible to multiple cluster hosts through a supported shared-access method. | Enables eligible VM migration and HA workflows; the filesystem or backend must support the intended multi-host use. |
| Snapshot | A point-in-time view used as a short-term checkpoint or recovery reference. | VM, guest, and array snapshots operate at different layers and have different consistency and rollback scope. |
| Storage migration | Moving a VM's virtual disks from one datastore or storage backend to another. | Distinct from compute-only live migration and subject to backend and VM configuration limits. |
| Sync replication | Replication that acknowledges writes according to the paired systems' synchronous protection rules. | Can reduce data loss for supported failures, with latency, quorum, and topology requirements. |
| Uniform / non-uniform host access | Whether hosts at both storage sites have equivalent direct paths to both storage systems. | Can change path behavior and recovery steps in dual-array Metro or active-sync designs. |
| Usable capacity | Capacity available to workloads after redundancy, metadata, reserves, formatting, and other overhead. | Must be sized separately from the 130 TB raw premise, snapshots, replicas, and backup retention. |
| Witness / mediator | An independent service or vote that helps paired systems decide which side may serve data. | Must be placed in an appropriate failure domain and is not interchangeable with compute quorum. |
| Volume chain | A sequence of base and changed disk images where each layer depends on an earlier layer. | Proxmox's shared-LVM snapshot preview uses qcow2 backing chains; preserve and manage the full chain correctly. |
