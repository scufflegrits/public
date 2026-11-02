# c8000-edge-licenses-throughput-2026-05-04.pdf — extracted text

- Source PDF: [c8000-edge-licenses-throughput-2026-05-04.pdf](c8000-edge-licenses-throughput-2026-05-04.pdf)
- PDF title metadata: Configure Licenses and Throughput for Catalyst 8000 Series Physical Platforms
- Publisher: Cisco (as registered in the research source entries).
- Source SHA-256: `78455970ac51f29a9ce684317a33d5e325360f1e538809e1011121bb710df21f`
- Converted: 2026-10-31 (UTC).
- Extraction tool: `pdftotext version 25.03.0`.
- Command: `pdftotext -layout -enc UTF-8 reference/c8000-edge-licenses-throughput-2026-05-04.pdf -`.
- PDF pages: 29; page headings below use PDF page numbers.
- Language: English; no OCR or translation performed.
- Source access date and document revision: see the original source-register entries below; conversion does not update them.
- Source register: [C8300-4T2X-LIC-1](../research-cisco-c8300-1n1s-4t2x-r1.1.0.md#c8300-4t2x-lic-1).
- Source register: [C8300-6T-LIC-1](../research-cisco-c8300-1n1s-6t-r1.1.0.md#c8300-6t-lic-1).

> This is layout-preserving plain-text extraction wrapped in Markdown,
> not a semantic reconstruction of tables. Fixed-width text blocks preserve
> column spacing, but reading order, merged cells, and glyphs can still be
> imperfect. Images, diagrams, and image-based tick marks are not transcribed.
> Verify consequential table values against the linked original PDF.

## PDF page 1

```text
Revised: May 4, 2026


Configure Licenses and Throughput for Catalyst 8000 Series
Physical Platforms

Available licenses
This document provides information about the licenses that are available for Cisco Catalyst 8200, 8300, and 8500 Edge Platforms,
the supported throughput options, and how you can configure the license and the throughput.

      Note

The information applies predominantly to a device operating in the autonomous mode. References to the controller mode are included
in certain sections for the sake of comparison and completeness. Where the information applies to controller mode, this has been
called-out categorically.

For a more detailed overview on Cisco Licensing, go to https://cisco.com/go/licensingguide.


What's new and changed
The following table provides a summary of license related changes applicable to the Cisco Catalyst 8200, 8300, and 8500 Edge
platforms. The table lists only the software release that introduced support for a given feature in a given software release train. Unless
noted otherwise, subsequent releases of that software release train also support that feature.

Table 1: Release-based changes in licensing


Feature name                                  Release                              Feature information

500 Mbps aggregate for Tier 1 and 250 Cisco IOS XE 17.14.1a                        When you configure a throughput of 250 Mbps or
Mbps throughput configuration in                                                   T1, if an HSECK9 license is available on the device,
autonomous mode                                                                    then aggregate throughput throttling is effective.
                                                                                   Throughput is capped at 500 Mbps and any
                                                                                   distribution of traffic in the upstream and
                                                                                   downstream direction is allowed. In earlier releases,
                                                                                   bidirectional throughput throttling was applicable
                                                                                   to T1 and 250 Mbps. Throughput was capped at 250
                                                                                   Mbps in each direction.
                                                                                   For more information, see Release-wise changes in
                                                                                   throttling behavior, on page 15.




                                                                                                                                        1
```

## PDF page 2

```text
Feature name                         Release                          Feature information

Aggregate throughput throttling -    Cisco IOS XE Cupertino 17.8.1a   For throughput levels greater than 250 Mbps and
physical platforms                                                    Tier 2 and higher tiers, when you configure the
                                                                      bidirectional throughput value on the device,
                                                                      aggregate throughput throttling is effective. This
                                                                      means that traffic is throttled in an aggregate manner
                                                                      irrespective of the distribution of the traffic in the
                                                                      upstream and downstream direction.
                                                                      Bidirectional throughput is represented in the license
                                                                      PID. For example, in DNA-C-500M-E-3Y and
                                                                      DNA-C-T2-E-3Y, the aggregate throughput is
                                                                      double the bidirectional throughput.
                                                                      For more information, see Release-wise changes in
                                                                      throttling behavior, on page 15.

Tier-based licenses                  Cisco IOS XE Cupertino 17.7.1a   Support for tier-based throughput configuration was
                                                                      introduced in addition to existing bandwidth-based
                                                                      (numeric) throughput configuration.
                                                                      Starting with the lowest throughput level, the
                                                                      available tiers are Tier 0 (T0), Tier 1 (T1), Tier 2
                                                                      (T2), and Tier3 (T3). Each tier represents a
                                                                      throughput level.
                                                                      If the license PID for a product is tier-based, the
                                                                      license is displayed with the tier value in the CSSM
                                                                      Web UI.
                                                                      For a product with a tier-based license, you can
                                                                      configure a tier-based throughput value, and you can
                                                                      also convert to a tier-based throughput value.
                                                                      For more information, see Throughput , on page 10
                                                                      and Numeric and tier-based throughput, on page 11.

Cisco Digital Network Architecture   Cisco IOS XE Amsterdam 17.3.2    Support for Cisco DNA licenses was introduced.
(DNA) licenses                                                        Cisco DNA Licenses are categorised into
                                                                      network-stack licenses and a DNA-stack add-on
                                                                      licenses.
                                                                      For more information, see Cisco DNA license, on
                                                                      page 3.

High Security license (HSECK9)       Cisco IOS XE Amsterdam 17.3.2    Support for the HSECK9 license was introduced.
                                                                      For more information, see High Security license ,
                                                                      on page 6.




2
```

## PDF page 3

```text
Feature name                            Release                                Feature information

Cisco Unified Border Element license Cisco IOS XE Amsterdam 17.3.2             Support for Cisco UBE, Cisco Unified CME, Cisco
(Cisco UBE license)                                                            Unified SRST licenses was introduced. For more
                                                                               information, see Cisco Unified Border Element
Cisco Unified Communications
                                                                               license, on page 10, Cisco Unified CME license, on
Manager Express license (Cisco
                                                                               page 10, and Cisco Unified SRST license, on page
Unified CME license)
                                                                               9.
Cisco Unified Survivable Remote Site
Telephony license (Cisco Unified
SRST license)

Use the Cisco Feature Navigator to find information about platform support and Cisco software image support. To access the Cisco
Feature Navigator, go to www.cisco.com/go/cfn. An account on Cisco.com is not required.


Cisco DNA license
A Cisco Digital Network Architecture (DNA) software license is a subscription-based licensing model that combines several
feature-specific licenses. A Cisco DNA license includes all feature licenses except the following: High Security (HSECK9), Cisco
Unified Border Element (Cisco UBE), Cisco Unified Communications Manager Express (Cisco Unified CME), and Cisco Unified
Survivable Remote Site Telephony (Cisco Unified SRST).
Cisco DNA licenses are categorized into network-stack licenses and DNA-stack add-on licenses. See the lists in this section that
specify the Cisco DNA Licenses that are available on Cisco Catalyst 8200, 8300, and 8500 Edge platforms.
Cisco DNA Licenses Available on Catalyst 8200 and 8300 Series Edge Platforms:
Network-stack licenses:
   • Network Essentials
   • Network Advantage: Includes features that are available with Network Essentials, and more.
   • Network Premier: Includes features that are available with Network Essentials, Network Advantage, and more.

DNA-stack add-on licenses:
   • Cisco DNA Essentials: Add-on license that is available only with Network Essentials.
   • Cisco DNA Advantage: Add-on license that's available only with Network Advantage. Includes features available with DNA
     Essentials and more.
   • Cisco DNA Premier: Add-on license that's available only with Network Premier. Includes features available with DNA Essentials,
     DNA Advantage and more.

Cisco DNA Licenses Available on Catalyst 8500 Series Edge Platforms:
Network-stack licenses:
   • Network Advantage
   • Network Premier: Includes features available with Network Advantage, and more.

DNA-stack add-on licenses:
   • Cisco DNA Advantage




                                                                                                                                   3
```

## PDF page 4

```text
    • Cisco DNA Premier: Add-on license that's available only with Network Premier. Includes features available with DNA Advantage
      and more.


Guidelines for using a Cisco DNA license
    • A network-stack license is a perpetual or permanent license and has no expiration date.
    • A DNA-stack add-on license is a subscription or a term license that is valid only until a certain date. A 3-year and a 5-year option
      is available for all DNA-stack add-on licenses. A 7-year subscription option is also available for certain DNA-stack add-on
      licenses.
    • Tier 3 (T3) or higher tiers are not supported with the Network Essentials and DNA Essentials licenses. If you have configured
      T3 or higher tiers as the throughput, you cannot change the boot level license to Network Essentials and DNA Essentials. For
      information about the various tiers available with Cisco DNA Licenses, see Tier and numeric throughput mapping, on page 13.
    • The DNA-stack add-on license that is available with each network-stack license is optional. You can configure a network-stack
      license without a DNA-stack add-on license, but you cannot configure DNA-stack add-on license without the corresponding
      network-stack license.
    • If you use a DNA-stack add-on license, renew the license before term expiry to continue using it, or deactivate the DNA-stack
      add-on license and then reload the device to continue operating with the network-stack license capabilities.


Ordering considerations for a Cisco DNA license
    • A Cisco DNA license subsumes all performance, boost, and technology package licenses (securityk9, uck9, and appxk9). Thus,
      when you order a Cisco DNA network-stack license, or a Cisco DNA-stack add-on license, if a performance, boost, and technology
      package license is required or applicable, it is automatically added to the order.
    • The license Product ID (PID) you purchase can only be a DNA-stack add-on license PID.
    • Even if you order a Cisco DNA license along with a new hardware, the license is not preconfigured on the device. You must
      configure the boot level license and then the throughput on the device.
    • When ordering a Cisco DNA license, you must also specifiy a throughput value. If the throughput you order is greater than 250
      Mbps, an HSECK9 license is required on all variants of Cisco Catalyst 8000 Edge Platforms Family except for Catalyst 8500
      and 8500L Series Edge Platforms. For more information, see High Security license , on page 6.
    • When you order a license PID with a tier-based throughput value of T1, an HSECK9 license is automatically added to the order.


Configure a boot level license
If you've purchased a Cisco DNA license for a new device, or if you have an existing device and you want to upgrade, downgrade,
add, or remove the currently configured license on your device, perform these steps.
This task sets a boot level license and requires a reload before the configured changes are effective.

Step 1       show version
             Displays the currently set boot level license.
             In the accompanying example, Network Advantage and DNA Advantage licences are configured on the device.
             Example:




4
```

## PDF page 5

```text
         Device# show version
         <output truncated>
         Technology Package License Information:

         -----------------------------------------------------------------
         Technology     Type         Technology-package Technology-package
                                     Current            Next Reboot
         -----------------------------------------------------------------
         Smart License Perpetual     network-advantage network-advantage
         Smart License Subscription dna-advantage       dna-advantage

         <output truncated>

Step 2   configure terminal
         Enters global configuration mode.
         Example:
         Device# configure terminal

Step 3   [no] license boot level {network-advantage [addon dna-advantage] | network-essentials [addon dna-essentials] |
         network-premier [addon dna-premier] }
         Sets a boot level license.
         First, configure a network-stack license and then configure the corresponding add-on license.
         In the command syntax, the configuration of a DNA-stack add-on license is optional.
         The accompanying example shows configuration on a C8300-1N1S-4T2X router. The network-stack license, Network
         Premier, and the corresponding add-on license: DNA-Premier, are configured.
         Example:
         Device(config)# license boot level network-premier addon dna-premier
         % use 'write' command to make license boot config take effect on next boot

Step 4   exit
         Exits global configuration mode and returns to privileged EXEC mode.
         Example:
         Device# exit

Step 5   copy running-config startup-config
         Saves your entries in the configuration file.
         Example:
         Device# copy running-config startup-config
         Destination filename [startup-config]?
         Building configuration...
         [OK]
         <output truncated>

Step 6   reload
         Reloads the device. The license levels you previously configured are effective and displayed only after this reload.
         Example:
         Device# reload
         Proceed with reload? [confirm]




                                                                                                                                5
```

## PDF page 6

```text
            *Dec 8 01:04:12.287: %SYS-5-RELOAD: Reload requested by console.
            Reload Reason: Reload Command.
            <output truncated>

Step 7      show version
            Displays the currently set boot level license.
            In the accompanying example, the output confirms that Network Premier and DNA-Premier licenses are configured.
            Example:
            Device# show version
            <output truncated>
            Technology Package License Information:

            -----------------------------------------------------------------
            Technology     Type         Technology-package Technology-package
                                        Current            Next Reboot
            -----------------------------------------------------------------
            Smart License Perpetual     network-premier    network-premier
            Smart License Subscription dna-premier         dna-premier
            <output truncated>

Step 8      show license summary
            Displays a summary of license usage which includes information about licenses being used, the count, and the status.
            Example:
            Device# show license summary

            Account Information:
              Smart Account: Eg-SA As of Dec 08 08:10:33 2021 UTC
              Virtual Account: Eg-VA

            License Usage:
              License                 Entitlement Tag               Count Status
              -----------------------------------------------------------------------------
              network-premier_T2      (NWSTACK_T2_P)                    1 IN USE
              dna-premier_T2          (DSTACK_T2_P)                     1 IN USE

What's next
Configure the throughput based on your license. For more information, see Throughput , on page 10



High Security license
The High Security license (HSECK9 license) is an export-controlled license and is restricted by U.S. export control laws. This license
is required for the use of full cryptographic functionality. That is, for throughput greater than 250 Mbps and tunnel count over and
above a certain number. Note that this requirement applies to all devices of Cisco Catalyst 8000 Edge Platforms Family except for
Catalyst 8500 and 8500L Series Edge Platforms.
On Cisco Catalyst 8500 and 8500L Series Edge Platforms, the throughput and tunnel scale are not impacted by the non-availability
of the HSECK9 license. On these platforms, the HSECK9 license is required only for compliance purposes. On all the remaining
models of Cisco Catalyst 8000 Edge Platforms Family, the supported tunnel count and throughput are restricted in the absence of an
HSECK9 license.
This table specifies the supported tunnel count and supported throughput without the HSECK9 license:




6
```

## PDF page 7

```text
PID                                        No. of tunnels without HSECK9 license Supported throughput without HSECK9
                                                                                 license

C8200-1N-4T                                1000                                       T0, T1

C8200L-1N-4T                               1000                                       T0, T1

C8300-1N1S-4T2X                            1000                                       T0, T1

C8300-1N1S-6T                              1000                                       T0, T1

C8300-2N2S-4T2X                            1000                                       T0, T1

C8300-2N2S-6T                              1000                                       T0, T1

C8500-12X4QC                               N/A                                        N/A

C8500-12X                                  N/A                                        N/A

C8500-20X6C                                N/A                                        N/A

C8500L-8S4X                                N/A                                        N/A


      Note

The term throughput refers to encrypted and unencrypted throughput, combined.

By using an HSECK9 license, the tunnel count restriction is lifted and you can configure throughput greater than 250 Mbps. For
detailed information about the available throughput options, see Tier and numeric throughput mapping, on page 13.

Verify HSECK9 license usage
To know if an HSECK9 license is being used on your device, enter the show license summary command in privileged EXEC mode.
The HSECK9 license as displayed as: Router US Export Lic. for DNA (DNA_HSEC).
For example:
Device# show license summary

Account Information:
  Smart Account: Eg-SA As of Dec 03 15:26:02 2021 UTC
  Virtual Account: Eg-VA

License Usage:
  License                 Entitlement Tag               Count Status
  ---------------------------------------------------------------------------
  network-advantage_T2    (NWSTACK_T2_A)                    1 IN USE
  dna-advantage_T2        (DSTACK_T2_A)                     1 IN USE
  Router US Export Lic... (DNA_HSEC)                        1 IN USE


Guidelines for using an HSECK9 license
An HSECK9 license is tied to a chassis. Therefore, one HSECK9 license is required for each chassis UDI where you want to use
cryptographic functionality.




                                                                                                                                 7
```

## PDF page 8

```text
An HSECK9 license requires authorization before you can use it. This authorisation is provided by a Smart Licensing Authorization
Code (SLAC). Generate and obtain an SLAC from the Cisco SSM portal before you install the SLAC for each HSECK9 license you
use.
The method of obtaining an SLAC from the Cisco SSM portal depends on the topology you have implemented. For more information,
see Install SLAC for an HSECK9 license, on page 8.

Verify HSECK9 status
To know if SLAC is installed, enter the show license authorization command in privileged exec mode. If SLAC is installed, the
status field displays: SMART AUTHORIZATION INSTALLED on <timestamp>.
For example:
Device# show license authorization
Overall status:
  Active: PID:C8300-1N1S-4T2X,SN:FDO2250A0J5
      Status: SMART AUTHORIZATION INSTALLED on Dec 03 08:24:35 2021 UTC
      Last Confirmation code: 418b11b3

Authorizations:
  Router US Export Lic. for DNA (DNA_HSEC):
    Description: U.S. Export Restriction Compliance license for DNA based Routers
    Total available count: 1
    Enforcement type: EXPORT RESTRICTED
    Term information:
      Active: PID:C8300-1N1S-4T2X,SN:FDO2250A0J5
        Authorization type: SMART AUTHORIZATION INSTALLED
        License type: PERPETUAL
          Term Count: 1

Purchased Licenses:
  No Purchase Information Available


Ordering considerations for an HSECK9 license
If you place an order for your Cisco Catalyst 8000 platform and your DNA licenses together, the HSECK9 license is automatically
added to the order, if applicable. For example, in case of Catalyst 8500 Series Edge Platforms, when you order the hardware, an
HSECK9 license is automatically added to the order because throughput support starts at greater than 250 Mbps on these platforms.
Further, the requisite SLAC for the HSECK9 license is also factory-installed on the device.
If you order your DNA license separately, the HSECK9 license is not added automatically to your oder. You must separately order
the HSECK9 license, if required.
If you plan to use an HSECK9 license with your hardware, provide your Smart Account and Virtual Account information along with
the hardware order. This enables Cisco to factory-install SLAC for the HSECK9 license on the hardware. You must still configure
throughput on the device before you start using it.

     Note

If you order the HSECK9 license separately and not with the hardware, SLAC cannot be factory-installed.


Install SLAC for an HSECK9 license
A Smart Licensing Authorization Code (SLAC) is generated in and obtained from Cisco Smart Software Manager (CSSM) portal.
To obtain the SLAC, there are multiple ways in which a product may be connected to the Cisco SSM portal. Each way of connecting
to Cisco SSM is called as a topology. You must implement one of the supported topologies before you can install SLAC.




8
```

## PDF page 9

```text
For information about all the methods, see the Supported Topologies section in the Smart Licensing Using Policy for Cisco Enterprise
Routing Platforms document.

     Note

Ensure that a boot level license is already configured on the device. To know how to configure a boot license, see Configure a boot
level license, on page 4.
In the output of the show version privileged EXEC command, ensure that a license is mentioned in the License Level field.


Required tasks after installing SLAC
Complete the following required tasks after installing SLAC - only if applicable to the platform:

Platform                                                   Required Tasks After Installing SLAC

For Cisco Catalyst 8200 and 8300 Series Edge               Enter the license feature hseck9 command in global configuration mode.
Platforms                                                  This enables the HSECK9 license on these platforms.

For Cisco Catalyst 8500L Series Edge Platforms             Reload the device after installing SLAC.


Where to go next:
Configure the throughput based on your license. For more information, see Throughput , on page 10.



Cisco Unified SRST license
A Cisco Unified Survivable Remote Site Telephony License (Cisco Unified SRST license) does not require any boot level configuration
before you enable it.
In the context of this licensing model, a Unified SRST license is an unenforced license. You must order a Cisco Unified SRST license
separately, if required. It is not automatically included with any other license.

Additional references
   • To configure the available Unified SRST features, refer to the configuration guide. For information about the features available
     with a Cisco Unified SRST license, see the Cisco Unified SCCP and SIP SRST System Administrator Guide (All Versions).
   • For information about supported platforms and about purchasing a Cisco Unified SRST license, see
     https://www.cisco.com/c/en/us/products/collateral/unified-communications/unified-communications-manager-express/datasheet-c78-744069.html.
   • For information about how to report usage of a Unified SRST license, see Smart Licensing Using Policy for Cisco Enterprise
     Routing Platforms.


What to do next:
After you purchase this license, configure the throughput. For more information, see Throughput , on page 10.




                                                                                                                                             9
```

## PDF page 10

```text
Cisco Unified Border Element license
A Cisco Unified Border Element (Cisco UBE) license does not require any boot level configuration before you enable it. After
purchase, you can refer to the configuration guide to configure the available Cisco UBE features.
You must order a Cisco UBE license separately, if required. Cisco UBE license is not automatically included with any other license.

Additional References
     • For information about the features available with a Cisco UBE license, see the Cisco Unified Border Element Configuration
       Guide.
     • For release-based information, see https://www.cisco.com/c/en/us/support/unified-communications/unified-border-element/
       products-installation-and-configuration-guides-list.html.
     • For information about supported platforms and about purchasing a Cisco UBE license, see
       https://www.cisco.com/c/en/us/products/collateral/unified-communications/unified-border-element/data-sheet-c78-729692.html.
     • For information about how to report usage of a Cisco UBE license, see Smart Licensing Using Policy for Cisco Enterprise
       Routing Platforms. In the context of this document, a Cisco UBE license is an unenforced license.


What to do next:
After you enable your license, configure the throughput. For more information, see Throughput , on page 10.


Cisco Unified CME license
A Cisco Unified Communications Manager Express License (Cisco Unified CME license) does not require any boot level configuration
before you enable it. After purchase, you can refer to the configuration guide to configure the available features.

Additional references
     • For information about the features available with a Cisco Unified CME license, see the Cisco Unified Communications Manager
       Express System Administrator Guide.
     • For information about supported platforms and about purchasing a Cisco Unified CME license, see
       https://www.cisco.com/c/en/us/products/collateral/unified-communications/unified-communications-manager-express/datasheet-c78-744069.html.
       You must order a Cisco Unified CME license separately, if required. It is not automatically included with any other license.
     • For information about how to report usage of a Cisco Unified CME license, see Smart Licensing Using Policy for Cisco Enterprise
       Routing Platforms. In the context of this document, a Cisco Unified CME license is an unenforced license.


What to do next:
After you enable your license, configure the throughput. For more information, see Throughput , on page 10.


Throughput
Throughput is a measure of the data that is transmitted through a network in a given amount of time. In the context of licensing,
throughput tells you how much data is allowed to be transferred through a device.




10
```

## PDF page 11

```text
You must first configure the throughput value in the autonomous mode before data can be transmitted (Tx) and received (Rx) at the
configured rate. If you don’t explicitly configure a throughput value, the default throughput is effective.
To know the configured throughput of a device, enter the show platform hardware throughput level command in privileged EXEC
mode.
The following sections provide information about how a throughput value is represented, whether the throughput on a device refers
to encrypted or unencrypted throughput and what this means, and if and how a limit may be enforced on a device throughput.

Numeric and tier-based throughput
Your Cisco DNA license product ID or PID contains the throughput you are entitled to. The throughput value is either represented
by a number or by a tier in the PID. The same value is configured on the device.

Numeric throughput value
When throughput is represented by a number, it is called a numeric throughput value. For example, DNA-C-10M-E-3Y is a license
PID with a numeric throughput value of 10M or 10 Mbps.
Depending on the device, some of the other available numeric throughput values are: 15M, 25M, 50M, 100M, 250M, 500M, 1G,
2.5G, 5G, 10G, and so on. Throughput greater than 250 Mbps requires an HSECK9 license.

Tier-Based throughput value
When throughput is represented by a tier, it is called a tier-based throughput value. A tier represents a throughput level and is mapped
to a numeric throughput value. For example, DNA-C-T0-E-3Y is a license PID with a tier-based throughput value of T0. The numeric
equivalent it is mapped to is a throughput of up to 25 Mbps.

     Note

Tier-based throughput configuration is supported starting with Cisco IOS XE Cupertino 17.7.1a. From this release onwards, tier-based
throughput configuration is also the recommended way of configuring throughput on the device.

Starting with the lowest throughput level, the available tiers are Tier 0 (T0), Tier 1 (T1), Tier 2 (T2), Tier 3 (T3), Tier 4 (T4), and
Tier 5 (T5). T2 and higher tiers require an HSECK9 license.

Notes about tiers
   • Not all tiers are available with all Cisco DNA licenses. For example, T3 and higher tiers are not available with the Network
     Essentials and DNA-Essentials licenses. This also means that if you have T3 as the configured throughput, you cannot change
     the boot level license to Network Essentials and DNA Essentials.
   • Each tier maps to or means a different numeric value for different platforms.
     The different platforms in the Cisco Catalyst 8000 Edge Platforms Family support different maximum throughput levels. For
     example, T2 means 1G throughput for C8300-2N2S-4T2X, 500M for C8200-1N-4T, and 250M for C8200L-1N-4T.


Additional references
   • To know which tiers are available with a particular DNA License and to know the numeric equivalent of each tier for a particular
     platform and see the Tier and numeric throughput mapping, on page 13 section.
   • To know when to configure a numeric throughput value and when to configure tier-based throughput on your device, see the
     Numeric vs. tier-based throughput configuration, on page 12 section.




                                                                                                                                      11
```

## PDF page 12

```text
Numeric vs. tier-based throughput configuration
With the introduction of tier-based throughput configuration in Cisco IOS XE Cupertino 17.7.1a, you can configure both numeric
and tier-based throughput on your device. This section provides information about when to configure a numeric throughput value
and when to configure tier-based throughput.
Identifying whether you have tier-based or numeric licenses
Cisco Smart Software Manager (Cisco SSM) is a portal that enables you to manage all your Cisco software licenses. All the license
PIDs you purchase are listed in the Cisco SSM Web UI at: https://software.cisco.com → Manage licenses.
To identify whether you have a tier-based license or a numeric license, log in to the portal and in the corresponding Smart Account
and Virtual Account, navigate to Inventory > Licences. The UI displays the throughput type. See this sample screenshot that shows
you how tier-based and numeric licenses are displayed:
Figure 1: Numeric and tier values - Cisco SSM web UI




Configure a numeric or tier-based throughput value
     • If you purchase a numeric license PID, the license is displayed with the numeric throughput value and tier-based value in the
       Cisco SSM Web UI. For such a license, we recommend that you configure only a numeric throughput value. For more information,
       see Configure numeric throughput, on page 20.
     • If you purchase a tier-based license PID, the license is displayed with only the tier value in the Cisco SSM Web UI. For such a
       license, you can either configure a tier-based throughput value to match the display in the CSSM Web UI, or you can configure
       a numeric throughput value. For more information, see Configure Tier-Based Throughput or Configure a Numeric Throughput.

Convert a numeric throughput to tier-based and vice versa
This table specifies when you can convert from numeric to tier-based throughput configuration, or vice versa, when this conversion
is required, and when it is optional.

If you...                                              then...

configure a numeric throughput value on the device do not convert to tier-based throughput value.
and the license PID is a numeric license,




12
```

## PDF page 13

```text
If you...                                             then...

configure a numeric throughput value on the device you can convert the throughput configuration to tier-based value. There is no
and the license PID is a tier-based license,       functional impact if you do not convert to a tier-based throughput value.
                                                      For more information, see Convert a numeric throughput value to tier-based,
                                                      on page 25.

upgrade to a release where tier-based throughput      you can convert the throughput to tier-based value after upgrade.There is no
values are supported and the license PID is           functional impact if you do not convert to a tier-based throughput value.
tier-based,
                                                      For more information, see Upgrade from numeric throughput to tier-based
                                                      throughput, on page 27.

upgrade to a release where tier-based throughput      do not convert to a tier-based throughput value.
values are supported, and your license PID is
numeric,

downgrade to a release where only numeric             change the configuration to a numeric throughput value before you downgrade.
throughput values are supported and your license
                                                      For more information, see Downgrade tier-based throughput to numeric
PID and throughput configuration are tier-based,
                                                      throughput, on page 27.


Tier and numeric throughput mapping
This section provides information about the numeric equivalent of each tier and the DNA licenses that each tier is available with.

Tier and numeric throughput mapping for Cisco Catalyst 8000 physical platforms




The mapping table in these images clarify only the numeric equivalent of a tier. This mapping does not reflect the final throughput
that you are entitled to. The entitled throughput depends on the device’s capability, the software version running on the device, and
the throttling behavior for that version. For more information, see Entitled Throughput and Throttling Specifications in the Autonomous
Mode.




                                                                                                                                    13
```

## PDF page 14

```text
     Note

When you purchase a license PID with a tier-based throughput value of T1, an HSECK9 license is automatically provided.


Encrypted and unencrypted throughput
Encrypted throughput, also known as crypto throughput, is throughput that is protected by a cryptographic algorithm.
Unencrypted throughput on the other hand, is in plain text. Unencrypted throughput is also referred to as Cisco Express Forwarding
(CEF) traffic.

     Important

All references to throughput in this document refer to cryptographic throughput.


Throttled and unthrottled throughput
Throttled throughput, is throughput on which a limit has been enforced. When you configure a throughput value, you are throttling
device throughput to the configured extent.
Unthrottled throughput means that no limit is enforced, and the device throughput is at the maximum capability of the device.

     Note

Unencrypted throughput (Tx and Rx), is unthrottled by default.


Types of throttling behavior: aggregate and bidirectional
The system can impose throttling in a bidirectional manner or an aggregate manner.

Bidirectional throughput throttling
Here, the system throttles data in each direction. When bidirectional throttling is effective, Tx and Rx data are capped at the bidirectional
throughput value separately.
For example, if the bidirectional throughput value is 25 Mbps or T0, and bidirectional throughput throttling is effective, Tx data is
capped at 25 Mbps and Rx data is capped at 25 Mbps.

     Note

The value that you see in a license PID (whether numeric or tier-based) represents a bidirectional throughput value.


Aggregate throughput throttling
Here, the system doubles the configured value and throttles throughput at this aggregate limit. When aggregate throughput throttling
is effective, traffic is not throttled separately in each direction.
For example, if the bidirectional throughput value that is configured is 500 Mbps and aggregate throughput throttling is effective,
the traffic in the upstream and downstream direction can be any ratio within the 1 Gbps aggregate limit. For instance, 800 Mbps Tx
and 200 Mbps Rx, or, 300 Mbps Tx and 700 Mbps Rx.




14
```

## PDF page 15

```text
Release-wise changes in throttling behavior
To know if the throughput on your device will be throttled in a bidirectional manner or in an aggregate manner, check the software
version running on the device. Refer to the release-wise changes in throttling behavior described in this table to identify the throttling
behavior.

Table 2: Release-wise changes in throttling behavior


Cisco IOS XE release                                      Throttling behavior

Starting with Cisco IOS XE 17.14.1a                       When you configure a throughput of 250 Mbps or T1, aggregate throughput
                                                          throttling is effective as long as an HSECK9 license is available on the device.
                                                          This means an aggregate limit of 500 Mbps is available for use in any Tx and
                                                          Rx ratio.
                                                          If an HSECK9 license is not available on the device and you configure a
                                                          throughput value of 250 Mbps, or T1, then bidirectional throughput throttling
                                                          is effective. The throughput is throttled at 250 Mbps in each direction.

Starting with Cisco IOS XE Cupertino 17.8.1a              When you configure a throughput value greater than 250 Mbps or T2 and higher
                                                          tiers, aggregate throughput throttling is effective.
                                                          On C8200L-1N-4T, if you configure a numeric value of 250 Mbps, bidirectional
                                                          throughput throttling is effective and a maximum of 250 Mbps is available in
                                                          each direction. But if you configure tier T2, aggregate throttling is effective
                                                          and 500 Mbps is available for use in any Tx and Rx ratio.

Until Cisco IOS XE Cupertino 17.7.x                       Only bidirectional throughput throttling is effective.


Entitled throughput and throttling specifications in the autonomous mode
These tables tell you about the throughput you are entitled to. This is based on the device, the throughput value, which can be aggregate
or numeric, and the release, which determines if throttling is imposed in an aggregate or bidirectional manner.

Table 3: C8200-1N-4T


                                                                                                   Throughput = Encrypted Throughput
                                                                                                          * HSECK9 license is required.

Supported         Entitled throughput &                Entitled throughput &       Entitled throughput &       Entitled throughput &
throughput values throttling in >= 17.4.1a             throttling in >= 17.7.1a    throttling in >= 17.8.1a    throttling in >= 17.14.1a
(default 10M)

10M                        10M bidirectional           10M bidirectional           10M bidirectional           10M bidirectional

15M                        15M bidirectional           15M bidirectional           15M bidirectional           15M bidirectional

25M                        25M bidirectional           25M bidirectional           25M bidirectional           25M bidirectional

50M                        50M bidirectional           50M bidirectional           50M bidirectional           50M bidirectional

100M                       100M bidirectional          100M bidirectional          100M bidirectional          100M bidirectional




                                                                                                                                        15
```

## PDF page 16

```text
250M                    250M bidirectional       250M bidirectional      250M bidirectional         With HSECK9: 500M
                                                                                                    aggregate
                                                                                                    Without HSECK9: 250M
                                                                                                    bidirectional

500M*                   500M bidirectional       500M bidirectional      1G aggregate               1G aggregate

T0                      -                        15M bidirectional       25M bidirectional          25M bidirectional

T1                      -                        100M bidirectional      100M bidirectional         With HSECK9: 500M
                                                                                                    aggregate
                                                                                                    Without HSECK9: 250M
                                                                                                    bidirectional

T2                      -                        500M bidirectional      1G aggregate               1G aggregate


Table 4: C8200L-1N-4T


                                                                                        Throughput = Encrypted Throughput
                                                                                                * HSECK9 license is required.

Supported throughput Entitled throughput & Entitled throughput & Entitled throughput & Entitled throughput &
values               throttling in >= >=   throttling in >= 17.7.1a throttling in >= 17.8.1a throttling in >= 17.14.1a
                     17.5.1a
(default 10M)

10M                         10M bidirectional       10M bidirectional      10M bidirectional         10M bidirectional

15M                         15M bidirectional       15M bidirectional      15M bidirectional         15M bidirectional

25M                         25M bidirectional       25M bidirectional      25M bidirectional         25M bidirectional

50M                         50M bidirectional       50M bidirectional      50M bidirectional         50M bidirectional

100M                        100M bidirectional      100M bidirectional     100M bidirectional        100M bidirectional

250M                        250M bidirectional      250M bidirectional     250M bidirectional        With HSECK9: 500M
                                                                                                     aggregate
                                                                                                     Without HSECK9: 250M
                                                                                                     bidirectional

T0                          -                       15M bidirectional      25M bidirectional         25M bidirectional

T1                          -                       100M bidirectional     100M bidirectional        With HSECK9: 500M
                                                                                                     aggregate
                                                                                                     Without HSECK9: 250M
                                                                                                     bidirectional

T2*                         -                       250M bidirectional     500M aggregate            500M aggregate




16
```

## PDF page 17

```text
-                                                                                 From 17.8.1a, On C8200-1N-4T-L,
                                                                                  if you configure a numeric value of
                                                                         Note     250 Mbps, a maximum of 250 Mbps
                                                                                  is available in each direction. But if
                                                                                  you configure tier-based value T2,
                                                                                  which requires an HSECK9 license,
                                                                                  500 Mbps is available for use in any
                                                                                  Tx and Rx ratio.


Table 5: C8300-1N1S-4T2X, C8300-2N2S-4T2X


                                                                                        Throughput = Encrypted Throughput
                                                                                              * HSECK9 license is required.

Supported throughput Entitled throughput & Entitled throughput & Entitled throughput & Entitled throughput &
values               throttling in >= 17.3.2 throttling in >= 17.7.1a throttling in >= 17.8.1a throttling in >= 17.14.1a
(default 10M)

10M                            10M bidirectional    10M bidirectional    10M bidirectional         10M bidirectional

15M                            15M bidirectional    15M bidirectional    15M bidirectional         15M bidirectional

25M                            25M bidirectional    25M bidirectional    25M bidirectional         25M bidirectional

50M                            50M bidirectional    50M bidirectional    50M bidirectional         50M bidirectional

100M                           100M bidirectional   100M bidirectional   100M bidirectional        100M bidirectional

250M                           250M bidirectional   250M bidirectional   250M bidirectional        With HSECK9: 500M
                                                                                                   aggregate
                                                                                                   Without HSECK9: 250M
                                                                                                   bidirectional

500M*                          500M bidirectional   500M bidirectional   1G aggregate              1G aggregate

1G*                            1G bidirectional     1G bidirectional     2G aggregate              2G aggregate

2.5G*                          2.5G bidirectional   2.5G bidirectional   5G aggregate              5G aggregate

T0                             -                    15M bidirectional    25M bidirectional         25M bidirectional

T1                             -                    100M bidirectional   100M bidirectional        With HSECK9: 500M
                                                                                                   aggregate
                                                                                                   Without HSECK9: 250M
                                                                                                   bidirectional

T2*                            -                    1G bidirectional     2G aggregate              2G aggregate

T3*                            -                    10G bidirectional    20G aggregate             20G aggregate




                                                                                                                           17
```

## PDF page 18

```text
Table 6: C8300-1N1S-6T, C8300-2N2S-6T


                                                                                                    Throughput = Encrypted Throughput
                                                                                                         * HSECK9 license is required.

Supported                    Entitled throughput Entitled throughput Entitled throughput Entitled throughput & throttling
throughput values            & throttling in >=  & throttling in >=  & throttling in >=  in >= 17.14.1a
                             17.3.2              17.7.1a             17.8.1a
(default 10M)

10M                          10M bidirectional        10M bidirectional       10M bidirectional       10M bidirectional

15M                          15M bidirectional        15M bidirectional       15M bidirectional       15M bidirectional

25M                          25M bidirectional        25M bidirectional       25M bidirectional       25M bidirectional

50M                          50M bidirectional        50M bidirectional       50M bidirectional       50M bidirectional

100M                         100M bidirectional       100M bidirectional      100M bidirectional      100M bidirectional

250M                         250M bidirectional       250M bidirectional      250M bidirectional      With HSECK9: 500M aggregate
                                                                                                      Without HSECK9: 250M
                                                                                                      bidirectional

500M*                        500M bidirectional       500M bidirectional      1G aggregate            1G aggregate

1G*                          1G bidirectional         1G bidirectional        2G aggregate            2G aggregate

T0                           -                        15M bidirectional       25M bidirectional       25M bidirectional

T1                           -                        100M bidirectional      100M bidirectional      With HSECK9: 500M aggregate
                                                                                                      Without HSECK9: 250M
                                                                                                      bidirectional

T2*                          -                        1G bidirectional        2G aggregate            2G aggregate


Table 7: C8500-12X, C8500-12X4QC


                                                                                                    Throughput = Encrypted Throughput
                                                                               *HSECK9 license required for compliance purposes only.

Supported throughput values Entitled throughput &                        Entitled throughput &           Entitled throughput &
                            throttling in >= 17.3.2                      throttling in >= 17.7.1a        throttling in >= 17.8.1a
(default 10M)

2.5G*                                   2.5G bidirectional               2.5G bidirectional              5G aggregate

5G*                                     5G bidirectional                 5G bidirectional                10G aggregate

10G*                                    10G bidirectional                10G bidirectional               20G aggregate

T3*                                     -                                10G bidirectional               20G aggregate




18
```

## PDF page 19

```text
Table 8: C8500L-8S4X


                                                                                             Throughput = Encrypted Throughput
                                                                       *HSECK9 license required for compliance purposes only.

Supported Throughput Values Entitled Throughput &                 Entitled Throughput &           Entitled Throughput &
                            Throttling in >= 17.4.1a              Throttling in >= 17.7.1a        Throttling in >= 17.8.1a
(default 10M)

1G*                             1G Bidirectional                  1G Bidirectional                2G Aggregate

2.5G*                           2G Bidirectional                  2G Bidirectional                5G Aggregate

5G*                             5G Bidirectional                  5G Bidirectional                10G Aggregate

10G*                            10G Bidirectional                 10G Bidirectional               20G Aggregate

T2*                             -                                 1G Bidirectional                2G Aggregate

T3*                             -                                 10G Bidirectional               20G Aggregate


Table 9: C8500-20X6C


                                                                                             Throughput = Encrypted Throughput
                                                                       *HSECK9 license required for compliance purposes only.

Supported Throughput Values                         Entitled Throughput and Throttling in >= 17.10.1a
(default T4)

T4*                                                 50G Aggregate

T5*                                                 Unthrottled



Entitled throughput and throttling specifications in the SD-WAN controller mode
PID                    Introductory release for Throughput without            Throughput with           Throughput with
                       PID                      HSECK9 -                      HSECK9                    HSECK9
                                                bi-directional
                                                                              (>=17.3.2 and <17.8.1a, (>17.8.1a, aggregate)
                                                                              bi-directional)

C8300-1N1S-4T2X        17.3.2                       250M                      unthrottled               unthrottled
(default 250M)

C8300-2N2S-6T          17.3.2                       250M                      1G                        2G
(default 250M)

C8300-1N1S-6T          17.3.2                       250M                      1G                        2G
(default 250M)




                                                                                                                              19
```

## PDF page 20

```text
PID                         Introductory release for Throughput without           Throughput with           Throughput with
                            PID                      HSECK9 -                     HSECK9                    HSECK9
                                                     bi-directional
                                                                                  (>=17.3.2 and <17.8.1a, (>17.8.1a, aggregate)
                                                                                  bi-directional)

C8300-2N2S-4T2X             17.3.2                     250M                       unthrottled               unthrottled
(default 250M)

C8200-1N-4T                 17.4.1a                    250M                       500M                      1G
(default 250M)

C8200L-1N-4T                17.5.1a                    250M                       250M                      500M
(default 250M)

C8500-12X4QC                17.3.2                     unthrottled                unthrottled               unthrottled
(default unthrottled)

C8500-12X                   17.3.2                     unthrottled                unthrottled               unthrottled
(default unthrottled)

C8500L-8S4X                 17.4.1a                    unthrott                   unthrottled               unthrottled
(default unthrottled)                                  led

C8500-20X6C                 17.10.1a                   unthrottled                -                         unthrottled
(default T4)



Configure numeric throughput
This task shows you how to change the numeric throughput level. If you do not configure a throughput level, the platform's default
throughput level is effective.
     • Read the sections Numeric and tier-based throughput, on page 11 and Numeric vs. tier-based throughput configuration, on page
       12.
     • Ensure that a boot level license is already configured on the device. Otherwise you will not be able to configure a throughput
       value. See Configure a boot level license, on page 4. In the output of the show version privileged EXEC command, ensure
       that a license is mentioned in the License Level field.
     • If you're configuring throughput greater than 250 Mbps, you must install a Smart Licensing Authorization Code (SLAC) before
       you start with this task. To know how to do this, see Install SLAC for an HSECK9 license, on page 8.
     • You can configure the 250M value with or without an HSECK9 license. The difference is that aggregate throttling is effective if
       HSECK9 is available on the device. For more information, see Release-wise changes in throttling behavior, on page 15.
     • Note the throughput you are entitled to. This is indicated in the Cisco DNA license PID you purchase.


Step 1       show platform hardware throughput level
             Displays the current throughput level on the device.




20
```

## PDF page 21

```text
         In the accompanying example:
            • The show platform hardware throughput crypto sample output is of a physical platform (a C8300-2N2S-4T2X).
              Here the throughput level is throttled at 250M.

         Example:
         Device# show platform hardware throughput crypto
         Current configured crypto throughput level: 250M
              Level is saved, reboot is not required
         Current enforced crypto throughput level: 250M
         Crypto Throughput is throttled at 250M
         Default Crypto throughput level: 10M
         Current boot level is network-advantage

Step 2   configure terminal
         Enters global configuration mode.
         Example:
         Device# configure terminal

Step 3   platform hardware throughput crypto {100M | 10M | 15M | 1G | 2.5G | 250M | 25M | 500M | 50M}
         Configures the throughput level. The displayed throughput options depend on the device.
                    Ensure that a boot level license is configured. Else, the command is not recognized as a valid one on the
                    command line interface.
         Note
         In the accompanying example, 1 Gbps is the throughput that is configured, and the software version running on the device
         is Cisco IOS XE Cupertino 17.8.1a. This means that aggregate throughput throttling applies. After reload, the sum of
         upstream and downstream throughput will not exceed the 2 Gbps limit.
         Example:
         Device(config)# platform hardware throughput crypto ?
           100M 100 mbps bidirectional thput
           10M   10 mbps bidirectional thput
           15M   15 mbps bidirectional thput
           1G    2 gbps aggregate thput
           2.5G 5 gbps aggregate thput
           250M 250 mbps bidirectional thput
           25M   25 mbps bidirectional thput
           500M 1gbps aggregate thput
           50M   50 mbps bidirectional thput
         Device(config)# platform hardware throughput crypto 1G
         % These values don't take effect until the next reboot.
         Please save the configuration.

Step 4   exit
         Exits global configuration mode and returns to privileged EXEC mode.
         Example:
         Device# exit

Step 5   copy running-config startup-config
         Saves your entries in the configuration file.
         Example:




                                                                                                                                21
```

## PDF page 22

```text
             Device# copy running-config startup-config
             Destination filename [startup-config]?
             Building configuration...
             [OK]

Step 6       reload
             Reloads the device.
             Example:
             Device# reload

Step 7       show platform hardware throughput level
             Displays the current throughput level on the device.
                        You can also enter the show platform hardware qfp active feature ipsec state privileged EXEC command
                        to display the configured throughput level.
             Tip
             Example:
             Device# show platform hardware throughput crypto
             Current configured crypto throughput level: 1G
                  Level is saved, reboot is not required
             Current enforced crypto throughput level: 1G
             Crypto Throughput is throttled at 2G(Aggregate)
             Default Crypto throughput level: 10M



Configure tier-based throughput
This task shows you how to configure a tier-based throughput level. If you do not configure a throughput level, the platform's default
throughput level is effective.
Tier-based throughput levels are supported starting with Cisco IOS XE Cupertino 17.7.1a release.
Configuration of a throughput level requires a reload on physical platforms.
     • Read the sections Numeric and tier-based throughput, on page 11 and Numeric vs. tier-based throughput configuration, on page
       12.
     • Ensure that a boot level license is already configured on the device. Otherwise you will not be able to configure a throughput
       value. To know how to configure boot level license, see Configure a boot level license, on page 4. In the output of the show
       version privileged EXEC command, ensure that a license is mentioned in the License Level field.
     • If you're configuring Tier 2 (T2) or a higher tier, you must install a Smart Licensing Authorization Code (SLAC) before you
       start with this task. To know how to do this, see Install SLAC for an HSECK9 license, on page 8. T2 or higher tiers are not
       displayed if SLAC is not installed.
     • If you want to configure Tier 3 (T3), ensure that the boot level license is Network Advantage/ DNA Advantage, or Network
       Premier/DNA Premier. T3 and higher tiers are not supported with Network Essentials and DNA Essentials.
     • You can configure the T1 value with or without an HSECK9 license. The difference is that aggregate throttling is effective if
       HSECK9 is available on the device. For more information, see Release-wise changes in throttling behavior, on page 15.
     • Note the throughput you are entitled to. This is indicated in the Cisco DNA license PID you purchase.


Step 1       show platform hardware throughput crypto




22
```

## PDF page 23

```text
         Displays the current throughput level on the device.
         In the accompanying example, the show platform hardware throughput crypto sample output is on C8300-2N2S-4T2X.
         Here, the throughput is currently throttled at 250 Mbps.
         Example:
         Device# show platform hardware throughput crypto
         show platform hardware throughput crypto
         Current configured crypto throughput level: 250M
              Level is saved, reboot is not required
         Current enforced crypto throughput level: 250M
         Crypto Throughput is throttled at 250M
         Default Crypto throughput level: 10M
         Current boot level is network-premier

Step 2   show license authorization
         (Optional) Displays SLAC information on the product instance.
         In the accompanying example, SLAC is installed on the platform. This is so we can configure T2.
         Example:
         Device# show license authorization
         Overall status:
           Active: PID:C8300-2N2S-4T2X,SN:FDO2250A0J5
               Status: SMART AUTHORIZATION INSTALLED on Mar 02 05:05:19 2022 UTC
               Last Confirmation code: 418b11b3

         Authorizations:
           Router US Export Lic. for DNA (DNA_HSEC):
             Description: U.S. Export Restriction Compliance license for
             DNA based Routers
             Total available count: 1
             Enforcement type: EXPORT RESTRICTED
             Term information:
               Active: PID:C8300-1N1S-4T2X,SN:FDO2250A0J5
                 Authorization type: SMART AUTHORIZATION INSTALLED
                 License type: PERPETUAL
                   Term Count: 1

         Purchased Licenses:
           No Purchase Information Available

Step 3   configure terminal
         Enters global configuration mode.
         Example:
         Device# configure terminal

Step 4   platform hardware throughput crypto {T0 | T1 | T2 | T3 | T4 | T5}
         Configures a tier-based throughput. The throughput options that are displayed depend on the device.
                    Only tiers are mentioned in the command for the sake of clarity. When you enter the command on the CLI,
                    numeric and tier values are displayed, as shown in the accompanying example.
         Note
                       • Ensure that you have configured a boot level license already. Otherwise the command for throughput
                         configuration is not recognized as a valid one on the command line interface.
                       • If you're configuring T2 or a higher tier, you must have SLAC installed. You cannot configure T2 or
                         a higher tier if SLAC is not installed.




                                                                                                                               23
```

## PDF page 24

```text
         In the accompanying example,
            • 1 Gbps is configured, and the software version running on the device is Cisco IOS XE Cupertino 17.8.1a release.
              This means aggregate throughput throttling applies. After reload, the sum of upstream and downstream throughput
              will not exceed the 2 Gbps limit.
            • T2 and higher tiers are displayed, because SLAC is installed. If SLAC is not available, T1 would have been the
              highest tier displayed.
                The software version running on the device is Cisco IOS XE Cupertino 17.8.1a. This means aggregate throughput
                throttling applies. After reload, the sum of upstream and downstream throughput will not exceed the 2 Gbps limit.

         Example:
         Device(config)# platform hardware throughput crypto ?
           100M 100 mbps bidirectional thput
           10M   10 mbps bidirectional thput
           15M   15 mbps bidirectional thput
           1G    2 gbps aggregate thput
           2.5G 5 gbps aggregate thput
           250M 250 mbps bidirectional thput
           25M   25 mbps bidirectional thput
           500M 1gbps aggregate thput
           50M   50 mbps bidirectional thput
           T0    T0(up to 15 mbps) bidirectional thput
           T1    T1(up to 100 mbps) bidirectional thput
           T2    T2(up to 2 gbps) aggregate thput
           T3    T3(up to 5 gbps) aggregate thput

         Device(config)# platform hardware throughput crypto T2
         % These values don't take effect until the next reboot.
         Please save the configuration.
         *Mar 02 05:06:19.042: %CRYPTO_SL_TP_LEVELS-6-SAVE_CONFIG_AND_RELOAD:
         New throughput level not applied until reload; please save config

         OR
         Device(config)# platform hardware throughput level MB ?
           100    Mbps
           1000   Mbps
           10000 Mbps
           15     Mbps
           25     Mbps
           250    Mbps
           2500   Mbps
           50     Mbps
           500    Mbps
           5000   Mbps
           T0     Tier0(up to 15M throughput)
           T1     Tier1(up to 100M throughput)
           T2     Tier2(up to 1G throughput)
           T3     Tier3(up to 10G throughput)
           T4     Tier4(unthrottled)

Step 5   exit
         Exits global configuration mode and returns to privileged EXEC mode.
         Example:
         Device# exit

Step 6   copy running-config startup-config
         Saves your entries in the configuration file.




24
```

## PDF page 25

```text
            Example:
            Device# copy running-config startup-config
            Destination filename [startup-config]?
            Building configuration...
            [OK]

Step 7      reload
            Reloads the device.
            Example:
            Device# reload

Step 8      show platform hardware throughput crypto
            Displays the current throughput level on the device.
            In the accompanying example, the tier value is set to T2. You can also enter the show platform hardware qfp active
            feature ipsec state privileged EXEC command to display the configured throughput level.
            Example:
            Device# show platform hardware throughput crypto
            Current configured crypto throughput level: T2
                 Level is saved, reboot is not required
            Current enforced crypto throughput level: 1G
            Crypto Throughput is throttled at 2G(Aggregate)
            Default Crypto throughput level: 10M
            Current boot level is network-premier



Convert a numeric throughput value to tier-based
This task shows you how to convert a numeric throughput value to a tier-based throughput value. To know how numeric throughput
values are mapped to tier values, see: Tier and numeric throughput mapping, on page 13 .
Converting the throughput level requires a reload.
   • Read the Numeric vs. tier-based throughput configuration, on page 12 section.
   • Ensure that a SLAC is installed on the device if you're converting a numeric throughput that is equal to or greater than 250 Mbps.
     To know how to install SLAC, see Install SLAC for an HSECK9 license, on page 8.
   • Ensure that the software version running on the device is Cisco IOS XE Cupertino 17.7.1a or a later release.


Step 1      show platform hardware throughput crypto
            Displays the currently running throughput on the device.
            Example:
            Device# show platform hardware throughput crypto
            Current configured crypto throughput level: 500M
                 Level is saved, reboot is not required
            Current enforced crypto throughput level: 500M
            Crypto Throughput is throttled at 500M
            Default Crypto throughput level: 10M
            Current boot level is network-premier

Step 2      license throughput crypto auto-convert
            Converts the numeric throughput to a tier-based throughput value. The converted tier value is displayed on the CLI.




                                                                                                                                    25
```

## PDF page 26

```text
         Example:
         Device# license throughput crypto auto-convert
         Crypto throughput auto-convert from level 500M to T2

         % These values don't take effect until the next reboot.
         Please save the configuration.
         *Dec 8 03:21:01.401: %CRYPTO_SL_TP_LEVELS-6-SAVE_CONFIG_AND_RELOAD:
         New throughput level
         not applied until reload; please save config

Step 3   copy running-config startup-config
         Saves your entries in the configuration file.
                    Even though the command you use to convert from numeric to tier-based throughput is a privileged EXEC
                    command, it changes running configuration from a numeric value to a tier-based value. You must therefore
         Note       save the configuration for the next reload to be displayed with a tier value.

         Example:
         Device# copy running-config startup-config
         Destination filename [startup-config]?
         Building configuration...
         [OK]

Step 4   reload
         Reloads the device.
         Example:
         Device# reload
         Proceed with reload? [confirm]
         *Dec 8 03:24:09.534: %SYS-5-RELOAD: Reload requested by console.
         Reload Reason:
         Reload Command

Step 5   show platform hardware throughput crypto
         Displays the currently running throughput on the device.
         Example:
         Device# show platform hardware throughput crypto
         Current configured crypto throughput level: T2
              Level is saved, reboot is not required
         Current enforced crypto throughput level: 1G
         Crypto Throughput is throttled at 1G
         Default Crypto throughput level: 10M
         Current boot level is network-premier

Step 6   license throughput crypto auto-convert by entering the
         Verifies whether the conversion is complete.
                    To cross-check whether the conversion is complete, you can also enter the conversion command again. If
                    the numeric throughput value has already been converted, the system displays a message confirming this.
         Tip
         Example:
         Device# license throughput crypto auto-convert
         Crypto throughput is already tier based, no need to convert.




26
```

## PDF page 27

```text
Upgrade from numeric throughput to tier-based throughput
If you're upgrading to Cisco IOS XE Cupertino 17.7.1 or a later release, and the license PID is a tier-based one, you can convert
throughput configuration to a tier-based value. You can also retain the numeric throughput configuration.

       Note

There is no functional impact if you have a tier-based license PID in Cisco SSM and you configure a numeric throughput value on
your device.

If you want to convert to a tier-based value note the required action depending on the throughput level that is configured:

Throughput configuration before          Action before upgrade                    Action after upgrade to 17.7.1 or later
upgrade

Lesser than 250 Mbps                     No action required.                      Convert a numeric throughput value to tier-based,
                                                                                  on page 25

Equal to 250 Mbps                        Obtain an HSECK9 license and install Convert a numeric throughput value to tier-based,
                                         SLAC if you want to convert to T2.   on page 25

Greater than 250 Mbps                    No action required.                      Convert a numeric throughput value to tier-based,
                                                                                  on page 25


Downgrade tier-based throughput to numeric throughput
If you're downgrading to a release where only numeric throughput configuration is supported, you must convert tier-based throughput
configuration to a numeric throughput value before you perform the downgrade. This is applicable even if the license PID is a
tier-based license PID.

       Caution

If you configured a tier-based throughput value before you performed a downgrade, and the downgrade goes through, the tier-based
configuration is not recognized by a pre-17.7.1 image. The configuration fails, and the throughput is not restored to the pre-downgrade
level. In this scenario, you must configure a numeric throughput level after the downgrade is complete.

Throughput configuration before               Action before downgrade                      Action after downgrade to a pre-17.7.1
downgrade                                                                                  version

Numeric                                       No action required.                          No action required.

Tier                                          Configure numeric throughput, on page 20 No action required.


Crypto throughput logging
From Cisco IOS XE 17.18.1a, network administrators can monitor and manage crypto throughput drops. This feature introduces
syslog messages that notify you when a drop in crypto throughput occurs. This offers better visibility and improves management.
This enhancement involves generating a rate-limited syslog to prevent flooding. The syslog message is displayed once every 24 hours
at the first occurrence of a crypto throughput drop. Even if multiple drops occur on the same day, it logs only one message. Any
further syslog notifications will only appear if another drop happens after a full 24-hour interval. You can use the show loggingcommand
to view these messages and confirm that crypto throughput drops are monitored.




                                                                                                                                     27
```

## PDF page 28

```text
The syslog message generated is:
*Nov 28 10:48:48.606: %IPSEC-3-DROP_POLICY_EXCEEDED: F0: cpp_cp_svr:
Throughput policy exceeded. <AGGR_CRYPTO_THRPUT_POLICY_DROP> : <0>,
interface: <Tunnel1>, aggregate: <on> QFP:0.0 Thread:<000 TS:00000004038669236232


Supported platforms
These Cisco Catalyst 8200 and 8300 Edge Platform models support Crypto Throughput drop messages.
     • C8300-2N2S-6T
     • C8300-1N1S-6T
     • C8200-1N-4T
     • C8200L-1N-4T



Report license usage
After you configure your license level and throughput, you should be able to use the features associated with your license. The next
step is to monitor your license usage to account for or report the licenses that you use, to Cisco. For this, you have to send a RUM
report (Resource Utilization Measurement Report) to Cisco SSM to report license usage information.
To know if reporting is required, wait for a system message or refer to the policy using show commands.
     • If reporting is required, the system displays the message: %SMART_LIC-6-REPORTING_REQUIRED: A Usage report
       acknowledgment will be required in [dec] days. Here, [dec] is the amount of time (in days) left to meet reporting requirements.
     • If you're using show commands, refer to the output of the show license status privileged EXEC command and check the Next
       ACK deadline field. This means a RUM report must be sent and the acknowledgment (ACK) from Cisco SSM must be installed
       by this date.

How you send the RUM report depends on the topology you have implemented in the Smart Licensing Using Policy environment.
For more information on sending RUM reports based on your implementation, see How to Configure Smart Licensing Using Policy:
Workflows by Topology.The following sections tell you how to monitor the license usage as per the license model.

Smart Licensing Using Policy
With this licensing model, you purchase the licenses you want to use, configure them on the device, and then report license usage,
as required. You do not have to complete any licensing-specific operations, such as registering or generating keys before you start
using the software and the licenses that are tied to it; unless you're using export-controlled and enforced licenses.
For more information, see Smart Licensing Using Policy for Cisco Enterprise Routing Platforms.

Managed Service Licensing Agreement
A Managed Service License Agreement (MSLA) is a buying program agreement, designed for Service Providers.
     • MSLA in Cisco SD-WAN controller mode
      In the Cisco SD-WAN controller mode, an MSLA is supported on all products in the Cisco Catalyst 8000 Edge Platforms Family.
      For more information, see:
      Managed Service Licensing Agreement (MSLA) for Cisco SD-WAN At-a-Glance
      Cisco SD-WAN Getting Started Guide → Manage Licenses for Smart Licensing Using Policy.




28
```

## PDF page 29

```text
 Cisco vManage How-Tos for Cisco IOS XE SD-WAN Devices → Manage Licenses for Smart Licensing Using Policy.
• MSLA in autonomous mode
 MSLA is not supported on Cisco Catalyst 8200, 8300, and 8500 platforms in autonomous mode.




                                                                                                             29
```
