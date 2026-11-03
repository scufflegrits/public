---
title: "CRITICAL ADVISORY: Pre-Upgrade Verification Required for vSphere Supervisor and VKS Environments Upgrading to vCenter 9.1.0 or 9.1.1"
author: Natalie Fisher
url: https://blogs.vmware.com/cloud-foundation/2026/10/09/critical-advisory-pre-upgrade-verification-required-for-vsphere-supervisor-and-vks-environments-upgrading-to-vcenter-9-1-0-or-9-1-1/
hostname: vmware.com
description: Overview and Call to Action While critical advisories are not typical blog topics, protecting customer environments and preventing unexpected data loss is our top priority. We are leveraging every communication channel available to ensure platform and infrastructure administrators are aware of a critical upgrade prerequisite. If you run vSphere Supervisor or VMware vSphere Kubernetes Service … Continued
sitename: VMware Cloud Foundation (VCF) Blog
date: "2026-10-09"
categories: ['Home Page']
fingerprint: f22fa8237bed4592
---
# Overview and Call to Action

While critical advisories are not typical blog topics, protecting customer environments and preventing unexpected data loss is our top priority. We are leveraging every communication channel available to ensure platform and infrastructure administrators are aware of a critical upgrade prerequisite.

If you run vSphere Supervisor or VMware vSphere Kubernetes Service (VKS) clusters and are planning an upgrade to vCenter Server 9.1.0 or 9.1.1, you must verify the vLCM/VUM database schema prior to initiating the upgrade.

Under specific conditions, upgrading without verifying and remediating database scheme inconsistencies caused by a vLCM/VUM reset **will result in Supervisor Control Plane Virtual Machines (VMs) and Foundation Load Balancers (FLBs) being removed and lost**.

# Environment and Applicability Matrix

Please review the following matrix to determine if your environment requires pre-upgrade verification:

| **Dimension** | **Details** | 
|---|---|
| **Target Versions** | vCenter Server / VMware Cloud Foundation (VCF) **9.1.0** and **9.1.1** | 
| **Source Versions** | vCenter Server **8.0 Update 3 (and later)**, **9.0.0**, **9.0.1**, and **9.0.2** | 
| **Impacted Solutions** | • vSphere Supervisor• vSphere Kubernetes Service (VKS)• Foundation Load Balancers (FLBs) | 
| **Trigger Condition** | The VMware Lifecycle Manager (vLCM / VUM) database depot was previously reset | 
| **Risk / Impact** | Loss of Supervisor Control Plane VMs and associated load balancer configurations upon completion of the 9.1.x upgrade. | 

# What Causes This Issue?

In earlier releases (vCenter 8.0 Update 3 through 9.0.x), administrators experiencing depot synchronization issues or patch repository corruption may have executed the standard vLCM database reset script documented in Broadcom KB 316581.

While this reset cleared depot corruption, running it on affected 8.0U3 or 9.0.x builds inadvertently caused database schema inconsistencies, specifically dropping required placement policy columns and relation tables.

When upgrading to vCenter 9.1.0 or 9.1.1, the new Lifecycle and Cluster Management (LCCM) subsystem relies on these database relations to discover and manage system VMs. Because of the missing schema definitions, LCCM operations cannot reconcile the Supervisor state, leading to the deletion of Supervisor Control Plane VMs and FLBs from inventory.

# What You Need to Do

To ensure a seamless upgrade and prevent disruption to your Kubernetes workloads:

## 1. Before Upgrading (Pre-Upgrade Check and Remediation)

Do not proceed with an upgrade to vCenter 9.1.0 or 9.1.1 until you have verified your database consistency.

Broadcom has published validation and remediation scripts to check for and fix this schema inconsistency before the upgrade is started.

Refer to **Broadcom KB 455737: Checking and Fixing VUMDB inconsistency issues after running vLCM reset script on 8.0U3 to 9.0.x** for the official database checker script, remediation script, and detailed execution instructions.

Note: Executing a health inspection using the **VCF Diagnostic Tool for vSphere (VDT)** will likewise identify this issue, returning a \[FAIL\] VUM SCHEMA CHECK status notification.

## 2. If You Have Already Upgraded and Encountered Missing Supervisor VMs

If an upgrade to 9.1.0 or 9.1.1 has already completed and your Supervisor Control Plane VMs are missing from inventory, immediate recovery requires reverting to your pre-upgrade backup/snapshot and restoring the Supervisor state before applying the database fix.

Refer to **Broadcom KB 457944: After upgrading to VCF 9.1 or VCF 9.1.1 from either 8.0U3 or 9.0.x, the Supervisor Control Plane VM’s are no longer in inventory** for the official recovery workflow.

# Official Reference Links

For the latest updates, validation utilities, and authoritative remediation steps, always refer directly to the official Broadcom Knowledge Base articles:

- **Broadcom KB 455737** — *Checking and Fixing VUMDB Inconsistency Issues After Running vLCM Reset Script (Authoritative Fix & Checker Scripts)*
- **Broadcom KB 457944** — *Supervisor Control Plane VMs No Longer in Inventory Post-Upgrade (Issue Overview & Recovery)*
- **Broadcom KB 316581** — *Reset VMware Lifecycle Manager Depot in vCenter Server Appliance*

# Summary

Before scheduling or initiating your next upgrade cycle to vCenter 9.1.x:

1. **Verify** your environment using the checker script in **KB 455737**.
2. **Remediate** if prompted by the script or VDT.
3. **Back up** your vCenter Server and Supervisor prior to performing any upgrade.

If you have questions or need assistance evaluating your environment, please open a support request through the **Broadcom Support Portal** referencing **KB 455737**.

### Discover more from VMware Cloud Foundation (VCF) Blog

Subscribe to get the latest posts sent to your email.
