---
title: VMware VKr Release Notes
author: CA Inc
url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-service-administration-and-development/9-1/release-notes/vmware-vkr-release-notes.html
hostname: broadcom.com
sitename: CA INC
date: "2026-10-23"
fingerprint: b7a37d4968e2e793
---
# VMware VKr Release Notes

This document contains the following sections

## Introduction

VMware vSphere Kubernetes releases | 22 October 2026

Check for additions and updates to these release notes.

## vSphere Kubernetes releases

VMware vSphere Kubernetes releases (VKrs) provide you with Kubernetes software distributions signed and supported by VMware for provisioning vSphere Kubernetes Service (VKS) clusters in the vSphere Supervisor environment. VMware VKrs follow the upstream Kubernetes versioning.

## Content Library

The availability of VKrs depends on the vCenter content library and its synchronization frequency. Use the command kubectl get kr to list the VKr that are available in your environment. If a release is not synchronized with your library, that release will not appear in the list returned by the command. Refer to the *Managing vSphere Kubernetes Service with vSphere Supervisor* documentation for more information.

## About vSphere Kubernetes releases

Historically, vSphere Kubernetes releases (VKr), formerly known as Tanzu Kubernetes releases (TKrs) have been distributed in two distinct formats: **legacy** and **non-legacy**. Each format was designed for compatibility with specific vSphere versions and was clearly labeled to communicate its intended environment and upgrade path.

- 
  - Utilized an older format compatible with vSphere 7.x.
  - Also supported on vSphere 8.x, but strictly for upgrade purposes.
  - Identified by the legacy-tkr annotation label.
  - Labeled as “for vSphere 7.x” in release notes and documentation.
- 
  - Introduced with vSphere 8.x, these TKrs support new features and enhanced compatibility.
  - Exclusively compatible with vSphere 8.x.
  - Labeled as “for vSphere 8.x” in release notes and documentation.

**Previous Release Designations**

Until recently, TKr releases included explicit version designations in their naming conventions and documentation, such as:

- TKr v1.28.8 for vSphere 8.x (non-legacy)
- TKr v1.28.7 for vSphere 7.x (legacy)

This approach provided clear guidance on which TKr should be used for a given vSphere version and ensured smooth upgrade paths.

**Change in Versioning and Compatibility (Effective VKr 1.29)**

Effective with VKr 1.29, the explicit “for vSphere m.n” designation will be discontinued, since the legacy TKrs are no longer supported. A single VKr release (non-legacy) will now operate across both vSphere 8.x and 9.x platforms.

## Compatibility and Upgrades

The VKrs for vSphere 8.x are updated to a package-based framework. While you can run vSphere 7.x VKrs on vSphere 8.x, you cannot take advantage of vSphere 8.x features unless you upgrade the cluster to use a VKr for vSphere 8.x.

Use the command kubectl get kr to verify compatibility of VKrs with the vSphere Kubernetes Service. See also the *Compatibility Matrix* section. Upgrading VKS clusters to a VKr for vSphere 8.x is allowed starting with the vSphere 8.0a release. You must update existing VKS clusters to a minimum VKr v1.21.x or later before upgrading your environment to vSphere 8.0a. After you have upgraded to vSphere 8.0a, update clusters to a VKr for vSphere 8.x format to take advantage of new features. See the *Updating vSphere Supervisor* documentation for details.

Upgrading is only supported when the origin and target VKrs are the same operating system. For example, you cannot upgrade from a Photon OS VKr to an Ubuntu VKr.

## Components and Packages

Use the command kubectl get kr VKR\_NAME -o yaml to list components and packages. The VKr format that supports provisioning VKS clusters on vSphere 8.x uses a package-based framework to deliver VMware software and Kubernetes components.

## CRITICAL REQUIREMENT for vSphere 8.0.0 Customers

If you have deployed vSphere Supervisor 8.0.0 GA, be aware of the following CRITICAL REQUIRMENT.

Before upgrading to vSphere 8 U1 you must create a temporary VKr content library to avoid a known issue that causes VKS Controller pods to go into CrashLoopBackoff when VKrs are pushed to the existing content library. To avoid this issue, complete the following steps.

**NOTE**: This requirement does not apply to content libraries you use for VMs provisioned through VM Service.

1. Synchronize all the items in the temporary content library.
2. Associate the temporary content library with the VKS.
3. Run the commandkubectl get tkrand verify that all the VKrs are created.
4. At this point the VKS Controller should be in a running state, which you can verify by listing the pods in the vSphere Namespace.
5. If the VKS Controller is in CrashLoopBackOff (CLBO) state, restart the VKS Controller deployment using the following command:kubectl rollout restart deployment -n vmware-system-tkg vmware-system-tkg-controller-manager
6. Upgrade to vSphere 8 U1.
7. Update the VKS configuration to use the original subscribed content library at https://wp-content.vmware.com/v2/latest/lib.json. NOTE: The content library is not namespace-scoped, so when you update one VKS configuration, the change should be propagated to all others. You should verify this by checking each vSphere Namespace.

## VKr v1.37.1

## What's New

- 

## Components

vSphere Kubernetes release 1.37.1 for use with vSphere 9.x and vSphere 8.x includes the following OS & Kubernetes components.

This release ships with the following operating system options

Operating System & Version

Kernel Version

🆕 Photon OS 5.0 (Immutable)

6.12.111-3.ph5

Photon 5.0

6.12.111-3.ph5

Ubuntu 22.04 LTS

5.15.0-198-generic

Ubuntu 24.04 LTS

7.0.0-38-generic

VKr 1.37.1 for use with vSphere 9.x and vSphere 8.x includes the following VMware packages.

**Component**

**Version**

kubernetes

1.37.1

coredns

1.14.7

etcd

3.7.2

containerd

2.4.0

Package

Version

antrea

2.7.0

calico

3.32.2

guest-cluster-auth-service

1.5.0

kapp-controller

0.60.9

metrics-server

0.9.0

pinniped

0.47.0

secretgen-controller

0.21.2

vsphere-cpi

1.37.0

vsphere-pv-csi

3.9.0

gateway-api

1.6.1

## Fixed Issues

**After upgrade to 1.36.1, application pods will be stuck in ContainerCreating state with FailedAttachVolume warning**

If a pod is stuck in ContainerCreating state, execute the following command -

kubectl get pods -A | grep ContainerCreating"

Describe the pod, and if you find the following warning pattern, execute the workaround

Warning FailedAttachVolume

2m9s (x59 over 104m) attachdetach-controller AttachVolume.Attach failed for volume "pvc-1f46ebd4-2606-4800-aa70-af8bdb75fdb8" : CSINode vks361-ph-336-calico-11ns5-c5-np1-worker-rf5zx-ttrqp-6qc7j does not contain driver csi.vsphere.vmware.com

This issues is fixed in 1.37.1

## Known Issues

**After worker node scale-up and scale-down operation on large VKS cluster with 3CP/150W, with auto-scaler enabled, many pods can go into OutOfPods/Pending state.**

This is caused due to a race condition in a scenario where auto-scaler is increasing the number of nodes, while there are a larger number of pods waiting to be scheduled. And scheduler assigns the pods to the first few nodes available.

**Workaround:**

Delete the pods marked with the error "OutOfPods".

**After VKS cluster upgrade a failed Antrea upgrade job remains in the cluster**

Sometimes, when the upgrades take longer you will notice an Antrea upgrade jobs in error state. These errors do not impact the functionality of the Antrea. These are transient errors that occur while the cluster is upgrading.

**Workaround**:

You can use the kubectl delete to clean up the failed jobs.

## VKr v1.36.4

## What's New

- Security Patches and Bug Fixes

## Components

vSphere Kubernetes release 1.36.4 for use with vSphere 9.x and vSphere 8.x includes the following OS & Kubernetes components.

This release ships with the following operating system options

Operating System & Version

Kernel Version

Photon 5.0

6.1.183-2.ph5

Ubuntu 22.04 LTS

5.15.0-194-generic

Ubuntu 24.04 LTS

7.0.0-34-generic

VKr 1.36.4 for use with vSphere 9.x and vSphere 8.x includes the following VMware packages.

**Component**

**Version**

kubernetes

1.36.4

coredns

1.14.7

etcd

3.6.14

containerd

2.3.4

Package

Version

antrea

2.6.3

calico

3.31.5

guest-cluster-auth-service

1.4.8

kapp-controller

0.60.9

metrics-server

0.8.1

pinniped

0.47.0

secretgen-controller

0.21.1

vsphere-cpi

1.36.0

vsphere-pv-csi

3.8.0

gateway-api

1.5.1

## Fixed Issues

**After upgrade to 1.36.1, application pods will be stuck in ContainerCreating state with FailedAttachVolume warning**

If a pod is stuck in ContainerCreating state, execute the following command -

kubectl get pods -A | grep ContainerCreating"

Describe the pod, and if you find the following warning pattern, execute the workaround

Warning FailedAttachVolume

2m9s (x59 over 104m) attachdetach-controller AttachVolume.Attach failed for volume "pvc-1f46ebd4-2606-4800-aa70-af8bdb75fdb8" : CSINode vks361-ph-336-calico-11ns5-c5-np1-worker-rf5zx-ttrqp-6qc7j does not contain driver csi.vsphere.vmware.com

**This issue is fixed in 1.36.4**

## Known Issues

**After worker node scale-up and scale-down operation on large VKS cluster with 3CP/150W, with auto-scaler enabled, many pods can go into OutOfPods/Pending state.**

This is caused due to a race condition in a scenario where auto-scaler is increasing the number of nodes, while there are a larger number of pods waiting to be scheduled. And scheduler assigns the pods to the first few nodes available.

**Workaround:**

Delete the pods marked with the error "OutOfPods".

**After VKS cluster upgrade a failed Antrea upgrade job remains in the cluster**

Sometimes, when the upgrades take longer you will notice an Antrea upgrade jobs in error state. These errors do not impact the functionality of the Antrea. These are transient errors that occur while the cluster is upgrading.

**Workaround**:

You can use the kubectl delete to clean up the failed jobs.

## VKr v1.35.8

## Release Snapshot

## What's New

- Bug fixes and security patches

## Components

vSphere Kubernetes release 1.35.6 for use with vSphere 9.x and vSphere 8.x includes the following OS & Kubernetes components.

This release ships with the following operating system options

**Operating System & Version**

**Kernel Version**

Photon 5.0

6.1.183-2.ph5

Ubuntu 22.04 LTS

5.15.0-194-generic

Ubuntu 24.04 LTS

7.0.0-34-generic

VKr 1.35.8 for use with vSphere 9.0 and vSphere 8.x includes the following VMware packages.

**Component**

**Version**

kubernetes

1.35.8

coredns

1.13.1

etcd

3.5.33

containerd

2.2.7

Package

Version

antrea

2.5.3

calico

3.30.6

guest-cluster-auth-service

1.4.8

kapp-controller

0.60.9

metrics-server

0.8.1

pinniped

0.47.0

secretgen-controller

0.21.1

vsphere-cpi

1.35.1

vsphere-pv-csi

3.7.0

gateway-api

1.4.0

## Fixed Issues

**After upgrade, application pods will be stuck in ContainerCreating state with FailedAttachVolume warning**

If a pod is stuck in ContainerCreating state, execute the following command -

kubectl get pods -A | grep ContainerCreating"

Describe the pod, and if you find the following warning pattern, execute the workaround

Warning FailedAttachVolume

2m9s (x59 over 104m) attachdetach-controller AttachVolume.Attach failed for volume "pvc-1f46ebd4-2606-4800-aa70-af8bdb75fdb8" : CSINode vks361-ph-336-calico-11ns5-c5-np1-worker-rf5zx-ttrqp-6qc7j does not contain driver csi.vsphere.vmware.com

This issue is fixed in 1.35.8

## Known Issues

**After worker node scale-up and scale-down operation on large VKS cluster with 3CP/150W, with auto-scaler enabled, many pods can go into OutOfPods/Pending state.**

This is caused due to a race condition in a scenario where auto-scaler is increasing the number of nodes, while there are a larger number of pods waiting to be scheduled. And scheduler assigns the pods to the first few nodes available.

**Workaround:**

Delete the pods marked with the error "OutOfPods".

**Autoscaler is unable to scale up windows nodes in a cluster containing multiple node pools with mixed OS types.**

In autoscaler-based guest clusters having hybrid node pools with different OS (Photon, Ubuntu, Windows), when scaling up applications on the clusters, Windows nodes are not scaled up even though Windows pods are in a pending state.

Workloads are stuck in a pending state and new nodes will not be deployed. The autoscaler pod logs show the error can't schedule pod : predicate "NodeAffinity" didn't pass (predicateReasons=\[node(s) didn't match Pod's node affinity/selector\];

**Workaround:**

When the cluster contains multiple node pools, the autoscaler will try to automatically scale up the node to handle pending pods. When the pod contains nodeSelector, the autoscaler will simulate the node to be created based on the annotation of the current node pool to evaluate whether it meets the needs of the current pod. Windows pods need nodeSelector to schedule to Windows nodes, so this problem will be encountered.

Add the annotation(capacity.cluster-autoscaler.kubernetes.io/labels: "key1=value1,key2=value2") in machine deployment for windows to inform the autoscaler that this node pool can create nodes with this label.

**After VKS cluster upgrade a failed Antrea upgrade job remains in the cluster**

Sometimes, when the upgrades take longer you will notice an Antrea upgrade jobs in error state. These errors do not impact the functionality of the Antrea. These are transient errors that occur while the cluster is upgrading.

**Workaround**:

You can use the kubectl delete to clean up the failed jobs.

## VKr v1.34.11

## Release Snapshot

## What's New

- Security Patches and Bug Fixes

## Components

vSphere Kubernetes release 1.34.9 for use with vSphere 9.x and vSphere 8.x includes the following OS & Kubernetes components.

This release ships with the following operating system options

Operating System & Version

Kernel Version

Photon 5.0

6.1.183-2.ph5

Ubuntu 22.04 LTS

5.15.0-194-generic

Ubuntu 24.04 LTS

7.0.0-34-generic

VKr 1.34.11 for use with vSphere 9.x and vSphere 8.x includes the following VMware packages.

Component

Version

kubernetes

1.34.11

coredns

1.12.1

etcd

3.5.33

containerd

2.1.9

Package

Version

antrea

2.4.5

calico

3.30.6

guest-cluster-auth-service

1.4.8

kapp-controller

0.60.9

metrics-server

0.8.1

pinniped

0.47.0

secretgen-controller

0.21.1

vsphere-cpi

1.34.0

vsphere-pv-csi

3.6.0

gateway-api

1.3.0

## Known Issues

No new known issues

## VKr v1.36.2

## What's New

- Security Patches and Bug Fixes

## Components

vSphere Kubernetes release 1.36.2 for use with vSphere 9.x and vSphere 8.x includes the following OS & Kubernetes components.

This release ships with the following operating system options

Operating System & Version

Kernel Version

Photon 5.0

6.1.176-4.ph5

Ubuntu 22.04 LTS

5.15.0-185-generic

Ubuntu 24.04 LTS

6.17.0-35-generic

VKr 1.36.2 for use with vSphere 9.x and vSphere 8.x includes the following VMware packages.

**Component**

**Version**

kubernetes

1.36.2

coredns

1.14.3

etcd

3.6.12

containerd

2.3.2

Package

Version

antrea

2.6.2

calico

3.31.5

guest-cluster-auth-service

1.4.8

kapp-controller

0.60.4

metrics-server

0.8.1

pinniped

0.46.0

secretgen-controller

0.21.1

vsphere-cpi

1.36.0

vsphere-pv-csi

3.8.0

gateway-api

1.5.1

## Fixed Issues

**Packages are in 'Reconcile failed' state after upgrade due to caBundle certificate mismatch**

After the cluster upgrades to this version, you may sometimes see that the packages are in 'Reconcile Failed' state. Due to this the upgrade is flagged as failed. This may happen because the kapp-controller from the old cluster still exists due to a possible race condition during the upgrade. Both the old and the new kapp-controller attempt to update the api service with their CA bundle causing this issue.

**Solution:**

This issue has been addressed in this release.

## Known Issues

**After upgrade to 1.36.1, application pods will be stuck in ContainerCreating state with FailedAttachVolume warning**

If a pod is stuck in ContainerCreating state, execute the following command -

kubectl get pods -A | grep ContainerCreating"

Describe the pod, and if you find the following warning pattern, execute the workaround

Warning FailedAttachVolume

2m9s (x59 over 104m) attachdetach-controller AttachVolume.Attach failed for volume "pvc-1f46ebd4-2606-4800-aa70-af8bdb75fdb8" : CSINode vks361-ph-336-calico-11ns5-c5-np1-worker-rf5zx-ttrqp-6qc7j does not contain driver csi.vsphere.vmware.com

**Workaround:**

restart the csi-node pods

kubectl delete pod vsphere-csi-node-\<xyz> -n vmware-system-csi

**After worker node scale-up and scale-down operation on large VKS cluster with 3CP/150W, with auto-scaler enabled, many pods can go into OutOfPods/Pending state.**

This is caused due to a race condition in a scenario where auto-scaler is increasing the number of nodes, while there are a larger number of pods waiting to be scheduled. And scheduler assigns the pods to the first few nodes available.

**Workaround:**

Delete the pods marked with the error "OutOfPods".

**After VKS cluster upgrade a failed Antrea upgrade job remains in the cluster**

Sometimes, when the upgrades take longer you will notice an Antrea upgrade jobs in error state. These errors do not impact the functionality of the Antrea. These are transient errors that occur while the cluster is upgrading.

**Workaround**:

You can use the kubectl delete to clean up the failed jobs.

## VKr v1.35.6

## Release Snapshot

## What's New

- Bug fixes and security patches

## Components

vSphere Kubernetes release 1.35.6 for use with vSphere 9.x and vSphere 8.x includes the following OS & Kubernetes components.

This release ships with the following operating system options

**Operating System & Version**

**Kernel Version**

Photon 5.0

6.1.176-4.ph5

Ubuntu 22.04 LTS

5.15.0-185-generic

Ubuntu 24.04 LTS

6.17.0-35-generic

VKr 1.35.6 for use with vSphere 9.0 and vSphere 8.x includes the following VMware packages.

**Component**

**Version**

kubernetes

1.35.6

coredns

1.13.1

etcd

3.5.31

containerd

2.2.5

Package

Version

antrea

2.5.2

calico

3.30.6

guest-cluster-auth-service

1.4.8

kapp-controller

0.60.4

metrics-server

0.8.1

pinniped

0.46.0

secretgen-controller

0.21.1

vsphere-cpi

1.35.1

vsphere-pv-csi

3.7.0

gateway-api

1.4.0

## Fixed Issues

After an ESX reboot, time drift could cause some of the VKS nodes to be in NotReady state

**Description:**

Following an ESX host reboot, VKS nodes scheduled on the rebooted host, may experience clock drift. While VKr relies on the **chrony** service to synchronize time with an NTP server, a race condition can occur: if the **kubelet** initializes before **chrony** finishes correcting the time, the **kubelet** will generate service tokens with past timestamps, rendering them invalid.

**Solution:**

This issue has been addressed in this release.

**Packages are in 'Reconcile failed' state after upgrade due to caBundle certificate mismatch**

After the cluster upgrades to this version, you may sometimes see that the packages are in 'Reconcile Failed' state. Due to this the upgrade is flagged as failed. This may happen because the kapp-controller from the old cluster still exists due to a possible race condition during the upgrade. Both the old and the new kapp-controller attempt to update the api service with their CA bundle causing this issue.

**Solution:**

This issue has been addressed in this release.

## Known Issues

**After upgrade, application pods will be stuck in ContainerCreating state with FailedAttachVolume warning**

If a pod is stuck in ContainerCreating state, execute the following command -

kubectl get pods -A | grep ContainerCreating"

Describe the pod, and if you find the following warning pattern, execute the workaround

Warning FailedAttachVolume

2m9s (x59 over 104m) attachdetach-controller AttachVolume.Attach failed for volume "pvc-1f46ebd4-2606-4800-aa70-af8bdb75fdb8" : CSINode vks361-ph-336-calico-11ns5-c5-np1-worker-rf5zx-ttrqp-6qc7j does not contain driver csi.vsphere.vmware.com

**Workaround:**

restart the csi-node pods

kubectl delete pod vsphere-csi-node-\<xyz> -n vmware-system-csi

**After worker node scale-up and scale-down operation on large VKS cluster with 3CP/150W, with auto-scaler enabled, many pods can go into OutOfPods/Pending state.**

This is caused due to a race condition in a scenario where auto-scaler is increasing the number of nodes, while there are a larger number of pods waiting to be scheduled. And scheduler assigns the pods to the first few nodes available.

**Workaround:**

Delete the pods marked with the error "OutOfPods".

**Autoscaler is unable to scale up windows nodes in a cluster containing multiple node pools with mixed OS types.**

In autoscaler-based guest clusters having hybrid node pools with different OS (Photon, Ubuntu, Windows), when scaling up applications on the clusters, Windows nodes are not scaled up even though Windows pods are in a pending state.

Workloads are stuck in a pending state and new nodes will not be deployed. The autoscaler pod logs show the error can't schedule pod : predicate "NodeAffinity" didn't pass (predicateReasons=\[node(s) didn't match Pod's node affinity/selector\];

**Workaround:**

When the cluster contains multiple node pools, the autoscaler will try to automatically scale up the node to handle pending pods. When the pod contains nodeSelector, the autoscaler will simulate the node to be created based on the annotation of the current node pool to evaluate whether it meets the needs of the current pod. Windows pods need nodeSelector to schedule to Windows nodes, so this problem will be encountered.

Add the annotation(capacity.cluster-autoscaler.kubernetes.io/labels: "key1=value1,key2=value2") in machine deployment for windows to inform the autoscaler that this node pool can create nodes with this label.

**After VKS cluster upgrade a failed Antrea upgrade job remains in the cluster**

Sometimes, when the upgrades take longer you will notice an Antrea upgrade jobs in error state. These errors do not impact the functionality of the Antrea. These are transient errors that occur while the cluster is upgrading.

**Workaround**:

You can use the kubectl delete to clean up the failed jobs.

## VKr v1.34.9

## Release Snapshot

## What's New

- Security Patches and Bug Fixes

## Components

vSphere Kubernetes release 1.34.9 for use with vSphere 9.x and vSphere 8.x includes the following OS & Kubernetes components.

This release ships with the following operating system options

Operating System & Version

Kernel Version

Photon 5.0

6.1.176-4.ph5

Ubuntu 22.04 LTS

5.15.0-185-generic

Ubuntu 24.04 LTS

6.8.0-124-generic

VKr 1.34.9 for use with vSphere 9.x and vSphere 8.x includes the following VMware packages.

Component

Version

kubernetes

1.34.9

coredns

1.12.1

etcd

3.5.31

containerd

2.1.9

Package

Version

antrea

2.4.5

calico

3.30.6

guest-cluster-auth-service

1.4.8

kapp-controller

0.60.4

metrics-server

0.8.1

pinniped

0.46.0

secretgen-controller

0.21.1

vsphere-cpi

1.34.0

vsphere-pv-csi

3.6.0

gateway-api

1.3.0

## Fixed Issues

## Known Issues

No new known issues

## VKr v1.33.13

## Release Snapshot

## What's New

- Security Patches & Bug Fixes

## Components

vSphere Kubernetes release 1.33.13 for use with vSphere 9.x and vSphere 8.x includes the following Kubernetes components.

This release ships with the following operating system options

Operating System & Version

Kernel Version

Photon 5.0

6.1.176-4.ph5

Ubuntu 22.04 LTS

5.15.0-186-generic

Ubuntu 24.04 LTS

6.8.0-136-generic

Component

Version

kubernetes

1.33.13

coredns

1.12.0

etcd

3.5.31

containerd

2.0.10

VKr 1.33.13 for use with vSphere 9.x and vSphere 8.x includes the following VMware packages.

Package

Version

antrea

2.3.2

calico

3.30.6

guest-cluster-auth-service

1.4.8

kapp-controller

0.60.4

metrics-server

0.8.1

pinniped

0.46.0

secretgen-controller

0.21.1

vsphere-cpi

1.33.0

vsphere-pv-csi

3.5.0

gateway-api

1.21

## Known Issues

## Fixed Issues

**Packages are in 'Reconcile failed' state after upgrade due to caBundle certificate mismatch**

After the cluster upgrades to 1.33.3, you may sometimes see that the packages are in 'Reconcile Failed' state. Because of this the upgrade is flagged as failed. This may happen because the kapp-controller from the old cluster still exists due to a possible race condition during the upgrade. Both the old and the new kapp-controller attempts to update the api service with thier CA bundle causing this issue.

**Solution:**

This issue has been addressed in this release.

## VKr v1.36.1

## What's New

**Pre-requisites for VKr 1.36 upgrade**

- Existing VKS clusters will need to rebase to builtin-generic-v3.7.0 as a part of, or prior to, any upgrade to Kubernetes v1.36 or later.

**Support for Kubernetes version 1.36.1**

- Support for Kubernetes 1.36 minor version along with updates to all of the components to support 1.36. With this release of VKr, theetcdversion has been upgraded to 3.6 minor version andcontainerdversion is updated from 2.2 to 2.3.

**Ubuntu VKr node updates** 

- - Disabled loading of unused graphics drivers like bochs, vmwgfx, virtual graphics drivers and VESA Framebuffer.

**Photon VKr node updates** 

- New opt-in ClusterClass variable “osConfiguration.immutability.usrPartitionMode” on the “builtin-generic-v3.7.0”ClusterClass. When set to ReadOnly, the/usrpartition is mounted read-only for the node's lifetime, providing defense-in-depth against DaemonSet tampering. Please refer to the VKS release notes.

**Deprecation Announcements (Upstream Kubernetes Project)**

- - Also, starting with VKr 1.36.1, theContainerduses config version 3. Any custom monitoring tools or operators that are dependent oncontainerdconfiguration version other than 3, must use version 3.

## Components

vSphere Kubernetes release 1.36.1 for use with vSphere 9.0 and vSphere 8.x includes the following OS & Kubernetes components.

This release ships with the following operating system options

Operating System & Version

Kernel Version

Photon 5.0

6.1.170-1.ph5

Ubuntu 22.04 LTS

5.15.0-181.191

Ubuntu 24.04 LTS

6.17.0-35.35\~24.04.1

VKr 1.36.1 for use with vSphere 9.0 and vSphere 8.x includes the following VMware packages.

**Component**

**Version**

kubernetes

1.36.1

coredns

1.14.3

etcd

3.6.11

containerd

2.3.1

cni-plugins

1.8.0

Package

Version

antrea

2.6.1

calico

3.31.5

guest-cluster-auth-service

1.4.7

kapp-controller

0.59.8

metrics-server

0.8.1

pinniped

0.46.0

secretgen-controller

0.20.1

vsphere-cpi

1.36.1

vsphere-pv-csi

3.8.0

gateway-api

1.5.1

## Fixed Issues

After an ESX reboot, time drift could cause some of the VKS nodes to be in NotReady state

Following an ESX host reboot, VKS nodes scheduled on the rebooted host, may experience clock drift. While VKr relies on the **chrony** service to synchronize time with an NTP server, a race condition can occur: if the **kubelet** initializes before **chrony** finishes correcting the time, the **kubelet** will generate service tokens with past timestamps, rendering them invalid.

This issue has been fixed in 1.36.1

## Known Issues

**After upgrade to 1.36.1, application pods will be stuck in ContainerCreating state with FailedAttachVolume warning**

If a pod is stuck in ContainerCreating state, execute the following command -

kubectl get pods -A | grep ContainerCreating"

Describe the pod, and if you find the following warning pattern, execute the workaround

Warning FailedAttachVolume

2m9s (x59 over 104m) attachdetach-controller AttachVolume.Attach failed for volume "pvc-1f46ebd4-2606-4800-aa70-af8bdb75fdb8" : CSINode vks361-ph-336-calico-11ns5-c5-np1-worker-rf5zx-ttrqp-6qc7j does not contain driver csi.vsphere.vmware.com

**Workaround:**

restart the csi-node pods

kubectl delete pod vsphere-csi-node-\<xyz> -n vmware-system-csi

**After worker node scale-up and scale-down operation on large VKS cluster with 3CP/150W, with auto-scaler enabled, many pods can go into OutOfPods/Pending state.**

This is caused due to a race condition in a scenario where auto-scaler is increasing the number of nodes, while there are a larger number of pods waiting to be scheduled. And scheduler assigns the pods to the first few nodes available.

**Workaround:**

Delete the pods marked with the error "OutOfPods".

**After VKS cluster upgrade a failed Antrea upgrade job remains in the cluster**

Sometimes, when the upgrades take longer you will notice an Antrea upgrade jobs in error state. These errors do not impact the functionality of the Antrea. These are transient errors that occur while the cluster is upgrading.

**Workaround**:

You can use the kubectl delete to clean up the failed jobs.

**Packages are in 'Reconcile failed' state after upgrade due to caBundle certificate mismatch**

After the cluster upgrades to this version, you may sometimes see that the packages are in 'Reconcile Failed' state. Due to this the upgrade is flagged as failed. This may happen because the kapp-controller from the old cluster still exists due to a possible race condition during the upgrade. Both the old and the new kapp-controller attempt to update the api service with their CA bundle causing this issue.

**Workaround:**

Try restarting the kapp-controller pod in the cluster, the correct CABundle content gets synced to the api-service and all packages get reconciled.

If the above workaround doesn't work, edit the CA bundle of the api service manually with the content of upgraded kapp-controller self signed cert.

## VKr v1.35.5

## Release Snapshot

Name

Release Date

vCenter

VKS

**v1.35.5+vmware.1-vkr.1**

28-May-2026

vCenter 9.0.0.0 or higher

vCenter 8.0 Update 3g or higher

## What's New

- Bug fixes and security patches

## Components

vSphere Kubernetes release 1.35.5 for use with vSphere 9.0 and vSphere 8.x includes the following OS & Kubernetes components.

This release ships with the following operating system options

Operating System & Version

Kernel Version

Photon 5.0

6.1.170-1.ph5

Ubuntu 22.04 LTS

5.15.0.179.163 (generic)

Ubuntu 24.04 LTS

6.17.0-29.29\~24.04.1 (hwe)

VKr 1.35.5 for use with vSphere 9.0 and vSphere 8.x includes the following VMware packages.

**Component**

**Version**

kubernetes

1.35.5

coredns

1.13.1

etcd

3.5.30

containerd

2.2.3

cni-plugins

1.8.0

Package

Version

antrea

2.5.1

calico

3.30.6

guest-cluster-auth-service

1.4.6

kapp-controller

0.59.1

metrics-server

0.8.1

pinniped

0.42.0

secretgen-controller

0.20.1

vsphere-cpi

1.35.1

vsphere-pv-csi

3.7.0

gateway-api

1.4.0

## Fixed Issues

**VKS Clusters fail to deploy with error "rpc not supported for learner"**

When a new control plane node joins an etcd cluster, it first enters a "learner" state where it syncs data but cannot vote. At times, control plane node may become stuck in the “Provisioning” phase, preventing the cluster from completing. The node successfully registers with etcd as a "learner" (a read-only replica) but is never promoted to a full voting member, leaving the cluster unable to progress without manual intervention.

**This issue has been fixed in VKr 1.35.5**

**Ubuntu 24.04 Nodes unexpectedly transition to the NotReady state caused by a kernel panic**

Workloads that trigger a specific kernel path are known to cause Ubuntu 24.04 nodes to unexpectedly transition to the **NotReady** state triggering the restart of all residing Pods and consequently causing application outages on the affected Node. VKr 1.35.5 upgraded the kernel version to address this issue.

## Known Issues

After an ESX reboot, time drift could cause some of the VKS nodes to be in NotReady state

Following an ESX host reboot, VKS nodes scheduled on the rebooted host, may experience clock drift. While VKr relies on the **chrony** service to synchronize time with an NTP server, a race condition can occur: if the **kubelet** initializes before **chrony** finishes correcting the time, the **kubelet** will generate service tokens with past timestamps, rendering them invalid.

**Workaround:**

Deleting the problematic node, the node will be recreated with correct time and the pods will be scheduled and running.

**After upgrade, application pods will be stuck in ContainerCreating state with FailedAttachVolume warning**

If a pod is stuck in ContainerCreating state, execute the following command -

kubectl get pods -A | grep ContainerCreating"

Describe the pod, and if you find the following warning pattern, execute the workaround

Warning FailedAttachVolume

2m9s (x59 over 104m) attachdetach-controller AttachVolume.Attach failed for volume "pvc-1f46ebd4-2606-4800-aa70-af8bdb75fdb8" : CSINode vks361-ph-336-calico-11ns5-c5-np1-worker-rf5zx-ttrqp-6qc7j does not contain driver csi.vsphere.vmware.com

**Workaround:**

restart the csi-node pods

kubectl delete pod vsphere-csi-node-\<xyz> -n vmware-system-csi

**After worker node scale-up and scale-down operation on large VKS cluster with 3CP/150W, with auto-scaler enabled, many pods can go into OutOfPods/Pending state.**

This is caused due to a race condition in a scenario where auto-scaler is increasing the number of nodes, while there are a larger number of pods waiting to be scheduled. And scheduler assigns the pods to the first few nodes available.

**Workaround:**

Delete the pods marked with the error "OutOfPods".

**Autoscaler is unable to scale up windows nodes in a cluster containing multiple node pools with mixed OS types.**

In autoscaler-based guest clusters having hybrid node pools with different OS (Photon, Ubuntu, Windows), when scaling up applications on the clusters, Windows nodes are not scaled up even though Windows pods are in a pending state.

Workloads are stuck in a pending state and new nodes will not be deployed. The autoscaler pod logs show the error can't schedule pod : predicate "NodeAffinity" didn't pass (predicateReasons=\[node(s) didn't match Pod's node affinity/selector\];

**Workaround:**

When the cluster contains multiple node pools, the autoscaler will try to automatically scale up the node to handle pending pods. When the pod contains nodeSelector, the autoscaler will simulate the node to be created based on the annotation of the current node pool to evaluate whether it meets the needs of the current pod. Windows pods need nodeSelector to schedule to Windows nodes, so this problem will be encountered.

Add the annotation (capacity.cluster-autoscaler.kubernetes.io/labels: "key1=value1,key2=value2") in machine deployment for windows to inform the autoscaler that this node pool can create nodes with this label.

**After VKS cluster upgrade a failed Antrea upgrade job remains in the cluster**

Sometimes, when the upgrades take longer you will notice an Antrea upgrade jobs in error state. These errors do not impact the functionality of the Antrea. These are transient errors that occur while the cluster is upgrading.

**Workaround**:

You can use the kubectl delete to clean up the failed jobs.

**Packages are in 'Reconcile failed' state after upgrade due to caBundle certificate mismatch**

After the cluster upgrades to this version, you may sometimes see that the packages are in 'Reconcile Failed' state. Due to this the upgrade is flagged as failed. This may happen because the kapp-controller from the old cluster still exists due to a possible race condition during the upgrade. Both the old and the new kapp-controller attempt to update the api service with their CA bundle causing this issue.

**Workaround:**

Try restarting the kapp-controller pod in the cluster, the correct CABundle content gets synced to the api-service and all packages get reconciled.

If the above workaround doesn't work, edit the CA bundle of the api service manually with the content of upgraded kapp-controller self signed cert.

## VKr v1.34.8

## Release Snapshot

Name

Release Date

vCenter

VKS

v1.34.8+vmware.1-vkr.1

28-May-2026

vCenter 9.0.0.0 or higher

vCenter 8.0 Update 3g or higher

## What's New

- Security Patches and Bug Fixes

## Components

vSphere Kubernetes release 1.34.8 for use with vSphere 9.0 and vSphere 8.x includes the following OS & Kubernetes components.

This release ships with the following operating system options

Operating System & Version

Kernel Version

Photon 5.0

6.1.170-1.ph5

Ubuntu 22.04 LTS

5.15.0.179.163 (generic)

Ubuntu 24.04 LTS

6.8.0-117.117 (generic)

VKr 1.34.8 for use with vSphere 9.0 and vSphere 8.x includes the following VMware packages.

Component

Version

kubernetes

1.34.8

coredns

1.12.1

etcd

3.5.30

containerd

2.1.7

cni-plugins

1.7.1

Package

Version

antrea

2.4.4

calico

3.30.6

guest-cluster-auth-service

1.4.6

kapp-controller

0.59.1

metrics-server

0.8.0

pinniped

0.41.0

secretgen-controller

0.19.2

vsphere-cpi

1.34.0

vsphere-pv-csi

3.6.0

gateway-api

1.3.0

## Fixed Issues

**CSI driver should return non-final errors to fix the orphaned volumes and snapshots problem**

This issue has been fixed in 1.34.8

**Antrea Egress Traffic is broken on Ubuntu22 node post VM Class update**

This issue has been fixed in VKr 1.34.8

**VKS Clusters fail to deploy with error "rpc not supported for learner"**

When a new control plane node joins an etcd cluster, it first enters a "learner" state where it syncs data but cannot vote. At times, control plane node may become stuck in the “Provisioning” phase, preventing the cluster from completing. The node successfully registers with etcd as a "learner" (a read-only replica) but is never promoted to a full voting member, leaving the cluster unable to progress without manual intervention.

**This issue has been fixed in VKr 1.35.5**

## Known Issues

No new known issues

## VKr v1.35.2

## Release Snapshot

Name

Release Date

vCenter

VKS

v1.35.2+vmware.1-vkr.3

13-April-2026

vCenter 9.0.0.0 or higher

vCenter 8.0 Update 3g or higher

## What's New

- Bug fixes and security patches

**Upgrade instructions**

With the release of VKr 1.35.2, version 1.35.0 will be deactivated and no longer available for new cluster creation.

- - 

If you have Cluster using Antrea CNI with NodePortLocal feature or Interworking enabled, it is recommended that you upgrade to v1.35.2.

## Components

vSphere Kubernetes release 1.35.2 for use with vSphere 9.0 and vSphere 8.x includes the following OS & Kubernetes components.

This release ships with the following operating system options

Operating System & Version

Kernel Version

Photon 5.0

6.1.164-2.ph5

Ubuntu 22.04 LTS

5.15.0.171.160 (generic)

Ubuntu 24.04 LTS

6.17.0-14.14\~24.04.1 (hwe)

VKr 1.35.2 for use with vSphere 9.0 and vSphere 8.x includes the following VMware packages.

Component

Version

kubernetes

1.35.2

coredns

1.13.1

etcd

3.5.27

containerd

2.2.1

cni-plugins

1.8.0

Package

Version

antrea

2.5.1

calico

3.30.6

guest-cluster-auth-service

1.4.6

kapp-controller

0.59.1

metrics-server

0.8.1

pinniped

0.42.0

secretgen-controller

0.20.1

vsphere-cpi

1.35.0

vsphere-pv-csi

3.7.0

gateway-api

1.4.0

## Fixed Issues

**CSI driver should return non-final errors to fix the orphaned volumes and snapshots problem**

This issue has been fixed in 1.35.2

**Antrea tn-proxy logs are not rotated**

This issue has been addressed in 1.35.2

Antrea annotation nodeportlocal.antrea.io on pod is missing after cluster update from VKr 1.34.x to VKr 1.35.0.

This issue has been fixed in 1.35.2

**Antrea Hybrid inter-subnet traffic disrupted after Node lifecycle operations**

In VKS clusters where Antrea hybrid mode is enabled, Pod-to-Pod traffic between nodes in different subnets may be disrupted following Node lifecycle operations. These operations include VM Class updates, Node scaling and the reuse of Pod CIDRs. This issue specifically affects clusters where nodes are distributed across multiple subnets.

Antrea Hybrid mode is available on VKS 3.6 running VKr version 1.35 or higher.

As a temporary workaround, restarting the antrea-agent Pods on the affected Nodes may temporarily restores Pod-to-Pod traffic, This workaround does not address the underlying issue, and the traffic disruption may reoccur if the triggering conditions are met again.

## Known Issues

After an ESX reboot, time drift could cause some of the VKS nodes to be in NotReady state

Following an ESX host reboot, VKS nodes scheduled on the rebooted host, may experience clock drift. While VKr relies on the **chrony** service to synchronize time with an NTP server, a race condition can occur: if the **kubelet** initializes before **chrony** finishes correcting the time, the **kubelet** will generate service tokens with past timestamps, rendering them invalid.

**Workaround:**

Deleting the problematic node, the node will be recreated with correct time and the pods will be scheduled and running.

**After upgrade, application pods will be stuck in ContainerCreating state with FailedAttachVolume warning**

If a pod is stuck in ContainerCreating state, execute the following command -

kubectl get pods -A | grep ContainerCreating"

Describe the pod, and if you find the following warning pattern, execute the workaround

Warning FailedAttachVolume

2m9s (x59 over 104m) attachdetach-controller AttachVolume.Attach failed for volume "pvc-1f46ebd4-2606-4800-aa70-af8bdb75fdb8" : CSINode vks361-ph-336-calico-11ns5-c5-np1-worker-rf5zx-ttrqp-6qc7j does not contain driver csi.vsphere.vmware.com

**Workaround:**

restart the csi-node pods

kubectl delete pod vsphere-csi-node-\<xyz> -n vmware-system-csi

**After worker node scale-up and scale-down operation on large VKS cluster with 3CP/150W, around 70 pods went into OutofPods/Pending state**

This is caused due to a race condition in a scenario where auto-scaler is increasing the number of nodes, while there are a larger number of pods waiting to be scheduled. And scheduler assigns the pods to the first few nodes available.

**Work around:**

Delete the pods marked with the error "OutOfPods".

**Autoscaler is unable to scale up windows nodes in a cluster containing multiple node pools with mixed OS types.**

In autoscaler-based guest clusters having hybrid node pools with different OS (Photon, Ubuntu, Windows), when scaling up applications on the clusters, Windows nodes are not scaled up even though Windows pods are in a pending state.

Workloads are stuck in a pending state and new nodes will not be deployed. The autoscaler pod logs show the error can't schedule pod : predicate "NodeAffinity" didn't pass (predicateReasons=\[node(s) didn't match Pod's node affinity/selector\];

When the cluster contains multiple node pools, the autoscaler will try to automatically scale up the node to handle pending pods. When the pod contains nodeSelector, the autoscaler will simulate the node to be created based on the annotation of the current node pool to evaluate whether it meets the needs of the current pod. Windows pods need nodeSelector to schedule to Windows nodes, so this problem will be encountered.

Add the annotation (capacity.cluster-autoscaler.kubernetes.io/labels: "key1=value1,key2=value2") in machine deployment to inform the autoscaler that this node pool can create nodes with this label.

**After VKS cluster upgrade a failed Antrea upgrade job remains in the cluster**

Sometimes, when the upgrades take longer you will notice an Antrea upgrade jobs in error state. These errors do not impact the functionality of the Antrea. These are transient errors that occur while the cluster is upgrading.

Workaround: You can use the kubectl delete to clean up the failed jobs.

**Packages are in 'Reconcile failed' state after upgrade due to caBundle certificate mismatch**

After the cluster upgrades to this version, you may sometimes see that the packages are in 'Reconcile Failed' state. Due to this the upgrade is flagged as failed. This may happen because the kapp-controller from the old cluster still exists due to a possible race condition during the upgrade. Both the old and the new kapp-controller attempt to update the api service with their CA bundle causing this issue.

1\. Try restarting the kapp-controller pod in the cluster, the correct CABundle content gets synced to the api-service and all packages get reconciled.

2\. If the above workaround doesn't work, edit the CA bundle of the api service manually with the content of upgraded kapp-controller self signed cert.

## VKr v1.35.0

## Release Snapshot

Name

Release Date

vCenter

VKS

**v1.35.0+vmware.2-vkr.4**

11-Feb-2026

vCenter 9.0.0.0 or higher

vCenter 8.0 Update 3g or higher

## What's New

- 
  -   - Existing VKS clusters will need to rebase tobuiltin-generic-v3.6.0as a part of, or prior to, any upgrade to Kubernetes v1.35 or later.
- 
  - Pre-built node images for Photon OS 5.0, Ubuntu 22.04 LTS, Ubuntu 24.04 LTS
  - Custom Node Images Support - RHEL 9, Microsoft Windows Server 2022
  - vSphere Kubernetes v1.35 and all subsequent patch releases are supported for  - CNI configurations (such as Antrea and Calico) are now managed through the VKS Addon Framework using theAddonConfigcustom resource.
- - 
  -   -   - 

## Deprecations Announcements

- cgroupv1support has now been removed -

## Components

vSphere Kubernetes release 1.35.0 for use with vSphere 9.0 and vSphere 8.x includes the following OS & Kubernetes components.

This release ships with the following operating system options

Operating System & Version

Kernel Version

Photon 5.0

6.12.60-18.ph5

Ubuntu 22.04 LTS

5.15.0.168-generic

Ubuntu 24.04 LTS

6.17.0-14-generic

VKr 1.35.0 for use with vSphere 9.0 and vSphere 8.x includes the following VMware packages.

Component

Version

kubernetes

v1.35.0

coredns

v1.13.1

etcd

v3.5.26

containerd

v2.2.1

cni-plugins

v1.8.0

Package

Version

antrea

v2.5.1

calico

v3.30.5

guest-cluster-auth-service

v1.4.5

kapp-controller

v0.59.1

metrics-server

v0.8.0

pinniped

v0.42.0

secretgen-controller

v0.20.0

vsphere-cpi

v1.35.0

vsphere-pv-csi

v3.7.0

gateway-api

v1.4.0

## Fixed Issues

Logrotate configuration has been added for rsyslog along with increasing the logrotate frequency to hourly. This fixes an issue where a large rsyslog would fill up disk space and render the node unresponsive.

## Known Issues

**Antrea Hybrid inter-subnet traffic disrupted after Node lifecycle operations**

In VKS clusters where Antrea hybrid mode is enabled, Pod-to-Pod traffic between nodes in different subnets may be disrupted following Node lifecycle operations. These operations include VM Class updates, Node scaling and the reuse of Pod CIDRs. This issue specifically affects clusters where nodes are distributed across multiple subnets.

Antrea Hybrid mode is available on VKS 3.6 running VKr version 1.35 or higher.

As a temporary workaround, restarting the antrea-agent Pods on the affected Nodes may temporarily restores Pod-to-Pod traffic, This workaround does not address the underlying issue, and the traffic disruption may reoccur if the triggering conditions are met again.

**After worker node scale-up and scale-down operation on large VKS cluster with 3CP/150W, around 70 pods went into OutofPods/Pending state**

**Autoscaler is unable to scale up windows nodes in a cluster containing multiple node pools with mixed OS types.**

In autoscaler-based guest clusters having hybrid node pools with different OS (Photon, Ubuntu, Windows), when scaling up applications on the clusters, Windows nodes are not scaled up even though Windows pods are in a pending state.

Workloads are stuck in a pending state and new nodes will not be deployed. The autoscaler pod logs show the error can't schedule pod : predicate "NodeAffinity" didn't pass (predicateReasons=\[node(s) didn't match Pod's node affinity/selector\];

When the cluster contains multiple node pools, the autoscaler will try to automatically scale up the node to handle pending pods. When the pod contains nodeSelector, the autoscaler will simulate the node to be created based on the annotation of the current node pool to evaluate whether it meets the needs of the current pod. Windows pods need nodeSelector to schedule to Windows nodes, so this problem will be encountered.

Add the annotation (capacity.cluster-autoscaler.kubernetes.io/labels: "key1=value1,key2=value2") in machine deployment to inform the autoscaler that this node pool can create nodes with this label.

**After VKS cluster upgrade a failed Antrea upgrade job remains in the cluster**

Sometimes, when the upgrades take longer you will notice an Antrea upgrade jobs in error state. These errors do not impact the functionality of the Antrea. These are transient errors that occur while the cluster is upgrading.

Workaround: You can use the kubectl delete to clean up the failed jobs.

**Packages are in 'Reconcile failed' state after upgrade due to caBundle certificate mismatch**

After the cluster upgrades to 1.33.3, you may sometimes see that the packages are in 'Reconcile Failed' state. Due to this the upgrade is flagged as failed. This may happen because the kapp-controller from the old cluster still exists due to a possible race condition during the upgrade. Both the old and the new kapp-controller attempt to update the api service with their CA bundle causing this issue.

1\. Try restarting the kapp-controller pod in the cluster, the correct CABundle content gets synced to the api-service and all packages get reconciled.

2\. If the above workaround doesn't work, edit the CA bundle of the api service manually with the content of upgraded kapp-controller self signed cert.

## VKr v1.34.2

## Release Snapshot

Name

Release Date

vCenter

VKS

v1.34.2+vmware.2-vkr.2

28-January-2026

vCenter 9.0.0.0 or higher

vCenter 8.0 Update 3g or higher

## What's New

- Support for Kubernetes version 1.34.2 for Photon OS 5.0, Ubuntu 22.04 LTS, and Ubuntu 24.04 LTS
- Security Patches and Bug Fixes

## Upgrade Instructions

- VKr 1.34 only works with cluster-class withbuiltin-generic-v3.5.0.
- 

## Components

vSphere Kubernetes release 1.34.2 for use with vSphere 9.0 and vSphere 8.x includes the following OS & Kubernetes components.

This release ships with the following operating system options

Operating System & Version

Kernel Version

Photon 5.0

6.1.159-10.ph5

Ubuntu 22.04 LTS

5.15.0.164-generic

Ubuntu 24.04 LTS

6.8.0-90-generic

VKr 1.34.2 for use with vSphere 9.0 and vSphere 8.x includes the following VMware packages.

Component

Version

kubernetes

1.34.2

coredns

1.12.1

etcd

3.5.26

containerd

2.1.5

cni-plugins

1.7.1

Package

Version

antrea

2.4.4

calico

3.30.3

guest-cluster-auth-service

1.4.4

kapp-controller

0.59

metrics-server

0.8.0

pinniped

0.41.0

secretgen-controller

0.19.2

vsphere-cpi

1.34.0

vsphere-pv-csi

3.6.0

gateway-api

1.3.0

## Known Issues

No new known issues

## VKr v1.33.6

## Release Snapshot

Name

Release Date

vCenter

VKS

v1.33.6+vmware.1-fips-vkr.2

29-Jan-2026

vCenter 9.0.0.0 or higher

vCenter 8.0 Update 3b or higher

## What's New

- Support for Kubernetes version 1.33.6 for Photon OS 5.0, Ubuntu 22.04 LTS and Ubuntu 24.04 LTS.
- Security Patches & Bug Fixes

Operating System

OS Version

Kernel Version

Photon OS

Photon 5.0

Ubuntu OS

Ubuntu 22.04 LTS

Ubuntu OS

Ubuntu 24.04 LTS

## Important Upgrade Recommendations

VKr 1.33 supports both Ubuntu 24.04 and Ubuntu 22.04. Whether you are creating a new v1.33 cluster, or upgrading from v1.32 to v1.33, you must update the resolve-os-image annotation in the cluster object configuration to reflect the required Ubuntu version number. Cluster object definitions with Ubuntu nodes will require an explicit field for os-name and os-version in the ClusterClass topology annotations to resolve to either Ubuntu 22.04 or Ubuntu 24.04.

The recommended configuration is to have ClusterClass topology annotations in the following format:

run.tanzu.vmware.com/resolve-os-image: "os-name=$osname,os-version=$osversion"

**Example 1:**To create or upgrade VKr 1.33 with Ubuntu 22.04 use the following:

run.tanzu.vmware.com/resolve-os-image: "os-name=ubuntu,os-version=22.04"

**Example 2:**To create or upgrade VKr 1.33 with Ubuntu 24.04 use the following:

run.tanzu.vmware.com/resolve-os-image: "os-name=ubuntu,os-version=24.04"

\-

**If the cluster was originally created in vCenter v7.x or vCenter 8.0 GA then upgrading from KR v1.32 to KR v1.33 or an upgrade using builtin-generic-v3.3.0 (or higher) clusterclass might fail.**

This issue is fixed in vSphere Kubernetes Service 3.5.0, and the workaround does not need to be applied if environments are upgraded to VKS 3.5.0 prior to cluster upgrades.

## Components

vSphere Kubernetes release 1.33.6 for use with vSphere 9.0 and vSphere 8.x includes the following Kubernetes components.

Component

Version

kubernetes

1.33.6

coredns

1.12.0

etcd

3.5.26

containerd

2.0.7

cni-plugins

1.6.2

VKr 1.33.3 for use with vSphere 9.0 and vSphere 8.x includes the following VMware packages.

Package

Version

antrea

2.3.2

calico

3.30.3

guest-cluster-auth-service

1.4.4

kapp-controller

0.56.1

metrics-server

0.8.0

pinniped

0.39.0

secretgen-controller

0.19.2

vsphere-cpi

1.33.0

vsphere-pv-csi

3.5.0

gateway-api

1.21

## Known Issues

**Packages are in 'Reconcile failed' state after upgrade due to caBundle certificate mismatch**

After the cluster upgrades to 1.33.3, you may sometimes see that the packages are in 'Reconcile Failed' state. Because of this the upgrade is flagged as failed. This may happen because the kapp-controller from the old cluster still exists due to a possible race condition during the upgrade. Both the old and the new kapp-controller attempts to update the api service with thier CA bundle causing this issue.

1\. Try restarting the kapp-controller pod in the cluster, the correct CABundle content will get synced to the api-service and all the packages get reconciled.

2\. If the above workaround doesn't work, edit the CA bundle of the api service manually with the content of upgraded kapp-controller self signed cert.

## VKr v1.32.10

## Release Snapshot

Name

Release Date

vCenter

VKS

v1.32.10+vmware.1-fips-vkr.2

29-January-2026

vCenter 9.0.0.0 or higher

vCenter 8.0 Update 3 or higher

vSphere Kubernetes Service 3.3.3 or higher

## What's New

Operating System

OS Version

Kernel Version

Photon OS

Photon 5.0

6.1.159-9.ph5

Ubuntu OS

Ubuntu 22.04 LTS

5.15.0-164-generic

- Support for Kubernetes patch version 1.32.10 for Photon OS 5 and Ubuntu 22.04 LTS.
- Security updates and general bug fixes.

## Upgrade Instructions

**If the cluster was originally created in vCenter v7.x or vCenter 8.0 GA then upgrading from KR v1.32 to KR v1.33 or an upgrade using builtin-generic-v3.3.0 (or higher) clusterclass might fail.**

This issue is fixed in vSphere Kubernetes Service 3.5.0, and the workaround does not need to be applied if environments are upgraded to VKS 3.5.0 prior to cluster upgrades.

## Components

vSphere Kubernetes release 1.32.10 includes the following Kubernetes components.

Component

Version

kubernetes

1.32.10

coredns

1.11.3

etcd

3.5.26

containerd

1.7.29

cni-plugins

1.6.0

VKr 1.32.10 includes the following VMware packages.

Package

Version

antrea

2.2.2

calico

3.29.6

guest-cluster-auth-service

1.4.1

kapp-controller

0.55.0

metrics-server

0.7.2

pinniped

0.39

secretgen-controller

0.18.1

vsphere-cpi

1.32.0

vsphere-pv-csi

3.4.0

gateway-api

1.0.0

## Known Issues

**After VKS cluster upgrade a failed Antrea upgrade job remains in the cluster**

Sometimes, when the upgrades take longer you will notice an Antrea upgrade jobs in error state. These errors do not impact the functionality of the Antrea. These are transient errors that occur while the cluster is upgrading.

Workaround: You can use the kubectl delete to clean up the failed jobs.

## VKr v1.31.14

## Release Snapshot

Name

Release Date

vCenter

VKS

v1.31.14+vmware.1-fips-vkr.2

30-Jan-2026

vCenter 9.0.0.0 or higher vCenter 8.0 Update 3 or higher

VKS 3.3.3 or higher

## What's New

Operating System

OS Version

Kernel Version

Photon OS

Photon 5.0

6.1.159-9.ph5

Ubuntu OS

Ubuntu 22.04 LTS

5.15.0-164-generic

- Support for Kubernetes patch version 1.31.14 for Photon OS 5.0 and Ubuntu 22.04 LTS.
- Security updates and general bug fixes.

## Upgrade Recommendations

**Important :**Always consult the official

**before planning or initiating any workload cluster upgrade. This is critical for a supported and successful transition.**

## Components

vSphere Kubernetes release 1.31.14 includes the following Kubernetes components.

Component

Version

kubernetes

1.31.14

coredns

1.11.3

etcd

3.5.26

containerd

1.7.29

cni-plugins

1.5.1

VKr 1.31.14 includes the following VMware packages.

Package

Version

antrea

2.1.2

calico

3.28.5

guest-cluster-auth-service

1.4.0

kapp-controller

0.53.0

metrics-server

0.7.2

pinniped

0.39.0

secretgen-controller

0.18.0

vsphere-cpi

1.31.1

vsphere-pv-csi

3.3.2

gateway-api

1.0.0

## Known Issues

**After VKS cluster upgrade a failed Antrea upgrade job remains in the cluster**

In some cases, when the upgrades take longer you will notice an Antrea upgrade jobs in error state. These errors do not impact the functionality of the Antrea. These are transient errors that occur while the cluster is upgrading.

Workaround: You can use the kubectl delete to clean up the failed jobs.

## VKr v1.34.1

## Release Snapshot

Name

Release Date

vCenter

VKS

**v1.34.1---vmware.1-vkr.4**

27-October-2025

vCenter 9.0.0.0 or higher

vCenter 8.0 Update 3g or higher

## What's New

- 

- 
  - Release name string in the past →  - Release name string from VKr 1.34.1 onwards →
- 
  - Dynamic Resource Allocation (DRA) feature has been graduated to stable in

## Upgrade Instructions

- VKr 1.34 only works with cluster-class withbuiltin-generic-v3.5.0.

- 

- 

## Components

vSphere Kubernetes release 1.34.1 for use with vSphere 9.0 and vSphere 8.x includes the following OS & Kubernetes components.

This release ships with the following operating system options

Operating System & Version

Kernel Version

Photon 5.0

6.1.155-6.ph5

Ubuntu 22.04 LTS

5.15.0-160

Ubuntu 24.04 LTS

6.8.0-86

VKr 1.34.1 for use with vSphere 9.0 and vSphere 8.x includes the following VMware packages.

Component

Version

kubernetes

v1.34.1

coredns

v1.12.1

etcd

v3.5.23

containerd

v2.1.4

cni-plugins

v1.7.1

Package

Version

antrea

v2.4.2

calico

v3.30.2

guest-cluster-auth-service

v1.4.3

kapp-controller

v0.58.0

metrics-server

v0.8.0

pinniped

v0.40.0

secretgen-controller

v0.19.2

vsphere-cpi

v1.34.0

vsphere-pv-csi

v3.6.0

gateway-api

v1.3.0

## Known Issues

No new known issues

## Fixed Issues

## VKr v1.33.3

## Release Snapshot

Name

Release Date

vCenter

VKS

**v1.33.3---vmware.1-fips-vkr.1**

26-September-2025

vCenter 9.0.0.0 or higher

vCenter 8.0 Update 3b or higher

## What's New

**Support for Kubernetes version 1.33.3**for Photon OS 5.0, Ubuntu 22.04 LTS and Ubuntu 24.04 LTS.

Operating System

OS Version

Kernel Version

Photon OS

Photon 5.0

6.1.148-1.ph5

Ubuntu OS

Ubuntu 22.04 LTS

5.15.0-153

Ubuntu OS

Ubuntu 24.04 LTS

6.8.0-60

- - Security updates & Bug fixes

## Important Upgrade Recommendations

VKr 1.33 supports both Ubuntu 24.04 and Ubuntu 22.04. Whether you are creating a new v1.33 cluster, or upgrading from v1.32 to v1.33, you must update the resolve-os-image annotation in the cluster object configuration to reflect the required Ubuntu version number. Cluster object definitions with Ubuntu nodes will require an explicit field for os-name and os-version in the ClusterClass topology annotations to resolve to either Ubuntu 22.04 or Ubuntu 24.04.

The recommended configuration is to have ClusterClass topology annotations in the following format:

run.tanzu.vmware.com/resolve-os-image: "os-name=$osname,os-version=$osversion"

**Example 1:**To create or upgrade VKr 1.33 with Ubuntu 22.04 use the following:

run.tanzu.vmware.com/resolve-os-image: "os-name=ubuntu,os-version=22.04"

**Example 2:**To create or upgrade VKr 1.33 with Ubuntu 24.04 use the following:

run.tanzu.vmware.com/resolve-os-image: "os-name=ubuntu,os-version=24.04"

\-

**If the cluster was originally created in vCenter v7.x or vCenter 8.0 GA then upgrading from KR v1.32 to KR v1.33 or an upgrade using builtin-generic-v3.3.0 (or higher) clusterclass might fail.**

This issue is fixed in vSphere Kubernetes Service 3.5.0, and the workaround does not need to be applied if environments are upgraded to VKS 3.5.0 prior to cluster upgrades.

## Components

vSphere Kubernetes release 1.33.1 for use with vSphere 9.0 and vSphere 8.x includes the following Kubernetes components.

Component

Version

kubernetes

v1.33.3

coredns

v1.12.0

etcd

v3.5.22

containerd

v2.0.5

cni-plugins

v1.6.2

VKr 1.33.3 for use with vSphere 9.0 and vSphere 8.x includes the following VMware packages.

Package

Version

antrea

v2.3.1

calico

v3.30.0

guest-cluster-auth-service

v1.4.2

kapp-controller

v0.56.1

metrics-server

v0.7.2

pinniped

v0.39.0

secretgen-controller

v0.19.1

vsphere-cpi

v1.33.0

vsphere-pv-csi

v3.5.0

gateway-api

v1.2.1

## Known Issues

**Packages are in 'Reconcile failed' state after upgrade due to caBundle certificate mismatch**

After the cluster upgrades to 1.33.3, you may sometimes see that the packages are in 'Reconcile Failed' state. Due to this the upgrade is flagged as failed. This may happen because the kapp-controller from the old cluster still exists due to a possible race condition during the upgrade. Both the old and the new kapp-controller attempt to update the api service with their CA bundle causing this issue.

1\. Try restarting the kapp-controller pod in the cluster, the correct CABundle content gets synced to the api-service and all packages get reconciled.

2\. If the above workaround doesn't work, edit the CA bundle of the api service manually with the content of upgraded kapp-controller self signed cert.

## VKr v1.32.7

## Release Snapshot

Name

Release Date

vCenter

VKS

v1.32.7+vmware.3-fips-vkr.1

26-Sept-2025

vCenter 9.0.0.0 or higher

vCenter 8.0 Update 3 or higher

vSphere Kubernetes Service 3.3.3 or higher

## What's New

Operating System

OS Version

Kernel Version

Photon OS

Photon 5.0

6.1.148-1.ph5

Ubuntu OS

Ubuntu 22.04 LTS

5.15.0-153

- Support for Kubernetes patch version 1.32.7 for Photon OS 5 and Ubuntu 22.04 LTS.
- Security updates and general bug fixes.

## Upgrade Instructions

**If the cluster was originally created in vCenter v7.x or vCenter 8.0 GA then upgrading from KR v1.32 to KR v1.33 or an upgrade using builtin-generic-v3.3.0 (or higher) clusterclass might fail.**

This issue is fixed in vSphere Kubernetes Service 3.5.0, and the workaround does not need to be applied if environments are upgraded to VKS 3.5.0 prior to cluster upgrades.

## Components

vSphere Kubernetes release 1.32.7 includes the following Kubernetes components.

Component

Version

kubernetes

v1.32.3

coredns

v1.11.3

etcd

v3.5.22

containerd

v1.7.28

cni-plugins

v1.6.0

VKr 1.32.7 includes the following VMware packages.

Package

Version

antrea

v2.2.0

calico

v3.29.2

guest-cluster-auth-service

v1.4.1

kapp-controller

v0.55.0

metrics-server

v0.7.2

pinniped

v0.39.0

secretgen-controller

v0.18.1

vsphere-cpi

v1.32.2

vsphere-pv-csi

v3.4.0

gateway-api

v1.0.0

## Known Issues

**VKS Cluster upgrade stuck from v1.31.7 -> v1.32.7 as machine is stuck in deleting phase**

**After VKS cluster upgrade a failed Antrea upgrade job remains in the cluster**

Sometimes, when the upgrades take longer you will notice an Antrea upgrade jobs in error state. These errors do not impact the functionality of the Antrea. These are transient errors that occur while the cluster is upgrading.

Workaround: You can use the kubectl delete to clean up the failed jobs.

## VKr 1.31.11

## Release Snapshot

**Name**

**Release Date**

**vCenter**

**VKS**

v1.31.11+vmware.3-fips-vkr.1

26-Sept-2025

vCenter 9.0.0.0 or higher

vCenter 8.0 Update 3 or higher

VKS 3.3.3 or higher

## Whats New

Operating System

OS Version

Kernel Version

Photon OS

Photon 5.0

6.1.148-1.ph5

Ubuntu OS

Ubuntu 22.04 LTS

5.15.0-153

- Bug fixes and Security updates

## Components

VKr 1.31.11 includes the following Kubernetes components

Component

Version

coredns

v1.11.3

etcd

v3.5.22

containerd

v1.7.28

cni-plugins

v1.5.1

VKr 1.31.11 includes the following Core packages

Package

Version

antrea

v2.1.1

calico

v3.28.3

guest-cluster-auth-service

v1.4.0

kapp-controller

v0.53.0

metrics-server

v0.7.1

pinniped

v0.39.0

secretgen-controller

v0.18.0

vsphere-cpi

v1.31.1

vsphere-pv-csi

v3.3.2

gateway-api

v1.0.0

## Upgrade Recommendations

## Known issues

**After VKS cluster upgrade a failed Antrea upgrade job remains in the cluster**

In some cases, when upgrades take longer you will notice an Antrea upgrade jobs in error state. These errors do not impact the functionality of Antrea. These are transient errors that occur while the cluster is upgrading.

You can use the kubectl delete

to clean up the failed jobs.
## VKr v1.30.14

## Release Snapshot

**Name**

**Release Date**

**vCenter**

**VKS**

v1.30.14+vmware.1-fips-vkr.3

26-Sept-2025

vCenter 9.0.0.0 or higher

vCenter 8.0 Update 3 or higher

VKS 3.3.3 or higher

## What's New

Operating System

OS Version

Kernel Version

Photon OS

Photon 5.0

6.1.148-2.ph5

Ubuntu OS

Ubuntu 22.04 LTS

5.15.0-153

- Kubernetes patch release version 1.30.14
- Addresses applicable security vulnerabilities and bug fixes

## Components

VKr 1.30.14 includes the following Kubernetes components.

Component

Version

kubernetes

v1.30.14

coredns

v1.11.3

etcd

v3.5.19

containerd

v1.6.39

cni-plugins

v1.4.0

VKr 1.30.14 includes the following VMware packages.

Package

Version

antrea

v1.15.1

calico

v3.27.5

guest-cluster-auth-service

v1.3.3

kapp-controller

v0.50.0

metrics-server

v0.6.2

pinniped

v0.25.0

secretgen-controller

v0.16.1

vsphere-cpi

v1.30.1

vsphere-pv-csi

v3.3.0

gateway-api-package

v1.0.0

capabilities

v0.33.1

## VKr v1.33.1

## Release Snapshot

Name

Release Date

vCenter

VKS

v1.33.1---vmware.1-fips-vkr.2

06/17/2025

vCenter 9.0.0.0 or higher

vCenter 8.0 Update 3b or higher

## What's New

**Support for Kubernetes version 1.33.1**for Photon OS 5.0, Ubuntu 22.04 LTS and Ubuntu 24.04 LTS.

Operating System

OS Version

Kernel Version

Photon OS

Photon 5.0

6.1.136-2.ph5

Ubuntu OS

Ubuntu 22.04 LTS

5.15.0-141

Ubuntu OS

Ubuntu 24.04 LTS

6.8.0-60

- 

- 

  - The podstatus.resizefield is now deprecated and will no longer be set. The status of a pod resize will be exposed under two new conditions:PodResizeInProgressandPodResizePendinginstead.
  - TheEndpointSlicehints field has graduated to GA. The  - TheWatchFromStorageWithoutResourceVersionfeature flag is deprecated and can no longer be enabled
  - Removed support for  - In addition, the following APIs have newer versions of them available in 1.33. Review and update your applications accordingly.
    - certificates.k8s.io/clustertrustbundles
    - coordination.k8s.io/leasecandidates
    - authentication.k8s.io/selfsubjectreviews
    - networking.k8s.io/ipaddresses
    - networking.k8s.io/servicecidrs
    - resource.k8s.io/deviceclasses
    - resource.k8s.io/resourceclaims
    - resource.k8s.io/resourceclaimtemplates
    - resource.k8s.io/resourceslices

## Important Upgrade Recommendations

VKr 1.33 only works with cluster-class with builtin-generic-v3.4.0.

\-

**Mandatory Step:**VKr 1.33 supports both Ubuntu 24.04 and Ubuntu 22.04. Whether you are creating a new v1.33 cluster, or upgrading from v1.32 to v1.33, you must update the

resolve-os-image

annotation in the cluster object configuration to reflect the required Ubuntu version number. Cluster object definitions with Ubuntu nodes will require an explicit field for os-name

and os-version

in the ClusterClass topology annotations to resolve to either Ubuntu 22.04 or Ubuntu 24.04. **Please note, not performing this step will result in an upgrade faillure**

The recommended configuration is to have ClusterClass topology annotations in the following format:

run.tanzu.vmware.com/resolve-os-image: "os-name=$osname,os-version=$osversion"

**Example 1:**To create or upgrade VKr 1.33 with Ubuntu 22.04 use the following:

run.tanzu.vmware.com/resolve-os-image: "os-name=ubuntu,os-version=22.04"

**Example 2:**To create or upgrade VKr 1.33 with Ubuntu 24.04 use the following:

run.tanzu.vmware.com/resolve-os-image: "os-name=ubuntu,os-version=24.04"

\-

**If the cluster was originally created in vCenter v7.x or vCenter 8.0 GA then upgrading from KR v1.32 to KR v1.33 or an upgrade using builtin-generic-v3.3.0 (or higher) clusterclass might fail.**

This issue is fixed in vSphere Kubernetes Service 3.5.0, and the workaround does not need to be applied if environments are upgraded to VKS 3.5.0 prior to cluster upgrades.

## Components

vSphere Kubernetes release 1.33.1 for use with vSphere 9.0 and vSphere 8.x includes the following Kubernetes components.

Component

Version

kubernetes

v1.33.1

coredns

v1.12.0

etcd

v3.5.21

containerd

v2.0.5

cni-plugins

v1.6.2

VKr 1.33.1 for use with vSphere 9.0 and vSphere 8.x includes the following VMware packages.

Package

Version

antrea

v2.3.0

calico

v3.30.0

guest-cluster-auth-service

v1.4.2

kapp-controller

v0.56.1

metrics-server

v0.7.2

pinniped

v0.39.0

secretgen-controller

v0.19.1

vsphere-cpi

v1.33.0

vsphere-pv-csi

v3.5.0

gateway-api

v1.2.1

## Known Issues

**Consumption Interface 1.02 GA can't create Ubuntu based VKr 1.33 Cluster**

VKr 1.33 offers a choice of Ubuntu 22.04 LTS and Ubuntu 24.04 LTS. This requires the OS-name and OS-version to be specified for VKS to resolve the same. Consumption Interface 1.02 will not be able to make the resolution. It will be available in future releases

Use the CLI to specify the OS-name and OS-version as instructed above in the 'Important Upgrade Recommendation' section

**After VKS cluster upgrade a failed Antrea upgrade job remains in the cluster**

In some cases, when the upgrades take longer you will notice an Antrea upgrade jobs in error state. These errors do not impact the functionality of the Antrea. These are transient errors that occur while the cluster is upgrading.

Workaround: You can use the kubectl delete to clean up the failed jobs.

**VKS clusters with Ubuntu v1.32.x and FIPS enablement can't be upgraded to v1.33.1 with Ubuntu 24.04 as OS version**

If you select Ubuntu 24.04 as a target version for 1.33.1 for FIPS enabled Ubuntu clusters of v1.32.x, the upgrade gets stuck. Ubuntu 24.04 does not yet support FIPS enablement at the moment.

**Workaround:**Use Ubuntu 22.04 as a target since Ubuntu 24.04 doesn't support FIPS Kernel updates via Ubuntu Pro.

## VKr v1.32.3

## Release Snapshot

Name

Release Date

vCenter

VKS

**v1.32.3---vmware.1-fips-vkr.2**

06/30/2025

vCenter 9.0.0.0 or higher

vCenter 8.0 Update 3 or higher

vSphere Kubernetes Service 3.3.3 or higher

## What's New

Operating System

OS Version

Kernel Version

Photon OS

Photon 5.0

6.1.138-2.ph5

Ubuntu OS

Ubuntu 22.04 LTS

5.15.0-140

- Support for Kubernetes patch version 1.32.3 for Photon OS 5 and Ubuntu 22.04 LTS.
- Security updates and general bug fixes.

## Upgrade Instructions

**If the cluster was originally created in vCenter v7.x or vCenter 8.0 GA then upgrading from KR v1.32 to KR v1.33 or an upgrade using builtin-generic-v3.3.0 (or higher) clusterclass might fail.**

This issue is fixed in vSphere Kubernetes Service 3.5.0, and the workaround does not need to be applied if environments are upgraded to VKS 3.5.0 prior to cluster upgrades.

## Components

vSphere Kubernetes release 1.32.3 includes the following Kubernetes components.

Component

Version

kubernetes

v1.32.3

coredns

v1.11.3

etcd

v3.5.19

containerd

v1.7.27

cni-plugins

v1.6.0

VKr 1.32.3 includes the following VMware packages.

Package

Version

antrea

v2.2.0

calico

v3.29.2

guest-cluster-auth-service

v1.4.1

kapp-controller

v0.55.0

metrics-server

v0.7.2

pinniped

v0.35.0

secretgen-controller

v0.18.1

vsphere-cpi

v1.32.2

vsphere-pv-csi

v3.4.0

gateway-api

v1.0.0

## Known Issues

**After VKS cluster upgrade a failed Antrea upgrade job remains in the cluster**

In some cases, when the upgrades take longer you will notice an Antrea upgrade jobs in error state. These errors do not impact the functionality of the Antrea. These are transient errors that occur while the cluster is upgrading.

Workaround: You can use the kubectl delete to clean up the failed jobs.

## VKr v1.31.7

## Release Snapshot

Name

Release Date

vCenter

VKS

**v1.31.7---vmware.1-fips-vkr.2**

06/30/2025

vCenter 9.0.0.0 or higher

vCenter 8.0 Update 3 or higher

vSphere Kubernetes Service 3.3.3 or higher

## What's New

Operating System

OS Version

Kernel Version

Photon OS

Photon 5.0

6.1.138-2.ph5

Ubuntu OS

Ubuntu 22.04 LTS

5.15.0-140

- Support for Kubernetes patch version 1.31.7 for Photon OS 5.0 and Ubuntu 22.04 LTS.
- Security updates and general bug fixes.

## Upgrade Recommendations

**Important :**Always consult the official

**before planning or initiating any workload cluster upgrade. This is critical for a supported and successful transition.**

## Components

vSphere Kubernetes release 1.31.7 includes the following Kubernetes components.

Component

Version

kubernetes

v1.31.7

coredns

v1.11.3

etcd

v3.5.19

containerd

v1.7.27

cni-plugins

v1.5.1

VKr 1.31.7 includes the following VMware packages.

Package

Version

antrea

v2.1.0

calico

v3.28.3

guest-cluster-auth-service

v1.4.0

kapp-controller

v0.53.0

metrics-server

v0.7.1

pinniped

v0.32.0

secretgen-controller

v0.18.0

vsphere-cpi

v1.31.1

vsphere-pv-csi

v3.3.2

gateway-api

v1.0.0

## Known Issues

**After VKS cluster upgrade a failed Antrea upgrade job remains in the cluster**

In some cases, when the upgrades take longer you will notice an Antrea upgrade jobs in error state. These errors do not impact the functionality of the Antrea. These are transient errors that occur while the cluster is upgrading.

Workaround: You can use the kubectl delete to clean up the failed jobs.

## VKr v1.30.11

## Release Snapshot

Name

Release Date

vCenter Server

VKS

**v1.30.11---vmware.1-fips-vkr.2**

06/30/2025

vCenter Server 9.0.0.0 or higher

vCenter Server 8.0 U3 or higher

VKS 3.3.3 or higher

## What's New

VKr 1.30.11 includes the following new features:

- - 

Support for Kubernetes version 1.30.11 for Photon OS 5.0 and Ubuntu 22.04 LTS.

Operating System

OS Version

Kernel Version

Photon OS

Photon-5

6.1.138-1.ph5

Ubuntu OS

Ubuntu 22.04.4 LTS

5.15.0-140

## Upgrade Recommendations

**Important :**Always consult the official

**before planning or initiating any workload cluster upgrade. This is critical for a supported and successful transition.**

## Components

VKr 1.30.11 includes the following Kubernetes components.

Component

Version

kubernetes

v1.30.11

coredns

v1.11.3

etcd

v3.5.19

containerd

v1.6.38

cni-plugins

v1.4.0

VKr 1.30.11 includes the following VMware packages.

Package

Version

antrea

v1.15.1

calico

v3.27.5

guest-cluster-auth-service

v1.3.3

kapp-controller

v0.50.0

metrics-server

v0.6.2

pinniped

v0.25.0

secretgen-controller

v0.16.1

vsphere-cpi

v1.30.1

vsphere-pv-csi

v3.3.0

gateway-api-package

v1.0.0

## VKr v1.29.15

## Release Snapshot

Name

Release Date

vCenter Server

VKS

**v1.29.15---vmware.1-fips-vkr.2**

06/30/2025

vCenter Server 9.0.0.0 or higher

vCenter Server 8.0 U3 or higher

VKS 3.3.3 or higher

## What's New

VKr 1.29.15 includes the following new features:

- - 

Support for Kubernetes version 1.29.15 for Photon OS 5.0 and Ubuntu 22.04 LTS.

Operating System

OS Version

Kernel Version

Photon OS

Photon-5

6.1.138-1.ph5

Ubuntu OS

Ubuntu 22.04.4 LTS

5.15.0-140

## Upgrade Recommendations

**Important :**Always consult the official

**before planning or initiating any workload cluster upgrade. This is critical for a supported and successful transition.**

## Components

VKr 1.29.15 includes the following Kubernetes components.

Component

Version

kubernetes

v1.29.15

coredns

v1.11.1

etcd

v3.5.19

containerd

v1.6.38

cni-plugins

v1.3.0

VKr 1.29.15 includes the following VMware packages.

Package

Version

antrea

v1.13.3

calico

v3.27.5

guest-cluster-auth-service

v1.3.3

kapp-controller

v0.50.0

metrics-server

v0.6.2

pinniped

v0.25.0

secretgen-controller

v0.15.0

vsphere-cpi

v1.29.0

vsphere-pv-csi

v3.2.0

gateway-api-package

v1.0.0

capabilities

v0.33.1

## Known Issues

**During upgrade from 1.28.7 to 1.29.15 - antrea package could get stuck in Reconcile failed state.** 

As part of the upgrade, antrea packages launches an upgrade job. If the upgrade job is scheduled on older version node, the job fails and doesn't auto-reconcile.

Manually delete the job  and let kapp resync the antrea pkgi succeed(wait 10min).

kubectl delete job -n vmware-system-antrea register-placeholder

## VKr v1.28.15

## Release Snapshot

Name

Release Date

vCenter Server

VKS

**v1.28.15---vmware.3-fips-vkr.3**

06/30/2025

vCenter Server 9.0.0.0 or higher

vCenter Server 8.0 U3 or higher

VKS 3.3.3 or higher

## What's New

VKr 1.28.15 includes the following new features:

- - 

Support for Kubernetes version 1.28.15 for Photon OS 5.0 and Ubuntu 22.04 LTS.

Operating System

OS Version

Kernel Version

Photon OS

Photon OS 5.0

6.1.138-2.ph5

Ubuntu OS

Ubuntu 22.04.4 LTS

5.15.0-138

## Upgrade Recommendations

- - 
  - Upgrade to VKS 3.3.3.
  - Upgrade the VKr 1.28.15 clusters to VKr 1.29.15.

## Components

VKr 1.28.15 includes the following Kubernetes components.

Component

Version

kubernetes

v1.28.15

coredns

v1.10.1

etcd

v3.5.19

containerd

v1.6.38

cni-plugins

v1.2.0

VKr 1.28.15 includes the following Core packages.

Package

Version

antrea

v1.13.3

calico

v3.26.3

guest-cluster-auth-service

v1.3.3

kapp-controller

v0.50.0

metrics-server

v0.6.2

pinniped

v0.25.0

secretgen-controller

v0.15.0

vsphere-cpi

v1.28.0

vsphere-pv-csi

v3.1.0

gateway-api-package

v1.0.0

capabilities

v0.32.1

## VKr v1.27.16

## Release Snapshot

**v1.27.16---vmware.2-fips-vkr.2**

06/30/2025

vCenter Server 8.0 Update 2c or higher

## What's New

VKr 1.27.16 includes the following new features:

- - 

Support for Kubernetes version 1.27.16 for Photon OS 3.0 and Ubuntu 22.04 LTS.

Operating System

OS Version

Kernel Version

Photon OS

Photon OS 3.0

4.19.325-1.ph3

Ubuntu OS

Ubuntu 22.04.4 LTS

5.15.0-138

## Upgrade Recommendation

- 
  - Upgrade to VKS 3.0.0+
  - Upgrade to KR 1.28.15

**Important:**Always consult the official

**before planning or initiating any workload cluster upgrade. This is critical for a supported and successful transition.**

## Components

VKr 1.27.16 includes the following Kubernetes components.

Component

Version

kubernetes

v1.27.16

coredns

v1.10.1

etcd

v3.5.15

containerd

v1.6.36

cni-plugins

v1.2.0

VKr 1.27.16 includes the following Core packages.

Package

Version

antrea

v1.13.3

calico

v3.26.3

guest-cluster-auth-service

v1.3.0

kapp-controller

v0.48.2

metrics-server

v0.6.2

pinniped

v0.25.0

secretgen-controller

v0.15.0

vsphere-cpi

v1.27.0

vsphere-pv-csi

v3.1.0

gateway-api-package

v0.8.1

## VKr v1.32.0

VKr 1.32 is generally available for use with vSphere 8.x.

## Release Snapshot

Name

Release Date

vCenter Server 8.0

VKS

v1.32.0---vmware.6-fips-vkr.2

2/17/2025

vCenter Server 8.0 U3 and greater

VKS 3.3 and later

## What's New

VKr 1.32.0 includes the following new features:

- - 
  1. Check if the snapshot validation webhook is installed from standard packages.
    - Run following command from the jumphost/external-gateway VM with tanzu CLI installed and check for package "external-csi-snapshot-webhook" in the package list.#tanzu package installed list
  2. Remove the redundant snapshot validation webhook if found installed.
    - Run the following command from the jumphost/external-gateway VM with tanzu CLI installed to delete package "external-csi-snapshot-webhook" in the guest cluster.#tanzu package installed delete external-csi-snapshot-webhook

Other improvements include:

- - 

Operating System

OS Version

Kernel Version

Photon OS

Photon-5

6.1.126-5.ph5

Ubuntu OS

Ubuntu 22.04.5 LTS

5.15.0-131-generic

## Upgrade Instructions

**If the cluster was originally created in vCenter v7.x or vCenter 8.0 GA then upgrading from KR v1.32 to KR v1.33 or an upgrade using builtin-generic-v3.3.0 (or higher) clusterclass might fail.**

This issue is fixed in vSphere Kubernetes Service 3.5.0, and the workaround does not need to be applied if environments are upgraded to VKS 3.5.0 prior to cluster upgrades.

## Components

VKr 1.32.0 for use with vSphere 8.x includes the following Kubernetes components.

Component

Version

kubernetes

v1.32.0

coredns

v1.11.3

etcd

v3.5.17

containerd

v1.7.25

cni-plugins

v1.6.0

VKr 1.32.0 for use with vSphere 8.x includes the following VMware components.

Component

Version

antrea

v2.2.0

calico

v3.29.1

guest-cluster-auth-service

v1.4.1

kapp-controller

v0.55.0

metrics-server

v0.7.2

pinniped

v0.35.0

secretgen-controller

v0.18.1

vsphere-cpi

v1.32.2

vsphere-pv-csi

v3.4

gateway-api-package

v1.0.0

## Known Issues

**Autoscaler is unable to scale up windows nodes in a cluster containing multiple node pools with mixed OS types.**

In autoscaler-based guest clusters having hybrid node pools with different OS (Photon, Ubuntu, Windows), when scaling up applications on the clusters, Windows nodes are not scaled up even though Windows pods are in a pending state.

Workloads are stuck in a pending state and new nodes will not be deployed. The autoscaler pod logs show the error can't schedule pod : predicate "NodeAffinity" didn't pass (predicateReasons=\[node(s) didn't match Pod's node affinity/selector\];

When the cluster contains multiple node pools, the autoscaler will try to automatically scale up the node to handle pending pods. When the pod contains nodeSelector, the autoscaler will simulate the node to be created based on the annotation of the current node pool to evaluate whether it meets the needs of the current pod. Windows pods need nodeSelector to schedule to Windows nodes, so this problem will be encountered.

Add the annotation (capacity.cluster-autoscaler.kubernetes.io/labels: "key1=value1,key2=value2") in machine deployment to inform the autoscaler that this node pool can create nodes with this label.

## Fixed Issues

This VKr 1.32 release fixes the issue described in *Important Upgrade Requirements* for VKr 1.31.1 for vSphere 8.x. You no longer need to migrate the objects of Antrea CRDs to the latest storage versions before upgrading VKS clusters from VKr 1.27.

## VKr v 1.31.4

## Release Snapshot

Name

Release Date

vCenter Server 8.0

VKS

v1.31.4---vmware.1-fips-vkr.3

2/10/2025

vCenter Server 8.0 U3 and later

VKS 3.2 and later

## What's New

VKr 1.31.4 includes the following new features:

- This patch release updates the Kubernetes and containerd versions. In addition, it fixes an issue found when upgrading VKS clusters with antrea from 1.27 or earlier.

- - 

Support for Kubernetes version 1.31.4 for Photon OS 5 and Ubuntu 22.04 LTS.

Operating System

OS Version

Kernel Version

Photon OS

Photon-5

6.1.126-5.ph5

Ubuntu OS

Ubuntu 22.04.4 LTS

5.15.0-131-generic

## Components

VKr 1.31.4 for use with vSphere 8.x includes the following Kubernetes components.

Component

Version

kubernetes

v1.31.4

coredns

v1.11.3

etcd

v3.5.16

containerd

v1.7.23

cni-plugins

v1.5.1

VKr 1.31.4 for use with vSphere 8.x includes the following VMware packages.

Package

Version

antrea

v2.1.0

calico

v3.28.1

guest-cluster-auth-service

v1.4.0

kapp-controller

v0.53.0

metrics-server

v0.7.1

pinniped

v0.32.0

secretgen-controller

v0.18.0

vsphere-cpi

v1.31.1

vsphere-pv-csi

v3.3.2

gateway-api-package

v1.0.0

## Fixed Issues

**Upgrade of VKS clusters hangs when upgrading from 1.27 or earlier to 1.31.1 with Antrea**

This manual step is required because VKr 1.31.1 comes with Antrea 2.1, where deprecated CRDs are removed and CRDs with new storage versions are introduced. If you have missed performing the migration steps described in the Important Upgrade Requirements section of these release notes, the following error will be displayed in the clusterbootstrap status of the Supervisor and upgrade will hang:

status: conditions: lastTransitionTime: "2024-11-26T09:04:15Z" message: |- kapp: Error: update customresourcedefinition/tiers.crd.antrea.io (apiextensions.k8s.io/v1) cluster: Updating resource customresourcedefinition/tiers.crd.antrea.io (apiextensions.k8s.io/v1) cluster: API server says: CustomResourceDefinition.apiextensions.k8s.io "tiers.crd.antrea.io" is invalid: status.storedVersions\[0\]: Invalid value: "v1alpha1": must appear in spec.versions (reason: Invalid)

## VKr v1.31.1

## Release Snapshot

VKr 1.31.1 is generally available for use with vSphere 8.x.

Name

Release Date

vCenter Server 8.0

VKS

v1.31.1---vmware.2-fips-vkr.2

10/3/2024

vCenter Server 8.0 U3 and later

VKS 3.2 and later

## What's New

VKr 1.31.1 includes the following new features:

- 

**Operating System**

**OS Version**

**Kernel Version**

Photon OS

VMware Photon OS 5.0

6.1.109-2.ph5

Ubuntu OS

Ubuntu 22.04.4 LTS

5.15.0-122-generic

## Upgrade Recommendations

**Update: \[8th Aug 2025\]**

- Highly recommended to upgrade to VKr 1.31.7 (requires upgraded to VKS 3.3.3) or VKr 1.31.4.
- Upgrade to 1.31.1 are known to get stuck causing downtime.

**Update: \[20th Dec 2024\]**

Some customers reported issues while upgrading VKS clusters from VKr 1.27

When upgrading VKS clusters from VKr 1.27 and earlier to VKr1.31.1 with Antrea 2.1.0, you must migrate all existing objects of Antrea CRDs to the latest storage version. Follow the steps to perform the migration correctly:

\# antctl upgrade api-storage --dry-run # antctl upgrade api-storage

## Components

VKr 1.31.1 for use with vSphere 8.x includes the following Kubernetes components.

Component

Version

kubernetes

v1.31.1

coredns

v1.11.3

etcd

v3.5.16

containerd

v1.7.22

cni-plugins

v1.5.1

VKr 1.31.1 for use with vSphere 8.x includes the following VMware packages.

Package

Version

antrea

v2.1.0

calico

v3.28.1

guest-cluster-auth-service

v1.4.0

kapp-controller

v0.53.0

metrics-server

v0.7.1

pinniped

v0.32.0

secretgen-controller

v0.18.0

vsphere-cpi

v1.31.0

vsphere-pv-csi

v3.3.1

gateway-api-package

v1.0.0

## Packages

The Standard Package version v2024.9.18 includes the following packages

**Package**

**Latest Version (recommended for 1.31)**

**Other included versions**

Cluster Autoscaler

v1.31.0+vmware.1-tkg.1

v1.30.0+vmware.1-tkg.1

v1.29.0+vmware.1-tkg.1

v1.28.0+vmware.1-tkg.1

v1.27.2+vmware.1-tkg.3

Cert Manager

v1.13.3+vmware.1-tkg.1

v1.12.10+vmware.2-tkg.1

v1.1.0+vmware.1-tkg.2

v1.1.0+vmware.2-tkg.1

v1.5.3+vmware.2-tkg.1

v1.5.3+vmware.4-tkg.1

v1.5.3+vmware.7-tkg.1

v1.5.3+vmware.7-tkg.3

v1.7.2+vmware.1-tkg.1

v1.7.2+vmware.3-tkg.1

v1.7.2+vmware.3-tkg.3

v1.11.1+vmware.1-tkg.1

v1.12.2+vmware.2-tkg.2

Contour

1.28.2+vmware.1-tkg.1

1.27.1+vmware.1-tkg.1

1.26.2+vmware.1-tkg.1

External DNS

0.13.6+vmware.1-tkg.1

v0.10.0+vmware.1-tkg.1

v0.10.0+vmware.1-tkg.2

v0.10.0+vmware.1-tkg.8

v0.11.0+vmware.1-tkg.2

v0.11.0+vmware.1-tkg.8

v0.12.2+vmware.7-tkg.1

Fluent Bit

v2.2.3+vmware.1-tkg.2

v1.7.5+vmware.1-tkg.1

v1.7.5+vmware.2-tkg.1

v1.8.15+vmware.1-tkg.1

v1.9.5+vmware.1-tkg.2

v2.1.6+vmware.1-tkg.1

v2.1.6+vmware.1-tkg.2

v2.2.3+vmware.1-tkg.1

FluxCD Helm Controller

0.36.2+vmware.1-tkg.1

v0.21.0+vmware.1-tkg.1

v0.21.0+vmware.1-tkg.5

v0.28.1+vmware.1-tkg.4

FluxCD Kustomize Controller

1.1.1+vmware.1-tkg.1

v0.24.4+vmware.1-tkg.1

v0.24.4+vmware.1-tkg.5

v0.32.0+vmware.1-tkg.4

FluxCD Source Controller

1.1.2+vmware.5-tkg.1

v0.24.4+vmware.2-tkg.3

v0.33.0+vmware.2-tkg.3

0.36.1+vmware.2-tkg.2

1.1.2+vmware.1-tkg.1

Grafana

v10.0.1+vmware.1-tkg.3

v7.5.7+vmware.1-tkg.1

v7.5.7+vmware.2-tkg.1

v7.5.16+vmware.1-tkg.1

v7.5.17+vmware.1-tkg.2

v10.0.1+vmware.1-tkg.2

Harbor

2.9.1+vmware.1-tkg.1

2.8.4+vmware.1-tkg.1

Prometheus

v2.45.0+vmware.1-tkg.3

v2.37.0+vmware.3-tkg.1

v2.43.0+vmware.2-tkg.1

v2.45.0+vmware.1-tkg.1

v2.45.0+vmware.1-tkg.2

External CSI Snapshot Validation Webhook

6.1.0+vmware.1-tkg.6

vSphere PV CSI Webhook

3.1.0+vmware.1-tkg.3

## Known Issues

**Upgrade of VKS clusters hangs when upgrading from 1.27 or earlier to 1.31.1 with Antrea**

This manual step is required becauseVKr 1.31.1 comes with Antrea 2.1, where deprecated CRDs are removed and CRDs with new storage versions are introduced. If you have missed performing the migration steps described in the Important Upgrade Requirements section of these release notes, the following error will be displayed in the clusterbootstrap status of the Supervisor and upgrade will hang:

status: conditions: lastTransitionTime: "2024-11-26T09:04:15Z" message: |- kapp: Error: update customresourcedefinition/tiers.crd.antrea.io (apiextensions.k8s.io/v1) cluster: Updating resource customresourcedefinition/tiers.crd.antrea.io (apiextensions.k8s.io/v1) cluster: API server says: CustomResourceDefinition.apiextensions.k8s.io "tiers.crd.antrea.io" is invalid: status.storedVersions\[0\]: Invalid value: "v1alpha1": must appear in spec.versions (reason: Invalid)

## Fixed Issues

VKr 1.31.1 for vSphere 8.x has the following fixed issue:

When VC public keys are renewed, after you authenticate with Kubernetes cluster successfully, you will get the following error with kubectl command:

          **$ kubectl get pod -A error: You must be logged in to the server (Unauthorized)**
        

The issue is fixed in 1.31.1. Public keys will be auto reloaded.

## VKr v1.30.1

## Release Snapshot

VKr 1.30.1 is generally available for use with vSphere 8.x.

Name

Release Date

vCenter Server 8.0

VKS

v1.30.1---vmware.1-fips-tkg.5

7/8/2024

vCenter Server 8.0 U3 and later

VKS 3.1 and later

## What's New

VKr 1.30.1 includes the following new features.

- Support for Kubernetes version 1.30.1 for Photon and Ubuntu operating systems.Operating Systems (OS)OS VersionKernel VersionPhotonVMware PhotonOS 5.06.1.83-4.ph5UbuntuUbuntu 22.04.4 LTS5.15.0-107-generic

## Components

VKr v1.30.1 for vSphere 8.x includes the following Kubernetes components.

Component

Version

kubernetes

v1.30.1

coredns

v1.11.1

etcd

v3.5.12

containerd

v1.6.31

cri-tools

v1.29.0

cni-plugins

v1.4.0

VKr v1.30.1 for vSphere 8.x includes the following VMware packages.

Package

Version

antrea

v1.15.1

calico

v3.27.3

guest-cluster-auth-service

v1.3.3

kapp-controller

v0.50.0

metrics-server

v0.6.2

pinniped

v0.25.0

secretgen-controller

v0.16.1

vsphere-cpi

v1.30.1

vsphere-pv-csi

v3.3.0

capabilities

v0.33.1

gateway-api-package

v1.0.0

## Packages

The Standard Package v2024.7.2 repository includes the following standard packages.

Package

Version

Upgrades from

Cluster Autoscaler

v1.30.0+vmware.1-tkg.1-ca

v1.29.0+vmware.1-tkg.1-ca

v1.28.0+vmware.1-tkg.1-ca

v1.27.2+vmware.1-tkg.3-ca

Cert Manager

1.12.10+vmware.1-tkg.1

v1.12.2+vmware.2-tkg.2-cert-manager

v1.11.1+vmware.1-tkg.1-cert-manager

v1.7.2+vmware.3-tkg.3-cert-manager

v1.5.3+vmware.7-tkg.3-cert-manager

v1.7.2+vmware.3-tkg.1-cert-manager

v1.5.3+vmware.7-tkg.1-cert-manager

v1.7.2+vmware.1-tkg.1-cert-manager

v1.5.3+vmware.4-tkg.1-cert-manager

v1.5.3+vmware.2-tkg.1-cert-manager

v1.1.0+vmware.2-tkg.1-cert-manager

v1.1.0+vmware.1-tkg.2-cert-manager

Contour

1.28.2+vmware.1-tkg.1

1.27.1+vmware.1-tkg.1

1.26.2+vmware.1-tkg.1

External DNS

v0.13.6+vmware.1-tkg.1-external-dns

v0.12.2+vmware.7-tkg.1-external-dns

v0.11.0+vmware.1-tkg.8-external-dns

v0.10.0+vmware.1-tkg.8-external-dns

v0.11.0+vmware.1-tkg.2-external-dns

v0.10.0+vmware.1-tkg.2-external-dns

v0.10.0+vmware.1-tkg.1-external-dns

Fluent Bit

v2.2.3+vmware.1-tkg.1-fluent-bit

v2.1.6+vmware.1-tkg.2-fluent-bit

v2.1.6+vmware.1-tkg.1-fluent-bit

v1.9.5+vmware.1-tkg.2-fluent-bit

v1.8.15+vmware.1-tkg.1-fluent-bit

v1.7.5+vmware.2-tkg.1-fluent-bit

v1.7.5+vmware.1-tkg.1-fluent-bit

FluxCD Helm Controller

v0.36.2+vmware.1-tkg.1-helm-ctrl

v0.28.1+vmware.1-tkg.4-helm-ctrl

v0.21.0+vmware.1-tkg.5-helm-ctrl

v0.21.0+vmware.1-tkg.1-helm-ctrl

FluxCD Kustomize Controller

v1.1.1+vmware.1-tkg.1-kustomize-ctrl

v0.32.0+vmware.1-tkg.4-kustomize-ctrl

v0.24.4+vmware.1-tkg.5-kustomize-ctrl

v0.24.4+vmware.1-tkg.1-kustomize-ctrl

FluxCD Source Controller

v1.1.2+vmware.5-tkg.1-source-ctrl

v1.1.2+vmware.5-tkg.1-source-ctrl

v0.36.1+vmware.2-tkg.2-source-ctrl

v0.33.0+vmware.2-tkg.3-source-ctrl

v0.24.4+vmware.2-tkg.3-source-ctrl

Grafana

v10.0.1+vmware.1-tkg.2-grafana

v7.5.17+vmware.1-tkg.2-grafana

v7.5.16+vmware.1-tkg.1-grafana

v7.5.7+vmware.2-tkg.1-grafana

v7.5.7+vmware.1-tkg.1-grafana

Harbor

v2.9.1+vmware.1-tkg.1-harbor

v2.8.4+vmware.1-tkg.1-harbor

Multus CNI

v4.0.1+vmware.2-tkg.1-multus-cni

v3.8.0+vmware.3-tkg.1-multus-cni

v3.8.0+vmware.2-tkg.2-multus-cni

v3.8.0+vmware.1-tkg.1-multus-cni

v3.7.1+vmware.2-tkg.2-multus-cni

v3.7.1+vmware.2-tkg.1-multus-cni

v3.7.1+vmware.1-tkg.1-multus-cni

Prometheus

v2.45.0+vmware.1-tkg.2-prometheus

v2.45.0+vmware.1-tkg.1-prometheus

v2.43.0+vmware.2-tkg.1-prometheus

v2.37.0+vmware.3-tkg.1-prometheus

External CSI Snapshot Validation Webhook

v6.1.0+vmware.1-tkg.6-snapshot-webhook

vSphere PV CSI Webhook

v3.1.0+vmware.1-tkg.3-vspherecsiwebhook

Whereabouts

v0.6.3+vmware.1-tkg.2-whereabouts

v0.5.1+vmware.2-tkg.1-whereabouts

v0.5.4+vmware.1-tkg.1-whereabouts

v0.5.4+vmware.2-tkg.1-whereabouts

## Known Issues

None.

## Fixed Issues

**After decreasing the node-pool max count, scale down of worker nodes is failing on VKS cluster.**

Fixed.

## TKr v1.29.5 for vSphere 8.x

## Release Snapshot

TKr 1.29.5 is generally available for use with vSphere 8.x.

- Contains fix for CVE-2024-6387
- Nvidia GPU fix

Name

Release Date

vCenter Server 8.0

TKG Service

v1.29.5---vmware.3-fips.1-tkg.1

9/6/2024

vCenter Server 8.0 U3 and later

TKG Service 3.1 and later

## What's New

TKr 1.29.5 includes the following new features.

- Support for Kubernetes version 1.29.5 for Photon OS and Ubuntu.Operating Systems (OS)OS VersionKernel VersionPhotonVMware Photon OS 5.06.1.83-4.ph5UbuntuUbuntu 22.04.4 LTS5.15.0-116-generic

## Components

TKr v1.29.5 for vSphere 8.x includes the following Kubernetes components.

Component

Version

kubernetes

v1.29.5

coredns

v1.11.1

etcd

v3.5.12

containerd

v1.6.31

cri-tools

v1.28.0

cni-plugins

v1.3.0

TKr 1.29.5 for vSphere 8.x includes the following VMware packages.

Package

Version

antrea

v1.13.3

calico

v3.27.3

guest-cluster-auth-service

v1.3.3

kapp-controller

v0.50.0

metrics-server

v0.6.2

pinniped

v0.25.0

secretgen-controller

v0.16.1

vsphere-cpi

v1.29.0

vsphere-pv-csi

v3.2.0

**gateway-api-package**

v1.0.0

## Packages

The Standard Package v2024.6.27 repository includes the following standard packages.

Package

Version

Cluster Autoscaler

1.29.0+vmware.1-tkg.1

Cert Manager

1.12.10+vmware.1-tkg.1

Contour

1.26.2+vmware.1-tkg.1

1.27.1+vmware.1-tkg.1

1.28.2+vmware.1-tkg.1

External DNS

0.13.6+vmware.1-tkg.1

Fluent Bit

2.1.6+vmware.1-tkg.2

FluxCD Helm Controller

0.36.2+vmware.1-tkg.1

FluxCD Kustomize Controller

1.1.1+vmware.1-tkg.1

FluxCD Source Controller

0.36.1+vmware.2-tkg.2

1.1.2+vmware.1-tkg.1

1.1.2+vmware.5-tkg.1

Grafana

10.0.1+vmware.1-tkg.2

Harbor

2.8.4+vmware.1-tkg.1

2.9.1+vmware.1-tkg.1

Prometheus

2.45.0+vmware.1-tkg.2

External CSI Snapshot Validation Webhook

6.1.0+vmware.1-tkg.6

vSphere PV CSI Webhook

3.1.0+vmware.1-tkg.3

## VKr v1.29.4

## Release Snapshot

VKr 1.29.4 is generally available for use with vSphere 8.x.

Name

Release Date

vCenter Server 8.0

v1.29.4---vmware.3-fips.1-tkg.1

6/27/2024

vCenter Server 8.0 U3 and later

## What's New

VKr 1.29.4 includes the following new features.

- Support for Kubernetes version 1.29.4 for Photon and Ubuntu operating systems.Photon OSUbuntu OSOS VersionVMware Photon Linux 5.0Ubuntu 22.04.4 LTSKernel Version6.1.83-4.ph55.15.0-107-generic
- Container runtime:
  - runc updated to version 1.1.12
  - containerd updated to version 1.6.31

## Components

TKr v1.29.4 for vSphere 8.x includes the following Kubernetes components.

Component

Version

kubernetes

v1.29.4

coredns

v1.10.1

etcd

v3.5.12

containerd

v1.6.31

cri-tools

v1.28.0

cni-plugins

v1.3.0

TKr v1.29.4 for vSphere 8.x includes the following VMware packages.

Package

Version

antrea

v1.13.3

calico

v3.27.3

guest-cluster-auth-service

v1.3.3

kapp-controller

v0.50.0

metrics-server

v0.6.2

pinniped

v0.25.0

secretgen-controller

v0.16.1

vsphere-cpi

v1.29.0

vsphere-pv-csi

v3.2.0

## Packages

The Standard Package v2024.6.27 repository includes the following standard packages.

Package

Version

Cluster Autoscaler

1.29.0+vmware.1-tkg.1

Cert Manager

1.12.10+vmware.1-tkg.1

Contour

1.26.2+vmware.1-tkg.1

1.27.1+vmware.1-tkg.1

1.28.2+vmware.1-tkg.1

External DNS

0.13.6+vmware.1-tkg.1

Fluent Bit

2.1.6+vmware.1-tkg.2

FluxCD Helm Controller

0.36.2+vmware.1-tkg.1

FluxCD Kustomize Controller

1.1.1+vmware.1-tkg.1

FluxCD Source Controller

0.36.1+vmware.2-tkg.2

1.1.2+vmware.1-tkg.1

1.1.2+vmware.5-tkg.1

Grafana

10.0.1+vmware.1-tkg.2

Harbor

2.8.4+vmware.1-tkg.1

2.9.1+vmware.1-tkg.1

Prometheus

2.45.0+vmware.1-tkg.2

External CSI Snapshot Validation Webhook

6.1.0+vmware.1-tkg.6

vSphere PV CSI Webhook

3.1.0+vmware.1-tkg.3

## Upgrade Recommendation

- 

## TKr 1.28.8 for vSphere 8.x

## Release Snapshot

TKr 1.28.8 is generally available for use with vSphere 8.x.

Name

Release Date

vCenter Server 8.0

v1.28.8---vmware.1-fips.1-tkg.2

5/8/2024

vCenter Server 8.0 U2c and later

## What's New

TKr 1.28.8 includes the following new features.

- Support for Kubernetes version 1.28.8 for PhotonOS and Ubuntu.
  - PhotonOS 5.0: Kernel version: 6.1.81-2.ph5
  - Ubuntu 22.04.4 LTS: Kernel version: 5.15.0-101-generic

- PhotonOS upgraded to PhotonOS 5
- runc updated to version 1.1.12
- containerd updated to version 1.6.28

## Components

TKr 1.28.8 for vSphere 8.x includes the following Kubernetes components.

Component

Version

kubernetes

v1.28.8

coredns

v1.10.1

etcd

v3.5.12

containerd

v1.6.28

cri-tools

v1.27.0

cni-plugins

v1.2.0

TKr 1.28.8 for vSphere 8.x includes the following VMware packages.

Package

Version

antrea

v1.13.3

calico

v3.26.3

guest-cluster-auth-service

v1.3.3

kapp-controller

v0.48.2

metrics-server

v0.6.2

pinniped

v0.25.0

secretgen-controller

v0.15.0

vsphere-cpi

v1.28.0

vsphere-pv-csi

v3.1.0

capabilities

v0.32.1

## Upgrade Recommendations

- 

## TKr 1.27.11 for vSphere 8.x

## Release Snapshot

TKr 1.27.11 is generally available for use with vSphere 8.x.

Name

Release Date

vCenter Server 8.0

v1.27.11---vmware.1-fips.1-tkg.2

4/18/2024

vCenter Server 8.0 U2c and later

## What's New

TKr 1.27.11 includes the following new features.

- Support for Kubernetes version 1.27.11 for PhotonOS and Ubuntu.
  - PhotonOS 3.0: Kernel version: 4.19.306-1.ph3
  - Ubuntu 22.04.4 LTS: Kernel version: 5.15.0-97-generic

- runc has been updated to version 1.1.12
- containerd has been updated to version 1.6.28

## Components

TKr 1.27.11 for vSphere 8.x includes the following Kubernetes components.

Component

Version

kubernetes

v1.27.11

coredns

v1.10.1

etcd

v3.5.11

containerd

v1.6.28

cri-tools

v1.26.0

cni-plugins

v1.2.0

TKr 1.27.11 for vSphere 8.x includes the following VMware packages.

Package

Version

antrea

v1.13.3

calico

v3.26.3

guest-cluster-auth-service

v1.3.0

kapp-controller

v0.48.2

metrics-server

v0.6.2

pinniped

v0.25.0

secretgen-controller

v0.15.0

vsphere-cpi

v1.27.0

vsphere-pv-csi

v3.1.0

capabilities

v0.32.1

## Resolved Issues

**After a power outage or other repeated I/O failures, the VKS cluster is unhealthy and the workloads are unavailable**

With VKr versions earlier than 1.27.11, repeated I/O failures, triggered by a power outage or datastore path change, can cause the control plane and worker node disks to be mounted as ReadOnly. As a result, the VKS cluster becomes unhealthy and its workloads unavailable.

Workaround:

- To resolve this issue on VKr versions earlier than 1.27.11, restart the VMs.
- On VKr version 1.27.11 and later, this issue is resolved.

## TKr 1.26.13 for vSphere 8.x

## Release Snapshot

TKr 1.26.13 is generally available for use with vSphere 8.x.

Name

Release Date

vCenter Server 8.0

v1.26.13---vmware.1-fips.1-tkg.3

3/15/2024

vCenter Server 8.0 U1c and later

## What's New

TKr 1.26.13 includes the following new features.

- Support for Kubernetes version 1.26.13 for PhotonOS and Ubuntu.
  - PhotonOS 3.0: Kernel version: 4.19.305-6.ph3
  - Ubuntu 20.04.6 LTS: Kernel version: 5.4.0-171-generic
- runc has been updated to version 1.1.12
- containerd has been updated to version 1.6.28

## Components

TKr 1.26.13 for vSphere 8.x includes the following Kubernetes components.

Component

Version

kubernetes

v1.26.13

coredns

v1.9.3

etcd

v3.5.11

containerd

v1.6.28

cri-tools

v1.25.0

cni-plugins

v1.1.1

TKr 1.26.13 for vSphere 8.x includes the following VMware packages.

Package

Version

antrea

v1.11.3

calico

v3.25.1

guest-cluster-auth-service

v1.3.0

kapp-controller

v0.45.2

metrics-server

v0.6.2

pinniped

v0.24.0

secretgen-controller

v0.14.2

vsphere-cpi

v1.26.2

vsphere-pv-csi

v3.1.0

capabilities

v0.30.0

## Fixed Issues

**High Slab memory usage / release photon with these 2 kernel params**

The Photon OS kernel used for TKR 1.23.8 and 1.24.9 had a cgroup memory leak.

**VKS clusters going to ClusterBootstrapReconciling state on a random basis.**

This issue is fixed with with this release of VKr which includes the Antrea v1.11.2 package.

## TKr 1.26.5 for vSphere 8.x

## Release Snapshot

TKr 1.26.5 is generally available for use with vSphere 8.x.

Name

Release Date

vCenter Server 8.0

v1.26.5---vmware.2-fips.1-tkg.1

8/24/2023

vCenter Server 8.0 U1c and later

## What's New

TKr 1.26.5 includes the following new features.

- Support for Kubernetes version 1.26.5 for PhotonOS and Ubuntu.
  - Photon OS Kernel version: photon-4.19.288-2.ph3
  - Ubuntu Kernel version: ubuntu-20.04.1
- With TKr 1.26.5, VKS on Supervisor will enforce PSA by default on VKS clusters.
  - Sample command to update pod security on a TKr 1.26 Kubernetes namespace:
    - kubectl label --overwrite ns NAMESPACE pod-security.kubernetes.io/enforce=privileged

    PSA policies on system namespaces cannot be changed.
  - See also:
    - TKr 1.25 Release Notes
    - TKG on Supervisor documentation

## Components

TKr 1.26.5 for vSphere 8.x includes the following Kubernetes components.

Component

Version

kubernetes

v1.26.5

coredns

v1.9.3

etcd

v3.5.6

TKr 1.26.5 for vSphere 8.x includes the following VMware packages.

Package

Version

antrea

v1.11.1

calico

v3.25.1

guest-cluster-auth-service

v1.3.0

kapp-controller

v0.45.2

metrics-server

v0.6.2

pinniped

v0.24.0

secretgen-controller

v0.14.2

vsphere-cpi

v1.26.2

vsphere-pv-csi

v3.1.0

capabilities

v0.30.0

## Known Issues

**VKS clusters using Antrea CNI have been observed flipping between Ready True/False.**

VKS clusters using VKr v1.26.5 with the Antrea package v1.11.1 can randomly enter into a ClusterBootstrapReconciling state.

Workaround: Upgrade to VKr v1.26.13 that includes the Antrea v1.11.2 package which fixes the issue.

## Fixed Issues

TKr 1.26.5 for vSphere 8.x has the following fixed issues.

**Iptables fails with exit code 3 (no child processes) due to bpfilter kernel bug**

**Verify naming length issue due to kapp is fixed**

Verify that the name length issue is fixed and available from v0.45.0 of kapp controller.

C**onsume linux kernel package for photon images instead of linux-esx**

The linux-esx kernel package lacks some of the features supported by the generic linux kernel package. Because there is no specific requirement to support linux-esx kernel, moving to the linux kernel package is preferred.

## TKr 1.25.7 for vSphere 8.x

## Release Snapshot

TKr 1.25.7 is generally available for use with vSphere 8.x.

Name

Release Date

vCenter Server 8.0

v1.25.7---vmware.3-fips.1-tkg.1

7/27/2023

vSphere 8.0 U1c and later

## What's New

TKr 1.25.7 includes the following new features.

- Support for Kubernetes version 1.25.7 for PhotonOS and Ubuntu.

- Support for Pod Security Admission (PSA) controller to replace Pod Security Policies (PSP).
  - With TKr 1.25, VKS supports applying pod security standards of type privileged, baseline, and restricted using the Pod Security Admission (PSA) controller. By default, for a VKS cluster created with 1.25 TKr, all namespaces have their pod security warn and audit modes set to restricted. This is a no-force setting: the PSA controller may generate warnings about pods violating policy, but the pods will continue to run. Some system pods running in kube-system, tkg-system, and vmware-system-cloud-provider require elevated privileges. These namespaces are excluded from pod security.
  - With 1.26 TKr, VKS will enforce PSA by default on VKS clusters. TKr 1.25 users should plan to migrate their VKS cluster workloads to PSA in anticipation of uprading VKS clusters to TKr 1.26.
  - PSA configuration for VKS:
    - TKr 1.25.7 - warn mode: restricted, audit mode: restricted, enforce mode: not set
    - TKr 1.26 and later - enforce mode: restricted
  - Sample commands to update pod security on a TKr 1.25 Kubernetes namespace:
    - kubectl label --overwrite ns NAMESPACE pod-security.kubernetes.io/audit=privileged
    - kubectl label --overwrite ns NAMESPACE pod-security.kubernetes.io/warn=privileged

    PSA policies on system namespaces cannot be changed.

## Components

TKr 1.25.7 for use with vSphere 8.x includes the following Kubernetes components.

Component

Version

kubernetes

v1.25.7

coredns

v1.9.3

etcd

v3.5.6

TKr 1.25.7 for use with vSphere 8.x includes the following VMware packages.

Package

Version

antrea

v1.9.0

calico

v3.24.1

guest-cluster-auth-service

v1.3.0

kapp-controller

v0.41.7

metrics-server

v0.6.2

pinniped

v0.12.1

secretgen-controller

v0.11.2

vsphere-cpi

v1.25.1

vsphere-pv-csi

v2.7.1

capabilities

v0.29.0

## Known Issues

TKr 1.25.7 for use with vSphere 8.x has the following known issues.

**For Clusters provisioned using the v1beta1 API, upgrading the Kubernetes version from TKr v1.24.9 to TKr v1.25.7 can result in an inconsistent cluster state if you couple the version upgrade with a scale up of the number of nodes in a node pool.**

For clusters provisioned using the v1beta1 API, attempting to perform a version upgrade from  TKr v1.24.9+vmware.1-tkg.4 to TKr v1.25.7+vmware.3-fips.1-tkg.1 in the same operation as a scale up of the number of replicas in a node pool can lead to the cluster upgrade failing. The control plane will upgrade, but the node pool scale up operation fails causing the cluster upgrade to roll back.

NOTE: This issue has been observed only on v1beta1 Clusters with Supervisor running Cluster API (CAPI) version less than 1.5.0. Supervisor running CAPI 1.5.0 or above will not face this issue.

If this issue does occur, scale in the node pool to 0 and wait for the cluster to complete the upgrade. Once the upgrade is successful then scale out the nodes to desired value.

NOTE: As a general practice, it is recommended that you perform a cluster version upgrade first and separately. Once the version upgrade completes successfully, you can then perform a second operation and scale in or out the number of nodes in a node pool.

## Fixed Issues

TKr 1.25.7 for use with vSphere 8.x has the following fixed issues.

**VKS clusters on Supervisor do not display pod metrics**

1.23.15 and 1.24.9 VKS VKr's were using cgroupfs as cgroupdriver for containerd. With 1.25 containerd uses systemd as cgroupdriver.

**Online volume expansion on restored pvc failed**

Fixes issue in online expansion of persistent  volume in workload cluster.

**Regression in performance of pvc creation**

Fixes performance issue caused by regression in pvcsi-driver shipped with VKr 1.24.9.

## TKr v1.28.7 for vSphere 7.x

## Release Snapshot

TKr 1.28.7 is generally available for use with vSphere 7.x.

Name

Release Date

vCenter Server 7.0

v1.28.7---vmware.1-fips.1-tkg.1

(Photon)
7/12/2024

vCenter Server 7.0 Update 3P and later

v1.28.7---vmware.1-fips.1-tkg.1.ubuntu

(Ubuntu)
7/12/2024

vCenter Server 7.0 Update 3P and later

## What's New

TKr 1.28.7 includes the following new features.

- Support for Kubernetes version 1.28.7 for Photon and Ubuntu operating systems.Operating Systems (OS)OS VersionKernel VersionPhotonVMware PhotonOS 5.06.1.83-4.ph5UbuntuUbuntu 22.04.4 LTS5.15.0-107-generic

## Components

TKr 1.28.7 for vSphere 7.x includes the following core components.

Component

Version

kubernetes

v1.28.7

coredns

v1.10.1

etcd

v3.5.12

containerd

v1.6.28

cri-tools

v1.27.0

cni-plugins

v1.2.0

TKr 1.28.7 for vSphere 7.x includes the following additional components.

Package

Version

antrea

v1.13.3

calico

v3.26.3

guest-cluster-auth-service

v1.3.3

metrics-server

v0.6.2

vsphere-cpi

v1.28.0

vsphere-pv-csi

v3.0.1

dockerd

v2.7.1

## Known Issues

None

## Fixed Issues

None

## TKr 1.27.10 for vSphere 7.x

## Release Snapshot

TKr 1.27.10 is generally available for use with vSphere 7.x.

Name

Release Date

vCenter Server 7.0

v1.27.10---vmware.1-fips.1-tkg.1

(Photon)
4/5/2024

vCenter Server 7.0 Update 3P and later

v1.27.10---vmware.1-fips.1-tkg.1.ubuntu

(Ubuntu)
4/5/2024

vCenter Server 7.0 Update 3P and later

## What's New

TKr 1.27.10 for vSphere 7.x includes the following new features.

- Support for Kubernetes version 1.27.10 for Photon OS and Ubuntu, respectively.
  - PhotonOS 3.0 | Kernel version: 4.19.306-1.ph3
  - Ubuntu 20.04.6 LTS | Kernel version: 5.4.0-172-generic
- runc has been updated to version 1.1.12
- containerd has been updated to version 1.6.28

## Components

TKr 1.27.10 for vSphere 7.x includes the following core components.

Component

Version

kubernetes

v1.27.10

coredns

v1.10.1

etcd

v3.5.11

containerd

v1.6.28

cri-tools

v1.26.0

cni-plugins

v1.2.0

TKr 1.27.10 for vSphere 7.x includes the following additional components.

Package

Version

antrea

v1.11.3

calico

v3.26.1

guest-cluster-auth-service

v1.3.2

metrics-server

v0.6.2

vsphere-cpi

v1.27.0

vsphere-pv-csi

v3.0.0

dockerd

v2.7.1

## Verify Compatibility

In addition to reviewing the compatibility matrix, you should independently verify compatibility before using or upgrading to a particular VKr. You must also verify compatibility before upgrading Supervisor. Note that upgrading Supervisor may initiate a rolling update of provisioned VKS clusters.

          **Compatibility with Supervisor**
        

To verify VKr compatibility with Supervisor, switch context to the target vSphere Namespace and run the command kubectl get tkr. The COMPATIBLE column displays a Boolean value showing the compatibility of each VKr with Supervisor. *True* means the release is compatible with Supervisor. *False* means it is not.

For the VKr to be compatible, Supervisor must be upgraded to the latest patch version shipped with the corresponding vCenter release.

**Compatibility with vSphere 8.x and 7.x**

There are two types of VKr formats: non-legacy VKrs and legacy VKRs.

- Non-legacy VKrs are purpose-built for vSphere 8.x and are only compatible with vSphere 8.x
- Legacy VKrs use a legacy format and are compatible with vSphere 7.x, and also with vSphere 8.x but for upgrade purposes only.

To verify VKr compatibility with vSphere, run the command kubectl get tkr TKR\_NAME --show-labels (or kubectl get tkr TKR-NAME -o yaml). To list only the VKrs that do not contain the legacy label, run the command kubectl get tkr -l '!run.tanzu.vmware.com/legacy-tkr'. See examples below.

If the release includes the label annotation run.tanzu.vmware.com/legacy-tkr, the image is based on the vSphere 7.x format. You can run a legacy VKr on vSphere 8.x, but you will not be able to take advantage of vSphere 8.x features such as class-based clusters and Carvel packaging until you upgrade to a non-legacy VKr. For more information, refer to the *Using TKG Service with vSphere Supervisor* documentation.

The following example shows that *v1.24.11---vmware.1-fips.1-tkg.1* is a legacy VKr because the legacy-tkr label is present.

kubectl get tkr v1.24.11---vmware.1-fips.1-tkg.1 -o yaml apiVersion: run.tanzu.vmware.com/v1alpha3 kind: TanzuKubernetesRelease metadata: creationTimestamp: "2023-07-14T04:25:04Z" finalizers: - tanzukubernetesrelease.run.tanzu.vmware.com generation: 1 labels: os-arch: amd64 os-name: photon os-type: linux os-version: "3.0"

The following example shows that *v1.25.7---vmware.3-fips.1-tkg.1* is a non-legacy VKr because the legacy-tkr label is absent.

kubectl get tkr v1.25.7---vmware.3-fips.1-tkg.1 -o yaml apiVersion: run.tanzu.vmware.com/v1alpha3 kind: TanzuKubernetesRelease metadata: creationTimestamp: "2023-07-27T04:20:13Z" finalizers: - tanzukubernetesrelease.run.tanzu.vmware.com generation: 2 labels: os-arch: amd64 os-name: ubuntu os-type: linux os-version: "20.04" name: v1.25.7---vmware.3-fips.1-tkg.1

The output of the command kubectl get tkr -l '!run.tanzu.vmware.com/legacy-tkr' returns all non-legacy VKrs. These are the vKrs purpose-built for vSphere 8.x and only compatible with vSphere 8.x. (Current as of April 11, 2024).

NAME VERSION READY COMPATIBLE CREATED v1.23.15---vmware.1-tkg.4 v1.23.15+vmware.1-tkg.4 True True 317d v1.23.8---vmware.2-tkg.2-zshippable v1.23.8+vmware.2-tkg.2-zshippable True True 317d v1.24.9---vmware.1-tkg.4 v1.24.9+vmware.1-tkg.4 True True 317d v1.25.7---vmware.3-fips.1-tkg.1 v1.25.7+vmware.3-fips.1-tkg.1 True True 259d v1.26.13---vmware.1-fips.1-tkg.3 v1.26.13+vmware.1-fips.1-tkg.3 True True 14d v1.26.5---vmware.2-fips.1-tkg.1 v1.26.5+vmware.2-fips.1-tkg.1 True True 231d

## List Components and Packages

The VKr for vSphere 8.x are updated to a package-based framework for VKS components, such as the container storage interface (CSI) and container network interface (CNI). To view the components and packages comprising a release, run the command kubectl get tkr TKR\_NAME -o yaml.

For example, the command kubectl get tkr v1.25.7---vmware.3-fips.1-tkg.1 -o yaml returns the following:

spec: bootstrapPackages: - name: antrea.tanzu.vmware.com.1.9.0+vmware.2-tkg.1-advanced-vmware - name: vsphere-pv-csi.tanzu.vmware.com.2.7.1+vmware.1-tkg.2-vmware - name: vsphere-cpi.tanzu.vmware.com.1.25.1+vmware.2-tkg.2-vmware - name: kapp-controller.tanzu.vmware.com.0.41.7+vmware.1-tkg.1-vmware - name: guest-cluster-auth-service.tanzu.vmware.com.1.3.0+tkg.1-vmware - name: metrics-server.tanzu.vmware.com.0.6.2+vmware.1-tkg.2-vmware - name: secretgen-controller.tanzu.vmware.com.0.11.2+vmware.1-tkg.3-vmware - name: pinniped.tanzu.vmware.com.0.12.1+vmware.3-tkg.4-vmware - name: capabilities.tanzu.vmware.com.0.29.0+vmware.1 - name: calico.tanzu.vmware.com.3.24.1+vmware.1-tkg.2-vmware kubernetes: coredns: imageTag: v1.9.3\_vmware.7-fips.1 etcd: imageTag: v3.5.6\_vmware.9-fips.1 imageRepository: localhost:5000/vmware.io pause: imageTag: "3.8" version: v1.25.7+vmware.3-fips.1 osImages: - name: ob-21961079-ubuntu-2004-amd64-vmi-k8s-v1.25.7---vmware.3-fips.1-tkg.1 - name: ob-21961086-photon-3-amd64-vmi-k8s-v1.25.7---vmware.3-fips.1-tkg.1 version: v1.25.7+vmware.3-fips.1-tkg.1

## Compatibility Matrix

The table lists VKrs and their compatibility with vCenter and Supervisor. The leading number is the Kubernetes version delivered with that release. Independently verify release compatibility before installing or upgrading. See the *Verify VKr Compatibility* section.

For the VKr to be compatible, Supervisor must be upgraded to the latest patch version shipped with the corresponding vCenter release.

**VKr for vSphere 8.x**

The table lists available VKrs for vSphere 8.x.

**VKr for vSphere 8.x**

**Name**

**Minimum vCenter Version**

**Supervisor Shipped with the Minimum vCenter Version**

**Release Date**

VKr 1.30.1 vSphere 8.x (Photon and Ubuntu)

v1.30.1---vmware.1-fips-tkg.5

vSphere 8.0 U3

Supervisor 1.26, 1.27, 1.28

7/8/2024

VKr 1.29.4 vSphere 8.x (Photon and Ubuntu)

v1.29.4---vmware.3-fips.1-tkg.1

vSphere 8.0 U3

Supervisor 1.26, 1.27, 1.28

6/27/2024

VKr 1.28.8 vSphere 8.x (Photon and Ubuntu)

v1.28.8---vmware.1-fips.1-tkg.2

vSphere 8.0 U2c

Supervisor 1.23, 1.24, 1.25

5/8/2024

VKr 1.27.11 vSphere 8.x (Photon and Ubuntu)

v1.27.11---vmware.1-fips.1-tkg.2

vSphere 8.0 U2c

Supervisor 1.23, 1.24, 1.25

4/18/2024

VKr 1.26.13 vSphere 8.x (Photon and Ubuntu)

v1.26.13---vmware.1-fips.1-tkg.3

vSphere 8.0 U1c

Supervisor 1.23, 1.24, 1.25

3/15/2024

VKr 1.26.5 vSphere 8.x (Photon and Ubuntu)

v1.26.5---vmware.2-fips.1-tkg.1

vSphere 8.0 U1c

Supervisor 1.23, 1.24, 1.25

8/24/2023

VKr 1.25.7 vSphere 8.x (Photon and Ubuntu)

v1.25.7+vmware.3-fips.1-tkg.1

vSphere 8.0 U1c

Supervisor 1.23, 1.24, 1.25

7/27/2023

VKr 1.24.9 for vSphere 8.x (Photon and Ubuntu)

v1.24.9---vmware.1-tkg.4

vSphere 8.0 U1

Supervisor 1.22, 1.23, 1.24

4/18/2023

VKr 1.23.15 for vSphere 8.x (Photon and Ubuntu)

v1.23.15---vmware.1-tkg.4

vSphere 8.0 U1

Supervisor 1.22, 1.23, 1.24

4/18/2023

VKr 1.23.8 for vSphere 8.x (Photon and Ubuntu)

v1.23.8---vmware.2-tkg.1-zshippable

vSphere 8.0

Supervisor 1.22, 1.23, 1.24

2/10/2023

**Legacy VKr for vSphere 7.x**

The table lists available VKrs for vSphere 7.x.

**VKr for vSphere 7.x**

**Name**

**Minimum vCenter Server Version**

**Supervisor Version Shipped with the Minimum vCenter Version**

**Release Date**

VKr 1.28.7 vSphere 7.x (Photon)

v1.28.7---vmware.1-fips.1-tkg.1

vCenter Server 7.0 Update 3P

vCenter Server 8.0 U2c (for upgrade to vSphere 8.x VKr)

Supervisor 1.23, 1.24, 1.25

7/12/2024

VKr 1.28.7 vSphere 7.x (Ubuntu)

v1.28.7---vmware.1-fips.1-tkg.1.ubuntu

vCenter Server 7.0 Update 3P

vCenter Server 8.0 U2c (for upgrade to vSphere 8.x VKr)

Supervisor 1.23, 1.24, 1.25

7/12/2024

VKr 1.27.10 vSphere 7.x (Photon)

v1.27.10+vmware.1-fips.1-tkg.1

vCenter Server 7.0 Update 3P

vCenter Server 8.0 U2c (for upgrade to vSphere 8.x VKr)

Supervisor 1.23, 1.24, 1.25

4/5/2024

VKr 1.27.10 vSphere 7.x (Ubuntu)

v1.27.10+vmware.1-fips.1-tkg.1.ubuntu

vCenter Server 7.0 Update 3P

vCenter Server 8.0 U2c (for upgrade to vSphere 8.x VKr)

Supervisor 1.23, 1.24, 1.25

4/5/2024

VKr 1.27.6 vSphere 7.x (Photon)

v1.27.6+vmware.1-fips.1-tkg.1

vCenter Server 7.0 Update 3P

vCenter Server 8.0 U2c (for upgrade to vSphere 8.x VKr)

Supervisor 1.23, 1.24, 1.25

1/31/2024

VKr 1.27.6 vSphere 7.x (Ubuntu)

v1.27.6+vmware.1-fips.1-tkg.1.ubuntu

vCenter Server 7.0 Update 3P

vCenter Server 8.0 U2c (for upgrade to vSphere 8.x VKr)

Supervisor 1.23, 1.24, 1.25

1/31/2024

VKr 1.26.12 vSphere 7.x (Photon)

v1.26.12+vmware.1-fips.1-tkg.1

vCenter Server 7.0 Update 3P

vCenter Server 8.0 U2b (for upgrade to vSphere 8.x VKr)

Supervisor 1.23, 1.24, 1.25

3/15/2024

VKr 1.26.12 vSphere 7.x (Ubuntu)

v1.26.12+vmware.1-fips.1-tkg.1.ubuntu

vCenter Server 7.0 Update 3P

vCenter Server 8.0 U2b (for upgrade to vSphere 8.x VKr)

Supervisor 1.23, 1.24, 1.25

3/15/2024

VKr 1.26.10 vSphere 7.x (Photon)

v1.26.10+vmware.1-fips.1-tkg.1

vCenter Server 7.0 Update 3P

vCenter Server 8.0 U2b (for upgrade to vSphere 8.x VKr)

Supervisor 1.23, 1.24, 1.25

12/07/2023

VKr 1.26.10 vSphere 7.x (Ubuntu)

v1.26.10+vmware.1-fips.1-tkg.1.ubuntu

vCenter Server 7.0 Update 3P

vCenter Server 8.0 U2b (for upgrade to vSphere 8.x VKr)

Supervisor 1.23, 1.24, 1.25

12/07/2023

VKr 1.25.13 vSphere 7.x (Photon)

v1.25.13+vmware.1-fips.1-tkg.1

vCenter Server 7.0 Update 3P

vCenter Server 8.0 U2b (for upgrade to vSphere 8.x VKr)

Supervisor 1.23, 1.24, 1.25

12/07/2023

VKr 1.25.13 vSphere 7.x (Ubuntu)

v1.25.13+vmware.1-fips.1-tkg.1.ubuntu

vCenter Server 7.0 Update 3P

vCenter Server 8.0 U2b (for upgrade to vSphere 8.x VKr)

Supervisor 1.23, 1.24, 1.25

12/07/2023

VKr 1.24.11 vSphere 7.x (Photon)

v1.24.11+vmware.1-fips.1-tkg.1

vCenter Server 7.0 Update 3N

vCenter Server 8.0a (for upgrade to vSphere 8.x VKr)

Supervisor 1.22, 1.23, 1.24

7/13/2023

VKr 1.24.11 vSphere 7.x (Ubuntu)

v1.24.11+vmware.1-fips.1-tkg.1.ubuntu

vCenter Server 7.0 Update 3N

vCenter Server 8.0a (for upgrade to vSphere 8.x VKr)

Supervisor 1.22, 1.23, 1.24

7/13/2023

VKr 1.23.8 for vSphere 7.x (Photon)

v1.23.8---vmware.3-tkg.1

vCenter Server 7.0 Update 3F

vCenter Server 8.0a (for upgrade to vSphere 8.x VKr)

Supervisor 1.20, 1.21, 1.22

1/6/2023

VKr 1.23.8 for vSphere 7.x (Ubuntu)

v1.23.8---vmware.3-tkg.1.ubuntu

vCenter Server 7.0 Update 3L

vCenter Server 8.0a (for upgrade to vSphere 8.x VKr)

Supervisor 1.21, 1.22, 1.23

5/18/2023

VKr 1.22.9 for vSphere 7.x (Photon)

v1.22.9---vmware.1-tkg.1.cc71bc8

vCenter Server 7.0 Update 3E

vCenter Server 8.0a (for upgrade to vSphere 8.x VKr)

Supervisor 1.20, 1.21, 1.22

3/28/2022

VKr 1.22.9 for vSphere 7.x (Ubuntu)

v1.22.9---vmware.1-tkg.1

vCenter Server 7.0 Update 3L

vCenter Server 8.0a (for upgrade to vSphere 8.x VKr)

Supervisor 1.21, 1.22, 1.23

4/5/2023

VKr 1.21.6 for vSphere 7.x (Photon)

v1.21.6+vmware.1-tkg.1.b3d708a

vCenter Server 7.0 Update 3

vCenter Server 8.0a+ (for upgrade to vSphere 8.x VKr)

Supervisor 1.20, 1.21, 1.22

2/21/2022

VKr 1.21.6 for vSphere 7.x (Ubuntu)

v1.21.6---vmware.1-tkg.1

vCenter Server 7.0 Update 3

vCenter Server 8.0a (for upgrade to vSphere 8.x VKr)

Supervisor 1.20, 1.21, 1.22

3/4/2022

VKr 1.21.2 for vSphere 7.x (Photon)

v1.21.2---vmware.1-tkg.1.ee25d55

vCenter Server 7.0 Update 3

vCenter Server 8.0a (for upgrade to vSphere 8.x VKr)

Supervisor 1.20, 1.21, 1.22

11/16/2021

**Historical VKrs**

The table lists historical VKrs. The version number is the Kubernetes version delivered with that release. While these VKrs are compatible with the specified environment, they do not support the latest TKG functionality and are superseded by later releases. In addition, you cannot upgrade to vSphere 8 using these releases.

**VMware Tanzu Kubernetes release**

**Description**

v1.20.12+vmware.1-tkg.1.b9a42f3

Compatible with vSphere 7.0 Update 2 if you are using Supervisor Cluster version 1.18.10 and above.

v1.20.9+vmware.1-tkg.1.a4cee5b.900

Compatible with vSphere 7.0 Update 2 if you are using Supervisor Cluster version 1.18.10 and above.

ubuntu-2004-v1.20.8-vmware.1-tkg.2

Compatible with vSphere 7.0 Update 3 if you are using Supervisor Cluster version 1.21.0.

v1.20.7+vmware.1-tkg.1.7fb9067

Compatible with vSphere 7.0 Update 2 if you are using Supervisor Cluster version 1.18.10 and above.

v1.20.2+vmware.1-tkg.2.3e10706

Compatible with vSphere 7.0 Update 2 if you are using Supervisor Cluster version 1.18.10 and above.

For Kubernetes version 1.20.2, you might also see v1.20.2+vmware.1-tkg.1.1d4f79a listed when you run kubectl get tanzukubernetesreleases. However, this VMware Tanzu Kubernestes release is deprecated due to a CVE and you must not use it.

v1.19.16+vmware.1-tkg.1.df910e2

Compatible with vSphere 7.0 Update 2 if you are using Supervisor Cluster version 1.18.10 and above.

v1.19.14+vmware.1-tkg.1.8753786.9254

Compatible with vSphere 7.0 Update 2 if you are using Supervisor Cluster version 1.18.10 and above.

v1.19.11+vmware.1-tkg.1.9d9b236.866

Compatible with vSphere 7.0 Update 2 if you are using Supervisor Cluster version 1.18.10 and above.

v1.19.7+vmware.1-tkg.2.f52f85a

Compatible with vSphere 7.0 Update 2 if you are using Supervisor Cluster version 1.18.10 and above.

For Kubernetes version 1.19.7, you might also see v1.19.7+vmware.1-tkg.1.fc82c41 listed when you run kubectl get tanzukubernetesreleases. However, this VMware Tanzu Kubernestes release is deprecated due to a CVE and you must not use it.

v1.18.19+vmware.1-tkg.1.17af790

Compatible with vSphere 7.0 Update 1 and above.

v1.18.15+vmware.1-tkg.2.ebf6117

Compatible with vSphere 7.0 Update 1 and above.

For Kubernetes version 1.18.15, you might also see v1.18.15+vmware.1-tkg.1.600e412 listed when you run kubectl get tanzukubernetesreleases. However, this VMware Tanzu Kubernestes release is deprecated due to a CVE and you must not use it.

v1.18.10+vmware.1-tkg.1.3a6cd48.629

Compatible with vSphere 7.0 Update 1 and above.

v1.18.5+vmware.1-tkg.1.c40d30d

Compatible with vSphere 7.0 Update 1 and above.

v1.17.17+vmware.1-tkg.1.d44d45a

Compatible with vSphere 7.0 Update 1 and above.

v1.17.13+vmware.1-tkg.2.2c133ed

Compatible with vSphere 7.0 Update 1 and above.

v1.17.11+vmware.1-tkg.2.ad3d374

Compatible with vSphere 7.0 Update 1 and above.

v1.17.8+vmware.1-tkg.1.5417466

Compatible with vSphere 7.0 Update 1 and above.

v1.17.7+vmware.1-tkg.1.154236c

Compatible with vSphere 7.0 Update 1 and above.

Incompatible with Antrea CNI.

v1.16.14+vmware.1-tkg.1.ada4837

Compatible with vSphere 7.0 Update 1, but not recommended for use with vSphere 7.0 Update 2.

v1.16.12+vmware.1-tkg.1.da7afe7

Compatible with vSphere 7.0 Update 1, but not recommended for use with vSphere 7.0 Update 2.

Incompatible with Antrea CNI.

v1.16.8+vmware.1-tkg.3.60d2ffd

Incompatible with vSphere 7.0 Update 1 and above.

Incompatible with Antrea CNI.
