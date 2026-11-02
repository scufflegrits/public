# Cisco C8375-E-G2 (Cisco 8300 Series Secure Router) - Model Research r1.1.0

## Research status

| Item | Status |
| --- | --- |
| Revision | r1.1.0; 2026-10-30 America/Chicago (continuation access dates recorded separately). Corrected maintenance/upgrade/module/CLI evidence; added sourced manager deployment, licensing, offline operation, ISE and exact-platform Catalyst Center compatibility research. |
| Request | `request-cisco-comparison-r1.1.0.md`, model 3 |
| Research cutoff | Cutoff 2026-10-30 America/Chicago. Original accesses: 2026-10-30; management/review continuation: 2026-10-31 UTC (still 2026-10-30 locally). Source entries retain actual access dates. |
| Confirmed identity | **Confirmed.** Supplied name `C8375-E-G2` = PID `C8375-E-G2`, "Cisco 8300 Secure Router with 2x10GE, 4x2.5GE, 1xNIM, 1xSM, and 1xPIM", Large platform class, Cisco 8300 Series Secure Routers, part of the Cisco 8000 Series Secure Routers family ([C8375-OG-1](#c8375-og-1) Table 1; [C8375-DS-1](#c8375-ds-1)). No source contradicted the request's pre-check. |
| Software basis | **Cisco IOS XE 17.15.5 (MD), the Cisco-suggested release** for this chassis: the Cisco Software Download page for "8300 Secure Router Gen2" marks IOSXE-17.15.5(MD) as "Suggested Release" (image `c8kg2be-universalk9.17.15.05.SPA.bin`, release date 2026-02-18) and links "Release Notes for C8375-E-G2" ([C8375-SWD-1](#c8375-swd-1)). This is a documented download designation; its applicability to the C8375-E-G2 is **inferred** from that link and from the C8375-E-G2 being the only 8300 Series Secure Router supported on 17.15.x (the C8355-G2 needs 17.18.1). Cisco's recommended-release document has no row for this family ([C8375-REL-1](#c8375-rel-1)). Newest available: 26.2.1 ([C8375-REL-2](#c8375-rel-2)). Minimum release for the chassis: IOS XE 17.15.3. Features that need a later release are marked **above basis**; see [Software](#software). |
| Operating mode | Autonomous mode (enterprise branch / WAN edge) is the baseline and the factory default. Controller (SD-WAN) mode and SD-Routing mode are also supported ([C8375-SCG-1](#c8375-scg-1) ch. 1; [C8375-LIC-1](#c8375-lic-1) "Scope"). |
| Run status | **Complete.** Every required section has findings or explicit gaps. The run was interrupted once by an API rate limit; the decision-relevant PSIRT check was done after it reset (see [Platform-specific caveats](#platform-specific-caveats)). An exhaustive PSIRT review was not attempted, by design. |
| Next steps | (1) Run Cisco Software Checker for IOS XE 17.15.5 against the C8375-E-G2: the August 2026 hardening advisory lists 17.15.6 as the first fixed 17.15.x release, so the suggested release is below it. (2) Re-check the download page for a move of the suggested-release star to 17.15.6. (3) Ask Cisco or the partner to confirm the SLR approval process and term-license renewal under SLR; SLR needs 17.18.1a or later, above the suggested release. |
| Material gaps found | Security status of the suggested 17.15.5 (below the advisory's first fixed 17.15.6); maximum power draw and heat dissipation; reporting cadence and expiry behavior for disconnected licensing on this exact platform (SLR, the cadence-free method, is above the 17.15.5 basis); `service unsupported-transceiver` and DOM show syntax for this platform; 802.1X/MAB and SXP on this host; pricing. Details in each section and in [References - unresolved](#references---unresolved). |

## Contents

- [Research status](#research-status)
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
  - [Cisco ISE integration](#cisco-ise-integration)
  - [Management platforms and disconnected deployment](#management-platforms-and-disconnected-deployment)
- [Modules and expansion](#modules-and-expansion)
  - [Slot map](#slot-map)
  - [NIM, SM, and carrier modules](#nim-sm-and-carrier-modules)
  - [Power supplies, memory, storage, fans, and accessories](#power-supplies-memory-storage-fans-and-accessories)
  - [Optics](#optics)
  - [Module reuse across the four platforms](#module-reuse-across-the-four-platforms)
- [Platform-specific caveats](#platform-specific-caveats)
- [Appendix A: identification and inventory commands](#appendix-a-identification-and-inventory-commands)
- [References](#references)
  - [References - unresolved](#references---unresolved)

## Summary

**Multicast Service Reflection:** Cisco’s [8000 Series Secure Routers licensing matrix](https://www.cisco.com/c/m/en_us/products/software/wan-routing-licensing-feature-matrix.html) explicitly lists MSR under Routing Advantage for the secure-router OS feature set; C8375-E-G2 is included in the Large platform class ([Cisco 8000 Series Secure Routers Licensing](https://www.cisco.com/c/en/us/td/docs/routers/cloud_edge/licensing/8000-series-secure-routers-licensing.html)). This documents the feature entitlement. The [IOS XE 17.x guide](https://www.cisco.com/c/en/us/td/docs/routers/ios-xe/ip-multicast/ip-multicast/m_imc_service_reflect-0.html) documents the CLI and general release information, but an exact C8375-E-G2 configuration test at the selected release was not found. The Catalyst 8000 troubleshooting article tests a Catalyst 8500, not C8375. The matrix separates CLI/Web UI routing features from SD-WAN subscriptions; controller-mode MSR is not documented. Sources reviewed 2026-11-01.

**Identity.** Supplied name `C8375-E-G2`; confirmed PID `C8375-E-G2` (no SKU
correction needed); official family Cisco 8300 Series Secure Routers within the
Cisco 8000 Series Secure Routers; Large platform class
([C8375-OG-1](#c8375-og-1) Table 1; [C8375-LIC-1](#c8375-lic-1) "Platform
class"). The 8300 Series has two models, C8375-E-G2 (modular) and C8355-G2
(fixed) ([C8375-DS-1](#c8375-ds-1); [C8375-HIG-1](#c8375-hig-1) "Chassis
views"). The only ordering variant found is a TAA-compliant order path started
from "C8375-E-G2++" in Cisco Commerce ([C8375-OG-1](#c8375-og-1) "Ordering
process", Step 2). AC, AC+PoE, and DC power are configurable options on the
one chassis PID, not separate chassis PIDs ([C8375-OG-1](#c8375-og-1)
Table 4). Meraki-managed (`-MX`) variants were not found for this model in the
sources checked; the datasheet names one only for the C8355-G2.

**Place in the lineup.** Cisco positions the 8300 Series Secure Routers for
large branches and calls the 8300/8200 Secure Routers "the next generation of
secure WAN appliances" relative to the Catalyst 8300 and 8200 Edge Platforms,
claiming higher IPsec and CEF performance, higher built-in WAN port density,
256-bit WAN MACsec on all front-panel ports, and feature parity with the
Catalyst 8300/8200 Edge Platforms ([C8375-FAQ-1](#c8375-faq-1) "Cisco 8200 and
8300 Series Secure Routers FAQ"). Cisco did not name the C8375-E-G2 as an
ISR4431 replacement in any source read here. It is, however, Cisco's named
migration product for both `C8300-1N1S-4T2X` and `C8300-1N1S-6T` in
End-of-Sale bulletin EOL15950, and those two are the ISR4431's named
replacements, so the C8375-E-G2 is second in that replacement chain
([C8375-EOL-3](#c8375-eol-3) Table 2; chain **inferred** from the two
notices).

**Relationship to the Catalyst 8300 (evidence only).**

| Aspect | Shared with Catalyst 8300 Edge | Not shared / different |
| --- | --- | --- |
| Operating system | Cisco IOS XE; autonomous and controller modes; universalk9 image ([C8375-SCG-1](#c8375-scg-1) ch. 1) | Separate image PIDs (`SC83G2UK9-1715`, `SC83G2NEK9-1715`) and separate release notes ([C8375-OG-1](#c8375-og-1) Table 4; [C8375-RN-1](#c8375-rn-1)) |
| Feature set | Cisco states feature parity with the Catalyst 8300/8200 Edge Platforms; CUBE/SRST "full feature parity with the Catalyst 8300 Series platform" ([C8375-FAQ-1](#c8375-faq-1)) | Processor: "all-new secure networking processor" ([C8375-HIG-1](#c8375-hig-1) "Cisco 8300 Series Secure Routers"); no physical PVDM or SM-X-PVDM support, replaced by vDSP ([C8375-FAQ-1](#c8375-faq-1)) |
| Licensing | Both use Smart Licensing Using Policy as the reporting mechanism | 8000 Series Secure Routers use platform-class licensing (OS Essentials / Routing Advantage / WAN Essentials / WAN Advantage), not bandwidth tiers, and HSECK9 "is not applicable and is not required" ([C8375-LIC-1](#c8375-lic-1) "Platform-Based licensing"). Compare tier names against the Catalyst 8300 file before assuming equivalence. |
| Module PIDs (list level) | These PIDs appear on both the C8375-E-G2 lists and the Catalyst 8300 datasheet list: C-NIM-4X, C-NIM-8T, C-NIM-8M, C-SM-16P4M2X, C-SM-NIM-ADPT, NIM-2FXO, NIM-VAB-A, SM-X-1T3/E3, M2USB-32G, C8300-FAN-1R ([C8375-OG-1](#c8375-og-1) Table 7; [C8375-C83DS-1](#c8375-c83ds-1) Table 7 and accessories) | Memory PIDs differ (MEM-C83G2-16GB/32GB vs MEM-C8300-xGB); SSD PIDs differ (SSD-M2SED-600G/2T vs SSD-M2NVME-2T). C-NIM-WAN-2X/4S are listed for the C8375-E-G2 only. C-NIM-1X, C-NIM-1M, C-NIM-2T, NIM-ES2-x, C-SM-40P8M2X, and UCS-E are on the Catalyst 8300 list but were not found on any C8375-E-G2 list checked ([C8375-C83DS-1](#c8375-c83ds-1) Table 7). |
| Power supply / chassis kit | PWR-CC1-400WAC appears in a C8375-E-G2 `show inventory` example as "400W AC power supply for Cisco C8300 1RU" and is also named in the Catalyst 8300 datasheet; C8300-FAN-1R, C8300-RM-19-1R, and C8300-NIM/SM/PIM-BLANK carry C8300 names ([C8375-SCG-1](#c8375-scg-1) ch. 14; [C8375-OG-1](#c8375-og-1) Table 4; [C8375-C83DS-1](#c8375-c83ds-1)) | PWR-CC1-760WAC is described as "760W AC Power Supply for Cisco C8375" ([C8375-SCG-1](#c8375-scg-1) ch. 14). Whether each shared PSU PID is supported on the other chassis must be checked in that chassis's own sources. |

**Key takeaways.**

1. **Orderable new, current, and lifecycle-clean at chassis level.** Series
   released 2025-06-09 ([C8375-SUP-1](#c8375-sup-1)); no chassis End-of-Sale
   notice found as of 2026-10-30. The software train is the lifecycle
   variable. Cisco's suggested release is IOS XE 17.15.5 ([C8375-SWD-1](#c8375-swd-1)), but the
   17.15.x train passed End-of-Sale on 2026-03-30 and its maintenance releases
   end 2027-03-30, with Cisco's migration guidance pointing to 17.18.1 or later
   ([C8375-EOL-2](#c8375-eol-2)). IOS XE 17.18.x got its End-of-Life notice on
   2026-10-30 ([C8375-EOL-1](#c8375-eol-1)), and 26.x releases carry 48-month
   sustaining support ([C8375-SWLC-1](#c8375-swlc-1)). For maintenance-release coverage, plan a move off 17.15.x by
   **2027-03-30**, about five months after the research cutoff. Security
   support and Last Date of Support are separate milestones.
1. **Licensing is simpler than the Catalyst 8300 model on paper but enforced
   on-device.** The perpetual OS Essentials license caps aggregate crypto
   throughput at 250 Mbps. Routing Advantage (84-month subscription) or
   perpetual OS Advantage is needed for DMVPN/FlexVPN/GETVPN, TrustSec,
   MPLS, CUBE/SRST and unthrottled crypto. From 17.18.1a, a device in Day-0
   Enforcement stays at 250 Mbps until Advantage is AUTHORIZED; an upgrade
   from an existing Advantage configuration enters Day-N and remains
   unthrottled
   ([C8375-LIC-1](#c8375-lic-1); [C8375-LFM-1](#c8375-lfm-1)).
1. **Offline licensing has a documented method: Specific License
   Reservation (SLR).** Cisco documents SLR on this exact PID (worked example
   uses C8375-E-G2), but enabling SLR requires "necessary approval and
   authorization from Cisco". Behavior when a reserved term license reaches
   its end date is not documented in the sources read
   ([C8375-LIC-1](#c8375-lic-1) "Specific License Reservation"). SLR needs
   Day-0 Enforcement, which starts at 17.18.1a, so it is **above the 17.15.5
   basis**. At the basis, the documented offline path is Smart Licensing
   Using Policy with offline CSLU or SSM On-Prem file exchange, at a cadence
   not stated for this platform. Offline eligibility is therefore
   **documented, with the method depending on release**: SLP file exchange on
   17.15.x, or SLR (with Cisco approval) on 17.18.1a or later.
1. **Interfaces:** 2 x 1G/10G SFP/SFP+ and 4 x 2.5G mGig RJ-45 (100M/1G/2.5G;
   no 10M documented), with UPOE+ (802.3bt, 90 W) on ports 0/0/2-0/0/3 only
   when the 760 W AC+PoE PSU is fitted. No built-in port is faster than 10G.
   Long-reach optics GLC-ZX-SMD, SFP-10G-ER(-S), and SFP-10G-ZR-I are listed
   for the chassis (SFP-10G-ZR-I and the `-S` optics from 17.18.2, above the
   17.15.5 basis) by Cisco's TMG matrix ([C8375-HIG-1](#c8375-hig-1);
   [C8375-TMG-1](#c8375-tmg-1)).
1. **Module support is narrower than the Catalyst 8300 at the PID level and
   moves by release.** Analog voice NIM/SM-X support arrived in 26.1 and
   BRI/E&M in 26.2 (autonomous mode only); DSL NIMs and SM-X-1T3/E3 are
   marked End of Life with last supported release 17.18.1
   ([C8375-OG-1](#c8375-og-1) Table 7 notes; [C8375-FAQ-1](#c8375-faq-1)
   Figure 1). At the 17.15.5 basis, C-NIM-WAN-2X/4S (17.18.1), CUBE/SRST and
   vDSP (17.18.2), and all voice modules (26.1/26.2) are **above basis**.

**Uncertainty that could change the decision.** (a) Whether Cisco will grant
SLR for the planned deployment, and what happens at a reserved term license's
end date; (b) the release choice: Cisco suggests 17.15.5, a train past
End-of-Sale and below the August 2026 advisory's first fix (17.15.6), while
SLR and the newer modules need 17.18.x (EoL announced) or 26.x (drops some
legacy modules); (c) Cisco-published performance figures
are "up to" marketing values with only partial test conditions.

## Lifecycle status

| Milestone | Chassis C8375-E-G2 | Source |
| --- | --- | --- |
| Series release / datasheet created | Series release date 2025-06-09 (support page); datasheet created 2025-06-10, amended 2025-09-05, page "Last updated" 2026-10-14 | [C8375-SUP-1](#c8375-sup-1); [C8375-DS-1](#c8375-ds-1) |
| End-of-Sale | No applicable EoL announcement found as of 2026-10-30 | [C8375-SUP-1](#c8375-sup-1) (EoL notices listed are software-train notices only) |
| End of SW Maintenance Releases | Not applicable (no chassis notice) | same |
| End of Vulnerability/Security Support | Not applicable (no chassis notice) | same |
| Last Date of Support | Not applicable (no chassis notice) | same |
| Cisco recommended replacement | Not applicable | - |
| Warranty | Cisco Limited 2-Year Return To Factory Hardware Warranty | [C8375-DS-1](#c8375-ds-1) |

Software-train notices (kept separate from the chassis; neither bulletin page
lists affected platforms, but both are posted on the 8300 Series Secure Routers
support page, [C8375-SUP-1](#c8375-sup-1)):

| Milestone | IOS XE 17.15.x (EOL15772, amended) | IOS XE 17.18.x (EOL15995) |
| --- | --- | --- |
| End-of-Life Announcement | 2025-09-30 | 2026-10-30 |
| End-of-Sale | 2026-03-30 | 2027-04-30 |
| End of SW Maintenance Releases | 2027-03-30 | 2028-04-29 |
| End of Vulnerability/Security Support | 2028-09-30 | 2029-09-30 |
| Last Date of Support | 2029-03-31 | 2030-03-30 |
| Cisco migration guidance | "migrate to Cisco IOS XE Release 17.18.1 or above" | "migrate to Cisco IOS XE 26.1.1 or above" |
| Source | [C8375-EOL-2](#c8375-eol-2) | [C8375-EOL-1](#c8375-eol-1) |

IOS XE 26.x policy: from 26.1.1 every release is an Extended Support release
with 48 months of sustaining support from GA; End-of-Life announcement 12 months
after GA, End-of-Sale 6 months later, End of SW Maintenance 12 months after
EoS, End of Vulnerability/Security Support 30 months after EoS, Last Date of
Support 3 years after EoS ([C8375-SWLC-1](#c8375-swlc-1)). **Inferred:** with
26.2.1 GA on 2026-08-31, sustaining support would run to about 2030-08; no
26.2.x EoL bulletin exists yet to confirm dates.

Module notices: DSL NIMs (NIM-VAB-A, NIM-VA-B, NIM-VAB-M, NIM-4SHDSL-EA) and
SM-X-1T3/E3 are marked "End of Life" on the C8375-E-G2 with "Last supported
release: 17.18.1" ([C8375-FAQ-1](#c8375-faq-1) Figure 1). No license or bundle
notices were found. No support horizon was supplied, so no pass/fail is
stated. Lifecycle sources checked: [C8375-SUP-1](#c8375-sup-1),
[C8375-EOL-1](#c8375-eol-1), [C8375-EOL-2](#c8375-eol-2),
[C8375-SWLC-1](#c8375-swlc-1), [C8375-FAQ-1](#c8375-faq-1). Absence of a
notice is not a guarantee of future support.

## Hardware specifications

| Item | Value | Source |
| --- | --- | --- |
| Form factor / rack units | 1RU modular chassis | [C8375-DS-1](#c8375-ds-1) Table 7 |
| Dimensions (H x W x D) | 1.73 x 17.5 x 16.25 in | [C8375-DS-1](#c8375-ds-1) Table 7 |
| Weight | 14.3 lb with dual AC PSUs and fan tray | [C8375-DS-1](#c8375-ds-1) Table 7 |
| CPU | "Secure networking processor" (Cisco SoC); 16 CPU cores | [C8375-SCG-1](#c8375-scg-1) Table 1; [C8375-OG-1](#c8375-og-1) "Overview" |
| DRAM | 16 GB DDR5 default (one DIMM, MEM-C83G2-16GB); upgrade to one 32 GB DIMM (MEM-C83G2-32GB); single-DIMM configuration only | [C8375-HIG-1](#c8375-hig-1) "Memory"; [C8375-OG-1](#c8375-og-1) Table 4; [C8375-FAQ-1](#c8375-faq-1) Table 5 |
| Storage | 16 GB default (datasheet); internal bootflash plus one removable M.2 slot: M2USB-32G, SSD-M2SED-600G, SSD-M2SED-2T (self-encrypting NVMe) | [C8375-DS-1](#c8375-ds-1) Table 5; [C8375-OG-1](#c8375-og-1) Table 4; [C8375-HIG-1](#c8375-hig-1) "Memory" |
| Fixed data ports | 4 x 2.5G mGig RJ-45 (`TwoGigabitEthernet0/0/0`-`0/0/3`, 100BASE-TX/1000BASE-T/2500BASE-T); 2 x 1G/10G SFP/SFP+ (`TenGigabitEthernet0/0/4`-`0/0/5`). All six are WAN ports; no flex or LAN-only ports; no combo ports. | [C8375-HIG-1](#c8375-hig-1) Table 1, "Built-in interface ports"; [C8375-SCG-1](#c8375-scg-1) ch. 8; [C8375-FAQ-1](#c8375-faq-1) Table 8 |
| Management / console / USB | 1 x RJ-45 1G out-of-band management; RJ-45 console and USB console (datasheet: Micro-USB; HIG cable table: "5-pin mini USB Type-B"); 1 x USB Type-C (3.0) port (USB0) | [C8375-DS-1](#c8375-ds-1) Table 5; [C8375-HIG-1](#c8375-hig-1) Table 1, Table 8 |
| Module slots | 1 NIM, 1 SM (single-wide), 1 PIM (cellular). Only one service module per chassis. Backplane support 10G. | [C8375-DS-1](#c8375-ds-1) Table 5; [C8375-HIG-1](#c8375-hig-1) "Install Cisco Catalyst Service Module"; [C8375-SCG-1](#c8375-scg-1) Table 1 |
| Power supplies | Two internal hot-swappable FRU bays. Default PWR-CC1-400WAC; options PWR-CC1-760WAC (AC + PoE) and PWR-CC1-500WDC (DC, -40 to -72 V, 48 V nominal). AC input 85-264 VAC. Whether the default order ships one or two PSUs: **unverified** (datasheet says "400W AC internal FRU (dual PSU)"; ordering guide lists one default PID). | [C8375-DS-1](#c8375-ds-1) Tables 5, 7; [C8375-OG-1](#c8375-og-1) Table 4; [C8375-HIG-1](#c8375-hig-1) Table 3 |
| PoE | UPOE+ (802.3bt, 90 W per port) on ports 0/0/2 and 0/0/3 only. PoE budget 360 W with PWR-CC1-760WAC; up to 720 W total PoE in Boost mode with two 760 W PSUs (also feeds a PoE-capable module). | [C8375-HIG-1](#c8375-hig-1) Table 4 note; [C8375-DS-1](#c8375-ds-1) Table 5; [C8375-SCG-1](#c8375-scg-1) Table 18 |
| Power draw | Typical 55 W with default PSU and no modules. Maximum power draw and heat dissipation (BTU/hr): **not found in sources checked.** PSU ratings (400/760/500 W) are capacity, not consumption. | [C8375-DS-1](#c8375-ds-1) Table 5 |
| Cooling / airflow | Field-replaceable fan tray (C8300-FAN-1R in an inventory example); "forward air flow (standard version)"; fans always on, speed temperature-controlled. Exact inlet/exhaust sides described only in a figure (not read as text). | [C8375-HIG-1](#c8375-hig-1) "Chassis ventilation", fan tray section; [C8375-SCG-1](#c8375-scg-1) ch. 14 |
| Operating temperature | 0-40 C up to 10,000 ft; 0-45 C up to 6,000 ft; NEBS short-term -5 to 55 C up to 6,000 ft. Storage -40 to 70 C. Humidity 5-85% operating. | [C8375-DS-1](#c8375-ds-1) Table 7; [C8375-HIG-1](#c8375-hig-1) Table 7 |
| Trust and crypto hardware | Secure Boot with signed images and SUDI hardware anchoring; secure storage; run-time defenses ([C8375-FAQ-1](#c8375-faq-1) security answer); tamper detection ([C8375-SCG-1](#c8375-scg-1) ch. 4); hardware crypto in the secure networking processor ([C8375-DS-1](#c8375-ds-1) key features). A discrete "TPM" or "Trust Anchor module" by name: **not found in sources checked.** | as cited |

## Performance

All values are Cisco "up to" figures from the datasheet, Table 6
([C8375-DS-1](#c8375-ds-1)). Release, operating mode, and license tier used for
testing are **not disclosed**. Port line rate (2 x 10G + 4 x 2.5G) is a
separate figure and is not comparable.

| Metric | Value | Packet size / mix | One-way or aggregate | Mode / release / tier | Other conditions |
| --- | --- | --- | --- | --- | --- |
| Forwarding | 38 Gbps | 512 B | not disclosed | not disclosed | not disclosed |
| IPsec | 20 Gbps | 512 B | not disclosed | not disclosed | cipher and tunnel count not disclosed |
| SD-WAN | 12 Gbps | 512 B | not disclosed | controller mode (implied by name), release not disclosed | "tested with IPsec, QoS, DPI, and Flexible NetFlow" |
| Threat Protection | 7 Gbps | EMIX | not disclosed | not disclosed | "100% DIA-NAT, NGFW, IPS, URLF, and AMP" |
| Licensed crypto cap | 250 Mbps aggregate crypto | - | aggregate | OS Essentials (no Advantage authorized) | a license limit, not a measured figure ([C8375-LIC-1](#c8375-lic-1)) |

Scale (datasheet Table 6): IPv4/IPv6 routes 2M; IPsec tunnels up to 4000 from
IOS XE 26.2.1, up to 3500 before; IPv4 ACLs 4000, ACEs 20K; NAT sessions 1.5M;
VRFs 4000.

**Source conflict.** The 8000 Series FAQ positions the whole 8300 Series at
"IPsec: Up to 30 Gbps (512B)" ([C8375-FAQ-1](#c8375-faq-1) Table 1), while the
datasheet gives 20 Gbps for both 8300 models. The datasheet is exact-PID and
newer, so it is used here; the 30 Gbps figure is unexplained.

**Release-dependent risk.** CSCww15035: "C8375-E-G2: IOS XE 26.1/26.2 UTD hits
high QFP utilization and sustained MemoryInterfaceDrop near 700-742 Mbps,
regression from 3.2 Gbps on 17.18.x", listed as resolved in the 26.2.x release
notes ([C8375-RN-1](#c8375-rn-1)). The fixed-in sub-release is not recorded in
what was read; verify before relying on UTD throughput on 26.x.

## Software

| Item | Release | Release date | Mode | Source |
| --- | --- | --- | --- | --- |
| Minimum for chassis | IOS XE 17.15.3 (17.15.3a) | not stated | autonomous and SD-WAN | [C8375-DS-1](#c8375-ds-1); [C8375-OG-1](#c8375-og-1) Table 4; [C8375-SCG-1](#c8375-scg-1) ch. 1 |
| Minimum SD-WAN Manager | 20.15.3 | - | controller | [C8375-DS-1](#c8375-ds-1) "Software management" |
| Cisco-suggested release | **IOS XE 17.15.5 (MD)** ("Suggested Release" on the download page) | 2026-02-18 (image date) | not stated; universalk9 image covers both | [C8375-SWD-1](#c8375-swd-1); [C8375-REL-1](#c8375-rel-1) has no row for this family |
| Newest available (verified) | IOS XE 26.2.1 | 2026-08-31 | autonomous; controller | [C8375-REL-2](#c8375-rel-2); [C8375-RN-1](#c8375-rn-1) (updated 2026-09-27) |
| Other current trains | Download page "Latest Release": 17.18.5 (MD), 26.2.1 (GA), 17.15.6 (MD), 26.1.2 (GA). Release notes: 26.1.1, 26.1.2; 17.18.1a, 17.18.2, 17.18.3a, 17.18.4, 17.18.5 | not stated | - | [C8375-SWD-1](#c8375-swd-1); [C8375-RN-3](#c8375-rn-3); [C8375-RN-2](#c8375-rn-2) |
| Documented ceiling / final release | none documented | - | - | - |
| **Basis used in this file** | **IOS XE 17.15.5, Cisco-suggested** | 2026-02-18 | autonomous | download designation ([C8375-SWD-1](#c8375-swd-1)) |

**Basis change.** An earlier draft of this file used IOS XE 26.2.1 as a
provisional basis because no recommendation had been found. The user then
supplied a screenshot of the Cisco Software Download page (login required,
captured 2026-10-30) showing "Suggested Release: IOSXE-17.15.5(MD)" for
"8300 Secure Router Gen2" ([C8375-SWD-1](#c8375-swd-1)). Under the request's rules a documented
download designation outranks the newest release, so the basis is now
17.15.5. Claims about 17.18.x and 26.x features are kept and marked **above
basis**. The recommended-release document is general guidance ("Whenever
possible, it is advised to install an Extended-Support release"), not a
designation for this PID ([C8375-REL-1](#c8375-rel-1)).

**Basis caveats (documented facts, combined here).** (a) The 17.15.x train
passed End-of-Sale on 2026-03-30, its maintenance releases end 2027-03-30,
and Cisco's guidance is to "migrate to Cisco IOS XE Release 17.18.1 or above"
([C8375-EOL-2](#c8375-eol-2)). (b) The August 2026 hardening advisory lists
17.15.6 as the first fixed 17.15.x release ([C8375-PSIRT-1](#c8375-psirt-1)),
and 17.15.6 (MD) is on the same download page under "Latest Release"
([C8375-SWD-1](#c8375-swd-1)); the suggested-release star had not moved to it at capture.
**Inferred:** 17.15.6 is the practical pick within the suggested train;
confirm with Cisco Software Checker. (c) The ordering guide's software image
PIDs end in `-1715` (`SC83G2UK9-1715`, `SC83G2NEK9-1715`), consistent with
17.15.x as the factory release ([C8375-OG-1](#c8375-og-1) Table 4).

Controller-mode claims: no SD-WAN Manager pairing for 17.15.5 was found. The
chassis minimum is SD-WAN Manager 20.15.3 ([C8375-DS-1](#c8375-ds-1)); the
26.2.x release notes pair 26.2.1 with SD-WAN Manager 26.2.1 for NGFW
workflows ([C8375-RN-1](#c8375-rn-1)).

**Install vs. bundle mode.** "From Cisco IOS XE 17.15.3a, Cisco 8300 Series
Secure Routers are shipped in install mode by default"; Cisco also warns that
bundle mode "will be deprecated in the near future" ([C8375-SCG-1](#c8375-scg-1)
ch. 7).

**Mode conversion.** `controller-mode enable` / `controller-mode disable` in
privileged EXEC. Switching autonomous to controller erases the startup
configuration and NVRAM certificates, like `write erase`
([C8375-SCG-1](#c8375-scg-1) ch. 1). Licensing effects: autonomous to SD-WAN
requires a reload, after which the device consumes no license and is
unthrottled; autonomous to SD-Routing needs no reload; an installed SLR code is
not returned automatically ([C8375-LIC-1](#c8375-lic-1) "Device mode change").

**ROMMON prerequisites.** 26.2.1: minimum 17.15(3.2r).s2.cp, recommended
17.18(3r).s2.cp ([C8375-RN-1](#c8375-rn-1)). 26.1.1: minimum 17.15(3.2r).s2.cp,
recommended 17.15(3.3r).s2.cp ([C8375-RN-3](#c8375-rn-3)).

**Minimum releases for notable features (C8375-E-G2).** Every row from
17.18.1 down is **above the 17.15.5 basis**.

| Feature | Minimum release | Mode | Source |
| --- | --- | --- | --- |
| Platform-based licensing | 17.15.3a | autonomous | [C8375-LIC-1](#c8375-lic-1) feature history |
| Day-0 license enforcement (and SLR, which requires it) | 17.18.1a | autonomous | [C8375-LIC-1](#c8375-lic-1) |
| C-NIM-WAN-2X / C-NIM-WAN-4S(P) | 17.18.1 | not stated | [C8375-RN-2](#c8375-rn-2); [C8375-FAQ-1](#c8375-faq-1) Figure 1 note [2] |
| CUBE and SRST | 17.18.2 | autonomous only | [C8375-RN-2](#c8375-rn-2); [C8375-FAQ-1](#c8375-faq-1) |
| vDSP | 17.18.2 | autonomous only | [C8375-FAQ-1](#c8375-faq-1) |
| Analog voice NIM/SM-X (FXS/FXO) | 26.1 | Routing (CLI) mode | [C8375-OG-1](#c8375-og-1) Table 7 note |
| BRI and E&M NIMs | 26.2 | autonomous only | [C8375-OG-1](#c8375-og-1) Table 7 note; [C8375-RN-1](#c8375-rn-1) |
| IPsec tunnel scale 4000 | 26.2.1 | not stated | [C8375-DS-1](#c8375-ds-1) Table 6 |
| Secure Router NGFW (V2 engine; migration from UTD V1) | 26.2.1 | not stated for this PID | [C8375-RN-1](#c8375-rn-1) |

Also above basis: GLC-GE-DR-LX and the `-S` 10G optics (17.18.2) and
SFP-10G-ZR-I on the built-in ports (17.18.2) ([Optics](#optics)), and
TACACS+ over TLS 1.3 (17.18.1). **Not affected at basis:** CSCww15035 (a
26.1/26.2 UTD regression), the 26.2 default changes below, and the DSL NIMs
and SM-X-1T3/E3 (last supported 17.18.1). On 17.15.x, Day-0 Enforcement does
not apply: an Advantage boot level is unthrottled after reload without an
authorization check ([C8375-LIC-1](#c8375-lic-1)).

26.2.x also changes defaults that affect ISE and management: RADIUS
Message-Authenticator requirements, TOFU for outbound SSH, proxy ARP disabled,
web server disabled, and Type 0/7 to Type 6 password conversion (the last named
for C8375-E-G2) ([C8375-RN-1](#c8375-rn-1)).

## Licensing

Licensing rules below are from the Cisco 8000 Series Secure Routers Licensing
guide (revised 2026-10-01), which covers autonomous mode; SD-Routing and SD-WAN
licenses are managed in Catalyst SD-WAN Manager ([C8375-LIC-1](#c8375-lic-1)
"Scope"). Legacy ISR technology packages (ipbase, appxk9, securityk9, uck9)
and Network/DNA tiers do not appear in any 8000 Series Secure Router licensing
source read here. They are **documented as replaced** by the platform-class
model ([C8375-LIC-1](#c8375-lic-1); [C8375-OG-1](#c8375-og-1) Tables 9-10).
Large-class license PIDs apply to the C8375-E-G2.

### Feature entitlement

| Capability | Tier / license | Dependencies | Mode / release | Source |
| --- | --- | --- | --- | --- |
| Static/dynamic routing (OSPF, BGP, EIGRP, IS-IS), NAT/PAT, QoS/HQoS, PBR, GRE, VRF-Lite/Multi-VRF, IP SLA, FNF | OS Essentials (perpetual, preloaded) | none | autonomous, 17.15.3+ | [C8375-LFM-1](#c8375-lfm-1) page 2 |
| P2P IPsec | OS Essentials | aggregate crypto limited to 250 Mbps | autonomous | [C8375-LFM-1](#c8375-lfm-1); [C8375-LIC-1](#c8375-lic-1) |
| L3/L4 firewall, ACL, 802.1X, RADIUS, AAA, TACACS+, PKI | OS Essentials | none | autonomous | [C8375-LFM-1](#c8375-lfm-1) "Security" |
| DMVPN, GETVPN, FlexVPN | Routing Advantage (term) or OS Advantage (perpetual) | Advantage boot level; AUTHORIZED status for unthrottled crypto (17.18.1a+) | autonomous / SD-Routing | [C8375-LFM-1](#c8375-lfm-1) "Advanced Encryption and VPN" |
| MPLS L2/L3 VPN, SR/SRv6, EVPN, VXLAN, LISP, advanced multicast | Routing Advantage / OS Advantage | as above | autonomous / SD-Routing | [C8375-LFM-1](#c8375-lfm-1) |
| TrustSec (SGT, SGACL, "SGX"), WAN/LAN MACsec, ETA, L7 firewall | Routing Advantage / OS Advantage | as above | autonomous / SD-Routing | [C8375-LFM-1](#c8375-lfm-1) "Advanced Security" |
| CGNAT, NBAR2, SD-AVC, mDNS | Routing Advantage / OS Advantage | as above | autonomous / SD-Routing | [C8375-LFM-1](#c8375-lfm-1) "Advanced Services" |
| Box-to-box HA for NAT/firewall, object tracking | Routing Advantage / OS Advantage | as above | autonomous / SD-Routing | [C8375-LFM-1](#c8375-lfm-1) |
| Guest Shell, application hosting | Routing Advantage / OS Advantage | storage for container apps (M.2 SSD options) | autonomous | [C8375-LFM-1](#c8375-lfm-1); [C8375-FAQ-1](#c8375-faq-1) |
| CUBE, SRST/eSRST, LGW, Webex SGW, MTP | Routing Advantage / OS Advantage | "Additional CUBE, Media Proxy, SRST licenses may be needed"; 17.18.2+ | autonomous only | [C8375-LFM-1](#c8375-lfm-1); [C8375-FAQ-1](#c8375-faq-1) |
| vDSP | "add-on Routing Advantage License" (wording as in FAQ) | 17.18.2+ | autonomous only | [C8375-FAQ-1](#c8375-faq-1) |
| SD-WAN (overlay, AAR, SD-AVC, AppQoE, cloud onRamp, L3-L7 firewall) | WAN Essentials (LIC-CSWAN-L-E) or WAN Advantage (LIC-CSWAN-L-A) | WAN Advantage adds MRF, multicast, per-VPN QoS, DRE, analytics; Essentials "VPNs limited to 10 VPN + 1 Management" | SD-WAN / SD-Routing | [C8375-LFM-1](#c8375-lfm-1) page 1 |
| Security - Threat (IPS/IDS) | LIC-SEC-L-T add-on | base: WAN Ess/Adv or Routing Adv/OS Adv; CLI and SD-WAN Manager; with Routing Advantage requires LIC-R-OP-SWM | autonomous (CLI) or SD-WAN | [C8375-OG-1](#c8375-og-1) Table 10 and ordering Step 8 |
| Security - URL Filtering | LIC-SEC-L-C add-on | base license + Threat add-on; "Feature supported via SD-WAN manager" | SD-WAN Manager-managed | [C8375-OG-1](#c8375-og-1) Table 10 |
| Security - Malware Defense | LIC-SEC-L-M add-on | base license + Threat add-on; "Feature supported via SD-WAN manager" | SD-WAN Manager-managed | [C8375-OG-1](#c8375-og-1) Table 10 |
| On-prem Catalyst Center / on-prem Secure WAN (SD-WAN) Manager management | LIC-R-OP-CC / LIC-R-OP-SWM | base: Routing Advantage / OS Advantage | - | [C8375-OG-1](#c8375-og-1) Table 10; [C8375-LFM-1](#c8375-lfm-1) |
| Cisco-hosted SD-WAN control (Cloud, Cloud Pro, MSP) | LIC-CSWAN-HCLD / -HCLDP-A / -HCLDPRO / -HCLDMSP | base: WAN Ess/Adv; needs internet to Cisco cloud (out of scope for an air-gapped design) | SD-WAN | [C8375-OG-1](#c8375-og-1) Table 10 |

The ordering guide states "Cisco Routing Advantage & OS Advantage provide the
same license as term and perpetual entitlements respectively"
([C8375-OG-1](#c8375-og-1) "Cisco Software Licenses and Subscriptions").
"SGX" is printed as-is in the matrix; whether it means SXP is **unverified**.

### Throughput and crypto

| Tier / license | Limit unlocked | Crypto restrictions | Prerequisites | Source |
| --- | --- | --- | --- | --- |
| OS Essentials (R-OS-L-E) | aggregate crypto throughput limited to 250 Mbps | P2P IPsec only | none (default boot level) | [C8375-LIC-1](#c8375-lic-1) "Available licenses" |
| Routing Advantage (LIC-ROS-L-A) / OS Advantage (R-OS-L-A) | crypto unthrottled | none stated beyond export rules | `license boot level advantage`, save, reload; on 17.18.1a+ status must be AUTHORIZED; on 17.15.x unthrottled after reload without authorization check | [C8375-LIC-1](#c8375-lic-1) "Configure a license", "Day-0 Enforcement" |
| WAN Advantage in autonomous mode | boot level Advantage is allowed with "a Cisco WAN Advantage license" per the configuration task | as above | as above; WAN licenses are otherwise described for SD-Routing/SD-WAN | [C8375-LIC-1](#c8375-lic-1) "Configure a license" |
| Controller (SD-WAN) mode | device consumes no on-box license; throughput unthrottled after mode change | managed in SD-WAN Manager | license attached in SD-WAN Manager before onboarding | [C8375-LIC-1](#c8375-lic-1) "Device mode change", "Support for Day-0 Enforcement" |
| HSECK9 | **not applicable, not required** | - | - | [C8375-LIC-1](#c8375-lic-1) "Platform-Based licensing" |
| Export authorization (separate from licensing) | image choice: UK9 (universal) or NEK9 (No Payload Encryption) | NEK9 = NPE image | US export classification and any end-use paperwork: **not assessed** (no US export source read) | [C8375-OG-1](#c8375-og-1) Table 4 |

There are no bandwidth throughput tiers: "The licenses are not associated with
a bandwidth tier" ([C8375-LIC-1](#c8375-lic-1)).

### Purchase and enforcement

| License | Perpetual / subscription | Term options | Orderable today | Reporting method | Deadlines / disconnected use | Expiry / noncompliance | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| OS Essentials R-OS-L-E | perpetual, preloaded | - | yes (with hardware) | "not deposited into your smart account nor do you need to report this license" | none | - | [C8375-LIC-1](#c8375-lic-1); [C8375-OG-1](#c8375-og-1) Table 9 |
| OS Advantage R-OS-L-A | perpetual | - | yes (factory pre-install or spare) | SLP (direct, CSLU, SSM On-Prem, offline) | cadence not stated in exact-platform sources | unresolved beyond the Day-0 rule below | [C8375-OG-1](#c8375-og-1) Table 9 |
| Routing Advantage LIC-ROS-L-A | subscription | 84-month subscription period ([C8375-LIC-1](#c8375-lic-1)); FAQ cites a "flexible 12- to 84-month term" for the Networking Subscription | yes | SLP (direct, CSLU, SSM On-Prem) or SLR (offline) | SLR needs no periodic reporting; for SLP the policy sets reporting intervals (values not stated for this platform) | Day-0 (17.18.1a+): unauthorized Advantage stays at 250 Mbps. SLR example license shows "Enforcement type: CONDITIONALLY-ENFORCED" and a term end date; behavior at term end **unresolved** | [C8375-LIC-1](#c8375-lic-1); [C8375-FAQ-1](#c8375-faq-1) |
| WAN Essentials / Advantage LIC-CSWAN-L-E/-A | subscription (Cisco Networking Subscription) | minimum 36 months | yes | managed in SD-WAN Manager | Manager Offline Mode: manual license-summary/report/ACK exchange; generic 90-day/prepaid-three-month/postpaid-monthly policy; verify the assigned WAN offer ([C8375-MGMT-SDW-SLP-1](#c8375-mgmt-sdw-slp-1)) | license must be attached before onboarding | [C8375-LIC-1](#c8375-lic-1); [C8375-OG-1](#c8375-og-1) Table 9 |
| LIC-SEC-L-T / -C / -M | subscription add-ons (term not stated) | not stated | yes | not stated | URL Filtering and Malware Defense need SD-WAN Manager; cloud lookups (URL reputation, file reputation) **inferred** to need internet | unresolved | [C8375-OG-1](#c8375-og-1) Table 10 |

Status values reported by the device: IN USE, NOT IN USE, PENDING, AUTHORIZED,
OUT OF COMPLIANCE, NOT AUTHORIZED. The only enforcement action Cisco documents
is the 250 Mbps crypto throttle ([C8375-LIC-1](#c8375-lic-1) "View the license
status of a device", Table 1). Upgrading to 17.18.1a+ from 17.15.x with
Essentials drops to 250 Mbps (Day-0); with Advantage it stays unthrottled
(Day-N) ([C8375-LIC-1](#c8375-lic-1) "Day-0 Enforcement after an upgrade").
Factory reset: `factory reset keep-license-info` retains licensing state;
`factory reset all` erases the trusted store and resets the Day-0 flag
([C8375-LIC-1](#c8375-lic-1) "Factory reset").

Pricing: **unknown**. No openly published Cisco US price list was found.
Quotes needed: C8375-E-G2 chassis with chosen PSU/memory/storage; R-OS-L-A
(perpetual) vs LIC-ROS-L-A (84-month); LIC-SEC-L-T/-C/-M and LIC-R-OP-SWM if
security add-ons are wanted; support (Basic/Standard/Signature) and RMA
upgrade ([C8375-OG-1](#c8375-og-1) "Cisco Support").

### Offline operation (no internet for license reporting)

**At the 17.15.5 basis.** SLR is not available: it requires Day-0
Enforcement, which starts at 17.18.1a ([C8375-LIC-1](#c8375-lic-1)). On
17.15.x, Advantage is unthrottled after reload without an authorization
check, so missing reports trigger no documented throughput effect. The
documented offline path is Smart Licensing Using Policy with offline CSLU or
SSM On-Prem synchronization ("can be done automatically over the network or
manually offline", [C8375-LIC-1](#c8375-lic-1) "Workflow" table). The
reporting cadence for this platform is **not stated**; see "Other
disconnected paths" below. **Documented upgrade distinction:** moving from 17.15.x with Essentials
to 17.18.1a or later enters Day-0 and sets the 250 Mbps crypto cap; moving
with an existing Advantage configuration enters Day-N and remains
unthrottled. Do not infer that every upgrade requires prior authorization
to avoid throttling. Reporting, term, and later factory-reset obligations
remain separate ([C8375-LIC-1](#c8375-lic-1), "Day-0 Enforcement after an
upgrade"). Plan any move needed for maintenance coverage by 2027-03-30
([C8375-EOL-2](#c8375-eol-2)).

**From 17.18.1a: SLR. Eligibility: documented, conditional.** Cisco documents Specific License
Reservation (SLR) for this exact PID as the offline method "for highly secure,
air-gapped networks" that "enables the use of all entitlements on the router
without the need for communication with Cisco", supported on platforms that
support Day-0 Enforcement (17.18.1a+ in autonomous mode). Its precondition is
"To enable SLR, you must have the necessary approval and authorization from
Cisco" ([C8375-LIC-1](#c8375-lic-1) "Specific License Reservation").

Administrator steps (autonomous mode, from [C8375-LIC-1](#c8375-lic-1); CLI is
quoted from the guide's examples):

1. **At purchase:** give Cisco the Smart Account. If the Smart Account is
   flagged for SLR pre-installation, the factory installs the SLR code and the
   device starts licensed (Day-0 state, activate to reach Day-N).
1. **Otherwise, on the device:** set `license boot level advantage`, save,
   reload; then in global configuration `license smart reservation` (the
   summary workflow also lists `license smart transport off`).
1. Generate a request code: `license smart reservation request local`.
1. On any internet-connected workstation, in Cisco SSM: Inventory > Licenses >
   License Reservation, enter the request code, reserve one specific license
   (Routing Advantage Large, tag `C8K_LARGE_ROUTING_A`), download the
   authorization code file.
1. Carry the file to the device and install:
   `license smart reservation install file bootflash:<file>`.
1. Verify: `show license reservation`, `show license summary` (expect
   "License Reservation is ENABLED" and AUTHORIZED), and
   `show license tech support | section Device` (expect Day-N).
1. On RMA or decommission: `license smart reservation return local`, then
   enter the return code in Cisco SSM (Product Instances > Remove).

**Cadence.** SLR needs no periodic usage reporting ("without needing constant
internet connectivity for usage reporting"). One-time steps per device at
install, plus a return/re-reserve on RMA. **Unresolved:** what an
administrator must do when a reserved *term* license (Routing Advantage,
84 months) reaches its end date or is renewed. The SLR example output shows a
TERM license with a start and end date, but no renewal procedure is given.
**Inferred:** a perpetual OS Advantage license (R-OS-L-A) avoids the term-end
question for the offline case; Cisco does not state this directly.

**Other disconnected paths.** The licensing guide lists on-premises
deployments (Cisco SSM On-Prem and CSLU) whose synchronization with Cisco SSM
"can be done automatically over the network or manually offline", and it says
SSM On-Prem "periodically synchronizes its license database with Cisco SSM"
([C8375-LIC-1](#c8375-lic-1) "Workflow" table, "Components"). The
family-level Smart Licensing Using Policy guide (which does not name the 8000
Series Secure Routers) describes disconnected CSLU and SSM On-Prem file
exchange and a default policy of 90-day first report and 90-day ongoing
reporting for unenforced subscription licenses ([C8375-SLP-1](#c8375-slp-1)
Table 4, "Supported Topologies"). Applying those values to the C8375-E-G2 is
**unverified**: this platform's licenses show "CONDITIONALLY-ENFORCED", a type
that guide's default-policy table does not list. Using CSLU or SSM On-Prem
offline means periodic manual file transfers (RUM report out, ACK in) at a
cadence set by the policy installed on the device.

**HSECK9 / export-controlled crypto offline:** not applicable; no HSEC
authorization code is needed ([C8375-LIC-1](#c8375-lic-1)).

**Controller mode callout.** In SD-WAN mode licenses are attached in Catalyst
SD-WAN Manager. Its documented offline license-summary/report/ACK exchange
is separate from autonomous SLR; see [Management platforms and disconnected
deployment](#management-platforms-and-disconnected-deployment) and
[C8375-MGMT-SDW-SLP-1](#c8375-mgmt-sdw-slp-1).

## Feature support and integration

### Feature matrix

| Feature | Supported | Mode | License / tier | Module or hardware | Minimum release | Key limits / scale | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SD-WAN | yes | controller (also SD-Routing) | WAN Essentials or WAN Advantage (36-month min.) | none | IOS XE 17.15.3 / SD-WAN Manager 20.15.3 | 12 Gbps SD-WAN (512 B); Essentials limited to 10 VPN + 1 management | [C8375-DS-1](#c8375-ds-1); [C8375-LFM-1](#c8375-lfm-1) |
| IPsec VPN | yes | both | P2P IPsec in Essentials (250 Mbps cap); DMVPN/FlexVPN/GETVPN and unthrottled need Advantage | none (crypto in SoC) | 17.15.3 | 20 Gbps (512 B); 3500 tunnels, 4000 from 26.2.1 | [C8375-LFM-1](#c8375-lfm-1); [C8375-LIC-1](#c8375-lic-1); [C8375-DS-1](#c8375-ds-1) |
| NAT | yes | both | NAT/PAT in Essentials; CGNAT and box-to-box NAT HA in Advantage | none | 17.15.3 | 1.5M NAT sessions | [C8375-LFM-1](#c8375-lfm-1); [C8375-DS-1](#c8375-ds-1) |
| QoS | yes | both | QoS/HQoS in Essentials; per-VPN/adaptive QoS in WAN Advantage | none | 17.15.3 | not published | [C8375-LFM-1](#c8375-lfm-1) |
| Voice / CUBE | yes | autonomous only | Routing Advantage / OS Advantage; additional CUBE/SRST licenses may be needed | vDSP (software DSP, 17.18.2+); no PVDM/SM-X-PVDM; analog FXS/FXO NIM/SM-X (26.1+); BRI, E&M (26.2+); T1/E1 MFT and PRI NIMs data-only | CUBE/SRST 17.18.2 | CUBE scale not published | [C8375-FAQ-1](#c8375-faq-1); [C8375-OG-1](#c8375-og-1) Table 7; [C8375-RN-1](#c8375-rn-1) |
| NGFW / UTD | yes | autonomous (Threat via CLI); URLF and Malware Defense via SD-WAN Manager | LIC-SEC-L-T (Threat), LIC-SEC-L-C, LIC-SEC-L-M on top of a base tier; LIC-R-OP-SWM with Routing Advantage | storage options for container apps (inferred need, not stated) | 17.15.3 (service-plane apps listed); NGFW V2 engine 26.2.1 | 7 Gbps Threat Protection (EMIX); see CSCww15035 | [C8375-SCG-1](#c8375-scg-1) Table 1; [C8375-OG-1](#c8375-og-1) Table 10; [C8375-RN-1](#c8375-rn-1) |
| PoE | yes | both (hardware) | none | PWR-CC1-760WAC required; UPOE+ on ports 0/0/2-0/0/3; C-NIM-8M (UPoE+) | 17.15.3 | 90 W per port (802.3bt); 360 W budget, 720 W in Boost with two 760 W PSUs | [C8375-HIG-1](#c8375-hig-1); [C8375-DS-1](#c8375-ds-1); [C8375-SCG-1](#c8375-scg-1) ch. 14 |
| Routing scale | yes | both | OSPF/BGP/EIGRP/IS-IS in Essentials | DRAM 16/32 GB | 17.15.3 | 2M IPv4/IPv6 routes; ACLs 4000 / ACEs 20K | [C8375-DS-1](#c8375-ds-1) Table 6 |
| Segmentation: VRF-Lite | yes | both | Essentials | none | 17.15.3 | 4000 VRFs | [C8375-LFM-1](#c8375-lfm-1); [C8375-DS-1](#c8375-ds-1) |
| Segmentation: MPLS L3VPN, EVPN | yes (entitlement) | autonomous / SD-Routing | Routing Advantage / OS Advantage | none | not stated | not published | [C8375-LFM-1](#c8375-lfm-1) |
| Segmentation: SGT (TrustSec) | entitlement documented; platform config not verified | not stated | Routing Advantage / OS Advantage | none | not stated | not published | [C8375-LFM-1](#c8375-lfm-1); [C8375-FAQ-1](#c8375-faq-1) |
| Multicast Service Reflection | Routing Advantage entitlement documented; exact runtime support at the selected C8375 release not directly tested | Autonomous/CLI feature entitlement; controller-mode MSR not documented | Routing Advantage (Cisco secure-router feature matrix) | Vif interface and PIM infrastructure | IOS XE guide: base feature 3.4S; unicast-to-multicast 17.9.1a; exact C8375 minimum not listed | Generic IOS XE guide limits apply; exact C8375 behavior not validated | [C8375-MSR-1](#c8375-msr-1); [C8375-MSR-LIC-1](#c8375-msr-lic-1); [C8375-MSR-PLAT-1](#c8375-msr-plat-1) |

No feature in the list is documented as deprecated at 17.15.5 or 26.2.1. Rows whose minimum is above 17.15.5 are listed under [Software](#software). CUBE/SRST, vDSP,
and the voice modules are documented as autonomous-only.

### Cisco ISE integration

| Integration | Supported | Mode | License / tier | Module / hardware | Minimum release | Router side vs. ISE side | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RADIUS device administration | yes (entitlement) | both | OS Essentials (RADIUS, AAA) | none | 17.15.3 | Router: AAA/RADIUS client config; 26.2 adds RADIUS Message-Authenticator requirements. ISE: network device, policy sets | [C8375-LFM-1](#c8375-lfm-1); [C8375-RN-1](#c8375-rn-1) |
| TACACS+ device administration | yes (entitlement); TACACS+ over TLS 1.3 from 17.18.1 | both | OS Essentials (TACACS/TACACS+) | none | 17.15.3; TLS 1.3 17.18.1 | Router: TACACS+ server/AAA config. ISE: Device Admin policy (ISE license tier not documented in sources read) | [C8375-LFM-1](#c8375-lfm-1); [C8375-RN-2](#c8375-rn-2) |
| TrustSec SGT inline tagging, SGACL enforcement | entitlement documented; exact-platform configuration **not verified** | not stated | Routing Advantage / OS Advantage | none stated | not stated | Router: CTS config; ISE: SGT/SGACL matrix | [C8375-LFM-1](#c8375-lfm-1) "Advanced Security"; [C8375-FAQ-1](#c8375-faq-1) |
| SXP | **not verified** (matrix prints "SGX") | - | - | - | - | - | [C8375-LFM-1](#c8375-lfm-1) |
| 802.1X on router or switch-module ports | 802.1X listed as an Essentials security feature; port types where it applies **not verified** | not stated | OS Essentials | switch modules C-NIM-8T/8M/4X, C-SM-16P4M2X would be the candidate ports (inferred: built-in ports are routed WAN ports) | not stated | Router: authenticator config; ISE: 802.1X policy | [C8375-LFM-1](#c8375-lfm-1); [C8375-FAQ-1](#c8375-faq-1) |
| MAB | **not verified** | - | - | - | - | - | not found in sources checked |
| Other: ISE integration in SD-WAN | listed under WAN Essentials/Advantage "Integration: Identity Services Engine (ISE), RADIUS" | controller | WAN Essentials / Advantage | none | not stated | configured through SD-WAN Manager | [C8375-LFM-1](#c8375-lfm-1) page 1 |

### Management platforms and disconnected deployment

This continuation supplies management evidence for the four-model comparison.
Router entitlements, the manager's own licensing, and hosting infrastructure
are separate. Autonomous CLI remains the baseline; local hosting alone does
not establish offline license compliance ([C8375-LIC-1](#c8375-lic-1),
[C8375-MGMT-CC-VA-1](#c8375-mgmt-cc-va-1),
[C8375-MGMT-SDW-SLP-1](#c8375-mgmt-sdw-slp-1)).

| Item | Catalyst Center | Catalyst SD-WAN Manager |
| --- | --- | --- |
| Deployment (documented) | Physical appliance on premises; virtual appliance on ESXi, AWS or Azure. | Customer-hosted Manager/control-component VMs on ESXi/KVM/UCS infrastructure; Cisco-hosted and cloud-delivered options also exist. |
| Own entitlement and infrastructure | VA SKU `DN-SW-APL-LIC` is deposited in a Smart Account and must be registered. Instance registration supports direct, On-Prem SSM or smart-proxy modes. Physical appliance is a separate purchase. Router subscriptions/management add-ons remain separate. Fully disconnected VA bootstrap and license-server synchronization need deployment-specific confirmation. | DNA subscriptions for legacy platforms include centralized Manager use; C8375 WAN tiers or Routing/OS Advantage plus `LIC-R-OP-SWM` supply the applicable offer. Compute/hypervisor and cloud-hosting options are separate provisioning choices. A universal separately required on-prem Manager license SKU was not established; obtain an offer-specific quote. |
| No internet at manager (documented) | TAC-enabled virtual air-gap mode on physical appliances and ESXi VAs; ESXi support includes 2.3.7.x. Prepare private address allow lists and local DNS/NTP/device/ISE reachability. Obtain approved upgrade packages and checksums through TAC and transfer them into the enclave. The published 3.x upgrade example is not a 2.3.7 upgrade procedure. | Offline Mode from Manager 20.6.1 / IOS XE 17.6.1a exchanges license-summary, report and ACK files with CSSM through an external workstation. Default interval 90 days; prepaid reporting every three months, postpaid monthly. Overdue sync raises an alert. |
| Reporting boundary | Catalyst Center 2.3.7.x device License Manager explicitly does not support On-Prem SSM **RUM reporting**, despite supporting On-Prem registration modes. Keep router SLP/SLAC and eligible SLR workflows separate. Generic device SLR instructions do not remove C8375 release/approval prerequisites. | SSM On-Prem mode differs from Offline Mode: it requires locally hosted Manager, reachable supported SSM On-Prem, and Manager/server sync every 24 hours. Its documented example server connects to CSSM. For entirely disconnected use, select documented manual Offline Mode or separately verify the server's manual synchronization procedure. |
| Updates and onboarding | Air-gap package transfer is documented; cloud catalogs/integrations need separate connectivity. | The bring-up guide supports local VM/image files, uploaded WAN Edge serial lists, and manual/enterprise certificate workflows. **Inferred:** plan local image storage, CA signing/renewal, DNS/NTP and backups; offline licensing does not waive these duties. |
| ISE integration | AAA, policy and Assurance use ISE/ERS/pxGrid, reachable nodes and trusted certificates. Devices assigned to an ISE-backed site can be propagated into ISE inventory. | SGT identity-firewall integration is documented from Manager 20.10.1 / IOS XE 17.10.1a. ISE supplies SGT/IP bindings to the SD-WAN control plane and Manager policy. Exact router enforcement still requires PID/release evidence. |
| Benefits/workload (inferred) | Central inventory, image management and assurance reduce repeated router work; add appliance/VM operations, compatible releases, integration and offline-update procedures. | Central provisioning, policy, upgrades and license assignment; requires local control-component operations and periodic offline license-file handling. A Cisco-hosted instance cannot serve an enclave with no route to that service. |

Sources by row: deployment/licensing —
[C8375-MGMT-CC-DS-1](#c8375-mgmt-cc-ds-1),
[C8375-MGMT-CC-VA-1](#c8375-mgmt-cc-va-1),
[C8375-MGMT-CC-SYS-1](#c8375-mgmt-cc-sys-1),
[C8375-MGMT-SDW-DS-1](#c8375-mgmt-sdw-ds-1),
[C8375-MGMT-SDW-FAQ-1](#c8375-mgmt-sdw-faq-1), and [C8375-OG-1](#c8375-og-1)
Tables 9–10; disconnected/reporting —
[C8375-MGMT-CC-AIR-1](#c8375-mgmt-cc-air-1),
[C8375-MGMT-CC-ADM-1](#c8375-mgmt-cc-adm-1), and
[C8375-MGMT-SDW-SLP-1](#c8375-mgmt-sdw-slp-1); onboarding —
[C8375-MGMT-SDW-GS-1](#c8375-mgmt-sdw-gs-1); ISE —
[C8375-MGMT-CC-SYS-1](#c8375-mgmt-cc-sys-1) and
[C8375-MGMT-ISE-1](#c8375-mgmt-ise-1). No manager deployment was lab-tested.

**Exact-platform Catalyst Center check.** The public application's JSON was
read as data for **Catalyst Center 2.3.7.11**. These are documented matrix
findings at train granularity, not exact-rebuild validation
([C8375-MGMT-CC-MX-1](#c8375-mgmt-cc-mx-1)):

| Router | Matrix row | Applicability at this research basis |
| --- | --- | --- |
| `ISR4431/K9` | `ISR 4431`; inventory/topology/SWIM/PnP/Assurance Y; 17.12.x included. | Covers the 17.12.8 basis at train granularity. The row also lists later trains; do not override the ISR's documented 17.12.x ceiling using that overbroad field. |
| `C8300-1N1S-4T2X` | Explicit shared row with 6T; the same functions Y; 17.15.x included. | Covers the 17.15.6 basis at train granularity; router entitlement follows its own offer. |
| `C8300-1N1S-6T` | Explicit shared row with 4T2X; the same functions Y; 17.15.x included. | As for 4T2X; does not establish identical WAN throughput or optics. |
| `C8375-E-G2` | Exact row; 17.15.x/17.18.x; inventory/topology/SWIM/PnP/Assurance Y, Application Policy NA; DNA Essentials/Advantage columns N. | Management compatibility at the 17.15.5 train basis is documented. DNA-column N does not mean management unsupported; use Routing/OS Advantage plus `LIC-R-OP-CC` from the platform offer. |

**SD-WAN Manager applicability.** C8375 controller operation needs minimum
IOS XE 17.15.3 / Manager 20.15.3 ([C8375-DS-1](#c8375-ds-1)). The [ISR software section](research-cisco-isr4431-r1.1.0.md#5-software) and
[C8300 software section](research-cisco-c8300-1n1s-4t2x-r1.1.0.md#software)
establish their controller basis; the model-specific compatibility findings
still govern. The shared
manager sources above do not establish a new controller/edge pairing or all
features on every PID: use each model's compatibility evidence. SD-Routing
uses autonomous mode with its own supported-platform/manager requirements
([C8375-LIC-1](#c8375-lic-1), "Scope").

**Sought evidence gaps:** fully disconnected activation for the selected
Catalyst Center VA/On-Prem combination; appliance-license term/enforcement
for that quoted offer; service-specific behavior of cloud intelligence
feeds; exact VM sizing for the unspecified site count. Management deployment,
licensing, offline operation and ISE sources were researched here. These are
bounded evidence/design gaps, rather than unattempted sections.

## Modules and expansion

### Slot map

| Slot | Type | Count | Notes | Source |
| --- | --- | --- | --- | --- |
| 0/0 | built-in ports | 6 | Tw0/0/0-0/0/3 (2.5G mGig RJ-45), Te0/0/4-0/0/5 (1G/10G SFP/SFP+) | [C8375-HIG-1](#c8375-hig-1) Table 1; [C8375-SCG-1](#c8375-scg-1) ch. 8 |
| NIM slot (0/1) | NIM | 1 | C-NIM switch/WAN modules supported only in the NIM slot (not in the SM-NIM adapter); one per chassis for marked modules | [C8375-FAQ-1](#c8375-faq-1) Figure 1 notes; [C8375-SCG-1](#c8375-scg-1) example shows Tw0/1/x |
| SM slot (1) | SM, single-wide | 1 | Only one service module per chassis; C-SM-NIM-ADPT carrier gives two NIM bays in this slot | [C8375-HIG-1](#c8375-hig-1) SM and NIM-adapter sections |
| PIM slot | cellular PIM | 1 | available, not assessed (cellular out of scope) | [C8375-DS-1](#c8375-ds-1); [C8375-OG-1](#c8375-og-1) Table 8 |
| M.2 slot | storage | 1 | M2USB-32G / SSD-M2SED-600G / SSD-M2SED-2T | [C8375-OG-1](#c8375-og-1) Table 4 |
| DIMM | memory (internal) | 1 | single DIMM, 16 or 32 GB | [C8375-FAQ-1](#c8375-faq-1) Table 5 note |
| PSU bays | power | 2 | hot-swap | [C8375-HIG-1](#c8375-hig-1) Table 3 |
| Fan tray | fan | 1 | field-replaceable; not hot-swappable on 8300/8200 Secure Routers ("Surprise replacement of the system fan tray is not supported") | [C8375-FAQ-1](#c8375-faq-1) OIR answer |

OIR is supported for modules with `hw-module subslot` stop/start before
removal ([C8375-FAQ-1](#c8375-faq-1)).

### NIM, SM, and carrier modules

Coverage: the union of the ordering guide Table 7, the datasheet module list,
and the FAQ Figure 1 "Validated modules on the Cisco 8300 Series Secure
Routers". Lists are not guaranteed complete, and absence from them does not
prove lack of support. "At basis 17.15.5" means the module's documented
minimum release is at or below 17.15.5 and it was not withdrawn before it;
"min. not stated" means the chassis supports the module but no per-module
minimum release was found, so support at 17.15.5 is **inferred** from the
17.15.3 chassis minimum. "Orderable" means listed in the current ordering
guide ([C8375-OG-1](#c8375-og-1), 2026-10-09).

| PID | Description / capability | Slot | Min release / mode | Dependency / placement | Chassis | At basis 17.15.5 | Orderable | Source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C-NIM-WAN-2X | 2-port 1/10G SFP/SFP+ WAN NIM, WAN MACsec | NIM | 17.18.1 | one per chassis; NIM slot only | yes | **no: needs 17.18.1** | yes | [C8375-OG-1](#c8375-og-1); [C8375-FAQ-1](#c8375-faq-1); [C8375-RN-2](#c8375-rn-2) |
| C-NIM-WAN-4S | 4-port 1G SFP WAN NIM, WAN MACsec (FAQ figure prints "C-NIM-WAN-4SP") | NIM | 17.18.1 | NIM slot only | yes | **no: needs 17.18.1** | yes | same |
| C-NIM-4X | 4-port 1/10G SFP/SFP+ switch NIM, LAN/WAN MACsec, optional L3 | NIM | not stated for this chassis | one per chassis; NIM slot only | yes | yes, min. not stated | yes | [C8375-OG-1](#c8375-og-1); [C8375-FAQ-1](#c8375-faq-1) |
| C-NIM-8T | 8-port 100M/1G switch NIM, MACsec, optional L3 | NIM | not stated | as above | yes | yes, min. not stated | yes | same |
| C-NIM-8M | 8-port 100M/1G/2.5G switch NIM, UPoE+, MACsec, optional L3 | NIM | not stated | as above; PoE needs PoE PSU (inferred) | yes | yes, min. not stated | yes | same |
| C-SM-16P4M2X | 22-port Catalyst L2 switch module (UADP); only path to L2 EtherChannel (LACP/PAgP) | SM | not stated; reload needed to activate switching mode | one SM per chassis | yes | yes, min. not stated | yes | [C8375-OG-1](#c8375-og-1); [C8375-HIG-1](#c8375-hig-1); [C8375-FAQ-1](#c8375-faq-1) |
| C-SM-NIM-ADPT | SM-form-factor carrier for two NIMs | SM | not stated | C-NIM modules not supported in it | yes | yes, min. not stated | yes | same |
| NIM-1T / NIM-2T / NIM-4T | 1/2/4-port high-speed serial | NIM | not stated | - | yes | yes, min. not stated | yes | [C8375-OG-1](#c8375-og-1); [C8375-FAQ-1](#c8375-faq-1) |
| NIM-16A / NIM-24A / SM-X-64A | async | NIM / SM | not stated | - | yes | yes, min. not stated | yes | same |
| NIM-2FXS/4FXOP, NIM-2FXSP, NIM-4FXSP, NIM-2FXO, NIM-4FXO | analog voice | NIM | 26.1, Routing (CLI) mode | - | yes | **no: needs 26.1** | yes | [C8375-OG-1](#c8375-og-1) Table 7 note |
| SM-X-8FXS/12FXO, SM-X-16FXS/2FXO, SM-X-24FXS/4FXO | analog voice | SM | 26.1, Routing (CLI) mode | - | yes | **no: needs 26.1** | yes | same |
| NIM-2BRI-NT/TE, NIM-4BRI-NT/TE, NIM-4E/M | BRI and E&M voice | NIM | 26.2, autonomous only | - | yes | **no: needs 26.2** | yes | [C8375-OG-1](#c8375-og-1); [C8375-RN-1](#c8375-rn-1) |
| NIM-1/2/4/8MFT-T1/E1, NIM-1/2/8CE1T1-PRI | T1/E1 and PRI | NIM | data-only "at launch" | voice on TDM NIMs on roadmap | yes (FAQ figure) | data-only | **not in ordering guide Table 7** | [C8375-FAQ-1](#c8375-faq-1) |
| NIM-VAB-A, NIM-VA-B, NIM-VAB-M, NIM-4SHDSL-EA | DSL | NIM | - | - | yes | yes, min. not stated (last supported 17.18.1) | listed in datasheet; not in ordering guide Table 7 | [C8375-FAQ-1](#c8375-faq-1) Figure 1; [C8375-DS-1](#c8375-ds-1) |
| SM-X-1T3/E3 | T3/E3 | SM | - | - | yes | yes, min. not stated (last supported 17.18.1) | listed in datasheet; not in ordering guide Table 7 | same |

Not supported: physical PVDM and SM-X-PVDM ([C8375-FAQ-1](#c8375-faq-1)).
UCS-E compute modules: **conflict.** The FAQ's capability list mentions
"edge computing (Cisco UCS E-Series) modules on the Cisco 8300 Series", but no
UCS-E PID appears in the validated-module figure, the ordering guide, or the
datasheet module list. Treat UCS-E as **not verified** on the C8375-E-G2.
Lifecycle status of individual modules beyond the FAQ's End of Life marks: not
checked per PID.

External Ethernet-connected devices (not internal modules): Cisco cellular
gateways are mentioned as an option ([C8375-FAQ-1](#c8375-faq-1)); cellular is
out of scope.

### Power supplies, memory, storage, fans, and accessories

| PID | Description | Default / option | Source |
| --- | --- | --- | --- |
| PWR-CC1-400WAC | 400 W AC PSU | default | [C8375-OG-1](#c8375-og-1) Table 4 |
| PWR-CC1-760WAC | 760 W AC PSU with PoE (360 W PoE) | option; required for PoE | [C8375-OG-1](#c8375-og-1); [C8375-DS-1](#c8375-ds-1) |
| PWR-CC1-500WDC | 500 W DC PSU | option | same |
| MEM-C83G2-16GB / MEM-C83G2-32GB | DRAM | default / upgrade | [C8375-OG-1](#c8375-og-1) Table 4 |
| M2USB-32G, SSD-M2SED-600G, SSD-M2SED-2T | M.2 storage | options | same |
| C8300-FAN-1R | fan tray (seen in inventory example) | included; not listed as an orderable option | [C8375-SCG-1](#c8375-scg-1) ch. 14 |
| C8300-RM-19-1R; C8300-RM-23-1R, C8300-RM-4PT-1R, C8300-WM-1R | mounting kits | default / options | [C8375-OG-1](#c8375-og-1) Table 4 |
| C-RFID-NONE / C-RFID-1R | RFID | default / option | same |
| C8300-NIM-BLANK, C8300-SM-BLANK, C8300-PIM-BLANK, C-M2-BLANK | blanks | auto-included when slot empty | same |

### Optics

**Port inventory.**

| Port type | Ports | Speeds / form factor | Restrictions | Source |
| --- | --- | --- | --- | --- |
| Built-in SFP/SFP+ | Te0/0/4-0/0/5 | 1G SFP and 10G SFP+ (also 100M via GLC-GE-100FX per TMG) | SFP-10G-T-X: "Supports 1000BASE-T and 10GBASE-T modes only". No count, power, or adjacency limit found. | [C8375-TMG-1](#c8375-tmg-1); [C8375-FAQ-1](#c8375-faq-1) |
| Built-in mGig RJ-45 | Tw0/0/0-0/0/3 | 100BASE-TX, 1000BASE-T, 2500BASE-T (no 10BASE-T documented for these ports) | PoE only on 0/0/2-0/0/3 | [C8375-HIG-1](#c8375-hig-1) "Built-in interface ports" |
| C-NIM-WAN-2X | 2 | 1G SFP / 10G SFP+ | GLC-TE: "Supports 1000BASE-T and 100MBASE-T data rates only"; SFP-10G-T-X: 1000BASE-T and 10GBASE-T only | [C8375-TMG-2](#c8375-tmg-2) |
| C-NIM-WAN-4S | 4 | 1G SFP | GLC-TE: 1000BASE-T and 100BASE-T only | [C8375-TMG-3](#c8375-tmg-3) |
| C-NIM-4X | 4 | 1G SFP / 10G SFP+ | as C-NIM-WAN-2X | [C8375-TMG-4](#c8375-tmg-4) |
| C-SM-16P4M2X | 2 SFP/SFP+ uplink-type ports (per front-panel figure labels "1G/10G SFP/+") | not verified | C-SM-16P4M2X not found in TMG autosuggest | [C8375-HIG-1](#c8375-hig-1) Figure 72 |

Module-port optics lists come from TMG entries for the module PID, which TMG
files under product family "C8300". They are **not host-specific**: they do
not prove the same optic works when the module sits in a C8375-E-G2.

**Minimum set** (TMG, platform filter C8375-E-G2 and module filters; accessed
2026-10-30; non-exhaustive). Min release shown is TMG's "Min Software
Support".

| Item | Built-in SFP/SFP+ (C8375-E-G2) | C-NIM-WAN-2X | C-NIM-WAN-4S | C-NIM-4X |
| --- | --- | --- | --- | --- |
| 1000BASE-SX | GLC-SX-MMD, MMF, up to 1000 m on OM3/OM4 (550 m OM2), 17.15.3 | GLC-SX-MMD, 17.18.1 | GLC-SX-MMD, 17.18.1 | GLC-SX-MMD, 17.11.1 |
| 1000BASE-LX/LH | GLC-LH-SMD; GLC-LX-SM-RGD; SMF 10 km; 17.15.3. GLC-GE-DR-LX (10 km) from 17.18.2 | same PIDs, 17.18.1 | same, 17.18.1 | same, 17.11.1 |
| 1000BASE-ZX | GLC-ZX-SMD, SMF 70 km, 17.15.3 | GLC-ZX-SMD | GLC-ZX-SMD | GLC-ZX-SMD |
| 1000BASE-T copper SFP | GLC-TE, Cat5e/6A 100 m, 17.15.3 (speed note: none on chassis entry) | GLC-TE (100M/1G only) | GLC-TE (100M/1G only) | GLC-TE (100M/1G only), 17.18.1 |
| 10GBASE-SR | SFP-10G-SR (17.15.3), SFP-10G-SR-S (17.18.2); MMF 400 m on OM4/OM5 | SFP-10G-SR, -SR-S | n/a (1G only) | SFP-10G-SR, -SR-S |
| 10GBASE-LR | SFP-10G-LR (17.15.3), SFP-10G-LR-S (17.18.2); SMF 10 km | SFP-10G-LR, -LR-S | n/a | SFP-10G-LR, -LR-S |
| 10GBASE-ER | SFP-10G-ER (17.15.3), SFP-10G-ER-S (17.18.2); SMF 40 km | SFP-10G-ER, -ER-S | n/a | SFP-10G-ER, -ER-S |
| 10GBASE-ZR | SFP-10G-ZR-I, SMF 70 km, 17.18.2 (no optical traffic below -28 C at cold start); DWDM-SFP10G-C-S also listed as 10GBASE-ZR (DWDM, not reviewed) | SFP-10G-ZR-I, 17.18.2 | n/a | SFP-10G-ZR-I, 17.18.2 |
| 10GBASE-T copper SFP+ | SFP-10G-T-X, 30 m on Cat6A/7 at 10G (100 m at 1G), 1G/10G modes only, 17.15.3 | SFP-10G-T-X (1G/10G only) | n/a | SFP-10G-T-X (1G/10G only) |
| 10G DAC | SFP-H10GB-CU2M/3M/4M/5M (passive; CU3M/CU5M version -02 or later), SFP-H10GB-ACU7M/ACU10M (active); AOC 1-10 m also listed | SFP-H10GB-ACU7M/ACU10M | n/a | SFP-H10GB-ACU7M/ACU10M |
| 1G DAC | not verified (no 1G DAC in TMG result) | not verified | not verified | not verified |

Long-reach restrictions found: only the SFP-10G-ZR-I cold-start temperature
note and its 17.18.2 minimum. No port, count, or power restriction on ZX, ER,
or ZR optics appeared in the sources checked.

**Ports faster than 10G.** None. The chassis has no SFP28/QSFP ports, and no
module on the C8375-E-G2 lists checked offers more than 10G
([C8375-DS-1](#c8375-ds-1); [C8375-OG-1](#c8375-og-1) Table 7).

**Copper SFPs (direct answer).**

| Port type | 1G copper SFP (1000BASE-T) | 10G copper SFP+ (10GBASE-T) |
| --- | --- | --- |
| Built-in SFP/SFP+ | **yes**: GLC-TE, 100 m; speeds negotiated on this chassis not noted in TMG (100 Mb not verified) | **yes**: SFP-10G-T-X, 30 m at 10G / 100 m at 1G; 1000BASE-T and 10GBASE-T only (no 100 Mb); count/thermal limits not found |
| C-NIM-WAN-2X | **yes**: GLC-TE, 100M and 1G only | **yes**: SFP-10G-T-X, 1G/10G only |
| C-NIM-WAN-4S | **yes**: GLC-TE, 100M and 1G only | no SFP+ cages (1G-only module) |
| C-NIM-4X | **yes**: GLC-TE, 100M and 1G only | **yes**: SFP-10G-T-X, 1G/10G only |
| C-SM-16P4M2X | not verified | not verified |

The built-in RJ-45 ports meet a 100M/1G/2.5G copper need directly (100 m
Cat5e class cabling per the HIG's Ethernet cabling section), without copper
SFPs, but they cannot do 10G copper and all four are WAN ports
([C8375-HIG-1](#c8375-hig-1)). The C-NIM-8T/8M switch NIMs add 100M/1G(/2.5G)
copper ports ([C8375-OG-1](#c8375-og-1) Table 7).

**Platform policy.** The IOS XE `show version` banner on this platform states
that when a fault "can be traced to the use of third-party transceivers ...
Cisco may withhold support under warranty or a Cisco support program" and may
require Cisco transceivers to be installed for diagnosis
([C8375-SCG-1](#c8375-scg-1) ch. 7, `show version` example). The HIG says "Use
only supported SFP/SFP+ modules on the platform", and the SFP link LED turns
amber when "The SFP is not supported" ([C8375-HIG-1](#c8375-hig-1)). Whether
`service unsupported-transceiver` exists on this platform: **not verified**
(not found in the configuration guide or other sources checked). DOM: TMG marks
"DOM Capable: Y" with DOM support from IOS XE 17.15.3 (17.18.2 for the -S
variants and SFP-10G-ZR-I) for the optical SFP/SFP+ entries. DACs, AOCs,
GLC-TE, SFP-10G-T-X, and GLC-GE-100FX show no DOM capability
([C8375-TMG-1](#c8375-tmg-1)). The CLI to display DOM on this platform was not
found in exact-platform sources (see Appendix A).

Compatibility tool: Cisco Optics-to-Device Compatibility Matrix (TMG),
<https://tmgmatrix.cisco.com/>, product filter "C8375-E-G2" (product family
"8300 Secure Router"), 41 results, accessed 2026-10-30. The ordering guide
points to this matrix for supported optics ([C8375-OG-1](#c8375-og-1) Step 5).

#### Not reviewed in this research

| Optics family | Status |
| --- | --- |
| CWDM | needed, not reviewed in this research |
| DWDM | needed, not reviewed in this research |
| BiDi | needed, not reviewed in this research |
| Extended-temperature (industrial) | needed, not reviewed in this research |

### Module reuse across the four platforms

All units are new purchases, so this is informational only.

- **From ISR4431 / Catalyst 8300 (C8300-1N1S-4T2X, C8300-1N1S-6T) to the
  C8375-E-G2:** only PIDs on a C8375-E-G2 list can be considered. Those that
  also appear on the Catalyst 8300 datasheet list are C-NIM-4X, C-NIM-8T,
  C-NIM-8M, C-SM-16P4M2X, C-SM-NIM-ADPT, the NIM/SM-X analog voice modules,
  serial/async NIMs, SM-X-64A, NIM-VAB-A, and SM-X-1T3/E3. DSL and T3/E3 stop
  at 17.18.1 on the C8375-E-G2, and voice modules need 26.1 or 26.2
  ([C8375-OG-1](#c8375-og-1); [C8375-C83DS-1](#c8375-c83ds-1); [C8375-FAQ-1](#c8375-faq-1)).
  **Not reusable or not verified:** PVDM4/SM-X-PVDM (documented unsupported),
  NIM-ES2-4/8/8-P, C-NIM-1X, C-NIM-1M, C-NIM-2T, C-SM-40P8M2X, and UCS-E (not
  on any C8375-E-G2 list checked). ISR4431-specific modules were not checked
  against the ISR4431's own lists here; see that model's file.
- **From the C8375-E-G2 to the Catalyst 8300 models:** C-NIM-WAN-2X/4S are not
  on the Catalyst 8300 datasheet module list read here. Memory (MEM-C83G2-*)
  and SSD (SSD-M2SED-*) PIDs are platform-specific.
- Matching slot names (NIM/SM/PIM) do not prove compatibility. Per-release
  support on the other chassis must come from that chassis's file.

## Platform-specific caveats

| Item | Affected | Impact | Fix / mitigation | Source |
| --- | --- | --- | --- | --- |
| CSCww15035: UTD high QFP utilization, drops near 700-742 Mbps (regression from 3.2 Gbps on 17.18.x) | C8375-E-G2, IOS XE 26.1/26.2 | severe UTD throughput loss | listed as resolved in 26.2.x release notes; confirm fixed-in version | [C8375-RN-1](#c8375-rn-1) |
| CSCwu39475: reload due to IOSd DBAL segfault in LLDP after SD-WAN template push | C8375-E-G2, open in 17.18.3a | reload in controller mode | none stated; 17.18.4 lists no customer-impacting open bugs | [C8375-RN-2](#c8375-rn-2) |
| Day-0 Enforcement throttles crypto to 250 Mbps until Advantage is AUTHORIZED | all 8000 Series Secure Routers, 17.18.1a+ autonomous | Day-0 Essentials/new deployment is capped; existing Advantage upgrade remains Day-N/unthrottled | Distinguish the pre-upgrade license and resulting state; prepare SLR/authorization for Day-0 cases, not every Advantage upgrade | [C8375-LIC-1](#c8375-lic-1) |
| DSL NIMs and SM-X-1T3/E3: last supported release 17.18.1 | C8375-E-G2 | usable at the 17.15.5 basis; 17.18.1 is the stated last-supported release, not the whole 17.18.x train | plan replacement before exceeding the stated 17.18.1 ceiling | [C8375-FAQ-1](#c8375-faq-1) |
| Fan tray not hot-swappable | 8300/8200 Secure Routers | power-down needed to replace fans | plan maintenance | [C8375-FAQ-1](#c8375-faq-1) |
| No L2 EtherChannel on onboard ports (only via C-SM-16P4M2X); L3 EtherChannel LACP only | C8375-E-G2 | design constraint for LAN bundling | use C-SM-16P4M2X | [C8375-FAQ-1](#c8375-faq-1) |
| Mode change autonomous to controller erases startup config and NVRAM certificates; SLR code not auto-returned | C8375-E-G2 | config/licensing loss if done casually | back up config; return SLR manually | [C8375-SCG-1](#c8375-scg-1); [C8375-LIC-1](#c8375-lic-1) |
| 26.2 security defaults (RADIUS Message-Authenticator, web server off, proxy ARP off, insecure-protocol warnings) | 8000 Series Secure Routers, 26.2.1 | may break legacy RADIUS/ISE or management setups after upgrade | review before upgrade | [C8375-RN-1](#c8375-rn-1) |
| Cisco-suggested release on a train past End-of-Sale | 17.15.5 suggested; 17.15.x End-of-Sale 2026-03-30, End of SW Maintenance 2027-03-30 | an upgrade to 17.18.x or 26.x is needed within the support life, bringing Day-0 Enforcement and module changes | plan the 17.18.x/26.x move and offline licensing (SLR) together | [C8375-SWD-1](#c8375-swd-1); [C8375-EOL-2](#c8375-eol-2) |
| Field notices | - | none found in sources checked | - | [C8375-SUP-1](#c8375-sup-1) (no field notice section content) |
| cisco-sa-hardening-iosxe-V8NMuMZJ (IOS XE Security Hardening Release, August 2026; Critical, CVSS 9.8; CVE-2026-20267 to -20273) | IOS XE in autonomous or controller mode "regardless of device configuration"; the advisory does not name the 8000 Series Secure Routers | seven vulnerability classes; "not known to be actively exploited"; no workarounds | first fixed: 17.15.6, 17.18.4/17.18.4a, 26.1.2. **The 17.15.5 basis is below the first fixed 17.15.x release** (affected, **inferred**: the advisory does not list this platform); 17.15.6 is on the download page. 26.2.1 is not listed | [C8375-PSIRT-1](#c8375-psirt-1); [C8375-SWD-1](#c8375-swd-1) |
| Other security advisories | - | exhaustive PSIRT review not attempted (decision-relevant check only) | run Cisco Software Checker for the chosen release | - |

Serial-number or hardware-revision dependencies: none found.

**Closest sibling SKU (C8355-G2).** The C8355-G2 is fixed (no NIM/SM, only a
PIM), has 4 x 10G SFP/SFP+, 4 x 5G mGig, and 2 x 1G RJ-45 (including LAN and
flex ports), 12 CPU cores, fixed 16 GB DRAM, an external 110 W PSU (230 W AC +
PoE option, 120 W PoE), and a 17.18.1 minimum release. It is listed with lower
SD-WAN (8.7 Gbps) and Threat Protection (3.9 Gbps) figures than the C8375-E-G2
(12 and 7 Gbps). Forwarding and IPsec figures are the same (38 and 20 Gbps).
Both are Large platform class and share license PIDs
([C8375-DS-1](#c8375-ds-1) Tables 5-6; [C8375-SCG-1](#c8375-scg-1) Table 1;
[C8375-LIC-1](#c8375-lic-1)).

## Appendix A: identification and inventory commands

Privilege: privileged EXEC (`#`) for all commands below. Commands are taken
from the exact-platform guides cited. None were run on hardware for this
research.

**Model, PID/VID, serial, IOS XE version, mode, inventory, environment**
([C8375-SCG-1](#c8375-scg-1) ch. 7 and ch. 14):

```text
show version
! Model, IOS XE version, "Router operating mode: Autonomous", license level, crypto throughput line
show inventory
! PID/VID/SN for chassis, PSUs, fan tray, PoE modules, transceivers
show platform
! Slot/module and PSU state (POE0/POE1, PSU ok/fail)
show platform diag
! Operational state of major hardware components
show diag all eeprom
! EEPROM data for chassis, PSUs, PoE modules
show environment
! Temperature, voltage, power sensors
show environment all
! Full sensor listing
show power
! Main PSU and PoE module mode (Redundant/Boost) and power available
show power inline
! Per-port PoE status
show interfaces summary
! Interface list (Tw0/0/0-3, Te0/0/4-5, module ports)
show platform software status control-processor brief
! Control-plane CPU/memory health
```

**Install/bundle mode** ([C8375-SCG-1](#c8375-scg-1) ch. 7, install command
table):

```text
show install summary
! Overview of the installed image (install mode)
show install active
! Active packages
show install log
! Install operation history
```

**ROMMON** ([C8375-RN-1](#c8375-rn-1) ROMMON upgrade steps):

```text
show rom-monitor r0
! Current ROMMON version, to compare with release-note minimums
```

**Licensing, UDI, reporting/reservation status, throughput level**
([C8375-LIC-1](#c8375-lic-1); `show license udi` from
[C8375-HIG-1](#c8375-hig-1) "Locate product identification details"):

```text
show license udi
! Chassis UDI (PID + SN) used for licensing
show license summary
! Licenses in use, tag, status; reservation-specific output is above the 17.15.5 basis
show platform hardware throughput crypto
! Whether crypto is rate limited, boot level, current mode
show running-config | include license
! Configured license boot level and UDI line
```

**Above basis — SLR and Day-0 inspection, autonomous IOS XE 17.18.1a or
later.** These commands and expected outputs are documented in later-feature
workflows, not verified at the 17.15.5 basis. They are kept out of the basis
capture block; this is an evidence limit, not a claim that the parser
rejects them on 17.15.5 ([C8375-LIC-1](#c8375-lic-1), "Verify Specific License
Reservation" and "Determining the compliance status of a device"):

```text
show license reservation
! Above basis: SLR status, reserved licenses, term start/end dates
show license tech support | section Device
! Above basis: Day-0 / Day-N enforcement state
show license tech support | include Day-
! Above basis: Day-0 verification lines
```

Not included (unverified for this platform/release): a DOM display command
(for example `show interfaces transceiver`), and `show license all` /
`show license status` / `show license usage`. These are common IOS XE syntax,
but no exact-platform source read here shows them. Install-mode
detection in `show version` output was not confirmed.

Paste-ready capture block (read-only `show` commands only):

```text
terminal length 0
show version
show inventory
show platform
show platform diag
show diag all eeprom
show environment all
show power
show power inline
show interfaces summary
show platform software status control-processor brief
show install summary
show install active
show rom-monitor r0
show license udi
show license summary
show platform hardware throughput crypto
show running-config | include license
```

Redact serial numbers and UDIs before sharing any output.

## References

#### C8375-MSR-1

- Title: IP Multicast Configuration Guide, Cisco IOS XE, “Implementing Multicast Service Reflection”
- Used for: generic IOS XE MSR configuration, prerequisites, Vif restrictions, and feature introduction information; not exact C8375 validation
- URL: https://www.cisco.com/c/en/us/td/docs/routers/ios-xe/ip-multicast/ip-multicast/m_imc_service_reflect-0.html
- Accessed: 2026-11-01
- Locator: Implementing Multicast Service Reflection; Feature Information for Multicast Service Reflection
- Local PDF: not saved (HTML)

#### C8375-MSR-LIC-1

- Title: Cisco 8000 Series Secure Routers WAN and Routing License Feature Matrices
- Used for: Routing Advantage entitlement for Multicast Service Reflection in the secure-router OS feature set
- URL: https://www.cisco.com/c/m/en_us/products/software/wan-routing-licensing-feature-matrix.html
- Accessed: 2026-11-01
- Locator: Cisco 8000 Series Secure Routers OS feature matrix; Advanced Multicast row
- Local PDF: not saved (HTML)

#### C8375-MSR-PLAT-1

- Title: Cisco 8000 Series Secure Routers Licensing
- Used for: platform class assigned to C8375-E-G2; not runtime MSR validation
- URL: https://www.cisco.com/c/en/us/td/docs/routers/cloud_edge/licensing/8000-series-secure-routers-licensing.html
- Accessed: 2026-11-01
- Locator: Platform-based licensing; platform classes
- Local PDF: not saved (HTML)

Original model sources were accessed 2026-10-30; new management sources were accessed 2026-10-31 UTC as recorded per entry. Locators are section names, table numbers, or
PDF page labels as printed. The original research encountered Cisco HTTP403
refusals and used the recorded fetch/browser methods. The new Common Policy
PDF was retrieved with ordinary curl after sandbox-network escalation and
checked with `pdfinfo` and `pdftotext`; no request headers were spoofed.

#### C8375-DS-1

- Title: Cisco 8300 Series Secure Routers Data Sheet (HTML).
- Used for: models, Table 5 technical specs, Table 6 performance/scale,
  Table 7 mechanical, module list, minimum releases, warranty.
- URL: <https://www.cisco.com/c/en/us/products/collateral/routers/secure-routers/8300-series-secure-routers-ds.html>
- Revision: "Last updated: October 14, 2026"; history: created 2025-06-10,
  amended 2025-09-05.
- Accessed: 2026-10-30. Read through the web-fetch tool (summarized
  rendering; table values cross-checked in two passes).
- Official PDF:
  <https://www.cisco.com/c/dam/en/us/products/collateral/routers/secure-routers/8300-series-secure-routers-ds.pdf>,
  saved as
  [reference/c8375-e-g2-datasheet-2026-06-02.pdf](reference/c8375-e-g2-datasheet-2026-06-02.pdf)
  (PDF modified 2026-06-02; 15 pages). Retrieved 2026-10-30 with a headless
  browser (Playwright Chromium) after `curl` got HTTP 403, with the user's
  approval. The PDF is older than the HTML page: it matches the HTML on
  typical power (55 W), forwarding/IPsec/SD-WAN/Threat figures (38/20/12/7
  Gbps), weight (14.3 lb), and the 17.15.3 minimum release, but lists 3,500
  IPsec tunnels without the HTML's "4000 from 26.2.1". It has no maximum
  power or heat dissipation figures either.

#### C8375-OG-1

- Title: Cisco 8000 Series Secure Routers Ordering Guide.
- Used for: PID/description/platform class (Table 1), configurable options
  (Table 4), NIM/SM list (Table 7), cellular (Table 8), licenses (Tables 9-10),
  ordering steps, TAA note, support offers.
- URL: <https://www.cisco.com/c/en/us/products/collateral/networking/sdwan-routers/8000-secure-routers/8000-secure-router-og.html>
  (PDF: <https://www.cisco.com/c/en/us/products/collateral/networking/sdwan-routers/8000-secure-routers/8000-secure-router-og.pdf>)
- Revision: HTML "Updated: October 9, 2026"; PDF modified 2026-10-09.
- Accessed: 2026-10-30.
- Local PDF: [reference/c8000-secure-routers-og-2026-10-09.pdf](reference/c8000-secure-routers-og-2026-10-09.pdf)

#### C8375-LIC-1

- Title: Cisco 8000 Series Secure Routers Licensing.
- Used for: platform-based licensing, Large class PIDs, OS Essentials 250 Mbps,
  HSECK9 not applicable, Day-0 Enforcement, SLR workflow and CLI, device mode
  change, factory reset, show commands.
- URL: <https://www.cisco.com/c/en/us/td/docs/routers/cloud_edge/licensing/8000-series-secure-routers-licensing.html>
  (PDF: <https://www.cisco.com/c/en/us/td/docs/routers/cloud_edge/licensing/8000-series-secure-routers-licensing.pdf>)
- Revision: PDF "Revised: October 1, 2026" (the HTML page header displayed
  "Updated August 14, 2025" when fetched; the PDF revision was used).
- Accessed: 2026-10-30. Locators: section names as cited; PDF pages 1-18.
- Local PDF: [reference/c8000-secure-routers-licensing-2026-10-01.pdf](reference/c8000-secure-routers-licensing-2026-10-01.pdf)

#### C8375-LFM-1

- Title: Cisco 8000 Series Secure Routers WAN and Routing License Feature
  Matrices.
- Used for: feature-to-tier mapping (page 1 WAN Essentials/Advantage; page 2
  OS Essentials/Routing Advantage). Column membership on page 2 was confirmed
  from a rendered page image.
- URL: <https://www.cisco.com/c/dam/m/en_us/products/software/wan-routing-licensing-feature-matrix.pdf>
- Revision: document code C83-5105295-00 06/26; PDF modified 2026-09-10.
- Accessed: 2026-10-30.
- Local PDF: [reference/c8000-secure-routers-license-feature-matrix-2026-06.pdf](reference/c8000-secure-routers-license-feature-matrix-2026-06.pdf)

#### C8375-FAQ-1

- Title: Cisco 8000 Series Secure Routers FAQ.
- Used for: positioning (Table 1), minimum releases (Table 2), relationship
  to Catalyst 8300/8200, validated modules (Figure 1, page 8), ports
  (Tables 3, 8), DRAM (Table 5), PSU/PoE (Tables 6-7), OIR, EtherChannel,
  voice/vDSP/CUBE, security features.
- URL: <https://www.cisco.com/c/en/us/products/collateral/networking/sdwan-routers/8000-series-secure-routers-faq.html>
  (PDF: <https://www.cisco.com/c/en/us/products/collateral/networking/sdwan-routers/8000-series-secure-routers-faq.pdf>)
- Revision: C67-5124049-02 06/26; PDF modified 2026-06-02.
- Accessed: 2026-10-30.
- Local PDF: [reference/c8000-secure-routers-faq-2026-06.pdf](reference/c8000-secure-routers-faq-2026-06.pdf)

#### C8375-HIG-1

- Title: Hardware Installation Guide for Cisco 8300 Series Secure Routers.
- Used for: chassis views (Table 1 port numbering), built-in port speeds,
  memory, PSU table (Table 3), LEDs and PoE note (Table 4), ventilation,
  environmental (Table 7), console cables (Table 8), cabling (Table 10),
  SFP/NIM/SM/adapter procedures, UDI.
- URL: <https://www.cisco.com/c/en/us/td/docs/routers/secure-routers/sec-8300-series/hardware_installation-guide/secure-8300-series-hig.html>
  (PDF: <https://www.cisco.com/c/en/us/td/docs/routers/secure-routers/sec-8300-series/hardware_installation-guide/secure-8300-series-hig.pdf>)
- Revision: "Updated July 31, 2025" (PDF file generated 2026-07-09).
- Accessed: 2026-10-30.
- Local PDF: [reference/c8300-secure-routers-hig-2025-07-31.pdf](reference/c8300-secure-routers-hig-2025-07-31.pdf)

#### C8375-SCG-1

- Title: Cisco 8300 Series Secure Routers Software Configuration Guide.
- Used for: modes and `controller-mode` (ch. 1), CPU cores (Table 1), install
  mode (ch. 7), `show version` third-party transceiver warning (ch. 7
  examples), interfaces (ch. 8), environmental and PoE commands, PoE power
  modes (ch. 14, Table 18), tamper detection (ch. 4).
- URL: <https://www.cisco.com/c/en/us/td/docs/routers/secure-routers/sec-8300-series/software-config-guide/secure-8300-series-scg.html>
  (PDF: <https://www.cisco.com/c/en/us/td/docs/routers/secure-routers/sec-8300-series/software-config-guide/secure-8300-series-scg.pdf>)
- Revision: First Published 2025-07-31; PDF generated 2026-09-29.
- Accessed: 2026-10-30.
- Local PDF: [reference/c8300-secure-routers-scg-2026-09-29.pdf](reference/c8300-secure-routers-scg-2026-09-29.pdf)

#### C8375-RN-1

- Title: Release Notes for Cisco 8000 Series Secure Routers, Release 26.2.x.
- Used for: C8375-E-G2 feature rows (CUBE/SRST, password conversion,
  insecure-protocol warnings), BRI/E&M modules autonomous-only, NGFW V2,
  resilient-infrastructure defaults, CSCww15035, ROMMON for 26.2.1.
- URL: <https://www.cisco.com/c/en/us/td/docs/routers/secure-routers/cisco-8000-series-secure-routers-release-26-2-x.html>
- Revision: updated 2026-09-27.
- Accessed: 2026-10-30 (web-fetch summary rendering). No local PDF.

#### C8375-RN-2

- Title: Release Notes for Cisco 8300 Series Secure Routers, Release 17.18.x.
- Used for: sub-releases 17.18.1a-17.18.5, C-NIM-WAN-2X/4S (17.18.1a),
  CUBE/SRST on C8375-E-G2 (17.18.2), TACACS+ over TLS 1.3, ROMMON row,
  CSCwu39475.
- URL: <https://www.cisco.com/c/en/us/td/docs/routers/secure-routers/sec-8300-series/release-notes/17-18-x/release-notes-cisco-8300-series-secure-routers-release-17-18-x.html>
- Revision: updated 2026-10-13.
- Accessed: 2026-10-30. No local PDF.

#### C8375-RN-3

- Title: Release Notes for Cisco 8000 Series Secure Routers, Release 26.1.x.
- Used for: sub-releases 26.1.1/26.1.2, CUBE TLS features naming C8375-E-G2,
  ROMMON row for 26.1.1.
- URL: <https://www.cisco.com/c/en/us/td/docs/routers/secure-routers/cisco-8000-series-secure-routers-release-26-1-x.html>
- Revision: updated 2026-10-12.
- Accessed: 2026-10-30. No local PDF.

#### C8375-SUP-1

- Title: Cisco 8300 Series Secure Routers support (series) page.
- Used for: series release date 2025-06-09, models, EoL notices listed
  (software only), document list.
- URL: <https://www.cisco.com/c/en/us/support/routers/8300-series-secure-routers/series.html>
- Revision: not stated. Accessed: 2026-10-30.

#### C8375-EOL-1

- Title: End-of-Sale and End-of-Life Announcement for Cisco IOS XE 17.18.x
  (EOL15995).
- Used for: 17.18.x milestones and migration guidance.
- URL: <https://www.cisco.com/c/en/us/products/collateral/ios-nx-os-software/ios-xe-17/ios-xe-17-18-x-eol.html>
- Revision: 2026-10-30. Accessed: 2026-10-30. Locator: Table 1.

#### C8375-EOL-2

- Title: End-of-Sale and End-of-Life Announcement for Cisco IOS XE 17.15.x
  (EOL15772, amended).
- Used for: 17.15.x milestones and migration guidance.
- URL: <https://www.cisco.com/c/en/us/products/collateral/ios-nx-os-software/ios-xe-17/ios-xe-17-15-x-eol.html>
- Revision: announced 2025-09-30, updated 2025-10-01. Accessed: 2026-10-30.

#### C8375-EOL-3

- Title: End-of-Sale and End-of-Life Announcement for the Cisco Catalyst
  C8500L-8S4X, C8300-1N1S-4T2X, C8300-1N1S-6T (EOL15950, amended).
- Used for: C8375-E-G2 named as the migration product for C8300-1N1S-4T2X and
  C8300-1N1S-6T (added during lead-agent reconciliation).
- URL: <https://www.cisco.com/c/en/us/products/collateral/networking/sdwan-routers/catalyst-8000-edge-platforms/catalyst-c8500l-8s4x-4t2x-c8300-1n1s-6t-eol.html>
- Revision: announced 2026-07-27; page updated 2026-10-19. Accessed:
  2026-10-30.
- Locator: Table 2 (PDF p. 4).
- Local PDF: [c8300-1n1s-eol15950-2026-10-19.pdf](reference/c8300-1n1s-eol15950-2026-10-19.pdf)

#### C8375-SWLC-1

- Title: Software Lifecycle Support Statement - IOS XE.
- Used for: 26.x Extended Support policy (48 months), milestone offsets.
- URL: <https://www.cisco.com/c/en/us/products/collateral/ios-nx-os-software/ios-xe-26/bulletin-c25-2378701.html>
- Revision: updated 2026-04-10. Accessed: 2026-10-30.

#### C8375-REL-1

- Title: Recommended Releases for Catalyst 8000 Edge, ASR1000, ISR4000,
  CSR1000v and ISR1000 Platforms (document 215567).
- Used for: confirming no recommended-release row for the 8000 Series Secure
  Routers; general Extended Support guidance.
- URL: <https://www.cisco.com/c/en/us/support/docs/ios-nx-os-software/ios-xe-16/215567-recommended-releases-for-asr1000-isr400.html>
- Revision: 9.0, published 2026-06-15. Accessed: 2026-10-30.

#### C8375-SWD-1

- Title: Cisco Software Download, "8300 Secure Router Gen2", IOS XE
  Software, Release IOSXE-17.15.5 (MD).
- Used for: the "Suggested Release" designation (IOSXE-17.15.5(MD)); "Latest
  Release" list (17.18.5 MD, 26.2.1 GA, 17.15.6 MD, 26.1.2 GA); image names
  `c8kg2be-universalk9.17.15.05.SPA.bin` and
  `c8kg2be-universalk9_npe.17.15.05.SPA.bin`, release date 18-Feb-2026; the
  page's "Release Notes for C8375-E-G2" link.
- URL: <https://software.cisco.com/download/home/286338258/type/282046477/release/IOSXE-17.15.5>
  (Cisco login required; not fetched from this host).
- Evidence: user-supplied screenshot, captured 2026-10-30, saved as
  [reference/c8375-e-g2-swdownload-suggested-2026-10-30.png](reference/c8375-e-g2-swdownload-suggested-2026-10-30.png).
- Accessed: 2026-10-30 (by the user).

#### C8375-REL-2

- Title: Cisco IOS XE 26.2.1 software release support page.
- Used for: 26.2.1 release date (2026-08-31).
- URL: <https://www.cisco.com/c/en/us/support/ios-nx-os-software/ios-xe-26-2-1/model.html>
- Revision: not stated. Accessed: 2026-10-30.

#### C8375-TMG-1

- Title: Cisco Optics-to-Device Compatibility Matrix, results for C8375-E-G2.
- Used for: optics minimum set, copper SFP answers, DOM capability, notes
  (network-device note on SFP-10G-T-X; transceiver notes).
- URL: <https://tmgmatrix.cisco.com/> (product filter C8375-E-G2; the result
  and notes were retrieved from the matrix's public search, notes, and PDF
  export endpoints).
- Revision: live data, 41 records. Accessed: 2026-10-30. Non-exhaustive.
- Local PDF (matrix PDF export):
  [reference/c8375-e-g2-tmg-optics-2026-10-30.pdf](reference/c8375-e-g2-tmg-optics-2026-10-30.pdf)

#### C8375-TMG-2

- Title: Cisco Optics-to-Device Compatibility Matrix, results for C-NIM-WAN-2X.
- Used for: module-port optics and copper SFP notes (31 records).
- URL: <https://tmgmatrix.cisco.com/> (product filter C-NIM-WAN-2X).
- Accessed: 2026-10-30. Module-level, not host-specific.
- Local PDF: [reference/c-nim-wan-2x-tmg-optics-2026-10-30.pdf](reference/c-nim-wan-2x-tmg-optics-2026-10-30.pdf)

#### C8375-TMG-3

- Title: Cisco Optics-to-Device Compatibility Matrix, results for C-NIM-WAN-4S.
- Used for: module-port optics (16 records).
- URL: <https://tmgmatrix.cisco.com/> (product filter C-NIM-WAN-4S).
- Accessed: 2026-10-30. Module-level, not host-specific.
- Local PDF: [reference/c-nim-wan-4s-tmg-optics-2026-10-30.pdf](reference/c-nim-wan-4s-tmg-optics-2026-10-30.pdf)

#### C8375-TMG-4

- Title: Cisco Optics-to-Device Compatibility Matrix, results for C-NIM-4X.
- Used for: module-port optics (31 C-NIM-4X records, read through the matrix
  API on 2026-10-30).
- URL: <https://tmgmatrix.cisco.com/> (product filter C-NIM-4X).
- Accessed: 2026-10-30. Module-level, not host-specific.
- Local PDF (reused; saved by another subagent, contains the C-NIM-4X rows):
  [reference/c8300-nim-1x-4x-2t-tmg-optics-2026-10-30.pdf](reference/c8300-nim-1x-4x-2t-tmg-optics-2026-10-30.pdf)

#### C8375-SLP-1

- Title: Smart Licensing Using Policy for Cisco Enterprise Routing Platforms
  (chapters "Information About Smart Licensing Using Policy" and "How Smart
  Licensing Using Policy Works").
- Used for: family-level disconnected topologies (CSLU disconnected, SSM
  On-Prem offline sync, no-connectivity file exchange) and default policy
  Table 4. **Does not name the 8000 Series Secure Routers**; applied here only
  as labeled family-level context.
- URL: <https://www.cisco.com/c/en/us/td/docs/routers/sl_using_policy/b-sl-using-policy/info_about.html>;
  <https://www.cisco.com/c/en/us/td/docs/routers/sl_using_policy/b-sl-using-policy/m-sle-how-smart-licensing-using-policy-works.html>
- Revision: chapters last updated 2023-08-01. Accessed: 2026-10-30.
- Local PDF (reused, saved by another subagent):
  [reference/enterprise-routing-slp-guide-2023-08-01.pdf](reference/enterprise-routing-slp-guide-2023-08-01.pdf)

#### C8375-PSIRT-1

- Title: Cisco IOS XE Software Security Hardening Release: August 2026
  (cisco-sa-hardening-iosxe-V8NMuMZJ).
- Used for: CVEs, severity, affected scope, first fixed releases.
- URL: <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-iosxe-V8NMuMZJ>
- Revision: version 1.1 (Final), first published 2026-08-05, updated
  2026-10-02. Accessed: 2026-10-30. Locator: "Affected Products", "Fixed
  Software". No local PDF.

#### C8375-C83DS-1

- Title: Cisco Catalyst 8300 Series Edge Platforms Data Sheet.
- Used for: list-level comparison of module, memory, storage, fan, and PSU PIDs
  with the C8375-E-G2 (Table 7, accessories, Table 9 and PSU notice).
- URL: <https://www.cisco.com/c/en/us/products/collateral/routers/catalyst-8300-series-edge-platforms/datasheet-c78-744088.html> (official equivalent; preserved local copy read).
- Revision: PDF modified 2026-10-06. Accessed (local read): 2026-10-30.
- Local PDF (reused, saved by another subagent):
  [reference/c8300-edge-datasheet-2026-10-06.pdf](reference/c8300-edge-datasheet-2026-10-06.pdf)

#### C8375-MGMT-CC-DS-1

- Title: Cisco Catalyst Center 2.3.7 Data Sheet.
- Used for: Physical/virtual deployment, management functions and device-subscription distinction.
- URL: <https://www.cisco.com/c/en/us/products/collateral/cloud-systems-management/dna-center/nb-06-dna-center-data-sheet-cte-en.html>
- Revision: 2.3.7 data sheet; document date not verified in the page read. Accessed: 2026-10-31 UTC.
- Locator: Licensing introduction; Appliance scale.
- Local PDF: not saved; HTML read.

#### C8375-MGMT-CC-VA-1

- Title: Catalyst Center Virtual Appliance Ordering Guide.
- Used for: DN-SW-APL-LIC, Smart Account registration and ESXi/AWS/Azure image choices.
- URL: <https://www.cisco.com/c/en/us/products/collateral/networking/catalyst-center/catalyst-center-virtual-appliance-og.html>
- Revision: Updated 2025-12-16. Accessed: 2026-10-31 UTC.
- Locator: Catalyst Center Virtual Appliance license, Table 2, registration steps.
- Local PDF: not saved; HTML read.

#### C8375-MGMT-CC-AIR-1

- Title: Cisco Catalyst Center Virtual Air Gap Deployment Guide.
- Used for: Physical/ESXi air-gap enablement, TAC workflow, address allow lists and manual upgrade packages.
- URL: <https://www.cisco.com/c/en/us/td/docs/cloud-systems-management/network-automation-and-management/catalyst-center/articles/virtual_air_gap_deployment/cisco-catalyst-center-virtual-air-gap-deployment-guide.html>
- Revision: Not stated in the page read. Accessed: 2026-10-31 UTC.
- Locator: Deployment workflow; installation prerequisites; physical appliance deployment; virtual appliance deployment on ESXi.
- Scope: The upgrade example is 3.1.x to 3.x.x; the ESXi support statement also names 2.3.7.x. This is not a generic 2.3.7 upgrade procedure.
- Local PDF: not saved; HTML read.

#### C8375-MGMT-CC-ADM-1

- Title: Cisco Catalyst Center Administrator Guide, Release 2.3.7.x — Manage Licenses.
- Used for: Device License Manager connectivity, On-Prem SSM RUM restriction and separate manual device SLR workflow.
- URL: <https://www.cisco.com/c/en/us/td/docs/cloud-systems-management/network-automation-and-management/catalyst-center/2-3-7/admin_guide/b_cisco_catalyst_center_admin_guide_237/b_cisco_dna_center_admin_guide_2_3_7_chapter_0101.html>
- Revision: Updated 2026-07-03. Accessed: 2026-10-31 UTC.
- Locator: Integration with Cisco Smart Accounts; Change license level; Enable SLR or PLR when the devices and Catalyst Center are not connected to CSSM.
- Scope: Generic device SLR workflow does not establish C8375 support at the 17.15.5 basis.
- Local PDF: not saved; HTML read.

#### C8375-MGMT-CC-SYS-1

- Title: Cisco Catalyst Center 2.3.7.x on ESXi Administrator Guide — Configure System Settings.
- Used for: Appliance Smart Licensing connection modes, On-Prem registration and ISE/ERS/pxGrid inventory integration.
- URL: <https://www.cisco.com/c/en/us/td/docs/cloud-systems-management/network-automation-and-management/catalyst-center/catalyst-center-va/esxi/2-3-7/Admin_Guide/b_cisco_catalyst_center_va_esxi_admin_guide_237x/m_va_esxi_admin_system_settings.html>
- Revision: Updated 2026-07-07. Accessed: 2026-10-31 UTC.
- Locator: Smart Licensing; Configure connection mode; Catalyst Center and Cisco ISE integration.
- Local PDF: not saved; HTML read.

#### C8375-MGMT-CC-MX-1

- Title: Cisco Catalyst Center Compatibility Matrix; public application data.
- Used for: Exact platform entries for ISR 4431, both C8300 1N1S PIDs and C8375-E-G2 at selected Center 2.3.7.11.
- URL: <https://www.cisco.com/c/dam/en/us/td/docs/Website/enterprise/catalyst_center_compatibility_matrix/index.html>
- Revision: Live data; no per-row revision stated. Accessed: 2026-10-31 UTC.
- Locator: DNAC Compatibility Matrix → 2.3.7.11 → Router → named platform rows.
- Scope: Data URL: <https://www.cisco.com/c/dam/en/us/td/docs/Website/enterprise/catalyst_center_compatibility_matrix/resources/data-min.json>, linked by the page's js/data-dnac.js. Downloaded JavaScript was read, never executed. Train listings do not override a documented platform ceiling.
- Local evidence: [original JSON](reference/catalyst-center-compatibility-matrix-accessed-2026-10-31.json); [selected rows and retrieval provenance](reference/catalyst-center-compatibility-selected-2026-10-31.json).

#### C8375-MGMT-SDW-DS-1

- Title: Cisco Catalyst SD-WAN Data Sheet.
- Used for: Customer-hosted/Cisco-hosted/cloud-delivered deployment and Secure Router WAN licensing distinction.
- URL: <https://www.cisco.com/c/en/us/solutions/collateral/enterprise-networks/sd-wan/nb-06-sd-wan-ds-cte-en.html>
- Revision: Updated 2026-07-27. Accessed: 2026-10-31 UTC.
- Locator: Flexible deployment models meet your needs; Unified Licensing for WAN (Cisco 8000 Series Secure Routers Only).
- Local PDF: not saved; HTML read.

#### C8375-MGMT-SDW-FAQ-1

- Title: Cisco Catalyst Software-Defined WAN (SD-WAN) FAQ.
- Used for: DNA subscription includes centralized cloud/on-prem Manager use and term-based SD-WAN entitlement on legacy families.
- URL: <https://www.cisco.com/c/en/us/solutions/collateral/enterprise-networks/sd-wan/nb-06-sw-defined-wan-faq-cte-en.html>
- Revision: Not stated in the page read. Accessed: 2026-10-31 UTC.
- Locator: Ordering and licensing; subscription component table; software-stack entitlements.
- Scope: Use C8375-specific ordering evidence for its newer WAN/Routing offers rather than carrying old DNA tiers across.
- Local PDF: not saved; HTML read.

#### C8375-MGMT-SDW-SLP-1

- Title: Deploying Smart Licensing Using Policy in Cisco Catalyst SD-WAN.
- Used for: Manager Offline Mode, minima, manual file roundtrip, cadence/compliance alert and On-Prem prerequisites/24-hour sync.
- URL: <https://www.cisco.com/c/en/us/td/docs/routers/sdwan/configuration/licensing/deploying-smart-licensing-using-policy-in-cisco-catalyst-sd-wan.html>
- Revision: Page date not stated in the text read; feature-history table names releases. Accessed: 2026-10-31 UTC.
- Locator: Feature history; Information About Offline Mode; Prerequisites for Cisco SSM On-Prem; Information About Cisco SSM On-Prem.
- Scope: Manager license assignment/reporting is distinct from autonomous router SLR and subscription-term obligations.
- Local PDF: not saved; HTML read.

#### C8375-MGMT-SDW-GS-1

- Title: Cisco Catalyst SD-WAN Getting Started Guide, IOS XE Release 17.x — Overlay Network Bring-Up Process.
- Used for: Local control-component VMs on KVM/ESXi, uploaded serial list, manual/enterprise certificate workflow.
- URL: <https://www.cisco.com/c/en/us/td/docs/routers/sdwan/configuration/sdwan-xe-gs-book/cisco-sd-wan-overlay-network-bringup.html>
- Revision: Not stated in the page read. Accessed: 2026-10-31 UTC.
- Locator: Create Cisco Catalyst SD-WAN Manager VM Instance on KVM; Configure Automatic or Manual Authorization; Place Routers in Valid State.
- Scope: No deployment was tested. Image repository and CA procedures must be chosen for the selected release.
- Local PDF: not saved; HTML read.

#### C8375-MGMT-ISE-1

- Title: Cisco Common Policy Integration Guide.
- Used for: Center/Manager ISE integration, SGT/IP binding exchange and identity-firewall minimum release.
- URL: <https://www.cisco.com/c/en/us/td/docs/cloud-systems-management/network-automation-and-management/catalyst-center/cisco-validated-solution-profiles/common-policy-integration-guide.pdf>
- Revision: 2026-01-14, printed on PDF page 1. Accessed: 2026-10-31 UTC.
- Locator: Printed/PDF pages 26–27, ISE integration with Catalyst Center and SD-WAN Manager.
- Scope: Validated solution-level evidence does not prove every exact-router enforcement feature.
- Local evidence: [PDF](reference/common-policy-integration-guide-accessed-2026-10-31.pdf); [text companion](reference/common-policy-integration-guide-accessed-2026-10-31.pdf.md).

### References - unresolved

Inaccessible URLs: none remain. The datasheet PDF, previously listed
here, was retrieved later ([C8375-DS-1](#c8375-ds-1)).

Not attempted (expected to need login or tools not available in this run):
Cisco Software Checker (interactive tool) for 17.15.5 and 26.2.1. The
Software Download page's suggested-release marker was later supplied by the
user as a screenshot ([C8375-SWD-1](#c8375-swd-1)); Cisco Commerce pricing.

Required claims with no source found (sought but not found):

- Maximum power consumption and heat dissipation (BTU/hr).
- Fully disconnected Catalyst Center VA activation for the selected On-Prem server combination; quoted appliance-license enforcement and exact manager sizing for unspecified site count. Management sources were read; these are evidence/design gaps.
- Behavior when an SLR-reserved term license reaches its end date; the SLR
  approval process and lead time.
- Reporting cadence for CSLU/SSM On-Prem disconnected operation on this
  platform (the "CONDITIONALLY-ENFORCED" license type is not in the
  family-level policy table).
- `service unsupported-transceiver` availability; DOM display command for this
  platform.
- SXP support (the matrix prints "SGX"); MAB; which ports support 802.1X.
- C-SM-16P4M2X optics list (not in TMG autosuggest).
- Whether the default order includes one or two PWR-CC1-400WAC PSUs.
- Fixed-in release for CSCww15035.
- Openly published US pricing.

Source conflicts recorded:

- IPsec "up to 30 Gbps" for the 8300 Series (FAQ Table 1) vs 20 Gbps for the
  C8375-E-G2 (datasheet Table 6). The datasheet value is used.
- "C-NIM-WAN-4SP" (FAQ Figure 1) vs "C-NIM-WAN-4S" (ordering guide, datasheet,
  TMG, 17.18.x release notes). The ordering guide PID is used.
- UCS-E listed as a capability of the 8300 Series (FAQ text) vs absent from
  every C8375-E-G2 module list. Left unresolved; UCS-E treated as not
  verified.
- Licensing guide revision: HTML header 2025-08-14 vs PDF "Revised: October 1,
  2026". The PDF is used.
- USB console connector: datasheet "Micro-USB" vs HIG cable table "5-pin mini
  USB Type-B". Unresolved; inspect physically.
- Routing Advantage term: licensing guide "84-month subscription period" vs
  FAQ "flexible 12- to 84-month term" (FAQ wording is about the Networking
  Subscription for SD-WAN). Confirm term options in a quote.
