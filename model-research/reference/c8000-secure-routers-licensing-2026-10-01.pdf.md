# c8000-secure-routers-licensing-2026-10-01.pdf — extracted text

- Source PDF: [c8000-secure-routers-licensing-2026-10-01.pdf](c8000-secure-routers-licensing-2026-10-01.pdf)
- PDF title metadata: Cisco 8000 Series Secure Routers Licensing
- Publisher: Cisco (as registered in the research source entries).
- Source SHA-256: `02f28234bbb1dc7c43cc790892191be82282260cdfdd82999fc040cf11d02ef5`
- Converted: 2026-10-31 (UTC).
- Extraction tool: `pdftotext version 25.03.0`.
- Command: `pdftotext -layout -enc UTF-8 reference/c8000-secure-routers-licensing-2026-10-01.pdf -`.
- PDF pages: 18; page headings below use PDF page numbers.
- Language: English; no OCR or translation performed.
- Source access date and document revision: see the original source-register entries below; conversion does not update them.
- Source register: [C8375-LIC-1](../research-cisco-c8375-e-g2-r1.1.0.md#c8375-lic-1).

> This is layout-preserving plain-text extraction wrapped in Markdown,
> not a semantic reconstruction of tables. Fixed-width text blocks preserve
> column spacing, but reading order, merged cells, and glyphs can still be
> imperfect. Images, diagrams, and image-based tick marks are not transcribed.
> Verify consequential table values against the linked original PDF.

## PDF page 1

```text
Revised: October 1, 2026


Cisco 8000 Series Secure Routers Licensing

Scope of this document
The Cisco 8000 Series Secure Routers offer a networking experience that combines security, routing, and SD-WAN capabilities into
a unified platform. These platforms operate in autonomous routing mode, SD-Routing mode, and SD-WAN controller mode.
This document provides information about licensing for all Cisco 8000 Series Secure Routers, covering essential concepts, required
configurations, and license assignment. The information in this document covers licensing in the context of autonomous mode.
Licenses for SD-Routing and SD-WAN devices are assigned and managed in Cisco Catalyst SD-WAN Manager.
   • For information on assigning SD-Routing licenses, see Assign Licenses to SD-Routing Devices.
   • For information on assigning SD-WAN licenses, see Assign Licenses to Devices, Cisco Catalyst SD-WAN Manager.




What's new and changed
Feature history table
This table provides a summary of license related changes applicable to the Cisco 8000 Series Secure Routers. These features are
available in all the releases subsequent to the one they were introduced in, unless noted otherwise.

Feature name                Release                Feature information

Support for additional      Cisco IOS XE 26.2.x Support for platform-based licensing was introduced for these platforms:
platforms
                                                      • C8211-G2
                                                      • C8255-G2-UCSXE




                                                                                                                                  1
```

## PDF page 2

```text
Feature name             Release               Feature information

Support for additional   Cisco IOS XE 26.1.x Support for platform-based licensing was introduced for these platforms:
platforms
                                                  • C8130-VAI-G2
                                                  • C8130-VAP-G2
                                                  • C8130H-G2
                                                  • C8131-G2
                                                  • C8151-CVAI-G2
                                                  • C8151-CVAP-G2
                                                  • C8151H-C-G2
                                                  • C8221-G2
                                                  • C8221L-G2
                                                  • C8225-G2
                                                  • C8650-G2

Day-0 Enforcement        Cisco IOS XE          Day-0 Enforcement refers to the immediate enforcement action taken on devices
                         17.18.1a              that are unlicensed from the moment they are deployed or when a software image
                                               is updated. With this functionality, unlicensed devices may have restricted
                                               functionality or be blocked from operating until they are properly licensed and
                                               authorized.
                                               All the Cisco 8000 Series Secure Routers support Day-0 Enforcement from
                                               Cisco IOS XE 17.18.1a release.

Support for additional   Cisco IOS XE          Support for platform-based licensing was introduced for these platforms:
platforms                17.18.1a
                                                  • C8130-G2
                                                  • C8140-G2
                                                  • C8151-G2
                                                  • C8161-G2
                                                  • C8231-G2
                                                  • C8235-G2
                                                  • C8355-G2
                                                  • C8550-G2
                                                  • C8570-G2

                                                  • C8231-E-G2
                                                  • C8235-E-G2




2
```

## PDF page 3

```text
Feature name                Release                 Feature information

Platform-Based Licensing Cisco IOS XE               Support for platform-based licensing was introduced on Cisco 8000 Series Secure
                         17.15.3a                   Routers: C8375-E-G2, C8455-G2, C8475-G2, C8550-G2, C8570-G2.
                                                    Platform-based licensing is a way of grouping licenses and devices based on
                                                    platform-classes. A platform class is a hierarchical categorization based on
                                                    product family and place in the network.



Before you begin
Before you install and manage your Cisco 8000 Series Secure Router licenses, ensure:
   • You have set up your Smart Account and one or more Virtual Accounts to manage your assets such as licenses and devices. To
     learn more about Smart Accounts and how to set them up, see Cisco Software: Smart Account Creation and Setup and How to
     Create a Smart Account. Smart Account and Virtual Accounts are required to view and manage your licenses through the Cisco
     SSM portal.
   • You have purchased the Cisco 8000 Series Secure Router of your choice. For information on ordering, see the Cisco 8000 Series
     Secure Routers Ordering Guide.
   • You are using Cisco IOS XE software, version 17.15.3 or later.



Platform-Based licensing
Cisco 8000 Series Secure Routers support a Platform-based licensing model that offers simplification and flexibility. This section
outlines some of the features of this licensing model.
   • Licenses and devices are grouped by platform-class. The platform-class provides a hierarchical categorization based on the
     product family and the device's role within the network. This central concept gives platform-based licensing its name. The
     licenses are not associated with a bandwidth tier.
   • This licensing model supports license portability across devices within the same platform-class. For example, you can use a
     license for C8455-G2, which can also be used on a C8475-G2 platform.
   • This licensing model also allows you to use the same license in different modes. For example, you can use an SD-WAN license
     while operating in SD-Routing mode.
   • A High Security license, also referred to as a HSEC or a HSECK9 license, is not applicable and is not required for Cisco 8000
     Series Secure Routers.

For a general overview on Cisco Licensing, go to https://cisco.com/go/licensingguide.


Available licenses
Cisco 8000 Series Secure Router supports two types of licenses: comes preloaded with Cisco Routing OS Essentials, an embedded
operating system software that delivers fundamental device functionality. You can then choose a subscription license to suit the
specific ways you intend to use your routing device, helping ensure a personalized and efficient solution.
   • Cisco OS Routing licenses: The Cisco OS Routing Essentials license is automatically available with a hardware order. This is
     a perpetual license and is the default license if you don't configure any other license on your device. The OS Essentials license




                                                                                                                                     3
```

## PDF page 4

```text
     is not deposited into your smart account nor do you need to report this license. When your device uses this license, the device
     will limit the aggregated crypto throughput to 250Mbps.
     An OS Advantage license upgrade is also available. When purchased with the hardware configuration, it is factory-preinstalled.
     It can also be ordered separately as a spare for later installation. OS Advantage license provides perpetual access to all Routing
     Advantage features.
    • Subscription-based liceses: These are subscription-based, which means you will have to purchase these licenses for a specific
      term period. The subscription licenses are further classified into several types. Based on your deployment requirements, choose
      an appropriate subscription license.


Subscription-based licenses
The subscription license is further supported in these types for Cisco 8000 Series Secure Routers:
    • Cisco Routing Advantage: This license offers advanced routing capabilities for a traditional routing deployment. This license
      has a 84-month subscription period, and can be used for a device in autonomous mode or SD-Routing mode.
    • WAN-Essentials: These are subscription-only licenses that are available as a part of Cisco Networking Subscription, and have
      a minimum term period of 36 months. These licenses can be used for devices in SD-Routing mode or SD-WAN mode.
    • WAN-Advantage: These are subscription-only licenses that are available as a part of Cisco Networking Subscription and have
      a minimum subscription term period of 36 months. These licenses can be used for devices in SD-Routing mode or SD-WAN
      mode.

For a full list of the features supported in the WAN-Essentials and WAN-Advantage licenses, see Cisco 8000 Series Secure Routers
WAN and Routing License Feature Matrices.

Platform class
A platform class is a hierarchical categorization of devices based on the device's product family and place in the network. Platform
classes are categorized as Small, Medium, Large, or Extra Large based on the throughput, performance, and positioning characteristics
of the underlying hardware platforms.
Knowing the available platform-classes ensures that the correct licenses are purchased and assigned to a device, because the available
licenses are also categorised the same way.
Refer to this table which provides the license type and the platform class that are available for the Cisco 8000 Series Secure Routers.




4
```

## PDF page 5

```text
Platform class and PIDs   License type and license tag - License type and license tag - License type and license tag -
                          autonomous mode                SD-Routing mode                SD-WAN controller mode

Small                     Cisco Routing OS Essentials    Cisco Routing Advantage -      Cisco WAN Essentials -
                                                                                        LIC-CSWAN-S-E
   • C8130-G2*            Cisco Routing Advantage        LIC-ROS-S-A
                                                                                        Cisco WAN Advantage -
   • C8140-G2*            LIC-ROS-S-A                    Cisco WAN Essentials -
                                                                                        LIC-CSWAN-S-A
                                                         LIC-CSWAN-S-E
   • C8130-VAI-G2*
                                                         Cisco WAN Advantage -
   • C8130-VAP-G2*                                       LIC-CSWAN-S-A
   • C8130H-G2*
   • C8151-G2
   • C8161-G2
   • C8131-G2
   • C8151-CVAI-G2
   • C8151-CVAP-G2
   • C8151H-C-G2

Medium                    Cisco Routing OS Essentials    Cisco Routing Advantage -      Cisco WAN Essentials -
                                                                                        LIC-CSWAN-M-E
   • C8211-G2             Cisco Routing Advantage        LIC-ROS-M-A
                                                                                        Cisco WAN Advantage -
   • C8221-G2             LIC-ROS-M-A                    Cisco WAN Essentials -
                                                                                        LIC-CSWAN-M-A
                                                         LIC-CSWAN-M-E
   • C8221L-G2
                                                         Cisco WAN Advantage -
   • C8225-G2                                            LIC-CSWAN-M-A
   • C8231-G2
   • C8235-G2
   • C8231-E-G2
   • C8235-E-G2
   • C8255-G2-UCSXE

Large                     Cisco Routing OS Essentials    Cisco Routing Advantage -      Cisco WAN Essentials -
                                                                                        LIC-CSWAN-L-E
   • C8355-G2             Cisco Routing Advantage        LIC-ROS-L-A
                                                                                        Cisco WAN Advantage -
   • C8375-E-G2           LIC-ROS-L-A                    Cisco WAN Essentials -
                                                                                        LIC-CSWAN-L-A
                                                         LIC-CSWAN-L-E
                                                         Cisco WAN Advantage -
                                                         LIC-CSWAN-L-A




                                                                                                                     5
```

## PDF page 6

```text
Platform class and PIDs          License type and license tag - License type and license tag - License type and license tag -
                                 autonomous mode                SD-Routing mode                SD-WAN controller mode

Xlarge                           Cisco Routing OS Essentials       Cisco Routing Advantage -        Cisco WAN Essentials -
                                                                                                    LIC-CSWAN-XL-E
    • C8455-G2                   Cisco Routing Advantage           LIC-ROS-XL-A
                                                                                                    Cisco WAN Advantage -
    • C8475-G2                   LIC-ROS-XL-A                      Cisco WAN Essentials -
                                                                                                    LIC-CSWAN-XL-A
                                                                   LIC-CSWAN-XL-E
    • C8550-G2
                                                                   Cisco WAN Advantage -
    • C8570-G2                                                     LIC-CSWAN-XL-A

2Xlarge                          Cisco Routing OS Essentials       Cisco Routing Advantage -        Cisco WAN Essentials -
                                                                                                    LIC-CSWAN-2XL-E
    • C8650-G2                   Cisco Routing Advantage           LIC-ROS-2XL-A
                                                                                                    Cisco WAN Advantage -
                                 LIC-ROS-2XL-A                     Cisco WAN Essentials -
                                                                                                    LIC-CSWAN-2XL-A
                                                                   LIC-CSWAN-2XL-E
                                                                   Cisco WAN Advantage -
                                                                   LIC-CSWAN-2XL-A

* SD-WAN support starts from IOS XE 26.2.1 release onwards.


Configure a license for a routing device
Follow these steps to configure a boot level license. This task applies only for Cisco 8000 Series Secure Routers running in the
autonomous mode.
Device# show version
<output truncated>
Router operating mode: Autonomous

When you order a new Cisco 8000 Series Secure Router, an OS Essentials license is included along with the hardware regardless of
the license type or tier you have purchased. When you boot the device, the default OS Essentials license comes up and the aggregated
crypto throughput is limited to 250 Mbps.
If you have purchased a Cisco Routing Advantage license or a Cisco WAN Advantage license, perform these steps to modify the
boot level license to Advantage.
Ensure a positive balance of the required licenses in Cisco SSM.

Step 1      enable
            Enables privileged EXEC mode. Enter your password, if prompted.

Step 2      configure terminal
            Enters global configuration mode.
            Example:
            Device# configure terminal

Step 3      license boot level advantage
            Configures the boot level license to Advantage.




6
```

## PDF page 7

```text
         Example:
         Device(config)# license boot level advantage
         % use 'write' command to make license boot config take effect on next boot


Step 4   exit
         Exits global configuration mode and returns to privileged EXEC mode.
         Example:
         Device# exit


Step 5   write running-config startup-config
         Saves the changes in the configuration file.
         Example:
         Device# copy running-config startup-config
         Destination filename [startup-config]?
         Building configuration...
         [OK]
         <output truncated>

Step 6   reload
         Reloads the device. After the device starts, for a device running on Cisco IOS XE 17.18.1a or later, the device communicates
         with Cisco SSM to check whether you have the required licenses for the Advantage tier and whether your license is
         AUTHORIZED. Once the device receives acknowledgement from Cisco SSM, throughput throttling is lifted and the
         throughput becomes unthrottled.
         If the license is not authorized, the throughput stays at 250 Mbps.
         To know how to connect the device with Cisco SSM, see Connect your device to Cisco SSM, on page 8.
         To learn more about license authorization and license enforcement behavior, see Day-0 Enforcement.
         Example:
         Device# reload
         Proceed with reload? [confirm]

         %SYS-5-RELOAD: Reload requested by console.
         Reload Reason: Reload Command.
         <output truncated>

         <output truncated>

         If you use Cisco IOS XE 17.15.x, after the reload, the device starts with the routing-Advantage license and crypto
         throughput is unthrottled.

Step 7   show version
         Displays the currently configured boot level license.
         This sample output that confirms that the Routing Advantage license is configured.
         Example:
         Device# show version
         <output truncated>

         License Type: is subscription
         License Level: advantage




                                                                                                                                   7
```

## PDF page 8

```text
            Next reload license Level: advantage
            The current crypto throughput level is unthrottled

            <output truncated>

Step 8      show license summary
            Displays a summary of license usage, which includes information about the licenses being used, the count, and the license
            status.
            Example:
            Device#show license summary
            License Reservation is ENABLED

            Account Information:
              Smart Account: <none>
              Virtual Account: <none>

            License Usage:
              License                 Entitlement Tag               Count Status
              -----------------------------------------------------------------------------
              Routing Advantage fo... (C8K_LARGE_ROUTING_A)             1 AUTHORIZED



            See this example where the license is not authorized.
            Device#show license summary
            Account Information:
              Smart Account: <none>
              Virtual Account: <none>

            License Usage:
              License                 Entitlement Tag               Count Status
              -----------------------------------------------------------------------------
              advantage               (C8K_LARGE_ROUTING_A)             1 PENDING

What's next
Complete usage reporting, if required. This licensing uses the Smart Licensing Using Policy infrastructure for license reporting.


Connect your device to Cisco SSM
Cisco Smart Software Manager (Cisco SSM) is the primary licensing server and portal where you can create your smart accounts
and manage licenses. After configuring a device license, connect your device to Cisco SSM to authorize the license and report license
usage. To do this, use the Smart Licensing Using Policy licensing policy.

Smart Licensing Using Policy
Smart Licensing Using Policy is a licensing solution that simplifies license management and reporting for network devices, including
Cisco 8000 Series Secure Routers. This solution enables a compliance relationship between a device and the Cisco Smart Software
Manager (Cisco SSM) cloud to account for hardware and software licenses that are configured and in use.
Smart Licensing Using Policy is based on predefined policies associated with a smart account. These policies determine how often
and under what conditions devices need to report their software license usage.
The policy sets the initial reporting requirements for:
    • new licenses,




8
```

## PDF page 9

```text
   • ongoing report acknowledgment protocols, and
   • intervals at which usage reports must be submitted to maintain license compliance.

Depending on the network requirements and security policy, the connection to Cisco SSM can be a direct connection over the internet,
mediated, or offline for air-gapped networks.

How Smart Licensing Using Policy deployments work

Summary
This section describes the various ways in which Smart Licensing Using Policy is used to connect a device to Cisco SSM. The
workflow also specifies how to deploy Smart Licensing Using Policy and the components involved.

Components of Smart Licensing Using Policy
All possible components involved in an implementation of Smart Licensing Using Policy are listed here, along with a brief description
of the component’s role in the implementation. Out of all these components, the product instance and Cisco SSM are a part of all the
deployments.
   • Product instance: In this document, a product instance refers to the Cisco 8000 Series Secure router, identified by a Unique
     Device Identifier (UDI). The product instance records and reports license usage (RUM reports) and provides alerts and system
     messages about overdue reports and communication failures. It securely stores RUM reports and usage data.
   • Cisco SSM: Cisco SSM is a portal that enables license management for all Cisco software licenses from a centralized location.
     Cisco SSM helps you manage current requirements and review usage trends to plan for future license requirements. Access the
     Cisco SSM Web UI from https://software.cisco.com. To manage your licenses, navigate to Smart Software Manager > Manage
     Licenses.
   • Cisco SSM (On-Prem): Cisco SSM (On-Prem) is locally connected and acts as a local license authority. Set up a Cisco SSM
     On-Prem license server, which periodically synchronizes its license database with Cisco SSM and functions in a similar way.
   • Cisco Smart License Utility (CSLU): CSLU is a Windows-based reporting utility that provides aggregate licensing workflows.
     This utility performs these key functions:
        • Provides options relating to how workflows are triggered. The workflows can be triggered by CSLU or by the product
          instance.
        • Collects usage reports from the product instance and uploads these usage reports to the corresponding Smart Account or
          Virtual Account – online, or offline, using files. Similarly, the RUM report ACK is collected online, or offline, and sent
          back to the product instance.

     CSLU can be integrated into the Smart Licensing Using Policy implementation in several ways. It can be used as a standalone
     Windows application that is either connected to or disconnected from Cisco SSM. Alternatively, you can deploy it on a Linux
     machine, such as a laptop or desktop. Cisco can also embed CSLU in a controller, such as Cisco Catalyst Center.


Workflow
To establish trust between the device and Cisco SSM, select one of the deployment methods mentioned in this table to deploy Smart
Licensing Using Policy.




                                                                                                                                       9
```

## PDF page 10

```text
      Smart License Using Policy Description                                                           Link to the detailed workflow
      deployment type

1.    On-Premises deployments       This deployment option enables you to manage your software Cisco SSM On-Prem
                                    licenses locally without direct communication with Cisco SSM deployment
                                    over the internet.
                                                                                                    Connected to Cisco SSM
                                    This type of deployment involves the use of either a license    through CSLU
                                    server, such as Smart Software Manager (SSM), or a Windows
                                    application, such as Cisco Smart License Utility (CSLU), on the
                                    premises to manage devices and licenses. These tools use a
                                    synchronization process to exchange license information with
                                    Cisco SSM which can be done automatically over the network
                                    or manually offline.
                                    These are the on-Premises deployments:
                                        • Cisco SSM On-Prem
                                        • CSLU

      Direct deployments            Direct deployment involves connecting devices to Cisco through Connected directly to Cisco
                                    the internet or an HTTP proxy server to report usage information SSM
                                    using the Smart transport mode. Direct deployment works out
                                    of the box with no additional configuration.
                                    This deployment option is ideal when you do not want to manage
                                    an on-premises server and want the device to communicate with
                                    Cisco directly or through a proxy.

      Offline deployments           Offline deployment is a type of smart licensing deployment that Specific License Reservation,
                                                                                                    on page 14
                                       • allows devices to be set up without internet access
                                        • does not require communication with Cisco, and
                                        • is used in highly secure environments.




Day-0 Enforcement
Day-0 Enforcement in licensing refers to the immediate enforcement action taken on devices that are unlicensed from the moment
they are deployed or when a software image is updated. This means that unlicensed devices may have restricted functionality or be
blocked from operating until they are properly licensed. This enforcement ensures that devices without proper licenses face enforcement
actions at deployment or during upgrades.

Support for Day-0 Enforcement
This list specifies the release from which Day-0 is supported for the various operating modes.
     • Autonomous mode: Starting with Cisco IOS XE 17.18.1a release, the Day-0 Enforcement functionality is supported for all the
       Cisco 8000 Series Secure routers operating in autonomous mode.
      If you use the hardware with Cisco IOS XE 17.15.3, Day-0 Enforcement does not apply.




10
```

## PDF page 11

```text
   • SD-Routing and SD-WAN modes: In these modes, the Cisco Catalyst SD-WAN Manager manages all the licenses. Note that a
     license must be attached to a device before you can onboard the device. To learn more about license management and enforcement
     for SD-WAN and SD-Routing modes, see Deploying Smart Licensing Using Policy in Cisco Catalyst SD-WAN.

See details about Day-0 Enforcement for autonomous devices in this document.

Licensing reporting and Day-0 Enforcement
Day-0 Enforcement is based on the Smart Licensing Using Policy infrastructure and is applied at a device level. After you configure
the boot level and install your license, you should be able to use the features associated with your license. The next step is to monitor
your license usage to account for or report the licenses that you use, to Cisco.
For this, you must send a Resource Utilization Measurement (RUM) report to Cisco SSM through direct connection mode, offline
mode, CSLU mode, or an on-prem mode. Based on the response from Cisco SSM, the license status and subsequent actions are
decided.

Prerequisites
This section provides the list of requirements for the Day-0 Enforcement functionality to work as intended.
   • Your device must be a part of the Cisco 8000 Series Secure router family.
   • A minimum of Cisco IOS XE 17.18.1 release must be installed for autonomous devices.
   • A valid license must be configured in your device.


Determining the compliance status of a device

Summary
To determine whether a device is in compliance or is out of compliance, see this process flow.

Workflow
1. A device requests a license.
2. The Smart Agent on the device checks if the device has an SLR code that includes the license. If yes, the device is marked as
   compliant.
3. If no SLR code is found, the device sends a license request to Cisco SSM, CSLU, or the on-prem manager and waits for a response.
   After receiving the compliance status—in-compliance or out-of-compliance—the license status of the device changes to
   AUTHORIZED or Out Of Compliance.

     Note

For autonomous mode devices, the device oversees license consumption and usage reports. License enforcement occurs on the
device side.



View the license status of a device
This task specifies the steps to view the current license level and status at a device level. The license status, in turn, determines the
enforcement behavior and the throughput throttling.




                                                                                                                                       11
```

## PDF page 12

```text
Step 1        Run the show license summary command.
              Example:
              Device# show license summary
              License Usage:
                License                 Entitlement Tag               Count Status
                -----------------------------------------------------------------------------
                advantage               (C8K_SMALL_ROUTING_A)            1 AUTHORIZED

              In the Status field, one of these options is displayed.
                  • IN USE: The entitlement is in use as intended.
                  • NOT IN USE: The entitlement is not in use, which may occur when the device has SLR code installed but is not
                    using it. For example, the SLR code may have Advantage tier, but the OS-level license is configured at the Essentials
                    tier.
                  • PENDING: When a license is in use but no status has been received from Cisco SSM or On-Prem.
                  • AUTHORIZED: When a device receives an authorized status for this tag.
                  • OUT OF COMPLIANCE: When a device consumes a license that the Smart Account is not entitled to. For example,
                    when the Smart Account that the device is registered to does not have the requested license available.
                  • NOT AUTHORIZED: This status appears when a license tag is in use but is not permitted. For example, it may
                    occur when SLR is in use and the authorization code is removed while an entitlement is active.

                          If you purchase a Routing-Advantage or WAN-Advantage license, the license status must be AUTHORIZED
                          for the throughput to change to unthrottled after you modify the license boot level to advantage.
              Note

Step 2        To view the throughput for your device, run the show platform hardware throughput crypto command.
              Example:
              Device# show platform hardware throughput crypto
              Crypto Throughput will not be rate limited
              Current boot level is advantage
              Platform is SD-Routing config capable.
              Current mode is autonomous
              Device Enforcement Mode:
               PID:C8161-G2,SN:FCW2833Y14D: Day-0



Day-0 Enforcement
After the Smart Agent determines the license status, if a device is found to be out-of-compliant, Day-0 Enforcement is applied.
This table lists the possible license status and the resulting enforcement for devices.

Table 1: Day-0 Enforcement behavior


License status                                                          Day-0 Enforcement behavior

Licensed with Advantage                                                 When boot level Advantage is configured, and no Routing
                                                                        Advantage license is available in the Smart Account, then the
                                                                        throughput is kept at the default value of 250 Mbps.
                                                                        When boot level Advantage is configured and the Routing
                                                                        Advantage license is authorized, the throughput is unthrottled.




12
```

## PDF page 13

```text
License status                                                      Day-0 Enforcement behavior

Licensed with Essentials                                            Your device comes with a default Essentials license. Your device
                                                                    boots in Essentials mode by default, and throughput is set to a
                                                                    value of 250Mbps.


Day-0 Enforcement and other considerations

Specific License Reservation
For use cases that cannot establish a connection with Cisco SSM, and where you have purhcased a Routing Advantage license, provide
your Smart Account information at the time of hardware purchase. If the Smart Account indicates that SLR pre-installation required,
manufactory installs the SLR code on the device and the device is licensed immediately. The device starts in the Day-0 state and you
must activate the licenses for the licenses to get to the Day-N state. To know how to enable and activate licenses in SLR mode, see
Specific License Reservation, on page 14.

Factory reset
If you run the factory reset keep-license-info command on your device, all the license related information is retained. This command
resets everything else except the licenses on the device. The Day-0 enforcement continues to function as expected.
If you run the factory reset all command, the Smart License trusted store is cleaned up, and all the information about the Smart
Licensing is erased. In this scenario, the Day-0 flag and is reset. It is recommended you run this command when you want to RMA
the device or you want to decommission the device.

High availability
For platforms that support the high availability functionality, the license UDI uses the chassis serial number. However, the trusted
store is located on each route processor. For all Smart Agent related information that is saved in the license trusted store, the Smart
Agent synchronizes to the standby route processor.

Device mode change
When you modify the device mode from autonomous mode to SD-WAN mode, a reload is required and the device does not consume
any license after the reload. The device will set the throughput to unthrottled.
When you modify the device mode from autonomous mode to SD-routing mode, a reload is not required. Throughput is unthrottled,
and the device will release current license when the connection to vManage is established.
If your device had SLR code installed, the device will not return the SLR code automatically. You must manually return the SLR
code with by running the license smart reservation return command. Then, follow the SLR return procedure to release the license.

Day-0 Enforcement after an upgrade
If you upgrade your device to Cisco IOS XE 17.18.1a or later, Day-0 Enforcement behavior is listed here.

License in older version          Throughput before upgrade         Day-0 state after the upgrade Throughput after the upgrade

Essentials                        Unthrottled                       Day-0                             250 Mbps

Advantage                         Unthrottled                       Day-N                             Unthrottled




                                                                                                                                     13
```

## PDF page 14

```text
Specific License Reservation
Specific License Reservation (SLR) is a solution specifically designed for classified environments where electronic communication
is restricted. In such environments, routers are unable to communicate directly with the Cisco SSM or through Cisco SSM On-Prem.
SLR enables the use of all entitlements on the router without the need for communication with Cisco. This functionality is especially
used in highly secure networks, and it is supported on platforms that support Day-0 Enforcement.
With SLR, a device generates a request code that is entered into Cisco SSM to get an authorization code. This process reserves a
specific software license directly onto the device's unique identifier (UDI) without needing constant internet connectivity for usage
reporting, making it ideal for highly secure, air-gapped networks. Once the authorization code is installed on the device, the license
is effectively reserved, remaining in place until it is explicitly released by the device by using a return code.

Summary
To enable SLR for your device, here are the high-level steps.

Workflow
1. Configure the Specific License Reservation feature by using the license smart reservation command.
2. Enable Specific License Reservation on the device by using the license smart transport off command.
3. Reserve your licenses and generate an authorization code from the Cisco SSM Web UI.
4. Register the device using the authorization code by using the license smart reservation install file bootflash:file-name command.

     Note

If the Smart Account indicates that SLR pre-installation is required, manufactory installs the SLR code on the device and the device
is licensed immediately. The device starts in the Day-0 state and you must activate the licenses for the licenses to get to the Day-N
state.



Enable Specific License Reservation
Perform this task to enable SLR for your device.
Before you begin
To enable SLR, you must have the necessary approval and authorization from Cisco. For assistance, go to www.cisco.com/go/scm
or contact your account.

Step 1      enable
            Example:
            Device> enable

            Enables privileged EXEC mode. Enter your password, if prompted.

Step 2      configure terminal
            Example:
            Device# configure terminal

            Enters global configuration mode.




14
```

## PDF page 15

```text
Step 3      Run the show license summary, show run | inc license, and show lice tech sup | inc INSTALL commands to view the
            license details before SLR is enabled.
            Example:
            Device#show license summary
            Account Information:
              Smart Account: <none>
              Virtual Account: <none>

            License Usage:
              License                 Entitlement Tag               Count Status
              -----------------------------------------------------------------------------
              advantage               (C8K_LARGE_ROUTING_A)             1 PENDING


            Device# show run | inc license
            license udi pid C8375-E-G2 sn FDO2819M0BF
            license boot level advantage

            Device# show lice tech sup | inc INSTALL
                Reservation status: NOT INSTALLED
            (Device# show license tech support | inc Day-
              Day-0 Verification: YES
              PID:C8375-E-G2,SN:FDO2819M0BF: Day-0

            Note that the license status is PENDING and the Reservation Status displays NOT INSTALLED.

Step 4      license smart reservation
            Example:
            Device(config)# license smart reservation

            Enables Specific License Reservation.


Generate an authorization code
Perform these steps to generate an authorization code.
Before you begin
Configure the boot level license for the device. To know how to do this, see Configure a license for a routing device, on page 6

Step 1      enable
            Example:
            Device> enable

            Enables privileged EXEC mode. Enter your password, if prompted.

Step 2      license smart reservation request local
            Example:
            Device# license smart reservation request local
            Enter this request code in the Cisco Smart Software Manager portal:
            UDI: PID:C8375-E-G2,SN:FDO2819M0BF
                Request code: DC-ZC8375-E-G2:FDO2819M0BF-AmwW2cqDa-EF

            Generates a request code for the active device that needs to be entered in Cisco SSM.




                                                                                                                                   15
```

## PDF page 16

```text
Reserve licenses in Cisco SSM
Perform these steps to reserve licenses in Cisco SSM for SLR.

Step 1      Log in to the Cisco SSM portal and choose Manage Licenses.
Step 2      Click Inventory.
Step 3      From the Virtual Account drop-down list, choose your Virtual Account.
Step 4      Choose the Licenses tab, and click License Reservation.
            In the Smart License Reservation pop-up window, the Enter Request Code option is selected by default.

Step 5      In the Reservation Request Code field, enter the request code that you previously generated and click Next.
Step 6      In the Select Licenses window, select the Reserve a specific license check-box and enter 1 in the Quantity to Reserve
            field.
Step 7      Review and confirm the license reservation and click Generate Authorization Code.
            After the authorization code is generated, click Copy to Clipboard to copy the code, or click Download as File to
            download the file and save it to the Flash drive or TFTP server.


Install the authorization code in the device
Perform these steps to install the authorization code you obtained from Cisco SSM in the device to authorize the license.
Before you begin
Ensure you generated the authorization code in Cisco SSM.

Step 1      enable
            Example:
            Device> enable

            Enables privileged EXEC mode. Enter your password, if prompted.

Step 2      license smart reservation install file {flash:filename | tftp://filepath}
            Example:
            Device#license smart reservation install file bootflash:slr
            Reservation install file successful
            Last Confirmation code UDI: PID:C8375-E-G2,SN:FDO2819M0BF
                Confirmation code: 99070266

            Loads the authorization code either from the Flash drive or the TFTP server and installs the authorization code in the
            device device to authorize the license.

Step 3      show license reservation
            Verifies whether the authorization code is installed properly.
            Example:
            Device# show license reservation
            Last Data Push: <none>
            Last File Export: <none>

            Overall status:
              Active: PID:C8375-E-G2,SN:FDO2819M0BF




16
```

## PDF page 17

```text
                Status: SPECIFIC INSTALLED on Oct 01 19:02:37 2025 UTC
                Last Confirmation code: ed558ef0

           Specified license reservations:
             Routing Advantage for C8000 Secure Router, Large (C8K_LARGE_ROUTING_A):
              Description: Routing Advantage License for Cisco 8000 Series Secure Router Large Class of Platforms

                Total reserved count: 1
                Enforcement type: CONDITIONALLY-ENFORCED
                Term information:
                  Active: PID:C8375-E-G2,SN:FDO2819M0BF
                    Authorization type: SPECIFIC INSTALLED on Oct 01 19:02:37 2025 UTC
                    License type: TERM
                      Start Date: 2024-NOV-08 UTC
                      End Date: 2026-OCT-09 UTC
                      Term Count: 1



Verify Specific License Reservation
Run the show commands specified in this task to verify that SLR is enabled and device is authorized.

Step 1     Run the show license summary command.
           Example:
           Device#show license summary
           License Reservation is ENABLED

           Account Information:
             Smart Account: <none>
             Virtual Account: <none>

           License Usage:
             License                 Entitlement Tag               Count Status
             -----------------------------------------------------------------------------
             Routing Advantage fo... (C8K_LARGE_ROUTING_A)             1 AUTHORIZED


           Note that License Reservation is ENABLED. Further, the license status is AUTHORIZED.

Step 2     Run the show license tech support | section Device command to verify the device enforcement state.
           Example:

           Device#show license tech support | section Device
           Device Enforcement State:
             PID:C8375-E-G2,SN:FDO2819M0BF: Day-N

           Once the license is athorized, the license enters the Day-N status.


Remove SLR from device
Remove SLR from a device using the procedure described here.

Step 1     enable
           Example:
           Device> enable

           Enables privileged EXEC mode. Enter your password, if prompted.




                                                                                                                17
```

## PDF page 18

```text
Step 2   license smart reservation return local
         Example:
         Device#license smart reservation return local
         This command will remove the license authorization code. Some features may not function properly.

         Do you want to continue? [yes/no]: yes
         Enter this return code in Cisco Smart Software Manager portal:
         UDI: PID:C8375-E-G2,SN:FDO2819M0BF
             Return code: Djr94X-iREP3e-cR55Pi-PZtCiK-hzGhN2-kpEqFd-oFw937-aHZD6z-Nap
         *Feb 2 19:06:11.800: %SMART_LIC-6-RESERVE_RETURNED: Specific License Reservation returned for udi
         PID:C8375-E-G2,SN:FDO2819M0BF. Smart Agent is now unregistered.
         *Feb 2 19:06:12.800: %SMART_LIC-3-OUT_OF_COMPLIANCE: One or more entitlements are out of compliance


         The system removes the license authorization code from the device and generates a unique return code. You must use
         this return code in Cisco SSM to de-register the license, making it available in your virtual account.

Step 3   Log in to the Cisco SSM Portal and navigate to Inventory.
Step 4   From the Virtual-Account drop-down list, choose your Virtual Account.
Step 5   Select the Product Instances tab and select the required product instance from the product instances list.
Step 6   From the Actions drop-down list, choose Remove.
Step 7   In the Remove Product Instance window, enter the return code in the Reservation Return Code field and click Remove
         Product Instance.
         The reservation information is removed and the license is made available in the virtual account.




18
```
