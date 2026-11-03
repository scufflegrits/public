Red Hat Satellite 6.19

Release notes

New features, deprecated and removed features, Technology Previews, known
issues, and bug fixes

Last Updated: 2026-09-11

Red Hat Satellite 6.19 Release notes

New features, deprecated and removed features, Technology Previews, known issues, and bug fixes

Red Hat Satellite Documentation Team
satellite-doc-list@redhat.com

Legal Notice

Copyright © Red Hat.

Except as otherwise noted below, the text of and illustrations in this documentation are licensed by
Red Hat under the Creative Commons Attribution–Share Alike 3.0 Unported license . If you
distribute this document or an adaptation of it, you must provide the URL for the original version.

Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert,
Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.

Red Hat, the Red Hat logo, JBoss, Hibernate, and RHCE are trademarks or registered trademarks of
Red Hat, LLC. or its subsidiaries in the United States and other countries.

Linux ® is the registered trademark of Linus Torvalds in the United States and other countries.

XFS is a trademark or registered trademark of Hewlett Packard Enterprise Development LP or its
subsidiaries in the United States and other countries.

The OpenStack ® Word Mark and OpenStack logo are trademarks or registered trademarks of the
Linux Foundation, used under license.

All other trademarks are the property of their respective owners.

Abstract

This document contains the release notes for Red Hat Satellite.

Table of Contents

Table of Contents

CHAPTER 1. OVERVIEW
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

4

1.1. ADVISORIES

1.2. MAJOR CHANGES IN RED HAT SATELLITE 6.19
1.3. RED HAT SATELLITE

1.4. ADDITIONAL RESOURCES

4

4
4

4

CHAPTER 2. NEW FEATURES AND ENHANCEMENTS
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

2.1. HOST PROVISIONING AND MANAGEMENT

2.2. RED HAT LIGHTSPEED

2.3. MODEL CONTEXT PROTOCOL
2.4. WEB UI

2.5. INSTALLATION AND UPGRADE
2.6. CONTENT MANAGEMENT

2.7. DOCUMENTATION

7.1. INSTALLATION AND UPGRADE
7.2. SECURITY AND AUTHENTICATION
7.3. CONTENT MANAGEMENT

7.4. HOST PROVISIONING AND MANAGEMENT
7.5. USERS AND ROLES
7.6. RED HAT LIGHTSPEED

8.1. SATELLITE-INSTALLER PARAMETERS
8.2. HAMMER CLI
8.3. REST API

8.4. ANSIBLE MODULES
8.5. COLLECTED USAGE METRICS

CHAPTER 3. TECHNOLOGY PREVIEW FEATURES
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

10

3.1. MODEL CONTEXT PROTOCOL
3.2. HOST PROVISIONING AND MANAGEMENT

10
10

CHAPTER 4. DEPRECATED FEATURES
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

11

CHAPTER 5. REMOVED FEATURES
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

14

5.1. SERVER ADMINISTRATION
5.2. HOST PROVISIONING AND MANAGEMENT
5.3. USERS AND ROLES

14
14
15

CHAPTER 6. KNOWN ISSUES
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

16

6.1. WEB UI

6.2. INSTALLATION AND UPGRADE

6.3. RED HAT LIGHTSPEED
6.4. SECURITY AND AUTHENTICATION
6.5. CONTENT MANAGEMENT

6.6. HOST PROVISIONING AND MANAGEMENT

6.7. BACKUP AND RESTORE

6.8. IPV6

16

16

16
17
18

19

19

20

CHAPTER 7. FIXED ISSUES
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

CHAPTER 8. CHANGES IN SATELLITE-INSTALLER PARAMETERS, HAMMER CLI, REST API, AND USAGE
METRICS
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

APPENDIX A. PROVIDING FEEDBACK ON RED HAT DOCUMENTATION
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

30

1

6
6

6

7
7

8
8

9

22
22
22
22

23
24
24

26
26
26
28

29
29

Red Hat Satellite 6.19 Release notes

APPENDIX B. REVISION HISTORY
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

31

APPENDIX C. LIST OF TICKETS BY COMPONENT
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

32

2

Table of Contents

3

Red Hat Satellite 6.19 Release notes

CHAPTER 1. OVERVIEW

Release notes include links to the original tickets. Private tickets have no links and instead feature the
following footnote[1].

1.1. ADVISORIES

You can view all advisories, including security and bug fixes, for major and minor versions of this release
on the Red Hat Customer Portal.

1.2. MAJOR CHANGES IN RED HAT SATELLITE 6.19

Red Hat Satellite 6.19 introduces the following major changes:

Red Hat Lightspeed vulnerability service in Satellite (previously a Technology Preview feature)
is fully supported. Additionally, the feature receives enhancements, such as improved role-
based access control and control over vulnerability analysis on hosts (Section 2.2, “Red Hat
Lightspeed”).

Satellite provides Puppet functionality through OpenVox packages (SAT-31648).

Transient packages on image mode hosts are now tracked (SAT-30671, SAT-36790).

SSH certificates are supported for remote execution (SAT-28038).

Multiple content view (CV) environments in hosts and activation keys (previously a Technology
Preview feature) are fully supported. Additionally, support for multiple CV environments in
hosts and activation keys in the Web UI is enhanced (SAT-26055).

Satellite MCP server (Technology Preview) can be granted write permissions, with which it can
incrementally update, publish, and promote content views (SAT-40970).

The OpenShift Virtualization plugin (Technology Preview) benefits from improved stability and
usability (SAT-41368).

For a complete list of changes in this release, see the following sections.

1.3. RED HAT SATELLITE

With Red Hat Satellite, you can deploy, configure, and maintain your systems across physical, virtual, and
cloud environments. Red Hat Satellite provides provisioning, remote management and monitoring of
multiple Red Hat Enterprise Linux deployments with a single, centralized tool.

Red Hat Satellite Server  synchronizes content from the Red Hat Customer Portal and other
sources. It provides detailed lifecycle management, user and group role-based access control,
integrated subscription management, and advanced GUI, CLI, and API access.

Red Hat Satellite Capsule Server  mirrors content from the Red Hat Satellite Server and
distributes it to different geographical locations. Host systems pull content and configurations
from the Capsule Server in their location instead of the central Satellite Server. The Capsule
Server also provides localized services such as Puppet server, DHCP, DNS, or TFTP, assisting in
scaling Red Hat Satellite as the number of managed systems in your environment grows.

1.4. ADDITIONAL RESOURCES

4

CHAPTER 1. OVERVIEW

Red Hat Satellite product life cycle  describes the time period for each major version and its level
of maintenance.

Satellite 6 component versions  describes upstream core components, Foreman plugins, and
integrated projects.

Overview, concepts, and deployment considerations  describes Red Hat Satellite concepts,
components, tools, and deployment planning.

Supported usage and versions of Satellite components  in  Overview, concepts, and deployment
considerations describes supported client architectures for content management, host
provisioning, and configuration management.

[1] This ticket does not have a link because it is private.

5

Red Hat Satellite 6.19 Release notes

CHAPTER 2. NEW FEATURES AND ENHANCEMENTS

Discover new capabilities and improvements introduced in Red Hat Satellite 6.19.

2.1. HOST PROVISIONING AND MANAGEMENT

Job templates can be cloned with Hammer CLI

With this update, you can clone job templates on the command line by using the new hammer job-
template clone sub-command. This is a CLI equivalent to the  POST /api/job_templates/:id/clone
API call. This enhancement streamlines workflows and aligns CLI capabilities with API functionality.
Jira:SAT-34616

Cloned templates track the original template ID

This update stores the original template reference in the new cloned_from metadata field. The
source template is also displayed in the Web UI and as output from the hammer template info --id
My_host_id, hammer report-template info --id My_host_id, and hammer job-template info --id
My_host_id commands. This enhancement improves template management and traceability.
Jira:SAT-18489

SSH certificates are supported for remote execution

You can configure your Capsules to use SSH certificates signed by your trusted certificate authority
(CA) during a remote execution connection. By enabling this feature, you can avoid the default Trust
on First Use (TOFU) model, and benefit from centralized trust management and revocation
capabilities. For more information, see Configuring Capsule and hosts to authenticate with SSH
certificates during remote execution in  Managing hosts.
Jira:SAT-28038

VMs with Libvirt compute resource can be provisioned on RHEL 10 hypervisors

With this update, you can create and provision virtual machines by using the Libvirt compute
resource on Red Hat Enterprise Linux 10 hypervisors.
Jira:SAT-40266

Port 80 is not required for global registration

With this update, host registration uses HTTPS for the /unattended/built endpoint. This means that
registration no longer requires port 80 and it is not possible to use port 80 during host registration.
Jira:SAT-41516

Reports and Host - Details can include hardware and cloud billing facts

With this update, you can incorporate cloud billing facts for AWS, Microsoft Azure, and Google Cloud,
and the hardware model into the Host - Installed Products report template and  Host - Details
pages. As a result, you can segment your systems based on billing sources and hardware.
Jira:SAT-39060

2.2. RED HAT LIGHTSPEED

Enhanced role-based access control for Red Hat Lightspeed in Satellite

The following new user permissions are available to control user access to RHEL hosts

6

CHAPTER 2. NEW FEATURES AND ENHANCEMENTS

The following new user permissions are available to control user access to RHEL hosts
Recommendations and Common Vulnerabilities and Exposures (CVE) data:

edit_advisor

view_advisor

edit_vulnerability

view_vulnerability

Additionally, this update adds the ForemanRhCloud Read Only built-in role, which includes the new
viewing permissions. The ForemanRHCloud built-in role now includes the new viewing and editing
permissions.

For more information, see Monitoring hosts by using Red Hat Lightspeed in Satellite  in  Managing
hosts.

Jira:SAT-40466[1]

Enhanced control over vulnerability analysis on hosts

With this update, you can disable vulnerability analysis on selected hosts, controlling which hosts are
included in vulnerability reporting. This functionality is available from the All Hosts page and Host
Details page.
For more information, see Disabling vulnerability analysis on hosts  in  Managing hosts.

Jira:SAT-40203

2.3. MODEL CONTEXT PROTOCOL

Patch hosts and incrementally update, publish, and promote content views by using MCP

With this update, you can patch hosts registered with your Satellite by using natural language
instructions through the Model Context Protocol (MCP). You can use your AI application connected
to the MCP server for Satellite to apply errata to hosts, incrementally update, publish, and promote
actions on content views. This improvement streamlines patch management, minimizing the
requirement for manual work and multiple steps.
For more information, see the following updated documentation:

Installing errata on hosts by using MCP .

Adding errata to an incremental content view by using MCP .

Publishing and promoting a content view by using MCP .

Jira:SAT-40970[1]

2.4. WEB UI

Compact table mode available in Satellite web UI to reduce table padding

With this update, the Compact table mode setting is available for viewing tables in Satellite web UI.

7

Red Hat Satellite 6.19 Release notes

With this update, the Compact table mode setting is available for viewing tables in Satellite web UI.
With Compact table mode enabled, Satellite web UI shows table rows with less space between
items. As a result, you can view more data on the screen at once.
To enable Compact table mode in the Satellite web UI, click the user menu in the top bar and select
My Account. Under the UI Preferences tab, select  Compact table mode.

Jira:SAT-32173

Container Image Tags page is redesigned

The Container Image Tags page in the Satellite web UI is enhanced for improved usability and easier
navigation when managing and viewing container content in Satellite. The enhancements include
displaying more details about container content and improved filtering. As a result, the redesigned
page provides a single location to view all information related to container image tags and their
associated metadata in Satellite.
To view the page, navigate to Content > Content types > Container image tags.

Jira:SAT-23851

All Hosts page improvements

This update adjusts the All Hosts page for easier management of host collections and system
purpose. Among other improvements, you can more efficiently make changes for multiple hosts.
Jira:SAT-35463

2.5. INSTALLATION AND UPGRADE

Leapp host upgrades support target version selection

When upgrading hosts to the next major Red Hat Enterprise Linux release, you can now specify a
particular target version for Leapp pre-upgrade checks and upgrades. This enhancement provides
more control and flexibility in host upgrades. For more information, see Upgrading hosts to next
major Enterprise Linux release.
Jira:SAT-38080

2.6. CONTENT MANAGEMENT

Satellite transitions to OpenVox 8

Satellite is transitioning to OpenVox 8 packages for Puppet management for Satellite Server,
Capsule Server, and clients. The implementation of OpenVox reduces operational risk and ensures
security continuity. To install these packages on the clients, enable the Red Hat Satellite Client 6
OpenVox repository for the Red Hat Enterprise Linux version your clients use. For more information,
see Upgrade Puppet agent 7 to OpenVox agent 8  in  Upgrading connected Red Hat Satellite to 6.19
and OpenVox versions supported for integration with Satellite  in  Managing configurations by using
Puppet integration.
Jira:SAT-31648[1]

Making transient packages on image mode hosts persistent

If you use Satellite to manage image mode hosts with transient packages, you can generate a new
Containerfile install command to persist transient packages in your container image. By placing the
command in the Containerfile, you can build a new container image that includes the necessary

8

CHAPTER 2. NEW FEATURES AND ENHANCEMENTS

packages. You can then upgrade your image mode host to the new image, incorporating the
packages into future builds.
For more information, see Persisting transient packages in your image  in  Managing content.

Jira:SAT-30671

Tracking transient packages on image mode hosts

Satellite provides options for viewing the persistence mode of packages on an image mode host:

On the host details page in the Satellite web UI, navigate to Content > Packages.
Persistence mode is displayed in the Persistence column.

From the command line, execute the hammer host package list --host-id My_Host_ID --
fields ALL command. Persistence mode is included in the output.

Note that information about package persistence is not yet available in Satellite. The data will be
provided by a future version of the Subscription Manager service.

Jira:SAT-36790

Enhanced support for multiple CV environments in hosts and activation keys in web UI

Previously, Satellite web UI could only display information about hosts and activation keys with
multiple content view (CV) environments assigned. With this update, you can also assign and manage
multiple CV environments for hosts and activation keys from the web UI.
For more information, see Managing content view environments  in  Managing content.

Note that with this release, the option to manage multiple CV environments in hosts and activation
keys is enabled by default.

Jira:SAT-26055

2.7. DOCUMENTATION

Source for documentation links in Satellite web UI can be configured for RHOKP

With this update, the Red Hat documentation server URL setting is available in the Satellite web UI.
You can use the setting to provide the URL of your instance of the Red Hat Offline Knowledge
Portal (RHOKP). When the RHOKP URL is provided, documentation links in the Satellite web UI point
to the RHOKP instance rather than the default docs.redhat.com site.
To view the Red Hat documentation server URL setting in the Satellite web UI, navigate to
Administer > Settings. The setting is located on the  General tab.

Jira:SAT-31701

Guidelines on expense management for your subscriptions

Your procurement team can review the new documentation on managing expenses for your Red Hat
subscriptions. For more information, see Expense management for Red Hat subscriptions  in
Overview, concepts, and deployment considerations .
Jira:SAT-36021[1]

9

Red Hat Satellite 6.19 Release notes

CHAPTER 3. TECHNOLOGY PREVIEW FEATURES

Explore Technology Preview features available in Red Hat Satellite 6.19.

For information on Red Hat scope of support for Technology Preview features, see Technology Preview
Features Support Scope.

3.1. MODEL CONTEXT PROTOCOL

MCP server is available for Satellite (Technology Preview)

Satellite provides a container image that you can use to run a Model Context Protocol (MCP) server
locally. The MCP server for Satellite is designed for advanced reporting and data analysis that
leverages AI capabilities. You can use it to generate dynamic and comprehensive reports from your
Satellite inventory. With the container image provided with Satellite 6.19, you can also use MCP to
patch hosts and incrementally update, publish, and promote content views. For more information on
this update, see Jira:SAT-40970.
For more information on MCP for Satellite, see Connecting AI applications to the MCP server for
Satellite.

Jira:SAT-35530

3.2. HOST PROVISIONING AND MANAGEMENT

OpenShift Virtualization plugin (Technology Preview)

You can provision virtual machines by using the OpenShift Virtualization plugin. For more
information, see Provisioning hosts.
Jira:SAT-18663[1]

Red Hat OpenShift Virtualization compute resource enhancements

This update introduces many fixes and improvements for the Red Hat OpenShift Virtualization
compute resource, which is a Technology Preview feature. This improves the stability and usability of
this feature.
Jira:SAT-41368

Kernel execution template (Technology Preview)

You can use the kernel execution (kexec) provisioning template for PXE-less boot methods. For
more information, see Discovery in PXE-less mode .
Jira:SAT-21012

10

CHAPTER 4. DEPRECATED FEATURES

CHAPTER 4. DEPRECATED FEATURES

The following functionalities are deprecated in Red Hat Satellite 6.19.

Deprecated functionalities will likely not be supported in future releases of this product and are not
recommended for new deployments. For the most recent list of deprecated functionality within a
particular major release, refer to the latest version of release documentation.

The support status of deprecated functionality remains unchanged within Red Hat Satellite 6.19. For
information about the length of support, see Red Hat Enterprise Linux Life Cycle  and Red Hat
Enterprise Linux Application Streams Life Cycle.

Deprecated hardware components are not recommended for new deployments on the current or future
releases. Hardware driver updates are limited to security and critical fixes only. Red Hat recommends
replacing this hardware as soon as reasonably feasible.

A package can be deprecated and not recommended for further use. Under certain circumstances, a
package can be removed from a product. Product documentation then identifies more recent packages
that offer functionality similar, identical, or more advanced to the one deprecated, and provides further
recommendations.

Hammer Admin is deprecated

The Hammer Admin plugin is deprecated. As an alternative, you can use the Satellite installer to
manage your Satellite Server or Satellite Capsule Server.
First deprecated in Satellite 6.19.

Jira:SAT-43244

API parameter deprecations

On hosts, the content_view_id and lifecycle_environment_id parameters are deprecated and will
be removed in a future release. On the POST /activation_keys and PUT /activation_keys/:id
activation keys, the content_view_id, environment_id, and environment parameters are
deprecated and will be removed in a future release. Check any automations you may have to make
sure they do not use API calls with these parameters.
Use the content_view_environment_ids or content_view_environments parameters instead.

First deprecated in Satellite 6.19.

Jira:SAT-42732

Legacy Job Invocations page is deprecated

The legacy Job Invocations Details page is deprecated and will be removed in a future version. The
new job details page is displayed by default.
First deprecated in Satellite 6.19.

Jira:SAT-43508

GRUB Legacy is deprecated in provisioning

GRUB Legacy, also known as GRUB version 1, is deprecated in provisioning and will be removed in a
future release. GRUB 1 was used by end of life distributions such as RHEL 6. Current distributions use
GRUB 2 and are not affected by the deprecation.
First deprecated in Satellite 6.18.

11

Red Hat Satellite 6.19 Release notes

Jira:SAT-39843

Puppet packages included in Satellite are deprecated

The puppet-agent and puppetserver packages, which are currently included in Satellite, are
deprecated. In a future release, Satellite will stop providing these packages. Satellite will provide
integration with OpenVox or Puppet packages that customers implement in their environment.
First deprecated in Satellite 6.18.

Jira:SAT-39110[1]

Sendmail is deprecated for delivering email

Delivering email by calling the sendmail binary on the system is deprecated and will be removed in a
future version. As an alternative, use the SMTP mail delivery method. For more information, see
Configuring Satellite Server for outgoing emails .
First deprecated in Satellite 6.18.

Jira:SAT-38905

External authentication with Red Hat Single Sign-On is deprecated

Configuring Satellite with Red Hat Single Sign-On (RH SSO) as an external authentication source is
deprecated. The RH SSO 7 product family reached End of Full Support. Instead of RH SSO, you can
configure Red Hat build of Keycloak as an external authentication source for Satellite.
To migrate from using RH SSO in your Satellite deployment, reconfigure the authentication source
settings on your 6.17 Satellite Server to follow the requirements for Red Hat build of Keycloak. For
more information, see Configuring SSO and 2FA with Red Hat build of Keycloak in Satellite .

For information on the current support policy for RH SSO, see Red Hat Application Services Product
Update and Support Policy.

First deprecated in Satellite 6.17.

Jira:SAT-27644

Legacy remote execution job form in the Satellite web UI is deprecated

The option to use the legacy web UI form to run remote execution jobs is deprecated and will be
removed in a future version. The new job invocation wizard will be the only available option. Note that
the new job invocation wizard is the default method to run remote execution jobs in Satellite 6.13 and
later versions.
First deprecated in Satellite 6.17.

Jira:SAT-30410

iPXE firmware is deprecated

Using iPXE firmware for network-boot provisioning is deprecated. Instead, use HTTP booting for
hosts in UEFI mode to reduce provisioning times. Note that iPXE firmware was never officially
supported in Red Hat Satellite.
First deprecated in Satellite 6.17

Jira:SAT-28823

12

CHAPTER 4. DEPRECATED FEATURES

hammer host subscription attach and hammer host subscription auto-attach commands are
deprecated

The hammer host subscription attach and hammer host subscription auto-attach commands are
deprecated. The commands are non-functional and do not result in attaching a subscription.
First deprecated in Satellite 6.16

Note: Entitlement-based subscription management was removed in Satellite 6.16.

Jira:SAT-28367

Asynchronous SSH remote execution mode is deprecated

The async-ssh remote execution mode is deprecated. If you have unstable connectivity between
Capsules and managed hosts, use the pull mode instead. For more information about pull mode, see
Transport Modes for Remote Execution in  Managing hosts.
First deprecated in Satellite 6.13.

Jira:SAT-16415

Package Group Actions is deprecated

The Package Group Actions option in the web UI is deprecated.
First deprecated in Satellite 6.10.

Jira:SAT-27578

katello-ca-consumer package and katello-rhsm-consumer script are deprecated

The katello-ca-consumer package and katello-rhsm-consumer script are deprecated. You must
use the global registration template to register a host.
First deprecated in Satellite 6.9.

Jira:SAT-21372

Bootstrap.py host registration script is deprecated

The bootstrap.py script for registering a host to Satellite or Capsule is deprecated. It is replaced with
the curl command created by using the global registration template.
First deprecated in Satellite 6.9.

Jira:SAT-21137

13

Red Hat Satellite 6.19 Release notes

CHAPTER 5. REMOVED FEATURES

The following functionalities are removed in Red Hat Satellite 6.19.

5.1. SERVER ADMINISTRATION

Legacy Content Host Details page and related API endpoints are removed

The legacy Content Host Details page is removed. The auto_attach parameter is removed from the
following endpoints:

PUT /activation_keys/:id

POST /activation_keys

POST /activation_keys/:id/copy

The following API endpoints are removed entirely:

PUT /activation_keys/:id/add_subscriptions

PUT /activation_keys/:id/remove_subscriptions

PUT /hosts/:host_id/subscriptions/auto_attach

PUT /hosts/:host_id/subscriptions/add_subscriptions

PUT /hosts/:host_id/subscriptions/remove_subscriptions

PUT /hosts/bulk/remove_subscriptions

PUT /hosts/bulk/add_subscriptions

PUT /hosts/bulk/auto_attach

Check that your automation does not use any of the removed endpoints.

Jira:SAT-21227[1]

5.2. HOST PROVISIONING AND MANAGEMENT

GRUB Legacy is removed from provisioning

GRUB Legacy, also known as GRUB version 1, is removed from provisioning. GRUB 1 was used in
RHEL versions prior to RHEL 7. Current distributions use GRUB 2 and are not affected by the
deprecation. Systems that were upgraded from an older version might contain obsolete GRUB 1 files
and templates.
Jira:SAT-38784

Content Host UI and package group actions in the web UI are removed

The Content Host UI is removed. This includes all pages under Hosts > Content Hosts. As an
alternative, use the new UI at Hosts > All Hosts.
Package group actions in the web UI are removed. As an alternative, use the Run Command remote
execution job template.

14

CHAPTER 5. REMOVED FEATURES

Jira:SAT-37927

5.3. USERS AND ROLES

Overriding organizations and locations on the filter level is no longer available

You can no longer specify organizations and locations when editing a permission filter. Filters now
always inherit the organizations and locations set at the role level. The web UI form for editing a filter
no longer includes the Override and Unlimited checkboxes. You can still add a search to the filter as
long as the selected resource type supports granular filtering.
Jira:SAT-28731, Jira:SAT-28820

15

Red Hat Satellite 6.19 Release notes

CHAPTER 6. KNOWN ISSUES

The following known issues have been identified in Red Hat Satellite 6.19. Review them to anticipate
potential problems and identify workarounds for your environment.

6.1. WEB UI

All Hosts page always links to the new host details UI

The links on the Hosts > All Hosts page always point to the new host details UI, even if the setting
New host details UI is set to  No.
To work around this problem, display the old host details UI by clicking the options menu in the upper
right and selecting Legacy UI.

Jira:SAT-37128

6.2. INSTALLATION AND UPGRADE

"Permission Denied" errors on Lightspeed pages in secured systems

Incorrect file permissions on the /var/lib/foreman/public/assets/apps directory in combination with
a non-default umask cause Lightspeed pages to fail with 403 "Permission Denied" errors. This
occurs, for example, in systems secured in accordance with CIS and STIG profiles, which use non-
default umasks.
To work around this problem, manually change the file permissions. For more information, see the
Red Hat Knowledgebase solution Several 'Permission Denied' errors on the iop-core-engine
container and other files/services after installing or upgrading to Satellite 6.18 with IOP enabled when
non-default umask is applied.

Jira:SAT-41246

6.3. RED HAT LIGHTSPEED

Red Hat Lightspeed vulnerability CVE map download fails with proxy

Satellite servers configured for the Red Hat Lightspeed vulnerability service in Satellite fail to
download CVE mapping files if the Satellite server uses an HTTP proxy to reach
https://security.access.redhat.com. This issue is caused by the iop-cvemap-download.service
service lacking HTTP proxy configuration.
To work around this problem, manually set the HTTPS_PROXY and NO_PROXY environment
variables for the iop-cvemap-download service. For more information, see  Installing Red Hat
Lightspeed in Satellite on a connected Satellite Server.

Jira:SAT-39459

Red Hat Lightspeed might fail on Satellite servers with managed DNS

When the named service is already running on a Satellite server, the  aardvark-dns service, which is
required for running containers, fails to start. This is caused by a conflict between named and
podman configurations for IPv4 connections. As a consequence, Red Hat Lightspeed installations
might fail on Satellite servers configured for managed DNS. To work around this problem, perform
the following steps:

1.  Set managed DNS in satellite-installer to  unmanaged:

16

CHAPTER 6. KNOWN ISSUES

# satellite-installer --foreman-proxy-dns-managed=false

2.  Configure your Satellite server to only listen on the local IP addresses by adding the

following content to the /etc/named/options.conf file:

listen-on-v6 { fd00:4::25; };
listen-on { 192.168.4.25; };

3.  Restart the named service.

4.  You can verify that the configuration works by checking that the DNS service is listening on

port 53:

[root@satellite6:/root]# netstat -tulpn| grep 53
tcp        0      0 10.130.0.1:53           0.0.0.0:*               LISTEN      2199/aardvark-dns
tcp        0      0 192.168.122.1:53        0.0.0.0:*               LISTEN      2252/dnsmasq
tcp        0      0 192.168.4.25:53         0.0.0.0:*               LISTEN      1016/named
tcp        0      0 127.0.0.1:953           0.0.0.0:*               LISTEN      1016/named
tcp6       0      0 fd00:4::25:53           :::*                    LISTEN      1016/named

Jira:SAT-39941

Cannot easily select all CVEs in Red Hat Lightspeed vulnerability

On the Red Hat Lightspeed vulnerability page, you cannot easily select all CVEs.
To work around this problem, manually click the drop-down list near the Select button and choose
Select page (100 items) for each page individually.

Jira:SAT-42758

Red Hat Lightspeed vulnerability service in Satellite does not work on IPv6 networks

Red Hat Lightspeed is configured with IPv4 networking only. On IPv6 networks, running a Red Hat
Lightspeed vulnerability service update fails to sync vulnerability data.
There is no known workaround.

Jira:SAT-41384

6.4. SECURITY AND AUTHENTICATION

FIPS-enabled hosts running RHEL 9.3 or earlier cannot upload OpenSCAP reports

On hosts that run RHEL 9.3 or earlier versions with FIPS mode enabled, uploading an OpenSCAP
report fails with the following error:

Unable to load certs
Neither PUB key nor PRIV key

For more details, see a related Knowledgebase solution. Note that the problem is fixed for hosts that
run RHEL 9.4 or later versions.

No known workaround exists.

17

Red Hat Satellite 6.19 Release notes

Jira:SAT-28297

6.5. CONTENT MANAGEMENT

Unable to synchronize custom repositories by using only the upstream username without password

Attempts to synchronize a custom repository by using only the upstream username fail with errors
about unauthorized access.
Satellite web UI displays the following error message:

An error occurred saving the repository: Validation failed: Upstream username requires upstream
password to be set.

Hammer CLI displays the following error message:

401, message='Unauthorized', url=<upstream_url>

No known workaround is available.

Jira:SAT-41022

Unable to upload more than 127 packages at once from the Satellite web UI

When uploading packages to a repository from the Satellite web UI, you can upload up to only 127
RPMs or other files. This known issue occurs due to a limitation with the Rack gem.
To work around this problem, use the API bulk uploader for operations that involve a large number of
files.

Jira:SAT-35291

Legacy empty CCVs that were previously published and promoted cannot be deleted

In some situations, composite content views (CCVs) that do not contain any content views cannot be
deleted. This issue affects CCVs that were created before Satellite 6.18 and were previously
published and promoted.
For example, when attempting to remove the CCV with the hammer content-view remove
command, the command displays the following error:

Could not remove objects from content view:
  PG::NotNullViolation: ERROR:  null value in column "katello_content_view_version_id" of relation
"katello_content_view_histories" violates not-null constraint

To work around this problem, publish a new version of the empty CCV and then delete it.

Jira:SAT-35940

Flatpak content becomes inaccessible after upgrading to Satellite 6.19

Upgrading to Satellite 6.19 prevents hosts from consuming Flatpak content managed by your
Satellite Server. The Flatpak registry static index endpoint located at
https://<satellite.example.com>/pulpcore_registry/index/static returns a server error.

This issue exists because the Pulp Core version included in Satellite 6.19 implements response

18

This issue exists because the Pulp Core version included in Satellite 6.19 implements response
caching that requires JSON-serializable responses, while the pulp-container FlatpakIndex view
returns a Python set in its response data.

CHAPTER 6. KNOWN ISSUES

No known workaround is available.

Jira:SAT-44554

6.6. HOST PROVISIONING AND MANAGEMENT

PXE/TFTP provisioning of RHEL 7 hosts on UEFI (EFI-based) firmware fails due to incompatible
bootloaders

During provisioning, Satellite copies the bootloader from the /boot directory of the underlying OS to
the /tftpboot directory. Because RHEL 9.7 and later versions provide a bootloader that is
incompatible with RHEL 7 and earlier versions, the provisioning of RHEL 7 with PXE/TFTP on UEFI
(EFI-based) firmware fails.
To work around this problem, manually provide the RHEL 7 systems with an older bootloader. For
more information, see the Red Hat Knowledgebase solution Provisioning a RHEL 7 client system
stuck at "Booting Kickstart default PXEGrub2" on Red Hat Satellite Capsule 6.18.

Jira:SAT-41340

Logs incorrectly show missing resources in Red Hat OpenShift Virtualization host creation

In deployments with the Red Hat OpenShift Virtualization compute resource, which is a Technology
Preview feature, the production log shows <Kubeclient::ResourceNotFoundError>
virtualmachineinstances.kubevirt.io "host.example.com" not found errors even though no
resources are missing from the provisioning. This is caused by attempts to access a missing
VirtualMachineInstance (VMI) that report a warning due to fog-kubevirt exception handling.
To work around this problem, ignore these warnings. No action is needed.

Jira:SAT-43378

Concurrent host registration fails with a database error

When you register multiple hosts of the same operating system version, the hosts initially fail to
register. The redundant creation of an operating system entry in the Red Hat Subscription
Management (RHSM) fact parser triggers a unique constraint violation.
To work around this problem, rerun the registration. Note that this leads to an increase in registration
time due to the need for retries.

Jira:SAT-43299

6.7. BACKUP AND RESTORE

Restoring from backup fails due to inconsistencies in the data

If the backup is generated from a database with inconsistencies, the restore fails. The satellite-
maintain tool uses the PostgreSQL amcheck extension to detect inconsistencies in the data before
backup to prevent issues during restore.
To work around this problem, contact Red Hat customer support to fix any detected inconsistencies
before proceeding with the backup. For more information, see Restoring Red Hat Satellite 6.16+ fails
complaining about db duplicates on CREATE UNIQUE INDEX in the  Red Hat Knowledgebase.

19

Red Hat Satellite 6.19 Release notes

Jira:SAT-35461

6.8. IPV6

virt-who is not supported on IPv6-only networks

Satellite does not support the virt-who agent in an IPv6-only network.
No known workaround exists.

Jira:RHEL-40069

Additional configuration is required in IPv6-only networks when using kinit for IdM and AD users

If your Satellite Server runs in an IPv6-only network and also runs on RHEL 9.6 and earlier versions,
Kerberos authentication for external users from Identity Management (IdM) and Active Directory
(AD) fails. This known issue is caused by a bug in the System Security Services Daemon (SSSD) and
occurs when the DNS name of the IdM or AD server can be translated to both an IPv4 and IPv6
address but the IPv4 address is not accessible, for example because it is blocked by a firewall.
To work around this problem, configure the lookup_family_order option in the
[domain/<domain_name>] in the  /etc/sssd/sssd.conf file:

[domain/example.com]
lookup_family_order = ipv6_only

Jira:SAT-32530

Mismatch of the IPv6 address entry when using a DHCPv6 server

When you use a DHCPv6 server to assign an IP address dynamically and you provision a host in an
IPv6 network, Satellite contains an IPv6 address that does not match the actual IPv6 address of the
host. This mismatch impairs host management capabilities, such as remote execution.
To work around this problem, perform one of the following steps:

Execute subscription-manager facts --upload on the host.

Wait for the next facts upload to resolve the issue. Note that the Ignore interfaces facts for
provisioning (ignore_puppet_facts_for_provisioning) setting can disable updating the
interfaces from facts.

Jira:SAT-30601

Host discovery fails in an IPv6 network

When you attempt to discover an unknown host in an IPv6 network, the discovery fails with Error:
1001: Failed to open TCP connection to satellite.example.com:443.
No known workaround exists.

Jira:SAT-30796

Failure to provision hosts in PXE-less Discovery over IPv6

After PXE-less host discovery on an IPv6 Satellite, when the host starts provisioning, fails to resolve
the DNS entry for Satellite. As a result, the host fails to fetch Kickstart and the required files.

20

No known workaround exists.

Jira:SAT-30794

CHAPTER 6. KNOWN ISSUES

21

Red Hat Satellite 6.19 Release notes

CHAPTER 7. FIXED ISSUES

Red Hat Satellite 6.19 fixes the following bugs that may have previously impacted Red Hat Satellite
deployments.

7.1. INSTALLATION AND UPGRADE

Red Hat Lightspeed no longer fails to enable when Host.NetworkBackend for Podman is set to CNI

Before this update, when Host.NetworkBackend for Podman was set to Container Network
Interface (CNI on a Satellite Server, satellite-installer failed to enable Red Hat Lightspeed. The
issue occured because the Red Hat Enterprise Linux 9.6 ISO provided a version of the container-
selinux policy that older than 2.237.0. With this release, the error starting IoP container due to CNI
network configuration is resolved.
Jira:SAT-39069

Validation no longer fails due to duplicate operating system entries

Before this update, Satellite duplicated operating system entries when uploading Puppet facts. As a
consequence, uploading facts failed with a validation error, which also affected Leapp upgrades. This
release improves how the fact parser handles operating system title uniqueness and prevents
duplicate entries. As a result, Satellite correctly reuses existing operating system entries instead of
trying to create new ones.
Jira:SAT-40641

7.2. SECURITY AND AUTHENTICATION

Proper session termination in certain API endpoints and enforced reauthentication

Before this update, API endpoints that call the add_smart_proxy_filters function bypassed user
authentication. This was due to improper session termination logic introduced in Satellite 6.18. In
addition, user sessions remained active beyond the period specified in the idle_timeout setting. This
affected the API endpoints related to the following resources:

Organizations

Repositories

Config reports

Hosts

As a consequence, removed and nonexistent users failed due to missing required permissions and not
due to failed authentication. In addition, user sessions were not terminated and could access certain
endpoints without reauthentication.

With this release, user sessions no longer bypass authentication and are terminated correctly. As a
result, users are forced to reauthenticate to access those resources.

Jira:SAT-38951

7.3. CONTENT MANAGEMENT

22

CHAPTER 7. FIXED ISSUES

Capsules sync correctly after upgrading Satellite Server to 6.18

Previously, after upgrading Satellite Server from version 6.17 to version 6.18 while keeping Capsules
at version 6.17, Capsule sync started failing. The 6.18.3 update fixes the problem, and 6.17 Capsules
sync as expected after upgrading Satellite Server to 6.18.
Jira:SAT-41180

Capsule sync no longer fails due to a null value in UUID of a host

Before this update, when attempting to sync Capsule in certain setups with an improperly registered
host, the sync failed due to a null value in the uuid column of the  hosts database table. This update
fixes the issue, and the host UUID is correctly set in the described setups.
Jira:SAT-39794

7.4. HOST PROVISIONING AND MANAGEMENT

Root password update added to cloud-init template for image-based deployment on VMware

Before this update, image-based deployment on VMware using Satellite set the root password to the
password defined in the VM template, not the password defined in the Host settings during the build
process. As a consequence, the root password remained unchanged from the VM template during
image-based deployment. With this release, the root password update has been incorporated into
the cloud-init template. Consequently, the root password changes correctly in accordance with the
Host settings in cloud-init templates.
Jira:SAT-20584

Provisioning RHEL 9 hosts no longer creates unnecessary localhost.localdomain entries

Before this update, provisioning of RHEL 9 hosts with Foreman discovery image (FDI), PXE-less
discovery, and static networking created an unnecessary localhost.localdomain entry due to a
missing hostname update. With this release, Satellite sets the hostname to the static value before
the Red Hat Subscription Manager call. As a result, setting the hostname prevents unnecessary
localhost.localdomain creation.
Jira:SAT-39469

Firmware type in Compute Profiles and the New Host form no longer reverts to Automatic

Before this update, the selected firmware type could be reset to Automatic or shown incorrectly in
the web UI. This release ensures that the firmware type keeps the correct value.
Jira:SAT-31447

Corrected power operations on hosts in Redfish BMC provider

Before this update, power operations were implemented in the Redfish provider of the baseboard
management controller (BMC) as follows:

Cycle – implemented incorrectly

Reboot – not implemented

Reset – not implemented

As a consequence, users experienced host shutdown instead of cycle and could not use host reboot
or reset. This release fixes implementation of all three operations. As a result, BMC operations work
correctly on the Redfish provider.

23

Red Hat Satellite 6.19 Release notes

Jira:SAT-37871

Incomplete Create host form on OpenShift Virtualization no longer duplicates disks

Before this update, submitting a Create host form on an OpenShift Virtualization compute resource
with a validation error, such as an empty required field, caused additional virtual disks to be added on
the Virtual machine tab. This might also have caused host creation failures.
This update fixes the issue. The disk configuration remains unchanged when validation fails, and
prevents disk duplication.

Jira:SAT-42730

7.5. USERS AND ROLES

External users can now log in to Satellite without specifying an email address

Previously, external users, such as users defined in Identity Management or Active Directory, were
unable to log in to Satellite without an email address. With this update, external users can log in to
Satellite even when their user account does not include an email address. Note that if the Mail
Enabled option is enabled for a user account in the Satellite web UI, the user is still prompted to
enter an email address.
Jira:SAT-23437

7.6. RED HAT LIGHTSPEED

hammer ping correctly lists Red Hat Lightspeed services in Satellite

Before this update, with Red Hat Lightspeed in Satellite enabled, the hammer ping command did
not display the Advisor and Vulnerability services. Additionally, some web UI elements, such as the
Recommendations tab on host details and the  Recommendations list page behaved as in a non-
Red Hat Lightspeed in Satellite setup.
This update fixes the problem, and hammer ping correctly displays the Advisor and Vulnerability
services.

Jira:SAT-39088

Tag generation works with Any location

Before this update, accessing the Recommendations or Vulnerabilities menu produced an error
message when the location was set to Any location. As a consequence, users could not see a global
view of all systems in Recommendations or Vulnerabilities. This update adds support for forwarding
Insights Cloud UI requests when the session has no location selected. Tag generation works when the
location is not set by using a wildcard location tag and relaxing host filtering on location. As a result,
you can access the Recommendations or Vulnerabilities menu without selecting a location.
Jira:SAT-38683

"Sync all inventory status" no longer fails with Red Hat Lightspeed

Before this update, with Red Hat Lightspeed enabled, performing the Sync all inventory status
operation on the Inventory Upload page could fail with an error similar to the following:

Could not get task details: TypeError: Cannot read properties of undefined (reading 'sync')

24

CHAPTER 7. FIXED ISSUES

This update adds inventory synchronization in IOP mode, hides cloud-specific UI components that
are not relevant in local Advisor Engine environments, and has fixed the issue. The Inventory Upload
page and its controls are adjusted for environments that use Red Hat Lightspeed, and using Sync all
inventory status no longer produces this error.

Jira:SAT-36556

Recommendations and Vulnerabilities no longer fail to switch hosts

Before this update, when switching between hosts by using the breadcrumb switcher on the host
details page, the Recommendations and Vulnerabilities tabs did not update to reflect the newly
selected host.
With this update, this issue is fixed for cases where you switch between two registered hosts with Red
Hat Lightspeed.

However, if you switch from a host that is registered to Red Hat Lightspeed to a host that is not
registered, you might still encounter a blank screen and loading spinner instead of being redirected to
the Overview tab. To work around this problem, reload the page.

Jira:SAT-38703

25

Red Hat Satellite 6.19 Release notes

CHAPTER 8. CHANGES IN SATELLITE-INSTALLER PARAMETERS,
HAMMER CLI, REST API, AND USAGE METRICS

Review these changes to update your existing workflows and discover new capabilities in Red Hat
Satellite.

8.1. SATELLITE-INSTALLER PARAMETERS

New satellite-installer parameters

--foreman-db-extra-options

--reset-foreman-db-extra-options

--foreman-proxy-plugin-remote-execution-script-ssh-host-ca-public-keys-file

--reset-foreman-proxy-plugin-remote-execution-script-ssh-host-ca-public-keys-file

--foreman-proxy-plugin-remote-execution-script-ssh-user-ca-public-key-file

--reset-foreman-proxy-plugin-remote-execution-script-ssh-user-ca-public-key-file

--iop-core-engine-log-level-insights-core-dr

--reset-iop-core-engine-log-level-insights-core-dr

--iop-core-engine-log-level-insights-kafka-service

--reset-iop-core-engine-log-level-insights-kafka-service

--iop-core-engine-log-level-insights-messaging

--reset-iop-core-engine-log-level-insights-messaging

--iop-core-engine-log-level-root

--reset-iop-core-engine-log-level-root

--reset-puppet-agent-manage-environment

--puppet-agent-manage-environment

Removed satellite-installer parameters

This release does not remove or replace any satellite-installer parameters.

8.2. HAMMER CLI

New Hammer commands and subcommands

This release does not add any Hammer commands or subcommands.

New Hammer options

--lifecycle-environment-ids is added to the following commands:

hammer content-view create

26

CHAPTER 8. CHANGES IN SATELLITE-INSTALLER PARAMETERS, HAMMER CLI, REST API, AND USAGE METRICS

hammer content-view create

hammer content-view update

--dependency-ids is added to the  hammer flatpak-remote remote-repository mirror
subcommand

--containerfile-install-command is added to the  hammer host package subcommand

--persistence is added to the  hammer host package subcommand

--clone is added to the  hammer job-template subcommand

--ui-compact-mode is added to the following commands:

hammer user update

hammer user create

--clone is added to the  hammer job-template subcommand

Removed Hammer commands and subcommands

add-subscription, remove-subscription, and subscriptions subcommands are removed
from the hammer activation-key command

attach and remove subcommands are removed from the  hammer host subscription
command

Removed Hammer options

--auto-attach is removed from the following commands:

hammer activation-key create

hammer activation-key updatesubscriptions

hammer host subscription

--autoheal is removed from the following commands:

hammer host create

hammer host update

location, location-id, location-title, organization, organization-id, and organization-title
are removed from the following commands:

hammer filter create

hammer filter update

hammer location create

hammer location delete

27

Red Hat Satellite 6.19 Release notes

hammer location info

hammer location list

hammer location update

Additional resources

For more information, see Using the Hammer CLI tool  or enter the commands with the  --help
option.

8.3. REST API

New API endpoints

Host_debs endpoints

/api/host_debs/:id

/api/host_debs/compare

/api/host_debs/installed_debs

Host_packages

/api/hosts/:host_id/transient_packages/containerfile_install_command

Host_tracer endpoints

/api/hosts/bulk/traces/auto_complete_search

Hosts_bulk_actions endpoints

api/hosts/bulk/assign_content_view_environments

/api/hosts/bulk/change_power_state

Removed API endpoints

Activation_keys endpoints

/api/activation_keys/:id/add_subscriptions

/api//activation_keys/:id/remove_subscriptions

/api/activation_keys/:id/auto_attach

/api/activation_keys/auto-attach

/api/activation_keys/:id/copy/auto-attach

Hosts endpoints

/api/hosts/:host_id/subscriptions/add_subscriptions

28

CHAPTER 8. CHANGES IN SATELLITE-INSTALLER PARAMETERS, HAMMER CLI, REST API, AND USAGE METRICS

/api/hosts/:host_id/subscriptions/remove_subscriptions

/api/hosts/bulk/remove_subscriptions

/api/hosts/bulk/add_subscriptions

/api/hosts/bulk/auto_attach

8.4. ANSIBLE MODULES

This release performs the following changes in the Satellite Ansible Collection.

New Ansible modules

redhat.satellite.content_view_history_info

Removed Ansible modules

This release does not remove any Ansible modules.

8.5. COLLECTED USAGE METRICS

New usage metrics

rh_cloud_connector_enabled

rh_cloud_exclude_host_package_info

rh_cloud_hosts_count

rh_cloud_inventory_upload_enabled

rh_cloud_minimal_data_collection

rh_cloud_mismatched_auto_delete

rh_cloud_mismatched_hosts_count

rh_cloud_obfuscate_inventory_hostnames

rh_cloud_obfuscate_inventory_ips

rh_cloud_recommendations_sync_enabled

rh_cloud_total_hits

Additional resources

For more information, see Usage metrics collection in Satellite  in  Administering Red Hat
Satellite.

29

Red Hat Satellite 6.19 Release notes

APPENDIX A. PROVIDING FEEDBACK ON RED HAT
DOCUMENTATION

We appreciate your feedback on our documentation. Let us know how we can improve it.

Use the Create Issue form in Red Hat Jira to provide your feedback. The Jira issue is created in the Red
Hat Satellite Jira project, where you can track its progress.

Prerequisites

Ensure you have registered a Red Hat account .

Procedure

1.  Click the following link: Create Issue. If Jira displays a login error, log in and proceed after you

are redirected to the form.

2.  Complete the Summary and Description fields. In the  Description field, include the

documentation URL, chapter or section number, and a detailed description of the issue. Do not
modify any other fields in the form.

3.  Click Create.

30

APPENDIX B. REVISION HISTORY

APPENDIX B. REVISION HISTORY

0.0-0

May 6 2026, Jan Fiala (jafiala@redhat.com)

Release of the Red Hat Satellite 6.19 Release Notes.

0.0-1

May 19 2026, Jan Fiala (jafiala@redhat.com)

Added SAT-41516 and SAT-41384

31

Red Hat Satellite 6.19 Release notes

APPENDIX C. LIST OF TICKETS BY COMPONENT

Bugzilla and JIRA tickets are listed in this document for reference. The links lead to the release notes in
this document that describe the tickets.

Component

Tickets

Authentication

Jira:SAT-38951, Jira:SAT-27644

Backup & Restore

Jira:SAT-35461

Branding

Jira:SAT-31701

Capsule - Content

Jira:SAT-41180, Jira:SAT-39794

Compute Resources - OCP-
V

Jira:SAT-42730, Jira:SAT-43378

Compute Resources -
VMWare

Jira:SAT-31447

Compute Resources - libvirt

Jira:SAT-40266

Container Image
Management

Jira:SAT-44554

Content Views

Jira:SAT-35940

Content management

Jira:SAT-26055

Fact

Hammer

Jira:SAT-40641

Jira:SAT-43244, Jira:SAT-28367

Host management

Jira:SAT-39060

Hosts

IPv6-bug

Jira:SAT-37927, Jira:SAT-37871, Jira:SAT-42732, Jira:SAT-27578

Jira:RHEL-40069, Jira:SAT-32530, Jira:SAT-30601, Jira:SAT-30796,
Jira:SAT-30794

Image Mode

Jira:SAT-30671, Jira:SAT-36790

Insights - Advisor

Jira:SAT-36556, Jira:SAT-39941

Insights - Vulnerability

Jira:SAT-40466, Jira:SAT-40203, Jira:SAT-39088, Jira:SAT-38683,
Jira:SAT-39459, Jira:SAT-42758, Jira:SAT-41384

32

APPENDIX C. LIST OF TICKETS BY COMPONENT

Component

Tickets

Installation

Jira:SAT-39069, Jira:SAT-41246

Leapp integration

Jira:SAT-38080

MCP

Jira:SAT-40970, Jira:SAT-35530

Performance

Jira:SAT-35291

Provisioning

Jira:SAT-38784, Jira:SAT-39469, Jira:SAT-18663, Jira:SAT-41368,
Jira:SAT-21012, Jira:SAT-39843, Jira:SAT-28823, Jira:SAT-41340

Provisioning Templates

Jira:SAT-18489, Jira:SAT-20584

Puppet

RH Cloud

Jira:SAT-31648, Jira:SAT-39110

Jira:SAT-38703

Registration

Jira:SAT-41516, Jira:SAT-43299

Remote Execution

Jira:SAT-34616, Jira:SAT-28038, Jira:SAT-43508, Jira:SAT-30410

Repositories

Jira:SAT-41022, Jira:SAT-35291

SCAP Plugin

Jira:SAT-28297

Subscription Management

Jira:SAT-21227

Upgrades

Jira:SAT-40641

Users and Roles

Jira:SAT-28731, Jira:SAT-23437

Web UI

other

Jira:SAT-32173, Jira:SAT-23851, Jira:SAT-35463, Jira:SAT-37128

Jira:SAT-31701, Jira:SAT-36021, Jira:SAT-38905, Jira:SAT-27644,
Jira:SAT-28823, Jira:SAT-27578, Jira:SAT-21372, Jira:SAT-21137

33

