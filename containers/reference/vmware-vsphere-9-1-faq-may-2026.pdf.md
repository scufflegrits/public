FREQUENTLY ASKED QUESTIONS:  May 2026

vSphere with VCF 9.1
General FAQ

Table of Contents

vSphere Releases – Release 9.1

VMware vSphere Releases – Release 9.1

Q1. What are the new features in release 9.1?

General / Pricing and Packaging

Operational Efficiency

Security and Compliance

Performance

Kubernetes and Supervisor Services

Miscellaneous

A. Refer to the release notes for the definitive list including
smaller features and bug fixes. The features listed below
are the highlighted features for this release:

• Enhanced NVMe memory tiering

• Quick patching for vCenter

• Live patching support for TPM-enabled hosts

• vSphere elastic provisioning (Zero touch provisioning)

• DRS Parallel processing of vMotion

• Offload encrypted vMotion to Intel QAT

• Faster vMotion for GPU workloads

• Performance improvements with topology-aware

resource scheduling

• Confidential computing*

• Endpoint detection and response (EDR) on ESX

• File integrity monitoring

General / Pricing and Packaging

Q2. What is vSphere?

A. vSphere is the enterprise workload engine that

modernizes compute infrastructure, providing the best
platform for modern workloads, while enabling security
and compliance.

Q3. How can customers purchase vSphere?

A. VMware vSphere serves as a foundational component
of VMware’s two flagship offerings,  VMware Cloud
Foundation (VCF) and VMware vSphere Foundation
(VVF). It is also available in two standalone editions,
VMware vSphere Standard and VMware vSphere
Enterprise Plus. Note that vSphere Standard and
vSphere Enterprise Plus are limited to version 8 Update
3 and earlier. vSphere 9.0 and 9.1 features are only

1

vSphere: General FAQ

available as part of VMware vSphere Foundation 9.0

and 9.1 and VMware Cloud Foundation	9.0 and 9.1.

Some features are only available through the VMware
Advanced Cyber Compliance (ACC) offering.

without impact experience zero downtime during
patching, while impactful services are restricted to a
very short window.

Q8. What is vSphere elastic provisioning? What is Zero

Q4. Is the free ESXi version still available for customers?

touch provisioning?

A. Customers can download Free ESXi versions up to
version 8 Update 3. Versions 9.0 and 9.1 are not
available to customers through the free version of ESXi.

Q5. Are all features available in all variations of vSphere?

A. No. Please refer to the a) vSphere Version Comparison
and b) vSphere Product Line Comparison and c) VCF
Feature Comparison docs for a detailed description of
which features are available with which versions of
vSphere, VVF, VCF and ACC.

A. vSphere elastic provisioning is a collection of features

aimed at scaling provisioning of ESX hosts and making
them ready for easy consumption. The first phase of
these features includes Zero touch provisioning (ZTP). It
utilizes UEFI HTTP for secure bootstrapping of desired
image and drives host state toward a desired
configuration using vSphere Configuration Profiles.

Security and Compliance

Operational Efficiency

Q9. What are the new improvements in Live Patching

Q6. What is NVMe memory tiering and what are its

benefits?

A. vSphere introduced Memory Tiering with NVMe in

release 9.0, allowing users to add memory capacity to a
host by using an NVMe device as a secondary memory
tier that is installed locally in a host, thus resulting in an
increase of available memory within the ESXi host.

     NVMe tiering addresses core-to-memory imbalances
and helps in better VM consolidation. With a 19%
reduction in cores and offloading 20-25% of memory
accesses, this feature can lead to up to 40% reduction in
TCO.

Q7. What are the new enhancements for NVMe memory

tiering?

A. vSphere 9.1 removes the reboot requirement for turning
on memory tiering. It introduces UI notifications to easily
identify eligible clusters and workloads while providing
visibility into device health and wear to enable proactive
replacement. It also expands. It also introduces RAID 1
mirroring for memory tiering, to provide more resiliency,
and better protection against NVMe failure.

support?

A. vSphere expands Live Patching support to include hosts
with TPM enabled.  Additionally, this feature is turned
on by default. These two features maximize the changes
that customers can benefit from zero down time during
patching.

Q10. What confidential computing capabilities are

available to customers, and what benefits do they
provide?

A. The base functionality includes turning on confidential
computing on Intel and AMD based servers specifically
for Intel TDX and AMD SEV-SNP respectively. In 9.0,
VCF customers needed to go through an RPQ process
in order to access the confidential computing
functionality. In release 9.1, this functionality will become
generally available as part of ACC. Additionally,
incremental features such as Quick Boot for confidential
VMs will be available.

Q11. Is confidential computing capability included with

VCF, VVF and/or standalone vSphere?

A. No, confidential computing will be available with the

ACC SKU.

Q8. What is vCenter quick patching and what are its

benefits?

Q12. Does ESX support EDR?

A. vCenter updates often require significant maintenance

A. Yes, vSphere 9.1 introduces a secure, supported

windows and manual effort, leading to service
interruptions that make it difficult for administrators to
keep up with critical security patches. vCenter quick
patching intelligently classifies vCenter services into
those with and without workload impact. Services

framework allowing third-party EDR agents to integrate
directly into the ESX hypervisor. This enables leading
EDR platforms to natively analyze process, file, and
network events for suspicious activity right at the
foundational layer.

Frequently Asked Questions | 2

Kubernetes and Supervisor Services

Q17. What is VMware vSphere Kubernetes Service?

A. VMware vSphere Kubernetes Service (VKS) is a built-in
Kubernetes runtime service in VCF. It orchestrates
Kubernetes management, enabling enterprises to run
modern applications alongside traditional workloads.
Running modern applications on VKS within VMware
Cloud Foundation (VCF) offers enterprises a powerful,
unified platform that integrates with the broader
VMware ecosystem, delivering a scalable, secure, and
efficient foundation for modern workloads. For more
information on VKS and new features in 9.1 please refer
to the VCF FAQ.

Miscellaneous

Q18. Where can I get a definitive list of feature

capabilities within vSphere?

A. Please refer to the a) vSphere Version Comparison and

b) vSphere Product Line Comparison and c) VCF
Feature Comparison docs for a detailed description of
which features are available with which versions of
vSphere, VVF, VCF and ACC.

vSphere: General FAQ

Q13. What are the benefits of file integrity monitoring?

A. File integrity monitoring ensures continuous

infrastructure security and compliance by enabling rapid
detection of tampering. It alerts administrators to
unauthorized modifications across critical assets,
including vCenter configuration files, before they can be
exploited.

Performance

Q14.How does vSphere help improve performance of all

workloads in release 9.1?

A. vSphere 9.1 optimizes for the next generation of high-

density processors through topology-aware scheduling.
By updating the NUMA scheduler to be more like DRS,
and using the same fairness models, vSphere enables
customers to improve the performance of a wide variety
of workloads by up to 68% on 4 socket systems and up
to 44% on 2 socket systems.

Q15.How does vSphere boost performance for guest

VMs?

A. vSphere leverages Intel’s Quick Assist Technology (QAT)

to offload encryption, decryption, and compression
tasks from the host/destination CPU during the vMotion
process. This feature delivers up to a 67% saving in
source CPU consumption and a 22% saving in
destination CPU usage. This boosts guest performance
during migration and frees up critical resources for other
applications.

Q16.How does vSphere improve performance for AI

workloads?

A. vSphere introduces passthrough support for the latest
class of high-performance accelerators, including Intel
Gaudi 3, AMD MI300, and NVIDIA Blackwell HGX
systems with NVSwitch for massive, multi-host AI model
distribution. vSphere boosts efficiency by increasing
GPU sharing capacity allowing up to 48 VMs per GPU
and providing a unified monitoring dashboard to track
capacity and utilization across different hardware
vendors.

Copyright © 2025 Broadcom. All rights reserved.
The term “Broadcom” refers to Broadcom Inc. and/or its subsidiaries. For more information, go to www.broadcom.com. All trademarks, trade names, service marks, and logos
referenced herein belong to their respective companies. Broadcom reserves the right to make changes without further notice to any products or data herein to improve
reliability, function, or design. Information furnished by Broadcom is believed to be accurate and reliable. However, Broadcom does not assume any liability arising out of the
application or use of this information, nor the application or use of any product or circuit described herein, neither does it convey any license under its patent rights nor the
rights of others.
Item No: vmw-bc-faq-a4-word-2025 May-25

