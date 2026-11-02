# c8300-nim-1x-4x-2t-tmg-optics-2026-10-30.pdf — extracted text

- Source PDF: [c8300-nim-1x-4x-2t-tmg-optics-2026-10-30.pdf](c8300-nim-1x-4x-2t-tmg-optics-2026-10-30.pdf)
- PDF title metadata: c8300-nim-1x-4x-2t-tmg-optics-2026-10-30.pdf
- Publisher: Cisco (as registered in the research source entries).
- Source SHA-256: `099a7512b2e2b00a447649a6bc3bb01df90d2d57514a75b6b946f03065ce0f20`
- Converted: 2026-10-31 (UTC).
- Extraction tool: `pdftotext version 25.03.0`.
- Command: `pdftotext -layout -enc UTF-8 reference/c8300-nim-1x-4x-2t-tmg-optics-2026-10-30.pdf -`.
- PDF pages: 3; page headings below use PDF page numbers.
- Language: English; no OCR or translation performed.
- Source access date and document revision: see the original source-register entries below; conversion does not update them.
- Source register: [C8300-4T2X-TMG-2](../research-cisco-c8300-1n1s-4t2x-r1.1.0.md#c8300-4t2x-tmg-2).
- Source register: [C8300-6T-TMG-1](../research-cisco-c8300-1n1s-6t-r1.1.0.md#c8300-6t-tmg-1).
- Source register: [C8375-TMG-4](../research-cisco-c8375-e-g2-r1.1.0.md#c8375-tmg-4).

> This is layout-preserving plain-text extraction wrapped in Markdown,
> not a semantic reconstruction of tables. Fixed-width text blocks preserve
> column spacing, but reading order, merged cells, and glyphs can still be
> imperfect. Images, diagrams, and image-based tick marks are not transcribed.
> Verify consequential table values against the linked original PDF.

## PDF page 1

```text
Cisco Optics-to-Device Compatibility Matrix Results

Network Device Product Family




C8300
Network        Transciever        Transceiver Data      Form Reach Cable Type             Media Connector Transceiver   Case     DOM       Min Software DOM
Device Product Product ID         Business    Rate      Factor                                  Type      Type          Temp     Capable   Support      Support
ID                                Unit
C-NIM-1X         SFP-10G-SR       TMG          10       SFP+      400m    Duplex Fiber    MMF   LC (UPC)   Optic        0 to     Y         IOS XE 17.3.2   IOS XE
                                               Gbps                                                                     70C                                17.3.2

Transceiver Notes for above line :
• FDDI: 26m; OM1: 33m; OM2: 82m; OM3: 300m; OM4/OM5: 400m
C-NIM-1X         SFP-10G-SR-S     TMG          10       SFP+      400m    Duplex Fiber    MMF   LC (UPC)   Optic        0 to     Y         IOS XE 17.6.1   IOS XE
                                               Gbps                                                                     70C                                17.6.1

Transceiver Notes for above line :
• FDDI: 26m; OM1: 33m; OM2: 82m; OM3: 300m; OM4/OM5: 400m
C-NIM-1X         SFP-10G-LRM      TMG          10       SFP+      220m    Duplex Fiber    MMF   LC (UPC)   Optic        0 to     Y         IOS XE 17.3.2   IOS XE
                                               Gbps                                                                     70C                                17.3.2

Transceiver Notes for above line :
• SFP-10G-LRM can be used on SMF with a maximum reach of 300m
C-NIM-1X         SFP-10G-LR       TMG          10       SFP+      10km    Duplex Fiber    SMF   LC (UPC)   Optic        0 to     Y         IOS XE 17.3.2   IOS XE
                                               Gbps                                                                     70C                                17.3.2
C-NIM-1X         SFP-10G-LR-S     TMG          10       SFP+      10km    Duplex Fiber    SMF   LC (UPC)   Optic        0 to     Y         IOS XE 17.6.1   IOS XE
                                               Gbps                                                                     70C                                17.6.1
C-NIM-1X         SFP-10G-ER       TMG          10       SFP+      40km    Duplex Fiber    SMF   LC (UPC)   Optic        0 to     Y         IOS XE 17.3.2   IOS XE
                                               Gbps                                                                     70C                                17.3.2
C-NIM-1X         SFP-10G-BXD-I    TMG          10       SFP+      10km    Single-strand   SMF   LC (UPC)   Optic        -40 to   Y         IOS XE 17.3.2   IOS XE
                                               Gbps                       Fiber                                         85C                                17.3.2
C-NIM-1X         SFP-10G-BXU-I    TMG          10       SFP+      10km    Single-strand   SMF   LC (UPC)   Optic        -40 to   Y         IOS XE 17.3.2   IOS XE
                                               Gbps                       Fiber                                         85C                                17.3.2
C-NIM-1X         SFP-10G-         TMG          10       SFP+      40km    Single-strand   SMF   LC (UPC)   Optic        -40 to   Y         IOS XE 17.3.2   IOS XE
                 BX40D-I                       Gbps                       Fiber                                         85C                                17.3.2
C-NIM-1X         SFP-10G-         TMG          10       SFP+      40km    Single-strand   SMF   LC (UPC)   Optic        -40 to   Y         IOS XE 17.3.2   IOS XE
                 BX40U-I                       Gbps                       Fiber                                         85C                                17.3.2
C-NIM-1X         SFP-H10GB-       TMG          10       SFP+      7m      Preterminated   DAC   N/A        Cable        0 to               IOS XE 17.3.2   —
                 ACU7M                         Gbps                       cable                                         70C
C-NIM-1X         SFP-H10GB-       TMG          10       SFP+      10m     Preterminated   DAC   N/A        Cable        0 to               IOS XE 17.3.2   —
                 ACU10M                        Gbps                       cable                                         70C
C-NIM-1X         DWDM-SFP10G- TMG              10       SFP+      80km    Duplex Fiber    SMF   LC (UPC)   Optic        0 to     Y         IOS XE 17.3.2   IOS XE
                 XX.XX                         Gbps                                                                     70C                                17.3.2
C-NIM-1X         GLC-BX-D         TMG          1 Gbps   SFP       10km    Single-strand   SMF   LC (UPC)   Optic        0 to     Y         IOS XE 17.3.2   IOS XE
                                                                          Fiber                                         70C                                17.3.2
C-NIM-1X         GLC-BX-U         TMG          1 Gbps   SFP       10km    Single-strand   SMF   LC (UPC)   Optic        0 to     Y         IOS XE 17.3.2   IOS XE
                                                                          Fiber                                         70C                                17.3.2
C-NIM-1X         GLC-BX40-D-I     TMG          1 Gbps   SFP       40km    Single-strand   SMF   LC (UPC)   Optic        -40 to   Y         IOS XE 17.3.2   IOS XE
                                                                          Fiber                                         85C                                17.3.2
C-NIM-1X         GLC-BX40-U-I     TMG          1 Gbps   SFP       40km    Single-strand   SMF   LC (UPC)   Optic        -40 to   Y         IOS XE 17.3.2   IOS XE
                                                                          Fiber                                         85C                                17.3.2
C-NIM-1X         GLC-BX80-D-I     TMG          1 Gbps   SFP       80km    Single-strand   SMF   LC (UPC)   Optic        -40 to   Y         IOS XE 17.3.2   IOS XE
                                                                          Fiber                                         85C                                17.3.2
C-NIM-1X         GLC-BX80-U-I     TMG          1 Gbps   SFP       80km    Single-strand   SMF   LC (UPC)   Optic        -40 to   Y         IOS XE 17.3.2   IOS XE
                                                                          Fiber                                         85C                                17.3.2
C-NIM-1X         GLC-BX40-DA-I    TMG          1 Gbps   SFP       40km    Single-strand   SMF   LC (UPC)   Optic        -40 to   Y         IOS XE 17.3.2   IOS XE
                                                                          Fiber                                         85C                                17.3.2
C-NIM-1X         GLC-EX-SMD       TMG          1 Gbps   SFP       40km    Duplex Fiber    SMF   LC (UPC)   Optic        -5 to    Y         IOS XE 17.3.2   IOS XE
                                                                                                                        85C                                17.3.2
C-NIM-1X         GLC-LX-SM-       TMG          1 Gbps   SFP       10km    Duplex Fiber    SMF   LC (UPC)   Optic        -40 to   Y         IOS XE 17.3.2   IOS XE
                 RGD                                                                                                    85C                                17.3.2

Transceiver Notes for above line :
• GLC-LX-SM-RGD can be used on MMF with a maximum reach of 550m
C-NIM-1X         GLC-SX-MMD       TMG          1 Gbps   SFP       1000m   Duplex Fiber    MMF   LC (UPC)   Optic        -5 to    Y         IOS XE 17.3.2   IOS XE
                                                                                                                        85C                                17.3.2

Transceiver Notes for above line :
• FDDI: 220m; OM1: 275m; OM2: 550m; OM3, OM4/OM5: 1000m
C-NIM-1X         GLC-LH-SMD       TMG          1 Gbps   SFP       10km    Duplex Fiber    SMF   LC (UPC)   Optic        -5 to    Y         IOS XE 17.3.2   IOS XE
                                                                                                                        85C                                17.3.2

Transceiver Notes for above line :
• GLC-LH-SMD can be used on MMF with a maximum reach of 550m
• LC mode-conditioning cable required for MMF applications
C-NIM-1X         GLC-ZX-SMD       TMG          1 Gbps   SFP       70km    Duplex Fiber    SMF   LC (UPC)   Optic        -5 to    Y         IOS XE 17.3.2   IOS XE
                                                                                                                        85C                                17.3.2
C-NIM-1X         DWDM-SFP-        TMG          1 Gbps   SFP       80km    Duplex Fiber    SMF   LC (UPC)   Optic        0 to     Y         IOS XE 17.3.2   IOS XE
                 XXXX                                                                                                   70C                                17.3.2
```

## PDF page 2

```text
Network        Transciever           Transceiver Data         Form Reach Cable Type                 Media Connector Transceiver   Case     DOM       Min Software DOM
Device Product Product ID            Business    Rate         Factor                                      Type      Type          Temp     Capable   Support      Support
ID                                   Unit
C-NIM-1X          SFP-10G-T-X        TMG            100M/1 SFP+        30m       Cat6A/7            Copper   RJ-45      Copper    -5 to              IOS XE 17.6.1   —
                                                    000M/1                                                                        85C
                                                    0G bps

Network Device Notes for above line :
• Supports 10GBASE-T mode only
Transceiver Notes for above line :
• Up to 30 meters with Cat6A/Cat7 or better (10G), up to 100 meters with Cat5e/Cat6A/Cat7 or better (100M/1000M)
C-NIM-2T          GLC-FE-100FX       TMG            100       SFP      2km       Duplex Fiber       MMF      LC (UPC)   Optic     -5 to              IOS XE 17.6.1   —
                                                    Mbps                                                                          85C
C-NIM-2T          GLC-FE-100LX       TMG            100       SFP      10km      Duplex Fiber       SMF      LC (UPC)   Optic     -5 to              IOS XE 17.6.1   —
                                                    Mbps                                                                          85C
C-NIM-2T          GLC-FE-100EX       TMG            100       SFP      40km      Duplex Fiber       SMF      LC (UPC)   Optic     -5 to              IOS XE 17.6.1   —
                                                    Mbps                                                                          85C
C-NIM-2T          GLC-BX-D           TMG            1 Gbps    SFP      10km      Single-strand      SMF      LC (UPC)   Optic     0 to     Y         IOS XE 17.6.1   IOS XE
                                                                                 Fiber                                            70C                                17.6.1
C-NIM-2T          GLC-BX-U           TMG            1 Gbps    SFP      10km      Single-strand      SMF      LC (UPC)   Optic     0 to     Y         IOS XE 17.6.1   IOS XE
                                                                                 Fiber                                            70C                                17.6.1
C-NIM-2T          GLC-BX40-D-I       TMG            1 Gbps    SFP      40km      Single-strand      SMF      LC (UPC)   Optic     -40 to   Y         IOS XE 17.6.1   IOS XE
                                                                                 Fiber                                            85C                                17.6.1
C-NIM-2T          GLC-BX40-U-I       TMG            1 Gbps    SFP      40km      Single-strand      SMF      LC (UPC)   Optic     -40 to   Y         IOS XE 17.6.1   IOS XE
                                                                                 Fiber                                            85C                                17.6.1
C-NIM-2T          GLC-BX80-D-I       TMG            1 Gbps    SFP      80km      Single-strand      SMF      LC (UPC)   Optic     -40 to   Y         IOS XE 17.6.1   IOS XE
                                                                                 Fiber                                            85C                                17.6.1
C-NIM-2T          GLC-BX80-U-I       TMG            1 Gbps    SFP      80km      Single-strand      SMF      LC (UPC)   Optic     -40 to   Y         IOS XE 17.6.1   IOS XE
                                                                                 Fiber                                            85C                                17.6.1
C-NIM-2T          GLC-BX40-DA-I      TMG            1 Gbps    SFP      40km      Single-strand      SMF      LC (UPC)   Optic     -40 to   Y         IOS XE 17.6.1   IOS XE
                                                                                 Fiber                                            85C                                17.6.1
C-NIM-2T          GLC-EX-SMD         TMG            1 Gbps    SFP      40km      Duplex Fiber       SMF      LC (UPC)   Optic     -5 to    Y         IOS XE 17.6.1   IOS XE
                                                                                                                                  85C                                17.6.1
C-NIM-2T          GLC-LX-SM-         TMG            1 Gbps    SFP      10km      Duplex Fiber       SMF      LC (UPC)   Optic     -40 to   Y         IOS XE 17.6.1   IOS XE
                  RGD                                                                                                             85C                                17.6.1

Transceiver Notes for above line :
• GLC-LX-SM-RGD can be used on MMF with a maximum reach of 550m
C-NIM-2T          GLC-SX-MMD         TMG            1 Gbps    SFP      1000m     Duplex Fiber       MMF      LC (UPC)   Optic     -5 to    Y         IOS XE 17.6.1   IOS XE
                                                                                                                                  85C                                17.6.1

Transceiver Notes for above line :
• FDDI: 220m; OM1: 275m; OM2: 550m; OM3, OM4/OM5: 1000m
C-NIM-2T          GLC-LH-SMD         TMG            1 Gbps    SFP      10km      Duplex Fiber       SMF      LC (UPC)   Optic     -5 to    Y         IOS XE 17.6.1   IOS XE
                                                                                                                                  85C                                17.6.1

Transceiver Notes for above line :
• GLC-LH-SMD can be used on MMF with a maximum reach of 550m
• LC mode-conditioning cable required for MMF applications
C-NIM-2T          GLC-ZX-SMD         TMG            1 Gbps    SFP      70km      Duplex Fiber       SMF      LC (UPC)   Optic     -5 to    Y         IOS XE 17.6.1   IOS XE
                                                                                                                                  85C                                17.6.1
C-NIM-4X          GLC-GE-100FX       TMG            100       SFP      2km       Duplex Fiber       MMF      LC (UPC)   Optic     0 to               IOS XE 17.12.1 —
                                                    Mbps                                                                          70C
C-NIM-4X          SFP-10G-SR         TMG            10        SFP+     400m      Duplex Fiber       MMF      LC (UPC)   Optic     0 to     Y         IOS XE 17.11.1 IOS XE
                                                    Gbps                                                                          70C                               17.11.1

Transceiver Notes for above line :
• FDDI: 26m; OM1: 33m; OM2: 82m; OM3: 300m; OM4/OM5: 400m
C-NIM-4X          SFP-10G-SR-S       TMG            10        SFP+     400m      Duplex Fiber       MMF      LC (UPC)   Optic     0 to     Y         IOS XE 17.11.1 IOS XE
                                                    Gbps                                                                          70C                               17.11.1

Transceiver Notes for above line :
• FDDI: 26m; OM1: 33m; OM2: 82m; OM3: 300m; OM4/OM5: 400m
C-NIM-4X          SFP-10G-LR         TMG            10        SFP+     10km      Duplex Fiber       SMF      LC (UPC)   Optic     0 to     Y         IOS XE 17.11.1 IOS XE
                                                    Gbps                                                                          70C                               17.11.1
C-NIM-4X          SFP-10G-LR-S       TMG            10        SFP+     10km      Duplex Fiber       SMF      LC (UPC)   Optic     0 to     Y         IOS XE 17.11.1 IOS XE
                                                    Gbps                                                                          70C                               17.11.1
C-NIM-4X          SFP-10G-ER         TMG            10        SFP+     40km      Duplex Fiber       SMF      LC (UPC)   Optic     0 to     Y         IOS XE 17.11.1 IOS XE
                                                    Gbps                                                                          70C                               17.11.1
C-NIM-4X          SFP-10G-ER-S       TMG            10        SFP+     40km      Duplex Fiber       SMF      LC (UPC)   Optic     0 to     Y         IOS XE 17.18.2 IOS XE
                                                    Gbps                                                                          70C                               17.18.2
C-NIM-4X          SFP-10G-BXD-I      TMG            10        SFP+     10km      Single-strand      SMF      LC (UPC)   Optic     -40 to   Y         IOS XE 17.11.1 IOS XE
                                                    Gbps                         Fiber                                            85C                               17.11.1
C-NIM-4X          SFP-10G-BXU-I      TMG            10        SFP+     10km      Single-strand      SMF      LC (UPC)   Optic     -40 to   Y         IOS XE 17.11.1 IOS XE
                                                    Gbps                         Fiber                                            85C                               17.11.1
C-NIM-4X          SFP-10G-           TMG            10        SFP+     40km      Single-strand      SMF      LC (UPC)   Optic     -40 to   Y         IOS XE 17.11.1 IOS XE
                  BX40D-I                           Gbps                         Fiber                                            85C                               17.11.1
C-NIM-4X          SFP-10G-           TMG            10        SFP+     40km      Single-strand      SMF      LC (UPC)   Optic     -40 to   Y         IOS XE 17.11.1 IOS XE
                  BX40U-I                           Gbps                         Fiber                                            85C                               17.11.1
C-NIM-4X          SFP-H10GB-         TMG            10        SFP+     7m        Preterminated      DAC      N/A        Cable     0 to               IOS XE 17.11.1 —
                  ACU7M                             Gbps                         cable                                            70C
C-NIM-4X          SFP-H10GB-         TMG            10        SFP+     10m       Preterminated      DAC      N/A        Cable     0 to               IOS XE 17.11.1 —
                  ACU10M                            Gbps                         cable                                            70C
C-NIM-4X          GLC-TE             TMG            10/100/ SFP        100m      Cat5e/6A           Copper   RJ-45      Copper    -5 to              IOS XE 17.18.1 —
                                                    1000                                                                          85C
                                                    Mbps

Network Device Notes for above line :
• Supports 1000BASE-T and 100MBASE-T data rates only.
C-NIM-4X          GLC-BX-D           TMG            1 Gbps    SFP      10km      Single-strand      SMF      LC (UPC)   Optic     0 to     Y         IOS XE 17.11.1 IOS XE
                                                                                 Fiber                                            70C                               17.11.1
C-NIM-4X          GLC-BX-U           TMG            1 Gbps    SFP      10km      Single-strand      SMF      LC (UPC)   Optic     0 to     Y         IOS XE 17.11.1 IOS XE
                                                                                 Fiber                                            70C                               17.11.1
C-NIM-4X          GLC-BX40-D-I       TMG            1 Gbps    SFP      40km      Single-strand      SMF      LC (UPC)   Optic     -40 to   Y         IOS XE 17.11.1 IOS XE
                                                                                 Fiber                                            85C                               17.11.1
```

## PDF page 3

```text
Network        Transciever              Transceiver Data          Form Reach Cable Type                    Media Connector Transceiver                Case      DOM          Min Software DOM
Device Product Product ID               Business    Rate          Factor                                         Type      Type                       Temp      Capable      Support      Support
ID                                      Unit
C-NIM-4X            GLC-BX40-U-I        TMG             1 Gbps    SFP        40km      Single-strand       SMF       LC (UPC)       Optic             -40 to    Y            IOS XE 17.11.1 IOS XE
                                                                                       Fiber                                                          85C                                   17.11.1
C-NIM-4X            GLC-BX80-D-I        TMG             1 Gbps    SFP        80km      Single-strand       SMF       LC (UPC)       Optic             -40 to    Y            IOS XE 17.11.1 IOS XE
                                                                                       Fiber                                                          85C                                   17.11.1
C-NIM-4X            GLC-BX80-U-I        TMG             1 Gbps    SFP        80km      Single-strand       SMF       LC (UPC)       Optic             -40 to    Y            IOS XE 17.11.1 IOS XE
                                                                                       Fiber                                                          85C                                   17.11.1
C-NIM-4X            GLC-BX40-DA-I       TMG             1 Gbps    SFP        40km      Single-strand       SMF       LC (UPC)       Optic             -40 to    Y            IOS XE 17.11.1 IOS XE
                                                                                       Fiber                                                          85C                                   17.11.1
C-NIM-4X            GLC-EX-SMD          TMG             1 Gbps    SFP        40km      Duplex Fiber        SMF       LC (UPC)       Optic             -5 to     Y            IOS XE 17.11.1 IOS XE
                                                                                                                                                      85C                                   17.11.1
C-NIM-4X            GLC-LX-SM-          TMG             1 Gbps    SFP        10km      Duplex Fiber        SMF       LC (UPC)       Optic             -40 to    Y            IOS XE 17.11.1 IOS XE
                    RGD                                                                                                                               85C                                   17.11.1

Transceiver Notes for above line :
• GLC-LX-SM-RGD can be used on MMF with a maximum reach of 550m
C-NIM-4X            GLC-SX-MMD          TMG             1 Gbps    SFP        1000m     Duplex Fiber        MMF       LC (UPC)       Optic             -5 to     Y            IOS XE 17.11.1 IOS XE
                                                                                                                                                      85C                                   17.11.1

Transceiver Notes for above line :
• FDDI: 220m; OM1: 275m; OM2: 550m; OM3, OM4/OM5: 1000m
C-NIM-4X            GLC-LH-SMD          TMG             1 Gbps    SFP        10km      Duplex Fiber        SMF       LC (UPC)       Optic             -5 to     Y            IOS XE 17.11.1 IOS XE
                                                                                                                                                      85C                                   17.11.1

Transceiver Notes for above line :
• GLC-LH-SMD can be used on MMF with a maximum reach of 550m
• LC mode-conditioning cable required for MMF applications
C-NIM-4X            GLC-ZX-SMD          TMG             1 Gbps    SFP        70km      Duplex Fiber        SMF       LC (UPC)       Optic             -5 to     Y            IOS XE 17.11.1 IOS XE
                                                                                                                                                      85C                                   17.11.1
C-NIM-4X            DWDM-SFP-           TMG             1 Gbps    SFP        80km      Duplex Fiber        SMF       LC (UPC)       Optic             0 to      Y            IOS XE 17.11.1 IOS XE
                    XXXX                                                                                                                              70C                                   17.11.1
C-NIM-4X            GLC-GE-DR-LX        TMG             1 Gbps    SFP        10km      Duplex Fiber        SMF       LC (UPC)       Optic             0 to      Y            IOS XE 17.18.2 IOS XE
                                                                                                                                                      70C                                   17.18.2
C-NIM-4X            DWDM-SFP10G- TMG                    10        SFP+       70km      Duplex Fiber        SMF       LC (UPC)       Optic             0 to      Y            IOS XE 17.11.1 IOS XE
                    C-S                                 Gbps                                                                                          70C                                   17.11.1
C-NIM-4X            SFP-10G-T-X         TMG             100M/1 SFP+          30m       Cat6A/7             Copper    RJ-45          Copper            -5 to                  IOS XE 17.11.1 —
                                                        000M/1                                                                                        85C
                                                        0G bps

Network Device Notes for above line :
• Supports 1000BASE-T and 10GBASE-T data rates only
Transceiver Notes for above line :
• Up to 30 meters with Cat6A/Cat7 or better (10G), up to 100 meters with Cat5e/Cat6A/Cat7 or better (100M/1000M)
C-NIM-4X            SFP-10G-ZR-I        TMG             10        SFP+       70km      Duplex Fiber        SMF       LC (UPC)       Optic             -28 to    Y            IOS XE 17.18.2 IOS XE
                                                        Gbps                                                                                          85C                                   17.18.2

Transceiver Notes for above line :
• At a cold start of -40C; the transceiver will be operational except optical traffic is not supported from -40 to -28C, all other low speed features (DOM, I2C, etc.) are operational. The module is
fully operational from -28C to 85C.
```
