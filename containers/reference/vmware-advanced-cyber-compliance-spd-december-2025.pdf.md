Advanced Cyber Compliance
Specific Program Documentation (“SPD”)
The Broadcom software program (“Software”) listed below is provided under the following terms and conditions in addition to any terms
and conditions referenced on the Broadcom quote, order form, statement of work, or other mutually agreed ordering document (each a
“Transaction Document”) under the applicable end user agreement or governing contract (collectively, the “Agreement”) entered into
by the Customer and the Broadcom entity (“Broadcom”) through which Customer obtained a license for Software. These terms shall be
effective from the effective date of such Transaction Document. Capitalized terms have the meanings ascribed to them herein, or,
otherwise, in the Agreement.
The version of the SPD published on legaldocs.broadcom.com on the date that Broadcom accepts the Customer’s Transaction Document
for Software applies to the version of Software in that Transaction Document. If the Customer installs a release of Software that Broadcom
provides as part of Support services, then the then-current version of the SPD published on legaldocs.broadcom.com on the date the
Customer installs that release applies to that release of Software.
Program Name: Advanced Cyber Compliance
1. DEFINITIONS.
All terms defined in the VMware Licensing Glossary published on https://docs.broadcom.com/doc/vmware-licensing-glossary
apply to this SPD unless specified herein.
“BIOS” means the Basic Input Output System, a set of routines that boots the operating system and sets up the hardware of
the Processor.
“Cloud Services” means computing infrastructure (such as compute, storage, networking, security, management etc.), including
related managed services, that a third party provider owns and makes available for use by customers (e.g. Amazon EC2, Dell
APEX, Google GCP, HPE GreenLake, Microsoft Azure, Oracle OCI, etc.).
“Core” means a single physical computational unit of the Processor.
“Deemed Internal Purpose Application” or “DIPA” means a software application that:
i) either:
A) Customer has internally developed for use by its internal or external users (including Customer’s
customers or partners), or
B) Customer has procured from a third party for use by Customer’s internal or external users to perform
a business operational task enabling those user’s use of or access to Customer's products or
services (Customer’s users as authorized in i) A) and B) collectively, “DIPA Users”);
ii) runs on Software but DIPA Users cannot access the Software or benefit from Software’s features or functionalities;
iii) is not ancillary to, embedded with, or packaged with a product or services that:
A) has any features or functionalities that directly or indirectly are related to, complementary with, or
competitive with, any features or functionalities of Software (including the management, delivery or
hosting thereof), or
B) is any form of managed services or information technology services including hosting services,
business process and infrastructure outsourcing services, support services, cloud services
(excluding Customer’s internally developed applications delivered in a cloud model that meet all other
conditions of the definition of DIPA), integration services, professional services etc.; and
iv) is not commercializing or embedding any features or functionalities of Software in any manner (including extensions
or expansions thereof).
Examples of DIPA applications include a financial institution Customer running an application on Software (that it developed
or procured) for its banking customers to use to obtain information about their bank accounts, a grocery chain Customer running
an application on Software (that it developed or procured) to operate its in-store point of sale machines, an airline running an
application on Software that it developed or procured to operate self check-in kiosks in airports, and a software company
December 2025

Advanced Cyber Compliance Specific Program Documentation
Customer delivering their internally developed human resource software application that runs on Software in a cloud model to
third party customers.
Examples of applications that are not DIPA applications include a service provider Customer hosting a third party’s application
on Software for its customers, a Customer running any application on Software to deliver hosted services, and a cloud services
or infrastructure services (including when combining their own applications with Software) to third parties.
“Processor” means a single, physical chip that houses at least one Core that can execute computer programs.
“Server” means a hardware system capable of running the server software. A hardware partition or blade is considered a
separate hardware system.
“vCenter Instance” means the vCenter Server component of Permitted Software Base.
2. USE RIGHTS AND LIMITATIONS.
● Permitted Base Software. Software may only be used as an add-on to active subscriptions to the following Broadcom software
(“Permitted Base Software”): VMware Cloud Foundation, VMware Telco Cloud Platform, and VMware Cloud Foundation Edge.
Software may not be used with, or the benefit of, any software other than Permitted Base Software.
● Licensing Metric. Software is licensed on a per Core license metric.
● Licensed Cores. Each Core, including Cores deactivated by the BIOS, managed by vCenter Instance(s) where Software is
utilized, or for which Software is installed, must be licensed. For clarity, Customer does not need to license Software for all
vCenter Instance(s) that Customer is entitled to, but in the event that Customer chooses to use and/or install Software on Cores
managed by a vCenter Instance, then all Cores in that vCenter Instance must have a license to Software. Customer may use
Software up to the number of Cores for which Customer has paid the applicable license fees. The minimum number of Cores
per Processor that Customer must license is the same quantity of Cores per Processor that the SPD applicable to the Permitted
Base Software requires as the minimum for that Permitted Base Software.
● Cyber and Disaster Recovery Feature Deployment. For use of the cyber and disaster recovery feature of Software, Customer
must have licenses to Permitted Base Software at both the source and target sites. For clarity, Customer may only use Software
to protect Cores licensed for Software as per the bullet above.
● Migration License. Customer may use its license to Software as a Migration License (as defined in the Agreement) by using
Software’s embedded evaluation mode feature for a maximum period allowed by that feature.
● License Portability Entitlement. Customer must not (and must not allow Customer’s Third-Party Agents to) use or deploy the
Software on any Cloud Services except to the extent when Software is being used exclusively as an add-on to a license to
VMware Cloud Foundation that has an entitlement which enables it to do so (in which case the right to use or deploy Software
on any Cloud Services shall be the same as the right described in the SPD applicable to the said license to VMware Cloud
Foundation).
● Underlying Hardware. Customer may only use Software on hardware that meets the then-current applicable Broadcom
requirements for such hardware in the Documentation, the Broadcom Software Maintenance Policy Handbook, and the
Broadcom Compatibility Guide found here: https://compatibilityguide.broadcom.com.
● Hosting Rights and Restrictions. Customer may use the Software to deliver its Deemed Internal Purpose Application(s)
to a third party via an internal or external network. Except as expressly provided in this paragraph, the use of the Software
for any other types of hosting or for the benefit of any third party in any manner is strictly prohibited.
● Support Services. License to Software includes entitlement to support and maintenance services that may only be used
for Software licensed herein.
● Benchmarking. Customer may use Software to conduct internal performance testing and benchmarking studies. Customer
may only disclose, publish or distribute the results of the studies to third parties if Broadcom has reviewed and approved of
the methodology, assumptions, and other parameters of the study prior to publication and distribution. Customer must
submit such requests to vmware-benchmark.pdl@broadcom.com.
3. THIRD PARTY INFORMATION AND TERMS.
December 2025 2

| Advanced Cyber Compliance  |     |     |     |     | Specific Program Documentation  |     |
| -------------------------- | --- | --- | --- | --- | ------------------------------- | --- |

●  Any required third-party software license terms are incorporated by this reference and are set forth in online documentation
at techdocs.broadcom.com or legaldocs.broadcom.com.

|                |     |     |     |     |     |      |
| -------------- | --- | --- | --- | --- | --- | ---- |
| December 2025  |     |     |     |     |     |   3  |