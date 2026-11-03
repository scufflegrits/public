---
title: Proxmox VE - User Guide
url: https://helpcenter.veeam.com/docs/vbr/userguide/platform_support_proxmox.html
hostname: veeam.com
description: Proxmox VE Virtual InfrastructureVeeam Backup & Replication provides support for the following versions of the Proxmox VE platform. Specification Requirement Platform Proxmox Virtual Environment versions 8.2–9.2 installed using the official ISO image provided by Proxmox. Proxmox Virtual Environment must be installed on a machine with the x86-64 / amd64 CPU architecture. Machines with the ARM CPU architecture are not supported.
sitename: Veeam Help Center
date: "2026-10-30"
categories: ['Veeam Help Center']
fingerprint: "3ff73b5f45d025c3"
---
# Proxmox VE

Proxmox VE Virtual Infrastructure

Veeam Backup & Replication provides support for the following versions of the Proxmox VE platform.

| Proxmox VE Virtual Infrastructure |  | 
|---|---|
| Specification | Requirement | 
|---|---|
| Platform | Proxmox Virtual Environment versions 8.2–9.2 installed using the official ISO image provided by Proxmox. Proxmox Virtual Environment must be installed on a machine with the x86-64 / amd64 CPU architecture. Machines with the ARM CPU architecture are not supported. | 
| Hypervisor | KVM | 
| Management Server | n/a | 

Consider that at least one file-level storage configured in Proxmox Virtual Environment is required.

Proxmox VE VMs

| Proxmox VE VMs |  | 
|---|---|
| Specification | Requirement | 
|---|---|
| Hardware | All types and versions of virtual hardware are supported | 
| OS | All operating systems supported by Proxmox VE. Guest processing is supported for OS versions released before the Veeam Backup & Replication build release date. | 
| Software | QEMU Guest Agent (optional, required for application-aware processing) Compatibility with QEMU Guest Agent released after the Veeam Backup & Replication build release date cannot be guaranteed. | 

Guest OS File Restore

File-level restore is supported for the following file systems, including Microsoft Windows LDM dynamic disks and Linux LVM:

| Guest OS File Restore |  | 
|---|---|
| OS | Supported File Systems | 
|---|---|
| Microsoft Windows | Windows file-level restore to original location is supported for the following Microsoft Windows operating systems except Nano Server: | 
| Linux | DRBD (Distributed Replicated Block Devices) are not supported. | 
| BSD | UFS, UFS2 | 
| Mac | HFS, HFS+ (volumes up to 2 TB) | 
| Solaris |  | 

For other requirements and limitations of guest OS file restore, see Requirements and Limitations.

Version Compatibility

The following table lists compatible versions of Veeam Backup & Replication and Veeam Plug-in for Proxmox VE.

| Version Compatibility |  |  |  | 
|---|---|---|---|
| Plug-In Release | Plug-In Build | Veeam Backup & Replication Build | Worker OS Version | 
|---|---|---|---|
| 4 | 13.4.0.300 | 13.1.1.18 13.1.0.411 | Veeam JeOS 9.6 | 
| 3 | 13.3.2.9 13.3.0.237 | 13.0.2.29 13.0.1.2067 13.0.1.1071 13.0.1.180 | Veeam JeOS 9.2 | 
| 2 | 13.2.0.457 | 13.0.0.4967 | Rocky Linux 8.10 | 
| 1.5 | 12.1.5.17 | 12.3.2.3617 |  | 
| 1.3 | 12.1.3.217 | 12.3.2.3617 12.3.1.1139 12.3.0.310 |  | 
| 1.1 | 12.1.1.1024 | 12.3.0.310 12.2.0.334 |  | 

Related Topics
