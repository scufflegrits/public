# c8000-secure-routers-faq-2026-06.pdf — extracted text

- Source PDF: [c8000-secure-routers-faq-2026-06.pdf](c8000-secure-routers-faq-2026-06.pdf)
- PDF title metadata: Cisco 8000 Series Secure Routers FAQ
- Publisher: Cisco (as registered in the research source entries).
- Source SHA-256: `e12c4e8ca72a28227ed674f56b1feefb56c933f66918efcedf64cd4096d292ce`
- Converted: 2026-10-31 (UTC).
- Extraction tool: `pdftotext version 25.03.0`.
- Command: `pdftotext -layout -enc UTF-8 reference/c8000-secure-routers-faq-2026-06.pdf -`.
- PDF pages: 16; page headings below use PDF page numbers.
- Language: English; no OCR or translation performed.
- Source access date and document revision: see the original source-register entries below; conversion does not update them.
- Source register: [C8375-FAQ-1](../research-cisco-c8375-e-g2-r1.1.0.md#c8375-faq-1).

> This is layout-preserving plain-text extraction wrapped in Markdown,
> not a semantic reconstruction of tables. Fixed-width text blocks preserve
> column spacing, but reading order, merged cells, and glyphs can still be
> imperfect. Images, diagrams, and image-based tick marks are not transcribed.
> Verify consequential table values against the linked original PDF.

## PDF page 1

```text
FAQ Cisco public




Cisco 8000 Series Secure Routers


Overview                                                        Contents
                                                                Overview . ...........................................................................................1
The Cisco® 8000 Series Secure Routers deliver the industry’s
most complete secure networking experience, combining
                                                                Cisco 8000 Series Secure Routers FAQ ..............................................2
cutting-edge security, routing, assurance, and SD-WAN
capabilities in a unified platform. Designed for diverse use    Cisco 8100 Series Secure Routers FAQ . .............................................5
cases—from branches and campuses to data centers—these
secure routers empower businesses to adapt dynamically to       Cisco 8200 and 8300 Series Secure Routers FAQ...............................7
evolving demands. Featuring the all-new secure networking
processor, the customized silicon is built for high-bandwidth   Cisco 8400 and 8500 Series Secure Routers FAQ ............................14
AI/ML workloads while reducing power consumption and
                                                                Cisco 8600 Series Secure Routers FAQ ............................................16
operational costs. The Cisco 8000 Series provides the
foundation for resilient networks that scale with your
business needs.




© 2026 Cisco and/or its affiliates. All rights reserved.
```

## PDF page 2

```text
FAQ Cisco public




Cisco 8000 Series Secure Routers FAQ

Q: What are the Cisco 8000 Series Secure Routers?

A: The Cisco 8000 Series Secure Routers offer a comprehensive range of solutions for modern network architectures. From small branches to large
enterprises, these platforms provide advanced security, SD-WAN capabilities, and high-performance routing to meet diverse business needs.

Q: What is the relative positioning among the various series within the portfolio?

A: Refer to the table below. See the Router Selector for more details on model selection.

Table 1.       Cisco 8000 Series Secure Routers positioning

     Platform                                              Positioning                                              Performance

     Cisco 8100 Series                                     Small branch: Flexible 1GE LAN/WAN secure                IPsec: Up to 1.5 Gbps (512B)
     Secure Routers                                        connectivity including 5G, DSL, XGS-PON options          Threat protection: Up to 1 Gbps (EMIX)

     Cisco 8200 Series                                     Medium-sized branch: Lead series for midsize             IPsec: Up to 5 Gbps (512B)
     Secure Routers                                        organizations, with 1GE, 2.5GE, and 10GE LAN/WAN         Threat protection: Up to 2.4 Gbps (EMIX)
                                                           secure connectivity along with cellular backup options

     Cisco 8300 Series                                     Large branch: Purpose-built for integrated edge          IPsec: Up to 30 Gbps (512B)
     Secure Routers                                        computing and 1GE, 2.5GE, 5GE, and 10GE LAN/WAN          Threat protection: Up to 7 Gbps (EMIX)
                                                           secure connectivity with additional expandability

     Cisco 8400 Series                                     Campus: High-performance 1GE, 10GE, and 25GE             IPsec: Up to 45 Gbps (512B)
     Secure Routers                                        secure connectivity for WAN aggregation                  Threat protection: Up to 10.9 Gbps (EMIX)


     Cisco 8500 Series                                     Data center: Highest-performance 1GE, 10GE, 40GE,        IPsec: Up to 63 Gbps (512B)
     Secure Routers                                        and 100GE secure connectivity for data center hub        IPsec tunnels: 10,000
                                                           access

     Cisco 8600 Series                                     Data center: Highest scale and performance with high     IPsec: Up to 160 Gbps (512B)
     Secure Routers                                        port density 1GE, 10GE, 40GE, and 100GE                  IPsec tunnels: 12,000




© 2026 Cisco and/or its affiliates. All rights reserved.
```

## PDF page 3

```text
FAQ Cisco public




                                                                           •   Cisco TrustSec®
Q: What security solutions are offered with the Cisco 8000 Series
                                                                           •   Identity-based networking (802.1X)
Secure Routers?
                                                                           •   Role-based command-line interface (CLI) access
A: Threat detection, prevention, and response                              •   Access Control Lists (ACLs)
                                                                           •   Authentication and integrity verification
Features designed to detect, prevent, and respond to security threats in
real time:                                                                 Routing and traffic security

• Intrusion Prevention and Detection (IPS/IDS)                             Features that help ensure secure routing, traffic isolation, and mitigation of
• Advanced Malware Protection (AMP)                                        malicious traffic:
• Anomaly detection and machine learning
                                                                           • Virtual route forwarding (VRF)-aware security
Network perimeter security                                                 • Source-based remotely triggered black hole (RTBH) filtering
                                                                           • Unicast reverse path forwarding (RPF)
Features that safeguard the network’s edge and control external access:
                                                                           Infrastructure and control plane protection
•   Enterprise firewall with application awareness
•   Zone-based firewall                                                    Features that protect the control plane and administrative access to devices:
•   Network Address Translation (NAT)
                                                                           • Control plane protection (CoPP)
•   Secure access service edge (SASE) integration
                                                                           • Secure Shell (SSH) v2
Web and DNS security                                                       • Management plane protections

Features that protect users and devices from web-based and DNS-layer       Device and system security
threats:
                                                                           Features that help ensure the integrity, security, and reliability of hardware
• URL filtering                                                            and software:
• DNS web-layer security agent
                                                                           • Secure Boot with signed images and hardware anchoring with Secure
• SSL proxy
                                                                             Unique Device Identity (SUDI)
Identity and access control                                                • Secure storage
                                                                           • Run-time defenses
Features that enforce secure access to the network, administrative         • Recovery mechanisms
interfaces, or resources:




© 2026 Cisco and/or its affiliates. All rights reserved.
```

## PDF page 4

```text
FAQ Cisco public




Q: What is the minimum Cisco IOS® XE Software release for the                 Q: What configuration, management, and monitoring options are
Cisco 8000 Series Secure Routers?                                             available for the Cisco 8000 Series Secure Routers?

A: The Cisco 8000 Series Secure Routers run Cisco IOS XE Software,            A: The 8000 Series Secure Routers can be managed and/or monitored via
which supports routing and SD-WAN. The minimum IOS XE Software                • Cisco Catalyst™ SD-WAN                • Onboard Cisco IOS XE Software
versions are listed in the table below.                                         Manager                                 WebUI
                                                                              • Cisco Catalyst Center                 • NETCONF, RESTCONF, and
Table 2.       Minimum Cisco IOS XE releases
                                                                              • Simple Network Management               YANG models
  Model                                                    Minimum IOS XE       Protocol (SNMP)                       • CLI
                                                           Software version
                                                                              Q: What are the software and licensing options for the Cisco 8000
  C8570-G2, C8550-G2, C8475-G2,                            IOS XE 17.15.3     Series Secure Routers?
  C8455-G2, C8375-E-G2
                                                                              A: There are two distinct licensing and subscription options for routing or
  C8355-G2, C8235-E-G2, C8231-E-G2,                        IOS XE 17.18.1     SD-WAN deployments:
  C8235-G2, C8231-G2, C8161-G2, C8151-G2,
  C8140-G2, C8130-G2                                                          • Routing Essentials (perpetual and included with hardware purchase)
                                                                              • Routing Advantage subscription
  C8130-VAI-G2, C8130-VAP-G2, C8151-                       IOS XE 26.1.1
  CVAI-G2, C8151-CVAP-G2, C8131-G2                                            SD-WAN requires a flexible 12- to 84-month term under the Cisco
                                                                              Networking Subscription with the following benefits:
  C8221-G2, C8225-G2                                       IOS XE 26.1.2
                                                                              • Platform-class licensing: Each platform class is categorized as small,
  C8221L-G2, C8650-G2                                      IOS XE 26.1.3        medium, large, or extra large based on the throughput, performance,
                                                                                and positioning characteristics of the underlying hardware platforms.
  C8211-G2, C8130H-G2, C8151H-C-G2                         IOS XE 26.1.2      • Elimination of bandwidth tiering: Licenses for the next-generation
                                                                                hardware will not be segmented by bandwidth tiers.
Note: The C8130H-G2, C8130-G2, C8130-VAI-G2, C8130-VAP-G2, and                • License portability: Licenses can be managed via Catalyst Center, SD-
C8140-G2 support routing mode only.                                             WAN Manager, or the Cisco Meraki™ dashboard (WAN only).

Q: Which Cisco 8000 Series Secure Routers support Cisco                       • Management: Licenses can be managed via Catalyst Center, SD-WAN
                                                                                Manager, or Meraki dashboard (WAN only).
ThousandEyes®?
                                                                              All SD-WAN license entitlements are subscription-based, with two tiers
A: ThousandEyes is supported on all platforms except models with
                                                                              available: Cisco WAN Essentials and Cisco WAN Advantage.
4GB DRAM.
                                                                              For additional licensing details and capabilities, please visit the Cisco 8000
                                                                              Series Secure Routers WAN and Routing License Feature Matrices.

© 2026 Cisco and/or its affiliates. All rights reserved.
```

## PDF page 5

```text
FAQ Cisco public




Cisco 8100 Series Secure Routers FAQ

Q: What are the different models within the Cisco 8100 Series?             Q: Does the Cisco 8100 Series support a DC power supply?

A: The Cisco 8100 Series Secure Routers consist of the following models:   A: All power supplies are AC-DC. No DC-DC power supplies are supported.
C8130-G2, C8130-VAI-G2, C8130-VAP-G2, C8130H-G2, C8131-G2,
                                                                           Q: Does the Cisco 8100 Series have a power button?
C8140-G2, C8151-G2, C8151-CVAI-G2, C8151-CVAP-G2, C8151H-C-G2,
and C8161-G2. The models have various combinations of WAN interfaces,      A: No. There is no power button on the Cisco 8100 Series Secure Routers.
cellular, Power over Ethernet (PoE), and security options.
                                                                           Q: How many GE WAN ports are available with the Cisco 8100 Series?
Q: Can I upgrade the DRAM and flash?
                                                                           A: The C8130-G2, C8131-G2, come with one RJ-45 1GE WAN port plus
A: No. Neither the DRAM nor the flash are upgradable.                      one RJ-45/SFP 1GE WAN combo port only. The C8140-G2, C8151-G2, and
                                                                           C8161-G2 come with two RJ-45/SFP 1GE WAN ports. The C8130-VAI-G2,
Q: Is the Cisco 8100 Series fanless?
                                                                           C8130-VAP-G2, C8151-CVAI-G2, and C8151-CVAP-G2 come with one RJ-
A: Yes, the Cisco 8100 Series Secure Routers are fanless.                  45/SFP 1GE WAN combo port, one XGS-PON/10G BASE-T port, and one
                                                                           RJ-11 (xDSL) port. C8130H-G2 and C8151H-C-G2 comes with 1x RJ-45
Q: Is the Cisco 8100 Series PoE and PoE+ capable?
                                                                           1GE WAN plus 1 x 10G Copper port.
A: Yes, the C8161-G2 supports either four PoE ports or two PoE+ ports.
                                                                           Q: What are the different mounting options for the Cisco 8100 Series?
Q: What power supplies are used on the Cisco 8100 Series?
                                                                           A: The Cisco 8100 Series platforms can be rack, wall, or desk mounted or
A: The C8130-G2, C8130H-G2, and C8131-G2 can be powered by a 30W           placed on a desktop. When mounting two Cisco 8100 Series routers in a
or 66W AC power supply. The C8130-VAI-G2, C8130-VAP-G2, C8140-G2,          rack, you must leave at least 1RU (1.75 inches, 4.45 cm) of space between
C8151-CVAI-G2, C8151-CVAP-G2, C8151-G2, and C8151H-C-G2 require            the devices for proper ventilation and cooling. This helps ensure that the
a 66W AC PSU. The C8161-G2 requires a 150W AC PSU.                         equipment operates efficiently and reduces the risk of overheating.

Q: Does the Cisco 8100 Series support an external power supply?            Q: Does the Cisco 8100 Series have feature parity with the Cisco ISR
                                                                           1000 Series?
A: All power supplies are external.
                                                                           A: Yes, the Cisco 8100 Series has software feature parity with the Cisco
                                                                           1000 Series Integrated Services Routers (ISR 1000 Series).




© 2026 Cisco and/or its affiliates. All rights reserved.
```

## PDF page 6

```text
FAQ Cisco public




Q: What VPN technologies are supported on the Cisco 8100 Series?            Q: Why are service providers migrating from DSL to XGS-PON, and
                                                                            what additional 10GE options are available?
A: The Cisco 8100 Series supports the following VPN technologies:
FlexVPN, Dynamic Multipoint VPN (DMVPN), Group Encrypted Transport          A: Service providers are moving to XGS-PON to meet increasing
VPN (GETVPN), Site-to-Site VPN, and Multiprotocol Label Switching           bandwidth demands from 4K/8K streaming, cloud applications, video
(MPLS) VPN.                                                                 conferencing, and multiple connected devices, while enabling future use
                                                                            cases such as IoT, smart cities, and 5G backhaul. XGS-PON also reduces
Q: Which Cisco 8100 Series platforms support cellular?
                                                                            operational costs by replacing legacy copper with scalable passive fiber.
A: The C8151-G2 and C8161-G2 platforms support 5G/Cat7 LTE with cellular    In addition, the C8130-VAI/P-G2 and C8151-CVAI/P-G2 platforms support
pluggable interface modules (PIMs). The C8151-CVAI-G2, C8151-CVAP-G2,       an SFP-10G-BASE-T module, providing flexible 10GE WAN connectivity
and C8151H-C-G2 models support embedded 5G Release 17 cellular.             (actual throughput may vary from the full line rate).

Q: Do the Cisco 8100 Secure Routers support dual SIMs?                      Q: What is the primary difference between the C8130H-G2 and
                                                                            C8151H-C-G2 routers?
A: Yes. The PIM supports dual SIMs in active-standby mode in the
C8151-G2 and C8161-G2 models. The C8151-CVAI-G2, C8151-CVAP-G2,             A: The C8130H-G2 focuses on Ethernet routing capabilities, while the
and C8151H-C-G2 support dual nano SIM slots.                                C8151H-C-G2 additionally provides 5G cellular connectivity along with
                                                                            SD-WAN, security, and ThousandEyes features.
Q: Do the Cisco 8100 Secure Routers support eSIM technology?
                                                                            Q: What are the throughput expectations for platforms with 10G
A: Yes, eSIM is supported on the C8151-G2 and C8161-G2 platforms.
                                                                            XGSPON and 10G Copper ports?
Q: Can the Cisco 8100 Series fall back to 4G?
                                                                            A: These platforms support 10G-capable interfaces. However, the actual
A: Yes, the Cisco 8100 Series supports 4G as well, and can fall back from   achievable throughput may be lower, depending on factors such as device
5G to 4G/LTE.                                                               architecture, processing capabilities, and traffic conditions.

Q: What is XGS-PON, and in which platforms is it supported?

A: The C8130-VAI/P-G2 and C8151-CVAI/P-G2 platforms support one
XGS-PON/10GBASE-T WAN port, delivering 10-Gbps symmetric fiber
access for multiuser environments. XGS-PON stands for 10-Gigabit
symmetric passive optical network, providing equal upload and download
speeds over passive fiber infrastructure.




© 2026 Cisco and/or its affiliates. All rights reserved.
```

## PDF page 7

```text
FAQ Cisco public




Cisco 8200 and 8300 Series Secure Routers FAQ

Q: What are the models within the Cisco 8300 and 8200 Series?               Q: What are the key differences between the Catalyst 8300 and 8200
                                                                            Edge Platforms and the Cisco 8300 and 8200 Series Secure Routers?
A: The Cisco 8300 and 8200 Series Secure Routers include the following
models:                                                                     A: The Cisco 8300 and 8200 Series Secure Routers are the next
                                                                            generation of secure WAN appliances, offering the following key benefits:
• C8375-E-G2: Cisco 8300 Series with one service module (SM), one
  network interface module (NIM) slot, one pluggable interface module       •   Higher IPsec performance and scale
  (PIM) slot, two 1GE/10GE Small-Form-Factor Pluggable (SFP) ports, and     •   Higher Cisco Express Forwarding performance
  four Multigigabit Ethernet (2.5GE) RJ-45 WAN ports, with Cisco UPOE®+
                                                                            •   Higher built-in WAN port density
  support on the last two ports.
                                                                            •   Improved backplane connectivity with high-speed connections
• C8355-G2: Cisco 8300 Series with one PIM slot, four 1GE/10GE SFP/
                                                                            •   Fixed and modular DRAM options
  SFP+ ports, four Multigigabit Ethernet (5GE) RJ-45 ports, and two 1GE
  RJ-45 ports, with UPOE+ support on all four Multigigabit ports.           •   256-bit WAN MACsec on all front-panel ports
• C8235-E-G2: Cisco 8200 Series with one PIM slot, one NIM slot, two        •   128-bit LAN MACsec on select models
  1GE/10GE SFP/SFP+ ports, and two Multigigabit Ethernet (2.5GE) RJ-45      • Embedded Layer 2 ports on select models
  ports, with UPOE+ support on both Multigigabit ports.
                                                                            Q: What are the key capabilities of the Cisco 8300 and 8200 Series
• C8321-E-G2: Cisco 8200 Series with one PIM slot, one NIM slot, two
  1GE/10GE SFP/SFP+ ports, and two Multigigabit Ethernet (2.5GE) RJ-45      Secure Routers?
  ports, with UPOE+ support on both Multigigabit ports.
                                                                            A: The Cisco 8300 and 8200 Series Secure Routers offer:
• C8235-G2: Cisco 8200 Series with one PIM slot, two 1GE/10GE SFP/
  SFP+ ports, and eight Multigigabit Ethernet (2.5GE) RJ-45 ports, with     • SD-WAN and SD-Routing capabilities
  UPOE+ support on ports 6-7 and PoE support on ports 4-5.                  • Support for Kernel-based Virtual Machine (KVM) containers, providing
• C8231-G2: Cisco 8200 Series with two 1GE/10GE WAN SFP/SFP+                  support for integrated applications
  ports, four Multigigabit Ethernet (2.5GE) RJ-45 ports with PoE+ support   • Support for applications including Snort® IDS/IPS, URL filtering,
  on port 7, and four 1GE RJ-45 ports.                                        advanced malware protection, Cisco Secure Malware Analytics, SSL
• C8225-G2: Cisco 8200 Series with two 1GE/10GE SFP/SFP+ ports and            proxy, and TCP optimization
  eight 1GE RJ-45 ports.                                                    • Open API programmability using NETCONF and YANG
• C8221-G2: Cisco 8200 Series with two 1GE/10GE SFP/SFP+ ports and          • Zero-touch provisioning (ZTP)
  eight 1GE RJ-45 ports.                                                    • Multiple options for WAN, LAN, voice, storage, and edge computing
• C8221L-G2: Cisco 8200 Series with two 10GE RJ-45 ports and eight            (Cisco UCS® E-Series) modules on the Cisco 8300 Series
  1GE RJ-45 ports.                                                          • Multiple options for WAN, LAN, and cellular on the Cisco 8200 Series
• C8211-G2: Cisco 8200 Series with two 1GE RJ-45/SFP combo ports            • Support for border node and control plane node functionalities in Cisco
  and four 1GE RJ-45 ports.                                                   Software- Defined Access (SD-Access)

© 2026 Cisco and/or its affiliates. All rights reserved.
```

## PDF page 8

```text
FAQ Cisco public




• Application quality of experience (AppQoE), TCP optimization, data redundancy elimination (DRE), Forward Error Correction (FEC), and packet
  duplication
• Comprehensive options for wireless WAN through LTE Cat7 and 5G

Q: Will the Cisco 8300 Series Secure Routers provide 100% module parity with the previous generation of platforms?

A: The figure below shows the list of validated modules on the Cisco 8300 Series.

                                                     Expansion Slots : C8375-E-G2                                                                                     Expansion Slots: C8235-E-G2, C8231-E-G2
                                                                   C8375-E-G2
                                                                                                                                                                                                      Slot Type                     Module Type

                                                                                                                                                                                                 Pluggable Interface Module (PIM)   CAT7 LTE, 5G SA
                                                                                                                                                                                                 Network Interface Module (NIM)     LAN, WAN, DSL, ASYNC
                                                                                                                                           C8235-G2 and C8231-G2 have no expansion slots

                                                                                                      NEW! IOS XE 26.1
                                                                                                                                                                                                                                     NEW! IOS XE 26.1


           Ethernet LAN/WAN[1]                  Cellular WANAN[4]             Ethernet LAN/WAN[1]   Ethernet LAN/WAN[1]           Ethernet                                  Cellular
                                                                                                                                                                                                  Digital Voice[4]                     Analog Voice
                                                                                                                                 LAN/WAN[1]                                 WAN[3]
            C-NIM-WAN-4SP            [2]
                                               P-LTEA7-EAL                    NIM-1MFT-T1/E1        NIM-2FXO                  C-NIM-WAN-4S                            P-LTEA7-EAL                NIM-1MFT-T1/E1                      NIM-2FXO
            C-NIM-WAN-2X[2]                    P-LTEA7-NA                     NIM-2MFT-T1/E1        NIM-4FXO                  C-NIM-WAN-2X                            P-LTEA7-NA                 NIM-2MFT-T1/E1                      NIM-4FXO
            C-SM-16P4M2X[3]                    P-LTEA7-JP                     NIM-4MFT-T1/E1        NIM-2FXSP                                                         P-LTEA7-JP                 NIM-4MFT-T1/E1                      NIM-2FXSP
                                               P-5GS6-R16SA-GL                NIM-8MFT-T1/E1        NIM-4FXSP                 C-NIM-4X (2xL3)[2]                                                 NIM-8MFT-T1/E1                      NIM-4FXSP
            C-NIM-4X (2xL3)[3]                                                                                                C-NIM-8T (2xL3)[2]                      P-5GS6-R16SA-GL            NIM-1CE1T1-PRI                      NIM-2FXS/4FXOP
                                                                              NIM-1CE1T1-PRI        NIM-2FXS/4FXOP
            C-NIM-8T (2x L3)[3]                                                                                               C-NIM-8M(2xL3)[2]                                                  NIM-2CE1T1-PRI
                                                                              NIM-2CE1T1-PRI        SM-X-8FXS/12FXO                                                                              NIM-8CE1T1-PRI
            C-NIM-8M(2x L3)[3]
                                                                              NIM-8CE1T1-PRI        SM-X-16FXS/2FXO
                                                                                                    SM-X-24FXS/4FXO]
                                                                                                                                                                                                       End of Life


                                                                                     End of Life                                  TDM WAN                                   ASYNC                       DSL

                                                                                                                               NIM-1T (Serial)                         NIM-16A                    NIM-VAB-A
           Ethernet LAN/WAN[1]                Ethernet LAN/WAN[1]             Ethernet LAN/WAN[1]   Ethernet LAN/WAN[1]        NIM-2T (Serial)                         NIM-24A                    NIM-VA-B
                                                                                                                               NIM-4T (Serial)                                                    NIM-VAM-M
            NIM-16A                            C-SM-NIM-ADPT                  NIM-VAB-A                                                                                                           NIM-4SHDSL-EA
                                                                                                    SM-X-1T3/E3
            NIM-24A                                                           NIM-VA-B
            SM-X-64A                                                          NIM-VAB-M             NIM-1T (Serial)
                                                                              NIM-4SHDSL-EA         NIM-2T (Serial)          [1] MACsec capable modules
                                                                                                    NIM-4T (Serial)          [2] Only one moduel per chassis. C-NIM supported only on NIM slot
                                                                                                                             [3] Same PIM supported on C8235-G2
                                                                                                                             [4] At launch, support for date only
                                                                                                                                 Last supported release: 17.18.1


          [1] MACsec capable modules
          [2] Available starting 17.18.1
          [3] Only one moduel per chassis. C-NIM supported only on NIM slot                                               Figure 2. Validated modules on the Cisco 8200 Series Secure Routers
          [4] Same PIM supported on C8355-G2, C8235-G2
          [5] At launch, support for date only
              Last supported release: 17.18.1




Figure 1. Validated modules on the Cisco 8300 Series Secure Routers




© 2026 Cisco and/or its affiliates. All rights reserved.
```

## PDF page 9

```text
FAQ Cisco public




Q: What are the available onboard Ethernet WAN port options on the                                    Platform               SM                      NIM                     PIM
Cisco 8300 and 8200 Series Secure Routers?
                                                                                                      C8235-E-G2             0                       1                       1
A: The onboard Ethernet WAN port options are outlined in the table below.
                                                                                                      C8235-G2               0                       0                       1
Table 3.       Onboard Ethernet WAN port options on the Cisco 8300 and 8200 Series Secure Routers     C8231-E-G2             0                       1                       1
  Platform                         Gigabit                 Multigigabit      Gigabit                  C8231-G2               0                       0                       0
                                   Ethernet SFP            Ethernet          Ethernet
                                                           RJ-45             RJ-45                  Q: What are the different DRAM configuration options on the Cisco
  C8375-E-G2                       2                       4                 –                      8300 and 8200 Series Secure Routers?

  C8355-G2                         4                       4                 2                      A: DRAM configuration options are shown in the table below.
  C8235-E-G2                       2                       2                 -
                                                                                                    Table 5.   Memory configuration options on the Cisco 8300 and 8200 Series Secure Routers
  C8235-G2                         2                       8                 –
                                                                                                      Platform                    Total default DRAM             DRAM upgrade options
  C8231-E-G2                       2                       2                 -
                                                                                                      C8375-E-G2                  16 GB                          32 GB
  C8231-G2                         2                       4                 4
                                                                                                      C8355-G2                    16 GB                          –
  C8225-G2                         2                       -                 8
  C8221-G2                         2                       -                 8                        C8235-E-G2                  16 GB                          -

  C8221L-G2                        -                       -                 10                       C8235-G2                    16 GB soldered                 –
  C8211-G2                         2                       -                 6                        C8231-E-G2                  8 GB                           -
                                                                                                      C8231-G2                    8 GB soldered                  –
Q: What are the SM and NIM hardware configuration options on the
Cisco 8300 and 8200 Series Secure Routers?                                                            C8225-G2                    16 GB soldered                 -
                                                                                                      C8221-G2                    8 GB soldered                  -
A: The NIM and SM hardware configuration options are shown in the table
below.                                                                                                C8221L-G2                   8 GB soldered                  -

Table 4.       NIM and SM configuration options on the Cisco 8300 and 8200 Series Secure Routers
                                                                                                      C8211-G2                    8 GB soldered                  -

  Platform                         SM                      NIM               PIM                    Note: For the C8375-E-G2, a single dual inline memory module (DIMM)
                                                                                                    configuration is supported. The upgrade option available is one 32-GB DIMM.
  C8375-E-G2                       1                       1                 1
  C8355-G2                         0                       0                 1


© 2026 Cisco and/or its affiliates. All rights reserved.
```

## PDF page 10

```text
FAQ Cisco public




Q: Is Online Insertion and Removal (OIR) supported on the Cisco 8300                      Platform              Type of PSU           Dual         Dual DC       PoE AC
and 8200 Series Secure Routers?                                                                                                       AC                         PSU

A: Yes, OIR is supported on the Cisco 8300 and 8200 Series Secure                         C8231-E-G2            Internal -            Yes          No            Yes
Routers. OIR commands are issued before removing and after installing a                                         Primary
                                                                                                                External -
module. (Example: hw-module subslot 2/0 stop/start)                                                             Secondary (AC
                                                                                                                or DC)
Note: Surprise replacement of the system fan tray is not supported. To
replace the fans, the system has to be powered down prior to the removal                  C8231-G2              External              No           No            Yes
of fans inside the fan tray.                                                              C8225-G2              External              Yes          No            No
Q: Do the Cisco 8300 and 8200 Series Secure Routers support                               C8221-G2              External              Yes          No            No
redundant power supplies?
                                                                                          C8221L-G2             External              Yes          No            No
A: Yes. The Cisco 8300 and 8200 Series support redundant power                            C8211-G2              External              Yes          No            No
supplies.
                                                                                        Q: What front-panel ports are PoE-capable on the Cisco 8300 and
Q: What are the power supply options for the Cisco 8300 and 8200
                                                                                        8200 Series Secure Routers?
Series Secure Routers?
                                                                                        A: The table below outlines the PoE-capable ports in the Cisco 8300 and
A: The available power supply options are detailed in the following table.
                                                                                        8200 Series Secure Routers.
Table 6.       Power supply options for the Cisco 8300 and 8200 Series Secure Routers
                                                                                        Table 7.   PoE-capable ports on the Cisco 8300 and 8200 Series Secure Routers
  Platform                        Type of PSU              Dual   Dual DC     PoE AC
                                                           AC                 PSU         Platform                                     Front-panel ports

  C8375-E-G2                      Internal                 Yes    Yes         Yes         C8375-E-G2                                   Ports 2-3 UPOE+)

  C8355-G2                        External                 Yes    No          Yes         C8355-G2                                     Ports 0-3 (UPOE+)
  C8235-E-G2                      Internal –               Yes    No          Yes         C8235-E-G2                                   Ports 0-1 (UPOE+)
                                  Primary
                                  External –                                              C8235-G2                                     Ports 4-5 (PoE), 6-7 (UPOE+)
                                  Secondary (AC
                                  or DC)                                                  C8231-E-G2                                   Ports 0-1 (UPOE+)

  C8235-G2                        External                 No     No          Yes         C8231-G2                                     Port 7 (PoE+)



© 2026 Cisco and/or its affiliates. All rights reserved.
```

## PDF page 11

```text
FAQ Cisco public




Q: Are solid-state drives (SSDs) supported on the Cisco 8300 and 8200 Series Secure Routers?

A: 600-GB and 2-TB M.2 NVMe SSDs are supported on the Cisco 8300 Series for container-based application hosting services and for general storage
purposes.600-GB E1.S SSDs are supported on the Cisco 8200 Series for container-based application hosting services and for general storage purposes.

Q: Do the front-panel ports on the Cisco 8300 and 8200 Series Secure Routers have Layer 2, Layer 3, or flex capability?

A: The front-panel ports on the Cisco 8300 and 8200 Series Secure Routers provide various connectivity options as listed in the table below.

Table 8.       Connectivity options on the front-panel ports of the Cisco 8300 and 8200 Series Secure Routers

  Platform                                                 WAN Ports                               Flex Ports                      LAN Ports

  C8375-E-G2                                               2x 10GE SFP/SFP+                        -                               –
                                                           4x 2.5GE mGig RJ-45 (2x UPOE+)

  C8355-G2                                                 2x 10GE SFP/SFP+                        2x 5GE mGig RJ-45 (2x UPOE+)    2x 10GE SFP/SFP+
                                                           2x 5GE mGig RJ-45 (2x UPOE+)            2x 1GE RJ-45
  C8235-E-G2                                               1x 10GE SFP/SFP+                        -                               -
                                                           2x 2.5GE mGig RJ-45 92x UPOE+)
  C8235-G2                                                 1x 10GE SFP/SFP+                        2x 2.5GE mGig RJ-45 (1x PoE+)   4x 2.5GE mGig RJ-45
                                                           2x 2.5GE mGig RJ-45 (2x UPOE+)
  C8231-E-G2                                               1x 10GE SFP/SFP+                        -                               -
                                                           2x 2.5GE mGig RJ-45 (2x UPOE+)
  C8231-G2                                                 2x 10GE SFP/SFP+                        2x 2.5GE mGig RJ-45             4x 1GE RJ-45
                                                           2x 2.5GE mGig RJ-45 (1x PoE+)
  C8225-G2                                                 2x 10GE SFP/SFP+                        2x 1GE RJ-45                    4x 1GE RJ-45
                                                           2x 1GE RJ-45
  C8221-G2                                                 2x 10GE SFP/SFP+                        2x 1GE RJ-45                    4x 1GE RJ-45
                                                           2x 1GE RJ-45
  C8221L-G2                                                2x 10GE RJ-45                           2x 1GE RJ-45                    6x 1GE RJ-45

  C8211-G2                                                 2x 1GE RJ-45/SFP combo port             2x 1GE RJ-45                    2x 1G RJ-45



© 2026 Cisco and/or its affiliates. All rights reserved.
```

## PDF page 12

```text
FAQ Cisco public




Q: Do the Cisco 8300 and 8200 Series Secure Routers support                Q: How do the C8211/C8221/C8225-G2 and C8231/C8235-G2 models
EtherChannel?                                                              differ?

A: There is no support for Layer 2 EtherChannels on the onboard ports.     A: All models provide similar levels of throughput and scale. The key
Layer 2 EtherChannels are supported only via the C-SM-16P4M2X              differences are based on the specific requirements of your deployment:
switch module on the C8375-E-G2 platform, both Link Aggregation
                                                                           • The C8231-G2 and C8235-G2 feature integrated PoE and cellular
Control Protocol (LACP) and Port Aggregation Protocol (PAgP). Layer 3
                                                                             capabilities.
EtherChannel is supported on onboard ports and NIMs (including flex
ports for onboard and NIM) and includes only LACP support.                 • The C8211-G2, C8221L-G2, C8221-G2, and C8225-G2 feature power
                                                                             supply redundancy in a small form factor and include post-quantum
Q: What cellular WAN options are available?
                                                                             Secure Boot for enhanced security in medium-sized branch offices.
A: 5G standalone and Cat7 LTE are supported on the Cisco 8300 and
                                                                           Q: Will FXS and FXO NIMs be supported on the Cisco 8300 and 8200
8200 Series Secure Routers in the PIM slot. In addition, these platforms
                                                                           Series?
support Cisco cellular gateways, providing deployment flexibility.
                                                                           A: Yes. FXS/FXO NIM support is planned for all models equipped with NIM
Q: Do the Cisco 8300 and 8200 Series Secure Routers support dual SIMs?
                                                                           slots, including the C8231-E-G2, C8235-E-G2, and C8375-E-G2. Support
A: Yes. The PIM supports dual SIMs in active-standby mode.                 is currently on the roadmap for Release 26.1 in autonomous mode.

Q: Do the Cisco 8300 and 8200 Series Secure Routers support eSIM           Q: Can I use TDM or PRI NIMs for voice services on the 8300 and 8200
technology?                                                                Series platforms?

A: Yes, eSIM is supported.                                                 A: At this time, time-division multiplexing (TDM) and primary rate interface
                                                                           (PRI) NIMs (such as the NIM-xMFT-T1/E1 and NIM-xCE1T1-PRI series) are
Q: What broadband technologies are supported on the Cisco 8300 Series?
                                                                           supported for data-only applications. This applies to the C8231-E-G2,
A: We have NIMs that support multimode VDSL2 and ADSL/2/2+ NIM Annex       C8235-E-G2, and C8375-E-G2. Voice support for these modules is not
A, B, and M. We also support SHDSL capability with the SHDSL NIM.          available at launch and is on the roadmap for a future release for TDM
                                                                           NIMs only (planned for autonomous mode).
Q: Do the Cisco 8300 and 8200 Series Secure Routers have feature
parity with previous generations of Catalyst 8300 and 8200 Series
Edge Platforms?

A: Yes. The Cisco 8300 and 8200 Series Secure Routers have feature
parity with the Catalyst 8300 and 8200 Series Edge Platforms.



© 2026 Cisco and/or its affiliates. All rights reserved.
```

## PDF page 13

```text
FAQ Cisco public




Q: Does the C8375-E-G2 support physical PVDM modules or SM-X-                Cisco 8400 and 8500 Series Secure Routers FAQ
PVDM DSP-Farm modules?
                                                                             Q: What are the Cisco 8400 and 8500 Series Secure Routers?
A: The Cisco 8000 Series Secure Routers are transitioning from
hardware-based packet voice digital signal processors (PVDMs) to virtual     A: The Cisco 8400 Series Secure Routers are designed as campus edge
digital signal processors (vDSPs). Consequently, physical PVDM and           routers to address the transition from 10 Gigabit Ethernet to 25 Gigabit
SM-X-PVDM modules are not supported. vDSP technology provides the            Ethernet at the WAN. These routers are powered by an all-new secure
necessary media resources without requiring dedicated hardware slots.        networking processor (SNP) to accelerate routing, encryption, and threat
                                                                             protection in a compact 1RU form factor.
Q: Which platforms support vDSP, and when will it be available?
                                                                             The Cisco 8500 Series Secure Routers are designed as enterprise
A: vDSP support begins in Release 17.18.2 and requires an add-on
                                                                             aggregation routers for data center or colocation deployments. These
Routing Advantage License. It is supported in autonomous mode only. The
                                                                             routers are powered by the third-generation Cisco QuantumFlow
following platforms are included:
                                                                             Processor® application-specific integrated circuit (ASIC) to accelerate
• C8231-G2, C8231-E-G2                                                       routing and encryption in a compact 1RU form factor,

• C8235-G2, C8235-E-G2                                                       Q: What are the different models of the Cisco 8400 Series Secure
                                                                             Routers?
• C8355-G2
                                                                             A: The Cisco 8400 Series has the following two models:
• C8375-E-G2
                                                                             • C8455-G2: Eight 1GE + two 1GE/10GE + two 10GE/25GE
Q: What is the status of CUBE/SRST support on the Cisco 8000 Series?
                                                                             • C8475-G2: Eight 1GE + eight 1GE/10GE + four 10GE/25GE
A: Cisco Unified Border Element (CUBE) and Survivable Remote Site
Telephony (SRST) support begins in Release 17.18.2, specifically for the     Q: What are the different models of the Cisco 8500 Series Secure
C8375-E-G2. This support is only for autonomous mode.                        Routers?

• Feature parity: CUBE/SRST on the C8375-E-G2 offers full feature parity     A: The Cisco 8500 Series has the following two models:
  with the Catalyst 8300 Series platform, including support for CUBE local
                                                                             • C8550-G2: Twelve 1GE/10GE
  transcoding interface (LTI), Secure Real-Time Transport Protocol (SRTP),
  Session Initiation Protocol (SIP) signaling/media interworking, and box-   • C8570-G2: Twelve 1GE/10GE + two 40GE + two 40GE/100GE
  to-box high availability (active-standby).                                   (max 240GE total)

• Cisco Unified Communications Manager integration: SIP trunks are
  supported with UCM v15 starting in Release 17.18.2.


© 2026 Cisco and/or its affiliates. All rights reserved.
```

## PDF page 14

```text
FAQ Cisco public




Q: What parts are field-replaceable on the Cisco 8400 and 8500 Series                        Q: Is MACsec supported on the Cisco 8400 and 8500 Series Secure
Secure Routers?                                                                              Routers?

A: See the table below. The fan tray can be replaced, but it is not                          A: Yes, WAN and LAN MACsec are supported on all built-in ports of the
hot-swappable.                                                                               Cisco 8400 and 8500 Series Secure Routers.

Table 9.       Field-replaceable and hot-swappable parts on the Cisco 8400 and 8500 Series   Q: Are threat protection, advanced malware protection, and URL
Secure Routers                                                                               filtering supported on the Cisco 8400 and 8500 Series Secure Routers?

  Part                                    Field-replaceable   Hot-swappable (OIR)            A: Threat protection, advanced malware protection, and URL filtering are
                                          unit (FRU)                                         all supported on the Cisco 8400 Series. They are not supported on the
                                                                                             Cisco 8500 Series.
  DRAM                                    Yes                 No
                                                                                             Q: Is broadband aggregation (Broadband Network Gateway [BNG]/
  M.2 storage                             Yes                 No
                                                                                             L2TP Access Concentrator [LAC], L2TP Network Server [LNS], and
  Fan tray                                Yes                 No                             Intelligent Wireless Access Gateway [iWAG]) supported on the Cisco
                                                                                             8400 and 8500 Series Secure Routers?
  Power supplies                          Yes                 Yes
                                                                                             A: Broadband aggregation is supported on the Cisco 8500 Series. It is not
Q: Are there redundant power supplies in the Cisco 8400 and 8500                             supported on the Cisco 8400 Series.
Series Secure Routers?
                                                                                             Q: Do the Cisco 8400 and 8500 Series Secure Routers have feature
A: Yes, redundant power supplies are included by default.                                    parity with the Catalyst 8500 Series Routers?

Q: What VPN technologies are supported on the Cisco 8400 and 8500                            A: The Cisco 8400 Series has feature parity with the Catalyst 8500L, while
Series Secure Routers?                                                                       the Cisco 8500 Series has feature parity with the Catalyst 8500.

A: The Cisco 8400 and 8500 Series Secure Routers support VPN                                 Q: Are the Cisco 8400 and 8500 Series Secure Routers ENERGY STAR
technologies including FlexVPN, DMVPN, and GETVPN.                                           certified?

                                                                                             A: Yes, all Cisco 8400 and 8500 Series Secure Routers are ENERGY STAR
                                                                                             certified.




© 2026 Cisco and/or its affiliates. All rights reserved.
```

## PDF page 15

```text
FAQ Cisco public




                                                                          Table 10. Field-replaceable and hot-swappable parts on the Cisco 8600 Series Secure
Cisco 8600 Series Secure Routers FAQ                                      Routers

Q: What are the Cisco 8600 Series Secure Routers?                          Part                       Field-replaceable        Hot-swappable (OIR)
                                                                                                      unit (FRU)
A: The Cisco 8600 Series Secure Routers are high-performance
aggregation routers designed for data center or colocation deployments.    DRAM                       Yes                      No
These routers are powered by the third-generation Cisco QuantumFlow
                                                                           M.2 storage                Yes                      No
Processor ASIC to accelerate routing and encryption.
                                                                           Fan tray                   Yes                      Yes
Q: What are the different models of the Cisco 8600 Series Secure
Routers?                                                                   Power supplies             Yes                      Yes
A: The Cisco 8600 Series has one model:
                                                                          Q: Are there redundant power supplies in the Cisco 8600 Series
• C8650-G2: Twenty 1GE/10GE + six 40GE/100GE                              Secure Routers?
Q: What is the maximum number of ports that can be enabled on the
                                                                          A: Yes, redundant power supply is included by default (N+1). N+2
C8650-G2?
                                                                          is optional.
A: All twenty 1GE/10GE SFP+ ports and all six QSFP28 ports can be
                                                                          Q: What power supply options are available for the Cisco 8600 Series
enabled at the same time on the C8650-G2. Customers will need to
                                                                          Secure Routers?
decide if they want each of the QSFP28 ports to operate at 100GE or
40GE.                                                                     A: The Cisco 8600 Series supports up to four 1100W AC or 950W DC
                                                                          power supplies.
Q: Are Ethernet breakout cables supported?
                                                                          Q: Does the Cisco 8600 Series support mixing the AC and DC power
A: The C8650-G2 platform does not support breakout cables
                                                                          supplies in the same chassis?
Q: What parts are field-replaceable on the Cisco 8600 Series?
                                                                          A: No. All the power supplies need to be the same hardware PID.
A: See the table below. The fan tray can be hot swappable. Replace the
                                                                          Q: What is the airflow direction for the power supply?
fan module within 3 minutes to maintain proper cooling of the chassis.
                                                                          A: The airflow for the power supply in the Cisco 8600 Series Secure
                                                                          Routers is front (port side) to back (bezel side).




© 2026 Cisco and/or its affiliates. All rights reserved.
```

## PDF page 16

```text
FAQ Cisco public




Q: How is power usage distributed among the power supplies on the                                                                       Q: Do the Cisco 8650-G2 Secure Routers have feature parity with the
C8650-G2?                                                                                                                               C8500-20X6C Series Routers?

A: All installed power supplies are used at all times. A minimum of two                                                                 A: The Cisco 8650-G2 Secure Routers have feature parity with
power supplies is required. If a third or fourth power supply is installed,                                                             C8500-20X6C.
the load for the system will be evenly distributed among all the installed
                                                                                                                                        Q: What Layer 2 tunneling mechanisms are available on the Cisco 8600
power supplies. There is no way to configure a given power supply to be
                                                                                                                                        Series Secure Routers?
in standby mode with no active usage.
                                                                                                                                        A: Cisco 8600 Series Secure Routers support Layer 2 Tunneling Protocol
Q: What VPN technologies are supported on the Cisco 8600 Series
                                                                                                                                        (L2TP) v2 and v3, Ethernet VPN (EVPN), Overlay Transport Virtualization
Secure Routers?
                                                                                                                                        (OTV), and Virtual Private LAN Service (VPLS) as the Layer 2 tunneling
A: The Cisco 8600 Secure Routers support VPN technologies including                                                                     mechanisms.
FlexVPN, DMVPN, and GETVPN.
                                                                                                                                        Q: What features from Cisco trustworthy solutions are offered on the
Q: Is MACsec supported on the Cisco 8600 Series Secure Routers?                                                                         Cisco 8600 Series Secure Routers?

A: Yes, WAN and LAN MACsec are supported on all built-in ports of the                                                                   A: The security features of trustworthy solutions that are offered on the
Cisco 8600 Series Secure Routers.                                                                                                       Cisco 8600 Series Secure Routers include:

Q: Is there a performance penalty when enabling MACsec?                                                                                 • Secure Boot with signed images and hardware anchoring with Secure
                                                                                                                                          Unique Device Identifier (SUDI)
A: The packets-per-second forwarding rate of the platform is not affected
                                                                                                                                        • Secure storage
by enabling MACsec on any or all ports on the Cisco 8600 Series Secure
                                                                                                                                        • Run-time defenses
Routers. MACsec does add protocol headers that will affect throughput,
                                                                                                                                        • Authentication and integrity verification
but that is inherent to the protocol.
                                                                                                                                        • Recovery mechanisms
Q: Are threat protection, advanced malware protection, and URL
                                                                                                                                        • Management plane protections
filtering supported on the Cisco 8600 Series Secure Routers?
                                                                                                                                        Q: Do the Cisco 8600 Series Secure Routers have separate hardware
A: Threat protection, advanced malware protection, and URL filtering are
                                                                                                                                        to accelerate VPN operations?
NOT supported on the Cisco 8600 Series.
                                                                                                                                        A: The C8650-G2 has hardware-accelerated encryption and decryption in
Q: Is broadband aggregation (BNG/LAC, LNS, and iWAG) supported on
                                                                                                                                        the third-generation Cisco QuantumFlow Processor.
the Cisco 8600 Series Secure Routers?

A: Broadband aggregation is supported on the Cisco 8600 Series.

© 2026 Cisco and/or its affiliates. All rights reserved. Cisco and the Cisco logo are trademarks or registered trademarks of Cisco and/or its affiliates in the U.S. and other countries. To view a list of Cisco trademarks, go to this URL: www.cisco.com/go/trademarks.
Third-party trademarks mentioned are the property of their respective owners. The use of the word partner does not imply a partnership relationship between Cisco and any other company. (1110R)                                                  C67-5124049-02 06/26
```
