# Research: Cisco C8300-1N1S-6T (r1.1.0)

Standalone model research file 4 of 4 for request
`request-cisco-comparison-r1.1.0.md`. Source tags use the prefix `C8300-6T-`
and resolve to headings under [References](#references).

## Research status

| Item | Status |
| --- | --- |
| Revision | r1.1.0; 2026-10-30 America/Chicago (continuation access dates recorded separately). Review corrections and completion of previously unattempted public-source work. |
| Research cutoff | Cutoff: 2026-10-30 America/Chicago. Original sources were accessed 2026-10-30; completion checks were accessed 2026-10-31 UTC (still 2026-10-30 America/Chicago). New source entries preserve their actual UTC access date; the cutoff and software basis are unchanged. |
| Confirmed identity | **Confirmed.** Supplied name `C8300-1N1S-6T` = PID `C8300-1N1S-6T`, Cisco Catalyst 8300 Series Edge Platforms, 1RU, 1 SM + 1 NIM + 1 PIM slot, 6×1G built-in ports (4×1G RJ-45 + 2×1G SFP) ([C8300-6T-DS-1](#c8300-6t-ds-1), [C8300-6T-OG-1](#c8300-6t-og-1), [C8300-6T-HIG-1](#c8300-6t-hig-1)). |
| **Lifecycle alert** | **The request's pre-check ("no EoL notice found") is contradicted.** Cisco bulletin **EOL15950** (announced 2026-07-27, amended, page updated 2026-10-19) puts C8300-1N1S-6T on End-of-Sale **2027-01-31**, Last Date of Support **2032-01-31**, last IOS XE train **28.2.x**, replacement **C8375-E-G2** ([C8300-6T-EOL-1](#c8300-6t-eol-1)). **As of 2026-10-30 the model is still orderable new** (End-of-Sale has not passed), with about three months of ordering left. The 1RU PoE power supply `PWR-CC1-500WAC` reaches End-of-Sale on the same date with no migration product. See [Lifecycle status](#lifecycle-status). |
| Software basis | **IOS XE 17.15.6** (Cisco-recommended: tech note 215567 rev 9.0, 2026-06-15, lists "17.12.8 or 17.15.6" for Catalyst 8300) ([C8300-6T-RR-1](#c8300-6t-rr-1)). Newest available train seen: **26.2.x (26.2.1)** ([C8300-6T-RN-2](#c8300-6t-rn-2)). Documented ceiling: **28.2.x** ([C8300-6T-EOL-1](#c8300-6t-eol-1)). |
| Operating mode | Autonomous mode (CLI) is the baseline. Controller mode (Catalyst SD-WAN) is supported by the same unified image; differences are called out ([C8300-6T-OG-1](#c8300-6t-og-1)). |
| Run status | **Complete**, with explicit evidence gaps. The completion pass read the formal SD-WAN compatibility tool, all seven field notices on the platform list, the August IOS XE hardening advisory and six October 2026 Snort advisories; corrected the CME conflict and module lifecycle; and verified additional inventory/environment commands from the saved platform guide. This is a decision-relevant review, not an exhaustive vulnerability or lab assessment. |

**Required review work completed:** the SD-WAN control-components matrix
and decision-relevant public security/field-notice review are documented in
[Software](#software) and [Platform-specific caveats](#platform-specific-caveats).

**Excluded or unavailable scope:** Cisco Feature Navigator and account-gated
Software Checker/Bug Search were not used; no credentials were supplied.
The 2RU sibling was considered only where shared documents establish a
placement limit. These exclusions do not supply positive compatibility or
security findings. Extended per-PID release/orderability details remain
explicit evidence gaps in the module tables after review of the available
public ordering, data-sheet and release sources.

**Sought but not found (evidence gaps after research):**

- Cisco documentation that `service unsupported-transceiver` exists on this
  platform, and TAC's position on third-party optics.
- 1G DAC cables, 1000BASE-SX/LX "SFP-GE-\*" variants, and any 100 Mb/s optic
  for the built-in SFP ports: not listed in TMG for this PID.
- Behavior when Smart Licensing Using Policy reporting deadlines are missed.
- Heat dissipation (BTU/hr), maximum power draw, CPU model and core count for
  this exact PID, TPM/trust-anchor details beyond "hardware-anchored Secure
  Boot and SUDI".
- Release date of IOS XE 17.15.6.
- A Catalyst 8300-specific statement of TACACS+ support. The generic IOS XE
  17.x Security and VPN Configuration Guide documents TACACS+ but lists no
  platforms, and the DNA routing matrix entitles TACACS+ in all three tiers
  but also names no platforms; support on this PID remains **inferred**.
- Openly published US pricing (none found; cost is **unknown**).

**Next steps:** confirm the TrustSec SGT and CME conflicts with Cisco; verify
any optional module and optics against the exact target release; confirm the
remaining DOM syntax on hardware or with TAC; obtain a US quote and check
serial-specific FN74146 eligibility before acceptance.

## Contents

- [Research status](#research-status)
- [Contents](#contents)
- [Summary](#summary)
- [Lifecycle status](#lifecycle-status)
- [Hardware specifications](#hardware-specifications)
- [Performance](#performance)
- [Software](#software)
- [Licensing](#licensing)
  - [Feature entitlement](#feature-entitlement)
  - [Throughput and crypto](#throughput-and-crypto)
  - [Purchase and enforcement](#purchase-and-enforcement)
  - [Offline operation (no internet for license reporting)](#offline-operation-no-internet-for-license-reporting)
- [Feature support and integration](#feature-support-and-integration)
  - [Feature matrix](#feature-matrix)
  - [Cisco ISE integration (router side)](#cisco-ise-integration-router-side)
- [Modules and expansion](#modules-and-expansion)
  - [Slot map](#slot-map)
  - [10G and Ethernet expansion](#10g-and-ethernet-expansion)
  - [Other module families](#other-module-families)
  - [Power supplies, memory, storage, and fans](#power-supplies-memory-storage-and-fans)
  - [Optics](#optics)
  - [Module reuse across the four platforms](#module-reuse-across-the-four-platforms)
- [Platform-specific caveats](#platform-specific-caveats)
  - [Differences from C8300-1N1S-4T2X](#differences-from-c8300-1n1s-4t2x)
- [Appendix A: identification and inventory commands](#appendix-a-identification-and-inventory-commands)
  - [Annotated listing](#annotated-listing)
  - [Paste-ready capture block](#paste-ready-capture-block)
- [References](#references)
  - [References - unresolved](#references---unresolved)

## Summary

**Multicast Service Reflection:** Cisco release notes document Unicast-to-Multicast Destination Reflection for the C8300-1N1S-6T product family starting in IOS XE 17.9.1a. This confirms family/release-level support for the MSR feature set; no test specific to this PID and the selected later IOS XE basis was located. [Catalyst 8200/8300 IOS XE 17.9 release notes](https://www.cisco.com/c/en/us/td/docs/routers/cloud_edge/c8300/rel_notes/17_9_x/cat8200-and-8300-rel-notes-xe-17-9-x.html) cover both exact C8300 PIDs and list Unicast-to-Multicast Destination Reflection in 17.9.1a. The [IOS XE 17.x multicast guide](https://www.cisco.com/c/en/us/td/docs/routers/ios-xe/ip-multicast/ip-multicast/m_imc_service_reflect-0.html) documents the `ip service reflect` configuration, its prerequisites and limitations, and MSR as introduced in IOS XE 3.4S.

| Field | Value |
| --- | --- |
| Model as supplied | `C8300-1N1S-6T` |
| Confirmed PID | `C8300-1N1S-6T` (no SKU correction needed) |
| Official family | Cisco Catalyst 8300 Series Edge Platforms ([C8300-6T-DS-1](#c8300-6t-ds-1), Table 2) |
| Cisco description | "C8300 1RU w/ 1G WAN"; 2×1GigE SFP, 4×1GigE RJ45, 8 GB DRAM, 16 GB M.2 storage ([C8300-6T-OG-1](#c8300-6t-og-1), Table 1, p. 3) |
| Identity sources | Datasheet C78-744088-09, ordering guide C07-744100-11, HIG Overview chapter |
| Variants and bundles | `C8300-1N1S-6T-V` (voice bundle with NIM-PVDM; listed as `NIM-PVDM-3`), `C83-1N1S-6T-CAP` (5-year DNA Advantage + 5-year SNTC 8x5xNBD bundle); both End-of-Sale 2027-01-31 with no migration product ([C8300-6T-EOL-1](#c8300-6t-eol-1), Table 2). No separate AC/DC base PID: power supplies are ordered as options ([C8300-6T-OG-1](#c8300-6t-og-1), Table 6). |

Role and lineup position: the 1RU, 1G-WAN member of the four-model Catalyst
8300 family. It shares the 1RU chassis, slots, memory, and module list with
`C8300-1N1S-4T2X`; the differences are the two built-in SFP ports (1G SFP here,
10G SFP+ on the 4T2X), a lower IPsec ceiling, and a lower throughput license
ceiling ([C8300-6T-DS-1](#c8300-6t-ds-1), Tables 2–5;
[C8300-6T-LIC-1](#c8300-6t-lic-1), Table 6).

Key takeaways:

1. **End-of-Sale is announced.** Orderable new until 2027-01-31 only; Last
   Date of Support 2032-01-31; last IOS XE train 28.2.x; Cisco's migration
   product is `C8375-E-G2` ([C8300-6T-EOL-1](#c8300-6t-eol-1)). A purchase now
   buys about five years of support. This is the largest decision risk.
1. **Performance is capped by licensing, not hardware alone.** Cisco
   publishes up to 1.9 Gbps IPsec (1400 bytes, autonomous mode); the highest
   throughput tier for this PID is **T2 = 2 Gbps aggregate encrypted
   throughput**; there is no T3 ([C8300-6T-DS-1](#c8300-6t-ds-1), Table 5;
   [C8300-6T-LIC-1](#c8300-6t-lic-1), Table 6;
   [C8300-6T-OG-1](#c8300-6t-og-1), p. 15). Unencrypted (CEF) throughput is
   documented as unthrottled by default ([C8300-6T-LIC-1](#c8300-6t-lic-1),
   "Throttled and unthrottled throughput").
1. **10G is only available through modules:** `C-NIM-1X` (1×10G),
   `C-NIM-4X` (4×1/10G, embedded NIM slot only), and the L2 switch module
   `C-SM-16P4M2X` (2×10G SFP+ uplinks) ([C8300-6T-DS-1](#c8300-6t-ds-1),
   Table 7; [C8300-6T-LANMOD-1](#c8300-6t-lanmod-1);
   [C8300-6T-SMSW-1](#c8300-6t-smsw-1)). No port faster than 10G exists.
1. **Offline licensing is documented.** Smart Licensing Using Policy supports
   the "No Connectivity to CSSM and No CSLU" topology with file-based
   reporting and file-based HSECK9 SLAC installation; SSM On-Prem supports
   manual (file) synchronization at least once a year
   ([C8300-6T-SLP-1](#c8300-6t-slp-1), pp. 45–46;
   [C8300-6T-ONP-1](#c8300-6t-onp-1)). Consequences of a missed report are
   not documented in the sources checked.
1. **Legacy switch NIMs cannot be newly ordered:** NIM-ES2-8/-8-P passed
   End-of-Sale 2025-03-05 and NIM-ES2-4 passed End-of-Sale 2025-04-17.
   Supported legacy hardware is distinct from an orderable new module;
   evaluate C-NIM-8T/8M for this chassis instead
   ([C8300-6T-EOL-2](#c8300-6t-eol-2),
   [C8300-6T-EOL-3](#c8300-6t-eol-3)).
1. **Hyperthreading:** contrary to the request's pre-check, the HIG lists
   `C8300-1N1S-6T` among the platforms where data-plane Hyperthreading (HT)
   support was added ([C8300-6T-HIG-1](#c8300-6t-hig-1), Overview, pp. 1–2;
   the list continues across the page break, and the HTML version shows all
   four PIDs).

Uncertainty that could change the decision: the per-tier feature map comes
from a family-level matrix and conflicts with the TrustSec matrix on SGT; no 1G DAC or 100 Mb/s optic listed for the built-in SFP
ports; pricing unknown. The built-in SFP ports accept the full 1G fiber
minimum set (SX, LX/LH, ZX) and the 1000BASE-T copper SFP `GLC-TE` from
17.3.2 ([C8300-6T-TMG-2](#c8300-6t-tmg-2)).

## Lifecycle status

Chassis notice: **EOL15950** "End-of-Sale and End-of-Life Announcement for the
Cisco Catalyst C8500L-8S4X, C8300-1N1S-4T2X, C8300-1N1S-6T" (marked
"Amended"; the page does not say what was amended)
([C8300-6T-EOL-1](#c8300-6t-eol-1), Table 1, p. 3–4). All milestones are
labeled HW.

| Milestone | Date | Source |
| --- | --- | --- |
| Series release (support page) | 2020-10-19 | [C8300-6T-SUP-1](#c8300-6t-sup-1) |
| End-of-Life Announcement | 2026-07-27 | [C8300-6T-EOL-1](#c8300-6t-eol-1), Table 1 |
| End-of-Sale | 2027-01-31 | [C8300-6T-EOL-1](#c8300-6t-eol-1), Table 1 |
| Last Ship Date | 2027-04-30 | [C8300-6T-EOL-1](#c8300-6t-eol-1), Table 1 |
| End of SW Maintenance Releases | 2031-03-30 | [C8300-6T-EOL-1](#c8300-6t-eol-1), Table 1 |
| End of Vulnerability/Security Support | 2032-01-31 | [C8300-6T-EOL-1](#c8300-6t-eol-1), Table 1 |
| End of Routine Failure Analysis | 2028-01-31 | [C8300-6T-EOL-1](#c8300-6t-eol-1), Table 1 |
| End of New Service Attachment | 2028-01-31 | [C8300-6T-EOL-1](#c8300-6t-eol-1), Table 1 |
| End of Service Contract Renewal | 2031-04-30 | [C8300-6T-EOL-1](#c8300-6t-eol-1), Table 1 |
| Last Date of Support | 2032-01-31 | [C8300-6T-EOL-1](#c8300-6t-eol-1), Table 1 |
| Last supported IOS XE train | 28.2.x | [C8300-6T-EOL-1](#c8300-6t-eol-1), text below Table 1 |
| Cisco recommended replacement | C8375-E-G2 ("Cisco C8300 Series Secure Router") | [C8300-6T-EOL-1](#c8300-6t-eol-1), Table 2 |

**Orderable new as of 2026-10-30: yes** (documented; End-of-Sale is
2027-01-31). After that date, Cisco states units may be available through the
Cisco Refresh (remanufactured) program, which does not meet the new-purchase
requirement ([C8300-6T-EOL-1](#c8300-6t-eol-1), "Product migration options").

Separate notices:

| Item | Notice | Status |
| --- | --- | --- |
| `C8300-1N1S-6T-V`, `C83-1N1S-6T-CAP` bundles | EOL15950 | End-of-Sale 2027-01-31, no migration product ([C8300-6T-EOL-1](#c8300-6t-eol-1), Table 2) |
| `PWR-CC1-500WAC` / `=` (1RU AC PSU with PoE) | EOL15950 | End-of-Sale 2027-01-31, no migration product ([C8300-6T-EOL-1](#c8300-6t-eol-1), Table 2) |
| `PWR-CC1-400WAC/2`, `C8300-PS-BLANK1R` / `=` | EOL15950 | End-of-Sale 2027-01-31 ([C8300-6T-EOL-1](#c8300-6t-eol-1), Table 2) |
| Select Catalyst 8300/8200/8500 convenience bundles | Listed 2022-11-07 on the support page | Title only; content not read ([C8300-6T-SUP-1](#c8300-6t-sup-1)) |
| IOS XE trains 17.3.x–17.18.x | Per-train EoL notices | Listed on the support page (17.18.x notice dated 2026-10-30); not read individually ([C8300-6T-SUP-1](#c8300-6t-sup-1)) |
| Licenses, modules (C-NIM-1X, C-NIM-4X, etc.) | — | No module or license EoL notice found in sources checked as of 2026-10-30 |

No support horizon was supplied, so the milestones are not tested against one.

## Hardware specifications

| Attribute | Value | Source |
| --- | --- | --- |
| Form factor / RU | Rack-mount, 1RU | [C8300-6T-DS-1](#c8300-6t-ds-1), Table 15 |
| Dimensions (H × W × D) | 1.73 in. × 17.50 in. × 16.25 in. (shared 1RU column with C8300-1N1S-4T2X) | [C8300-6T-DS-1](#c8300-6t-ds-1), Table 15 |
| Weight | 20 lb (chassis with 2× AC PSUs and fan tray) | [C8300-6T-DS-1](#c8300-6t-ds-1), Table 15 |
| CPU | Family: "8 or 12 core CPU". Core count for this PID **not stated**; **inferred** 8-core because the datasheet names only C8300-2N2S-4T2X as the 12-core platform. Data-plane HT support listed for this PID. | [C8300-6T-DS-1](#c8300-6t-ds-1), Table 1 and "Dynamic core allocation"; [C8300-6T-HIG-1](#c8300-6t-hig-1), p. 1–2 |
| DRAM | 8 GB default (1 DIMM); upgrades MEM-C8300-16GB, MEM-C8300-32GB | [C8300-6T-OG-1](#c8300-6t-og-1), Table 3; [C8300-6T-HIG-1](#c8300-6t-hig-1), p. 10 |
| Flash / storage | 8 GB on-board flash (not upgradeable); 16 GB M.2 USB default; options M2USB-32G, SSD-M2NVME-600G (OG) / SSD-M2SED-600G, SSD-M2NVME-2T (DS) | [C8300-6T-OG-1](#c8300-6t-og-1), Table 3; [C8300-6T-DS-1](#c8300-6t-ds-1), Tables 1, 8 |
| Fixed Ethernet ports | GE 0/0/0–0/0/3: RJ-45 10BASE-T/100BASE-TX/1000BASE-T. GE 0/0/4–0/0/5: SFP, 1 Gbps SFP modules. Layer 3 ports. Not combo ports. | [C8300-6T-HIG-1](#c8300-6t-hig-1), Tables 1, pp. 2–3, 9; [C8300-6T-DS-1](#c8300-6t-ds-1), Table 2 |
| 10G built-in ports | None ("-" in 10G column) | [C8300-6T-DS-1](#c8300-6t-ds-1), Table 2 |
| Management / console / USB | RJ-45 console, micro-USB console, USB 3.0 Type-A (USB0), USB 3.0 Type-C (USB1). No out-of-band GigabitEthernet0 management interface: FAQ states only in-band management. | [C8300-6T-HIG-1](#c8300-6t-hig-1), Table 1; [C8300-6T-FAQ-1](#c8300-6t-faq-1), out-of-band management question |
| Module slots | 1 NIM, 1 SM (single-wide), 1 PIM; up to 3 NIMs with C-SM-NIM-ADPT | [C8300-6T-OG-1](#c8300-6t-og-1), Table 4 |
| Power supplies | Dual AC PSUs ship by default (PWR-CC1-250WAC); options PWR-CC1-500WAC (AC with PoE), PWR-CC1-400WDC; DS also lists PWR-CC1-400WHV (240–380 V DC). Hot-swap, dual. | [C8300-6T-OG-1](#c8300-6t-og-1), Table 6; [C8300-6T-DS-1](#c8300-6t-ds-1), Table 9; [C8300-6T-HIG-1](#c8300-6t-hig-1), Table 5 |
| PSU capacity | 250 W (250WAC); 500 W (500WAC, PoE budget 250 W); 400 W (400WDC, 400WHV) | [C8300-6T-DS-1](#c8300-6t-ds-1), Table 9 |
| PoE | No built-in PoE ports. PoE on NIM/SM ports requires at least one PoE-capable PSU | [C8300-6T-DS-1](#c8300-6t-ds-1), Table 1 |
| Power consumption | Typical 82 W (no modules, single PSU). Maximum draw: **not found**. | [C8300-6T-DS-1](#c8300-6t-ds-1), Table 11 |
| Heat dissipation | **Not found in sources checked** | — |
| Input voltage | AC 85–264 VAC; DC −40 to −72 V (48 V nominal) | [C8300-6T-DS-1](#c8300-6t-ds-1), Table 15 |
| Airflow | Internal fan tray (C8300-FAN-1R, shipped by default); airflow figure in HIG, direction not stated in text. Reverse-airflow NEBS option is documented for 2RU only. | [C8300-6T-HIG-1](#c8300-6t-hig-1), pp. 12–13; [C8300-6T-DS-1](#c8300-6t-ds-1), "NEBS", Table 8 |
| Operating temperature | 0 to 40 °C (32 to 104 °F); altitude 0–3050 m | [C8300-6T-DS-1](#c8300-6t-ds-1), Table 15 |
| Acoustics | Sound pressure 49/71 dBA typical/max; sound power 60/82 dBA | [C8300-6T-DS-1](#c8300-6t-ds-1), Table 15 |
| MTBF | 536,060 hours (1RU column) | [C8300-6T-DS-1](#c8300-6t-ds-1), Table 15 |
| Security hardware | Hardware-anchored Secure Boot and SUDI; Trustworthy Solutions 2.0; IPsec and SSL crypto hardware acceleration. TPM / Trust Anchor module naming: **not found**. | [C8300-6T-DS-1](#c8300-6t-ds-1), Table 1 |
| Warranty | Cisco Limited 1-Year Return To Factory Hardware Warranty | [C8300-6T-OG-1](#c8300-6t-og-1), p. 22 |
| Included accessories | 19-in. rack kit, RFID tag (deselectable), fan tray, slot blanks when no module ordered | [C8300-6T-OG-1](#c8300-6t-og-1), Table 7 |

## Performance

All figures are Cisco "up to" or test values from
[C8300-6T-DS-1](#c8300-6t-ds-1). Conditions not listed are **not disclosed**.
Licensed limits and port line rates are separate rows and are not converted.

| Metric | Value | Packet size / mix | Direction | Mode | Release | License tier | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| IPv4 forwarding | Up to 19.7 Gbps | 1400 bytes | not disclosed | Autonomous | not disclosed | not disclosed | DS Table 5 |
| IPsec | Up to 1.9 Gbps | 1400 bytes | not disclosed | Autonomous | not disclosed | not disclosed | DS Table 5 |
| IPsec | 1.9 Gbps | IMIX (352-byte average) | not disclosed | Autonomous | not disclosed | not disclosed | DS Table 5 |
| SD-WAN IPsec | Up to 2 Gbps | 1400 bytes | not disclosed | Controller | not disclosed | not disclosed | DS Table 3 |
| SD-WAN IPsec with IQDF (IPsec+QoS+DPI+FNF) | Up to 2 Gbps | 1400 bytes | not disclosed | Controller | not disclosed | not disclosed | DS Table 3 |
| SD-WAN IPsec | 1.8 Gbps | IMIX | not disclosed | Controller | not disclosed | not disclosed | DS Table 3 |
| SD-WAN IPsec with IQDF | 1.7 Gbps | IMIX | not disclosed | Controller | not disclosed | not disclosed | DS Table 3 |
| 50% IQDF + 50% DIA (NAT, NGFW, IPS, URLF, AMP) | 2.6 Gbps | Firewall EMIX | not disclosed | Controller | 17.12.2 | not disclosed | DS Table 4 |
| DIA with NAT + NGFW + IPS + URLF + AMP | 2.1 Gbps | Firewall EMIX | not disclosed | Controller | 17.12.2 | not disclosed | DS Table 4 |
| **Licensed crypto ceiling** (T2 or 1G numeric) | 2G aggregate | n/a (licensed limit) | aggregate (≥17.8.1a) | Autonomous | ≥17.8.1a | T2 + HSECK9 | [C8300-6T-LIC-1](#c8300-6t-lic-1), Table 6 |
| **Licensed crypto ceiling, controller mode** | 2G aggregate with HSECK9; 250M bidirectional without | n/a | aggregate (>17.8.1a) | Controller | >17.8.1a | HSECK9 | [C8300-6T-LIC-1](#c8300-6t-lic-1), controller-mode table |
| Port line rate, built-in | 6 × 1 Gbps | n/a | per port | both | — | — | DS Table 2 |

Scale (autonomous mode, DS Table 6, same for all four C8300 models): 4000
IPsec SVTI tunnels; 4000 ACLs; 72K IPv4 ACEs; IPv4 routes 1.6M (8 GB) up to
4M (32 GB); IPv6 routes 1.5M (8 GB) up to 4M (32 GB); 8K queues; NAT sessions
1.2M (8 GB) up to 2M (32 GB); 512K firewall sessions; 4000 VRFs. SD-WAN
overlay tunnel scale: 6000 (DS Table 3). Without HSECK9 the tunnel count is
limited to 1000 ([C8300-6T-LIC-1](#c8300-6t-lic-1), HSECK9 table).

## Software

| Release role | Version | Release date | Recommendation/notice date | Mode | Source |
| --- | --- | --- | --- | --- | --- |
| Cisco-recommended (chosen basis) | 17.15.6 | not found | 2026-06-15 (rev 9.0) | not split by mode in source | [C8300-6T-RR-1](#c8300-6t-rr-1); listed in [C8300-6T-RN-1](#c8300-6t-rn-1) |
| Cisco-recommended (alternative) | 17.12.8 | not found | 2026-06-15 (rev 9.0) | not split by mode | [C8300-6T-RR-1](#c8300-6t-rr-1) |
| Newest available train seen | 26.2.x (26.2.1) | not stated (release notes updated 2026-09-27) | — | autonomous and controller | [C8300-6T-RN-2](#c8300-6t-rn-2) |
| Documented ceiling | 28.2.x train | future | EOL15950 (updated 2026-10-19) | — | [C8300-6T-EOL-1](#c8300-6t-eol-1) |
| Minimum for platform | 17.3.2 | — | — | both | [C8300-6T-DS-1](#c8300-6t-ds-1), Table 12 |

- **Recommendation provenance:** Cisco tech note 215567, "Choose Stable Cisco
  IOS XE Release for Enterprise Routing Platforms", row "Catalyst 8300":
  "17.12.8 or 17.15.6", note "Depending on feature requirements". It applies
  to the Catalyst 8300 platform family (all four PIDs); it does not split
  autonomous and controller mode ([C8300-6T-RR-1](#c8300-6t-rr-1)). Basis
  chosen: 17.15.6, the newer of the two, because it includes the 17.14.1a
  T1/250M aggregate-throttling change. **Controller-mode basis:** Cisco's
  SD-WAN recommended-release document (215676 rev 21.0, 2026-08-19) lists
  "17.12.8, 17.15.6" for Cisco IOS XE SD-WAN (cEdge) and "20.12.8.1, 20.15.6"
  for the control components (SD-WAN Manager, Controller, Validator); it does
  not name the Catalyst 8300 and says only routers that support a version
  qualify ([C8300-6T-SDWAN-1](#c8300-6t-sdwan-1)). **Documented family-level controller pairing:** the formal compatibility
  tool lists IOS XE 17.15.6 for Catalyst 8300 under control components
  20.15.6 and 20.15.6.1. The latter is compatibility evidence, not a new
  recommended-release designation. Exact-PID application is inferred from
  the model being in that named family ([C8300-6T-COMP-1](#c8300-6t-comp-1),
  [C8300-6T-COMP-2](#c8300-6t-comp-2)). Do not assume arbitrary mixed-version
  combinations from matching train numbers.
- **Feature minimums relevant here:** tier-based throughput 17.7.1a; aggregate
  throttling 17.8.1a; T1/250M 500M aggregate with HSECK9 17.14.1a
  ([C8300-6T-LIC-1](#c8300-6t-lic-1), Table 1); C-NIM-4X and C-NIM-8T 17.11.1;
  C-NIM-8M 17.12.2 ([C8300-6T-LANMOD-1](#c8300-6t-lanmod-1)); C-NIM-2T and
  C-NIM-1M 17.6.1 ([C8300-6T-WANMOD-1](#c8300-6t-wanmod-1)). **Some module
  optics need releases above the basis** (C-NIM-4X: GLC-TE 17.18.1;
  SFP-10G-ZR-I, SFP-10G-ER-S, GLC-GE-DR-LX 17.18.2) ([C8300-6T-TMG-1](#c8300-6t-tmg-1)).
- **Install vs. bundle mode:** "From Cisco IOS XE Cupertino 17.7.1a, Cisco
  Catalyst 8000 Edge platforms are shipped in install mode by default"; bundle
  mode boots a single .bin, install mode boots `packages.conf`
  ([C8300-6T-SCG-1](#c8300-6t-scg-1), "Software Installation").
- **Modes:** the unified image supports autonomous and controller mode; order
  default is autonomous (`IOSXE-AUTO-MODE`), `IOSXE-CTRL-MODE` selects
  controller; Cisco states you can switch between modes
  ([C8300-6T-OG-1](#c8300-6t-og-1), Table 2, p. 6). The software guide documents privileged EXEC `controller-mode enable`
  (autonomous to controller) and `controller-mode disable` (reverse). The
  first direction erases startup configuration and NVRAM information, including
  certificates; plan configuration/certificate backup and onboarding before
  conversion. These state-changing commands are excluded from Appendix A
  ([C8300-6T-SCG-1](#c8300-6t-scg-1), Overview, PDF pp. 7–8).
- **ROMMON:** minimum 17.3(4.2r); recommended 17.9(7r) per 17.15.x notes and
  26.1(1r) per 26.2.x notes; below the minimum, Cisco says to boot 17.12.4
  (17.15 notes) or 17.12.5 (26.2 notes) first to auto-upgrade ROMMON
  ([C8300-6T-RN-1](#c8300-6t-rn-1); [C8300-6T-RN-2](#c8300-6t-rn-2)).
- **26.2.x notes:** UTD moves from the NGFW V1 engine to the V2 engine with
  separately managed LSP/VDB packages; insecure protocols warn and the web
  server is disabled by default ([C8300-6T-RN-2](#c8300-6t-rn-2)). Applies only
  if moving beyond the basis.

## Licensing

Licensing layers at 17.15.6 (autonomous mode): Network-stack license
(perpetual) + optional DNA-stack add-on (subscription), or Catalyst Routing
Essentials (7-year subscription); throughput level; HSECK9; separately
ordered UC licenses. Legacy ISR technology packages (ipbase, appxk9,
securityk9, uck9) do not apply: "Catalyst 8300 and 8200 edge platforms do not
require specific UCK9, SECK9, or APPK9 licenses"
([C8300-6T-OG-1](#c8300-6t-og-1), p. 11); a DNA license "subsumes all
performance, boost, and technology package licenses"
([C8300-6T-LIC-1](#c8300-6t-lic-1), "Ordering considerations"). Only Smart
Licensing Using Policy is supported ([C8300-6T-OG-1](#c8300-6t-og-1), p. 22).

### Feature entitlement

| Capability | Tier or license | Dependencies | Mode / release | Source |
| --- | --- | --- | --- | --- |
| Base routing ("Everything in Cisco's IP-Base") | Catalyst Routing Essentials, or Network Essentials and above | — | Autonomous | [C8300-6T-OG-1](#c8300-6t-og-1), p. 16; [C8300-6T-LIC-1](#c8300-6t-lic-1) |
| Point-to-point IPsec | All three tiers ("Secure infrastructure: IPsec (point to point)"); Routing Essentials also per OG-1 ("Point-2-Point IPSec with HSEC") | HSECK9 for >250 Mbps or >1000 tunnels | Autonomous | [C8300-6T-OG-1](#c8300-6t-og-1), p. 16; [C8300-6T-MX-1](#c8300-6t-mx-1) |
| DMVPN, GET VPN, FlexVPN | DNA Essentials or DNA Advantage, not Routing Essentials (no SSL VPN except on Catalyst 8000V) | HSECK9 as above | Autonomous | [C8300-6T-MX-1](#c8300-6t-mx-1) footnote 1 |
| Application-based firewall (NGFW) | All three tiers ("Perimeter security: L3-L7 firewall, ACL") | — | Autonomous | [C8300-6T-OG-1](#c8300-6t-og-1), p. 16; [C8300-6T-MX-1](#c8300-6t-mx-1) |
| On-premises SD-Routing (SD-WAN Manager managing an autonomous router) | Routing Essentials | SD-WAN Manager on-prem | Autonomous | [C8300-6T-OG-1](#c8300-6t-og-1), p. 16 |
| CUBE | Minimum DNA Essentials (Network Essentials) **plus** CUBE license (A-FLEX-3) | CUBE license ordered separately; unenforced | Autonomous | [C8300-6T-OG-1](#c8300-6t-og-1), Table 9; [C8300-6T-LIC-1](#c8300-6t-lic-1), "Cisco Unified Border Element license" |
| SRST | Minimum DNA Advantage (Network Advantage) plus SRST license (A-FLEX-3) | Unenforced SRST license | Autonomous | [C8300-6T-OG-1](#c8300-6t-og-1), Table 9 |
| Voice modules (FXS/FXO, BRI, E&M, T1/E1 MFT, DSP) | Minimum DNA Advantage (Network Advantage) | Module hardware | Autonomous | [C8300-6T-OG-1](#c8300-6t-og-1), Table 9 |
| UC/voice with Routing Essentials | Not entitled ("doesn't come with any UC/Voice feature entitlements") | — | — | [C8300-6T-OG-1](#c8300-6t-og-1), p. 11 |
| TrustSec (SGT classification, SXP, inline tagging, SGACL) | **Conflict:** Network Advantage (family row) per the GBP matrix; all three tiers per the DNA routing matrix ("Network segmentation": TrustSec SGT, SGACL). Network Advantage assumed until Cisco confirms | — | Both (family) | [C8300-6T-GBP-1](#c8300-6t-gbp-1), Table 1; [C8300-6T-MX-1](#c8300-6t-mx-1) |
| SD-WAN (controller mode) | DNA subscription (Essentials or Advantage); only the DNA stack is consumed in SD-WAN | SD-WAN Manager/controllers | Controller | [C8300-6T-DNA-1](#c8300-6t-dna-1), Appendix D |
| UTD (IPS/IDS, URL filtering, AMP) | DNA Essentials or DNA Advantage, not Routing Essentials ("Threat protection"). AMP and URL filtering "Supported only with SD-Routing" (footnote 3); IPS/IDS has no such footnote | UTD container / signature packages | Autonomous (IPS/IDS); SD-Routing (AMP, URLF) | [C8300-6T-MX-1](#c8300-6t-mx-1) footnote 3 |
| DNA Advantage only | Carrier-grade NAT; MPLS L2/L3 VPN, LDP, TE, VPLS, EVPN; L2TPv3, EoGRE; WCCP; NBAR2 custom packs, ALG, SD-AVC; app hosting; VXLAN; SRST, CME category (platform support conflicting), analog/digital voice cards; LISP | — | Autonomous | [C8300-6T-MX-1](#c8300-6t-mx-1) |
| Throughput T3 and higher | Not available with Network/DNA Essentials (and not offered on this PID at all) | — | Autonomous | [C8300-6T-LIC-1](#c8300-6t-lic-1), "Guidelines for using a Cisco DNA license" |

Ordering contents of Routing Essentials: "All required entitlements such as
NWSTACK-T2-E, DSTACK-T0-E, HSEC is auto-included"; it "unlocks maximum
platform throughput capability for IP-CEF and Crypto traffic throughput up to
2Gbps" ([C8300-6T-OG-1](#c8300-6t-og-1), pp. 16, 19). **Inferred:** on this
PID, Routing Essentials reaches the T2 ceiling, because Cisco states T2 is
this PID's maximum ([C8300-6T-OG-1](#c8300-6t-og-1), p. 15).

### Throughput and crypto

Export authorization (HSECK9), crypto capability, and the throughput license
are kept separate below.

| Tier / license | Limit unlocked (autonomous, ≥17.14.1a) | Crypto restriction | Prerequisites | Source |
| --- | --- | --- | --- | --- |
| Default (no throughput config) | 10M bidirectional | — | Boot-level license configured | [C8300-6T-LIC-1](#c8300-6t-lic-1), Table 6 |
| 10M / 15M / 25M / 50M / 100M | Same value, bidirectional | No HSECK9 needed | Boot-level license | Table 6 |
| T0 | 25M bidirectional (15M in 17.7.x) | No HSECK9 needed | Tier PID; 17.7.1a+ | Table 6 |
| 250M or T1 | 500M aggregate with HSECK9; 250M bidirectional without | Works without HSECK9 (bidirectional) | T1 PID auto-adds HSECK9 | Table 6; Table 1 |
| 500M\* (numeric) | 1G aggregate | HSECK9 required | SLAC installed | Table 6 |
| 1G\* (numeric) | 2G aggregate | HSECK9 required | SLAC installed | Table 6 |
| T2\* | 2G aggregate (**maximum for this PID**) | HSECK9 required | SLAC installed | Table 6; [C8300-6T-OG-1](#c8300-6t-og-1), p. 15 |
| T3 and above | **Documented unsupported** on this PID (no row; T2 is maximum) | — | — | Table 6; OG p. 15 |
| HSECK9 (`C8000-HSEC`, `C8000-HSEC-DNA`, spare `C8000-HSEC=`) | Lifts the 1000-tunnel limit and the 250 Mbps cap | Export-controlled; one per chassis UDI; needs SLAC; then `license feature hseck9` | Included with DNA subscriptions; factory SLAC install only if ordered with hardware and SA/VA supplied | [C8300-6T-OG-1](#c8300-6t-og-1), Table 8, p. 10; [C8300-6T-LIC-1](#c8300-6t-lic-1), "High Security license" |

Throughput changes require saving the configuration and a reload
([C8300-6T-LIC-1](#c8300-6t-lic-1), "Configure numeric throughput"). Throttling
applies to crypto throughput; "Unencrypted throughput (Tx and Rx), is
unthrottled by default" ([C8300-6T-LIC-1](#c8300-6t-lic-1), p. 14).

**Source conflicts:**

1. The same guide's HSECK9 table note says "The term throughput refers to
   encrypted and unencrypted throughput, combined" (p. 7), while p. 14 says all
   throughput references mean crypto throughput and CEF is unthrottled. **Left
   unresolved;** the throttling tables are labeled "Throughput = Encrypted
   Throughput", which supports the p. 14 reading.
1. The DNA ordering guide gives generic tier sizes "T1: up to 400 Mbps
   aggregate", "T2: up to 2 Gbps aggregate" ([C8300-6T-DNA-1](#c8300-6t-dna-1),
   Tables 6/9), while the platform guide gives T1 = 500M aggregate with
   HSECK9 from 17.14.1a ([C8300-6T-LIC-1](#c8300-6t-lic-1), Table 6). The
   platform-specific guide is chosen for this PID; the ordering guide does not
   list the Catalyst 8300 in its Table 9.
1. Without HSECK9 the ordering guide says "one-way encrypted throughput of up
   to 250 Mbps" ([C8300-6T-OG-1](#c8300-6t-og-1), p. 10), consistent with
   "250M bidirectional" in [C8300-6T-LIC-1](#c8300-6t-lic-1). No conflict.
1. TrustSec SGT tier: Network Advantage per the GBP matrix
   ([C8300-6T-GBP-1](#c8300-6t-gbp-1)), but the DNA routing matrix ticks
   "Network segmentation" (TrustSec SGT, SGACL) for all three tiers
   ([C8300-6T-MX-1](#c8300-6t-mx-1)). **Left unresolved;** Network Advantage is assumed.
1. CME: the data sheet lists CUCME, while the exact-family FAQ says on-box
   CME is unsupported. A DNA matrix category or CUBE/SRST order row does
   not settle that chassis-support conflict ([C8300-6T-DS-1](#c8300-6t-ds-1),
   Table 13; [C8300-6T-FAQ-1](#c8300-6t-faq-1), Collaboration).

### Purchase and enforcement

| License | Perpetual / subscription | Terms | Orderable today (2026-10-30) | Reporting method | Deadlines / connectivity (Cisco default policy) | Expiry or noncompliance | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Network Essentials / Advantage / Premier | Perpetual | — | Yes, as part of a DNA subscription PID (the purchasable PID is the DNA-stack add-on) | Direct, CSLU, SSM On-Prem, or offline file | Unenforced perpetual: first report 365 days (only if bought from a distributor/partner), report on change 90 days | Not documented in sources checked | [C8300-6T-LIC-1](#c8300-6t-lic-1); [C8300-6T-SLP-1](#c8300-6t-slp-1), Table 4 |
| DNA Essentials / Advantage (add-on) | Subscription | 3, 5, or 7 years (7-year not in EAs) | Yes (with the chassis until 2027-01-31) | As above | Unenforced subscription: first report 90 days, then every 90 days, report on change 90 days | On term expiry: renew, or deactivate the add-on and reload to keep network-stack features | [C8300-6T-DNA-1](#c8300-6t-dna-1); [C8300-6T-LIC-1](#c8300-6t-lic-1); [C8300-6T-SLP-1](#c8300-6t-slp-1), Table 4 |
| DNA Premier | Subscription | not verified | **Not verified** (datasheet lists only Routing Essentials, DNA Essentials, DNA Advantage) | — | — | — | [C8300-6T-DS-1](#c8300-6t-ds-1), "Licensing" |
| Catalyst Routing Essentials (`ROUT-P-C8300-E-7Y`) | Subscription | 7 years only; no bandwidth tiering | Yes; autonomous mode only (cannot be selected with `IOSXE-CTRL-MODE`) | As above | Bundles NWSTACK-T2-E (perpetual element) and DSTACK-T0-E; reporting cadence depends on which licenses are in use (see offline section) | Not documented | [C8300-6T-OG-1](#c8300-6t-og-1), Table 12, pp. 17–19 |
| HSECK9 | Perpetual (shown as PERPETUAL, EXPORT RESTRICTED) | — | Yes (included with DNA subscriptions; spare `C8000-HSEC=`) | SLAC (authorization code) install | Export policy: report values 0 (no periodic reporting); authorization required before use | Removing an authorization code "removes the licenses ... and may cause a change in the behavior" | [C8300-6T-LIC-1](#c8300-6t-lic-1), "Verify HSECK9 status"; [C8300-6T-SLP-1](#c8300-6t-slp-1), Table 4; [C8300-6T-SLP-2](#c8300-6t-slp-2) |
| CUBE and SRST licenses (CME unresolved) | not verified | not verified | Yes (A-FLEX-3 major-line PID) | Usage reporting via SLP | Unenforced | Not documented | [C8300-6T-OG-1](#c8300-6t-og-1), Table 9; [C8300-6T-LIC-1](#c8300-6t-lic-1) |
| MSLA | — | — | **Documented unsupported** in autonomous mode | — | — | — | [C8300-6T-LIC-1](#c8300-6t-lic-1), "Managed Service Licensing Agreement" |

The SLP guide states that a value of zero means no report is required for that
trigger ("If the value here is not zero, reporting is required after the
change is made"), and a product instance that has never consumed a license
need not report ([C8300-6T-SLP-1](#c8300-6t-slp-1), p. 6). Cisco describes SLP
as "a licensing solution that does not interrupt the operations of your
network" ([C8300-6T-SLP-1](#c8300-6t-slp-1), Chapter 1), but no source checked
states the effect of a missed deadline: **unresolved.** The only documented
symptoms are syslog messages such as `%SMART_LIC-6-REPORTING_REQUIRED` ("A
Usage report acknowledgement will be required in [dec] days")
([C8300-6T-SLP-2](#c8300-6t-slp-2)).

### Offline operation (no internet for license reporting)

**Eligibility: documented.** Cisco documents an air-gapped topology for
Catalyst 8300 ("Workflow for Topology: No Connectivity to CSSM and No CSLU"),
and the Catalyst 8300 is a supported SLP product from IOS XE 17.3.2
([C8300-6T-SLP-1](#c8300-6t-slp-1), pp. 2, 45–46). An internet-connected
workstation (not the router) is still needed to exchange files with CSSM.

Steps (from [C8300-6T-SLP-1](#c8300-6t-slp-1), pp. 45–46, and
[C8300-6T-LIC-1](#c8300-6t-lic-1)):

1. CSSM web UI (from any connected workstation): ensure Smart Account /
   Virtual Account access.
1. Router: `license smart transport off`; save the configuration.
1. Router: set the boot level license (`license boot level ...`), reload.
1. HSECK9 SLAC (needed for >250 Mbps or >1000 tunnels): either
   - Option 1: generate and download a SLAC in CSSM by entering the product
     instance's UDI, then install the file on the router; or
   - Option 2 (17.7.1a+): generate a SLAC request file on the router
     (`license smart authorization request ...` / `... save <path>`), upload it
     to CSSM, download the SLAC, install it with `license smart import`.
   - Then `license feature hseck9` (Catalyst 8200/8300 requirement), and set
     the throughput level; save and reload.
   - Alternative: if HSECK9 is ordered with the hardware and the SA/VA is
     supplied, Cisco factory-installs the SLAC
     ([C8300-6T-LIC-1](#c8300-6t-lic-1), "Ordering considerations for an
     HSECK9 license").
1. Reporting: `license smart save usage all file bootflash:<file>` (from
   17.7.1a this also includes a trust-code request); copy the file off the
   router; upload it to CSSM; download the ACK; install it on the router
   (`license smart import`).

Cadence (Cisco default policy, inferred from Table 4 applied to the licenses
in use; the actual policy is shown by `show license all`):

| Configuration in use | Offline reporting workload |
| --- | --- |
| Network-stack only (traditional routing; per [C8300-6T-DNA-1](#c8300-6t-dna-1) only the network stack is consumed) + HSECK9 | One-time SLAC install per chassis; report within 90 days after any license change; first report within 365 days only if bought through a partner/distributor |
| Network stack + DNA add-on configured (subscription consumed) | First report within 90 days, then at least every 90 days, plus within 90 days of any change |
| Any config, every change of license level | One report-and-ACK cycle within 90 days |

**SSM On-Prem option:** free ISO-packaged server; it can run fully offline
with "Manual synchronization involves a file transfer at least once a year"
([C8300-6T-ONP-1](#c8300-6t-onp-1)); routers sync to it with
`license smart sync local`, and On-Prem exports usage to Cisco via file when
disconnected ([C8300-6T-SLP-1](#c8300-6t-slp-1), "Workflow for Topology: SSM
On-Prem Deployment"). This moves per-router file handling to one annual
On-Prem exchange, at the cost of running the On-Prem VM.

**CSLU disconnected** is also documented (CSLU collects from routers; the
admin exports/imports files to CSSM) ([C8300-6T-SLP-1](#c8300-6t-slp-1)).

## Feature support and integration

Basis: IOS XE 17.15.6, autonomous mode unless stated.

### Feature matrix

| Feature | Supported | Mode | License / tier | Module / hardware | Min release | Key limits | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SD-WAN | Yes | Controller | DNA Essentials/Advantage subscription | — | 17.3.2 (platform) | 6000 overlay tunnels; 2G aggregate crypto with HSECK9 | [C8300-6T-DS-1](#c8300-6t-ds-1), Tables 3, 14; [C8300-6T-LIC-1](#c8300-6t-lic-1) |
| IPsec VPN | Yes | Both | Any tier; HSECK9 for >250 Mbps / >1000 tunnels | Crypto acceleration built in | 17.3.2 | 4000 SVTI tunnels; 1.9 Gbps (1400 B); T2 cap 2G aggregate | [C8300-6T-DS-1](#c8300-6t-ds-1), Tables 5, 6, 13 |
| NAT | Yes | Both | All three tiers (NAT/PAT IPv4/v6); carrier-grade NAT DNA Advantage only | — | 17.3.2 | 1.2M sessions (8 GB), 2M (32 GB) | [C8300-6T-DS-1](#c8300-6t-ds-1), Tables 6, 14; [C8300-6T-MX-1](#c8300-6t-mx-1) |
| QoS (CBWFQ, WRED, HQoS, NBAR) | Yes | Both | MQC, HQoS, NBAR2 standard packs in all three tiers; NBAR2 custom packs DNA Advantage only | — | 17.3.2 | 8K queues | [C8300-6T-DS-1](#c8300-6t-ds-1), Tables 6, 13; [C8300-6T-MX-1](#c8300-6t-mx-1) |
| Voice / CUBE / SRST | Yes for documented voice functions; exact feature/mode restrictions must be checked | Autonomous; controller support is feature-dependent, not blanket parity | CUBE: DNA Essentials + CUBE license; SRST and voice modules: DNA Advantage | Voice NIM/SM-X and DSP for TDM; controller IP media uses NIM-PVDM/SM-X-PVDM | 17.3.2 platform minimum; per-function minima not verified | No blanket scale claim | [C8300-6T-DS-1](#c8300-6t-ds-1), Tables 7, 13; [C8300-6T-OG-1](#c8300-6t-og-1), Table 9; [C8300-6T-FAQ-1](#c8300-6t-faq-1), Collaboration |
| On-box CME | **Conflicting evidence**: data sheet lists CUCME; family FAQ explicitly says no on-box CME | Autonomous claim conflicting; controller support not established | DNA Advantage category in family matrix does not establish chassis support | — | Not verified | Do not select CME for a new deployment without Cisco confirmation | [C8300-6T-DS-1](#c8300-6t-ds-1), Table 13; [C8300-6T-FAQ-1](#c8300-6t-faq-1), on-box CME question |
| NGFW / UTD (ZBFW, Snort IPS, URL filtering, AMP) | Yes (documented in controller-mode feature table; datasheet lists on-box NGFW, IPS/IDS, AMP, URL filtering) | ZBFW and IPS/IDS both modes; AMP/URLF SD-Routing and controller | ZBFW all tiers; IPS/IDS DNA Essentials or Advantage; AMP/URLF via SD-Routing only | — | 17.3.2 | 512K firewall sessions; 2.1 Gbps DIA w/ NGFW+IPS+URLF+AMP (controller, 17.12.2) | [C8300-6T-DS-1](#c8300-6t-ds-1), Tables 1, 4, 6, 14; [C8300-6T-MX-1](#c8300-6t-mx-1) |
| PoE | Yes, via modules only | Both | Not license-gated in sources checked | C-NIM-1M, C-NIM-8M, NIM-ES2-8-P, C-SM-16P4M2X + PoE PSU (PWR-CC1-500WAC) | C-NIM-8M 17.12.2; C-NIM-1M 17.6.1 | 250 W PoE budget (500WAC); C-SM-16P4M2X: 4 UPOE (250 W) / 8 UPOE (500 W boost) | [C8300-6T-DS-1](#c8300-6t-ds-1), Tables 1, 7, 9; [C8300-6T-SMSW-1](#c8300-6t-smsw-1) |
| Routing scale | Yes | Autonomous | — | DRAM upgrade raises scale | 17.3.2 | 1.6M IPv4 / 1.5M IPv6 routes (8 GB), 4M (32 GB); BGP, OSPF, EIGRP, IS-IS, RIP | [C8300-6T-DS-1](#c8300-6t-ds-1), Tables 6, 13 |
| Segmentation: VRF-Lite | Yes | Both | All three tiers (VRF-Lite, Multi-VRF, EVN) | — | 17.3.2 | 4000 VRFs | [C8300-6T-DS-1](#c8300-6t-ds-1), Table 6; [C8300-6T-MX-1](#c8300-6t-mx-1) |
| Segmentation: SGT | Yes (family-level) | Both | Network Advantage | — | not stated | see ISE table | [C8300-6T-GBP-1](#c8300-6t-gbp-1) |
| MPLS, L2/L3 VPN, LISP | Yes | Autonomous | DNA Advantage ("Advanced MPLS and VRF support"; LISP under "Cisco innovation") | — | 17.3.2 | — | [C8300-6T-DS-1](#c8300-6t-ds-1), Table 13 |
| Multicast Service Reflection | Yes (product-family release-note support) | Autonomous CLI configuration documented; controller mode not established | Network Advantage indicated by Cisco MSR tech note; verify exact entitlement for this PID | Vif interface and PIM infrastructure | Unicast-to-multicast support introduced 17.9.1a; selected release later | IOS XE 17.x documents `ip service reflect`; family-level support; exact-PID test not found | [C8300-6T-MSR-REL-1](#c8300-6t-msr-rel-1); [C8300-6T-MSR-1](#c8300-6t-msr-1); [C8300-6T-MSR-LIC-1](#c8300-6t-msr-lic-1) |

No feature in the matrix was found deprecated at 17.15.6. In 26.2.x the UTD
signature workflow changes (V2 engine) ([C8300-6T-RN-2](#c8300-6t-rn-2)).

### Cisco ISE integration (router side)

| Integration | Supported | Mode | License / tier | Module / hardware | Min release | Limits | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RADIUS device administration (AAA) | Yes | Both | not verified | — | 17.3.2 | — | [C8300-6T-DS-1](#c8300-6t-ds-1), Table 13 ("RADIUS, Authentication, Authorization, and Accounting (AAA)") |
| TACACS+ device administration | Yes, **inferred for this PID**: Cisco's "Security and VPN Configuration Guide, Cisco IOS XE 17.x", chapter "Configuring TACACS", documents TACACS+ via AAA (for example `aaa group server tacacs ...`, `aaa authentication login default group tacacs+ local`); the chapter lists no platforms and refers to Cisco Feature Navigator, but names the Catalyst 8500 Edge Platforms in a note, so it covers the Catalyst 8000 Edge family's IOS XE 17.x. No Catalyst 8300-specific statement was found. | Both (not verified for controller mode) | All three tiers ("802.1X/AAA support": TACACS/TACACS+), family-level | — | not stated | — | [C8300-6T-SEC-1](#c8300-6t-sec-1); [C8300-6T-MX-1](#c8300-6t-mx-1) |
| SGT classification, SXP, inline tagging, SGACL | Yes, **inferred for this PID**: Cisco's Tier 1 "Catalyst 8000 series routers" row lists IP-to-SGT, subnet-to-SGT, L3IF-to-SGT; SXP speaker/listener V4 (V5 from 17.9.1); SGT over Ethernet, GETVPN, DMVPN, IPsec; SGACL, SG firewall, SGT-based PBR/QoS, SGT caching. The row names C8300-2N2S-6T, not C8300-1N1S-6T; the scale table covers "C8300" generically. | Both | Network Advantage | — | not stated | C8300 family: 1800 unidirectional / 900 bidirectional SXP connections; 750,000 IP-SGT bindings (both modes) | [C8300-6T-GBP-1](#c8300-6t-gbp-1), Tables 1 and 8 |
| Inline SGT propagation (SD-WAN) | Yes | Controller | DNA subscription | — | not stated | — | [C8300-6T-DS-1](#c8300-6t-ds-1), Table 14 |
| 802.1X and MAB on switch ports | Yes on `C-SM-16P4M2X` copper ports (802.1X, multidomain authentication, guest VLAN, MAB); other switch NIMs **not verified** | Autonomous | not verified | C-SM-16P4M2X | not stated | — | [C8300-6T-SMSW-1](#c8300-6t-smsw-1) |
| Change of Authorization (CoA) | Chapter exists in the C8200/C8300 configuration guide (title only read) | — | — | — | — | — | [C8300-6T-SCG-1](#c8300-6t-scg-1) (TOC) |

Router vs. ISE: the router is configured with AAA/RADIUS servers, SXP peers,
and (for SGACL) receives policy from ISE; ISE holds the SGT, SGACL, and SXP
mappings. ISE licensing: the GBP matrix's ISE row lists "Advantage (for both
TrustSec and pxGrid)" ([C8300-6T-GBP-1](#c8300-6t-gbp-1), Table 1).

## Modules and expansion

Coverage: module lists were taken from the datasheet Table 7 and ordering guide
Table 5 (both apply to all four C8300 models), plus module datasheets. The
lists are not claimed complete. "Supported on chassis" = listed for the
C8300 family; "at basis" = no withdrawal found and minimum release ≤ 17.15.6;
"orderable" = no EoL notice found in sources checked (not a guarantee).

### Slot map

| Slot / bay | Count | Accepts | Notes | Source |
| --- | --- | --- | --- | --- |
| Slot 0 bay 0 (built-in) | 6 ports | GE 0/0/0–0/0/3 RJ-45; GE 0/0/4–0/0/5 SFP (1G) | — | [C8300-6T-HIG-1](#c8300-6t-hig-1) |
| NIM slot | 1 | Single NIM (incl. C-NIM-4X, the only slot type it accepts) | Online insertion only for NIMs in a NIM slot | [C8300-6T-OG-1](#c8300-6t-og-1), Table 4; [C8300-6T-WANMOD-1](#c8300-6t-wanmod-1) |
| SM slot | 1 (single-wide) | SM-X single-wide modules, C-SM-16P4M2X, UCS-E160S-M3, or C-SM-NIM-ADPT (2 NIMs → 3 NIMs total) | Double-wide modules are **not supported** on 1RU (C-SM-40P8M2X, SM-X-72FXS per OG footnote; UCS-E D models **inferred** not to fit) | [C8300-6T-OG-1](#c8300-6t-og-1), Tables 4–5 |
| PIM slot | 1 | Cellular (LTE/5G) pluggables: **available, not assessed** | Out of scope | [C8300-6T-OG-1](#c8300-6t-og-1), Table 4 |
| M.2 storage | 1 | M.2 USB or NVMe | External slot | [C8300-6T-HIG-1](#c8300-6t-hig-1), p. 10 |
| DIMM | 1 | 8/16/32 GB DDR4 | Internal | [C8300-6T-OG-1](#c8300-6t-og-1), p. 7 |
| PSU bays | 2 | 250WAC (default), 500WAC (PoE), 400WDC, 400WHV | Hot-swap | [C8300-6T-DS-1](#c8300-6t-ds-1), Table 9 |
| Fan tray | 1 | C8300-FAN-1R | Ships by default | [C8300-6T-DS-1](#c8300-6t-ds-1), Table 8 |

### 10G and Ethernet expansion

| PID | Description | Capability added | Slot | Min release / mode | Dependency | Placement limits | On chassis | At basis | Orderable | Source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C-NIM-1X | 1-port 10G/1G SFP+ WAN NIM, 256-bit MACsec | 1×10G L3 WAN | NIM slot, or in C-SM-NIM-ADPT | 17.3.2; SD-WAN supported | — | Catalyst 8300 only (not ISR4000) | Yes | Yes | Yes (no EoL found) | [C8300-6T-WANMOD-1](#c8300-6t-wanmod-1); [C8300-6T-OG-1](#c8300-6t-og-1), Table 5 |
| C-NIM-4X | 4-port 1G/10G SFP/SFP+ LAN/WAN NIM, MACsec, optional L3 on two highest ports | Up to 4×10G (10G backplane, 4:1 oversubscribed) | Embedded NIM slot only | 17.11.1; SD-WAN 20.11 | — | One LAN/WAN module per chassis; not in C-SM-NIM-ADPT; not on C8200 | Yes | Yes | Yes (no EoL found) | [C8300-6T-LANMOD-1](#c8300-6t-lanmod-1) |
| C-SM-16P4M2X | 22-port L2 switch SM (16×1G RJ-45, 4×2.5G mGig, 2×10G SFP+ uplinks), UADP, PoE/PoE+/UPOE | 2×10G (L2), switch ports, PoE | SM slot (single-wide; 1RU supported) | not stated ("supported by default") | PoE PSU for PoE | — | Yes | not verified | not verified | [C8300-6T-SMSW-1](#c8300-6t-smsw-1); [C8300-6T-DS-1](#c8300-6t-ds-1), p. 11 |
| C-NIM-2T | 2-port 100M/1G combo RJ-45/SFP WAN NIM, MACsec | 2×1G L3 | NIM slot or adapter | 17.6.1 | — | — | Yes | Yes | Yes (no EoL found) | [C8300-6T-WANMOD-1](#c8300-6t-wanmod-1) |
| C-NIM-1M | 1-port 2.5G/1G RJ-45 WAN NIM, 90 W UPOE+ | 1×2.5G L3 + PoE | NIM slot or adapter | 17.6.1 | PoE PSU | — | Yes | Yes | Yes (no EoL found) | [C8300-6T-WANMOD-1](#c8300-6t-wanmod-1) |
| C-NIM-8T | 8-port 10M/100M/1G LAN/WAN NIM, MACsec | 8×1G switch ports (2 L3-capable) | Embedded NIM slot only | 17.11.1 | — | One LAN/WAN module per chassis | Yes | Yes | Yes (no EoL found) | [C8300-6T-LANMOD-1](#c8300-6t-lanmod-1) |
| C-NIM-8M | 8-port 100M/1G/2.5G LAN/WAN NIM, UPOE+ on 4 ports (up to 360 W) | mGig + PoE | Embedded NIM slot only | 17.12.2 | PoE PSU (platform rule) | One LAN/WAN module per chassis | Yes | Yes | Yes (no EoL found) | [C8300-6T-LANMOD-1](#c8300-6t-lanmod-1) |
| NIM-ES2-4 / -8 / -8-P | 4/8-port GbE switch NIM (-P with PoE) | L2 switch ports | NIM slot | not stated | PoE PSU for -P | — | Yes | not verified | **No**: -8/-8-P End-of-Sale 2025-03-05; -4 End-of-Sale 2025-04-17 | [C8300-6T-DS-1](#c8300-6t-ds-1), Table 7; [C8300-6T-EOL-2](#c8300-6t-eol-2), [C8300-6T-EOL-3](#c8300-6t-eol-3) |
| C-SM-NIM-ADPT | Single-wide SM-X carrier for 2 NIMs | 2 more NIM bays | SM slot | 17.3.2 | — | Full OIR for NIMs inside it; C-NIM-4X/8T/8M not supported in it | Yes | Yes | Yes (no EoL found) | [C8300-6T-WANMOD-1](#c8300-6t-wanmod-1); [C8300-6T-LANMOD-1](#c8300-6t-lanmod-1) |

**Inferred maximum 10G ports:** C-NIM-4X in the NIM slot (4×10G) plus either
C-SM-16P4M2X (2×10G L2 uplinks) or C-SM-NIM-ADPT with two C-NIM-1X (2×10G
L3). Each placement is documented; the combination was not tested.

### Other module families

| Family | PIDs (from Cisco lists) | Notes | Source |
| --- | --- | --- | --- |
| Voice NIMs | NIM-2FXO, NIM-4FXO, NIM-2FXSP, NIM-4FXSP, NIM-2FXSP/4FXOP, NIM-4E/M, NIM-2BRI-NT/TE, NIM-4BRI-NT/TE, NIM-1/2/4/8MFT-T1/E1, NIM-1/2/8CE1T1-PRI | Need DNA Advantage (Network Advantage) | [C8300-6T-DS-1](#c8300-6t-ds-1), Table 7; [C8300-6T-OG-1](#c8300-6t-og-1), Tables 5, 9 |
| DSP | NIM-PVDM-32/64/128/256; SM-X-PVDM-500/1000/2000/3000 | — | Same |
| Voice SM-X | SM-X-8FXS/12FXO, SM-X-16FXS/2FXO, SM-X-24FXS/4FXO (single-wide); SM-X-72FXS (double-wide, **2RU only**) | — | Same |
| Compute (UCS-E) | UCS-E160S-M3/K9 (single-wide, 6-core); UCS-E180D-M3, UCS-E1120D-M3, UCS-E1100D-M6 (double-wide) | Double-wide models **inferred** not to fit the single SM slot of the 1RU chassis | [C8300-6T-DS-1](#c8300-6t-ds-1), Table 7 |
| Serial / async / DSL / ISDN | NIM-1T/2T/4T, NIM-16A/24A, NIM-VAB-A, NIM-VA-B, NIM-VAB-M, NIM-4SHDSL-EA, NIM-2/4BRI-S/T, SM-X-1T3/E3, SM-X-64A (OG only) | — | [C8300-6T-DS-1](#c8300-6t-ds-1), Table 7; [C8300-6T-OG-1](#c8300-6t-og-1), Table 5 |
| Cellular (PIM/NIM) | Available, not assessed | Out of scope | — |

Per-PID minimum release, withdrawal status, and current orderability for this
table remain **not verified** where no exact evidence is given; listing a PID
is not an orderability finding. The separate Ethernet table identifies the
NIM-ES2 End-of-Sale dates, so those legacy modules are excluded from this
new-purchase design ([C8300-6T-EOL-2](#c8300-6t-eol-2),
[C8300-6T-EOL-3](#c8300-6t-eol-3)).

### Power supplies, memory, storage, and fans

| PID | Description | Notes | Source |
| --- | --- | --- | --- |
| PWR-CC1-250WAC | 250 W AC (default, ×2) | 12 V 21 A; 80 Plus Silver | [C8300-6T-OG-1](#c8300-6t-og-1), Table 6; [C8300-6T-DS-1](#c8300-6t-ds-1), Table 9 |
| PWR-CC1-500WAC | 500 W AC with PoE, PoE budget 250 W | **End-of-Sale 2027-01-31, no migration product** | [C8300-6T-DS-1](#c8300-6t-ds-1), Table 9; [C8300-6T-EOL-1](#c8300-6t-eol-1) |
| PWR-CC1-400WDC | 400 W DC (−40 to −72 V) | Terminal block | Same |
| PWR-CC1-400WHV | 400 W HVDC (240–380 V) | Listed in DS only, not in OG Table 6 | [C8300-6T-DS-1](#c8300-6t-ds-1), Table 9 |
| PWR-CC1-400WAC | Temporary pandemic substitute for 250WAC | No longer shipped; same support as 250WAC | [C8300-6T-DS-1](#c8300-6t-ds-1), "Important notice" |
| MEM-C8300-8GB/16GB/32GB | DRAM | Default 8 GB | [C8300-6T-OG-1](#c8300-6t-og-1), Table 3 |
| M2USB-16G/32G, SSD-M2NVME-600G, SSD-M2SED-600G, SSD-M2NVME-2T | Storage | OG and DS differ in the 600 GB PID naming; both listed | [C8300-6T-OG-1](#c8300-6t-og-1), Table 3; [C8300-6T-DS-1](#c8300-6t-ds-1), Table 8 |
| C8300-FAN-1R | 1RU fan tray | Default | [C8300-6T-DS-1](#c8300-6t-ds-1), Table 8 |

### Optics

Non-exhaustive. Built-in port results come from a TMG export filtered to
`C8300-1N1S-6T` (13 records) ([C8300-6T-TMG-2](#c8300-6t-tmg-2)). Module-port
results come from a TMG export of C-NIM-1X, C-NIM-2T, and C-NIM-4X rows
(module-level, not host-filtered) ([C8300-6T-TMG-1](#c8300-6t-tmg-1)),
cross-checked with the module datasheet
([C8300-6T-WANMOD-1](#c8300-6t-wanmod-1)).

**Port inventory**

| Port type | Speeds | Form factor | Restrictions / notes | Source |
| --- | --- | --- | --- | --- |
| Built-in GE 0/0/0–0/0/3 | 10/100/1000 | RJ-45 | — | [C8300-6T-HIG-1](#c8300-6t-hig-1), p. 9 |
| Built-in GE 0/0/4–0/0/5 | 1 Gbps | SFP | "support 1Gbps SFP modules"; no 10G; TMG lists 13 optics, all 1G, from 17.3.2 ([C8300-6T-TMG-2](#c8300-6t-tmg-2)) | [C8300-6T-HIG-1](#c8300-6t-hig-1), p. 9 |
| C-NIM-1X | 1G / 10G | SFP+ | Datasheet (2021): no RJ-45 copper SFP and no 10/100 SFP; TMG lists SFP-10G-T-X from 17.6.1 (conflict below) | [C8300-6T-WANMOD-1](#c8300-6t-wanmod-1); [C8300-6T-TMG-1](#c8300-6t-tmg-1) |
| C-NIM-4X | 100M / 1G / 10G | SFP/SFP+ | 4:1 oversubscribed to 10G backplane | [C8300-6T-LANMOD-1](#c8300-6t-lanmod-1) |
| C-NIM-2T | 100M / 1G | RJ-45/SFP combo (one active per group) | — | [C8300-6T-WANMOD-1](#c8300-6t-wanmod-1) |
| C-SM-16P4M2X uplinks | 1G / 10G | SFP+ | Optics not listed in datasheet | [C8300-6T-SMSW-1](#c8300-6t-smsw-1) |

**Minimum set** (TMG rows: built-in column from [C8300-6T-TMG-2](#c8300-6t-tmg-2), module columns from [C8300-6T-TMG-1](#c8300-6t-tmg-1); "—" = not listed; DOM as TMG shows). The built-in ports also list BiDi optics (GLC-BX-D/U, GLC-BX40-D-I/U-I/DA-I, GLC-BX80-D-I/U-I), not reviewed here.

| Item | Built-in SFP 0/0/4–5 | C-NIM-1X | C-NIM-4X | C-NIM-2T | Reach / media |
| --- | --- | --- | --- | --- | --- |
| 1000BASE-SX | GLC-SX-MMD (17.3.2, DOM 17.3.2) | GLC-SX-MMD (17.3.2, DOM) | GLC-SX-MMD (17.11.1, DOM) | GLC-SX-MMD (17.6.1) | 1000 m OM3/OM4, MMF |
| 1000BASE-LX/LH | GLC-LH-SMD; GLC-LX-SM-RGD (17.3.2, DOM 17.3.2) | GLC-LH-SMD (17.3.2, DOM) | GLC-LH-SMD (17.11.1, DOM) | GLC-LH-SMD (17.6.1) | 10 km SMF |
| 1000BASE-ZX | GLC-ZX-SMD (17.3.2, DOM 17.3.2); also GLC-EX-SMD 40 km | GLC-ZX-SMD (17.3.2, DOM) | GLC-ZX-SMD (17.11.1, DOM) | GLC-ZX-SMD (17.6.1) | 70 km SMF (TMG) |
| 1000BASE-T copper SFP | GLC-TE (17.3.2; "Supports 1000BASE-T data rate only"; no DOM) | — (datasheet: not supported) | GLC-TE (**17.18.1**, 100/1000 only) | — | 100 m Cat5e/6A |
| 10GBASE-SR | n/a (1G port) | SFP-10G-SR, -SR-S (DOM) | SFP-10G-SR, -SR-S (DOM) | n/a | 400 m OM4, MMF |
| 10GBASE-LR | n/a | SFP-10G-LR, -LR-S (DOM) | SFP-10G-LR, -LR-S (DOM) | n/a | 10 km SMF |
| 10GBASE-ER | n/a | SFP-10G-ER (DOM) | SFP-10G-ER (17.11.1), SFP-10G-ER-S (**17.18.2**) | n/a | 40 km SMF |
| 10GBASE-ZR | n/a | **not verified** (not listed) | SFP-10G-ZR-I (**17.18.2**; traffic from −28 °C) | n/a | 70 km SMF |
| 10GBASE-T copper SFP+ | n/a | SFP-10G-T-X (17.6.1; 10GBASE-T only) | SFP-10G-T-X (17.11.1; 1000BASE-T and 10GBASE-T only) | n/a | 30 m Cat6A/7 (10G) |
| 10G DAC | n/a | SFP-H10GB-ACU7M, -ACU10M (active) | SFP-H10GB-ACU7M, -ACU10M (active) | n/a | 7 m / 10 m |
| 1G DAC | not listed (**not verified**) | not verified | not verified | not verified | — |

Long-reach restrictions found: SFP-10G-ZR-I requires 17.18.2 (above the
17.15.6 basis) and carries traffic only from −28 °C to 85 °C case temperature;
no power or port-position restriction was found for ZX/ER/ZR in the sources
checked ([C8300-6T-TMG-1](#c8300-6t-tmg-1)). On the built-in SFP ports,
GLC-ZX-SMD (70 km) carries no TMG note or restriction
([C8300-6T-TMG-2](#c8300-6t-tmg-2)).

**Ports faster than 10G:** none on the chassis or in any module listed for
it ([C8300-6T-DS-1](#c8300-6t-ds-1), Tables 2 and 7).

**Copper SFPs (direct answer):**

| Port type | 1G copper SFP (1000BASE-T) | 10G copper SFP+ (10GBASE-T) |
| --- | --- | --- |
| Built-in SFP ports | **Yes**: GLC-TE, from 17.3.2, 100 m on Cat5e/6A; TMG network-device note "Supports 1000BASE-T data rate only" (100 Mb/s not supported); no DOM; no count, thermal, or adjacent-port limit listed | Not applicable (1G SFP ports) |
| C-NIM-1X | **No** per datasheet ("does not support RJ-45 copper SFP modules") | **Conflict**: datasheet says no copper SFP; TMG lists SFP-10G-T-X (17.6.1, "Supports 10GBASE-T mode only", 30 m Cat6A/7) |
| C-NIM-4X | **Yes**: GLC-TE, 100M/1000M only, 100 m, from 17.18.1 (above basis) | **Yes**: SFP-10G-T-X, 1000BASE-T and 10GBASE-T only (no 100M), 30 m at 10G, from 17.11.1 |
| C-NIM-2T | Not listed (has RJ-45 combo ports instead) | n/a |

No limit on the number of copper SFP+ modules, adjacent-port rule, or thermal
limit was found in sources checked. The four built-in RJ-45 ports
(10/100/1000) meet a 1G copper need without copper SFPs
([C8300-6T-HIG-1](#c8300-6t-hig-1), p. 9). Conflict resolution for C-NIM-1X:
TMG (live data, 2026-10-30) is newer and transceiver-specific; the datasheet
was updated 2021-09-23. Prefer TMG, but treat as **unresolved** until Cisco
confirms.

**Platform policy:** Cisco documentation of `service unsupported-transceiver`
on this platform and of TAC's position on third-party optics: **not found in
sources checked**. The HIG's SFP EN LED shows amber when "The SFP is not
supported or is in a faulty state" ([C8300-6T-HIG-1](#c8300-6t-hig-1),
Table 6), so the platform detects unsupported optics. **DOM:** TMG marks the
built-in-port fiber optics (SX, LH, LX-RGD, EX, ZX, BX) as DOM capable with
DOM support from IOS XE 17.3.2; GLC-TE has no DOM
([C8300-6T-TMG-2](#c8300-6t-tmg-2)). Module-port optics are DOM capable from
the listed release ([C8300-6T-TMG-1](#c8300-6t-tmg-1)). A C8300-specific DOM
display command was not verified (see Appendix A gaps).

**Not reviewed in this research**

| Optics family | Status |
| --- | --- |
| CWDM | needed, not reviewed in this research |
| DWDM | needed, not reviewed in this research |
| BiDi | needed, not reviewed in this research |
| Extended-temperature (industrial) | needed, not reviewed in this research |

Transceiver tool: <https://tmgmatrix.cisco.com/> (search `C8300-1N1S-6T`),
accessed 2026-10-30; results non-exhaustive.

### Module reuse across the four platforms

- **ISR4431 → C8300-1N1S-6T:** Cisco says the Catalyst 8300 supports "most of
  the widely deployed" ISR 4000 NIMs and SMs; the NIM-ES2, voice, DSP, serial,
  DSL, ISDN, and SM-X modules in the lists above are shared PIDs. C-NIM-1X,
  C-SM-NIM-ADPT, C-SM-16P4M2X, and C-SM-40P8M2X are C8300-specific and "not
  compatible with Cisco 4000 Series ISRs" ([C8300-6T-OG-1](#c8300-6t-og-1),
  p. 7 and Table 5 footnote). Moving a specific owned module is out of scope
  (new purchase only).
- **C8300-1N1S-4T2X ↔ C8300-1N1S-6T:** same module tables and slot layout
  (documented for all four C8300 models) ([C8300-6T-DS-1](#c8300-6t-ds-1),
  Table 7; [C8300-6T-OG-1](#c8300-6t-og-1), Tables 4–5).
- **C8375-E-G2:** not verified from this file's sources; see that model's file.

## Platform-specific caveats

| Item | Affected | Impact | Fix / mitigation | Source |
| --- | --- | --- | --- | --- |
| EOL15950 End-of-Sale | C8300-1N1S-6T and bundles, PWR-CC1-500WAC | Orderable until 2027-01-31; support ends 2032-01-31; no PoE PSU replacement listed | Buy before 2027-01-31 or choose C8375-E-G2 | [C8300-6T-EOL-1](#c8300-6t-eol-1) |
| FN74146 (Critical, rev 2.0, 2024-12-20) | C8300-1N1S-6T and others; units in a date range | DRAM defect: correctable errors, then resets or failure to boot | Check serial with Serial Number Validation Tool; replace DIMM via upgrade program | [C8300-6T-FN-1](#c8300-6t-fn-1) |
| FN72510: IPsec weak-crypto defaults | Catalyst 8000 family, 17.11.1a and later; includes basis | Legacy DES/3DES/MD5 and weak DH configurations can fail tunnel negotiation after an upgrade | Migrate to strong algorithms before deployment; do not assume an older configuration will negotiate unchanged | [C8300-6T-FN-2](#c8300-6t-fn-2), Enterprise Routing applicability table |
| FN72578: SLP CPU/memory | Enumerated older 17.3–17.7 releases with accumulating unacknowledged RUM reports | High CPU/memory; especially relevant to disconnected license operations | Notice lists fixes 17.3.7/17.6.5/17.9.1 or later; basis 17.15.6 is above those fixes, an inference from release progression. Follow the actual reporting policy | [C8300-6T-FN-3](#c8300-6t-fn-3), Products Affected and Solution |
| FN74350: CUBE TLS EKU | Exact C8300-1N1S-6T PID listed; relevant when using public-CA CUBE mutual TLS | Changing public-CA client-authentication EKU issuance may affect certificates | Audit certificate EKUs/peer policy; notice documents private/alternate CA options and a 26.1.1 enhancement above basis. Below 26.1.1 strict EKU checks depend on match/CC-mode configuration | [C8300-6T-FN-4](#c8300-6t-fn-4), Workaround/Solution |
| FN72323: QuoVadis certificates | Older releases and cloud-facing Smart Licensing/Call Home TLS | Certificate-chain expiry can break online communication | Notice lists 17.3.4/17.4.2/17.5.1/17.6.1/17.7.1 or later fixes; basis is later (inferred). This old Smart Licensing notice does not establish SLP missed-deadline behavior | [C8300-6T-FN-5](#c8300-6t-fn-5), Products Affected and Solution |
| FN72509: SNMP weak-crypto defaults | IOS XE 17.11.1a and later, configuration dependent | Legacy MD5/DES/3DES SNMPv3 users can stop working after an upgrade | Replace with supported strong authentication/privacy algorithms before upgrading | [C8300-6T-FN-6](#c8300-6t-fn-6), Problem Description and Solution |
| FN72570: OSPFv3 IPsec weak crypto | IOS XE 17.11.1 and later, configuration dependent | Legacy weak OSPFv3 IPsec protection can prevent neighborship | Migrate the affected OSPFv3 IPsec configuration to the documented strong algorithms before upgrade | [C8300-6T-FN-7](#c8300-6t-fn-7), Problem Description and Solution |
| IOS XE August 2026 hardening | IOS XE autonomous and controller modes, regardless of configuration | Multiple critical/high vulnerability classes | First fixed 17.15 release is **17.15.6**, the basis; other advisories still require separate assessment | [C8300-6T-PSIRT-1](#c8300-6t-psirt-1), Affected Products and Fixed Software |
| Snort 3 October 2026 hardening and five related advisories | Optional vulnerable UTD engine on Catalyst 8300; installed engine/package matters | Hardening issues and MIME/NetFlow/GRE/GTP/VBA denial-of-service paths; no published workaround in these bulletins | 17.15 fixed UTD image: **secapp-utd.17.15.06.1.0.21_SV3.12.4.0_XE17.15**. Inspect actual UTD engine version; the IOS XE version alone does not prove the container was updated | [C8300-6T-PSIRT-2](#c8300-6t-psirt-2), [C8300-6T-PSIRT-3](#c8300-6t-psirt-3), [C8300-6T-PSIRT-4](#c8300-6t-psirt-4), [C8300-6T-PSIRT-5](#c8300-6t-psirt-5), [C8300-6T-PSIRT-6](#c8300-6t-psirt-6), [C8300-6T-PSIRT-7](#c8300-6t-psirt-7) |
| Optics above basis | C-NIM-4X with GLC-TE, SFP-10G-ZR-I, SFP-10G-ER-S | Need 17.18.1/17.18.2, above the 17.15.6 basis | Use 17.18.x if those optics are required | [C8300-6T-TMG-1](#c8300-6t-tmg-1) |
| LAN/WAN NIM limits | C-NIM-4X/8T/8M | One per chassis; embedded NIM slot only | Plan slot use | [C8300-6T-LANMOD-1](#c8300-6t-lanmod-1) |
| ROMMON minimum | C8300-1N1S-4T2X/6T | Below 17.3(4.2r) needs a staged upgrade | Boot 17.12.4/17.12.5 first | [C8300-6T-RN-1](#c8300-6t-rn-1) |

Review scope: the public platform lists were read, and all seven listed field
notices plus the six October 2026 Snort notices were read for applicability,
impact and remedy, together with the IOS XE August hardening bulletin.
Older advisory archives were not treated as an exhaustive assessment, and no
Software Checker result or claim that the release has no vulnerabilities is
made ([C8300-6T-FN-LIST-1](#c8300-6t-fn-list-1),
[C8300-6T-PSIRT-LIST-1](#c8300-6t-psirt-list-1)).

Applicability by serial number: FN74146 depends on chassis and DIMM serial
numbers. No serial number was checked against Cisco's validation tool.

### Differences from C8300-1N1S-4T2X

| Item | C8300-1N1S-6T | C8300-1N1S-4T2X | Source |
| --- | --- | --- | --- |
| Ports 0/0/4–0/0/5 | SFP, 1G | SFP+, 10G | [C8300-6T-HIG-1](#c8300-6t-hig-1), Table 1 |
| IPsec 1400 B (autonomous) | Up to 1.9 Gbps | Up to 16.9 Gbps | [C8300-6T-DS-1](#c8300-6t-ds-1), Table 5 |
| IPsec IMIX (autonomous) | 1.9 Gbps | 6.6 Gbps | Same |
| IPv4 forwarding 1400 B | Up to 19.7 Gbps | Up to 19.7 Gbps | Same |
| Max throughput tier | T2 (2G aggregate) | T3 (20G aggregate in ≥17.8.1a) | [C8300-6T-LIC-1](#c8300-6t-lic-1), Tables 5–6; [C8300-6T-OG-1](#c8300-6t-og-1), p. 15 |
| Controller-mode crypto with HSECK9 | 2G aggregate | Unthrottled | [C8300-6T-LIC-1](#c8300-6t-lic-1), controller table |
| Typical power (no modules) | 82 W | 245 W | [C8300-6T-DS-1](#c8300-6t-ds-1), Table 11 |
| Data-plane Hyperthreading listed | Yes | Yes | [C8300-6T-HIG-1](#c8300-6t-hig-1), pp. 1–2 |
| Crypto throughput drop syslog (17.18.1a) | Listed | Not listed | [C8300-6T-LIC-1](#c8300-6t-lic-1), p. 28 |
| Lifecycle | EOL15950, same dates | EOL15950, same dates | [C8300-6T-EOL-1](#c8300-6t-eol-1) |

## Appendix A: identification and inventory commands

All commands are read-only `show` commands at privilege level 15 (privileged
EXEC). Redact serial numbers and UDIs before sharing output.

### Annotated listing

Software identification ([C8300-6T-SCG-1](#c8300-6t-scg-1),
Software Installation; [C8300-6T-LIC-1](#c8300-6t-lic-1)):

```text
! Source group 1: C8300-6T-SCG-1 (Software Installation) and C8300-6T-LIC-1
show version
! Model, IOS XE version, license level, and (per sample output) "Router operating mode: Autonomous"
show install summary
! Install-mode package state; used to distinguish install from bundle boot
```

License state ([C8300-6T-SLP-1](#c8300-6t-slp-1), command reference;
[C8300-6T-LIC-1](#c8300-6t-lic-1)):

```text
! Source group 2: C8300-6T-SLP-1 (Command Reference) and C8300-6T-LIC-1
show license udi
! Chassis UDI (PID and serial) used for licensing
show license summary
! Licenses in use, including DNA_HSEC (HSECK9)
show license status
! Transport, policy, "Next ACK deadline" and reporting status
show license usage
! Per-license usage and enforcement type
show license authorization
! SLAC status ("SMART AUTHORIZATION INSTALLED") for HSECK9
show license all
! All licensing data, including the policy in use
show license tech support
! Licensing troubleshooting bundle (sample output exists for Catalyst 8300)
```

Throughput ([C8300-6T-LIC-1](#c8300-6t-lic-1), throughput verification):

```text
! Source group 3: C8300-6T-LIC-1 (Throughput)
show platform hardware throughput crypto
! Configured and enforced crypto throughput level, boot level
show platform hardware throughput level
! Configured throughput level
```

Modules and operational status ([C8300-6T-SCG-1](#c8300-6t-scg-1),
slot/subslot chapters and Notification Management Table 15, PDF pp. 190–191):

```text
! Source group 4: C8300-6T-SCG-1 (Slot and subslot configuration; modules)
show hw-module subslot all oir
! Module presence and operational state per subslot
show facility-alarm status
! Active alarms (for example module removal)
show platform software status control-process brief
! Processor, memory, and CPU utilization for platform components
show interfaces summary
! Interface states and counters
show ip interface brief
! Interface IP and status summary
show inventory
! PID/VID/serial inventory; documented in the platform guide Call Home capture commands
show platform
! Chassis and module platform state; documented in the same capture table
show environment
! Environmental status for temperature, fan, and power sensing; same platform table
```

Optional UTD inspection ([C8300-6T-PSIRT-3](#c8300-6t-psirt-3),
Determine Whether UTD Is Enabled):

```text
show utd engine standard status
! Whether the optional UTD engine is running and its installed engine version
```

Gaps (omitted from the capture block): standalone `show power`,
`show interfaces transceiver`, and exact DOM light-level/temperature syntax
were not verified for this PID at the basis. `show environment` supplies the
documented platform environmental capture path; no lab output or DOM syntax
is invented. The general inventory command does not establish that every
optic exports every inventory or DOM field.

### Paste-ready capture block

```text
terminal length 0
show version
show install summary
show license udi
show license summary
show license status
show license usage
show license authorization
show license all
show license tech support
show platform hardware throughput crypto
show platform hardware throughput level
show hw-module subslot all oir
show facility-alarm status
show platform software status control-process brief
show interfaces summary
show ip interface brief
show inventory
show platform
show environment
show utd engine standard status
```

## References

#### C8300-6T-MSR-1

- Title: IP Multicast Configuration Guide, Cisco IOS XE, “Implementing Multicast Service Reflection”
- Used for: MSR configuration, prerequisites, Vif restrictions, unicast-to-multicast behavior, and feature introduction information
- URL: https://www.cisco.com/c/en/us/td/docs/routers/ios-xe/ip-multicast/ip-multicast/m_imc_service_reflect-0.html
- Accessed: 2026-11-01
- Locator: Implementing Multicast Service Reflection; Feature Information for Multicast Service Reflection
- Local PDF: not saved (HTML)

#### C8300-6T-MSR-REL-1

- Title: Release Notes for Cisco Catalyst 8200 and Catalyst 8300 Series Edge Platforms, Cisco IOS XE Cupertino 17.9.x
- Used for: family/release-level evidence for Unicast-to-Multicast Destination Reflection
- URL: https://www.cisco.com/c/en/us/td/docs/routers/cloud_edge/c8300/rel_notes/17_9_x/cat8200-and-8300-rel-notes-xe-17-9-x.html
- Accessed: 2026-11-01
- Locator: New and Changed Information; feature entry for IOS XE 17.9.1a
- Local PDF: not saved (HTML)

#### C8300-6T-MSR-LIC-1

- Title: Configure and Troubleshoot Multicast Service Reflection on Catalyst 8000
- Used for: Network Advantage licensing indication only; Cisco's example is a Catalyst 8500 running IOS XE 17.9.4, not this PID
- URL: https://www.cisco.com/c/en/us/support/docs/ip/protocol-independent-multicast-sparse-mode-pim-sm/221125-configure-and-troubleshoot-multicast-ser.html
- Accessed: 2026-11-01
- Locator: Requirements and lab configuration
- Local PDF: not saved (HTML)

Each entry: title; used for; URL; revision; accessed; locator; local PDF.

#### C8300-6T-DS-1

- Title: Cisco Catalyst 8300 Series Edge Platforms Data Sheet.
- Used for: identity, ports, slots, performance, scale, power, mechanical,
  modules, minimum software, licensing tiers listed.
- URL:
  <https://www.cisco.com/c/en/us/products/collateral/routers/catalyst-8300-series-edge-platforms/datasheet-c78-744088.html>
  (PDF: `.../datasheet-c78-744088.pdf`).
- Revision: C78-744088-09, 10/26 (page "Updated: October 6, 2026").
- Accessed: 2026-10-30. Locators: Tables 1–16 as cited.
- Local PDF (reused; identical SHA-256 to this run's download):
  [reference/c8300-edge-datasheet-2026-10-06.pdf](reference/c8300-edge-datasheet-2026-10-06.pdf)

#### C8300-6T-OG-1

- Title: Cisco Catalyst 8300/8200 Series Edge Platforms Ordering Guide.
- Used for: identity, slots, PSUs, accessories, HSEC PIDs, UC licensing,
  Routing Essentials, tier note, warranty, modes.
- URL:
  <https://www.cisco.com/c/en/us/products/collateral/routers/catalyst-8300-series-edge-platforms/cat-8300-8200-series-edge-plat-og.pdf>
- Revision: C07-744100-11, 06/26.
- Accessed: 2026-10-30. Locators: Tables 1–12, pages as cited.
- Local PDF (reused; identical SHA-256 to this run's download):
  [reference/c8300-c8200-edge-og-2026-06-17.pdf](reference/c8300-c8200-edge-og-2026-06-17.pdf)

#### C8300-6T-HIG-1

- Title: Hardware Installation Guide for Cisco Catalyst 8300 Series Edge
  Platforms, chapter "Overview".
- Used for: identity, port layout, port media, memory, PSU options, LEDs,
  Hyperthreading platform list, slot numbering.
- URL (HTML):
  <https://www.cisco.com/c/en/us/td/docs/routers/cloud_edge/c8300/hardware_installation/b-catalyst-8300-series-edge-platforms-hig/m-overview.html>
- Revision: PDF chapter generated 2026-06-15 (PDF metadata); HTML page shows
  "Updated: October 28, 2020".
- Accessed: 2026-10-30. Locators: pp. 1–14, Tables 1–7.
- Local PDF (reused, pre-existing):
  [reference/c8300-edge-hig-overview-2026-06.pdf](reference/c8300-edge-hig-overview-2026-06.pdf)

#### C8300-6T-EOL-1

- Title: End-of-Sale and End-of-Life Announcement for the Cisco Catalyst
  C8500L-8S4X, C8300-1N1S-4T2X, C8300-1N1S-6T (EOL15950, Amended).
- Used for: lifecycle milestones, last IOS XE train, replacement, affected
  bundles and PSUs.
- URL:
  <https://www.cisco.com/c/en/us/products/collateral/networking/sdwan-routers/catalyst-8000-edge-platforms/catalyst-c8500l-8s4x-4t2x-c8300-1n1s-6t-eol.html>
- Revision: announced 2026-07-27; updated 2026-10-19.
- Accessed: 2026-10-30. Locators: Tables 1–2, pp. 3–6.
- Local PDF (reused, saved by another subagent):
  [reference/c8300-1n1s-eol15950-2026-10-19.pdf](reference/c8300-1n1s-eol15950-2026-10-19.pdf)

#### C8300-6T-SUP-1

- Title: Cisco Catalyst 8300 Series Edge Platforms support page.
- Used for: series status "Available", release date 2020-10-19, notice lists,
  field-notice and advisory titles, document links.
- URL:
  <https://www.cisco.com/c/en/us/support/routers/catalyst-8300-series-edge-platforms/series.html>
- Revision: live page. Accessed: 2026-10-30.

#### C8300-6T-RR-1

- Title: Choose Stable Cisco IOS XE Release for Enterprise Routing Platforms
  (Document ID 215567).
- Used for: recommended release 17.12.8 or 17.15.6.
- URL:
  <https://www.cisco.com/c/en/us/support/docs/ios-nx-os-software/ios-xe-16/215567-recommended-releases-for-asr1000-isr400.html>
- Revision: 9.0, 2026-06-15. Accessed: 2026-10-30. Locator: "Catalyst 8300"
  row.

#### C8300-6T-RN-1

- Title: Release Notes for Cisco Catalyst 8200 and 8300 Series Edge
  Platforms, Cisco IOS XE 17.15.x.
- Used for: 17.15.6 listed; supported hardware; ROMMON table.
- URL:
  <https://www.cisco.com/c/en/us/td/docs/routers/cloud_edge/c8300/rel_notes/17-15-x/cat8200-and-8300-rel-notes-xe-17-15-x.html>
- Revision: first published 2024-08-27; last updated 2026-08-05.
- Accessed: 2026-10-30.

#### C8300-6T-RN-2

- Title: Release Notes for Cisco Catalyst 8200 and 8300 Series Edge
  Platforms, Release 26.2.x.
- Used for: newest release 26.2.1; ROMMON; UTD engine change.
- URL:
  <https://www.cisco.com/c/en/us/td/docs/routers/cloud_edge/c8300/rel_notes/26-x/release-notes-catalyst-8200-and-catalyst-8300-series-edge-platforms-release-26-2-x.html>
- Revision: updated 2026-09-27. Accessed: 2026-10-30.

#### C8300-6T-LIC-1

- Title: Configure Licenses and Throughput for Catalyst 8000 Series Physical
  Platforms.
- Used for: license stacks, HSECK9, throughput tables, commands, MSLA.
- URL:
  <https://www.cisco.com/c/en/us/td/docs/routers/cloud_edge/configure-licenses-throughput-catalyst-8000-platforms.html>
- Revision: PDF "Revised: May 4, 2026" (HTML page showed 2024-10-29 when read
  through a summarizer; the PDF is used).
- Accessed: 2026-10-30. Locators: Tables 1–6, controller-mode table, pp. 3–28.
- Local PDF (reused, saved by another subagent):
  [reference/c8000-edge-licenses-throughput-2026-05-04.pdf](reference/c8000-edge-licenses-throughput-2026-05-04.pdf)

#### C8300-6T-SLP-1

- Title: Smart Licensing Using Policy for Cisco Enterprise Routing Platforms.
- Used for: supported products, policy defaults, offline and On-Prem
  workflows, commands.
- URL:
  <https://www.cisco.com/c/en/us/td/docs/routers/sl_using_policy/b-sl-using-policy/info_about.html>
  (and `how_to_configure_workflows.html`, `cmd_ref.html`).
- Revision: last modified 2023-08-01.
- Accessed: 2026-10-30. Locators: pp. 2, 6–7 (Table 4), 45–46; command
  reference chapter.
- Local PDF (reused, saved by another subagent):
  [reference/enterprise-routing-slp-guide-2023-08-01.pdf](reference/enterprise-routing-slp-guide-2023-08-01.pdf)

#### C8300-6T-SLP-2

- Title: Troubleshooting Smart Licensing Using Policy.
- Used for: reporting syslog messages; effect of removing an authorization
  code.
- URL:
  <https://www.cisco.com/c/en/us/td/docs/routers/sl_using_policy/b-sl-using-policy/troubleshooting.html>
- Revision: updated 2023-08-01. Accessed: 2026-10-30.

#### C8300-6T-ONP-1

- Title: Cisco Smart Software Manager On-Prem data sheet.
- Used for: manual synchronization at least once a year; ISO; no charge.
- URL:
  <https://www.cisco.com/c/en/us/products/collateral/cloud-systems-management/smart-software-manager-satellite/datasheet-c78-734539.html>
- Revision: updated 2026-07-08. Accessed: 2026-10-30.

#### C8300-6T-DNA-1

- Title: Cisco DNA Software for SD-WAN and Routing Ordering Guide.
- Used for: subscription terms, perpetual element, stack consumption by mode,
  generic tier sizes, HSEC inclusion.
- URL:
  <https://www.cisco.com/c/en/us/products/collateral/software/dna-subscription-routing/guide-c07-740642.html>
- Revision: updated 2026-06-17. Accessed: 2026-10-30. Locators: Step 3,
  Tables 6 and 9, Appendix D.

#### C8300-6T-WANMOD-1

- Title: Cisco Catalyst 8000 Gigabit Ethernet WAN Modules Data Sheet.
- Used for: C-NIM-1X, C-NIM-2T, C-NIM-1M, C-SM-NIM-ADPT specs, hosts,
  minimum releases, transceiver table.
- URL:
  <https://www.cisco.com/c/en/us/products/collateral/routers/catalyst-8300-series-edge-platforms/catalyst-8000-gigabit-ethernet-wan-modules-ds.html>
- Revision: updated 2021-09-23. Accessed: 2026-10-30. Locators: Tables 2, 5.

#### C8300-6T-LANMOD-1

- Title: Cisco Catalyst 8000 Series Gigabit Ethernet LAN/WAN Modules Data
  Sheet.
- Used for: C-NIM-4X/8T/8M specs, limits, releases, PoE.
- URL:
  <https://www.cisco.com/c/en/us/products/collateral/routers/catalyst-8300-series-edge-platforms/catalyst-8000-series-gigabit-ethernet-lan-wan-modules-ds.html>
- Revision: updated 2024-02-07. Accessed: 2026-10-30. Locators: Tables 1, 4, 8.

#### C8300-6T-SMSW-1

- Title: Cisco Catalyst 8000 SM-Based Switching Modules Data Sheet.
- Used for: C-SM-16P4M2X ports, PoE port counts on C8300-1N1S-6T, 802.1X/MAB,
  TrustSec, MACsec.
- URL:
  <https://www.cisco.com/c/en/us/products/collateral/routers/catalyst-8300-series-edge-platforms/catalyst-8000-sm-switch-module-ds.html>
- Revision: updated 2024-06-17. Accessed: 2026-10-30. Locators: Tables 2–5.

#### C8300-6T-TMG-1

- Title: Cisco Optics-to-Device Compatibility Matrix results (product family
  C8300; rows for C-NIM-1X, C-NIM-2T, C-NIM-4X).
- Used for: module-port optics minimum set, copper SFP answers, DOM, minimum
  releases.
- URL: <https://tmgmatrix.cisco.com/> (module filters).
- Revision: live data exported 2026-10-30. Non-exhaustive; module-level, not
  filtered to this host PID.
- Accessed: 2026-10-30.
- Local PDF (reused, saved by another subagent):
  [reference/c8300-nim-1x-4x-2t-tmg-optics-2026-10-30.pdf](reference/c8300-nim-1x-4x-2t-tmg-optics-2026-10-30.pdf)

#### C8300-6T-TMG-2

- Title: Cisco Optics-to-Device Compatibility Matrix results, network device
  `C8300-1N1S-6T` (product family C8300; 13 records).
- Used for: built-in SFP port optics minimum set, copper SFP answer
  (`GLC-TE` note), DOM, minimum releases.
- URL: <https://tmgmatrix.cisco.com/> (search text `C8300-1N1S-6T`). Retrieved
  through the site's public endpoints `POST /public/api/networkdevice/search`
  and `POST /public/api/networkdevice/search/export/pdf` with the app's own
  filter body (`searchInput: ["C8300-1N1S-6T"]`, all other filters empty,
  page 1, 100 per page), the same method the other agents used. No custom
  headers beyond `Content-Type: application/json`.
- Revision: live data, exported 2026-10-30. Non-exhaustive.
- Accessed: 2026-10-30.
- Local PDF (saved in this run):
  [reference/c8300-1n1s-6t-tmg-optics-2026-10-30.pdf](reference/c8300-1n1s-6t-tmg-optics-2026-10-30.pdf)

#### C8300-6T-SEC-1

- Title: Security and VPN Configuration Guide, Cisco IOS XE 17.x, chapter
  "Configuring TACACS".
- Used for: TACACS+ via AAA on IOS XE 17.x (example commands); no platform
  list (refers to Cisco Feature Navigator); a note names the Catalyst 8500
  Edge Platforms.
- URL:
  <https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/sec_usr_tacacs/configuration/xe-17/sec-usr-tacacs-xe-17-book.html>
- Revision: updated 2021-01-11. Accessed: 2026-10-30 (read through a
  summarizing fetch tool; some command names were missing from the
  extracted text).

#### C8300-6T-MX-1

- Title: Cisco DNA Software SD-WAN and Routing Matrices.
- Used for: per-category tier map for autonomous mode (Catalyst Routing
  Essentials / DNA Essentials / DNA Advantage), the feature list behind each
  category, footnotes 1 and 3, and the TACACS+ entitlement. Names no
  platforms. The tier ticks are images; they were read from the page code
  and the category lists from the page's tooltips, with a headless browser
  (Playwright Chromium), 2026-10-30.
- URL:
  <https://www.cisco.com/c/m/en_us/products/software/sd-wan-routing-matrix.html>
  (PDF:
  <https://www.cisco.com/c/dam/m/en_us/products/software/dna-software/dna-software-sd-wan-routing-matrix/pdf/Cisco_DNA_Software_SD-WAN_and_Routing_Matrices.pdf>)
- Revision: PDF modified 2025-05-02. Accessed: 2026-10-30.
- Local copies:
  [reference/dna-sd-wan-routing-matrices-2025-05-02.pdf](reference/dna-sd-wan-routing-matrices-2025-05-02.pdf);
  [reference/dna-routing-matrix-tiers-2026-10-30.txt](reference/dna-routing-matrix-tiers-2026-10-30.txt)
  (derived text of ticks and category lists).

#### C8300-6T-SDWAN-1

- Title: Cisco Recommended Catalyst SD-WAN Software Versions for Controllers
  and WAN Edge Routers (Document ID 215676).
- Used for: recommended cEdge (17.12.8, 17.15.6) and control-component
  (20.12.8.1, 20.15.6) releases.
- URL:
  <https://www.cisco.com/c/en/us/support/docs/routers/sd-wan/215676-cisco-tac-and-bu-recommended-sd-wan-soft.html>
- Revision: 21.0, 2026-08-19. Accessed: 2026-10-30. Locator: recommended
  release table (read through a summarizing fetch tool; columns matched by
  order).

#### C8300-6T-SCG-1

- Title: Cisco Catalyst 8200 and 8300 Series Edge Platforms Software
  Configuration Guide (chapters "Software Installation", "Slot and subslot
  configuration", "Cisco Service module and network interface modules", and
  the table of contents).
- Used for: install mode default, mode line in `show version`, show
  commands, OIR behavior, CoA chapter title.
- URL:
  <https://www.cisco.com/c/en/us/td/docs/routers/cloud_edge/c8300/software_config/cat8300-edge-software-config.html>
- Revision: updated 2026-05-04. Accessed: 2026-10-30; saved PDF re-read 2026-10-31 UTC. Additional locators: Overview PDF pp. 7–8 (mode conversion) and Notification Management Table 15, PDF pp. 190–191 (inventory, platform, environmental commands).

#### C8300-6T-FN-1

- Title: Field Notice FN74146, Limited Number of Cisco Catalyst Routers Can
  Experience Memory Failures - Hardware Upgrade Available.
- URL: <https://www.cisco.com/c/en/us/support/docs/field-notices/741/fn74146.html>
- Revision: 2.0, last published 2024-12-20. Accessed: 2026-10-30.

#### C8300-6T-GBP-1

- Title: Cisco Group Based Policy Platform and Capability Matrix (Inclusive
  of TrustSec Software-Defined Segmentation).
- Used for: Catalyst 8000 router TrustSec capabilities, license, SXP scale.
- URL:
  <https://www.cisco.com/c/dam/en/us/solutions/collateral/enterprise-networks/trustsec/cisco-trustsec-platform-capability-matrix.pdf>
- Revision: PDF modified 2026-02-23. Accessed: 2026-10-30. Locators: Table 1
  (Tier 1 Catalyst 8000 row, p. 5), Table 8.
- Local PDF (reused, saved by another subagent):
  [reference/cisco-gbp-trustsec-platform-matrix-2026-02-23.pdf](reference/cisco-gbp-trustsec-platform-matrix-2026-02-23.pdf)

#### C8300-6T-FAQ-1

- Title: Catalyst 8300 Series Edge Platforms FAQ
- Used for: CME conflict, feature-specific voice mode qualification, no out-of-band management interface
- URL: <https://www.cisco.com/c/en/us/products/collateral/routers/catalyst-8300-series-edge-platforms/cat-8300-series-edge-qa.html>
- Revision: updated 2026-06-23. Accessed: 2026-10-31 UTC.
- Locator: Platform out-of-band interface question; Collaboration on-box CME and DSP questions. No local PDF saved.

#### C8300-6T-COMP-1

- Title: Cisco Catalyst SD-WAN Control Components Compatibility Matrix and Recommended Computing Resources — Compatibility Matrix
- Used for: official transition to the public Compatibility Matrix Tool
- URL: <https://www.cisco.com/c/en/us/td/docs/routers/sdwan/release/notes/compatibility-and-server-recommendations/comp-matrix.html>
- Revision: updated 2026-09-25. Accessed: 2026-10-31 UTC.
- Locator: What is changing; link to Compatibility Matrix Tool. No local PDF saved.

#### C8300-6T-COMP-2

- Title: Catalyst SD-WAN Control Component Compatibility Matrix — filtered Catalyst 8300 results

- Used for: formal control-component/edge pairing at 20.15.6/17.15.6; compatibility is distinct from recommendation

- URL: <https://www.cisco.com/c/dam/en/us/td/docs/Website/enterprise/catalyst_sdwan_compatibility_matrix/index.html>

- Revision: live tool, no per-result revision stated. Accessed: 2026-10-31 UTC.

- Locator: Controller release 20.15; Product Type IOSXE; product Catalyst 8300/Catalyst 8500 12X/124QC; row 20.15.6, 20.15.6.1. No local PDF saved.

- Retrieval: public installed Playwright browser, ordinary UI selection. The initial sandbox browser launch failed; the formally approved execution outside the sandbox succeeded.

- Saved filtered result: [reference/c8300-sdwan-compatibility-20.15-accessed-2026-10-31.txt](reference/c8300-sdwan-compatibility-20.15-accessed-2026-10-31.txt).

#### C8300-6T-FN-2

- Title: FN72510 — IPsec weak cryptographic algorithms
- Used for: configuration-dependent IPsec upgrade risk
- URL: <https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72510.html>
- Revision: 1.5, updated 2026-01-20. Accessed: 2026-10-31 UTC.
- Locator: Problem Description; Workaround/Solution Enterprise Routing table. No local PDF saved.

#### C8300-6T-FN-3

- Title: FN72578 — SLP high CPU/memory usage
- Used for: affected releases, RUM accumulation and fixed releases
- URL: <https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72578.html>
- Revision: updated 2023-09-29. Accessed: 2026-10-31 UTC.
- Locator: Products Affected; Workaround/Solution. No local PDF saved.

#### C8300-6T-FN-4

- Title: FN74350 — CUBE public-CA TLS client-authentication EKU changes
- Used for: exact chassis applicability and basis-vs-26.1.1 certificate behavior
- URL: <https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74350.html>
- Revision: 2.0, updated 2026-06-23. Accessed: 2026-10-31 UTC.
- Locator: Products Affected; Workaround/Solution options and fixed-release table. No local PDF saved.

#### C8300-6T-FN-5

- Title: FN72323 — QuoVadis Root CA 2 decommission
- Used for: historical affected releases and fixed-release context
- URL: <https://www.cisco.com/c/en/us/support/docs/field-notices/723/fn72323.html>
- Revision: updated 2023-10-05. Accessed: 2026-10-31 UTC.
- Locator: Products Affected; Workaround/Solution. No local PDF saved.

#### C8300-6T-FN-6

- Title: FN72509 — SNMP weak cryptographic algorithms
- Used for: configuration-dependent SNMPv3 upgrade risk
- URL: <https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72509.html>
- Revision: updated 2023-08-15. Accessed: 2026-10-31 UTC.
- Locator: Problem Description; Recommended Solution. No local PDF saved.

#### C8300-6T-FN-7

- Title: FN72570 — OSPFv3 IPsec weak cryptographic algorithms
- Used for: configuration-dependent OSPFv3 upgrade risk
- URL: <https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72570.html>
- Revision: updated 2023-06-29. Accessed: 2026-10-31 UTC.
- Locator: Problem Description; Recommended Solution. No local PDF saved.

#### C8300-6T-FN-LIST-1

- Title: Catalyst 8300 Series Edge Platforms — Field Notices
- Used for: scope of seven listed notices reviewed
- URL: <https://www.cisco.com/c/en/us/support/routers/catalyst-8300-series-edge-platforms/products-field-notices-list.html>
- Revision: live index. Accessed: 2026-10-31 UTC.
- Locator: Cisco Catalyst 8300 Edge Platform list. No local PDF saved.

#### C8300-6T-PSIRT-LIST-1

- Title: Catalyst 8300 Series Edge Platforms — Security Advisories, Responses and Notices
- Used for: scope selection for decision-relevant review
- URL: <https://www.cisco.com/c/en/us/support/routers/catalyst-8300-series-edge-platforms/products-security-advisories-list.html>
- Revision: live index. Accessed: 2026-10-31 UTC.
- Locator: October 2026 Snort advisory links; older archive explicitly non-exhaustive. No local PDF saved.

#### C8300-6T-PSIRT-1

- Title: Cisco IOS XE Software Security Hardening Release: August 2026
- Used for: autonomous/controller affected scope and first fixed 17.15.6
- URL: <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-iosxe-V8NMuMZJ>
- Revision: 1.1, updated 2026-10-02. Accessed: 2026-10-31 UTC.
- Locator: Affected Products; Fixed Software. No local PDF saved.

#### C8300-6T-PSIRT-2

- Title: Multiple Cisco Products Snort 3 Security Hardening Release: October 2026
- Used for: UTD applicability, fixed package and feature-specific advisory review
- URL: <https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-hardening-snort3-ybgmhTQe.html>
- Revision: 1.1, updated 2026-10-22. Accessed: 2026-10-31 UTC.
- Locator: Affected Products; Fixed Software — UTD on Cisco IOS XE Software. No local PDF saved.

#### C8300-6T-PSIRT-3

- Title: Multiple Cisco Products Snort 3 SMTP MIME Denial of Service Vulnerability
- Used for: UTD applicability, fixed package and feature-specific advisory review
- URL: <https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-snort3-mime-vulns-bkXjcKkt.html>
- Revision: 1.1, updated 2026-10-22. Accessed: 2026-10-31 UTC.
- Locator: Vulnerable Products — Unified Threat Defense; Determine Whether UTD Is Enabled; UTD Fixed Releases. No local PDF saved.

#### C8300-6T-PSIRT-4

- Title: Multiple Cisco Products Snort 3 Denial of Service Vulnerabilities
- Used for: UTD applicability, fixed package and feature-specific advisory review
- URL: <https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-snort3-misc-dos-6mB22qAK.html>
- Revision: 1.1, updated 2026-10-22. Accessed: 2026-10-31 UTC.
- Locator: Vulnerable Products; Details; UTD Fixed Releases. No local PDF saved.

#### C8300-6T-PSIRT-5

- Title: Multiple Cisco Products Snort 3 Generic Routing Encapsulation Denial of Service Vulnerability
- Used for: UTD applicability, fixed package and feature-specific advisory review
- URL: <https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-snort3-gre-JNpMHrTv.html>
- Revision: 1.1, updated 2026-10-22. Accessed: 2026-10-31 UTC.
- Locator: Vulnerable Products; UTD Fixed Releases. No local PDF saved.

#### C8300-6T-PSIRT-6

- Title: Multiple Cisco Products Snort 3 Denial of Service Vulnerability (GTP codec)
- Used for: UTD applicability, fixed package and feature-specific advisory review
- URL: <https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-snort3-gtpcodec-dos-Rmecfepz.html>
- Revision: 1.1, updated 2026-10-22. Accessed: 2026-10-31 UTC.
- Locator: Vulnerable Products; UTD Fixed Releases. No local PDF saved.

#### C8300-6T-PSIRT-7

- Title: Multiple Cisco Products Snort 3 Visual Basic for Applications Buffer Overflow Denial of Service Vulnerability
- Used for: UTD applicability, fixed package and feature-specific advisory review
- URL: <https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-snort3-vba-bufdos-jAuFdvn9.html>
- Revision: 1.1, updated 2026-10-22. Accessed: 2026-10-31 UTC.
- Locator: Vulnerable Products; UTD Fixed Releases. No local PDF saved.

#### C8300-6T-EOL-2

- Title: EOL15562 — Cisco LAN Switch Network Interface Modules
- Used for: separate supported-chassis versus new-order lifecycle finding
- URL: <https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/network-modules/lan-switch-network-interface-modules-eol.html>
- Revision: 2024-12-05. Accessed: 2026-10-31 UTC.
- Locator: Tables 1–2; NIM-ES2-8/-8-P End-of-Sale 2025-03-05, Last Date of Support 2030-03-31. No local PDF saved.

#### C8300-6T-EOL-3

- Title: EOL15584 — Cisco Switch module for Modular Platforms
- Used for: separate supported-chassis versus new-order lifecycle finding
- URL: <https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/network-modules/switch-modular-platform-eol.html>
- Revision: amended, updated 2025-01-23. Accessed: 2026-10-31 UTC.
- Locator: Tables 1–2; NIM-ES2-4 End-of-Sale 2025-04-17, Last Date of Support 2030-04-30. No local PDF saved.

#### C8300-6T-TMG-3

- Title: Legacy GE transceiver compatibility link, redirected to Cisco Compatibility Information index
- Used for: resolve original access-gap classification; does not prove platform optics support
- URL: <https://www.cisco.com/c/en/us/td/docs/interfaces_modules/transceiver_modules/compatibility/matrix/GE_Tx_Matrix.html>
- Revision: public redirect observed 2026-10-31 UTC. Accessed: 2026-10-31 UTC.
- Locator: HTTP 200 final URL https://www.cisco.com/c/en/us/support/interfaces-modules/transceiver-modules/products-device-support-tables-list.html; general matrix user-manual links only. No local PDF saved.

### References - unresolved

No unreadable public URL remains from the original list. The legacy GE matrix
URL returned HTTP 200 after redirecting to Cisco's general transceiver
compatibility index on 2026-10-31 UTC; it supplies no exact-platform result
([C8300-6T-TMG-3](#c8300-6t-tmg-3)). Current platform optics evidence remains
[C8300-6T-TMG-2](#c8300-6t-tmg-2).

Required claims with no source found after the public-source review:
`service unsupported-transceiver` support and TAC position on third-party
optics; a Catalyst 8300-specific TACACS+ release/mode statement; behavior on
missed SLP reports; heat dissipation and maximum power consumption; the
17.15.6 release date; remaining DOM display syntax; CME's conflicting source
claims; per-PID release/withdrawal/orderability details where the module tables
mark them unverified; and openly published US pricing. Quotes are needed for
chassis, Routing Essentials or DNA subscription, modules, optics and support.
Account-gated tools and hardware checks remain vendor/user follow-ups, not
research that was silently left unattempted.
