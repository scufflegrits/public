# c8300-edge-datasheet-2026-10-06.pdf — extracted text

- Source PDF: [c8300-edge-datasheet-2026-10-06.pdf](c8300-edge-datasheet-2026-10-06.pdf)
- PDF title metadata: Cisco Catalyst 8300 Series Edge Platforms Data Sheet
- Publisher: Cisco (as registered in the research source entries).
- Source SHA-256: `080c1fb4ec06d188943ff5d5aea4f24a408fae4f614e9ba08c48a2567865c669`
- Converted: 2026-10-31 (UTC).
- Extraction tool: `pdftotext version 25.03.0`.
- Command: `pdftotext -layout -enc UTF-8 reference/c8300-edge-datasheet-2026-10-06.pdf -`.
- PDF pages: 24; page headings below use PDF page numbers.
- Language: English; no OCR or translation performed.
- Extraction diagnostics: Syntax Warning: Invalid Font Weight (13 occurrences); verify table values against the PDF.
- Source access date and document revision: see the original source-register entries below; conversion does not update them.
- Source register: [C8300-4T2X-DS-1](../research-cisco-c8300-1n1s-4t2x-r1.1.0.md#c8300-4t2x-ds-1).
- Source register: [C8300-6T-DS-1](../research-cisco-c8300-1n1s-6t-r1.1.0.md#c8300-6t-ds-1).
- Source register: [C8375-C83DS-1](../research-cisco-c8375-e-g2-r1.1.0.md#c8375-c83ds-1).
- Source register: [ISR4431-DS-3](../research-cisco-isr4431-r1.1.0.md#isr4431-ds-3).

> This is layout-preserving plain-text extraction wrapped in Markdown,
> not a semantic reconstruction of tables. Fixed-width text blocks preserve
> column spacing, but reading order, merged cells, and glyphs can still be
> imperfect. Images, diagrams, and image-based tick marks are not transcribed.
> Verify consequential table values against the linked original PDF.

## PDF page 1

```text
    Data sheet
    Cisco public




                    Cisco Catalyst 8300 Series
                          Edge Platforms




    © 2026 Cisco and/or its affiliates. All rights reserved.   Page 1 of 24
-
```

## PDF page 2

```text
    Contents
    Product overview                                                     3
    Platform details                                                     5
    Platform Performance                                                 6
    Overall platform benefits                                            8
    Supported modules                                                  12
    Memory, storage, and accessory options                             15
    Optics and transceivers modules                                    16
    Resiliency and high availability                                   16
    Power supplies                                                     16
    Software requirements                                              18
    Software features                                                  18
    Licensing                                                          20
    Cisco Smart Licensing                                              20
    Specifications                                                     20
    Ordering information                                               22
    Cisco Services                                                     22
    Cisco Capital                                                      23
    For more information                                               23
    Document history                                                   24




    © 2026 Cisco and/or its affiliates. All rights reserved.   Page 2 of 24
-
```

## PDF page 3

```text
    The Cisco Catalyst 8300 Series Edge Platforms are best-of-breed, 5G-ready, cloud
    edge platforms designed for accelerated services, multi-layer security, cloud-native
    agility, and edge intelligence to accelerate your journey to cloud.




    Cisco Catalyst 8300 Series Edge Platforms (Catalyst 8300) with Cisco IOS XE SD-WAN Software deliver
    Cisco’s secure, cloud-scale Catalyst SD-WAN solution for the branch. The Catalyst 8300 Series is
    purpose-built for high performance and integrated SD-WAN Services along with flexibility to deliver
    security and networking services together from the cloud or on premises. It provides higher WAN port
    density and a redundant power supply capability. The Catalyst 8300 Series Edge Platforms have a wide
    variety of interface options to choose from—ranging from lower and higher module density with backward
    compatibility to a variety of existing WAN, LAN, voice, and compute modules. Powered by Cisco IOS XE,
    fully programmable software architecture, and API support, these platforms can facilitate automation at
    scale to achieve zero-touch IT capability while migrating workloads to the cloud. Catalyst 8300 Series
    Edge Platforms also come with Trustworthy Solutions 2.0 infrastructure that secures the platforms against
    threats and vulnerabilities with integrity verification and remediation of threats.

    The Catalyst 8300 Series Edge Platforms are well suited for medium-sized and large enterprise branch
    offices for high WAN IPSec performance with integrated Cisco Catalyst SD-WAN services.


    Product overview
    Product highlights

    Table 1.        Product highlights

     Product feature                           Benefits and description

     Multicore processors                        ● 8 or 12 core CPU with 8-GB memory default (up to 32 GB memory upgrade)

                                                 ● High-performance multicore processors support high-speed WAN connections.

                                                 ● Dynamic core allocation architecture that can leverage data plane cores for I/O and
                                                   service plane as per-user configuration.

     Embedded IPsec VPN                          ● Up to 9.3 Gbps of IPSec Internet Mix (IMIX) traffic
     hardware acceleration
                                                 ● Increases scalability for IPSec throughput needs for medium- and large-sized branches

                                                 ● SSL and crypto hardware acceleration


     Integrated Gigabit Ethernet                 ● Provides 6 built-in Layer 3 Ethernet ports for WAN or LAN with port speeds ranging from
     ports                                         10Mbps, 100Mbps, 1Gbps and up to 10Gbps, depending on platform model
                                                 ● All platforms have at least 2 Ethernet ports that can support Small Form-Factor
                                                   Pluggable (SFP or SFP+) based connectivity in addition to 4 RJ-45 connections, enabling
                                                   fiber or copper connectivity.




    © 2026 Cisco and/or its affiliates. All rights reserved.                                                                         Page 3 of 24
-
```

## PDF page 4

```text
     Product feature                           Benefits and description

     DRAM                                        ● All Catalyst 8300 platforms have 8GB default DRAM and can be upgraded to 16GB and
                                                   32GB for higher scale and performance.

     Flash memory support                        ● All Catalyst 8300 platforms have an integrated on-board 8GB flash and it is not
                                                   upgradeable. M.2 storage provides upgrade options for additional storage.

     M.2 storage                                 ● All the Catalyst 8300 models ship with default 16GB M.2 USB for SD-WAN logging and
                                                   additional storage on the platform. It can be upgraded to 32GB M.2 USB and to 600GB
                                                   or 2TB M.2 Non-Volatile Memory Express (NVMe)

     Default dual power supplies                 ● All Catalyst 8300 platforms ship with dual power supplies for redundancy.

                                                 ● AC Power over Ethernet (PoE), DC and Reversed-airflow DC (NEBS) options are
                                                   available on all models.
                                                 ● Enabling PoE ports on Network Interface Modules (NIM) or on Service Modules (SM)
                                                   requires at least one PoE supporting PSU to be installed

     Modularity and form factor                  ● 1RU and 2RU form factor

                                                 ● Supports SM, NIM, and Pluggable Interface Module (PIM) slots


     Integrated security                         ● Advanced security features available on-box, including Next-Generation Firewall
                                                   (NGFW) with Application Awareness, IPS/IDS, Advanced Malware Protection, URL
                                                   filtering, and Cisco Umbrella® Secure Internet Gateway (SIG) (Secure Access Service
                                                   Edge [SASE])
                                                 ● Hardware-anchored Secure Boot and Secure Unique Device Identification (SUDI)
                                                   support for Plug and Play to verify the identity of the hardware and software

     Dedicated management for                    ● Netops: manage routers through Catalyst SD-WAN manager or Cisco DNA Center
     netops and secops
                                                 ● Secops: option to combine security policy management and visibility of the integrated
                                                   NGFW with standalone Cisco Secure Firewalls as well as other security technologies
                                                   through Cisco Security Cloud Control
                                                   ◦ Unified security enforcement and visibility across all Cisco NGFWs-standalone and
                                                      router-integrated
                                                   ◦ Create objects that can be shared across Cisco security technologies as well as
                                                      configure policies and push them to the desired enforcement point
                                                   ◦ Visualize the router NGFW and Cisco Secure Firewall logs in the same dashboard and
                                                      view




    © 2026 Cisco and/or its affiliates. All rights reserved.                                                                         Page 4 of 24
-
```

## PDF page 5

```text
    Platform details
    Models and configurations

    Figures 1 through 4 highlight the different models included in the Catalyst 8300 Series Edge Platforms.




    C8300-2N2S-4T2X is a 2RU platform with 2 SM and 2 NIM slots plus 2 x 10Gbps and 4 x 1Gbps embedded Layer3
    Ethernet ports




    C8300-2N2S-6T is a 2RU platform with 2 SM and 2 NIM slots plus 6 x 1Gbps embedded Layer3 Ethernet ports




    C8300-1N1S-4T2X is a 1RU platform with 1 SM slot and 1 NIM slot plus 2 x 10Gbps and 4 x 1Gbps embedded Layer3
    Ethernet ports




    C8300-1N1S-6T is a 1RU platform with 1 SM slot and 1 NIM slot plus 6 x 1Gbps embedded Layer3 Ethernet ports




    © 2026 Cisco and/or its affiliates. All rights reserved.                                                      Page 5 of 24
-
```

## PDF page 6

```text
    Tables 2 and 3 detail platform specifications and performance, respectively.

    Table 2.         Cisco Catalyst 8300 Series specifications

        Model                       Description                          10G port      1G port     Slots        Memory     Storage
                                                                         density       density                  (DRAM)     (M.2 SSD)
                                                                                                                default    default

        C8300-2N2S-4T2X             C8300 2RU w/ 10G WAN                 2             4           2 SM         8 GB       16 GB
                                    (2 SM and 2 NIM slots, and                                     2 NIM
                                    2 x 10-Gigabit Ethernet
                                    and 4 x 1-Gigabit Ethernet                                     1 PIM
                                    ports)

        C8300-2N2S-6T               C8300 2RU w/ 1G WAN                  -             6           2 SM         8 GB       16 GB
                                    (2 SM and 2 NIM slots, and                                     2 NIM
                                    6 x 1-Gigabit Ethernet
                                    ports)                                                         1 PIM

        C8300-1N1S-4T2X             C8300 1RU w/ 10G WAN                 2             4           1 SM         8 GB       16 GB
                                    (1 SM slot and 1 NIM slot,                                     1 NIM
                                    and 2 x 10-Gigabit
                                    Ethernet and 4 x 1-Gigabit                                     1 PIM
                                    Ethernet ports)

        C8300-1N1S-6T               C8300 1RU w/ 1G WAN                  -             6           1 SM         8 GB       16 GB
                                    (1 SM slot and 1 NIM slot,                                     1 NIM
                                    and 6 x 1-Gigabit Ethernet
                                    ports)                                                         1 PIM



    Platform Performance
    Traffic patterns and use cases

    Table 3.         Cisco Catalyst 8300 Series Catalyst SD-WAN performance

        Feature                                                C8300-2N2S-          C8300-1N1S-        C8300-2N2S-6T      C8300-1N1S-6T
                                                               4T2X (2RU w/         4T2X (1RU w/       (2RU w/ 1G WAN)    (1RU w/ 1G WAN)
                                                               10G WAN)             10G WAN)

        SD-WAN IPsec Throughput                                Up to 18.8Gbps       Up to 17Gbps       Up to 2Gbps        Up to 2Gbps
        (1400Bytes)

        SD-WAN IPsec Throughput with IQDF**                    Up to 18.8Gbps       Up to 17Gbps       Up to 2Gbps        Up to 2Gbps
        (1400Bytes)

        SD-WAN IPsec Throughput (IMIX*)                        7.6Gbps              6.3Gbps            1.8Gbps            1.8Gbps

        SD-WAN IPsec Throughput with IQDF**                    5.6Gbps              5.5Gbps            1.7Gbps            1.7Gbps
        (IMIX*)

        SD-WAN Overlay Tunnels scale                           6000                 6000               6000               6000

    *
         IMIX is average packet size of 352 Bytes packet size

    **
         IQDF traffic pattern: IPSec + Quality of Service (QoS) + Deep Packet Inspection (DPI) + Flexible Netflow (FNF)




    © 2026 Cisco and/or its affiliates. All rights reserved.                                                                        Page 6 of 24
-
```

## PDF page 7

```text
    Catalyst SD-WAN Multi-layer security performance use cases

    The Cisco Catalyst 8300 Series Edge platforms connect branch offices to the Internet and cloud, with
    industry-leading protection against major web attacks. Table 3b below provides test results for three
    common Multi-layer Security use cases in Catalyst SD-WAN.

           ●   The first use case is with 50% of the traffic encrypted in IQDF traffic pattern (IPSec + Quality of Service
               (QoS) + Deep Packet Inspection (DPI) + Flexible Netflow (FNF) and another 50% of unencrypted Direct
               Internet Access (DIA) traffic protected by advanced security features. This protection includes NG-FW,
               IPS, URLF (URL-Filtering) and AMP (Advanced Malware Protection).
           ●   The third use case is with 100% unencrypted DIA traffic protected by the same advanced security
               features as in the second use case,

    Table 4.        Cisco Catalyst 8300 Series Catalyst SD-WAN, Multi-layer security performance use cases*

        Feature                                     C8300-2N2S-4T2X      C8300-1N1S-4T2X         C8300-2N2S-6T           C8300-1N1S-6T
                                                    (2RU w/ 10G WAN)     (1RU w/ 10G WAN)        (2RU w/ 1G WAN)         (1RU w/ 1G WAN)

        50% IQDF* + 50% (DIA w. NAT +               5.9Gbps              3.3Gbps                 2.8Gbps                 2.6Gbps
        NGFW + IPS + URLF + AMP)

        DIA w. NAT + NGFW + IPS +                   4.9Gbps              2.9Gbps                 2.3Gbps                 2.1Gbps
        URLF + AMP

    *
        Tested with IOS XE release 17.12.2. All NGFW + UTD tests with Firewall EMIX traffic profile


    Table 5.        Cisco Catalyst 8300 Series autonomous mode (non SD-WAN) performance specifications

        Feature                                      C8300-2N2S-4T2X     C8300-1N1S-4T2X         C8300-2N2S-6T           C8300-1N1S-6T
                                                     (2RU w/ 10G WAN)    (1RU w/ 10G WAN)        (2RU w/ 1G WAN)         (1RU w/ 1G WAN)

        IPv4 Forwarding Throughput                   Up to 19.7Gbps      Up to 19.7Gbps          Up to 19.7Gbps          Up to 19.7Gbps
        (1400Bytes)

        IPsec Throughput (1400Bytes)                 Up to 18.9Gbps      Up to 16.9Gbps          Up to 1.9Gbps           Up to 1.9Gbps

        IPsec Throughput (IMIX*)                     9.3Gbps             6.6Gbps                 1.9Gbps                 1.9Gbps

    *
        IMIX is average packet size of 352 Bytes packet size


    Table 6.        Cisco Catalyst 8300 Series autonomous mode (non SD-WAN) system scalability

        Feature                                       C8300-2N2S-4T2X      C8300-1N1S-4T2X            C8300-2N2S-6T       C8300-1N1S-6T
                                                      (2RU w/ 10G WAN)     (1RU w/ 10G WAN)           (2RU w/ 1G WAN)     (1RU w/ 1G WAN)

        Number of IPsec SVTI Tunnels                  4000                 4000                       4000                4000

        Number of ACLs per system                     4000                 4000                       4000                4000

        Number of IPv4 ACEs per system 72K                                 72K                        72K                 72K

        Number of IPv4 Routes                         1.6M w/ default      1.6M w/ default            1.6M w/ default     1.6M w/ default
                                                      8GB, up to 4M w/     8GB, up to 4M w/           8GB, up to 4M w/    8GB, up to 4M w/
                                                      32GB                 32GB                       32GB                32GB




    © 2026 Cisco and/or its affiliates. All rights reserved.                                                                       Page 7 of 24
-
```

## PDF page 8

```text
     Feature                                          C8300-2N2S-4T2X    C8300-1N1S-4T2X    C8300-2N2S-6T      C8300-1N1S-6T
                                                      (2RU w/ 10G WAN)   (1RU w/ 10G WAN)   (2RU w/ 1G WAN)    (1RU w/ 1G WAN)

     Number of IPv6 Routes                            1.5M w/ default    1.5M w/ default    1.5M w/ default    1.5M w/ default
                                                      8GB, up to 4M w/   8GB, up to 4M w/   8GB, up to 4M w/   8GB, up to 4M w/
                                                      32GB               32GB               32GB               32GB

     Number of Queues                                 8K                 8K                 8K                 8K

     Number of NAT Sessions                           1.2M w/ default    1.2M w/ default    1.2M w/ default    1.2M w/ default
                                                      8GB, up to 2M w/   8GB, up to 2M w/   8GB, up to 2M w/   8GB, up to 2M w/
                                                      32GB               32GB               32GB               32GB

     Number of Firewall Sessions                      512K               512K               512K               512K

     Number of VRFs                                   4000               4000               4000               4000



    Overall platform benefits
    Dynamic core allocation

    Dynamic core allocation architecture will allow you to tailor the Cisco Catalyst 8300 Series Edge platform’s
    multicore resources to fit your business needs. You can choose between two core allocations.

         ●    Service-oriented core allocation has the platform’s Multicore resources set to balance throughput with
              providing adequate resources for containerized services. Choose this if integrated, container based,
              services are required. It will allow for KVM and/or Docker container-based applications on up to 5 cores,
              depending on platform. This is the factory default core allocation with which all C8300 platforms are
              shipped.
         ●    Data plane heavy core allocation has the platform’s Multicore resources optimized for high traffic
              throughput. Choose this architecture when throughput is of higher priority, A Data plane heavy
              architecture will on 8-core platforms completely remove resources for containerized services, whereas
              on the 12-core platform, C8300-2N2S-4T2X, it will reduce service plane resources from 5 to 4 cores.In
              order to maximize the platforms performance and your investment, it’s recommended to change into a
              Data plane heavy core allocation when container-based services are not being required.
    Accelerated services with Cisco Software-Defined WAN

    Cisco Catalyst SD-WAN is a set of intelligent software services that allow you to connect users, devices,
    and branch office locations reliably and securely across a diverse set of WAN transport links. Cisco
    Catalyst 8000 Series Edge Platforms can dynamically route traffic across the “best” link based on up-to-
    the-minute application and network conditions for great application experiences. You get tight control over
    application performance, bandwidth usage, data privacy, and availability of your WAN links—control you
    need as your branches conduct greater volumes of mission-critical business with both on-premises and
    cloud controllers.




    © 2026 Cisco and/or its affiliates. All rights reserved.                                                            Page 8 of 24
-
```

## PDF page 9

```text
    SD-Routing

    Simplifying traditional routing deployment and workflows with Cisco Software-Defined Routing

    Cisco SD-Routing enables Cisco routing devices to be managed through Cisco Catalyst™ SD-WAN
    Manager, bringing operational simplicity and agility to traditional routing deployments by avoiding truck
    rolls for routine operational tasks. It also reduces OpEx by leveraging Catalyst SD-WAN Manager as the
    unified management platform for Catalyst SD-WAN as well as routing deployments.

    SD-Routing enables customers to manage their routing devices in a flexible manner through on-premises
    controllers and will also be offered through cloud-delivered controllers in the near future.

    Operationally, Cisco SD-Routing provides intuitive device lifecycle orchestration workflows for secure
    device onboarding as well as secure device software upgrades. By leveraging the rich monitoring and
    troubleshooting capabilities of Catalyst SD-WAN Manager, administrators can quickly isolate and resolve
    network problems.
    Application performance optimization

    Ensure that Cisco Catalyst SD-WAN networks meet Service-Level Agreements (SLAs) and maintain strong
    performance, even if network problems occur. With branch multi-cloud access, you can accelerate your
    SaaS applications with a simple template push from the Cisco Catalyst SD-WAN controller. Features like
    Transmission Control Protocol (TCP) optimization, forward error correction, and packet duplication help
    application performance for a better user experience.
    Application visibility

    Applications and users are more distributed than ever, and the internet has effectively become the new
    enterprise WAN. As organizations continue to embrace internet, cloud, and SaaS, network and IT teams
    are challenged to deliver consistent and reliable connectivity and application performance over networks
    and services they don’t own or directly control.

    The Catalyst 8300 Series Edge Platforms are integrated with Cisco ThousandEyes internet and cloud
    intelligence. IT managers now have expanded visibility, including hop-by-hop analytics, into network
    underlay, proactive monitoring of the Cisco Catalyst SD-WAN overlay, and performance measurement of
    SaaS applications. This granular visibility ultimately lowers the Mean Time to Identification of Issues (MTTI)
    and accelerates resolution time.
    Multi-layer security

    You can now move your traditional and complex WAN networks to a more agile software-defined WAN
    with integrated security. The Cisco Catalyst 8300 Series Edge platforms connect branch offices to the
    Internet and cloud, with industry-leading protection against major web attacks. Secure Direct Internet
    Access (DIA) to the branches helps optimize branch workloads for improved performance, specifically for
    cloud-hosted applications. At the same time, DIA ensures your branch is protected from external threats.




    © 2026 Cisco and/or its affiliates. All rights reserved.                                                  Page 9 of 24
-
```

## PDF page 10

```text
    Unified communications

    The Cisco Catalyst 8300 Edge platforms offer rich voice services in both Cisco Catalyst SD-WAN and
    traditional IOS-XE software feature stacks. Cisco is the only SDWAN vendor to natively integrate
    analog/digital IP directly into single CPE reducing Capex and Opex costs. In SD-WAN mode, the Catalyst
    8300 Series also prevent internal and external outages using SRST enabling Branch router to assume role
    of call control PBX for Telephony survivability. They also continue to support the long list of traditional IOS-
    XE voice use cases like Cisco Unified Border Element (CUBE) Session Border Controller (SBC), Cisco
    Unified Communications Manager Express (CUCME), Survivable Remote Site Telephony (SRST), ISDN and
    Voice over IP.
    Cloud-native agility with a programmable software architecture

    Cisco continues to offer a feature-rich traditional IOS-XE routing stack on the Cisco Catalyst 8300 Series
    Edge Platforms. IP Routing, IPSec, Quality of Service (QoS), firewall, Network Address Translation (NAT),
    Network-Based Application Recognition (NBAR), Flexible NetFlow (FNF), and many other features are part
    of Cisco IOS-XE, a fully programmable software architecture with API support and a wide variety of
    protocols and configurations. With an integrated software image and a single binary file, you can now
    choose between Cisco IOS XE SD-WAN and IOS XE. And easily move from one to the other when you
    choose to do so.
    LTE and 5G Wireless WAN

    The Cisco Catalyst 8300 Series Edge Platforms are built 5G networks. With the higher throughputs
    provided by CAT18 LTE and 5G, wireless WAN connections become feasible as primary transports for
    different use cases. These platforms support both integrated pluggable modules as well as external cellular
    gateways with LTE or 5G capability for improved throughputs that address all those use cases. Based on a
    specific branch’s direct line of sight and cellular coverage, this solution provides the flexibility of either
    using integrated PIM module or an external gateway. The integrated module can work in tandem with a
    cellular gateway for Active-Active redundancy.
    Interface flexibility

    Layer 2 LAN (Switched) and Layer 3 WAN (Routed) ports

    The Catalyst 8300 Series continues Cisco’s support for a flexible single-box solution with both switching
    and routing. The NIM based Layer 2 LAN modules provide 4 and 8-port switching with optional PoE
    capability for up to 1Gbps. The NIM based Layer 3 WAN modules provides extended Layer 3 port density
    for up to 10Gbps with full Layer 3 feature parity to the six embedded Layer 3 ports.

    LANWAN – Flexible Layer 2 Switching and Layer 3 Routing

    In addition to a wide range of NIM based Ethernet modules for a flexible and scalable combination of
    switched L2 ports and routed L3 ports, the Cisco Catalyst 8300 Series Edge Platforms also offer a new
    LANWAN module series which combines both capabilities. These new NIM based modules offer combined
    Layer 2 & Layer 3 connectivity with full Layer 3 feature parity to the embedded Layer 3 ports. LANWAN
    modules are offered as 8-port RJ45 modules ranging from 100Mbps up to 2.5Gbps mGig with 90 PoE
    capacity, plus a 4-port SFP+ NIM module with capacity for up to 10Gbps. In addition, LANWAN modules
    also support LAN MACsec for all ports operating in Layer 2 mode and WAN MACsec for all ports operating
    in Layer 3 mode. The introduction of LANWAN series modules offer unprecedented flexibility for the branch
    through higher density of Layer 3 ports, with options for higher PoE capacity and with HW-based MACsec
    for secure connections.



    © 2026 Cisco and/or its affiliates. All rights reserved.                                                   Page 10 of 24
-
```

## PDF page 11

```text
    High-density Switching

    The Cisco Catalyst 8300 Series Edge Platforms support high-density Unified Access Data Plane (UADP)-
    based 22-port and 50-port Layer 2 switch modules. This allows the edge platform to operate as a branch-
    in-a-box solution with 1G, Cisco Multigigabit Technology (mGig), and 10G ports for downstream switches
    and devices. The 22-port Layer-2 module is a single-wide module that can be used on both the 1RU and
    2RU platforms. The 50-port Layer-2 module is a double-wide module that can be used on the 2RU
    platforms.

    Cisco UCS-E compute

    The Cisco Catalyst 8300 Series Edge Platforms will support the Cisco UCS-E M3 modules as well as the
    new Cisco UCS-E M6 module for branch compute needs. We support both Cisco and third-party Virtual
    Network Functions (VNFs) on the Cisco Enterprise NFV Infrastructure Software (NFVIS) hypervisor running
    on the UCS-E compute blade server. Cisco UCS-E M3 modules have 6-, 8-, and 12-core options to
    choose from based on the number of VNFs that need to be run at the branch. The Cisco UCS-E M6 module
    is a new, fully up-to-date, compute module built for today’s more demanding compute applications. It
    comes with 3GHz clocked 10-core architecture and 2x 10Gbps connections both internally as well as
    externally. This will support very effective compute operations while also eliminating any bottlenecks for
    traffic flowing between the module and the host router.

    Voice modules

    The Cisco Catalyst 8300 Series Edge Platforms will continue to support a variety of voice modules for the
    different voice needs at the branch. Voice module examples include Foreign Exchange Station (FXS),
    Foreign Exchange Office (FXO), Digital Signal Processor (DSP), etc.

    NEBS (Network Equipment-Building System)

    The Cisco Catalyst 8300 Series Edge Platforms 2RU versions can be made NEBS compliant by choosing
    the optional PWR-CC1-650WDCR power supplies with reverse airflow. This will automatically include
    C8300-FAN-2R-R, the NEBS compliant fan assembly, which will make the C8300 system NEBS compliant.

    Sustainability

    The Cisco Catalyst 8300 Series Edge Platforms are designed ground-up with sustainability in mind. These
    platforms are standardized on highly efficient power supplies and common form factors for sharing tooling
    & accessories. We have eliminated use of plastic bezels as well as the need for wet paint, thereby reducing
    hazardous chemicals, and facilitating recyclability.

    All platforms are designed for maximizing efficient use of PCBs and material in motherboard designs and
    for employing common modules across platforms. Over 70% of the ISR4000 platform family’s modules are
    being reused by the Cisco Catalyst 8300 Series Edge Platforms.

    We standardize on integration of features to a single, very power effective, System on a Chip (SoC)
    architecture across the platform portfolio with dynamic power management plus added power and thermal
    management capabilities on modules. All platforms furthermore include a barometer to sense atmospheric
    pressure and estimate installation altitude. Fan speeds can thereby be reduced in installations at lower
    altitudes, yielding significant energy savings.




    © 2026 Cisco and/or its affiliates. All rights reserved.                                              Page 11 of 24
-
```

## PDF page 12

```text
    Throughput Efficiency (Gbps per Watt)

    The use of a single, effective, SoC architecture in the he Cisco Catalyst 8300 Series Edge family provides
    significantly higher performance per consumed wattage than its predecessors with up to 75% reduction in
    power per Gbps compared to equivalent ISR4k platform.


    Supported modules
    Table 7.        Modules supported on Cisco Catalyst 8300 Series Edge Platforms

     Product number                             Description

     Ethernet Layer 3 modules

     C-NIM-1X                                   1-port 10Gbps SFP/SFP+ NIM with WAN MACSec

     C-NIM-1M                                   1-port 2.5/1Gbps RJ-45 WAN, 90W Poe 802.3 af/at/bt NIM

     C-NIM-2T                                   2-port 100Mbps/1Gbps dual-mode RJ45/SFP, NIM with WAN MACSec

     LAN modules

     C-NIM-4X                                   4-port 1/10Gbps SFP/SFP+ switch NIM, LAN/WAN MACSec & Optional L3

     C-NIM-8T                                   8-port 100Mbps/1Gbps switch NIM, LAN/WAN MACSec & Optional L3

     C-NIM-8M*                                  8-port 100M/1/2.5Gbps switch NIM, UPoE, LAN/WAN MACSec & Optional L3

     NIM-ES2-4                                  Cisco 4-port Gigabit Ethernet switch NIM

     NIM-ES2-8                                  Cisco 8-port Gigabit Ethernet switch NIM

     NIM-ES2-8-P                                Cisco 8-port Gigabit Ethernet switch NIM with PoE support

     C-SM-16P4M2X                               Cisco 22-port Catalyst L2 switch module with UADP ASIC

     C-SM-40P8M2X                               Cisco 50-port Catalyst L2 switch module with UADP ASIC

     Compute modules

     UCS-E160S-M3/K9                            UCS-E, single-wide, Intel Broadwell 6-core CPU; up to 64 GB RAM, 1-2 HDD

     UCS-E180D-M3/K9                            UCS-E, double-wide, Intel Broadwell 8-core CPU; up to 128 GB RAM, 1-4 HDD

     UCS-E1120D-M3/K9                           UCS-E, double-wide, Intel Broadwell 12-core CPU; up to 128 GB RAM, 1-4 HDD

     UCS-E1100D-M6/K9                           UCS-E, double-wide, Intel Icelake 10-core CPU; up to 128 GB RAM, 1-4 SSD

     Voice modules

     NIM-2FXO                                   2-port FXO NIM

     NIM-4FXO                                   4-port FXO NIM

     NIM-2FXSP                                  2-port FXS NIM



    © 2026 Cisco and/or its affiliates. All rights reserved.                                                                Page 12 of 24
-
```

## PDF page 13

```text
     Product number                             Description

     NIM-4FXSP                                  4-port FXS NIM

     NIM-2FXSP/4FXOP                            2-port FXS and 4-port FXO NIM

     NIM-4E/M                                   4-port E/M NIM

     NIM-2BRI-NT/TE                             2-port BRI (NT and TE) NIM

     NIM-4BRI-NT/TE                             4-port BRI (NT and TE) NIM

     SM-X-8FXS/12FXO                            8-port FXS and 12-port FXO single-wide service module

     SM-X-16FXS/2FXO                            16-port FXS and 2-port FXO single-wide service module

     SM-X-24FXS/4FXO                            24-port FXS and 4-port FXO single-wide service module

     SM-X-72FXS                                 72-port FXS double-wide service module

     NIM-PVDM-32                                32-channel Voice DSP NIM Module

     NIM-PVDM-64                                64-channel Voice DSP NIM Module

     NIM-PVDM-128                               128-channel Voice DSP NIM Module

     NIM-PVDM-256                               256-channel Voice DSP NIM Module

     SM-X-PVDM-3000                             3080-channel high-density voice DSP module

     SM-X-PVDM-2000                             2048-channel high-density voice DSP module

     SM-X-PVDM-1000                             1024-channel high-density voice DSP module

     SM-X-PVDM-500                              768-channel high-density voice DSP module

     NIM-1MFT-T1/E1                             1-port multiflex trunk voice/clear-channel data T1/E1 module

     NIM-2MFT-T1/E1                             2-port multiflex trunk voice/clear-channel data T1/E1 module

     NIM-4MFT-T1/E1                             4-port multiflex trunk voice/clear-channel data T1/E1 module

     NIM-8MFT-T1/E1                             8-port multiflex trunk voice/clear-channel data T1/E1 module

     DSL/broadband

     NIM-VAB-A                                  Multi-mode VDSL2/ADSL/2/2+ NIM Annex A

     NIM-VA-B                                   Multi-mode VDSL2/ADSL/2/2+ NIM Annex B

     NIM-VAB-M                                  Multi-mode VDSL2/ADSL/2/2+ NIM Annex M

     NIM-4SHDSL-EA                              Multi-mode G.SHDSL NIM




    © 2026 Cisco and/or its affiliates. All rights reserved.                                                   Page 13 of 24
-
```

## PDF page 14

```text
     Product number                             Description

     ISDN BRI for Data

     NIM-2BRI-S/T                               2-port ISDN BRI WAN interface card for data

     NIM-4BRI-S/T                               4-port ISDN BRI WAN interface card for data

     Channelized T1/E1 and ISDN PRI

     NIM-1CE1T1-PRI                             1-port Multiflex trunk voice/channelized data T1/E1 module

     NIM-2CE1T1-PRI                             2-port Multiflex trunk voice/channelized data T1/E1 module

     NIM-8CE1T1-PRI                             8-port Multiflex trunk voice/channelized data T1/E1 module

     Serial WAN interface

     SM-X-1T3/E3                                1-port clear-channel T3/E3 service module

     NIM-1T                                     1-port serial high-speed WAN interface card

     NIM-2T                                     2-port serial high-speed WAN interface card

     NIM-4T                                     4-port serial high-speed WAN interface card

     Async WAN interface

     NIM-16A                                    16-port Asynchronous Module

     NIM-24A                                    24-port Asynchronous Module

     Wireless WAN (LTE)

     P-5GS6-R16SA-GL*                           5G Sub-6 GHz Pluggable – 5G SA Global

     P-5GS6-GL                                  5G Sub-6 GHz Pluggable – Global

     P-LTEAP18-GL                               CAT18 LTE Advanced Pro Pluggable - Global

     P-LTEA7-NA*                                CAT7 LTE Advanced Pluggable - North America

     P-LTEA7-EAL*                               CAT7 LTE Advanced Pluggable - EMEA, APAC, and LATAM

     P-LTEA7-JP*                                CAT7 LTE Advanced Pluggable - Japan

     P-LTEA-EA                                  CAT6 LTE Advanced Pluggable - North America and EMEA

     P-LTEA-LA                                  CAT6 LTE Advanced Pluggable - APAC, ANZ, and LATAM

     NIM-LTEA-EA                                CAT6 LTE Advanced - North America and EMEA

     NIM-LTEA-LA                                CAT6 LTE Advanced - APAC, ANZ, and LATAM




    © 2026 Cisco and/or its affiliates. All rights reserved.                                                 Page 14 of 24
-
```

## PDF page 15

```text
        Product number                          Description

        NIM Carrier Adapter Card

        C-SM-NIM-ADPT                           Single-wide 2x NIM carrier module in SM-X form factor

    *
        Supported with IOS XE release 17.12.2.



    Memory, storage, and accessory options
    Table 8.        Cisco Catalyst 8300 Series memory, storage, and accessory options

        Product number                         Description

        MEM-C8300-8GB                          Cisco C8300 Edge Platform - 8 GB Memory

        MEM-C8300-16GB                         Cisco C8300 Edge Platform - 16GB Memory

        MEM-C8300-32GB                         Cisco C8300 Edge Platform - 32GB Memory

        M2USB-16G                              Cisco C8000 Edge Platform - 16G M.2 USB SSD Storage

        M2USB-32G                              Cisco C8000 Edge Platform - 32G M.2 USB SSD Storage

        SSD-M2SED-600G                         Cisco C8000 Edge Platform - 600GB M.2 NVMe Self-Encrypted Drive (SED) Storage

        SSD-M2NVME-2T                          Cisco C8000 Edge Platform – 2TB M.2 NVMe Self-Encrypted Drive (SED) Storage

        C8300-RM-19-1R                         Cisco C8300 1RU Edge Platform - Rack Mount kit - 19"

        C8300-RM-23-1R                         Cisco C8300 1RU Edge Platform - Rack Mount kit - 23"

        C8300-RM-19-2R                         Cisco C8300 2RU Edge Platform - Rack Mount kit - 19"

        C8300-RM-23-2R                         Cisco C8300 2RU Edge Platform - Rack Mount kit - 23"

        C8300-RM-4PT-1R                        Cisco C8300 1RU Edge Platform – 4-post Rack Mount kit - 19"

        C8300-RM-4PT-2R                        Cisco C8300 2RU Edge Platform - 4-post Rack Mount kit - 19"

        C8300-FAN-1R                           Cisco C8300 1RU Edge Platform - Fan Tray Assembly

        C8300-FAN-2R                           Cisco C8300 2RU Edge Platform Fan Tray Assembly

        C8300-FAN-2R-R                         Cisco C8300 2RU Edge Platform Reverse Airflow Fan Tray Assembly for NEBS

        C-RFID-1R                              Cisco C8300 1RU Edge Platform - RFID

        C-RFID-2R                              Cisco C8300 2RU Edge Platform - RFID

        C8300-SM-BLANK                         Cisco C8300 SM Blank




    © 2026 Cisco and/or its affiliates. All rights reserved.                                                              Page 15 of 24
-
```

## PDF page 16

```text
     Product number                            Description

     C8300-NIM-BLANK                           Cisco C8300 NIM Blank

     C8300-PIM-BLANK                           Cisco C8300 PIM Blank


    The fan tray is shipped default with the Cisco Catalyst 8300 Edge Series Platforms.


    Optics and transceivers modules
    Find a full list of optics and transceivers here.


    Resiliency and high availability
    Platform redundancy is critical for branch operations, as any downtime has direct impact to a customer’s
    business. To address that priority, Cisco makes a dual power supply default on all the Catalyst 8300
    platforms to ensure that there is always a backup power supply module in case the primary power supply
    fails.


    Power supplies
    Important notice:

    To address the precarious component situation during the pandemics, Cisco shipped PWR-CC1-400WAC
    as a temporary substitute power supply in place of the current 250-watt power supply, PWR-CC1-
    250WAC, used on our Catalyst 8300 1RU platforms. PWR-CC1-400WAC is no longer shipped with our
    Catalyst 8300 1RU platforms but retains the same support as the PWR-CC1-250WAC power supply.

    For more information this, previous, temporary measure, please visit
    https://www.cisco.com/c/en/us/products/collateral/routers/catalyst-8300-series-edge-
    platforms/catalyst-8300-series-pb.html.

    Table 9.        Cisco Catalyst 8300 1RU edge platform power supply specifications

     Power supply feature               PWR-CC1-               PWR-CC1-         PWR-CC1-         PWR-CC1-          PWR-CC1-
                                        250WAC                 400WAC*          500WAC           400WDC            400WHV

     Power maximum                      250W                   250W             500W             400W              400W
     rating
                                                                                PoE (Yes)
                                                                                PoE Budget:
                                                                                250W

     Input-voltage range                100 to 240 VAC         100 to 240 VAC   100 to 240 VAC   DC: -40 to -72V   DC: 240 – 380V
     and frequency
                                        50 – 60 Hz             50 – 60 Hz       50 – 60 Hz

     Power supply                       80 Plus Silver         80 Plus Silver   80 Plus Silver   85 %              80 Plus Platinum
     efficiency

     Input current                      3A – 1.25A             6A – 3A          6 A – 2.5A       13 A – 7.25 A     1.75 A – 1.1 A

     Output ratings                     12V 21A                12V 33A          12V 21A          12 V 33.5 A       12V 54A
                                                                                54 V – 4.5 A


    © 2026 Cisco and/or its affiliates. All rights reserved.                                                              Page 16 of 24
-
```

## PDF page 17

```text
        Power supply feature            PWR-CC1-               PWR-CC1-             PWR-CC1-          PWR-CC1-            PWR-CC1-
                                        250WAC                 400WAC*              500WAC            400WDC              400WHV

        Output holdup time              20ms                   20ms                 20ms              2 ms                20ms

        Power supply input              IEC 320 C14            IEC 320 C14          IEC 320 C14       Terminal block      Saf-D-Grid
        receptacles

        Power cord rating               5A                     10A                  10A               15 A # 14 wire      5A

    *
    See Important Notice above


    Table 10.       Cisco Catalyst 8300 2RU edge platform power supply specifications

        Power supply feature           PWR-CC1-650WAC                PWR-CC1-1000WAC       PWR-CC1-650WDC          PWR-CC1-650WDCR
                                                                                                                   (NEBS)

        Power maximum                  650W                          1000W                 650W                    650W
        rating
                                                                     PoE (Yes)
                                                                     PoE Budget: 500W

        Input-voltage range            100 to 240 VAC                100 to 240 VAC        DC: -40 to -72V         DC: -40 to -72V
        and frequency
                                       50 – 60 Hz                    50 – 60 Hz

        Power supply                   80 Plus Gold                  80 Plus Gold          80 Plus Gold            80 Plus Gold
        efficiency

        Input current                  7.2 A – 3 A                   11.5 A – 4.63 A       18 A – 10 A             18 A – 10 A

        Output ratings                 12V 54A                       12V 83A               12 V54 A                12 V 54 A

        Output holdup time             20ms                          20ms                  4 ms                    4 ms

        Power supply input             IEC 320 C14                   IEC 320 C14           Terminal block          Terminal block
        receptacles

        Power cord rating              10A                           12A                   20 A # 14 wire          20 A # 14 wire


    Table 11.       Cisco Catalyst 8300 Edge platform Typical power consumption

        Power consumption,           C8300-2N2S-4T2X             C8300-1N1S-4T2X           C8300-2N2S-6T           C8300-1N1S-6T
        no modules, single
        PSU

        Typical power                275W                        245W                      89W                     82W
        (watts)


    RFID tags: Catalyst 8300 Series Edge Platforms have an embedded RFID tag that holds Serial Number and
    Product ID for easy asset and inventory management using commercial RFID readers. The RFID tag is
    external and can be easily removed if needed or can be unselected at the time of ordering.




    © 2026 Cisco and/or its affiliates. All rights reserved.                                                                      Page 17 of 24
-
```

## PDF page 18

```text
    Software requirements
    Cisco DNA Software for the Catalyst 8300 Series offers comprehensive solutions for enterprise branch
    networks.

    Table 12.       Catalyst 8300 Series minimum software requirements

     Platform Product ID (PID)                     Description                                 Minimum software requirement

     C8300-2N2S-4T2X                               Cisco Catalyst 8300 Series Edge Platforms   Cisco IOS XE Software Release 17.3.2
     C8300-1N1S-4T2X
     C8300-2N2S-6T
     C8300-1N1S-6T



    Software features
    Catalyst 8300 Series features for autonomous mode and for Catalyst SD-WAN.

    Table 13.       Catalyst 8300 Series Software features and protocols for autonomous mode

     Feature                                    Description

     Protocols                                  IPv4, IPv6, static routes, Routing Information Protocol Versions 1 and 2 (RIP and RIPv2),
                                                Open Shortest Path First (OSPF), Enhanced Interior Gateway Routing Protocol (EIGRP),
                                                Border Gateway Protocol (BGP), BGP Router Reflector, Intermediate System-to-
                                                Intermediate System (IS-IS), Multicast Internet Group Management Protocol Version 3
                                                (IGMPv3), Protocol Independent Multicast Sparse Mode (PIM SM), PIM Source-Specific
                                                Multicast (SSM), Resource Reservation Protocol (RSVP), Cisco Discovery Protocol,
                                                Encapsulated Remote Switched Port Analyzer (ERSPAN), Cisco IOS IP Service-Level
                                                Agreements (IPSLA), Call Home, Cisco IOS Embedded Event Manager (EEM), Internet Key
                                                Exchange (IKE), Access Control Lists (ACL), Ethernet Virtual Connections (EVC), Dynamic
                                                Host Configuration Protocol (DHCP), Frame Relay, DNS, Locator ID Separation Protocol
                                                (LISP), Hot Standby Router Protocol (HSRP), RADIUS, Authentication, Authorization, and
                                                Accounting (AAA), Application Visibility and Control (AVC), Distance Vector Multicast
                                                Routing Protocol (DVMRP), IPv4-to-IPv6 Multicast, Multiprotocol Label Switching (MPLS),
                                                Layer 2 and Layer 3 VPN, IPsec, Layer 2 Tunneling Protocol Version 3 (L2TPv3),
                                                Bidirectional Forwarding Detection (BFD), IEEE 802.1ag, and IEEE 802.3ah

     Encapsulations                             Generic Routing Encapsulation (GRE), Ethernet, 802.1q VLAN, Point-to-Point Protocol
                                                (PPP), Multilink Point-to-Point Protocol (MLPPP), Frame Relay, Multilink Frame Relay
                                                (MLFR) (FR.15 and FR.16), High-Level Data Link Control (HDLC), Serial (RS-232, RS-449,
                                                X.21, V.35, and EIA-530), and PPP over Ethernet (PPPoE)

     Traffic management                         Quality of Service (QoS), Class-Based Weighted Fair Queuing (CBWFQ), Weighted
                                                Random Early Detection (WRED), Hierarchical QoS, Policy-Based Routing (PBR), and
                                                Network-Based Application Recognition (NBAR)

     Cryptographic algorithms                   Encryption: DES, 3DES, AES-128 or AES-256 (in CBC and GCM modes)
                                                Authentication: RSA (748/1024/2048 bit), ECDSA (256/384 bit)
                                                Integrity: MD5, SHA, SHA-256, SHA-384, SHA-512




    © 2026 Cisco and/or its affiliates. All rights reserved.                                                                    Page 18 of 24
-
```

## PDF page 19

```text
     Feature                                    Description

     Unified Communication                      Call Admission Control (CAC), Cisco Unified Border Element (CUBE) Session Border
                                                Controller(SBC), Cisco Unified Communications Manager Express (CUCME), ISDN,
                                                RADIUS, RFC4040 based Clear Channel codec signaling with SIP, Resource Reservation
                                                Protocol (RSVP), RTP Control Protocol (RTCP), Session Initiation Protocol for VoIP(SIP),
                                                Survivable Remote Site Telephony (SRST), Secure Real-time Transport Protocol(SRTP),
                                                and Voice modules


    Table 14.       Catalyst 8300 Series Software features and protocols for controller (Catalyst SD-WAN) mode

     Feature                                    Description

     Core Features                              IPv4, IPv6, static routes, Open Shortest Path First (OSPF), Enhanced Interior Gateway
                                                Routing Protocol (EIGRP), BoGateway Protocol (BGP), Overlay Management Protocol
                                                (OMP), Application Aware Routing (AAR), Traffic EngineerinService Insertion, zero-trust,
                                                whitelisting, tamper-proof module, DTLS/TLS, IPsec, classification, prioritization, low
                                                latequeuing, remarking, shaping, scheduling, policing, mirroring, Multicast IPv4 Support,
                                                Service advertisement and inserpolicy, SNMP, NTP, DNS client, Dynamic Host
                                                Configuration Protocol (DHCP), DHCP client, DHCP server, DHCP relaarchival, syslog, SSH,
                                                SCP, Cflowd v10 IPFIX export, IPv6 for transport-side, VRRP, MPLS, NAT (DIA, Service-
                                                side, soverload/PAT, NAT64, etc), NAT pools, split DNS, Access Control Lists (ACL),
                                                Bidirectional Forwarding Detection (BFNetconf over SSH, CLI, NTP server support, BFD
                                                with service-side BGP, BGP community propagation to OMP, 6 SLA for AAR,
                                                Trustsec/SDA (Inline SGT propagation), custom app with SD-AVC, multicast AAR, dynamic
                                                on-demand tunnSM, OSPFv3, route policies, Multi-VRF support

     Encapsulations                             Generic Routing Encapsulation (GRE), Ethernet, 802.1q VLAN

     Application Experience                     Quality of service (QoS), Forward Error Correction (FEC), COS Marking, Weighted Random
                                                Early Detection (WRED)Hierarchical QoS, Policy-Based Routing (PBR), Network-Based
                                                Application Recognition (NBAR), Software Defined A Visibility and Control (SD-AVC), per
                                                tunnel QoS, Cloud onRamp for SaaS, Enhanced Office 365 traffic steering, DirecAccess,
                                                Flexible Netflow (FnF)

     Cryptographic Algorithms                   Encryption: AES-256 (in CBC and GCM modes), Internet Key Exchange (IKE), Cisco PKI
                                                Authentication: AAA, RSA (2048 bit), ESP-256-CBC, HMAC-SHA1, ECDSA (256/384 bit)
                                                Integrity: SHA-1, SHA-2

     Security                                   Built-in end-to-end segmentation (VPNs), ZBFW, PKI, Cisco DNA Layer Security, Snort
                                                IPS/IDS, URL Filtering, Advanced Protection (AMP), ThreatGrid (TG), ALG for ZBFW

     Unified Communication                      Cisco Unified Border Element (CUBE), Survivable Remote Site Telephony (SRST),
                                                Cisco Unified Communications Manager Express (CUCME) and Voice Modules




    © 2026 Cisco and/or its affiliates. All rights reserved.                                                                    Page 19 of 24
-
```

## PDF page 20

```text
    Licensing
    The Catalyst 8300 Series Edge Platforms are offered only with a Cisco DNA Software subscription,
    Enterprise Agreement, and Managed Service Licensing Agreement (MSLA). For more details, refer to this
    licensing guide.

    Cisco DNA Subscriptions offered with the Catalyst 8300 Series

         ●    Catalyst Routing Essentials
         ●    Cisco DNA Essentials
         ●    Cisco DNA Advantage

    For a more detailed overview on Cisco Licensing, visit the Licensing Hub.


    Cisco Smart Licensing
    Cisco Smart Licensing is a flexible licensing model that provides you with an easier, faster, and more
    consistent way to purchase and manage software across the Cisco portfolio and across your organization.
    And it’s secure – you control what users can access. With Smart Licensing you get:

         ●    Easy Activation: Smart Licensing establishes a pool of software licenses that can be used across the
              entire organization—no more PAKs (Product Activation Keys).
         ●    Unified Management: Cisco License Central (CLC) provides a complete view into all of your Cisco
              products and services in an easy-to-use portal, so you always know what you have and what you are
              using.
         ●    License Flexibility: Your software is not node-locked to your hardware, so you can easily use and
              transfer licenses as needed.

    To use Smart Licensing, you must first set up a Smart Account on Cisco License Central.

    For a more detailed overview on Cisco Licensing, visit the Licensing Hub.


    Specifications
    Table 15.       Mechanical specifications

     Description                                       Specification

     Part number                                       C8300-2N2S-4T2X                   C8300-1N1S-4T2X
                                                       C8300-2N2S-6T                     C8300-1N1S-6T

     Dimensions (H x W x D)                            3.5 in. x 17.25 in. x 18.52 in.   1.73 in. x 17.50 in. x 16.25 in.

     Rack Units (RU)                                   2RU                               1RU

     Chassis weight with 2X AC                         40 lbs                            20 lbs
     power supplies and fan tray




    © 2026 Cisco and/or its affiliates. All rights reserved.                                                                Page 20 of 24
-
```

## PDF page 21

```text
     Description                                       Specification

     Acoustics:                                        59 dBa/73 dBa (Non-NEBS)                 49 dBa/71 dBa
     Sound pressure                                    63 dBa/75 dBa (NEBS)
     (Typical/maximum)

     Acoustics:                                        74 dBa/87 dBa (Non-NEBS)                 60 dBa/82 dBa
     Sound power                                       77 dBa/89 dBa (NEBS)
     (Typical/maximum)

     Input voltage                                     AC: 85 to 264 VAC
                                                       DC: -40 to 72V; 48V nominal

     Operating temperature                             32 to 104°F
                                                       (0 to 40°C)

     Storage temperature                               -40 to 150°F
                                                       (-40 to 70°C)

     Relative humidity operating and                   Ambient (noncondensing) operating: 5 to 85%
     nonoperating noncondensing
                                                       Ambient (noncondensing) nonoperating and storage: 5 to 95%

     Altitude                                          0 to 10,000 feet
                                                       (0 to 3050 meters)

     Mean Time Between Failures                        710,300 hours                            536,060 hours
     (MTBF)


    Table 16.       Safety and compliance

     Description                                      Specification

     Safety certifications                            UL 60950-1
                                                      CAN/CSA-C22.2 No. 60950-1
                                                      EN 60950-1
                                                      IEC 60950-1
                                                      AS/NZS 60950-1
                                                      IEC/EN 60825 Laser Safety
                                                      FDA: Code of Federal Regulations Laser Safety

     EMC (Emissions)                                  47 CFR Part 15 Class A
                                                      ICES 003 Class A
                                                      AS/NZS CISPR 32 Class A
                                                      CISPR 32 Class A
                                                      EN55032 Class A
                                                      VCCI-CISPR 32 Class A



    © 2026 Cisco and/or its affiliates. All rights reserved.                                                        Page 21 of 24
-
```

## PDF page 22

```text
     Description                                      Specification

                                                      CNS-13438 Class A
                                                      KN32 Class A
                                                      IEC/EN 61000-3-2: Power Line Harmonics
                                                      IEC/EN 61000-3-3: Voltage Fluctuations and Flicker

     EMC (Immunity)                                   IEC/EN-61000-4-2: Electrostatic Discharge Immunity
                                                      IEC/EN-61000-4-3: Radiated Immunity
                                                      IEC/EN-61000-4-4: Electrical Fast Transient Immunity
                                                      IEC/EN-61000-4-5: Surge AC, DC, and Signal Ports
                                                      IEC/EN-61000-4-6: Immunity to Conducted Disturbances
                                                      IEC/EN-61000-4-8: Power Frequency Magnetic Field Immunity
                                                      IEC/EN-61000-4-11: Voltage DIPS, Short Interruptions, and Voltage Variations
                                                      KN35

     EMC (ETSI/EN)                                    EN300 386: Telecommunications Network Equipment (EMC)
                                                      EN55032: Multimedia Equipment (Emissions)
                                                      EN55024: Information Technology Equipment (Immunity)
                                                      EN55035: Multimedia Equipment (Immunity)
                                                      EN61000-6-1: Generic Immunity Standard



    Ordering information
    To place an order, visit the Cisco Ordering Home Page. To download software, visit the Cisco Software
    Center.


    Cisco Services
    Get faster results with expert guidance

    Cisco Professional Services provide industry-leading expertise to help you plan, design, implement, and
    optimize your network. So you can drive better outcomes from the start and get more value – faster.

    Cisco Support, powered by Cisco IQ, helps you prevent issues before they happen. You get automated
    recommendations, early risk detection, and an always-current view of every asset, software version, and
    configuration across your environment. But we know a list isn’t enough. Cisco IQ also instantly analyzes this
    data and summarizes the most critical observations. So your teams can focus on what matters most.

    Explore Cisco Services




    © 2026 Cisco and/or its affiliates. All rights reserved.                                                                   Page 22 of 24
-
```

## PDF page 23

```text
    Cisco Capital
    Flexible payment solutions to help you achieve your objectives

    Cisco Capital makes it easier to get the right technology to achieve your objectives, enable business
    transformation and help you stay competitive. We can help you reduce the total cost of ownership,
    conserve capital, and accelerate growth. In more than 100 countries, our flexible payment solutions can
    help you acquire hardware, software, services and complementary third-party equipment in easy,
    predictable payments. Learn more.


    For more information
    For more information about the Cisco Catalyst 8300 Series Edge Platforms, visit
    https://www.cisco.com/go/C8300 or contact your local Cisco account representative.




    © 2026 Cisco and/or its affiliates. All rights reserved.                                             Page 23 of 24
-
```

## PDF page 24

```text
    Document history
     New or revised topic                                         Described In                 Date

     General Updates to document, including SD-Routing, licensing Product Overview, Platform   August 2024
     and performance characteristics.                             Performance, Overall
                                                                  Platform Benefits and
                                                                  Licensing

     Describing why a new 400W PSU is added toC8300               Power supplies               September 21, 2022

     Added column with technical specs for new400W PSU            Power supplies, Table 6      September 21, 2022




    Printed in USA                                                                                    C78-744088-09   10/26


    © 2026 Cisco and/or its affiliates. All rights reserved.                                                    Page 24 of 24
-
```
