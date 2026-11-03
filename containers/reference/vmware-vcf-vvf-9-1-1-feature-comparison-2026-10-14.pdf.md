Oct 14, 2026
VMware Cloud Foundation 9.1.1 and
VMware vSphere Foundation 9.1.1
Feature Comparison & Upgrade Paths

VMware Cloud Foundation 9.1.1 and VMware vSphere Foundation 9.1.1: Feature Comparison & Upgrade Paths
This feature comparison document outlines the key differences between our two primary platforms - VMware
Cloud Foundation and VMware vSphere Foundation.
VMware Cloud Foundation – a private cloud platform that combines the scale and agility of public
cloud with security and performance of on-premises infrastructure, delivering increased productivity
and lower Total Cost of Ownership (TCO).
• VMware Cloud Foundation is a full-stack Infrastructure as a Service (IaaS) platform that delivers
software-defined compute, storage, networking, Kubernetes, security, and management.
• Integrated automation enables a self-service platform to rapidly deploy VMs/containers for
developer agility.
• Hardened platform offering built-in resilience, scaling, and clustering for n-stop operations.
• Provides cloud agility to scale infrastructure without scaling staff, delivering cloud consumption on-
premises.
• Provides automation and orchestration to simplify Day 0, Day 1, and Day 2 tasks.
• Available as a single SKU to simplify full stack deployment.
VMware vSphere Foundation – an enterprise-grade workload platform for modern infrastructure
delivering virtualized benefits, simplified management, cost efficiency, scalability and serves as the core
foundation for VMware Cloud Foundation.
• Unified workload platform for running VMs and containers side by side with a native Kubernetes
runtime.
• Intelligent operations management delivers enhanced visibility and infrastructure optimization.
• Hyperconverged infrastructure integrates compute and storage virtualization for efficient resource
management.
• Simplified deployment and scalability with a single SKU, enabling faster application delivery and
future ready infrastructure.
Figure 1: shows VMware by Broadcom simplified portfolio
WHITE PAPER | 2

VMware Cloud Foundation 9.1.1 and VMware vSphere Foundation 9.1.1: Feature Comparison & Upgrade Paths
Detailed Feature Comparison
•  VMware Cloud Foundation - a private cloud platform software that delivers integrated components,
including vSphere, vSphere Kubernetes Service, VCF Operations, VCF Operations for networks, VCF
Operations fleet management, VCF Automation, vSAN, and NSX.
•  VMware vSphere Foundation - a software that delivers some VCF capabilities or limited versions
thereof, including vSphere, vSphere Kubernetes Service, VCF Operations and vSAN.
•  VMware Cloud Foundation Edge - VMware Cloud Foundation Edge is an optimized configuration of
VMware Cloud Foundation tailored for edge use cases.

Table of Contents:

[Compute | Storage | Networking | VKS | VCF Automation | VCF Operations | Private AI | Advanced Services]

|     | VMware vSphere  | VMware Cloud   | VMware Cloud   |
| --- | --------------- | -------------- | -------------- |
Features
|                    | Foundation  | Foundation Edge  | Foundation  |
| ------------------ | ----------- | ---------------- | ----------- |
|                    |             |                  |             |
| Compute            |             |                  |             |
| Included Services  |             |                  |             |
vSphere Kubernetes Service (VKS)
|     | ●   | ●   | ●   |
| --- | --- | --- | --- |
VM Service
|                                   | ●      | ●   | ●   |
| --------------------------------- | ------ | --- | --- |
| Storage Service                   | ● [2]  | ●   | ●   |
| Network Service                   | ● [2]  | ●   | ●   |
| Local Harbor Registry             | ●      | ●   | ●   |
| Regional Harbor Registry Service  |        | ●   | ●   |
vSphere Pod Service
|                              | ●   | ●   | ●   |
| ---------------------------- | --- | --- | --- |
| Foundational Load Balancing  | ●   | ●   | ●   |
| Service Mesh                 | ●   | ●   | ●   |
| External DNS                 | ●   | ●   | ●   |
| ArgoCD Operator              |     | ●   | ●   |
| Secret Store Service         |     | ●   | ●   |
| IaaS Policy Service          |     |     |     |
|                              |     | ●   | ●   |
| Data Services                | ●   | ●   | ●   |
| Workload Availability Zones  | ●   | ●   | ●   |
| VKS multi-cluster lifecycle  |     | ●   | ●   |
management
| Build Your Own Image (BYOI)     | ●   | ●   | ●   |
| ------------------------------- | --- | --- | --- |
| Supervisor Independent Updates  | ●   | ●   | ●   |
| Custom Zone Optimization        | ●   | ●   | ●   |
WHITE PAPER | 3

VMware Cloud Foundation 9.1.1 and VMware vSphere Foundation 9.1.1: Feature Comparison & Upgrade Paths
|     | VMware vSphere  | VMware Cloud   | VMware Cloud   |
| --- | --------------- | -------------- | -------------- |
Features
|                            | Foundation  | Foundation Edge  | Foundation  |
| -------------------------- | ----------- | ---------------- | ----------- |
| Compute                    |             |                  |             |
| Operations Management      |             |                  |             |
| vSphere Lifecycle Manager  | ●           | ●                | ●           |
| Live Patching for ESX      | ●           | ●                | ●           |
| vCenter Quick Patching     | ●           | ●                | ●           |
| vCenter Server Profiles    | ●           | ●                | ●           |
| vCenter Update Planner     | ●           | ●                | ●           |
Content Library
|                                      | ●   | ●    | ●    |
| ------------------------------------ | --- | ---- | ---- |
| vSphere Configuration Profiles       | ●   | ●    | ●    |
| Host Profiles                        | ●   | [3]  | [3]  |
| Auto Deploy                          | ●   | [3]  | [3]  |
| vSphere elastic provisioning (ZTP -  | ●   | ●    | ●    |
Zero Touch Provisioning)
| Green Metrics             | ●   | ●   | ●   |
| ------------------------- | --- | --- | --- |
| Built-in Security         |     |     |     |
| Identity Federation       | ●   | ●   | ●   |
| Hardware TPM 2.0 Support  | ●   | ●   | ●   |
| Virtual TPM 2.0           | ●   | ●   | ●   |
FIPS 140-2, and Common Criteria
|     | ●   | ●   | ●   |
| --- | --- | --- | --- |
Certification
| TLS 1.2  | ●      | ●      | ●      |
| -------- | ------ | ------ | ------ |
| TLS 1.3  | ● [4]  | ● [4]  | ● [4]  |
Virtual Machine Encryption
|                                       | ●   | ●   | ●   |
| ------------------------------------- | --- | --- | --- |
| Standard Key Provider (External KMS)  | ●   | ●   | ●   |
| Native Key Provider                   | ●   | ●   | ●   |
| File Integrity Monitoring             | ●   | ●   | ●   |
| Confidential Computing [15]           |     | ●   | ●   |
EDR integration for ESX
|                          | ●   | ●   | ●   |
| ------------------------ | --- | --- | --- |
| Application Performance  |     |     |     |
Per-VM Enhanced vMotion
|     | ●   | ●   | ●   |
| --- | --- | --- | --- |
Compatibility (EVC)
| Instant Clone                         | ●   | ●   | ●   |
| ------------------------------------- | --- | --- | --- |
| Distributed Resource Scheduler (DRS)  | ●   | ●   | ●   |
WHITE PAPER | 4

VMware Cloud Foundation 9.1.1 and VMware vSphere Foundation 9.1.1: Feature Comparison & Upgrade Paths
|     | VMware vSphere  | VMware Cloud   | VMware Cloud   |
| --- | --------------- | -------------- | -------------- |
Features
|                               | Foundation  | Foundation Edge  | Foundation  |
| ----------------------------- | ----------- | ---------------- | ----------- |
| Compute                       |             |                  |             |
| Storage DRS                   | ●           | ●                | ●           |
| Distributed Power Management  | ●           | ●                | ●           |
(DPM)
| Storage Policy-Based Management     | ●   | ●   | ●   |
| ----------------------------------- | --- | --- | --- |
| I/O Controls (storage)              | ●   | ●   | ●   |
| Single Root I/O Virtualization (SR- | ●   | ●   | ●   |
IOV)
| vSphere Persistent Memory  | ●   | ●   | ●   |
| -------------------------- | --- | --- | --- |
| Memory Tiering             | ●   | ●   | ●   |
| NVIDIA GRID vGPU           | ●   | ●   | ●   |
Accelerated Graphics for VMs
|                                 | ●   | ●   | ●   |
| ------------------------------- | --- | --- | --- |
| Dynamic DirectPath IO           | ●   | ●   | ●   |
| Enhanced DirectPath I/O         | ●   | ●   | ●   |
| Vendor Device Group             | ●   | ●   | ●   |
| Heterogeneous vGPU profiles on  | ●   | ●   | ●   |
same GPU
| DRS automation for vGPU workloads  | ●   | ●   | ●   |
| ---------------------------------- | --- | --- | --- |
| DPU Support and Dual DPU Support   |     | ●   | ●   |
| Business Continuity                |     |     |     |
| vMotion                            | ●   | ●   | ●   |
Cross-vCenter vMotion
|     | ●   | ●   | ●   |
| --- | --- | --- | --- |
Encrypted vMotion
|                                 | ●   | ●   | ●   |
| ------------------------------- | --- | --- | --- |
| vCenter Enhanced Linked Mode    | ●   | ●   | ●   |
| vSMP                            | ●   | ●   | ●   |
| vSphere High Availability (HA)  | ●   | ●   | ●   |
| Proactive HA                    | ●   | ●   | ●   |
Storage vMotion
|     | ●   | ●   | ●   |
| --- | --- | --- | --- |
Fault Tolerance
|                                | ●   | ●   | ●   |
| ------------------------------ | --- | --- | --- |
| vSphere Replication            | ●   | ●   | ●   |
| Support for 4k Native Storage  | ●   | ●   | ●   |
| vSphere Quick Boot             | ●   | ●   | ●   |
WHITE PAPER | 5

VMware Cloud Foundation 9.1.1 and VMware vSphere Foundation 9.1.1: Feature Comparison & Upgrade Paths
|     | VMware vSphere  | VMware Cloud   | VMware Cloud   |
| --- | --------------- | -------------- | -------------- |
Features
|                                | Foundation  | Foundation Edge  | Foundation  |
| ------------------------------ | ----------- | ---------------- | ----------- |
| Compute                        |             |                  |             |
| vCenter File-Based Backup and  | ●           | ●                | ●           |
Restore
Cross vCenter Mixed Version
|     | ●   | ●   | ●   |
| --- | --- | --- | --- |
Provisioning
| Hot and Cold Migration to the Cloud    | ●   | ●   | ●   |
| -------------------------------------- | --- | --- | --- |
| Policy-based Governance                | ●   | ●   | ●   |
| Kubernetes Automation                  | ●   | ●   | ●   |
| Workload Lifecycle Management          | ●   | ●   | ●   |
| vCenter Orchestration & Extensibility  | ●   | ●   | ●   |
| Storage                                |     |     |     |
vSAN Express Storage Architecture
|     | ●   | ●   | ●   |
| --- | --- | --- | --- |
(ESA)
| vSAN Original Storage Architecture  | ●   | ●   | ●   |
| ----------------------------------- | --- | --- | --- |
(OSA)
| All-Flash Hardware  | ●   | ●   | ●   |
| ------------------- | --- | --- | --- |
Basic Compression and Deduplication  ● (OSA Only)  ● (OSA Only)  ● (OSA Only)
Advanced Compression and Global  ● (ESA Only)  ● (ESA Only)  ● (ESA Only)
Deduplication
| Data-at-Rest Encryption          | ●   | ●      | ●      |
| -------------------------------- | --- | ------ | ------ |
| Data in-Transit Encryption       | ●   | ● [3]  | ● [3]  |
| Storage Policy-Based Management  | ●   | ●      | ●      |
Software Checksum
|                                        | ●   | ●       | ●       |
| -------------------------------------- | --- | ------- | ------- |
| vSAN over RDMA                         | ●   | ● [3]   | ● [3]   |
| Quality of Service (QoS) – IOPS Limit  | ●   | ●       | ●       |
| Auto-Managed RAID                      | ●   | ●       | ●       |
| vSAN storage clusters                  | ●   | ●       | ●       |
| vSAN Witness Host/ 2 Node Support      |     |         |         |
|                                        |     | ●       |         |
| vSAN cyber recovery clusters           |     |         |         |
|                                        |     | ● [15]  | ● [15]  |
| Remote Datastores                      | ●   | ●       | ●       |
| Stretched Cluster                      | ●   | ●       | ●       |
| 2-Node Cluster                         | ●   | ● [3]   | ● [3]   |
| File Services                          | ●   | ●       | ●       |
| Object Storage                         |     |         |         |
|                                        |     | ● [17]  | ● [17]  |
WHITE PAPER | 6

VMware Cloud Foundation 9.1.1 and VMware vSphere Foundation 9.1.1: Feature Comparison & Upgrade Paths
|     | VMware vSphere  | VMware Cloud   | VMware Cloud   |
| --- | --------------- | -------------- | -------------- |
Features
|                                     | Foundation  | Foundation Edge  | Foundation  |
| ----------------------------------- | ----------- | ---------------- | ----------- |
| Storage                             |             |                  |             |
| iSCSI Target Service                | ●           | ● [3]            | ● [3]       |
| Cloud Native Storage (CNS) Control  | ●           | ●                | ●           |
Plane
| vSphere Container Storage Interface  | ●   | ●   | ●   |
| ------------------------------------ | --- | --- | --- |
(CSI) Driver
| Rack Awareness (Fault Domains)  | ●   | ● [3]  | ● [3]  |
| ------------------------------- | --- | ------ | ------ |
Snapshot Manager with Flexible
|     | ●   | ●   | ●   |
| --- | --- | --- | --- |
Scheduling
| Immutable Snapshots  | ●   | ●   | ●   |
| -------------------- | --- | --- | --- |
Any-to-vSAN Replication
|                   | ● [14]  | ● [14]  | ● [14]  |
| ----------------- | ------- | ------- | ------- |
| External Storage  |         |         |         |

VMFS - Fibre Channel  ●  ● (Principal, Supplemental)  ● (Principal, Supplemental)
|     | ●   | ●   |     |
| --- | --- | --- | --- |
VMFS - iSCSI
|                 |     | (Supplemental)  | ● (Supplemental)  |
| --------------- | --- | --------------- | ----------------- |
| VMFS - FCoE     | ●   | ●               |                   |
|                 |     | (Supplemental)  | ● (Supplemental)  |
| VMFS - NVMe/FC  | ●   | ●               |                   |
|                 |     | (Supplemental)  | ● (Supplemental)  |
|                 | ●   | ●               |                   |
VMFS - NVMe/TCP
|     |     | (Supplemental)  | ● (Supplemental)  |
| --- | --- | --------------- | ----------------- |
|     | ●   | ●               |                   |
VMFS - NVMe/RDMA
|     |     | (Supplemental)  | ● (Supplemental)  |
| --- | --- | --------------- | ----------------- |
NFS - v3  ●  ● (Principal, Supplemental)  ● (Principal, Supplemental)
|     | ●   | ●   | ●   |
| --- | --- | --- | --- |
NFS - v4.1
|                                       |     | (Supplemental)  | (Supplemental)  |
| ------------------------------------- | --- | --------------- | --------------- |
| Storage I/O QoS Controls (SIOC)       | ●   | ●               | ●               |
| Storage Array Integration (VAAI) for  | ●   | ●               | ●               |
Block Storage
Storage Array Integration (VAAI) for
|     | ●   | ●   | ●   |
| --- | --- | --- | --- |
NFS Storage
| Workload (VMDK) Clustering   | ●   | ●   | ●   |
| ---------------------------- | --- | --- | --- |
Auto config with NFS
|     | ●   | ●   | ●   |
| --- | --- | --- | --- |
3rd party storage plugins
|                                 | ●   | ●   | ●   |
| ------------------------------- | --- | --- | --- |
| Host commissioning and cluster  | ●   | ●   | ●   |
management
|     |     |     |     |
| --- | --- | --- | --- |
|     |     |     |     |
WHITE PAPER | 7

VMware Cloud Foundation 9.1.1 and VMware vSphere Foundation 9.1.1: Feature Comparison & Upgrade Paths
|     | VMware vSphere  | VMware Cloud   | VMware Cloud   |
| --- | --------------- | -------------- | -------------- |
Features
|                                    | Foundation  | Foundation Edge  | Foundation  |
| ---------------------------------- | ----------- | ---------------- | ----------- |
| Networking                         |             |                  |             |
| vSphere Distributed Switch         | ●           | ●                | ●           |
| Link Aggregation Control Protocol  | ●           | ● [3]            | ● [3]       |
(LACP)
| Load-Based Teaming              | ●   | ●   | ●   |
| ------------------------------- | --- | --- | --- |
| Network I/O QoS Control (NIOC)  | ●   | ●   | ●   |
| Private VLAN                    | ●   | ●   | ●   |
| MAC Learning                    | ●   | ●   | ●   |
BPDU Guard
|                                   | ●       | ●             | ●             |
| --------------------------------- | ------- | ------------- | ------------- |
| Guest VLAN Tagging                | ●       | ●             | ●             |
| VLAN Backed Networking            | ●       | ●             | ●             |
| Virtual Networking                |         |               |               |
|                                   |         | ●             | ●             |
| Spoofguard                        |         | ●             | ●             |
| L2 Multicast                      | ●       | ●             | ●             |
| L3 Multicast                      |         | ●             | ●             |
| Enhanced Datapath                 |         | ●             | ●             |
| Enhanced Datapath for DPUs        |         |               |               |
|                                   |         | ●             | ●             |
| IPv4 and IPv6 Routing             |         | ●             | ●             |
| Dynamic Routing (OSPFv2/BGP/BFD)  |         | ●             | ●             |
| VRF                               |         | ●             | ●             |
| EVPN                              |         | ●             | ●             |
| NAT                               |         | ●             | ●             |
| L2 and L3 VPN                     |         |               |               |
|                                   |         | ●             | ●             |
| Quality of Service (QoS)          | ●       | ●             | ●             |
|                                   | (NIOC)  | (NIOC & NSX)  | (NIOC & NSX)  |
| NSX Edge Bridge for Networking    |         | ●             | ●             |
| DNS, DHCP and IPAM                |         | ●             | ●             |
| Container Networking with NCP     |         | ● [16]        | ● [16]        |
| Container Networking with Antrea  | ● [16]  | ● [16]        | ● [16]        |
| Policy, Tagging, and Grouping     |         | ●             | ●             |
| Multi-Tenancy with Projects       |         |               |               |
|                                   |         | ●             | ●             |
| Virtual Private Cloud (VPCs)      |         | ●             | ●             |
WHITE PAPER | 8

VMware Cloud Foundation 9.1.1 and VMware vSphere Foundation 9.1.1: Feature Comparison & Upgrade Paths
|     | VMware vSphere  | VMware Cloud   | VMware Cloud   |
| --- | --------------- | -------------- | -------------- |
Features
|                                        | Foundation  | Foundation Edge  | Foundation  |
| -------------------------------------- | ----------- | ---------------- | ----------- |
| Networking                             |             |                  |             |
|                                        |             |                  |             |
| Load Balancing for VCF Infrastructure  |             | ●                | ●           |
Components (i.e. VCF appliances) [12]
Layer 4 Load Balancing for vSphere
|     | ●   | ●   | ●   |
| --- | --- | --- | --- |
Supervisor (including VM Service,
vSphere PODs, and VKS Clusters)[11],[12]
| Manager / Controller Clustering  |     | ●   | ●   |
| -------------------------------- | --- | --- | --- |
| Federation                       |     | ●   | ●   |
| NSX Edge in VM and Bare-Metal    |     | ●   | ●   |
Form Factor for Networking
| Automated and Manual Manager and  |     | ●   | ●   |
| --------------------------------- | --- | --- | --- |
Edge Deployment
| Automated Host Prep  |     | ●   | ●   |
| -------------------- | --- | --- | --- |
| Port Mirroring       | ●   | ●   | ●   |
Netflow/IPFIX
|                              | ●   | ●   | ●   |
| ---------------------------- | --- | --- | --- |
| Traceflow                    |     |     |     |
|                              |     | ●   | ●   |
| Live Traffic Analysis        |     | ●   | ●   |
| Packet Capture               | ●   | ●   | ●   |
| vSphere Kubernetes Services  |     |     |     |
(VKS) & VCF Cloud Services
| vSphere Kubernetes Service (VKS):  | ●   | ●   | ●   |
| ---------------------------------- | --- | --- | --- |
Improved VKS cluster scalability; Fast
deploy for VKS clusters; Intelligent
Node pool placement
VM Service: Import VMs without
|     | ●   | ●   | ●   |
| --- | --- | --- | --- |
changing the network
| Storage and Data Services        |     | ●   | ●   |
| -------------------------------- | --- | --- | --- |
| Network Services: Dual- network  |     | ●   | ●   |
support for VKS; Supervisor
deployment using DGTW
| Private AI Services                 |     | ●   | ●   |
| ----------------------------------- | --- | --- | --- |
| Harbor Image Registry Service       | ●   | ●   | ●   |
| Container Service                   | ●   | ●   | ●   |
| GitOps Integration                  |     | ●   | ●   |
| Supervisor Services: Multi-cluster  |     |     |     |
|                                     |     | ●   | ●   |
zones and cluster decommission
| Secret Service: Simplified secrets  |     |     |     |
| ----------------------------------- | --- | --- | --- |
|                                     |     | ●   | ●   |
injection; Policies and roles to access
Secrets
WHITE PAPER | 9

VMware Cloud Foundation 9.1.1 and VMware vSphere Foundation 9.1.1: Feature Comparison & Upgrade Paths
|     | VMware vSphere  | VMware Cloud   | VMware Cloud   |
| --- | --------------- | -------------- | -------------- |
Features
|                              | Foundation  | Foundation Edge  | Foundation  |
| ---------------------------- | ----------- | ---------------- | ----------- |
| vSphere Kubernetes Services  |             |                  |             |
(VKS) & VCF Cloud Services
| External DNS                              |     | ●   | ●   |
| ----------------------------------------- | --- | --- | --- |
| Cert Manager                              |     | ●   | ●   |
| Cloud Management                          |     |     |     |
| VCF Automation                            |     |     |     |
| Modern Cloud Interface                    |     |     |     |
|                                           |     |     |     |
| Self-Service Catalog [5]                  |     |     |     |
|                                           |     | ●   | ●   |
| Self-Service IaaS [6]                     |     | ●   | ●   |
| UI / CLI / Unified APIs (declarative K8s  |     |     |     |
|                                           |     | ●   | ●   |
APIs [6] | REST APIs [5])
| Workload Performance & Cost  |     | ●   | ●   |
| ---------------------------- | --- | --- | --- |
Visibility for Consumers (w/ VCF
Operations) [6]
Private Cloud Services [6]
|                                     |     |     |     |
| ----------------------------------- | --- | --- | --- |
| Core Services: VM, VKS, Container,  |     |     |     |
|                                     |     | ●   | ●   |
Network, Volume, VM Image
| Extensible Services (ArgoCD,  |     | ●   | ●   |
| ----------------------------- | --- | --- | --- |
Contour, Harbor, Service Mesh,
Velero, etc.)
| Services Framework (Pre-bundled  |     | ●   | ●   |
| -------------------------------- | --- | --- | --- |
Services: Harbor, DSM, Secret Store
Service, VKSM Auto-Attach Service,
Encryption Management (BYOK),
Multi-tenant DR (VLR), Metrics
Aggregator Service, Configuration
Service, VCD Migration Assistant,
Lumos In-Product Feedback Service)
| Private AI Services [6], [10]    |     |     |     |
| -------------------------------- | --- | --- | --- |
| Catalog Setup Wizard (Automated  |     | ●   | ●   |
Private AI service setup)
| GPU-capable DL VM & GPU-capable  |     | ●   | ●   |
| -------------------------------- | --- | --- | --- |
VKS Cluster provisioning
| DSM Integration for RAG-based  |     | ●   | ●   |
| ------------------------------ | --- | --- | --- |
workloads
| Vector DBs, Data Indexing & Retrieval  |     |     |     |
| -------------------------------------- | --- | --- | --- |
|                                        |     | ●   | ●   |
service, AI Agent Builder service,
Model Context Protocol (MCP)
Blueprints & Infrastructure as Code
|                                     |     |     |     |
| ----------------------------------- | --- | --- | --- |
| Visual Canvas Template Designer w/  |     | ●   | ●   |
declarative YAML syntax [5]
| Blueprints (YAML [5] | K8s manifest in  |     | ●   | ●   |
| --------------------------------------- | --- | --- | --- |
YAML [6])
WHITE PAPER | 10

VMware Cloud Foundation 9.1.1 and VMware vSphere Foundation 9.1.1: Feature Comparison & Upgrade Paths
|     | VMware vSphere  | VMware Cloud   | VMware Cloud   |
| --- | --------------- | -------------- | -------------- |
Features
|                                   | Foundation  | Foundation Edge  | Foundation  |
| --------------------------------- | ----------- | ---------------- | ----------- |
| VCF Automation                    |             |                  |             |
| Git Integration (GitHub, GitLab,  |             | ●                | ●           |
Bitbucket) [5]
| VCF Automation TF Provider [5]  |     |     |     |
| ------------------------------- | --- | --- | --- |
|                                 |     | ●   | ●   |
| Automated deployment &          |     | ●   | ●   |
configuration of private cloud
services [6]
| Automated deployment &  |     | ●   | ●   |
| ----------------------- | --- | --- | --- |
configuration of SDDC objects [7] (e.g.,
NSX n/w, Security Groups, Firewalls
[8], Avi LB [9])
| App Stack Formation (capture group  |     |     |     |
| ----------------------------------- | --- | --- | --- |
|                                     |     | ●   | ●   |
of VMs into blueprints & reuse
blueprints to redeploy) [6]
Kubernetes Multi-Cluster
| Management                     |     |     |     |
| ------------------------------ | --- | --- | --- |
| Centralized VKS Cluster Fleet  |     | ●   | ●   |
Visibility
| VKS Policy Management                   |     | ●   | ●   |
| --------------------------------------- | --- | --- | --- |
| Data Protection                         |     |     |     |
|                                         |     | ●   | ●   |
| Add-on Management [18]                  |     | ●   | ●   |
| Governance & Policies                   |     |     |     |
| Zones, Regions, Organization, Project,  |     | ●   | ●   |
IAM (for Ent IT Admin) [5]
| Namespace Classes, Namespaces,  |     | ●   | ●   |
| ------------------------------- | --- | --- | --- |
VPC (for Ent IT Admin) [6]
| Namespaces & Private Cloud Services  |     |     |     |
| ------------------------------------ | --- | --- | --- |
|                                      |     | ●   | ●   |
Management (for LOB Admin) [6]
| Policies (approval, lease, day 2  |     | ●   | ●   |
| --------------------------------- | --- | --- | --- |
action) (for Org Admin) [5]
| Resource Policies (IaaS, VKS) w/  |     | ●   | ●   |
| --------------------------------- | --- | --- | --- |
Policy as Code (for Org Admin) [6]
| Infrastructure Placement Policies (for  |     | ●   | ●   |
| --------------------------------------- | --- | --- | --- |
Ent IT Admin) [6]
| Tenant Identity Management & RBAC  |     |     |     |
| ---------------------------------- | --- | --- | --- |
|                                    |     | ●   | ●   |
(for Org Admin) [6]
| Custom Naming Policy (for Org  |     | ●   | ●   |
| ------------------------------ | --- | --- | --- |
Admin) [5]
| Cost Visibility, Pricing [1], Notifications  |     | ●   | ●   |
| -------------------------------------------- | --- | --- | --- |
(alerts, reports, bills) (w/ VCF
Operations) (for Ent IT Admin & Org
Admin)
|     |     |     |     |
| --- | --- | --- | --- |
WHITE PAPER | 11

VMware Cloud Foundation 9.1.1 and VMware vSphere Foundation 9.1.1: Feature Comparison & Upgrade Paths
|     | VMware vSphere  | VMware Cloud   | VMware Cloud   |
| --- | --------------- | -------------- | -------------- |
Features
|                 | Foundation  | Foundation Edge  | Foundation  |
| --------------- | ----------- | ---------------- | ----------- |
| VCF Automation  |             |                  |             |

| Tenant Management [6]       |     |     |     |
| --------------------------- | --- | --- | --- |
| Tenant Resource Management  |     | ●   | ●   |
(compute, storage, network) (for Ent
IT Admin)
| Tenant Network Isolation w/ VCF  |     | ●   | ●   |
| -------------------------------- | --- | --- | --- |
Networking (for Ent IT Admin)
| Tenant Operations (utilization,  |     | ●   | ●   |
| -------------------------------- | --- | --- | --- |
chargeback, alerts)
| Tenant Branding (for Org Admin)  |     | ●   | ●   |
| -------------------------------- | --- | --- | --- |
| Quick / Manual Setup of          |     | ●   | ●   |
Organizations (for Ent IT Admin)
| Provider and Consumer Dashboards    |     |     |     |
| ----------------------------------- | --- | --- | --- |
|                                     |     | ●   | ●   |
| Certificate Management (for Ent IT  |     | ●   | ●   |
Admin & Org Admin)
| Content Management [6]                  |     |     |     |
| --------------------------------------- | --- | --- | --- |
|                                         |     |     |     |
| Centralize Content Hub for blueprints,  |     |     |     |
|                                         |     | ●   | ●   |
content libraries (VM Images),
orchestrator workflows
| Publish content to self-service catalog  |     | ●   | ●   |
| ---------------------------------------- | --- | --- | --- |
| Provider Tenant Admin to Tenant          |     | ●   | ●   |
sharing: content library and catalog
items
| Provider Tenant Admin to Tenant  |     | ●   | ●   |
| -------------------------------- | --- | --- | --- |
sharing: content library and catalog
items
| Content Library Creation (for Org  |     | ●   | ●   |
| ---------------------------------- | --- | --- | --- |
Admin & Project Admin)
| Subscription to external & Canonical  |     | ●   | ●   |
| ------------------------------------- | --- | --- | --- |
(Ubuntu OS images) content libraries
Network & Security Automation [6]
|                                      |     |     |     |
| ------------------------------------ | --- | --- | --- |
| Self-service networking (e.g., VPN,  |     | ●   | ●   |
NAT, static routes on TG, GW Firewall
[8]) for Org consumption
| Distributed Transit Gateway support  |     | ●   | ●   |
| ------------------------------------ | --- | --- | --- |
for VPCs (VLAN support)
| IPAM Support                         |     | ●      | ●      |
| ------------------------------------ | --- | ------ | ------ |
| Shared Subnets (across Orgs)         |     | ●      | ●      |
| Security Profiles, Security Groups,  |     | ● [8]  | ● [8]  |
DFW, GW Firewall (for Org Admin)
|     |     |     |     |
| --- | --- | --- | --- |
|     |     |     |     |
WHITE PAPER | 12

VMware Cloud Foundation 9.1.1 and VMware vSphere Foundation 9.1.1: Feature Comparison & Upgrade Paths
|     | VMware vSphere  | VMware Cloud   | VMware Cloud   |
| --- | --------------- | -------------- | -------------- |
Features
|     | Foundation  | Foundation Edge  | Foundation  |
| --- | ----------- | ---------------- | ----------- |
VCF Automation
|     |     |     |     |
| --- | --- | --- | --- |
Orchestration & Extensibility
|                              |     |     |     |
| ---------------------------- | --- | --- | --- |
| Workflow Orchestration (VCF  |     | ●   | ●   |
Operations orchestrator) [5]
Event Subscription Service, Custom
|     |     | ●   | ●   |
| --- | --- | --- | --- |
Resources/Custom Day 2, XaaS [5]
| Action-Based Extensibility (ABX)  |     | ●   | ●   |
| --------------------------------- | --- | --- | --- |
(FaaS) [7]
| Integrations (Ansible [7], Puppet [7],  |     | ●   | ●   |
| --------------------------------------- | --- | --- | --- |
VMware Salt[7], ServiceNow ITSM [7],
IPAM (Infoblox)[5], IPAM SDK[7], AD[5])
Workload Lifecycle Management
|     |     |     |     |
| --- | --- | --- | --- |
Workload discovery and onboarding
|     |     | ●   | ●   |
| --- | --- | --- | --- |
[7]
| Day 2 Actions & Custom Actions [5]  |     | ●   | ●   |
| ----------------------------------- | --- | --- | --- |
Advanced Workload Placement (w/
|     |     | ●   | ●   |
| --- | --- | --- | --- |
VCF Operations) [7]
| Resource right-sizing and reclamation  |     | ●   | ●   |
| -------------------------------------- | --- | --- | --- |
(w/ VCF Operations) [7]
| VCF Operations        |                         |        |        |
| --------------------- | ----------------------- | ------ | ------ |
| VCF AI Assistant      |                         | ●[17]  | ●[17]  |
| VCF Installer         | ●                       | ●      | ●      |
| Lifecycle Management  | (VVF customers utilize  | ●      | ●      |
vLCM)
License Management (IPv4, IPv6)
|                                       | ●   | ●   | ●   |
| ------------------------------------- | --- | --- | --- |
| Certificate Management                |     | ●   | ●   |
| Password Management                   |     | ●   | ●   |
| 3rd party password vault integration  |     | ●   | ●   |
with OpenID Connect (OIDC)
Configuration Drift Management     Requires Advanced   Requires Advanced
|     |     | Cyber Compliance   Cyber Compliance add- |     |
| --- | --- | ---------------------------------------- | --- |
(deprecated)
|                                  |     | add-on  | on   |
| -------------------------------- | --- | ------- | ---- |
| Centralized Tag Management       |     | ●       | ●    |
| Global inventory                 | ●   | ●       | ●    |
| Identity and Access Management,  | ●   | N/A     | N/A  |
Single Sign-on (vSphere interface)
| Identity and Access Management,  |     | ●   | ●   |
| -------------------------------- | --- | --- | --- |
Single Sign-on
(VCF Operations interface)
| GPU & vGPU monitoring  | ●   | ●   | ●   |
| ---------------------- | --- | --- | --- |
WHITE PAPER | 13

VMware Cloud Foundation 9.1.1 and VMware vSphere Foundation 9.1.1: Feature Comparison & Upgrade Paths
|     | VMware vSphere  | VMware Cloud   | VMware Cloud   |
| --- | --------------- | -------------- | -------------- |
Features
|     | Foundation  | Foundation Edge  | Foundation  |
| --- | ----------- | ---------------- | ----------- |
VCF Operations
|                               |     |     |     |
| ----------------------------- | --- | --- | --- |
| Audit events across vCenter,  | ●   | ●   | ●   |
vSphere, vSAN, and NSX
Log Management
|     | ●   | ●   | ●   |
| --- | --- | --- | --- |
VCF Health and Diagnostics
|                                        | ●   | ●   | ●   |
| -------------------------------------- | --- | --- | --- |
| Storage Operations (vSAN)              | ●   | ●   | ●   |
| Visualization (OOTB; Custom): Alerts,  | ●   | ●   | ●   |
Dashboards, Views, Reports, Heat
Map, Performance Charts, Super
Metrics, Metric Correlation,
Relationship Mapping
| Metric visualization using PromQL  | ●   | ●   | ●   |
| ---------------------------------- | --- | --- | --- |
| Performance Monitoring and         | ●   | ●   | ●   |
Analytics
| Real-time monitoring  |     | ●   | ●   |
| --------------------- | --- | --- | --- |
Compliance Management with    Requires Advanced   Requires Advanced
remediation, including regulatory  Cyber Compliance   Cyber Compliance add-
| compliance Security baseline, PCI),  |     | add-on  | on  |
| ------------------------------------ | --- | ------- | --- |
custom compliance templates,
vSphere hardening
| Real-Time predictive capacity  |     |     |     |
| ------------------------------ | --- | --- | --- |
|                                |     | ●   | ●   |
management, including trending
(Workload What-If analysis), right-
sizing, workload optimization (manual
and automated)
Troubleshooting with guided
|     | ●   | ●   | ●   |
| --- | --- | --- | --- |
remediation
| Cost Management and Optimization  | ●   | ●   | ●   |
| --------------------------------- | --- | --- | --- |
with Fine-Grained Cost Analytics
(Service and Data Center costs,
Reclamation, Planning)
| VKS Cost Management            |     |     |     |
| ------------------------------ | --- | --- | --- |
|                                |     |     |     |
| VKS Observability (real-time)  |     | ●   | ●   |
| Custom Profiles for VMs        | ●   | ●   | ●   |
| Data Protection and Recovery   | ●   | ●   | ●   |
(Integrated VMware Live Cyber
Recovery and VMware Live Site
Recovery)
Service Discovery and Application
|     | ●   | ●   | ●   |
| --- | --- | --- | --- |
Dependency Mapping
| Out-of-the-Box Discovery,  |     | ●   | ●   |
| -------------------------- | --- | --- | --- |
Monitoring, and Troubleshooting for
Packaged Applications
Extensibility via VMW & 3rd-Party
|     | ●   | ●   | ●   |
| --- | --- | --- | --- |
Infrastructure Management Packs
|     |     |     |     |
| --- | --- | --- | --- |
(SDDC, Compute, Storage, Network,
K8s/Container)
WHITE PAPER | 14

VMware Cloud Foundation 9.1.1 and VMware vSphere Foundation 9.1.1: Feature Comparison & Upgrade Paths
|     | VMware vSphere  | VMware Cloud   | VMware Cloud   |
| --- | --------------- | -------------- | -------------- |
Features
|                                    | Foundation  | Foundation Edge  | Foundation  |
| ---------------------------------- | ----------- | ---------------- | ----------- |
| VCF Operations                     |             |                  |             |
|                                    |             |                  |             |
| Extensibility via VMW & 3rd-Party  |             | ●                | ●           |
App & Management Packs (e.g., DBs,
middleware, app management)
| Application Monitoring (Telegraf  |     | ●   | ●   |
| --------------------------------- | --- | --- | --- |
Agent)
| Prometheus Management Pack  |     | ●   | ●   |
| --------------------------- | --- | --- | --- |
Builder, Prom QL API
Logs Alerting
|                 | ●   | ●   | ●   |
| --------------- | --- | --- | --- |
| Logs Query API  | ●   | ●   | ●   |
| Logs Scheduled  | ●   | ●   | ●   |
dashboard reports
| Logs Partitioning              | ●   | ●   | ●   |
| ------------------------------ | --- | --- | --- |
| Logs Content Pack support      | ●   | ●   | ●   |
| Security Operations (SecOps)   |     | ●   | ●   |
| Supervisor Cluster monitoring  | ●   | ●   | ●   |
(Metrics and Dashboard)
| vSphere Kubernetes Service Cluster  | ●   | ●   | ●   |
| ----------------------------------- | --- | --- | --- |
monitoring
VCF Operations orchestrator
|                              | ●   | ●   | ●   |
| ---------------------------- | --- | --- | --- |
| VCF Operations for networks  |     |     |     |
| Network Visibility and       |     | ●   | ●   |
Troubleshooting for vSphere, and
NSX
| Network Assessment and  |     | ●   | ●   |
| ----------------------- | --- | --- | --- |
Optimization Report
| Virtual flows (VDS IPFIX, VM to VM,  |     | ●   | ●   |
| ------------------------------------ | --- | --- | --- |
VM to Physical, Antrea IPFIX)
| Physical flows (NetFlow v7 and v9,  |     | ●   | ●   |
| ----------------------------------- | --- | --- | --- |
and sFlow)
| IPv6 Flows support for vSphere and  |     |     |     |
| ----------------------------------- | --- | --- | --- |
|                                     |     | ●   | ●   |
NSX
| Flow Analytics and Insights  |     | ●   | ●   |
| ---------------------------- | --- | --- | --- |
(Thresholds and Outliers)
| Application discovery (Automated  |     | ●   | ●   |
| --------------------------------- | --- | --- | --- |
and Manual - names, tags, RegEx,
ServiceNOW, csv)
| Application health, monitoring &  |     | ●   | ●   |
| --------------------------------- | --- | --- | --- |
troubleshooting, Analytics & Intents
| DNS mapping (import BIND zone file)  |     | ●   | ●   |
| ------------------------------------ | --- | --- | --- |
|                                      |     |     |     |
WHITE PAPER | 15

VMware Cloud Foundation 9.1.1 and VMware vSphere Foundation 9.1.1: Feature Comparison & Upgrade Paths
|     | VMware vSphere  | VMware Cloud   | VMware Cloud   |
| --- | --------------- | -------------- | -------------- |
Features
|                                   | Foundation  | Foundation Edge  | Foundation  |
| --------------------------------- | ----------- | ---------------- | ----------- |
| VCF Operations for networks       |             |                  |             |
|                                   |             |                  |             |
| NSX virtual network and physical  |             | ●                | ●           |
network fabric visibility
(Virtual+Physical)
| Physical Device integration (Cisco,  |     | ●   | ●   |
| ------------------------------------ | --- | --- | --- |
Arista, Juniper, Infoblox) for underlay
network visibility
| Network device auto-discovery        |     | ●   | ●   |
| ------------------------------------ | --- | --- | --- |
| NSX Federation Visibility            |     | ●   | ●   |
| Migration Plan, supporting workload  |     | ●   | ●   |
mobility across and within
Datacenters
| Network Visibility for native  |     |     |     |
| ------------------------------ | --- | --- | --- |
|                                |     | ●   | ●   |
Kubernetes (VKS), and Red Hat
OpenShift using NSX container plugin
| Avi Load Balancer Integration  |     | ●   | ●   |
| ------------------------------ | --- | --- | --- |
(Separate Add-On for Avi is required)
| vDefend Firewall network  |     | ●   | ●   |
| ------------------------- | --- | --- | --- |
segmentation planning and
operations (Separate Add-On for
vDefend is required)
| Highlight critical VMs via the Crown  |     | ●   | ●   |
| ------------------------------------- | --- | --- | --- |
Jewels reachability and visibility
analysis for security posture
| Visibility of Incomplete TCP sessions  |     |     |     |
| -------------------------------------- | --- | --- | --- |
|                                        |     | ●   | ●   |
for DDoS monitoring
| User friendly Search/Query capability   |     | ●   | ●   |
| --------------------------------------- | --- | --- | --- |
| Guided network troubleshooting          |     |     |     |
|                                         |     | ●   | ●   |
| Path Visibility for NSX Virtual         |     | ●   | ●   |
Network and Underlay Physical
network
| Network Map topology visualization  |     | ●   | ●   |
| ----------------------------------- | --- | --- | --- |
across VCF & underlay
| Network assurance & verification  |     | ●   | ●   |
| --------------------------------- | --- | --- | --- |
(Intents) for VCF & underlay
| Private AI                           |     |     |     |
| ------------------------------------ | --- | --- | --- |
| Multi-tenant Model Sharing           |     | ●   | ●   |
| Data Indexing and Retrieval Service  |     | ●   | ●   |
| Agent Builder Service                |     | ●   | ●   |
| Model Context protocol               |     | ●   | ●   |
| AI Metrics Observability             |     | ●   | ●   |
| Model Store                          |     | ●   | ●   |
WHITE PAPER | 16

VMware Cloud Foundation 9.1.1 and VMware vSphere Foundation 9.1.1: Feature Comparison & Upgrade Paths
|     | VMware vSphere  | VMware Cloud   | VMware Cloud   |
| --- | --------------- | -------------- | -------------- |
Features
|                                     | Foundation  | Foundation Edge  | Foundation  |
| ----------------------------------- | ----------- | ---------------- | ----------- |
| Private AI                          |             |                  |             |
| Model Runtime                       |             | ●                | ●           |
| CPU-only AI workloads               |             | ●                | ●           |
| AI Blueprints Quick Start           |             | ●                | ●           |
| Deep Learning VM Templates          |             | ●                | ●           |
| vGPU Profile visibility             |             | ●                | ●           |
| Vector Databases for RAG            |             | ●                | ●           |
| Advanced Services (Add-ons) [13]    |             |                  |             |
| Additional Storage Capacity - vSAN  | ●           | ●                | ●           |
| Advanced Cyber Compliance (ACC)     |             | ●                | ●           |
| ACC - Compliance Enforcement and    |             | ●                | ●           |
Policy Management for Workloads
and VCF stack
| ACC - On-Premises Cyber and  |     | ●   | ●   |
| ---------------------------- | --- | --- | --- |
Disaster Recovery
| ACC - Policy-Based VPC Connectivity  |     |     |     |
| ------------------------------------ | --- | --- | --- |
|                                      |     | ●   | ●   |
| ACC - Confidential Computing         |     | ●   | ●   |
| Site Recovery Manager                | ●   | ●   | ●   |
| Live Recovery Cloud                  | ●   | ●   | ●   |
| Load Balancing                       | ●   | ●   | ●   |
| Advanced Security                    |     | ●   | ●   |
| Application Services                 |     |     |     |
|                                      |     | ●   | ●   |
| Data Services                        |     | ●   | ●   |
| Network Observability                |     | ●   | ●   |
| Business Operations                  |     | ●   | ●   |
| Identity Security                    |     |     |     |
|                                      |     | ●   | ●   |

WHITE PAPER | 17

VMware Cloud Foundation 9.1.1 and VMware vSphere Foundation 9.1.1: Feature Comparison & Upgrade Paths
Footnotes
[1] - Org for VM Apps includes ability to markup w/ rate card
[2] - Denotes features that are limited to the support of VM Service and VKS.
[3] - Denotes features compatible with VCF but t integrated with VCF Operations fleet management.
[4] - For more information about using TLS 1.3 with FIPS 140-3 requirements, consult the product
documentation.
[5] - Available in both Org for All Apps and VM Apps.
[6] - Available in Org for All Apps.
[7] - Available in Org for VM Apps.
[8] - Requires Firewall add-on.
[9] - Requires Avi LB add-on.
[10] - Requires PAIF-N add-on.
[11] - Ingress / Gateway API provided by Contour Ingress Controller / Supervisor Service.
[12] - It is recommended that customers requiring general-purpose or advanced load balancing capabilities
should purchase Avi Load Balancer. Customers who need additional time to migrate from existing VCF
load balancing functionality to Avi may continue using full VCF load balancing capabilities until May 30,
2027, provided they have purchased the required Avi licenses. Please refer to this knowledge base
article 439411 for further details on Avi licensing and migration options.
[13] - Advanced services are available for separate purchases and are not included in the core VMware Cloud
Foundation or VMware vSphere Foundation offerings.
[14] - Requires VMware Site Recovery Manager (SRM) License.
[15] - Requires VCF Advanced Cyber Compliance (Advanced Services Add-on).
[16] - Support for Antrea will be provided for VMware VKS only. Support for NCP will be provided for
VMware vSphere Supervisor, and Tanzu Elastic Runtime only.
[17] - Tech Preview
[18] - This feature is accessible with VKS 3.5+
WHITE PAPER | 18

VMware Cloud Foundation 9.1.1 and VMware vSphere Foundation 9.1.1: Feature Comparison & Upgrade Paths
Upgrade Paths
The below graphics show upgrade paths from previous products to new offerings.
Compute Paths

|     | Previous Products  |     | Recommended Solution  |     |
| --- | ------------------ | --- | --------------------- | --- |

vSphere Enterprise Plus

vSphere Enterprise
|     |     |     | vSphere Foundation  |     |
| --- | --- | --- | ------------------- | --- |
vSphere for Desktop

|     | vSphere Scale-Out  |     |     |     |
| --- | ------------------ | --- | --- | --- |

|     |     |     | vSphere Standard  |     |
| --- | --- | --- | ----------------- | --- |
Storage Paths

|     | Previous Products  |     | Recommended Solution  |     |
| --- | ------------------ | --- | --------------------- | --- |

|     | vSphere   | vSAN  |     |     |
| --- | --------- | ----- | --- | --- |

|     | NSX   | Aria  |     |     |
| --- | ----- | ----- | --- | --- |

|     | vSphere   | vSAN  |                           |     |
| --- | --------- | ----- | ------------------------- | --- |
|     |           |       | VMware Cloud Foundation   |     |
|     |           | Aria  |                           |     |

vSphere
vSAN

NSX

|     |           |       | VMware Cloud Foundation   |     |
| --- | --------- | ----- | ------------------------- | --- |
|     | vSphere   | vSAN  |                           |     |

vSphere Foundation & vSAN Add-on

WHITE PAPER | 19

VMware Cloud Foundation 9.1.1 and VMware vSphere Foundation 9.1.1: Feature Comparison & Upgrade Paths
Networking/ Security Paths
Previous Products Recommended Solution
vSphere vSAN
NSX Aria
vSphere
VMware Cloud Foundation
NSX Aria
&
vSphere vSAN Firewall
NSX
vSphere
NSX
Management Path
Previous Products Recommended Solution
vSphere
Aria Suite Enterprise or
vRCU Enterprise
VMware Cloud Foundation
vSphere
vROPs + vRA or Aria Suite Advanced
or vRCU Advanced
vSphere
vSphere Foundation
vROPs or Aria Suite Standard or
vRCU Standard
WHITE PAPER | 20

VMware Cloud Foundation 9.1.1 and VMware vSphere Foundation 9.1.1: Feature Comparison & Upgrade Paths
vCloud Suite Paths
Previous Products Recommended Solution
vCloud Suite Enterprise
Aria Suite Enterprise
vSphere Enterprise Plus
VMware Cloud Foundation
vCloud Suite Advanced
Aria Suite Advanced
vSphere Enterprise Plus
vCloud Suite Standard
Aria Suite Standard
vSphere Foundation
vSphere Enterprise Plus
VCF Paths
Previous Products Recommended Solution
VCF Enterprise
VCF Advanced VMware Cloud Foundation
&
VCF Standard
Firewall
VCF Starter
For additional details, contact your VMware account team and sales representative.
WHITE PAPER | 21

Disclaimer
Although great care has been taken to ensure the accuracy and completeness of this whitepaper. Broadcom does not accept any legal
responsibility for any actions taken based on the information contained herein and Broadcom makes no representations or warranties of
any kind.
Copyright © 2026 Broadcom. All rights reserved.
The term “Broadcom” refers to Broadcom Inc. and/or its subsidiaries. For more information, go to www.broadcom.com. All trademarks, trade names, service marks, and logos
referenced herein belong to their respective companies. Broadcom reserves the right to make changes without further notice to any products or data herein to improve
reliability, function, or design. Information furnished by Broadcom is believed to be accurate and reliable. However, Broadcom does not assume any liability arising out of the
application or use of this information, nor the application or use of any product or circuit described herein, neither does it convey any license under its patent rights nor the
rights of others.