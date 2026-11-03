Veeam Kasten and
Red Hat OpenShift
Virtualization
Reference
Architecture

Table of Contents
Veeam Kasten and Red Hat OpenShift Virtualization Reference Architecture .............................................................................................1
Table of Contents ............................................................................................................................................................................................................... 2
Executive Overview ............................................................................................................................................................................................................ 3
Technology Overview ....................................................................................................................................................................................................... 4
Red Hat OpenShift Virtualization Overview ........................................................................................................................................................................................ 4
Initial Migration ........................................................................................................................................................................................................................................... 5
Storage Considerations for VM Workloads ................................................................................................................................................................................. 7
Veeam Kasten Overview ............................................................................................................................................................................................................................... 8
Architecture and Design Considerations .................................................................................................................................................................................... 10
Target Use Cases .............................................................................................................................................................................................................. 13
Backup and Recovery ................................................................................................................................................................................................................................... 15
Disaster Recovery ........................................................................................................................................................................................................................................... 16
RTOs and RPOs ......................................................................................................................................................................................................................................... 18
3-2-1 Rule ....................................................................................................................................................................................................................................................... 18
Backup and Recovery Testing ........................................................................................................................................................................................................... 19
DR Testing .................................................................................................................................................................................................................................................... 19
Application and VM Mobility .................................................................................................................................................................................................................... 19
Ransomware Protection ............................................................................................................................................................................................................................. 20
Encryption ................................................................................................................................................................................................................................................... 20
FIPS 140-3 .................................................................................................................................................................................................................................................... 20
Object Storage Immutability ............................................................................................................................................................................................................. 20
Recommended Design and Architecture .................................................................................................................................................................. 21
Hybrid Cloud Architecture ......................................................................................................................................................................................................................... 21
Continuous Deliver (CD) with ArgoCD ................................................................................................................................................................................................ 22
Integration of Veeam Kasten with Red Hat Advanced Cluster Security for Kubernetes ........................................................................................ 22
Integration of Veeam Kasten with Veeam Data Platform ....................................................................................................................................................... 25
Veeam Kasten Veeam Data Platform Plug-in .......................................................................................................................................................................... 25
Veeam Data Platform Repository for Kasten Backup Data ............................................................................................................................................. 26
Feature and Functionality Implementation to Support VMs and Applications ........................................................................................... 27
Deployment Configuration ........................................................................................................................................................................................................................27
On-Premises ................................................................................................................................................................................................................................................27
Public Cloud ............................................................................................................................................................................................................................................... 30
Veeam Kasten Configuration ............................................................................................................................................................................................................ 31
Permutations and Other Patterns ............................................................................................................................................................................. 35
On-Premises Only .................................................................................................................................................................................................................................... 35
Public Cloud Only ................................................................................................................................................................................................................................... 35
Tertiary/Multi-site ................................................................................................................................................................................................................................... 35
References ......................................................................................................................................................................................................................... 36
© 2025 Veeam Software. Confidential information. All rights reserved. All trademarks are the property of their respective owners. 9.10.2025 | 2

Executive Overview
Red Hat OpenShift has become the de facto standard for enterprise cloud-native orchestration platforms.
OpenShift offers wide support for multiple hardware and infrastructure platforms, both on-premises and in
the public cloud. With the introduction of Red Hat OpenShift Virtualization, where virtual machines (VMs)
can run adjacent to containerized applications in one platform, comes additional agility and flexibility for
customers who embrace cloud native architecture and IT transformation. As organizations modernize from
an infrastructure-centric virtualization approach toward the application-centric approach of cloud-native
computing, OpenShift Virtualization provides the platform, tooling, and ecosystem required to support an
array of use cases at scale.
While Red Hat OpenShift and OpenShift Virtualization provide “day 1” and “day 2” capabilities to manage
workloads, Veeam Kasten provides the requisite data protection, mobility, disaster recovery (DR), and
ransomware protection that enterprise and public sector organizations need for containerized and VM
workloads. This document serves as a guide to help you deploy these solutions together in a standardized,
repeatable, and referenceable pattern.
© 2025 Veeam Software. Confidential information. All rights reserved. All trademarks are the property of their respective owners. 9.10.2025 | 3

Technology Overview
Red Hat OpenShift Virtualization Overview
Red Hat OpenShift Virtualization uses a kernel-based virtual machine (KVM) (the Linux kernel hypervisor) to
bring VMsv to OpenShift as native objects, with features and capabilities that support cluster management
and scalability as well as VM consumption. KVM is a core component of the Red Hat Enterprise Linux kernel
and has been used in production for over 15 years in other hypervisor products like Red Hat Virtualization,
Red Hat OpenStack Platform, and Red Hat Enterprise Linux. The KVM used by Red Hat OpenShift is the
same KVM, QEMU, and libvirt used by those platforms. Red Hat OpenShift includes robust, stable, and
scalable type-1 hypervisors for virtualization workloads.
Containerized Apps
libvirt
QEMU
RHEL Core OS
KVM
Driver Driver Driver
Driver Storage Network
Hardware
Figure 1: Protect OpenShift Virtualization VMs with Kasten
In Figure 1, we see that Red Hat OpenShift provides a collection of pods that run on the cluster. These pods
run in a namespace and serve up containers, or in the case of OpenShift Virtualization, VMs are capable of
running a full OS. The integration of KVM and QEMU also allows for the installation and execution of a
complete OS environment on top of Kubernetes pods.
In this way, Red Hat OpenShift clusters can run VMs and container pods simultaneously to provide a unified
platform that supports traditional applications that run in Linux or Windows VMs in addition to modern
cloud-native applications in Kubernetes containers. This greatly facilitates operations for organizations that
want to “lift and shift” existing applications and workloads and those who may want to explore application
modernization strategies in the future.
© 2025 Veeam Software. Confidential information. All rights reserved. All trademarks are the property of their respective owners. 9.10.2025 | 4

Kubect(usetcommands)
Node
VirtualMachineCR ~ .vmx
kubelet
P (D o a d ernonSet) P (p o e d r VMI) Pod
API Server
virt-handler virt-launcher container
virt-controller Virt-controller libvirtd
Cluster components
qemu
KuberVirtcomponent
Kubernetes component
PVC
Figure 2: VM Components in OpenShift Virtualization
VMs are deployed and managed with the same scheduler that’s used for containerized workloads. Native
features like host affinity, resource awareness, load balancing, and high availability are all inherited from
Red Hat OpenShift cluster services. VMs connected to the cluster software-defined network (SDN) are
accessible via standard Kubernetes methods, including services and routes, while also being subject to
controlling traffic by using network policy and ingress/egress configuration. This provides robust methods
to enable access to VMs from inside and outside the cluster, along with platform-level security controls to
manage access to VM-hosted applications.
OpenShift Virtualization has several deployment options, including self-managed bare metal hosts on-
premises or in the cloud in AWS via self-managed clusters or Red Hat OpenShift on AWS’s (ROSA’s)
managed service.
Initial Migration
Many organizations are investigating VM alternatives to modernize their application development and
deployment architecture. Red Hat OpenShift is a good option for organizations who are considering migrating
from traditional hypervisor architectures to a unified platform that’s capable of running traditional applications
in VMs as well as modern cloud-native applications in containers. While many virtualization platforms exist,
this reference architecture assumes your source platform is VMware vSphere. The following table aligns
concepts in vSphere with their equivalent concept in OpenShift Virtualization:
Feature vSphere OpenShift Virtualization
Where VM disks are stored Datastore PVC/PV
Policy-based storage Storage Policy Based Management (SPBM) StorageClass
Non-disruptive VM migration vMotion Live migration
© 2025 Veeam Software. Confidential information. All rights reserved. All trademarks are the property of their respective owners. 9.10.2025 | 5

| Feature                              |     | vSphere          |     |     | OpenShift Virtualization  |     |     |
| ------------------------------------ | --- | ---------------- | --- | --- | ------------------------- | --- | --- |
| Non-disruptive VM storage migration  |     | Storage vMotion  |     |     | N/A                       |     |     |
Active resource balancing  Dynamic Resource Scheduling (DRS)  Pod eviction policy, descheduler
Physical network configuration  vSwitch/DvSwitch  NMstate Operator, Multus
Overlay network configuration  NSX-T  OVN-Kubernetes, CNI partners, Multus
Host/VM metrics  vCenter, vRealize Operations  OpenShift Metrics and Monitoring

For migration, it is recommended that you use the Red Hat Migration Toolkit for Virtualization (MTV), In
addition to importing VMs from Red Hat Virtualization, Red Hat OpenStack , and VMware vSphere to
OpenShift Virtualization, the Migration Toolkit for Virtualization also imports VMs from OPVA format and
between Red Hat OpenShift clusters. Additionally, VMs from other OpenShift Virtualization clusters can be
migrated to your current cluster with the migration toolkit. Once VMs have been successfully migrated to
the Red Hat OpenShift cluster, Veeam Kasten can provide backup, recovery, mobility, and ransomware
protection for these VMs. The diagram below demonstrates the logical flow of migrating from virtualization
sources to the target of OpenShift Virtualization:
MTV Data Transfer
OpenShift MTV
|     |     |     |     |     | VM App App | VM  |     |
| --- | --- | --- | --- | --- | ---------- | --- | --- |
MTV Queries vSphere
Worker Node
• Protect VM Workloads
• Pulls from original source
|               |         |     | • C a n   d o   d i | ff e r e n t i a l   S y n c |     | • P r o t e c t   C lo | u d   N a t ive Apps |
| ------------- | ------- | --- | ------------------- | ---------------------------- | --- | ---------------------- | -------------------- |
| V e e a m B a | c k u p |     |                     |                              |     | • E n a b l e   V M    |   m o bi lit y       |
&   R e pli c a ti o n • O n e   C o n v e r s i o n • D e f e n d   a g a in s t
|     |     |     | • M o st  P e r f | o r m a n t   S t o r a g e |     |     |     |
| --- | --- | --- | ----------------- | --------------------------- | --- | --- | --- |
Ransomware Attacks
|     | vSphere |     |     |     | OCP-V |     |     |
| --- | ------- | --- | --- | --- | ----- | --- | --- |
Figure 3: Red Hat OpenShift Migration Toolkit for Virtualization (MTV)

|       |           |               |     |     |     |     |     |
| ----- | --------- | ------------- | --- | --- | --- | --- | --- |

© 2025 Veeam Software. Confidential information. All rights reserved. All trademarks are the property of their respective owners.  9.10.2025 | 6

Storage Considerations for VM Workloads
OpenShift Virtualization does not use datastores, where one storage device (e.g.., LUN, NFS export, etc.)
holds many VM disks. This means that the use case where your storage device is running out of GiB or IOPS
and needs to have capacity “freed” does not apply to OpenShift Virtualization.
OpenShift Virtualization uses Kubernetes CSI abstraction for VM storage, where VM disks are mapped to
Persistent Volume Claims (PVCs). Most enterprise storage vendors offer a CSI driver to let Red Hat
OpenShift workloads leverage storage arrays, which enables customers to employ existing storage
investments for their Red Hat OpenShift platform.
Several container-native storage solutions also provide cluster data services as well as a simple CSI driver.
Likewise, these solutions can use existing physical storage platforms to protect their organizational
investment or leverage a converged solution where cluster storage is served by physical disks on OpenShift
worker nodes. I/O is distributed via Red Hat OpenShift Data Foundation (ODF), which is included in the Red
Hat OpenShift Platform Plus subscription service.
It is worth noting that a vendor’s CSI driver must offer the following minimum capabilities to effectively
support OpenShift Virtualization and Veeam Kasten:
• VolumeSnapshots for storage-based snapshots
• Read/write/many (RWX) to allow LiveMigration capabilities
OpenShift Cluster
Worker Node 1 Worker Node 2
rwx
SAN Storage
Figure 4: Block VolumeMode and Read/Write/Many (RWX) for Live Migration
© 2025 Veeam Software. Confidential information. All rights reserved. All trademarks are the property of their respective owners. 9.10.2025 | 7

In addition to the capabilities listed above, it’s strongly recommended that your underlying storage offers
RWX access for block VolumeMode capabilities as well as Change Block Tracking (CBT) to allow for
performant I/O and optimized backup and restore. While this standard was defined in the latest Kubernetes
CSI standard, it has yet to be adopted widely. At the time of writing, Veeam Kasten can provide incremental
snapshot capabilities for OpenShift Data Foundation (ODF) and AWS EC2 EBS storage with EBS storage
that supports full CBT.
Figure 5: PVC VolumeMode and Underlying Storage Configurations
Veeam Kasten Overview
Veeam Kasten is an enterprise-grade and secure data management platform that enterprises can deploy
to protect their containerized and VM workloads that are deployed on Red Hat OpenShift.
Veeam Kasten can be used for:
• Backup/restore to protect cloud-native applications, VMs on Kubernetes, and business-critical data.
• DR to manage backups that were replicated off-site to meet business and regulatory requirements.
• Application mobility to let you move applications between clouds and on-premises for test/dev, load
balancing, and upgrades.
• Ransomware protection with the ability to leverage immutable object storage offerings off-cluster and
ensure backup data is unaltered or indelible.
© 2025 Veeam Software. Confidential information. All rights reserved. All trademarks are the property of their respective owners. 9.10.2025 | 8

For cloud-native applications, Red Hat OpenShift provides resiliency and scale. However, protecting data
for stateful workloads (e.g., databases) requires functionality that’s not available in Red Hat OpenShift itself.
Cloud-native applications that use microservices and containers are also fundamentally different from
earlier architectures in that their components are frequently added, rescheduled, or removed. This results in
a very dynamic environment that therefore requires a data protection platform that natively understands
this architecture and can dynamically detect and protect applications and data.
Cloud (ROSA)
Table 1: Solution Overview
Veeam Kasten is purpose-built for Kubernetes and has a deep understanding of cloud-native application
design and dependencies, which enables it to effectively coordinate backup operations in an application-
aware fashion. Veeam Kasten also protects the complete application stack and provides a solution with
unparalleled operational simplicity and ease. This makes it easy for developers and operations teams to
deploy and use Veeam Kasten via a web-based management portal or through Kubernetes-native API/CLI.
Veeam Kasten also provides comprehensive end-to-end security with encryption and ransomware
protection. This data management platform supports both relational and No-SQL databases (e.g.,
Cassandra, MongoDB, and Kafka) and seamlessly integrates with Red Hat OpenShift and storage vendors
(e.g., Dell Technologies, NetApp, and Pure Storage), both on-premises and in the public cloud (e.g., AWS,
Google Cloud, and Azure). This includes security solutions that further harden Veeam Kasten and
protect your data.
In this reference architecture, Veeam Kasten is used to protect business-critical applications in a hybrid
cloud deployment that runs on Red Hat OpenShift clusters. Veeam Kasten is also used to support
application mobility for dev/test where an application is developed and tested in the public cloud and
moved on-premises for staging and production via on-premises storage. Veeam Kasten also enables easy
application migration from different public clouds to on-premises infrastructures and vice versa. It also
offers simplicity and seamless data conversion between infrastructure formats and ensures data security
by encrypting migration data both in-transit and at rest.
© 2025 Veeam Software. Confidential information. All rights reserved. All trademarks are the property of their respective owners. 9.10.2025 | 9
PCO RedHatOpenShift
Container Platform
enalP
ataD
App 1 VM 1 RDS VM 2 App 3
Target Storage
Data
Protection
RedHat OpenShift
Data Foundation
EBS
On-Premises
MCA
Red Hat
Advanced Cluster Management for Kubernetes
RedHatOpenShift
Container Platform
Other Storage*

Architecture and Design Considerations
Kasten Application Architecture
As noted earlier, Veeam Kasten is deployed as a cloud-native application within each Red Hat OpenShift
cluster you want to protect. This differs from the typical infrastructure-centric approach for deploying
backup infrastructure that’s distinct or outside the infrastructure you’re protecting. This is due to
fundamental differences in architecture between traditional server virtualization infrastructures and the
cloud-native architecture of Red Hat OpenShift.
Veeam Kasten consists of several services and pods, which can be deployed to OpenShift either through the
certified Red Hat OpenShift Operator or a Helm chart. The various components of Veeam Kasten and its
communication paths are highlighted in the diagram below:
Browser CLI API
80,443
6443
8000, 8877
|          | 8000 | 6443  | 6443 |     |     |
| -------- | ---- | ----- | ---- | --- | --- |
| auth-svc |      | kube- |      |     |     |
gateway kanister-svc
apiserver
|     |     | 6443 | 6443 |     |     |
| --- | --- | ---- | ---- | --- | --- |
8000-8003
|     | 8000 8000 | 443/10250 |     |     |     |
| --- | --------- | --------- | --- | --- | --- |
8000
frontend-svc dashboardbff-svc aggregatedapis- 8000 catalog-svc crypto-svc
svc
8000-8003
|     | 8000 9090 | 8000 |     |     |     |
| --- | --------- | ---- | --- | --- | --- |
8000
|     | 80  |     | 8000 |     |     |
| --- | --- | --- | ---- | --- | --- |
prometheus- executor
| metering-svc |     | jobs-svc |     | 8000 | Temp Pods |
| ------------ | --- | -------- | --- | ---- | --------- |
server aau-ustvhthc-s-svvcc
443, …
|     |     | 8000       | 8000 |        |         |
| --- | --- | ---------- | ---- | ------ | ------- |
|     |     | controller |      | 443, … | Storage |
logging-svc
manager-svc
© 2025 Veeam Software. All rights reserved. All trademarks are the property of their respective owners.
|     | Figure 6: Veeam Kasten Logical Components  |     |     |     |     |
| --- | ------------------------------------------ | --- | --- | --- | --- |

© 2025 Veeam Software. Confidential information. All rights reserved. All trademarks are the property of their respective owners.  9.10.2025 | 10

Multi-Cluster Manager
Once deployed, Veeam Kasten can be managed on the Kasten multi-cluster Manager. The multi-cluster
manager simplifies Veeam Kasten operations across multiple Kubernetes clusters.
Hree, administrators define primary-secondary relationships between Kasten instances. Primary Kasten
instances provide a single-entry point and dashboard for administrators to manage secondary instances.
Veeam Kasten resources, like policies and profiles, are defined in the primary instance and then distributed
to secondary instances. Secondary instances enact their policies and the secondaries' actions, and metrics
are summarized in the primary instance.
Sizing
Veeam Kasten is deployed as a Kubernetes application within the Red Hat OpenShift cluster. By default,
Veeam Kasten will deploy to the kasten-io namespace. Like other cloud-native applications, the resource
requirements for Veeam Kasten may vary depending on the number and size of workloads you want to
back up. Data mover pods are only provisioned when a backup or restore action is triggered. Once
complete, the pods are deleted. At a minimum, the cluster should have enough capacity to accommodate
the Red Hat OpenShift platform components, as well as any workloads running that run on the cluster and
in Veeam Kasten. Veeam Kasten’s footprint requirements are as follows:
Type  Requested CPU (Cores)  Limit CPU (Cores)  Requested Memory (GB)
| Base                        | 1   | 2   | 1    |
| --------------------------- | --- | --- | ---- |
| DR                          | 1   | 1   | 0.3  |
| Dynamic (per parallel job)  | 1   | 1   | 0.4  |
| Total                       | 3   | 4   | 1.8  |
Table 2: Resource Requirements for Veeam Kasten

Veeam Kasten can perform up to nine parallel backup jobs, so the estimated maximum footprint can be
calculated as the sum of base requirements, DR requirements, and 9 x dynamic requirements, for a total of:
| Type         |     | Value  |     |
| ------------ | --- | ------ | --- |
| Cores        |     | 12     |     |
| Memory (GB)  |     | 7.9GB  |     |
Table 3: Total Resource Requirements for Veeam Kasten Supporting OCP-V

© 2025 Veeam Software. Confidential information. All rights reserved. All trademarks are the property of their respective owners.  9.10.2025 | 11

Veeam Kasten can be configured and tuned for backup and restore parallelism in order to meet
application demands with Helm or Operator configuration values.
Refer to the Veeam Kasten documentation to understand how workload sizes (e.g. 20GB or 200GB) and
types (e.g. random I/O versus sequential) can dictate dynamic resource requirements.
Authentication and Authorization
Veeam Kasten supports integrations with Red Hat OAuth for authentication. This means that the same
authentication mechanism can be used for both Red Hat OpenShift and Veeam Kasten authentication. By
using OpenShift OAuth as a single authentication method, administrators can eliminate the overhead that
comes with administering differing IAM systems while improving the end user experience. For more
information on how to deploy OAuth as the authentication mechanism for Veeam Kasten, refer to the
relevant documentation.
For authorization, Veeam Kasten leverages native Kubernetes RoleBindings and ClusterRoleBindings. By
default, Veeam Kasten deploys three default ClusterRoles:
1. k10-admin: The k10-admin ClusterRole is useful for administrators who want uninterrupted access to all
Kasten operations.
The k10-admin user can work with all K10 APIs, including profiles, policies, policy presets, actions, restore
points, transform sets, and blueprint bindings.
2. k10-basic: The k10-basic ClusterRole is useful for administrators who want to give operational Veeam
Kasten access to users in specific namespaces.
A user with the k10-basic ClusterRole is allowed to back up and restore applications in the namespaces
they have access to. This user can also create policies in the application's namespace to back up and
export the application. The k10-basic ClusterRole also gives this user access to view applications, actions,
and restore point details in their namespaces. A user with the k10-basic ClusterRole is also allowed to
cancel actions in the namespaces they have access to.
3. k10-config-view: The k10-config-view ClusterRole is useful for administrators who want to give K10
configuration view access to some users.
The k10-config-view ClusterRole gives a user read-only access to K10 configuration information, including
profiles, policies, policy presets, transform sets, and blueprint bindings on the dashboard.
For more information about Veeam Kasten, role- based access control (RBAC), and how to configure
appropriate RoleBindings and ClusterRoleBindings, refer to the relevant documentation.
© 2025 Veeam Software. Confidential information. All rights reserved. All trademarks are the property of their respective owners. 9.10.2025 | 12

Target Use Cases
Veeam Kasten caters to several use cases for data protection, DR, ransomware protection, and
application mobility.
Veeam Kasten’s application-centric approach to data protection affords you the ability to support several
backup and recovery scenarios, as highlighted in the diagram below:
Figure 7: Veeam Kasten Data Protection Use Cases
It is also worth identifying the key differentiators for Veeam Kasten in relation to other offerings like Velero
or Red Hat OpenShift Advanced Data Protection (OADP). Generally speaking, these solutions offer
namespace protection, which may be suitable for smaller environments that don’t require advanced data
protection features (e.g. application awareness), ransomware protection, or a user interface. Generally,
these solutions offer namespace protection, which may be suitable for smaller environments that don’t
require advanced data protection features (e.g. application awareness), ransomware protection, or a user
interface. While they may also be useful for developer project snapshots and backups, they lack cluster-
wide enterprise capabilities.
Veeam Kasten OADP
Kubernetes-native APIs
User Interface
© 2025 Veeam Software. Confidential information. All rights reserved. All trademarks are the property of their respective owners. 9.10.2025 | 13

Veeam Kasten OADP
Encryption
• Unique per application, per policy • Common encryption key for ALL repos
• FIPS-140-3 compliant
• External KMS support
Immutability
• Reusable library with common example transforms
Self-service
• Reusable blueprints
• Dynamic blueprint assignment
• Snapshot hooks and logical backups
Reusable Transforms
• Reusable library with common example transforms • Single resource modifier ConfigMap per
restore
Application Consistency
• Reusable blueprints
• Managing individual hook command
• Dynamic blueprint assignment annotations on workloads
• Snapshot hooks and logical backups • No logical backups
Block Mode Export
Monitoring and Reporting
• Built-in reporting and monitoring capabilities
• Simplified integration with third party metrics and
monitoring tools
For production and/or business- critical applications and VM workloads, Veeam Kasten provides a full suite
of features and capabilities, along with a rich user interface, cataloging, and dashboards for end-to-end
backup, DR, and ransomware protection.
© 2025 Veeam Software. Confidential information. All rights reserved. All trademarks are the property of their respective owners. 9.10.2025 | 14

Backup and Recovery
Veeam Kasten uses policy-based backup constructs to define frequency, retention, and lifecycle
management for assets protected by Red Hat OpenShift. Policies can be defined to protect metadata and
persistent application data groups by doing the following:
1. Name: This is the most common. Assets are grouped via an OpenShift project, which relates to the
Kubernetes namespace. All application metadata (e.g. deploy spec, statefulsets, configmaps, and
secrets) as well as persistent volume data (e.g. PVCs) deployed within the targeted namespace are
backed up or imported per your defined policy schedule.
VMs can be grouped logically into namespaces based on the workloads they host, and recovering
individual VMs in a namespace is possible with Veeam Kasten’s exclude filters or labels.
2. Label: Rather than targeting assets on a per-OpenShift-project basis, Kubernetes labels can be used to
protect any asset with the label applied, regardless of namespace. Label-based policies are also useful
for protecting resources or applications that span multiple OpenShift projects and/or namespaces.
3. None: This is typically used to protect cluster-scope resources. These include non-namespaced resources
that are not captured in application snapshots, such as Custom Resource Definitions, ClusterRoles, and
ClusterRoleBindings.
Policy types are defined as:
1. Snapshot: As the basis for backups, snapshot policies typically perform storage snapshot operations
and as well as capture application metadata. This is, where backups are stored both on cluster and off-
cluster (optional but recommended) in a defined location profile within protocols such as S3, S3-
compatible, Azure Blob, or NFS. Snapshot policies are typically defined on a recurring schedule, to
perform regular backup operations, but can be configured to run on demand too. Snapshot backup
policies can also incorporate Veeam Kasten’s logical and/or application- consistent backup capabilities
via Kanister blueprints.
2. Import: As the basis for importing a backup from an off-cluster location, import policies can be
configured to perform recurring import operations or configured as on-demand policies.
On-demand: Typically used for one-off restores, like when restoring or moving an application from one
cluster to another or restoring in a Hot-Cold scenario after a DR event.
Scheduled: Typically used to support a hot-warm DR architecture, scheduled import policies regularly
import metadata and persistent data to the DR warm site to minimize recovery time objectives (RTOs).
Veeam Kasten policies can be configured to occur at specific times through time offsets, or alternatively
during a set backup window, with the option to stagger jobs. If your backup creation is not finished within
the selected interval, it will be canceled.
© 2025 Veeam Software. Confidential information. All rights reserved. All trademarks are the property of their respective owners. 9.10.2025 | 15

Figure 8: Kasten Backup Policy with Frequency, Scheduling, and Retention Options
Disaster Recovery
DR for cloud- native and VM workloads on Red Hat OpenShift shares many similar concepts with legacy or
traditional workloads. An important distinction for cloud- native workloads is the emphasis on the
application and its data, rather than the underlying infrastructure or encapsulating VM.
In short, in a traditional application platform, an application’s state is provided at the application layer.
When you recover the application and mount the recovered data, the application state recovers. In
Kubernetes, however, application pods are ephemeral and the application state is provided by a persistent
storage layer. For this reason, when you recover, the application and its data must be cluster-aware for the
application's state to recover.
As a result, Veeam Kasten focuses on DR for cloud- native and VM workloads, rather than for the Red Hat
OpenShift cluster itself. Following that philosophy, for a hot-cold DR architecture, it is recommended that a
new Veeam Kasten instance be deployed on a newly deployed/greenfield OpenShift cluster. Then, Veeam
Kasten configuration data and data protection recovery can be restored, which in turn enables the
organization to recover protected applications.
© 2025 Veeam Software. Confidential information. All rights reserved. All trademarks are the property of their respective owners. 9.10.2025 | 16

For a hot-warm DR architecture, it is recommended that a secondary Red Hat OpenShift cluster be
deployed along with an instance of Veeam Kasten. Scheduled import policies are created to regularly
import the persistent data to the DR site for shorter recovery time objectives (RTOs).
Hot-Cold/Rebuild Hot-Cold/Replicate
|     |                |     | Red Hat       |                | Red Hat       |
| --- | -------------- | --- | ------------- | -------------- | ------------- |
|     |                |     | OpenShift on  |                | OpenShift on  |
|     |                |     | AWS (ROSA)    |                | AWS (ROSA)    |
|     | OpenShift Data |     | AWS EBS IO2   | OpenShift Data | AWS EBS IO2   |
|     | Foundation     |     | Block Storage | Foundation     | Block Storage |
|     | On-Premises    |     |               | On-Premises    |               |
Amazon EC2
|     | Datacenter |     |     | Datacenter |     |
| --- | ---------- | --- | --- | ---------- | --- |
Figure 9: DR Approaches with Kasten
|       |           |       |         |     |     |
| ----- | --------- | ----- | ------- | --- | --- |

| Strategy  |     | Recovery Time  |     | Cost (Infrastructure)  | Use Case              |
| --------- | --- | -------------- | --- | ---------------------- | --------------------- |
| Rebuild   |     | High           |     | Low                    | Pre-production/small  |
organizations with
constrained budgets
| Replicate  |     | Medium  |     | High  | Production and/or  |
| ---------- | --- | ------- | --- | ----- | ------------------ |
enterprise workloads

© 2025 Veeam Software. Confidential information. All rights reserved. All trademarks are the property of their respective owners.  9.10.2025 | 17

RTOs and RPOs
RTO and recovery point objective (RPO) definitions help organizations plan their infrastructure, backup
policies, and overall approaches to ensure the most critical systems and/or data have the lowest RTOs and
RPOs. Lower values are better, but typically more costly too. While both of these metrics are time measures,
they ultimately address two different things:
• RPO is measured before disaster. It represents the amount of time during which you may lose
unrecoverable transactions prior to the disaster.
• RTO is measured after the disaster. It represents the time it will take to make your services available for
new transactions.
Any transactions
executed during RPO
Transactions made Service is not restored,
will bedefinitely lost, Disaster
before RPO will be no transaction can
and won’t be present
restored after recovery be initiated
after recovery
time
RPO RTO
Last backup
Figure 10: DR Approaches and RTO/Cost Trade-off
3-2-1 Rule
Once we have defined all the numbers required for sizing calculations, we need to look at the infrastructure
estate. It is a best practice to follow the 3-2-1 Rule, which says:
• H ave a t le ast t h ree co p ie s of y ou r data .
• Store the copies on two different media types.
• Keep one backup copy off-site.
Veeam Kasten can help fulfill all 3-2-1 Rule requirements, as detailed below:
Have at Least Three Copies of Data
It is recommended that you always have three copies of data. These three copies can be original data
on the persistent volume claim (PVC), the snapshot data, and the snapshot data exported to an
external location.
© 2025 Veeam Software. Confidential information. All rights reserved. All trademarks are the property of their respective owners. 9.10.2025 | 18

Store the copies on Two Different Media
Veeam Kasten is storage and cloud-agnostic, meaning it supports multiple storage infrastructures,
including block, file, and object storage. For example, storing your data on PVC and external S3 counts as
two different media. Having two copies of data, one on PVC and the other as a local snapshot on the
Kubernetes cluster, does not count as two different media. In case a disaster makes the cluster beyond
recoverable, both copies of data will be lost.
Keep One Backup Copy Off-Site:
Set up backup copy jobs to transfer your backups offsite to another location like a public cloud provider or
secondary storage in a separate site. Exporting backups to a locally hosted profile via NFS file storage is not
considered offsite.
Backup and Recovery Testing
Backups are only useful if they are recoverable. Simply targeting workloads and data for backup is not
enough to ensure that organizations can withstand disaster, data corruption, ransomware attacks, or
accidental deletion. Similar to the business continuity testing described above, organizations should
perform a backup recovery test on a regular basis to make sure they are correct and can be restored.
These tests help organizations ensure they meet their RTO and RPO targets.
DR Testing
In line with testing backup and recovery, organizations should aim to conduct a full DR test too. Ideally
organizations should have an end-to-end documented DR plan in place that includes people, processes and
systems that are all documented ahead of time. This plan can serve as the single source of truth during test
exercises and in real-world events. Organizations that have the most robust and/or mature DR plans and
infrastructures will regularly run through partial or full DR tests in production environments. This could look
like failing over from datacenter A to datacenter B, or operating out of datacenter B for a set time before
failing back to datacenter A.
Application and VM Mobility
Due to the nature of how Veeam Kasten protects cloud- native applications and VMs on Red Hat OpenShift,
applications and VMs can be easily cloned or migrated both within a single Red Hat OpenShift cluster or
from one Red Hat OpenShift cluster to another. Leveraging the built-in transform engine, Veeam Kasten
can adjust applications or VMs as they are restored in a new cluster to accommodate different
configurations, such as a changing the StorageClass for a PVC, adding or removing annotations, or
adjusting the number of annotations, or adjusting the number of pod replicas.
© 2025 Veeam Software. Confidential information. All rights reserved. All trademarks are the property of their respective owners. 9.10.2025 | 19

This flexibility eases management overhead while allowing organizations to leverage heterogenous
infrastructures for their primary and secondary data centers.
Lastly, this mobility empowers organizations to perform upgrades on infrastructures with little –to no
downtime, like when upgrading from Red Hat OpenShift 3.x to 4.x.
Ransomware Protection
Encryption
Veeam Kasten provides always-on encryption, both in-flight and at-rest, for all application data and
metadata exported from the cluster.
Veeam Kasten also implements envelope encryption to provide application- and policy-unique AES-256-
GCM keys. Individual encryption keys are not stored but derived on-demand to improve security and
reduce management overhead. This design principle means that even if a ransomware attack compromises
your production data, backups will remain untouched and unreadable without the appropriate keys.
FIPS 140-3
Veeam Kasten can also be installed in FIPS mode. This leverages OpenSSL for its implementation of
cryptographic primitives and algorithms, which is provided through Red Hat's Universal Base Images (UBI).
When operating in FIPS mode, Veeam Kasten leverages only FIPS-approved algorithms and RNG methods
that are compliant with FIPS 140-3 standards. Compliance is pivotal for organizations that must adhere to
stringent security protocols, which effectively fortifies data Kubernetes data protection measures in
Kubernetes environments against sophisticated threats like ransomware.
Object Storage Immutability
Veeam Kasten allows you to prohibit the deletion of data in object storage repositories by making that data
temporarily immutable. This is done to enhance security and protect VM and application data from loss
due to attacks, malware activity (e.g., ransomware), or other actions.
Through the use of Object Lock on supported location profile storage systems, Veeam Kasten can protect
backups from being manipulated or deleted. Supported location profile storage solutions include:
• Amazon S3
• Azure Blob
• S3-compatible storage (e.g., Ceph S3, MinIO, etc)
© 2025 Veeam Software. Confidential information. All rights reserved. All trademarks are the property of their respective owners. 9.10.2025 | 20

Recommended Design
and Architecture
The recommended design and architecture is a hybrid approach, where on-premises Red Hat OpenShift
with Red Hat OpenShift Virtualization is installed and running both containerized and VM workloads.
Veeam Kasten DR is then configured to export the Veeam Kasten catalog and configuration data once per
hour. The DR passphrase is then stored securely in HashiCorp Vault.
Authentication for Veeam Kasten is configured to use the respective cluster’s Oauth authentication
mechanism, where Okta is the upstream OpenIDConnect service for each. This ensures that each cluster
shares the same identity directory for administrators, and the directory is outside both failure domains.
A second Red Hat OpenShift cluster is provisioned on a bare metal instance that’s running on Red Hat
OpenShift Service on AWS (ROSA) with EBS io2 storage as a warm standby (i.e., the replicate strategy
defined above). Here, Veeam, where Kasten is deployed and configured with a regularly scheduled import
policy.  In the event of a disaster, some or all workloads can be restored to the ROSA cluster via Veeam
Kasten, and if/when service is restored for the on-premises datacenter, VM and application workloads can
be restored back to the on-premises cluster. This leverages the same mechanism as import policies to
migrate workloads back on-premises.
Hybrid Cloud Architecture
The multi-cloud architecture is illustrated in the diagram below.
| VPC |     | VPC |     |
| --- | --- | --- | --- |
ACS
Red HatOpenShift on AWS
(ROSA)
app-1
Vault Policy-based export of
RestorePoints(app
| app-2     | metadata & PVC) |                                      |           |
| --------- | --------------- | ------------------------------------ | --------- |
| VM1 VM2   | VM3             |                                      |           |
| kasten-io | Kasten Catalog  | Policy-based import of RestorePoints | kasten-io |
Protection
Oauth
| admission- |     | Object Lock |     |
| ---------- | --- | ----------- | --- |
controller
Enabled S3-
| a d m i s s i o n  |     | Compatible |     |
| ------------------ | --- | ---------- | --- |
| co n t r o l l e r | ACS | Storage    |     |
Stream Image
| OpenShift Data         |     |     | AWS EBS IO2   |
| ---------------------- | --- | --- | ------------- |
| Foundation             |     |     | Block Storage |
| On-Premises Datacenter |     |     | Amazon EC2    |
Figure 11: Veeam Kasten and Red Hat OpenShift Multicloud Architecture

© 2025 Veeam Software. Confidential information. All rights reserved. All trademarks are the property of their respective owners.  9.10.2025 | 21

Continuous Deliver (CD) with ArgoCD
ArgoCD is an open source continuous delivery (CD) tool that automates the deployment and management
of applications on Kubernetes clusters.
ArgoCD can be easily installed on a Red Hat OpenShift cluster with the Red Hat OpenShift GitOps operator,
available on the Red Hat Operator Hub.
By leveraging ArgoCD to deploy Veeam Kasten to various Red Hat OpenShift clusters, administrators can
ensure it is deployed in a standardized, repeatable way, while minimizing the risk of misconfiguration due to
human error. Plus, because Veeam Kasten is a Kubernetes application and its resources are defined via
standardized Kubernetes resources, it can be managed and synchronized automatically via ArgoCD.
Veeam Kasten can be deployed and managed by either using the ArgoCD user interface or the argocd cli.
For more information on how to deploy and manage Veeam Kasten via ArgoCD, refer to this GitHub project.
For a simple practical example of how to use ArgoCD pre-sync jobs to protect applications automatically,
refer to this GitHub project.
Integration of Veeam Kasten with Red Hat
Advanced Cluster Security for Kubernetes
Because Veeam Kasten is a data protection solution, it requires a broad set of permissions to read and write
to namespaces and infrastructure. Therefore, it should be closely monitored and protected against
unauthorized access and manipulation. While this product has been implemented in the most secure way
possible, it should be monitored and protected as a critical component of the overall platform. With Red Hat
Advanced Cluster Security for Kubernetes (RHACS), policies can be created specifically to monitor, alert, and
enforce Veeam Kasten configurations.
Figure 12: Red Hat Advanced Cluster Security Monitoring of Kasten
© 2025 Veeam Software. Confidential information. All rights reserved. All trademarks are the property of their respective owners. 9.10.2025 | 22

Using the policy management capabilities within RHACS, we can easily create policies to defend against
unauthorized secret manipulation, such as changing the Kasten DR password. The Kasten DR password is
used to encrypt Kasten DR backups and is required to perform recoveries. Unfortunately, if it is accessed or
changed by a threat actor, it can be used to exfiltrate critical application data or be an attack
vector for ransomware.
Below is an example policy that was implemented within RHACS to monitor and alert on any unauthorized
operations or secrets within the kasten-io namespace:
{
"policies": [
{
"id": "ef083648-54dc-433d-bf15-e24ea0c787e2",
"name": "Kasten DR Secret Compromised",
"description": "Someone has changed the K10 Disaster Recovery
Secret",
"rationale": "Changing the Kasten DR Recovery passphrase could
allow a malicious actor to recover your backup data and workloads from the
off-cluster storage",
"remediation": "Ensure you rotate the passphrase often",
"disabled": false,
"categories": [
"Anomalous Activity",
"Kubernetes Events"
],
"lifecycleStages": [
"RUNTIME"
],
"eventSource": "AUDIT_LOG_EVENT",
"exclusions": [],
"scope": [
{
"cluster": "839fa90b-eb54-48ae-984b-8de59418ac51",
"namespace": "kasten-io",
"label": null
}
],
"severity": "CRITICAL_SEVERITY",
"enforcementActions": [],
"notifiers": [],
"lastUpdated": "2024-08-06T15:50:49.742922674Z",
"SORTName": "",
"SORTLifecycleStage": "",
"SORTEnforcement": false,
"policyVersion": "1.1",
"policySections": [
{
"sectionName": "Policy Section 1",
"policyGroups": [
{
"fieldName": "Kubernetes Resource",
"booleanOperator": "OR",
"negate": false,
© 2025 Veeam Software. Confidential information. All rights reserved. All trademarks are the property of their respective owners. 9.10.2025 | 23

"values": [
{
"value": "SECRETS"
}
]
},
{
"fieldName": "Kubernetes API Verb",
"booleanOperator": "OR",
"negate": false,
"values": [
{
"value": "UPDATE"
},
{
"value": "DELETE"
},
{
"value": "PATCH"
},
{
"value": "GET"
}
]
},
{
"fieldName": "Kubernetes User Name",
"booleanOperator": "OR",
"negate": true,
"values": [
{
"value": "system:serviceaccount:kasten-
io:k10-k10"
}
]
}
]
}
],
"mitreAttackVectors": [],
"criteriaLocked": false,
"mitreVectorsLocked": false,
"isDefault": false
}
]
© 2025 Veeam Software. Confidential information. All rights reserved. All trademarks are the property of their respective owners. 9.10.2025 | 24

Additionally, a policy can be configured to monitor, alert, and enforce the restriction of executing code or
scripts within Veeam Kasten pods. This policy can be implemented easily by cloning the Kubernetes Actions:
Exec into pod policy and applying the following changes:
Configuration Item Value
Severity Critical
Description Alerts when Kubernetes API receives a request to execute a
command in a Veeam Kasten container. This could represent
an attack via the backup infrastructure.
Restrict by scope — inclusion scope
Cluster <cluster name>
Namespace kasten-io
Integration of Veeam Kasten
with Veeam Data Platform
Veeam Kasten Veeam Data Platform Plug-in
While Veeam Kasten is distinct from Veeam Data Platform (formerly Veeam Backup & Replication) due to
the differing architecture of Kubernetes, various management and reporting capabilities can be integrated
within the Veeam Data Platform console via the Veeam Kasten Veeam Data Platform plug-in.
When adding a Veeam Kasten instance through the Veeam Kasten plug-in, credentials must be
specified so Veeam Data Platform can retrieve and manage backup policies from Veeam Kasten. If using
Red Hat OpenShift Authentication (OAuth), it is recommended that you use a service account
defined within OpenShift.
apiVersion: v1
kind: ServiceAccount
metadata:
name: vbr-kasten
namespace: default
Once created, the service account should be assigned to the k10-admin role using a ClusterRoleBinding:
kind: ClusterRoleBinding
apiVersion: rbac.authorization.k8s.io/v1
© 2025 Veeam Software. Confidential information. All rights reserved. All trademarks are the property of their respective owners. 9.10.2025 | 25

metadata:
name: vbr-k10-admin
subjects:
- kind: ServiceAccount
name: vbr-kasten
namespace: default
roleRef:
apiGroup: rbac.authorization.k8s.io
kind: ClusterRole
name: k10-admin
Once configured and authenticated, Veeam Kasten policy runs will be visible within the Veeam Data
Platform console.
For more information around how to configure this plug-in for Veeam Kasten, review the
Veeam Documentation.
Veeam Data Platform Repository for Kasten Backup Data
For existing Veeam and VMware customers, Veeam Kasten supports using a Veeam Repository. The
prerequisites for leveraging this Veeam Repository for Veeam Kasten backups of Red Hat OpenShift
Virtualization VMs are as follows:
• VM disks must be stored on a vSphere CSI-provisioned storage class.
• A separate S3 or NFS location profile is required to store VM metadata.
Because this reference architecture employs storage via OpenShift Data Foundation (ODF),
traditional Veeam repositories cannot be leveraged for backup data, and therefore will not be
covered in this document.
For more information on Veeam Repository location, refer to the relevant Kasten documentation.
© 2025 Veeam Software. Confidential information. All rights reserved. All trademarks are the property of their respective owners. 9.10.2025 | 26

Feature and Functionality
Implementation to Support
VMs and Applications
Deployment Configuration
On-Premises
Network
By default, OpenShift Virtualization is installed with a single, internal pod network. Subsequent networks are
configured by installing the Kubernetes NMState Operator. Once installed, administrators can configure
additional networks and a Linux bridge network to allow external access to VMs. Additional network
management tools, such as Cisco Application Centric Infrastructure (ACI), Juniper Apstra, F5 XC, Tigera,
and others are often used to provide additional functionality.
Storage
Persistent storage is required for stateful applications that run in Kubernetes clusters. Many traditional
storage vendors provide Container Storage Interface (CSI) drivers to enable their hardware to work with
Kubernetes. Administrators should review operators for scalability and feature completeness since storage
vendors differ in the readiness of their CSI drivers for workloads that run in Kubernetes.
Several container-native storage solutions exist that use the CSI framework. These can also build scalability
for several storage classes and access modes, as well as the other data services expected for workloads
that run in Red Hat OpenShift. Notable solutions include IBM Storage Fusion, Portworx Enterprise, and Red
Hat OpenShift Data Foundation.
For this reference architecture, we will refer to OpenShift Data Foundation (ODF) as the software-defined
storage for our OpenShift cluster. ODF provides file and block storage for containerized and VM workloads
within the Red Hat OpenShift cluster. ODF can also be used to provision a multi-cloud object gateway and
S3-compatible immutable object storage. In this reference architecture, however, we use Amazon S3 with
immutable object storage to ensure that backup data is stored off-site in a separate failure domain from
the primary cluster.
ODF provides the requisite read/write/many capabilities for block volumeMode PVCs, as noted in the
“Storage Considerations for VM Workloads” section above.
© 2025 Veeam Software. Confidential information. All rights reserved. All trademarks are the property of their respective owners. 9.10.2025 | 27

Storage Validation
The Red Hat ODF CSI can be validated using Kasten’s k10_primer tools. These tools perform tests on the
target cluster storage to validate that the required capabilities and configurations are in place to support
block volumeMode exports in Veeam Kasten.
For Veeam Kasten to protect VMs on ODF RADOS Block Device (RBD) storage and perform backup exports,
the storage class needs the following annotation:
k10.kasten.io/sc-supports-block-mode-exports=true
This annotation can be observed in the example StorageClass definition below:
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
annotations:
description: Provides RWO and RWX Block volumes suitable for Virtual
Machine disks
storageclass.kubevirt.io/is-default-virt-class: "true"
name: ocs-storagecluster-ceph-rbd-virtualization
parameters:
clusterID: openshift-storage
csi.storage.k8s.io/controller-expand-secret-name: rook-csi-rbd-provisioner
csi.storage.k8s.io/controller-expand-secret-namespace: openshift-storage
csi.storage.k8s.io/fstype: ext4
csi.storage.k8s.io/node-stage-secret-name: rook-csi-rbd-node
csi.storage.k8s.io/node-stage-secret-namespace: openshift-storage
csi.storage.k8s.io/provisioner-secret-name: rook-csi-rbd-provisioner
csi.storage.k8s.io/provisioner-secret-namespace: openshift-storage
imageFeatures: layering,deep-flatten,exclusive-lock,object-map,fast-diff
imageFormat: "2"
mapOptions: krbd:rxbounce
mounter: rbd
pool: ocs-storagecluster-cephblockpool
provisioner: openshift-storage.rbd.csi.ceph.com
reclaimPolicy: Delete
volumeBindingMode: Immediate
Note that, in the storage class above, the parameter mapOptions is set to “krbd:rxbounce”. This is to
mitigate CRC/signature issues in Windows VMs as outlined in this kubevirt article.
Additionally, the volumesnapshotclass requires the following annotation:
k10.kasten.io/is-snapshot-class=true
© 2025 Veeam Software. Confidential information. All rights reserved. All trademarks are the property of their respective owners. 9.10.2025 | 28

The k10_primer tools can be run to validate that the cluster is able to provision, snapshot, and export block
mode PVCs for VMs provisioned within the Red Hat OpenShift cluster.
curl https://docs.kasten.io/tools/k10_primer.sh | bash /dev/stdin blockmount -
s ocs-storagecluster-ceph-rbd-virtualization
Compute
For this reference architecture, a Red Hat OpenShift cluster was deployed on three Dell R720
Rackmount servers.
Air-Gapped and Offline Environments
Veeam Kasten supports air-gapped installation for highly secure or remote environments. This leverages an
on-premises private container registry with Helm or the Red Hat offline operator. Using Helm versus
OpenShift Operator will be decided by the organization or agency requirements. Below is a table outlining
key considerations for these two different approaches.

|     | Offline Helm  | Offline Red Hat OpenShift Operator  |
| --- | ------------- | ----------------------------------- |
Mechanism  Ability to use caching or proxy via a hosted  Private registry leveraging mirrored
|         | container image repository (e.g. JFrog  | and pruned Red Hat marketplace  |
| ------- | --------------------------------------- | ------------------------------- |
|         | Artifactory) or manual upload           | index image                     |
| Method  | k10offline tool                         | opm and oc cli                  |
Options/Considerations  Can leverage Iron Bank K10  Can remove default Red Hat Operator
|     | Container Images  | catalog services  |
| --- | ----------------- | ----------------- |
Kasten Red Hat OpenShift Offline
| Reference  | Kasten Air-Gapped Install  |     |
| ---------- | -------------------------- | --- |
Operator Install

© 2025 Veeam Software. Confidential information. All rights reserved. All trademarks are the property of their respective owners.  9.10.2025 | 29

Public Cloud
Network
In a hot/warm architecture, we can implement the same layer-three networking and IP schema within the
ROSA cluster as what was implemented in the on-premises configuration. This ensures that, as VM
workloads are restored into the ROSA cluster, they will have the requisite connectivity to continue
operations without having to re-IP the VM.
Storage
Amazon EBS io2 SSD storage is leveraged for optimum performance for VM workloads. Aside from direct
read-write performance benefits, full CBT is available for optimized backup and restore performance,
where only changed blocks are read, deduped, compressed, and transmitted for each incremental backup.
Amazon EBS io2 storage provides the requisite read/write/many block VolumeMode capabilities noted in
the “Storage Considerations for VM Workloads” section above.
Storage Validation
The AWS EBS io2 CSI can be validated using Kasten’s k10_primer tools. These tools perform tests on target
cluster storage to validate that the required capabilities and configurations are in place to support block
VolumeMode exports in Veeam Kasten.
For Veeam Kasten to protect VMs on io2 storage and perform backup exports, the storage class needs the
following annotation:
k10.kasten.io/sc-supports-block-mode-exports=true
This annotation can be observed in the example StorageClass definition below:
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
name: io2
annotations:
k10.kasten.io/sc-supports-block-mode-exports: "true"
storageclass.kubernetes.io/is-default-class: "true"
provisioner: ebs.csi.aws.com
volumeBindingMode: WaitForFirstConsumer
parameters:
type: io2
iopsPerGB: "200"
© 2025 Veeam Software. Confidential information. All rights reserved. All trademarks are the property of their respective owners. 9.10.2025 | 30

Additionally, the volumesnapshotclass requires the following annotation:
k10.kasten.io/is-snapshot-class=true
The k10_primer tools can be run to validate the cluster is able to provision, snapshot, and export block mode
PVCs for VMs provisioned within the Red Hat OpenShift cluster.
curl https://docs.kasten.io/tools/k10_primer.sh | bash /dev/stdin blockmount -
s io2
Compute
ROSA is deployed with a “Classic” control plane using the c5n.metal instance type. At the time of authoring,
Hosted Control Plane (HCP) is not supported for ROSA with OpenShift Virtualization.
A minimum cluster footprint of two worker nodes is deployed to serve as a warm standby and run the
Veeam Kasten application. In the event of disaster, additional nodes can be quickly added to
accommodate the restoration of OpenShift Virtualization VM and cloud-native application workloads.
Veeam Kasten Configuration
Veeam Kasten is deployed to each Red Hat OpenShift cluster via the OpenShift certified Operator.
Each cluster is deployed with the additional configuration options configured for Veeam Kasten to enable
Oauth configuration:
scc
create: true
route
enabled: true
tls
enabled: true
auth:
openshift
enabled: true
dashboardURL=https://k10-route-kasten-io.${APPS_BASE_DOMAIN}/k10/
openshiftURL=https://${API_BASE_DOMAIN}:6443
insecureCA: false
Kasten Multi-Cluster
The Veeam Kasten instance deployed in the on-premises data center is configured with multi-cluster
enabled, with itself set as primary. The Veeam Kasten instance deployed within ROSA is configured as a
secondary cluster.
A global location profile policy is configured and distribution is created to ensure that the same AWS S3
location profile is distributed to both Veeam Kasten instances.
© 2025 Veeam Software. Confidential information. All rights reserved. All trademarks are the property of their respective owners. 9.10.2025 | 31

Veeam Kasten Policies
The primary Veeam Kasten cluster is configured with two backup policies with the following settings:
Item Value
Name app1-backup
Action Snapshot
Backup Frequency Hourly
Backup Window From: 8:00pm
To: 4:00am local time
Use staggering enabled
Snapshot Retention 12 hourly snapshots
7 daily snapshots
4 weekly snapshots
2 monthly snapshots
2 yearly snapshots
Enable Backups via Snapshot Exports Enabled
Export frequency: Every snapshot
Export location profile: S3ObjectStorage
Select Applications By Name
Applications to target: app-1
Select Application Resources All resources
Table 4: Primary Policy 1
Item Value
Name app2-backup
Action Snapshot
Backup Frequency Hourly
Backup Window From: 8:00pm
To: 4:00am local time
Use staggering enabled
Snapshot Retention 12 hourly snapshots
7 daily snapshots
4 weekly snapshots
© 2025 Veeam Software. Confidential information. All rights reserved. All trademarks are the property of their respective owners. 9.10.2025 | 32

Item Value
2 monthly snapshots
2 yearly snapshots
Enable Backups via Snapshot Exports Enabled
Export frequency: Every snapshot
Export location profile: S3ObjectStorage
Select Applications By Name
Applications to target: app-1
Select Application Resources All resources
Table 5: Primary Policy 2
The secondary cluster is configured with the following policies:
Item Value
Name app1-import
Action Import
Restore After Import Enabled
Data-only restore enabled
Backup Frequency Hourly
Config Data for import <token exported from primary cluster>
Profile for Import S3ObjectStorage
Table 6: Secondary Policy 1
© 2025 Veeam Software. Confidential information. All rights reserved. All trademarks are the property of their respective owners. 9.10.2025 | 33

Item Value
Name app2-import
Action Import
Restore After Import Enabled
Data-only restore enabled
Backup Frequency Hourly
Config Data for import <token exported from primary cluster>
Profile for Import S3ObjectStorage
Table 6: Secondary Policy 1
With the above policies in place, the hot/warm DR architecture is in place, where, in the event of failure, a
full restore on the ROSA cluster can be triggered either manually via the UI, via a RestoreAction using
YAML, or automatically triggered via Ansible.
© 2025 Veeam Software. Confidential information. All rights reserved. All trademarks are the property of their respective owners. 9.10.2025 | 34

Permutations and Other Patterns
Following the reference architecture defined above, organizations can achieve a robust virtualization
platform while minimizing RTOs and balancing cloud costs. The architecture noted above can be adapted
into several other patterns:
On-Premises Only
Rather than leveraging public cloud solutions such as AWS ROSA, the secondary site could be deployed in
an on-premises or collocated datacenter. Ideally, the secondary site is in a completely independent failure
domain, so in the event of disaster, workloads can be recovered with no dependency on resources or assets
in the primary datacenter. This approach would require additional sizing considerations since the flexibility
of scaling up or down worker nodes in AWS EC2 is not available in an entirely on-premises pattern.
Public Cloud Only
Equivalently, the architecture can be adapted to use only public cloud infrastructures for the primary and
secondary sites. Ideally this would be accomplished using two different cloud providers (e.g. ROSA on AWS
and ROKS on IBM Cloud), to account for potential provider outages and leverage completely independent
infrastructure (e.g. geographic location, network, storage, and compute infrastructure, etc.).
The caveat around storage requirements should be kept in mind when choosing public cloud providers. For
instance, at the time of authoring, Azure does not offer bare metal instances, which is required for
OpenShift Virtualization.
Tertiary/Multi-site
This reference architecture can be easily expanded to include additional sites, or implement a hot-warm-
cold, or hot-hot-warm approach. For hot-hot, ODF synchronous replication can be used to stretch storage
across sites, where Veeam Kasten provides backup and recovery capabilities like in the event of accidental
deletion or data corruption.
© 2025 Veeam Software. Confidential information. All rights reserved. All trademarks are the property of their respective owners. 9.10.2025 | 35

References
ID Asset
R1 Red Hat OpenShift Virtualization Reference Architecture
R2 Veeam Kasten Best Practice Guide
R3 Veeam Kasten Best Practice Guide
R4 Red Hat OpenShift Documentation
Table 8: References
© 2025 Veeam Software. Confidential information. All rights reserved. All trademarks are the property of their respective owners. 9.10.2025 | 36