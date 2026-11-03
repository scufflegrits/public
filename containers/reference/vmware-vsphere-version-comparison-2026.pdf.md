VMware vSphere®
Version Comparison
VMware vSphere is available in two standalone editions, VMware vSphere Standard and VMware vSphere
Enterprise Plus, and is also included as a component in VMware Cloud Foundation and VMware vSphere
Foundation. Note that vSphere Standard and vSphere Enterprise Plus are only available as versions up to the 8
Update 3 release. Currently, vSphere 9.1 features are only available as part of VMware vSphere Foundation 9.1
and VMware Cloud Foundation 9.1.
vSphere Version Comparison
Key Features / Capabilities Version 7.x Version 8.x Version 9.x
Key Attributes
| vCenter Lifecycle Management Service | ✓   | ✓   | ✓   |
| ------------------------------------ | --- | --- | --- |
Kubernetes Runtime and Supervisor Services
| vSphere Kubernetes Service (VKS) | ✓   | ✓   | ✓   |
| -------------------------------- | --- | --- | --- |
| VM Service                       | ✓   | ✓   | ✓   |
| Storage Service                  | ✓   | ✓   | ✓   |
|                                  | ✓   | ✓   | ✓   |
Network Service
|     | ✓   | ✓   | ✓   |
| --- | --- | --- | --- |
Container Registry Service
| Harbor Image Registry Service | ✓   | ✓   | ✓   |
| ----------------------------- | --- | --- | --- |
| vSphere Pod Service           | ✓   | ✓   | ✓   |
| Load Balancer Service         | ✓   | ✓   | ✓   |
| Service Mesh                  |     |     | ✓   |
| External DNS                  | ✓   | ✓   | ✓   |
| ArgoCD                        |     |     | ✓   |
|                               | ✓   | ✓   | ✓   |
Secret Service
1

VMware vSphere® Version Comparison
vSphere Version Comparison
Key Features / Capabilities Version 7.x Version 8.x Version 9.x
| IaaS Policy Service | ✓   | ✓   | ✓   |
| ------------------- | --- | --- | --- |
|                     | ✓   | ✓   | ✓   |
Data Services
|     | ✓   | ✓   | ✓   |
| --- | --- | --- | --- |
AI Services
| Workload Availability Zones                 |     | ✓   | ✓   |
| ------------------------------------------- | --- | --- | --- |
| Simplified VKS cluster lifecycle Management |     | ✓   | ✓   |
| Customizable base OS Images                 |     | ✓   | ✓   |
| Supervisor Independent Updates              |     |     | ✓   |
| Custom Zone Optimization                    |     |     | ✓   |
Operations Management
| vSphere Lifecycle Manager | ✓   | ✓   | ✓   |
| ------------------------- | --- | --- | --- |
|                           |     | ✓   | ✓   |
Live Patching for ESX
|     | ✓   | ✓   | ✓   |
| --- | --- | --- | --- |
vCenter Server Profiles
| vCenter Update Planner                                | ✓   | ✓   | ✓   |
| ----------------------------------------------------- | --- | --- | --- |
| Content Library                                       | ✓   | ✓   | ✓   |
| vSphere Configuration Profiles                        |     | ✓   | ✓   |
| Host Profiles                                         | ✓   | ✓   | ✓   |
| Auto Deploy                                           |     | ✓   | ✓   |
| vSphere Elastic Provisioning(Zero Touch Provisioning) |     |     | ✓   |
|                                                       | ✓   | ✓   |     |
Virtual Volumes (vVols)
|     |     | ✓   | ✓   |
| --- | --- | --- | --- |
Green Metrics
Built-in Security
| Identity Federation                          | ✓   | ✓   | ✓   |
| -------------------------------------------- | --- | --- | --- |
| Hardware TPM 2.0 Support                     | ✓   | ✓   | ✓   |
| Virtual TPM 2.0                              | ✓   | ✓   | ✓   |
| FIPS 140-2 and Common Criteria Certification | ✓   | ✓   | ✓   |
Solution Overview | 2

VMware vSphere® Version Comparison
vSphere Version Comparison
Key Features / Capabilities Version 7.x Version 8.x Version 9.x
| TLS 1.2 | ✓   | ✓   | ✓   |
| ------- | --- | --- | --- |
|         |     | ✓ 1 | ✓ 1 |
TLS 1.3
|     | ✓   | ✓   | ✓   |
| --- | --- | --- | --- |
Virtual Machine Encryption
| Standard Key Provider (External KMS) | ✓   | ✓   | ✓   |
| ------------------------------------ | --- | --- | --- |
| Native Key Provider                  | ✓   | ✓   | ✓   |
| Secure boot                          | ✓   | ✓   | ✓   |
| File Integrity Monitoring            |     |     | ✓   |
| Confidential Computing               |     |     | ✓   |
| EDR Integration for ESX              |     |     | ✓   |
✓
Memory Tiering Encryption on NVMe
Application Performance
|     | ✓   | ✓   | ✓   |
| --- | --- | --- | --- |
Per-VM Enhanced vMotion Compatibility (EVC)
| Instant Clone                        | ✓   | ✓   | ✓   |
| ------------------------------------ | --- | --- | --- |
| Distributed Resource Scheduler (DRS) | ✓   | ✓   | ✓   |
| Storage DRS                          | ✓   | ✓   | ✓   |
| Distributed Power Management (DPM)   | ✓   | ✓   | ✓   |
| Storage Policy-Based Management      | ✓   | ✓   | ✓   |
| I/O Controls (storage)               | ✓   | ✓   | ✓   |
|                                      |     | ✓   | ✓   |
Single Root I/O Virtualization (SR-IOV)
|     | ✓   | ✓   | No2 |
| --- | --- | --- | --- |
vSphere persistent memory
| Memory Tiering               |     |     | ✓   |
| ---------------------------- | --- | --- | --- |
| NVIDIA GRID vGPU             | ✓   | ✓   | ✓   |
| Accelerated Graphics for VMs | ✓   | ✓   | ✓   |
| Dynamic DirectPath IO        | ✓   | ✓   | ✓   |
| Vendor Device Group          |     | ✓   | ✓   |
Solution Overview | 3

VMware vSphere® Version Comparison
vSphere Version Comparison
Key Features / Capabilities Version 7.x Version 8.x Version 9.x
| Heterogeneous vGPU profiles on same GPU |     | ✓   | ✓   |
| --------------------------------------- | --- | --- | --- |
|                                         |     | ✓   | ✓   |
DRS automation for vGPU workloads
|     |     | ✓   | ✓   |
| --- | --- | --- | --- |
Support for NVIDIA NVSwitch and NVLink
Business Continuity
| vMotion                      | ✓   | ✓   | ✓   |
| ---------------------------- | --- | --- | --- |
| Cross-vCenter vMotion4       | ✓   | ✓   | ✓   |
| Encrypted vMotion            | ✓   | ✓   | ✓3  |
| vCenter Enhanced Linked Mode | ✓   | ✓   | ✓4  |
| vSMP                         | ✓   | ✓   | ✓   |
| High Availability (HA)       | ✓   | ✓   | ✓   |
|                              | ✓   | ✓   | ✓   |
Proactive HA
|     | ✓   | ✓   | ✓   |
| --- | --- | --- | --- |
Storage vMotion
| Fault Tolerance                       | ✓   | ✓   | ✓   |
| ------------------------------------- | --- | --- | --- |
| vSphere Replication                   | ✓   | ✓   | ✓   |
| Support for 4k Native Storage         | ✓   | ✓   | ✓   |
| vSphere Quick Boot                    | ✓   | ✓   | ✓   |
| vCenter File-Based Backup and Restore | ✓   | ✓   | ✓   |
| vCenter Server Appliance Migration    | ✓   | ✓   | ✓   |
|                                       | ✓   | ✓   | ✓   |
Cross vCenter Mixed Version Provisioning
|     | ✓   | ✓   | ✓   |
| --- | --- | --- | --- |
Hot and Cold Migration to the Cloud
| Policy-based Governance |     | ✓   | ✓   |
| ----------------------- | --- | --- | --- |
(1) - For more information about use of TLS 1.3 with FIPS 140-3 requirements consult the product documentation.
(2) –Not supported on 9.0
(3) – With Intel QAT offload in vSphere 9.1.
(4) – Deprecated in 9.0.
Copyright © 2026 Broadcom. All rights reserved.
The term “Broadcom” refers to Broadcom Inc. and/or its subsidiaries. For more information, go to www.broadcom.com. All trademarks, trade names, service marks, and logos
referenced herein belong to their respective companies. Broadcom reserves the right to make changes without further notice to any products or data herein to improve reliability,
function, or design. Information furnished by Broadcom is believed to be accurate and reliable. However, Broadcom does not assume any liability arising out of the application or
use of this information, nor the application or use of any product or circuit described herein, neither does it convey any license under its patent rights nor the rights of others.
Item No: vsphere-9-1-version-comparison_V3 4/26