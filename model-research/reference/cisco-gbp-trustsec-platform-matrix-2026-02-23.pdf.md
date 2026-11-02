# cisco-gbp-trustsec-platform-matrix-2026-02-23.pdf — extracted text

- Source PDF: [cisco-gbp-trustsec-platform-matrix-2026-02-23.pdf](cisco-gbp-trustsec-platform-matrix-2026-02-23.pdf)
- PDF title metadata: Cisco Group Based Policy – Platform and Capability Matrix
- Publisher: Cisco (as registered in the research source entries).
- Source SHA-256: `41c54e00ec2feef2456cf2843e56072d08d2378f958a2218020a05cc93e98ba6`
- Converted: 2026-10-31 (UTC).
- Extraction tool: `pdftotext version 25.03.0`.
- Command: `pdftotext -layout -enc UTF-8 reference/cisco-gbp-trustsec-platform-matrix-2026-02-23.pdf -`.
- PDF pages: 21; page headings below use PDF page numbers.
- Language: English; no OCR or translation performed.
- Source access date and document revision: see the original source-register entries below; conversion does not update them.
- Source register: [C8300-4T2X-TS-1](../research-cisco-c8300-1n1s-4t2x-r1.1.0.md#c8300-4t2x-ts-1).
- Source register: [C8300-6T-GBP-1](../research-cisco-c8300-1n1s-6t-r1.1.0.md#c8300-6t-gbp-1).
- Source register: [ISR4431-SEC-4](../research-cisco-isr4431-r1.1.0.md#isr4431-sec-4).

> This is layout-preserving plain-text extraction wrapped in Markdown,
> not a semantic reconstruction of tables. Fixed-width text blocks preserve
> column spacing, but reading order, merged cells, and glyphs can still be
> imperfect. Images, diagrams, and image-based tick marks are not transcribed.
> Verify consequential table values against the linked original PDF.

## PDF page 1

```text
                 Cisco Group Based Policy Platform and Capability Matrix
                 (Inclusive of TrustSec Software-Defined Segmentation)

                 Cisco Group Based Policy (also known as TrustSec Software-Defined Segmentation) uniquely builds upon your
                 existing identity-aware infrastructure by enforcing segmentation and access control policies in a scalable manner.
                 This document summarizes the platforms and features that are validated in Cisco Group Based Policy testing. For
                 more information about Cisco Group Based Policy please visit the following links:
                 https://www.cisco.com/c/en/us/products/security/what-is-network-segmentation.html
                 https://www.cisco.com/c/en/us/solutions/enterprise-networks/trustsec/index.html


                 As an aid to deployment, products are grouped into Tier I, II, and III with regard to feedback on design and
                 deployment. Tier I products are in Table 1 and have full Group Based Policy functionality with few caveats,
                 and they are common components in successful deployments. Tier II products are in Table 2 and have full
                 Group Based Policy functionality, but there are some caveats involved in their deployment. Tier III products
                 are in Table 3 and do not have full Group Based Policy functionality and only support Classification and SXP
                 based Propagation. These products tend to be older with a less rich feature set and more caveats to consider
                 when deploying. In some cases, depending on the Solution-Level Validated Version, a product may be cross
                 listed in multiple Tiers. This will be noted in the entry with a link to the cross posting and the Solution-Level
                 Version in parenthesis. Non-Tiered Security Products are listed in Table 4. End of Sale Products are listed in
                 Table 5. It’s important to note that in some cases products in Tables 1, 2, and 3 may be at or near their End of
                 Life or End of Sale. In this case, the product entry will have a note indicating End of Sale/Life. For a full list of
                 Cisco products that have reached their End of Sale or Life and to review Cisco’s policy on End of Sale or Life
                 products, please visit the links at the top of Table 5. Tables 6 through 9 are Group Based Policy Scalability
                 Tables. Finally, Table 10 defines TrustSec Group Based Policy Interoperability with Application Centric
                 Infrastructure.

                 In Tables 1, 2, 3, and 4, Cisco Platform Support Matrix, Dynamic classification includes IEEE 802.1X, MAC
                 Authentication Bypass (MAB), Web Authentication (Web Auth), and Easy Connect. IP to SGT, VLAN to SGT,
                 subnet to SGT, port profile to SGT, L2IF to SGT, and L3IF to SGT use the static classification method.


                    §    Table 1: Tier I Cisco Group Based Policy Platform Support Matrix
                    §    Table 2: Tier II Cisco Group Based Policy Platform Support Matrix
                    §    Table 3: Tier III Cisco Group Based Policy Platform Support Matrix
                    §    Table 4: Non-Tiered Security Cisco Group Based Policy Platform Support Matrix
                    §    Table 5: End of Sale Group Based Policy Platform Support Matrix
                    §    Table 6: Cisco Group Based Policy Platform Scalability of Switch, Wireless, and Security Products
                    §    Table 7: Cisco Identity Services Engine (ISE) SXP Scaling
                    §    Table 8: Cisco Group Based Policy Platform Scalability of Router Products
                    §    Table 9: Cisco Group Based Policy Platform Scalability of SGACLs
                    §    Table 10: TrustSec Group-Based Policy (GBP) Interoperability




© 2026 Cisco and/or its affiliates. All rights reserved. This document is Cisco Public information                                       1
```

## PDF page 2

```text
                Table 1. Tier I Cisco Group Based Policy Platform Support Matrix
                Tier I products have full Group Based Policy functionality with few caveats, and they are common components in
                successful deployments.

                 System                                Platform                            License     Security Group SGT Exchange         Inline SGT          SGT
                Component                                                                                Tag (SGT)     Protocol (SXP)       Tagging        Enforcement
                                                                                                        Classification  Support and                           ______
                                                                                                                          Version                            Services

                                Catalyst 3650 and 3850 Series                            IP Base K9    Dynamic,       Speaker,          SGT over          SGACL, Logging
                                Software Catalyst 3650 Series                            & above or    IP to SGT (v4, Listener          Ethernet          (3.6.6E)
                                                                                         Cisco ONE     v6), VLAN to   V4                                      __
                                Software Catalyst 3850 Series                                          SGT, Port to
                                                                                         Foundation                                                       SGT NetFlow v9
                                                                                         & above       SGT,
                                                                                                       Subnet to SGT,
                                                                                                       L3IF to SGT

                   Tier I     Catalyst 3650 and 3850 Series                              IP Base K9    Dynamic,       Speaker,          SGT over          SGACL, Monitor
                                                                                         & above or    IP to SGT (v4, Listener          Ethernet,         mode, Logging
               Cisco Catalyst Software Catalyst 3650 Series                                            v6),
                3000 Series Software Catalyst 3850 Series                                Cisco ONE                    V4                SGT over
                                                                                         Foundation    VLAN to SGT,                     VXLAN
                                                                                         & above       Port to SGT,
                                                                                                       Subnet to SGT,
                                                                                                       L3IF to SGT

                                Catalyst 3850-XS Series                                  IP Base K9    Dynamic,       Speaker,          SGT over          SGACL
                                Software Catalyst 3850 Series                            & above or    IP to SGT,     Listener          Ethernet Note5;
                                                                                         Cisco ONE     VLAN to SGT, V4
                                                                                         Foundation    Port to SGT,
                                                                                         & above       Subnet to SGT,
                                                                                                       L3IF to SGT
                                Catalyst 4500 E-Series Supervisor Engine 8-E and         IP Base K9    Support for     Speaker,         SGT over          SGACL,
                                8L-E                                                     & above or    v4/v6:          Listener         Ethernet.         Logging
                                                                                         Cisco ONE     Dynamic,       V4                (See note 2 for
                                 Software 8L-E                                           Foundation    IP to SGT                        supported line
                                                                                         & above       VLAN to SGT,                     cards)            SGT NetFlow v9
                                 Software 8-E                                                          Port to SGT,
                   Tier I          Note: Tier II and Tier III contain entries for 4500                 Subnet to SGT,
                                                                                                       L3IF-to- SGT
               Cisco Catalyst                                                                          Note12

                4500 Series
                                Catalyst 4500-X Series (Cisco IOS XE 3.6.3E, 3.6.6) IP Base K9         Support for     Speaker,         SGT over          SGACL,
                                                                                    & above or         v4/v6:          Listener         Ethernet.         Logging
                                Software Catalyst 4500-X Series                          Cisco ONE     Dynamic,       V4
                                                                                         Foundation    IP to SGT
                                                                                         & above       VLAN to SGT,
                                                                                                       Port to SGT,
                                                                                                       Subnet to SGT,
                                                                                                       L3IF-to- SGT
                                   Note: Tier II and Tier III contain entries for 4500                 Note12




                                Catalyst 6500 Series Supervisor Engine 2T &              2T: IP Base   Support for     Speaker,         SGT over          SGACL (IPv4,
                                Supervisor 6T                                            K9            v4/v6:          Listener         Ethernet          IPv6),
                                                                                                       Dynamic,       V4                supported on:     Monitor mode,
                                Software Catalyst 6500 Supervisor Engine 2T                                                             WS-X69xx
                                                                                                       IP to SGT      (IPv4, IPv6)                        Logging.
                                                                                                       VLAN to SGT,                     modules,
                                Catalyst 6807-XL                                         6T: IP        Port to SGT,                     C6800-
                                                                                         Services K9   Subnet to SGT,                   32P10G/G-XL,      SGT Caching
                                Software Catalyst 6807-XL                                                                               C6800-
                                                                                                       L3IF-to- SGT                                       SGT NetFlow v9
                                                                                                                                        16P10G/G-XL,
                              Cisco IOS 15.4(1)SY2 15.2(1)SY05 15.2(1)SY0a                                                              C6800-
                              Sup 6T Cisco IOS 15.4(1)SY1                                                                               8P10G/G-XL,
                   Tier I
                                                                                                                                        SGT over
               Cisco Catalyst
                                                                                                                                        VXLAN
                6500 Series Note: Tier III contains entries for 6500


                                Catalyst 6880-X, 6840-X (incl 6816-X-LE), and            IP Base K9    Support for     Speaker,         SGT over          SGACL (IPv4,
                                6800ia                                                   & above or    v4/v6:          Listener         Ethernet.         IPv6),
                                Software Catalyst 6880-X                                 Cisco ONE     Dynamic,       V4                                  Monitor mode,
                                Software Catalyst 6840-X                                 Foundation    IP to SGT      (IPv4, IPv6)                        Logging.
                                                                                         & above       VLAN to SGT,
                                                                                                       Port to SGT,
                                                                                                       Subnet to SGT,                                     SGT Caching
                                                                                                       L3IF-to- SGT                                       SGT NetFlow v9

© 2026 Cisco and/or its affiliates. All rights reserved. This document is Cisco Public information                                                                        2
```

## PDF page 3

```text
                                Cisco Catalyst 9200 Series                       Network       Support for         Speaker,         SGT over         SGACL V4, V6
                   Tier I                                                        Advantage     v4/v6:              Listener         Ethernet         (Note 17),
               Cisco Catalyst Software Catalyst 9200 Series                                    Dynamic,       V4                    SGT over         Monitor mode,
                9200 Series                                                                    IP to SGT,                           VXLAN            Logging.
                                                                                                              V5 from 17.9.1
                                                                                               VLAN to SGT,                                            _
                                                                                               Port to SGT,                                          SGT NetFlow v9
                                                                                               Subnet to SGT,
                                                                                               L3IF to SGT,                                          SGACL drops in
                                                                                                                                                     NetFlow - 17.13.1

                                Catalyst 9300 Series                             Network       Support for         Speaker,         SGT over         SGACL V4, V6
                   Tier I                                                        Advantage     v4/v6:              Listener         Ethernet         (Note 17),
               Cisco Catalyst Software Catalyst 9300 Series                                    Dynamic,       V4                    SGT over         Monitor mode,
                9300 Series                                                                    IP to SGT,                           VXLAN            Logging.
                                                                                                              V5 from 17.9.1
                                                                                               VLAN to SGT,                                            _
                                                                                               Port to SGT,                                          SGT NetFlow v9
                                                                                               Subnet to SGT,                                        SGACL drops in
                                                                                               L3IF to SGT                                           NetFlow - 17.13.1

                                Catalyst 9400 Series Supervisor Engine-1 & 1XL   Network       Support for         Speaker,         SGT over         SGACL V4, V6
                                Software Catalyst 9400 Supervisor Engine-1       Advantage     v4/v6:              Listener         Ethernet         (Note 17),
                                                                                               Dynamic,       V4                    SGT over         Monitor mode,
                   Tier I                                                                                                                            Logging.
                                                                                               IP to SGT,     V5 from 17.9.1        VXLAN
               Cisco Catalyst                                                                  VLAN to SGT,                                            _
                9400 Series                                                                    Port to SGT,                                          SGT Caching
                                                                                               Subnet to SGT,
                                                                                               L3IF to SGT                                           SGT NetFlow v9
                                                                                                                                                     SGACL drops in
                                                                                                                                                     NetFlow - 17.13.1

                                Catalyst 9500 Series                             Network       Support for         Speaker,         SGT over         SGACL V4, V6
                                                                                 Advantage     v4/v6:              Listener         Ethernet         (Note 17),
                                                                                               Dynamic,       V4                    SGT over         Monitor mode.
                                Software Catalyst 9500 Series
                                                                                               IP to SGT,     V5 from 17.9.1        VXLAN              _
                                                                                               VLAN to SGT,                                          SGT Caching
                                                                                               Port to SGT,
                                                                                               Subnet to SGT,                                        SGT NetFlow v9
                                                                                               L3IF to SGT                                           SGACL drops in
                   Tier I                                                                                                                            NetFlow - 17.13.1
               Cisco Catalyst
                9500 Series Catalyst 9500H/X Series                              Network       Support for         Speaker,         SGT over         SGACL V4, V6
                                                                                 Advantage     v4/v6:              Listener         Ethernet         (Note 17),
                                                                                               Dynamic,       V4                    (Silicon One     Monitor mode,
                                                                                               IP to SGT,                           models           Logging.
                                                                                                              V5 from 17.9.1        supported from
                                                                                               VLAN to SGT,                                            _
                                                                                               Port to SGT,                         17.13.1)
                                                                                                                                                     SGT NetFlow v9
                                                                                               Subnet to SGT,                       SGT over
                                                                                               L3IF to SGT                          VXLAN            SGACL drops in
                                                                                                                                                     NetFlow - 17.13.1
                                                                                                                                                     (Doppler only)
                                Cisco Catalyst 9600 Series                       Network       Support for         Speaker,         SGT over         SGACL V4, V6
                   Tier I     Software Catalyst 9600 Series                      Advantage     v4/v6:              Listener         Ethernet         (Note 17),
               Cisco Catalyst                                                                  Dynamic,       V4                    (Silicon One     Monitor mode,
                9600 Series                                                                    IP to SGT,                           models           Logging.
                                                                                                              V5 from 17.9.1        supported from
                                                                                               VLAN to SGT,                                            _
                                                                                               Port to SGT,                         17.13.1)
                                                                                                                                                     SGT NetFlow v9
                                                                                               Subnet to SGT,                       SGT over
                                                                                               L3IF to SGT                          VXLAN.           SGACL drops in
                                                                                                                                                     NetFlow - 17.13.1
                                                                                                                                                     (Doppler only)

                                Cisco Catalyst 9800 Series                       No license    Support for         Speaker,         SGT over         SGACL V4, V6
                   Tier I                                                        for the 9800 v4/v6:               Listener         Ethernet         (Note 17),
               Cisco Catalyst                                                    itself. Each Dynamic,             V4               SGT over         Monitor mode,
                9800 Series                                                      AP joined is IP to SGT,                            VXLAN            Logging.
                                                                                 licensed                          V5 from 17.9.1
                                                                                               Subnet to SGT,                                          _
                                                                                 through       Policy Profile to
                                                                                 global                                                              SGT NetFlow v9
                                                                                               SGT
                                                                                 setting of
                                                                                 either
                                                                                 Essentials or
                                                                                 Advantage




© 2026 Cisco and/or its affiliates. All rights reserved. This document is Cisco Public information                                                                   3
```

## PDF page 4

```text
                                  IE 3400 Series                                    Network      Dynamic,       Speaker,       SGT over         SGACL V4, V6
                    Tier I      Software Catalyst IE3400 Heavy Duty Series          Advantage    IP to SGT,     Listener       Ethernet         (Note 17 and 19),
               Cisco Industrial Software Catalyst IE3400 Rugged Series                           VLAN to SGT, V4                                Monitor mode,
                  Ethernet                                                                       Port to SGT,                                   Logging.
                  Switches                                                                       Subnet to SGT,                                    _
                                IEM-3300-x module does not support TrustSec                      L3IF to SGT
                                                                                                                                                SGT NetFlow v9
                                IEM-3400-8T, 8S and 8P do support TrustSec
                                                                                                                                                -----------
                                                                                                                                                Does NOT
                                                                                                                                                support vlan-list
                                                                                                                                                enforcement

                                  IE 9300                                           Network      Support for      Speaker,     SGT over         SGACL V4, V6
                                                                                    Advantage    v4/v6:           Listener     Ethernet         (Note 17),
                                                                                                 Dynamic, IP to   V4                            Monitor mode,
                                                                                                 SGT (v4, v6),                                  Logging.
                                                                                                 VLAN to SGT,                                     _
                                                                                                 Port to SGT,                                   SGT NetFlow v9
                                                                                                 Subnet to SGT

                                  IR 8340                                           Both         IP to SGT,       Speaker,     SGT over         SGACL,
                    Tier I                                                          Network      Subnet to SGT,   Listener     Ethernet, SGT    Monitor mode &
               Cisco Industrial                                                     Essentials   L3IF to SGT      V4           over GETVPN,     Logging
                  Ethernet                                                          and                                        DMVPN, or        SGT caching
                                                                                    Advantage                                  IPsec VPN
                  Routers

                                  1540, 1560 AP series                              -            Dynamic          Speaker,     SGT over         SGACL
                                  Software AP 1540                                                                Listener     Ethernet Note6
                    Tier I        Software AP 1560                                                                V4Note6
                Cisco Access
                   Points
                                  1700, 2700, 3700, AP Series (Wave 1)              -            Dynamic          Speaker,     SGT over         SGACL
                                  Software AP 1700                                                                Listener     Ethernet Note6
                                  Software AP 2700                                                                V4Note6
                                  Software AP 3700

                                  1815, 1830, 1850, 2800, 3800 AP Series (Wave 2)   -            Dynamic          Speaker,     SGT over         SGACL
                                  Software AP 1815                                                                Listener     Ethernet Note6
                                  Software AP 1830                                                                V4Note6
                                  Software AP 1850
                                  Software AP 2800
                                  Software AP3800
                                  Software AP4800

                                  8540 Series Wireless Controller                   -            Dynamic          Speaker v2   SGT over         Supports AP
                                  (Cisco AireOS 8.9)                                                                           Ethernet         SGACL in
                                  Software 8540 Wireless Controller                                                                             Centralized and
                                                                                                                                                Flex Connect
                                  Note: Tier III contains entries for 8540                                                                      mode)

                                  5520 Series Wireless Controller                   -            Dynamic          Speaker v2   SGT over         Supports AP
                                  (Cisco AireOS 8.9)                                                                           Ethernet         SGACL in
                   Tier I                                                                                                                       Centralized and
                              Software 5520 Wireless Controller
               Cisco Wireless                                                                                                                   Flex Connect
                              Note: Tier III contains entries for 5520                                                                          mode)
                 Controller
                   Series     3504 Wireless Controller                              -            Dynamic          Speaker v2   SGT over         Supports AP
                                  Software 3540 Wireless Controller                                                            Ethernet         SGACL in
                                                                                                                               (Centralized     Centralized and
                                                                                                                               mode)            Flex Connect
                                                                                                                                                mode)

                                  vWLC                                              -            Dynamic          Speaker v2                    Supports APs in
                                  Software vWLC                                                                                                 Flex mode only




© 2026 Cisco and/or its affiliates. All rights reserved. This document is Cisco Public information                                                                  4
```

## PDF page 5

```text
                                 Nexus 7000 with M3-Series modules                  Base            IP to SGT1,       Speaker,         SGT over           SGACL,
                                                                                    License         Port Profile to   Listener         Ethernet5;         Monitor mode &
                                                                                    NX-OS 6.1       SGT, VLAN         V4               SGT over           logging
                                 Cisco NX-OS 8.1(2), 8.1(1), 8.0(1) 7.3.2           and later       to SGT2,
                                 7.3(0)D1(1) [logging, monitor mode], 7.2(0)D1(1)                                                      VXLAN
                   Tier I                                                                           Port to SGT2
                                                                                                                                       5
               Cisco Nexus®                                                                         Subnet to                           : F3
                7000 Series                                                                         SGT5 Note14                        interoperability
                                                                                                                                       requires M3 ‘no
                                                                                                                                       propagate-sgt l2
                                 Note: Tier II contains entries for Nexus 7000s                                                        control’
                                                                                                                                       command


                                 ISR 1000 Series                                     IP Base/K9     IP to SGT,        Speaker,         SGT over           SGACL, Monitor
                                                                                    for classify/   Subnet to         Listener         Ethernet, SGT      mode & Logging
                                                                                    propagate,      SGT, L3IF to      V4               over GETVPN,       SG Firewall
                                 Cisco 1000 Series ISRs DSL and LTE SKUs            SGACL,          SGT                                DMVPN, or
                    Tier I                                                                                            V5 from 17.9.1   IPsec VPN
                                                                                    Security/K9
                    Cisco                                                           for SG FW                                                             SGT based PBR.
                 Integrated                                                         enforcement                                                           SGT Caching
               Services Router
                    (ISR)                                                                                                                                 SGT based QoS.

                                 ISR 1100 Series                                     IP Base/K9     IP to SGT,        Speaker,         SGT over           SGACL, Monitor
                                                                                    for classify/   Subnet to         Listener         Ethernet, SGT      mode & Logging
                                                                                    propagate,      SGT, L3IF to      V4               over GETVPN,       SG Firewall
                                 Recommended Software                               SGACL,          SGT                                DMVPN, or
                                                                                                                      V5 from 17.9.1   IPsec VPN
                                                                                    Security/K9
                                                                                    for SG FW                                                             SGT based PBR.
                                                                                    enforcement                                                           SGT Caching
                                                                                                                                                          SGT based QoS.

                                 4000 Series                                         IP Base/K9     IP to SGT,        Speaker,         SGT over           SGACL, Monitor
                                 ISR 4431, 4451-X, 4321, 4331, 4351                 for classify/   Subnet to         Listener         Ethernet, SGT      mode & Logging
                                                                                    propagate,      SGT, L3IF to      V4               over GETVPN,       SG Firewall
                                 (Cisco IOS XE Denali 16.3.2, Everest 16.4.1)       SGACL,          SGT                                DMVPN, or
                                                                                     Security/K9                      V5 from 17.9.1   IPsec VPN
                                 Software ISR 4000 Series                            for SG FW                                                            SGT based PBR.
                                                                                     enforcement                                                          SGT Caching
                                 Note: Tier II contains entries for 4451                                                                                  SGT based QoS.

                                 ISRv                                               IP Base/K9      IP to SGT,        Speaker,         SGT over           SGACL, Monitor
                                                                                    for classify/   Subnet to         Listener         Ethernet,          mode & Logging
                                                                                    propagate,      SGT, L3IF to
                                                                                    SGACL                             V4               SGT over IPsec
                                                                                                    SGT                                VPN, DMVPN
                                                                                                                      V5 from 17.9.1

                                 CSR 1000V                                          IP Base/K9      IP to SGT,        Speaker,         SGT over           SGACL, Monitor
                                                                                    for classify/   Subnet to         Listener         Ethernet,          mode & Logging
                    Tier I     (Cisco IOS XE 16.6.3 Denali 16.3.2, Everest          propagate,
                Cisco Cloud 16.4.1)                                                                 SGT, L3IF to      V4               SGT over IPsec
                                                                                    SGACL;          SGT
               Services Router Recommended Software                                                                   V5 from 17.9.1   VPN, DMVPN
                                 Note: Tier II contains entries for CSR 1000V

                                 ASR 1004, 1006, 1013, 1001-X, 1002-X,1002-HX,      IP Base/K9      IP to SGT,        Speaker,         SGT over           SGACL,
                    Tier I     1006-X, and 1009-X                                   for classify/   Subnet to         Listener         Ethernet, SGT      Monitor mode &
                    Cisco      (Cisco IOS XE 16.5.1b Denali 16.3.2, Everest         propagate,      SGT, L3IF to      V4               over GETVPN,       Logging,
                Aggregation 16.4.1)                                                 SGACL,          SGT                                DMVPN, or
                                                                                                                      V5 from 17.9.1   IPsec VPN          SG Firewall
               Services Router Software ASR 1004                                    Security/K9
                   (ASR)                                                            for SGFW
                                 Software ASR 1006                                  enforce-                                                              SGT based PBR.
                                 Software ASR 1013                                  ment                                                                  SGT Caching
                                 Software ASR 1001-X                                                                                                      SGT based QoS.
                                 Software ASR1002-X
                                 Software ASR 1002-HX
                                 Software ASR 1006-X
                                 Software ASR 1009-X


                                 Note: Tier II contains entries for ASR
                   Tier 1     C8200-1N-4T, C8200L-1N-4T, C8500-12X, C8500L- Network                 IP to SGT,        Speaker,         SGT over           SGACL, Monitor
               Cisco Catalyst 8S4X, C8300-2N2S-6T, C8000V 16vCPU/16GB,      Advantage               Subnet to         Listener         Ethernet, SGT      mode & Logging
                8000 series   C8000V 8vCPU/8GB, C8000V 2vCPU/4GB                                    SGT, L3IF to      V4               over GETVPN,       SG Firewall
                  routers                                                                           SGT                                DMVPN, or
                                                                                                                      V5 from 17.9.1   IPsec VPN
                                 Software 8000v Edge                                                                                   Note18             SGT based PBR.
                                 Software 8500 Edge                                                                                                       SGT Caching
                                                                                                                                                          SGT based QoS.


© 2026 Cisco and/or its affiliates. All rights reserved. This document is Cisco Public information                                                                         5
```

## PDF page 6

```text
                                  ISE 34xx, 35xx, 36xx, 37xx                          Advantage     Dynamic, IP to   Speaker,         –                –
                    Tier I        Appliance & VMware                                  (for both     SGT, Subnet      Listener
                Cisco Identity                                                        TrustSec      to SGT           V4
                  Services                                                            and pxGrid)
                                  Software ISE                                                                       pxGrid
                   Engine

                                  Meraki MS390 14+                                    Advantage     Dynamic, IP to   Unsupported     SGT over          SGACL, Logging,
                                           9300-M                                                   SGT, VLAN to                     Ethernet          AVC NetFlow v10
                                           9300L-M                                                  SGT, Port to                                       Source group
                   Tier 1
                                           9300X-M                                                  SGT, Subnet to                                     record attribute
               Meraki Devices                                                                       SGT                                                (390/9300)

              This document       MS130(R/X): MS17 +                                  Advantage     Dynamic,         Unsupported     SGT over          SGACL, Logging
              is best effort. For                                                                   VLAN to SGT,                     Ethernet
              real-time                                                                             Port to SGT
              updates please
              see:
              https://document
              ation.meraki.co MR (27 +)                                               Advantage     Dynamic, SSID    Unsupported     SGT over          SGACL, Logging
              m/Platform_Man                                                                        to SGT, Group                    Ethernet
              agement/Dashb                                                                         Policy to SGT
              oard_Administra
              tion/Design_and
              _Configure/Confi
              guration_Guides
              /Adaptive_Policy MX/Z3+: 18.1 +                                         Advantage     VLAN to SGT,     Unsupported     SGT over          Unsupported
              /Adaptive_Policy                                                        /SD-WAN       Port to SGT                      Ethernet, SGT
              _Overview                                                                                                              over SDWAN




                Table 2. Tier II Cisco Group Based Policy Platform Support Matrix
                Tier II products have full Group Based Policy functionality but there are some caveats involved in their deployment.

                 System                                   Platform                        License    Security Group Tag   SGT Exchange Inline SGT              SGT
                Component                                 _______                                           (SGT)         Protocol (SXP) Tagging           Enforcement
                                                                                                       Classification      Support and                       ______
                                                                                                                             Version
                                         Solution Validated Software Version                                                                                Services

                                 Catalyst 3560-CX Series                              IP Base K9    (L2 adjacent hosts    Speaker,         No          SGACL Note16
                   Tier II    (Cisco IOS 15.2(3)E)                                                  only)                 Listener
               Cisco Catalyst                                                                       Dynamic,              V4
                3000 Series                                                                         IP to SGT (v4, v6),
                              Software Catalyst 3560-CX                                             VLAN to SGT,
                                                                                                    Subnet to SGT
                                 Note: Tier III contain entries for 3560

                                 Catalyst 4500 E-Series Supervisor Engine 7-E and 7L-E IP Base K9   Dynamic, IP to SGT, Speaker,           SGT over    SGACL, Logging
                                 (Cisco IOS XE 3.7.1E)                                 & above or   VLAN to SGT, Subnet Listener           Ethernet.   [3.8.0E]
                                                                                      Cisco ONE     to SGT, L3IF to SGT, V4                (See note
                   Tier II                                                                          Port to SGT Note12
               Cisco Catalyst                                                         Foundation                                           2 for       SGT NetFlow v9
                                                                                      & above                                              supporte
                4500 Series                                                                                                                d line
                                                                                                                                           cards)
                                 Note: Tier I and Tier III contain entries for 4500
                                 Note: End of Sale/Life

                  Tier II        CGR 2010 Series                                      -             Dynamic,              Speaker,         SGT over    SG Firewall
                  Cisco                                                                             IP to SGT,            Listener         GETVPN,
                Connected        Software CGR 2010 Series                                           VLAN to SGT           V4               SGT over
                Grid Router                                                                                                                IPsec
                  Series                                                                                                                   VPN
                                 IE 4000 Series                                       LAN Base,     (L2 adjacent hosts    Speaker Note11   SGT over    SGACL Note16
                                                                                      IP Services   only)                 V4               Ethernet
                                                                                      for SGToE     Dynamic, IP to SGT,
                                 Software IE 4000 Series                                            VLAN to SGT,
                                                                                      & SGACL
                   Tier II                                                                          Subnet to SGT
                   Cisco




© 2026 Cisco and/or its affiliates. All rights reserved. This document is Cisco Public information                                                                       6
```

## PDF page 7

```text
                 Industrial   IE 5000 Series                                        LAN Base,     (L2 adjacent hosts  Speaker Note11         SGT over      SGACL Note16
                 Ethernet                                                           IP Services   only)                                      Ethernet
                 Switches                                                                                             V4
                                                                                    for SGToE     Dynamic, IP to SGT,                        on1G &
                              Software IE 5000 Series                               & SGACL       VLAN to SGT, Subnet                        10G
                                                                                                  to SGT                                     interfaces
                                                                                                                                             only
                              Nexus 7000 with M2-Series modules                     Base          IP to SGT1,             Speaker,           SGT over      SGACL
                                                                                    License       Port Profile to SGT,    Listener           Ethernet5;
                              Cisco NX-OS 8.1(1), 8.0(1) 7.3(0)D1(1)                                                                                       Monitor mode &
                                                                                    NX-OS 6.1     VLAN to SGT2,           V4                               limited logging
                              [Monitor mode & limited logging],                     and later     Port to SGT2                               5
                                                                                                                                              : M2
                              7.2(0)D1(1)                                                         Subnet to SGT5                             cannot link
                                                                                                  Note14
                                                                                                                                             to F3
                                                                                                                                             module.
                                                                                                  1
                                                                                                   :FabricPath support
                                                                                                  requires 6.2(10) or
                                                                                                  later.

                   Tier II                                                                        2
                                                                                                    VPC/VPC+ support
               Cisco Nexus®                                                                       requires 7.2(0)D1(1)
                7000 Series                                                                       or later.
                              Note: Tier 1 contains entries Nexus 7000s
                                                                                                  5
                                                                                                    Subnet to SGT
                                                                                                  requires 7.3(0)D1(1)
                                                                                                  or later.

                              Nexus 7700 F-SeriesNote4 modules                     Base           IP to SGT1,             Speaker,           SGT over      SGACL
                                                                                   License        Port Profile to SGT,    Listener           Ethernet35
                              F3 modules do not support SGT tagging with other     NX-OS 6.1
                              Cisco products unless these products support the                    VLAN to SGT2,           V4                 ;
                                                                                   and later      Port to SGT2
                              SGT tagging exemption feature for Layer 2 protocols.
                              M3 series support this by enabling ‘no propagate-sgt                Subnet to SGT5                             3
                                                                                                  Note14                                      : F3
                              l2-control’ command.                                                                                           interfaces
                                                                                                  1:FabricPath                               (L2 or L3)
                              Cisco NX-OS 8.1(1), 8.0(1) 7.3(0)D1(1), 7.2(0)D1(1)                 support requires                           require
                                                                                                  6.2(10) or later.                          802.1Q or
                                                                                                                                             FabricPat
                                                                                                  2 VPC/VPC+                                 h
                                                                                                  support requires                           4
                                                                                                                                              : F2e
                                                                                                  7.2(0)D1(1) or later.                      (Copper)
                   Tier II                                                                                                                   all ports;
               Cisco Nexus®                                                                       5 Subnet to SGT
                                                                                                                                             F2e (SFP)
                7000 Series                                                                       requires                                   & F3
                                                                                                  7.3(0)D1(1) or later.                      (10G)-
                                                                                                                                             last 8
                                                                                                                                             ports; All
                                                                                                                                             others- no
                                                                                                                                             support
                                                                                                                                             5
                              Note: Tier 1 contains entries for Nexus 7000s                                                                   : Not
                                                                                                                                             supported
                              Nexus 6000/5600 Series                                -             (L2 adjacent hosts      Speaker            between
                                                                                                                                             SGT over      SGACL Note16
                                                                                                  only)                                      F3  and
                                                                                                                                             Ethernet
                              Software Nexus 6000                                                                         V1                 either M2
                                                                                                  Port to SGT
                   Tier II                                                                                                                   or F2e
                Cisco Nexus   Nexus 5548P, 5548UP, and 5596UP                       -             (L2 adjacent hosts      Speaker            SGT over      SGACL Note16
                5000, 6000
                              Software Nexus 5548P                                                only)                   V1    1            Ethernet
                   Series
                                                                                                  Port to SGT
                              Software Nexus 5548UP
                              Software Nexus 5596UP
                                                                                                                          1
                                                                                                                              : FabricPath



                              Nexus 1000V for VMware                                Advanced      Dynamic (802.1x)        Speaker,           SGT over      SGACL, Logging
                                                                                    license for   Note15
                                                                                                        ,                                    EthernetN
                              vSphere                                               SGToE/                                Listener v4        ote9
                                                                                    SGACL         IP to SGT,              v1 (prior to
                  Tier II     Software Nexus 1000V                                  support       Port Profile to SGT     5.2(1)SV3(3.1)
               Cisco Nexus
               1000 Series                                                          Advanced
                              Nexus 1000VE Virtual Edge                                           Port Profile to SGT,    Speaker,           No            SGACL
                                                                                    license for
                                                                                    SGACL         IP to SGT               Listener v4
                              Software Nexus 1000VE                                 support




© 2026 Cisco and/or its affiliates. All rights reserved. This document is Cisco Public information                                                                           7
```

## PDF page 8

```text
                             890, 1900, 2900, 3900 Series                       IP Base/K9      IP to SGT, Subnet to   Speaker,   SGT over SG Firewall
                                                                                for classify/   SGT, L3IF to SGT       Listener   Ethernet
                                                                                propagate,                                        (no
                    Tier II  Software ISR 890 and 1900                                                                 V4         support on (890: No services)
                                                                                Security/K
                    Cisco                                                       9 for SG                                          ISR
                                                                                                                                              SGT based PBR.
                 Integrated                                                     FW                                                G2-Cisco
                  Services   Software 2900 Series                                                                                 800         SGT Caching
                                                                                enforcem
                Router (ISR)                                                    ent                                               Series),    SGT based QoS
                                                                                                                                  SGT over
                              Software 3900 Series
                                                                                                                                  GETVPN,
                                                                                                                                  DMVPN,
                                                                                                                                  or IPsec
                                                                                                                                  VPN
                              4000 Series                                      IP Base/K9       IP to SGT, Subnet to   Speaker,   SGT over    SG Firewall
                              (ISR 4451-X validated)                           for classify/    SGT, L3IF to SGT       Listener   Ethernet,
                                                                               propagate,                              V4         SGT over
                              (Cisco IOS XE 3.15.01S)                           Security/K                                        GETVPN,     SGT based PBR.
                                                                                9 for SG                                          DMVPN,      SGT Caching
                    Tier II  Software ISR 4000 Series                           FW                                                or IPsec    SGT based QoS.
                                                                                enforcem                                          VPN
                    Cisco                                                                                                                     SGT NetFlow v9
                                                                                ent
                 Integrated
                  Services   Note: Tier I contains entries for 4451 Products
                Router (ISR)
                             SM-X Layer 2/3 EtherSwitch Module                  IP              Dynamic, IP to SGT,    Speaker,   SGT over    SGACL
                                                                                Services/K9     VLAN to SGT            Listener   Ethernet.
                              Software SM-X Layer 2/3                                                                  V4


                              Cloud Services Router 1000V Series (CSR)          IP Base/K9      IP to SGT, Subnet to   Speaker,   SGT over    SG Firewall
                   Tier II  (Cisco IOS XE 3.15.01S)                             for classify/   SGT, L3IF to SGT       Listener   Ethernet,
                Cisco Cloud Software CSR 1000V                                  propagate,                             V4         SGT over    SGT based PBR.
                 Services                                                       Security/K9                                       IPsec       SGT Caching
                   Router                                                       for enforce-                                      VPN,
                                                                                                                                              SGT NetFlow v9
                             Note: Tier I contains entries for CSR 1000V        ment                                              DMVPN




                              ASR 1000 Series Router Processor 1 or 2 (RP1,     IP Base/K9      IP to SGT, Subnet to   Speaker,   SGT over    SG Firewall
                              RP2); ASR 1001, 1002,1004, 1006 and 1013 with     for classify/   SGT, L3IF to SGT       Listener   Ethernet,
                              ESP (10,20, 40, 100, 200) and SIP (10/40)         propagate,                             V4         SGT over    SGT based PBR
                              (Cisco IOS XE 3.13.0S)                            Security/K9                                       GETVPN,     (1000 RP2)
                              Software ASR 1000 RP1                             for enforce-                                      IPsec
                                                                                ment                                              VPN, or     SGT based QoS.
                              Software ASR 1000 RP2                                                                               DMVPN       SGT Caching
                   Tier II
                              Software ASR 1001                                                                                               SGT NetFlow v9
               Cisco Aggreg-
               ation Services Software ASR 1002
                   Router     Software ASR 1004
                   (ASR)      Software ASR 1006
                              Software ASR 1013
                              Note: Tier I contains entries for ASR Products


                              ASR 1001-X and 1002-X                                             IP to SGT, Subnet to   Speaker,   SGT over    SG Firewall
                               (Cisco IOS XE 3.13.0S)                                           SGT, L3IF to SGT       Listener   Ethernet,
                                                                                IP Base/K9
                                                                                for classify/                          V4         SGT over    SGT based PBR
                                                                                propagate,                                        GETVPN,
                              Software ASR 1001-X                                                                                 IPsec       SGT based QoS.
                              Software ASR 1002-X                               Security/K9                                       VPN,        SGT Caching
                                                                                for enforce-                                      DMVPN
                                                                                ment                                                          SGT NetFlow v9


                              Note: Tier I contains entries for ASR Products




                Table 3. Tier III Cisco Group Based Policy Platform Support Matrix
                Tier III products do not have full Group Based Policy functionality and support Classification and SXP based
                propagation only.




© 2026 Cisco and/or its affiliates. All rights reserved. This document is Cisco Public information                                                           8
```

## PDF page 9

```text
                 System                       Platform               License     Security       SGT Exchange           Inline SGT Tagging            SGT
                Component                                                       Group Tag       Protocol (SXP)                                   Enforcement
                                                                                  (SGT)          Support and                                        ______
                                                                               Classification      Version                                         Services


                                  Catalyst 2960-Plus Series          LAN     Dynamic, IP to Speaker              No                         No
                                                                     Base K9 SGT, VLAN to V4
                                                                             SGT, Subnet to
                                  Software 2960-Plus Series                  SGT
                                  Note: End of Sale/Life
                                  Catalyst 2960-C Series             LAN     Dynamic, IP to Speaker              No                         No
                                  Software 2960-C Series             Base K9 SGT, VLAN to V4
                                                                             SGT, Subnet to
                                                                             SGT
                   Tier III       Note: End of Sale/Life
                   Cisco          Catalyst 2960-CX Series            LAN     Dynamic, IP to Speaker              No                         No
                              ®                                      Base K9 SGT, VLAN to V4
                 Catalyst         Software 2960-CX Series
                                                                             SGT, Subnet to
                2000 Series
                                                                             SGT
                                  Note: End of Sale/Life
                                  Catalyst 2960-X Series             LAN     Dynamic, IP to Speaker              No                         No
                                  Software 2960-X Series             Base K9 SGT, VLAN to V4
                                                                             SGT, Subnet to
                                                                             SGT
                                  Note: End of Sale/Life
                                  Catalyst 2960-XR Series            IP Lite   Dynamic, IP to Speaker            No                         No
                                  Software 2960-XR Series            K9        SGT, VLAN to V4
                                                                               SGT, Subnet to
                                                                               SGT
                                  Note: End of Sale/Life
                                  Catalyst 3560-C/CG Series          IP Base   (L2 adjacent     Speaker, Listener No                        No
                                  (Cisco IOS 15.0(1)SE2)             K9        hosts only)      V4
                                                                               Dynamic,
                   Tier III   Software Catalyst 3560-C                         IP to SGT,
               Cisco Catalyst                                                  VLAN to SGT,
                3000 Series                                                    Subnet to SGT
                              Note: Tier II contains entries for
                              Nexus 3560
                                  Note: End of Sale/Life

                                  Catalyst                           IP Base   Dynamic, IP to   Speaker, Listener No                        No
                   Tier III   4500 E-Series Supervisor               K9        SGT Note12       V4
               Cisco Catalyst Engine 6-E and 6L-E;
                4500 Series       (Cisco IOS 15.1(1)SG)
                                  Software 4500 Supervisor
                                  Engine 6-E
                                  Software Supervisor Engine 6L-
                                  E


                                  Note: Tier I and Tier II contain
                                  entries for 4500
                                  Note: End of Sale/Life

                                  Catalyst 6500 Series Supervisor IP Base      Dynamic, IP to   Speaker, Listener No                        No
                                  Engine 32 and 720               K9           SGT              V4
                                  Cisco IOS 15.2(2)SY2,
                   Tier III       15.2(1)SY0a, 15.2(3a)E
               Cisco Catalyst
                6500 Series Software 6500 Series
                              Supervisor Engine 720


                                  Note: Tier I contain entries for
                                  6500
                                  Note: End of Sale/Life
                  Tier III        CGS 2500 Series                    -         Dynamic,         Speaker,         No                         No
                   Cisco          Software CGS-2520-16S-8PC                    IP to SGT,       Listener
                Connected                                                      VLAN to SGT,     V3
                Grid Switch       Software CGS-2520-24TC                       Port to SGT,
                  Series                                                       Subnet to SGT




© 2026 Cisco and/or its affiliates. All rights reserved. This document is Cisco Public information                                                             9
```

## PDF page 10

```text
                              IE 2000 & 2000U Series              LAN      (L2 adjacent        Speaker, Listener No                                No
                  Tier III     IE 3000 Series                     Base     hosts only)         V4
              Cisco Industrial Software IE 2000 Series                     Dynamic,
                 Ethernet                                                  IP to SGT,
                 Switches      Software IE 2000U Series                    VLAN to SGT,
                               Software IE 3000 Series                     Subnet to SGT

                               5500 Series (5508, 5520)           -        Dynamic             Speaker V2       No                                 No
                               2500 Series (2504)
                              (Cisco AireOS 8.3.102.0,
                              7.6.130.0)
                              Software 5500 Series
                              Software 2500 Series

                  Tier III    Note: Tier I contains entries for
                  Cisco       8520
                 Wireless     Note: End of Life/Sale
                 Controller
                  Series
                              8500 Series (8540,8510)             -        Dynamic             Speaker V2       No                                 No
                              (Cisco AireOS 8.3.102.0
                              (pre 8.4))
                              Software 8500 Series
                              Note: Tier I contains entries for
                              8540




                Table 4. Non-Tiered Security Cisco Group Based Policy Platform Support Matrix
                 System             Platform            License   Security Group        SGT     Inline SGT Tagging                             SGT
                Component                                           Tag (SGT)        Exchange                                              Enforcement
                                                                   Classification     Protocol                                                ______
                                                                                       (SXP)                                                 Services
                                                                                    Support and
                                                                                      Version

                              ASA 5580              -                               Speaker,                            SG Firewall
                                                                                    Listener
                              Software ASA                                          v2
                              5580

                              ASA 5506-X,
               Cisco Adaptive 5506H-X, 5506W-
                  Security    X, 5508-X, 5516-X
                 Appliance                                        Remote            Speaker,
                                                    -             Access VPN        Listener        SGT over Ethernet   SG Firewall (IPv4, IPv6)
                              Software ASA                        (IPsec, SSL-      V3
                              5506-X                              VPN); SGT
                                                                  assigned via                                          SGT based PBR
                              Software ASA
                              5506H-X                             ISE Authz.

                              Software ASA
                              5506W-X
                              Software ASA
                              5516-X
                              Software ASA
                              5508-X

                              ASA 5525-X,           -             Remote            Speaker,        SGT over Ethernet   SG Firewall (IPv4, IPv6)
                              5545-X, 5555-X                      Access VPN        Listener
               Cisco Adaptive with FirePower                      (IPsec, SSL-
                  Security                                        VPN); SGT         V3                                  SGT based PBR.
                              Services
                 Appliance                                        assigned via
                              Software ASA                        ISE Authz.
                              5525-X
                              Software ASA
                              5545-X

                              ASAv                  -             Remote            Speaker,        SGT over Ethernet   SG Firewall
                                                                  Access VPN        Listener
                              Software ASAv                       (IPsec, SSL-      V3
                                                                  VPN); SGT                                             SGT based PBR.
                                                                  assigned via
                                                                  ISE Authz.


© 2026 Cisco and/or its affiliates. All rights reserved. This document is Cisco Public information                                                       10
```

## PDF page 11

```text
                                   Secure FW 1000,      -            Remote Access Speaker,           SGT over Ethernet    SG Firewall (IPv4, IPv6)
                                   2100, 3100, 4100,                 VPN (IPsec,   Listener
                                   4200, 9300                        SSL-VPN)      V3                                      SGT based PBR.
                                   (ASA software)

               Cisco Secure
                                   Secure FW 1000,      Firepower    Remote Access pxGrid             SGT over Ethernet    SG Firewall (src SGTs only before ver 6.5, src & dst
                  Firewall
                                   2100, 3100, 4100,    Threat       VPN; SGT                                              from 6.5)
                                   4200, 9300, FTDv     Defense      assigned via
                                                        Base         pxGrid (not via
                                   (Firepower Threat                 ISE Authz)                                            SGT based PBR.
                                   Defense software)


                   Cisco           ISA 3000 Series      -            Remote Access Speaker,           SGT over Ethernet    SG Firewall (IPv4, IPv6)
                 Industrial        Software ISA 3000                 VPN (IPsec,   Listener
                  Security                                           SSL-VPN)      V3                                      SGT b based PBR.
                 Appliance




                Table 5. End of Sale Group Based Policy Platform Support Matrix
                          ( https://www.cisco.com/c/en/us/products/eos-eol-listing.html )
                          ( https://www.cisco.com/c/en/us/products/eos-eol-policy.html )
               EOS System              Platform         License     Security Group     SGT Exchange             Inline SGT Tagging                         SGT
                Component                                             Tag (SGT)        Protocol (SXP)                                                  Enforcement
                                                                     Classification     Support and                                                       ______
                                                                                          Version                                                        Services


                                   Catalyst 2960-      LAN Base     Dynamic,          Speaker             No                               No
              Cisco Catalyst
                               ®   S and 2960-SF       K9           IP to SGT,        V4 Note1
                                   Series                           VLAN to SGT,
                2000 Series
                                                                    Subnet to SGT

                                   Catalyst 3560-      IP Base K9 (L2 adjacent        Speaker, Listener   No                               No
                                   E and 3750-E                   hosts only)         V2
                                   Series                         Dynamic,
                                                                  IP to SGT,
                                                                  VLAN to SGT

               Cisco Catalyst
                              Catalyst 3560-           IP Base K9 (L2 adjacent        Speaker             SGT over Ethernet,               SGACL Note16
                3000 Series
                              X and 3750-X                        hosts only)         V4                  SGT over VXLAN                   (Maximum of 8 VLANs on a VLAN-
                              Series                              Dynamic,                                                                 trunk link)
                                                                  IP to SGT
                                                                  (prefix must be
                                                                  32),
                                                                  VLAN to SGT,
                                                                  Port to SGT
                                                                  (only on switch
                                                                  to switch links)
                                   Cisco Catalyst      IP Base K9 Dynamic, IP to      Speaker, Listener   No                               No
               Cisco Catalyst 4948 Series                         SGT                 V4
                4500 Series




© 2026 Cisco and/or its affiliates. All rights reserved. This document is Cisco Public information                                                                          11
```

## PDF page 12

```text
                                Cisco Nexus       Base         IP to SGT1,        Speaker, Listener   SGT over Ethernet.                SGACL
                                7000 F2-          License      Port Profile to    V3                  4
                                                                                                       : M & F2e (Copper-) all ports;
                                Series***         NX-OS 6.1    SGT, VLAN                              F2e (SFP) - last 8 ports; All
                                modules           and later    to SGT2,                               others- no support
                                                               Port to SGT2
                                                               Subnet to
                                                               SGT5
                                                               1
                                                                :FabricPath
                                                               support
               Cisco Nexus®
                                                               requires
                7000 Series
                                                               6.2(10) or later
                                                               2
                                                                 VPC/VPC+
                                                               support
                                                               requires
                                                               7.2(0)D1(1) or
                                                               later.
                                                               5
                                                                 Subnet to
                                                               SGT requires
                                                               7.3(0)D1(1) or
                                                               later.

                                5760 Wireless     IP Base K9 Dynamic,             Speaker, Listener   SGT over Ethernet                 SGACL
                                Controller                   IP to SGT,           V4
                                Series                       VLAN to SGT,
                                                             Port to SGT,
                                                             Subnet to
                                                             SGT
                              Wireless            -          Dynamic              Speaker V2          No                                No
                              Services
               Cisco Wireless Module 2
                 Controller   (WiSM2)


                                Flex 7500         -            Dynamic            Speaker V2          No                                No
                                Series Wireless
                                Controller


                                ASR 1001,         IP         IP to SGT,     Speaker, Listener         SGT over Ethernet,                SG Firewall
                                1002              Base/K9    Subnet to SGT, V4                        SGT over GETVPN, IPsec VPN,
                                                  for        L3IF to SGT                              or DMVPN                          SGT based PBR (1000 RP2)
               Cisco Aggreg-                      classify/
               ation Services                     propagate.                                                                            SGT based QoS.
                   Router                                                                                                               SGT Caching.
                                                  Security/K
                   (ASR)                          9 for                                                                                 SGT NetFlow v9
                                                  enforce-
                                                  ment

                              ISE 3315, 3355,                                                         –                                 –
               Cisco Identity 3395,
                 Services     Appliance
                  Engine


                                ASA 5510,         -                               Speaker, Listener                                     SG Firewall
                                5520, 5540,                                       v2
                                5550

                   Cisco        ASA               -            Remote             Speaker, Listener   SGT over Ethernet                 SG Firewall (IPv4, IPv6)
                 Adaptive       5505Note3,                     Access VPN         V2 (IPv4, IPv6)
                  Security      5512, 5515,                    (IPsec, SSL-                                                             SGT based PBR.
                 Appliance      5525, 5545,                    VPN)
                                5555, 5585

                                ASA 5512-X,       -            Remote             Speaker, Listener   SGT over Ethernet                 SG Firewall (IPv4, IPv6)
                                5515-X, 5585-                  Access VPN
                                                               (IPsec, SSL-       V3
                                X with                                                                                                  SGT based PBR.
                                FirePower                      VPN)
                                Services

               Cisco Fire       FirePOWER         Threat &     -                  -                   SGT over Ethernet                 -
               POWER            7000 and 8000     Apps (TA)
                                Series




© 2026 Cisco and/or its affiliates. All rights reserved. This document is Cisco Public information                                                                 12
```

## PDF page 13

```text
                  Cisco Group Based Policy scalability is platform dependent. The tables below provide insight into the SXP maximum
                  number of connections (peers) a platform is able to support along with the maximum number of IP-SGT bindings that
                  can be managed. Table 6 show switch, wireless, and security products, Table 7 shows ISE SXP scaling, and Table 8
                  shows router product scalability. Table 6 results use a CPU load method, except for newer ASA and Firepower results
                  which use a CPS (connections per second) traffic load with a maximum performance degradation of 5%. The CPS
                  method is considered a better measure for firewalls. Table 9 lists select platform maximum number of supported
                  SGACLs.


                Table 6. Cisco Group Based Policy Platform Scalability of Switch, Wireless, and Security Products
                                 Platform                Maximum SXP connections      Maximum IP-SGT bindings                    Comments




               Catalyst 2960-S Series                   1,000                                        1,000

               Catalyst 2960-X & 2960-XR Series         1,000                                        1,000


               Catalyst 3750-X & 3560-X Series          1,000 (500 Bidirectional)                  200,000
               (non-stack)
               Catalyst 3650 & 3850 Series              256 (128 Bidirectional)                     12,000

               Catalyst 4500 Supervisor                 1,000 (900 Bidirectional)         100,000 routed/L3
               Engine 6-E
                                                                                         2,000 Switched/L2
               Catalyst 4500 Supervisor Engine          1,800 (900 Bidirectional)         128,000 routed/L3
               7-E, 8-E                                                                  2,000 Switched/L2
               Catalyst 4500 Supervisor Engine 7L-E, 1,800 (900 Bidirectional)             32,000 routed/L3
               8L-E                                                                      2,000 Switched/L2

               Catalyst 4500-X Series                   1000                              32,000 routed/L3
                                                                                         2,000 Switched/L2
               Catalyst 6500 Series Supervisor          2000 (1,000 Bidirectional)                 200,000
               Engine 720
               Catalyst 6500 Series Supervisor          2000 (1,000 Bidirectional)                 256,000
               Engine 2T and 6T
               Catalyst 6800 Series                     2,000 (1,000 Bidirectional)                256,000


               Catalyst 9200L                           200 (100 Bidirectional)                      8,081


               Catalyst 9200                            200 (100 Bidirectional)                     10,000
               Catalyst 9200CX
               Catalyst 9300/L/LM Series                256 (130 Bidirectional)                     10,000


               Catalyst 9300X                                                                       32,000


               Catalyst 9400 Supervisor     Engine-1 & 256 (130 Bidirectional)                      40,000
               Sup-1XL
               Catalyst 9400X                                                                      109,000


               Catalyst 9500                            256 (130 Bidirectional)                     40,000


               Catalyst 9500H & 9500X                                                              200,000


               Catalyst 9600/X                          240                                        200,000      200k mappings for both Sup1 and Sup2


               Industrial Ethernet 3400                 500                               1024 Host to SGT.
                                                                                         (64 subnet to SGT)

               Industrial Ethernet 9300                 512 (256 Bidirectional)         10,000 (5,000 IPv6)




© 2026 Cisco and/or its affiliates. All rights reserved. This document is Cisco Public information                                                     13
```

## PDF page 14

```text
               1540, 1560, 1570 Series                  5                                             3000
               1552 AP
               1700, 2700, 2800, 3700, AP Series
               (Wave 1)
               1815, 1830, 1850, 2800, 3800 AP Series
               (Wave 2)

               91xx AP                                  5                                            5,000    200 SGTs max



               WLC Catalyst 9800CL (Large)                                                        750,000



               WLC Catalyst 9800-40                                                               750,000



               WLC Catalyst 9800-80                                                               750,000



               WLC Catalyst 9800-L                                                                150,000



               WLC 8540, 8510 Series                    5                                           64,000


               WLC 2504                                 5                                            1,000


               WLC 3504                                 5                                            3,000

               WLC 5520                                 5                                           20,000


               WLC 5508                                 5                                            7,000


               WLC 5760 Series                          128                                         12,000


               vWLC                                     5                                           15,000


               WISM2                                    5                                           15,000


               Nexus 7000 M1 XL, M2, M3                 980 (450 Bidirectional)            200,000 (7.2, +)
                                                                                           50,000 (pre 7.2)

               Nexus 7000 M1 (non-XL)                   980 (450 Bidirectional)                   128,000


               Nexus 1000V                              ?? (64 Bidirectional)                        6,000    NX-OS 5.2(1)SV3(3.1)

               Nexus 7000 F2, F2e                       980 (450 Bidirectional)                     32,000    Recommend 25,000 for planning purposes


               Nexus 7000 F3                            980                                         64,000    Recommend 50,000 for planning purposes

               Nexus 6000, 5600, 5500                   4 per VRF                 2,000 per SXP connection    Max of 4 VRF

               Nexus 1000v                              64 (32* Bidirectional               6,000 per VSM     *: Bidirectional max not tested; SGACL & IP-SGT
                                                        connections)                                          mappings pushed from ISE via SSH


               ASA 5505                                 10                                             250


               ASA 5510                                 25                                           1,000


               ASA 5520                                 50                                           2,500


               ASA 5540                                 100                                          5000


               ASA 5550                                 150                                          7,500


               ASA 5580-20                              250                                         10,000


               ASA 5580-40                              500                                         20,000




© 2026 Cisco and/or its affiliates. All rights reserved. This document is Cisco Public information                                                      14
```

## PDF page 15

```text
               ASA 5585-SSP10                        150                              18,750


               ASA 5585-SSP20                        250                              25,000


               ASA 5585-SSP40                        500                              50,000


               ASA 5585-SSP60                        1,000                          100,000


               ASA 5506-X                            2,000                          195,000


               ASA 5555-X                            2,000                          500,000


               FP-2100 running ASA code              TBD                                TBD     Expected to be similar to FP-4100


               FP-4110 running ASA code              2,000                                 1M


               FP-9300 SM-36 running ASA code        2,000                                 1M


               FTD running on vFTD, KVM, VMWare, pxGrid                               64,000
               AWS, Azure
               FTD running on ASA 5508, 5516, 5525, pxGrid                            64,000
               5545, 5555
               FTD running on Firepower 1000, 1010, pxGrid                            64,000
               1100, 1120, 1140, 1150
               FTD running on Firepower 2110, 2120, pxGrid                            64,000
               2130, 3105, 3110, 3120, 4110
               FTD running on Firepower 2140, 3130, pxGrid                          150,000
               3140, 4112, 4115, 4120, 4125
               FTD running on Firepower 9300 and     pxGrid                         300,000
               4145, 4215
               FTD running on Firepower 4225, 4245   pxGrid                         315,000


               ISE 3495 ISE 2.0                      20                             100,000


               ISE 2.1 with single SXPN              100                            250,000


               ISE 2.1 with 2 SXPN                   200                            500,000


               ISE 2.4 -> 3.1                        200                     350,000 (1 pair)   Minimum 6 nodes redundant
                                                                             700,000 (2 pair)   Max 4 SXPSN pairs supported
                                                                           1,050,000 (3 pair)
                                                                           1,400,000 (4 pair)

               Open Daylight SDN Controller          100                              25,000
               Nitrogen Release
               Cisco Web Security Appliance (WSA)                                   150,000




                Table 7. Cisco Identity Services Engine (ISE) SXP Scaling
                                                                                                      Max
                                                                                   Max
                                                                                                ISE SXP Bindings
                                                                            ISE SXP Bindings
                     Deployment Type                 Platform   Max PSNs                           (Dedicated           Max ISE SXP Peers
                                                                              (Shared SXP &
                                                                                                    RADIUS &
                                                                              RADIUS PSNs)
                                                                                                    SXPSNs)
               Standalone All personas on     3515                 0               3,500                      N/A                   20
               same node,
                                              3595                 0               20,000                     N/A                   30
               2 nodes redundant
                                              3615                 0               12,500                     N/A                   30
                                              3655/3715            0               25,000                     N/A                   40
                                              3695/3755/3795       0               50,000                     N/A                   50
               Uniified PAN+MnT on same       3515 as PAN+MNT      6               3,750                    7,500               200
               node and dedicated PSNs
               Minimum 4 nodes redundant      3595 as PAN+MNT      6               10,000                  20,000               200



© 2026 Cisco and/or its affiliates. All rights reserved. This document is Cisco Public information                                       15
```

## PDF page 16

```text
                                               3655 as PAN+MNT                  6                  12,500                        25,000              200
                                               3695 as PAN+MNT                  6                  25,000                        50,000              200
                                               3715 as PAN+MNT                  6                  37,500                        75,000              200
                                               3755/3795 as                     6                  75,000                      150,000               200
                                                PAN+MNT
                Dedicated All personas on      3595/3655 as PAN                 50                  N/A                350,000 (1 pair)          200 (1 pair)
                dedicated nodes.                and MnT                                                                500,000 (2 pair)          400 (2 pair)
                Minimum 6 nodes redundant
                                               3595/3695/3755/3795              50                  N/A                 350,000 (1 pair)         200 (1 pair)
                                                as PAN and Large                                                        700,000 (2 pair)         400 (2 pair)
                                                MNT                                                                   1,050,000 (3 pair)         600 (3 pair)
                                                                                                                      1,400,000 (4 pair)         800 (4 pair)




                 Table 8. Cisco Group Based Policy Platform Scalability of Router Products
                          Platform              Maximum Unidirectional    Maximum Bidirectional                        Maximum IP SGT Bindings
                                                   SXP Connections          SXP Connections
                                                (Speaker only/ Listener
                                                        only)

               890 Series Routers              100                                                 1,000

               1900 Series Routers             500                        250                      100,000 with unidirectional SXP connections
                                                                                                   25,000 with bidirectional SXP connections

               2900, 3900 Series ISRG2         250                        125                      180,000 with unidirectional SXP connections
                                                                                                   125,000 with bidirectional SXP connections


               4400 Series ISR                 1800                       900                      750,000 (IOS XE 3.15 and 3.16)
                                                                                                   135,000 (IOS XE earlier than 3.15)

               ASR 1000 Series                 1800                       900                      750,000 uni-directional (IOS XE 3.15 and 3.16)
                                                                                                   180,000 (IOS XE earlier than 3.15)
               ASR 1006 RP2 as SXP Reflector                              250 with 100 bindings,
                                                                          126 with 500 bindings

               Cloud Services Router 1000V     900                        450                      750,000 (IOS XE 3.15 and        3.16)
               Series (CSR)                                                                        135,000 (IOS XE earlier than 3.15)

               C8500, C8400, C8300, C8500-     1800                       900                      750,000 IPv4 and IPv6 in both SDWAN controller and
               G2, C8400-G2, C8300-G2                                                              Autonomous modes.


               C8200-G2                        500                        250                      390,000 bindings



               C8200-1N-4T                     1800                       900                      135,000 bindings



               C8200L-1N-4T                    500                        250                      135,000 in both SDWAN controller and Autonomous modes.



               C8100-G2                        100                        50                       10,000 bindings



               C8000V 16vCPU/16GB              1800                       900                      720,000 IPv4 and IPv6 in SDWAN controller mode.
                                                                                                   750,000 IPv4 and IPv6 in Autonomous mode.


               C8000V 8vCPU/8GB                900                        450                      720,000 IPv4 and IPv6 in SDWAN controller mode.
                                                                                                   750,000 IPv4 and IPv6 in Autonomous mode.




© 2026 Cisco and/or its affiliates. All rights reserved. This document is Cisco Public information                                                              16
```

## PDF page 17

```text
               C8kV-4vCPU/8GB & C8000V             250                          125                   100,000 IPv4 and IPv6 in both SDWAN controller and
               2vCPU/4GB                                                                              Autonomous modes.


               ISR1121X-8P                         500                          250                   100,000 IPv4 and IPv6 in both SDWAN controller and
                                                                                                      Autonomous modes.




                 Table 9. Cisco Group Based Policy Platform Scalability of SGACLs
                                Platform                    Maximum number of SG ACEs                                            Notes


               Catalyst 3750-X & 3560-X                                                        1015 maximum unique cells


               Catalyst 3650                             1,350                                 Max # of ACEs in SGACL should be 300 or less due to buffer size limits
               Catalyst 3850-SE, 3850-XS                                                       256 Source to unique Destination Groups
               Catalyst 3850                                                                   4,000 SGT/DGT Policies

               Catalyst 4500-X,                          64,000                                Ranges between 64,000 ACEs in 1 SGACL to 1 ACE in 64,000 SGACLs
               Catalyst 4500 Sup 7-E/7L-E/8-E/8L-E


               Catalyst 6500 Series Supervisor           16,000
               Engine 2T and 6T

               Catalyst 6840-X                           16,000

               Catalyst 6880-X                           64,000 (XL), 16,000 (LE)


               Catalyst 9200/L                           1,408                                 256 Source to unique Destination Groups in releases < 17.2, then 4,096
               Catalyst 9200CX                                                                 from 17.2
                                                                                               2,000 SGT/DGT Policies
               Catalyst 9300/L/LM                        Total ACL entries: 5,000              256 Source to unique Destination Groups in releases < 17.2, then 4,096
                                                                                               from 17.2
                                                                                               8,000 SGT/DGT Policies

               Catalyst 9300X                            Total ACL entries: 4,800              4,096 Source to unique Destination Groups
                                                                                               7,400 SGT/DGT Policies


               Catalyst 9400 Supervisor Engine-1 & -     18,000                                256 Source to unique Destination Groups in releases < 17.2, then 4,096
               1XL                                                                             from 17.2
                                                                                               8,000 SGT/DGT Policies
               Catalyst 9400X                            16,000                                32,000 SGT/DGT Policies

               Catalyst 9500                             18,000                                256 Source to unique Destination Groups in releases < 17.2, then 4,096
                                                                                               from 17.2
                                                                                               8,000 SGT/DGT Policies
               Catalyst 9500H & 9500X                    27,000                                32,000 SGT/DGT Policies

               Catalyst 9600 Sup-1 & Sup-2               Total number of ACE entries: 27,000   256 Source to unique Destination Groups in releases < 17.2, then 4,096
                                                                                               from 17.2
                                                                                               SGT/DGT policies 32,000

               Industrial Ethernet 3400                  6630                                  SGT/DGT 21 * 21, Max ACE per SGACL 15

               Industrial Ethernet 9300                  1,408                                 2,000 SGT/DGT policies


               1540, 1560, 1570 Series                   256 ACEs per SGACL                    400 unique SGACLs, 50 SGTs
               1552 AP
               1700, 2700, 2800, 3700, AP Series
               (Wave 1)
               1815, 1830, 1850, 2800, 3800 AP
               Series (Wave 2)



© 2026 Cisco and/or its affiliates. All rights reserved. This document is Cisco Public information                                                                  17
```

## PDF page 18

```text
               91xx AP                                                           Validated for 50 SGTs and 200 unique SGACLs per AP


               WLC Catalyst 9800-40             32,000 ACE’s                     512 Max no. SGTs
                                                                                 256 Max no. ACE’s per SGACL
                                                                                 128 Max no. unique SGACLs
                                                                                 65,536 SGT/DGT Policy recommended limit (256*256*16*256)

               WLC Catalyst 9800-80             96,000 ACE’s                     512 Max no. SGTs
                                                                                 256 max no. ACE’s per SGACL
                                                                                 128 Max no. unique SGACLs
                                                                                 65,536 SGT/DGT Policy recommended limit (256*256*16*256)

               WLC 8540, 5520, 3504             256 ACEs per SGACL               800 unique SGACLs, 512 SGTs

               Nexus 7K M3, M2, M1 Modules      128,000


               Nexus 7K F3, F2, F2e Modules,    16,000


               Nexus 7K F1 Modules              1024


               Nexus 1000V                      6,000

               Nexus 5500                       124                              124 SGACL TCAM entries available per bank of 8 ports for feature use (4
                                                                                 of 128 are default entries)
                                                                                 Sum of SGACL entries per 8 port bank cannot contain more than 124
                                                                                 permissions in total
                                                                                 SGACL can be reused extensively; Over 2000 SGT, DGT combinations
                                                                                 possible from reusing 124 lines of permissions

               Nexus 5600, 6000                 1148


               ASR 1000                         4,096 per cell                   62,500 maximum number of unique cells


               C8500, C8400, C8300, C8500-G2,   64,000                           64,000 SGT/DGT Policies
               C8400-G2, C8300-G2
               C8000V 16vCPU/16GB
               C8000V 8vCPU/8GB


               C8200-G2                         20,000                           20,000 SGT/DGT Policies




               C8200-1N-4T                      62,000                           62,000 SGT/DGT Policies




               C8200L-1N-4T                     20,000                           20,000 SGT/DGT Policies

               C8kV-4vCPU/8GB & C8000V          10,000                           10,000 SGT/DGT Policies
               2vCPU/4GB
               C8100-G2                         10,000                           8,000 SGT/DGT Policies


               ISR1121X-8P                      10,000                           10,000 SGT/DGT Policies




                  Table 10 provides cross-platform group-based policy exchange interoperability testing results. Application
                  Centric Infrastructure (ACI) and Group Based Policy integration enables customers to apply consistent
                  security policy across the enterprise- leveraging user roles and device type together with application context.
                  The validated Open Source Open Daylight SDN use case included Nexus 7k SXPv3, ASA SXPv3, and
                  OpenDaylight SXPv4 (Nitrogen and earlier releases) working together in the Data Center.




© 2026 Cisco and/or its affiliates. All rights reserved. This document is Cisco Public information                                                   18
```

## PDF page 19

```text
                  Table 10. TrustSec Group-Based Policy (GBP) Interoperability
                     System Component                   Platform         Solution-Level          Group Information       Interoperability Platform & Propagation method
                                                                        Validated Version           Exchange

               Cisco Nexus 9000 Series            Cisco 9000          NX-OS 13.2 (4e)
               Switches                           Series:
                                                  Spine & Leaf                               EndPoint Group – Security
                                                                                             Group Mappings via
                                                                                                                         Cisco ISE 2.4 Patch 6 ACI API
                                                                                             TrustSec-ACI policy and
               Cisco Application Policy           Cisco APIC-DC       APIC-DC 3.2 (4e)
                                                                                             data plane exchange
               Infrastructure Controller – Data                       Policy plane;
               Center
               Nexus 9k (in L2 mode) can          Cloudscale ASICs    NX-OS 9.3.3            Nexus 9k in L2 mode can     Providing interoperability in CTS enabled
               forward an SGT tagged packet       in Standalone NX-                          propagate SGT unmodified    environments.
               unmodified.                        OS mode.                                   between two CTS devices
                                                  FX, FX2, FX3 and                                                       NO PLANS for generating or rewriting SGT in
                                                  GX                                                                     packets.
                                                                                                                         NO PLANS for classification or enforcement in
                                                                                                                         standalone NX-OS mode.
               Nexus 9k (in L3 mode) can          Cloudscale ASICs    NX-OS 10.2.2F          Nexus 9k in L3 mode to      Providing interoperability in CTS enabled
               forward an SGT tagged packet       in Standalone NX-                          propagate SGT unmodified    environments.
               unmodified.                        OS mode.                                   between two CTS devices
                                                  FX, FX2, FX3 and                                                       NO PLANS for generating or rewriting SGT in
                                                  GX                                                                     packets.
                                                                                                                         NO PLANS for classification or enforcement in
                                                                                                                         standalone NX-OS mode.
               Meraki Adaptive Policy.            Security & SD-      MX17 Beta.
               Adaptive Policy transport across WAN (MX)              Subsequent major FW
               MX LAN and AutoVPN for full-                           version will support
               stack LAN segmentation                                 Adaptive Policy
                                                                      enforcement.

               Open Daylight SDN controller       ODL SDN             Lithium, Beryllium,    SGT via SXP v4              Cisco ISE 2.1- SXP v4
                                                                      Carbon                                             Nexus 7000 7.3- SXP v3
                                                                                                                         ASA 9.6.1- SXP v3

               Open Daylight SDN controller       ODL SDN             Nitrogen               IPv4, IPv6 SXP Peering      Cisco ISE 2.4
                                                                                                                         ASR 1001-X IOS XE 16.5.1b
                                                                                                                         CSR 1000v IOS XE 16.6.3
                                                                                                                         Cat 6500 IOS 15.4(1)SY2
                                                                                                                         Cat 3850 IOS 3.6.8E




                 Notes
                  1: Catalyst 2960 S/SF Product management recommends 15.0(2)SE which supports SXP v2.
                  2: Product part numbers of supported line cards for SGT over Ethernet on the Cisco Catalyst 4500 Supervisor
                    Engine 7-E, 7L-E, 8-E, and 8L-E include the following: WS-X4712-SFP+E, WS-X4712-SFP-E, WS-X4748-
                    UPOE+E, WS-X4748-RJ45V+E, WS-X4748-RJ45- E, WS-X4724-SFP-E, WS-X4748-SFP-E, and WS-X4748-
                    12X48U+E.
                  3: Cisco ASA 5505 does not support releases after 9.2.
                  4: Cisco Nexus 7000 F1-Series modules do not support Cisco TrustSec.
                  5: Use of inline tagging with LACP requires future IOS XE Denali or IOS 3.7 release (CSCva22545)
                  6: For SXP support, AP must run in FlexConnect Mode
                  7: With IPv6 support, DGT can be IPv4.
                  8: Prior versions of this document listed Cisco Catalyst 3750-X validated version, IOS 12.2(3)E1, and WLC AireOS
                    8.1. These releases have been deferred.


© 2026 Cisco and/or its affiliates. All rights reserved. This document is Cisco Public information                                                                       19
```

## PDF page 20

```text
                 9: When inline tagging (SGToE) is enabled with the VIC 12xx and VIC 13xx, packet processing is handled at the
                   processor level which will attribute to lower network I/O performance. An alternative solution is to use Intel
                   adaptors.
                 10: IOS XE Everest 16.6.2 SMU is required for ISE BYOD, Guest, and Posture features. See ISE Compatibility
                   Matrix: https://www.cisco.com/c/en/us/support/security/identity-services-engine/products-device-support-tables-
                   list.html
                 11: The IE 4000 and IE 5000 platforms perform similarly to the Catalyst 3560-X and 3750-X platforms in the
                   reliance on IP Address, MAC Address, and physical port/VLAN of the device, learned via dot1x or MAB or IP
                   Device Tracking (IPDT). These devices cannot use information learned via SXP for either enforcement or tag
                   propagation as the device is not directly attached. SXP v4 is supported in Speaker mode only.
                 12: Catalyst 4500 Series Release 3.9 and later, with the introduction of VRF, an SVI is needed for L3 lookup to
                   derive SGT for switched traffic, and an SVI is also needed on the VLAN for the derivation of source group for L2
                   traffic.
                 13: The N7K must have an SVI on the VLAN if the mappings reside in the VRF. If N7K is L2 only, create an SVI
                   without IP to be able to utilize the mappings from the VRF. SVI is not required if entered into the VLAN.
                 14: Dynamic classification with IEEE 802.1x on Nexus 1000V requires 5.2(1)SV3(4.1). This is validated with
                   VMware Horizon 7 VDI.
                 15: Port based platforms cannot do enforcement of policy for remote IP addresses, ie. they can only classify or
                   enforce IP addresses present in the IPDT table (hosts that are L2 adjacent).
                 16: Port based platforms cannot do enforcement of policy for remote IP addresses, ie. they can only classify or
                   enforce IP addresses present in the IPDT table (hosts that are L2 adjacent).
                 17: IPv6 SGACL Support added in IOS-XE 16.10.1 and validation in solution validation 6.5 release was carried out
                   with IOS-XE 16.12.1
                 18: For the C82xx and C83xx, the following WAN modules do support SGT inline tagging: C-NIM-2T, C-NIM-1M,
                   C-NIM-1X.
                 19: IE3400 supports SGACL on base switch and only on IEM-3400 expansion modules. IEM-3300-8P and IEM-
                   3300-16P are non-FPGA expansion modules on the 3400 and do not support enforcement. When non-FPGA
                   expansion module used then base 3400 does not support enforcement.




© 2026 Cisco and/or its affiliates. All rights reserved. This document is Cisco Public information                                    20
```

## PDF page 21

```text
 Printed in USA                                                                                      C96-731479-00 v6.4c   1/19




© 2026 Cisco and/or its affiliates. All rights reserved. This document is Cisco Public information                          21
```
