---
title: VMware vSphere Kubernetes Service 3.8 Release Notes
author: CA Inc
url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-service-administration-and-development/9-1/release-notes/vks-release-notes/vmware-tanzu-kubernetes-grid-service-38-release-notes.html
hostname: broadcom.com
sitename: CA INC
date: "2026-10-23"
fingerprint: "3e914b559aa1e790"
---
# VMware vSphere Kubernetes Service 3.8 Release Notes

This document contains the following sections

## About the vSphere Kubernetes Service 3.8 Release Notes

vSphere Kubernetes Service (VKS) provides components for provisioning and managing the lifecycle of Kubernetes clusters in the vSphere Supervisor environment.

These release notes provide details for each VKS release. Refer to the *Managing vSphere Kubernetes Service with vSphere Supervisor* documentation for usage information.

## Prerequisites for VKS 3.8 Upgrade

- 
  - 

Deploying the incorrect YAML configuration will result in image registry resolution failures.

To download VKS distribution image with VCFDT tool, specify --vcf-version 9.1 --component=SUPERVISOR\_SERVICE\_VKS --component-version=3.8.0+v1.37.

- 

## Deprecation Announcements

- - - - - - 

## Supervisor Upgrade Considerations for VKS 3.8

**Before upgrading to Supervisor 9.1, ensure all VKS clusters are using ClusterClass 3.6.0 or later.**Clusters on earlier ClusterClasses may experience system-initiated rolling updates, either as a result of the Supervisor 9.1 upgrade or due to subsequent configuration changes. See Understanding the Update Model for VKS Clusters for more information.

## vSphere Kubernetes Service 3.8.0+v1.37

## Release Snapshot

Name

Release Date

vSphere Kubernetes Service 3.8.0+v1.37

October 22 2026

## What's New

**Lifecycle and Upgrades**

- - - - 

**Configuration and Security**

- - - - - - - - - 

**Add-ons and Add-on Management**

- - - - - - - - 

**Networking**

- - 

## Fixed Issues

**Cluster upgrades and in-place updates on VKS 3.7 may fail when the MachineConfig CRD is missing.**

Following a vSphere Kubernetes Service (VKS) upgrade to the 3.7.x, in-place configuration updates or cluster upgrades may become stuck. This interruption in progress is caused by a missing MachineConfig CustomResourceDefinition (CRD).

This issue is fixed in VKS 3.8.0.

**Special Characters in osConfiguration.systemProxy.http\[s\] credentials cause systemd failures**

When credentials are encoded onto the URL for http/https proxies, special characters will result in percent-encoding (i.e: & becomes %26). % is treated as a special character by systemd and the resulting configuration file will be broken, preventing containerd from starting.

This issue is fixed in VKS 3.8.0.

**Configuring invalid node.labels values passes cluster validation but causes kubelet to crash at node startup.**

An invalid node.labels value (such as a kubernetes.io/ or k8s.io/ namespace label that kubelet does not recognize, like node-role.kubernetes.io/worker) passes cluster validation but causes kubelet to crash when nodes start up.

This issue is fixed in VKS 3.8.0 with validation for the node.labels ClusterClass variable.

**Add-on configuration fails when an optional dependency’s resource type is unavailable.**

An AddonConfig fails reconciliation when its definition references an optional dependency selected by labels and the dependency’s CustomResourceDefinition (CRD) is absent. The configuration reports DependencyListFailed, potentially with a no matches for kind error, and cannot complete despite the dependency being optional.

This issue is fixed in VKS 3.8.0.

**Retrieving add-on default values fails when schema defaults contain nested integers.**

Inspecting an available add-on’s default configuration can fail with a cannot deep copy int error when its schema contains integer defaults within arrays or objects. This prevents users from retrieving the affected add-on’s default configuration.

This issue is fixed in VKS 3.8.0.

**VKS cluster upgrades intermittently hang due to non-deterministic AddonRelease selection caused by orphaned resources.**

Workload cluster upgrades stall when multiple AddonReleases share a version due to undeleted, orphaned Antrea or Calico resources from previous Kubernetes releases. During an upgrade, the system non-deterministically selects the incorrect orphaned release, causing the upgrade process to hang.

This issue is fixed in VKS 3.8.0.

**Updating only the ClusterClass version can leave cluster nodes running an outdated machineadm binary.**

When you update only the ClusterClass, the cluster's KubeadmConfig spec sometimes doesn't change. In that case no node rollout happens, so the cluster is on the latest ClusterClass but its nodes still have an older machineadm binary. Newer VKS cluster variables depend on machineadm to reach the nodes. With a stale binary, those variables are either rejected with an error or silently dropped.

This issue is fixed in VKS 3.8.0.

**Enabling apiServerConfiguration.extraAuthentication on a cluster's API server breaks the cluster's default Pinniped-based login with a 401 error.**

When you configure extra authentication for your cluster's API server, you will be unable to access the cluster using kubectl. Any attempt to run a command using the default login flow such as running vcf cluster kubeconfig get followed by a kubectl command will fail during the credential exchange. You will see a direct client-side error stating could not complete Concierge credential exchange: ... Unauthorized. While this completely prevents new administrative logins via this path, any workloads already running on the cluster remain completely unaffected.

This issue is fixed in VKS 3.8.0.

**Rollout of Nodes When Using Harbor Supervisor Service with Custom Certificates**

When you use VKS alongside a Harbor Supervisor Service configured with a custom certificate, clusters on ClusterClasses builtin-generic-v3.2.0, builtin-generic-v3.3.0, or builtin-generic-v3.4.0 might undergo a node rollout after an upgrade. This rollout occurs because the ordering of trusted certificates is now deterministic, ensuring that subsequent cluster reconciliations by VKS always add the same certificate with a consistent ordering. This behavior is a one-time rollout, and existing clusters will not undergo automatic rollouts in the future. This issue is observed only when using a Harbor Supervisor version earlier than 2.11.2+vmware.1-tkg.2.

This issue is fixed in VKS 3.8.0.

## Known Issues

**Delay in realizing AddonRepositoryInstall if there is an unreachable OCI Helm Registry in any AddonRepositoryInstall.**

Reconciling an OCI Helm AddonRepositoryInstall that points to an unreachable endpoint causes delays for all subsequent AddonRepositoryInstall reconciliations, including accessible repositories.

Ensure all AddonRepository resources reference reachable internal registries rather than external endpoints that are blocked in your environment. If the controller is already stalled on an unreachable repository, delete the offending AddonRepositoryInstall, ensure AddonRepository references a reachable registry, and recreate AddonRepositoryInstall.

          **AIDEIntegrityCheckPassed condition remains stuck in False after removing unmanaged drift if a trusted MachineConfig change was applied concurrently.**

If unmanaged file-integrity drift occurs on a node and a trusted MachineConfig-managed update (such as an SSH banner change) is applied concurrently, resolving the drift file alone does not clear the AIDEIntegrityCheckPassed=False condition. The initial pre-check failure prevents the baseline database from updating, leaving the node flagged until it is manually re-baselined.

Workaround: Contact Broadcom Support for a workaround.

**Exceeding supported VKS workload cluster and Helm-based add-on scale thresholds causes add-on manager OOM crashes.**

Memory consumption for the add-on manager scales with the total number of VKS workload clusters and active Helm add-ons. In high-cluster topologies, exceeding supported add-on limits causes the add-on manager to run out of memory (OOM) and terminate. While the add-on workloads continue to run normally on the VKS workload clusters, the resulting add-on manager restarts disrupt reconciliation and cause ClusterAddon custom resources on the Supervisor to intermittently flap and report Ready: False.

Workaround:

Keep deployments within the verified scale boundaries per Supervisor based on your cluster inventory:

- Up to 300 clusters: Do not exceed 600 total Helm-based add-ons.
- Up to 500 clusters: Do not exceed 100 total Helm-based add-ons.

Also, when performing large rollouts, stagger add-on provisioning across clusters in smaller batches rather than dispatching them concurrently to avoid triggering sharp memory spikes.

          **AddonRepositoryInstall for private Helm registries fails authentication if no initialized VKS workload cluster exists on the Supervisor.**

The add-on manager processes credentials from ClusterRegistryConfig resources for Helm repositories only during VKS workload cluster reconciliation loops. On a Supervisor with zero initialized workload clusters, credentials are not loaded into the active runtime of the add-on manager. Consequently, AddonRepositoryInstall for private Helm registries fails with authentication errors during chart discovery, preventing the creation of Addon, AddonRelease, and AddonConfigDefinition (ACD) resources for the Helm charts and versions defined in the AddonRepository's spec.

Workaround: Provision at least one VKS workload cluster on the Supervisor. Once the workload cluster finishes initialization, the add-on manager synchronizes ClusterRegistryConfig credentials, allowing AddonRepositoryInstall to authenticate successfully on its next reconciliation retry.

**Provisioning clusters with more than 250 worker nodes and extra storage mounts may take longer than usual to complete.**

This can occur when many nodes are provisioned at the same time, as in a cluster of more than 250 workers, and the underlying storage is slow to respond. Preparing the extra volumes (for example, for /var/lib/containerd or /var/lib/kubelet) can take longer than the time the node allows for setup. Affected nodes don't complete their setup and stay in Provisioned with the message Waiting for a Node with spec.providerID… to exist. The cluster may show WorkerMachinesReady: Unknown and not all workers are available. The cluster eventually recovers without any intervention, and all workers become ready.No action is required, because the cluster reaches a healthy state on its own. To reduce the likelihood of the issue, scale large clusters up in smaller batches instead of creating all nodes at once.

Workaround: No action is required, because the cluster reaches a healthy state on its own. To reduce the likelihood of the issue, scale large clusters up in smaller batches instead of creating all nodes at once.

**In-place update eligible changes could lead to 2 extra spare nodes being created for a multi node control plane**

VKS supports in-place node configuration updates for a subset of configurations. For control plane availability, a spare node with updated configuration is created while existing nodes update in-place until replica counts match. On Clusters with KR version 1.37, in-place eligible changes may occasionally create 2 spare control plane nodes instead of 1. This non-deterministic behavior depends on node health, failure domains, and other factors, and users may not always observe this behavior.

This behavior is applicable to clusters using KR 1.37 and CC version builtin-generic-v3.8.0 only.

Workaround: There is no manual intervention necessary for this propagation. Even with the creation of 2 spare nodes, the cluster update should succeed successfully.

**Pre-existing Helm AddonRepositoryInstall (ARI) Reports Non-Ready Status Following VKS 3.8 Upgrades**

When upgrading a VKS cluster from version 3.7 to 3.8, the Helm AddonRepositoryInstall (ARI) custom resource may unexpectedly report a Non-Ready status. This occurs because VKS 3.8 begins cascading some of the Helm chart metadata fields to Addon objects that were not populated in VKS 3.7. Consequently, these affected Addons will continue to operate with their older 3.7 feature sets rather than fully utilizing the upgraded system's capabilities.

Workaround: Contact Broadcom Support for a workaround.

**Windows Workloads Experience Silent Network Failures Following Node Rollouts**

During a Windows post-upgrade node rollout after configuring a container registry in the Supervisor, an internal networking timeout can prevent a Pod’s network interface from being fully configured. Consequently, the affected Windows workloads lose all network connectivity and become completely unreachable via their LoadBalancer VIP. This outage is particularly difficult to detect because Kubernetes falsely reports the impacted Pods as healthy and Running with populated endpoints. Affected Pods will not automatically recover on their own and must be manually recreated to restore application access.

Workaround: Delete the affected Pod. The Deployment recreates it, and once the node is no longer under rollout load the adapter is created within the timeout and connectivity is restored.

**Installing the Secret Store Supervisor Service on a Supervisor that hosts or will host VKS clusters with Windows nodes causes those clusters to enter an Add-on Reconcile Failed state.**

The vault-injector *ClusterAddon* on affected Windows-node clusters shows *Reconciled: False / Ready: False*, with the deployment failing to roll out. The vault-injector addon deployed by the Secret Store Supervisor Service does not currently support Windows nodes, so the pod cannot come up on clusters with Windows worker nodes, and the addon reconciliation times out. This is not limited to newly created clusters — existing Windows-node clusters are also affected once the service is installed.

Workaround: For the affected cluster, run the following command to opt out: *kubectl label cluster -n vault-injector.kubernetes.vmware.com/install=false --overwrite* This automatically removes *clusteraddon* from the namespace. To confirm, run the following command: *kubectl -n get clusteraddon | grep "vault-injector"*

**VKS cluster rollouts stall indefinitely when bootstrapping failure leaves the machine without a nodeRef**

This issue occurs during a rollout when a new machine fails to bootstrap (specifically, failing to join the cluster and thus missing a nodeRef). Eventually, this machine is marked for remediation according to the configured health check conditions. Because the machine is part of an in-place update process, the controller attempts to move the machine to a new revision rather than simply deleting it. However, because the move mechanism requires a valid nodeRef to proceed, and standard deletion is disabled for machines pending an in-place update, the controller enters a deadlock. It cannot update, move, or delete the machine, causing the rollout to stall indefinitely.

Workaround: Contact Broadcom Support for a resolution.

**Automatic Control Plane Rollout When Using Custom ClusterClass After Upgrading to VKS v3.5 and Later**

Existing VKS clusters created with a custom ClusterClass (CC) that uses the builtin-generic-v3.4.0 class experience an automatic rollout of their control plane nodes after an upgrade to VKS 3.5.0 or later.

This unscheduled rollout affects only the control plane nodes; workloads running on the cluster remain unaffected.

Workaround: No workaround is available for this issue because it stems from an incorrect inference of the base version of the custom ClusterClass (in this case, 3.4.0).

**Mixed-OS Clusters That Use Cilium CNI Fail to Reach a Ready State**

When you deploy a VKS cluster with mixed worker nodes (Windows OS and Photon OS), the Windows worker nodes remain in a Not Ready state. This issue occurs because the Cilium Container Network Interface (CNI) does not provide support for Windows operating systems.

Workaround: If your workloads require Windows worker nodes, use a different supported CNI. If you must use the Cilium CNI, provision the cluster exclusively with supported Linux worker nodes, such as Photon OS.

**VKS Cluster Creation with OIDC Configuration Fails When Initiated from the VCFA UI**

When you attempt to provision a VKS cluster with OIDC authentication via the VCFA UI, the cluster creation process fails. This issue blocks administrators from using the graphical interface to configure OIDC for the Kubernetes API server.

The UI generates an improperly formatted cluster YAML file during the submission process. Specifically, it incorrectly populates the audiences field under apiServerConfiguration.extraAuthentication.jwt.issuer as a single string, rather than the required YAML list or array format.

Workaround:

The issue is fixed in VCF 9.1.1.0100, upgrade to resolve.

If you are using VCF 9.1.1.0 or below: To successfully provision a VKS cluster with OIDC configuration, bypass the UI and use the CLI or API to submit the cluster deployment. Ensure that the audiences field in your payload is formatted as a list:

issuer: audiences: - 0oay8xwjv1A2Qrbst697 url: https://integrator-8865151.okta.com/oauth2/default
