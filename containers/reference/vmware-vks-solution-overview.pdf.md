Solution Overview

VKS is the CNCF-certified
Kubernetes runtime built directly
into VCF, to run all apps. VKS is
among the first platforms certified
under the new CNCF Kubernetes
AI Conformance Program. VKS
enables platform engineers
to easily deploy, manage and
scale Kubernetes clusters while
leveraging a comprehensive set of
cloud services included in VCF, as
well as all CNCF-conformant third-
party services.

VMware vSphere
Kubernetes Service
Accelerate Modern App deployment at
scale with tighter security and lower TCO

Organizations seek a consistent, secure, and efficient way to run modern
containerized applications as well as traditional applications that use virtual
machines. With the industry experiencing a shift toward cloud-native
technologies, Kubernetes is playing a pivotal role in this transition. According
to the latest State of Platform Engineering Report1, 64% of platform engineers
identify Kubernetes as a primary focus area for achieving automated, reliable,
and standardized application deployment.

VMware Cloud Foundation (VCF) delivers exactly what they look for: a unified
platform that integrates compute, storage, networking, and security with
built-in automation and lifecycle management. VCF helps organizations
eliminate silos, reduce TCO, streamline management, and accelerate their
modernization journey.

Organizations looking to modernize their workloads are often faced with a few
key challenges:

1. Infrastructure Silos and Multiple Operating Models

Many organizations have fragmented and disconnected infrastructure
environments driven by rapid business growth, shifting organizational needs,
mergers, and acquisitions. Kubernetes often compounds this complexity when
compute, storage, and networking are managed in separate silos, creating
inconsistent operations and significant management friction.

2. Disparate Components Slowing Time to Market

While Kubernetes is incredibly powerful and a standard for modern
infrastructure, it is also inherently complex. Kubernetes requires integration
with dozens of separate tools to achieve enterprise-grade security,
compliance, lifecycle management, and consistent operations at scale.
Enterprises are responsible for integrating and operating a complex
ecosystem securely and consistently. This is where many enterprises struggle,
leading to increased operational overhead, risk, and slower time to value.

3. Skill Gaps in Modern IT

While Kubernetes is now the backbone of modern IT, the steep learning curve
often leaves organizations struggling to upskill their teams. This expertise gap
can trigger a cascade of issues ranging from longer deployment cycles to poor
performance with heightened operational risk.

1.  State of Platform Engineering: Report 4, December 2025:

https://platformengineering.org/reports/state-of-platform-engineering-volume-4

1

SOLUTION OVERVIEWVMware vSphere Kubernetes Service

 “According to the report from
IDC 85% of containers are

projected to run within VMs

by 2028, driven by increasing

demands for security and
scalability2.

4. Outdated Infrastructure Services

Traditional IT infrastructure often acts as a bottleneck for platform teams,
lacking the speed, agility, and automation required for rapid iteration.
Consequently, platform engineers operating in Kubernetes environments are
frequently constrained by rigid infrastructure that stifles the velocity of
application deployment.

5. Security and Compliance

Organizations are increasingly caught between the need for rapid deployment
and the stringent requirements of Security and Compliance. As infrastructure
scales, managing sensitive credentials across fragmented environments
becomes a major liability, often leading to a broadened attack surface and
unauthorized access risks. Furthermore, navigating global regulatory
frameworks with a patchwork of manual processes becomes challenging to
sustain, leaving the organization vulnerable to both sophisticated cyberattacks
and costly regulatory penalties.

Solution Description
VMware vSphere Kubernetes Service (VKS) is the CNCF-certified Kubernetes
runtime built directly into VCF, to run all apps. VKS is among the first
platforms certified under the new CNCF Kubernetes AI Conformance
Program. VKS enables platform engineers to easily deploy, manage, and
scale Kubernetes clusters while leveraging a comprehensive set of cloud
services included in VCF, as well as all CNCF-conformant third-party services.

Cloud admins benefit from policies, governance and control, flexibility of
upgrades, enterprise grade security, and simplified lifecycle management for
easier modern apps adoption.

Figure 1: VMware Cloud Foundation

2.  IDC Whitepaper on convergence of Containers and VMs in Modern IT Infrastructure: https://www.

vmware.com/docs/vmw-idc-containers-vms-modern-it-infrastructure-white-paper

Solution Overview | 2

VMware vSphere Kubernetes Service

Loomis, a global leader in cash-
handling products and services:

 “We are moving more and more

workloads on Kubernetes

environments. It’s like a

revolution where we migrate

legacy solutions to a modern

platform.”

Jean-Michel Blanc,
Ground Head of System Engineering,
Loomis

The Modern Cloud Interface facilitates the operation of services such as
orchestration, applications, and service catalogs through an automated
system. This means a more streamlined operational experience for both cloud
admins and platform engineers.

Cloud admins can establish policies with the governance and controls they
need. These policies enable platform engineers with self-service access to
deploy and manage both virtual machines and Kubernetes clusters

Platform engineers can also define their virtual machine configuration in a
manifest and deploy it using the same API patterns as they would use to
deploy Kubernetes clusters.

Figure 2: VKS offers comprehensive set of cloud services along with all conformant third-
party services

Cloud admins can extend the service offering with a set of comprehensive
cloud services required by Platform engineers to deploy their workloads. Let’s
explore the key features that establish VKS as the preferred Kubernetes
service for modern workloads running on VCF, the industry-leading private
cloud platform for all enterprise applications:

• Unified API to provision and manage both VMs and containers: A

consistent API that allows users to create, deploy, and manage both VMs
and Kubernetes clusters. This simplifies automation, reduces integration
challenges, and ensures uniform policies and security controls across all
workloads. With a unified API, VCF allows platform engineers to interact
with infrastructure resources in a consistent manner, eliminates the need for
separate tooling, and lowers training costs.

• Self-service access to cloud services with governance: Through a role-

based access model, Platform engineers can leverage self-service
capabilities to provision infrastructure resources and rich cloud services,
such as VM Service, Network Services, and Image Registry, on demand,
while cloud admins maintain governance and control through policies and
resource quotas. Self-service access also supports multi-tenancy with
isolated environments for different teams and projects.

Solution Overview | 3

VMware vSphere Kubernetes Service

 “We have to modernize our data
center infrastructure. VMware

Cloud Foundation allows us

to build a flexible and scalable

private cloud infrastructure

that helps with our operational

needs. And it complies with

regulatory standards.”

Christian Böke,
Project Management Lead,
Ratiodata

• Multi-modal access with declarative API, CLI, and Ul: VCF offers cloud

admins and platform engineers with a range of flexible interfaces that align
with their preferred choice for workflows. VCF provides a consistent
operational experience and standardized way to manage resources whether
it’s Graphical User Interface (GUI) for visual management, the powerful
Command Line Interface (CLI) for scripting and automation, or the robust
APIs for integration with external tools and CI/CD pipelines. By leveraging
existing expertise, teams maintain high productivity and operational
efficiency without the friction of learning entirely new toolsets.

• Operational agility with Multiple Clusters per Zone and Custom Zones:
With VCF multiple clusters can be deployed in each zone enabling cloud
admins to replace, retire, or upgrade hardware without impacting
application availability or disrupting the desired state. VCF also brings
intelligent node pool placement defaults to accelerate deployment cycles
while eliminating the risk of placement failures and the operational burden of
debugging complex configuration errors. VCF also supports independent
workload zones, enabling cloud admins to align resources with application
needs. Supporting both single and multi-zone configurations, this flexibility
simplifies high availability and disaster recovery. By creating specialized
zones, such as dedicated GPU clusters for AI, organizations can achieve
granular control, optimized utilization, and the agility to support diverse,
high-performance deployments at scale.

• Efficient Cluster scaling: VKS can scale to support 500 clusters in a single

control plane, ensuring seamless expansion within the management domain.
Organizations can achieve better isolation, a reduced blast radius, and
customized cluster configurations offering greater flexiblity for large-scale
Kubernetes deployments. VKS supports autoscaling, automatically adjusting
the number of service instances based on real-time resource metrics like
CPU and memory usage. VKS clusters deploy rapidly in minutes and scale
dynamically from zero to peak capacity, and back to zero when idle,
maximizing resource efficiency, accelerating deployments, and slashing
infrastructure costs.

• Multi-Cluster management at scale: With VKS multi-cluster management
platform engineers get visibility and control over the entire cluster fleet
without sacrificing the simplicity and operational consistency required at
scale. VKS multi-cluster management provides industry leading capabilities
including RBAC and policy management, cluster inspections, data
protection, package management, and continuous delivery. Leveraging VCF
Automation, organizations can automate the manual toil using fleet-wide
multi-cluster management with visibility into cluster health, utilization, and
Kubernetes version details. Organizations can enforce consistent security
and compliance policies implemented using Open Policy Agent (OPA)
Gatekeeper. VKS ensures resilience with integrated data protection to easily
backup and restore clusters, namespaces, and groups of resources. Add-on
management simplifies lifecycle tasks for core and user-managed packages.

• Distributed application security with Istio service mesh: While the shift to

microservices has enabled greater architectural flexibility, it has also
introduced significant operational complexity. Specifically, managing secure
and reliable connectivity between these distributed components has become
a primary challenge Istio Service Mesh provides traffic management,
security, and observability features, making it easier to deploy, manage, and
secure microservices at scale. Istio Service Mesh is integrated with VCF to
simplify service-to-service communication in modern applications. This

Solution Overview | 4

VMware vSphere Kubernetes Service

integration simplifies Kubernetes operations with visibility, governance, and
control, and enhances end-to-end security and observability for distributed
applications.

• Broadcom-built ArgoCD Operator: Purposefully designed for VCF, the

ArgoCD operator seamlessly integrates GitOps workflows into the platform.
This enables platform teams to manage Kubernetes clusters, virtual
machines, and vSphere Pods through a single, version-controlled, and
declarative deployment model. Once deployed by cloud admins, platform
engineers can provision self-service ArgoCD instances scoped to specific
vSphere Namespaces. This ensures that while engineers have the autonomy
they need, the lifecycle, access control, and resource governance remain
centrally managed. By leveraging Git as the single source of truth, the
ArgoCD operator enables unified, auditable, and consistent delivery across
both traditional and cloud-native workloads.

• Robust security and resiliency: VCF provides built-in fault tolerance, high

availability, and six levels of workload isolation from data center to the
application namespace, ensuring that the infrastructure remains secure,
resilient, and compliant. VKS takes advantage of enterprise-grade security in
VCF with features like end-to-end encryption (at rest and in transit), role-
based access control, integrated security dashboards, and distributed
firewalls. VCF delivers a consistent and streamlined secret injection workflow
that helps strengthen security, improves auditability, and ensures secrets are
managed consistently across all workloads. VKS supports encryption classes
for workload clusters and granular policies to access secrets offering better
control of encryption keys and meeting internal and external regulatory
encryption requirements. With VKS organizations achieve better security
hardening with declarative orchestration for AppArmor by establishing
uniform security baseline and preventing both known and unknown
application flaws from being exploited at the operating system level. Option
to enable FIPS mode at the OS level further strengthens security by ensuring
only FIPS-approved cryptographic modules are used within the operating
system.

Key Benefits
VCF enables platform teams to leverage self-service experience with VKS and
deploy modern workloads with the following benefits:

• Unified platform for managing VMs and Containers: VCF enables unified
management of traditional and modern workloads through consistent API,
simplifying operations, and reducing the need for separate platforms. This
helps organizations leverage their skillset to deploy all workloads without
fragmenting the IT teams. With centralized policy management, consistent
lifecycle, and infrastructure abstraction organizations achieve a seamless
operational experience across traditional and modern workloads.

• Simplified Kubernetes operations using existing skillset: VCF provides a
robust set of consistent APIs across all building-block services including AI
to create, deploy, and manage both VMs and Kubernetes clusters. This
simplifies automation, reduces integration challenges, and ensures uniform
policies and security controls across all workloads. Platform engineers
interact with compute resources in a consistent manner, eliminating the
need for separate tooling, lowers training costs, and addressing skillset
gaps.

Solution Overview | 5

VMware vSphere Kubernetes Service

• Multi-Cluster lifecycle management, policy, and backup at scale: Using

VCF Automation platform engineers get visibility and control over the entire
cluster fleets without sacrificing the simplicity and operational consistency
required at scale. Platform engineers can automate lifecycle management of
VKS packages, enforce security and compliance policies, and eliminate
configuration drift.

• CNCF certified Kubernetes runtime: VKS empowers organizations to
capitalize on the latest open-source innovations by deploying a CNCF-
certified Kubernetes distribution. This ensures full compatibility with the
broader cloud-native ecosystem, providing upstream concurrency that
prevents vendor lock-in. Platform engineers can run all modern applications
on VKS and easily migrate existing workloads on other certified Kubernetes
environments. The latest VKS 3.6 release adds support for VKr version 1.35.

• CNCF certified Kubernetes AI Conformant platform: VKS is among the first

platforms certified under the new CNCF Kubernetes AI Conformance
Program. VKS provides a standardized way to validate behavior of AI and
machine learning workloads including accelerator usage, scheduling
patterns, and reproducibility. Platform teams can offer a consistent and
standardized AI platform that supports innovation, portability, and
performance while adhering to the governance, privacy, and sovereignty
constraints. Data Scientists can move faster from development to
production.

• Multiple Kubernetes versions supported for upgrade flexibility: VKS

ensures compatibility across three Kubernetes versions at any given time
that allows different enterprise teams to run the version their apps need and
have the control and flexibility to upgrade at their own pace. VKS supports
three  vSphere Kubernetes release (Vkr) versions.

• LTS for Kubernetes minor releases: Stable deployments with 24 months
support for every vSphere Kubernetes release minor version, including
patches for quantified critical security vulnerabilities. With long term support
enterprises can plan upgrades aligned with business priorities.

• Seamless CI/CD pipeline and tooling alignment: VCF and VKS align with an

organization’s Continuous Delivery (CD) pipeline integrating with the
broader ecosystem of platform engineering tools like ArgoCD, Harbor, and
Helm among others. Ecosystem collaboration with partners in networking,
security, and API management further reduces the need for costly
re-tooling. Broader autonomy for platform engineers with choice of OS and
CNI add-ons.

• Security and Compliance: Organizations can run sensitive and regulated
workloads on a secure, compliant platform that meets data residency and
data sovereignty requirements. VKS simplifies the deployment of
Kubernetes clusters, providing enhanced security for application data in
isolated regions with flexible security postures at the cluster level. VKS
leverages the six layers of fault and threat isolation to enhance security and
significantly reduces the attack surface.

• Lower Total Cost of Ownership: By enabling higher VM density per host,
advanced memory management, and disaggregated vSAN storage with
features like deduplication and compression, VCF drives better resource
utilization and infrastructure efficiency. Organizations also reduce costs by
lowering licensing fees and maximizing the value of existing hardware.

Solution Overview | 6

VMware vSphere Kubernetes Service

Ready to take the next step?

Explore VMware Cloud Foundation
resources, hands-on labs, and
technical guides to start your
journey today:

• Learn more about VKS at vSphere
Kubernetes Service website and
VCF Blog page

• Explore the Forrester webinar and

blog

• Check out the VKS Infographic

• Access to technical resources at

VCF Resource Center

• Follow us on VCF social media: X,

LinkedIn, and YouTube

Conclusion
VMware Cloud Foundation is a single platform with built-in Kubernetes
runtime that enables enterprises to run modern applications alongside virtual
machines. It simplifies deployment, integrates infrastructure components,
automates lifecycle management, and ensures security and scalability. As a
result, VMware Cloud Foundation reduces TCO and complexity while
delivering high performance with consistency.

Copyright © 2026 Broadcom. All rights reserved.
The term “Broadcom” refers to Broadcom Inc. and/or its subsidiaries. For more information, go to www.broadcom.com. All trademarks, trade names, service marks, and logos
referenced herein belong to their respective companies. Broadcom reserves the right to make changes without further notice to any products or data herein to improve reliability,
function, or design. Information furnished by Broadcom is believed to be accurate and reliable. However, Broadcom does not assume any liability arising out of the application or
use of this information, nor the application or use of any product or circuit described herein, neither does it convey any license under its patent rights nor the rights of others.
Item No: VKS Solution Brief with VCF 9.1 updates 4/26

