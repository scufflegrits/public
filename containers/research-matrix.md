# VM and Container Platform Comparison Matrix

Research baseline: **2026-10-30**. Targeted evidence notes were added
**2026-11-02**; see the dated notes in the platform reports. This matrix
summarizes the project research. It is a desk-research comparison, not a
deployment certification or a claim that every independently current component
forms a supported combination.

## Platforms compared

Rows represent practical stacks rather than vendor names alone. VMware's VVF
and VCF bundles are separate because their included services differ. Red Hat's
OpenShift Virtualization Engine (OVE) is separate because it is a VM-only
offering, while OpenShift Container Platform (OCP) supports application
containers as well as VMs with the applicable entitlement.

## Capability and operations matrix

| Stack | Workloads it runs | Management | Availability, migration, and protection | Networking and multicast | Commercial and support boundary |
|---|---|---|---|---|---|
| **VMware VVF 9.1.1 + VKS** | ESX virtual machines; Kubernetes applications on VKS clusters. VKS worker nodes run in VMs. | vCenter manages hosts and VMs; VKS/Kubernetes APIs manage cluster workloads. VCF Operations and Automation scope differs from VVF. | Host HA normally restarts affected VMs; vMotion supports eligible planned moves. Application recovery and backup are separate layers; confirm recovery products and rights. | VM VLAN paths are **conditional**. VKS Antrea multicast is a documented, configured IPv4/Linux path; Antrea IPv6 multicast is unsupported. Node secondary interfaces provide another network path, but pods do not use it automatically. Primary network is immutable after cluster creation. | Subscription; **quote required**. VVF includes a narrower set of services than VCF. SRM and Live Recovery Cloud are separately purchased Advanced Services. Exact hardware, guest, and service compatibility require lookup. [VMware report](research-vmware-r1.0.1.md#architecture-and-workload-support), [comparison licensing](research-vm-comparison-r1.0.1.md#licensing-support-and-required-add-ons) |
| **VMware VCF 9.1.1 + VKS** | Same core VM and VKS workload types as VVF, with broader private-cloud services. | vCenter plus VCF Operations for fleet management; VCF Automation adds organization and self-service workflows. Kubernetes APIs still own application deployments. | VM HA and planned migration remain separate from application-level resilience. Backup and site recovery require their own design and entitlements. | Adds NSX and broader network services. VKS secondary-network capability depends on release and prerequisites; node-level links are separate from pod-level multi-NIC. Do not infer end-to-end application multicast from an attached interface. | Subscription; **quote required**. VCF adds NSX, Automation, and broader fleet/network services over VVF. Advanced recovery services and some capacity remain separate. Hardware/guest/service matrices are unresolved for a specific target. [VMware report](research-vmware-r1.0.1.md#verified-product-baseline), [comparison licensing](research-vm-comparison-r1.0.1.md#licensing-support-and-required-add-ons) |
| **Proxmox VE 9.2 + PBS 4.2; PDM optional** | QEMU/KVM virtual machines and native LXC system containers. Application runtimes can run inside guests. Kubernetes is a separately assembled guest-VM stack; this project's selected Kubernetes/Multus path is **not verified** end to end. | VE manages one cluster from any surviving member. PDM manages inventory/actions across independent clusters; PBS owns backup tasks and stores. Guest apps and Kubernetes remain separate management domains. | VE HA can restart VMs after failure; live migration supports eligible planned work. PBS provides a distinct backup service. Replication, backup, and site recovery are not interchangeable. | VM/LXC bridge and VLAN multicast is **conditional** on guest, bridge, firewall, and physical-network configuration. Extra VM NICs are documented. Multus can request extra pod interfaces, but the full Proxmox/Kubernetes/CNI support and multicast path are **not verified**. | VE/PBS features are available without a paid tier; subscriptions add support and enterprise repository access. VE pricing is per occupied CPU socket; PBS pricing is per backup server. Enterprise signed-package freshness remains unverified. [Proxmox report](research-proxmox-r1.0.1.md#architecture-and-workload-support), [comparison licensing](research-vm-comparison-r1.0.1.md#licensing-support-and-required-add-ons) |
| **RHEL 10.2 with KVM/libvirt and Podman** | Linux and certified Windows guests on KVM; Podman runs Linux application containers on the RHEL host or inside a Linux guest. Base RHEL is not a Kubernetes platform. | Cockpit/libvirt handles host VM work; Satellite handles OS content/provisioning; Ansible Automation Platform handles automation. They are separate products and do not create one distributed scheduler. | RHEL tools alone do not provide the same integrated cluster VM/pod lifecycle as OpenShift. HA, backup, replication, and recovery need separately selected services and application design. | VM bridges can provide a **conditional** multicast path. Container NAT/rootless paths do not establish external multicast; exact runtime, guest, firewall, and fabric behavior needs qualification. | RHEL subscription and support scope depend on SKU and deployment. Podman is documented for RHEL; Docker Engine is unsupported by Red Hat on RHEL 10. OpenShift, Satellite, automation, and backup are separate entitlements unless a bundle grants specific rights. [Red Hat report](research-rhel-r1.0.1.md#architecture-and-workload-support), [comparison licensing](research-vm-comparison-r1.0.1.md#licensing-support-and-required-add-ons) |
| **OCP 4.22 + OpenShift Virtualization 4.22.9** | Linux application pods on OpenShift; QEMU/KVM VMs managed through Kubernetes resources. Windows containers are a separate, conditional WMCO path with version-specific OS and network requirements. | The OpenShift console/API manages one cluster's hosts, VMs, and pods. Advanced Cluster Management adds fleet operations across clusters but does not merge their schedulers. | Kubernetes/Virtualization HA and VM live migration have prerequisites. Bare-metal live migration requires multiple workers, recommends at least three, and requires shared RWX storage. OADP and etcd backup protect different layers; partner products may be needed. | Project-level OVN-Kubernetes IPv4 pod multicast is documented when enabled. External-LAN multicast is **not verified** by that feature alone. Additional SR-IOV interfaces are a conditional path; IPv6/application behavior needs separate evidence. | **Quote required** for the complete edition and add-ons. OCP/OKE/Platform Plus rights differ. OADP inclusion is documented for the listed editions; ACM, storage, DR, guest, and support rights depend on the chosen edition and order. [Red Hat report](research-rhel-r1.0.1.md#architecture-and-workload-support), [comparison licensing](research-vm-comparison-r1.0.1.md#licensing-support-and-required-add-ons) |
| **OVE with OpenShift Virtualization** | VM-focused OpenShift offering. It does not grant the same application-container rights as OCP/Platform Plus; guest OS and application licensing remain separate. | Uses the OpenShift cluster console/API for VM operations. This row is for the VM-only entitlement, not a mixed OVE/OCP node pool. | Uses OpenShift Virtualization VM lifecycle and its HA/live-migration prerequisites. OADP is listed for OVE; validate what data and recovery objectives the chosen backup plan covers. | OpenShift VM networking is available subject to supported configuration. Do not infer that project pod multicast or SR-IOV pod behavior proves an external VM/application multicast path. | **Quote required**. Bare-metal node entitlement; separate RHEL guest subscriptions may apply. A cluster cannot mix OVE product type with OCP/Plus node types. [Red Hat report](research-rhel-r1.0.1.md#licensing-subscriptions-and-support), [comparison licensing](research-vm-comparison-r1.0.1.md#licensing-support-and-required-add-ons) |

## Fit at a glance

| If the main need is… | First stacks to evaluate | Main tradeoff to resolve |
|---|---|---|
| Existing vSphere VM estate with Kubernetes | VVF + VKS; VCF + VKS when NSX, automation, or broader fleet services are needed | Bundle price, feature rights, certified hardware, and separate protection entitlements |
| Integrated VM and Linux system-container operations | Proxmox VE + PBS | Team owns guest application/Kubernetes integration; enterprise support and package freshness need confirmation |
| Per-host Linux virtualization and application containers | RHEL + KVM/Podman | More host-by-host or separately assembled management; no Kubernetes control plane in base RHEL |
| Kubernetes-led operations for pods and VMs | OCP + OpenShift Virtualization | Subscription, storage/network certification, cluster skills, and HA prerequisites |
| Red Hat VM-only operations | OVE | VM-only entitlement and guest rights; changing to app-container workloads may require a different cluster product type |

These are starting points for evaluation, not universal winners. Workload
inventory, hardware, support expectations, network requirements, and recovery
targets can change the fit. The [comparison report](research-vm-comparison-r1.0.1.md)
contains the wider evidence and recommendations.

## Evidence terms and open checks

- **Documented supported** means a vendor source documents the path under its
  stated conditions.
- **Conditional** means a documented capability depends on configuration,
  version, hardware, entitlement, or another stated requirement.
- **Documented unsupported** means a vendor source explicitly excludes the
  path.
- **Not verified** means this research did not establish the support claim; it
  does not prove that the capability is impossible.

Before selection, reconcile the unresolved URL count in the
[link-check ledger](research-link-checks-r1.0.1.tsv), obtain entitled
hardware/guest/support matrices, confirm signed Proxmox enterprise repository
metadata, verify the selected add-on lifecycles and entitlements, and validate
application-specific multicast and recovery needs. The project has not
performed a proof of concept or live failure/network test. Track follow-up in
the [TODO](TODO-r1.0.1.md).

## Appendix: Acronyms and key terms

### Acronyms and abbreviations

| Acronym or abbreviation | Full form | Meaning in this comparison |
|---|---|---|
| ACM | Advanced Cluster Management | Red Hat product for fleet operations across OpenShift clusters. It adds management functions but does not merge the clusters' schedulers. |
| API | Application programming interface | A defined way for software and management tools to communicate; Kubernetes, VMware, and Proxmox expose APIs for operations. |
| CNI | Container Network Interface | The plugin interface Kubernetes uses to configure pod network connections. The interface alone does not guarantee that a particular plugin or full network path is supported. [Networking details](research-vm-comparison-r1.0.1.md#networking-and-multicast) |
| CPU | Central processing unit | Processor resource used in product licensing and capacity planning; licensing rules differ by vendor. |
| CSI | Container Storage Interface | The plugin interface Kubernetes uses to connect persistent storage to pods and virtual machines. A compatible and supported storage driver is still required. [Storage and operations](research-vm-comparison-r1.0.1.md#other-capabilities-and-operations) |
| HA | High availability | Features intended to keep workloads available after failures. In this matrix, HA often means restarting a VM or replacing a pod, not uninterrupted execution. [Availability details](research-vm-comparison-r1.0.1.md#availability-failover-and-maintenance) |
| IGMP | Internet Group Management Protocol | IPv4 protocol used by hosts and network equipment to signal multicast group membership. [Networking details](research-vm-comparison-r1.0.1.md#networking-and-multicast) |
| KVM | Kernel-based Virtual Machine | Linux virtualization technology used by Proxmox and Red Hat to run virtual machines. |
| LXC | Linux Containers | Linux system-container technology integrated with Proxmox VE; containers share the host's Linux kernel. |
| MLD | Multicast Listener Discovery | IPv6 protocol used by hosts and network equipment to signal multicast group membership. [Networking details](research-vm-comparison-r1.0.1.md#networking-and-multicast) |
| NAT | Network address translation | A technique that rewrites network addresses, commonly used by default container networks; NAT by itself does not provide multicast forwarding. |
| NIC | Network interface card | A physical or virtual network adapter. A VM or Kubernetes node can have multiple NICs, but workloads may need additional configuration to use them. |
| OADP | OpenShift APIs for Data Protection | Red Hat's OpenShift backup APIs and tooling for protecting application resources and data; it does not by itself define every recovery layer or objective. [Backup details](research-rhel-r1.0.1.md#backup-restore-and-disaster-recovery) |
| OCP | OpenShift Container Platform | Red Hat's Kubernetes platform used here with OpenShift Virtualization for application pods and VMs. |
| OVE | OpenShift Virtualization Engine | Red Hat's VM-focused OpenShift offering. Its product rights differ from OCP and Platform Plus. |
| PBS | Proxmox Backup Server | Proxmox's separate backup product for protecting and restoring supported workloads. |
| PDM | Proxmox Datacenter Manager | Proxmox product for managing inventory and selected operations across independent Proxmox clusters and sites. |
| QEMU | Quick Emulator | Machine emulator used with KVM to run virtual machines in Proxmox and OpenShift Virtualization. |
| RHEL | Red Hat Enterprise Linux | Red Hat's Linux operating system, used in this matrix with KVM/libvirt and Podman. |
| RWX | ReadWriteMany | Kubernetes storage access mode that allows a volume to be mounted read/write by multiple nodes; required for the documented OpenShift Virtualization live-migration path described in the report. [Requirements](research-rhel-r1.0.1.md#availability-failover-and-maintenance) |
| SR-IOV | Single Root I/O Virtualization | Hardware capability that divides a physical network adapter into virtual functions for direct workload access; supported use depends on the NIC and configuration. [Networking details](research-vm-comparison-r1.0.1.md#networking-and-multicast) |
| VCF | VMware Cloud Foundation | VMware's broader private-cloud bundle, including services beyond the narrower VVF bundle. |
| VDS | vSphere Distributed Switch | VMware virtual switch that provides network connectivity for vSphere hosts and their VMs. |
| VE | Proxmox Virtual Environment | Proxmox's virtualization platform for managing KVM virtual machines and LXC system containers. |
| VKS | vSphere Kubernetes Service | VMware's Kubernetes service running through vSphere Supervisor. |
| VM | Virtual machine | A software-defined computer with its own guest operating system, running on a physical host. |
| VVF | VMware vSphere Foundation | VMware bundle for vSphere and selected related services; its included services differ from VCF. |

### Key terms

| Term | Plain-language definition | How it applies here |
|---|---|---|
| Application container | An application packaged with its files and dependencies, then run by a container runtime. It generally shares the Linux kernel of its host or guest OS. | Podman and Kubernetes manage application containers in different ways; a supported OS does not automatically make every runtime or application combination supported. |
| Cluster | A group of computers coordinated as one platform or service. | VMware, Proxmox, and OpenShift each have their own cluster boundaries and management rules; a cluster in one product is not a shared cluster across vendors. |
| Guest operating system | The operating system installed inside a VM. | Guest OS and application support may belong to a different provider than the hypervisor. |
| Host | The physical server or operating system that provides resources to VMs or containers. | A container can run on a physical host or inside a VM guest; the distinction affects networking, support, and failure boundaries. |
| Kubernetes-managed VM | A VM represented and managed through Kubernetes resources and APIs. | OpenShift Virtualization provides this model; running Kubernetes inside a Proxmox or VMware guest does not make that hypervisor's VMs Kubernetes-managed. |
| Live migration | Moving a running VM from one host to another while aiming to keep it running. | Used mainly for planned maintenance; it depends on compatible hosts, networking, storage, and product-specific prerequisites. |
| Multicast | Network delivery where a sender transmits to a group of interested receivers instead of sending a separate copy to each one. | End-to-end multicast depends on workload membership, runtime or pod networking, VM/host networking, and the physical network. A working VM network alone does not establish pod multicast. [Comparison](research-vm-comparison-r1.0.1.md#networking-and-multicast) |
| Node secondary interface | An extra network adapter attached to a Kubernetes node in addition to its primary interface. | It gives the node another network path; pods do not automatically send traffic over it. Pod-level extra interfaces require additional configuration and network plugins. |
| Pod | Kubernetes' basic deployable unit, containing one or more related containers that share a network identity. | The pod network and interfaces are separate from the VM network adapters of the host running the Kubernetes node. |
| Replication | Keeping another copy of data or a workload updated on another system or site. | Replication can aid recovery, but it is not the same as an independent, retained backup and may copy corruption or deletion. |
| System container | An isolated Linux environment that behaves more like a lightweight OS instance than one application process. | Proxmox LXC is a system-container option. It shares the host kernel and is distinct from an application container or Kubernetes pod. |
| VM restart after failure | Starting an affected VM on a healthy host after a failure is detected. | Common hypervisor HA behavior; it involves downtime and is different from live migration or application-level failover. |
