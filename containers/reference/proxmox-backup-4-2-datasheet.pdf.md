P R O X M O X
B A C K U P   S E R V E R

O V E R V I E W

B E N E F I T S

Proxmox Backup Server is an enterprise backup
solution for backing up and restoring virtual machines,
containers, and physical hosts. With key features
like incremental backups, deduplication, Zstandard
compression, and authenticated encryption (AE),
Proxmox Backup Server ensures that protecting
your most valuable data is quick and effortless. Tight
integration with Proxmox VE makes Proxmox Backup
Server a great choice for seamlessly backing up your
VMs and containers – even between remote sites. The
intuitive web-interface provides a great user experience
for deploying, managing, and monitoring the server, for
IT experts and novices alike. Proxmox Backup Server is
lightning fast, meaning that when disaster strikes, you‘ll
have that file, archive or VM back in no time.

W H Y   P R O X M O X   B A C K U P
S E R V E R ?

Every system administrator knows that the
occurrence of data loss is only a matter of time and
the best you can be is prepared. For this reason,
reliable backup software is the most essential
software that you can invest in. To meet your
operational goals, the easy-to-use Proxmox Backup
Server lets you back up your data in a space-efficient
manner, restore it in a flash, and effectively reduce
work hours thanks to simplified management. By
supporting incremental, fully deduplicated backups,
Proxmox Backup Server significantly reduces network
load and saves valuable storage space. With strong
encryption and methods of ensuring data integrity,
backing up data, even to targets which are not fully
trusted, is safe. Moreover, the available range of
access control options help to ensure that users are
limited to only the level of access they require. With
enterprise support available from the Proxmox team,
you will get the most from your software solution.

Versatility

Backup and restore diverse workloads,
including VMs, containers, and physical hosts
without artificial limits.

Unified management
Manage and monitor all backup, restore,
and maintenance tasks easily with the intuitive
GUI or CLI.

Efficient & Fast

Incremental, deduplicated and compressed
backups optimize storage usage and speed.

Secure

Data integrity, strong encryption on client-side,
and ransomware protection for critical data,
on-premises or remotely.

Tape Backup

Ideal for a 3-2-1 backup strategy and for
compliance-driven industries.

100% Open-Source

No hidden licensing fee and full access to
source code for customization.

Made for Production
Keep your business running smoothly with
Enterprise-grade services & technical support
from Proxmox.

1/5© 2026 Proxmox Server Solutions. All rights reserved. All trademarks are the property of their respective owners. PROXMOX  BACKUP SERVER V4.2DATASHEETEnterprise-Class Backup Solution

Proxmox VE Integration

 D Secure backup of VMs, containers, and

physical hosts.

 D Optimized for virtual environments like Proxmox VE.
 D Written in Rust for performance, speed, and

memory efficiency.

 D Store on-premises and remotely.
 D Stand-alone solution means no vendor lock-in.

 D Proxmox Virtual Environment is fully supported.
 D Add datastores and run backups in the same way

you would with any other Proxmox VE storage type.

 D Best choice for quick and simple backup of VMs
(supporting QEMU dirty bitmaps) and containers.
 D Restore single files from VM and container backups.
 D Live-restore feature allows for starting a VM,

as soon as the restore starts.

Free & Open-Source Software
 D Licensed under the GNU AGPL, v3.
 D Debian-based, using the Proxmox kernel with

OpenZFS support.

 D Public code repository (Git).
 D Open development on transparent mailing list.
 D Bug tracker for issue tracking.
 D Community support forum.
 D Documentation, project page, video tutorials,

Incremental, Deduplicated Backups
 D Only changes since the last backup are sent and
stored – whether it’s an archive, VM, or container.

 D The deduplication layer reduces the amount of

duplicate data on the backup server.

 D Using Proxmox File Archive Format (.pxar) allows
you to achieve a high level of deduplication.

 D Metadata and data are stored separately for faster

howto guides, and much more.

change detection.

Enterprise Support Agreement
 D Avoid hidden costs with clear subscription model.
 D Flexible support options that grow with your needs.
 D Access to the stable and extensively tested

Enterprise Repository.

 D Updates and version upgrades via GUI.
 D Proxmox Offline Mirror tool to keep air-gapped

systems up-to-date.

 D Premium technical support from the highly-skilled

Proxmox support team.

 D Large network of resellers & partners who help

 D Low network impact – only changes in data are
transferred from the backup client to the server.

 D Storage space is used efficiently.
 D Fast incremental backup (QEMU dirty-bitmap

support) for running VMs.

 D Use of Zstandard compression to compress several

GBs of data per second, before sending.

 D Datastore namespaces enable deduplication of

data from multiple backup sources.

Flexible retention options
 D Schedule from the server or trigger manually

with your project.

from the client.

 D Built-in Prune Simulator to visualize settings.
 D Intelligently thin-out backups over time.
 D Fine-grained pruning selection of whole datastore

or specific namespaces.

Client-Server Model
 D Separation allows multiple, unrelated hosts to use

the backup server.

 D The client tool will work with most modern Linux
distributions, allowing you to create and manage
backups from all your hosts.

 D Ability to encrypt on the client-side, to ensure data

is secure before reaching the server.

2/5© 2026 Proxmox Server Solutions. All rights reserved. All trademarks are the property of their respective owners. PROXMOX  BACKUP SERVER V4.2DATASHEETEncryption

Data integrity

 D Strong client-side encryption with AES-256 in

 D Accurate and consistent backups with built-in

Galois/Counter Mode (GCM) means data is useless
to unauthorized persons.

 D Use of a master key (RSA public/private key pair)
to store encrypted version of the encryption key.
Print secret encryption keys on paper to place in a
secure vault for safe, long-term storage.

SHA-256 checksum algorithm.

 D Schedule regular backup verification, to detect

bit rot and confirm backups are safe.

 D Maintenance mode with active operations

tracking allows for safer maintenance windows.

Access Control
 D Broad array of privilege roles (groups permission

sets), to specify each user’s permissions.

 D Create API Tokens and lock them further down for
secure and easily revocable access, for example to
a specific datastore and namespace.

 D Multiple Authentication Realms: Add Linux

PAM users, utilize the Backup Server realm for
systemindependent access with user-self service,
or relay authentication to your OpenID Connect
single signon solution.

 D Support for LDAP as authentication realm.
 D Support for Microsoft Active Directory (MS ADS).
 D Setup Two-Factor Authentication.
 D Restricted by default: new users or API tokens do

not have any permissions.

Two-Factor Authentication
 D Can be activated and configured via GUI,

providing high security.

 D Configure multiple 2nd factors.
 D Time-based One Time Passwords (TOTP).
 D Web Authentication (WebAuthn).
 D Single-use recovery code.
 D TFA/TOTP lockout to protect against

brute-forceattacks.

Ransomware Protection
 D Off-server and off-site synchronization for

recovery.

 D Data for existing blocks is not rewritten.
 D Fine-grained user and access management system.
 D SHA-256 checksums and verification jobs can

indicate possible ransomware.

Quick Restore
 D Fast and simple restore via the GUI – ease

stressful situations.

 D Granular recovery options.
 D Quickly search contents of an archive.
 D Restore single files/directories/archives using the

GUI or interactive recovery shell.

 D Download as ZIP or zstd-compressed tar archive.

Remote Synchronization
 D Encrypt snapshots on the fly during push sync,
decrypt them during pull sync, and manage all
tape and sync encryption keys centrally.   N E W
 D Synchronize datastores or individual namespaces
from other locations for redundancy or long-term
archival.

 D Efficiently synchronize data to offsite locations.
 D Only transfer changes since previous sync.
 D Filter the backups which should be synced.
 D Schedule sync jobs to run regularly or start them

manually in the GUI.

3/5© 2026 Proxmox Server Solutions. All rights reserved. All trademarks are the property of their respective owners. PROXMOX  BACKUP SERVER V4.2DATASHEETTape Backup

Web-Based Management Interface

 D Native tape support fully integrated into

Proxmox Backup Server.

 D Supports LTO-5 and later (with best-effort

support for LTO-4).

 D Tape backup/restore jobs.
 D Flexible retention policies.
 D New user space tape driver (in Rust).
 D Support for various tape autoloaders (pmtx-tool).
 D Proxmox LTO Barcode Label Generator for

organizing your tape library.

S3-compatible object storage
 D Monitor request counts and traffic statistics for S3-
backed datastores, with configurable thresholds
and notifications.   N E W

 D Native support for S3-compatible object storage as

backend for backups.

 D Move backup groups and namespaces within the
same datastore with per-group locking for data
consistency.   N E W

 D Intuitive, integrated, web-based user interface.
 D Available in multiple languages.
 D Create and manage datastores.
 D Administer removable datastores.
 D Organize datastores into namespaces.
 D Browse and restore backups.
 D Get an overview of performance, backup tasks,

and usage statistics.

 D Integrated HTML documentation.
 D Access to a secure HTML5 console.
 D Full integration of the ACME protocol, manage TLS
certificates from Let’s Encrypt and other providers,
optionally with external account binding (EAB).
 D Manage network configuration and interfaces.
 D Configure users, access permissions, remote

 D Access public and private cloud environments for

stores and subscriptions.

storing backup data.

Modern Linux Server Experience
 D Flexible notification system: rule-based

notifications sent as email via local Postfix MTA or
authenticated SMTP, or sent via a Gotify instance.

 D Webhooks for the notification system enable
system events to trigger HTTP requests.

 D Secure boot compatibility.
 D Automated and unattended installation for full
automation of the setup process on bare-metal
machines.

 D Support for external metric server.

 D Check for updates and perform upgrades.
 D Configure and schedule network bandwidth

limits, to avoid network saturation.

 D Record and render markdown-formatted

notes on the server.

Command Line Interface (CLI)
 D Manage all components of your server.
 D Intelligent tab completion.
 D Full UNIX man page documentation.

REST API
 D Easy integration for 3rd party management tools.
 D Simple, human-readable data format

(JSON as primary data format).

 D Endpoints available for most server

management tasks.

4/5© 2026 Proxmox Server Solutions. All rights reserved. All trademarks are the property of their respective owners. PROXMOX  BACKUP SERVER V4.2DATASHEETL E A R N   M O R E

Project Page: pbs.proxmox.com
Bugtracker: bugzilla.proxmox.com
Code repository: git.proxmox.com

H O W   T O   B U Y

Visit the Proxmox Online Shop to purchase a subscription: shop.proxmox.com
Find an authorized reseller in your area: www.proxmox.com/partners/explore

H E L P   A N D   S U P P O R T

Proxmox Customer Portal: my.proxmox.com
Community Support Forum: forum.proxmox.com

S A L E S
I N Q U I R I E S ?

Please contact our team:
sales@proxmox.com.

A B O U T   P R O X M O X

Proxmox Server Solutions GmbH is a software provider dedicated to developing powerful and efficient open-source
server solutions. The privately held company is based in Vienna (Europe).

Proxmox Server Solutions GmbH

Bräuhausgasse 37, 1050 Vienna, Austria
office@proxmox.com, www.proxmox.com

© 2026 Proxmox Server Solutions. All rights reserved. All trademarks are the property of their respective owners.

5 / 5

5/5© 2026 Proxmox Server Solutions. All rights reserved. All trademarks are the property of their respective owners. PROXMOX  BACKUP SERVER V4.2DATASHEET
