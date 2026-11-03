VMware Cloud Foundation (VCF)
Specific Program Documentation (“SPD”)

The Broadcom software program(s) (“Software”) listed below is provided under the following terms and conditions in addition
to any terms and conditions referenced on the Broadcom quote, order form, statement of work, or other mutually agreed
ordering  document  (each  a  “Transaction  Document”)  under  the  applicable  end  user  agreement  or  governing  contract
(collectively, the “Agreement”) entered into by Customer and the Broadcom entity (“Broadcom”) through which Customer
obtained a license for the Software. These terms shall be effective from the effective date of such Transaction Document.
Capitalized terms have the meanings ascribed to them herein, or, otherwise, in the Agreement.

The  version  of  the  SPD  published  on  legaldocs.broadcom.com  on  the  date  that  Broadcom  accepts  the  Customer’s
Transaction Document for Software applies to the version of Software in that Transaction Document. If Customer installs a
release of Software that Broadcom provides as part of Support services, then the then-current version of the SPD published
on legaldocs.broadcom.com on the date Customer installs that release applies to that release of Software.

LICENSE TO THIS SOFTWARE REQUIRES CUSTOMERS WHO INSTALL, DEPLOY OR USE VERSIONS 9 OR ABOVE
TO  PROVIDE  BROADCOM  WITH  A  REGULARLY-SCHEDULED  VERIFIED  REPORT  DETAILING  CUSTOMER’S
INSTALLED  BASE  AND  LICENSE  COMPLIANCE  FOR  THAT  VERSION  OF  SOFTWARE  USING  THE  FORMAT  AND
PROCESS  SPECIFIED  BY  BROADCOM  DESCRIBED  HEREIN  AS  WELL  AS
IN  THE  DOCUMENTATION
(“COMPLIANCE  REPORT”).  CUSTOMER’S  FAILURE  TO  TRANSMIT  OR  UPLOAD  A  TIMELY,  UNALTERED
COMPLIANCE REPORT WILL RESULT IN FEATURES AND FUNCTIONALITIES OF THE MANAGEMENT PLANE  OF
THE  SOFTWARE  TO  BE  DEGRADED  AND/OR  BLOCKED  IN  ADDITION  TO  SUPPORT  ENTITLEMENTS  FOR  THIS
SOFTWARE BEING SUSPENDED (INCLUDING ACCESS TO UPDATES OR UPGRADES) AS FURTHER DESCRIBED
HEREIN AS WELL AS IN THE DOCUMENTATION.

Program Name: VMware Cloud Foundation (VCF)

1.  DEFINITIONS.

All terms defined in the VMware Licensing Glossary published on https://docs.broadcom.com/doc/vmware-licensing-glossary
apply to this SPD unless specified herein

“BIOS” means the Basic Input Output System, a set of routines that boots the operating system and sets up the hardware of
the Processor.

“Certified Cloud Services” means Broadcom’s then current list of Cloud Services that are certified by Broadcom for the use
of Customers to port license entitlements to and deploy Software.

“Cloud Services”  means computing infrastructure (including compute, storage, networking, security, management etc.) that
a Customer does not own, and which a third party markets or makes available as a service to its customers (including as a
bundle of, or as integrated with, managed services). Notwithstanding the foregoing, Cloud Services excludes infrastructure
deployed on-premises (whether in Customer’s data center or a co-location facility) provided that the third party who markets
or makes available the said infrastructure does not have access to, and does not perform any services with respect to, the
Software (including managed services, installation, etc).

“Cluster”  is  a  software  grouping  of  Servers  running  vSphere  and/or  vSAN  for  the  purpose  of  resource  sharing.

“Core” means a single physical computational unit of the Processor.

“Instance” means a single installation of the Software on a physical server or Virtual Machine.

June 2026

VMware Cloud Foundation (VCF)

   Specific Program Documentation

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

Examples of DIPA applications include a financial institution Customer running an application on Software (that it developed
or procured) for its banking customers to use to obtain information about their bank accounts, a grocery chain Customer running
an application on Software (that it developed or procured) to operate its in-store point of sale machines, an airline running an
application  on  Software  that  it  developed  or  procured  to  operate  self  check-in  kiosks  in  airports,  and  a  software  company
Customer delivering their internally developed human resource software application that runs on Software in a cloud model to
third party customers.
Examples of applications that are not DIPA applications include a service provider Customer hosting a third party’s application
on Software for its customers, a Customer running any application on Software to deliver hosted services, and a cloud services
or infrastructure services (including when combining their own applications with Software) to third parties.

“Processor” means a single, physical chip that houses at least one Core that can execute computer programs.

“Server”  means  a  hardware  system capable  of  running  the  server  software.  A  hardware partition or  blade is considered a
separate hardware system.

“TiB” means a unit of physical storage capacity that is equal to 2^40 bytes.

“Virtual Machine” means a software container that can run its own operating system and execute applications like a physical
machine.

“VKS Add-ons” means open-source or third party software packages that Broadcom may make available to download from
time to time to run on, or integrate with, a vSphere Kubernetes Service (VKS) cluster.

“VMware vSphere Supervisor” means those components that support or form part of the features and capabilities for running
containerized applications in vSphere, including but not limited to the Supervisor, the vSphere Kubernetes Service, vSphere
Kubernetes releases (VKr), VKS Add-ons, VCF Plugins and associated CLI Plugins.

2.    USE RIGHTS AND LIMITATIONS.

●  License Metric. Software is subscription software licensed on a per Core license metric with a minimum licensing requirement

of 16 Cores per Processor.

●  Licensed Cores.  Each Core on the Server where Software is installed must be licensed, including Cores deactivated by the
BIOS. The required number of Core licenses equals the number of Cores on the Server, subject to the minimum of 16 Core
licenses per Processor. Customer may use Software on a Server with up to the number of Cores for which Customer has paid
the applicable license fees.

●  Software Components. All components and capabilities included in Software (e.g. vSphere, NSX, VCF Operations, etc.) may

only be utilized on, or for, the same physical Cores where the vSphere component in Software Core license is deployed.

June 2026

2

VMware Cloud Foundation (VCF)

   Specific Program Documentation

●  Recovery and Testing. Customer may perform recovery and/or testing activities in the aggregate for up to 15 days per year
using the embedded evaluation mode feature of the Software. For clarity, this section does not grant Customer any rights to use
additional Cores than the number of Cores for which Customer has paid the applicable license fees.

●  Component Specific Rights and Limitations.  The following table describes additional component/capability specific license

entitlement rights and limitations of VCF:

VCF
Component

#

Metric
Entitlement

Entitlement Details

1

vSphere

1 Core

VMware Tools is a suite of utilities and drivers that can be installed in a Guest Operating
System to enhance the performance and functionality of a Guest Operating System when
running in a Virtual Machine in conjunction with a vSphere hypervisor. Customer may not
use VMware Tools with any other hypervisor. Customer may distribute the VMware Tools
to  third  parties  solely  when  installed  in  a  Guest  Operating  System  within  a  Virtual
Machine.  Customer  is  liable  for  compliance  by  those  third  parties  with  the  terms  and
conditions of the Agreement.

2

vSAN

1 TiB

Customer is entitled to 1 TiB of vSAN capacity for each Core licensed for VCF. vSAN can
only be aggregated and utilized across Cores where the vSphere in VCF is deployed.

Customer  may  only  use  the  VCF  Operations,  VCF  Automation  and  VCF  Operations  for
Networks  capabilities  in  VCF  (“VCF  O/A  Capabilities”)  to  manage  Cores  licensed  for
Software  and  Cores  Customer  may  have  separately  licensed  for  another  Broadcom
software  called  VMware  Cloud  Foundation  Edge  ("VCFE")  only.  Customer  who  have
licenses to both Software and VCFE may only manage environments with a mixture of such,
Cores using VCF O/A and VCFE O/A (as defined in the SPD for VCFE) to the extent the
total  number  of  Cores  managed  by  VCF  O/A  and  VCFE  O/A  does  not  exceed  the  total
number of VCF and VCFE Cores Customer has licensed.

3

VCF Operations
VCF Automation
VCF Operations
for Networks

1 Core

4

vCenter Server

1 Instance

5

6

vSphere
Kubernetes
Service (VKS)

1 Core

VCF Private AI
Services (if
applicable)

1 Core

●  Notwithstanding  the  foregoing,  Customer  is  entitled  to  use  any  VCF  O/A
Capabilities,  then-currently  supported  by  Software,  to  manage  the  use  of
equivalent number of Cores, as the number of Cores licensed for VCF on-prem,
for  use  on  the  license-integrated  versions  (where  provider  is  licensee) of  Azure
VMware  Solution,  Google  Cloud  VMware  Engine,  and/or  Oracle  Cloud  VMware
Solution (“MaaS Offerings”) at no additional cost until the earlier of the expiration
or termination of the subscription term or the date that the MaaS Offering adopts
solution.
part
VCF  O/A

Capabilities

integrated

as

its

of

●  Specific  to  VMware  Cloud  on  AWS,  Customer  is  entitled  to  use  only  the  VCF
Operations  Logs  Capabilities,  then-currently  supported  by  Software,  for  logs
generated by VMware Cloud on AWS at no additional cost until the earlier of the
expiration or termination of the subscription term or the date that VMware Cloud
on AWS adopts VCF Operations Logs Capabilities as part of its integrated solution.
The  quantity  of  VMware  Cloud  on  AWS  cores  that  use  VCF  Operations  Logs
Capabilities in VCF cannot exceed the VCF cores purchased.

The vCenter Server component of the deployed version of Software may only be used to
provide centralized management capabilities to vSphere component licenses that have an
entitlement to upgrade to that deployed version of Software (irrespective of the technically
supported version that the Customer may be running).

●  Software includes support for certain VKS Add-ons, and the scope and applicability
of such support depends on which of the then-current tiers the VKS Add-on has
been designated. Please refer to the Documentation for more details.

●  VKS components have a shorter support life cycle period compared to the lifecycle

period generally applicable to the Software.

License to Software only includes entitlement to VCF Private AI Services as a component
of  Software  to  the  extent  the specific  SKU  indicated  in  the Transaction  Document of the
Customer’s Order is one that, at the time of purchase, includes entitlement to VCF Private
AI Services as a component of Software. In such cases that Customer has an entitlement
to Software that includes VCF Private AI Services component, Customer is entitled to use
Data Services Manager (DSM) control plane to deploy and manage PostgreSQL database
with VCF Private AI Services only, and not for any other feature of DSM or for any other

June 2026

3

VMware Cloud Foundation (VCF)

VCF
Component

#

Metric
Entitlement

   Specific Program Documentation

purpose.

Entitlement Details

●  Legacy Perpetual License Upgrade Restrictions. Customers with perpetual licenses to legacy VMware software that also used
the name VCF when it was offered and who have active subscription to Support and Subscription Services (“Legacy Perpetual
Software”) are entitled to upgrade to Software version 5.x until the earlier of their Support and Subscription Services end date or
the end of support of version 5.x. For clarity, Customers do not have an entitlement to upgrade Legacy Perpetual Software to any
version of Software above 5.x.

●  Legacy Per Core Upgrade Restrictions. Licenses to Software obtained as a result of upgrading from a per Core legacy VMware
subscription offering  (including  VCF+/-S  (all editions) and VCF  Cloud  Packs+/-S  (Advanced  and  Enterprise  edition)), wherein
such  legacy  offerings  were  purchased  prior  to  February  4,  2024,  (“Qualified  Legacy  Offerings”)  are  entitled  to  the  existing
features and capabilities that came in the Qualified Legacy Offerings prior to its upgrade to VCF, except for the Enterprise edition,
and subject to the following additional restrictions: Such Customers with Qualified Legacy Offerings are entitled to use vSAN
either

i) on the original metric (per Core) or,
ii) 1 TiB for each Core license to use for vSAN storage clusters

until the earlier of the expiration of their VCF subscription or their upgrade to version 9 or later.

●  Export restrictions and restrictions on use of NSX Software. VMware NSX Software is of United States Origin and contains
some features (including features which support network infrastructure) which result in the application of stricter export control
classifications  pursuant  to  the  United  States  Export  Administration  Regulations  (EAR).  For  some  uses  of  the  VMware  NSX
Software, such as for use by “More Sensitive” Government End Users as defined in Part 772 of the EAR, there may be restrictions
or prohibitions applicable to Customer’s proposed use of the Software if that use is in or for certain Group D:1 countries (which
include  China  or  Russia)  where  VMware’s  Bulk  Export  License  may  not  be  used.  Customer  is  responsible  for  ensuring  that
Customer’s proposed use of the VMware NSX Software is not in violation of applicable United States or local law.

●  License Portability. Customer must not use or deploy (“Port”) the Software on any Cloud Services that are not found on the
then-current  list  of  Certified  Cloud  Services  (a  copy  of  which  is  found  here:  https://www.vmware.com/docs/vmware-cloud-
foundation-license-portability-list-of-certified-cloud-providers). In such cases, Customer must Port the entire set of components
of the Software to that Certified Cloud Service, and continues to be the licensee. Customer shall provide ongoing representations
reasonably requested by the provider of that Certified Cloud Services around the validity of licenses Ported. In the event that
Customer Ports to a Cloud Service that was on the list of Certified Cloud Services at the time Customer Ported but was later
removed, then that Cloud Service shall be deemed to continue to be on the list of Certified Cloud Services only with respect to
those licenses that had already been Ported and only until the expiration of those licenses’ then-current subscription periods.

The  right  to  Port  hereunder  does  not  apply  to  i)  licenses  obtained  through  a  third  party  who  resold  those  licenses  under
Broadcom's Value-Added OEM Program (for clarity, such licenses may only be used on infrastructure that the license was sold
with, ii) licenses obtained through an upgrade under Qualified Legacy Offerings that are not Enterprise edition, or iii) Software
licensed to a partner under the Cloud Service Provider Program or Metal-as-a-Service Program.

●

iSCSI Support. Customer may only use the iSCSI Support feature in vSAN with physical, non-virtualized Servers. The iSCSI
Support feature supports Microsoft clustering with shared disks. Initiators can be either from virtual machines or physical servers.
For guest initiators in virtual machines, those virtual machines can be residing on:

- The same vSAN Cluster that provides this iSCSI Support feature; or
- An external vSAN or vSphere Cluster.

The iSCSI Support is limited to a maximum of 128 sessions per Server, a maximum of 128 targets per Cluster, and a maximum
of 1024 logical unit numbers (LUNs) per cluster. Raw device mapping (RDMs) for Microsoft Windows Server Failover Clustering
(WSFC) using iSCSI target service is not officially supported on vSAN.

●  Underlying  Hardware.  Customer may only  use  Software on  hardware  that meets the  then-current  applicable  Broadcom
requirements  for  such  hardware  in  the  Documentation,  the  Broadcom  Software  Maintenance  Policy  Handbook,  and  the
Broadcom Compatibility Guide found here: https://compatibilityguide.broadcom.com.

●  Hosting Rights and Restrictions. Customer may use the Software to deliver its Deemed Internal Purpose Application(s) to a
third party via an internal or external network. Except as expressly provided in this paragraph, the use of the Software for  any
other types of hosting or for the benefit of any third party in any manner is strictly prohibited.

June 2026

4

VMware Cloud Foundation (VCF)

   Specific Program Documentation

●  Support Services. License to Software includes entitlement to support and maintenance services that may only be used for
Software licensed herein, and may not be used for any other software, including former offers of components of Software
that Customer may have licensed separately.

●  Benchmarking. Customer may use Software to conduct internal performance testing and benchmarking studies. Customer may
only  disclose,  publish  or  distribute  the  results  of  the  studies  to  third  parties  if  Broadcom  has  reviewed  and  approved  of  the
methodology, assumptions, and other parameters of the study prior to publication and distribution. Customer must submit such
requests to vmware-benchmark.pdl@broadcom.com.

●  Compliance Reporting for Software Versions.

●  Mandatory  Compliance  Reporting.  Customer  who  install,  use  or  deploy  Software  must  provide  Broadcom  with  a
Compliance Report (as defined above) for that version of Software 180 days from the date that the license is registered
and  every  180  days  thereafter  by  ensuring  that  the  Compliance  Report  files  generated  by  the  Software  are  either
transmitted by the Software or uploaded by Customer in accordance with the product Documentation.

●  Failure to Report. Customer’s failure to transmit or upload a timely, unaltered Compliance Report, in accordance with
the Documentation will result in features and functionalities of the management plane of the Software to be degraded
and/or blocked in addition to support entitlements for this Software being suspended (including access to Updates or
Upgrades).

●  Assumption of Risk of Failure to Report. Customer assumes any and all risks associated with the loss of any and all
functionality and patch access when caused by Customer’s failure to provide timely, unaltered Compliance Reports.

3.

THIRD PARTY INFORMATION AND TERMS.

●  Any required third-party software license terms are incorporated by this reference and are set forth in online documentation

at techdocs.broadcom.com or legaldocs.broadcom.com.

June 2026

5

