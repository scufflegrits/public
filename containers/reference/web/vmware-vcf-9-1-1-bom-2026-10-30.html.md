---
title: Bill of Materials 9.1.1
author: CA Inc
url: https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-1/release-notes/vmware-cloud-foundation-9-1-1-0-release-notes/vmware-cloud-foundation-9-1-1-0-bill-of-material.html
hostname: broadcom.com
sitename: CA INC
date: "2026-10-29"
fingerprint: f0ecb9c4d9eec69f
---
# Bill of Materials 9.1.1

This document contains the following sections

## Bill of Materials (BOM)

VMware Cloud Foundation (VCF) is comprised of the following components listed in the Bill of Materials (BOM) table. The components in the BOM are interoperable and compatible. You can select which components to apply in your deployment based on the impact to your environment and operational costs. The Broadcom Support Portal allows you to download the appropriate set of bits based on your entitlement.

VMware Cloud Foundation Component

vSphere Foundation Component

Version

Build Number

VCF Installer/ SDDC Manager

Yes (VCF Installer only)

9.1.1.0

25713928

ESX

Yes

9.1.1.0

25714478

vCenter

Yes

9.1.1.0

25712839

vSAN ESA Witness

Yes

9.1.1.0

25714474

vSAN File Services \*

Yes

9.1.1.0200

25846901

vSAN OSA Witness

Yes

9.1.1.0

25714473

NSX

\-

9.1.1.0

25691509

VCF Operations

Yes

9.1.1.0

25679751

Cloud proxy

Yes

9.1.1.0

25679891

License server

Yes

9.1.1.0

25679819

VCF Operations for networks

\-

9.1.1.0

25682214

VCF Operations HCX

\-

9.1.1.0

25690219

VCF Operations orchestrator

Yes

9.1.1.0

25679883

VCF Automation

\-

9.1.1.0

25714559

Supervisor

Yes

9.1.1.0

25714555

VKS Add-ons (former VKS Standard Packages)

Yes

3.7.0+20260618

25497365

vSphere Kubernetes releases

Yes

1.34.2+vmware.2-vkr.2

N/A

Fleet lifecycle

Yes

9.1.1.0

25713934

Identity broker

\-

9.1.1.0

25679886

Log management

Yes

9.1.1.0

25679624

Real-time metrics

\-

9.1.1.0

25679622

Real-time metrics store

\-

9.1.1.0

25714471

Salt RaaS

\-

9.1.1.0

25679895

Salt master

\-

9.1.1.0

25679895

SDDC lifecycle

Yes

9.1.1.0

25713940

Software depot

Yes

9.1.1.0

25713941

Telemetry

Yes

9.1.1.0

25671600

VCF services runtime

Yes

9.1.1.0

25714471

VCF download tool

Yes

9.1.1.0

25713929

VCF Consumption CLI

Yes

9.1.1.0

25662425

VCF Consumption CLI Plugins & Database

Yes

9.1.1.0

25665404

\*vSAN File Services 9.1.1.0200 substitutes all previous 9.1.x releases of vSAN File Services.

**Supervisor Services**

VMware Cloud Foundation Component

vSphere Foundation Component

Version

Build Number

VMware vSphere Kubernetes Service

Yes

3.7.0+v1.36

N/A

Harbor (Supervisor service)

Yes

2.15.2+vmware.1-vks.1

25639075

CA Cluster issuer (Supervisor service)

Yes

9.1.1.0

25662423

Contour (Supervisor service)

Yes

1.33.5

25639301

External DNS (Supervisor service)

Yes

0.21.0+vmware.2-vks.1

25639209

ArgoCD (Supervisor service)

\-

1.2.0

25642124

VKSM Auto-attach

\-

9.1.1.0

25714559

Supervisor Management Proxy

Yes

9.1.1.0

25665478

VMware vSphere Supervisor LCI

Yes

9.1.2

25714560

**VCF Services**

VMware Cloud Foundation Component

Included in VCF SKU

Version

Build Number

Migration service engine (VCF service)

Yes

9.1.1.0

25714559

Migration Service (VCF service)

Yes

9.1.1.0

25714559

ArgoCD (VCF service)

Yes

1.2.0

25642124

Configuration Service (VCF service)

Yes

9.1.1.0

25670523

Data Services (VCF service)

Add-on

9.1.1.0

25651575

Encryption Management (VCF service)

Yes

9.1.1.0

25714559

Metrics Aggregator (VCF service)

Yes

9.1.1.0

25665407

Protection and Recovery (VCF service)

Add-on

9.1.1.0

25691510

Harbor (VCF service)

Yes

9.1.1.0

25714559

Secret Store (VCF service)

Yes

9.1.1.0

25710217

The following VMware Cloud Foundation add-ons are interoperable with the components from the VCF BOM above:

VMware Cloud Foundation Add-on

VMware vSphere Foundation Component

Version

Build Number

## Dependencies

- The Product Interoperability Matrix provides the upgrade order dependencies.
- The functionality of VMware Private AI Foundation with NVIDIA is delivered as a combination of components. The following components are now all part of the VCF software:
  - Guided deployment workflow in the vSphere Client
  - AI catalog items in VCF Automation
  - VMware Deep Learning VM 9.1.1.0For more information about VMware Deep Learning VM image releases, see the VMware Deep Learning VM Release Notes.
  - Private AI Services 3.0For more information about Private AI Services releases, see the VMware Private AI Services Release Notes.
- Third-party products from the VCF ecosystem maintain their existing dependencies at the component level. For example, OEM driver add-ons, ESX device drivers, and UI plugins.
- VCF versioning is not applicable to any component with external dependency for the version, such as the Kubernetes version.
- Clusters that don’t have active VMware Supervisor are supported, but do not support key capabilities of VCF, such as VCF Automation workflows.
