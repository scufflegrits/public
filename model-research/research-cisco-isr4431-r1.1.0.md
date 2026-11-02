# Cisco ISR4431/K9 — Model Research (r1.1.0)

Standalone research file for model 1 of
`request-cisco-comparison-r1.1.0.md`. Reference baseline only: this model is
past End-of-Sale and cannot be bought new.

## Research status

| Item | Value |
| --- | --- |
| Revision | r1.1.0; 2026-10-30 America/Chicago (continuation access dates recorded separately). Review corrections and completion of previously unattempted public-source work. |
| Research cutoff | 2026-10-30 America/Chicago. Original research was accessed 2026-10-30; completion checks were accessed 2026-10-31 UTC (still 2026-10-30 America/Chicago). Source entries retain their actual access dates. |
| Source access dates | Original entries: 2026-10-30. Completion sources/rechecks: 2026-10-31 UTC (2026-10-30 America/Chicago). Publication, access and software-release dates remain separate. |
| Supplied name | Cisco 4431 |
| Confirmed identity | `ISR4431/K9` — Cisco 4000 Series Integrated Services Routers (ISR 4400 sub-family). Confirmed from EOL14896 Table 2 and the 4000 Family data sheet ordering text ([ISR4431-EOL-1](#isr4431-eol-1), [ISR4431-DS-1](#isr4431-ds-1)). No source contradicts the request's pre-check. |
| Software basis | Cisco IOS XE 17.12.8, autonomous; Cisco-recommended for ISR4431 ([ISR4431-REL-1](#isr4431-rel-1)); final train 17.12.x ([ISR4431-REL-3](#isr4431-rel-3)). Controller basis: IOS XE SD-WAN 17.12.8 with Manager 20.12.8.1 as a recommended same-train candidate ([ISR4431-SDWAN-1](#isr4431-sdwan-1)); the public matrix confirms Manager 20.12.8.1 with ISR4000 17.12.x at family level; exact ISR4431 PID applicability follows the family row. EOL14896 permits Manager 20.12/20.15/20.18, but that is not a recommendation for arbitrary rebuild combinations ([ISR4431-SDWAN-3](#isr4431-sdwan-3)). |
| Operating mode | Autonomous mode (enterprise branch / WAN edge). Controller mode supported from IOS XE 17.2.1 ([ISR4431-DS-1](#isr4431-ds-1)). |
| Orderable new | **No.** End-of-Sale 2023-11-07; reference baseline only, not eligible for recommendation. |
| Run status | **Complete, with explicit evidence gaps.** The continuation read the public controller recommendation and device matrix, the previously omitted module data sheets, selected current PSIRT advisories and relevant field notices. This is a decision-relevant review, not an exhaustive CVE assessment. No required public-source section is left unattempted. |
| Access-limited or omitted scope | Login-gated Software Download (exact image release dates), Feature Navigator and Software Checker were not used; US quote/pricing is not applicable to a new ISR4431 order because the chassis is End-of-Sale. Exhaustive CVE enumeration, hardware testing, and out-of-scope cellular/special optics are excluded. Required module and advisory research was attempted; unresolved exact-release support and module orderability remain evidence gaps. |
| Material evidence gaps | Exact ISR4000 DNA feature-tier applicability remains inferred; actual IPsec throughput with HSEC/Boost, routing scale, DOM show syntax and third-party optics policy remain unverified. Module chassis support is now documented for the listed switch, voice, PVDM4, DSL and BRI data families; exact 17.12.8 recertification and current module orderability are not established for every PID. See [References - unresolved](#references---unresolved). |
| Next steps for a deployment | Validate the actual UTD package, CPLD/ROMMON, module PIDs and serials; obtain Cisco confirmation for any unresolved feature or exact-release/module combination. New-purchase eligibility remains **fails** irrespective of these follow-ups. |

## Contents

- [Research status](#research-status)
- [Contents](#contents)
- [1. Summary](#1-summary)
- [2. Lifecycle status](#2-lifecycle-status)
  - [Chassis, spares, and licenses](#chassis-spares-and-licenses)
  - [Software train](#software-train)
  - [Replacement path](#replacement-path)
- [3. Hardware specifications](#3-hardware-specifications)
- [4. Performance](#4-performance)
- [5. Software](#5-software)
- [6. Licensing](#6-licensing)
  - [Feature entitlement](#feature-entitlement)
  - [Throughput and crypto](#throughput-and-crypto)
  - [Purchase and enforcement](#purchase-and-enforcement)
  - [Offline operation (no internet)](#offline-operation-no-internet)
- [7. Feature support and integration](#7-feature-support-and-integration)
  - [Feature matrix](#feature-matrix)
  - [Cisco ISE integration](#cisco-ise-integration)
- [8. Modules and expansion](#8-modules-and-expansion)
  - [Slot map](#slot-map)
  - [Module families](#module-families)
  - [Optics](#optics)
  - [Module reuse across the four platforms](#module-reuse-across-the-four-platforms)
- [9. Platform-specific caveats](#9-platform-specific-caveats)
- [10. Appendix A: identification and inventory commands](#10-appendix-a-identification-and-inventory-commands)
  - [Annotated listing](#annotated-listing)
  - [Paste-ready capture block](#paste-ready-capture-block)
- [References](#references)
  - [References - unresolved](#references---unresolved)

## 1. Summary

**Multicast Service Reflection:** Cisco release notes document Unicast-to-Multicast Destination Reflection for the ISR4431 product family starting in IOS XE 17.9.1a. This confirms family/release-level support for the MSR feature set; no test specific to this PID and the selected later IOS XE basis was located. [Cisco 4000 Series IOS XE 17.9 release notes](https://www.cisco.com/c/en/us/td/docs/routers/access/4400/release/xe-17-9/isr4k-rel-notes-xe-17-9.html) list the Cisco 4431 among the 4000 Series models and list Unicast-to-Multicast Destination Reflection as a 17.9.1a feature. The [IOS XE 17.x multicast guide](https://www.cisco.com/c/en/us/td/docs/routers/ios-xe/ip-multicast/ip-multicast/m_imc_service_reflect-0.html) documents the `ip service reflect` configuration, its prerequisites and limitations, and MSR as introduced in IOS XE 3.4S.

- **Identity:** supplied as "Cisco 4431"; confirmed PID `ISR4431/K9`, base
  router "4GE, 3NIM, 8G FLASH, 4G DRAM", Cisco 4000 Series Integrated Services
  Routers ([ISR4431-EOL-1](#isr4431-eol-1), Table 2). No SKU correction
  needed. Bundles on the same chassis: `ISR4431-AX/K9`, `ISR4431-AXV/K9`,
  `ISR4431-DNA`, `ISR4431-PM20`, `ISR4431-SEC/K9`, `ISR4431-V/K9`,
  `ISR4431-VSEC/K9` — all End-of-Sale under the same notice.
- **Role:** 1RU modular branch router, 4 onboard 1G ports, 3 NIM slots and 1
  ISC (PVDM4 DSP) slot, **no SM-X slot and no 10G port**
  ([ISR4431-DS-1](#isr4431-ds-1), Table 5). Default 500 Mbps aggregate
  throughput, 1 Gbps with the performance license.

Key takeaways:

1. **Not orderable new.** End-of-Sale 2023-11-07; Last Date of Support
   2028-11-30 ([ISR4431-EOL-1](#isr4431-eol-1)). It fails the "new purchase"
   hard requirement and is a reference baseline only.
1. **Software ceiling is documented:** "the last supported software release for
   all other ISR4K series routers is 17.12.x" (all ISR 4000 except ISR 4461)
   ([ISR4431-REL-3](#isr4431-rel-3)). IOS XE 17.12.x reaches End of
   Vulnerability/Security Support 2027-09-30 ([ISR4431-EOL-3](#isr4431-eol-3)),
   with Cisco stating ad-hoc security maintenance releases for ISR 4K until
   November 2028 ([ISR4431-EOL-1](#isr4431-eol-1)).
1. **Cisco's named replacements are themselves now End-of-Sale-announced:**
   EOL14896 maps `ISR4431/K9` → `C8300-1N1S-4T2X` or `C8300-1N1S-6T`; EOL15950
   (announced 2026-07-27) sets End-of-Sale 2027-01-31 for both and maps them to
   `C8375-E-G2` ([ISR4431-EOL-4](#isr4431-eol-4)). This affects the comparison
   (models 2 and 4), not only this baseline.
1. **Offline licensing is documented** for the ISR 4000 under Smart Licensing
   Using Policy (SLP) from IOS XE 17.3.2, including the air-gapped "No
   Connectivity to CSSM and No CSLU" topology and offline SLAC installation for
   HSECK9 ([ISR4431-LIC-1](#isr4431-lic-1)).
1. **Decision-relevant uncertainty:** UTD/Snort IPS on this model needs 8 GB
   (12 GB for the High profile) DRAM against a 4 GB control-plane default, and
   the memory upgrade PIDs are End-of-Sale ([ISR4431-SEC-2](#isr4431-sec-2),
   [ISR4431-EOL-1](#isr4431-eol-1)). Not material to the purchase because the
   model is not orderable. At the17.12.8 baseline, the October2026 Snort3
   fixes also require checking the separate UTD package; the documented
   fixed package is recorded in [Platform-specific caveats](#9-platform-specific-caveats)
   ([ISR4431-PSIRT-2](#isr4431-psirt-2)).

## 2. Lifecycle status

### Chassis, spares, and licenses

EOL14896 ("End-of-Sale and End-of-Life Announcement for the Cisco ISR4200,
ISR4300 and select ISR4400 Series Platform", marked Amended, page updated
2024-11-06) — Table 1 ([ISR4431-EOL-1](#isr4431-eol-1)). Applies to
`ISR4431/K9` and its bundles, and to the ISR 4400 license PIDs listed below.

| Milestone (Cisco name) | Date | Source |
| --- | --- | --- |
| Product release / announcement | Product release **2014-09-30**; announcement date not found | [ISR4431-SUP-1](#isr4431-sup-1), product information |
| End-of-Life Announcement | 2022-11-07 | [ISR4431-EOL-1](#isr4431-eol-1) |
| End-of-Sale (HW, License) | 2023-11-07 | [ISR4431-EOL-1](#isr4431-eol-1) |
| Last Ship (HW, License) | 2024-02-06 | [ISR4431-EOL-1](#isr4431-eol-1) |
| End of SW Maintenance Releases (HW) | 2025-08-31 | [ISR4431-EOL-1](#isr4431-eol-1) |
| End of Vulnerability/Security Support (HW) | 2028-11-30 | [ISR4431-EOL-1](#isr4431-eol-1) |
| End of Routine Failure Analysis (HW) | 2024-11-06 | [ISR4431-EOL-1](#isr4431-eol-1) |
| End of New Service Attachment (HW) | 2024-11-06 | [ISR4431-EOL-1](#isr4431-eol-1) |
| End of Service Contract Renewal (HW) | 2028-02-05 | [ISR4431-EOL-1](#isr4431-eol-1) |
| Last Date of Support (HW) | 2028-11-30 | [ISR4431-EOL-1](#isr4431-eol-1) |
| Cisco recommended replacement | `C8300-1N1S-4T2X` or `C8300-1N1S-6T` (for `ISR4431-PM20`: none) | [ISR4431-EOL-1](#isr4431-eol-1) |

The Cisco 4431 support page shows status "End of Sale", End-of-Sale
07-Nov-2023, End-of-Support 30-Nov-2028 ([ISR4431-SUP-1](#isr4431-sup-1)),
consistent with the table.

ISR 4400 items in the same notice with **no replacement listed** (documented,
[ISR4431-EOL-1](#isr4431-eol-1)): `MEM-4400-4GU8G`, `MEM-4400-4GU16G` (DRAM
upgrades); `PWR-4430-AC(/2)`, `PWR-4430-DC(/2)`, `PWR-4430-POE-AC(/2)`;
`FL-44-PERF-K9` (Performance on Demand), `FL-4430-BOOST-K9` (Booster
Performance, 4430); `SL-44-APP-K9`, `SL-44-SEC-K9`, `SL-44-SECNPE-K9`,
`SL-44-UC-K9` (technology package licenses).

Spares notice EOL15205 (Amended, updated 2024-03-29) — separate milestones
([ISR4431-EOL-2](#isr4431-eol-2)):

| Milestone (Cisco name) | Date |
| --- | --- |
| End-of-Life Announcement | 2023-10-26 |
| End-of-Sale (HW) | 2024-01-26 |
| Last Ship (HW) | 2024-04-25 |
| End of Routine Failure Analysis (HW) | 2025-01-25 |
| End of New Service Attachment (HW) | 2025-01-25 |
| End of Service Contract Renewal (HW) | 2028-04-22 |
| Last Date of Support (HW) | 2029-01-31 |

Spares covered include `PWR-4430-AC=`, `PWR-4430-DC=`, `PWR-4430-POE-AC=`
("500W AC Power Supply for Cisco ISR 4430"), `ACS-4430-FANASSY(=)`,
`MEM-4400-2G=`, `MEM-4400-4G=`, `MEM-4400-8G(=)`, `MEM-4400-DP-2G=`,
`MEM-FLSH-8G=`, `MEM-FLSH-16G=`, `MEM-FLSH-32G=`, `FL-4430-BOOST-K9=`,
`FL-44-HSEC-K9=`, `FL-44-PERF-K9=`, `SL-44-SEC-K9=`, `SL-44-SECNPE-K9=`,
`SL-44-UC-K9=`. Cisco states no replacement is available for these spares.

Module notices: the 4000 Series EoL listing shows notices for CAT 6 NIMs
(2024-08-01), LTE NIMs/3G WAIMs (2019-05-01) and others
([ISR4431-EOL-5](#isr4431-eol-5)); the switch-NIM notices were read in the continuation; other module
notices remain explicit evidence gaps where the model/PID scope or milestones
could not be established from the sources checked.

Switch-module lifecycle follow-up (separate from chassis EOL):
`NIM-ES2-8` and `NIM-ES2-8-P` reached **End-of-Sale 2025-03-05**,
End of SW Maintenance 2026-03-05, End of Vulnerability/Security Support
2028-03-05, and Last Date of Support 2030-03-31
([ISR4431-EOL-6](#isr4431-eol-6), Tables 1/2). `NIM-ES2-4` reached
**End-of-Sale 2025-04-17**, Last Date of Support 2030-04-30
([ISR4431-EOL-7](#isr4431-eol-7), Tables 1/2). These documented chassis
options cannot be treated as orderable-new switch modules at this cutoff.
A bulletin naming a replacement PID does not establish ISR4431 compatibility.

### Software train

| Notice | Milestone (Cisco name) | Date | Source |
| --- | --- | --- | --- |
| EOL15518, IOS XE 17.12.x (OS SW) | End-of-Sale | 2025-03-30 | [ISR4431-EOL-3](#isr4431-eol-3) |
|  | End of SW Maintenance Releases | 2026-03-30 | [ISR4431-EOL-3](#isr4431-eol-3) |
|  | End of Vulnerability/Security Support | 2027-09-30 | [ISR4431-EOL-3](#isr4431-eol-3) |
|  | Last Date of Support | 2028-03-31 | [ISR4431-EOL-3](#isr4431-eol-3) |
| EOL14896 platform text | "ad-hoc EoVSS maintenance releases will be made available for ISR 4K until November 2028" | 2028-11 (month only) | [ISR4431-EOL-1](#isr4431-eol-1) |

EOL15518 does not name affected platforms on the page read; its applicability
to ISR 4000 images is **inferred** (it is listed on the 4000 Series EoL page
[ISR4431-EOL-5](#isr4431-eol-5)).

### Replacement path

| Step | From | To | Status / dates | Source |
| --- | --- | --- | --- | --- |
| 1 | `ISR4431/K9` (and bundles except PM20) | `C8300-1N1S-4T2X` or `C8300-1N1S-6T` | Named replacement in EOL14896 | [ISR4431-EOL-1](#isr4431-eol-1) |
| 2 | `C8300-1N1S-4T2X`, `C8300-1N1S-6T` | `C8375-E-G2` | EOL15950 (Amended): announced 2026-07-27, End-of-Sale 2027-01-31, Last Date of Support 2032-01-31; last train "28.2.x" | [ISR4431-EOL-4](#isr4431-eol-4) |

Support horizon: none supplied, so milestones are reported, not judged.
Keeping an ISR4431 past 2028-11-30 means no TAC support; past 2027-09-30 only
ad-hoc security releases are promised (inferred from the two notices above).

## 3. Hardware specifications

Values are from the Cisco 4000 Family ISR data sheet Table 5 unless noted
([ISR4431-DS-1](#isr4431-ds-1); page shows "Updated" 2026-06-23, last history
entry 2024-08-28). Table 5 text is flattened in the HTML; values below follow
column order (4461, 4451, **4431**, 4351, 4331, 4321, 4221). The power and
weight rows were later checked against the data sheet PDF, rendered as page
images (Table 5, pp. 11-13), which removed the column-alignment doubt and
corrected two values: typical power and weight had been read from a
neighbouring column.

| Item | ISR4431/K9 value | Label / source |
| --- | --- | --- |
| Form factor / rack units | Rack-mount, 1 RU | documented, DS-1 |
| Dimensions (H × W × D) | 1.73 × 17.25 × 19.97 in (43.9 × 438.15 × 507.2 mm) | documented, DS-1 |
| Weight | 18.5 lb (8.4 kg) with AC PSU, no modules; 18.6 lb (8.4 kg) with AC PoE PSU, no modules; 22.4 lb (10.2 kg) typical, fully loaded with modules. DC PSU, no modules: printed as 28.8 lb (13.1 kg), the same figure as the 2RU 4451 and 4351, so likely a Cisco table error | documented, DS-1 PDF Table 5 p. 13 (page image); the DC figure is as printed |
| CPU | "High-performance multicore processors"; core count not disclosed. Separate control-plane and forwarding-plane processors ([ISR4431-HIG-1](#isr4431-hig-1), Figure 1-16). Data-plane cores: 3 PPE + 1 I/O at 500 Mbps; 5 PPE + 1 I/O with performance license ([ISR4431-LIC-3](#isr4431-lic-3)) | documented |
| DRAM — control/services plane | 4 GB default, 16 GB maximum | documented, DS-1 |
| DRAM — data plane | 2 GB default, 2 GB maximum | documented, DS-1 |
| Flash | 8 GB default, 32 GB maximum (eMMC; 8/16/32 GB per HIG) | documented, DS-1, [ISR4431-HIG-1](#isr4431-hig-1) |
| Onboard WAN/LAN 10/100/1000 ports | 4 total; 4 RJ-45-capable and 4 SFP-capable — dual-mode (RJ-45 or SFP per port, "The SFP port shares the same physical port as an RJ-45 GE port with the same number") | count documented, DS-1; dual-mode applicability to 4431 **inferred** (4 total = 4 RJ-45 + 4 SFP; HIG dual-mode text is family-level) |
| Onboard 10G ports | None ("-") | documented, DS-1 |
| Management port | Dedicated Gigabit Ethernet management port "GE0" | documented (family), DS-1 Table 2, HIG-1 |
| Console / aux / USB | 1 RJ-45 serial console, 1 USB mini-B console, 1 RJ-45 auxiliary, 2 USB 2.0 type A | documented, DS-1 |
| Module slots | 3 NIM (OIR supported), 1 onboard ISC (PVDM4), 0 SM-X, 0 double-wide SM | documented, DS-1; ISC for PVDM4 also HIG-1 |
| PIM slot | None found | not found in sources checked |
| Power options | Internal AC, DC, and PoE power supplies; dual hot-swap supplies supported. PIDs: `PWR-4430-AC`, `PWR-4430-DC`, `PWR-4430-POE-AC` (500 W AC) | DS-1; HIG-1 Table 1-4; PIDs from [ISR4431-EOL-1](#isr4431-eol-1)/[ISR4431-EOL-2](#isr4431-eol-2) |
| AC input | 100–240 VAC autoranging, 47–63 Hz; 3–1.3 A max | documented, DS-1 |
| DC input | 48–60 V, 12 A max | documented, DS-1 |
| Typical power, no modules | 65 W | documented, DS-1 PDF Table 5 p. 11 (page image) |
| Maximum power, AC PSU (no PoE) | 250 W | DS-1 (as extracted) |
| Maximum power, DC PSU (no PoE) | 437 W | documented, DS-1 PDF Table 5 p. 11 |
| Maximum power, PoE PSU (platform) | 500 W with PoE redundant; 1,000 W with PoE boost, no redundancy | DS-1; alignment inferred (row has 11 values for 7 columns) |
| Endpoint PoE budget (PoE PSU) | 250 W with optional redundancy; 500 W with PoE boost, no redundancy | DS-1 |
| Front-panel PoE | **Not supported**: "Cisco 4431 ISR, Cisco 4321 ISR and Cisco 4221 do not support front panel PoE+" | documented, HIG-1 |
| Heat dissipation | not found in sources checked | — |
| Airflow | I/O side to bezel side | documented, DS-1 |
| MTBF | 512,970 hours | documented, DS-1 PDF Table 5 p. 13 |
| Operating temperature | 0–40 °C (32–104 °F) | documented, DS-1 |
| Secure boot / anti-counterfeit | Hardware-based secure boot of bootloader; on-board tamper-proof silicon for hardware authentication | documented (family), DS-1 |
| TPM / Trust Anchor module | not mentioned in DS-1 | not found in sources checked |
| Crypto acceleration | "Embedded IP Security (IPsec) VPN hardware acceleration" (family architecture, Table 2) | documented (family), DS-1 |

**Source conflict (PoE):** HIG-1 Table 1-4 (2014) shows no "PoE Power Supply
Converter" for the 4431, while DS-1 (revised 2024) lists PoE PSU wattage and
endpoint PoE for the 4431, and EOL15205 lists `PWR-4430-POE-AC=` as a 500 W
AC PSU for ISR 4430. Resolution: DS-1 is chassis-specific and newer, so PoE
from a PoE PSU to module ports is taken as **documented**; front-panel PoE is
documented as unsupported. The NIM-ES2-8-P is now documented for the 4431
([ISR4431-MOD-2](#isr4431-mod-2), Tables 6 and 9); see section 8.

## 4. Performance

All figures are Cisco "up to"/aggregate values from DS-1 Table 5 unless
noted. Mode: autonomous (inferred; DS-1 does not state mode). Release:
not disclosed. Packet size / traffic mix: **not disclosed** unless noted.

| Metric | Value | Conditions disclosed | Tier / license | Source |
| --- | --- | --- | --- | --- |
| Aggregate throughput (default) | 500 Mbps | Aggregate; mix not disclosed | No performance license | [ISR4431-DS-1](#isr4431-ds-1) Table 5 |
| Aggregate throughput (performance) | 1 Gbps | Aggregate; mix not disclosed | `FL-44-PERF-K9` (DS-1 Table 7) | [ISR4431-DS-1](#isr4431-ds-1) |
| Aggregate CEF-only throughput (boost) | "Over 4 Gbps" | CEF only; "Using onboard Gigabit Ethernet Interfaces" | Boost license | [ISR4431-DS-1](#isr4431-ds-1) |
| Boost (per license description) | "up to 3.4 Gbps CEF" | `FL-4430-BOOST-K9` description | Boost | [ISR4431-DS-1](#isr4431-ds-1) Table 8 |
| Encrypted throughput without HSEC | 250 Mbps (cap) | Licensed limit, since IOS XE 16.8.1; 1,000 secure tunnels | No HSECK9 | [ISR4431-DS-1](#isr4431-ds-1) |
| IPsec throughput (with HSEC) | not found in sources checked | — | — | — |
| Services-enabled / SD-WAN throughput | not found in sources checked | — | — | — |
| Port line rate | 4 × 1 Gbps onboard | Line rate, not a forwarding figure | — | [ISR4431-DS-1](#isr4431-ds-1) |

**Source conflict (boost):** DS-1 Table 5 gives "Over 4 Gbps" CEF-only for the
4431; DS-1 Table 8 describes `FL-4430-BOOST-K9` as "up to 3.4 Gbps CEF". Both
are in the same document, measured under undisclosed conditions; left
unresolved. Doc 217135 adds that boost "disables the aggregate shaper", so
maximum throughput then depends on the features in use
([ISR4431-LIC-3](#isr4431-lic-3)).

Scale figures found: TrustSec "4400 Series ISR" — 1,800 unidirectional / 900
bidirectional SXP connections, 750,000 IP-SGT bindings (IOS XE 3.15 and 3.16)
([ISR4431-SEC-4](#isr4431-sec-4), Table 8). CUBE: 3,000 basic-audio sessions,
750 SRTP-RTP, 750 media-proxy ([ISR4431-DS-4](#isr4431-ds-4), Table 3).
Route, NAT-session, and IPsec-tunnel scale with HSEC: not found in sources
checked.

## 5. Software

| Designation | Release | Release date | Mode | Source / note |
| --- | --- | --- | --- | --- |
| Cisco-recommended | 17.9.10 **or** 17.12.8 ("Depending on feature requirements") | not found in sources checked | not stated (autonomous assumed) | [ISR4431-REL-1](#isr4431-rel-1), doc 215567 rev 9.0, published 2026-06-15; Cisco recommendation document (not labeled "advisory"), row "ISR4200/4300/4431/4451" names the exact platform |
| Newest available (documented) | 17.12.8 | not found in sources checked | both | Newest rebuild in 17.12.x release notes (last updated 2026-08-05) [ISR4431-REL-2](#isr4431-rel-2); download page not checked |
| Documented ceiling | 17.12.x train | — | both | "Starting with Cisco IOS XE 17.15.x, only the ISR 4461 platform is supported; the last supported software release for all other ISR4K series routers is 17.12.x" [ISR4431-REL-3](#isr4431-rel-3); EOL14896: last trains 17.9.x and 17.12.x, 17.10.x/17.11.x not supported [ISR4431-EOL-1](#isr4431-eol-1) |
| Controller-mode pairing | Basis 17.12.8; recommended same-train candidate Manager20.12.8.1. Other lifecycle-permitted Manager trains20.15/20.18 need exact compatibility checks | Recommendation updated 2026-08-19; image release dates unresolved | controller | [ISR4431-SDWAN-1](#isr4431-sdwan-1), [ISR4431-SDWAN-2](#isr4431-sdwan-2); lifecycle bounds [ISR4431-EOL-1](#isr4431-eol-1) |

**Chosen basis:** IOS XE **17.12.8**, autonomous mode — it is within Cisco's
recommendation for the exact platform and on the documented last train.
17.9.10 is the alternative recommendation; the lifecycle analysis here is for
the chosen 17.12.x basis. No 17.9.x milestone is inferred from an unread notice.

Other software facts:

- **Install vs. bundle mode:** install commands introduced in IOS XE 16.6.2;
  bundle-to-install conversion uses the one-step install procedure; Cisco
  ships all IOS XE platforms in install mode by default only from 17.15.1a,
  which the ISR4431 cannot run ([ISR4431-CFG-4](#isr4431-cfg-4)). Bundle mode
  is not stated as deprecated for 17.12.

- **Autonomous/controller:** universalk9 image boots in either mode from
  17.2.1 ([ISR4431-DS-1](#isr4431-ds-1)); `show version` reports "Router
  operating mode: Autonomous" in a Cisco example
  ([ISR4431-CFG-4](#isr4431-cfg-4)). Mode conversion must follow the selected
  controller deployment procedure; no conversion was performed here.

- **Minimum releases for notable features:** Smart Licensing 16.6.1; SLP
  17.3.2 ([ISR4431-LIC-1](#isr4431-lic-1)); exact ISR4431 SD-WAN minimum
  **16.10.1**, last train **17.12.x** ([ISR4431-SDWAN-2](#isr4431-sdwan-2)); dual persona
  17.2.1; HSEC 250 Mbps cap 16.8.1 ([ISR4431-DS-1](#isr4431-ds-1)); on-device
  SLAC request 17.7.1a; DNA_HSEC tagging 17.6.1a
  ([ISR4431-LIC-1](#isr4431-lic-1)).

- **ROMMON/CPLD at 17.12:** release notes list existing ROMMON 16.12(2r) and
  CPLD 19042950 for the 4431 (not labeled minimum)
  ([ISR4431-REL-2](#isr4431-rel-2), Table 1).

- **Legacy PAK prerequisite (conditional):** if an older PAK deployment has
  no license snapshot, first move to the latest 17.6.x or 17.9.x release so
  the snapshot and Device-Led Conversion can complete, then move to the
  17.12.8 target. Cisco removed the PAK-managing library from 17.11.1a; this
  intermediate upgrade requirement applies when targeting 17.12.1a or later
  without the snapshot, not to every upgrade ([ISR4431-REL-1](#isr4431-rel-1),
  Additional Considerations, re-read 2026-10-31 UTC).

- **Controller recommendation:** the public recommendation now lists
  17.12.8/17.15.6 edge releases and 20.12.8.1/20.15.6 controllers. Select
  17.12.8 for ISR4431 because its documented ceiling excludes 17.15.6;
  20.12.8.1 is the same-train candidate, not evidence that every rebuild
  combination is compatible ([ISR4431-SDWAN-1](#isr4431-sdwan-1),
  [ISR4431-SDWAN-2](#isr4431-sdwan-2)).

## 6. Licensing

At 17.12 the ISR 4000 has three stacked licensing layers: (a) technology
packages / RTU licenses (`ipbasek9`, `appxk9`, `securityk9`, `uck9`) still
present under SLP as "NOT ENFORCED" licenses; (b) Cisco DNA subscriptions
(Essentials / Advantage), which carry a perpetual Network Essentials / Network
Advantage element; (c) throughput (Performance, Boost) and export-controlled
HSECK9. Because the chassis is End-of-Sale (licenses included, per EOL14896),
nothing in this section is "orderable new" for an ISR4431 purchase; it is
recorded for baseline comparison.

### Feature entitlement

| Capability | Tier / license | Dependencies | Mode / release | Source |
| --- | --- | --- | --- | --- |
| Base routing | `ipbasek9` — default, "always available" (stated in a PAK-migration example) | none | autonomous, 17.3.2+ | [ISR4431-LIC-1](#isr4431-lic-1) PDF p. 123 — applicability to 4431 **inferred** |
| Application features (AppX) | `appxk9` / `ISR_4400_Application` ("AppX License for Cisco ISR 4400 Series") | — | autonomous | [ISR4431-LIC-1](#isr4431-lic-1) PDF p. 65 |
| Security (IPsec, firewall) | `securityk9` / `ISR_4400_Security`; TrustSec SG firewall enforcement needs "Security/K9" | HSECK9 above 250 Mbps encrypted | autonomous | [ISR4431-LIC-1](#isr4431-lic-1) p. 65; [ISR4431-SEC-4](#isr4431-sec-4) |
| Unified communications (voice) | `uck9` / `ISR_4400_UnifiedCommunication` | DSPs for transcoding | autonomous | [ISR4431-LIC-1](#isr4431-lic-1) p. 65 |
| CUBE | DNA Essentials: "basic CUBE (without DSP services)"; DNA Advantage: rich voice, SRST/FXO/FXS/DSP | DSP resources for transcoding | both; SIP only in SD-WAN mode | [ISR4431-LIC-2](#isr4431-lic-2) App. D; [ISR4431-DS-4](#isr4431-ds-4) |
| DNA tiers (routing) | Cisco DNA Essentials (incl. Network Essentials perpetual) / Cisco DNA Advantage (incl. Network Advantage perpetual); 3-, 5-, 7-year terms | — | both | [ISR4431-LIC-2](#isr4431-lic-2); DS-1 |
| Security features (FW, IPS, URL filtering, Secure Endpoint, DNS security) | Listed as supported on "ISR 4000 (… 4431 …)" in the DNA guide Table 10; tier per feature not extracted | 8 GB memory and 8 GB boot flash minimum | — | [ISR4431-LIC-2](#isr4431-lic-2) Table 10 |
| Snort IPS (UTD) | "Cisco IOS XE image with security license" | 8 GB RAM / 8 GB flash (12/12 High profile on 4431); not with boost | autonomous | [ISR4431-SEC-2](#isr4431-sec-2) |
| Feature-to-DNA-tier mapping (IPsec, NAT, QoS, etc.) | **unresolved** — not itemized in the DNA ordering guide read | — | — | gap |

### Throughput and crypto

| License | Limit unlocked | Crypto restriction | Prerequisites | Source |
| --- | --- | --- | --- | --- |
| None (default) | 500 Mbps aggregate | 250 Mbps encrypted, 1,000 tunnels without HSEC | — | [ISR4431-DS-1](#isr4431-ds-1) |
| `FL-44-PERF-K9` (Performance on Demand, 4400) | 1 Gbps aggregate | unchanged | Reload required | DS-1 Table 7; [ISR4431-LIC-3](#isr4431-lic-3) |
| `FL-4430-BOOST-K9` (Booster, 4430) | Unthrottled CEF ("up to 3.4 Gbps CEF" / "Over 4 Gbps") | unchanged | RTU from 17.3.2; `platform hardware throughput level boost`; reload; blocks UTD virtual-service | DS-1; [ISR4431-LIC-3](#isr4431-lic-3); [ISR4431-SEC-2](#isr4431-sec-2) |
| DNA bandwidth tiers (T0–T3) | Performance/Boost fulfilled automatically from the bandwidth tier; "no relevance" in SD-WAN mode | T1 requires one-way encrypted < 250 Mbps | — | [ISR4431-LIC-2](#isr4431-lic-2) App. D, Table 6/9 (Table 9 lists ISR4430 row; checkmarks not extractable) |
| HSECK9 (export-controlled) | Removes the 250 Mbps / 1,000-tunnel curtailment | Export-controlled; requires SLAC under SLP | `license feature hseck9`; SLAC | DS-1; [ISR4431-LIC-1](#isr4431-lic-1) |

HSECK9 PIDs and entitlements ([ISR4431-LIC-1](#isr4431-lic-1), PDF p.
355–357; spares in [ISR4431-EOL-2](#isr4431-eol-2)):

| Release era | PID | CSSM entitlement |
| --- | --- | --- |
| 17.5.x and earlier | `FL-44-HSEC-K9`, `FL-44-HSEC-K9=` | `ISR_4400_Hsec` (device-specific) |
| 17.6.1 and later | `ISR4K-HSECK9`, `ISR4K-HSECK9=`; `DNA-HSEC-L` (EA); `DNA-HSEC-UPGD(=)` (existing device-specific holders) | "DNA-HSEC Router US Export Lic for DNA" |

Export authorization (HSECK9 entitlement), crypto capability (hardware IPsec
acceleration), and performance licensing (PERF/BOOST) are separate items.
The **1 Gbps Performance tier is not an absolute chassis or crypto maximum**:
Boost removes the aggregate forwarding shaper. Neither the unthrottled CEF
marketing figure nor HSEC authorization establishes a measured encrypted
throughput ceiling. The actual IPsec ceiling remains **unknown**, so do not
score it as 1 Gbps or mark every encrypted rate above that unavailable
([ISR4431-DS-1](#isr4431-ds-1), [ISR4431-LIC-3](#isr4431-lic-3)).

### Purchase and enforcement

| License | Perpetual / subscription | Terms | Orderable today | Reporting method | Disconnected reporting | On expiry / noncompliance | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Technology packages (`appxk9`, `securityk9`, `uck9`) | Perpetual (RTU or PAK) | — | **No** (`SL-44-*` End-of-Sale 2023-11-07) | SLP: direct, CSLU, SSM On-Prem, offline file | Unenforced perpetual: ACK required; first report 365 days (distributor/partner purchase), report-on-change 90 days | Not enforced; syslog when ACK deadline missed | EOL-1; [ISR4431-LIC-1](#isr4431-lic-1) |
| Cisco DNA Essentials / Advantage | Subscription (DNA) + perpetual Network stack (autonomous) | 3, 5, 7 years | Not for this chassis (chassis End-of-Sale; `ISR4431-DNA` bundle End-of-Sale) | same | Unenforced subscription: first report 90 days, every 90 days | Controller-mode license "does require renewal upon expiry"; enforcement on missed report not documented → **unresolved** | DS-1; [ISR4431-LIC-2](#isr4431-lic-2); [ISR4431-LIC-1](#isr4431-lic-1) |
| `FL-44-PERF-K9`, `FL-4430-BOOST-K9` | Perpetual | — | **No** (End-of-Sale) | same | as unenforced perpetual | not documented → unresolved | EOL-1 |
| HSECK9 (`ISR4K-HSECK9`, `DNA-HSEC-*`) | Perpetual (export-controlled) | — | Not verified for ISR4K at cutoff | SLAC (online or file-based) | Export-controlled: ACK required, first report 0 days | Without SLAC, encrypted throughput stays capped at 250 Mbps (inferred from DS-1 + LIC-1) | [ISR4431-LIC-1](#isr4431-lic-1) |

Policy values are Cisco's default policy table
([ISR4431-LIC-1](#isr4431-lic-1), "Information About Smart Licensing Using
Policy"). The guide states that if an ACK "is required and is not received by
this deadline, a syslog is displayed" (PDF p. 306) and documents
`%SMART_LIC-6-REPORTING_REQUIRED` (PDF p. 340). No feature-disabling
consequence was found; treat functional impact as **unresolved**, not as "no
impact".

### Offline operation (no internet)

Eligibility: **documented** — the ISR 4000 is in the SLP supported-product
table from IOS XE 17.3.2 ("All models … are supported – unless indicated
otherwise"), and the air-gapped topology applies
([ISR4431-LIC-1](#isr4431-lic-1)).

Options:

1. **No Connectivity to CSSM and No CSLU** (air-gapped, file-based).
1. **CSLU Disconnected from CSSM** — CSLU on-site, signed files moved
   manually.
1. **SSM On-Prem** — usage synced to CSSM ad hoc, on schedule, or via "signed
   files that are saved offline and then upload[ed]"; the local account itself
   must be registered/synchronized with CSSM before usage sync (PDF p. 28).
   SSM On-Prem therefore still needs periodic file exchange with CSSM; no
   offline frequency is stated.

Administrator steps for option 1 (Cisco doc 217046 and SLP guide workflow;
[ISR4431-LIC-4](#isr4431-lic-4), [ISR4431-LIC-1](#isr4431-lic-1)):

```text
! one-time, global configuration: no transport to Cisco
license smart transport off
! each reporting cycle, privileged EXEC: export usage (RUM) to a file
license smart save usage all file bootflash:all_rum.txt
! copy the file off-box, then on an internet-connected workstation:
!   CSSM > Smart Software Licensing > Reports > Usage Data Files > Upload Usage Data
!   download the ACK file from the Acknowledgement column
! back on the router, privileged EXEC: install the ACK
license smart import bootflash:<ack-file>.txt
```

HSECK9 offline (SLAC): either generate the SLAC in the CSSM Web UI (Inventory

> Product Instances > Authorize License-Enforced Features, using PID and serial
> number) and install the downloaded file with `license smart import`, or (from
> 17.7.1a) create a request on the router with
> `license smart authorization request replace hseck9 local` and
> `license smart authorization request save bootflash:slac.txt`, upload it via
> Usage Data Files, and import the returned code. Cisco says to use `replace`,
> not `add`. On ISR 4000 the feature is enabled with `license feature hseck9`
> ([ISR4431-LIC-1](#isr4431-lic-1), PDF p. 204). When selecting the SLAC license
> name in CSSM, Cisco says to use `ISR_4400_Hsec` "if using the offline mode"
> (mapping table, [ISR4431-LIC-1](#isr4431-lic-1)).

Cadence: driven by the policy installed with the first ACK (defaults above).
With Cisco default policy, subscription licenses need a report every 90 days;
export-controlled licenses need the SLAC before use. Cisco recommends a
reporting interval of 7 days or less only for post-paid (MSLA) use.

## 7. Feature support and integration

### Feature matrix

Basis: IOS XE 17.12.8, autonomous unless noted. "Family" means the source
covers the Cisco 4000 Series ISR, not the 4431 by name.

| Feature | Supported | Mode | License / tier | Module / HW required | Min release | Key limits | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SD-WAN | yes | controller | DNA subscription (term-based in controller mode); PERF/BOOST "no relevance" | — | 16.10.1 exact-PID SD-WAN; 17.2.1 dual persona | Last train 17.12.x; Manager 20.12/20.15/20.18 | [ISR4431-SDWAN-2](#isr4431-sdwan-2); [ISR4431-EOL-1](#isr4431-eol-1); [ISR4431-LIC-2](#isr4431-lic-2) |
| IPsec VPN (IKEv2, FlexVPN, DMVPN, GETVPN) | yes (family) | both | `securityk9` (inferred); HSECK9 above 250 Mbps encrypted | onboard crypto acceleration (family) | not stated | 250 Mbps / 1,000 tunnels without HSEC | [ISR4431-SEC-1](#isr4431-sec-1); DS-1 |
| NAT | yes (family) | autonomous | not verified | — | not stated | not found | [ISR4431-CFG-7](#isr4431-cfg-7) |
| QoS (MQC, shaping) | yes (family) | autonomous | not verified | — | not stated | Aggregate throughput license shaper applies (doc 217135) | [ISR4431-CFG-8](#isr4431-cfg-8); [ISR4431-LIC-3](#isr4431-lic-3) |
| Voice / CUBE | yes | both (SIP only in SD-WAN mode) | `uck9` (legacy) or DNA Essentials (basic) / Advantage (rich voice) | DSP (PVDM4 in ISC) for transcoding; voice NIMs for TDM | not stated | 3,000 basic sessions; 4431 listed under CUBE "End of Life platforms" | [ISR4431-DS-4](#isr4431-ds-4); [ISR4431-LIC-2](#isr4431-lic-2) |
| NGFW / UTD (ZBFW, Snort IPS, URL filtering) | yes | autonomous (UTD) | security license; ZBFW family-documented | DRAM ≥ 8 GB (12 GB High profile) → control-plane upgrade from 4 GB default; flash ≥ 8 GB | 17.1.1 doc set | Not with boost license; OVA container only to 16.10 (IOx later) | [ISR4431-SEC-2](#isr4431-sec-2); [ISR4431-SEC-1](#isr4431-sec-1); [ISR4431-LIC-2](#isr4431-lic-2) Table 10 |
| PoE | yes (module ports only) | autonomous documented; controller feature configuration not verified | IP Base for NIM-ES2 switching | NIM-ES2-8-P + PWR-4430-POE-AC; no front-panel PoE | 3.15 (switch NIM minimum) | 250 W endpoint (redundant) / 500 W (boost) | [ISR4431-MOD-2](#isr4431-mod-2), Tables 6/9/11; DS-1 |
| Routing scale | not verified | — | — | — | — | not found in sources checked | gap |
| Segmentation — VRF-Lite | documented on ISR4431 at16.12.2t; applicability at17.12.8 **inferred** | autonomous | exact tier not verified | Built-in routed subinterfaces in CVD example | Exact minimum not established; demonstrated16.12.2t | No scale inferred from example VRF count | [ISR4431-CFG-9](#isr4431-cfg-9), fusion-device procedures and Appendix 1; [ISR4431-MX-1](#isr4431-mx-1), family entitlement context |
| Segmentation — SGT | yes | autonomous | IP Base/K9 to classify/propagate/SGACL; Security/K9 for SG firewall | — | validated on 16.3.2 / 16.4.1 | see ISE table | [ISR4431-SEC-4](#isr4431-sec-4) Table 1 |
| Multicast Service Reflection | Yes (product-family release-note support) | Autonomous CLI configuration documented; controller mode not established | not established | Vif interface and PIM infrastructure | Unicast-to-multicast support introduced 17.9.1a; selected release later | IOS XE 17.x documents `ip service reflect`; family-level support; exact-PID test not found | [ISR4431-MSR-REL-1](#isr4431-msr-rel-1); [ISR4431-MSR-1](#isr4431-msr-1) |

Deprecations in the selected release: none documented in the 17.12 release
notes ([ISR4431-REL-2](#isr4431-rel-2)).

### Cisco ISE integration

| Integration | Supported | Mode | License (router) | Module / HW | Min release | Limits / notes | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RADIUS device administration | yes (family) | autonomous | not stated | — | not stated | Configured on router (AAA/RADIUS); policy on ISE | [ISR4431-SEC-1](#isr4431-sec-1) ("RADIUS" chapter) |
| TACACS+ device administration | yes (family) | autonomous | not stated | — | not stated | Router: `aaa` + TACACS+ server; ISE: Device Admin policy (ISE license tier not documented in sources checked) | [ISR4431-SEC-1](#isr4431-sec-1) ("TACACS") |
| SGT inline tagging | yes | autonomous | IP Base/K9 | — | 16.3.2 / 16.4.1 (validated) | "SGT over Ethernet, SGT over GETVPN, DMVPN, or IPsec VPN" | [ISR4431-SEC-4](#isr4431-sec-4) |
| SXP | yes | autonomous | IP Base/K9 | — | V4; V5 from 17.9.1 | Speaker and listener; 1,800 uni / 900 bi connections; 750,000 bindings (4400 Series) | [ISR4431-SEC-4](#isr4431-sec-4) Tables 1, 8 |
| SGACL enforcement | yes | autonomous | IP Base/K9; SG firewall needs Security/K9 | — | as above | Monitor mode and logging; SGT-based PBR, QoS, caching | [ISR4431-SEC-4](#isr4431-sec-4); [ISR4431-SEC-3](#isr4431-sec-3) |
| 802.1X / MAB on switch NIM ports | yes (documented module capability) | autonomous; controller configuration not verified | IP Base; ISE feature tier not established by this module source | NIM-ES2-4, NIM-ES2-8, NIM-ES2-8-P | 3.15 module minimum; exact 17.12.8 configuration validation unresolved | Switch ports perform authentication; configure router AAA/port policies and ISE authorization. MAB and dynamic VLANs documented | [ISR4431-MOD-2](#isr4431-mod-2), feature table and exact ISR4431 platform Table 6 |
| Other (e.g., IP-to-SGT classification) | yes | autonomous | IP Base/K9 | — | — | IP-to-SGT, subnet-to-SGT, L3IF-to-SGT classification | [ISR4431-SEC-4](#isr4431-sec-4) |

On the router: AAA server groups, CTS/SXP peers, SGT mappings and SGACL
download. On ISE: network device definitions, device-admin policy sets, SGT
and SGACL matrix, SXP domains. ISE license tiers: not documented in the
sources checked.

## 8. Modules and expansion

### Slot map

| Slot | Count | Notes | Source |
| --- | --- | --- | --- |
| Onboard GE (0/0) | 4 | Dual-mode RJ-45 / SFP (1G); front-panel PoE not supported | DS-1; HIG-1 |
| NIM (0/1–0/3) | 3 | OIR supported; slot numbering 0/1–0/3 **inferred** (HIG: NIM bays start at bay 1). Cellular NIMs: available, not assessed | DS-1; HIG-1 |
| ISC | 1 | PVDM4 voice DSP | DS-1; HIG-1 |
| SM-X | 0 | none | DS-1 |
| PIM | 0 | none found | not found |
| Power supplies | 2 | Internal, hot-swap, AC / DC / PoE | DS-1; HIG-1 |
| Fan | 1 assembly | `ACS-4430-FANASSY` | [ISR4431-EOL-2](#isr4431-eol-2) |

**Source conflict (SM-X):** the GE WAN module data sheet lists the 4431 among
"Platforms with SM-X slot" ([ISR4431-DS-2](#isr4431-ds-2), 2019), while the
chassis data sheet gives 0 SM-X slots for the 4431 ([ISR4431-DS-1](#isr4431-ds-1),
revised 2024). The chassis-specific source wins; the TMG matrix also lists no
10G optics for the 4431 while listing them for SM-X-capable 4351/4451-X
([ISR4431-OPT-1](#isr4431-opt-1)), consistent with no SM-X slot (inferred).

### Module families

Coverage: the continuation read Cisco's current interfaces/modules matrix
and the module sources below. **Documented** chassis compatibility does not
by itself prove exact **17.12.8/mode support or current orderability**. Those
three findings remain separate in the last column. The 17.12 release notes
were checked for relevant module restrictions, but do not provide a complete
per-PID certification table; exact-basis rows therefore remain unverified.
Current orderability/lifecycle was sought in the public module and series
notices, without establishing every module's commercial status. This is a
non-exhaustive list, not permission to order a legacy module without checking
its PID/release ([ISR4431-REL-2](#isr4431-rel-2),
[ISR4431-MOD-9](#isr4431-mod-9), [ISR4431-EOL-5](#isr4431-eol-5)).

| PID | Description | Capability | Slot | Min release / mode | Dependency | Placement | Lifecycle | On chassis / at 17.12 / orderable | Source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `NIM-1GE-CU-SFP` | 1-port dual-mode GE/SFP WAN NIM | Extra routed 1G port | NIM | IOS XE 3.16 for auto-failover features | — | "as many … as the platform slot density allows" | not checked | yes (All 4000 ISRs) / not verified / not checked | [ISR4431-DS-2](#isr4431-ds-2) |
| `NIM-2GE-CU-SFP` | 2-port dual-mode GE/SFP WAN NIM | 2 routed 1G ports; WAN MACsec (256-bit) | NIM | 3.16 (MACsec) | MACsec needs Security + HSEC licenses (DS-1) | as above | not checked | yes / not verified / not checked | [ISR4431-DS-2](#isr4431-ds-2); DS-1 |
| `NIM-1MFT-T1/E1`, `NIM-2MFT-T1/E1`, `NIM-4MFT-T1/E1`, `NIM-8MFT-T1/E1` (and PRI variants by port count) | T1/E1 multiflex voice/WAN NIMs | TDM voice / WAN | NIM | IOS XE 3.13.1 | IP Base (data); UC package (voice); DSPs | 1-, 2-, 4-, 8-port all "Yes" for 4431 | not checked | yes / not verified / not checked | [ISR4431-MOD-1](#isr4431-mod-1) (2015 FAQ) |
| `MEM-4400-4GU8G`, `MEM-4400-4GU16G` | Control-plane DRAM upgrades | 8 GB / 16 GB control plane | DIMM | — | needed for UTD | — | End-of-Sale 2023-11-07 | yes / — / no | [ISR4431-EOL-1](#isr4431-eol-1) |
| `MEM-FLSH-16G=`, `MEM-FLSH-32G=` | Flash upgrades | Storage | internal | — | — | — | End-of-Sale 2024-01-26 (spares) | yes (4430) / — / no | [ISR4431-EOL-2](#isr4431-eol-2) |
| `PWR-4430-AC`, `PWR-4430-DC`, `PWR-4430-POE-AC` | Power supplies | AC / DC / 500 W AC with PoE | PSU bay | — | — | dual | End-of-Sale | yes / — / no | [ISR4431-EOL-1](#isr4431-eol-1); [ISR4431-EOL-2](#isr4431-eol-2) |
| `ACS-4430-FANASSY` | Fan assembly | Cooling | fan bay | — | — | — | End-of-Sale 2024-01-26 (spares) | yes / — / no | [ISR4431-EOL-2](#isr4431-eol-2) |
| `NIM-ES2-4` | 4-port GE switch | L2 copper switching, 802.1X/MAB | NIM | 3.15; autonomous baseline | IP Base | Up to 3 | End-of-Sale 2025-04-17 | documented / not explicitly recertified / **no** | [ISR4431-MOD-2](#isr4431-mod-2), Tables 6/11; [ISR4431-EOL-7](#isr4431-eol-7) |
| `NIM-ES2-8` | 8-port GE switch | L2 copper switching, 802.1X/MAB | NIM | 3.15; autonomous baseline | IP Base | Up to 3 | End-of-Sale 2025-03-05 | documented / not explicitly recertified / **no** | [ISR4431-MOD-2](#isr4431-mod-2), Tables 6/11; [ISR4431-EOL-6](#isr4431-eol-6) |
| `NIM-ES2-8-P` | 8-port PoE/PoE+ switch | Switching and endpoint power | NIM | 3.15; autonomous baseline | IP Base + PoE PSU | Up to 3; shared chassis power budget | End-of-Sale 2025-03-05 | documented / not explicitly recertified / **no** | [ISR4431-MOD-2](#isr4431-mod-2), Tables 6/9/11; [ISR4431-EOL-6](#isr4431-eol-6) |
| `PVDM4-32` | 32-channel voice DSP | IP voice services or T1/E1 packetization | Motherboard/ISC or T1/E1 NIM | Minimum not established here | UC entitlement; T1/E1 DSP must be on that NIM | One motherboard slot; extra PVDM4s on T1/E1 NIMs | Unknown | documented / exact basis unverified / unknown | [ISR4431-MOD-3](#isr4431-mod-3), Table 1 and form-factor text |
| `PVDM4-64` | 64-channel voice DSP | As PVDM4-32 | Motherboard/ISC or T1/E1 NIM | As above | As above | As above | Unknown | documented / exact basis unverified / unknown | [ISR4431-MOD-3](#isr4431-mod-3) |
| `PVDM4-128` | 128-channel voice DSP | As PVDM4-32 | Motherboard/ISC or T1/E1 NIM | As above | As above | As above | Unknown | documented / exact basis unverified / unknown | [ISR4431-MOD-3](#isr4431-mod-3) |
| `PVDM4-256` | 256-channel voice DSP | As PVDM4-32 | Motherboard/ISC or T1/E1 NIM | As above | As above | As above | Unknown | documented / exact basis unverified / unknown | [ISR4431-MOD-3](#isr4431-mod-3) |
| `NIM-2FXO`, `NIM-4FXO` | 2/4 analog FXO ports | PSTN/PBX voice | NIM | Exact ISR4431 interoperability table: 3.16; autonomous | UC package; onboard DSP | NIM slot | Unknown | documented / exact basis unverified / unknown | [ISR4431-MOD-4](#isr4431-mod-4); [ISR4431-MOD-5](#isr4431-mod-5), Table 3 |
| `NIM-2FXS`, `NIM-4FXS`, `NIM-2FXS/4FXO` | 2/4 FXS or combo voice | Analog phone/fax and mixed voice | NIM | Exact ISR4431 table: 3.16; autonomous | UC package; onboard DSP | NIM slot | Unknown | documented / exact basis unverified / unknown | [ISR4431-MOD-4](#isr4431-mod-4); [ISR4431-MOD-5](#isr4431-mod-5), Table 3 |
| `NIM-2FXSP`, `NIM-4FXSP`, `NIM-2FXS/4FXOP` | Revised analog voice PIDs | Functionally equivalent P variants | NIM | 16.5+; autonomous | UC package; onboard DSP | NIM slot | Unknown | documented for4400 family / exact basis unverified / unknown | [ISR4431-MOD-4](#isr4431-mod-4), Tables 1/2 |
| `NIM-4E/M` | 4 E/M voice ports | Analog E/M voice | NIM | Module source: 3.14.3+; autonomous | UC package; onboard DSP | NIM slot | Unknown | documented for4400 family / exact basis unverified / unknown | [ISR4431-MOD-4](#isr4431-mod-4) |
| `NIM-2BRI-NT/TE`, `NIM-4BRI-NT/TE` | 2/4 BRI voice ports | BRI voice, distinct from S/T data NIMs | NIM | Exact ISR4431 table: 3.14; autonomous | UC package; onboard DSP | NIM slot | Unknown | documented / exact basis unverified / unknown | [ISR4431-MOD-5](#isr4431-mod-5), Table 3 |
| `NIM-1CE1T1-PRI`, `NIM-2CE1T1-PRI`, `NIM-8CE1T1-PRI` | Channelized T1/E1/PRI | Voice or channelized data | NIM | Exact ISR4431 table: 3.13; autonomous | Voice DSP and UC entitlement where used for voice | NIM slot | Unknown | documented / exact basis unverified / unknown | [ISR4431-MOD-5](#isr4431-mod-5), Table 3 |
| `NIM-VAB-A`, `NIM-VA-B`, `NIM-VAB-M` | Annex A, B/J, M DSL | VDSL2/ADSL2+ WAN | Onboard NIM only | 3.14+; autonomous | IP Base; DSLAM/profile fit | Up to 3 on ISR4431 | Unknown | documented / exact basis unverified / unknown | [ISR4431-MOD-6](#isr4431-mod-6), Tables 6/7 |
| `NIM-2BRI-S/T`, `NIM-4BRI-S/T` | 2/4 BRI S/T data ports | ISDN data/backup | NIM | 16.6.1; autonomous | IP Base | Up to 3 on ISR4431 | Unknown | documented / exact basis unverified / unknown | [ISR4431-MOD-7](#isr4431-mod-7), Tables 4–7 |
| `NIM-16A`, `NIM-24A` | 16/24 async serial ports | Terminal-server console access; no SLIP/PPP routing | NIM | Data sheet16.3.1; current matrix16.4.1; autonomous | IP Base; appropriate octal cable | Up to 3 on ISR4431 | Unknown | documented / exact basis unverified / unknown | [ISR4431-MOD-8](#isr4431-mod-8), Tables 2–4; [ISR4431-MOD-9](#isr4431-mod-9) |
| `NIM-1T`, `NIM-2T`, `NIM-4T` | 1/2/4 synchronous serial ports | Legacy synchronous WAN | NIM | Current matrix3.13; original family DS3.12; exact basis unresolved | IP Base | Subject to3 NIM slots | Unknown | inferred from current matrix; older DS names4451 only / unverified / unknown | [ISR4431-MOD-9](#isr4431-mod-9); [ISR4431-MOD-10](#isr4431-mod-10) |

The analog FXS/FXO/E&M and BRI voice NIMs contain their own DSP; they do
not require a motherboard PVDM for voice packetization. A motherboard PVDM4
serves IP media functions, while T1/E1 packetization uses a PVDM4 on that NIM
([ISR4431-MOD-3](#isr4431-mod-3), [ISR4431-MOD-4](#isr4431-mod-4)).
`SM-X-PVDM-*` is **documented unsupported** on ISR4431, and the PVDM source
restricts `NIM-PVDM-*` to Catalyst 8300/ISR 4461; a matching NIM slot does not
make it compatible ([ISR4431-MOD-3](#isr4431-mod-3), platform support).
UCS-E/SM-X reuse is unavailable through the absent SM-X slot. Cellular remains
available, not assessed. This module pass does not investigate cellular PIDs.

### Optics

Source: Cisco's live Optics-to-Device Compatibility Matrix (TMG) for network
device "4431" (product family ISR4000), 22 records, exported from Cisco on
2026-10-30 ([ISR4431-OPT-2](#isr4431-opt-2)). It replaces the 2022
third-party copy ([ISR4431-OPT-1](#isr4431-opt-1)) for the chassis ports. The
live data matches the 2022 copy on every chassis minimum-set PID and release,
except that DOM software support for GLC-SX-MMD and GLC-LH-SMD is listed from
IOS XE 3.1, and GLC-T and SFP-GE-T are now marked End-of-Sale. NIM-1GE/2GE
rows still come from the 2022 copy. TMG results are non-exhaustive.

**Port inventory**

| Port type | Speeds | Form factor | Restrictions | Source |
| --- | --- | --- | --- | --- |
| Onboard GE 0/0/0–0/0/3 | 10/100/1000 (RJ-45); 100 Mbps and 1 Gbps optics in SFP | RJ-45 or SFP (dual-mode) | One medium per port; `media-type rj45` or `media-type sfp`, auto-detect default, auto-failover without automatic failback | DS-1; [ISR4431-CFG-5](#isr4431-cfg-5); OPT-1 |
| NIM-1GE/2GE-CU-SFP ports | as onboard | RJ-45 or SFP | MACsec only on NIM-2GE | DS-2; OPT-1 |
| 10G (SFP+) ports | **none on chassis or verified modules** | — | — | DS-1 |

**Minimum set** (onboard ports; NIM-1GE/2GE-CU-SFP rows in OPT-1 list the same
PIDs, min releases differ as noted)

| Item | PID | Reach / media | Onboard min SW | NIM-2GE min SW | DOM | Source |
| --- | --- | --- | --- | --- | --- | --- |
| 1000BASE-SX | `GLC-SX-MMD` | 1,000 m on OM3/OM4 (550 m OM2), MMF LC | IOS XE 3.1 (DOM 3.1) | 3.15 | Y | OPT-2; OPT-1 (NIM) |
| 1000BASE-LX/LH | `GLC-LH-SMD` | 10 km SMF (550 m MMF w/ mode-conditioning cable) | 3.1 (DOM 3.1) | 3.15 | Y | OPT-2; OPT-1 (NIM) |
| 1000BASE-ZX | `GLC-ZX-SMD` | 70 km SMF | 3.16.1 | 3.16.1 | Y | OPT-2; OPT-1 (NIM) |
| (1000BASE-EX) | `GLC-EX-SMD` | 40 km SMF | 3.15 | listed | Y | OPT-2; OPT-1 (NIM) |
| 1000BASE-T SFP | `GLC-T` (End-of-Sale), `GLC-TE`, `SFP-GE-T` (End-of-Sale) | 100 m Cat5e/6A, "10/100/1000 Mbps" rate | 3.11 / 3.16 / 3.13 | 3.15 / 3.16 / 3.15 | N | OPT-2; OPT-1 (NIM) |
| 10GBASE-SR/LR/ER/ZR | — | — | not applicable (no 10G port) | — | — | DS-1; OPT-1 |
| 10GBASE-T SFP+ | — | — | not applicable | — | — | — |
| 1G DAC | none listed | — | **not verified** | — | — | OPT-2 |
| 10G DAC | — | — | not applicable | — | — | — |

Long-reach restrictions: none stated in OPT-2 for ZX/EX beyond case
temperature (−5 to 85 °C). OPT-2 also lists 100 Mb/s fiber SFPs
(`GLC-FE-100FX/LX/EX/ZX`, `GLC-GE-100FX`, `GLC-FE-100BX-D/U`), 1G BiDi
(`GLC-BX-D/U`, `GLC-BX40-D/U-I`, `GLC-BX80-D/U-I`), and `CWDM-SFP-XXXX` /
`DWDM-SFP-XXXX` for the chassis. Power/thermal limits: not found.

**Ports faster than 10G:** none on the chassis or any module found for the
ISR4431.

**Copper SFPs (direct answer)**

| Port type | 1G copper SFP (1000BASE-T) | 10G copper SFP+ (10GBASE-T) |
| --- | --- | --- |
| Onboard SFP | **yes** — `GLC-T`, `GLC-TE`, `SFP-GE-T`; rate listed "10/100/1000 Mbps"; 100 m; count/adjacency limits not found; 100 Mbps negotiation not verified beyond the rate column | **no port** (not applicable) |
| NIM-1GE/2GE-CU-SFP | **yes** — same PIDs (OPT-1) | not applicable |

Built-in RJ-45: yes, each onboard port can be used as 10/100/1000 RJ-45
directly, so copper needs are met without copper SFPs — at the cost of that
port's SFP position (dual-mode, inferred as above).

**Platform policy:** Cisco's third-party optics position and whether
`service unsupported-transceiver` exists on this platform: **not verified**.
DOM: OPT-2 lists "DOM Capable = Y" and DOM software support for the fiber
optics above (copper SFPs N). The DOM `show` command is documented only in a
generic, multi-platform form (Appendix A).

**Not reviewed in this research**

| Optics family | Status |
| --- | --- |
| CWDM | needed, not reviewed in this research (OPT-1 lists `CWDM-SFP-XXXX` rows) |
| DWDM | needed, not reviewed in this research (OPT-1 lists `DWDM-SFP-XXXX` rows) |
| BiDi | needed, not reviewed in this research |
| Extended-temperature (industrial) | needed, not reviewed in this research |

### Module reuse across the four platforms

| Direction / family | Finding | Label | Source |
| --- | --- | --- | --- |
| General | "Over 70% of the ISR4000 platform family's modules are being reused by the Cisco Catalyst 8300 Series Edge Platforms." | documented (family, unspecific) | [ISR4431-DS-3](#isr4431-ds-3) |
| T1/E1 MFT NIMs (`NIM-1/2/4/8MFT-T1/E1`) | Listed for the ISR4431 and in the C8300 supported-module table | documented on both | MOD-1; DS-3 Table 7 |
| NIM-ES2, listed analog/BRI voice and DSL families | Chassis support now documented on ISR4431 and listed for C8300; release/mode and orderability remain separate checks | documented at chassis-list level | [ISR4431-MOD-2](#isr4431-mod-2) through [ISR4431-MOD-7](#isr4431-mod-7); DS-3 |
| `NIM-1GE-CU-SFP`, `NIM-2GE-CU-SFP` | Supported on ISR 4000; not in the C8300 data-sheet module table (absence is not proof of non-support) | not verified on C8300 | DS-2; DS-3 |
| PVDM4 (ISC) | C8300 data sheet lists no ISC/PVDM4; C8300 DSPs come from `NIM-PVDM-*` / `SM-X-PVDM-*` | not found on C8300 | DS-3 |
| C8300 / C8375 SM and PIM modules → ISR4431 | Cannot be installed: ISR4431 has no SM-X or PIM slot | inferred (slot absence, DS-1) | DS-1 |
| C8375-E-G2 modules ↔ ISR4431 | Not checked in this file; see model 3 file | not verified | — |

Reuse is noted only because the request asks; all purchases are new.

## 9. Platform-specific caveats

The continuation read the public advisory/field-notice bodies rather than
accepting support-page titles as applicability evidence. Scope: selected
decision-relevant IOS XE hardening, UTD, Secure Boot and licensing/voice
notices, plus the 17.12 release notes. This is not an exhaustive vulnerability
assessment or a claim that a particular installed router is clear of issues.

| Item | Affected / applicability | Impact | Fix / mitigation and basis assessment | Source |
| --- | --- | --- | --- | --- |
| Final train17.12.x | ISR4431 | No later feature train | Stay within exact platform ceiling; replacement required for later trains | [ISR4431-REL-3](#isr4431-rel-3), [ISR4431-EOL-1](#isr4431-eol-1) |
| IOS XE August2026 hardening | IOS XE autonomous/controller; PID applicability inferred from OS scope | Multiple vulnerability classes, highest CVSS9.8 | First fixed17.12 release17.12.8; basis meets this bulletin's release floor; no workaround | [ISR4431-PSIRT-1](#isr4431-psirt-1), Fixed Releases |
| October2026 Snort3 hardening | UTD Snort3 feature/package, not a bare-router assumption | Critical engine vulnerabilities | For17.12, first fixed UTD package `secapp-utd.17.12.08.1.2.8_SV3.12.4.0_XE17.12`; validate the installed engine as well as IOS XE17.12.8 | [ISR4431-PSIRT-2](#isr4431-psirt-2), UTD fixed table |
| Snort3 SMTP MIME / miscellaneous DoS | 4000 Series with vulnerable UTD installed; family scope | Remote denial of service | Same17.12.8 UTD package above; no UTD file means these conditional advisories do not apply | [ISR4431-PSIRT-3](#isr4431-psirt-3), [ISR4431-PSIRT-4](#isr4431-psirt-4) |
| CVE-2024-20508 | UTD plus Web Filtering and/or Multi-Tenancy | Snort failure: fail-open may bypass inspection; fail-close may drop inspected traffic | First fixed UTD17.12 release17.12.4; verify engine version/configuration, not just chassis image | [ISR4431-PSIRT-5](#isr4431-psirt-5) |
| CVE-2019-1649 Secure Boot | ISR4431 explicitly listed; elevated local access | FPGA/Secure Boot tampering or device unusable | Cisco lists utility `isr4400_cpld_update_v1.1_SPA.bin`; confirm platform-specific CPLD procedure and actual firmware, not only IOS XE | [ISR4431-PSIRT-6](#isr4431-psirt-6), exact ISR4431 row |
| FN72510 weak IPsec algorithms | ISR4000 from17.11.1a; therefore basis17.12.8 | Legacy weak algorithms rejected; tunnels can fail after upgrade | Update peers/proposals to stronger algorithms; default behavior change, not a reason to bypass compliance | [ISR4431-FN-1](#isr4431-fn-1) |
| FN72578 SLP resource use | RUM report accumulation; exact ISR4431 included | High CPU/memory; important to disconnected reporting operations | Notice lists fixed17.3.7/17.6.5/17.9.1 or later. Basis is later, but monitor offline report/ACK workflow; exact symptom fix at basis inferred from that wording | [ISR4431-FN-2](#isr4431-fn-2) |
| FN72323 trust roots | Affected Cisco services/older trust stores;4431 listed | Online licensing/Call Home TLS failures | Fixed17.7.1 or later among listed branches; basis is later. PLR/SLR exemption in this old notice does not establish SLR support on ISR4431; file reporting avoids direct router TLS reliance (inferred) | [ISR4431-FN-3](#isr4431-fn-3) |
| FN74350 CUBE certificates | ISR4431 listed; mTLS/certificate use determines exposure | Certificate EKU changes can affect secure communication | Notice explicitly says ISR4000 cannot run26.1.1 and its26.1 solution is unavailable. At older releases, EKU checking depends on `match eku client-auth`/cc-mode; audit actual trust/certificate configuration with TAC | [ISR4431-FN-4](#isr4431-fn-4), Workaround/Solution |
| UTD resources / Boost | Default4GB control memory | UTD needs8GB (12GB High profile); Boost blocks UTD container | Check RAM, module/lifecycle fit and desired Boost use before enabling UTD | [ISR4431-SEC-2](#isr4431-sec-2) |
| New-purchase failure | ISR4431 and named C8300 replacements' ordering windows | Chassis is already End-of-Sale | Reference only; compare current orderable platforms | [ISR4431-EOL-1](#isr4431-eol-1), [ISR4431-EOL-4](#isr4431-eol-4) |

Hardware/serial applicability: firmware status and actual device configuration
must be collected for Secure Boot and the conditional UTD/voice notices.
The support page's `PWR-CC1-500WAC` FN74118 entry is not evidence that this
PSU is compatible with ISR4431; no applicability is inferred from a page
listing alone ([ISR4431-SUP-1](#isr4431-sup-1), [ISR4431-HIG-1](#isr4431-hig-1)).

Closest sibling: ISR4451-X — DS-1 gives it 1 Gbps default / 2 Gbps
performance throughput, and the TMG matrix lists 10G SFP+ optics for it
(module-based); the ISR4431 has neither. The ISR 4461 remains supported on
17.15+ ([ISR4431-REL-3](#isr4431-rel-3)).

## 10. Appendix A: identification and inventory commands

All commands are privileged EXEC (`#`) read-only. Redact serial numbers and
UDIs before sharing output.

### Annotated listing

Model, version, mode, install state — [ISR4431-CFG-3](#isr4431-cfg-3),
[ISR4431-CFG-4](#isr4431-cfg-4):

```text
show version
! IOS XE version, PID, serial, ROMMON; "Router operating mode: Autonomous" on 17.x
show version installed
! installed packages
show install summary
! install-mode package state (install mode only)
show platform
! chassis, slots/subslots, module states
```

Inventory, environment, power — [ISR4431-CFG-2](#isr4431-cfg-2):

```text
show inventory
! PID/VID/serial for chassis, PSUs, fan, modules, SFPs
show diag chassis eeprom
! chassis EEPROM (PID, serial, MAC, hardware revision)
show environment all
! temperatures, fan, PSU status
show power
! power supply and PoE budget
show power inline
! per-port PoE (PoE-capable ports only)
```

Throughput level — [ISR4431-LIC-3](#isr4431-lic-3),
[ISR4431-CFG-3](#isr4431-cfg-3):

```text
show platform hardware throughput level
! current throughput level (e.g., unthrottled with boost)
```

Licensing and reporting — [ISR4431-LIC-1](#isr4431-lic-1) (command reference,
PDF p. 250 ff.):

```text
show license summary
! licenses in use and status
show license usage
! per-license usage and enforcement type
show license status
! transport, policy, last ACK, next ACK deadline
show license authorization
! SLAC / HSECK9 authorization state
show license udi
! PID and serial (UDI)
show license all
! combined licensing detail
```

Gaps (left out of the capture block): DOM light levels and temperature.
[ISR4431-CMD-1](#isr4431-cmd-1) documents `show interfaces transceiver` ("to
display information about the optical transceivers that have digital optical
monitoring (DOM) enabled") with per-platform syntax for Catalyst 6500/7600,
7200 VXR, ASR 901 and ASR 1000, but no ISR 4000 form, so
`show interfaces transceiver` on the ISR4431 is **inferred** from the ASR 1000
(IOS XE) form; module-specific `show hw-module subslot …`
forms not verified at 17.12; `license boot level` (configuration) is not
read-only and its ISR 4000 syntax is not verified.

### Paste-ready capture block

```text
terminal length 0
show version
show version installed
show install summary
show platform
show inventory
show diag chassis eeprom
show environment all
show power
show power inline
show platform hardware throughput level
show license summary
show license usage
show license status
show license authorization
show license udi
show license all
```

## References

#### ISR4431-MSR-1

- Title: IP Multicast Configuration Guide, Cisco IOS XE, “Implementing Multicast Service Reflection”
- Used for: MSR configuration, prerequisites, Vif restrictions, unicast-to-multicast behavior, and feature introduction information
- URL: https://www.cisco.com/c/en/us/td/docs/routers/ios-xe/ip-multicast/ip-multicast/m_imc_service_reflect-0.html
- Accessed: 2026-11-01
- Locator: Implementing Multicast Service Reflection; Feature Information for Multicast Service Reflection
- Local PDF: not saved (HTML)

#### ISR4431-MSR-REL-1

- Title: Release Notes for Cisco 4000 Series Integrated Services Routers, Cisco IOS XE Cupertino 17.9.x
- Used for: family/release-level evidence for Unicast-to-Multicast Destination Reflection; ISR 4431 model-family identification
- URL: https://www.cisco.com/c/en/us/td/docs/routers/access/4400/release/xe-17-9/isr4k-rel-notes-xe-17-9.html
- Accessed: 2026-11-01
- Locator: New and Changed Information; feature entry for IOS XE 17.9.1a
- Local PDF: not saved (HTML)

#### ISR4431-EOL-1

- Title: End-of-Sale and End-of-Life Announcement for the Cisco ISR4200,
  ISR4300 and select ISR4400 Series Platform (EOL14896, Amended)
- Used for: identity, chassis/license milestones, replacement PIDs, train
  statements, EoS memory/PSU/license PIDs
- URL:
  https://www.cisco.com/c/en/us/products/collateral/routers/4000-series-integrated-services-routers-isr/select-isr4k-series-platform-eol.html
- Date/revision: updated 2024-11-06
- Accessed: 2026-10-30
- Locator: Table 1 (milestones); text after Table 1 (IOS XE trains); Table 2
  (part numbers)
- Local PDF:
  [reference/isr4k-eol14896-2024-11-06.pdf](reference/isr4k-eol14896-2024-11-06.pdf)
  (PDF modified 2024-11-06; 14 pages). Retrieved 2026-10-30 with a headless
  browser, with the user's approval. Milestone dates match the HTML page.

#### ISR4431-EOL-2

- Title: End-of-Sale and End-of-Life Announcement for the Cisco ISR4200,
  ISR4300 and select ISR4400 Series Platform Spares (EOL15205, Amended)
- Used for: spares milestones and PIDs
- URL:
  https://www.cisco.com/c/en/us/products/collateral/routers/4000-series-integrated-services-routers-isr/isr4200-isr4300-sel-isr4400-spa-eol.html
- Date/revision: updated 2024-03-29
- Accessed: 2026-10-30
- Locator: Tables 1 and 2
- Local PDF: not saved

#### ISR4431-EOL-3

- Title: End-of-Sale and End-of-Life Announcement for the Cisco IOS XE 17.12.x
  (EOL15518)
- Used for: software-train milestones
- URL:
  https://www.cisco.com/c/en/us/products/collateral/ios-nx-os-software/ios-xe-17/ios-xe-17-12-x-eol.html
- Date/revision: announced 2024-10-03
- Accessed: 2026-10-30
- Locator: Table 1
- Local PDF: not saved

#### ISR4431-EOL-4

- Title: End-of-Sale and End-of-Life Announcement for the Cisco Catalyst
  C8500L-8S4X, C8300-1N1S-4T2X, C8300-1N1S-6T (EOL15950, Amended)
- Used for: replacement-chain status
- URL: https://www.cisco.com/c/en/us/products/collateral/networking/sdwan-routers/catalyst-8000-edge-platforms/catalyst-c8500l-8s4x-4t2x-c8300-1n1s-6t-eol.html
- Date/revision: announced 2026-07-27; PDF created 2026-10-19
- Accessed: 2026-10-30 (local copy read)
- Locator: Table 1 (p. 3), last-train text (p. 4), Table 2
- Local PDF:
  [reference/c8300-1n1s-eol15950-2026-10-19.pdf](reference/c8300-1n1s-eol15950-2026-10-19.pdf)
  (reused)

#### ISR4431-EOL-5

- Title: Cisco 4000 Series Integrated Services Routers — End-of-Life and
  End-of-Sale Notices (listing)
- Used for: inventory of related platform, module, and software notices
- URL:
  https://www.cisco.com/c/en/us/products/routers/4000-series-integrated-services-routers-isr/eos-eol-notice-listing.html
- Date/revision: not stated
- Accessed: 2026-10-30
- Locator: listing entries
- Local PDF: not applicable

#### ISR4431-SUP-1

- Title: Cisco 4431 Integrated Services Router — support page
- Used for: product status, field notices, advisory listing
- URL:
  https://www.cisco.com/c/en/us/support/routers/4441-x-integrated-services-router-isr/model.html
- Date/revision: not stated
- Accessed: 2026-10-30
- Locator: Product status; Field Notices; Security Advisories
- Local PDF: not applicable

#### ISR4431-DS-1

- Title: Cisco 4000 Family Integrated Services Router Data Sheet (c78-732542)
- Used for: hardware, throughput, licensing overview, modes, secure boot
- URL:
  https://www.cisco.com/c/en/us/products/collateral/routers/4000-series-integrated-services-routers-isr/data_sheet-c78-732542.html
  (PDF:
  https://www.cisco.com/c/en/us/products/collateral/routers/4000-series-integrated-services-routers-isr/data_sheet-c78-732542.pdf)
- Date/revision: page "Updated" 2026-06-23; last history entry 2024-08-28
- Accessed: 2026-10-30
- Locator: Table 2 (features), Table 5 (specifications), Tables 6–8
  (bundles, performance/boost licenses), licensing and ordering text
- Local PDF:
  [reference/isr4000-datasheet-c78-732542-2026-06-23.pdf](reference/isr4000-datasheet-c78-732542-2026-06-23.pdf)
  (PDF modified 2026-06-23; 28 pages). Retrieved 2026-10-30 with a headless
  browser (Playwright Chromium) after plain `curl` got "Access Denied", with
  the user's approval. Table 5 pp. 11-13 read as rendered page images.

#### ISR4431-DS-2

- Title: Cisco 4000 Series Integrated Services Router Gigabit Ethernet WAN
  Modules Data Sheet (c78-730527)
- Used for: NIM-1GE/2GE-CU-SFP platform support, MACsec, OIR
- URL:
  https://www.cisco.com/c/en/us/products/collateral/routers/4000-series-integrated-services-routers-isr/datasheet-c78-730527.html
- Date/revision: updated 2019-07-17
- Accessed: 2026-10-30
- Locator: Table 1
- Local PDF: not saved

#### ISR4431-DS-3

- Title: Cisco Catalyst 8300 Series Edge Platforms Data Sheet
- Used for: module reuse statement and C8300 module table
- URL:
  https://www.cisco.com/c/en/us/products/collateral/routers/catalyst-8300-series-edge-platforms/datasheet-c78-744088.html
- Date/revision: updated 2026-10-06
- Accessed: 2026-10-30 (HTML)
- Locator: Sustainability section; Table 7
- Local PDF:
  [reference/c8300-edge-datasheet-2026-10-06.pdf](reference/c8300-edge-datasheet-2026-10-06.pdf)
  (saved by another subagent; reused)

#### ISR4431-DS-4

- Title: Cisco Unified Border Element Data Sheet (version 15)
- Used for: CUBE session scale for the 4431; DSP requirement
- URL:
  https://www.cisco.com/c/en/us/products/collateral/unified-communications/unified-border-element/data-sheet-c78-729692.html
- Date/revision: updated 2026-10-14
- Accessed: 2026-10-30
- Locator: Table 1; Table 3 (End of Life platforms)
- Local PDF: not saved

#### ISR4431-HIG-1

- Title: Hardware Installation Guide for Cisco 4000 Series Integrated Services
  Routers — Overview of the Cisco 4000 Series ISRs
- Used for: slots, PoE, power options, flash, DIMMs, management port
- URL:
  https://www.cisco.com/c/en/us/td/docs/routers/access/4400/hardware/installation/guide4400-4300/C4400_isr/Overview.html
- Date/revision: updated 2014-09-10
- Accessed: 2026-10-30
- Locator: Table 1-4; PoE section; dual-mode port section; Figures 1-13,
  1-14, 1-16
- Local PDF: not saved

#### ISR4431-REL-1

- Title: Choose Stable Cisco IOS XE Release for Enterprise Routing Platforms
  (document 215567)
- Used for: Cisco-recommended release
- URL:
  https://www.cisco.com/c/en/us/support/docs/ios-nx-os-software/ios-xe-16/215567-recommended-releases-for-asr1000-isr400.html
- Date/revision: revision 9.0, 2026-06-15
- Accessed: 2026-10-30
- Locator: recommended-release table, row "ISR4200/4300/4431/4451"
- Local PDF: not saved

#### ISR4431-REL-2

- Title: Release Notes for Cisco 4000 Series ISRs, Cisco IOS XE Dublin
  17.12.x
- Used for: 4431 coverage, newest rebuild 17.12.8, ROMMON/CPLD, SLP notes
- URL:
  https://www.cisco.com/c/en/us/td/docs/routers/access/4400/release/xe-17-12/isr4k-rel-notes-xe-17-12.html
- Date/revision: first published 2023-08-22; updated 2026-08-05
- Accessed: 2026-10-30
- Locator: Table 1 (firmware); resolved-bug sections per rebuild
- Local PDF: not saved

#### ISR4431-REL-3

- Title: Release Notes for Cisco 4000 Series ISRs, Cisco IOS XE Release
  17.15.x
- Used for: documented software ceiling (17.12.x)
- URL:
  https://www.cisco.com/c/en/us/td/docs/routers/access/4400/release/xe-17-15/isr4k-rel-notes-xe-17-15.html
- Date/revision: first published 2024-08-26; updated 2026-08-05
- Accessed: 2026-10-30
- Locator: supported-platform statement
- Local PDF: not saved

#### ISR4431-REL-4

- Title: Cisco 4000 Series ISRs — Release Notes listing
- Used for: inventory of release-note trains (17.13–17.18 exist for the
  family; applicability limited by REL-3)
- URL:
  https://www.cisco.com/c/en/us/support/routers/4000-series-integrated-services-routers-isr/products-release-notes-list.html
- Date/revision: not stated
- Accessed: 2026-10-30
- Locator: IOS XE 17.x list
- Local PDF: not applicable

#### ISR4431-LIC-1

- Title: Smart Licensing Using Policy for Cisco Enterprise Routing Platforms
- Used for: SLP support from 17.3.2, policy defaults, topologies, offline
  workflow, SLAC, HSECK9 mapping and ordering PIDs, ISR 4400 license names,
  command reference
- URL: https://www.cisco.com/c/en/us/td/docs/routers/sl_using_policy/b-sl-using-policy.html
  (chapters read: `.../b-sl-using-policy/info_about.html`,
  `.../m-sle-how-smart-licensing-using-policy-works.html`,
  `.../how_to_configure_workflows.html`, `.../task_library.html`)
- Date/revision: first published 2020-09-25; last modified 2023-08-01
- Accessed: 2026-10-30
- Locator: PDF p. 27–28 (topologies, SSM On-Prem sync); p. 57 (HSECK9 upgrade
  behavior); p. 65 (ISR 4400 license names); p. 123 (default licenses); p. 155
  (DNA_HSEC); p. 204 (`license feature hseck9`); p. 250 ff. (command
  reference); p. 306 (ACK deadline syslog); p. 340 (`REPORTING_REQUIRED`); p.
  355–357 (HSECK9 ordering)
- Local PDF:
  [reference/enterprise-routing-slp-guide-2023-08-01.pdf](reference/enterprise-routing-slp-guide-2023-08-01.pdf)
  (saved by another subagent; reused)

#### ISR4431-LIC-2

- Title: Cisco DNA Software for SD-WAN and Routing Ordering Guide
  (c07-740642)
- Used for: DNA tiers, terms, ISR 4000 Appendix D, security feature table
- URL:
  https://www.cisco.com/c/en/us/products/collateral/software/dna-subscription-routing/guide-c07-740642.html
- Date/revision: updated 2026-06-17
- Accessed: 2026-10-30
- Locator: Tables 1–3, 6, 9, 10; Appendix D
- Local PDF: not saved

#### ISR4431-LIC-3

- Title: Implement Performance License for Integrated Service Router 4000
  (document 217135)
- Used for: PPE core counts, throughput/boost activation, reload, commands
- URL:
  https://www.cisco.com/c/en/us/support/docs/routers/4000-series-integrated-services-routers/217135-performance-license-on-cisco-isr4000.html
- Date/revision: revision 4.0, 2026-06-25
- Accessed: 2026-10-30
- Locator: ISR 4431 throughput table; boost section
- Local PDF: not saved

#### ISR4431-LIC-4

- Title: Configure Smart Licensing Using Policy on IOS XE Routers (document
  217046\)
- Used for: ISR4000 SLP from 17.3.2; offline reporting steps
- URL:
  https://www.cisco.com/c/en/us/support/docs/ios-nx-os-software/ios-xe-17/217046-configure-smart-licensing-using-policy-o.html
- Date/revision: updated 2026-07-01
- Accessed: 2026-10-30
- Locator: Components Used; offline topology sections
- Local PDF: not saved

#### ISR4431-CFG-1

- Title: Cisco 4000 Series ISRs Software Configuration Guide, Cisco IOS XE 17
  (book)
- Used for: chapter inventory (no SLP or throughput chapter; Smart Licensing
  chapter is pre-SLP)
- URL:
  https://www.cisco.com/c/en/us/td/docs/routers/access/isr4400/software/configuration/xe-17/isr4400-sw-config-xe-17.html
- Date/revision: updated 2024-08-26
- Accessed: 2026-10-30
- Locator: table of contents; "Smart Licensing" chapter
- Local PDF: not saved

#### ISR4431-CFG-2

- Title: Environmental Monitoring and PoE Management (ISR 4000 SW config
  guide, IOS XE 17)
- Used for: inventory/environment/power `show` commands
- URL:
  https://www.cisco.com/c/en/us/td/docs/routers/access/isr4400/software/configuration/xe-17/isr4400-sw-config-xe-17/environmental_monitoring_and_poe_management.html
- Date/revision: updated 2024-08-26
- Accessed: 2026-10-30
- Locator: command examples
- Local PDF: not saved

#### ISR4431-CFG-3

- Title: Installing the Software (ISR 4000 SW config guide, IOS XE 17)
- Used for: `show version`, `show version installed`, `show platform`,
  `show platform hardware throughput level`
- URL:
  https://www.cisco.com/c/en/us/td/docs/routers/access/isr4400/software/configuration/xe-17/isr4400-sw-config-xe-17/installing_the_software.html
- Date/revision: updated 2024-08-26
- Accessed: 2026-10-30
- Locator: command examples
- Local PDF: not saved

#### ISR4431-CFG-4

- Title: Installing the Software using install Commands (ISR 4000 SW config
  guide, IOS XE 17)
- Used for: install/bundle mode, install `show` commands, operating-mode line
- URL:
  https://www.cisco.com/c/en/us/td/docs/routers/access/isr4400/software/configuration/xe-17/isr4400-sw-config-xe-17/m_installing-the-software-using-install-commands.html
- Date/revision: not stated
- Accessed: 2026-10-30
- Locator: restrictions; show-command list; downgrade example
- Local PDF: not saved

#### ISR4431-CFG-5

- Title: SFP Auto-Detect and Auto-Failover (ISR 4000 SW config guide, IOS XE
  17\)
- Used for: dual-media port behavior, `media-type`
- URL:
  https://www.cisco.com/c/en/us/td/docs/routers/access/isr4400/software/configuration/xe-17/isr4400-sw-config-xe-17/sfp_auto_detect_and_auto_failover.html
- Date/revision: not stated
- Accessed: 2026-10-30
- Locator: chapter body
- Local PDF: not saved

#### ISR4431-CFG-7

- Title: IP Addressing Configuration Guide, Cisco IOS XE 17.x
- Used for: NAT support on Cisco 4000 Series ISR (family)
- URL: https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-addressing/b-ip-addressing.html
- Date/revision: updated 2022-11-15
- Accessed: 2026-10-30
- Locator: "This Document Applies to These Products"; NAT chapters
- Local PDF: not saved

#### ISR4431-CFG-8

- Title: Quality of Service Configuration Guide, Cisco IOS XE 17.x
- Used for: QoS support on Cisco 4000 Series ISR (family)
- URL: https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/qos/b-quality-of-service.html
- Date/revision: updated 2022-03-11
- Accessed: 2026-10-30
- Locator: "This Document Applies to These Products"
- Local PDF: not saved

#### ISR4431-SEC-1

- Title: Security and VPN Configuration Guide, Cisco IOS XE 17.x
- Used for: AAA/RADIUS/TACACS+, IPsec/IKEv2/FlexVPN/DMVPN/GETVPN, ZBFW,
  TrustSec on Cisco 4000 Series ISR (family)
- URL: https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/sec-vpn/b-security-vpn.html
- Date/revision: updated 2021-01-11
- Accessed: 2026-10-30
- Locator: product list; chapter list
- Local PDF: not saved

#### ISR4431-SEC-2

- Title: Snort IPS — Security Configuration Guide: Unified Threat Defense,
  Cisco IOS XE 17
- Used for: Snort IPS support on 4431, resource requirements, restrictions
- URL:
  https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/sec_data_utd/configuration/xe-17/sec-data-utd-xe-17-book/snort-ips.html
- Date/revision: updated 2019-12-04
- Accessed: 2026-10-30
- Locator: supported platforms; resource profile table; restrictions
- Local PDF: not saved

#### ISR4431-SEC-3

- Title: Cisco TrustSec Configuration Guide, Cisco IOS XE Gibraltar 16.12.x
- Used for: TrustSec feature set applies to 4000 Series ISRs (family; 16.12
  doc)
- URL:
  https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/sec_usr_cts/configuration/xe-16-12/sec-usr-cts-xe-16-12-book.html
- Date/revision: updated 2019-07-15
- Accessed: 2026-10-30
- Locator: product list; SXP and SGACL chapters
- Local PDF: not saved

#### ISR4431-SEC-4

- Title: Cisco Group Based Policy Platform and Capability Matrix (Inclusive of
  TrustSec Software-Defined Segmentation)
- Used for: ISR 4431 TrustSec capabilities and license; SXP scale
- URL: https://www.cisco.com/c/dam/en/us/solutions/collateral/enterprise-networks/trustsec/cisco-trustsec-platform-capability-matrix.pdf
- Date/revision: 2026-02-23 (per filename)
- Accessed: 2026-10-30 (local copy read)
- Locator: Table 1 (PDF p. 5, "4000 Series ISR 4431, 4451-X, 4321, 4331,
  4351"); Table 8 (PDF p. 16)
- Local PDF:
  [reference/cisco-gbp-trustsec-platform-matrix-2026-02-23.pdf](reference/cisco-gbp-trustsec-platform-matrix-2026-02-23.pdf)
  (reused)

#### ISR4431-MOD-1

- Title: Cisco fourth-generation T1/E1 multiflex trunk voice/WAN NIM — Q&A
  (q-and-a-c67-733647)
- Used for: T1/E1 NIM support on 4431
- URL:
  https://www.cisco.com/c/en/us/products/collateral/routers/4000-series-integrated-services-routers-isr/q-and-a-c67-733647.html
- Date/revision: updated 2015-02-24 (predates some 4431 features; its PVDM4
  statements are superseded by DS-1/HIG-1)
- Accessed: 2026-10-30
- Locator: Table 2
- Local PDF: not saved

#### ISR4431-OPT-1

- Title: Cisco Optics-to-Device Compatibility Matrix Results — Network Device
  Product Family ISR4000 (third-party mirror of Cisco TMG output)
- Used for: ISR4431 onboard and NIM-1GE/2GE optics, min software, DOM
- URL: https://data.nag.wiki/Cisco/Datasheets/ISR4000/ISR4000_TMGCMPDF.pdf
  (third-party host, last resort)
- Date/revision: PDF created 2022-03-20
- Accessed: 2026-10-30
- Locator: rows "4431", "NIM-1GE-CU-SFP", "NIM-2GE-CU-SFP" (pp. 1–6)
- Local PDF:
  [reference/isr4000-tmg-matrix-2022-03-20.pdf](reference/isr4000-tmg-matrix-2022-03-20.pdf)
  (saved by this subagent; verified as PDF, 8 pages, text readable)

#### ISR4431-OPT-2

- Title: Cisco Optics-to-Device Compatibility Matrix results, network device
  "4431" (product family ISR4000; 22 records)
- Used for: chassis optics minimum set, min software, DOM, End-of-Sale flags
- URL: https://tmgmatrix.cisco.com/ (search text `4431`). Retrieved through
  the site's public endpoints `POST /public/api/networkdevice/search` and
  `.../search/export/pdf` with the app's own filter body
  (`searchInput: ["4431"]`), the same method used for the other models. TMG's
  autosuggest knows this device as `4431`, not `ISR4431`.
- Date/revision: live data, exported 2026-10-30
- Accessed: 2026-10-30
- Locator: device "4431"
- Local PDF:
  [reference/isr4431-tmg-optics-2026-10-30.pdf](reference/isr4431-tmg-optics-2026-10-30.pdf)

#### ISR4431-MX-1

- Title: Cisco DNA Software SD-WAN and Routing Matrices
- Used for: DNA Essentials vs. DNA Advantage feature categories (applicability
  to the ISR 4000 **inferred**: the matrix names no platforms, and its
  Catalyst Routing Essentials column is a Catalyst 8000 offer)
- URL: https://www.cisco.com/c/m/en_us/products/software/sd-wan-routing-matrix.html
  (PDF: https://www.cisco.com/c/dam/m/en_us/products/software/dna-software/dna-software-sd-wan-routing-matrix/pdf/Cisco_DNA_Software_SD-WAN_and_Routing_Matrices.pdf)
- Date/revision: PDF modified 2025-05-02
- Accessed: 2026-10-30
- Locator: "Platform based routing features" section and footnotes
- Local copies:
  [reference/dna-sd-wan-routing-matrices-2025-05-02.pdf](reference/dna-sd-wan-routing-matrices-2025-05-02.pdf);
  tick values and category feature lists read from the page code:
  [reference/dna-routing-matrix-tiers-2026-10-30.txt](reference/dna-routing-matrix-tiers-2026-10-30.txt)

#### ISR4431-CMD-1

- Title: Cisco IOS Interface and Hardware Component Command Reference —
  show hw-module slot tech-support through show interfaces vg-anylan
- Used for: `show hw-module subslot` existence on 4400 Series ISR;
  `show interfaces transceiver` description and per-platform syntax (no ISR
  4000 form). Full page text read 2026-10-30 with a headless browser after
  the web-fetch tool truncated it.
- URL: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/interface/command/ir-cr-book/ir-s4.html
- Date/revision: updated 2023-10-05
- Accessed: 2026-10-30
- Locator: `show hw-module subslot` command history
- Local PDF: not saved

#### ISR4431-SDWAN-1

- Title: Cisco Recommended Catalyst SD-WAN Software Versions for Controllers and WAN Edge Routers (215676).
- Used for: Controller/edge recommended releases; hardware support remains a separate gate.
- URL: <https://www.cisco.com/c/en/us/support/docs/routers/sd-wan/215676-cisco-tac-and-bu-recommended-sd-wan-soft.html>
- Document revision: Updated 2026-08-19; revision21.0.
- Accessed: 2026-10-31 UTC (2026-10-30 America/Chicago); public source body read through native webpage tools, not search snippets.
- Locator: Current Recommended Releases Overview and hardware qualification footnote.
- Local PDF: not saved; existing saved PDFs were preserved.

#### ISR4431-SDWAN-2

- Title: Cisco Catalyst SD-WAN Device Compatibility.
- Used for: Exact ISR4431 SD-WAN minimum16.10.1 and final17.12.x train.
- URL: <https://www.cisco.com/c/en/us/td/docs/routers/sdwan/release/compatibility/sdwan-device-compatibility.html>
- Document revision: Live page; revision date not recorded.
- Accessed: 2026-10-31 UTC (2026-10-30 America/Chicago); public source body read through native webpage tools, not search snippets.
- Locator: Cisco ISR4000 Series table, ISR4431 row.
- Local PDF: not saved; existing saved PDFs were preserved.

#### ISR4431-SDWAN-3

- Title: Catalyst SD-WAN Control Component Compatibility Matrix — filtered ISR4000 results
- Used for: 20.12.8.1 / 17.12.x compatibility; family-level ISR4000 evidence, applied to ISR4431
- URL: <https://www.cisco.com/c/dam/en/us/td/docs/Website/enterprise/catalyst_sdwan_compatibility_matrix/index.html>
- Revision: live tool; accessed 2026-10-31 UTC.
- Locator: Controller release 20.12; IOSXE; product ISR4000; row20.12.8.1,20.12.8.2.
- Saved filtered result: [reference/isr4000-sdwan-compatibility-20.12-accessed-2026-10-31.txt](reference/isr4000-sdwan-compatibility-20.12-accessed-2026-10-31.txt) and captured JSON.

#### ISR4431-MOD-2

- Title: Cisco 4-Port, 8-Port, and8-Port with PoE/PoE+ Gigabit Ethernet LAN Switch Network Interface Modules Data Sheet.
- Used for: Exact ISR4431 switch-NIM capacity, PoE, IP Base,802.1X and MAB.
- URL: <https://www.cisco.com/c/en/us/products/collateral/routers/4000-series-integrated-services-routers-isr/data_sheet_c78-612808.html>
- Document revision: Updated 2017-11-30.
- Accessed: 2026-10-31 UTC (2026-10-30 America/Chicago); public source body read through native webpage tools, not search snippets.
- Locator: Feature table; Tables6,9,10,11.
- Local PDF: not saved; existing saved PDFs were preserved.

#### ISR4431-MOD-3

- Title: Cisco Packet Voice Digital Signal Processor Modules for Cisco Unified Communications Solutions.
- Used for: PVDM4 PIDs/slot use;4431 excludes SM-X-PVDM and NIM-PVDM.
- URL: <https://www.cisco.com/c/en/us/products/collateral/routers/4000-series-integrated-services-routers-isr/data_sheet_c78-728307.html>
- Document revision: Updated 2020-11-23.
- Accessed: 2026-10-31 UTC (2026-10-30 America/Chicago); public source body read through native webpage tools, not search snippets.
- Locator: Form factor and options; Table 1; Cisco platform availability; Table 5.
- Local PDF: not saved; existing saved PDFs were preserved.

#### ISR4431-MOD-4

- Title: Analog Voice Network Interface Modules for Cisco 4000 Series ISRs Data Sheet.
- Used for: Analog/BRI voice PIDs, own DSP, UC package and module minimum releases.
- URL: <https://www.cisco.com/c/en/us/products/collateral/routers/4000-series-integrated-services-routers-isr/datasheet-c78-733646.html>
- Document revision: Updated 2017-05-16.
- Accessed: 2026-10-31 UTC (2026-10-30 America/Chicago); public source body read through native webpage tools, not search snippets.
- Locator: Tables 1/2; Cisco IOS XE Software Release Requirements.
- Local PDF: not saved; existing saved PDFs were preserved.

#### ISR4431-MOD-5

- Title: Cisco2900,3900,and4000 Series ISR Interoperability with Cisco Unified Communications Manager Data Sheet.
- Used for: Exact ISR4431 mapping for analog, BRI voice, MFT and PRI PIDs.
- URL: <https://www.cisco.com/c/en/us/products/collateral/unified-communications/tdm-gateways/data-sheet-c78-729824.html>
- Document revision: Page revision date not recorded.
- Accessed: 2026-10-31 UTC (2026-10-30 America/Chicago); public source body read through native webpage tools, not search snippets.
- Locator: Table 3, Cisco4431 block; interoperability minima are not proof of later release recertification.
- Local PDF: not saved; existing saved PDFs were preserved.

#### ISR4431-MOD-6

- Title: Cisco Multimode VDSL2 and ADSL2/2+ Network Interface Module Data Sheet.
- Used for: DSL PIDs and exact ISR4431 platform/placement/IP Base support.
- URL: <https://www.cisco.com/c/en/us/products/collateral/routers/4000-series-integrated-services-routers-isr/datasheet-c78-733645.html>
- Document revision: Updated 2015-08-04.
- Accessed: 2026-10-31 UTC (2026-10-30 America/Chicago); public source body read through native webpage tools, not search snippets.
- Locator: Software Support; Platform Support; Tables6/7.
- Local PDF: not saved; existing saved PDFs were preserved.

#### ISR4431-MOD-7

- Title: Cisco2-and4-Port ISDN BRI S/T Network Interface Modules Data Sheet.
- Used for: Data BRI PIDs, exact ISR4431 max 3,16.6.1 minimum, IP Base.
- URL: <https://www.cisco.com/c/en/us/products/collateral/routers/4000-series-integrated-services-routers-isr/datasheet-c78-739839.html>
- Document revision: Updated 2017-10-23.
- Accessed: 2026-10-31 UTC (2026-10-30 America/Chicago); public source body read through native webpage tools, not search snippets.
- Locator: Tables4–7; distinct from voice NT/TE modules.
- Local PDF: not saved; existing saved PDFs were preserved.

#### ISR4431-MOD-8

- Title: Asynchronous Terminal Server Interface Modules for Cisco 4000 Series ISRs Data Sheet.
- Used for: Exact ISR4431 NIM16A/24A support, mode/feature limitations and minimum-release conflict.
- URL: <https://www.cisco.com/c/en/us/products/collateral/routers/4000-series-integrated-services-routers-isr/datasheet-c78-739968.html>
- Document revision: Updated 2018-01-04.
- Accessed: 2026-10-31 UTC (2026-10-30 America/Chicago); public source body read through native webpage tools, not search snippets.
- Locator: Applications; Tables2–4; current family matrix gives different minimum.
- Local PDF: not saved; existing saved PDFs were preserved.

#### ISR4431-MOD-9

- Title: Cisco 4000 Series Integrated Services Routers — Interfaces and Modules.
- Used for: Family compatibility inventory and minimum-release context; merged columns require caution.
- URL: <https://www.cisco.com/c/en/us/products/routers/4000-series-integrated-services-routers-isr/relevant-interfaces-and-modules.html>
- Document revision: Page revision not stated in the read content.
- Accessed: 2026-10-31 UTC (2026-10-30 America/Chicago); public source body read through native webpage tools, not search snippets.
- Locator: Switch, DSP, voice, broadband, serial, async, BRI and PRI sections; do not apply mixed family minima as exact basis certification.
- Local PDF: not saved; existing saved PDFs were preserved.

#### ISR4431-MOD-10

- Title: Cisco 4400 Series ISR1-,2-,and4-Port Serial Network Interface Modules Data Sheet.
- Used for: Serial PIDs/capability; original platform table names4451 only, so exact ISR4431 support is not established by this sheet.
- URL: <https://www.cisco.com/c/en/us/products/collateral/routers/4000-series-integrated-services-routers-isr/datasheet-c78-732155.html>
- Document revision: Updated 2014-07-02.
- Accessed: 2026-10-31 UTC (2026-10-30 America/Chicago); public source body read through native webpage tools, not search snippets.
- Locator: Tables 1/2 and software-support text; compare current family matrix.
- Local PDF: not saved; existing saved PDFs were preserved.

#### ISR4431-PSIRT-1

- Title: Cisco IOS XE Software Security Hardening Release: August2026.
- Used for: IOS XE-wide scope and17.12.8 first fixed release; PID applicability inferred from IOS XE scope.
- URL: <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-iosxe-V8NMuMZJ>
- Document revision: Version 1.1;2026-10-02; first 2026-08-05.
- Accessed: 2026-10-31 UTC (2026-10-30 America/Chicago); public source body read through native webpage tools, not search snippets.
- Locator: Vulnerable Products and Fixed Releases.
- Local PDF: not saved; existing saved PDFs were preserved.

#### ISR4431-PSIRT-2

- Title: Multiple Cisco Products Snort 3 Security Hardening Release: October2026.
- Used for: UTD Snort3 engine fixes and exact17.12 UTD package.
- URL: <https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-hardening-snort3-ybgmhTQe.html>
- Document revision: Version 1.1;2026-10-22; first 2026-10-21.
- Accessed: 2026-10-31 UTC (2026-10-30 America/Chicago); public source body read through native webpage tools, not search snippets.
- Locator: Affected Products and UTD on Cisco IOS XE Software fixed table.
- Local PDF: not saved; existing saved PDFs were preserved.

#### ISR4431-PSIRT-3

- Title: Multiple Cisco Products Snort 3 SMTP MIME Denial of Service Vulnerability.
- Used for: 4000-Series UTD applicability and first fixed17.12 engine package.
- URL: <https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-snort3-mime-vulns-bkXjcKkt.html>
- Document revision: Version 1.1;2026-10-22.
- Accessed: 2026-10-31 UTC (2026-10-30 America/Chicago); public source body read through native webpage tools, not search snippets.
- Locator: UTD affected-products/configuration and fixed tables.
- Local PDF: not saved; existing saved PDFs were preserved.

#### ISR4431-PSIRT-4

- Title: Multiple Cisco Products Snort 3 Denial of Service Vulnerabilities.
- Used for: 4000-Series conditional UTD scope and first fixed17.12 engine package.
- URL: <https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-snort3-misc-dos-6mB22qAK.html>
- Document revision: Version 1.1;2026-10-22.
- Accessed: 2026-10-31 UTC (2026-10-30 America/Chicago); public source body read through native webpage tools, not search snippets.
- Locator: UTD affected-products, status check and fixed tables.
- Local PDF: not saved; existing saved PDFs were preserved.

#### ISR4431-PSIRT-5

- Title: Cisco Unified Threat Defense Snort IPS Engine for Cisco IOS XE Security Policy Bypass and DoS.
- Used for: CVE-2024-20508 feature conditions, fail-open/fail-close impact and17.12.4 fix.
- URL: <https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-utd-snort3-dos-bypas-b4OUEwxD.html>
- Document revision: Version 1.0;2024-09-25.
- Accessed: 2026-10-31 UTC (2026-10-30 America/Chicago); public source body read through native webpage tools, not search snippets.
- Locator: Summary, Vulnerable Products and Fixed Software.
- Local PDF: not saved; existing saved PDFs were preserved.

#### ISR4431-PSIRT-6

- Title: Cisco Secure Boot Hardware Tampering Vulnerability.
- Used for: CVE-2019-1649 exact ISR4431 firmware utility and elevated local attack requirements.
- URL: <https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-20190513-secureboot.html>
- Document revision: First2019-05-13; current revision date not recorded.
- Accessed: 2026-10-31 UTC (2026-10-30 America/Chicago); public source body read through native webpage tools, not search snippets.
- Locator: Summary and Vulnerable Products, Cisco4431 row.
- Local PDF: not saved; existing saved PDFs were preserved.

#### ISR4431-FN-1

- Title: FN72510 — Weak Cryptographic Algorithms Are Not Allowed by Default for IPsec.
- Used for: ISR4000 default behavior from17.11.1a and configuration implications.
- URL: <https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72510.html>
- Document revision: Version 1.5;2026-01-20.
- Accessed: 2026-10-31 UTC (2026-10-30 America/Chicago); public source body read through native webpage tools, not search snippets.
- Locator: Workaround/Solution enterprise-routing table.
- Local PDF: not saved; existing saved PDFs were preserved.

#### ISR4431-FN-2

- Title: FN72578 — Smart Licensing Using Policy Might Cause High CPU/Memory Usage.
- Used for: RUM accumulation in disconnected operations and published fixed branches.
- URL: <https://www.cisco.com/c/en/us/support/docs/field-notices/725/fn72578.html>
- Document revision: Updated 2023-09-29.
- Accessed: 2026-10-31 UTC (2026-10-30 America/Chicago); public source body read through native webpage tools, not search snippets.
- Locator: Problem Description, Workaround/Solution and exact ISR4431 affected-products list.
- Local PDF: not saved; existing saved PDFs were preserved.

#### ISR4431-FN-3

- Title: FN72323 — QuoVadis Root CA2 Decommission.
- Used for: Affected services, trust-root update paths and scope of old reservation exemption.
- URL: <https://www.cisco.com/c/en/us/support/docs/field-notices/723/fn72323.html>
- Document revision: Updated 2023-10-05.
- Accessed: 2026-10-31 UTC (2026-10-30 America/Chicago); public source body read through native webpage tools, not search snippets.
- Locator: Workaround/Solution, Software Upgrade and4431 affected-products entry.
- Local PDF: not saved; existing saved PDFs were preserved.

#### ISR4431-FN-4

- Title: FN74350 — CUBE TLS Certificate EKU Changes.
- Used for: Exact ISR4431 exposure,26.1.1 solution unavailable to ISR4000, older-release EKU conditions.
- URL: <https://www.cisco.com/c/en/us/support/docs/field-notices/743/fn74350.html>
- Document revision: Version 2.0;2026-06-23.
- Accessed: 2026-10-31 UTC (2026-10-30 America/Chicago); public source body read through native webpage tools, not search snippets.
- Locator: Products Affected and Workaround/Solution note and Option 4.
- Local PDF: not saved; existing saved PDFs were preserved.

#### ISR4431-EOL-6

- Title: End-of-Sale and End-of-Life Announcement for Cisco LAN Switch Network Interface Modules (EOL15562).
- Used for: NIM-ES2-8/-8-P chassis/module lifecycle and orderability distinction.
- URL: <https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/network-modules/lan-switch-network-interface-modules-eol.html>
- Revision: updated 2024-12-05.
- Accessed: 2026-10-31 UTC (2026-10-30 America/Chicago); public source body read.
- Locator: Tables 1 and2.
- Local PDF: not saved.

#### ISR4431-EOL-7

- Title: End-of-Sale and End-of-Life Announcement for Cisco Switch Module for Modular Platforms (EOL15584, amended).
- Used for: NIM-ES2-4 lifecycle and orderability.
- URL: <https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/network-modules/switch-modular-platform-eol.html>
- Revision: updated 2025-01-23; announcement2025-01-16.
- Accessed: 2026-10-31 UTC (2026-10-30 America/Chicago); public source body read.
- Locator: Tables 1 and2.
- Local PDF: not saved.

#### ISR4431-CFG-9

- Title: Software-Defined Access Macro Segmentation Deployment Guide.
- Used for: exact ISR4431 VRF-Lite deployment evidence at16.12.2t; not a17.12.8 certification or license-tier source.
- URL: <https://www.cisco.com/c/en/us/td/docs/solutions/CVD/Campus/cisco-sda-macro-segmentation-deploy-guide.html>
- Revision: updated 2020-08-04.
- Accessed: 2026-10-31 UTC (2026-10-30 America/Chicago); public source body read.
- Locator: Process 9, fusion-device VRF-Lite/BGP procedures and Appendix 1 (ISR4431/K9,16.12.2t).
- Local PDF: not saved.

### References - unresolved

The public module and selected advisory follow-up was completed. Remaining
items below are evidence/access gaps, not required sections left unattempted.

Inaccessible or unreadable URLs:

| URL | Accessed | Reason | Expected content | Affected claims |
| --- | --- | --- | --- | --- |
| https://www.cisco.com/c/en/us/td/docs/interfaces_modules/transceiver_modules/compatibility/matrix/GE_comp_matrix.html | 2026-10-30 | HTTP 404 (re-checked 2026-10-30 with a headless browser: still 404) | legacy GE SFP compatibility matrix | copper SFP speeds, DOM |

Required claims with no source found:

- Which DNA tier (Essentials vs. Advantage) entitles IPsec, NAT, QoS,
  VRF-Lite on ISR 4000 in autonomous mode.
- `license boot level` syntax for ISR 4000 at 17.12.
- Release dates of the IOS XE17.12.8 and17.9.10 chassis images (separate from UTD package release/fix dates).
- Original announcement date of the ISR4431; product release 2014-09-30 is documented by SUP-1.
- IPsec throughput with HSEC, SD-WAN throughput, routing/NAT/tunnel scale.
- `service unsupported-transceiver` and Cisco's third-party optics policy for
  this platform.
- Exact 17.12.8/mode certification and current orderability for every listed module PID; chassis compatibility alone is insufficient.
- Exact serial-NIM4431/release applicability where the original data sheet names only 4451 and current matrix uses merged family columns; async module minimum16.3.1 versus16.4.1 conflict remains.
- Controller-mode 802.1X/MAB configuration on NIM-ES2; autonomous module capability is now documented.
- Heat dissipation (BTU/hr).
