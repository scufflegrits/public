---
title: Red Hat Virtualization Life Cycle - Red Hat Customer Portal
url: https://access.redhat.com/support/policy/updates/rhev
hostname: redhat.com
description: "Red Hat offers support services for five years for each major release of Red Hat Virtualization throughout two main Production Support phases: Full Support and Maintenance Support."
sitename: Red Hat Customer Portal
date: "2011-06-03"
fingerprint: b775d84688a3ab5f
---
# Red Hat Virtualization Life Cycle

## Overview

Red Hat Virtualization is comprised of two operational components:

- Red Hat Virtualization Manager (RHV-M), which provides a centralized management platform for a virtualized environment
- Red Hat Virtualization Hypervisor (RHV-H), which provides the hypervisor for a cluster of virtual machines

Red Hat has offered support services for five years for each major release of Red Hat Virtualization. After 5 years of Production Support, Red Hat Virtualization support has 2 years of Extended Life Phase support, which is described later in this document.

This policy has been in effect for major releases and applies to the latest released minor version of the product. For example, when Red Hat Virtualization 4 was released in August, 2016, the version 4 series then became a fully supported major version of the product. When Red Hat Virtualization 4.4 was released in August, 2020, version 4.4 then became the fully supported product version with the earlier versions of 4.x still supported for production use, but no longer receiving back ports or feature enhancements.

Red Hat retains the right to evaluate and adjust the support policy, duration and terms of the Red Hat Virtualization product life cycle phases for any current or planned releases and versions of the product.

With the release of RHV 4.4 Red Hat continues to invest in and support customers with a production-ready virtualization portfolio. The latest addition to this portfolio is OpenShift with OpenShift Virtualization, which provides continuity and roadmap delivery for the KVM-based virtualization stack currently managed by RHV. Moving forward the RHV management feature set will be converged with OpenShift and OpenShift Virtualization providing customers with requirements for containers and VMs a migration path and a common platform for deploying and managing both.

## Details

Red Hat Virtualization Production Support services will be provided as per the Scope of Coverage policies defined for Red Hat products.

The Red Hat Virtualization Product Support Life Cycle Phases are described here:

|  | Red Hat Product Life Cycle Phase Descriptions |  |  |  | 
|---|---|---|---|---|
| Description | Full Support | Extended Update Support (for eligible versions) <sup>5</sup> | Maintenance Support <sup>5</sup> | Extended Life Phase Support | 
| Access to previously released content through the Red Hat Customer Portal | Yes | Yes | Yes | Yes | 
| Self Help through the Red Hat Customer Portal | Yes | Yes | Yes | Yes | 
| Technical Support <sup>1</sup> | Unlimited | Unlimited | Unlimited | Limited and Upgrade assistance <sup>6</sup> | 
| Asynchronous Security Errata (RHSA) | Yes | Yes | Yes | No | 
| Asynchronous Bug Fix Errata (RHBA) <sup>2</sup> | Yes | Yes <sup>3</sup> | Yes | No | 
| Minor Releases | Yes | No | No | No | 
| Refreshed Hardware Enhancements <sup>4</sup> | Yes | No | Yes <sup>4</sup> | No | 
| Feature Backports, Enhancements | Yes | No <sup>3</sup> | No | No | 

1. Technical Support depends on the service level included in your Red Hat Virtualization subscription agreement.
2. Red Hat may choose, as an intermediate measure, to address serious issues that have an impact to customer business with a hotfix, while a Red Hat Bug Fix Advisory is created and verified.
3. While in EUS phase, feature and/or bug backports might be provided at the discretion of Red Hat.
4. Native Hardware Enablement (in Full Support phase) is provided by backporting hardware drivers, etc., to the relevant version of the Red Hat Virtualization Hypervisor. During the Maintenance Phase, it is limited to hardware enablement that does not require substantial software changes.
5. EUS / Maintenance Support is only for the Hypervisor (RHV-H). The customer needs to use the latest version of the Manager (RHV-M) to get support.
6. Check below to learn how the product is supported during the Extended Life Phase.

## Life Cycle Dates

The Red Hat Virtualization Product Support Life Cycle dates are described here:

**Note:** EUS is available for all customers for all EUS Supported versions (4.2 and 4.3).

## Red Hat Virtualization Life Cycle

### Full Support Phase:

During the Full Support Phase, qualified Critical and Important Security Advisories (RHSAs) will be released as they become available. Urgent and selected High Priority Bug Fix Advisories (RHBAs) will be released as they become available; all other available fix and qualified patches may be released via periodic updates.

If available, new or improved hardware enablement, may be provided at the discretion of Red Hat and are generally provided in minor releases. Hardware enablement that does not require substantial software changes may be provided independently from minor releases at Red Hat’s discretion.

For any minor release made available during this phase, the available and qualified errata advisories (RHSAs, RHBAs, and RHEAs) will be cumulatively included with the contents of previously released product updates. This means that if a customer is running an older version of the product and reports a bug, that bug will be fixed in the latest version of the software and a customer may need to upgrade in order to take advantage of that fix.

### Extended Update Support:

Beginning with Red Hat Virtualization 4.2, Red Hat provides Extended Update Support (EUS) which provides customers an added 1 year of support, for the minor version they are running. For example, customers running version 4.2 will continue to have access to fixes for a full 2 years, even with the release of version 4.3.

**Note:**

- EUS is available for select Red Hat Virtualization 4.2 and higher versions only.
- EUS is available only for the Hypervisor (RHV-H) and not for the Manager (RHV-M).
- EUS is not available for IBM Power architecture.
- EUS feature backports are provided at the discretion of Red Hat.

### Maintenance Support Phase:

During the Maintenance Support Phase, qualified Critical and Important Security Security Advisories (RHSAs) will be released as they become available. Urgent and Selected High Priority Bug Fix Advisories (RHBAs) may be released as they become available. Other Bug Fix (and Enhancement (RHEA) Advisories may be released at Red Hat’s discretion, but should not be expected.

If available, hardware enablement that does not require substantial software changes may be provided at the discretion of Red Hat, generally in minor releases. New software functionality is not available during this phase.

New features or enhancements will not be provided.

### Extended Life Phase (ELP):

During the Extended Life Phase, a Red Hat Virtualization Manager subscription provides continued access to previously released content on the Red Hat Customer Portal, as well as other content such as documentation and the Red Hat Knowledgebase.

For versions of products in the Extended Life Phase, Red Hat will provide limited ongoing technical support. No bug fixes, security fixes, hardware enablement or root-cause analysis will be available during this phase, and support will be provided on existing installations only. Advice for migrating to currently supported Red Hat Virtualization versions may also be provided.

Red Hat reserves the right to terminate the ongoing support in the Extended Life Phase for a particular version of Red Hat Virtualization at any time.
**Note:** Support for Extended Life Phase is provided only for the latest minor release of the product (example 4.1.z where z stands for the latest version).

### Upgrade Policy for Major Releases:

Red Hat will provide a supported upgrade path between major releases for Red Hat Virtualization Manager. Upgrades will be supported between the latest minor release of previous version to the most current version of the next higher major release. In these cases, the upgrade process will be limited to support upgrading from the latest minor release of the previous version to the new major version.

For Example:

- Upgrading from Red Hat Enterprise Virtualization 3.6.11 to Red Hat Virtualization 4.0 is supported, with 3.6.11 being the most current release of the 3 Series of minor releases.
- Upgrade from Red Hat Enterprise Virtualization 3.5 to Red Hat Virtualization 4.0 is not supported. In order to achieve this upgrade, the customer should first upgrade to Red Hat Enterprise Virtualization 3.6.11, before the upgrade to Red Hat Virtualization 4.0.

Upgrade from Beta / Pre-release or Upstream releases to a fully supported release is not supported.

### Upgrade Policy for Minor Releases:

Customers are expected to update to new minor and z-stream releases as and when they become available. Accelerated fixes will not be provided for issues that have been previously fixed in a subsequent release; customers are expected and encouraged to keep their systems current and upgraded to the latest version of product to keep up to date on all patches and fixes.

In circumstances where the reported issue is not fixed in the current shipping release, the customer is still expected to upgrade their systems to the latest release (n) or in some exceptional cases, the immediate previous release (n-1). This is to ensure that any fixes are developed and verified against the latest or the immediate previous release.

### Security Updates:

Throughout the support lifecycle, qualified security issues of Critical or Important impact, as well as select mission-critical bugs, will be addressed by updated packages. For more information on how the impact of security issues is assessed, please refer to Issue Severity Classification.

### Delivery of Red Hat Virtualization Advisories:

Software changes to Red Hat Virtualization are delivered through individual updates known as errata advisories. These advisories are delivered through the Red Hat Customer Portal or through other authorized portals. Errata advisories can be released individually on an as-needed basis or aggregated and distributed as a minor release.

Errata advisories may contain security fixes (Red Hat Security Advisories or RHSAs), bug fixes (Red Hat Bug Fix Advisories or RHBAs), or feature enhancements (Red Hat Enhancement Advisories or RHEAs). All errata advisories are tested and qualified against the respective, active Red Hat Virtualization major release. For example, a Red Hat Virtualization 4 RHSA will be applied cumulatively to the latest Red Hat Virtualization 4 version and patch set.

All released errata advisories remain accessible to active subscribers for the entire Red Hat Virtualization life cycle. Within each major release of Red Hat Virtualization any errata advisory (including one released as part of a minor release) will be applied cumulatively to the latest release of Red Hat Virtualization, including any patch sets for advisories released after the version currently used by the customer.

Red Hat actively develops only the last major version’s minor release (for example a bug found in Red Hat Enterprise Virtualization 3.6 or Red Hat Virtualization 4.0 after the release of Red Hat Virtualization 4.1 could only be fixed in an errata to a 4.1.z release). Errata advisories or hotfixes for earlier releases are provided at the discretion of Red Hat to address critical impact security issues with a significant customer business impact.

During the life cycle of a major release Red Hat makes commercially reasonable efforts to maintain binary compatibility for the core runtime environment across all minor releases and errata advisories. If necessary, Red Hat may make exceptions to this compatibility goal for critical impact security issues or other significant issues.

## Red Hat Virtualization Manager Compatibility

Red Hat Virtualization uses the concept of Compatibility Level to describe the functionality and compatibility of the virtual environment.

Each minor version of Red Hat Virtualization delivers a new Compatibility Level based on the minor version number. Each release of Red Hat Virtualization Manager supports at least the current and previous minor release Compatibility Level.

The following table outlines the Data Center/Cluster Compatibility levels supported by Red Hat Virtualization Manager.

| Red Hat Virtualization Manager Compatibility Matrix |  |  | 
|---|---|---|
| RHV Release | Release Date | RHVH Supported Compatibility Levels | 
| 2.1 | November 3rd, 2009 | 2.1 | 
| 2.2 | June 23rd, 2010 | 2.2, 2.1 | 
| 3.0 | January 18th, 2012 | 3.0, 2.2 | 
| 3.1 | December 5th, 2012 | 3.1, 3.0 | 
| 3.2 | June 11th, 2013 | 3.2, 3.1, 3.0 | 
| 3.3 | January 21st, 2014 | 3.3, 3.2, 3.1, 3.0 | 
| 3.4 | June 16th, 2014 | 3.4, 3.3, 3.2, 3.1, 3.0 | 
| 3.5 | Februrary 11th, 2015 | 3.5, 3.4, 3.3 | 
| 3.6 | March 9th, 2016 | 3.6, 3.5, 3.4 | 
| 4.0 | August, 2016 | 4.0, 3.6 | 
| 4.1 | April 18th, 2017 | 4.1, 4.0, 3.6 | 
| 4.2 | May 15th, 2018 | 4.2, 4.1, 4.0, 3.6 | 
| 4.3 | May 8th, 2019 | 4.3, 4.2, 4.1 | 
| 4.4 | August 4th, 2020 | 4.7, 4.6, 4.5, 4.4, 4.3, 4.2 | 

## Red Hat Virtualization Tested Configurations

Red Hat highly recommends the use of tested configurations. The Package Manifest, accessible in the documentation section of the Red Hat customer portal, contains a list of tested packages. We highly recommend that production Red Hat Virtualization environments use tested configurations unless otherwise advised by Red Hat Support.

## Red Hat Hypervisor Upgrade and Support Policy

Red Hat will provide a supported upgrade path for all hypervisors within the same major release. Upgrading hypervisors from one major release to another major release is not supported. Red Hat will attempt to provide migration paths between major releases at its discretion.

The following table outlines the compatibility levels supported by the Red Hat Virtualization Hypervisor and by the corresponding Red Hat Enterprise Linux release with the appropriate management agent installed.

| Red Hat Virtualization Hypervisor |  |  | 
|---|---|---|
| Red Hat Virtualization Hypervisor | Red Hat Enterprise Linux Release | Supported RHVH Compatibility Levels | 
| RHEV-H 3.6 | 7.3 | 3.6, 3.5 | 
| RHEV-H 3.6\* | 7.3 EUS\* | 3.6, 3.5 | 
| RHVH 4.0 | 7.3 | 4.0, 3.6 | 
| RHVH 4.1 | 7.5 | 4.1, 4.0, 3.6 | 
| RHVH 4.2 | 7.5, 7.6 | 4.2, 4.1, 4.0, 3.6 | 
| RHVH 4.3 | 7.6, 7.7 <sup>1</sup>, 7.8<sup>2</sup>, 7.9<sup>3</sup> | 4.3, 4.2, 4.1 | 
| RHVH 4.4 | 8.2, 8.3 <sup>4</sup>, RHEL AV 8.3.1<sup>5</sup>, 8.4<sup>6</sup>, 8.5<sup>7</sup>, 8.6 <sup>8</sup> | 4.7 <sup>8</sup>, 4.6<sup>6</sup>, 4.5<sup>4</sup>, 4.4 | 

\* Red Hat Virtualization 3.6 Extended Lifecycle Support only

<sup>1</sup> Supported with RHV 4.3.5 and above only.

<sup>2</sup>Supported with RHV 4.3.9 and above only.

<sup>3</sup>Supported with RHV 4.3.11 and above only.

<sup>4</sup>Supported with RHV 4.4.3 and above only.

<sup>5</sup>RHEL AV 8.3.1 is supported with RHV 4.4.4-2 Update

<sup>6</sup>Supported with RHV 4.4.6

<sup>7</sup>Supported with RHV 4.4.9

<sup>8</sup>Supported with RHV 4.4 SP1
