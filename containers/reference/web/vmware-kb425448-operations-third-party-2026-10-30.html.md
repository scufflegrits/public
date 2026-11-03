---
title: Compatibility and Support Policy for VMware Aria Operations on Proxmox and Third-Party Hypervisors
url: https://knowledge.broadcom.com/external/article/425448/compatibility-and-support-policy-for-vmw.html
hostname: broadcom.com
description: Compatibility and Support Policy for VMware Aria Operations on Proxmox and Third-Party Hypervisors
sitename: Broadcom Inc
date: "2026-01-01"
fingerprint: f5e6189fd4ebcf1e
---
VCF Operations/Automation (formerly VMware Aria Suite)

Customers may inquire whether migrating the **VMware Aria Operations** (formerly vRealize Operations) virtual appliance or **Cloud Proxy** from a VMware vSphere environment to a third-party hypervisor, such as **Proxmox VE (KVM)**, is a supported configuration. This article clarifies the official support stance from Broadcom regarding the hosting of Aria Operations components on non-VMware platforms.


- **Product:** VCF Operations / VMware Aria Operations (All Versions)
- **Appliance Type:** Analytics Nodes, Witness Nodes, Cloud Proxies
- **Source Hypervisor:** VMware ESXi
- **Target Hypervisor:** Proxmox VE, KVM, Nutanix AHV, Microsoft Hyper-V


Broadcom provides VMware Aria Operations as a hardened, pre-configured **Virtual Appliance (OVA)**. This appliance is engineered, tested, and certified specifically for the VMware vSphere stack. Moving the appliance to a third-party hypervisor alters the underlying hardware abstraction layer, which the software is not designed to handle.

**Running the VMware Aria Operations virtual appliance on Proxmox VE or any other third-party hypervisor is not supported.**

To maintain a supported status and ensure operational stability, the following requirements must be met:

The VMware Aria Operations virtual appliance and Cloud Proxy must be deployed on hosts running:

- **VMware ESX/ESXi 6.5 Update 1 or later.** 
- Managed by **VMware vCenter Server 6.5 or later.**

**Note:** If you are currently on ESXi 6.0 or older, you must upgrade your vCenter and ESXi to version 6.5 U1+ before migrating or upgrading to recent versions like Aria Operations 8.18.x.


While technical workarounds may allow the appliance to boot on Proxmox (KVM), Broadcom does not support this due to:

- **Support Eligibility:** Global Support Services (GSS) may request that any reported issue (performance, database latency, or stability) be reproduced on a supported vSphere environment before providing assistance.
- **Upgrade Risks:** Aria "Upgrade Paks" contain kernel updates and drivers specific to VMware virtual hardware. Applying these on Proxmox can lead to irreversible filesystem corruption or kernel panics.
- **Integration Failures:** The appliance relies on **VMware Tools** for lifecycle management, quiescent snapshots, and internal health monitoring. These features do not function correctly on non-VMware hypervisors.

For detailed system requirements and the latest interoperability data, please refer to the following official Broadcom documentation:

Yes

No
