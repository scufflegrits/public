# c-nim-wan-4s-tmg-optics-2026-10-30.pdf — extracted text

- Source PDF: [c-nim-wan-4s-tmg-optics-2026-10-30.pdf](c-nim-wan-4s-tmg-optics-2026-10-30.pdf)
- PDF title metadata: c-nim-wan-4s-tmg-optics-2026-10-30.pdf
- Publisher: Cisco (as registered in the research source entries).
- Source SHA-256: `e55d355e99021f63aa562b431a28db02cc47d5894b1580f43d50e41c569ab150`
- Converted: 2026-10-31 (UTC).
- Extraction tool: `pdftotext version 25.03.0`.
- Command: `pdftotext -layout -enc UTF-8 reference/c-nim-wan-4s-tmg-optics-2026-10-30.pdf -`.
- PDF pages: 1; page headings below use PDF page numbers.
- Language: English; no OCR or translation performed.
- Source access date and document revision: see the original source-register entries below; conversion does not update them.
- Source register: [C8375-TMG-3](../research-cisco-c8375-e-g2-r1.1.0.md#c8375-tmg-3).

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
Network        Transciever         Transceiver Data       Form Reach Cable Type           Media Connector Transceiver   Case     DOM       Min Software DOM
Device Product Product ID          Business    Rate       Factor                                Type      Type          Temp     Capable   Support      Support
ID                                 Unit
C-NIM-WAN-4S     GLC-GE-100FX      TMG           100      SFP     2km     Duplex Fiber    MMF      LC (UPC)   Optic     0 to               IOS XE 17.18.1 —
                                                 Mbps                                                                   70C
C-NIM-WAN-4S     GLC-TE            TMG           10/100/ SFP      100m    Cat5e/6A        Copper   RJ-45      Copper    -5 to              IOS XE 17.18.1 —
                                                 1000                                                                   85C
                                                 Mbps

Network Device Notes for above line :
• Supports 1000BASE-T and 100MBASE-T data rates only.
C-NIM-WAN-4S     GLC-BX-D          TMG           1 Gbps   SFP     10km    Single-strand   SMF      LC (UPC)   Optic     0 to     Y         IOS XE 17.18.1 IOS XE
                                                                          Fiber                                         70C                               17.18.1
C-NIM-WAN-4S     GLC-BX-U          TMG           1 Gbps   SFP     10km    Single-strand   SMF      LC (UPC)   Optic     0 to     Y         IOS XE 17.18.1 IOS XE
                                                                          Fiber                                         70C                               17.18.1
C-NIM-WAN-4S     GLC-BX40-D-I      TMG           1 Gbps   SFP     40km    Single-strand   SMF      LC (UPC)   Optic     -40 to   Y         IOS XE 17.18.1 IOS XE
                                                                          Fiber                                         85C                               17.18.1
C-NIM-WAN-4S     GLC-BX40-U-I      TMG           1 Gbps   SFP     40km    Single-strand   SMF      LC (UPC)   Optic     -40 to   Y         IOS XE 17.18.1 IOS XE
                                                                          Fiber                                         85C                               17.18.1
C-NIM-WAN-4S     GLC-BX80-D-I      TMG           1 Gbps   SFP     80km    Single-strand   SMF      LC (UPC)   Optic     -40 to   Y         IOS XE 17.18.1 IOS XE
                                                                          Fiber                                         85C                               17.18.1
C-NIM-WAN-4S     GLC-BX80-U-I      TMG           1 Gbps   SFP     80km    Single-strand   SMF      LC (UPC)   Optic     -40 to   Y         IOS XE 17.18.1 IOS XE
                                                                          Fiber                                         85C                               17.18.1
C-NIM-WAN-4S     GLC-BX40-DA-I     TMG           1 Gbps   SFP     40km    Single-strand   SMF      LC (UPC)   Optic     -40 to   Y         IOS XE 17.18.1 IOS XE
                                                                          Fiber                                         85C                               17.18.1
C-NIM-WAN-4S     GLC-EX-SMD        TMG           1 Gbps   SFP     40km    Duplex Fiber    SMF      LC (UPC)   Optic     -5 to    Y         IOS XE 17.18.1 IOS XE
                                                                                                                        85C                               17.18.1
C-NIM-WAN-4S     GLC-LX-SM-        TMG           1 Gbps   SFP     10km    Duplex Fiber    SMF      LC (UPC)   Optic     -40 to   Y         IOS XE 17.18.1 IOS XE
                 RGD                                                                                                    85C                               17.18.1

Transceiver Notes for above line :
• GLC-LX-SM-RGD can be used on MMF with a maximum reach of 550m
C-NIM-WAN-4S     GLC-SX-MMD        TMG           1 Gbps   SFP     1000m   Duplex Fiber    MMF      LC (UPC)   Optic     -5 to    Y         IOS XE 17.18.1 IOS XE
                                                                                                                        85C                               17.18.1

Transceiver Notes for above line :
• FDDI: 220m; OM1: 275m; OM2: 550m; OM3, OM4/OM5: 1000m
C-NIM-WAN-4S     GLC-LH-SMD        TMG           1 Gbps   SFP     10km    Duplex Fiber    SMF      LC (UPC)   Optic     -5 to    Y         IOS XE 17.18.1 IOS XE
                                                                                                                        85C                               17.18.1

Transceiver Notes for above line :
• GLC-LH-SMD can be used on MMF with a maximum reach of 550m
• LC mode-conditioning cable required for MMF applications
C-NIM-WAN-4S     GLC-ZX-SMD        TMG           1 Gbps   SFP     70km    Duplex Fiber    SMF      LC (UPC)   Optic     -5 to    Y         IOS XE 17.18.1 IOS XE
                                                                                                                        85C                               17.18.1
C-NIM-WAN-4S     DWDM-SFP-         TMG           1 Gbps   SFP     80km    Duplex Fiber    SMF      LC (UPC)   Optic     0 to     Y         IOS XE 17.18.1 IOS XE
                 XXXX                                                                                                   70C                               17.18.1
C-NIM-WAN-4S     GLC-GE-DR-LX      TMG           1 Gbps   SFP     10km    Duplex Fiber    SMF      LC (UPC)   Optic     0 to     Y         IOS XE 17.18.2 IOS XE
                                                                                                                        70C                               17.18.2
```
