---
title: Licensing standalone ESXi hosts in VMware Cloud Foundation and vSphere Foundation 9.1 environments
url: https://knowledge.broadcom.com/external/article/458772/licensing-standalone-esxi-hosts-in-vmwar.html
hostname: broadcom.com
description: Licensing standalone ESXi hosts in VMware Cloud Foundation and vSphere Foundation 9.1 environments
sitename: Broadcom Inc
date: "2026-01-01"
fingerprint: "7b656ed04d27f38f"
---
VMware vSphere ESXi

VMware Cloud Foundation (VCF) and VMware vSphere Foundation (VVF) 9.1 introduce a centralized, subscription-based licensing architecture. Traditional 25-character license keys are not supported. This article outlines the requirements and supported deployment models for licensing hosts in 9.1 environments, including air-gapped or standalone scenarios

- VMware Cloud Foundation 9.1
- VMware vSphere Foundation 9.1
- VCF Operations 9.1
- Isolated (Air-gapped) or Connected networks

Licensing for version 9.1 and later utilizes a centralized Solution License File managed by VCF Operations. Standalone license keys cannot be applied directly to individual ESXi hosts or vCenter instances independently. A management footprint consisting of VCF Operations and vCenter is required to generate and apply licensing.

To license ESXi 9.1 hosts in a standalone or isolated environment, execute the following steps to deploy the required management stack:

1. Deploy VCF Operations 9.1 using the supported manual deployment workflow.
2. Register the VCF Operations instance in the VCF Business Services console.
3. For isolated environments, follow the disconnected registration workflow.
4. Assign a primary license to your vCenter Server 9.1 instance via the VCF Operations console.
5. Add the ESXi host to the vCenter Server. The host inherits the license automatically from the vCenter instance.
6. Verify the host license status in the vSphere Client.
Note: If deployment of the management stack is not feasible, remaining on ESXi 8.x is the only supported path for standalone, unmanaged licensing.

Yes

No
