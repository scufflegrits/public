# Cisco C8300-1N1S-4T2X: Model Research (r1.1.0)

Standalone research file for model 2 of
`request-cisco-comparison-r1.1.0.md`. Written for a new-purchase, multi-site
enterprise branch / WAN edge deployment in autonomous mode, managed by CLI,
with Cisco ISE and **no internet connectivity for license reporting**.

## Research status

| Item | Status |
| --- | --- |
| Revision | r1.1.0; 2026-10-30 America/Chicago (continuation access dates recorded separately). Review corrections and completion of previously unattempted public-source work. |
| Research cutoff date | 2026-10-30 America/Chicago. Original sources accessed 2026-10-30; completion review accessed additional public sources 2026-10-31 UTC (still 2026-10-30 America/Chicago). Individual registers retain their actual access dates. |
| Confirmed identity | `C8300-1N1S-4T2X`, Cisco Catalyst 8300 Series Edge Platforms (1RU, 2×10G SFP+ and 4×1G RJ-45, 1 NIM, 1 SM, 1 PIM). Supplied as "8300-1S1N-4T2X"; the slot order was reversed. Confirmed in [C8300-4T2X-DS-1](#c8300-4t2x-ds-1), [C8300-4T2X-OG-1](#c8300-4t2x-og-1), [C8300-4T2X-HIG-1](#c8300-4t2x-hig-1), and [C8300-4T2X-EOL-1](#c8300-4t2x-eol-1). |
| **Lifecycle alert** | **The request's "Current" status is out of date.** Cisco announced End-of-Sale for `C8300-1N1S-4T2X` on 2026-07-27 in EOL15950 (amended, page updated 2026-10-19). End-of-Sale is 2027-01-31 and Last Date of Support is 2032-01-31. The named migration product is `C8375-E-G2`. **As of 2026-10-30 the chassis can still be ordered new, until 2027-01-31.** The sibling `C8300-1N1S-6T` is in the same bulletin. See [Lifecycle status](#lifecycle-status). |
| Software basis | **Cisco IOS XE 17.15.6** (Extended-Support train 17.15.x). The Cisco TAC recommended-release document (215567, rev. 9.0, 2026-06-15) lists "17.12.8 or 17.15.6" for the Catalyst 8300 family. 17.15.6 was chosen because the 17.12.x End of SW Maintenance Releases date (2026-03-30) has already passed. Newest available release: 26.2.1 (release notes updated 2026-09-27). Documented ceiling: the 28.2.x train (EOL15950). See [Software](#software). |
| Operating mode | Autonomous mode (CLI) is the baseline. Controller mode (Catalyst SD-WAN) is supported on the same image; differences are called out where documented. |
| Run status | **Complete**, with explicit evidence gaps. Required public-source research and the r1.1.0 correction pass are complete. The decision-relevant review read advisory applicability/fixed-release sections, the HIG power/FRU chapters, and module authentication evidence; it is not an exhaustive vulnerability assessment. |
| Not attempted | No required public-source research remains unattempted. Login-gated Software Download dates, Feature Navigator, Bug Search Tool and Commerce/partner quotes were not accessed; these are evidence/tool limitations, not verified findings. Extended installation procedures and unrelated sibling configurations are outside the decision-relevant review. |
| Material evidence gaps | Family license-matrix applicability and the TrustSec SGT tier conflict remain labeled; third-party optics policy, DOM display syntax, SLP missed-deadline feature effects, maximum power/heat and published US prices remain unverified. **802.1X/MAB is documented on C-SM-16P4M2X copper ports**; other modules remain unverified ([C8300-4T2X-SMSW-1](#c8300-4t2x-smsw-1)). |

## Contents

- [Research status](#research-status)
- [Summary](#summary)
  - [Key takeaways](#key-takeaways)
  - [Uncertainty that could change the decision](#uncertainty-that-could-change-the-decision)
- [Lifecycle status](#lifecycle-status)
  - [Chassis and accessory notice](#chassis-and-accessory-notice)
  - [Bundle notice](#bundle-notice)
  - [Software-train notices](#software-train-notices)
- [Hardware specifications](#hardware-specifications)
  - [Power supplies](#power-supplies)
  - [Hyperthreading and core allocation](#hyperthreading-and-core-allocation)
- [Performance](#performance)
  - [Published throughput](#published-throughput)
  - [Published scale](#published-scale)
- [Software](#software)
  - [Release table](#release-table)
  - [Install mode, bundle mode, and operating modes](#install-mode-bundle-mode-and-operating-modes)
- [Licensing](#licensing)
  - [Licensing layers that apply](#licensing-layers-that-apply)
  - [Table 1: Feature entitlement](#table-1-feature-entitlement)
  - [Table 2: Throughput and crypto](#table-2-throughput-and-crypto)
  - [Table 3: Purchase and enforcement](#table-3-purchase-and-enforcement)
  - [Offline operation (no internet for license reporting)](#offline-operation-no-internet-for-license-reporting)
  - [Controller-mode licensing callout](#controller-mode-licensing-callout)
  - [Pricing](#pricing)
- [Feature support and integration](#feature-support-and-integration)
  - [Feature matrix](#feature-matrix)
  - [Cisco ISE integration](#cisco-ise-integration)
- [Modules and expansion](#modules-and-expansion)
  - [Slot map](#slot-map)
  - [NIM modules](#nim-modules)
  - [SM-X and service modules](#sm-x-and-service-modules)
  - [PIM and cellular](#pim-and-cellular)
  - [Memory, storage, fans, and accessories](#memory-storage-fans-and-accessories)
  - [Optics](#optics)
  - [Module reuse across the four platforms](#module-reuse-across-the-four-platforms)
- [Platform-specific caveats](#platform-specific-caveats)
  - [Differences from the sibling C8300-1N1S-6T](#differences-from-the-sibling-c8300-1n1s-6t)
  - [Source conflicts](#source-conflicts)
- [Appendix A: identification and inventory commands](#appendix-a-identification-and-inventory-commands)
  - [Annotated listing](#annotated-listing)
  - [Paste-ready capture block](#paste-ready-capture-block)
  - [Commands not verified for this platform](#commands-not-verified-for-this-platform)
- [References](#references)
  - [Cisco datasheets, ordering, and hardware](#cisco-datasheets-ordering-and-hardware)
  - [Lifecycle](#lifecycle)
  - [Software releases](#software-releases)
  - [Licensing sources](#licensing-sources)
  - [Optics sources](#optics-sources)
  - [Features, ISE, and caveats](#features-ise-and-caveats)
  - [References - unresolved](#references---unresolved)

## Summary

**Multicast Service Reflection:** Cisco release notes document Unicast-to-Multicast Destination Reflection for the C8300-1N1S-4T2X product family starting in IOS XE 17.9.1a. This confirms family/release-level support for the MSR feature set; no test specific to this PID and the selected later IOS XE basis was located. [Catalyst 8200/8300 IOS XE 17.9 release notes](https://www.cisco.com/c/en/us/td/docs/routers/cloud_edge/c8300/rel_notes/17_9_x/cat8200-and-8300-rel-notes-xe-17-9-x.html) cover both exact C8300 PIDs and list Unicast-to-Multicast Destination Reflection in 17.9.1a. The [IOS XE 17.x multicast guide](https://www.cisco.com/c/en/us/td/docs/routers/ios-xe/ip-multicast/ip-multicast/m_imc_service_reflect-0.html) documents the `ip service reflect` configuration, its prerequisites and limitations, and MSR as introduced in IOS XE 3.4S.

| Field | Value |
| --- | --- |
| Supplied name | 8300-1S1N-4T2X |
| Confirmed PID | `C8300-1N1S-4T2X` (SKU correction: the PID puts the NIM count before the SM count, "1N1S") |
| Official family | Cisco Catalyst 8300 Series Edge Platforms (Catalyst 8000 Edge Platforms Family) |
| Identity sources | [C8300-4T2X-DS-1](#c8300-4t2x-ds-1) Table 2; [C8300-4T2X-OG-1](#c8300-4t2x-og-1) Table 1; [C8300-4T2X-HIG-1](#c8300-4t2x-hig-1) "Chassis Views"; [C8300-4T2X-EOL-1](#c8300-4t2x-eol-1) Table 2 |
| Variants | No AC/DC chassis variants. Power type is chosen through the PSU options on the base PID ([Power supplies](#power-supplies)). The convenience bundle `C8300-DNA` was End-of-Sale on 2023-02-03 ([C8300-4T2X-EOL-2](#c8300-4t2x-eol-2)). |

The C8300-1N1S-4T2X is the 1RU, 10G-WAN member of the Catalyst 8300 Series.
It is one of Cisco's named replacements for the ISR 4431. It runs the unified
IOS XE image, which boots in autonomous mode (traditional routing) or
controller mode (Catalyst SD-WAN) ([C8300-4T2X-OG-1](#c8300-4t2x-og-1),
section B). It differs from the `C8300-1N1S-6T` mainly in its two built-in
SFP+ ports (10G instead of 1G SFP). That gives it higher published IPsec
throughput, eligibility for the Tier 3 / 2.5G throughput levels, and
unthrottled controller-mode crypto with HSECK9.

### Key takeaways

1. **End-of-Sale is announced; the chassis is still orderable new.** EOL15950
   sets End-of-Sale at 2027-01-31, End of SW Maintenance Releases at
   2031-03-30, and Last Date of Support at 2032-01-31 (see
   [Lifecycle status](#lifecycle-status)). The last supported IOS XE train is 28.2.x. Cisco's migration product
   is `C8375-E-G2` ([C8300-4T2X-EOL-1](#c8300-4t2x-eol-1)). The 1RU PoE power
   supply `PWR-CC1-500WAC` is in the same notice.
1. **Licensing is subscription-led.** The chassis must be ordered with a Cisco
   DNA Essentials or DNA Advantage subscription (3-, 5-, or 7-year), or with
   Catalyst Routing Essentials (7-year only, autonomous mode only). The DNA
   tiers include a perpetual Network Essentials or Network Advantage stack for
   autonomous mode. Catalyst Routing Essentials has no perpetual element. DNA
   Premier was discontinued in August 2024
   ([C8300-4T2X-OG-1](#c8300-4t2x-og-1);
   [C8300-4T2X-DNA-2](#c8300-4t2x-dna-2)).
1. **HSECK9 controls crypto scale.** Without HSECK9 the router is limited to
   1,000 tunnels and the T0/T1 throughput levels (250 Mbps per direction).
   `C8000-HSEC` (with hardware) or `C8000-HSEC-DNA` (with `L-DNA-C8300`) is
   included with DNA subscriptions. HSECK9 needs a SLAC, which can be
   factory-installed or installed offline by file
   ([C8300-4T2X-LIC-1](#c8300-4t2x-lic-1);
   [C8300-4T2X-OG-1](#c8300-4t2x-og-1) section G).
1. **No-internet licensing has a documented path.** SLP supports a "No
   Connectivity to CSSM and No CSLU" topology: transport off, RUM reports
   saved to a file and uploaded from a connected workstation, ACK imported
   back. SSM On-Prem is an alternative
   ([C8300-4T2X-SLP-1](#c8300-4t2x-slp-1)). Eligibility under the hard
   requirement: **documented**. The administrator workload is set by the
   policy CSSM applies. The Cisco default policy requires a report every 90
   days for subscription licenses.
1. **Optics.** The built-in SFP+ ports list 1000BASE-SX/LX/LH/ZX, 10GBASE-SR,
   -LR, and -ER, 10G DAC, `GLC-TE` (1000BASE-T only), and `SFP-10G-T-X`
   (10GBASE-T only, 30 m). **10GBASE-ZR and 1G DAC are not listed** for the
   built-in ports. `SFP-10G-ZR-I` (70 km) is listed only on the `C-NIM-4X`
   module, from IOS XE 17.18.2 ([C8300-4T2X-TMG-1](#c8300-4t2x-tmg-1);
   [C8300-4T2X-TMG-2](#c8300-4t2x-tmg-2)). There are no ports faster than 10G.

### Uncertainty that could change the decision

- **Lifecycle vs. the comparison's assumptions.** A platform with
  End-of-Sale on 2027-01-31 meets "orderable new" only until that date. Buying
  for a multi-site rollout that runs past 2027-01-31 would require ordering
  ahead or switching platforms.
- **Tier mapping conflicts.** Cisco documents give different Mbps values for
  T1 (100M, 200M, or 250M), T2, and T3 on this PID
  ([Source conflicts](#source-conflicts)). Confirm the tier with Cisco or a
  partner before sizing.
- **Long-reach 10G.** 10GBASE-ZR is not verified on the built-in ports. If
  80 km 10G is required, it is not verified on this chassis in the sources
  checked; `SFP-10G-ZR-I` (70 km) needs `C-NIM-4X` and IOS XE 17.18.2 or later,
  which is above the 17.15.6 basis.

## Lifecycle status

### Chassis and accessory notice

Source: EOL15950 (amended), "End-of-Sale and End-of-Life Announcement for the
Cisco Catalyst C8500L-8S4X, C8300-1N1S-4T2X, C8300-1N1S-6T", page updated
2026-10-19 ([C8300-4T2X-EOL-1](#c8300-4t2x-eol-1), Table 1, PDF pp. 3–4).

| Milestone (Cisco name) | Date | Notes |
| --- | --- | --- |
| Product launch / series release | 2020-10-19 | "Series Release Date" on the support page ([C8300-4T2X-SUP-1](#c8300-4t2x-sup-1)) |
| End-of-Life Announcement Date | 2026-07-27 | EOL15950 |
| End-of-Sale Date | 2027-01-31 | Last date to order. **Still orderable new on 2026-10-30.** |
| Last Ship Date | 2027-04-30 |  |
| End of SW Maintenance Releases | 2031-03-30 |  |
| End of Vulnerability/Security Support | 2032-01-31 |  |
| End of Routine Failure Analysis Date | 2028-01-31 |  |
| End of New Service Attachment Date | 2028-01-31 |  |
| End of Service Contract Renewal Date | 2031-04-30 |  |
| Last Date of Support | 2032-01-31 |  |
| Last supported IOS XE train | 28.2.x | "The last supported IOS-XE Release train will be 28.2.x" (PDF p. 4) |
| Cisco's recommended replacement | C8375-E-G2 | "Cisco C8300 Series Secure Router, C8375-E-G2" (Table 2) |

Other part numbers in EOL15950 that matter for this chassis (Table 2):
`PWR-CC1-500WAC` and `PWR-CC1-500WAC=` (1RU AC PSU with PoE),
`PWR-CC1-400WAC/2`, `C8300-PS-BLANK1R`, `M2USB-75G`, and the voice bundle
`C8300-1N1S-6T-V` (6T only). None of these has a migration product listed. The
bulletin also notes that Cisco Refresh (remanufactured) units may remain
available until Last Date of Support. Refresh units are not new purchases.

No support horizon was supplied, so there is no pass/fail test against these
dates.

**Correction to the request:** the pre-check marked this model "Current". The
support page now lists every Catalyst 8300 model as "EOL Announced"
([C8300-4T2X-SUP-1](#c8300-4t2x-sup-1)).

### Bundle notice

EOL14900, "Cisco Select Catalyst 8300, 8200 and 8500 series Convenience
Bundles" ([C8300-4T2X-EOL-2](#c8300-4t2x-eol-2), Tables 1–2): `C8300-DNA`
bundle (for `C8300-1N1S-4T2X` and the other C8300 models). End-of-Life
Announcement 2022-11-04, End-of-Sale 2023-02-03, Last Ship 2023-05-04. The
replacement is the base PID ordered with a subscription.

### Software-train notices

| Train | Notice | End-of-Sale | End of SW Maintenance Releases | End of Vulnerability/Security Support | Last Date of Support | Source |
| --- | --- | --- | --- | --- | --- | --- |
| 17.15.x | EOL15772 | 2026-03-30 | 2027-03-30 | 2028-09-30 | 2029-03-31 | [C8300-4T2X-EOL-3](#c8300-4t2x-eol-3) |
| 17.12.x | EOL15518 | 2025-03-30 | 2026-03-30 (passed) | 2027-09-30 | 2028-03-31 | [C8300-4T2X-EOL-4](#c8300-4t2x-eol-4) |
| 17.18.x | EOL15995 | 2027-04-30 | 2028-04-29 | 2029-09-30 | 2030-03-30 | [C8300-4T2X-EOL-5](#c8300-4t2x-eol-5) |

The 17.15.x bulletin advises moving to 17.18.1 or later. The
End of Vulnerability/Security Support column for 17.15.x and 17.12.x is the
date in the row between End of SW Maintenance and Last Date of Support in each
bulletin.

**Module lifecycle:** NIM-ES2-8 and NIM-ES2-8-P passed End-of-Sale
2025-03-05 (support to 2030-03-31); NIM-ES2-4 passed End-of-Sale
2025-04-17 (support to 2030-04-30). These are compatibility/reference
options, not new-purchase module choices
([C8300-4T2X-EOL-6](#c8300-4t2x-eol-6),
[C8300-4T2X-EOL-7](#c8300-4t2x-eol-7)). Other module/license-specific
notices beyond the sources below were not found in the decision-relevant check. Lifecycle sources checked:
[C8300-4T2X-SUP-1](#c8300-4t2x-sup-1) (EoL listing),
[C8300-4T2X-EOL-1](#c8300-4t2x-eol-1) through
[C8300-4T2X-EOL-4](#c8300-4t2x-eol-4).

## Hardware specifications

All values apply to `C8300-1N1S-4T2X` unless noted. Primary source:
[C8300-4T2X-DS-1](#c8300-4t2x-ds-1) (datasheet updated 2026-10-06; table
locators are PDF pages).

| Item | Value | Label / source |
| --- | --- | --- |
| Form factor / rack units | 1RU; 19 in rack kit `C8300-RM-19-1R` included by default; 23 in and 4-post kits optional | Documented: DS-1 Table 15 (p. 20); [C8300-4T2X-OG-1](#c8300-4t2x-og-1) Table 7 |
| Dimensions (H × W × D) | 1.73 in × 17.50 in × 16.25 in | Documented: DS-1 Table 15 |
| Weight | 20 lb with 2 AC PSUs and fan tray | Documented: DS-1 Table 15 |
| CPU | x86 system-on-chip, 8 cores; Intel QuickAssist (QAT) crypto engine; DPDK data plane | Documented: [C8300-4T2X-WP-1](#c8300-4t2x-wp-1) ("8-core system (… C8300-1N1S-4T2X …)") |
| DRAM | 8 GB default (one DIMM); upgrades 16 GB or 32 GB (`MEM-C8300-16GB`, `MEM-C8300-32GB`) | Documented: DS-1 Table 1, Table 8; OG-1 Table 3 |
| Flash / storage | 8 GB onboard flash (not upgradable); 16 GB M.2 USB default; options 32 GB M.2 USB, 600 GB or 2 TB M.2 NVMe SED | Documented: DS-1 Table 1, Table 8 (OG-1 Table 3 lists `SSD-M2NVME-600G`; see [Source conflicts](#source-conflicts)) |
| Fixed ports | 4 × 10/100/1000 RJ-45 (Gi0/0/0–0/0/3); 2 × SFP+ (Te0/0/4–0/0/5) that also accept 1G SFP (speed auto-detected from the optic) | Documented: [C8300-4T2X-HIG-1](#c8300-4t2x-hig-1) Table 1; WP-1 Table 1 note |
| Combo ports | None documented | Not found in sources checked |
| Management Ethernet | **No dedicated out-of-band GigabitEthernet0 port; in-band management only.** | Documented: [C8300-4T2X-FAQ-1](#c8300-4t2x-faq-1), out-of-band management question, re-read 2026-10-31 UTC |
| Module slots | 1 NIM, 1 SM (single-wide), 1 PIM; up to 3 NIMs total using `C-SM-NIM-ADPT(R)` in the SM slot; double-wide SMs not supported on 1RU | Documented: OG-1 Table 4, Table 5 footnote 1 |
| Shared-resource limits | 10G backplane from the NIM and SM slots to the data-plane cores; up to 12 Gbps CEF aggregation across ports (ingress oversubscription by design) | Documented: WP-1 (block diagram and "Connectivity options") |
| Power options | Dual hot-swap PSUs shipped by default; AC, AC with PoE, DC, and HV AC/DC options | Documented: HIG-1 Table 5; DS-1 Table 9; see [Power supplies](#power-supplies) |
| PoE budget | No built-in PoE. With PWR-CC1-500WAC, 250 W module PoE in redundant active/standby mode; **500 W with two PoE supplies in active/active Boost, without redundancy**. | Documented: [C8300-4T2X-SMSW-1](#c8300-4t2x-smsw-1), Tables 2–3; DS-1 Table 9 |
| Typical power | 245 W typical, no modules, single PSU (configuration stated by Cisco) | Documented: DS-1 Table 11 (p. 17) |
| Maximum power / heat | Not found after checking the data sheet and HIG Overview, Prepare for Installation, and Internal Components/FRUs chapters. HIG power guidance refers back to the data sheet; PSU capacity is not maximum consumption. | Unverified: [C8300-4T2X-HIG-2](#c8300-4t2x-hig-2) |
| Airflow | Internal 3-fan C8300-FAN-1R tray; variable speed. **Inferred from the arrows in Figure 9:** intake at the side opposite the PSU/fan bank, exhaust through the PSU/fan side. Figure 9 was visually inspected; the direction is not a verbatim textual specification. | HIG-1, PDF p. 13, Figure 9; DS-1 Sustainability |
| Operating temperature | 0 to 40 °C (32 to 104 °F); altitude 0–3,050 m; humidity 5–85 % non-condensing | Documented: DS-1 Table 15 |
| Acoustics / MTBF | 49/71 dBA sound pressure (typical/max); MTBF 536,060 h | Documented: DS-1 Table 15 |
| Secure boot / trust anchor | Hardware-anchored Secure Boot and SUDI; "secure storage", run-time defenses, integrity verification (Trustworthy Solutions 2.0). A TPM or named trust-anchor chip is not stated. | Documented: DS-1 Table 1; [C8300-4T2X-FAQ-1](#c8300-4t2x-faq-1) "Security"; SUDI commands in [C8300-4T2X-SCG-1](#c8300-4t2x-scg-1) p. 212 |
| Crypto acceleration | Dedicated Intel QAT chip; all IPsec encryption and decryption is done in QAT | Documented: FAQ-1; WP-1 |

### Power supplies

Included: two PSUs by default (`PWR-CC1-250WAC` is the default AC unit)
([C8300-4T2X-OG-1](#c8300-4t2x-og-1) Table 6). PSU **capacity** is shown
below; it is not consumption.

| PID | Type | Rated output | Notes | Source |
| --- | --- | --- | --- | --- |
| `PWR-CC1-250WAC` | AC 100–240 V | 250 W | Default; 80 Plus Silver; IEC C14 | DS-1 Table 9; OG-1 Table 6 |
| `PWR-CC1-400WAC` | AC | 250 W (as listed) | Temporary pandemic-era substitute, no longer shipped; same support as the 250 W unit | DS-1 "Power supplies" notice and Table 9 |
| `PWR-CC1-500WAC` | AC with PoE | 500 W; PoE 250 W | Needed for PoE modules. **In EOL15950 (End-of-Sale 2027-01-31).** | DS-1 Table 9; [C8300-4T2X-EOL-1](#c8300-4t2x-eol-1) Table 2 |
| `PWR-CC1-400WDC` | DC −40 to −72 V | 400 W | Terminal block | DS-1 Table 9; OG-1 Table 6 |
| `PWR-CC1-400WHV` | HV DC 240–380 V | 400 W | Listed in the datasheet only; not in the ordering guide table | DS-1 Table 9 |

Redundancy: dual hot-swap PSUs on all models ([C8300-4T2X-HIG-1](#c8300-4t2x-hig-1)
Table 5). A NEBS reverse-airflow option exists only for 2RU models
([C8300-4T2X-DS-1](#c8300-4t2x-ds-1), "NEBS").

### Hyperthreading and core allocation

- **Hyperthreading: documented for this PID.** The HIG Overview chapter says:
  "The support for the Hyperthreading (HT) for the data plane Packet
  Processing Engine is added on the following platforms", followed by
  `C8300-2N2S-4T2X`, `C8300-2N2S-6T`, `C8300-1N1S-4T2X`
  ([C8300-4T2X-HIG-1](#c8300-4t2x-hig-1), p. 1).
- **The pre-check's "not listed for C8300-1N1S-6T" is probably a page-break
  misreading (inferred).** The next page of the same PDF starts with the
  bullet "• C8300-1N1S-6T" directly above "This chapter contains the following
  sections". It sits outside any other list. The most likely reading is that
  it is the fourth item of the HT list, carried over the page break (HIG-1,
  p. 2). The text checked does not give the minimum release or a CLI for HT.
  "Hyperthreading" does not appear in the 17.9, 17.12, 17.15, 17.18, 26.1, or
  26.2 release notes checked.
- **Core allocation:** 8-core system. The factory default is the
  service-oriented allocation (4 data-plane cores, 2 of them PPE). The
  data-plane-heavy allocation moves all service cores to the data plane
  (7 data-plane cores, 5 PPE) and removes container hosting on 8-core models.
  Cisco recommends data-plane-heavy when containers are not needed
  ([C8300-4T2X-DS-1](#c8300-4t2x-ds-1) "Dynamic core allocation";
  [C8300-4T2X-WP-1](#c8300-4t2x-wp-1)). A Cisco tech note covering C8300 shows
  `platform resource` templates and `show platform software cpu allocation`.
  Its examples were run on a C8500L ([C8300-4T2X-CPU-1](#c8300-4t2x-cpu-1)).

## Performance

All figures are Cisco-published "up to" or tested values from
[C8300-4T2X-DS-1](#c8300-4t2x-ds-1) Tables 3–6 (PDF pp. 6–7). Unless stated,
Cisco does not disclose the release, license tier, cipher, tunnel count, or
whether the figure is one-way or aggregate: those conditions are **not
disclosed**. These are platform capability figures. Licensed limits are in
[Table 2: Throughput and crypto](#table-2-throughput-and-crypto), and
licensed limits cap encrypted throughput below these values. Port line rate
(2 × 10G + 4 × 1G) is a separate thing again.

### Published throughput

| Metric | Value | Packet size / mix | Mode | Release | Other conditions | Locator |
| --- | --- | --- | --- | --- | --- | --- |
| IPv4 forwarding | Up to 19.7 Gbps | 1400 B | Autonomous | not disclosed | not disclosed | Table 5 |
| IPsec | Up to 16.9 Gbps | 1400 B | Autonomous | not disclosed | not disclosed | Table 5 |
| IPsec | 6.6 Gbps | IMIX (352 B average) | Autonomous | not disclosed | not disclosed | Table 5 |
| SD-WAN IPsec | Up to 17 Gbps | 1400 B | Controller | not disclosed | not disclosed | Table 3 |
| SD-WAN IPsec with IQDF | Up to 17 Gbps | 1400 B | Controller | not disclosed | IQDF = IPsec + QoS + DPI + FNF | Table 3 |
| SD-WAN IPsec | 6.3 Gbps | IMIX (352 B) | Controller | not disclosed | not disclosed | Table 3 |
| SD-WAN IPsec with IQDF | 5.5 Gbps | IMIX (352 B) | Controller | not disclosed | IQDF | Table 3 |
| 50 % IQDF + 50 % DIA (NAT+NGFW+IPS+URLF+AMP) | 3.3 Gbps | Firewall EMIX | Controller | IOS XE 17.12.2 | Multi-layer security use case | Table 4 |
| DIA with NAT+NGFW+IPS+URLF+AMP | 2.9 Gbps | Firewall EMIX | Controller | IOS XE 17.12.2 | Multi-layer security use case | Table 4 |

Other Cisco statements, kept separate because their conditions differ: the
architecture white paper gives "between 10 and 12 Gbps" data plane and
"between 2 and 5 Gbps" IPsec at 352-byte IMIX for the 8300 Series, and a
12 Gbps CEF aggregation ceiling for the 4T2X models
([C8300-4T2X-WP-1](#c8300-4t2x-wp-1), 2022-09-23). These are family-level
ranges and are not comparable with Table 5.

### Published scale

Autonomous mode, [C8300-4T2X-DS-1](#c8300-4t2x-ds-1) Table 6 (same values for
all four C8300 models): 4,000 IPsec SVTI tunnels (1,000 without HSECK9, per
[C8300-4T2X-LIC-1](#c8300-4t2x-lic-1)); 4,000 ACLs; 72K IPv4 ACEs;
1.6M IPv4 / 1.5M IPv6 routes with 8 GB, up to 4M with 32 GB; 8K queues;
1.2M NAT sessions with 8 GB, up to 2M with 32 GB; 512K firewall sessions;
4,000 VRFs. Controller mode: 6,000 SD-WAN overlay tunnels (Table 3). VLANs: 4K
([C8300-4T2X-FAQ-1](#c8300-4t2x-faq-1)).

## Software

### Release table

| Role | Release / train | Release or doc date | Mode | Applicability check | Source |
| --- | --- | --- | --- | --- | --- |
| Cisco-recommended (**basis**) | 17.15.6 (alternative: 17.12.8) | Release date not found; recommendation published 2026-06-15 | Autonomous | TAC document 215567, family row "Catalyst 8300" (not a PSIRT advisory; Cisco describes it as aligned with the Software Center gold-star releases). 17.15.6 is in the 17.15.x release notes for C8200/C8300, with no new features and "no customer impacting bugs" open. | [C8300-4T2X-REC-1](#c8300-4t2x-rec-1); [C8300-4T2X-RN-1](#c8300-4t2x-rn-1) |
| Newest 17.x | 17.18.5 | Release notes updated 2026-10-13 | Autonomous / controller | Listed in the C8200/C8300 17.18.x release notes; ROMMON matrix covers this PID | [C8300-4T2X-RN-2](#c8300-4t2x-rn-2) |
| Newest available | 26.2.1 | Release notes updated 2026-09-27 | Autonomous / controller | First 26.2.x release for C8200/C8300; ROMMON matrix lists this PID (minimum ROMMON 17.3(4.2r), recommended 26.1(1r)) | [C8300-4T2X-RN-3](#c8300-4t2x-rn-3) |
| Documented ceiling | 28.2.x train | Stated 2026-07-27 (amended 2026-10-19) | All | "The last supported IOS-XE Release train will be 28.2.x" for this PID | [C8300-4T2X-EOL-1](#c8300-4t2x-eol-1) |
| Minimum release | 17.3.2 | — | All | Datasheet and ordering guide | [C8300-4T2X-DS-1](#c8300-4t2x-ds-1) Table 12; [C8300-4T2X-OG-1](#c8300-4t2x-og-1) |

**Basis rationale:** 17.12.x passed End of SW Maintenance Releases on
2026-03-30 ([C8300-4T2X-EOL-4](#c8300-4t2x-eol-4)). 17.15.x keeps
maintenance until 2027-03-30 ([C8300-4T2X-EOL-3](#c8300-4t2x-eol-3)). Cisco
names 17.9, 17.12, 17.15, and 17.18 as long-term trains, and extended-support
releases are "every subsequent third release"
([C8300-4T2X-REC-1](#c8300-4t2x-rec-1)). A deployment starting in 2027 would
probably move to 17.18.x. That is **inferred**: 17.18 is the next extended
train, but Cisco's June 2026 recommendation does not list it yet. Controller
mode uses the same IOS XE release, with an SD-WAN Manager / controller version
dependency that was not researched here.

Feature minimums relevant to the decision (all from sources above):
tier-based throughput 17.7.1a; aggregate throttling 17.8.1a; 500 Mbps
aggregate for T1/250M with HSECK9 17.14.1a ([C8300-4T2X-LIC-1](#c8300-4t2x-lic-1));
factory-installed trust code 17.7.1a; offline SLAC request file 17.7.1a
([C8300-4T2X-SLP-1](#c8300-4t2x-slp-1)); C-NIM-4X 17.11.1; SFP-10G-ZR-I on
C-NIM-4X 17.18.2 ([C8300-4T2X-TMG-2](#c8300-4t2x-tmg-2)).

Upgrade prerequisites: minimum ROMMON 17.3(4.2r) for 17.15.x and later. The
recommended ROMMON is 17.9(7r) for 17.15.x and 17.18.x and 26.1(1r) for
26.2.x. If ROMMON is below the minimum, Cisco recommends booting 17.12.5
first to auto-upgrade it ([C8300-4T2X-RN-1](#c8300-4t2x-rn-1) Table 2;
[C8300-4T2X-RN-3](#c8300-4t2x-rn-3)). From 17.11.1, weak crypto algorithms
are disallowed by default (FN72510), and PAK licenses without a snapshot need
a two-step upgrade ([C8300-4T2X-REC-1](#c8300-4t2x-rec-1)).

### Install mode, bundle mode, and operating modes

- From 17.7.1a, Catalyst 8000 Edge platforms ship in **install mode**
  (`packages.conf`). Bundle mode (single `.bin`) is still supported, and
  conversion uses the one-step install procedure
  ([C8300-4T2X-SCG-1](#c8300-4t2x-scg-1) Table 9, pp. 49–51). Cisco says
  bundle mode is to be discontinued in a future release
  ([C8300-4T2X-REC-1](#c8300-4t2x-rec-1)).
- **Autonomous mode is the default.** Order code `IOSXE-AUTO-MODE`; controller
  mode is `IOSXE-CTRL-MODE` ([C8300-4T2X-OG-1](#c8300-4t2x-og-1) Table 2).
  Switching uses `controller-mode enable` / `controller-mode disable`.
  **Switching to controller mode erases the startup configuration and NVRAM,
  certificates included**; switching back keeps the YANG-based configuration
  ([C8300-4T2X-SCG-1](#c8300-4t2x-scg-1) pp. 7–8).
- `show version` reports "Router operating mode: Autonomous" (SCG-1 sample
  output, pp. 47–48).

## Licensing

### Licensing layers that apply

At 17.15.6 in autonomous mode:

1. **Subscription tier (orderable today):** Cisco DNA Essentials or Cisco DNA
   Advantage (3, 5, or 7 years; cloud `DNA-C-…` or on-premises `DNA-P-…`
   management variants), or Catalyst Routing Essentials (`ROUT-P-C8300-E-7Y`,
   7-year only). Cisco DNA Premier was discontinued in August 2024
   ([C8300-4T2X-DNA-2](#c8300-4t2x-dna-2); [C8300-4T2X-DNA-1](#c8300-4t2x-dna-1)
   Table 6; [C8300-4T2X-OG-1](#c8300-4t2x-og-1) Table 12).
1. **Network stack (perpetual) configured on the box:** Network Essentials (with
   DNA Essentials) or Network Advantage (with DNA Advantage), set with
   `license boot level` ([C8300-4T2X-LIC-1](#c8300-4t2x-lic-1)). The CLI still
   accepts `network-premier`, but Premier is not orderable today.
1. **Legacy ISR packages (ipbase, appxk9, securityk9, uck9):** do not apply.
   The DNA licenses "subsume" them ([C8300-4T2X-LIC-1](#c8300-4t2x-lic-1);
   [C8300-4T2X-OG-1](#c8300-4t2x-og-1) section H).
1. **Throughput:** a numeric or tier (T0–T3) crypto throughput level, set with
   `platform hardware throughput crypto`.
1. **Crypto export entitlement:** HSECK9 (`DNA_HSEC`), installed by SLAC.
1. **Separately licensed services:** CUBE and SRST (`A-FLEX-3`), each with a
   minimum DNA tier; UC is not included in Catalyst Routing Essentials
   ([C8300-4T2X-OG-1](#c8300-4t2x-og-1) Table 9).
1. **Reporting mechanism:** Smart Licensing Using Policy (SLP), the only mode
   supported ([C8300-4T2X-FAQ-1](#c8300-4t2x-faq-1)).

### Table 1: Feature entitlement

Per-feature tiers below come from Cisco's DNA routing matrix, "Platform based
routing features" section ([C8300-4T2X-MX-1](#c8300-4t2x-mx-1)). Its tier ticks are images; they were read
from the page code with a headless browser (Playwright) on 2026-10-30, along
with the feature list behind each category name. The matrix assigns
categories to three columns: Catalyst Routing Essentials, Cisco DNA
Essentials, and Cisco DNA Advantage. It names no platforms, so applying it to
this PID is **inferred** (Catalyst Routing Essentials is a Catalyst 8000
offer).

| Capability | Tier or license | Dependencies | Mode / release | Source |
| --- | --- | --- | --- | --- |
| Base routing (IP Base-equivalent) | Catalyst Routing Essentials, Network Essentials, or Network Advantage | A boot level license must be configured | Autonomous | [C8300-4T2X-DNA-2](#c8300-4t2x-dna-2); [C8300-4T2X-LIC-1](#c8300-4t2x-lic-1) |
| Point-to-point IPsec | All three tiers ("Secure infrastructure: IPsec (point to point)") | HSECK9 for > 250 Mbps or > 1,000 tunnels | Autonomous | [C8300-4T2X-MX-1](#c8300-4t2x-mx-1); [C8300-4T2X-OG-1](#c8300-4t2x-og-1) Routing Essentials section; LIC-1 |
| DMVPN, GET VPN, FlexVPN | DNA Essentials or DNA Advantage, not Catalyst Routing Essentials (footnote 1: "No SSL VPN support except on Catalyst 8000V") | HSECK9 as above | Autonomous | [C8300-4T2X-MX-1](#c8300-4t2x-mx-1) |
| Application-based firewall (ZBFW / NGFW) | All three tiers ("Perimeter security: L3-L7 firewall, ACL") | — | Autonomous | [C8300-4T2X-MX-1](#c8300-4t2x-mx-1); OG-1; DNA-2 |
| MPLS | Cisco DNA Advantage (Network Advantage) | — | Autonomous | [C8300-4T2X-FAQ-1](#c8300-4t2x-faq-1) |
| DNA Essentials adds (not in Routing Essentials) | MACsec; BFD; CUBE (IP to IP) and CUBE HA (categories "MACsec support", "Advanced Routing Capabilities", "Essential Voice/UC features") | — | Autonomous | [C8300-4T2X-MX-1](#c8300-4t2x-mx-1) |
| DNA Advantage only | Carrier-grade NAT; MPLS L2/L3 VPN, LDP, TE, VPLS, EVPN, segment routing; L2TPv3, EoGRE, 6RD/ISATAP; WCCP and object tracking; NBAR2 custom packs, ALG, SD-AVC; app hosting/guest shell; VXLAN, OTV, VASI; ISDN BRI, X.25; analog/digital voice cards, SRST, CME, DSP farm; ETA, mDNS, EPC, LISP; multicast VPN | — | Autonomous | [C8300-4T2X-MX-1](#c8300-4t2x-mx-1) |
| CUBE | `A-FLEX-3` plus minimum Cisco DNA Essentials / Network Essentials | Not available with Catalyst Routing Essentials | Autonomous | OG-1 Table 9 |
| SRST | `A-FLEX-3` plus minimum Cisco DNA Advantage / Network Advantage | — | Autonomous | OG-1 Table 9 |
| Voice modules (FXS/FXO, BRI, E&M, T1/E1, DSP) | Cisco DNA Advantage / Network Advantage | Module hardware | Autonomous | OG-1 Table 9 |
| TrustSec (SGT, SXP, SGACL) | **Conflict:** Network Advantage per Cisco's GBP matrix; all three tiers per the DNA routing matrix ("Network segmentation" lists TrustSec SGT, SGACL) | ISE | Autonomous and controller | [C8300-4T2X-TS-1](#c8300-4t2x-ts-1) p. 5; [C8300-4T2X-MX-1](#c8300-4t2x-mx-1) |
| IPS/IDS, URL filtering, AMP (UTD) | DNA Essentials or DNA Advantage, not Catalyst Routing Essentials ("Threat protection"). Footnote 3: AMP and URL filtering "Supported only with SD-Routing"; "URL Filtering Sandboxing with AMP requires DNA Advantage". IPS/IDS has no footnote, so it is in scope for autonomous mode | 8 GB DRAM minimum; 16 GB for the on-box URL database | Autonomous (IPS/IDS); SD-Routing (AMP, URLF) | [C8300-4T2X-MX-1](#c8300-4t2x-mx-1) footnote 3; [C8300-4T2X-DNA-1](#c8300-4t2x-dna-1) Table 10 notes |
| Catalyst Center management | DNA Essentials, DNA Advantage, or Catalyst Routing Essentials | An active DNA-stack (term) entitlement for controller-led orchestration | Autonomous | FAQ-1 |
| On-premises SD-Routing (SD-WAN Manager) | Included in Catalyst Routing Essentials; also DNA tiers | — | Autonomous (SD-Routing); minimum release not stated | DNA-2; OG-1 |
| Catalyst SD-WAN | DNA Essentials (up to 10 user VPNs + 1 management VPN) or DNA Advantage (unlimited segmentation) | SD-WAN controllers (`L-CONTROLLER-ADD`) | Controller | DNA-2; DNA-1 Step 4 |

### Table 2: Throughput and crypto

Throughput licensing limits **encrypted** traffic. Unencrypted (CEF) traffic is
not throttled by default ([C8300-4T2X-LIC-1](#c8300-4t2x-lic-1), "Throttled
and unthrottled throughput"; [C8300-4T2X-DNA-2](#c8300-4t2x-dna-2)).

| Tier / numeric level | Limit unlocked on C8300-1N1S-4T2X (autonomous, 17.14.1a and later) | Crypto restriction / prerequisite | License tiers allowed | Source |
| --- | --- | --- | --- | --- |
| Default (no config) | 10M bidirectional | — | — | LIC-1 table "C8300-1N1S-4T2X, C8300-2N2S-4T2X" (PDF p. 17) |
| 10M, 15M, 25M, 50M, 100M | Same value, bidirectional | No HSECK9 needed | Essentials, Advantage | LIC-1 p. 17; tier image p. 13 |
| T0 | 25M bidirectional | No HSECK9 needed | Essentials, Advantage | LIC-1 p. 17 |
| 250M / T1 | With HSECK9: 500M aggregate. Without: 250M bidirectional. | HSECK9 optional | Essentials, Advantage | LIC-1 p. 17 |
| 500M | 1G aggregate | HSECK9 (SLAC) required | Essentials, Advantage | LIC-1 p. 17 |
| 1G / T2 | 2G aggregate | HSECK9 required | Essentials, Advantage | LIC-1 p. 17 |
| 2.5G | 5G aggregate | HSECK9 required | Advantage only (and Premier, which is no longer orderable) | LIC-1 p. 17; tier image p. 13 |
| T3 | 20G aggregate (10G bidirectional) per LIC-1 table; see conflicts | HSECK9 required; T3 not allowed with Network/DNA Essentials | Advantage only | LIC-1 p. 17; [C8300-4T2X-OG-1](#c8300-4t2x-og-1) Table 11 ("Tier 3 … provides the max platform throughput for C8300-1N1S-4T2X") |
| Catalyst Routing Essentials | Crypto "up to 2 Gbps" per the ordering guide; the BoM auto-includes `NWSTACK-T2-E`, `DSTACK-T0-E`, and HSEC | HSEC included | n/a (no tiering) | OG-1 Routing Essentials section. The FAQ says "up to device capability"; see [Source conflicts](#source-conflicts). |

Export authorization, crypto capability, and performance are separate:

- **Export authorization:** HSECK9 (`DNA_HSEC`, "Router US Export Lic. for
  DNA") is export-controlled, perpetual, tied to one chassis UDI, and needs a
  SLAC. After installing the SLAC on C8200/C8300, run
  `license feature hseck9` ([C8300-4T2X-LIC-1](#c8300-4t2x-lic-1), "High
  Security license"). Without HSECK9: 1,000 tunnels, T0/T1 only, 250 Mbps per
  direction. Cisco offers no temporary HSEC license on the C8300
  ([C8300-4T2X-FAQ-1](#c8300-4t2x-faq-1)).
- **Ordering:** `C8000-HSEC` is auto-included when DNA is ordered with the
  hardware; `C8000-HSEC-DNA` with `L-DNA-C8300`; spare `C8000-HSEC=`. If the
  Smart Account / Virtual Account is given with the hardware order, Cisco can
  factory-install the SLAC. If HSEC is ordered separately, it cannot be
  ([C8300-4T2X-OG-1](#c8300-4t2x-og-1) Table 8;
  [C8300-4T2X-LIC-1](#c8300-4t2x-lic-1)).
- **Performance:** set separately with
  `platform hardware throughput crypto`, followed by a reload.

### Table 3: Purchase and enforcement

| License | Perpetual / subscription | Terms | Orderable today (2026-10-30) | Reporting method | Reporting deadlines (Cisco default policy) | Behavior on expiry / noncompliance | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Cisco DNA Essentials / Advantage (DNA stack) | Subscription (unenforced) | 3Y, 5Y, 7Y (no 7Y under EA) | Yes, with the chassis until its End-of-Sale (2027-01-31) (inferred: no separate license EoL notice found) | Direct, CSLU, SSM On-Prem, controller, or offline file | First report within 90 days, then every 90 days; report on change within 90 days. ACK required. | Autonomous: base routing by CLI keeps working on the perpetual stack; Catalyst Center WAN management stops. Controller: WAN management stops. | [C8300-4T2X-DNA-1](#c8300-4t2x-dna-1) Table 6; [C8300-4T2X-DNA-2](#c8300-4t2x-dna-2); [C8300-4T2X-SLP-1](#c8300-4t2x-slp-1) "Policy: Cisco default" (p. 8) |
| Network Essentials / Advantage (network stack) | Perpetual (unenforced) | n/a | Yes, only as part of a DNA subscription | As above | First report within 365 days only if bought through a distributor or partner; report on change within 90 days. | Stays after the DNA term ends ([C8300-4T2X-FAQ-1](#c8300-4t2x-faq-1)) | SLP-1 p. 8; FAQ-1 |
| Catalyst Routing Essentials | Subscription only; no perpetual element | 7Y only | Yes (`ROUT-P-C8300-E-7Y`); not in EA or MSLA | As above | Inferred: the "Unenforced/Non-Export Subscription" policy (90 / 90 / 90 days) | "Any further use … would … be out of compliance" after expiry ([C8300-4T2X-FAQ-1](#c8300-4t2x-faq-1)). Technical enforcement: unresolved. | [C8300-4T2X-OG-1](#c8300-4t2x-og-1) Table 12; DNA-2; FAQ-1 |
| HSECK9 (`C8000-HSEC`, `DNA_HSEC`) | Perpetual, export-controlled | n/a | Yes | SLAC install (factory, online, or offline file) | Export policy: first report 0, frequency 0, on change 0 (no recurring reporting) | Without an installed SLAC: 250 Mbps per direction and 1,000 tunnels | SLP-1 p. 7–8; LIC-1 |
| CUBE / SRST (`A-FLEX-3`) | Not stated in sources checked | Not stated | Yes (per the 2026-06-17 ordering guide) | Unenforced; reported via SLP | Depends on the license type (not stated) | Not stated | OG-1 Table 9; LIC-1 |
| Throughput tier (in the DNA PID) | Part of the DNA PID | As above | Yes | As above | As above | No hard enforcement of non-crypto tiers; configuring an unowned tier gives out-of-compliance messages and no TAC support for related issues. Crypto is capped at 250 Mbps without HSEC. | DNA-2 ("Are bandwidth or throughput tiers enforced?") |

What happens if a SLP ACK deadline is missed is **unresolved** in the sources
checked. The SLP guide documents only the `%SMART_LIC-6-REPORTING_REQUIRED`
notification and the "Next ACK deadline" field. It describes SLP as designed
"not [to] interrupt the operations of your network"
([C8300-4T2X-SLP-1](#c8300-4t2x-slp-1), "Information About" and system
messages). MSLA is not supported in autonomous mode on C8200/C8300/C8500
([C8300-4T2X-LIC-1](#c8300-4t2x-lic-1)).

### Offline operation (no internet for license reporting)

**Eligibility: documented.** SLP covers C8300 from IOS XE 17.3.2
([C8300-4T2X-SLP-1](#c8300-4t2x-slp-1), Table 1). Two documented ways to run
with no path from the router to Cisco:

**Option A: No Connectivity to CSSM and No CSLU** (SLP-1, printed pp. 24–25
topology and p. 45 workflow). All exchanges are files carried by hand to an
internet-connected workstation.

1. At order time, give the Smart Account / Virtual Account so Cisco
   factory-installs the HSECK9 SLAC; from 17.7.1a a trust code is also
   factory-installed ([C8300-4T2X-LIC-1](#c8300-4t2x-lic-1);
   [C8300-4T2X-SLP-1](#c8300-4t2x-slp-1) "Trust Code"). A factory trust code
   cannot be used for online CSSM communication. That does not matter offline.
1. On the router: `license smart transport off`, then save the configuration.
1. Set `license boot level …` and the crypto throughput; reload.
1. If the SLAC was not factory-installed (17.7.1a or later): generate a SLAC
   request file on the router ("Generating and Saving a SLAC Request on the
   Product Instance", printed p. 203). Upload it to CSSM from a connected
   workstation, download the SLAC file, copy it to `bootflash:`, and run
   `license smart import bootflash:<file>` (printed p. 215). Alternatively,
   generate the SLAC in the CSSM web UI by entering the device's UDI. Then
   `license feature hseck9`.
1. Reporting: `license smart save usage all file bootflash:<file>`, copy the
   file off the router, upload it to CSSM, download the ACK, and run
   `license smart import` on the router (p. 45). Check
   `show license status` for "Next ACK deadline".

**Cadence (Cisco default policy, SLP-1 p. 8; the policy actually applied is
shown by `show license all`):** with a DNA subscription in use, the first RUM
report is due within 90 days and then every 90 days, plus within 90 days of
any license change. The perpetual network stack alone needs a report only on
change, or within 365 days when bought through a partner. HSECK9 needs no
recurring report. Workload: about **one offline upload/download cycle per
router per quarter**, plus one per license change. **Inferred** from the
default policy; a customized policy can be requested from Cisco Licensing.

**Option B: SSM On-Prem** (SLP-1 printed pp. 26–27, 46). Routers report to an
on-premises SSM On-Prem server, by push or pull. SSM On-Prem then syncs usage
with CSSM, either online or "through signed files that are saved offline". The
SSM On-Prem local account must still be registered and synchronized with a
CSSM Virtual Account. Whether that registration can be done entirely offline
is **not verified** in the sources checked. SSM On-Prem cuts the per-router
workload to one periodic file exchange for the whole server.

**Missed deadlines:** unresolved (see Table 3).

### Controller-mode licensing callout

In controller mode, the same DNA subscription applies, and the HSECK9
throughput table differs. This PID is **unthrottled** with HSECK9
(250M bidirectional default without it), while the 6T models are capped at
2G aggregate ([C8300-4T2X-LIC-1](#c8300-4t2x-lic-1), "Entitled throughput …
SD-WAN controller mode", PDF p. 19). For SD-WAN, Cisco counts all WAN
traffic, not only IPsec, against the bandwidth tier. MSLA is supported in
controller mode ([C8300-4T2X-DNA-2](#c8300-4t2x-dna-2); LIC-1). Catalyst
Routing Essentials cannot be ordered with `IOSXE-CTRL-MODE`
([C8300-4T2X-OG-1](#c8300-4t2x-og-1)).

### Pricing

**Unknown.** Cisco US list prices were not found in openly published Cisco
sources. Quotes needed: chassis `C8300-1N1S-4T2X`; DNA Essentials and DNA
Advantage at T1/T2/T3 for 3/5/7 years (`DNA-P-…` on-premises variants for an
offline site); `ROUT-P-C8300-E-7Y`; `A-FLEX-3` if voice is used; PSU, memory,
and module options; Smart Net Total Care. The DNA subscription's embedded
support does **not** cover the network stack or hardware
([C8300-4T2X-OG-1](#c8300-4t2x-og-1) "Services").

## Feature support and integration

### Feature matrix

Basis: IOS XE 17.15.6, autonomous mode unless stated. "Not verified" means
the support was not confirmed in Cisco sources for this PID and release.

| Feature | Supported | Mode | License / tier | Module / hardware | Minimum release | Key limits / scale (published) | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SD-WAN | Yes | Controller only | DNA Essentials or Advantage; controller subscription | None | 17.3.2 | 6,000 overlay tunnels; 17 Gbps 1400 B IPsec | [C8300-4T2X-DS-1](#c8300-4t2x-ds-1) Tables 3, 14; [C8300-4T2X-DNA-1](#c8300-4t2x-dna-1) |
| IPsec VPN | Yes | Both | All tiers; HSECK9 for > 250 Mbps or > 1,000 tunnels | QAT on board | 17.3.2 | 4,000 SVTI tunnels; 16.9 Gbps 1400 B | DS-1 Tables 5–6, 13; [C8300-4T2X-LIC-1](#c8300-4t2x-lic-1) |
| DMVPN / FlexVPN / GET VPN | Yes (tier entitlement documented, family-level) | Autonomous | DNA Essentials or Advantage; not Routing Essentials | — | — | — | [C8300-4T2X-MX-1](#c8300-4t2x-mx-1) |
| NAT | Yes | Both | All three tiers (NAT/PAT IPv4/v6); carrier-grade NAT DNA Advantage only | — | 17.3.2 | — | [C8300-4T2X-MX-1](#c8300-4t2x-mx-1) |
| QoS (HQoS, CBWFQ, NBAR) | Yes | Both | MQC, HQoS, NBAR2 standard packs in all three tiers; NBAR2 custom packs and SD-AVC DNA Advantage only | — | 17.3.2 | — | [C8300-4T2X-MX-1](#c8300-4t2x-mx-1) |
| Voice / CUBE | Yes | Both (SD-WAN: SIP only) | CUBE: `A-FLEX-3` + DNA Essentials minimum; SRST/voice modules: DNA Advantage | Voice NIM/SM-X and PVDM DSP modules for TDM/analog | 17.3.2 | Not published | DS-1 Tables 13–14; [C8300-4T2X-OG-1](#c8300-4t2x-og-1) Table 9; [C8300-4T2X-DNA-1](#c8300-4t2x-dna-1) |
| CME | Conflicting | Autonomous | DNA Advantage (if supported) | — | — | — | DS-1 Table 13 lists CUCME; [C8300-4T2X-FAQ-1](#c8300-4t2x-faq-1) lists CME as a parity exception ([Source conflicts](#source-conflicts)) |
| NGFW / UTD (ZBFW, Snort IPS, URLF, AMP) | ZBFW: yes. IPS/IDS: entitled in autonomous mode (family-level matrix); AMP/URLF: SD-Routing or controller only | ZBFW both; IPS/IDS autonomous and controller; AMP/URLF SD-Routing and controller | ZBFW all tiers; IPS/IDS DNA Essentials or Advantage; AMP/URLF via SD-Routing only | 8 GB DRAM; 16 GB for the on-box URL database | 17.3.2 (ZBFW); 26.2.1 adds Catalyst NGFW V2 | — | [C8300-4T2X-MX-1](#c8300-4t2x-mx-1); [C8300-4T2X-DNA-1](#c8300-4t2x-dna-1) |
| PoE | Yes, via modules only | Both | Not license-gated (not verified) | PoE NIM/SM (`C-NIM-8M`, `C-NIM-1M` (NIM-ES2-8-P is historical/EOS)) + `PWR-CC1-500WAC` (250 W budget; EoS 2027-01-31) | Not stated | 250 W redundant active/standby; 500 W with two PoE PSUs in active/active Boost, no redundancy | DS-1 Tables 1, 7, 9; [C8300-4T2X-EOL-1](#c8300-4t2x-eol-1); [C8300-4T2X-SMSW-1](#c8300-4t2x-smsw-1), Tables 2–3 |
| Routing scale | Yes | Both | MPLS needs DNA Advantage | 32 GB DRAM for the maximum | 17.3.2 | 1.6M IPv4 / 1.5M IPv6 routes (8 GB), 4M (32 GB); BGP, OSPF, EIGRP, IS-IS | DS-1 Tables 6, 13; FAQ-1 |
| Segmentation: VRF-Lite | Yes | Both | All three tiers (VRF-Lite, Multi-VRF, EVN) | — | 17.3.2 | — | [C8300-4T2X-MX-1](#c8300-4t2x-mx-1) |
| Segmentation: SGT | Yes (family row) | Both | Network Advantage | Inline tagging through `C-NIM-2T`, `C-NIM-1M`, `C-NIM-1X` (note 18) | Not stated | 64,000 SGT/DGT policies; 1,800 / 900 SXP connections; 750,000 bindings | [C8300-4T2X-TS-1](#c8300-4t2x-ts-1) pp. 5, 16, 18, 20 |
| Multicast Service Reflection | Yes (product-family release-note support) | Autonomous CLI configuration documented; controller mode not established | Network Advantage indicated by Cisco MSR tech note; verify exact entitlement for this PID | Vif interface and PIM infrastructure | Unicast-to-multicast support introduced 17.9.1a; selected release later | IOS XE 17.x documents `ip service reflect`; family-level support; exact-PID test not found | [C8300-4T2X-MSR-REL-1](#c8300-4t2x-msr-rel-1); [C8300-4T2X-MSR-1](#c8300-4t2x-msr-1); [C8300-4T2X-MSR-LIC-1](#c8300-4t2x-msr-lic-1) |

### Cisco ISE integration

| Integration | Supported | Mode | License / tier | Module / hardware | Minimum release | Key limits | Router vs. ISE configuration | Source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| RADIUS device administration | Yes | Both | All tiers | — | 17.3.2 | — | Router: AAA and RADIUS server group. ISE: network device entry and policy. **From 26.2.1 the router drops RADIUS replies without a valid Message-Authenticator (Attribute 80)**; ISE must return it. | [C8300-4T2X-DS-1](#c8300-4t2x-ds-1) Table 13; [C8300-4T2X-RN-3](#c8300-4t2x-rn-3) Table 1 |
| TACACS+ device administration | Yes, **inferred for this PID** from family AAA/TACACS+ documentation. | Autonomous baseline; controller applicability unverified | All three tiers, family-level matrix | — | Not established by cited matrix | — | Router: AAA/TACACS+ server configuration. ISE: network-device and Device Administration policy. | [C8300-4T2X-MX-1](#c8300-4t2x-mx-1); entitlement does not establish a minimum release or mode support |
| TrustSec SGT inline tagging | Yes, through specific WAN NIMs; built-in ports not verified | Both | Network Advantage | Note 18: for C82xx/C83xx, `C-NIM-2T`, `C-NIM-1M`, and `C-NIM-1X` support inline tagging | Not stated | — | Router: `cts` interface configuration. ISE: SGT definitions | [C8300-4T2X-TS-1](#c8300-4t2x-ts-1) pp. 5, 20 |
| SXP | Yes (family row) | Both | Network Advantage | — | Not stated | 1,800 unidirectional / 900 bidirectional connections; 750,000 bindings | Router: SXP peers. ISE: SXP service (pxGrid / SXP; ISE Advantage per the matrix) | TS-1 pp. 5, 16 |
| SGACL enforcement | Yes (family row) | Both | Network Advantage | — | Not stated | 64,000 SGT/DGT policies | Router: role-based enforcement. ISE: SGACL matrix (downloaded to the router). 17.15.6 fixes an SGACL CoA download bug (CSCws96978). | TS-1 pp. 5, 18; [C8300-4T2X-RN-1](#c8300-4t2x-rn-1) |
| 802.1X / MAB on switch ports | Yes on **C-SM-16P4M2X copper ports**; other modules/ports unverified. | Autonomous baseline; controller feature applicability not established here | Module supported with all Cisco DNA subscriptions; Routing Essentials applicability not established | C-SM-16P4M2X, single-wide SM slot | Module feature minimum not stated in this source; support at basis inferred from current family module support | 20 copper ports; 802.1X, MAB and multidomain authentication | Router: module port authentication. ISE: identity/authorization policy. Do not infer built-in WAN-port authenticator support. | [C8300-4T2X-SMSW-1](#c8300-4t2x-smsw-1), Security feature support and Tables 1–3 |
| Other: SD-Access border / control plane | Yes | Autonomous | Not stated | — | Not stated | — | Catalyst Center and ISE | [C8300-4T2X-FAQ-1](#c8300-4t2x-faq-1) |

ISE classification: the GBP matrix lists the C8300-2N2S-6T row (Tier 1,
Catalyst 8000 routers) and family-level scale rows ("C8300"). The 4T2X PID is
not named. Applicability to this PID is **inferred** from the shared C8300
software and the family rows. Note 18 suggests inline tagging on C83xx goes
through the listed WAN modules; whether the built-in ports support it is not
verified.

## Modules and expansion

### Slot map

| Slot | Count | Accepts | Notes | Source |
| --- | --- | --- | --- | --- |
| Slot 0, bay 0 | — | Built-in 4 × RJ-45 1G + 2 × SFP+ 10G | Gi0/0/0–0/0/3, Te0/0/4–0/0/5 | [C8300-4T2X-HIG-1](#c8300-4t2x-hig-1) |
| NIM | 1 | NIM family | 10G backplane | [C8300-4T2X-OG-1](#c8300-4t2x-og-1) Table 4; [C8300-4T2X-WP-1](#c8300-4t2x-wp-1) |
| SM (single-wide) | 1 | SM-X single-wide, `C-SM-16P4M2X`, UCS-E single-wide, or `C-SM-NIM-ADPT(R)` (2 more NIMs) | Double-wide SMs (`C-SM-40P8M2X`, `SM-X-72FXS`, double-wide UCS-E) are 2RU only | OG-1 Tables 4–5 |
| PIM | 1 | Cellular PIM | **Available, not assessed** (cellular out of scope) | OG-1 Table 5 |
| M.2 | 1 | M.2 USB or NVMe storage | External slot | HIG-1 |
| PSU | 2 | 1RU PSUs | Hot-swap | HIG-1 Table 5 |
| DIMM | 1 | MEM-C8300-8/16/32GB | Internal | OG-1 Table 3 |

Internal modules only. External Ethernet devices (for example a separate
switch) are outside this list.

### NIM modules

Coverage: [C8300-4T2X-OG-1](#c8300-4t2x-og-1) Table 5 (2026-06-17) and
[C8300-4T2X-DS-1](#c8300-4t2x-ds-1) Table 7 (2026-10-06). "Supported on
chassis" = listed for the C8300 family in both. "At 17.15.6" = **inferred**
(minimum release at or below 17.15.6 where known, and no withdrawal found).
"Orderable today" is not verified per module except the explicit NIM-ES2
End-of-Sale findings below. Compatibility lists do not prove new orderability. Modules marked † are C8300-specific and are not
compatible with the ISR 4000 (OG-1 footnote).

| PID | Description / capability | Slot | Min release / mode | Dependency | Supported on chassis | At 17.15.6 | Orderable today | Source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `C-NIM-1X` † | 1 × 10G SFP/SFP+ L3 WAN, WAN MACsec | NIM | 17.3.2 (per TMG optics) | — | Yes | Inferred | Not checked | DS-1, OG-1 |
| `C-NIM-2T` | 2 × 1G dual-mode RJ-45/SFP L3 WAN, WAN MACsec | NIM | 17.6.1 (per TMG optics) | — | Yes | Inferred | Not checked | DS-1, OG-1 |
| `C-NIM-1M` | 1 × 2.5G/1G RJ-45 WAN, 90 W PoE | NIM | Not found | PoE PSU | Yes | Inferred | Not checked | DS-1, OG-1 |
| `C-NIM-4X` | 4 × 1/10G SFP/SFP+ switch, LAN/WAN MACsec, optional L3 | NIM | 17.11.1 (per TMG optics) | — | Yes | Inferred | Not checked | DS-1, OG-1 |
| `C-NIM-8T` | 8 × 100M/1G switch, MACsec, optional L3 | NIM | Not found | — | Yes | Inferred | Not checked | DS-1, OG-1 |
| `C-NIM-8M` | 8 × 100M/1/2.5G switch, UPoE, MACsec, optional L3 | NIM | DS-1 marks "\*" (17.12.2) | PoE PSU | Yes | Inferred | Not checked | DS-1, OG-1 |
| `NIM-ES2-4`, `NIM-ES2-8`, `NIM-ES2-8-P` | 4/8-port GE switch (-P: PoE) | NIM | Not found | -P needs a PoE PSU | Yes | Inferred | **No**: -4 EOS 2025-04-17; -8/-8-P EOS 2025-03-05 | DS-1, OG-1; [EOL-6](#c8300-4t2x-eol-6), [EOL-7](#c8300-4t2x-eol-7) |
| Voice: `NIM-2FXO`, `NIM-4FXO`, `NIM-2FXSP`, `NIM-4FXSP`, `NIM-2FXSP/4FXOP`, `NIM-4E/M`, `NIM-2BRI-NT/TE`, `NIM-4BRI-NT/TE` | Analog/BRI voice | NIM | Not found | DNA Advantage; DSP | Yes | Inferred | Not checked | DS-1, OG-1 |
| DSP: `NIM-PVDM-32/64/128/256` | Voice DSP | NIM | Not found | DNA Advantage | Yes | Inferred | Not checked | DS-1, OG-1 |
| T1/E1: `NIM-1/2/4/8MFT-T1/E1`, `NIM-1/2/8CE1T1-PRI` | Voice/data T1/E1, PRI | NIM | Not found | — | Yes | Inferred | Not checked | DS-1, OG-1 |
| Serial/async: `NIM-1T`, `NIM-2T`, `NIM-4T`, `NIM-16A`, `NIM-24A` | Serial WAN, async | NIM | Not found | — | Yes | Inferred | Not checked | DS-1, OG-1 |
| DSL/BRI data: `NIM-VAB-A`, `NIM-VA-B`, `NIM-VAB-M`, `NIM-4SHDSL-EA`, `NIM-2BRI-S/T`, `NIM-4BRI-S/T` | DSL, ISDN data | NIM | Not found | — | Yes | Inferred | Not checked | DS-1, OG-1 |
| Cellular NIMs (available, not assessed) | Cellular | NIM | — | — | Available, not assessed | — | — | DS-1 |

### SM-X and service modules

| PID | Capability | Slot fit on 1RU | Min release | Supported on chassis | At 17.15.6 | Source |
| --- | --- | --- | --- | --- | --- | --- |
| `C-SM-NIM-ADPT(R)` † | Carrier for 2 NIMs in one SM slot | Yes (up to 3 NIMs total) | Not found | Yes | Inferred | DS-1 Table 7; OG-1 Tables 4–5 |
| `C-SM-16P4M2X` † | 22-port L2 switch (UADP), 1G/mGig/10G uplinks | Yes (single-wide) | Not found | Yes | Inferred | DS-1 "High-density Switching"; OG-1 |
| `C-SM-40P8M2X` † | 50-port L2 switch | **No** (double-wide, 2RU) | — | No (1RU) | — | OG-1 Table 5 footnote 1 |
| `SM-X-8FXS/12FXO`, `SM-X-16FXS/2FXO`, `SM-X-24FXS/4FXO` | Analog voice | Yes | Not found | Yes | Inferred | DS-1; OG-1 |
| `SM-X-72FXS` | 72 FXS | **No** (double-wide) | — | No (1RU) | — | OG-1 footnote 1 |
| `SM-X-PVDM-500/1000/2000/3000` | High-density DSP | Yes (not marked double-wide) | Not found | Yes | Inferred | DS-1; OG-1 |
| `SM-X-1T3/E3`, `SM-X-64A` | T3/E3; 64-port async | Yes | Not found | Yes | Inferred | OG-1 |
| `UCS-E160S-M3/K9` | Compute, single-wide, 6-core | Yes | Not found | Yes | Inferred | DS-1; OG-1 |
| `UCS-E180D-M3/K9`, `UCS-E1120D-M3/K9`, `UCS-E1100D-M6/K9` | Compute, double-wide | **No** (double-wide; inferred from "double-wide" in DS-1 and the 1RU single SM slot) | — | Inferred no | — | DS-1 Table 7 |

### PIM and cellular

The PIM slot takes cellular PIMs (`P-LTEA-*`, `P-LTEAP18-GL`, `P-5GS6-*`).
**Available, not assessed** (LTE/5G out of scope)
([C8300-4T2X-DS-1](#c8300-4t2x-ds-1) Table 7). Blank: `C8300-PIM-BLANK`.

### Memory, storage, fans, and accessories

From [C8300-4T2X-DS-1](#c8300-4t2x-ds-1) Table 8 and
[C8300-4T2X-OG-1](#c8300-4t2x-og-1) Tables 3 and 7: `MEM-C8300-8GB` (default),
`MEM-C8300-16GB`, `MEM-C8300-32GB`; `M2USB-16G` (default), `M2USB-32G`,
`SSD-M2SED-600G` / `SSD-M2NVME-600G` (naming differs between the sources),
`SSD-M2NVME-2T`; `C8300-FAN-1R` (default fan tray); rack kits
`C8300-RM-19-1R` (default), `C8300-RM-23-1R`, `C8300-RM-4PT-1R`; RFID
`C-RFID-1R`; blanks for NIM, SM, and PIM. `M2USB-75G` is in EOL15950
([C8300-4T2X-EOL-1](#c8300-4t2x-eol-1)). FN74146 covers some
`MEM-C8300-8GB=` / `MEM-C8300-32GB=` DIMMs (see
[Platform-specific caveats](#platform-specific-caveats)).

### Optics

Source for all compatibility claims: the Cisco Optics-to-Device Compatibility
Matrix (TMG) filtered to `C8300-1N1S-4T2X`
([C8300-4T2X-TMG-1](#c8300-4t2x-tmg-1)) and to `C-NIM-1X`, `C-NIM-4X`,
`C-NIM-2T` ([C8300-4T2X-TMG-2](#c8300-4t2x-tmg-2)), accessed 2026-10-30.
**These results are non-exhaustive.** TMG gives one list per network device
PID and does not say which built-in port each optic fits. Built-in SFP+
entries are read as applying to Te0/0/4–0/0/5 (**inferred**: these are the
only pluggable built-in ports).

#### Port inventory

| Port type | Speeds | Form factor | Restrictions | Source |
| --- | --- | --- | --- | --- |
| Built-in Gi0/0/0–0/0/3 | 10/100/1000 Mb/s | RJ-45 | Copper only | [C8300-4T2X-HIG-1](#c8300-4t2x-hig-1) "GE Ports" |
| Built-in Te0/0/4–0/0/5 | 1G (SFP) or 10G (SFP+), auto-detected from the optic | SFP+ | `GLC-TE`: 1000BASE-T only. `SFP-10G-T-X`: 10GBASE-T only, 30 m. 10G DACs `SFP-H10GB-CU1M/3M/5M` need version -02 or later. No per-port count or thermal limit is published in the sources checked. | TMG-1; [C8300-4T2X-WP-1](#c8300-4t2x-wp-1) Table 1 note |
| `C-NIM-1X` | 1G / 10G | SFP/SFP+ | `SFP-10G-T-X`: 10GBASE-T only. `GLC-TE` not listed. | TMG-2 |
| `C-NIM-4X` | 100M (FX) / 1G / 10G | SFP/SFP+ | `GLC-TE`: 1000BASE-T and 100BASE-T, from 17.18.1. `SFP-10G-T-X`: 1000BASE-T and 10GBASE-T. `SFP-10G-ZR-I` from 17.18.2. | TMG-2 |
| `C-NIM-2T` | 100M / 1G | RJ-45 / SFP | SFP side: 100BASE-FX/LX/EX and 1G optics. No copper SFP listed. | TMG-2; [C8300-4T2X-DS-1](#c8300-4t2x-ds-1) Table 7 |

#### Minimum set

"Not verified" means not listed in TMG for that port type; it does not mean
unsupported.

| Item | Built-in SFP+ (Te0/0/4–5) | C-NIM-1X | C-NIM-4X | C-NIM-2T (SFP) | Reach / media |
| --- | --- | --- | --- | --- | --- |
| 1000BASE-SX | `GLC-SX-MMD` (17.3.2) | `GLC-SX-MMD` | `GLC-SX-MMD` (17.11.1) | `GLC-SX-MMD` (17.6.1) | 1,000 m OM3/OM4; 550 m OM2; MMF |
| 1000BASE-LX/LH | `GLC-LH-SMD`, `GLC-LX-SM-RGD` (17.3.2) | Same | Same (17.11.1) | Same (17.6.1) | 10 km SMF (550 m on MMF) |
| 1000BASE-ZX | `GLC-ZX-SMD` (17.3.2) | `GLC-ZX-SMD` | `GLC-ZX-SMD` (17.11.1) | `GLC-ZX-SMD` (17.6.1) | 70 km SMF |
| 1000BASE-T SFP | `GLC-TE` (17.3.2), 1000BASE-T only | Not verified | `GLC-TE` (17.18.1), 100M and 1G | Not verified | 100 m Cat5e |
| 10GBASE-SR | `SFP-10G-SR` (17.3.2), `SFP-10G-SR-S` (17.6.1) | Same | Same (17.11.1) | n/a (1G module) | 400 m OM4; 300 m OM3 |
| 10GBASE-LR | `SFP-10G-LR` (17.3.2), `SFP-10G-LR-S` (17.6.1) | Same | Same (17.11.1) | n/a | 10 km SMF |
| 10GBASE-ER | `SFP-10G-ER` (17.3.2) | `SFP-10G-ER` | `SFP-10G-ER` (17.11.1), `SFP-10G-ER-S` (17.18.2) | n/a | 40 km SMF |
| 10GBASE-ZR | **Not verified** | **Not verified** | `SFP-10G-ZR-I` (17.18.2; above the 17.15.6 basis) | n/a | 70 km SMF (as listed in TMG) |
| 10GBASE-T SFP+ | `SFP-10G-T-X` (17.6.1), 10G only | `SFP-10G-T-X`, 10G only | `SFP-10G-T-X` (17.11.1), 1G and 10G | n/a | 30 m Cat6A/7 |
| 10G DAC | `SFP-H10GB-CU1M/2M/3M/4M/5M` (17.9.1); `-ACU7M`, `-ACU10M` (17.3.2) | `-ACU7M`, `-ACU10M` only | `-ACU7M`, `-ACU10M` (17.11.1) | n/a | 1–10 m |
| 1G DAC | **Not verified** | Not verified | Not verified | Not verified | — |

Long-reach notes: `GLC-ZX-SMD` and `SFP-10G-ER` carry no platform note in TMG.
`SFP-10G-ZR-I` has a transceiver note about cold start: optical traffic is not
supported from −40 °C to −28 °C. No distance, power, or port restriction for
long-reach optics on this chassis was found. Also listed but outside the
minimum set: 10G AOC cables (17.9.1), 1G/10G BiDi
(`GLC-BX*`, `SFP-10G-BX*`), `GLC-EX-SMD` (40 km), and `SFP-10G-LRM`.

#### Ports faster than 10G

**None.** The chassis has 2 × 10G SFP+ and 4 × 1G RJ-45. The C8300 modules
listed top out at 10G ([C8300-4T2X-DS-1](#c8300-4t2x-ds-1) Tables 2, 7). No
25G, 40G, or QSFP ports.

#### Copper SFPs

| Port type | 1G copper SFP (1000BASE-T) | 10G copper SFP+ (10GBASE-T) | Restrictions |
| --- | --- | --- | --- |
| Built-in SFP+ Te0/0/4–0/0/5 | **Yes**: `GLC-TE`, 1000 Mb/s only (100 Mb/s not supported), 100 m | **Yes**: `SFP-10G-T-X`, 10 Gb/s only on this chassis, 30 m on Cat6A/Cat7 | No count, thermal, or adjacent-port limit found in TMG or the datasheet. Not verified. |
| `C-NIM-1X` | Not verified | **Yes**: `SFP-10G-T-X`, 10GBASE-T only | As above |
| `C-NIM-4X` | **Yes**: `GLC-TE`, 100 Mb/s and 1000 Mb/s, from 17.18.1 (not at the 17.15.6 basis) | **Yes**: `SFP-10G-T-X`, 1G and 10G, from 17.11.1 | As above |
| `C-NIM-2T` SFP side | Not verified (the module also has RJ-45 ports) | n/a | — |

Source: [C8300-4T2X-TMG-1](#c8300-4t2x-tmg-1),
[C8300-4T2X-TMG-2](#c8300-4t2x-tmg-2) (network-model notes). The four
built-in RJ-45 ports meet a 10/100/1000 copper need without copper SFPs. They
do not provide 10G copper.

#### Platform policy

- **Third-party optics / `service unsupported-transceiver`:** not found in
  Cisco documentation for this platform in the sources checked. Its effect on
  TAC support is **not verified**. The HIG LED table shows an amber "SFP EN"
  LED for "SFP is not supported or is in a faulty state"
  ([C8300-4T2X-HIG-1](#c8300-4t2x-hig-1) Table 6).
- **DOM:** TMG marks DOM capable "Y" with DOM support from IOS XE 17.3.2 for
  the listed fiber optics on the built-in ports, and from 17.6.1 for the `-S`
  variants. There is no DOM for DACs, AOCs, `GLC-TE`, or `SFP-10G-T-X`
  ([C8300-4T2X-TMG-1](#c8300-4t2x-tmg-1)). A DOM display command is not
  verified for this platform ([Appendix A](#commands-not-verified-for-this-platform)).

#### Not reviewed in this research

| Optics family | Status |
| --- | --- |
| CWDM | Needed, not reviewed in this research |
| DWDM | Needed, not reviewed in this research (TMG lists DWDM entries for `C-NIM-1X` and `C-NIM-4X`, not for the built-in ports) |
| BiDi | Needed, not reviewed in this research |
| Extended-temperature (industrial) optics | Needed, not reviewed in this research |

### Module reuse across the four platforms

- **From ISR 4431:** Cisco says the C8300 keeps backward compatibility with
  "most" ISR 4000 NIMs and SMs and that over 70 % of ISR 4000 modules are
  reused ([C8300-4T2X-OG-1](#c8300-4t2x-og-1) section D;
  [C8300-4T2X-DS-1](#c8300-4t2x-ds-1) "Sustainability"). Per-PID: an ISR 4000
  module fits only if it is in the C8300 lists above. Not listed for C8300 in
  either source: for example `NIM-2GE-CU-SFP` and older UCS-E M2. That is
  absence from the lists, not proof of non-support. The reverse direction:
  `C-NIM-1X`, `C-SM-NIM-ADPTR`, `C-SM-16P4M2X`, and `C-SM-40P8M2X` are "not
  compatible with Cisco 4000 Series ISRs" (OG-1 Table 5 footnote).
- **With C8375-E-G2:** the 8000 Series Secure Routers ordering guide lists for
  C8375-E-G2 `C-NIM-4X`, `C-NIM-8T`, `C-NIM-8M`, `C-SM-16P4M2X`, `C-SM-NIM-ADPT`,
  `NIM-1T/2T/4T`, `NIM-16A/24A`, `SM-X-64A`, the analog voice NIMs and SM-X
  modules, and `NIM-4E/M` and the BRI NIMs. It also lists new WAN NIMs
  `C-NIM-WAN-2X` and `C-NIM-WAN-4S`. FXO/FXS are supported in Routing (CLI)
  mode from 26.1, and BRI and E&M from 26.2
  ([C8300-4T2X-OG-2](#c8300-4t2x-og-2), p. 14). `C-NIM-1X`, `C-NIM-2T`,
  `C-NIM-1M`, `NIM-ES2-*`, PVDM DSPs, T1/E1, DSL, and UCS-E were **not found**
  in that list. Whether `C-NIM-WAN-2X/4S` work in the C8300-1N1S-4T2X is not
  verified (they are absent from the C8300 lists).
- **With C8300-1N1S-6T:** same chassis, slots, and module lists in OG-1 and
  DS-1 (**documented** shared lists; identical support inferred).

## Platform-specific caveats

| Item | Affected | Impact | Fix / mitigation | Source |
| --- | --- | --- | --- | --- |
| End-of-Sale announced (EOL15950) | Chassis, `PWR-CC1-500WAC`, `M2USB-75G` | Orderable until 2027-01-31; last train 28.2.x; Last Date of Support 2032-01-31 | Order before 2027-01-31 or choose `C8375-E-G2` | [C8300-4T2X-EOL-1](#c8300-4t2x-eol-1) |
| FN74146: DRAM memory failures (rev. 2.0 added the C8300 chassis) | All four C8300 PIDs; `MEM-C8300-8GB=`, `MEM-C8300-32GB=`; **serial-number dependent** | Persistent correctable memory errors, which can lead to an uncorrectable event | Check serials in the Serial Number Validation Tool; DRAM replacement program | [C8300-4T2X-FN-1](#c8300-4t2x-fn-1) |
| FN72510: weak crypto algorithms not allowed by default for IPsec | Catalyst 8000 IOS XE 17.11.1a and later, including basis 17.15.6 | Legacy weak-algorithm IPsec peers can fail negotiation | Use supported strong algorithms; inspect peer configuration before upgrade | [C8300-4T2X-FN-2](#c8300-4t2x-fn-2), Enterprise Routing table |
| FN72578: SLP might cause high CPU/memory | Enumerated 17.3.2a–17.7.1 releases; basis 17.15.6 is above the documented fixes | Accumulated unacknowledged RUM reports caused high CPU/memory on affected versions | Cisco fixes: 17.3.7, 17.6.5, 17.9.1 or later. Does not prove a generic feature-throttle consequence for missing reports. | [C8300-4T2X-FN-3](#c8300-4t2x-fn-3) |
| FN74350: CUBE and public-CA client-auth EKU changes (May 2026) | Exact PID listed; applicability depends on CUBE TLS trustpoint/peer certificates | Certificate EKU changes may affect mutual TLS; prior to 26.1.1 strict EKU validation depends on match eku client-auth or cc-mode | Check the notice alternatives and peer trust; new certificate handling enhancements start at 26.1.1, above basis | [C8300-4T2X-FN-4](#c8300-4t2x-fn-4), Products Affected and Option 4 |
| Snort 3 security advisories, 2026-10-22 (several DoS) | UTD on IOS XE using an affected Snort 3 package | October hardening addresses memory, privilege and resource vulnerabilities; no workaround documented | For 17.15, Cisco names **secapp-utd.17.15.06.1.0.21_SV3.12.4.0_XE17.15** with Snort 3.12.4.0. Router IOS XE 17.15.6 alone does not prove the UTD package is fixed. | [C8300-4T2X-PSIRT-1](#c8300-4t2x-psirt-1), UTD fixed-release table |
| 26.2.1 secure-by-default changes | 26.2.1 and later | RADIUS Message-Authenticator required (ISE must send Attribute 80); proxy ARP off; HTTP server off on factory config; outbound SSH TOFU | Plan ISE and config changes before moving above 17.x | [C8300-4T2X-RN-3](#c8300-4t2x-rn-3) Table 1 |
| Controller-mode switch erases configuration | Mode conversion | Startup config and NVRAM (certificates) erased | Back up first | [C8300-4T2X-SCG-1](#c8300-4t2x-scg-1) pp. 7–8 |
| Overrun drops with uneven GRE traffic distribution across data-plane cores (CSCws72902) | C8200/C8300/C8500L; resolved in 17.18.3a; applicability to the 17.15.6 basis not established by this row | GRE traffic can be distributed unevenly and drop | The public 17.18.x notes list resolution in 17.18.3a. CSCws95993 is a different, adjacent licensing bug. | [C8300-4T2X-RN-2](#c8300-4t2x-rn-2), Table 5, re-read 2026-10-31 UTC |
| ROMMON minimum | Units with ROMMON below 17.3(4.2r) | Cannot boot newer trains directly | Boot 17.12.5 to auto-upgrade, or upgrade ROMMON | [C8300-4T2X-RN-3](#c8300-4t2x-rn-3) |

This decision-relevant review read the cited notices and advisory fixed-release
sections. **Documented:** the August 2026 IOS XE hardening advisory names
17.15.6 as its first fixed 17.15 release, matching this basis
([C8300-4T2X-PSIRT-2](#c8300-4t2x-psirt-2)). This establishes coverage for that
advisory, not a universal security clearance. Configuration-specific exposure,
installed UTD package and hardware serial applicability still need deployment
validation. An exhaustive vulnerability assessment is outside this research.

### Differences from the sibling C8300-1N1S-6T

| Item | C8300-1N1S-4T2X | C8300-1N1S-6T | Source |
| --- | --- | --- | --- |
| Ports 0/0/4–0/0/5 | SFP+ 10G (accepts 1G SFP) | SFP 1G | [C8300-4T2X-HIG-1](#c8300-4t2x-hig-1) Table 1; [C8300-4T2X-OG-1](#c8300-4t2x-og-1) Table 1 |
| IPsec 1400 B / IMIX (autonomous) | 16.9 / 6.6 Gbps | 1.9 / 1.9 Gbps | [C8300-4T2X-DS-1](#c8300-4t2x-ds-1) Table 5 |
| SD-WAN IPsec 1400 B | 17 Gbps | 2 Gbps | DS-1 Table 3 |
| Typical power (no modules, single PSU) | 245 W | 82 W | DS-1 Table 11 |
| CEF aggregation ceiling | 12 Gbps | 10 Gbps | [C8300-4T2X-WP-1](#c8300-4t2x-wp-1) |
| Highest autonomous throughput level | Numeric 2.5G = 5G aggregate; tier T3 = 20G aggregate (published entitlement table; source conflict retained) | Numeric 1G / T2 = 2G aggregate | [C8300-4T2X-LIC-1](#c8300-4t2x-lic-1), Tables 5–6; [Source conflicts](#source-conflicts) |
| Controller-mode crypto with HSECK9 | Unthrottled | 2G aggregate | LIC-1 p. 19 |
| Crypto throughput drop syslog | Not in Cisco's supported-platform list | Listed | LIC-1 "Crypto throughput logging" (the 17.18 notes say "Catalyst 8300"; see conflicts) |
| Hyperthreading | Listed | Listed (inferred; page break) | HIG-1 pp. 1–2 |
| Slots, modules, PSUs, memory, lifecycle | Same | Same (6T also has the `-V` voice bundle, EoS) | OG-1; DS-1; [C8300-4T2X-EOL-1](#c8300-4t2x-eol-1) |

### Source conflicts

| Topic | Claim A | Claim B | Resolution |
| --- | --- | --- | --- |
| Lifecycle status | Request pre-check: "Current; no EoL notice found" | EOL15950 (2026-07-27, amended 2026-10-19): End-of-Sale 2027-01-31 | **EOL15950 applies** (exact PID, Cisco bulletin) |
| T1 numeric value | LIC-1 tier image and CLI: T1 = 25M–100M ("up to 100 mbps") | [C8300-4T2X-DNA-1](#c8300-4t2x-dna-1) Table 6: "up to 200 Mbps (Agg. 400)"; [C8300-4T2X-OG-1](#c8300-4t2x-og-1) Table 11: "up to 250M BW (500M Aggr)" | Unresolved. LIC-1's entitlement table (with HSECK9, 17.14.1a+: 500M aggregate) agrees with OG-1. Confirm with Cisco. |
| T3 numeric value on this PID | LIC-1 entitlement table: 10G bidirectional / 20G aggregate; OG-1 Table 11: "up to 10G BW (20G Aggr)" | LIC-1 tier image: T3 column covers only 2.5G for this PID; a LIC-1 CLI example shows "T3 (up to 5 gbps) aggregate" | Unresolved. The platform's published IPsec maximum (16.9 Gbps at 1400 B) is below 20G aggregate either way. |
| Catalyst Routing Essentials crypto | OG-1: crypto "up to 2Gbps" (BoM includes `NWSTACK-T2-E`) | [C8300-4T2X-DNA-2](#c8300-4t2x-dna-2): "Throughput capability for IP-CEF and Crypto traffic up to device capability" | Unresolved; OG-1 is more specific (2026-06-17). Confirm with Cisco. |
| CME support | DS-1 Table 13 lists CUCME for autonomous mode | [C8300-4T2X-FAQ-1](#c8300-4t2x-faq-1) lists "Call Manager Express (CME)" as an exception to ISR 4000 feature parity | Unresolved |
| Crypto throughput logging on 4T2X | [C8300-4T2X-RN-2](#c8300-4t2x-rn-2): from 17.18.1a "on Cisco Catalyst 8300 and Catalyst 8200" | LIC-1 supported list names only the 6T models and the C8200s | Unresolved |
| Built-in SFP+ MACsec | WP-1: "1G/10G WAN MACsec is possible on the … SFP+ built-in ports" | WP-1 Table 1: "MACsec on SFP+ ports on C8300-2N2S-4T2X" | Unresolved for the 1RU model |
| Default core allocation | DS-1 and WP-1: service-oriented is the factory default for C8300 | CPU-1 (run on C8500L): data-plane-heavy is "the default template for standard routing" | DS-1 applies (exact family; CPU-1 examples are from another platform) |
| 600 GB NVMe PID | DS-1: `SSD-M2SED-600G` | OG-1: `SSD-M2NVME-600G` | Unresolved naming; check in CCW |
| TrustSec SGT tier | [C8300-4T2X-TS-1](#c8300-4t2x-ts-1) p. 5: Network Advantage | [C8300-4T2X-MX-1](#c8300-4t2x-mx-1): "Network segmentation" (TrustSec SGT, SGACL) ticked for all three tiers | **Unresolved**; Network Advantage is assumed (the stricter reading) until Cisco confirms |

## Appendix A: identification and inventory commands

All commands below are read-only, privileged EXEC (`#`) unless noted. Before
sharing output, **redact serial numbers and UDIs**.

### Annotated listing

Platform, version, mode, and inventory
([C8300-4T2X-SCG-1](#c8300-4t2x-scg-1): Call Home command lists pp. 190–194
and `show version` sample pp. 47–48):

```text
show version
! Model, IOS XE version, "Router operating mode: Autonomous|Controller", license level, memory
show inventory
! PID, VID, serial for chassis, PSUs, fan tray, modules, and transceivers
show platform
! Slot/subslot state of the chassis, modules, and PSUs
show environment
! Temperature, power, and fan sensors (power/fan status)
show diag all eeprom detail
! EEPROM detail per FRU (PID/VID/serial, hardware revision)
show hw-module subslot all oir
! Module online-insertion state per subslot (SCG-1 pp. 105-106)
```

Install vs. bundle mode ([C8300-4T2X-SCG-1](#c8300-4t2x-scg-1) Table 9,
pp. 49–51):

```text
show install summary
! Install-mode package state; in bundle mode the boot is a single .bin
show install active
! Active packages (install mode)
show install committed
! Committed packages (install mode)
```

Licensing and reporting ([C8300-4T2X-SLP-1](#c8300-4t2x-slp-1) command
references; [C8300-4T2X-LIC-1](#c8300-4t2x-lic-1)):

```text
show license udi
! Chassis UDI (PID + serial) used for SLAC and CSSM
show license summary
! Licenses in use, e.g. network-advantage_T2, dna-advantage_T2, DNA_HSEC
show license status
! Transport type, trust code installed, Next ACK deadline
show license usage
! Per-license usage and enforcement type
show license authorization
! SLAC status, e.g. "SMART AUTHORIZATION INSTALLED" for DNA_HSEC
show license all
! Policy in use and reporting requirements
show license rum
! RUM reports held on the device (17.7.1 and later)
show platform hardware throughput crypto
! Configured and enforced crypto throughput level, boot level
```

Security identity and CPU allocation
([C8300-4T2X-SCG-1](#c8300-4t2x-scg-1) p. 212;
[C8300-4T2X-CPU-1](#c8300-4t2x-cpu-1)):

```text
show platform sudi certificate
! SUDI certificate chain (hardware trust anchor identity)
show platform software cpu allocation
! Control/data/service core split and template; example output in CPU-1 is from a C8500L
```

### Paste-ready capture block

```text
terminal length 0
show version
show inventory
show platform
show environment
show diag all eeprom detail
show hw-module subslot all oir
show install summary
show install active
show install committed
show license udi
show license summary
show license status
show license usage
show license authorization
show license all
show license rum
show platform hardware throughput crypto
show platform sudi certificate
show platform software cpu allocation
```

### Commands not verified for this platform

Left out of the capture block because no C8300 source for them was found in
the documents checked:

- Transceiver detail / DOM light levels and temperature (for example
  `show interfaces transceiver detail`, or
  `show hw-module subslot 0/0 transceiver <port> status`). DOM support is
  documented by TMG, but the display command is not.
- `show sdwan …` commands for controller-mode checks (controller mode out of
  baseline scope).
- `show rom-monitor r0` appears in the 26.2.x release-note ROMMON procedure
  ([C8300-4T2X-RN-3](#c8300-4t2x-rn-3)). It was left out because that page is
  an upgrade procedure, not a command reference. It is a likely-safe candidate
  to add after checking.

## References

#### C8300-4T2X-MSR-1

- Title: IP Multicast Configuration Guide, Cisco IOS XE, “Implementing Multicast Service Reflection”
- Used for: MSR configuration, prerequisites, Vif restrictions, unicast-to-multicast behavior, and feature introduction information
- URL: https://www.cisco.com/c/en/us/td/docs/routers/ios-xe/ip-multicast/ip-multicast/m_imc_service_reflect-0.html
- Accessed: 2026-11-01
- Locator: Implementing Multicast Service Reflection; Feature Information for Multicast Service Reflection
- Local PDF: not saved (HTML)

#### C8300-4T2X-MSR-REL-1

- Title: Release Notes for Cisco Catalyst 8200 and Catalyst 8300 Series Edge Platforms, Cisco IOS XE Cupertino 17.9.x
- Used for: family/release-level evidence for Unicast-to-Multicast Destination Reflection
- URL: https://www.cisco.com/c/en/us/td/docs/routers/cloud_edge/c8300/rel_notes/17_9_x/cat8200-and-8300-rel-notes-xe-17-9-x.html
- Accessed: 2026-11-01
- Locator: New and Changed Information; feature entry for IOS XE 17.9.1a
- Local PDF: not saved (HTML)

#### C8300-4T2X-MSR-LIC-1

- Title: Configure and Troubleshoot Multicast Service Reflection on Catalyst 8000
- Used for: Network Advantage licensing indication only; Cisco's example is a Catalyst 8500 running IOS XE 17.9.4, not this PID
- URL: https://www.cisco.com/c/en/us/support/docs/ip/protocol-independent-multicast-sparse-mode-pim-sm/221125-configure-and-troubleshoot-multicast-ser.html
- Accessed: 2026-11-01
- Locator: Requirements and lab configuration
- Local PDF: not saved (HTML)

Original source access dates are 2026-10-30. Newly read public sources and
review rechecks use 2026-10-31 UTC; the cutoff remains 2026-10-30
America/Chicago. Each register gives its actual access date. "PDF" links
point to preserved local copies in `reference/`.

### Cisco datasheets, ordering, and hardware

#### C8300-4T2X-DS-1

- Title: Cisco Catalyst 8300 Series Edge Platforms Data Sheet
- Used for: identity, specifications, performance, scale, modules, PSUs,
  minimum software, licensing names
- URL: https://www.cisco.com/c/en/us/products/collateral/routers/catalyst-8300-series-edge-platforms/datasheet-c78-744088.html
  (PDF: https://www.cisco.com/c/en/us/products/collateral/routers/catalyst-8300-series-edge-platforms/datasheet-c78-744088.pdf)
- Date / revision: updated 2026-10-06
- Accessed: 2026-10-30
- Locator: Tables 1–16 (Table 2–3 p. 6; Tables 4–6 p. 7; Table 7 p. 12;
  Table 8 p. 15; Table 9 p. 16; Tables 10–11 p. 17; Tables 12–13 p. 18;
  Table 14 p. 19; Table 15 p. 20)
- Local PDF: [c8300-edge-datasheet-2026-10-06.pdf](reference/c8300-edge-datasheet-2026-10-06.pdf)

#### C8300-4T2X-OG-1

- Title: Cisco Catalyst 8300/8200 Series Edge Platforms Ordering Guide
- Used for: PIDs, slots, module list, PSU options, HSEC PIDs, UC licensing,
  DNA tiers, Catalyst Routing Essentials
- URL: https://www.cisco.com/c/en/us/products/collateral/routers/catalyst-8300-series-edge-platforms/cat-8300-8200-series-edge-plat-og.html
- Date / revision: updated 2026-06-17
- Accessed: 2026-10-30
- Locator: Tables 1–12; Table 11 is an image on PDF p. 15
- Local PDF: [c8300-c8200-edge-og-2026-06-17.pdf](reference/c8300-c8200-edge-og-2026-06-17.pdf)

#### C8300-4T2X-OG-2

- Title: Cisco 8000 Series Secure Routers Ordering Guide (saved by the
  C8375-E-G2 agent; reused)
- Used for: module list for C8375-E-G2 (reuse check only)
- URL: <https://www.cisco.com/c/en/us/products/collateral/networking/sdwan-routers/8000-secure-routers/8000-secure-router-og.html> (official equivalent; the preserved local PDF was read)
- Date / revision: 2026-10-09 as recorded for the same preserved source in C8375-OG-1; no newer revision substituted
- Accessed: 2026-10-30 (local copy read)
- Locator: PDF p. 14 (supported modules)
- Local PDF: [c8000-secure-routers-og-2026-10-09.pdf](reference/c8000-secure-routers-og-2026-10-09.pdf)

#### C8300-4T2X-HIG-1

- Title: Hardware Installation Guide for Cisco Catalyst 8300 Series Edge
  Platforms, chapter "Overview"
- Used for: chassis views, port numbering, hyperthreading list, PSU option
  table, LEDs, memory options
- URL: https://www.cisco.com/c/en/us/td/docs/routers/cloud_edge/c8300/hardware_installation/b-catalyst-8300-series-edge-platforms-hig.html
  (guide landing page; the saved PDF is the Overview chapter only)
- Date / revision: PDF created 2026-06-15, modified 2026-06-18 (no revision
  printed); pre-existing file, reused
- Accessed: 2026-10-30 (local copy)
- Locator: p. 1 (HT list), p. 2 (continuation bullet, Table 1), p. 10
  (memory, Table 5), pp. 11–12 (Table 6)
- Local PDF: [c8300-edge-hig-overview-2026-06.pdf](reference/c8300-edge-hig-overview-2026-06.pdf)

#### C8300-4T2X-WP-1

- Title: Cisco Catalyst 8300 and 8200 Series Edge Platforms Architecture
  White Paper
- Used for: CPU cores, QAT, core allocation, CEF aggregation, port options
- URL: https://www.cisco.com/c/en/us/products/collateral/routers/catalyst-8200-series-edge-platforms/catalyst-8300-8200-series-edge-platforms-architecture-wp.html
- Date / revision: updated 2022-09-23
- Accessed: 2026-10-30
- Locator: "Dynamic core allocation", Figure 12 notes, "Connectivity
  options", Tables 1–2

#### C8300-4T2X-FAQ-1

- Title: Cisco Catalyst 8300 Series Edge Platforms FAQ
- Used for: Trustworthy features, QAT, MPLS license, ISR 4000 parity,
  licensing behavior, HSEC
- URL: https://www.cisco.com/c/en/us/products/collateral/routers/catalyst-8300-series-edge-platforms/cat-8300-series-edge-qa.html
- Date / revision: updated 2026-06-23
- Accessed: 2026-10-30
- Locator: "Security", "Licensing" questions

#### C8300-4T2X-SCG-1

- Title: Catalyst 8200 and Catalyst 8300 Edge Software Configuration Guide
- Used for: mode switching, install/bundle mode, show-command evidence, CoA
  limitations, SUDI
- URL: https://www.cisco.com/c/en/us/td/docs/routers/cloud_edge/c8300/software_config/cat8300-edge-software-config.html
  (PDF: https://www.cisco.com/c/en/us/td/docs/routers/cloud_edge/c8300/software_config/cat8300-edge-software-config.pdf)
- Date / revision: updated 2026-05-04 (PDF generated 2026-09-28)
- Accessed: 2026-10-30
- Locator: pp. 7–8, 47–51, 105–106, 190–194, 203, 212
- Local PDF: [c8300-c8200-edge-swcfg-2026-05-04.pdf](reference/c8300-c8200-edge-swcfg-2026-05-04.pdf)

#### C8300-4T2X-CPU-1

- Title: Configure and Troubleshoot Catalyst 8000 CPU Resource Allocation
  (TAC tech note 225805)
- Used for: `platform resource` templates, CPU allocation command, HT mention
- URL: https://www.cisco.com/c/en/us/support/docs/routers/catalyst-8000v-edge-software/225805-configure-and-troubleshoot-catalyst.html
- Date / revision: updated 2026-04-24
- Accessed: 2026-10-30
- Locator: "Configure", "Check CPU Allocation" (examples run on C8500L)

### Lifecycle

#### C8300-4T2X-EOL-1

- Title: End-of-Sale and End-of-Life Announcement for the Cisco Catalyst
  C8500L-8S4X, C8300-1N1S-4T2X, C8300-1N1S-6T (EOL15950, amended)
- Used for: all chassis milestones, last IOS XE train, migration product,
  affected accessories
- URL: https://www.cisco.com/c/en/us/products/collateral/networking/sdwan-routers/catalyst-8000-edge-platforms/catalyst-c8500l-8s4x-4t2x-c8300-1n1s-6t-eol.html
- Date / revision: announced 2026-07-27; page updated 2026-10-19
- Accessed: 2026-10-30
- Locator: Table 1 (PDF pp. 3–4), release-train sentence and Table 2 (p. 4)
- Local PDF: [c8300-1n1s-eol15950-2026-10-19.pdf](reference/c8300-1n1s-eol15950-2026-10-19.pdf)

#### C8300-4T2X-EOL-2

- Title: End-of-Sale and End-of-Life Announcement for the Cisco Select
  Catalyst 8300, 8200 and 8500 series Convenience Bundles (EOL14900)
- Used for: `C8300-DNA` bundle milestones
- URL: https://www.cisco.com/c/en/us/products/collateral/routers/catalyst-8300-series-edge-platforms/select-catalyst-8300-8200-8500-series-convenience-bundles-eol.html
- Date / revision: updated 2022-11-07
- Accessed: 2026-10-30
- Locator: Tables 1–2

#### C8300-4T2X-EOL-3

- Title: End-of-Sale and End-of-Life Announcement for the Cisco IOS XE 17.15.x
  (EOL15772, amended)
- Used for: 17.15.x milestones
- URL: https://www.cisco.com/c/en/us/products/collateral/ios-nx-os-software/ios-xe-17/ios-xe-17-15-x-eol.html
- Date / revision: updated 2025-10-01
- Accessed: 2026-10-30
- Locator: Table 1

#### C8300-4T2X-EOL-4

- Title: End-of-Sale and End-of-Life Announcement for the Cisco IOS XE 17.12.x
  (EOL15518)
- Used for: 17.12.x milestones
- URL: https://www.cisco.com/c/en/us/products/collateral/ios-nx-os-software/ios-xe-17/ios-xe-17-12-x-eol.html
- Date / revision: updated 2024-10-03
- Accessed: 2026-10-30
- Locator: Table 1

#### C8300-4T2X-SUP-1

- Title: Cisco Catalyst 8300 Series Edge Platforms support page and EoL
  listing
- Used for: series release date, "EOL Announced" status, document and field
  notice listings (titles only)
- URL: https://www.cisco.com/c/en/us/support/routers/catalyst-8300-series-edge-platforms/series.html
  and https://www.cisco.com/c/en/us/products/routers/catalyst-8300-series-edge-platforms/eos-eol-notice-listing.html
- Date / revision: not stated (listing entries dated up to 2026-10-30)
- Accessed: 2026-10-30
- Locator: "Overview", "Field Notices", "End-of-Life and End-of-Sale Notices"

### Software releases

#### C8300-4T2X-REC-1

- Title: Recommended Releases for Catalyst 8000 Edge, ASR1000, ISR4000 and
  ISR1000 Platforms (TAC document 215567)
- Used for: Cisco-recommended release; extended/standard support model;
  install-mode and PAK notes
- URL: https://www.cisco.com/c/en/us/support/docs/ios-nx-os-software/ios-xe-16/215567-recommended-releases-for-asr1000-isr400.html
- Date / revision: revision 9.0, 2026-06-15
- Accessed: 2026-10-30
- Locator: "Recommendations" table, row "Catalyst 8300"; "Additional
  Considerations"

#### C8300-4T2X-RN-1

- Title: Release Notes for Cisco Catalyst 8200 and Catalyst 8300 Series Edge
  Platforms, Cisco IOS XE Release 17.15.x
- Used for: 17.15.6 content, ROMMON matrix, resolved bugs
- URL: https://www.cisco.com/c/en/us/td/docs/routers/cloud_edge/c8300/rel_notes/17-15-x/cat8200-and-8300-rel-notes-xe-17-15-x.html
- Date / revision: updated 2026-08-05
- Accessed: 2026-10-30
- Locator: "New and Changed Software Features in 17.15.6", Table 2,
  "Resolved Bugs in 17.15.6"

#### C8300-4T2X-RN-2

- Title: Release Notes for Catalyst 8200 and Catalyst 8300 Series Edge
  Platforms, Release 17.18.x
- Used for: newest 17.x rebuild (17.18.5), ROMMON matrix, crypto throughput
  logging, bugs
- URL: https://www.cisco.com/c/en/us/td/docs/routers/cloud_edge/c8300/rel_notes/17-18-x/release-notes-catalyst-8200-and-catalyst-8300-series-edge-platforms-release-17-18-x.html
- Date / revision: updated 2026-10-13
- Accessed: 2026-10-30
- Locator: "New software features" (17.18.1a), resolved issues, ROMMON table

#### C8300-4T2X-RN-3

- Title: Release Notes for Cisco Catalyst 8200 and Catalyst 8300 Series Edge
  Platforms, Release 26.2.x
- Used for: newest release (26.2.1), secure-by-default changes, ROMMON matrix
- URL: https://www.cisco.com/c/en/us/td/docs/routers/cloud_edge/c8300/rel_notes/26-x/release-notes-catalyst-8200-and-catalyst-8300-series-edge-platforms-release-26-2-x.html
- Date / revision: updated 2026-09-27
- Accessed: 2026-10-30
- Locator: Table 1, Table 2, "ROMMON Compatibility Matrix"

#### C8300-4T2X-RN-4

- Title: Release Notes for Catalyst 8200 and Catalyst 8300, Release 26.1.x
- Used for: hyperthreading search (no match); 26.1.2 is the latest rebuild
  listed
- URL: https://www.cisco.com/c/en/us/td/docs/routers/cloud_edge/c8300/rel_notes/26-x/release-notes-catalyst-8200-and-catalyst-8300-series-edge-platforms-release-26-1-x.html
- Date / revision: updated 2026-08-05
- Accessed: 2026-10-30
- Locator: table of contents

### Licensing sources

#### C8300-4T2X-LIC-1

- Title: Configure Licenses and Throughput for Catalyst 8000 Series Physical
  Platforms
- Used for: DNA license structure, HSECK9 rules, throughput tables,
  controller-mode entitlement, MSLA, commands
- URL: https://www.cisco.com/c/en/us/td/docs/routers/cloud_edge/configure-licenses-throughput-catalyst-8000-platforms.html
- Date / revision: PDF "Revised: May 4, 2026" (HTML page shows "Updated
  October 29, 2024")
- Accessed: 2026-10-30
- Locator: PDF p. 4 (DNA guidelines), pp. 4–6 (HSECK9), p. 13 (tier image),
  p. 17 (C8300-1N1S-4T2X table), p. 19 (controller mode), p. 24 (CLI
  examples), p. 29 (MSLA)
- Local PDF: [c8000-edge-licenses-throughput-2026-05-04.pdf](reference/c8000-edge-licenses-throughput-2026-05-04.pdf)

#### C8300-4T2X-SLP-1

- Title: Smart Licensing Using Policy for Cisco Enterprise Routing Platforms
- Used for: SLP concepts, default policy, offline and SSM On-Prem topologies
  and workflows, file import, commands, system messages
- URL: https://www.cisco.com/c/en/us/td/docs/routers/sl_using_policy/b-sl-using-policy.html
  (PDF: https://www.cisco.com/c/en/us/td/docs/routers/sl_using_policy/b-sl-using-policy.pdf)
- Date / revision: first published 2020-09-25; last modified 2023-08-01 (PDF
  generated 2026-09-01)
- Accessed: 2026-10-30
- Locator: printed pages 5–8 (Tables 1–4, default policy), 24–27
  (topologies), 45–46 (workflows), 154 (HSECK9 options), 203 and 215 (SLAC
  request, file import), 328 (system messages)
- Local PDF: [enterprise-routing-slp-guide-2023-08-01.pdf](reference/enterprise-routing-slp-guide-2023-08-01.pdf)

#### C8300-4T2X-DNA-1

- Title: Cisco DNA Software for SD-WAN and Routing Ordering Guide
- Used for: DNA PID format, cloud vs. on-premises variants, terms, tier
  definitions, security applicability matrix
- URL: https://www.cisco.com/c/en/us/products/software/one-wan-subscription/wan-subscription-part-number.html
  (redirects to https://www.cisco.com/c/en/us/products/collateral/software/dna-subscription-routing/guide-c07-740642.html)
- Date / revision: updated 2026-06-17
- Accessed: 2026-10-30
- Locator: Table 5, Table 6, Table 10 and notes, Step 4

#### C8300-4T2X-DNA-2

- Title: Cisco DNA Software for SD-WAN and Routing Subscriptions FAQ
- Used for: tier contents, Premier discontinuation, Routing Essentials terms,
  expiry behavior, enforcement
- URL: https://www.cisco.com/c/en/us/products/collateral/software/one-wan-subscription/nb-06-dna-sw-rout-sub-faq-ctp-en.html
- Date / revision: updated 2026-06-16
- Accessed: 2026-10-30
- Locator: offer overview, "Changes to the offer (August 2024)",
  "Catalyst 8000 Edge Platform Family offer structure", expiry question

#### C8300-4T2X-MX-1

- Title: Cisco DNA Software for SD-WAN and Routing feature matrix
- Used for: per-category tier map for autonomous mode (Catalyst Routing
  Essentials / DNA Essentials / DNA Advantage), the feature list behind each
  category, and footnotes 1 and 3. The tier ticks are images; they were read
  from the page code (`blue_tick.png` per tier cell) and the category lists
  from the page's tooltips, with a headless browser (Playwright Chromium),
  2026-10-30. Names no platforms.
- URL: https://www.cisco.com/c/m/en_us/products/software/sd-wan-routing-matrix.html
  (PDF: https://www.cisco.com/c/dam/m/en_us/products/software/dna-software/dna-software-sd-wan-routing-matrix/pdf/Cisco_DNA_Software_SD-WAN_and_Routing_Matrices.pdf;
  the old `c95-742999` PDF link redirects to the page)
- Date / revision: PDF modified 2025-05-02
- Accessed: 2026-10-30
- Locator: "Platform based routing features" section and footnotes
- Local copies:
  [reference/dna-sd-wan-routing-matrices-2025-05-02.pdf](reference/dna-sd-wan-routing-matrices-2025-05-02.pdf);
  [reference/dna-routing-matrix-tiers-2026-10-30.txt](reference/dna-routing-matrix-tiers-2026-10-30.txt)
  (derived text of ticks and category lists)

### Optics sources

#### C8300-4T2X-TMG-1

- Title: Cisco Optics-to-Device Compatibility Matrix, filtered to network
  device `C8300-1N1S-4T2X`
- Used for: built-in port optics, minimum releases, DOM, notes
- URL: https://tmgmatrix.cisco.com/ (results read through the site's public
  search, notes, and PDF-export endpoints with the device filter
  `C8300-1N1S-4T2X`)
- Date / revision: live data, exported 2026-10-30 (37 records)
- Accessed: 2026-10-30
- Locator: full result list; network-model notes for `GLC-TE` and
  `SFP-10G-T-X`
- Local PDF: [c8300-1n1s-4t2x-tmg-optics-2026-10-30.pdf](reference/c8300-1n1s-4t2x-tmg-optics-2026-10-30.pdf)

#### C8300-4T2X-TMG-2

- Title: Cisco Optics-to-Device Compatibility Matrix, filtered to
  `C-NIM-1X`, `C-NIM-4X`, `C-NIM-2T`
- Used for: module port optics, ZR, copper SFP behavior on modules
- URL: https://tmgmatrix.cisco.com/ (same method)
- Date / revision: live data, exported 2026-10-30
- Accessed: 2026-10-30
- Locator: per-module result lists and notes
- Local PDF: [c8300-nim-1x-4x-2t-tmg-optics-2026-10-30.pdf](reference/c8300-nim-1x-4x-2t-tmg-optics-2026-10-30.pdf)

### Features, ISE, and caveats

#### C8300-4T2X-TS-1

- Title: Cisco Group Based Policy – Platform and Capability Matrix
  (Inclusive of TrustSec Software-Defined Segmentation)
- Used for: TrustSec capabilities, license tier, scale, note 18
- URL: https://www.cisco.com/c/dam/en/us/solutions/collateral/enterprise-networks/trustsec/cisco-trustsec-platform-capability-matrix.pdf
- Date / revision: PDF dated 2026-02-23
- Accessed: 2026-10-30
- Locator: p. 5 (Tier 1 Catalyst 8000 row), p. 16 (SXP scale), p. 18
  (SGACL scale), p. 20 (note 18)
- Local PDF: [cisco-gbp-trustsec-platform-matrix-2026-02-23.pdf](reference/cisco-gbp-trustsec-platform-matrix-2026-02-23.pdf)

#### C8300-4T2X-FN-1

- Title: Field Notice FN74146 – Limited Number of Cisco Catalyst Routers Can
  Experience Memory Failures – Hardware Upgrade Available
- Used for: DRAM caveat, affected PIDs, serial validation
- URL: https://www.cisco.com/c/en/us/support/docs/field-notices/741/fn74146.html
- Date / revision: updated 2024-12-20 (revision 2.0 added the C8300 PIDs)
- Accessed: 2026-10-30
- Locator: "Products Affected", "Problem Description", "Workaround/Solution",
  "How to Identify Affected Products"

#### C8300-4T2X-SMSW-1

- Title: Cisco Catalyst 8000 SM-Based Switching Modules Data Sheet.
- URL: <https://www.cisco.com/c/en/us/products/collateral/routers/catalyst-8300-series-edge-platforms/catalyst-8000-sm-switch-module-ds.html>
- Revision: 2024-06-17. Accessed: 2026-10-31 UTC.
- Used for: C-SM-16P4M2X port authentication, DNA licensing, and 1RU PoE modes.
- Locators: Tables 1–3; Software; Security feature support. Both exact 1RU PIDs appear in Tables 2–3. No feature minimum release is supplied.

#### C8300-4T2X-HIG-2

- Title: Hardware Installation Guide, Prepare for Installation and Install Internal Components and Field Replaceable Units.
- URLs: <https://www.cisco.com/c/en/us/td/docs/routers/cloud_edge/c8300/hardware_installation/b-catalyst-8300-series-edge-platforms-hig/Preinstall.html>; <https://www.cisco.com/c/en/us/td/docs/routers/cloud_edge/c8300/hardware_installation/b-catalyst-8300-series-edge-platforms-hig/m-install-internal-modules-FRUs.html>
- Revision: Prepare chapter marked 2020-10-28; FRU revision not stated. Accessed: 2026-10-31 UTC.
- Used for: completing the power/cooling source check. Locators: Router Environmental Requirements, Power Guidelines and Requirements, fan/PSU installation. No maximum chassis consumption or BTU/h value was found; power guidance points to the data sheet. The live book TOC has no separate Technical Specifications chapter.

#### C8300-4T2X-EOL-5

- Title: End-of-Sale and End-of-Life Announcement for Cisco IOS XE 17.18.x (EOL15995).
- URL: <https://www.cisco.com/c/en/us/products/collateral/ios-nx-os-software/ios-xe-17/ios-xe-17-18-x-eol.html>
- Revision: 2026-10-30. Accessed: 2026-10-31 UTC. Locator: Table 1, migration guidance.
- Used for: 17.18.x milestones, migration to 26.1.1 or above.

#### C8300-4T2X-FN-2

- Title: FN72510, Weak Cryptographic Algorithms Are Not Allowed by Default for IPsec.
- URL: <https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72510.html>
- Revision: 1.5, 2026-01-20. Accessed: 2026-10-31 UTC.
- Used for/locator: Enterprise Routing affected-version table and workaround; Catalyst 8000 17.11.1a and later.

#### C8300-4T2X-FN-3

- Title: FN72578, Smart Licensing Using Policy Might Cause High CPU/Memory Usage.
- URL: <https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72578.html>
- Revision: 2023-09-29. Accessed: 2026-10-31 UTC.
- Used for/locator: Products Affected, Problem Description, Workaround/Solution; enumerated affected releases and fixed-release alternatives.

#### C8300-4T2X-FN-4

- Title: FN74350, CUBE TLS Certificates and Client Authentication EKU.
- URL: <https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74350.html>
- Revision: 2.0, 2026-06-23. Accessed: 2026-10-31 UTC.
- Used for/locator: Products Affected (exact PID), Workaround/Solution Option 4, first-fixed table. Applies conditionally to CUBE TLS designs.

#### C8300-4T2X-PSIRT-1

- Title: Multiple Cisco Products Snort 3 Security Hardening Release: October 2026.
- URL: <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-snort3-ybgmhTQe>
- Revision: 1.1, updated 2026-10-22. Accessed: 2026-10-31 UTC.
- Used for/locator: Affected Products and UTD on Cisco IOS XE Software fixed-release table. UTD package identity is separate from router image identity.

#### C8300-4T2X-PSIRT-2

- Title: Cisco IOS XE Software Security Hardening Release: August 2026.
- URL: <https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-hardening-iosxe-V8NMuMZJ.html>
- Revision: 1.1, updated 2026-10-02. Accessed: 2026-10-31 UTC.
- Used for/locator: Affected Products (autonomous/controller), Fixed Releases table (17.15.6).

#### C8300-4T2X-EOL-6

- Title: Cisco LAN Switch Network Interface Modules End-of-Sale and End-of-Life Announcement (EOL15562).
- URL: <https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/network-modules/lan-switch-network-interface-modules-eol.html>
- Revision: 2024-12-05. Accessed: 2026-10-31 UTC.
- Used for/locator: Tables 1–2, NIM-ES2-8/-8-P milestones and replacement names. Replacement naming alone does not prove host compatibility.

#### C8300-4T2X-EOL-7

- Title: Cisco Switch Module for Modular Platforms End-of-Sale and End-of-Life Announcement (EOL15584, amended).
- URL: <https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/network-modules/switch-modular-platform-eol.html>
- Revision: updated 2025-01-23. Accessed: 2026-10-31 UTC.
- Used for/locator: Tables 1–2, NIM-ES2-4 milestones. New-purchase availability is distinct from chassis/release compatibility.

### References - unresolved

No inaccessible URLs remain. The `c95-742999` matrix PDF link, previously
listed here, redirects to the matrix page now read in full
([C8300-4T2X-MX-1](#c8300-4t2x-mx-1)).

Required claims with no source found (sought, not found):

- Maximum power draw and heat dissipation (BTU/h), after checking HIG power/FRU chapters and the data sheet. Airflow direction is separately labeled as a visual inference from HIG Figure 9.
- TPM / named trust-anchor hardware.
- `service unsupported-transceiver` and the third-party optics TAC policy for
  this platform.
- A C8300 command reference for transceiver DOM display.
- Behavior when a SLP ACK deadline is missed; whether SSM On-Prem
  registration can be done fully offline.
- Release dates for 17.15.6 and 26.2.1 (Software Download, login required;
  not attempted).
- Published US pricing.
