# Virtual machine and container platform comparison

Research cutoff: **2026-10-30**. Specification: r1.0.2. Desk research only; no
deployment, purchases, configuration changes, live multicast/failover tests or
measured recovery claims. Platform detail: [VMware](research-vmware-r1.0.1.md),
[Proxmox](research-proxmox-r1.0.1.md), [Red Hat](research-rhel-r1.0.1.md).

Document revision: **r1.0.1**. Baseline: unversioned
`research-vm-comparison.md` (r1.0.0 for preservation bookkeeping; archived in
`99_Archive/`). Review date:
**2026-10-30**; research cutoff unchanged. Synthesized after the three r1.0.1
platform reports were revised. Review status: independent claim review recorded
in [research-review-r1.0.1.md](research-review-r1.0.1.md) and
[research-claim-audit-r1.0.1.tsv](research-claim-audit-r1.0.1.tsv); document
checks for this revision are recorded in
[research-verification-r1.0.1.md](research-verification-r1.0.1.md).

## Executive summary

The platforms meet different operational needs. VMware vSphere is VM
infrastructure with a supported Kubernetes path through Supervisor and vSphere
Kubernetes Service (VKS). Proxmox Virtual Environment (VE) directly manages
Kernel-based Virtual Machine (KVM)/QEMU VMs and Linux Containers (LXC);
application-container runtimes and Kubernetes generally run inside guest VMs
under separate support. Red Hat Enterprise Linux (RHEL) supplies KVM and Podman;
OpenShift adds the integrated Kubernetes management plane, with OpenShift
Virtualization putting VMs under Kubernetes lifecycle control. Comparing bare
RHEL with a complete VMware/Proxmox cluster would omit required management,
availability and protection components. [C1](#c1), [C3](#c3), [C4](#c4),
[C6](#c6).

All can administer multiple hosts, but the boundaries differ. vCenter manages
VMware hosts/VMs; VMware Cloud Foundation (VCF) adds fleet/self-service
services. VE has distributed per-cluster management and Datacenter Manager (PDM)
for independent Proxmox clusters/sites. OpenShift's console controls cluster
hosts, VMs and application pods; Advanced Cluster Management (ACM) adds fleet
functions. Guest container processes, backup products, operating-system
maintenance and other vendors' hypervisors may retain separate interfaces. None
creates one universal cross-vendor scheduling/failover domain. [C2](#c2),
[C4](#c4), [C6](#c6), [C12](#c12).

Provisioning VMs is distinct from orchestrating applications: templates/images
create guests; Kubernetes controllers reconcile pod replicas/updates; guest
runtimes supervise local containers. Host high availability (HA) normally
**restarts** affected VMs/containers. Live migration addresses planned
maintenance. Application replicas, consistent storage, fencing and traffic
recovery determine continuity. Backup and site recovery require their own
policies, copies, tools and often additional subscriptions. [C2](#c2),
[C4](#c4), [C10](#c10).

Multicast cannot be reduced to one answer per vendor. Bridged/VLAN VM paths are
conditional candidates; VMware documents VKS IPv4/Linux and additional VLAN
paths; OpenShift documents enabled-project IPv4 pod multicast and additional
SR-IOV interfaces. Default NAT, an arbitrary Container Network Interface (CNI),
IPv6 unicast, or a working hypervisor network does not establish container
application multicast. No universally supported dual-stack external-LAN
container path was established. [C3](#c3), [C9](#c9), [C11](#c11).

Conditional fit: Proxmox offers integrated VM/LXC operations and published
support prices without software feature tiers; VMware suits existing vSphere
ecosystems and broader private-cloud requirements where entitlements/footprint
fit; OpenShift suits Kubernetes-led operations and mixed VM/pod modernization.
RHEL/Podman is a simpler host-level option, while OpenShift Virtualization
Engine (OVE) is a VM-only entitlement. Inventory, skills, support expectations,
application network needs and recovery targets can change that assessment. No
universal winner or invented total cost is presented.

## Compared stacks and assumptions

| Family / path                | Reference stack                                                                                                                                               | Compatibility                                                                                                                                                                                                                                                                                                             |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| VMware W-VM / W-VKS          | VCF or VMware vSphere Foundation (VVF) **9.1.1**; ESX/vCenter **9.1.1.0100**; Supervisor; optional current VKS **3.8.0+v1.37**, VKr **1.37.1+vmware.4-vkr.1** | Core BOM GA Sep3; patch Oct12. Oct22 VKS is asynchronous: Supervisor Kubernetes>=1.33 and correct depot/YAML/matrix required. GA BOM lists older VKS 3.7/VKr 1.34.2. Shipped current Linux node images include Photon5/Ubuntu22.04/24.04, containerd 2.4.0, Antrea 2.7.0 or Calico 3.32.2, CSI3.9.0. [C2](#c2), [C3](#c3) |
| Proxmox P-VM / P-LXC         | **VE 9.2**, **PBS 4.2** for backup, **PDM 1.1** for fleet management; integrated QEMU 11/LXC 7 and supported storage                                          | Guides9.2.13/4.2.8-1/1.1.9 are dated snapshots, not universal latest package declarations. Public index observes pve-manager9.2.24/PBS 4.2.8-1/PDM 1.1.9; enterprise patch set remains unverified. Select current enterprise updates when support required. [C4](#c4), [C14](#c14)                                        |
| Proxmox guest app/Kubernetes | Linux guest; Docker 29.9.2/Debian13 candidate; upstream Kubernetes 1.37.1/containerd 2.4.2/Calico 3.33 candidate                                              | These individually current components do not establish a Proxmox-certified commercial stack. Guest Podman, Windows containers and exact Kubernetes integration support remain unverified. [Proxmox support mapping](research-proxmox-r1.0.1.md#architecture-and-workload-support)                                         |
| Red Hat RH1                  | **RHEL 10.2**, Podman **5.8.2**, KVM/libvirt on certified hardware/guest combinations                                                                         | OS/runtime path separate from OpenShift. RHEL 9.8 remains a parallel supported minor line; rolling container tools have their own lifecycle. Guest certification still required. [C8](#c8)                                                                                                                                |
| Red Hat RH2/RH3              | Bare-metal **OpenShift 4.22** + **Virtualization4.22.9**; Kubernetes/CRI-O **1.35**; optional **OADP 1.6**, **ODF 4.22**, **ACM 2.17**                        | Stable release manifests verify OCP 4.22.18; later MicroShift reference is not proof of a newer OCP update channel. Use matching minors/current errata and certified hardware/CSI. Other current companions include ACS 4.11, Quay 3.18, AAP 2.7, Satellite 6.19; not presumed all installed. [C6](#c6), [C13](#c13)      |

No hardware, host count, workload inventory, sites, budget, existing
entitlement, storage or multicast application specification was supplied. Common
assumption is certified x86-64 bare-metal infrastructure with separately
supported Linux/Windows guests, redundant production networks and correctly
licensed software. Proxmox's official Arm64 path and Red Hat edge/cloud
alternatives have different matrices; they are not silently included. No
arbitrary latest-version cross-vendor combination is recommended.

Status dimensions remain separate: **documented supported** means the
vendor/upstream documents the named path; **conditional** requires stated
prerequisites; **documented unsupported** needs an explicit exclusion; **not
verified** means missing applicable evidence. Support provider and entitlement
are not the same as capability. *Technical inference*, *recommendation* and
*proposed validation* do not establish commercial certification.

## VM and container support

| Execution path                    | VMware                                                                                                                                                 | Proxmox                                                                                                                                                                           | Red Hat                                                                                                                                                                                                                                                         |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Conventional VM                   | ESX 9.1.1 guest; Broadcom infrastructure support, guest/application vendor separate; VVF/VCF subscription; **conditional** exact certification         | VE 9.2 QEMU/KVM; Proxmox infrastructure, guest vendor separate; full software features free; **documented supported** platform with guest qualifications                          | RHEL 10.2 KVM or OpenShift 4.22 Virtualization; Red Hat platform, guest/app provider separate; **conditional** certified guests/subscription. [C2](#c2), [C4](#c4), [C6](#c6)                                                                                   |
| Native system containers          | No selected ESX LXC/LXD product; guest candidate **not verified**                                                                                      | LXC 7 directly on VE, shared host Linux kernel, Proxmox integration support; **documented supported**. OCI image-to-LXC feature remains preview, excluded from production support | No selected supported RHEL LXC/LXD platform; **not verified**. VM offers separate guest kernel. [C4](#c4), [C8](#c8)                                                                                                                                            |
| Application runtime in guest/host | Docker/Podman in supported guest; each runtime/OS owns its support, exact whole stack **conditional/not verified**                                     | Guest VM recommended for Docker/application orchestration; VE sees VM. Docker Debian path **conditional**, other exact combinations **not verified**                              | Podman 5.8.2 on RHEL 10.2 **documented supported** tool path, app support separate. Docker Engine unsupported **by Red Hat** on RHEL 10; Docker's own install path does not change provider boundary. [C8](#c8), platform tables                                |
| Kubernetes applications           | VKS 3.8/VKr 1.37.1 in VM nodes, containerd 2.4.0 and selected shipped CNI/CSI; **documented supported** conditional product path, VKS included VVF/VCF | Guest Kubernetes/runtime/CNI/storage are separately built/supported; named upstream candidate **not verified** as whole commercial stack                                          | OCP 4.22/RHCOS/CRI-O 1.35 Linux pods, **documented supported** product path. OKE/OCP/Plus entitlement differs from OVE. [C3](#c3), [C4](#c4), [C6](#c6), [C7](#c7)                                                                                              |
| VMs managed through Kubernetes    | Supervisor VM Service and VKS node VM APIs; not generic KubeVirt equivalence                                                                           | No selected first-party Kubernetes VM controller; additional tooling would be separate                                                                                            | OpenShift Virtualization KVM/QEMU in launcher pods, VM custom resources, integrated placement/storage/networking; **documented supported** with matching version and hardware. [C3](#c3), [C6](#c6)                                                             |
| Windows containers                | Windows guest/runtime or qualified VKS worker path; exact current combination **not verified** here                                                    | Windows VM does not create native Windows LXC; exact runtime/support combination **not verified**                                                                                 | Qualified Windows compute/containerd with WMCO 10.22.1 release notes and version-qualified Windows Server2022/2025 matrix, **conditional**; Microsoft licensing and kernel/image matching separate. [C6](#c6), [Red Hat table](research-rhel-r1.0.1.md#architecture-and-workload-support) |

A supported guest OS does not establish every runtime/distribution inside it.
Linux containers share the execution host/guest Linux kernel; Windows images
need a compatible Windows kernel. Kubernetes portability concerns
images/manifests as well as CNI/CSI, privileges, secrets, storage and
application behavior. Main evaluation excludes previews and arbitrary
bare-hypervisor runtime installs.

## Centralized management

| Interface                                                   | Scope                                                                                     | Workload control                                                                                                                                                                                     | Outage / rights                                                                                                                                                                                            |
| ----------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| VMware vCenter; centralized appliance                       | Multiple ESX hosts/clusters; VCF Operations groups/manages fleet across vCenters/sites    | VM/Supervisor/VKS infrastructure; individual application deployments use Kubernetes APIs. VCF Automation adds catalogs/organization workflows; guest, NSX/recovery/backup consoles remain            | Running VMs/host HA may continue during manager loss; centralized placement/changes affected. VCF design protects vCenter with vSphere HA, **not vCenter HA/FT**. VVF/VCF rights differ. [C2](#c2)         |
| Proxmox VE; distributed per-node GUI/API/pmxcfs             | One Proxmox cluster accessible through any surviving member                               | Host/VM/LXC inventory, templates, migration/HA, network/storage, updates, backup scheduling, RBAC and audit; guest runtime/pod administration separate                                               | Access-node loss: use another. Quorum loss makes configuration read-only and may fence HA nodes. Features included, subscription support optional. [C4](#c4)                                               |
| PDM; separate central service                               | Multiple independent Proxmox clusters/standalone nodes and PBS remotes across sites       | Fleet inventory, selected power/snapshot/migration/update/installation/SDN actions; some views read-only; full VE/PBS provisioning/storage/backup policies retain local interfaces                   | PDM outage removes fleet entry, not each remote's execution/HA. Enterprise access tied to qualifying remote subscriptions; no separate PDM subscription. [C4](#c4)                                         |
| RHEL Cockpit/libvirt, Satellite, AAP                        | Host console versus OS estate versus automation workflow domains                          | VM/Podman host tasks, OS content/provisioning/patching and scripted APIs respectively; no single distributed scheduler from bare RHEL                                                                | Host workloads continue if dashboard/automation server unavailable; jobs/content orchestration delayed. Satellite/AAP separate products. [C6](#c6), [C8](#c8)                                              |
| OpenShift console/API; replicated per-cluster control plane | One OCP cluster, hosts/VMs/pods; ACM hub adds many fleet operations across clusters/sites | VM templates/migration/storage/network and Kubernetes lifecycle in cluster; guest OS maintenance separate. ACM policy/search/observability/VM operations do not merge local schedulers               | Console-only outage allows CLI/API. API/etcd quorum loss impairs scheduling/reconciliation; ACM hub outage leaves healthy local clusters. ACM separately entitled or qualifying Plus. [C6](#c6), [C7](#c7) |
| Mixed-vendor automation, backup or monitoring               | AAP certified collections, Veeam supported protection, Zabbix/provider monitoring         | Workflow/backup/metrics scope is not full host lifecycle parity. ACM third-party Kubernetes import/operation matrix differs by distribution/version; Proxmox Ansible collection is community content | Separate support/contracts/credentials and product dependencies. No merged HA or scheduling domain. Running the Operations appliance on Proxmox is explicitly unsupported. [C10](#c10), [C12](#c12)        |

All central managers need supported versions, DNS/time/TLS/identity, reachable
APIs, RBAC and protected audit/configuration. VE cluster networking needs low
latency/quorum; use PDM for independent distant sites rather than assuming a
WAN-stretched cluster. VMware9.1 vCenter Groups replace deprecated Enhanced
Linked Mode for current grouping. OpenShift/ACM and VMware configuration maxima
are product/workload-qualified; report-specific limits are not deployment sizing
promises. Proxmox's guide does not establish a universal tested node ceiling.
[C2](#c2), [C4](#c4), [C6](#c6).

**One-place answer:** yes within each platform's specified management domain;
multiple clusters/sites need the fleet product, guest containers may need guest
tools, and other vendors require separately supported integrations. A dashboard
failure and loss of the authoritative cluster control plane have different
consequences.

## Provisioning and orchestration

| Lifecycle task                  | VMware                                                                                                  | Proxmox                                                                                                  | Red Hat                                                                                             |
| ------------------------------- | ------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| Install/onboard infrastructure  | VCF Installer, vCenter/fleet lifecycle; certify hosts/network/storage                                   | VE installer/API and PDM prepared answers; create/join VE cluster                                        | RHEL installer/Satellite or OCP installer/Operators; certify hardware/CSI/CNI                       |
| Create VM and initialize        | vCenter templates/content library/API/PowerCLI; DRS/policies place; guest initialization tooling        | VE GUI/qm/API, ISO/template/clone/Cloud-Init; choose host/storage/VLAN                                   | RHEL Cockpit/virt-install/libvirt or OpenShift VirtualMachine template/instance type/CDI/cloud-init |
| Create container platform       | Enable Supervisor, VKS namespace/cluster and supported node images                                      | Provision control-plane/worker VMs, then install separate supported distribution/runtime/network/storage | RHEL Podman for local app, or provision OCP/RHCOS/CRI-O; add Virtualization for VMs                 |
| Deploy/scale/update app         | Kubernetes manifests/Operators/add-ons within VKS; ordinary guest runtime separate                      | Guest runtime/Compose or Kubernetes controllers; VE HA is not app replica scaling                        | Podman Quadlet/systemd locally; OCP Deployment/StatefulSet/Operators/GitOps for cluster apps        |
| Maintain desired state/failures | vSphere VM HA, VKS node controllers, Kubernetes pod controllers and app replication at different layers | VE HA whole guest, guest/runtime or Kubernetes app controllers; physical capacity operator-owned         | libvirt/optional RHEL HA or Virtualization controllers/fencing plus Kubernetes/app replication      |
| Retire while retaining data     | Remove service/VM/manifests after app shutdown; deliberate disk/PVC/backup/key/DNS retention            | Remove HA/replication references and VM/LXC/app; separately retain disks/mount data/backups              | Remove VM/app custom resources/units; deliberate PVC/reclaim policy, snapshot and backup retention  |

Sources: platform lifecycle sections and primary [VMware services](#c3), [VE
guide](#c4), [Red Hat VM/containers](#c6), [RHEL tools](#c8). Automation does
not supply missing storage/network design, secrets policy, spare capacity or
application upgrade compatibility.

**VM workflow:** operator selects certified template/image, attaches
storage/network, configures identity/secrets/guest agent, registers HA and
backup, then monitors app health. Host failure invokes the platform's safe
restart mechanism; guest/database and traffic recovery follow. Data loss invokes
backup/replica recovery. Retirement explicitly preserves required durable data,
logs and recovery copies.

**Application workflow:** provision the runtime or Kubernetes cluster first;
deploy pinned image/manifests, probes, replicas, Secrets, endpoints and
persistent volumes. Runtime/Kubernetes/app controllers own restarts and
rollouts; infrastructure tools own hosts/VM nodes. Back up resources and data
consistently. On node/host loss, fencing and storage attachment precede safe
data writes and readiness-based traffic. Delete resources and revoke secrets
only under the chosen data-retention policy. These are proposed operating
workflows, not executed deployment tests.

## Networking and multicast

The full path includes runtime network mode/CNI, guest OS/NIC, hypervisor switch
or host bridge, overlay/underlay, firewall, physical switch/querier and routers.
IPv4 uses Internet Group Management Protocol (IGMP); IPv6 uses Multicast
Listener Discovery (MLD). Layer2 forwarding and inter-subnet multicast routing
are separate requirements. Application traffic is distinct from internal
platform/fabric multicast.

| Path / endpoints                                                                         | Physical scope                                                           | IPv4                                                                      | IPv6                                                            | Needs / owners                                                                                                                                                                                                                                          |
| ---------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------- | --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| VMware W-VM↔VM on vDS/VLAN                                                               | Same host, cross host, both directions external LAN                      | **conditional**                                                           | **conditional**                                                 | Broadcom switch mechanisms plus guest/physical network joins, IGMP/MLD filtering/querier and permitted data; app support separate. [C2](#c2), [VMware matrix](research-vmware-r1.0.1.md#networking-and-multicast)                                       |
| Proxmox P-VM↔VM; P-LXC↔LXC; VM↔LXC on bridge/VLAN                                        | Same host, cross host, bidirectional external LAN                        | **conditional**                                                           | **conditional**                                                 | Linux bridge IGMP/MLD is upstream fact; attached endpoint end-to-end support is technical inference, not Proxmox app certification. Firewalls and physical topology must permit traffic. [C4](#c4), [C11](#c11)                                         |
| RHEL KVM VM↔VM on LAN bridge                                                             | Same host, cross host, bidirectional LAN                                 | **conditional**                                                           | **conditional**                                                 | Documented bridge attachment plus upstream membership capability; full app result is technical inference. Red Hat host/guest provider/network owner share responsibilities. [C8](#c8), [C11](#c11)                                                      |
| Docker/Podman Linux host-network container in guest VM↔VM/container/LAN                  | Same/cross physical host and external via VM interface                   | **conditional** inference                                                 | **conditional** inference                                       | Shares **guest** namespace, not physical host. Runtime mode support does not certify whole app path; guest NIC/bridge/MLD/IGMP/firewalls still govern. [C8](#c8), platform matrices                                                                     |
| Default Docker/Podman/libvirt NAT or rootless pasta                                      | Local bridge differs from cross-guest/external                           | External full path **not verified**                                       | External full path **not verified**                             | Port publishing/unicast NAT is not multicast membership/routing. Do not assume all same-host containers share one L2 segment. [C8](#c8), platform matrices                                                                                              |
| Guest rootful macvlan / ipvlan L2                                                        | VM↔container, container↔container and LAN according to attachment        | **conditional** candidate                                                 | Family/path-specific **conditional/not verified**               | Multiple MAC/filter/port-security and host-parent isolation matter. No universal support claim; RHEL rootless macvlan explicitly unsupported. Docker ipvlan L3 drops multicast: **documented unsupported**. [C8](#c8), platform matrices                |
| VMware VKS 3.8/Antrea 2.7 Linux primary CNI                                              | Pod↔pod same/cross host; pod↔external/VM if node network forwards/routes | **conditional** documented path                                           | Antrea multicast **documented unsupported**                     | Enable/configure feature, interfaces, groups and suitable encap/noEncap/hybrid mode; not networkPolicyOnly. Windows excluded; policy ingress limits. Broadcom path plus upstream Antrea evidence. [C3](#c3), [C11](#c11)                                |
| VMware VKS node secondary interfaces/VPC VLAN Extension                                | Node gains a separate path; pod↔external documented; pod↔VM/pod conditional on shared network | **conditional** vendor-documented capability                              | End-to-end **not verified**                                     | An extra node interface does not route pod traffic automatically; workload configuration is needed. Primary network is immutable after cluster creation; secondary interfaces cannot be removed without recreating the cluster. VKS 3.8 supports VLAN-backed VPC unlike\<=3.7.1. [C3](#c3), [C17](#c17) |
| NSX9.1 VM routed multicast                                                               | Across segments and external routed subnets                              | **conditional**, PIM-SM/IGMPv2                                            | **not verified**; NSX feature documented for IPv4 networks only | VCF NSX Edge/tier0/tier1, upstream rendezvous point/PIM/reverse routes. No Federation/multi-VRF/downlink L2 bridge; Gateway Firewall limitation. [C2](#c2)                                                                                              |
| Proxmox guest Kubernetes 1.37.1/containerd 2.4.2/Calico 3.33 candidate                   | Pod↔pod/VM/LAN, same/cross host                                          | **not verified** full path                                                | **not verified** full path                                      | Current CNI/Kubernetes compatibility is not positive multicast evidence or Proxmox commercial stack support. Host-network/secondary-CNI alternatives need separate qualification. [Proxmox matrix](research-proxmox-r1.0.1.md#networking-and-multicast) |
| Proxmox guest Kubernetes with secondary VM NICs and Multus                             | VM nodes can use separate bridges/VLANs; pods can request additional interfaces | **not verified** end to end                                                | **not verified** end to end                                      | Proxmox documents multiple VM NICs. Multus is Apache-2.0 open source: it lets a pod request extra connections and calls other CNI plugins to provide them. Exact stack support and multicast remain unverified. [C4](#c4), [C18](#c18) |
| OCP 4.22 OVN-Kubernetes pod↔pod within enabled project                                   | Same physical host / cross physical hosts                                | **documented supported** when enabled                                     | Family-specific **not verified**                                | Off by default; low-bandwidth coordination guidance. Multicast bypasses NetworkPolicy including deny-all; do not assume policy isolation. Red Hat product evidence. [C9](#c9)                                                                           |
| OCP default-overlay pod↔external LAN / differently attached VM                           | Same host does not remove network boundary                               | **not verified**                                                          | **not verified**                                                | Namespace multicast is not LAN routing/bridging; Service/Route is not a multicast gateway. [C9](#c9)                                                                                                                                                    |
| OCP additional SR-IOV pod interface↔VF pod/LAN                                           | Same/cross host and external according to NIC/fabric                     | **conditional** vendor-documented capability                              | End-to-end **not verified**                                     | Supported NIC/VF/Operator, interface selection/all-multicast/membership and physical switching/routing. Migration/rescheduling resources differ from overlay. [C9](#c9)                                                                                 |
| OpenShift VM↔pod/VM on secondary localnet/bridge/SR-IOV; Windows/MicroShift alternatives | Path-specific same/cross/external                                        | Secondary L2 **conditional inference**; other full paths **not verified** | Application path **not verified**                               | Supported IPv6 attachment or multicast DNS does not certify arbitrary IPv6 groups/endpoints. Exact binding/hardware/guest support and migration restrictions apply. [C6](#c6), [C9](#c9)                                                                |

VLANs alone do not route groups between subnets. Switch snooping needs valid
memberships and an effective querier; routers need appropriate multicast
protocol/source/group policy and reverse routes. Guest/runtime/host firewalls
must allow data and IGMP/MLD/control traffic. NSX IPv6 neighbor-discovery fixes
do not establish routed application multicast. All three need application
group/port/family/rate/topology requirements before selection. [C2](#c2),
[C11](#c11).

For external LAN traffic, qualify a documented VM bridge/VLAN path or the
specific VKS/OVN/SR-IOV alternative supported by its release/network evidence.
Do not promise a default CNI, NAT configuration or arbitrary dual-stack
container solution. Commercial support confirmation and practical validation
remain required where the matrix says conditional/inference.

## Availability, failover, and maintenance

| Event / layer                      | VMware                                                                            | Proxmox                                                                | Red Hat                                                                                     | Impact / needs                                                                                                       |
| ---------------------------------- | --------------------------------------------------------------------------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| App/container process fails        | Runtime/Kubernetes/app probes and replicas                                        | Guest runtime/Kubernetes or LXC service manager                        | Podman/systemd or OCP controllers                                                           | Local restart differs from replica continuity; persistent app state and readiness/load balancing matter              |
| VM/host fails                      | Configured vSphere HA safely reboots VM; VKS/pod controllers may act separately   | HA Manager, Corosync/quorum/watchdog fencing restart registered VM/LXC | RHEL HA add-on if engineered; OCP health/fencing/remediation then VM restart/pod reschedule | Accessible disks, safe ownership and surviving capacity required; guest memory/sessions lost on ordinary restart     |
| Partition/quorum loss              | HA isolation/datastore/locking policies; storage/control-plane quorum separate    | pmxcfs read-only without quorum; isolated HA nodes may self-fence      | etcd majority, storage quorum and safe node remediation/fencing                             | Protective outage can be correct behavior; do not force competing writers or bypass quorum                           |
| Storage/network failure            | Array/vSAN/multipath/NSX/network protection                                       | Ceph/ZFS/external storage and redundant paths                          | CSI/storage/ODF and redundant fabric                                                        | HA cannot recreate missing data or a broken LAN. App/multicast rejoin and traffic recovery separate                  |
| Management access/hub fails        | Host execution/HA may continue; central orchestration impaired                    | Use another VE node; PDM remote clusters continue independently        | CLI/API if console lost; healthy local clusters survive ACM hub loss                        | Loss of UI is different from API/quorum failure; backups/credentials/access recovery needed                          |
| Planned maintenance                | Eligible vMotion/DRS evacuation and supported rolling/live patches                | VM live migration; **LXC restart migration**, HA maintenance policies  | Eligible VM live migration; pods drain/replace, disruption budgets and Operator updates     | Requires compatible CPUs/devices/storage, spare resources, networking; passthrough/local storage can block migration |
| Fault-tolerant continued execution | FT for eligible VMs, constraints separate; not for vCenter in selected VCF design | Equivalent lockstep VM facility not established                        | Equivalent lockstep VM facility not established                                             | Do not describe a reboot, replica promotion or live migration as the same protection                                 |
| Site fails                         | Entitled SRM/Protection and Recovery/ACC/cloud recovery plus destination          | PBS sync/restore or validated replication with operator recovery plan  | Entitled ODF/ACM DR or OADP/partner restore plus alternate site                             | Infrastructure/app recovery order, data authority, traffic and tested failback needed; local HA is insufficient      |

Evidence: [VMware technical/recovery documentation](#c2), [VE/PBS guides](#c4),
[OpenShift virtualization/HA](#c6), [backup/DR sources](#c10). Automatic actions
exist only when configured and supported; no universal automatic failback to the
original host/site is inferred.

Minimum versus resilient topology: a vSphere two-host HA concept does not
establish a complete VCF deployment; documented VCF vSAN OSA HA model requires
four hosts. VE recommends three nodes for reliable HA quorum; two-node clusters
can use an external QDevice vote, which is not data/capacity. OpenShift supports
single-node/compact/standard alternatives, but single-node Virtualization lacks
HA/live migration; resilient control plane uses quorum and multiple eligible
workers. Storage replicas/witnesses, separate power/network failure domains and
N+failure capacity must be sized for the actual design. [C2](#c2), [C4](#c4),
[C6](#c6).

After host loss: establish safe failure/fencing, restart VM or place replacement
pod, recover accessible persistent data, allow guest/database startup, then
expose ready endpoints and restore multicast membership. Existing app replicas
may continue serving if state/quorum/failure-domain design allows. Planned live
migration preserves eligible VM running state; failure recovery
reboots/replaces. Failback requires repairing/validating the host, controlled
placement and, for DR, reverse/reseed replication and agreed traffic cutback.

Recovery time objective (RTO) is tolerated service-restoration duration;
recovery point objective (RPO) is tolerated data-loss exposure.
Detection/fencing, storage attach, boot, database recovery and traffic all
affect RTO; write consistency, replica lag and usable backup age affect RPO. No
measured times, universal zero-loss guarantee or availability score is
justified. Review current upgrade/security risks, including VMware's Oct9
Supervisor schema advisory, and each product's maintenance constraints.
[C2](#c2), platform risk sections.

## Backup and disaster recovery

| Protected scope                            | VMware stack                                                                                  | Proxmox stack                                                                                         | Red Hat stack                                                                                                  | Consistency                                                                                                              |
| ------------------------------------------ | --------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| Host/manager configuration                 | Supported vCenter/VCF/Supervisor state backups                                                | Explicit VE/pmxcfs, PDM, PBS host/config/key protection; not automatic full bare-metal restore        | RHEL/libvirt config, Satellite/AAP backups; OCP etcd/static resources separately                               | Rebuild compatible management/identity/network before workload recovery; VM jobs alone do not capture all infrastructure |
| VM                                         | Qualified VADP/VDDK partner backup; selected native vSAN protection                           | vzdump to file/PBS; full VM and supported file/live restore                                           | VM/CSI snapshots, OADP or Kasten/partner, RHEL guest protection                                                | Included disks only; guest agents/quiesce improve consistency but do not prove database/application consistency          |
| System container / local runtime           | Guest/image/config/data tools; no selected native ESX LXC                                     | LXC vzdump includes selected managed mounts; **bind/device mount data excluded**                      | Podman config/Quadlet/images plus volumes/bind mounts/application tools                                        | Image/container export is not durable-data backup; external mounts/secrets/registry need explicit coverage               |
| Kubernetes objects and persistent app data | Qualified Velero/vSphere plugin/partner plus app hooks; exact3.8 plugin pairing unverified    | Separate etcd/objects/volume/app tools; chosen complete Velero stack unverified                       | OADP 1.6 or Kasten 9.0.9 plus compatible CSI/object storage/app hooks; etcd separately                         | Independent VM-node snapshots do not establish cluster/app-consistent recovery. OADP is not full-cluster/etcd DR         |
| Retention/off-site/immutability            | Product/repository and native snapshot entitlement specific; independent copies/keys required | PBS verify/prune/garbage collection, remote sync, tape/WORM; supported S3 with local persistent cache | Supported object/CSI/data-mover destinations, partner export; object-lock and key custody qualified separately | Protected flag/snapshot/cloud bucket is not automatically administrator-proof immutability or separate failure domain    |
| Site recovery                              | Entitled recovery service, paired sites/storage/cloud and plans                               | Independent PBS/copies or validated storage replicas, spare site and manual orchestration             | ODF Metro/Regional DR with ACM/entitlement or restore to compatible site                                       | Async data/backup points expose later writes; recovery order and failback differ from local restart                      |

Sources and tools: [C2](#c2), [C3](#c3), [C4](#c4), [C10](#c10). All require
schedules, retention, backup-job monitoring, separate credentials/key copies,
application-consistency procedures and restore validation. PBS S3 support in4.2
is current supported capability, not the older preview status; it does not
establish universal Object Lock behavior. VMware lists SRM and Live Recovery
Cloud as separately purchased add-ons, so recovery-site rights follow the
order, not the core VVF/VCF edition. Red Hat's January 2026 subscription guide
lists OADP as included for OVE as well as OKE/OCP/Plus; confirm it in the
order.

**VM restore:** select clean usable point, restore keys/access, isolate target,
map disks/networks, restore VM/configuration and excluded data, validate
guest/database, then enable traffic. **Application restore:** recover compatible
cluster/storage/Operators/CRDs, resources/secrets and consistent data, control
startup order, validate database/app state, then redirect endpoints. Site order
also includes DNS/time/identity, backup access, management, registry,
storage/compute/control planes and application dependencies. Failback needs
data-authority checks and controlled reprotection; snapshots/replicas do not
replace retained backups.

## Other capabilities and operations

| Capability / tradeoff | VMware                                                                               | Proxmox                                                                                                    | Red Hat                                                                                             |
| --------------------- | ------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| Compute/isolation     | Mature VM resource/mobility ecosystem, supported device/CPU constraints              | KVM VM kernels plus lighter shared-kernel LXC; optional official Arm path differs                          | RHEL KVM/Podman or Kubernetes-managed VMs/pods; strong kernel/security-context distinctions         |
| Storage               | vSAN/VMFS/NFS/qualified arrays, policy storage/CSI; capacity rights matter           | Local ZFS/LVM, NFS/iSCSI/Ceph and provider integrations; type dictates migration/snapshot/replica features | CSI/PVC classes, certified external storage or ODF; RWX/fencing and driver support central          |
| Security/identity     | RBAC/federation/broker, encryption/vTPM, NSX; advanced security/compliance separate  | RBAC/realms/API tokens/MFA, firewall/AppArmor/seccomp and guest controls                                   | SELinux/RBAC/OAuth/SCC, compliance/security Operators; ACS/Quay/Plus rights separate                |
| Updates/lifecycle     | Core fleet/host and asynchronous VKS/service versions need coordinated compatibility | Debian/APT/enterprise streams, Ceph lifecycle, guest/Kubernetes separate; Offline Mirror optional          | RHEL DNF/bootc/Satellite versus OCP Cluster Version/Machine Config/Operator updates                 |
| Automation            | vSphere/VCF APIs, SDK/CLI/PowerCLI, Automation/IaC with proper rights                | GUI/CLI/REST/Cloud-Init/PDM; community Ansible/Terraform provider support distinct                         | libvirt/Podman APIs, oc/Kubernetes/GitOps; separate AAP and certified collections                   |
| Monitoring/operations | Operations/log/network services, product-specific licensing                          | Native graphs/tasks/notifications/PDM plus Zabbix/provider tools                                           | Cluster monitoring/alerts, ACM/observability/ACS and guest tools                                    |
| Hardware/scale        | Compatibility/configmax and management/storage sizing required                       | Supported CPUs/storage, low-latency cluster/quorum; no universal guide node ceiling                        | Certified hardware/guest/CSI and tested OCP/Virtualization/ACM limits; not universal density        |
| Operational fit       | VM/private-cloud expertise and management footprint                                  | Integrated VM/LXC infrastructure; team owns guest app/Kubernetes integration                               | RHEL simpler per-host; OpenShift adds integrated desired state with more platform skills/components |

Evidence: [C1](#c1), [C2](#c2), [C4](#c4), [C6](#c6), [C8](#c8), [C12](#c12).
These are qualitative operational implications; no invented benchmark, staffing
ratio, density guarantee or weighted winner is asserted.

## Licensing, support, and required add-ons

| Offering                                              | Capabilities                                                                                                                           | Rights / extras                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ----------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| VMware VVF vs VCF                                     | VVF: vSphere/vCenter/VKS/selected Operations/vSAN; VCF adds NSX, Automation and broader fleet/network services                         | Subscription physical cores, minimum16 per processor; vSAN allowance0.25 TiB/core VVF vs1 TiB/core VCF subject to terms. Guest, extra capacity, advanced services and backup are separate. SRM and Live Recovery Cloud are separately purchased Advanced Services for both VVF and VCF. **Quote required**. [C1](#c1) footnotes 13–14, [C5](#c5)                                                                                                       |
| VMware standalone / Edge / free                       | Standard/Enterprise Plus through8U3, Edge optimized edge-only alternative, free ESXi 8U3 distinct                                      | Exact order/region/term/support and advanced recovery rights need confirmation; no9.1 standalone rights inferred.9.x licensing requires Operations/vCenter and compliance workflow. [C5](#c5)                                                                                                                                                                                                                                                          |
| Proxmox free / Community / Basic / Standard / Premium | Same full VE/PBS features; paid service changes repository/support coverage                                                            | VE per occupied CPU socket/year, PBS per backup server/year. PDM has no separate subscription; enterprise repository needs>=80% remotes Basic+. Guest/partner/backup hardware/cloud charges separate. [C4](#c4), [C15](#c15)                                                                                                                                                                                                                           |
| RHEL Server / Virtual Datacenters / developer option  | OS/KVM/Podman; unlimited guest model or qualified no-cost individual16-system option                                                   | Socket/virtual-node/SKU terms and support tier matter; RHEL base is not OpenShift/Satellite/AAP/backup. Developer eligibility not enterprise support. [C7](#c7), [C8](#c8)                                                                                                                                                                                                                                                                             |
| OVE / OKE / OCP / Platform Plus                       | OVE VM-only; OpenShift Kubernetes Engine (OKE) runtime+VMs; OCP developer platform; Plus adds ACM/ACS/Quay/ODF Essentials within terms | OVE bare-metal node; other eligible core-pair/node options. OVE RHEL guest rights separate; qualifying OKE/OCP/Plus guest rights documented. OADP is listed as included for all four editions; DR Hub/Cluster Operators only for Plus. One product type per cluster: OVE and OCP/Plus nodes cannot be mixed. Plus storage/managed-node limits and ODF Advanced/DR extra rights need confirmation. **Quote required** complete stack. [C7](#c7) pp7, 29 |
| Red Hat companions / partner products                 | HA, Satellite, AAP, storage/DR, security/registry/fleet and Kasten fill specific gaps                                                  | Separate products/subscriptions or limited bundle rights; installing an Operator does not grant entitlement. Standard/Premium changes coverage; guest/application licenses remain separate. [C6](#c6), [C7](#c7), [C10](#c10)                                                                                                                                                                                                                          |

**Published prices verified2026-10-30:** Proxmox Austrian vendor English online
offering, EUR net of VAT, one-year term: VE Community/Basic/Standard/Premium
**€120/€370/€550/€1,100 per occupied socket**; PBS **€560/€1,120/€2,240/€4,480
per server**. Premium24/7 began Oct19; Standard24/7 is scheduled by end2026, not
already delivered. Response times are initial critical-case response
commitments, not resolution or application availability. All subscribed nodes in
one VE cluster require the same tier. [C15](#c15).

Red Hat US storefront, USD, one-year displayed RHEL Server SKU examples:
Self-support **US$383.90**, Standard **US$878.90**, Premium **US$1,428.90**;
validate physical/virtual quantity, regional eligibility, taxes and selected
add-ons. These are not prices for OpenShift or an entire cluster. VMware
selected-stack and Red Hat OpenShift/companion complete-stack prices remain
**quote required**. [C16](#c16).

Relevant stack additions: VMware advanced services include ACC, advanced
security, load balancing, application/data services, network observability,
business operations, identity security and extra vSAN capacity; Proxmox
companion products are PBS, PDM and Offline Mirror plus supported provider
integrations; Red Hat adds ACM, ACS, Quay, ODF/DR, OADP, Satellite, AAP and
release-compatible networking/delivery Operators according to edition. Full
inventories and uncertain independent product versions are retained in the
platform reports. Catalog inclusion is not a commercial entitlement. [C1](#c1),
[C4](#c4), [C6](#c6), [C7](#c7).

No total cost of ownership can be calculated without cores/sockets/nodes,
capacity, growth, support tier, sites, storage/network hardware, backup
retention, guest/application contracts and staff capabilities. Published support
prices should not be compared as though they buy the same stack or
responsibility scope.

## Conditional recommendations

| Scenario                           | Proposed stack                                                                                                                                                       | Tradeoff / unknowns                                                                                                                                                                                                                                                     |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| VM-focused incumbent VMware estate | VVF 9.1.1 plus certified storage/network and qualified backup; VCF when NSX/private-cloud automation/fleet services needed                                           | Preserve certified appliance/operations dependencies; verify upgrade path, management footprint, quote and needed recovery/FT features before assuming migration saves cost                                                                                             |
| Kubernetes-focused applications    | OCP 4.22 with certified CSI/network, OADP/partner backup; add Virtualization for VMs and ACM for fleet. VKS 3.8 is a documented alternative in a VMware-led platform | Team's Kubernetes/vSphere skills, application Operator ecosystem, guest rights, CNI/CSI and support requirements determine fit; avoid independently latest unsupported combinations                                                                                     |
| Mixed VMs and containers           | Kubernetes-led: OKE/OCP/Plus+Virtualization. VM-led: VVF/VCF+VKS or VE+LXC/guest containers with separate orchestration                                              | “Container” must mean system container or application pod explicitly. Proxmox central VM/LXC management is not supported Kubernetes service; OVE alone does not grant end-user app-container rights, and one OpenShift cluster cannot mix OVE nodes with OCP/Plus nodes |
| Cost-sensitive small deployment    | VE 9.2 + separately protected PBS 4.2; add paid tier/PDM as support/fleet needs require. For a few Linux services, RHEL 10.2/Podman is another host-level choice     | Free feature access does not eliminate support, quorum, backup hardware or operating skill costs. Single host cannot provide host-failure HA; quote designs using actual capacity/recovery needs                                                                        |
| External-LAN multicast dependent   | Qualify VM bridge/VLAN path, or specific documented VKS IPv4 secondary/Antrea or OCP SR-IOV pod path                                                                 | Need family/groups/ports/source-specific semantics, throughput, topology and security. No unconditional dual-stack container recommendation; physical fabric/NIC and support confirmation can dominate platform choice                                                  |
| VM-only Red Hat migration          | OVE + certified bare-metal storage/network + backup + guest subscriptions; MTV for supported source migration                                                        | OVE commercial restrictions differ from OCP; validate source/target versions, guest conversion and recovery. OADP is listed as included for OVE. Guest/app containers require core-pair entitlement of those VMs or changing the whole cluster's product type           |

These are recommendations to evaluate named stacks under stated conditions, not
unconditional deployment/support assurances. No platform is selected solely by
marketing feature counts or list support price.

## Migration and portability

VMware-to-Proxmox import requires guest firmware/disk/controller/driver changes,
storage/network mapping and application/license validation. The current VE guide
retains technology-preview status for its ESXi import wizard; do not treat that
as an unconditional supported production migration service. Independent vendor
backup conversion paths need their own current matrices. [C4](#c4), [C10](#c10).

MTV 2.12 documents supported VMware/RHV/OpenStack/Hyper-V source combinations
and OCP/Virtualization destinations; check exact source version, guest
conversion, disk/network mapping, cutover and rollback. RHV 4.4 is a legacy
lifecycle/migration issue rather than a new-platform baseline. Moving to
OpenShift changes operational objects, identities, storage/backup/fencing and
skills as well as disks. VMware/Proxmox/Red Hat cross-cluster migration
capabilities do not imply generic cross-hypervisor live migration. [C6](#c6),
[C13](#c13).

OCI images and Kubernetes manifests help move applications, but security
contexts, privileged/host networking, storage classes, CSI snapshots, CNI/IP
assumptions, registry/secrets, Operators and architecture can bind them to a
stack. LXC system containers may need conversion/rebuild as VMs or app
containers because of shared-kernel and filesystem assumptions. Windows
kernel/image and application licensing still apply.

PBS backup formats, vSphere snapshots/replicas and CSI/Kasten/OADP recovery
points are not universally interchangeable. Preserve tested guest/disk exports,
manifests/configuration and application-native database exports/logs; qualify
target recovery and keys before retiring the source. Management inventory can
coexist through automation/monitoring, but neither shared dashboards nor open
formats eliminate support boundaries or migration testing. No benchmark or
quantified migration effort is invented.

## Open questions and proposed validation

Prioritized selection/procurement questions:

1. Inventory VM/OS/application support requirements, Windows/Linux container
   needs, privileged networking, PCI/GPU/SR-IOV devices and storage features.
   Clarify system-container versus application-container intent.
1. Supply hosts, CPUs/cores/sockets, sites, capacity/growth, certified
   hardware/storage/NICs, staff skills, existing entitlements, support hours and
   budget. Obtain version-specific support/entitlement quotes for the complete
   stack, not just hypervisor.
1. Define availability and recovery targets per application: RTO/RPO, acceptable
   restart/session loss, synchronous/asynchronous state, retained backups,
   independent immutable copies and site failback.
1. Specify multicast family, groups/source semantics, ports, hop limits,
   L2/routed topology, external senders/receivers, throughput and
   membership/rejoin/loss requirements. Confirm vendor support for the complete
   proposed path, especially IPv6, Windows, secondary NICs and policy behavior.
1. Resolve evidence gaps: exact enterprise/errata patches;
   guest/hardware/optional-service matrices; VMware SRM/Live Recovery SKUs, RPO
   tiers and ACC rights; order confirmation of documented OVE OADP inclusion and
   current ODF Advanced/DR terms; Proxmox support-transition contract
   and newest Veeam plug-in/build pairing. Obtain gated sources through normal
   entitled access.

**Proposed proof of concept, not performed:** build the smallest supported
topology meeting the chosen failure domains; provision a representative VM and
stateful app, configure identity/audit/updates, and document exact
versions/rights. Test manager/console/link loss separately from cluster quorum,
worker, storage, network and whole-site failures. Verify safe fencing, surviving
capacity, volume ownership, guest/pod recovery, application consistency and
traffic. Exercise planned migration/drain/rolling update and controlled
failback. Restore VM, excluded mount data, Kubernetes objects and database/PVC
data into isolation; recover keys and test independent copy
retention/immutability and site dependency order. Measure outcomes against
agreed targets.

For multicast, run joined senders/receivers both directions for VM↔VM,
container↔container, VM↔container and external LAN: same host, cross host, then
routed subnets separately. Record IPv4/IPv6 independently. Inspect endpoint
joins, IGMP/MLD queries/reports/leaves, bridge/vDS/OVS/VF membership, physical
switch/router state and policy drops; capture at runtime/guest interface, host
uplink and physical receiver. Repeat after migration, HA restart, rescheduling,
membership aging and querier/link failure. Include negative policy/isolation
checks, particularly OVN multicast NetworkPolicy exemption. Successful unicast
or one local multicast test is insufficient evidence for other paths.

## References

All sources accessed **2026-10-30**. Material claims link to these primary
sources and standalone report sections. Publication/update dates below are
recorded where available; rolling pages otherwise have no reliable displayed
date. Platform bibliographies retain the full inventory and all failed
discovery/access URLs; no source was assumed read through an authentication
wall.

### C1

**C1 — VMware offerings/capability inventory:** Broadcom, *VCF/VVF 9.1.1 Feature
Comparison & Upgrade Paths*,Oct14 2026. [Original
PDF](https://www.vmware.com/docs/vmware-cloud-foundation-9-1-feature-comparison-and-upgrade-paths),
[local](reference/vmware-vcf-vvf-9-1-1-feature-comparison-2026-10-14.pdf).

### C2

**C2 — VMware architecture/BOM/availability/network/recovery:** Broadcom, *VCF
9.1.x technical documentation* and9.1.1 BOM, updatedOct29 2026.
[BOM](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-1/release-notes/vmware-cloud-foundation-9-1-1-0-release-notes/vmware-cloud-foundation-9-1-1-0-bill-of-material.html),
[original
PDF](https://techdocs.broadcom.com/content/dam/broadcom/techdocs/us/en/pdf/vmware/vcf/vcf-90/vmware-cloud-foundation-9-1.pdf),
[local](reference/vmware-cloud-foundation-9-1-technical-documentation.pdf).

### C3

**C3 — VMware supported Kubernetes path:** Broadcom, *VKS 3.8* and *VKr release
notes*,Oct22 2026:
[VKS](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-service-administration-and-development/9-1/release-notes/vks-release-notes/vmware-tanzu-kubernetes-grid-service-38-release-notes.html),
[VKr](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-service-administration-and-development/9-1/release-notes/vmware-vkr-release-notes.html).
*Service Administration/Development9.1*: [original
PDF](https://techdocs.broadcom.com/content/dam/broadcom/techdocs/us/en/pdf/vmware/vcf/Supervisor-Async/vmware-cloud-foundation-service-administration-and-development-9-1.pdf),
[local](reference/vmware-vcf-service-administration-development-9-1.pdf); PDF
lags3.8 HTML, used for architecture/multi-network/Velero with qualification.

### C4

**C4 — Proxmox core/companion operations:** Proxmox, *VE Administration
Guide9.2.13*,Sep24 2026: [original
PDF](https://pve.proxmox.com/pve-docs/pve-admin-guide.pdf),
[local](reference/proxmox-ve-9-admin-guide.pdf). *PBS 4.2.8-1
Documentation*,Oct2:
[original](https://pbs.proxmox.com/docs/proxmox-backup.pdf),
[local](reference/proxmox-backup-4-2-guide.pdf). *PDM 1.1.9
Documentation*,Oct14:
[original](https://pdm.proxmox.com/docs/proxmox-datacenter-manager.pdf),
[local](reference/proxmox-datacenter-manager-1-1-guide.pdf).
HA/backup/management/support boundaries; feature entitlement distinguished from
support.

### C5

**C5 — VMware commercial rights/delivery:** Broadcom, *VCF SPD*,June2026
[original](https://ftpdocs.broadcom.com/cadocs/0/VCF_SPD_June2026.pdf),
[local](reference/vmware-vcf-spd-june-2026.pdf); *VVF SPD*,June2026
[original](https://ftpdocs.broadcom.com/cadocs/0/VVF_SPD_June2026.pdf),
[local](reference/vmware-vvf-spd-june-2026.pdf); *vSphere9.1 FAQ*,May2026
[original](https://www.vmware.com/docs/vsphere-9-1-faq),
[local](reference/vmware-vsphere-9-1-faq-may-2026.pdf). KB458772 [standalone
licensing
dependencies](https://knowledge.broadcom.com/external/article/458772/licensing-standalone-esxi-hosts-in-vmwar.html),Oct21.
Order-specific terms take precedence over feature marketing.

### C6

**C6 — Red Hat mixed-workload platform/compatibility:** Red Hat, *OCP 4.22
Virtualization*,updatedOct29 2026 [original
PDF](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/pdf/virtualization/OpenShift_Container_Platform-4.22-Virtualization-en-US.pdf),
[local](reference/rhel-openshift-4.22-virtualization.pdf); [Operator
lifecycle/compatibility](https://access.redhat.com/support/policy/updates/openshift_operators),
rolling; [ACM 2.17
docs](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.17),
rolling.

### C7

**C7 — Red Hat editions/rights/metrics:** Red Hat, *Self-managed OpenShift
subscription guide*,Jan23 2026
[HTML](https://www.redhat.com/en/resources/self-managed-openshift-subscription-guide),
[original
PDF](https://www.redhat.com/rhdc/managed-files/cl-self-managed-openshift-subscription-guide-3202913pr-202601-en.pdf),
[local](reference/rhel-openshift-subscription-guide-202601.pdf); *RHEL
subscription guide*,Jul21 2026
[guide](https://www.redhat.com/en/resources/red-hat-enterprise-linux-subscription-guide).
OVE/OKE/OCP/Plus, guest and support terms.

### C8

**C8 — RHEL host/runtime:** Red Hat, *RHEL 10.2 Release Notes* [original
PDF](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/pdf/10.2_release_notes/Red_Hat_Enterprise_Linux-10-10.2_Release_Notes-en-US.pdf),
[local](reference/rhel-10.2-release-notes.pdf); *RHEL 10 Containers*
[original](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/pdf/building_running_and_managing_containers/Red_Hat_Enterprise_Linux-10-Building_running_and_managing_containers-en-US.pdf),
[local](reference/rhel-10-container-guide.pdf); *Linux VMs*
[original](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/pdf/configuring_and_managing_linux_virtual_machines/Red_Hat_Enterprise_Linux-10-Configuring_and_managing_Linux_virtual_machines-en-US.pdf),
[local](reference/rhel-10-linux-virtual-machines.pdf). Rolling current versioned
documentation.

### C9

**C9 — OpenShift multicast:** Red Hat, *OCP 4.22 OVN-Kubernetes*
[HTML](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/ovn-kubernetes_network_plugin/index),
[original
PDF](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/pdf/ovn-kubernetes_network_plugin/OpenShift_Container_Platform-4.22-OVN-Kubernetes_network_plugin-en-US.pdf),
[local](reference/rhel-openshift-4.22-ovn-kubernetes.pdf); *Hardware networks*
[HTML](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/hardware_networks/index),
[original
PDF](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/pdf/hardware_networks/OpenShift_Container_Platform-4.22-Hardware_networks-en-US.pdf),
[local](reference/rhel-openshift-4.22-hardware-networks.pdf). Rolling documented
pod/SR-IOV paths and policy limits.

### C10

**C10 — Backup/DR support scopes:** Veeam, [vSphere
matrix](https://helpcenter.veeam.com/docs/vbr/userguide/platform_support_vm.html),
[Proxmox
matrix](https://helpcenter.veeam.com/docs/vbr/userguide/platform_support_proxmox.html)
(Oct22 2026 update), [Kasten current
support](https://docs.kasten.io/latest/operating/support/), [release
notes](https://docs.kasten.io/latest/releasenotes/) (9.0.9 Oct22). Red Hat, [OCP
4.22
backup/restore](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/backup_and_restore/index),
[ODF 4.22
DR](https://docs.redhat.com/en/documentation/red_hat_openshift_data_foundation/4.22/html/configuring_openshift_data_foundation_disaster_recovery_for_openshift_workloads/metro-dr-solution).
Broadcom [vSAN Protection and
Recovery](https://blogs.vmware.com/cloud-foundation/2026/05/14/vmware-vsan-protection-and-recovery-enhancements-for-vcf-9-1/),May14
2026\. Full related public PDFs/source inventories in platform reports; a support
matrix is not an entitlement grant.

### C11

**C11 — Upstream multicast mechanisms:** Linux kernel project, [Ethernet
Bridging](https://docs.kernel.org/networking/bridge.html), rolling; Antrea
project, [2.7 multicast
guide](https://antrea.io/docs/v2.7.0/docs/multicast-guide/), versioned. IGMP/MLD
and IPv4/Linux/Windows/policy limits; upstream capability distinguished from
end-to-end commercial support.

### C12

**C12 — Mixed-vendor support boundaries:** Red Hat, [Ansible Certified Content
FAQ](https://access.redhat.com/articles/4916901),Sep25 2026;
[certified/validated
content](https://access.redhat.com/articles/ansible-automation-platform-certified-content),Jul20;
Ansible community,
[community.proxmox2.0.0](https://docs.ansible.com/projects/ansible/latest/collections/community/proxmox/index.html),
rolling; Broadcom [Operations appliance on Proxmox
policy](https://knowledge.broadcom.com/external/article/425448/compatibility-and-support-policy-for-vmw.html).
Distinct workflow and provider support scopes.

### C13

**C13 — Release/migration evidence:** Red Hat/OpenShift [stable4.22
manifest](https://mirror.openshift.com/pub/openshift-v4/clients/ocp/stable-4.22/release.txt),
accessed cutoff; *MTV 2.12 Planning* [original
PDF](https://docs.redhat.com/en/documentation/migration_toolkit_for_virtualization/2.12/pdf/planning_your_migration_to_red_hat_openshift_virtualization/Migration_Toolkit_for_Virtualization-2.12-Planning_your_migration_to_Red_Hat_OpenShift_Virtualization-en-US.pdf),
[local](reference/rhel-mtv-2.12-planning.pdf); [RHV
lifecycle](https://access.redhat.com/support/policy/updates/rhev), rolling.
Source/target matrices matter.

### C14

**C14 — Proxmox current catalogs/package observations:** Proxmox,
[downloads](https://www.proxmox.com/en/downloads), [release
catalog](https://proxmox.com/en/about/company-details/press-releases), rolling
throughOct29 2026. [Public VE
index](http://download.proxmox.com/debian/pve/dists/trixie/pve-no-subscription/binary-amd64/Packages.gz),
[PBS
index](http://download.proxmox.com/debian/pbs/dists/trixie/pbs-no-subscription/binary-amd64/Packages.gz),
[PDM
index](http://download.proxmox.com/debian/pdm/dists/trixie/pdm-no-subscription/binary-amd64/Packages.gz);
public HTTP observations, not authenticated enterprise-channel verification.

### C15

**C15 — Proxmox current support pricing:** Proxmox Austrian vendor, [VE
pricing/FAQ](https://www.proxmox.com/en/products/proxmox-virtual-environment/pricing),
[PBS
pricing/FAQ](https://www.proxmox.com/en/products/proxmox-backup-server/pricing),
checkedOct30 2026. EUR net annual metric, support coverage dates and tier
conditions; downloaded January agreements with older coverage wording in
platform report.

### C16

**C16 — Red Hat published host price:** Red Hat, [US RHEL Server
storefront](https://www.redhat.com/en/store/red-hat-enterprise-linux-server),
checkedOct30 2026, USD one-year SKU examples; not a complete-stack quote.

### C17

**C17 — VKS multi-network overview:** Broadcom, [*VCF 9.1 Brings
Multi-Network Support to VMware vSphere Kubernetes Service*](https://blogs.vmware.com/cloud-foundation/2026/06/02/vcf-9-1-brings-multi-network-support-to-vsphere-kubernetes-service/),
published2026-06-02, accessed2026-11-02. Explains node-level secondary
interfaces, their distinction from pod-level multi-NIC, and NSX VPC/VDS scope.

### C18

**C18 — Multus multi-network behavior and license:** Kubernetes Network
Plumbing Working Group, [Multus CNI repository](https://github.com/k8snetworkplumbingwg/multus-cni)
and [usage guide](https://github.com/k8snetworkplumbingwg/multus-cni/blob/master/docs/how-to-use.md),
accessed2026-11-02. Apache-2.0 license; Multus delegates extra pod interfaces
to other CNI plugins and does not itself supply their network implementation.

### References - unresolved

All issues/access attempts refer to **2026-10-30**. Detailed failed URLs and
substitutes are retained in each platform's unresolved-reference section:
[VMware](research-vmware-r1.0.1.md#references---unresolved),
[Proxmox](research-proxmox-r1.0.1.md#references---unresolved), [Red
Hat](research-rhel-r1.0.1.md#references---unresolved).

| Source / intended evidence                                                                                                                                                                          | Limitation and affected conclusion                                                                                                                             | Next step                                                                                                                   |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| [Broadcom compatibility](https://compatibilityguide.broadcom.com/), [configuration maximums](https://configmax.broadcom.com/), [lifecycle](https://support.broadcom.com/group/ecx/productlifecycle) | Exact proposed hardware/guest/optional-service lookup and every latest lifecycle/patch not retrieved; portal/interactive qualification remains                 | Obtain applicable certified results/current matrices; core BOM/VKS notes do not certify arbitrary targets                   |
| [HTTPS Proxmox package index](https://download.proxmox.com/debian/pve/dists/trixie/pve-no-subscription/binary-amd64/Packages.gz)                                                                    | Hostname certificate validation failed; HTTP public observations recovered, enterprise/signed latest set unverified                                            | Use normally authenticated signed enterprise metadata during deployment; no TLS verification disabled                       |
| [Veeam migration guide](https://www.veeam.com/whitepapers/veeam-hypervisor-migration-guide-vmware-proxmox-ve_wp.pdf)                                                                               | Official web PDF extraction read2026-11-02. Version1.0 describes full recovery with on-the-fly conversion; it says cross-hypervisor on-the-fly conversion only works with Proxmox as source. Direct download still returns HTML, so no valid local PDF retained. | Use as a scoped migration reference, not a universal conversion guarantee; obtain a valid downloadable copy if the project requires a local source artifact. |
| [ACM 2.17 support matrix](https://access.redhat.com/articles/7142376)                                                                                                                               | Subscriber-exclusive detailed body; exact third-party distributions/operations/scale unresolved                                                                | Entitled review before mixed-vendor commitment                                                                              |
| [Podman rootless multicast solution](https://access.redhat.com/solutions/7033979)                                                                                                                   | RHEL 8/9 public summary, subscriber body not read; not applied to RHEL 10.2                                                                                    | Obtain current release-specific support evidence; default external multicast remains unverified                             |
| [OVE overview PDF](https://www.redhat.com/rhdc/managed-files/cl-openshift-virtualization-engine-overview-1689750pr-202502-en_0.pdf)                                                                 | Initial503 resolved on final public retry; [valid local overview](reference/rhel-openshift-virtualization-engine-overview-2025.pdf) saved, metadata May13 2025 | Current subscription guide governs edition facts and lists OADP for OVE (p29); current ODF Advanced terms remain unverified |

Browser-denied Broadcom pages/Proxmox HTML were often recovered through normal
public direct HTML/PDF downloads. That resolves content access where stated, not
every deployment-specific support question. No unavailable source is claimed
read, and no field tests were run.

**r1.0.1 rerun (2026-10-31 01:03–01:04 UTC, same review day local time):**
216 unique URLs; 140 HEAD 2xx, 9 GET 2xx after HEAD failure, 67 unresolved.
docs.redhat.com returned HTTP 403 to every scripted request (54 URLs), including
documents whose PDFs are saved and were read locally. That is an access
observation, not evidence against those sources. Per-URL results are in the
link-check log. The table below is the baseline probe, kept for history.

Final link verification on **2026-10-30** also observed the following
unsuccessful **HTTP HEAD** probes. These do not revoke earlier successful
content reads or valid local PDF copies. A HEAD response is a link-availability
observation, not a support determination. Full methods/results, including
successful GET retries and uncollected preliminary requests, are retained in
[the link-check log](research-link-checks-r1.0.1.tsv). Retry normal public
access or
use the cited local PDF; deployment-specific support gaps remain as stated
above.

| URL                                                                                                                                                                                                                               | Final probe result        | Evidence effect / next step                                                                                                              |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| [Source endpoint](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/hardware_networks/index)                                                                                                 | Timed out after18 seconds | Live HEAD unresolved; previously read content/local PDF remains usable where cited. Retry vendor endpoint; no additional claim inferred. |
| [Source endpoint](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/pdf/hardware_networks/OpenShift_Container_Platform-4.22-Hardware_networks-en-US.pdf)                                                 | Timed out after18 seconds | Live HEAD unresolved; previously read content/local PDF remains usable where cited. Retry vendor endpoint; no additional claim inferred. |
| [Source endpoint](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/pdf/ovn-kubernetes_network_plugin/OpenShift_Container_Platform-4.22-OVN-Kubernetes_network_plugin-en-US.pdf)                         | Timed out after18 seconds | Live HEAD unresolved; previously read content/local PDF remains usable where cited. Retry vendor endpoint; no additional claim inferred. |
| [Source endpoint](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/pdf/10.2_release_notes/Red_Hat_Enterprise_Linux-10-10.2_Release_Notes-en-US.pdf)                                                           | HTTP503                   | Live HEAD unresolved; previously read content/local PDF remains usable where cited. Retry vendor endpoint; no additional claim inferred. |
| [Source endpoint](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/pdf/building_running_and_managing_containers/Red_Hat_Enterprise_Linux-10-Building_running_and_managing_containers-en-US.pdf)               | HTTP503                   | Live HEAD unresolved; previously read content/local PDF remains usable where cited. Retry vendor endpoint; no additional claim inferred. |
| [Source endpoint](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/pdf/configuring_and_managing_linux_virtual_machines/Red_Hat_Enterprise_Linux-10-Configuring_and_managing_Linux_virtual_machines-en-US.pdf) | HTTP503                   | Live HEAD unresolved; previously read content/local PDF remains usable where cited. Retry vendor endpoint; no additional claim inferred. |
| [Source endpoint](https://docs.redhat.com/en/documentation/red_hat_openshift_data_foundation/4.22/html/configuring_openshift_data_foundation_disaster_recovery_for_openshift_workloads/metro-dr-solution)                         | HTTP503                   | Live HEAD unresolved; previously read content/local PDF remains usable where cited. Retry vendor endpoint; no additional claim inferred. |
