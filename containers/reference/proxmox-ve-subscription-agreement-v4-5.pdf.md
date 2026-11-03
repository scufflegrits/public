Proxmox Virtual Environment
Subscription Agreement
Proxmox Virtual Environment (Proxmox VE) is a complete open-source platform for enterprise
virtualization. A Proxmox VE subscription is a service program specially designed for IT professionals and
businesses. It helps ensure business continuity by providing access to the stable Proxmox Enterprise-
Repository and optional technical support.
1 Subscription Plans for Proxmox VE
|     | PREMIUM | STANDARD | BASIC | COMMUNITY |
| --- | ------- | -------- | ----- | --------- |
Access to stable Enterprise-
|     | Yes | Yes | Yes | Yes |
| --- | --- | --- | --- | --- |
Repository and regular updates
| Complete feature-set | Yes           | Yes           | Yes           | Yes        |
| -------------------- | ------------- | ------------- | ------------- | ---------- |
| License              | GNU AGPLv3    | GNU AGPLv3    | GNU AGPLv3    | GNU AGPLv3 |
|                      | via Customer  | via Customer  | via Customer  | Community  |
Technical support
|     | Portal | Portal | Portal | support |
| --- | ------ | ------ | ------ | ------- |
Support tickets included Unlimited 10 per year 3 per year None *
|                          | 2 hours** within a  | 4 hours** within a  |                |            |
| ------------------------ | ------------------- | ------------------- | -------------- | ---------- |
| Initial response time    |                     |                     | 1 business day | n/a        |
|                          | business day        | business day        |                |            |
| Remote support (via SSH) | Yes                 | Yes                 | No             | No         |
| Offline key activation   | Yes                 | Yes                 | Contact us     | Contact us |
 Datacenter Manager:
| Enterprise-Repository and  | Yes | Yes | Yes | No  |
| -------------------------- | --- | --- | --- | --- |
support
|     | € 1100 | € 550 | € 370 | € 120 |
| --- | ------ | ----- | ----- | ----- |

Pricing
|     | per year     | per year     | per year     | per year     |
| --- | ------------ | ------------ | ------------ | ------------ |
|     | & CPU-socket | & CPU-socket | & CPU-socket | & CPU-socket |
* Support via public Proxmox support forum
** Guaranteed first response time on critical support requests
© Proxmox Server Solutions GmbH | Vienna (Austria)
Price list valid between January 12, 2026 and January 10, 2027 1/6
office@proxmox.com | www.proxmox.com

Subscription Agreement for Proxmox VE
Note:
• The subscription model is based on the number of physical servers and their CPU sockets.
• In a cluster each node needs a valid subscription. All nodes must have the same subscription level.
• Subscription period is one year (12 months) from purchase date. All prices are net prices in EUR.
VAT will be added, if applicable.
• Technical support for the Premium, Standard, and the Basic Subscription levels is provided via the
web and email-based Proxmox Customer Portal (in English or German) at https://my.proxmox.com
• Technical support for integrations by recognized third-party Solution Providers is limited to Basic,
Standard, and Premium subscribers.
• Community support for the Community Subscription is done via the public Proxmox support
forum at https://forum.proxmox.com
Important note:
(Re-)Distributing Software packages received under this Subscription Agreement to a third party or using
any of the subscription services for the benefit of a third party is a material breach of the agreement, even
if the open-source license applicable to individual software packages may give you the right to distribute
those packages (this limitation is not intended to interfere with your rights under those individual
licenses).
2 Scope of Coverage
A Proxmox VE Subscription includes the following:
• Access to the Proxmox VE Enterprise Repository
• Installation support
• Usage
• Configuration
• Diagnosis
• Bug reports and fixes for packages in the Proxmox VE repository, including Ceph packages
Technical support only covers the latest stable release.
What is not included: We do not support modified packages, third party software, community projects
upon which our releases are based on, code development, system and network design, designing security
rules, backup/recovery strategies, data recovery and high availability design.
Technology previews are not supported in production environments.
© Proxmox Server Solutions GmbH | Vienna (Austria)
Price list valid between January 12, 2026 and January 10, 2027 2/6
office@proxmox.com | www.proxmox.com

Subscription Agreement for Proxmox VE
3 Additional Terms and Conditions
3.1. What is a Proxmox subscription?
A Proxmox subscription provides access to professional support services and is a service program
designed to help IT professionals and businesses keep their Proxmox deployments up-to-date.
3.2. What is the Enterprise Repository?
The Proxmox VE Enterprise Repository is the default, stable, and recommended repository for Proxmox
VE. It is available to all Proxmox VE subscribers, and we recommend using it for your production servers.
3.3. Purchasing and activating a Proxmox VE subscription
The easiest way to order a subscription plan for Proxmox VE is via the Proxmox Online Shop at
https://shop . proxmox .com or via a Proxmox reseller. After your purchase has been confirmed you will
receive a welcome email including the subscription key and all necessary instructions on how to activate
your subscription.
Go to the web interface of Proxmox VE, select the tab “Subscription” – then click “Upload Subscription Key”,
and insert your key. Each subscription key is bound to the unique "Server ID" of your server and is
regularly checked for validity.
3.4. Offline subscription key activation and offline updates
The ‘proxmox-offline-mirror’ tool can be used to manage subscription keys for air-gapped systems or
systems that cannot access the public internet. To use this functionality, you need a subscription key for
Proxmox Offline Mirror itself.
Note: Please reach out to our sales team for details and purchasing options.
Contact: sales@proxmox.com
3.5. How many CPU-sockets does my server have?
To see the number of CPU-sockets of your server go to the web user interface of your Proxmox VE server,
select the node and go to the “Summary” tab – the CPU name and the socket count will be listed there.
3.6. Nested Virtualization
Nested virtualization is when you run a hypervisor, like Proxmox VE or others, inside a virtual machine
(which is of course running on another hypervisor) instead of on real hardware. In other words, you have a
host hypervisor, hosting a guest hypervisor (as a VM), which can hosts its own VMs.
© Proxmox Server Solutions GmbH | Vienna (Austria)
Price list valid between January 12, 2026 and January 10, 2027 3/6
office@proxmox.com | www.proxmox.com

Subscription Agreement for Proxmox VE
Please note, running Proxmox VE in such a nested virtualization setup is not covered by this support
agreement.
3.7. How many subscriptions do I need?
Each of your Proxmox VE servers will need a subscription, containing the right CPU socket count. Each
subscription key is bound to the unique "Server ID" of your server.
3.8. Subscriptions for a Proxmox VE cluster
In a Proxmox VE cluster all nodes need to have the same subscription level.
Example: Consider having a cluster with three nodes, each node has 1 CPU-socket. You want to get a
“Standard Subscription” for your cluster. This means that you need to buy 3 x “Proxmox VE Standard
Subscription 1 CPU/year”.
3.9. How many support tickets do I get in total if I buy two or more
Proxmox VE subscriptions?
Each subscription level includes a certain amount of support tickets (e.g., three support tickets for a Basic
Subscription).
Example: If you run two physical servers with Proxmox VE and you order two Basic Subscriptions (each
subscription containing three support tickets) you will have three tickets for each of your physical servers.
3.10. How do I receive software updates?
Information about new packages is sent via email to the email address of the root account. All updates are
displayed on the web interface, including changelogs (if available). Applying updates via the web interface
is supported.
3.11. Upgrade your subscription level
You can easily upgrade from one subscription level to a higher one during your subscription period. Only
the difference between the two subscription prices will be charged. In case you wish to upgrade, please
open a ticket in the Proxmox Online Shop at https://shop . proxmox .com or contact your reseller.
3.12. Downgrade
Downgrades from a higher level to a lower level of subscription are not possible during the one year
period. But you can cancel your subscription after one year and order a new level.
© Proxmox Server Solutions GmbH | Vienna (Austria)
Price list valid between January 12, 2026 and January 10, 2027 4/6
office@proxmox.com | www.proxmox.com

Subscription Agreement for Proxmox VE
3.13. Server change – moving subscription key to a new server
If you want to move your subscription key to a new server, for example because you have replaced your
hardware, you can reissue your subscription key. This can be done 3 times per year without any costs
involved via the self service portal at https://shop . proxmox .com (or via your reseller). If you need to reissue
a subscription key more often, please open a ticket in the online shop or contact your reseller.
3.14. Renewal and Cancellation
Renewal: A Proxmox Subscription will automatically renew after one year from your initial purchase date.
30 days before the renewal date you will receive a renewal invoice. As renewal rates may be subject to
change, you can cancel the renewal when you receive the renewal invoice.
Cancellation: If you do not want to renew, you need to request a cancellation. Cancel yourself either via
your account on https://shop.proxmox.com, instruct your reseller to do so, or contact the sales team of
the Proxmox Online Shop at https://shop . proxmox .com .
You can cancel your Proxmox Subscription at any time. Your access will continue for the remaining time of
your paid subscription period (billing cycle). Already activated and paid products and services cannot be
refunded.
3.15. Multi-year subscriptions
The default subscription period is one year. When ordering, you can choose the preferred billing cycle: you
can pay for one, two or three years in advance. By doing this, you are protected from the annual price
changes.
3.16. Definition of a critical support request
A critical issue severely impacts the use of the software in a production environment. This includes loss of
data and nonworking production servers. The situation halts the business operations and no procedural
workaround exists.
The ticket priority is subject to change by the support agent at any time. Please always submit your
subscription keys on ticket creation.
3.17. Business hours
The enterprise support team is available on Austrian business days between 7:00 and 17:00 (CET/CEST) -
(7 a.m. to 5 p.m.).
© Proxmox Server Solutions GmbH | Vienna (Austria)
Price list valid between January 12, 2026 and January 10, 2027 5/6
office@proxmox.com | www.proxmox.com

Subscription Agreement for Proxmox VE
3.18. Proxmox VE is open-source software. Why should I pay for it?
Proxmox VE source code is licensed under the GNU Affero General Public License version 3 (AGPLv3)
which means you have the freedom to use the software’s source code. Hence, you do not pay for the
software’s source code (or license); you pay for the subscription support service.
The Proxmox VE subscription service adds real business value to your open-source environment by
providing access to a broad infrastructure of services, like:
• Access to the exclusive Enterprise Repository with stable software updates.
• Enterprise support to resolve your urgent technical requests.
• Access to Proxmox experts via the Customer Portal.
• Flexible subscription plans scalable to your business needs.
3.19. Can I use Proxmox VE without a subscription?
Proxmox VE is open-source software distributed under the GNU AGPLv3. You have the freedom to
download, use, and modify the software for private or business use. So yes, you can. Just be aware that if
you choose to run Proxmox VE without the Enterprise Repository, you may have packages that are not
always heavily tested and validated. We do not recommend using the No-Subscription Repository for
production servers. Read more details at https://pve.proxmox.com/wiki/Package_repositories
3.20. Technical pre-sales support
The best place for pre-sales questions is the Proxmox Support Forum. Or send an email to
office@proxmox.com.
3.21. How many contacts can I register on the Proxmox Customer
Portal?
For each organization/subscription, you can register up to three contact email addresses in the Proxmox
Customer Portal.
Note: The use of email addresses with auto-replies (for example: an email address of a ticket system) is
prohibited to prevent email loops due to automatic replies.
3.22. Is co-terming available?
Yes, co-terming for multiple contracts is available at the time of renewal.
- End of document -
© Proxmox Server Solutions GmbH | Vienna (Austria)
Price list valid between January 12, 2026 and January 10, 2027 6/6
office@proxmox.com | www.proxmox.com