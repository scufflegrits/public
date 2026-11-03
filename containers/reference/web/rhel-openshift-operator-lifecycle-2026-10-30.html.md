---
title: OpenShift Operator Life Cycles - Red Hat Customer Portal
url: https://access.redhat.com/support/policy/updates/openshift_operators
hostname: redhat.com
description: OpenShift Operator Life Cycles
sitename: Red Hat Customer Portal
date: "2026-07-09"
fingerprint: "45e35c975e839441"
---
# OpenShift Operator Life Cycles

This document outlines and describes software maintenance Life Cycle classifications which are being introduced for Operators shipped by Red Hat for use with OpenShift Container Platform.


- **Note**: When reviewing your operator usage, you should review it in context with the appropriate Red Hat OpenShift cluster version life cycle you are running, using the Red Hat Life Cycles App, to see all the appropriate life cycle information in one place.

OpenShift Operators bring additional functionality and extend the capabilities of an OpenShift cluster. Red Hat provides a large number of Operators through the OpenShift OperatorHub, entitled and supported per their corresponding product offering. Each offering and subsequent Operator, may be subject to its own release cadence and maintenance life cycle. With the installation of each Operator, cluster administrators should be aware of their corresponding life cycle, ensuring support boundaries are understood and adhered to.

Red Hat is simplifying this task with the introduction of three new maintenance Life Cycle classifications; Platform Aligned, Platform Agnostic and Rolling Stream. Each of these outline criteria in the form of minimum capability and support timeline an Operator should meet. This is in effect starting with OpenShift 4.14 or newer. Operator version lines not available on OCP 4.14 or newer do not fall into this categorization.

## Product Aligned

## Platform Aligned

## Platform Agnostic

Information on update channels for OpenShift Operators can be found on the Operator Update Information Checker application.

# Product Aligned Operators

The following Products make Operators available for installation/integration with the underlying OpenShift Container Platform and maintain their own independent life cycles. These operators are **not listed** in the Platform Aligned, Platform Agnostic, or Rolling Stream tables below. For lifecycle dates, OCP compatibility, and support terms, refer to the linked product lifecycle page.

## JBoss Middleware

## 6 operators

- Red Hat 3scale API Management
- Red Hat 3scale APIcast Operator
- Red Hat Data Grid
- Red Hat JBoss Enterprise Application Platform
- Red Hat JBoss Web Server
- Red Hat Service Interconnect

## Red Hat OpenStack Services on OpenShift

## 20 operators

- OpenStack Operator
- OpenStack AnsibleEE Operator
- OpenStack Baremetal Operator
- Barbican Operator
- Cinder Operator
- Designate Operator
- Glance Operator
- Heat Operator
- Horizon Operator
- Infra Operator
- Ironic Operator
- Keystone Operator
- Manila Operator
- Neutron Operator
- Nova Operator
- Octavia Operator
- OVN Operator
- Placement Operator
- Swift Operator
- Test Operator

# Platform Aligned Operators

The following operators are released and maintained closely bound to the support lifecycle of the underlying OpenShift Container Platform (OCP) cluster.

Released as part of, or within 1 month of the new OCP minor version the operator aligns with, the operator shares the same boundaries of full support and maintenance support phases. While operators in this category will still be compatible with older OCP versions, cluster administrators can expect support duration through the aligned OCP cluster version, and remain on a given minor version branch of the operator, enabling simplified validation and upgrade strategies. Customers are still expected to apply patches to the operator to receive the newest bug fix and security advisories.

#### Red Hat OpenShift Data Foundation

| Version | Tier | Supported OpenShift versions | OpenShift Aligned Version | General availability | Full support ends | Maintenance ends | EUS ends | EUS Term 2 ends | EUS Term 3 ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 4.22 | Platform Aligned | 4.22 | 4.22 | 09 Jul 2026 | 11 Feb 2027 | 31 Dec 2027 | 30 Jun 2028 | 30 Jun 2029 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.21 | Platform Aligned | 4.21, 4.22 | 4.21 | 09 Mar 2026 | 09 Oct 2026 | 23 Aug 2027 | N/A | N/A | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.20 | Platform Aligned | 4.20, 4.21 | 4.20 | 18 Nov 2025 | 09 Jun 2026 | 21 Apr 2027 | 21 Oct 2027 | 21 Oct 2028 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.19 | Platform Aligned | 4.19, 4.20 | 4.19 | 28 Jul 2025 | 18 Feb 2026 | 17 Dec 2026 | N/A | N/A | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.18 | Platform Aligned | 4.18, 4.19 | 4.18 | 11 Mar 2025 | 28 Oct 2025 | 25 Aug 2026 | 25 Feb 2027 | 25 Feb 2028 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.16 | Platform Aligned | 4.16, 4.17 | 4.16 | 17 Jul 2024 | 30 Jan 2025 | 27 Dec 2025 | 27 Jun 2026 | 27 Jun 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.14 | Platform Aligned | 4.15, 4.14 | 4.14 | 08 Nov 2023 | 18 Jun 2024 | 01 May 2025 | 31 Oct 2025 | 31 Oct 2026 | 31 Oct 2027 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (14)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 4.17 | Platform Aligned | 4.17, 4.18 | 4.17 | 30 Oct 2024 | 11 Jun 2025 | 01 Apr 2026 | N/A | N/A | N/A | 
| 4.15 | Platform Aligned | 4.15, 4.16 | 4.15 | 19 Mar 2024 | 16 Oct 2024 | 27 Aug 2025 | N/A | N/A | N/A | 
| 4.13 | N/A | 4.13, 4.14 | 4.13 | 21 Jun 2023 | 08 Feb 2024 | 17 Nov 2024 | N/A | N/A | N/A | 
| 4.12 | N/A | 4.12, 4.13 | 4.12 | 31 Jan 2023 | 21 Sep 2023 | 17 Jul 2024 | 17 Jan 2025 | N/A | N/A | 
| 4.11 | N/A | 4.11, 4.12 | 4.11 | 24 Aug 2022 | 30 Apr 2023 | 10 Feb 2024 | N/A | N/A | N/A | 
| 4.10 | N/A | 4.10, 4.11 | 4.10 | 13 Apr 2022 | 24 Nov 2022 | 10 Sep 2023 | N/A | N/A | N/A | 
| 4.9 | N/A | 4.9, 4.10 | 4.9 | 13 Dec 2021 | 13 Jun 2022 | 13 Jun 2023 | N/A | N/A | N/A | 
| 4.8 | N/A | 4.8, 4.9 | 4.8 | 03 Aug 2021 | 03 Feb 2022 | 27 Apr 2023 | N/A | N/A | N/A | 
| 4.7 | N/A | 4.7, 4.8 | 4.7 | 19 May 2021 | 19 Nov 2021 | 19 Nov 2022 | N/A | N/A | N/A | 
| 4.6 | N/A | 4.5, 4.6, 4.7 | 4.6 | 17 Dec 2020 | 19 Jun 2021 | 17 Dec 2022 | N/A | N/A | N/A | 
| 4.5 | N/A | 4.4, 4.5, 4.6 | 4.5 | 15 Sep 2020 | 17 Jan 2021 | 03 Aug 2021 | N/A | N/A | N/A | 
| 4.4 | N/A | 4.3, 4.4, 4.5 | 4.4 | 04 Jun 2020 | 15 Oct 2020 | 19 May 2021 | N/A | N/A | N/A | 
| 4.3 | N/A | 4.2, 4.3, 4.4 | 4.3 | 14 Apr 2020 | 04 Jul 2020 | 17 Dec 2020 | N/A | N/A | N/A | 
| 4.2 | N/A | 4.2, 4.3 | 4.2 | 14 Jan 2020 | 14 May 2020 | 15 Sep 2020 | N/A | N/A | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**4 months

**Valid Subscriptions:**OpenShift Platform Plus / OpenShift Data Foundation Essentials / OpenShift Data Foundation Advanced

**Operators sharing this lifecycle:**

- OpenShift Data Foundation (odf-operator) — Update Info
- ODF Multicluster Orchestrator (odf-multicluster-orchestrator) — Update Info
- OpenShift Data Foundation Client (ocs-client-operator) — Update Info
- Openshift DR Cluster Operator (odr-cluster-operator) — Update Info
- Openshift DR Hub Operator (odr-hub-operator) — Update Info
- cephcsi-operator (cephcsi-operator) — Update Info
- mcg-operator (mcg-operator) — Update Info
- ocs-operator (ocs-operator) — Update Info
- odf-csi-addons-operator (odf-csi-addons-operator) — Update Info
- odf-dependencies (odf-dependencies) — Update Info
- odf-prometheus-operator (odf-prometheus-operator) — Update Info
- recipe (recipe) — Update Info
- rook-ceph-operator (rook-ceph-operator) — Update Info

#### Red Hat Advanced Cluster Management for Kubernetes

| Version | Tier | Supported OpenShift versions | OpenShift Aligned Version | General availability | Full support ends | Maintenance ends | EUS ends | EUS Term 2 ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2.17 | Platform Aligned | 4.20, 4.21, 4.22 | 4.22 | 18 Jun 2026 | 24 Jul 2027 | 15 Dec 2027 | 27 May 2028 | 29 May 2029 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 2.16 | Platform Aligned | 4.19, 4.20, 4.21, 4.22 | 4.21 | 10 Mar 2026 | 09 Apr 2027 | 10 Sep 2027 | N/A | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 2.15 | Platform Aligned | 4.18, 4.19, 4.20, 4.21 | 4.20 | 03 Dec 2025 | 08 Jan 2027 | 01 Jun 2027 | 12 Nov 2027 | 13 Nov 2028 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 2.14 | Platform Aligned | 4.17, 4.18, 4.19, 4.20 | 4.19 | 01 Aug 2025 | 02 Oct 2026 | 24 Feb 2027 | N/A | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 2.13 | Platform Aligned | 4.16, 4.17, 4.18, 4.19 | 4.18 | 20 Mar 2025 | 17 Apr 2026 | 18 Sep 2026 | 12 Feb 2027 | 13 Feb 2028 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 2.11 | Platform Aligned | 4.14, 4.15, 4.16, 4.17 | 4.16 | 18 Jul 2024 | 15 Aug 2025 | 16 Jan 2026 | 12 Jun 2026 | 11 Jun 2027 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (12)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 2.12 | Platform Aligned | 4.15, 4.16, 4.17, 4.18 | 4.17 | 06 Nov 2024 | 15 Jan 2026 | 09 Jun 2026 | N/A | N/A | 
| 2.10 | N/A | 4.13, 4.14, 4.15, 4.16 | 4.15 | 21 Mar 2024 | 22 Oct 2024 | 23 Sep 2025 | N/A | N/A | 
| 2.9 | N/A | 4.12, 4.13, 4.14, 4.15 | N/A | 15 Nov 2023 | 16 Jul 2024 | 17 Jun 2025 | N/A | N/A | 
| 2.8 | N/A | 4.11, 4.12, 4.13, 4.14 | N/A | 08 Jun 2023 | 09 Jul 2024 | 10 Dec 2024 | N/A | N/A | 
| 2.7 | N/A | 4.10, 4.11, 4.12, 4.13 | N/A | 06 Feb 2023 | 07 Mar 2024 | 16 Aug 2024 | N/A | N/A | 
| 2.6 | N/A | 4.9, 4.10, 4.11, 4.12 | N/A | 29 Aug 2022 | 11 Sep 2023 | 13 Dec 2023 | N/A | N/A | 
| 2.5 | N/A | N/A | N/A | 08 Jun 2022 | 08 Dec 2022 | 07 Jul 2023 | N/A | N/A | 
| 2.4 | N/A | N/A | N/A | 10 Nov 2021 | 08 Jul 2022 | 10 Dec 2022 | N/A | N/A | 
| 2.3 | N/A | N/A | N/A | 09 Aug 2021 | 10 Dec 2021 | 07 Oct 2022 | N/A | N/A | 
| 2.2 | N/A | N/A | N/A | 04 Mar 2021 | 09 Sep 2021 | 08 Jul 2022 | N/A | N/A | 
| 2.1 | N/A | N/A | N/A | 05 Nov 2020 | 05 Apr 2021 | 05 Dec 2021 | N/A | N/A | 
| 2.0 | N/A | N/A | N/A | 30 Jul 2020 | 05 Dec 2020 | 09 Sep 2021 | N/A | N/A | 

**Estimated release cadence:**4 months

**Valid Subscriptions:**OpenShift Platform Plus / Red Hat Advanced Cluster Management for Kubernetes

#### multicluster engine for Kubernetes

| Version | Tier | Supported OpenShift versions | OpenShift Aligned Version | General availability | Full support ends | Maintenance ends | EUS ends | EUS Term 2 ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2.17 | Platform Aligned | 4.22, 4.21, 4.20 | 4.22 | 18 Jun 2026 | 31 Dec 2026 | 31 Dec 2027 | 30 Jun 2028 | 30 Jun 2029 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 2.11 | Platform Aligned | 4.21, 4.20, 4.19, 4.22 | 4.21 | 10 Mar 2026 | 09 Apr 2027 | 10 Sep 2027 | N/A | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 2.10 | Platform Aligned | 4.18, 4.19, 4.20, 4.21 | 4.20 | 03 Dec 2025 | 08 Jan 2027 | 01 Jun 2027 | 12 Nov 2027 | 13 Nov 2028 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 2.9 | Platform Aligned | 4.19, 4.18, 4.17, 4.20 | 4.19 | 01 Aug 2025 | 02 Oct 2026 | 24 Feb 2027 | N/A | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 2.8 | Platform Aligned | 4.16, 4.17, 4.18, 4.19 | 4.18 | 12 Mar 2025 | 17 Apr 2026 | 18 Sep 2026 | 12 Feb 2027 | 13 Feb 2028 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 2.6 | Platform Aligned | 4.14, 4.15, 4.16, 4.17 | 4.16 | 16 Jul 2024 | 15 Aug 2025 | 15 Jan 2026 | 12 Jun 2026 | 11 Jun 2027 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (7)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 2.7 | Platform Aligned | 4.15, 4.16, 4.17, 4.18 | 4.17 | 05 Nov 2024 | 06 Jan 2026 | 02 Jun 2026 | N/A | N/A | 
| 2.5 | N/A | 4.16, 4.15, 4.14, 4.13 | 4.15 | 12 Mar 2024 | 22 Oct 2024 | 23 Sep 2025 | N/A | N/A | 
| 2.4 | N/A | 4.12, 4.13, 4.14, 4.15 | N/A | 15 Nov 2023 | 16 Jul 2024 | 17 Jun 2025 | N/A | N/A | 
| 2.3 | N/A | 4.11, 4.12, 4.13, 4.14 | N/A | 08 Jun 2023 | 09 Jul 2024 | 10 Dec 2024 | N/A | N/A | 
| 2.2 | N/A | 4.10, 4.11, 4.12, 4.13 | N/A | 06 Feb 2023 | 07 Mar 2024 | N/A | N/A | N/A | 
| 2.1 | N/A | 4.9, 4.10, 4.11, 4.12 | N/A | 29 Aug 2022 | 11 Sep 2023 | N/A | N/A | N/A | 
| 2.0 | N/A | N/A | N/A | 06 Jun 2022 | 07 Sep 2022 | N/A | N/A | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**4 months

**Valid Subscriptions:**OpenShift Kubernetes Engine / OpenShift Container Platform / OpenShift Platform Plus

#### Red Hat Quay

| Version | Tier | Supported OpenShift versions | OpenShift Aligned Version | General availability | Full support ends | Maintenance ends | EUS ends | EUS Term 2 ends | EUS Term 3 ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3.18 | Platform Aligned | 4.12, 4.14, 4.16, 4.18, 4.19, 4.20, 4.21, 4.22 | 4.22 | 29 Jul 2026 | 31 Dec 2026 | 31 Dec 2027 | 30 Jun 2028 | 30 Jun 2029 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 3.17 | Platform Aligned | 4.12, 4.14, 4.16, 4.18, 4.19, 4.20, 4.21 | 4.21 | 24 Mar 2026 | 29 Oct 2026 | 03 Aug 2027 | N/A | N/A | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 3.16 | Platform Aligned | 4.12, 4.14, 4.16, 4.17, 4.18, 4.19, 4.20 | 4.20 | 18 Dec 2025 | 24 Jun 2026 | 21 Apr 2027 | 21 Oct 2027 | 21 Oct 2028 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 3.15 | Platform Aligned | 4.12, 4.14, 4.15, 4.16, 4.17, 4.18, 4.19 | 4.19 | 07 Jul 2025 | 18 Mar 2026 | 17 Dec 2026 | N/A | N/A | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 3.14 | Platform Aligned | 4.12, 4.14, 4.15, 4.16, 4.17, 4.18 | 4.18 | 02 Apr 2025 | 07 Oct 2025 | 25 Aug 2026 | 25 Feb 2027 | 25 Feb 2028 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 3.12 | Platform Aligned | 4.12, 4.14, 4.15, 4.16 | 4.16 | 23 Jul 2024 | 30 Jan 2025 | 27 Dec 2025 | 27 Jun 2026 | 27 Jun 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 3.10 | Platform Aligned | 4.11, 4.12, 4.13, 4.14 | 4.14 | 28 Nov 2023 | 02 Jul 2024 | 01 May 2025 | 31 Oct 2025 | 31 Oct 2026 | 31 Oct 2027 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 3.9 | Platform Aligned | 4.10, 4.11, 4.12, 4.13 | 4.12 | 14 Aug 2023 | 28 Feb 2024 | 17 Jun 2024 | 17 Jan 2025 | 17 Jan 2026 | 17 Jan 2027 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (12)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 3.13 | Platform Aligned | 4.12, 4.14, 4.15, 4.16, 4.17 | 4.17 | 30 Oct 2024 | 02 Jul 2025 | 01 Apr 2026 | N/A | N/A | N/A | 
| 3.11 | Platform Aligned | 4.12, 4.13, 4.14, 4.15 | 4.15 | 02 Apr 2024 | 23 Oct 2024 | 27 Aug 2025 | N/A | N/A | N/A | 
| 3.8 | Platform Aligned | 4.8, 4.9, 4.10, 4.11, 4.12, 4.13 | N/A | 06 Dec 2022 | 14 Nov 2023 | 17 Nov 2023 | N/A | N/A | N/A | 
| 3.7 | N/A | 4.6, 4.7, 4.8, 4.9, 4.10, 4.11, 4.12, 4.13 | N/A | 23 May 2022 | 06 Dec 2022 | 14 Aug 2023 | N/A | N/A | N/A | 
| 3.6 | N/A | 4.6, 4.7, 4.8, 4.9, 4.10 | N/A | 19 Oct 2021 | 23 May 2022 | 06 Dec 2022 | N/A | N/A | N/A | 
| 3.5 | N/A | 4.5, 4.6, 4.7, 4.8, 4.9 | N/A | 15 Apr 2021 | 19 Oct 2021 | 23 May 2022 | N/A | N/A | N/A | 
| 3.4 | N/A | 4.4, 4.5, 4.6, 4.7, 4.8 | N/A | 04 Feb 2021 | 15 Apr 2021 | 19 Oct 2021 | N/A | N/A | N/A | 
| 3.3 | N/A | 4.2, 4.3, 4.4, 4.5, 4.6, 4.7 | N/A | 13 May 2020 | 04 Feb 2021 | 15 Apr 2021 | N/A | N/A | N/A | 
| 3.2 | N/A | 4.2, 4.3, 4.4, 4.5, 4.6 | N/A | 18 Dec 2019 | 13 May 2020 | 04 Feb 2021 | N/A | N/A | N/A | 
| 3.1 | N/A | 4.1, 4.2, 4.3 | N/A | 05 Sep 2019 | 18 Dec 2019 | 13 May 2020 | N/A | N/A | N/A | 
| 3.0 | N/A | 4.1 | N/A | 01 May 2019 | 05 Sep 2019 | 18 Dec 2019 | N/A | N/A | N/A | 
| 2.9 | N/A | 4.1 | N/A | 03 Apr 2019 | 04 Apr 2019 | 05 Sep 2019 | N/A | N/A | N/A | 

**Estimated release cadence:**4 months

**Valid Subscriptions:**OpenShift Kubernetes Engine / OpenShift Container Platform / OpenShift Platform Plus

#### Red Hat Quay Container Security Operator

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends | EUS Term 2 ends | EUS Term 3 ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3.18 | Platform Aligned | 4.12, 4.14, 4.16, 4.18, 4.19, 4.20, 4.21, 4.22 | 29 Jul 2026 | 31 Dec 2026 | 31 Dec 2027 | 30 Jun 2028 | 30 Jun 2029 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 3.17 | Platform Aligned | 4.12, 4.14, 4.16, 4.18, 4.19, 4.20, 4.21 | 24 Mar 2026 | 29 Oct 2026 | 03 Aug 2027 | N/A | N/A | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 3.16 | Platform Aligned | 4.12, 4.14, 4.16, 4.17, 4.18, 4.19, 4.20 | 18 Dec 2025 | 24 Jun 2026 | 21 Apr 2027 | 21 Oct 2027 | 21 Oct 2028 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 3.15 | Platform Aligned | 4.12, 4.14, 4.15, 4.16, 4.17, 4.18, 4.19 | 07 Jul 2025 | 18 Mar 2026 | 17 Dec 2026 | N/A | N/A | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 3.14 | Platform Aligned | 4.12, 4.14, 4.15, 4.16, 4.17, 4.18 | 02 Apr 2025 | 07 Oct 2025 | 25 Aug 2026 | 25 Feb 2027 | 25 Feb 2028 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 3.12 | Platform Aligned | 4.12, 4.14, 4.15, 4.16 | 23 Jul 2024 | 30 Jan 2025 | 27 Dec 2025 | 27 Jun 2026 | 27 Jun 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 3.10 | Platform Aligned | 4.11, 4.12, 4.13, 4.14 | 28 Nov 2023 | 02 Jul 2024 | 01 May 2025 | 23 Oct 2025 | 31 Oct 2026 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 3.9 | Platform Aligned | 4.10, 4.11, 4.12, 4.13 | 14 Aug 2023 | 28 Feb 2024 | 17 Jun 2024 | 17 Jan 2025 | 17 Jan 2026 | 17 Jan 2027 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (12)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 3.13 | Platform Aligned | 4.12, 4.14, 4.15, 4.16, 4.17 | 30 Oct 2024 | 02 Jul 2025 | 01 Apr 2026 | N/A | N/A | N/A | 
| 3.11 | Platform Aligned | 4.12, 4.14, 4.15 | 02 Apr 2024 | 23 Oct 2024 | 27 Aug 2025 | N/A | N/A | N/A | 
| 3.8 | N/A | 4.8, 4.9, 4.10, 4.11, 4.12, 4.13 | 06 Dec 2022 | 14 Nov 2023 | 17 Nov 2023 | N/A | N/A | N/A | 
| 3.7 | N/A | 4.6, 4.7, 4.8, 4.9, 4.10, 4.11, 4.12, 4.13 | 23 May 2022 | 06 Dec 2022 | 14 Aug 2023 | N/A | N/A | N/A | 
| 3.6 | N/A | 4.6, 4.7, 4.8, 4.9, 4.10 | 19 Oct 2021 | 23 May 2022 | 06 Dec 2022 | N/A | N/A | N/A | 
| 3.5 | N/A | 4.5, 4.6, 4.7, 4.8, 4.9 | 15 Apr 2021 | 19 Oct 2021 | 23 May 2022 | N/A | N/A | N/A | 
| 3.4 | N/A | 4.4, 4.5, 4.6, 4.7, 4.8 | 04 Feb 2021 | 15 Apr 2021 | 19 Oct 2021 | N/A | N/A | N/A | 
| 3.3 | N/A | 4.2, 4.3, 4.4, 4.5, 4.6, 4.7 | 13 May 2020 | 04 Feb 2021 | 15 Apr 2021 | N/A | N/A | N/A | 
| 3.2 | N/A | 4.2, 4.3, 4.4, 4.5, 4.6 | 18 Dec 2019 | 13 May 2020 | 04 Feb 2021 | N/A | N/A | N/A | 
| 3.1 | N/A | 4.1, 4.2, 4.3 | 05 Sep 2019 | 18 Dec 2019 | 13 May 2020 | N/A | N/A | N/A | 
| 3.0 | N/A | 4.1 | 01 May 2019 | 05 Sep 2019 | 18 Dec 2019 | N/A | N/A | N/A | 
| 2.9 | N/A | 4.1 | 03 Apr 2019 | 04 Apr 2019 | 05 Sep 2019 | N/A | N/A | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**4 months

**Valid Subscriptions:**OpenShift Kubernetes Engine / OpenShift Container Platform / OpenShift Platform Plus

#### Red Hat Quay bridge operator

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends | EUS Term 2 ends | EUS Term 3 ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3.18 | Platform Aligned | 4.12, 4.14, 4.16, 4.18, 4.19, 4.20, 4.21, 4.22 | 29 Jul 2026 | 31 Dec 2026 | 31 Dec 2027 | 30 Jun 2028 | 30 Jun 2029 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 3.17 | Platform Aligned | 4.12, 4.14, 4.16, 4.18, 4.19, 4.20, 4.21 | 24 Mar 2026 | 29 Oct 2026 | 03 Aug 2027 | N/A | N/A | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 3.16 | Platform Aligned | 4.12, 4.14, 4.16, 4.17, 4.18, 4.19, 4.20 | 18 Dec 2025 | 24 Jun 2026 | 21 Apr 2027 | 21 Oct 2027 | 21 Oct 2028 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 3.15 | Platform Aligned | 4.12, 4.14, 4.15, 4.16, 4.17, 4.18, 4.19 | 07 Jul 2025 | 18 Mar 2026 | 17 Dec 2026 | N/A | N/A | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 3.14 | Platform Aligned | 4.12, 4.14, 4.15, 4.16, 4.17, 4.18 | 02 Apr 2025 | 07 Oct 2025 | 25 Aug 2026 | 25 Feb 2027 | 25 Feb 2028 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 3.12 | Platform Aligned | 4.12, 4.14, 4.15, 4.16 | 23 Jul 2024 | 30 Jan 2025 | 27 Dec 2025 | 27 Jun 2026 | 27 Jun 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 3.10 | Platform Aligned | 4.11, 4.12, 4.13, 4.14 | 28 Nov 2023 | 02 Jul 2024 | 01 May 2025 | 31 Oct 2025 | 31 Oct 2026 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 3.9 | Platform Aligned | 4.10, 4.11, 4.12, 4.13 | 14 Aug 2023 | 28 Feb 2024 | 17 Jun 2024 | 17 Jan 2025 | 17 Jan 2026 | 17 Jan 2027 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (12)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 3.13 | Platform Aligned | 4.12, 4.14, 4.15, 4.16, 4.17 | 30 Oct 2024 | 02 Jul 2025 | 01 Apr 2026 | N/A | N/A | N/A | 
| 3.11 | Platform Aligned | 4.12, 4.13, 4.14, 4.15 | 02 Apr 2024 | 23 Oct 2024 | 27 Aug 2025 | N/A | N/A | N/A | 
| 3.8 | Platform Aligned | 4.8, 4.9, 4.10, 4.11, 4.12, 4.13 | 06 Dec 2022 | 14 Nov 2023 | 17 Nov 2023 | N/A | N/A | N/A | 
| 3.7 | N/A | 4.6, 4.7, 4.8, 4.9, 4.10, 4.11, 4.12, 4.13 | 23 May 2022 | 06 Dec 2022 | 14 Aug 2023 | N/A | N/A | N/A | 
| 3.6 | N/A | 4.6, 4.7, 4.8, 4.9, 4.10 | 19 Oct 2021 | 23 May 2022 | 06 Dec 2022 | N/A | N/A | N/A | 
| 3.5 | N/A | 4.5, 4.6, 4.7, 4.8, 4.9 | 15 Apr 2021 | 19 Oct 2021 | 23 May 2022 | N/A | N/A | N/A | 
| 3.4 | N/A | 4.4, 4.5, 4.6, 4.7, 4.8 | 04 Feb 2021 | 15 Apr 2021 | 19 Oct 2021 | N/A | N/A | N/A | 
| 3.3 | N/A | 4.2, 4.3, 4.4, 4.5, 4.6, 4.7 | 13 May 2020 | 04 Feb 2021 | 15 Apr 2021 | N/A | N/A | N/A | 
| 3.2 | N/A | 4.2, 4.3, 4.4, 4.5, 4.6 | 18 Dec 2019 | 13 May 2020 | 04 Feb 2021 | N/A | N/A | N/A | 
| 3.1 | N/A | 4.1, 4.2, 4.3 | 05 Sep 2019 | 18 Dec 2019 | 13 May 2020 | N/A | N/A | N/A | 
| 3.0 | N/A | 4.1 | 01 May 2019 | 05 Sep 2019 | 18 Dec 2019 | N/A | N/A | N/A | 
| 2.9 | N/A | 4.1 | 03 Apr 2019 | 04 Apr 2019 | 05 Sep 2019 | N/A | N/A | N/A | 

**Estimated release cadence:**4 months

**Valid Subscriptions:**OpenShift Kubernetes Engine / OpenShift Container Platform / OpenShift Platform Plus

| Version | Tier | Supported OpenShift versions | OpenShift Aligned Version | General availability | Full support ends | Maintenance ends | EUS ends | EUS Term 2 ends | EUS Term 3 ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 4.22 | Platform Aligned | 4.22 | 4.22 | 09 Jun 2026 | 31 Dec 2026 | 31 Dec 2027 | 30 Jun 2028 | 30 Jun 2029 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.21 | Platform Aligned | 4.21 | 4.21 | 03 Feb 2026 | 09 Sep 2026 | 03 Aug 2027 | N/A | N/A | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.20 | Platform Aligned | 4.20 | 4.20 | 21 Oct 2025 | 03 May 2026 | 21 Apr 2027 | 21 Oct 2027 | 21 Oct 2028 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.19 | Platform Aligned | 4.19 | 4.19 | 17 Jun 2025 | 21 Jan 2026 | 17 Dec 2026 | N/A | N/A | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.18 | Platform Aligned | 4.18 | 4.18 | 25 Feb 2025 | 17 Sep 2025 | 25 Aug 2026 | 25 Feb 2027 | 25 Feb 2028 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.16 | Platform Aligned | 4.16 | 4.16 | 27 Jun 2024 | 01 Jan 2025 | 27 Dec 2025 | 27 Jun 2026 | 27 Jun 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.14 | Platform Aligned | 4.14 | 4.14 | 31 Oct 2023 | 27 May 2024 | 01 May 2025 | 31 Oct 2025 | 31 Oct 2026 | 31 Oct 2027 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.12 | Platform Aligned | 4.12 | 4.12 | 17 Jan 2023 | 17 Aug 2023 | 17 Jul 2024 | 17 Jan 2025 | 17 Jan 2026 | 17 Jan 2027 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (5)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 4.17 | Platform Aligned | 4.17 | 4.17 | 01 Oct 2024 | 25 May 2025 | 01 Apr 2026 | N/A | N/A | N/A | 
| 4.15 | Platform Aligned | 4.15 | 4.15 | 27 Feb 2024 | 27 Sep 2024 | 27 Aug 2025 | N/A | N/A | N/A | 
| 4.13 | Platform Aligned | 4.13 | 4.13 | 17 May 2023 | 31 Jan 2024 | 17 Nov 2024 | N/A | N/A | N/A | 
| 4.11 | Platform Aligned | 4.11 | 4.11 | 10 Aug 2022 | 17 Apr 2023 | 10 Feb 2024 | N/A | N/A | N/A | 
| 4.10 | Platform Aligned | 4.10 | 4.10 | 10 Mar 2022 | 10 Nov 2022 | 10 Sep 2023 | N/A | N/A | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**4 months

**Valid Subscriptions:**OpenShift Kubernetes Engine / OpenShift Container Platform / OpenShift Platform Plus

| Version | Tier | Supported OpenShift versions | OpenShift Aligned Version | General availability | Full support ends | Maintenance ends | EUS ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 4.22 | Platform Aligned | 4.22 | 4.22 | 09 Jun 2026 | 31 Dec 2026 | 31 Dec 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.21 | Platform Aligned | 4.21 | 4.21 | 10 Feb 2026 | 09 Sep 2026 | 03 Aug 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.20 | Platform Aligned | 4.20 | 4.20 | 21 Oct 2025 | 03 May 2026 | 21 Apr 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.19 | Platform Aligned | 4.19 | 4.19 | 17 Jun 2025 | 21 Jan 2026 | 17 Dec 2026 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.18 | Platform Aligned | 4.18 | 4.18 | 25 Feb 2025 | 17 Sep 2025 | 25 Aug 2026 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.16 | Platform Aligned | 4.16 | 4.16 | 27 Jun 2024 | 01 Jan 2025 | 27 Dec 2025 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (1)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 4.17 | Platform Aligned | 4.16 | 4.16 | 01 Oct 2024 | 25 May 2025 | 01 Apr 2026 | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**4 months

**Valid Subscriptions:**OpenShift Container Platform / OpenShift Platform Plus

| Version | Tier | Supported OpenShift versions | OpenShift Aligned Version | General availability | Full support ends | Maintenance ends | EUS ends | EUS Term 2 ends | EUS Term 3 ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 4.22 | Platform Aligned | 4.22 | 4.22 | 09 Jun 2026 | 31 Dec 2026 | 31 Dec 2027 | 30 Jun 2028 | 30 Jun 2029 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.21 | Platform Aligned | 4.21 | 4.21 | 03 Feb 2026 | 09 Sep 2026 | 03 Aug 2027 | N/A | N/A | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.20 | Platform Aligned | 4.20 | 4.20 | 21 Oct 2025 | 03 May 2026 | 21 Apr 2027 | 21 Oct 2027 | 21 Oct 2028 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.19 | Platform Aligned | 4.19 | 4.19 | 17 Jun 2025 | 21 Jan 2026 | 17 Dec 2026 | N/A | N/A | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.18 | Platform Aligned | 4.18 | 4.18 | 25 Feb 2025 | 17 Sep 2025 | 25 Aug 2026 | 25 Feb 2027 | 25 Feb 2028 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.16 | Platform Aligned | 4.16 | 4.16 | 27 Jun 2024 | 01 Jan 2025 | 27 Dec 2025 | 27 Jun 2026 | 27 Jun 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.14 | Platform Aligned | 4.14 | 4.14 | 31 Oct 2023 | 27 May 2024 | 01 May 2025 | 31 Oct 2025 | 31 Oct 2026 | 31 Oct 2027 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.12 | Platform Aligned | 4.12 | 4.12 | 17 Jan 2023 | 17 Aug 2023 | 17 Jul 2024 | 17 Jan 2025 | 17 Jan 2026 | 17 Jan 2027 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (5)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 4.17 | Platform Aligned | 4.17 | 4.17 | 01 Oct 2024 | 25 May 2025 | 01 Apr 2026 | N/A | N/A | N/A | 
| 4.15 | Platform Aligned | 4.15 | 4.15 | 27 Feb 2024 | 27 Sep 2024 | 27 Aug 2025 | N/A | N/A | N/A | 
| 4.13 | Platform Aligned | 4.13 | 4.13 | 17 May 2023 | 31 Jan 2024 | 17 Nov 2024 | N/A | N/A | N/A | 
| 4.11 | Platform Aligned | 4.11 | 4.11 | 10 Aug 2022 | 17 Apr 2023 | 10 Feb 2024 | N/A | N/A | N/A | 
| 4.10 | Platform Aligned | 4.10 | 4.10 | 10 Mar 2022 | 10 Nov 2022 | 10 Sep 2023 | N/A | N/A | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**4 months

**Valid Subscriptions:**OpenShift Kubernetes Engine / OpenShift Container Platform / OpenShift Platform Plus

| Version | Tier | Supported OpenShift versions | OpenShift Aligned Version | General availability | Full support ends | Maintenance ends | EUS ends | EUS Term 2 ends | 
|---|---|---|---|---|---|---|---|---|
| 0.8 | Platform Aligned | 4.22 | 4.22 | 16 Jun 2026 | 31 Dec 2026 | 31 Dec 2027 | 30 Jun 2028 | 30 Jun 2029 | 
| 0.7 | Platform Aligned | 4.21 | 4.21 | 24 Feb 2026 | 09 Sep 2026 | 03 Aug 2027 | N/A | N/A | 
| 0.6 | Platform Aligned | 4.20 | 4.20 | 16 Sep 2025 | 03 May 2026 | 21 Apr 2027 | 21 Oct 2027 | 21 Oct 2028 | 
| 0.5 | Platform Aligned | 4.18 | 4.18 | 21 Jan 2025 | 16 Sep 2025 | 25 Aug 2026 | 25 Feb 2027 | 25 Feb 2028 | 
| 0.4 | Platform Aligned | 4.16 | 4.16 | 08 May 2024 | 21 Jan 2025 | 27 Dec 2025 | 27 Jun 2026 | 27 Jun 2027 | 
| 0.2 | Platform Aligned | 4.14 | 4.14 | 12 Sep 2023 | 20 Feb 2024 | 01 May 2025 | 31 Oct 2025 | 31 Oct 2026 | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**4 months

**Valid Subscriptions:**OpenShift Kubernetes Engine / OpenShift Container Platform / OpenShift Platform Plus

| Version | Tier | Supported OpenShift versions | OpenShift Aligned Version | General availability | Full support ends | Maintenance ends | EUS ends | EUS Term 2 ends | EUS Term 3 ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 4.22 | Platform Aligned | 4.22 | 4.22 | 09 Jun 2026 | 31 Dec 2026 | 31 Dec 2027 | 30 Jun 2028 | 30 Jun 2029 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.21 | Platform Aligned | 4.21 | 4.21 | 10 Feb 2026 | 09 Sep 2026 | 03 Aug 2027 | N/A | N/A | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.20 | Platform Aligned | 4.20 | 4.20 | 21 Oct 2025 | 03 May 2026 | 21 Apr 2027 | 21 Oct 2027 | 21 Oct 2028 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.19 | Platform Aligned | 4.19 | 4.19 | 17 Jun 2025 | 21 Jan 2026 | 17 Dec 2026 | N/A | N/A | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.18 | Platform Aligned | 4.18 | 4.18 | 25 Feb 2025 | 17 Sep 2025 | 25 Aug 2026 | 25 Feb 2027 | 25 Feb 2028 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.16 | Platform Aligned | 4.16 | 4.16 | 27 Jun 2024 | 01 Jan 2025 | 27 Dec 2025 | 27 Jun 2026 | 27 Jun 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.14 | Platform Aligned | 4.14 | 4.14 | 31 Oct 2023 | 27 May 2024 | 01 May 2025 | 31 Oct 2025 | 31 Oct 2026 | 31 Oct 2027 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.12 | Platform Aligned | 4.12 | 4.12 | 17 Jan 2023 | 17 Aug 2023 | 17 Jul 2024 | 17 Jan 2025 | 17 Jan 2026 | 17 Jan 2027 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (3)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 4.17 | Platform Aligned | 4.17 | 4.17 | 01 Oct 2024 | 25 May 2025 | 01 Apr 2026 | N/A | N/A | N/A | 
| 4.15 | Platform Aligned | 4.15 | 4.15 | 27 Feb 2024 | 27 Sep 2024 | 27 Aug 2025 | N/A | N/A | N/A | 
| 4.13 | Platform Aligned | 4.13 | 4.13 | 17 May 2023 | 31 Jan 2024 | 17 Nov 2024 | N/A | N/A | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**4 months

**Valid Subscriptions:**OpenShift Container Platform / OpenShift Platform Plus

| Version | Tier | Supported OpenShift versions | OpenShift Aligned Version | General availability | Full support ends | Maintenance ends | EUS ends | EUS Term 2 ends | EUS Term 3 ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 4.22 | Platform Aligned | 4.22 | 4.22 | 09 Jun 2026 | 31 Dec 2026 | 31 Dec 2027 | 30 Jun 2028 | 30 Jun 2029 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.21 | Platform Aligned | 4.21 | 4.21 | 03 Feb 2026 | 09 Sep 2026 | 03 Aug 2027 | N/A | N/A | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.20 | Platform Aligned | 4.20 | 4.20 | 21 Oct 2025 | 03 May 2026 | 21 Apr 2027 | 21 Oct 2027 | 21 Oct 2028 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.19 | Platform Aligned | 4.19 | 4.19 | 17 Jun 2025 | 21 Jan 2026 | 17 Dec 2026 | N/A | N/A | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.18 | Platform Aligned | 4.18 | 4.18 | 25 Feb 2025 | 17 Sep 2025 | 25 Aug 2026 | 25 Feb 2027 | 25 Feb 2028 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.16 | Platform Aligned | 4.16 | 4.16 | 27 Jun 2024 | 01 Jan 2025 | 27 Dec 2025 | 27 Jun 2026 | 27 Jun 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.14 | Platform Aligned | 4.14 | 4.14 | 31 Oct 2023 | 27 May 2024 | 01 May 2025 | 31 Oct 2025 | 31 Oct 2026 | 31 Oct 2027 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (4)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 4.17 | Platform Aligned | 4.17 | 4.17 | 01 Oct 2024 | 25 May 2025 | 01 Apr 2026 | N/A | N/A | N/A | 
| 4.15 | Platform Aligned | 4.15 | 4.15 | 27 Feb 2024 | 27 Sep 2024 | 27 Aug 2025 | N/A | N/A | N/A | 
| 4.13 | N/A | 4.13 | 4.13 | 17 May 2023 | 31 Jan 2024 | 17 Nov 2024 | N/A | N/A | N/A | 
| 4.12 | N/A | 4.12 | 4.12 | 17 Jan 2023 | 17 Aug 2023 | 17 Jul 2024 | N/A | N/A | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**4 months

| Version | Tier | Supported OpenShift versions | OpenShift Aligned Version | General availability | Full support ends | Maintenance ends | EUS ends | EUS Term 2 ends | EUS Term 3 ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 4.22 | Platform Aligned | 4.22 | 4.22 | 09 Jun 2026 | 31 Dec 2026 | 31 Dec 2027 | 30 Jun 2028 | 30 Jun 2029 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.21 | Platform Aligned | 4.21 | 4.21 | 03 Feb 2026 | 09 Sep 2026 | 03 Aug 2027 | N/A | N/A | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.20 | Platform Aligned | 4.20 | 4.20 | 21 Oct 2025 | 03 May 2026 | 21 Apr 2027 | 21 Oct 2027 | 21 Oct 2028 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.19 | Platform Aligned | 4.19 | 4.19 | 17 Jun 2025 | 21 Jan 2026 | 17 Dec 2026 | N/A | N/A | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.18 | Platform Aligned | 4.18 | 4.18 | 25 Feb 2025 | 17 Sep 2025 | 25 Aug 2026 | 25 Feb 2027 | 25 Feb 2028 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.16 | Platform Aligned | 4.16 | 4.16 | 27 Jun 2024 | 01 Jan 2025 | 27 Dec 2025 | 27 Jun 2026 | 27 Jun 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.14 | Platform Aligned | 4.14 | 4.14 | 31 Oct 2023 | 27 May 2024 | 01 May 2025 | 31 Oct 2025 | 31 Oct 2026 | 31 Oct 2027 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **Previous operator releases without a tiered strategy** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.12 | N/A | 4.12 | 4.12 | 17 Jan 2023 | 17 Aug 2023 | 17 Jul 2024 | 17 Jan 2025 | 17 Jan 2026 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (3)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 4.17 | Platform Aligned | 4.17 | 4.17 | 01 Oct 2024 | 25 May 2025 | 01 Apr 2026 | N/A | N/A | N/A | 
| 4.15 | Platform Aligned | 4.15 | 4.15 | 27 Feb 2024 | 27 Sep 2024 | 27 Aug 2025 | N/A | N/A | N/A | 
| 4.13 | N/A | 4.13 | 4.13 | 17 May 2023 | 31 Jan 2024 | 17 Nov 2024 | N/A | N/A | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**4 months

| Version | Tier | Supported OpenShift versions | OpenShift Aligned Version | General availability | Full support ends | Maintenance ends | EUS ends | EUS Term 2 ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 4.22 | Platform Aligned | 4.22 | 4.22 | 09 Jun 2026 | 31 Dec 2026 | 31 Dec 2027 | 30 Jun 2028 | 30 Jun 2029 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.21 | Platform Aligned | 4.21 | 4.21 | 03 Feb 2026 | 09 Sep 2026 | 03 Aug 2027 | N/A | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.20 | Platform Aligned | 4.20 | 4.20 | 21 Oct 2025 | 03 May 2026 | 21 Apr 2027 | 21 Oct 2027 | 21 Oct 2028 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.19 | Platform Aligned | 4.19 | 4.19 | 17 Jun 2025 | 21 Jan 2026 | 17 Dec 2026 | N/A | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.18 | Platform Aligned | 4.18 | 4.18 | 25 Feb 2025 | 17 Sep 2025 | 25 Aug 2026 | 25 Feb 2027 | 25 Feb 2028 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.16 | Platform Aligned | 4.16 | 4.16 | 27 Jun 2024 | 01 Jan 2025 | 27 Dec 2025 | 27 Jun 2026 | 27 Jun 2027 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.14 | Platform Aligned | 4.14 | 4.14 | 31 Oct 2023 | 27 May 2024 | 01 May 2025 | 31 Oct 2025 | 31 Oct 2026 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (2)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 4.17 | Platform Aligned | 4.17 | 4.17 | 01 Oct 2024 | 25 May 2025 | 01 Apr 2026 | N/A | N/A | 
| 4.15 | Platform Aligned | 4.15 | 4.15 | 27 Feb 2024 | 27 Sep 2024 | 27 Aug 2025 | N/A | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**4 months

**Valid Subscriptions:**OpenShift Container Platform / OpenShift Platform Plus

| Version | Tier | Supported OpenShift versions | OpenShift Aligned Version | General availability | Full support ends | Maintenance ends | EUS ends | EUS Term 2 ends | EUS Term 3 ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 4.22 | Platform Aligned | 4.22 | 4.22 | 09 Jun 2026 | 31 Dec 2026 | 31 Dec 2027 | 30 Jun 2028 | 30 Jun 2029 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.21 | Platform Aligned | 4.21 | 4.21 | 10 Feb 2026 | 09 Sep 2026 | 03 Aug 2027 | N/A | N/A | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.20 | Platform Aligned | 4.20 | 4.20 | 21 Oct 2025 | 03 May 2026 | 21 Apr 2027 | 21 Oct 2027 | 21 Oct 2028 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.19 | Platform Aligned | 4.19 | 4.19 | 17 Jun 2025 | 21 Jan 2026 | 17 Dec 2026 | N/A | N/A | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.18 | Platform Aligned | 4.18 | 4.18 | 25 Feb 2025 | 17 Sep 2025 | 25 Aug 2026 | 25 Feb 2027 | 25 Feb 2028 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.16 | Platform Aligned | 4.16 | 4.16 | 27 Jun 2024 | 01 Jan 2025 | 27 Dec 2025 | 27 Jun 2026 | 27 Jun 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.14 | Platform Aligned | 4.14 | 4.14 | 31 Oct 2023 | 27 May 2024 | 01 May 2025 | 31 Oct 2025 | 31 Oct 2026 | 31 Oct 2027 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.12 | Platform Aligned | 4.12 | 4.12 | 17 Jan 2023 | 17 Aug 2023 | 17 Jul 2024 | 17 Jan 2025 | 17 Jan 2026 | 17 Jan 2027 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (5)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 4.17 | Platform Aligned | 4.17 | 4.17 | 01 Oct 2024 | 25 May 2025 | 01 Apr 2026 | N/A | N/A | N/A | 
| 4.15 | Platform Aligned | 4.15 | 4.15 | 27 Feb 2024 | 27 Sep 2024 | 27 Aug 2025 | N/A | N/A | N/A | 
| 4.13 | Platform Aligned | 4.13 | 4.13 | 17 May 2023 | 31 Jan 2024 | 17 Nov 2024 | N/A | N/A | N/A | 
| 4.11 | Platform Aligned | 4.11 | 4.11 | 10 Aug 2022 | 17 Apr 2023 | 10 Feb 2024 | N/A | N/A | N/A | 
| 4.10 | Platform Aligned | 4.10 | 4.10 | 10 Mar 2022 | 10 Nov 2022 | 10 Sep 2023 | N/A | N/A | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**4 months

**Valid Subscriptions:**OpenShift Kubernetes Engine / OpenShift Container Platform / OpenShift Platform Plus

| Version | Tier | Supported OpenShift versions | OpenShift Aligned Version | General availability | Full support ends | Maintenance ends | EUS ends | EUS Term 2 ends | EUS Term 3 ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 4.22 | Platform Aligned | 4.22 | 4.22 | 09 Jun 2026 | 31 Dec 2026 | 31 Dec 2027 | 30 Jun 2028 | 30 Jun 2029 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.21 | Platform Aligned | 4.21 | 4.21 | 03 Feb 2026 | 09 Sep 2026 | 03 Aug 2027 | N/A | N/A | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.20 | Platform Aligned | 4.20 | 4.20 | 31 Oct 2025 | 03 Jun 2026 | 21 Apr 2027 | 21 Oct 2027 | 21 Oct 2028 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.19 | Platform Aligned | 4.19 | 4.19 | 17 Jun 2025 | 21 Jan 2026 | 17 Dec 2026 | N/A | N/A | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.18 | Platform Aligned | 4.18 | 4.18 | 25 Feb 2025 | 17 Sep 2025 | 25 Aug 2026 | 25 Feb 2027 | 25 Feb 2028 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.16 | Platform Aligned | 4.16 | 4.16 | 27 Jun 2024 | 01 Jan 2025 | 27 Dec 2025 | 27 Jun 2026 | 27 Jun 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.14 | Platform Aligned | 4.14 | 4.14 | 31 Oct 2023 | 27 May 2024 | 01 May 2025 | 31 Oct 2025 | 31 Oct 2026 | 31 Oct 2027 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.12 | Platform Aligned | 4.12 | 4.12 | 17 Jan 2023 | 17 Aug 2023 | 17 Jul 2024 | 17 Jan 2025 | 17 Jan 2026 | 17 Jan 2027 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (3)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 4.17 | Platform Aligned | 4.17 | 4.17 | 01 Oct 2024 | 25 May 2025 | 01 Apr 2026 | N/A | N/A | N/A | 
| 4.15 | Platform Aligned | 4.15 | 4.15 | 08 Feb 2024 | 09 May 2024 | 27 Aug 2025 | N/A | N/A | N/A | 
| 4.13 | N/A | 4.13 | 4.13 | 01 May 2023 | 01 Aug 2023 | 17 Nov 2024 | N/A | N/A | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**4 months

**Valid Subscriptions:**OpenShift Kubernetes Engine / OpenShift Container Platform / OpenShift Platform Plus

| Version | Tier | Supported OpenShift versions | OpenShift Aligned Version | General availability | Full support ends | Maintenance ends | EUS ends | EUS Term 2 ends | 
|---|---|---|---|---|---|---|---|---|
| 0.7 | Platform Aligned | 4.22 | 4.22 | 16 Jun 2026 | 31 Dec 2026 | 31 Dec 2027 | 30 Jun 2028 | 30 Jun 2029 | 
| 0.6 | Platform Aligned | 4.21 | 4.21 | 24 Feb 2026 | 09 Sep 2026 | 03 Aug 2027 | N/A | N/A | 
| 0.5 | Platform Aligned | 4.20 | 4.20 | 24 Nov 2025 | 03 May 2026 | 21 Apr 2027 | 21 Oct 2027 | 21 Oct 2028 | 
| 0.4 | Platform Aligned | 4.18 | 4.18 | 21 Jan 2025 | 24 Nov 2025 | 25 Aug 2026 | 25 Feb 2027 | 25 Feb 2028 | 
| 0.3 | Platform Aligned | 4.16 | 4.16 | 08 May 2024 | 21 Jan 2025 | 27 Dec 2025 | 27 Jun 2026 | 27 Jun 2027 | 
| 0.2 | Platform Aligned | 4.14 | 4.14 | 12 Sep 2023 | 20 Feb 2024 | 01 May 2025 | 31 Oct 2025 | 31 Oct 2026 | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**4 months

**Valid Subscriptions:**OpenShift Kubernetes Engine / OpenShift Container Platform / OpenShift Platform Plus

| Version | Tier | Supported OpenShift versions | OpenShift Aligned Version | General availability | Full support ends | Maintenance ends | EUS ends | EUS Term 2 ends | EUS Term 3 ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 4.22 | Platform Aligned | 4.22 | 4.22 | 09 Jun 2026 | 31 Dec 2026 | 31 Dec 2027 | 30 Jun 2028 | 30 Jun 2029 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.21 | Platform Aligned | 4.21 | 4.21 | 03 Feb 2026 | 09 Sep 2026 | 03 Aug 2027 | N/A | N/A | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.20 | Platform Aligned | 4.20 | 4.20 | 21 Oct 2025 | 03 May 2026 | 21 Apr 2027 | 21 Oct 2027 | 21 Oct 2028 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.19 | Platform Aligned | 4.19 | 4.19 | 17 Jun 2025 | 21 Jan 2026 | 17 Dec 2026 | N/A | N/A | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.18 | Platform Aligned | 4.18 | 4.18 | 25 Feb 2025 | 17 Sep 2025 | 25 Aug 2026 | 25 Feb 2027 | 25 Feb 2028 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.16 | Platform Aligned | 4.16 | 4.16 | 27 Jun 2024 | 01 Jan 2025 | 27 Dec 2025 | 27 Jun 2026 | 27 Jun 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.14 | Platform Aligned | 4.14 | 4.14 | 31 Oct 2023 | 27 May 2024 | 01 May 2025 | 31 Oct 2025 | 31 Oct 2026 | 31 Oct 2027 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.12 | Platform Aligned | 4.12 | 4.12 | 17 Jan 2023 | 17 Aug 2023 | 17 Jul 2024 | 17 Jan 2025 | 17 Jan 2026 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (3)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 4.17 | Platform Aligned | 4.17 | 4.17 | 01 Oct 2024 | 25 May 2025 | 01 Apr 2026 | N/A | N/A | N/A | 
| 4.15 | Platform Aligned | 4.15 | 4.15 | 27 Feb 2024 | 27 Sep 2024 | 27 Aug 2025 | N/A | N/A | N/A | 
| 4.13 | Platform Aligned | 4.13 | 4.13 | 17 May 2023 | 31 Jan 2024 | 17 Nov 2024 | N/A | N/A | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**4 months

**Valid Subscriptions:**OpenShift Kubernetes Engine / OpenShift Container Platform / OpenShift Platform Plus

| Version | Tier | Supported OpenShift versions | OpenShift Aligned Version | General availability | Full support ends | Maintenance ends | EUS ends | EUS Term 2 ends | EUS Term 3 ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 4.22 | Platform Aligned | 4.22 | 4.22 | 09 Jun 2026 | 31 Dec 2026 | 31 Dec 2027 | 30 Jun 2028 | 30 Jun 2029 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.21 | Platform Aligned | 4.21 | 4.21 | 10 Feb 2026 | 09 Sep 2026 | 03 Aug 2027 | N/A | N/A | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.20 | Platform Aligned | 4.20 | 4.20 | 21 Oct 2025 | 03 May 2026 | 21 Apr 2027 | 21 Oct 2027 | 21 Oct 2028 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.19 | Platform Aligned | 4.19 | 4.19 | 17 Jun 2025 | 21 Jan 2026 | 17 Dec 2026 | N/A | N/A | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.18 | Platform Aligned | 4.18 | 4.18 | 25 Feb 2025 | 17 Sep 2025 | 25 Aug 2026 | 25 Feb 2027 | 25 Feb 2028 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.16 | Platform Aligned | 4.16 | 4.16 | 27 Jun 2024 | 01 Jan 2025 | 27 Dec 2025 | 27 Jun 2026 | 27 Jun 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.14 | Platform Aligned | 4.14 | 4.14 | 31 Oct 2023 | 27 May 2024 | 01 May 2025 | 31 Oct 2025 | 31 Oct 2026 | 31 Oct 2027 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.12 | Platform Aligned | 4.12 | 4.12 | 17 Jan 2023 | 17 Aug 2023 | 17 Jul 2024 | 17 Jan 2025 | 17 Jan 2026 | 17 Jan 2027 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (5)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 4.17 | Platform Aligned | 4.17 | 4.17 | 01 Oct 2024 | 25 May 2025 | 01 Apr 2026 | N/A | N/A | N/A | 
| 4.15 | Platform Aligned | 4.15 | 4.15 | 27 Feb 2024 | 27 Sep 2024 | 27 Aug 2025 | N/A | N/A | N/A | 
| 4.13 | Platform Aligned | 4.13 | 4.13 | 17 May 2023 | 31 Jan 2024 | 17 Nov 2024 | N/A | N/A | N/A | 
| 4.11 | Platform Aligned | 4.11 | 4.11 | 10 Aug 2022 | 17 Apr 2023 | 10 Feb 2024 | N/A | N/A | N/A | 
| 4.10 | Platform Aligned | 4.10 | 4.10 | 10 Mar 2022 | 10 Nov 2022 | 10 Sep 2023 | N/A | N/A | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**4 months

| Version | Tier | Supported OpenShift versions | OpenShift Aligned Version | General availability | Full support ends | Maintenance ends | EUS ends | EUS Term 2 ends | EUS Term 3 ends | 
|---|---|---|---|---|---|---|---|---|---|
| 0.12 | Platform Aligned | 4.22 | 4.22 | 16 Jun 2026 | 31 Dec 2026 | 31 Dec 2027 | 30 Jun 2028 | 30 Jun 2029 | N/A | 
| 0.11 | Platform Aligned | 4.21 | 4.21 | 24 Feb 2026 | 09 Sep 2026 | 03 Aug 2027 | N/A | N/A | N/A | 
| 0.10 | Platform Aligned | 4.20 | 4.20 | 16 Sep 2025 | 03 May 2026 | 21 Apr 2027 | 21 Oct 2027 | 21 Oct 2028 | N/A | 
| 0.9 | Platform Aligned | 4.18 | 4.18 | 21 Jan 2025 | 16 Sep 2025 | 25 Aug 2026 | 25 Feb 2027 | 25 Feb 2028 | N/A | 
| 0.8 | Platform Aligned | 4.16 | 4.16 | 08 May 2024 | 21 Jan 2025 | 27 Dec 2025 | 27 Jun 2026 | 27 Jun 2027 | N/A | 
| 0.6 | Platform Aligned | 4.14 | 4.14 | 12 Sep 2023 | 08 Nov 2023 | 01 May 2025 | 31 Oct 2025 | 31 Oct 2026 | N/A | 
| 0.4 | Platform Aligned | 4.12 | 4.12 | 10 Jan 2023 | 08 Nov 2023 | 17 Jul 2024 | 17 Jan 2025 | 17 Jan 2026 | 18 Jan 2027 | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**4 months

**Valid Subscriptions:**OpenShift Kubernetes Engine / OpenShift Container Platform / OpenShift Platform Plus

| Version | Tier | Supported OpenShift versions | OpenShift Aligned Version | General availability | Full support ends | Maintenance ends | EUS ends | EUS Term 2 ends | EUS Term 3 ends | 
|---|---|---|---|---|---|---|---|---|---|
| 5.7 | Platform Aligned | 4.22 | 4.22 | 16 Jun 2026 | 31 Dec 2026 | 31 Dec 2027 | 30 Jun 2028 | 30 Jun 2029 | N/A | 
| 5.6 | Platform Aligned | 4.21 | 4.21 | 24 Feb 2026 | 09 Sep 2026 | 03 Aug 2027 | N/A | N/A | N/A | 
| 5.5 | Platform Aligned | 4.20 | 4.20 | 24 Nov 2025 | 03 May 2026 | 21 Apr 2027 | 21 Oct 2027 | 21 Oct 2028 | N/A | 
| 5.4 | Platform Aligned | 4.18 | 4.18 | 21 Jan 2025 | 24 Nov 2025 | 25 Aug 2026 | 25 Feb 2027 | 25 Feb 2028 | N/A | 
| 5.3 | Platform Aligned | 4.16 | 4.16 | 20 Feb 2024 | 21 Jan 2025 | 27 Dec 2025 | 27 Jun 2026 | 27 Jun 2027 | N/A | 
| 5.2 | Platform Aligned | 4.14 | 4.14 | 12 Sep 2023 | 20 Feb 2024 | 01 May 2025 | 31 Oct 2025 | 31 Oct 2026 | N/A | 
| 5.0 | Platform Aligned | 4.12 | 4.12 | 10 Jan 2023 | 02 May 2023 | 17 Jul 2024 | 17 Jan 2025 | 17 Jan 2026 | 18 Jan 2027 | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**4 months

**Valid Subscriptions:**OpenShift Kubernetes Engine / OpenShift Container Platform / OpenShift Platform Plus

| Version | Tier | Supported OpenShift versions | OpenShift Aligned Version | General availability | Full support ends | Maintenance ends | EUS ends | EUS Term 2 ends | EUS Term 3 ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 4.22 | Platform Aligned | 4.22 | 4.22 | 09 Jun 2026 | 31 Dec 2026 | 31 Dec 2027 | 30 Jun 2028 | 30 Jun 2029 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.21 | Platform Aligned | 4.21 | 4.21 | 03 Feb 2026 | 09 Sep 2026 | 03 Aug 2027 | N/A | N/A | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.20 | Platform Aligned | 4.20 | 4.20 | 21 Oct 2025 | 03 May 2026 | 21 Apr 2027 | 21 Oct 2027 | 21 Oct 2028 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.19 | Platform Aligned | 4.19 | 4.19 | 17 Jun 2025 | 21 Jan 2026 | 17 Dec 2026 | N/A | N/A | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.18 | Platform Aligned | 4.18 | 4.18 | 25 Feb 2025 | 17 Sep 2025 | 25 Aug 2026 | 25 Feb 2027 | 25 Feb 2028 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.16 | Platform Aligned | 4.16 | 4.16 | 27 Jun 2024 | 01 Jan 2025 | 27 Dec 2025 | 27 Jun 2026 | 27 Jun 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.14 | Platform Aligned | 4.14 | 4.14 | 01 Nov 2023 | 27 May 2024 | 01 May 2025 | 31 Oct 2025 | 31 Oct 2026 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.12 | Platform Aligned | 4.12 | 4.12 | 17 Jan 2023 | 17 Aug 2023 | 17 Jul 2024 | 17 Jan 2025 | 17 Jan 2026 | 17 Jan 2027 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (3)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 4.17 | Platform Aligned | 4.17 | 4.17 | 01 Oct 2024 | 25 May 2025 | 01 Apr 2026 | N/A | N/A | N/A | 
| 4.15 | Platform Aligned | 4.15 | 4.15 | 27 Feb 2024 | 27 Sep 2024 | 27 Aug 2025 | N/A | N/A | N/A | 
| 4.13 | Platform Aligned | 4.13 | 4.13 | 17 May 2023 | 31 Jan 2024 | 17 Nov 2024 | N/A | N/A | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**4 months

**Valid Subscriptions:**OpenShift Kubernetes Engine / OpenShift Container Platform / OpenShift Platform Plus

| Version | Tier | Supported OpenShift versions | OpenShift Aligned Version | General availability | Full support ends | Maintenance ends | EUS ends | EUS Term 2 ends | EUS Term 3 ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 4.22 | Platform Aligned | 4.22 | 4.22 | 09 Jun 2026 | 31 Dec 2026 | 31 Dec 2027 | 30 Jun 2028 | 30 Jun 2029 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.21 | Platform Aligned | 4.21 | 4.21 | 03 Feb 2026 | 09 Sep 2026 | 03 Aug 2027 | N/A | N/A | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.20 | Platform Aligned | 4.20 | 4.20 | 21 Oct 2025 | 03 May 2026 | 21 Apr 2027 | 21 Oct 2027 | 21 Oct 2028 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.19 | Platform Aligned | 4.19 | 4.19 | 17 Jun 2025 | 21 Jan 2026 | 17 Dec 2026 | N/A | N/A | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.18 | Platform Aligned | 4.18 | 4.18 | 25 Feb 2025 | 17 Sep 2025 | 25 Aug 2026 | 25 Feb 2027 | 25 Feb 2028 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.16 | Platform Aligned | 4.16 | 4.16 | 27 Jun 2024 | 01 Jan 2025 | 27 Dec 2025 | 27 Jun 2026 | 27 Jun 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.14 | Platform Aligned | 4.14 | 4.14 | 31 Oct 2023 | 27 May 2024 | 01 May 2025 | 31 Oct 2025 | 31 Oct 2026 | 31 Oct 2027 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.12 | Platform Aligned | 4.12 | 4.12 | 17 Jan 2023 | 17 Aug 2023 | 17 Jul 2024 | 17 Jan 2025 | 17 Jan 2026 | 17 Jan 2027 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (4)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 4.17 | Platform Aligned | 4.17 | 4.17 | 01 Oct 2024 | 25 May 2025 | 01 Apr 2026 | N/A | N/A | N/A | 
| 4.15 | Platform Aligned | 4.15 | 4.15 | 27 Feb 2024 | 27 Sep 2024 | 27 Aug 2025 | N/A | N/A | N/A | 
| 4.13 | Platform Aligned | 4.13 | 4.13 | 17 May 2023 | 31 Jan 2024 | 17 Nov 2024 | N/A | N/A | N/A | 
| 4.11 | Platform Aligned | 4.11 | 4.11 | 10 Aug 2022 | 17 Apr 2023 | 10 Feb 2024 | N/A | N/A | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**4 months

**Valid Subscriptions:**OpenShift Kubernetes Engine / OpenShift Container Platform / OpenShift Platform Plus

| Version | Tier | Supported OpenShift versions | OpenShift Aligned Version | General availability | Full support ends | Maintenance ends | EUS ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 10.22 | Platform Aligned | 4.22 | 4.22 | 09 Jun 2026 | 31 Dec 2026 | 31 Dec 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 10.21 | Platform Aligned | 4.21 | 4.21 | 03 Feb 2026 | 09 Sep 2026 | 03 Aug 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 10.20 | Platform Aligned | 4.20 | 4.20 | 22 Oct 2025 | 03 May 2026 | 21 Apr 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 10.19 | Platform Aligned | 4.19 | 4.19 | 17 Jul 2025 | 21 Jan 2026 | 17 Dec 2026 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 10.18 | Platform Aligned | 4.18 | 4.18 | 20 Mar 2025 | 17 Oct 2025 | 25 Aug 2026 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 9.0 | Platform Aligned | 4.14 | 4.14 | 27 Nov 2023 | 27 Feb 2024 | 31 Oct 2026 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **Previous operator releases without a tiered strategy** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 7.2 | N/A | 4.12 | 4.12 | 30 Jan 2023 | 10 May 2023 | 17 Jul 2024 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (10)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 10.17 | Platform Aligned | 4.17 | 4.17 | 01 Oct 2024 | 20 Jun 2025 | 01 Apr 2026 | N/A | 
| 10.16 | Platform Aligned | 4.16 | 4.16 | 05 Aug 2024 | 01 Jan 2025 | 27 Dec 2025 | N/A | 
| 10.15 | Platform Aligned | 4.15 | 4.15 | 26 Feb 2024 | 27 Jun 2024 | 27 Aug 2025 | N/A | 
| 8.1 | N/A | 4.13 | 4.13 | 10 May 2023 | 31 Oct 2023 | 17 Nov 2024 | N/A | 
| 6.0 | N/A | 4.11 | 4.11 | 23 Aug 2022 | 30 Jan 2023 | 10 Feb 2024 | N/A | 
| 5.1 | N/A | 4.10 | 4.10 | 28 Mar 2022 | 23 Aug 2022 | 10 Sep 2023 | N/A | 
| 4.0 | N/A | 4.9 | 4.9 | 28 Oct 2021 | 28 Mar 2022 | 18 Apr 2023 | N/A | 
| 3.1 | N/A | 4.8 | 4.8 | 04 Aug 2021 | 28 Oct 2021 | 27 Jan 2023 | N/A | 
| 2.0 | N/A | 4.7 | 4.7 | 02 Mar 2021 | 04 Aug 2021 | 24 Aug 2022 | N/A | 
| 1.0 | N/A | 4.6 | 4.6 | 16 Dec 2020 | 02 Mar 2021 | 18 Oct 2021 | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**4 months

**Valid Subscriptions:**Red Hat OpenShift support for Windows Containers

| Version | Tier | Supported OpenShift versions | OpenShift Aligned Version | General availability | Full support ends | Maintenance ends | EUS ends | EUS Term 2 ends | EUS Term 3 ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 4.22 | Platform Aligned | 4.22 | 4.22 | 16 Jun 2026 | 31 Dec 2026 | 31 Dec 2027 | 30 Jun 2028 | 30 Jun 2029 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.21 | Platform Aligned | 4.21 | 4.21 | 12 Feb 2026 | 09 Sep 2026 | 03 Aug 2027 | N/A | N/A | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.20 | Platform Aligned | 4.20 | 4.20 | 21 Oct 2025 | 03 May 2026 | 21 Apr 2027 | 21 Oct 2027 | 21 Oct 2028 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.19 | Platform Aligned | 4.19 | 4.19 | 17 Jun 2025 | 21 Jan 2026 | 17 Dec 2026 | N/A | N/A | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.18 | Platform Aligned | 4.18 | 4.18 | 25 Feb 2025 | 17 Sep 2025 | 25 Aug 2026 | 25 Feb 2027 | 25 Feb 2028 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.16 | Platform Aligned | 4.16 | 4.16 | 09 Jul 2024 | 15 Jan 2025 | 09 Jan 2026 | 09 Jul 2026 | 09 Jul 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.14 | Platform Aligned | 4.14 | 4.14 | 08 Nov 2023 | 28 May 2024 | 01 May 2025 | 31 Oct 2025 | 31 Oct 2026 | 31 Oct 2027 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.12 | Platform Aligned | 4.12 | 4.12 | 24 Jan 2023 | 17 Aug 2023 | 24 Jul 2024 | 24 Jan 2025 | 24 Jan 2026 | 17 Jan 2027 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (10)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 4.17 | Platform Aligned | 4.17 | 4.17 | 15 Oct 2024 | 25 May 2025 | 15 Apr 2026 | N/A | N/A | N/A | 
| 4.15 | Platform Aligned | 4.15 | 4.15 | 28 Feb 2024 | 09 Oct 2024 | 28 Aug 2025 | N/A | N/A | N/A | 
| 4.13 | N/A | 4.13 | 4.13 | 17 May 2023 | 31 Jan 2024 | 17 Nov 2024 | N/A | N/A | N/A | 
| 4.11 | N/A | 4.11 | 4.11 | 15 Sep 2022 | 24 Apr 2023 | 12 Mar 2024 | N/A | N/A | N/A | 
| 4.10 | N/A | 4.10 | 4.10 | 16 Mar 2022 | 12 Dec 2022 | 12 Sep 2023 | N/A | N/A | N/A | 
| 4.9 | N/A | 4.9 | 4.9 | 03 Nov 2021 | 16 Apr 2022 | 24 Jan 2023 | N/A | N/A | N/A | 
| 4.8 | N/A | 4.8 | 4.8 | 28 Jul 2021 | 02 Dec 2021 | 15 Sep 2022 | N/A | N/A | N/A | 
| 2.6 | N/A | 4.7 | 4.7 | 10 Mar 2021 | 27 Aug 2021 | 16 Mar 2022 | N/A | N/A | N/A | 
| 2.5 | N/A | 4.6 | 4.6 | 16 Nov 2020 | 09 Apr 2021 | 02 Nov 2021 | N/A | N/A | N/A | 
| 2.4 | N/A | 4.5 | 4.5 | 29 Jul 2020 | 16 Dec 2020 | 28 Jul 2021 | N/A | N/A | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**4 months

**Valid Subscriptions:**OpenShift Kubernetes Engine / OpenShift Container Platform / OpenShift Platform Plus

| Version | Tier | Supported OpenShift versions | OpenShift Aligned Version | General availability | Full support ends | Maintenance ends | EUS ends | EUS Term 2 ends | EUS Term 3 ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 4.22 | Platform Aligned | 4.22 | 4.22 | 09 Jun 2026 | 31 Dec 2026 | 31 Dec 2027 | 30 Jun 2028 | 30 Jun 2029 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.21 | Platform Aligned | 4.21 | 4.21 | 10 Feb 2026 | 09 Sep 2026 | 03 Aug 2027 | N/A | N/A | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.20 | Platform Aligned | 4.20 | 4.20 | 21 Oct 2025 | 03 May 2026 | 21 Apr 2027 | 21 Oct 2027 | 21 Oct 2028 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.19 | Platform Aligned | 4.19 | 4.19 | 17 Jun 2025 | 21 Jan 2026 | 17 Dec 2026 | N/A | N/A | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.18 | Platform Aligned | 4.18 | 4.18 | 25 Feb 2025 | 17 Sep 2025 | 25 Aug 2026 | 25 Feb 2027 | 25 Feb 2028 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.16 | Platform Aligned | 4.16 | 4.16 | 27 Jun 2024 | 01 Jan 2025 | 27 Dec 2025 | 27 Jun 2026 | 27 Jun 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.14 | Platform Aligned | 4.14 | 4.14 | 31 Oct 2023 | 27 May 2024 | 01 May 2025 | 31 Oct 2025 | 31 Oct 2026 | 31 Oct 2027 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (2)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 4.17 | Platform Aligned | 4.17 | 4.17 | 01 Oct 2024 | 25 May 2025 | 01 Apr 2026 | N/A | N/A | N/A | 
| 4.15 | Platform Aligned | 4.15 | 4.15 | 27 Feb 2024 | 27 Sep 2024 | 27 Aug 2025 | N/A | N/A | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**4 months

**Valid Subscriptions:**OpenShift Kubernetes Engine / OpenShift Container Platform / OpenShift Platform Plus

| Version | Tier | Supported OpenShift versions | OpenShift Aligned Version | General availability | Full support ends | Maintenance ends | EUS ends | EUS Term 2 ends | EUS Term 3 ends | 
|---|---|---|---|---|---|---|---|---|---|
| 0.13 | Platform Aligned | 4.22 | 4.22 | 16 Jun 2026 | 31 Dec 2026 | 31 Dec 2027 | 30 Jun 2028 | 30 Jun 2029 | N/A | 
| 0.12 | Platform Aligned | 4.21 | 4.21 | 24 Feb 2026 | 09 Sep 2026 | 03 Aug 2027 | N/A | N/A | N/A | 
| 0.11 | Platform Aligned | 4.20 | 4.20 | 24 Nov 2025 | 03 May 2026 | 21 Apr 2027 | 21 Oct 2027 | 21 Oct 2028 | N/A | 
| 0.10 | Platform Aligned | 4.18 | 4.18 | 21 Jan 2025 | 24 Nov 2025 | 25 Aug 2026 | 25 Feb 2027 | 25 Feb 2028 | N/A | 
| 0.9 | Platform Aligned | 4.16 | 4.16 | 17 Jul 2024 | 21 Jan 2025 | 27 Dec 2025 | 27 Jun 2026 | 27 Jun 2027 | N/A | 
| 0.7 | Platform Aligned | 4.14 | 4.14 | 12 Sep 2023 | 20 Feb 2024 | 01 May 2025 | 31 Oct 2025 | 31 Oct 2026 | N/A | 
| 0.5 | Platform Aligned | 4.12 | 4.12 | 10 Jan 2023 | 23 Oct 2023 | 17 Jul 2024 | 17 Jan 2025 | 17 Jan 2026 | 18 Jan 2027 | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**4 months

**Valid Subscriptions:**OpenShift Kubernetes Engine / OpenShift Container Platform / OpenShift Platform Plus

| Version | Tier | Supported OpenShift versions | OpenShift Aligned Version | General availability | Full support ends | Maintenance ends | EUS ends | EUS Term 2 ends | EUS Term 3 ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 4.22 | Platform Aligned | 4.22 | 4.22 | 09 Jun 2026 | 31 Dec 2026 | 31 Dec 2027 | 30 Jun 2028 | 30 Jun 2029 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.21 | Platform Aligned | 4.21 | 4.21 | 03 Feb 2026 | 09 Sep 2026 | 03 Aug 2027 | N/A | N/A | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.20 | Platform Aligned | 4.20 | 4.20 | 21 Oct 2025 | 03 May 2026 | 21 Apr 2027 | 21 Oct 2027 | 21 Oct 2028 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.19 | Platform Aligned | 4.19 | 4.19 | 17 Jun 2025 | 21 Jan 2026 | 17 Dec 2026 | N/A | N/A | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.18 | Platform Aligned | 4.18 | 4.18 | 25 Feb 2025 | 17 Sep 2025 | 25 Aug 2026 | 25 Feb 2027 | 25 Feb 2028 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.16 | Platform Aligned | 4.16 | 4.16 | 27 Jun 2024 | 01 Jan 2025 | 27 Dec 2025 | 27 Jun 2026 | 27 Jun 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.14 | Platform Aligned | 4.14 | 4.14 | 31 Oct 2023 | 27 May 2024 | 01 May 2025 | 31 Oct 2025 | 31 Oct 2026 | 31 Oct 2027 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.12 | Platform Aligned | 4.12 | 4.12 | 17 Jan 2023 | 17 Aug 2023 | 17 Jul 2024 | 17 Jan 2025 | 17 Jan 2026 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (3)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 4.17 | Platform Aligned | 4.17 | 4.17 | 01 Oct 2024 | 25 May 2025 | 01 Apr 2026 | N/A | N/A | N/A | 
| 4.15 | Platform Aligned | 4.15 | 4.15 | 27 Feb 2024 | 27 Sep 2024 | 27 Aug 2025 | N/A | N/A | N/A | 
| 4.13 | Platform Aligned | 4.13 | 4.13 | 17 May 2023 | 31 Jan 2024 | 17 Nov 2024 | N/A | N/A | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**4 months

**Valid Subscriptions:**OpenShift Kubernetes Engine / OpenShift Container Platform / OpenShift Platform Plus

| Version | Tier | Supported OpenShift versions | OpenShift Aligned Version | General availability | Full support ends | Maintenance ends | EUS ends | EUS Term 2 ends | 
|---|---|---|---|---|---|---|---|---|
| 0.3 | Platform Aligned | 4.22 | 4.22 | 16 Jun 2026 | 31 Dec 2026 | 31 Dec 2027 | 30 Jun 2028 | 30 Jun 2029 | 

**Additional Links:**Operator Update Information Checker

**Valid Subscriptions:**OpenShift Kubernetes Engine / OpenShift Container Platform / OpenShift Platform Plus

| Version | Tier | Supported OpenShift versions | OpenShift Aligned Version | General availability | Full support ends | Maintenance ends | EUS ends | EUS Term 2 ends | EUS Term 3 ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 4.22 | Platform Aligned | 4.22 | 4.22 | 09 Jun 2026 | 31 Dec 2026 | 31 Dec 2027 | 30 Jun 2028 | 30 Jun 2029 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.21 | Platform Aligned | 4.21 | 4.21 | 03 Feb 2026 | 09 Sep 2026 | 03 Aug 2027 | N/A | N/A | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.20 | Platform Aligned | 4.20 | 4.20 | 21 Oct 2025 | 03 May 2026 | 21 Apr 2027 | 21 Oct 2027 | 21 Oct 2028 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.19 | Platform Aligned | 4.19 | 4.19 | 17 Jun 2025 | 21 Jan 2026 | 17 Dec 2026 | N/A | N/A | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.18 | Platform Aligned | 4.18 | 4.18 | 25 Feb 2025 | 17 Sep 2025 | 25 Aug 2026 | 25 Feb 2027 | 25 Feb 2028 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.16 | Platform Aligned | 4.16 | 4.16 | 27 Jun 2024 | 01 Jan 2025 | 27 Dec 2025 | 27 Jun 2026 | 27 Jun 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.14 | Platform Aligned | 4.14 | 4.14 | 31 Oct 2023 | 27 Jun 2024 | 01 May 2025 | 31 Oct 2025 | 31 Oct 2026 | 31 Oct 2027 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.12 | Platform Aligned | 4.12 | 4.12 | 17 Jan 2023 | 17 Aug 2023 | 17 Jul 2024 | 17 Jan 2025 | 17 Jan 2026 | 18 Jan 2027 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (3)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 4.17 | Platform Aligned | 4.17 | 4.17 | 01 Oct 2024 | 25 May 2025 | 01 Apr 2026 | N/A | N/A | N/A | 
| 4.15 | Platform Aligned | 4.15 | 4.15 | 27 Feb 2024 | 27 Sep 2024 | 27 Aug 2025 | N/A | N/A | N/A | 
| 4.13 | Platform Aligned | 4.13 | 4.13 | 17 May 2023 | 31 Jan 2024 | 17 Nov 2024 | N/A | N/A | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**4 months

**Valid Subscriptions:**OpenShift Container Platform / OpenShift Platform Plus

| Version | Tier | Supported OpenShift versions | OpenShift Aligned Version | General availability | Full support ends | Maintenance ends | EUS ends | EUS Term 2 ends | EUS Term 3 ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 4.22 | Platform Aligned | 4.22 | 4.22 | 09 Jun 2026 | 31 Dec 2026 | 31 Dec 2027 | 30 Jun 2028 | 30 Jun 2029 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.21 | Platform Aligned | 4.21 | 4.21 | 10 Feb 2026 | 09 Sep 2026 | 03 Aug 2027 | N/A | N/A | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.20 | Platform Aligned | 4.20 | 4.20 | 21 Oct 2025 | 03 May 2026 | 21 Apr 2027 | 21 Oct 2027 | 21 Oct 2028 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.19 | Platform Aligned | 4.19 | 4.19 | 17 Jun 2025 | 21 Jan 2026 | 17 Dec 2026 | N/A | N/A | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.18 | Platform Aligned | 4.18 | 4.18 | 25 Feb 2025 | 17 Sep 2025 | 25 Aug 2026 | 25 Feb 2027 | 25 Feb 2028 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.16 | Platform Aligned | 4.16 | 4.16 | 27 Jun 2024 | 01 Jan 2025 | 27 Dec 2025 | 27 Jun 2026 | 27 Jun 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.14 | Platform Aligned | 4.14 | 4.14 | 31 Oct 2023 | 27 May 2024 | 01 May 2025 | 31 Oct 2025 | 31 Oct 2026 | 31 Oct 2027 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.12 | Platform Aligned | 4.12 | 4.12 | 17 Jan 2023 | 17 Aug 2023 | 17 Jul 2024 | 17 Jan 2025 | 17 Jan 2026 | 17 Jan 2027 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (5)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 4.17 | Platform Aligned | 4.17 | 4.17 | 01 Oct 2024 | 25 May 2025 | 01 Apr 2026 | N/A | N/A | N/A | 
| 4.15 | Platform Aligned | 4.15 | 4.15 | 27 Mar 2024 | 27 Sep 2024 | 27 Aug 2025 | N/A | N/A | N/A | 
| 4.13 | Platform Aligned | 4.13 | 4.13 | 17 May 2023 | 31 Jan 2024 | 17 Nov 2024 | N/A | N/A | N/A | 
| 4.11 | Platform Aligned | 4.11 | 4.11 | 10 Mar 2022 | 17 Apr 2023 | 10 Feb 2024 | N/A | N/A | N/A | 
| 4.10 | Platform Aligned | 4.10 | 4.10 | 10 Mar 2022 | 10 Nov 2022 | 10 Sep 2023 | N/A | N/A | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**4 months

**Valid Subscriptions:**OpenShift Kubernetes Engine / OpenShift Container Platform / OpenShift Platform Plus

# Platform Agnostic Operators

The following operators are released independent of OpenShift Container Platform releases, allowing for an increased frequency to introduce new features.

Operators will typically have multiple minor version branches supported in parallel on an OCP release, but each will generally have a shorter life cycle than that of a given OCP release. Customers can select the desired minor version using the respective OLM release channel of the operator package. Customers need to anticipate the need to update to a newer minor version of the operator at the end of the operator lifecycle of the current version or when planning to update the OCP cluster to stay supported. While a given operator minor version may not support the latest available OCP release, there will always be a version of the operator available for every supported version of OpenShift at any given point in time.

#### logging for Red Hat OpenShift

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 6.6 | Platform Agnostic | 4.20, 4.21, 4.22 | 14 Jul 2026 | 31 Dec 2026 | 31 Dec 2027 | 30 Jun 2029 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 6.5 | Platform Agnostic | 4.19, 4.20, 4.21, 4.22 | 01 Apr 2026 | 14 Aug 2026 | 17 Dec 2026 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 6.2 | Platform Agnostic | 4.16, 4.17, 4.18, 4.19, 4.20 | 12 Mar 2025 | 16 Aug 2025 | 25 Aug 2026 | 21 Oct 2028 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 6.0 | Platform Agnostic | 4.14, 4.15, 4.16, 4.17 | 24 Sep 2024 | 13 Dec 2024 | 27 Dec 2025 | 27 Jun 2027 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (13)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 6.4 | Platform Agnostic | 4.18, 4.19, 4.20, 4.21 | 13 Nov 2025 | 01 May 2026 | 14 Jul 2026 | N/A | 
| 6.3 | Platform Agnostic | 4.17, 4.18, 4.19, 4.20 | 16 Jul 2025 | 13 Dec 2025 | 01 Apr 2026 | N/A | 
| 6.1 | Platform Agnostic | 4.15, 4.16, 4.17, 4.18 | 13 Nov 2024 | 12 Apr 2025 | 13 Nov 2025 | N/A | 
| 5.9 | Platform Agnostic | 4.13, 4.14, 4.15, 4.16 | 04 Apr 2024 | 24 Oct 2024 | 03 Nov 2025 | N/A | 
| 5.8 | Platform Agnostic | 4.12, 4.13, 4.14, 4.15, 4.16, 4.17 | 02 Nov 2023 | 05 May 2024 | 03 Nov 2025 | N/A | 
| 5.7 | N/A | 4.11, 4.12, 4.13, 4.14 | 10 May 2023 | 04 Dec 2023 | 24 Sep 2024 | N/A | 
| 5.6 | N/A | 4.10, 4.11, 4.12, 4.13 | 19 Jan 2023 | 10 Jun 2023 | 18 Jan 2025 | N/A | 
| 5.5 | N/A | 4.9, 4.10, 4.11, 4.12 | 18 Aug 2022 | 19 Feb 2023 | 02 Nov 2023 | N/A | 
| 5.4 | N/A | 4.8, 4.9, 4.10, 4.11 | 20 Apr 2022 | 18 Sep 2022 | 10 May 2023 | N/A | 
| 5.3 | N/A | 4.8, 4.9, 4.10 | 15 Nov 2021 | 20 May 2022 | 19 Jan 2023 | N/A | 
| 5.2 | N/A | 4.7, 4.8, 4.9 | 07 Sep 2021 | 15 Dec 2021 | 24 Aug 2022 | N/A | 
| 5.1 | N/A | 4.7, 4.8 | 21 Jul 2021 | 07 Sep 2021 | 20 Apr 2022 | N/A | 
| 5.0 | N/A | 4.7 | 24 Feb 2021 | 21 Aug 2021 | 15 Nov 2021 | N/A | 

**Estimated release cadence:**4 months

**Valid Subscriptions:**OpenShift Kubernetes Engine / OpenShift Container Platform / OpenShift Platform Plus

#### Loki operator

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 6.6 | Platform Agnostic | 4.20, 4.21, 4.22 | 14 Jul 2026 | 31 Dec 2026 | 31 Dec 2027 | 30 Jun 2029 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 6.5 | Platform Agnostic | 4.19, 4.20, 4.21, 4.22 | 01 Apr 2026 | 14 Aug 2026 | 17 Dec 2026 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 6.2 | Platform Agnostic | 4.16, 4.17, 4.18, 4.19, 4.20 | 12 Mar 2025 | 16 Aug 2025 | 25 Aug 2026 | 21 Oct 2028 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 6.0 | Platform Agnostic | 4.14, 4.15, 4.16, 4.17 | 24 Sep 2024 | 13 Dec 2024 | 27 Dec 2025 | 27 Jun 2027 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (5)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 6.4 | Platform Agnostic | 4.18, 4.19, 4.20, 4.21 | 13 Nov 2025 | 01 May 2026 | 14 Jul 2026 | N/A | 
| 6.3 | Platform Agnostic | 4.17, 4.18, 4.19, 4.20 | 16 Jul 2025 | 13 Dec 2025 | 01 Apr 2026 | N/A | 
| 6.1 | Platform Agnostic | 4.15, 4.16, 4.17, 4.18 | 13 Nov 2024 | 12 Apr 2025 | 13 Nov 2025 | N/A | 
| 5.9 | Platform Agnostic | 4.13, 4.14, 4.15, 4.16 | 04 Apr 2024 | 24 Oct 2024 | 03 Nov 2025 | N/A | 
| 5.8 | Platform Agnostic | 4.12, 4.13, 4.14, 4.15 | 02 Nov 2023 | 05 May 2024 | 03 Nov 2025 | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**4 months

**Valid Subscriptions:**OpenShift Kubernetes Engine / OpenShift Container Platform / OpenShift Platform Plus

#### Red Hat OpenShift Service Mesh

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3.5 | Platform Agnostic | 4.20, 4.21, 4.22, 5.0 | 29 Oct 2026 | 29 Apr 2027 | 21 Oct 2028 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 3.4 | Platform Agnostic | 4.20, 4.21, 4.22, 5.0 | 09 Jul 2026 | 11 Jan 2027 | 21 Oct 2028 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 3.3 | Platform Agnostic | 4.18, 4.19, 4.20, 4.21, 4.22 | 19 Mar 2026 | 21 Sep 2026 | 25 Feb 2028 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 3.2 | Platform Agnostic | 4.18, 4.19, 4.20, 4.21, 4.22 | 14 Nov 2025 | 14 May 2026 | 25 Aug 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 3.1 | Platform Agnostic | 4.19, 4.18, 4.17, 4.16, 4.20 | 06 Aug 2025 | 31 Jan 2026 | 27 Jul 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 3.0 | Platform Agnostic | 4.14, 4.15, 4.16, 4.17, 4.18, 4.19, 4.20 | 12 Mar 2025 | 12 Sep 2025 | 31 Oct 2026 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 2.6 | Platform Agnostic | 4.14, 4.15, 4.16, 4.17, 4.18, 4.19, 4.20 | 08 Aug 2024 | 12 Apr 2025 | 30 Jun 2026 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (8)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 2.5 | Platform Agnostic | 4.15, 4.14, 4.13, 4.12, 4.16 | 19 Mar 2024 | 08 Sep 2024 | 19 Sep 2025 | N/A | 
| 2.4 | N/A | 4.10, 4.11, 4.12, 4.13, 4.14 | 15 Jun 2023 | 19 Apr 2024 | 12 Mar 2025 | N/A | 
| 2.3 | N/A | 4.9, 4.10, 4.11, 4.12, 4.13, 4.14 | 16 Nov 2022 | 15 Jul 2023 | 08 Aug 2024 | N/A | 
| 2.2 | N/A | 4.9, 4.10, 4.11, 4.12, 4.13, 4.14 | 30 Jun 2022 | 16 Dec 2022 | 19 Mar 2024 | N/A | 
| 2.1 | N/A | 4.6, 4.7, 4.8, 4.9, 4.10, 4.11, 4.12 | 03 Nov 2021 | 30 Jul 2022 | 15 Jun 2023 | N/A | 
| 2.0 | N/A | 4.6, 4.7, 4.8 | 28 Oct 2020 | 03 Dec 2021 | 16 Nov 2022 | N/A | 
| 1.1 | N/A | 4.3, 4.4, 4.5, 4.6 | 09 Apr 2020 | 28 Nov 2020 | 30 Jun 2022 | N/A | 
| 1.0 | N/A | 4.1, 4.2, 4.3 | 04 Sep 2019 | 09 May 2020 | 22 Oct 2020 | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**6 months

**Operators sharing this lifecycle:**

- Red Hat OpenShift Service Mesh (servicemeshoperator) — Update Info
- Red Hat OpenShift Service Mesh 3 (servicemeshoperator3) — Update Info

#### Kiali

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2.33 | Platform Agnostic | 4.20, 4.21, 4.22, 5.0 | 29 Oct 2026 | 29 Apr 2027 | 21 Oct 2028 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 2.27 | Platform Agnostic | 4.20, 4.21, 4.22, 5.0 | 09 Jul 2026 | 11 Jan 2027 | 21 Oct 2028 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 2.22 | Platform Agnostic | 4.18, 4.19, 4.20, 4.21, 4.22 | 19 Mar 2026 | 21 Sep 2026 | 25 Feb 2028 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 2.17 | Platform Agnostic | 4.18, 4.19, 4.20, 4.21, 4.22 | 14 Nov 2025 | 14 May 2026 | 25 Aug 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 2.11 | Platform Agnostic | 4.16, 4.17, 4.18, 4.19, 4.20 | 06 Aug 2025 | 31 Jan 2026 | 27 Jul 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 2.4 | Platform Agnostic | 4.14, 4.15, 4.16, 4.17, 4.18, 4.19, 4.20 | 12 Mar 2025 | 12 Sep 2025 | 31 Oct 2026 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 1.73 | Platform Agnostic | 4.14, 4.15, 4.16, 4.17, 4.18, 4.19, 4.20 | 19 Mar 2024 | 12 Apr 2025 | 30 Jun 2026 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (7)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 1.65 | N/A | 4.10, 4.11, 4.12, 4.13 | 15 Jun 2023 | 19 Apr 2024 | 12 Mar 2025 | N/A | 
| 1.57 | N/A | 4.9, 4.10, 4.11, 4.12, 4.13 | 16 Nov 2022 | 15 Jul 2023 | 08 Aug 2024 | N/A | 
| 1.48 | N/A | 4.9, 4.10, 4.11, 4.12, 4.13 | 30 Jun 2022 | 16 Dec 2022 | 19 Mar 2024 | N/A | 
| 1.36 | N/A | 4.6, 4.7, 4.8, 4.9, 4.10, 4.11, 4.12 | 03 Nov 2021 | 30 Jul 2022 | 15 Jun 2023 | N/A | 
| 1.24 | N/A | 4.6, 4.7, 4.8 | 28 Oct 2020 | 03 Dec 2021 | 16 Nov 2022 | N/A | 
| 1.12 | N/A | 4.3, 4.4, 4.5, 4.6 | 09 Apr 2020 | 28 Nov 2020 | 30 Jun 2022 | N/A | 
| 1.0 | N/A | 4.1, 4.2, 4.3 | 04 Sep 2019 | 09 May 2020 | 22 Oct 2020 | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**4 months

**Valid Subscriptions:**OpenShift Container Platform / OpenShift Platform Plus

#### Gatekeeper operator

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3.21 | Platform Agnostic | 4.14, 4.16, 4.18, 4.19, 4.20, 4.21, 4.22, 5.0 | 13 Apr 2026 | 13 Jan 2027 | 14 Apr 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 3.20 | Platform Agnostic | 4.20, 4.19, 4.18, 4.17, 4.16, 4.14 | 18 Nov 2025 | 18 Nov 2026 | 13 Jan 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 3.19 | Platform Agnostic | 4.14, 4.16, 4.17, 4.18, 4.19 | 10 Jul 2025 | 13 Apr 2026 | 18 Nov 2026 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (5)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 3.18 | Platform Agnostic | 4.16, 4.17, 4.18, 4.14, 4.19 | 20 Mar 2025 | 18 Nov 2025 | 13 Apr 2026 | N/A | 
| 3.17 | Platform Agnostic | 4.16, 4.17, 4.18, 4.19, 4.14 | 06 Nov 2024 | 10 Jul 2025 | 18 Nov 2025 | N/A | 
| 3.15 | Platform Agnostic | 4.14, 4.16, 4.17, 4.18, 4.19 | 18 Jul 2024 | 20 Mar 2025 | 10 Jul 2025 | N/A | 
| 3.14 | N/A | 4.14, 4.15, 4.16 | 21 Mar 2024 | 22 Oct 2024 | 20 Mar 2025 | N/A | 
| 3.11 | N/A | 4.12, 4.13, 4.14 | 15 Nov 2023 | 16 Jul 2024 | 17 Jun 2025 | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**4 months

**Valid Subscriptions:**OpenShift Platform Plus / Red Hat Advanced Cluster Management for Kubernetes

#### Klusterlet

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **End of Life versions (6)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 2.5 | N/A | N/A | 12 Mar 2024 | 22 Oct 2024 | 23 Sep 2025 | N/A | 
| 2.4 | N/A | N/A | 15 Nov 2023 | 16 Jul 2024 | 17 Jun 2025 | N/A | 
| 2.3 | N/A | N/A | 08 Jun 2023 | 08 Feb 2024 | 08 Aug 2024 | N/A | 
| 2.2 | N/A | N/A | 06 Feb 2023 | 09 Oct 2023 | 08 Apr 2024 | N/A | 
| 2.1 | N/A | N/A | 29 Aug 2022 | 10 Mar 2023 | 13 Oct 2023 | N/A | 
| 2.0 | N/A | N/A | 06 Jun 2022 | 07 Sep 2022 | 07 Jul 2023 | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**4 months

#### Submariner

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.22 | Platform Agnostic | 4.20, 4.19, 4.18 | 04 Dec 2025 | 05 Jan 2027 | 10 Sep 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 0.20 | Platform Agnostic | 4.16, 4.17, 4.18 | 19 Mar 2025 | 17 Apr 2026 | 11 Sep 2026 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 0.19 | Platform Agnostic | 4.15, 4.16, 4.17 | 06 Nov 2024 | 08 Dec 2025 | 09 Jun 2026 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (6)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 0.18 | N/A | 4.14, 4.15, 4.16 | 18 Jul 2024 | 15 Aug 2025 | 16 Jan 2026 | N/A | 
| 0.17 | N/A | 4.14, 4.15, 4.13, 4.16 | 21 Mar 2024 | 22 Oct 2024 | 23 Sep 2025 | N/A | 
| 0.16 | N/A | 4.12, 4.13, 4.14 | 15 Nov 2023 | 16 Jul 2024 | 17 Jun 2025 | N/A | 
| 0.15 | N/A | 4.11, 4.12, 4.13 | 08 Jun 2023 | 09 Jul 2024 | 10 Dec 2024 | N/A | 
| 0.14 | N/A | 4.10, 4.11, 4.12, 4.13 | 06 Feb 2023 | 07 Mar 2024 | 09 Jul 2024 | N/A | 
| 0.13 | N/A | 4.9, 4.10, 4.11, 4.12 | 29 Aug 2022 | 11 Sep 2023 | 13 Dec 2023 | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**4 months

#### VolSync

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.16 | Platform Agnostic | 4.22, 4.21, 4.20, 5.0 | 09 Jun 2026 | 30 Sep 2026 | 04 Feb 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 0.15 | Platform Agnostic | 4.21, 4.20, 4.19, 4.22 | 04 Mar 2026 | 30 Jun 2026 | 29 Oct 2026 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (10)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 0.14 | Platform Agnostic | 4.20, 4.19, 4.18, 4.21 | 04 Dec 2025 | 31 Mar 2026 | 09 Jun 2026 | N/A | 
| 0.13 | Platform Agnostic | 4.20, 4.19, 4.18, 4.17 | 14 Jul 2025 | 31 Oct 2025 | 04 Mar 2026 | N/A | 
| 0.12 | Platform Agnostic | 4.16, 4.17, 4.18 | 20 Mar 2025 | 30 Jun 2025 | 04 Dec 2025 | N/A | 
| 0.11 | Platform Agnostic | 4.15, 4.16, 4.17 | 17 Nov 2024 | 28 Feb 2025 | 14 Jul 2025 | N/A | 
| 0.10 | N/A | 4.16, 4.15, 4.14 | 18 Jul 2024 | 31 Oct 2024 | 20 Mar 2025 | N/A | 
| 0.9 | N/A | 4.13, 4.14, 4.15 | 21 Mar 2024 | 30 Jun 2024 | 17 Nov 2024 | N/A | 
| 0.8 | N/A | 4.12, 4.13, 4.14 | 15 Nov 2023 | 29 Feb 2024 | 18 Jul 2024 | N/A | 
| 0.7 | N/A | 4.10, 4.11, 4.12, 4.13, 4.14 | 08 Jun 2023 | 30 Sep 2023 | 21 Mar 2024 | N/A | 
| 0.6 | N/A | 4.10, 4.11, 4.12, 4.13 | 06 Feb 2023 | 31 May 2023 | 21 Mar 2024 | N/A | 
| 0.5 | N/A | 4.9, 4.10, 4.11, 4.12 | 29 Aug 2022 | 30 Nov 2022 | 13 Dec 2023 | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**4 months

**Valid Subscriptions:**OpenShift Platform Plus / Red Hat Advanced Cluster Management for Kubernetes

#### multicluster global hub

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1.8 | Platform Agnostic | 4.22, 4.21, 4.20 | 18 Jul 2026 | 16 Jul 2027 | 17 Dec 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 1.7 | Platform Agnostic | 4.21, 4.20, 4.19 | 10 Mar 2026 | 09 Apr 2027 | 10 Sep 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 1.6 | Platform Agnostic | 4.20, 4.19, 4.18, 4.17, 4.21 | 04 Dec 2025 | 12 Feb 2027 | 07 Jul 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 1.5 | Platform Agnostic | 4.19, 4.18, 4.17 | 21 Jul 2025 | 02 Oct 2026 | 24 Feb 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 1.4 | Platform Agnostic | 4.15, 4.16, 4.17, 4.18 | 20 Mar 2025 | 17 Apr 2026 | 18 Sep 2026 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 1.3 | Platform Agnostic | 4.15, 4.16, 4.17, 4.18 | 06 Nov 2024 | 15 Jan 2026 | 09 Jun 2026 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (1)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 1.2 | Platform Agnostic | 4.14, 4.15, 4.16 | 18 Jul 2024 | 15 Aug 2025 | 16 Jan 2026 | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**4 months

#### Red Hat OpenShift Serverless

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1.37 | Platform Agnostic | 4.20, 4.19, 4.18, 4.17, 4.16, 4.21, 4.22, 5.0 | 24 Nov 2025 | 15 Dec 2026 | 15 Mar 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (28)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 1.36 | Platform Agnostic | 4.19, 4.18, 4.17, 4.16, 4.15, 4.14 | 17 Jul 2025 | 24 Dec 2025 | 24 Mar 2026 | N/A | 
| 1.35 | Platform Agnostic | 4.17, 4.16, 4.15, 4.14 | 22 Jan 2025 | 17 Aug 2025 | 17 Nov 2025 | N/A | 
| 1.34 | Platform Agnostic | 4.17, 4.16, 4.15, 4.14, 4.13 | 10 Oct 2024 | 22 Feb 2025 | 22 May 2025 | N/A | 
| 1.33 | Platform Agnostic | 4.16, 4.15, 4.14, 4.13, 4.12 | 20 Jun 2024 | 10 Nov 2024 | 10 Feb 2025 | N/A | 
| 1.32 | Platform Agnostic | 4.15, 4.14, 4.13, 4.12 | 14 Mar 2024 | 20 Jul 2024 | 20 Oct 2024 | N/A | 
| 1.31 | Platform Agnostic | 4.15, 4.14, 4.13, 4.12 | 12 Dec 2023 | 14 Apr 2024 | 14 Jul 2024 | N/A | 
| 1.30 | N/A | 4.11, 4.12, 4.13 | 18 Sep 2023 | 12 Dec 2023 | 12 Jan 2024 | N/A | 
| 1.29 | N/A | 4.11, 4.12, 4.13 | 05 Jun 2023 | 18 Sep 2023 | 18 Oct 2023 | N/A | 
| 1.28 | N/A | 4.8, 4.9, 4.10, 4.11, 4.12 | 05 Apr 2023 | 05 Jun 2023 | N/A | N/A | 
| 1.27 | N/A | 4.8, 4.9, 4.10, 4.11, 4.12 | 09 Feb 2023 | 05 Apr 2023 | N/A | N/A | 
| 1.26 | N/A | 4.8, 4.9, 4.10, 4.11, 4.12 | 13 Dec 2022 | 09 Feb 2023 | N/A | N/A | 
| 1.25 | N/A | 4.8, 4.9, 4.10, 4.11 | 20 Oct 2022 | 13 Dec 2022 | N/A | N/A | 
| 1.24 | N/A | 4.8, 4.9, 4.10, 4.11 | 10 Aug 2022 | 20 Oct 2022 | N/A | N/A | 
| 1.23 | N/A | 4.7, 4.8, 4.9, 4.10, 4.6 | 30 Jun 2022 | 10 Aug 2022 | N/A | N/A | 
| 1.22 | N/A | 4.7, 4.8, 4.9, 4.10, 4.6 | 09 May 2022 | 30 Jun 2022 | N/A | N/A | 
| 1.21 | N/A | 4.7, 4.8, 4.9, 4.10, 4.6 | 23 Mar 2022 | 09 May 2022 | N/A | N/A | 
| 1.20 | N/A | 4.7, 4.8, 4.9, 4.6 | 03 Feb 2022 | 24 Mar 2022 | N/A | N/A | 
| 1.19 | N/A | 4.7, 4.8, 4.9, 4.6 | 23 Nov 2021 | 03 Feb 2022 | N/A | N/A | 
| 1.18 | N/A | 4.7, 4.8, 4.9, 4.6 | 21 Oct 2021 | 23 Nov 2021 | N/A | N/A | 
| 1.17 | N/A | 4.7, 4.8, 4.6 | 16 Sep 2021 | 21 Oct 2021 | N/A | N/A | 
| 1.16 | N/A | 4.7, 4.8, 4.6 | 13 Jul 2021 | 16 Sep 2021 | N/A | N/A | 
| 1.15 | N/A | 4.7, 4.6 | 08 Jun 2021 | 13 Aug 2021 | N/A | N/A | 
| 1.14 | N/A | 4.7, 4.6 | 22 Apr 2021 | 07 Jul 2021 | N/A | N/A | 
| 1.13 | N/A | 4.7, 4.6 | 15 Feb 2021 | 22 May 2021 | N/A | N/A | 
| 1.12 | N/A | 4.6 | 14 Jan 2021 | 15 Mar 2021 | N/A | N/A | 
| 1.11 | N/A | 4.6 | 18 Nov 2020 | 14 Feb 2021 | N/A | N/A | 
| 1.10 | N/A | 4.5 | 14 Oct 2020 | 27 Nov 2020 | N/A | N/A | 
| 1.7 | N/A | 4.3, 4.4 | 29 Apr 2020 | 13 Aug 2020 | N/A | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**3 months

**Valid Subscriptions:**OpenShift Container Platform / OpenShift Platform Plus

#### Red Hat OpenShift Serverless Logic Operator

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1.37 | Platform Agnostic | 4.20, 4.19, 4.18, 4.17, 4.16 | 24 Nov 2025 | 15 Dec 2026 | 15 Mar 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (28)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 1.36 | Platform Agnostic | 4.20, 4.19, 4.18, 4.16, 4.14, 4.12 | 17 Jul 2025 | 24 Dec 2025 | 24 Mar 2026 | N/A | 
| 1.35 | N/A | N/A | 22 Jan 2025 | 17 Aug 2025 | 17 Nov 2025 | N/A | 
| 1.34 | N/A | N/A | 10 Oct 2024 | 22 Feb 2025 | 22 May 2025 | N/A | 
| 1.33 | N/A | N/A | 20 Jun 2024 | 10 Nov 2024 | 10 Feb 2025 | N/A | 
| 1.32 | N/A | N/A | 14 Mar 2024 | 20 Jul 2024 | 20 Oct 2024 | N/A | 
| 1.31 | N/A | N/A | 12 Dec 2023 | 14 Apr 2024 | 14 Jul 2024 | N/A | 
| 1.30 | N/A | N/A | 18 Sep 2023 | 12 Dec 2023 | 12 Jan 2024 | N/A | 
| 1.29 | N/A | N/A | 05 Jun 2023 | 18 Sep 2023 | 18 Oct 2023 | N/A | 
| 1.28 | N/A | N/A | 05 Apr 2023 | 05 Jun 2023 | N/A | N/A | 
| 1.27 | N/A | N/A | 09 Feb 2023 | 05 Apr 2023 | N/A | N/A | 
| 1.26 | N/A | N/A | 13 Dec 2022 | 09 Feb 2023 | N/A | N/A | 
| 1.25 | N/A | N/A | 20 Oct 2022 | 13 Dec 2022 | N/A | N/A | 
| 1.24 | N/A | N/A | 10 Aug 2022 | 20 Oct 2022 | N/A | N/A | 
| 1.23 | N/A | N/A | 30 Jun 2022 | 10 Aug 2022 | N/A | N/A | 
| 1.22 | N/A | N/A | 09 May 2022 | 30 Jun 2022 | N/A | N/A | 
| 1.21 | N/A | N/A | 23 Mar 2022 | 09 May 2022 | N/A | N/A | 
| 1.20 | N/A | N/A | 03 Feb 2022 | 24 Mar 2022 | N/A | N/A | 
| 1.19 | N/A | N/A | 23 Nov 2021 | 03 Feb 2022 | N/A | N/A | 
| 1.18 | N/A | N/A | 21 Oct 2021 | 23 Nov 2021 | N/A | N/A | 
| 1.17 | N/A | N/A | 16 Sep 2021 | 21 Oct 2021 | N/A | N/A | 
| 1.16 | N/A | N/A | 13 Jul 2021 | 16 Sep 2021 | N/A | N/A | 
| 1.15 | N/A | N/A | 08 Jun 2021 | 13 Aug 2021 | N/A | N/A | 
| 1.14 | N/A | N/A | 22 Apr 2021 | 07 Jul 2021 | N/A | N/A | 
| 1.13 | N/A | N/A | 15 Feb 2021 | 22 May 2021 | N/A | N/A | 
| 1.12 | N/A | N/A | 14 Jan 2021 | 15 Mar 2021 | N/A | N/A | 
| 1.11 | N/A | N/A | 18 Nov 2020 | 14 Feb 2021 | N/A | N/A | 
| 1.10 | N/A | N/A | 14 Oct 2020 | 27 Nov 2020 | N/A | N/A | 
| 1.7 | N/A | N/A | 29 Apr 2020 | 13 Aug 2020 | N/A | N/A | 

**Additional Links:**Operator Update Information Checker

**Valid Subscriptions:**OpenShift Container Platform / OpenShift Platform Plus

#### Red Hat Trusted Profile Analyzer

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends | 
|---|---|---|---|---|---|---|
| 3.1 | Platform Agnostic | 4.22, 4.21, 4.20, 4.19, 4.18 | 20 Aug 2026 | 20 Aug 2027 | N/A | N/A | 

**Estimated release cadence:**4 months

**Valid Subscriptions:**Red Hat Trusted Profile Analyzer

**Operators sharing this lifecycle:**

- Red Hat Trusted Profile Analyzer (rhtpa-operator) — Update Info

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends | 
|---|---|---|---|---|---|---|
| 1.3 | Platform Agnostic | 4.12, 4.14, 4.16, 4.18, 4.19, 4.20, 4.21, 4.22, 5.0 | 16 Dec 2025 | 31 Jan 2027 | 01 Jun 2027 | N/A | 
| 1.2 | Platform Agnostic | 4.20, 4.19, 4.18, 4.17 | 02 Jan 2025 | 09 Jun 2026 | 11 Jan 2027 | N/A | 
| 1.1 | Platform Agnostic | 4.20, 4.19, 4.18, 4.17, 4.16, 4.14 | 31 Oct 2023 | 03 Feb 2026 | 09 Jun 2026 | N/A | 
| 1.0 | Platform Agnostic | 4.20, 4.19, 4.18, 4.17, 4.16, 4.14 | 25 Apr 2023 | 21 Oct 2025 | 03 Feb 2026 | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**Not Specified

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1.9 | Platform Agnostic | 4.18, 4.19, 4.20, 4.21, 4.22 | 19 Aug 2026 | 31 Dec 2026 | 28 Feb 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 1.8 | Platform Agnostic | 4.17, 4.18, 4.19, 4.20, 4.21 | 18 May 2026 | 30 Sep 2026 | 31 Dec 2026 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (8)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 1.7 | Platform Agnostic | 4.16, 4.17, 4.18, 4.19, 4.20, 4.21 | 10 Feb 2026 | 18 Jun 2026 | 30 Aug 2026 | N/A | 
| 1.6 | Platform Agnostic | 4.16, 4.17, 4.18, 4.19 | 10 Oct 2025 | 10 Mar 2026 | 18 May 2026 | N/A | 
| 1.5 | Platform Agnostic | 4.16, 4.17, 4.18, 4.19 | 17 Jul 2025 | 10 Nov 2025 | 10 Feb 2026 | N/A | 
| 1.4 | Platform Agnostic | 4.18, 4.17, 4.16, 4.15 | 17 Apr 2025 | 17 Aug 2025 | 10 Oct 2025 | N/A | 
| 1.3 | Platform Agnostic | 4.14, 4.15, 4.16, 4.17, 4.18 | 22 Jan 2025 | 17 May 2025 | 10 Oct 2025 | N/A | 
| 1.2 | Platform Agnostic | 4.12, 4.14, 4.13, 4.15, 4.16, 4.17 | 26 Nov 2024 | 22 Feb 2025 | 17 Apr 2025 | N/A | 
| 1.1 | Platform Agnostic | 4.16, 4.15, 4.14, 4.13, 4.12 | 05 Aug 2024 | 26 Dec 2024 | 22 Jan 2025 | N/A | 
| 1.0 | Platform Agnostic | 4.15, 4.14, 4.13, 4.12 | 04 Dec 2023 | 05 Sep 2024 | 26 Nov 2024 | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**Not Specified

**Valid Subscriptions:**OpenShift Container Platform / OpenShift Platform Plus

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends | 
|---|---|---|---|---|---|---|
| 7.0 | Platform Agnostic | N/A | 30 May 2018 | 31 May 2022 | 31 May 2024 | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**Not Specified

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1.20 | Platform Agnostic | 4.19, 4.20, 4.21, 4.22, 5.0 | 02 Jul 2026 | 15 Nov 2026 | 15 Mar 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 1.19 | Platform Agnostic | 4.18, 4.19, 4.20, 4.21, 4.22 | 20 Apr 2026 | 02 Aug 2026 | 31 Oct 2026 | 25 Feb 2028 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 1.18 | Platform Agnostic | 4.17, 4.18, 4.19, 4.20, 4.21 | 30 Oct 2025 | 20 May 2026 | 02 Aug 2026 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 1.17 | Platform Agnostic | 4.16, 4.17, 4.18, 4.19, 4.20 | 06 Aug 2025 | 30 Nov 2025 | 20 May 2026 | 27 Jul 2027 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (7)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 1.16 | Platform Agnostic | 4.14, 4.15, 4.16, 4.17, 4.18, 4.19 | 27 May 2025 | 06 Sep 2025 | 30 Nov 2025 | N/A | 
| 1.15 | Platform Agnostic | 4.14, 4.15, 4.16, 4.17, 4.18, 4.19 | 22 Jan 2025 | 27 Jun 2025 | 06 Aug 2025 | N/A | 
| 1.14 | Platform Agnostic | 4.14, 4.15, 4.16, 4.17 | 08 Jul 2024 | 21 Feb 2025 | 27 May 2025 | N/A | 
| 1.13 | Platform Agnostic | 4.13, 4.14, 4.15, 4.16 | 16 Jan 2024 | 30 Apr 2024 | 30 Oct 2024 | N/A | 
| 1.12 | N/A | 4.12, 4.13, 4.14 | 02 Oct 2023 | 31 Jan 2024 | 30 Apr 2024 | N/A | 
| 1.11 | N/A | 4.12, 4.13, 4.14 | 05 Jun 2023 | 30 Sep 2023 | 31 Dec 2023 | N/A | 
| 1.10 | N/A | 4.12, 4.13 | 23 Mar 2023 | 30 Jun 2023 | 30 Sep 2023 | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**3 months

**Valid Subscriptions:**OpenShift Kubernetes Engine / OpenShift Container Platform / OpenShift Platform Plus

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends | 
|---|---|---|---|---|---|---|
| 1.3 | Platform Agnostic | 4.20, 4.19, 4.18, 4.17 | 08 Oct 2024 | 28 Feb 2027 | 30 Jun 2027 | N/A | 
| 1.2 | Platform Agnostic | 4.20, 4.19, 4.18, 4.17, 4.16, 4.14 | 14 Nov 2023 | 09 Jun 2026 | 11 Jan 2027 | N/A | 
| 1.1 | Platform Agnostic | 4.20, 4.19, 4.18, 4.17, 4.16, 4.14, 4.12 | 16 Dec 2022 | 03 Feb 2026 | 09 Jun 2026 | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**Not Specified

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends | 
|---|---|---|---|---|---|---|
| 1.2 | Platform Agnostic | 4.19, 4.20, 4.21, 4.22, 5.0 | 09 Jul 2026 | 15 Nov 2026 | 15 Mar 2027 | N/A | 
| 1.1 | Platform Agnostic | 4.18, 4.19, 4.20, 4.21, 4.22 | 25 Mar 2026 | 09 Aug 2026 | 19 Dec 2026 | N/A | 
| 1.0 | Platform Agnostic | 4.20, 4.21, 4.22 | 03 Nov 2025 | 24 Apr 2026 | 09 Aug 2026 | N/A | 

**Additional Links:**Operator Update Information Checker

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends | 
|---|---|---|---|---|---|---|
| 1.0 | Platform Agnostic | 4.18, 4.19, 4.20, 4.21, 4.22, 5.0 | 12 Feb 2026 | 09 Sep 2026 | 03 Aug 2027 | N/A | 

**Additional Links:**Operator Update Information Checker

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2.7 | Platform Agnostic | 4.18, 4.19, 4.20, 4.21, 4.22, 5.0 | 11 Aug 2026 | 11 Nov 2026 | 11 Mar 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 2.6 | Platform Agnostic | 4.14, 4.16, 4.18, 4.19, 4.20, 4.21 | 24 Mar 2026 | 24 Jun 2026 | 24 Oct 2026 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 2.5 | Platform Agnostic | 4.14, 4.16, 4.17, 4.18, 4.19, 4.20 | 08 Dec 2025 | 03 May 2026 | 21 Apr 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 2.4 | Platform Agnostic | 4.14, 4.15, 4.16, 4.17, 4.18, 4.19 | 26 Jun 2025 | 26 Nov 2025 | 26 Jun 2026 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (6)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 2.3 | Platform Agnostic | 4.14, 4.15, 4.16, 4.17, 4.18 | 06 Mar 2025 | 06 Aug 2025 | 06 Mar 2026 | N/A | 
| 2.2 | Platform Agnostic | 4.14, 4.15, 4.16, 4.17 | 21 Nov 2024 | 21 May 2025 | 21 Nov 2025 | N/A | 
| 2.1 | Platform Agnostic | 4.14, 4.15, 4.16, 4.17 | 01 May 2024 | 01 Nov 2024 | 30 Apr 2025 | N/A | 
| 2.0 | Platform Agnostic | 4.14 | 29 Nov 2023 | 31 Jan 2024 | 30 Apr 2024 | N/A | 
| 1.1 | N/A | 4.12, 4.13 | 27 Jun 2023 | 31 Aug 2023 | 30 Nov 2023 | N/A | 
| 1.0 | N/A | 4.12 | 06 Feb 2023 | 24 May 2023 | 28 Aug 2023 | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**3 months

**Valid Subscriptions:**OpenShift Kubernetes Engine / OpenShift Container Platform / OpenShift Platform Plus

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2.7 | Platform Agnostic | 4.18, 4.19, 4.20, 4.21, 4.22, 5.0 | 11 Aug 2026 | 11 Nov 2026 | 11 Mar 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 2.6 | Platform Agnostic | 4.14, 4.16, 4.18, 4.19, 4.20, 4.21 | 24 Mar 2026 | 24 Jun 2026 | 24 Oct 2026 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 2.5 | Platform Agnostic | 4.14, 4.16, 4.17, 4.18, 4.19, 4.20 | 08 Dec 2025 | 03 May 2026 | 21 Apr 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 2.4 | Platform Agnostic | 4.14, 4.15, 4.16, 4.17, 4.18, 4.19 | 26 Jun 2025 | 26 Nov 2025 | 26 Jun 2026 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (5)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 2.3 | Platform Agnostic | 4.14, 4.15, 4.16, 4.17, 4.18 | 06 Mar 2025 | 06 Aug 2025 | 06 Mar 2026 | N/A | 
| 2.2 | Platform Agnostic | 4.14, 4.15, 4.16, 4.17 | 21 Nov 2024 | 21 May 2025 | 21 Nov 2025 | N/A | 
| 2.1 | Platform Agnostic | 4.14, 4.15, 4.16, 4.17 | 01 May 2024 | 01 Nov 2024 | 30 Apr 2025 | N/A | 
| 2.0 | Platform Agnostic | 4.14 | 29 Nov 2023 | 31 Jan 2024 | 30 Apr 2024 | N/A | 
| 1.1 | N/A | 4.12, 4.13 | 27 Jun 2023 | 31 Aug 2023 | 30 Nov 2023 | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**3 months

**Valid Subscriptions:**OpenShift Kubernetes Engine / OpenShift Container Platform / OpenShift Platform Plus

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 5.4 | Platform Agnostic | 4.22 | 09 Jun 2026 | 31 Dec 2026 | 31 Dec 2027 | 30 Jun 2028 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 5.3 | Platform Agnostic | 4.20, 4.21 | 21 Oct 2025 | 09 Sep 2026 | 03 Aug 2027 | 21 Oct 2027 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 5.2 | Platform Agnostic | 4.19, 4.20 | 17 Jun 2025 | 03 May 2026 | 21 Apr 2027 | 21 Oct 2027 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 5.1 | Platform Agnostic | 4.17, 4.18 | 23 Oct 2024 | 17 Sep 2025 | 25 Aug 2026 | 25 Feb 2027 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 5.0 | Platform Agnostic | 4.15, 4.16 | 06 Mar 2024 | 01 Jan 2025 | 27 Dec 2025 | 27 Jun 2026 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.14 | Platform Agnostic | 4.14 | 31 Oct 2023 | 27 May 2024 | 01 May 2025 | 31 Oct 2025 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (3)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 4.13 | Platform Agnostic | 4.13 | 17 May 2023 | 31 Jan 2024 | 17 Nov 2024 | N/A | 
| 4.12 | Platform Agnostic | 4.12 | 17 Jan 2023 | 17 Aug 2023 | 17 Jan 2025 | 17 Jan 2026 | 
| 4.11 | Platform Agnostic | N/A | 10 Aug 2022 | 17 Apr 2023 | 09 Feb 2024 | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**6 months

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends | 
|---|---|---|---|---|---|---|
| 1.0 | Platform Agnostic | 4.18, 4.19, 4.20, 4.21, 4.22, 5.0 | 18 Sep 2025 | 03 May 2026 | 21 Apr 2027 | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**24 months

**Valid Subscriptions:**OpenShift Container Platform / OpenShift Platform Plus

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1.8 | Platform Agnostic | 4.14, 4.15, 4.16, 4.17, 4.18, 4.19, 4.20 | 02 Oct 2023 | 31 Jul 2026 | 31 Dec 2026 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (1)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 1.7 | Platform Agnostic | 4.14, 4.15, 4.16 | 01 Mar 2022 | 01 Jul 2024 | 01 Jul 2025 | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**Not Specified

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2.12 | Platform Agnostic | 4.20, 4.21, 4.22 | 16 Jun 2026 | 01 Feb 2027 | 01 Jun 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 2.11 | Platform Agnostic | 4.19, 4.20, 4.21 | 23 Feb 2026 | 06 Oct 2026 | 01 Feb 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 2.10 | Platform Agnostic | 4.18, 4.19, 4.20 | 04 Nov 2025 | 16 Jun 2026 | 06 Oct 2026 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 2.9 | Platform Agnostic | 4.17, 4.18, 4.19 | 10 Jul 2025 | 23 Feb 2026 | 16 Jul 2026 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (7)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 2.8 | Platform Agnostic | 4.16, 4.17, 4.18 | 31 Mar 2025 | 04 Nov 2025 | 23 Mar 2026 | N/A | 
| 2.7 | Platform Agnostic | 4.14, 4.15, 4.16, 4.17, 4.18 | 22 Sep 2024 | 10 Jul 2025 | 04 Dec 2025 | N/A | 
| 2.6 | Platform Agnostic | 4.12, 4.13, 4.14, 4.15, 4.16 | 17 Apr 2024 | 22 Sep 2024 | 30 Apr 2025 | N/A | 
| 2.5 | N/A | N/A | 13 Sep 2023 | 17 Apr 2024 | 22 Oct 2024 | N/A | 
| 2.4 | N/A | N/A | 17 Apr 2023 | 13 Sep 2023 | 23 May 2024 | N/A | 
| 2.3 | N/A | N/A | 15 Mar 2022 | 17 Apr 2023 | 13 Oct 2023 | N/A | 
| 2.2 | N/A | N/A | 08 Dec 2021 | 15 Mar 2022 | 17 May 2023 | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**4 months

**Valid Subscriptions:**OpenShift Kubernetes Engine / OpenShift Container Platform / OpenShift Platform Plus

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends | EUS Term 2 ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1.6 | Platform Agnostic | 4.22 | 09 Jun 2026 | 31 Dec 2026 | 31 Dec 2027 | 30 Jun 2028 | 30 Jun 2029 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 1.5 | Platform Agnostic | 4.19, 4.20, 4.21 | 17 Jun 2025 | 03 May 2026 | 21 Apr 2027 | 21 Oct 2027 | 21 Oct 2028 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 1.4 | Platform Agnostic | 4.14, 4.15, 4.16, 4.17, 4.18 | 10 Jul 2024 | 17 Jun 2025 | 09 Jun 2026 | 25 Feb 2027 | 25 Feb 2028 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 1.3 | Platform Agnostic | 4.12, 4.13, 4.14, 4.15 | 29 Nov 2023 | 10 Jul 2024 | 17 Jun 2025 | 31 Oct 2025 | 31 Oct 2026 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (3)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 1.2 | N/A | N/A | 14 Jun 2023 | 29 Nov 2023 | 10 Jul 2024 | N/A | N/A | 
| 1.1 | N/A | N/A | 01 Sep 2022 | 14 Jun 2023 | 29 Nov 2023 | N/A | N/A | 
| 1.0 | N/A | N/A | 09 Feb 2022 | 01 Sep 2022 | 14 Jun 2023 | N/A | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**Not Specified

**Valid Subscriptions:**OpenShift Kubernetes Engine / OpenShift Container Platform / OpenShift Platform Plus

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Previous operator releases without a tiered strategy** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 5.8 (For logging) | N/A | 4.12, 4.13, 4.14, 4.15 | 02 Nov 2023 | 05 May 2024 | 03 Nov 2025 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (1)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 5.8 (For Tracing, service mesh and kiali) | N/A | 4.12, 4.13, 4.14, 4.15, 4.16, 4.17 | 02 Nov 2023 | 05 May 2024 | 03 Nov 2025 | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**Not Specified

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 4.11 | Platform Agnostic | 4.12, 4.14, 4.16, 4.18, 4.19, 4.20, 4.21, 4.22, 5.0 | 15 Jun 2026 | 15 Dec 2026 | 15 Apr 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.10 | Platform Agnostic | 4.12, 4.14, 4.16, 4.17, 4.18, 4.19, 4.20, 4.21 | 03 Mar 2026 | 03 Sep 2026 | 04 Jan 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (18)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 4.9 | Platform Agnostic | 4.12, 4.14, 4.16, 4.17, 4.18, 4.19, 4.20 | 30 Oct 2025 | 30 Apr 2026 | 31 Aug 2026 | N/A | 
| 4.8 | Platform Agnostic | 4.12, 4.14, 4.16, 4.17, 4.18, 4.19, 4.20 | 09 Jul 2025 | 09 Jan 2026 | 09 May 2026 | N/A | 
| 4.7 | Platform Agnostic | 4.12, 4.14, 4.16, 4.17, 4.18, 4.19, 4.20 | 17 Mar 2025 | 17 Sep 2025 | 17 Jan 2026 | N/A | 
| 4.6 | Platform Agnostic | 4.12, 4.14, 4.15, 4.16, 4.17, 4.18 | 03 Dec 2024 | 03 Jun 2025 | 03 Oct 2025 | N/A | 
| 4.5 | Platform Agnostic | 4.12, 4.14, 4.15, 4.16, 4.17 | 24 Jul 2024 | 24 Jan 2025 | 24 May 2025 | N/A | 
| 4.4 | Platform Agnostic | 4.12, 4.13, 4.14, 4.15, 4.16 | 28 Mar 2024 | 28 Sep 2024 | 28 Jan 2025 | N/A | 
| 4.3 | N/A | 4.11, 4.12, 4.13, 4.14, 4.15 | 15 Nov 2023 | 15 Jun 2024 | N/A | N/A | 
| 4.2 | N/A | N/A | 18 Sep 2023 | 18 Mar 2024 | N/A | N/A | 
| 4.1 | N/A | N/A | 29 Jun 2023 | 29 Dec 2023 | N/A | N/A | 
| 4.0 | N/A | N/A | 03 May 2023 | 03 Nov 2023 | N/A | N/A | 
| 3.74 | N/A | N/A | 27 Feb 2023 | 27 Nov 2023 | N/A | N/A | 
| 3.73 | N/A | N/A | 06 Dec 2022 | 07 Jun 2023 | N/A | N/A | 
| 3.72 | N/A | N/A | 26 Sep 2022 | 27 Mar 2023 | N/A | N/A | 
| 3.71 | N/A | N/A | 25 Jul 2022 | 25 Jan 2023 | N/A | N/A | 
| 3.70 | N/A | N/A | 04 Jul 2022 | 02 Dec 2022 | N/A | N/A | 
| 3.69 | N/A | N/A | 21 Mar 2022 | 21 Sep 2022 | N/A | N/A | 
| 3.68 | N/A | N/A | 02 Feb 2022 | 02 Aug 2022 | N/A | N/A | 
| 3.67 | N/A | N/A | 16 Dec 2021 | 15 Jul 2022 | N/A | N/A | 

**Estimated release cadence:**4 months

**Valid Subscriptions:**OpenShift Platform Plus / Red Hat Advanced Cluster Security

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **End of Life versions (4)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 1.10 | N/A | 4.16 | 01 Mar 2023 | 30 Jun 2024 | 30 Jun 2025 | N/A | 
| 1.8 | N/A | 4.11 | 05 Sep 2022 | 01 Mar 2023 | 01 Apr 2023 | N/A | 
| 1.6 | N/A | 4.10 | 02 Dec 2021 | 12 Jul 2022 | 12 Aug 2022 | N/A | 
| 1.4 | N/A | 4.8 | 18 Aug 2021 | 02 Dec 2021 | 02 Jan 2022 | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**6 months

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1.4 | Platform Agnostic | 4.18, 4.19, 4.20, 4.21, 4.22, 5.0 | 20 Jul 2026 | 05 Oct 2026 | 05 Nov 2026 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 1.3 | Platform Agnostic | 4.18, 4.19, 4.20, 4.21, 4.22 | 10 Mar 2026 | 20 Jul 2026 | 20 Sep 2026 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 1.2 | Platform Agnostic | 4.18, 4.19, 4.20 | 16 Dec 2025 | 10 Mar 2026 | 10 Apr 2026 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (2)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 1.1 | Platform Agnostic | 4.18, 4.19 | 01 Oct 2025 | 16 Dec 2025 | 16 Jan 2026 | N/A | 
| 1.0 | Platform Agnostic | 4.18, 4.19 | 10 Jul 2025 | 01 Oct 2025 | 16 Dec 2025 | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**4 months

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1.10 | Platform Agnostic | 4.18, 4.19, 4.20, 4.21, 4.22 | 10 Jun 2026 | 03 Nov 2026 | 28 Feb 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 1.9 | Platform Agnostic | 4.16, 4.18, 4.19, 4.20, 4.21, 4.22 | 04 Mar 2026 | 10 Jun 2026 | 03 Nov 2026 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (9)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 1.8 | Platform Agnostic | 4.16, 4.17, 4.18, 4.19, 4.20 | 11 Nov 2025 | 04 Mar 2026 | 10 Jun 2026 | N/A | 
| 1.7 | Platform Agnostic | 4.16, 4.17, 4.18, 4.19 | 20 Aug 2025 | 11 Nov 2025 | 04 Mar 2026 | N/A | 
| 1.6 | Platform Agnostic | 4.14, 4.15, 4.16, 4.17, 4.18 | 14 May 2025 | 20 Aug 2025 | 11 Nov 2025 | N/A | 
| 1.5 | Platform Agnostic | 4.14, 4.15, 4.16, 4.17, 4.18 | 28 Mar 2025 | 14 May 2025 | 20 Aug 2025 | N/A | 
| 1.4 | Platform Agnostic | 4.14, 4.15, 4.16, 4.17 | 18 Dec 2024 | 28 Mar 2025 | 14 May 2025 | N/A | 
| 1.3 | Platform Agnostic | 4.16, 4.15, 4.14, 4.13 | 03 Oct 2024 | 18 Dec 2024 | 28 Mar 2025 | N/A | 
| 1.2 | Platform Agnostic | 4.13, 4.14, 4.15 | 26 Jun 2024 | 03 Oct 2024 | 18 Dec 2024 | N/A | 
| 1.1 | Platform Agnostic | 4.12, 4.13, 4.14, 4.15 | 20 Mar 2024 | 26 Jun 2024 | 03 Oct 2024 | N/A | 
| 1.0 | Platform Agnostic | 4.12, 4.13, 4.14 | 12 Dec 2023 | 20 Mar 2024 | 26 Jun 2024 | N/A | 

**Estimated release cadence:**about 4 months

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3.5 | Platform Agnostic | 5.0, 4.22, 4.21, 4.20, 4.19 | 27 Aug 2026 | 29 Mar 2027 | 28 Feb 2028 | 28 Feb 2028 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 3.4 | Platform Agnostic | 4.21, 4.20, 4.19 | 14 May 2026 | 16 Nov 2026 | N/A | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 2.25 | Platform Agnostic | 4.21, 4.20, 4.19, 4.18, 4.17, 4.16 | 23 Oct 2025 | 25 May 2026 | 26 Apr 2027 | 26 Apr 2027 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (32)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 3.3 | Platform Agnostic | 4.21, 4.20, 4.19 | 05 Mar 2026 | 05 Oct 2026 | N/A | N/A | 
| 3.2 | Platform Agnostic | 4.19, 4.20 | 22 Jan 2026 | 05 Mar 2026 | N/A | N/A | 
| 3.0 | Platform Agnostic | 4.20, 4.19 | 13 Nov 2025 | 15 Jan 2026 | N/A | N/A | 
| 2.24 | Platform Agnostic | 4.19, 4.18, 4.17, 4.16 | 07 Oct 2025 | 23 Oct 2025 | N/A | N/A | 
| 2.23 | Platform Agnostic | 4.19, 4.18, 4.17, 4.16, 4.15 | 14 Aug 2025 | 18 Sep 2025 | N/A | N/A | 
| 2.22 | Platform Agnostic | 4.19, 4.18, 4.17, 4.16 | 21 Jul 2025 | 16 Feb 2026 | N/A | N/A | 
| 2.21 | Platform Agnostic | 4.19, 4.18, 4.17, 4.16 | 17 Jun 2025 | 17 Dec 2025 | N/A | N/A | 
| 2.20 | Platform Agnostic | 4.19, 4.18, 4.17, 4.16, 4.15 | 14 May 2025 | 19 Jun 2025 | N/A | N/A | 
| 2.19 | Platform Agnostic | 4.19, 4.18, 4.17, 4.16, 4.14 | 16 Apr 2025 | 17 Nov 2025 | N/A | N/A | 
| 2.18 | Platform Agnostic | 4.19, 4.18, 4.17, 4.16, 4.14 | 12 Mar 2025 | 16 Apr 2025 | N/A | N/A | 
| 2.17 | Platform Agnostic | 4.19, 4.18, 4.17, 4.16, 4.14 | 13 Feb 2025 | 12 Mar 2025 | N/A | N/A | 
| 2.16 | Platform Agnostic | 4.19, 4.18, 4.16, 4.14 | 09 Dec 2024 | 07 Jul 2025 | 09 Jun 2026 | 09 Jun 2026 | 
| 2.15 | Platform Agnostic | N/A | 14 Nov 2024 | 09 Dec 2024 | N/A | N/A | 
| 2.14 | Platform Agnostic | N/A | 17 Oct 2024 | 14 Nov 2024 | N/A | N/A | 
| 2.13 | Platform Agnostic | N/A | 16 Sep 2024 | 14 Apr 2025 | N/A | N/A | 
| 2.12 | Platform Agnostic | N/A | 26 Aug 2024 | 19 Sep 2024 | N/A | N/A | 
| 2.11 | Platform Agnostic | N/A | 16 Jul 2024 | 01 Jan 2025 | N/A | N/A | 
| 2.10 | Platform Agnostic | N/A | 24 Jun 2024 | 22 Jan 2025 | N/A | N/A | 
| 2.9 | Platform Agnostic | N/A | 01 May 2024 | 24 Jun 2024 | N/A | N/A | 
| 2.8 | Platform Agnostic | N/A | 19 Mar 2024 | 14 Oct 2024 | 12 Sep 2025 | 12 Sep 2025 | 
| 1.30 | N/A | N/A | 01 Aug 2023 | 25 Oct 2023 | N/A | N/A | 
| 1.29 | N/A | N/A | 12 Jul 2023 | 10 Oct 2023 | N/A | N/A | 
| 1.28 | N/A | N/A | 20 Jun 2023 | 11 Sep 2023 | N/A | N/A | 
| 1.27 | N/A | N/A | 05 Jun 2023 | 27 Aug 2023 | N/A | N/A | 
| 1.26 | N/A | N/A | 10 May 2023 | 01 Aug 2023 | N/A | N/A | 
| 1.25 | N/A | N/A | 20 Apr 2023 | 04 Jul 2023 | N/A | N/A | 
| 1.24 | N/A | N/A | 28 Mar 2023 | 19 Jun 2023 | N/A | N/A | 
| 1.23 | N/A | N/A | 15 Mar 2023 | 06 Jun 2023 | N/A | N/A | 
| 1.22 | N/A | N/A | 14 Feb 2023 | 08 May 2023 | N/A | N/A | 
| 1.21 | N/A | N/A | 30 Jan 2023 | 23 Apr 2023 | N/A | N/A | 
| 1.20 | N/A | N/A | 11 Jan 2023 | 04 Apr 2023 | N/A | N/A | 
| 0.1 | N/A | N/A | 19 Sep 2022 | 10 Jan 2023 | N/A | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**3 months

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1.22 | Platform Agnostic | 4.18, 4.19, 4.20, 4.21, 4.22, 5.0 | 30 Sep 2026 | 31 Jan 2027 | 30 Jun 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 1.21 | Platform Agnostic | 4.18, 4.19, 4.20, 4.21, 4.22 | 24 Jun 2026 | 31 Oct 2026 | 31 Mar 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 1.20 | Platform Agnostic | 4.14, 4.16, 4.17, 4.18, 4.19, 4.20, 4.21 | 25 Mar 2026 | 31 Jul 2026 | 15 Dec 2026 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 1.19 | Platform Agnostic | 4.14, 4.16, 4.17, 4.18, 4.19, 4.20, 4.21 | 18 Dec 2025 | 25 Apr 2026 | 30 Sep 2026 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (18)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 1.18 | Platform Agnostic | 4.14, 4.16, 4.17, 4.18, 4.19, 4.20 | 25 Sep 2025 | 18 Jan 2026 | 24 Jun 2026 | N/A | 
| 1.17 | Platform Agnostic | 4.19, 4.18, 4.17, 4.16, 4.15, 4.14, 4.12 | 07 Aug 2025 | 25 Oct 2025 | 25 Mar 2026 | N/A | 
| 1.16 | Platform Agnostic | 4.18, 4.17, 4.16, 4.15, 4.14, 4.12 | 31 Mar 2025 | 07 Sep 2025 | 18 Dec 2025 | N/A | 
| 1.15 | Platform Agnostic | 4.14, 4.15, 4.16, 4.17 | 12 Dec 2024 | 31 May 2025 | 25 Sep 2025 | N/A | 
| 1.14 | Platform Agnostic | 4.12, 4.13, 4.14, 4.15, 4.16, 4.17 | 19 Sep 2024 | 12 Jan 2025 | 07 Aug 2025 | N/A | 
| 1.13 | Platform Agnostic | 4.12, 4.13, 4.14, 4.15, 4.16 | 08 Jul 2024 | 19 Oct 2024 | 31 Mar 2025 | N/A | 
| 1.12 | Platform Agnostic | 4.12, 4.13, 4.14, 4.15 | 20 Mar 2024 | 08 Aug 2024 | 12 Jan 2025 | N/A | 
| 1.11 | Platform Agnostic | 4.12, 4.13, 4.14 | 08 Dec 2023 | 20 Apr 2024 | 19 Sep 2024 | N/A | 
| 1.10 | Platform Agnostic | 4.12, 4.13, 4.14 | 28 Sep 2023 | 08 Jan 2024 | 08 Jul 2024 | N/A | 
| 1.9 | Platform Agnostic | 4.12, 4.13, 4.14 | 01 Jun 2023 | 28 Oct 2023 | 20 Mar 2024 | N/A | 
| 1.8 | N/A | 4.10, 4.11, 4.12 | 15 Mar 2023 | 01 Jul 2023 | 08 Dec 2023 | N/A | 
| 1.7 | N/A | 4.10, 4.11, 4.12 | 14 Dec 2022 | 15 Apr 2023 | 28 Sep 2023 | N/A | 
| 1.6 | N/A | 4.8, 4.9, 4.10, 4.11 | 27 Jul 2022 | 14 Jan 2023 | 01 Jun 2023 | N/A | 
| 1.5 | N/A | 4.8, 4.9, 4.10, 4.11 | 20 Apr 2022 | 27 Aug 2022 | 15 Mar 2023 | N/A | 
| 1.4 | N/A | 4.7, 4.8, 4.9, 4.10, 4.11 | 25 Jan 2022 | 20 May 2022 | 14 Dec 2022 | N/A | 
| 1.3 | N/A | 4.7, 4.8, 4.9 | 14 Oct 2021 | 25 Feb 2022 | 27 Jun 2022 | N/A | 
| 1.2 | N/A | 4.8 | 28 Jul 2021 | 14 Nov 2021 | 20 Apr 2022 | N/A | 
| 1.1 | N/A | 4.7 | 26 Apr 2021 | 28 Aug 2021 | 25 Jan 2022 | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**3 months

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1.24 | Platform Agnostic | 4.14, 4.16, 4.18, 4.19, 4.20, 4.21, 4.22, 5.0 | 17 Sep 2026 | 31 Dec 2026 | 31 Jan 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 1.23 | Platform Agnostic | 4.14, 4.16, 4.18, 4.19, 4.20, 4.21, 4.22 | 17 Jul 2026 | 31 Oct 2026 | 31 Dec 2026 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 1.22 | Platform Agnostic | 4.16, 4.18, 4.19, 4.20, 4.21, 4.22 | 27 Apr 2026 | 31 Aug 2026 | 30 Sep 2026 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 1.15 | Platform Agnostic | 4.14, 4.15, 4.16 | 21 Jun 2024 | 09 Nov 2024 | 31 Oct 2026 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (17)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 1.21 | Platform Agnostic | 4.14, 4.16, 4.17, 4.18, 4.19, 4.20 | 22 Jan 2026 | 27 May 2026 | 17 Jul 2026 | N/A | 
| 1.20 | Platform Agnostic | 4.16, 4.17, 4.18, 4.19, 4.20 | 25 Sep 2025 | 22 Feb 2026 | 27 Apr 2026 | N/A | 
| 1.19 | Platform Agnostic | 4.15, 4.16, 4.17, 4.18, 4.19, 4.20 | 15 Jul 2025 | 25 Oct 2025 | 22 Jan 2026 | N/A | 
| 1.18 | N/A | 4.18, 4.17, 4.16, 4.15 | 17 Mar 2025 | 15 Aug 2025 | 25 Sep 2025 | N/A | 
| 1.17 | N/A | 4.15, 4.16, 4.17, 4.18 | 12 Dec 2024 | 17 Apr 2025 | 15 Jul 2025 | N/A | 
| 1.16 | N/A | 4.15, 4.16, 4.17, 4.18 | 09 Oct 2024 | 12 Jan 2025 | 17 Mar 2025 | N/A | 
| 1.14 | N/A | 4.12, 4.13, 4.14, 4.15, 4.16 | 27 Feb 2024 | 21 Jul 2024 | 17 Jan 2026 | N/A | 
| 1.13 | N/A | 4.12, 4.13, 4.14 | 30 Nov 2023 | 27 Mar 2024 | 09 Oct 2024 | N/A | 
| 1.12 | N/A | 4.12, 4.13, 4.14 | 02 Oct 2023 | 30 Dec 2023 | 21 Jun 2024 | N/A | 
| 1.11 | N/A | 4.12, 4.13, 4.14 | 16 Jun 2023 | 02 Nov 2023 | 27 Feb 2024 | N/A | 
| 1.10 | N/A | 4.10, 4.11, 4.12, 4.13 | 17 Apr 2023 | 16 Jul 2023 | 30 Nov 2023 | N/A | 
| 1.9 | N/A | 4.10, 4.11, 4.12, 4.13 | 18 Jan 2023 | 17 May 2023 | 02 Oct 2023 | N/A | 
| 1.8 | N/A | 4.10, 4.11, 4.12 | 22 Aug 2022 | 18 Feb 2023 | 16 Jun 2023 | N/A | 
| 1.7 | N/A | 4.9, 4.10 | 20 Apr 2022 | 22 Sep 2022 | 17 Apr 2023 | N/A | 
| 1.6 | N/A | 4.9 | 30 Nov 2021 | 20 May 2022 | 18 Jan 2023 | N/A | 
| 1.5 | N/A | 4.8 | 28 Jul 2021 | 30 Dec 2021 | 22 Aug 2022 | N/A | 
| 1.4 | N/A | 4.7 | 27 Apr 2021 | 28 Aug 2021 | 20 Apr 2022 | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**Not Specified

**Valid Subscriptions:**OpenShift Container Platform / OpenShift Platform Plus

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends | 
|---|---|---|---|---|---|---|
| 7.0 | Platform Agnostic | N/A | 28 Feb 2018 | 31 May 2022 | 31 May 2024 | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**No futher releases

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1.3 | Platform Agnostic | 4.19 | 09 Jul 2025 | 03 May 2026 | 21 Apr 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 1.2 | Platform Agnostic | 4.17, 4.18 | 16 Oct 2024 | 17 Sep 2025 | 25 Aug 2026 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 1.1 | Platform Agnostic | 4.15, 4.16 | 27 Feb 2024 | 01 Jan 2025 | 27 Dec 2025 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (1)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 1.0 | Platform Agnostic | 4.13, 4.14 | 18 May 2023 | 27 May 2024 | 01 May 2025 | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**6 months

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1.5 | Platform Agnostic | 4.20 | 29 Oct 2025 | 09 Sep 2026 | 03 Aug 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 1.4 | Platform Agnostic | 4.18, 4.19 | 25 Feb 2025 | 17 Sep 2025 | 17 Dec 2026 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (4)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 1.3 | Platform Agnostic | 4.16, 4.17 | 01 Jul 2024 | 25 May 2025 | 01 Apr 2026 | N/A | 
| 1.2 | Platform Agnostic | 4.14, 4.15 | 01 Nov 2023 | 27 Sep 2024 | 27 Aug 2025 | N/A | 
| 1.1 | N/A | 4.11 | 01 Sep 2022 | 31 Jan 2024 | 17 Nov 2024 | N/A | 
| 1.0 | N/A | 4.10 | 18 Apr 2022 | 10 Nov 2022 | 17 Nov 2024 | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**6 months

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1.17 | Platform Agnostic | 4.22 | 29 Jun 2026 | 31 Dec 2026 | 31 Dec 2027 | 30 Jun 2029 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 1.16 | Platform Agnostic | 4.21 | 17 Mar 2026 | 09 Sep 2026 | 03 Aug 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 1.15 | Platform Agnostic | 4.20 | 27 Nov 2025 | 03 May 2026 | 21 Apr 2027 | 21 Oct 2028 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 1.14 | Platform Agnostic | 4.19 | 25 Sep 2025 | 21 Jan 2026 | 17 Dec 2026 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 1.13 | Platform Agnostic | 4.18 | 02 Jun 2025 | 17 Sep 2025 | 25 Aug 2026 | 25 Feb 2028 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 1.11 | Platform Agnostic | 4.16 | 13 Aug 2024 | 01 Jan 2025 | 27 Dec 2025 | 27 Jun 2027 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (4)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 1.8 | N/A | 4.13 | 06 Jun 2023 | 31 Jan 2024 | 17 Nov 2024 | N/A | 
| 1.7 | N/A | 4.12 | 28 Feb 2023 | 17 Aug 2023 | 17 Jul 2024 | N/A | 
| 1.6 | N/A | 4.11 | 27 Sep 2022 | 17 Apr 2023 | 10 Feb 2024 | N/A | 
| 1.5 | N/A | 4.10 | 18 May 2022 | 10 Nov 2022 | 10 Sep 2023 | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**Not Specified

**Valid Subscriptions:**OpenShift Container Platform / OpenShift Platform Plus

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends | 
|---|---|---|---|---|---|---|
| 1.1 | Platform Agnostic | 4.20, 4.21, 4.22, 5.0 | 30 Jun 2026 | 16 Nov 2026 | 16 Dec 2026 | N/A | 
| 1.0 | Platform Agnostic | 4.18, 4.19, 4.20, 4.21 | 17 Dec 2025 | 30 Jul 2026 | 31 Aug 2026 | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**4 months

**Valid Subscriptions:**OpenShift Container Platform / OpenShift Platform Plus

# Rolling-Stream Operators

The following operators have a single rolling stream in which fixes and features are introduced.

Released independently and with a variable cadence, cluster administrators should expect to continually validate Rolling Stream Operators and upgrade to the latest release, to maintain a supported state. New releases are required to support all in-maintenance OpenShift Container Platform versions, ensuring a cluster administrator could remain on an non current cluster version and still be supported.

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Previous operator releases without a tiered strategy** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 7 | N/A | 4.12, 4.13, 4.14, 4.15, 4.16, 4.17, 4.18, 4.19, 4.20 | 30 May 2017 | 31 Dec 2026 | 30 Apr 2028 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

**Additional Links:**Operator Update Information Checker

**Valid Subscriptions:**Red Hat Runtimes / Red Hat Integration / Red Hat Process Automation / Red Hat AMQ

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends | 
|---|---|---|---|---|---|---|
| 1.10 | Platform Agnostic | 4.12, 4.14, 4.16, 4.17, 4.18, 4.19, 4.20, 4.21, 4.22, 5.0 | 05 Mar 2018 | 30 Jun 2022 | 30 Jun 2024 | N/A | 

**Additional Links:**Operator Update Information Checker

**Valid Subscriptions:**Red Hat Integration / Red Hat AMQ

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1.10 | Rolling Stream | 4.12, 4.14, 4.16, 4.18, 4.19, 4.20, 4.21, 4.22, 5.0 | 15 Sep 2026 | 15 Dec 2026 | N/A | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (2)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 1.9 | Rolling Stream | 4.12, 4.14, 4.16, 4.18, 4.19, 4.20, 4.21, 4.22 | 16 Apr 2026 | 15 Sep 2026 | N/A | N/A | 
| 1.8 | Rolling Stream | 4.12, 4.14, 4.16, 4.17, 4.18, 4.19, 4.20, 4.21 | 24 Nov 2025 | 16 Apr 2026 | N/A | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**4 months

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends | 
|---|---|---|---|---|---|---|
| 4.5 | Rolling Stream | 4.12, 4.14, 4.16, 4.18, 4.19, 4.20, 4.21, 4.22, 5.0 | 12 Oct 2026 | 28 Feb 2027 | 28 Feb 2027 | N/A | 
| 4.4 | Rolling Stream | 4.12, 4.14, 4.16, 4.18, 4.19, 4.20, 4.21, 4.22 | 22 Apr 2026 | 12 Oct 2026 | 12 Oct 2026 | N/A | 

**Additional Links:**Operator Update Information Checker

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2.19.1 | Rolling Stream | 4.12, 4.14, 4.16, 4.18, 4.19, 4.20, 4.21 | 18 May 2026 | Release of CMA 2.20.1 | N/A | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 2.18.1 | Rolling Stream | 4.12, 4.14, 4.16, 4.17, 4.18, 4.19, 4.20 | 15 Jan 2026 | 18 May 2026 | N/A | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (7)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 2.17.2 | Rolling Stream | 4.12, 4.14, 4.16, 4.17, 4.18, 4.19 | 25 Sep 2025 | 15 Jan 2026 | N/A | N/A | 
| 2.15.1 | Rolling Stream | 4.12, 4.14, 4.15, 4.16, 4.17, 4.18 | 02 Apr 2025 | 25 Sep 2025 | N/A | N/A | 
| 2.14.1 | Rolling Stream | 4.12, 4.13, 4.14, 4.15, 4.16 | 26 Aug 2024 | 02 Apr 2025 | N/A | N/A | 
| 2.13.1 | Rolling Stream | 4.12, 4.13, 4.14, 4.15, 4.16 | 24 Jul 2024 | 26 Aug 2024 | N/A | N/A | 
| 2.12.1 | Rolling Stream | 4.12, 4.13, 4.14, 4.15 | 15 Apr 2024 | 24 Jul 2024 | N/A | N/A | 
| 2.11.2 | N/A | 4.11, 4.12, 4.13 | 23 Oct 2023 | 17 Jul 2024 | N/A | N/A | 
| 2.10.1 | N/A | 4.10, 4.11, 4.12, 4.13 | 12 Jun 2023 | 10 Feb 2024 | N/A | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**3 months

**Valid Subscriptions:**OpenShift Kubernetes Engine / OpenShift Container Platform / OpenShift Platform Plus

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends | 
|---|---|---|---|---|---|---|
| 0.7 | Rolling Stream | 4.12, 4.14, 4.16, 4.18, 4.19, 4.20, 4.21, 4.22, 5.0 | 07 Oct 2024 | 31 Dec 2027 | N/A | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**4 months

**Valid Subscriptions:**OpenShift Container Platform / OpenShift Platform Plus

| Version | Tier | Supported OpenShift versions | OpenShift Aligned Version | General availability | Full support ends | Maintenance ends | EUS ends | EUS Term 2 ends | 
|---|---|---|---|---|---|---|---|---|
| 0.6 | Rolling Stream | 4.16, 4.17, 4.18, 4.19 | N/A | 16 Sep 2025 | 03 May 2026 | 17 Dec 2026 | N/A | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**4 months

**Valid Subscriptions:**OpenShift Kubernetes Engine / OpenShift Container Platform / OpenShift Platform Plus

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1.5.0 | Rolling Stream | 4.12, 4.14, 4.16, 4.18, 4.19, 4.20, 4.21, 4.22, 5.0 | 30 Sep 2026 | 01 Feb 2027 | N/A | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (2)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 1.4.0 | Rolling Stream | 4.12, 4.14, 4.16, 4.18, 4.19, 4.20, 4.21, 4.22 | 02 Jun 2026 | 01 Oct 2026 | N/A | N/A | 
| 1.3.8 | Rolling Stream | 4.12, 4.14, 4.16, 4.17, 4.18, 4.19, 4.20, 4.21 | 17 Dec 2025 | 02 Jun 2026 | N/A | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**6 months

**Valid Subscriptions:**OpenShift Kubernetes Engine / OpenShift Container Platform / OpenShift Platform Plus

| Version | Tier | Supported OpenShift versions | OpenShift Aligned Version | General availability | Full support ends | Maintenance ends | EUS ends | EUS Term 2 ends | 
|---|---|---|---|---|---|---|---|---|
| 0.5 | Rolling Stream | 4.16, 4.17, 4.18, 4.19 | N/A | 24 Nov 2025 | 03 May 2026 | 17 Dec 2026 | N/A | N/A | 
| 0.4 | Rolling Stream | 4.14, 4.15, 4.16, 4.17, 4.18, 4.19 | N/A | 21 Jan 2025 | 24 Nov 2025 | N/A | N/A | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**4 months

**Valid Subscriptions:**OpenShift Kubernetes Engine / OpenShift Container Platform / OpenShift Platform Plus

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 8.2 | Rolling Stream | 4.12, 4.14, 4.16, 4.18, 4.19, 4.20, 4.21, 4.22, 5.0 | 21 Jul 2026 | 30 Nov 2026 | 28 Feb 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (10)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 8.1 | Rolling Stream | 4.12, 4.14, 4.16, 4.18, 4.19, 4.20, 4.21 | 25 Mar 2026 | 14 Jul 2026 | 14 Oct 2026 | N/A | 
| 8.0 | Rolling Stream | 4.12, 4.14, 4.16, 4.18, 4.19, 4.20, 4.21 | 30 Sep 2025 | 25 Mar 2026 | 26 Jun 2026 | N/A | 
| 7.3 | Rolling Stream | N/A | 21 May 2025 | 30 Sep 2025 | 30 Dec 2025 | N/A | 
| 7.2 | Rolling Stream | N/A | 21 Jan 2025 | 21 May 2025 | 21 Aug 2025 | N/A | 
| 7.1 | Rolling Stream | N/A | 15 Aug 2024 | 21 Jan 2025 | 21 Apr 2025 | N/A | 
| 7.0 | Rolling Stream | N/A | 30 Jan 2024 | 15 Aug 2024 | 15 Nov 2024 | N/A | 
| 6.2 | Rolling Stream | N/A | 22 Aug 2023 | 30 Jan 2024 | 30 Apr 2024 | N/A | 
| 6.1 | Rolling Stream | N/A | 27 Apr 2023 | 22 Aug 2023 | 22 Nov 2023 | N/A | 
| 6.0 | Rolling Stream | N/A | 17 Nov 2022 | 27 Apr 2023 | 27 Jul 2023 | N/A | 
| 5.1 | Rolling Stream | N/A | 10 Dec 2020 | 17 Nov 2022 | N/A | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**4 months

**Valid Subscriptions:**OpenShift Kubernetes Engine / OpenShift Container Platform / OpenShift Platform Plus

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **End of Life versions (3)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 1.2 | N/A | N/A | 14 Sep 2023 | 30 Sep 2024 | 30 Sep 2024 | N/A | 
| 1.1 | N/A | N/A | 31 May 2023 | 14 Sep 2023 | 14 Sep 2023 | N/A | 
| 1.0 | N/A | N/A | 17 Nov 2022 | 31 May 2023 | 31 May 2023 | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**Not Specified

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1.4 | Rolling Stream | 4.16, 4.18, 4.19, 4.20, 4.21, 4.22, 5.0 | 28 Oct 2026 | 01 Mar 2027 | N/A | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 1.3 | Rolling Stream | 4.16, 4.18, 4.19, 4.20, 4.21 | 06 Apr 2026 | 06 Nov 2026 | N/A | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 1.2 | Rolling Stream | 4.16, 4.17, 4.18, 4.19, 4.20 | 28 Oct 2025 | 06 Apr 2026 | N/A | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (2)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 1.1 | Rolling Stream | 4.16, 4.17, 4.18 | 18 Mar 2025 | 28 Oct 2025 | N/A | N/A | 
| 1.0 | Rolling Stream | 4.16, 4.17 | 31 Oct 2024 | 18 Mar 2025 | N/A | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**6 months

**Valid Subscriptions:**OpenShift Kubernetes Engine / OpenShift Container Platform / OpenShift Platform Plus

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **End of Life versions (2)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 1.1 | Rolling Stream | 4.17 | 24 Jan 2025 | 01 Jul 2025 | 01 Oct 2025 | N/A | 
| 1.0 | Rolling Stream | 4.13, 4.14 | 27 Nov 2023 | 01 Apr 2024 | 01 Jul 2024 | N/A | 

**Additional Links:**Operator Update Information Checker

**Valid Subscriptions:**OpenShift Container Platform / OpenShift Platform Plus

| Version | Tier | Supported OpenShift versions | OpenShift Aligned Version | General availability | Full support ends | Maintenance ends | EUS ends | EUS Term 2 ends | EUS Term 3 ends | 
|---|---|---|---|---|---|---|---|---|---|
| 0.10 | Rolling Stream | 4.16, 4.17, 4.18, 4.19 | N/A | 16 Sep 2025 | 03 May 2026 | 17 Dec 2026 | N/A | N/A | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**4 months

**Valid Subscriptions:**OpenShift Kubernetes Engine / OpenShift Container Platform / OpenShift Platform Plus

| Version | Tier | Supported OpenShift versions | OpenShift Aligned Version | General availability | Full support ends | Maintenance ends | EUS ends | EUS Term 2 ends | EUS Term 3 ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 5.5 | Rolling Stream | 4.16, 4.17, 4.18, 4.19 | N/A | 24 Nov 2025 | 03 May 2026 | 17 Dec 2026 | N/A | N/A | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (1)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 5.4 | Rolling Stream | 4.14, 4.15, 4.16, 4.17, 4.19 | N/A | 21 Jan 2025 | 24 Nov 2025 | N/A | N/A | N/A | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**4 months

**Valid Subscriptions:**OpenShift Kubernetes Engine / OpenShift Container Platform / OpenShift Platform Plus

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends | 
|---|---|---|---|---|---|---|
| 5.0 | Rolling Stream | 4.20, 4.19, 4.18, 4.17, 4.16, 4.14, 4.12, 4.21, 4.22, 5.0 | 03 Aug 2022 | 30 Jun 2027 | 30 Jun 2027 | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**Not Specified

**Valid Subscriptions:**OpenShift Container Platform / OpenShift Platform Plus

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Previous operator releases without a tiered strategy** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 4.2 | N/A | 4.19, 4.20, 4.21, 4.22 | 26 May 2026 | 30 Nov 2026 | 30 Nov 2026 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (8)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 4.1 | N/A | 4.20, 4.19, 4.18, 4.17, 4.16 | 25 Nov 2025 | 26 May 2026 | 26 May 2026 | N/A | 
| 4.0 | N/A | 4.18, 4.17, 4.16, 4.15, 4.14, 4.13, 4.12 | 19 Mar 2025 | 25 Nov 2025 | 25 Nov 2025 | N/A | 
| 3.0 | N/A | 4.16, 4.15, 4.14, 4.13, 4.12 | 02 Jul 2024 | 19 Mar 2025 | 19 Mar 2025 | N/A | 
| 2.4 | N/A | N/A | 12 Dec 2023 | 02 Jul 2024 | 02 Jul 2024 | N/A | 
| 2.3 | N/A | N/A | 19 May 2023 | 15 Nov 2023 | 15 Nov 2023 | N/A | 
| 2.2 | N/A | N/A | 15 Nov 2022 | 16 May 2023 | 16 May 2023 | N/A | 
| 2.1 | N/A | N/A | 10 May 2022 | 15 Nov 2022 | 15 Nov 2022 | N/A | 
| 2.0 | N/A | N/A | 18 Oct 2021 | 10 May 2022 | 10 May 2022 | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**6 months

**Valid Subscriptions:**Red Hat build of OpenJDK

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends | 
|---|---|---|---|---|---|---|
| 26.6 | Rolling Stream | 4.22, 4.21, 4.20, 4.19, 4.18, 4.17, 4.16, 4.14, 4.12 | 03 Jun 2026 | 15 Nov 2026 | 15 May 2027 | N/A | 
| 26.4 | Rolling Stream | 4.14, 4.16, 4.17, 4.18, 4.19, 4.20, 4.21 | 30 Oct 2025 | 03 Jun 2026 | 03 Dec 2026 | N/A | 
| 26.2 | Rolling Stream | 4.12, 4.14, 4.15, 4.16, 4.17, 4.18, 4.19, 4.20, 4.21 | 13 May 2025 | 30 Oct 2025 | 03 Jun 2026 | N/A | 
| 26.0 | Rolling Stream | 4.19, 4.18, 4.17, 4.16, 4.14, 4.15 | 13 Nov 2024 | 13 May 2025 | 13 Nov 2025 | N/A | 
| 24.0 | Rolling Stream | 4.18, 4.17, 4.16, 4.15, 4.14, 4.12 | 25 Apr 2024 | 13 Nov 2024 | 13 May 2025 | N/A | 
| 22.0 | Rolling Stream | 4.17, 4.16, 4.15, 4.14, 4.12 | 15 Nov 2023 | 25 Apr 2024 | 31 Jan 2025 | N/A | 

**Estimated release cadence:**6 months

**Valid Subscriptions:**OpenShift Container Platform / OpenShift Platform Plus

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends | 
|---|---|---|---|---|---|---|
| 0.158 | Rolling Stream | 4.12, 4.14, 4.16, 4.18, 4.19, 4.20, 4.21, 4.22, 5.0 | 08 Sep 2026 | 30 Nov 2026 | 30 Nov 2026 | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**3 months

**Valid Subscriptions:**OpenShift Kubernetes Engine / OpenShift Container Platform / OpenShift Platform Plus

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1.2 | Rolling Stream | 4.19, 4.20, 4.21, 4.22 | 14 Jul 2026 | 30 Nov 2026 | 30 Nov 2026 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (2)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 1.1 | Rolling Stream | 4.18, 4.19, 4.20, 4.21 | 14 Apr 2026 | 13 Jul 2026 | 13 Jul 2026 | N/A | 
| 1.0 | Rolling Stream | 4.17, 4.18, 4.19, 4.20 | 12 Aug 2025 | 13 Apr 2026 | 13 Apr 2026 | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**3 months

**Valid Subscriptions:**OpenShift Container Platform / OpenShift Platform Plus

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends | 
|---|---|---|---|---|---|---|
| 1.12 | Platform Agnostic | 4.12, 4.10, 4.11, 4.13 | 29 Jun 2023 | N/A | 30 Jun 2024 | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**6 months

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends | 
|---|---|---|---|---|---|---|
| 7.13 | Platform Agnostic | 4.12, 4.13, 4.14, 4.15, 4.16, 4.17, 4.18, 4.19, 4.20 | 10 Jun 2024 | N/A | 30 Jun 2024 | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**6 months

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends | 
|---|---|---|---|---|---|---|
| 1.13 | Platform Agnostic | 4.12, 4.13, 4.14, 4.15, 4.16, 4.17, 4.18, 4.19, 4.20 | 10 Jun 2024 | N/A | 30 Jun 2024 | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**6 months

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **End of Life versions (19)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 2.7 | Rolling Stream | N/A | 27 Feb 2024 | 21 May 2024 | N/A | N/A | 
| 2.6 | Rolling Stream | N/A | 06 Feb 2024 | 30 Apr 2024 | N/A | N/A | 
| 2.5 | Rolling Stream | N/A | 13 Dec 2023 | 31 Mar 2024 | N/A | N/A | 
| 2.4 | Rolling Stream | N/A | 27 Nov 2023 | 19 Feb 2024 | N/A | N/A | 
| 1.33 | Rolling Stream | N/A | 03 Oct 2023 | 27 Dec 2023 | N/A | N/A | 
| 1.32 | Rolling Stream | N/A | 05 Sep 2023 | 29 Nov 2023 | N/A | N/A | 
| 1.31 | Rolling Stream | N/A | 24 Aug 2023 | 17 Nov 2023 | N/A | N/A | 
| 1.30 | N/A | N/A | 01 Aug 2023 | 25 Oct 2023 | N/A | N/A | 
| 1.29 | N/A | N/A | 12 Jul 2023 | 10 Oct 2023 | N/A | N/A | 
| 1.28 | N/A | N/A | 20 Jun 2023 | 11 Sep 2023 | N/A | N/A | 
| 1.27 | N/A | N/A | 05 Jun 2023 | 27 Aug 2023 | N/A | N/A | 
| 1.26 | N/A | N/A | 10 May 2023 | 01 Aug 2023 | N/A | N/A | 
| 1.25 | N/A | N/A | 20 Apr 2023 | 04 Jul 2023 | N/A | N/A | 
| 1.24 | N/A | N/A | 28 Mar 2023 | 19 Jun 2023 | N/A | N/A | 
| 1.23 | N/A | N/A | 15 Mar 2023 | 06 Jun 2023 | N/A | N/A | 
| 1.22 | N/A | N/A | 14 Feb 2023 | 08 May 2023 | N/A | N/A | 
| 1.21 | N/A | N/A | 30 Jan 2023 | 23 Apr 2023 | N/A | N/A | 
| 1.20 | N/A | N/A | 11 Jan 2023 | 04 Apr 2023 | N/A | N/A | 
| 0.1 | N/A | N/A | 19 Sep 2022 | 10 Jan 2023 | N/A | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**3 months

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends | 
|---|---|---|---|---|---|---|
| 2.0 | Rolling Stream | 4.16, 4.18, 4.19, 4.20, 4.21, 4.22, 5.0 | 27 Oct 2026 | 31 Dec 2027 | 31 Dec 2027 | N/A | 
| 1.1 | Rolling Stream | 4.16, 4.18, 4.19, 4.20, 4.21, 4.22 | 20 May 2026 | 29 Oct 2026 | 29 Oct 2026 | N/A | 
| 1.0 | Rolling Stream | 4.15, 4.16, 4.17, 4.18, 4.19 | 09 Jun 2025 | 20 May 2026 | 20 May 2026 | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**12 months

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1.13 | Rolling Stream | 4.19, 4.20, 4.21, 4.22, 5.0 | 14 Jul 2026 | 30 Nov 2026 | 30 Nov 2026 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (3)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 1.12 | Rolling Stream | 4.18, 4.19, 4.20, 4.21 | 08 Apr 2026 | 13 Jul 2026 | 13 Jul 2026 | N/A | 
| 1.11 | Rolling Stream | 4.17, 4.18, 4.19, 4.20 | 02 Dec 2025 | 07 Apr 2026 | 07 Apr 2026 | N/A | 
| 1.10 | Rolling Stream | 4.16, 4.17, 4.18, 4.19 | 31 Jul 2025 | 01 Dec 2025 | 01 Dec 2025 | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**4 months

**Valid Subscriptions:**OpenShift Container Platform / OpenShift Platform Plus

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1.5 | Rolling Stream | 4.22, 4.21, 4.20, 4.19, 5.0 | 06 Oct 2026 | 28 Feb 2027 | 30 Jun 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 1.4 | Rolling Stream | 4.22, 4.21, 4.20, 4.19, 4.18 | 16 Apr 2026 | 06 Oct 2026 | 10 Dec 2026 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (4)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 1.3 | Rolling Stream | 4.20, 4.19, 4.18, 4.17, 4.16 | 07 Oct 2025 | 15 Apr 2026 | 06 Oct 2026 | N/A | 
| 1.2 | Rolling Stream | 4.15, 4.16, 4.17, 4.18, 4.19 | 02 May 2025 | 07 Oct 2025 | 16 Apr 2026 | N/A | 
| 1.1 | Rolling Stream | 4.14, 4.15, 4.16, 4.17 | 12 Nov 2024 | 02 May 2025 | 07 Oct 2025 | N/A | 
| 1.0 | Rolling Stream | 4.13, 4.14, 4.15, 4.16 | 18 Apr 2024 | 12 Nov 2024 | 13 Jan 2025 | N/A | 

**Estimated release cadence:**4 months

**Valid Subscriptions:**Red Hat Trusted Artifact Signer

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends | 
|---|---|---|---|---|---|---|
| 0.10 | Rolling Stream | 4.12, 4.14, 4.16, 4.17, 4.18, 4.19, 4.20, 4.21, 4.22, 5.0 | 17 Feb 2026 | 27 Oct 2026 | N/A | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**6 months

**Valid Subscriptions:**OpenShift Kubernetes Engine / OpenShift Container Platform / OpenShift Platform Plus

| Version | Tier | Supported OpenShift versions | OpenShift Aligned Version | General availability | Full support ends | Maintenance ends | EUS ends | EUS Term 2 ends | EUS Term 3 ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.11 | Rolling Stream | 4.16, 4.17, 4.18, 4.19 | N/A | 24 Nov 2025 | 03 May 2026 | 17 Dec 2026 | N/A | N/A | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (1)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 0.10 | Rolling Stream | 4.14, 4.15, 4.16, 4.17, 4.18, 4.19 | N/A | 21 Jan 2025 | 24 Nov 2025 | N/A | N/A | N/A | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**4 months

**Valid Subscriptions:**OpenShift Kubernetes Engine / OpenShift Container Platform / OpenShift Platform Plus

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends | 
|---|---|---|---|---|---|---|
| 7.6 | Rolling Stream | 4.12, 4.14, 4.16, 4.17, 4.18, 4.19, 4.20 | 01 Jun 2016 | 30 Jun 2022 | 30 Jun 2025 | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**Not Specified

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **End of Life versions (9)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 1.12 | Rolling Stream | 4.17 | 01 Oct 2024 | 25 May 2025 | 01 Apr 2026 | N/A | 
| 1.10 | Rolling Stream | 4.15 | 02 Apr 2024 | 27 Sep 2024 | 27 Aug 2025 | N/A | 
| 1.9 | Rolling Stream | 4.14 | 12 Dec 2023 | 27 May 2024 | 01 May 2025 | 31 Oct 2025 | 
| 1.4 | Rolling Stream | 4.9 | 29 Nov 2021 | 10 Jun 2022 | 18 Apr 2023 | N/A | 
| 1.3 | Rolling Stream | 4.8 | 11 Aug 2021 | 27 Jan 2022 | 27 Jan 2023 | N/A | 
| 1.8 | N/A | 4.13 | 06 Jun 2023 | 31 Jan 2024 | 17 Nov 2024 | N/A | 
| 1.7 | N/A | 4.12 | 28 Feb 2023 | 17 Aug 2023 | 17 Jul 2024 | N/A | 
| 1.6 | N/A | 4.11 | 27 Sep 2022 | 17 Apr 2023 | 10 Feb 2024 | N/A | 
| 1.5 | N/A | 4.10 | 18 May 2022 | 10 Nov 2022 | 10 Sep 2023 | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**Not Specified

**Valid Subscriptions:**OpenShift Container Platform / OpenShift Platform Plus

The following operators have a single rolling stream release and do not publish version information.

#### Red Hat OpenShift distributed tracing platform

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**3 months

#### Tempo Operator

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**3 months

**Valid Subscriptions:**OpenShift Container Platform / OpenShift Platform Plus

#### Red Hat OpenShift Dev Spaces

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3.31 | Rolling Stream | 4.16, 4.18, 4.19, 4.20, 4.21, 4.22, 5.0 | 27 Oct 2026 | 28 Feb 2027 | 28 Feb 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 3.30 | Rolling Stream | 4.16, 4.18, 4.19, 4.20, 4.21, 4.22, 5.0 | 02 Sep 2026 | 30 Jan 2027 | 30 Jan 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 3.29 | Rolling Stream | 4.16, 4.18, 4.19, 4.20, 4.21, 4.22 | 08 Jul 2026 | 30 Nov 2026 | 30 Nov 2026 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 3.28 | Rolling Stream | 4.16, 4.17, 4.18, 4.19, 4.20, 4.21 | 29 May 2026 | 09 Oct 2026 | 09 Oct 2026 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (44)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 3.27 | Rolling Stream | 4.16, 4.17, 4.18, 4.19, 4.20, 4.21 | 30 Mar 2026 | 29 Aug 2026 | 29 Aug 2026 | N/A | 
| 3.26 | Rolling Stream | 4.16, 4.17, 4.18, 4.19, 4.20, 4.21 | 10 Feb 2026 | 30 Jun 2026 | 30 Jun 2026 | N/A | 
| 3.25 | Rolling Stream | 4.16, 4.17, 4.18, 4.19, 4.20 | 15 Dec 2025 | 10 May 2026 | 10 May 2026 | N/A | 
| 3.24 | Rolling Stream | 4.20, 4.19, 4.18, 4.17, 4.16, 4.14 | 23 Oct 2025 | 15 Mar 2026 | 15 Mar 2026 | N/A | 
| 3.23 | Rolling Stream | 4.19, 4.18, 4.17, 4.16, 4.14 | 15 Sep 2025 | 23 Jan 2026 | 23 Jan 2026 | N/A | 
| 3.22 | Rolling Stream | 4.14, 4.15, 4.16, 4.17, 4.18, 4.19 | 29 Jul 2025 | 15 Dec 2025 | 15 Dec 2025 | N/A | 
| 3.21 | Rolling Stream | 4.14, 4.15, 4.16, 4.17, 4.18 | 28 May 2025 | 29 Oct 2025 | 29 Oct 2025 | N/A | 
| 3.20 | Rolling Stream | 4.18, 4.17, 4.16, 4.15, 4.14 | 17 Apr 2025 | 28 Aug 2025 | 28 Aug 2025 | N/A | 
| 3.19 | Rolling Stream | 4.14, 4.15, 4.16, 4.17, 4.18 | 13 Mar 2025 | 17 Jul 2025 | 17 Jul 2025 | N/A | 
| 3.18 | Rolling Stream | 4.14, 4.15, 4.16, 4.17 | 04 Feb 2025 | 13 Jun 2025 | 13 Jun 2025 | N/A | 
| 3.17 | Rolling Stream | 4.12, 4.13, 4.14, 4.15, 4.16, 4.17 | 25 Nov 2024 | 04 May 2025 | 04 May 2025 | N/A | 
| 3.16 | Rolling Stream | 4.12, 4.13, 4.14, 4.15, 4.16 | 13 Sep 2024 | 25 Feb 2025 | 25 Feb 2025 | N/A | 
| 3.15 | Rolling Stream | 4.13, 4.14, 4.15, 4.16 | 19 Jul 2024 | 13 Dec 2024 | 13 Dec 2024 | N/A | 
| 3.14 | Rolling Stream | 4.12, 4.13, 4.14, 4.15, 4.16 | 10 Jun 2024 | 19 Oct 2024 | 19 Oct 2024 | N/A | 
| 3.13 | Rolling Stream | 4.12, 4.13, 4.14, 4.15 | 30 Apr 2024 | 10 Sep 2024 | 10 Sep 2024 | N/A | 
| 3.12 | Rolling Stream | 4.12, 4.13, 4.14, 4.15 | 14 Mar 2024 | 30 Jul 2024 | 30 Jul 2024 | N/A | 
| 3.11 | Rolling Stream | 4.12, 4.13, 4.14, 4.15 | 31 Jan 2024 | 14 Jun 2024 | 14 Jun 2024 | N/A | 
| 3.10 | Rolling Stream | 4.11, 4.12, 4.13, 4.14 | 06 Dec 2023 | 30 Apr 2024 | 30 Apr 2024 | N/A | 
| 3.9 | Rolling Stream | 4.11, 4.12, 4.13, 4.14 | 20 Oct 2023 | 06 Mar 2024 | 06 Mar 2024 | N/A | 
| 3.8 | N/A | 4.10, 4.12, 4.13 | 30 Aug 2023 | 20 Jan 2024 | 20 Jan 2024 | N/A | 
| 3.7 | N/A | 4.10, 4.12, 4.13 | 06 Jul 2023 | 30 Nov 2023 | 30 Nov 2023 | N/A | 
| 3.6 | N/A | 4.10, 4.11, 4.12, 4.13 | 18 May 2023 | 06 Oct 2023 | 06 Oct 2023 | N/A | 
| 3.5 | N/A | 4.10, 4.11, 4.12 | 20 Mar 2023 | 18 Aug 2023 | 18 Aug 2023 | N/A | 
| 3.4 | N/A | 4.10, 4.11 | 09 Feb 2023 | 20 Jun 2023 | 20 Jun 2023 | N/A | 
| 3.3 | N/A | 4.10, 4.11 | 13 Dec 2022 | 09 May 2023 | 09 May 2023 | N/A | 
| 3.2 | N/A | 4.10, 4.11 | 24 Oct 2022 | 13 Mar 2023 | 13 Mar 2023 | N/A | 
| 3.1 | N/A | 4.10, 4.11 | 22 Aug 2022 | 24 Jan 2023 | 24 Jan 2023 | N/A | 
| 3.0 | N/A | 4.10 | 13 Jun 2022 | 22 Nov 2022 | 22 Nov 2022 | N/A | 
| 2.15 | N/A | 4.8, 4.10 | 15 Feb 2022 | 13 Sep 2022 | 13 Sep 2022 | N/A | 
| 2.14 | N/A | 4.8, 4.9 | 18 Jan 2022 | 15 May 2022 | 15 May 2022 | N/A | 
| 2.13 | N/A | 4.8, 4.9 | 30 Nov 2021 | 18 Apr 2022 | 18 Apr 2022 | N/A | 
| 2.12 | N/A | 4.8, 4.9 | 14 Oct 2021 | 01 Mar 2022 | 01 Mar 2022 | N/A | 
| 2.11 | N/A | 4.6 | 14 Sep 2021 | 14 Jan 2022 | 14 Jan 2022 | N/A | 
| 2.10 | N/A | 4.6 | 28 Jul 2021 | 14 Dec 2021 | 14 Dec 2021 | N/A | 
| 2.9 | N/A | 4.6 | 30 Jun 2021 | 28 Oct 2021 | 28 Oct 2021 | N/A | 
| 2.8 | N/A | N/A | 29 Apr 2021 | 30 Sep 2021 | 30 Sep 2021 | N/A | 
| 2.7 | N/A | 4.6 | 15 Mar 2021 | 29 Jul 2021 | 29 Jul 2021 | N/A | 
| 2.6 | N/A | 4.6 | 05 Feb 2021 | 15 Jun 2021 | 15 Jun 2021 | N/A | 
| 2.5 | N/A | 4.4 | 18 Nov 2020 | 18 May 2021 | 18 May 2021 | N/A | 
| 2.4 | N/A | 4.4 | 01 Oct 2020 | 01 Apr 2021 | 01 Apr 2021 | N/A | 
| 2.3 | N/A | 4.3, 4.4 | 20 Aug 2020 | 20 Feb 2021 | 20 Feb 2021 | N/A | 
| 2.2 | N/A | 4.3, 4.4 | 09 Jul 2020 | 09 Jan 2021 | 09 Jan 2021 | N/A | 
| 2.1 | N/A | 4.3 | 14 Apr 2020 | 14 Oct 2020 | 14 Oct 2020 | N/A | 
| 2.0 | N/A | 4.2 | 26 Nov 2019 | 09 Jul 2020 | 09 Jul 2020 | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**3 months

**Valid Subscriptions:**OpenShift Container Platform / OpenShift Platform Plus

#### DevWorkspace Operator

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends | 
|---|---|---|---|---|---|---|
| 1.0 | Rolling Stream | 4.16, 4.18, 4.19, 4.20, 4.21, 4.22, 5.0 | 13 Oct 2026 | 31 Jan 2027 | 31 Jan 2027 | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**3 months

#### Red Hat Trusted Profile Analyzer

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3.0 | Rolling Stream | 4.22, 4.21, 4.20, 4.19, 4.18 | 27 Jul 2026 | 31 Jan 2027 | 31 Jul 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 2.2 | Rolling Stream | 4.16, 4.17, 4.18, 4.19, 4.20 | 25 Nov 2025 | 27 Jul 2026 | 31 Dec 2026 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (6)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 2.1 | Rolling Stream | 4.15, 4.16, 4.17, 4.18, 4.19 | 28 Jul 2025 | 25 Nov 2025 | 27 Jul 2026 | N/A | 
| 2.0 | Rolling Stream | 4.14, 4.15, 4.16, 4.17, 4.18 | 16 Apr 2025 | 28 Jul 2025 | 25 Nov 2025 | N/A | 
| 1.3 | Rolling Stream | 4.14, 4.15, 4.16, 4.17 | 06 Feb 2025 | 16 Apr 2025 | 18 Apr 2025 | N/A | 
| 1.2 | Rolling Stream | 4.14, 4.15, 4.16, 4.17 | 18 Nov 2024 | 06 Feb 2025 | 16 Apr 2025 | N/A | 
| 1.1 | Rolling Stream | 4.14, 4.15, 4.16 | 03 Jul 2024 | 18 Nov 2024 | 06 Feb 2025 | N/A | 
| 1.0 | Rolling Stream | 4.14, 4.15 | 02 May 2024 | 03 Jul 2024 | 18 Nov 2024 | N/A | 

**Estimated release cadence:**4 months

**Valid Subscriptions:**Red Hat Trusted Profile Analyzer

**Operators sharing this lifecycle:**

- Red Hat Trusted Profile Analyzer (rhtpa-operator) — Update Info
- Red Hat Trusted Profile Analyzer exploit intelligence (exploit-iq-operator) — Update Info

#### streams for Apache Kafka

| Version | Tier | Supported OpenShift versions | General availability | Full support ends | Maintenance ends | EUS ends |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 3.2 | Platform Agnostic | 4.22, 4.21, 4.20, 4.19, 4.18, 4.16, 4.14, 4.12 | 04 May 2026 | 31 May 2027 | 30 Nov 2027 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| 2.9 | Platform Agnostic | 4.22, 4.21, 4.20, 4.19, 4.18, 4.16, 4.14, 4.12 | 13 Jan 2022 | 31 Mar 2026 | 31 Oct 2026 | N/A |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 
| **End of Life versions (3)** |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

| 3.1 | Platform Agnostic | 4.22, 4.21, 4.20, 4.19, 4.18, 4.16, 4.14, 4.12 | 16 Dec 2025 | 04 May 2026 | N/A | N/A | 
| 3.0 | Platform Agnostic | 4.22, 4.21, 4.20, 4.19, 4.18, 4.16, 4.14, 4.12 | 31 Jul 2025 | 16 Dec 2025 | N/A | N/A | 
| 1.8 | N/A | N/A | 21 Oct 2018 | 31 Jan 2022 | N/A | N/A | 

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**18 months

**Valid Subscriptions:**Red Hat AMQ / Red Hat Application Foundations

**Operators sharing this lifecycle:**

- Streams for Apache Kafka (amq-streams) — Update Info
- Streams for Apache Kafka Console (amq-streams-console) — Update Info
- Streams for Apache Kafka Proxy (amq-streams-proxy) — Update Info

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**4 months

**Valid Subscriptions:**OpenShift Kubernetes Engine / OpenShift Container Platform / OpenShift Platform Plus

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**Not Specified

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**Not Specified

**Valid Subscriptions:**OpenShift Kubernetes Engine / OpenShift Container Platform / OpenShift Platform Plus

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**Not Specified

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**Not Specified

**Additional Links:**Operator Update Information Checker

**Estimated release cadence:**Not Specified

**Valid Subscriptions:**Red Hat Application Foundations / Red Hat Integration

# Footnotes

- Red Hat can choose to address critical or important bug fixes upon request, with significant business impact for the customer through a hotfix, as a temporary measure while the bug fix patch is being created.
- The latest Major and Minor releases are the primary source for software enhancements. Roll-ups, updates, and patches are specifically reserved for bug fixes.
- Latest security update information available at: https://access.redhat.com/site/security/updates/
- Red Hat provides Critical impact security fixes and selected urgent-priority bug fixes, if and when available.
- Subscription information is provided per Operator Bundles in OpenShift Container Platform OperatorHub and may differ per Red Hat offering. The OpenShift Sizing and Subscription guide should be referenced for information on the various OpenShift offerings.
- Scope of coverage available at: https://access.redhat.com/support/offerings/production/soc/
- Service level agreements available at: https://access.redhat.com/support/offerings/production/sla
- Availability limited to specific architectures.
- Third-Party Support: https://access.redhat.com/third-party-software-support
