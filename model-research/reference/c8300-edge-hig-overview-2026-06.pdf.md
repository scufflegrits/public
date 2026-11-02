# c8300-edge-hig-overview-2026-06.pdf — extracted text

- Source PDF: [c8300-edge-hig-overview-2026-06.pdf](c8300-edge-hig-overview-2026-06.pdf)
- PDF title metadata: Overview
- Publisher: Cisco (as registered in the research source entries).
- Source SHA-256: `58fb105b14b5a2c76020077a5113f3adfcd883555f9d48ce4bb5f380e1e319b5`
- Converted: 2026-10-31 (UTC).
- Extraction tool: `pdftotext version 25.03.0`.
- Command: `pdftotext -layout -enc UTF-8 reference/c8300-edge-hig-overview-2026-06.pdf -`.
- PDF pages: 14; page headings below use PDF page numbers.
- Language: English; no OCR or translation performed.
- Source access date and document revision: see the original source-register entries below; conversion does not update them.
- Source register: [C8300-4T2X-HIG-1](../research-cisco-c8300-1n1s-4t2x-r1.1.0.md#c8300-4t2x-hig-1).
- Source register: [C8300-6T-HIG-1](../research-cisco-c8300-1n1s-6t-r1.1.0.md#c8300-6t-hig-1).

> This is layout-preserving plain-text extraction wrapped in Markdown,
> not a semantic reconstruction of tables. Fixed-width text blocks preserve
> column spacing, but reading order, merged cells, and glyphs can still be
> imperfect. Images, diagrams, and image-based tick marks are not transcribed.
> Verify consequential table values against the linked original PDF.

## PDF page 1

```text
  Overview
  The Cisco Catalyst 8300 Series Edge Platforms are best-of-breed, 5G-ready, cloud edge platforms designed
  for accelerated services, multi-layer security, cloud-native agility, and edge intelligence to accelerate your
  journey to cloud.
  Cisco Catalyst 8300 Series Edge Platforms with Cisco IOS XE SD-WAN Software deliver Cisco’s secure,
  cloud-scale SD-WAN solution for the branch. The Cisco Catalyst 8300 Series Edge Platforms is built for high
  performance and integrated SD-WAN Services along with flexibility to deliver security and networking
  services together from the cloud or on premises. It provides higher WAN port density and a redundant power
  supply capability. The Cisco Catalyst 8300 Series Edge Platforms have a wide variety of interface options to
  choose from—ranging from lower and higher module density with backward compatibility to a variety of
  existing WAN, LAN, LTE, voice, and compute modules. Powered by Cisco IOS XE, fully programmable
  software architecture, and API support, these platforms can facilitate automation at scale to achieve zero-touch
  IT capability while migrating workloads to the cloud. The Cisco Catalyst 8300 Series Edge Platforms also
  come with Trustworthy Solutions 2.0 infrastructure that secures the platforms against threats and vulnerabilities
  with integrity verification and remediation of threats.
  The Cisco Catalyst 8300 Series Edge Platforms are well suited for medium-sized and large enterprise branch
  offices for high WAN IPSec performance with integrated SD-WAN services.
  Cisco Catalyst 8300 Series Edge Platforms target these use cases:
       • Enterprise Branch office, Managed Service Provide CPE, Internet Gateway for DIA, SASE cloud platform
         with SD-WAN
       • Next-generation of Software Defined (SD) Branch routing platforms

  For more information on the features and specifications, refer to the Cisco Catalyst 8300 Series Edge Platforms
  datasheet.



Note    Sections in this documentation apply to all models of Cisco Catalyst 8300 Series Edge Platforms unless a
        reference to a specific model is made explicitly.

  The support for the Hyperthreading (HT) for the data plane Packet Processing Engine is added on the following
  platforms:
       • C8300-2N2S-4T2X
       • C8300-2N2S-6T
       • C8300-1N1S-4T2X




                                                                                         Overview
                                                                                                            1
```

## PDF page 2

```text
                                                                                                                          Overview
 Chassis Views




                         • C8300-1N1S-6T
                    This chapter contains the following sections:
                         • Chassis Views, on page 2
                         • Locating Labels on Cisco Catalyst 8300 Series Edge Platforms, on page 6
                         • Hardware Features of Cisco Catalyst 8300 Series Edge Platforms, on page 9


Chassis Views
                    This section contains views of the Power Supply and I/O sides of the Cisco Catalyst 8300 Series Edge Platforms,
                    showing the locations of power and signal interfaces, module slots, status indicators, and chassis identification
                    labels:
                    Cisco Catalyst 8300 Series Edge Platforms are available in these models:
                         • C8300-1N1S-4T2X
                         • C8300-1N1S-6T
                         • C8300-2N2S-4T2X
                         • C8300-2N2S-6T




                  Note      N=Network Interface Modue, S=Services Module, and T=Gigabit Ethernet, X=Ten Gigabit


                    Figure 1: C8300-1N1S-4T2X|6T Chassis - I/O Side




                    Table 1: I/O Side


                     1 LED                                                   2 RJ-45 Gigabit Ethernet port (1G 0/0/0)

                     3 RJ-45 Gigabit Ethernet port (1G 0/0/2)                4 SFP+/10 Gigabit Ethernet port (10G 0/0/4)
                                                                                SFP/1 Gigabit Ethernet port (1G 0/0/4)

                     5 NIM Slot1                                             6 SM Slot1

                     7 RFID (Optional)                                       8 USB Type C (3.0) (USB 1)




                 Overview
      2
```

## PDF page 3

```text
Overview




            9 USB Type A (3.0) (USB 0)                                    10 RJ-45 Console

           11 Micro-USB Console                                           12 RJ-45 Gigabit Ethernet port (1G 0/0/1)

           13 RJ-45 Gigabit Ethernet port (1G 0/0/3)                      14 SFP+/10 Gigabit Ethernet port (10G 0/0/5)
                                                                             SFP/1 Gigabit Ethernet port (1G 0/0/5)

           15 M.2 USB/NVMe storage                                        16 Device Label Tray

           Figure 2: C8300-1N1S-4T2X|6T Chassis - PSU/Fan Tray Side




           Table 2: PSU/Fan Tray Side


           1 AC/DC power supply unit (PSU1) 2 Power, Preset, OK, LED

           3 ALARM Fail LED                              4 Ground lug

           5 Fan tray vent                               6 3-Internal Fan tray

           7 PIM Slot 1                                  8 Power switch

           9 AC/DC Power Supply Unit (PSU0)

           Figure 3: C8300-2N2S-4T2X|6T Chassis - I/O Side




           Table 3: I/O Side


           1 USB Type A (3.0) (USB 0)                                       2 LED




                                                                                                      Overview
                                                                                                                         3
```

## PDF page 4

```text
                                                                                                         Overview




        3 RJ-45 Console                                           4 RJ-45 Gigabit Ethernet port (1G 0/0/0)

        5 RJ-45 Gigabit Ethernet port (1G 0/0/2)                  6 SFP+/10 Gigabit Ethernet port (10G 0/0/4) for
                                                                    C8300-2N2S-4T2X
                                                                    SFP/1 Gigabit Ethernet port (1G 0/0/4) for
                                                                    C8300-2N2S-6T

        7 M.2 USB/NVMe storage                                    8 NIM Slot 1

        9 NIM Slot 2                                              01 PIM Slot 1

        11 RFID (Optional)                                        21 SM Slot 2

        31 Device label tray                                      41 SM Slot 1

        51 SFP+/10 Gigabit Ethernet port (10G 0/0/5) for          61 RJ-45 Gigabit Ethernet port (1G 0/0/3)
           C8300-2N2S-4T2X
           SFP/1 Gigabit Ethernet port (1G 0/0/5) for
           C8300-2N2S-6T

        71 RJ-45 Gigabit Ethernet port (1G 0/0/1)                 81 Micro-USB Console

        91 USB Type C(3.0) (USB 1)

       Figure 4: C8300-2N2S-4T2X|6T Chassis - PSU/Fan Tray Side




       Table 4: PSU/Fan Tray Side


        1 Ground Lug            2 FRU Fan tray

        3 Power Switch          4 PSU0 Power LED

        5 PSU0                  6 POE Power Module 0/1, behind removable Fan tray

        7 PSU1 Power            8 PSU1
          LED

       For detailed information on LEDs, see the section on LED indicators.




    Overview
4
```

## PDF page 5

```text
 Overview
                                                                                                    Platform Summary




Platform Summary
              The figure below shows the internal view of Cisco Catalyst 8300 Series Edge Platforms with components and
              module locations.
              Figure 5: Platform Summary of C8300-1N1S-4T2X|6T




               1 DIMM 2 CPU

               3 NIM       4 M.2 card
                 slot        slot

               5 SM




                                                                                               Overview
                                                                                                                 5
```

## PDF page 6

```text
                                                                                                                              Overview
  Locating Labels on Cisco Catalyst 8300 Series Edge Platforms




                        Figure 6: Platform Summary of C8300-2N2S-4T2X|6T Chassis




                         1 DIMMs            2 CPU

                         3 M.2 Card         4 Label
                           slot               tray

                         5 SM               6 NIM

                         7 PIM



Locating Labels on Cisco Catalyst 8300 Series Edge Platforms
                        Use the Cisco Product Identification (CPI) tool to find labels on the platform. The tool provides detailed
                        illustrations and descriptions of where labels are located on Cisco products. It includes the following features:
                            • A search option that allows browsing for models by using a tree-structured product hierarchy
                            • A search field on the final results page that makes it easier to look up multiple products
                            • End-of-sale products clearly identified in results lists

                        The tool streamlines the process of locating serial number labels and identifying products. Serial number
                        information expedites the entitlement process and is required for access to support services.


Location of labels on Cisco Catalyst 8300 Series Edge Platforms
                        The figure below shows the location of the labels on the Cisco Catalyst 8300 Series Edge Platforms. Labels
                        are located at the same location on all the Cisco Catalyst 8300 Series Edge Platforms




                    Overview
       6
```

## PDF page 7

```text
Overview
                                                                Location of labels on Cisco Catalyst 8300 Series Edge Platforms




             The Serial number (SN), Common language equipment identifier (CLEI), Top Assembly Number (TAN),
             Product ID (PID), PID version ID (VID), and Quick response (QR) code are printed on a label on the back
             of the platform or on a label tray located on the chassis.



           Note   The RFID tags on the devices are pre-fitted and does not come with spare RFID tags.

             Figure 7: Label Location on a C8300-1N1S-4T2X|6T




             1 SN         2 CLEI

             3 TAN        4 MAC

             5 PIDVID 6 QR
                        code




                                                                                                      Overview
                                                                                                                            7
```

## PDF page 8

```text
                                                                                                                    Overview
   Locate Product Identification Details




                          Figure 8: Label Location on a C8300-2N2S-4T2X|6T




                           1 SN            2 CLEI

                           3 TAN           4 MAC

                           5 PIDVID 6 QR
                                      code


Locate Product Identification Details

                          Software License
                          The serial number (SN), product ID (PID), version ID (VID), and Common Language Equipment Identifier
                          (CLEI) are printed on a label on the bottom of the device or on the label tray.




                      Overview
        8
```

## PDF page 9

```text
 Overview
                                                                      Hardware Features of Cisco Catalyst 8300 Series Edge Platforms




                  To obtain a software license, you need the unique device identifier (UDI) of the device where the license is
                  to be installed.
                  The UDI has two main components:
                      • Product ID (PID)
                      • Serial number (SN)

                  The UDI can be viewed using the show license udi command in privileged Exec mode in Cisco Internet
                  Operating System (IOS) software.
                  For additional information on the UDI, see the << >>document on cisco.com.



Hardware Features of Cisco Catalyst 8300 Series Edge Platforms
                  This section describes the hardware features of Cisco Catalyst 8300 Series Edge Platforms


Built-In Interface Ports
                  The Cisco Catalyst 8300 Series Edge Platforms have multiple 10/100/1000 front panel ports and Small Form
                  Pluggables.



            Warning    To comply with the Telcordia GR-1089 NEBS standard for electromagnetic compatibility and safety, connect
                       the Management Ethernet ports only to intra-building or unexposed wiring or cable. The intra-building cable
                       must be shielded and the shield must be grounded at both ends. The intra-building port(s) of the equipment
                       or subassembly must not be metallically connected to interfaces that connect to the OSP or its wiring. These
                       interfaces are designed for use as intra-building interfaces only (Type 2 or Type 4 ports as described in
                       GR-1089-CORE) and require isolation from the exposed OSP cabling. The addition of Primary Protectors in
                       not sufficient protection in order to connect these interfaces metallically to OSP wiring.


GE or SFP Ports
                  The following GE and SFP ports are available on the Catalyst 8300 series edge platforms:

                  GE Ports
                  The GE RJ-45 copper interface ports support 10BASE-T, 100BASE-TX, and 1000BASE-T.

                  SFP Ports
                  The small-form-factor pluggable (SFP) ports support 1Gbps SFP modules.

                  SFP+ Ports
                  The enhanced small-form-factor pluggable (SFP) ports support 10 Gbps SFP+ modules.




                                                                                                            Overview
                                                                                                                                 9
```

## PDF page 10

```text
                                                                                                                           Overview
  Removable and Interchangeable Modules and Cards




Removable and Interchangeable Modules and Cards
                      Service Modules (SMs), Network Interface Modules (NIMs), Pluggable Interface Modules (PIMs) and M.2
                      USB/NVMe storage fit into external slots and can be removed or replaced without opening the chassis.

                      External Slots
                           • Service Modules
                           • Network Interface Modules
                           • Pluggable Interface Modules
                           • M.2 USB/NVMe storage




                    Note      The LTE Pluggable Interface Module interfaces with the host CPU through the USB3.0 interface. The host
                              then accesses the LTE related signals through the I2C interface of the pluggable module.


                      Internal Slots
                           • Memory

                      See the Cisco Catalyst 8300 Series Edge Platforms product page on cisco.com for a list of supported modules
                      and interface cards.


Memory
                      Cisco Catalyst 8300 Series Edge Platforms contain DIMMs that store running configuration and routing tables,
                      and are used for packet buffering by the network interfaces.
                           • Boot/NVRAM—Stores the bootstrap program (ROM monitor) and the configuration register. The
                             boot/NVRAM is not serviceable.
                           • Internal memory—Internal bootflash memory
                           • Removable M.2 card—Available in 16GB (default), 32GB M.2 USB and 600GB M.2 NVMe SSD
                           • DRAM options
                                 • 1x 8GB DDR4 (default)
                                 • 1x 16GB DDR4 (upgrade)
                                 • 1x 32GB DDR4 (upgrade)



Power Supply
                      The Cisco Catalyst 8300 Series Edge Platforms support a variety of power supply configurations. These
                      devices have power supplies that are field replaceable and externally accessible. The following table summarizes
                      the power options:




                   Overview
      10
```

## PDF page 11

```text
  Overview
                                                                                  LEDs for Cisco Catalyst 8300 Series Edge Platforms




Table 5: Field Replaceable Unit Power Options


Model                   AC Input         PSU with Integrated   PoE Power Supply     Dual, Hot           DC Input
                        PSU              PoE                   Converter            Swap                PSU

C8300-1N1S-4T2X Y                        Y                     N                    Y                   Y

C8300-1N1S-6T           Y                Y                     N                    Y                   Y

C8300-2N2S-4T2X Y                        N**                   Y                    Y                   Y

C8300-2N2S-6T           Y                N**                   Y                    Y                   Y




                         Note     **PoE with AC PSU+ a separate PoE adapter.



LEDs for Cisco Catalyst 8300 Series Edge Platforms
                            Table 6: LEDs Indicators


                            LED                                Color                          Description

                            Logo                               Blue                           Cisco Logo LED
                                                                                              Off: The system is powered off
                                                                                              Blue: The system is powered on

                            PWR                                Green/Amber                    Power Supply Status
                                                                                              Off: The system is powered off
                                                                                              Yellow: A Power Supply in the
                                                                                              system is not functioning correctly
                                                                                              Green: All installed PSUs are
                                                                                              operating correctly

                            STATUS                             Green/Amber/Red                System Status
                                                                                              Red: The system is booting
                                                                                              Red Blinking Red: The system has
                                                                                              failed a hardware integrity error
                                                                                              Yellow: Rommon has completed
                                                                                              booting and system is at Rommon
                                                                                              prompt or booting platform
                                                                                              software.
                                                                                              Green: Normal System Operation




                                                                                                            Overview
                                                                                                                                 11
```

## PDF page 12

```text
                                                                                                                              Overview
   Fans, Ventilation, and Airflow




                           LED                                 Color                                Description

                           ENV                                 Green/Amber/Red                      Environmental Status
                                                                                                    Off: Monitor is not active.
                                                                                                    Red: The system has detected a
                                                                                                    critical overcurrent event and may
                                                                                                    shut down.
                                                                                                    Blinking Yellow: One or more
                                                                                                    temperature sensors in the system
                                                                                                    are outside the acceptable range.
                                                                                                    Yellow: One or more fans in the
                                                                                                    system are outside the acceptable
                                                                                                    range.
                                                                                                    Green: All temperature sensors and
                                                                                                    fans in the system are within
                                                                                                    acceptable range.

                           USB CON                             Green                                USB Console Active
                                                                                                    Green indicates that the active
                                                                                                    console port is USB.

                           RJ-45 CON                           Green/Yellow                         Serial Console Active
                                                                                                    Green indicates that RJ-45 is the
                                                                                                    active console port.

                           SFP EN                              Green                                SFP Enable LED
                                                                                                    SFP+ Enable LED
                                                                                                    Off: Not present
                                                                                                    Green: The SFP is supported and
                                                                                                    no faults.
                                                                                                    Amber: The SFP is not supported
                                                                                                    or is in a faulty state

                           SFP LINK                            Green                                SFP port 0/1 Link LED
                                                                                                    Off: No Link (or not present)
                                                                                                    Green: Link established



Fans, Ventilation, and Airflow
Chassis Ventilation
                          The chassis temperature is regulated with internal fans. An onboard temperature sensor controls the fan speed.
                          The fans are always on when the device is powered on. Under all conditions, the fans operate at the slowest




                      Overview
        12
```

## PDF page 13

```text
 Overview
                                                                                 Slots, Subslots-Bay, Ports, and Interfaces




             speed possible to conserve power and reduce noise. When necessary, the fans operate at higher speeds under
             conditions of higher ambient temperature and altitude.
             Figure 9: Airflow of C8300-1N1S-4T2X|6T




             Figure 10: Airflow of C8300-2N2S-4T2X|6T




Slots, Subslots-Bay, Ports, and Interfaces
             The Cisco Catalyst 8300 Series Edge Platforms support interface modules: Service Modules (SM) and Network
             Modules (NIMs) and Pluggable Interface Modules (PIMs).




                                                                                                  Overview
                                                                                                                        13
```

## PDF page 14

```text
                                                                                                                                Overview
    Slot Numbering




                        Figure 11:




                        In all cases, the device designates its interfaces using a 3-tuple notation that lists the slot, bay, and port. The
                        3-tuple value is zero based. An example of a 3-tuple is 0/1/2. This refers to slot 0, the second bay in slot 0
                        (the first bay is 0 so the second bay is 1), and the third port in bay 1. See the following table for more examples.

                        Table 7: Slot, Subslot-Bay and Port Numbering


                         3-Tuple            Slot                   Bay                    Port
                         Example

                         0/1/2              0                      2nd                    3rd

                         0/0/1              0                      1st                    2nd

                         1/1/1              1                      2nd                    2nd

                             • Slots and bays are numbered from the left to the right, and from the top to the bottom.
                             • The two USB ports are named USB0 and USB1. They do not have slot or bay numbers.




                      Note      USB0 and USB1 can be used to insert flash drives.


Slot Numbering
                        Slots are numbered 0, 1, and 2.

About Slot 0
                        The following are the main features of Slot 0:
                             • Slot 0 is reserved for integrated ports and NIMs, it can be used for either SM or NIM.
                             • NIMs are designated by the number of the first slot that they occupy. A double-wide SM occupies two
                               slots, but its designation is only the left-most slot number.
                             • The ten GE ports (or native interface ports) always reside in slot 0 and bay 0. The ports are called
                               Gigabitethernet 0/0/0, Gigabitethernet 0/0/1, Gigabitethernet 0/0/2, and Gigabitethernet 0/0/3 (up to as
                               many ports supported on the particular router).


Subslot and Bay Numbering
                             • Integrated devices, also known as integrated ports or FPGEs, and NIMs reside in a fixed section of bay
                               0.
                             • Motherboard NIMs bays start at bay 1 because the integrated devices and integrated NIMs take up bay
                               0.




                     Overview
        14
```
