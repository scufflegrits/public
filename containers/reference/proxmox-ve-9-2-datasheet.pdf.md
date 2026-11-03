P R O X M O X
V I R T U A L
E N V I R O N M E N T

O V E R V I E W

B E N E F I T S

Proxmox Virtual Environment is a complete, open-
source solution for enterprise virtualization that
integrates the KVM hypervisor and Linux containers
(LXC), software-defined storage (SDS) and networking
(SDN) on a single platform. From the central user
interface, you can manage VMs and containers,
storage resources, network configuration, and high
availability for clusters. The interface also provides
access to multiple out-of-the-box tools for tasks such
as backup/restore, live-migration, storage replication,
and firewall configuration. Proxmox VE is designed
to scale to cluster-level and enables you to virtualize
even the most demanding of Linux and Windows
application workloads. By combining two virtualization
technologies on a single platform, Proxmox VE
provides maximum flexibility for your data center.
It includes strong high-availability (HA) support and –
thanks to the unique multi-master design – you don’t
need any additional management server, thus saving
resources and allowing HA without a single point of
failure (SPOF).

E N T E R P R I S E - R E A D Y

Enterprises use the powerful Proxmox VE platform
to easily install, manage, and monitor their hyper-
converged (HCI) data centers. Multiple authentication
sources, combined with role-based user and
permission management enable flexible control of
HA clusters. The REST API enables easy integration
of third-party management tools, such as custom
hosting environments. The future-proof and
open-source development model of Proxmox VE
guarantees full access to the product’s source code as
well as maximum flexibility and security.

Streamlined IT Infrastructure
A single platform to manage VMs, containers,
storage, and networks.

Unified Operations
Seamlessly deploy and monitor VMs and
containers with the intuitive REST API, GUI,
and CLI for easy operation and integration.

Software-Defined Storage

SDS made simple – Thanks to built-in support
for Ceph, ZFS, and other storage backends.

Scale without Limits

Build highly available clusters in minutes and
easily scale clusters to support your growing
workloads.

100% Open-Source
No hidden licensing fee and full access to
source code for customization.

Made for Production
Keep your business running smoothly with
Enterprise-grade services & technical support
from Proxmox.

1/6© 2026 Proxmox Server Solutions. All rights reserved. All trademarks are the property of their respective owners.PROXMOX VIRTUAL ENVIRONMENT V9.2DATASHEETIndustry-leading Enterprise Virtualization

 Highly Available (HA) Cluster

 D Linux and Windows servers, 32- and 64-bit

operating systems.

 D Support for the latest Intel and AMD server chip

sets – for great VM performance.

 D Near bare-metal performance for real-world

enterprise workloads.

 D No single point of failure (no SPOF).
 D Multi-master cluster.
 D Manage the HA settings for KVM and LXC via GUI.
 D Cluster Resource Scheduling (CRS), including
dynamic mode with real-time node and guest
resource utilization.       N E W

 D Management layer containing all the capabilities

 D pmxcfs – unique Proxmox VE Cluster File

to manage and monitor an open-source,
software-defined data center.

 D Import wizard for VMware ESXi VMs.

Free & Open-Source Software
 D Licensed under the GNU AGPL, v3.
 D Debian-based, using the Proxmox kernel with

OpenZFS support.

 D Designed for community cooperation.
 D Public code repository (Git).
 D Open development on transparent mailing list.
 D Bug tracker for issue tracking.
 D Community support forum.
 D Documentation, project page, video tutorials,

howto guides, and much more.

Enterprise Support Agreement
 D Avoid hidden costs with clear subscription model.
 D Flexible support options that grow with your needs.
 D Access to the stable and extensively tested

Enterprise Repositories for Proxmox VE and Ceph.

 D Updates and version upgrades via GUI.
 D Proxmox Offline Mirror tool to keep air-gapped

systems up-to-date.

 D Premium technical support from the highly-skilled

Proxmox support team.

 D Supported by a global network of 3,000 official
Proxmox integration partners for deployment,
migration, and professional services.

Self-Fencing
 D The Proxmox VE HA Manager uses self fencing, pro-
vided by hardware watchdog or kernel softdog timers.

 D No simultaneous data access or corruption.
 D Works „out-of-the-box“.
 D Includes Proxmox VE HA Simulator for testing.

System: database-driven file system for storing
configuration files, replicated in real-time across
all nodes using Corosync.

 D Based on proven Linux HA technologies, providing

stable and reliable HA service.

 D Resource agents for KVM and containers (LXC).
 D Watchdog-based fencing.
 D HA node and resource affinity rules.
 D Dynamic Load Balancer for HA-managed guests to
reduce node imbalance across the cluster.       N E W

 D Preserves HA resource state during planned

maintenance workflows.       N E W
 D HA arm/disarm workloads.       N E W

Unified Virtual Guests Operation
 D Create and maintain VMs and containers on a

single platform.

 D Set hard and soft limits for CPU and Memory.
 D Pin virtual guests to a set of CPU cores.
 D Migrate to any cluster node.

Virtual Machines with QEMU/KVM
 D Independent from OS: Run unmodified Windows,

Linux, BSD, or others.

 D QEMU/KVM for low overhead.
 D Custom CPU models to tailor virtual CPU

features for specific workloads and compatibility
requirements.       N E W

 D Snapshot a full VM; optionally with memory (live).
 D Hot-plug network devices, USB devices, disks,

CPUs, and memory to a running VM.

 D PCI(e) pass-through using the GUI.
 D Import VMs from other hypervisors (via OVF/OVA
files) directly via the GUI from file-based storages.

 D Setup UEFI with secure boot and a Trusted

Platform Module (TPM) to run modern guest OS.

 D View guest display from anywhere with noVNC
HTML5 web console or SPICE client (virt-viewer).

2/6© 2026 Proxmox Server Solutions. All rights reserved. All trademarks are the property of their respective owners.PROXMOX VIRTUAL ENVIRONMENT V9.2DATASHEETContainers with LXC

Software-Defined Storage (SDS) with Ceph

 D Proxmox Container Toolkit (pct) provides easy and
flexible management of Linux Container (LXC).

 D Ready-to use images of most common Linux
distributions, TurnKey Linux templates, and
support for OCI images.

 D Fine-grained memory and CPU resource control.
 D Shares the host kernel: Almost zero overhead.
 D Security features like AppArmor, seccomp,

 D Integrated Ceph, a distributed object store and file

system.

 D Management via GUI or CLI.
 D Easy-to-use installation wizard.
 D Run Ceph RBD and CephFS directly on the

Proxmox VE cluster nodes.

 D Proxmox delivers its own Ceph packages.
 D Ceph support is included in the support

Cgroups, and kernel namespaces.

agreement.

 D Snapshot and rollback the full container state at

 D Add external Ceph clusters as storage via GUI.

Software-Defined Network (SDN)
 D Manage and control complex networking

configurations and multi-tenant setups via GUI.
 D Separate the different network areas into zones
consisting of virtual networks (VNets), optionally
including IP address management (IPAM).

 D Applicable to all sizes of networks, from a simple
routed NAT setup, traditional separation into
802.1q VLANs, to features like QinQ, VXLAN
tunneling, and BGP-based EVPN infrastructures.
 D Cluster-wide synchronization of the configuration.
 D Live reload after a configuration is changed.
 D Dynamic routing protocols including OpenFabric,

OSPF and BGP.       N E W

Linux Network Stack
 D Flexible options to manage local nodes.
 D Well-known tools with configuration via the GUI.
 D IPv4 and IPv6 support.
 D Support for VLANs, bonds, and bridges.

any time.

 D Quick maintenance with web console (xterm.js).

Live/Online Migration
 D Move QEMU VMs from one physical host to

another with zero downtime.
 D Local storage live-migration.
 D Live migration with mediated devices.

Flexible Storage Options
 D Local storage such as ZFS, Btrfs, LVM, and

LVMthin.

 D Shared storage such as CIFS, iSCSI or NFS.
 D Distributed storage such as Ceph RBD and

CephFS.

 D Encryption support for Ceph OSD and ZFS.
 D Unlimited number of storage definitions

(clusterwide).

Storage Replication Stack (ZFS)
 D Built-in, open-source storage replication

framework.

 D Redundancy for guests using local storage.
 D Data availability without using shared storage.
 D Asynchronous replication.
 D Minimize data loss in the case of a failure.
 D Improve reliability, fault-tolerance, and

accessibility of your data.

 D Enables fast, live migration (sync only delta since

last replication).

 D Flexible scheduling options with the calendar

events format.

3/6© 2026 Proxmox Server Solutions. All rights reserved. All trademarks are the property of their respective owners.PROXMOX VIRTUAL ENVIRONMENT V9.2DATASHEETBackup and Restore

Multiple Authentication Sources

 D Full backups of VMs and containers.
 D Live snapshot backups.
 D Define flexible backup job schedules with the

calendar event format.

 D Configure multiple backup storages.
 D GUI and CLI integration.
 D Backup and restore via GUI.
 D Set up backup retention policies via GUI.
 D Run scheduled backup jobs manually in the GUI.
 D Monitor backup jobs in the GUI via the tab “Tasks”.
 D Automatically add notes to backups using a

template.

 D Backup fleecing using fast local storage as a buffer
for I/O-heavy guests with slow backup targets.
 D Support for 3rd party backup provider plugins.

Integration of Proxmox Backup Server
 D Full support for the open-source, enterprise

backup solution from Proxmox.

 D Incremental, fully deduplicated backups of VMs,

containers, and physical hosts.

 D QEMU dirty-bitmaps for extremely fast VM backup.
 D Strong encryption on the client-side, with easy

encryption key management.
 D Single-file and directory restore.
 D With live-restore, guests start as soon as the

 D Proxmox VE supports multiple authentication

realms.

 D Linux PAM standard authentication
(e.g., ‘root’ and other local users).

 D Built-in Proxmox VE authentication server.
 D Microsoft Active Directory (MS ADS).
 D LDAP
 D Single Sign-On (SSO) with OpenID Connect.
 D Regular and automated user synchronization for

LDAP/AD realms

Flexible Access Control
 D User and permission management for all

objects (VMs, storage systems, nodes, hardware
resources, networking zones, etc.) .

 D Proxmox VE comes with a number of predefined
roles (groups of privileges) which cover common
use cases. The contained privileges can be seen in
the GUI.

 D Permissions to control access to objects (access
control lists). Each permission specifies a subject
(user or group) and a role (set of privileges) on a
specific path.

 D Create API Tokens and lock them further down for

secure, and easily revocable access.

 D Restricted by default: new users or API tokens do

restore does.

not have any permissions.

Disk Management
 D View all disks and their partitions.
 D Check S.M.A.R.T health status of disks.
 D Wipe all data from a partition or disk via the GUI.
 D Create ZFS (RAID-Z, dRAID, RAID 0/1/10),

LVM(-thin) and file based (ext4, XFS) storages.

VM Templates and Clones
 D Deploying VMs from templates is blazing fast, very
convenient, and if you use linked clones, highly
storage efficient.
 D Linked and full clones.

Two-Factor Authentication
 D Providing high security.
 D Support for multiple 2nd factors for a single

account.

VM Hardware passthrough
 D Assign PCI(e) or USB devices to VMs and

containers via the GUI.

 D Hot-plug USB devices and ports into running VMs.
 D Use virtual functions to share a single device with

 D Ability to use a hardware token (Webauthn, TOTP,

multiple guests.

Yubikey-OTP).

 D Generate single-use recovery codes.
 D TFA/TOTP lockout to protect against brute-force

 D Pass through whole disks using the CLI.
 D Resource mappings for VMs, with hardware pass-
through/cluster-wide mapping of PCI/USB devices.

attacks.

4/6© 2026 Proxmox Server Solutions. All rights reserved. All trademarks are the property of their respective owners.PROXMOX VIRTUAL ENVIRONMENT V9.2DATASHEETProxmox VE Firewall

REST API

 D Supporting IPv4 and IPv6.
 D Linux-based netfilter technology. Stateful firewall

for easy, dynamic filtering.

 D Distributed: configurations in Proxmox VE cluster file
system, with filtering rules applied on each node.
 D Cluster-wide IP sets, aliases, and security groups.
 D Tight integration with the SDN functionality
(access of IPAM information as IP-sets).

 D 3 levels of configuration (data center, host, VM/CT).
 D Support for custom ‘raw’ tables; enable SYN flood

attack protection.

 D Easy integration for third-party management tools.
 D Rest API (JSON as primary data format).
 D Alternative human-readable API format with

interactive browser, as built-in documentation.

 D Full support for API tokens.
 D Automatic JSON Schema powered parameter

verification.

 D Easy means of creating command line tools (use

the same API).

 D Resource Oriented Architecture (ROA).
 D Declarative API definition using JSON Schema.

Web-based Management Interface
 D Integrated - no need to install a separate manage-
ment tool nor any additional management node.

 D Fast and easy creation of VMs and containers.
 D Seamless integration and easy management of an

entire cluster. Group virtual guests by assigned tags.

 D Fast, search-driven interface able to handle

thousands of VMs and containers.

 D Based on the Ext JS JavaScript framework.
 D Secure HTML5 console, supporting SSL.
 D Let’s Encrypt TLS certificates via the ACME-based

DNS or HTTP challenge mechanism.
 D Subscription management via GUI.
 D Simple management of APT package repositories,

and upgrades via GUI.

 D Modern web interface for cluster management on

mobile devices.

 D Integrated documentation.

Command Line (CLI)
 D Manage all components of your virtual

environment.

 D CLI with intelligent tab completion.
 D Full UNIX man page documentation.

Modern Linux Server Experience
 D Flexible notification system: rule-based

notifications sent as email via local Postfix MTA or
authenticated SMTP, or sent via a Gotify instance.

 D Webhooks for the notification system enable
system events to trigger HTTP requests.

 D Secure boot compatibility.
 D Kernel pinning: select preferred kernel version.
 D Automated and unattended installation for full
automation of the setup of bare-metal nodes.
 D Tailored installation ISO offering installation via

GUI, terminal, or serial port.

Android App
 D Connect to Proxmox VE instances.
 D Manage clusters, nodes, VMs, and containers.
 D Access SPICE and HTML5 consoles.
 D Based on the Flutter framework.

GPU workloads
 D GPU Passthrough.
 D Officially supported plattform for NVIDIA vGPU.

5/6© 2026 Proxmox Server Solutions. All rights reserved. All trademarks are the property of their respective owners.PROXMOX VIRTUAL ENVIRONMENT V9.2DATASHEETL E A R N   M O R E

Project page: pve.proxmox.com
Bugtracker: bugzilla.proxmox.com
Code repository: git.proxmox.com

H O W   T O   B U Y

Visit the Proxmox Online Shop to purchase a subscription: shop.proxmox.com
Find an authorized reseller in your area: www.proxmox.com/partners/explore

H E L P   A N D   S U P P O R T

Proxmox Customer Portal: my.proxmox.com
Community Support Forum: forum.proxmox.com

T R A I N I N G   P R O X M O X   V E

Learn Proxmox VE easily – Visit a training:
www.proxmox.com/services/training

S A L E S
I N Q U I R I E S ?

Please contact our team:
sales@proxmox.com.

A B O U T   P R O X M O X

Proxmox Server Solutions GmbH is a software provider dedicated to developing powerful and efficient open-source
server solutions. The privately held company is based in Vienna (Europe).

Proxmox Server Solutions GmbH

Bräuhausgasse 37, 1050 Vienna, Austria
office@proxmox.com, www.proxmox.com

© 2026 Proxmox Server Solutions. All rights reserved. All trademarks are the property of their respective owners.

6 / 6

6/6© 2026 Proxmox Server Solutions. All rights reserved. All trademarks are the property of their respective owners.PROXMOX VIRTUAL ENVIRONMENT V9.2DATASHEET
