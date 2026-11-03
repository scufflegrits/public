---
title: Ceased Renewal of "Infrastructure" SKUs for Obsolete Workflows - Red Hat Customer Portal
url: https://access.redhat.com/solutions/7118759
hostname: redhat.com
description: Some customers who renew their subscriptions may receive a slightly different bill of materials than previous contracts. The reasons for this could be unclear, and this article will clarify.
sitename: Red Hat Customer Portal
date: "2025-05-08"
tags: ['subscription_management, subscription_watch']
fingerprint: bfbd40d62d0085c9
---
# Ceased Renewal of "Infrastructure" SKUs for Obsolete Workflows

## Environment

Renewals in the Red Hat OpenShift Container Platform and Red Hat Virtualization family after May 8th, 2025.

## Issue

Some customers who renew their subscriptions may receive a slightly different bill of materials than previous contracts. The reasons for this could be unclear, and this article will clarify.

## Resolution

### Why is there a change?

Red Hat offers the self-managing portions of its software platform for free. Any components focused on care and feeding of the software platform rather than executing customer workloads are offered gratis, but historically required a special subscription for compatibility with existing entitlement tooling. Part of retiring these tools is eliminating the need for the "infra" subscriptions that supported infra deployments.

Current versions of Red Hat's software platforms are designed to identify and ignore infrastructure AKA control plane deployments.

### What is changing?

#### Subscriptions for Red Hat Virtualization no longer awarded for RHV renewals:

- RV00045
- RV00046
- RV00100
- RV00099

The above SKUs were used to provision "free" RHEL in the name of running RHV Manager. Simple Content Access will now allow RHV customers to freely provision RHEL for their RHV Managers.

#### Subscriptions for Red Hat OpenShift Container Platform no longer awarded for OCP renewals:

- MCT2741
- MCT3857
- MW00420
- MW00787
- MW00700

The above SKUs were used to provision "free" RHEL serving as Infrastructure nodes for OCP version 3. Simple Content Access will now allow OCP version 3 customers to freely provision RHEL servers for their Infrastructure nodes.

### FAQ

#### I am an extended lifecycle RHV customer and after my renewal the RHEL usage screens at the Hybrid Cloud Console tell me I am over-provisioned. What do I do?

Work with your account team. Total EOL for RHV is August 31, 2026 - and a very few accounts could encounter this. The overall ratio of RHV Managers to RHEL guests should be small, and differentiated by infra type at the subscription service. Some customers may be able to ignore "Physical" RHEL entirely.

#### I am an extended lifecycle OpenShift 3 customer - will I see any RHEL oddities at the Hybrid Cloud Console?

You should not. The HCC already groups RHEL systems running OpenShift as part of the OpenShift usage page. v3 clusters are known to run about 15% Infra overhead, as indicated in the HCC Subscriptions service docs (see the blue Note).

#### I am OpenShift 4+ customer. I won't see any impact, will I?

You will not. As indicated in the HCC Subscriptions service docs, all current version of OpenShift 4 self-identify Infra / Control Plane usage and automatically discount it. Infra subscriptions were never necessary for OpenShift v4+.

## Root Cause

An update to entitlement tooling, retiring no longer needed SKUs, and renewals of EOL products.

## Diagnostic Steps

N/A

This solution is part of Red Hat’s fast-track publication program, providing a huge library of solutions that Red Hat engineers have created while supporting our customers. To give you the knowledge you need the instant it becomes available, these articles may be presented in a raw and unedited form.

## Comments
