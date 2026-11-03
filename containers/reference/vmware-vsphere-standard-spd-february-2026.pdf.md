VMware vSphere Standard

Specific Program Documentation (“SPD”)

The Broadcom software program(s) (“Software”) listed below is provided under the following terms and conditions in addition to any
terms and conditions referenced on the Broadcom quote, order form, statement of work, or other mutually agreed ordering document
(each a “Transaction Document”) under the applicable end user agreement or governing contract (collectively, the “Agreement”)
entered into by Customer and the Broadcom entity (“Broadcom”) through which Customer obtained a license for the Software. These
terms shall be effective from the effective date of such Transaction Document. Capitalized terms have the meanings ascribed to them
herein, or, otherwise, in the Agreement.

The version of the SPD published on legaldocs.broadcom.com on the date that Broadcom accepts the Customer’s Transaction Document
for Software applies to the version of Software in that Transaction Document. If Customer installs a release of Software that Broadcom
provides  as  part  of  Support  services,  then  the  then-current  version  of  the  SPD  published  on  legaldocs.broadcom.com  on  the  date
Customer installs that release applies to that release of Software.

Program Name: VMware vSphere Standard

1.  DEFINITIONS.

All terms defined in the VMware Licensing Glossary published on https://docs.broadcom.com/doc/vmware-licensing-glossary
apply to this SPD unless specified herein.

“BIOS” means the Basic Input Output System, a set of routines that boots the operating system and sets up the hardware of
the Processor.

“Cloud Services” means computing infrastructure (including compute, storage, networking, security, management etc.) that
a Customer does not own, and which a third party markets or makes available as a service to its customers (including as a
bundle of, or as integrated with, managed services). Notwithstanding the foregoing, Cloud Services excludes infrastructure
deployed on-premises (whether in Customer’s data center or a co-location facility) provided that the third party who markets
or makes available the said infrastructure does not have access to, and does not perform any services with respect to, the
Software (including managed services, installation, etc).

“Core” means a single physical computational unit of the Processor.

“Deemed Internal Purpose Application” or “DIPA” means a software application that:

i) either:

A)  Customer  has  internally  developed  for  use  by  its  internal  or  external  users  (including  Customer’s

customers or partners), or

B)  Customer has procured from a third party for use by Customer’s internal or external users to perform
a  business  operational  task  enabling  those  user’s  use  of  or  access  to  Customer's  products  or
services (Customer’s users as authorized in i) A) and B) collectively, “DIPA Users”);
ii) runs on Software but DIPA Users cannot access the Software or benefit from Software’s features or functionalities;
iii) is not ancillary to, embedded with, or packaged with a product or services that:

A)  has any features or functionalities that directly or indirectly are related to, complementary with, or
competitive with, any features or functionalities of Software (including the management, delivery or
hosting thereof), or
is  any  form  of  managed  services  or  information  technology  services  including  hosting  services,
business  process  and  infrastructure  outsourcing  services,  support  services,  cloud  services
(excluding Customer’s internally developed applications delivered in a cloud model that meet all other
conditions of the definition of DIPA), integration services, professional services etc.; and

B)

iv) is not commercializing or embedding any features or functionalities of Software in any manner (including extensions
or expansions thereof).

February 2026

VMware vSphere Standard

Specific Program Documentation

Examples of DIPA applications include a financial institution Customer running an application on Software (that it developed
or procured) for its banking customers to use to obtain information about their bank accounts, a grocery chain Customer running
an application on Software (that it developed or procured) to operate its in-store point of sale machines, an airline running an
application  on  Software  that  it  developed  or  procured  to  operate  self  check-in  kiosks  in  airports,  and  a  software  company
Customer delivering their internally developed human resource software application that runs on Software in a cloud model to
third party customers.
Examples of applications that are not DIPA applications include a service provider Customer hosting a third party’s application
on Software for its customers, a Customer running any application on Software to deliver hosted services, and a cloud services
or infrastructure services (including when combining their own applications with Software) to third parties.

“Instance” means a single installation of the Software on a physical server or Virtual Machine.

“Processor” means a single, physical chip that houses at least one Core that can execute computer programs.

“Server” means a hardware system capable of running the server software. A hardware partition or blade is considered a
separate hardware system.

“Virtual Machine” means a software container that can run its own operating system and execute applications like a physical
machine.

2.    USE RIGHTS AND LIMITATIONS.

●  License Metric. Software is subscription software licensed on a per Core license metric with a minimum licensing requirement

of 16 Cores per Processor.

●  Licensed Cores. Each Core on the Server where Software is installed must be licensed, including Cores deactivated by the
BIOS. The required number of Core licenses equals the number of Cores on the Server, subject to the minimum of 16 Core
licenses per Processor. Customer may use Software on a Server with up to the number of Cores for which Customer has paid
the applicable license fees.

●  Migration License. Customer may use its license to Software as a Migration License (as defined in the Agreement) by using

Software’s embedded evaluation mode feature for a maximum period allowed by that feature.

●  Component Specific Rights and Limitations. The following table describes additional component specific license entitlement

rights and limitations of vSphere Standard:

vSphere
Standard
Component

Metric
Entitlement

vSphere

1 Core

#

1

Entitlement Details

VMware Tools is a suite of utilities and drivers that can be installed in a Guest Operating
System to enhance the performance and functionality of a Guest Operating System when
running in a Virtual Machine in conjunction with a vSphere hypervisor. Customer may not
use VMware Tools with any other hypervisor. Customer may distribute the VMware Tools to
third parties solely when installed in a Guest Operating System within a Virtual Machine.
Customer is liable for compliance by those third parties with the terms and conditions of the
Framework Agreement.

2

vCenter
Server

1 Instance

vCenter Server may be used to provide centralized management capabilities to any licensed
VMware by Broadcom infrastructure environments with an active subscription to Support and
Subscription Services.

●  Restrictions on Use with Cloud Services. Customer must not (and must not allow Customer’s Third-Party Agents to) use or

deploy the Software on any Cloud Services.

●  Underlying Hardware. Customer may only use Software on hardware that meets the then-current applicable Broadcom

requirements for such hardware in the Documentation, the Broadcom Software Maintenance Policy Handbook, and the
Broadcom Compatibility Guide found here: https://compatibilityguide.broadcom.com.

February 2026

2

VMware vSphere Standard

Specific Program Documentation

●  Hosting Rights and Restrictions. Customer may use the Software to deliver its Deemed Internal Purpose Application(s) to a
third party via an internal or external network. Except as expressly provided in this paragraph, the use of the Software for  any
other types of hosting or for the benefit of any third party in any manner is strictly prohibited.

●  Support Services. License to Software includes entitlement to support and maintenance services that may only be used for

Software licensed herein, and may not be used for any other software, including former offers of components of Software that
Customer may have licensed separately.

●  Benchmarking. Customer may use Software to conduct internal performance testing and benchmarking studies. Customer

may only disclose, publish or distribute the results of the studies to third parties if Broadcom has reviewed and approved of the
methodology, assumptions, and other parameters of the study prior to publication and distribution. Customer must submit such
requests to vmware-benchmark.pdl@broadcom.com.

●  Legacy Perpetual License Upgrade Restrictions. Customers with perpetual licenses to legacy VMware software that also

used the name vSphere Standard when it was offered and who have active subscription to Support and Subscription Services
(“Legacy Perpetual Software”) are entitled to upgrade to Software version 8.x until the earlier of their Support and
Subscription Services end date or the end of support of version 8.x. For clarity, Customers do not have an entitlement to
upgrade Legacy Perpetual Software to any version of Software above 8.x.

3.

THIRD PARTY INFORMATION AND TERMS.

●  Any required third-party software license terms are incorporated by this reference and are set forth in online documentation

at techdocs.broadcom.com or legaldocs.broadcom.com.

February 2026

3

