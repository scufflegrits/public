# Cisco Router Comparison and Recommendation (r1.1.0)

Comparison file 5 of 5 for `request-cisco-comparison-r1.1.0.md`. Built only
from the four model files and the sources registered in them; it adds no new
factual sources. Citations link to the source-register entry in the model file
that holds it (`<model file>#<tag>`), or to a section of that file.

Model files feeding this comparison:

| # | Model (confirmed PID) | File | File run status |
| --- | --- | --- | --- |
| 1 | `ISR4431/K9` | [research-cisco-isr4431-r1.1.0.md](research-cisco-isr4431-r1.1.0.md) | Complete |
| 2 | `C8300-1N1S-4T2X` | [research-cisco-c8300-1n1s-4t2x-r1.1.0.md](research-cisco-c8300-1n1s-4t2x-r1.1.0.md) | Complete |
| 3 | `C8375-E-G2` | [research-cisco-c8375-e-g2-r1.1.0.md](research-cisco-c8375-e-g2-r1.1.0.md) | Complete |
| 4 | `C8300-1N1S-6T` | [research-cisco-c8300-1n1s-6t-r1.1.0.md](research-cisco-c8300-1n1s-6t-r1.1.0.md) | Complete |

## Research status

| Item | Status |
| --- | --- |
| Revision | r1.1.0; 2026-10-30 America/Chicago (continuation access dates recorded separately). Review corrections and completion of previously unattempted public-source work. |
| Research cutoff date | 2026-10-30 America/Chicago. Original access dates are 2026-10-30; completion research additionally accessed sources on 2026-10-31 UTC (still 2026-10-30 America/Chicago). Registers retain actual access dates. |
| Basis — `ISR4431/K9` | IOS XE 17.12.8, autonomous mode. Cisco-recommended ("17.9.10 or 17.12.8"); 17.12.x is Cisco's documented last train for this platform. |
| Basis — `C8300-1N1S-4T2X` | IOS XE 17.15.6, autonomous mode. Cisco-recommended ("17.12.8 or 17.15.6" for Catalyst 8300); 17.15.6 chosen because 17.12.x maintenance ended 2026-03-30. |
| Basis — `C8375-E-G2` | IOS XE 17.15.5, autonomous mode. Cisco-suggested release on the Software Download page ("Suggested Release", from a user-supplied screenshot; applicability to this PID inferred). 17.15.6 is the first fixed 17.15.x release for the August 2026 hardening advisory. SLR, `C-NIM-WAN-2X/4S`, CUBE/SRST, voice modules, and built-in ZR optics need 17.18.x or 26.x, above this basis. |
| Basis — `C8300-1N1S-6T` | IOS XE 17.15.6, autonomous mode. Cisco-recommended (same document as model 2). |
| Run status | **Complete, with explicit evidence gaps.** The four model reviews, selected public-source security and controller checks, and management-platform deployment/licensing/offline research are complete. The review is not an exhaustive CVE assessment; vendor-only, account-gated, and hardware/serial-specific checks remain explicit follow-ups. |
| Major change from the request | Cisco bulletin **EOL15950** (announced 2026-07-27, amended 2026-10-19) puts **both** `C8300-1N1S-4T2X` and `C8300-1N1S-6T` on End-of-Sale **2027-01-31** and names `C8375-E-G2` as their migration product. The request's pre-check showed both as current. |
| Not attempted (this file) | No new research in the comparison itself; the request requires gaps to be researched in the model files first. Gaps exposed here are listed in [Open questions](#open-questions). |

## Contents

- [Research status](#research-status)
- [Summary](#summary)
- [Side-by-side tables](#side-by-side-tables)
  - [Lifecycle](#lifecycle)
  - [Hardware, power, and security hardware](#hardware-power-and-security-hardware)
  - [Ports and slots](#ports-and-slots)
  - [Performance](#performance)
  - [Software basis and ceiling](#software-basis-and-ceiling)
  - [Licensing overview](#licensing-overview)
  - [Module families](#module-families)
- [Licensing comparison](#licensing-comparison)
  - [Entitlement per capability](#entitlement-per-capability)
  - [Throughput needed at representative WAN bandwidths (illustrative)](#throughput-needed-at-representative-wan-bandwidths-illustrative)
- [Feature and ISE comparison](#feature-and-ise-comparison)
  - [Feature matrix](#feature-matrix)
  - [ISE integration](#ise-integration)
- [Offline licensing comparison](#offline-licensing-comparison)
- [Management options](#management-options)
- [Optics comparison](#optics-comparison)
  - [Minimum set](#minimum-set)
  - [Copper SFPs](#copper-sfps)
  - [Policy, DOM, and faster ports](#policy-dom-and-faster-ports)
- [Module comparison](#module-comparison)
- [Lifecycle and risk](#lifecycle-and-risk)
- [Decision matrix](#decision-matrix)
  - [Hard requirements](#hard-requirements)
  - [Weighted scoring (illustrative)](#weighted-scoring-illustrative)
  - [Evidence coverage](#evidence-coverage)
  - [Sensitivity](#sensitivity)
- [Deployment inputs to confirm](#deployment-inputs-to-confirm)
- [Open questions](#open-questions)
- [References](#references)

## Summary

**Multicast Service Reflection:** Cisco release notes document Unicast-to-Multicast Destination Reflection for ISR 4000 and Catalyst 8300 families from IOS XE 17.9.1a. This supports the ISR4431/K9 and both Catalyst 8300 PIDs at family/release-note level. Cisco’s current 8000 Series Secure Routers license matrix explicitly includes MSR under Routing Advantage, documenting C8375-E-G2 entitlement; exact runtime validation for that PID/release remains absent. The cited configuration examples use autonomous IOS XE CLI. Controller-mode MSR is not documented in the sources reviewed. Sources reviewed 2026-11-01: [ISR 4000 release notes](https://www.cisco.com/c/en/us/td/docs/routers/access/4400/release/xe-17-9/isr4k-rel-notes-xe-17-9.html), [Catalyst 8200/8300 release notes](https://www.cisco.com/c/en/us/td/docs/routers/cloud_edge/c8300/rel_notes/17_9_x/cat8200-and-8300-rel-notes-xe-17-9-x.html), [secure-router license matrix](https://www.cisco.com/c/m/en_us/products/software/wan-routing-licensing-feature-matrix.html), [Catalyst 8000 MSR licensing note](https://www.cisco.com/c/en/us/support/docs/ip/protocol-independent-multicast-sparse-mode-pim-sm/221125-configure-and-troubleshoot-multicast-ser.html), and the [IOS XE 17.x guide](https://www.cisco.com/c/en/us/td/docs/routers/ios-xe/ip-multicast/ip-multicast/m_imc_service_reflect-0.html).

**Recommendation for a new multi-site purchase: the `C8375-E-G2`, subject to
three confirmations.** It is the only one of the four with no End-of-Sale
notice, and it is Cisco's named migration product for both Catalyst 8300
models. It has built-in 2 × 1G/10G SFP+ plus 4 × 2.5G mGig RJ-45 and no
throughput tiers or HSECK9 to manage. Its Cisco-suggested release, IOS XE
17.15.5, is on a train past End-of-Sale whose maintenance ends 2027-03-30, so
the deployment must plan a move to 17.18.x or 26.x. The three confirmations:

1. Cisco approves **Specific License Reservation (SLR)** for the deployment,
   and states what happens when a reserved term license ends. SLR needs IOS
   XE 17.18.1a or later, above the suggested release. On 17.15.x the offline
   method is periodic Smart Licensing file exchange at a cadence not stated
   for this platform.
1. A **release choice** is accepted. Cisco suggests 17.15.5, but the 2026-08
   security advisory's first fixed 17.15.x release is 17.15.6, and SLR, the
   C8375-only WAN NIMs, CUBE/SRST, voice modules, and built-in ZR optics all
   need 17.18.x or 26.x.
1. The **module needs** fit its documented list. PVDM is documented
   unsupported. C-NIM-1X, C-NIM-2T, NIM-ES2 and UCS-E support was not
   verified from C8375 module lists; absence does not prove non-support.
   Voice uses vDSP from 17.18.2, with analog modules from 26.1.

The `C8300-1N1S-4T2X` scores slightly higher in the illustrative matrix (75
vs 72) now that the C8375-E-G2 is scored at its suggested 17.15.5 release. It
is the fallback only if every site's units can be ordered before **2027-01-31** and
the shorter support runway (Last Date of Support 2032-01-31) is acceptable. It
has the more mature software position (a Cisco-recommended release) and the
broader module list. The `C8300-1N1S-6T` has the same End-of-Sale date, a
2 Gbps licensed crypto ceiling, and 10G only through modules. The `ISR4431/K9`
is a reference baseline only: End-of-Sale since 2023-11-07, so it can't be
bought new. Throughput is TBD, so tier sizing stays conditional. See
[Throughput needed at representative WAN bandwidths](#throughput-needed-at-representative-wan-bandwidths-illustrative).

## Side-by-side tables

Column order follows the request. "Unknown" = not established in the model
file; "n/a" = not applicable; "documented unsupported" = a source says no.

### Lifecycle

| Milestone | `ISR4431/K9` (baseline) | `C8300-1N1S-4T2X` | `C8375-E-G2` | `C8300-1N1S-6T` |
| --- | --- | --- | --- | --- |
| Launch | unknown | Series release 2020-10-19 | Series release 2025-06-09 | Series release (same series as model 2) |
| End-of-Life Announcement | 2022-11-07 (EOL14896) | 2026-07-27 (EOL15950) | none found as of 2026-10-30 | 2026-07-27 (EOL15950) |
| End-of-Sale | **2023-11-07 (passed)** | **2027-01-31** | n/a | **2027-01-31** |
| End of SW Maintenance Releases | 2025-08-31 | 2031-03-30 | n/a | 2031-03-30 |
| End of Vulnerability/Security Support | 2028-11-30 | 2032-01-31 | n/a | 2032-01-31 |
| Last Date of Support | 2028-11-30 | 2032-01-31 | n/a | 2032-01-31 |
| Cisco replacement | `C8300-1N1S-4T2X` or `C8300-1N1S-6T` | `C8375-E-G2` | n/a | `C8375-E-G2` |
| Orderable new on 2026-10-30 | **No** | Yes, until 2027-01-31 | Yes | Yes, until 2027-01-31 |
| Sources | [ISR4431-EOL-1](research-cisco-isr4431-r1.1.0.md#isr4431-eol-1) | [C8300-4T2X-EOL-1](research-cisco-c8300-1n1s-4t2x-r1.1.0.md#c8300-4t2x-eol-1), [C8300-4T2X-SUP-1](research-cisco-c8300-1n1s-4t2x-r1.1.0.md#c8300-4t2x-sup-1) | [C8375-SUP-1](research-cisco-c8375-e-g2-r1.1.0.md#c8375-sup-1) | [C8300-6T-EOL-1](research-cisco-c8300-1n1s-6t-r1.1.0.md#c8300-6t-eol-1) |

The `C8300-1N1S-6T` file records the series release date only through the
shared Catalyst 8300 support page in model 2. Accessory note: the C8300 PoE
power supply `PWR-CC1-500WAC` is in the same End-of-Sale notice, with no
migration product.

### Hardware, power, and security hardware

| Item | `ISR4431/K9` | `C8300-1N1S-4T2X` | `C8375-E-G2` | `C8300-1N1S-6T` |
| --- | --- | --- | --- | --- |
| Form factor | 1RU | 1RU | 1RU | 1RU |
| Dimensions (H × W × D) | 1.73 × 17.25 × 19.97 in | 1.73 × 17.50 × 16.25 in | 1.73 × 17.5 × 16.25 in | 1.73 × 17.50 × 16.25 in |
| Weight | 18.5 lb (AC PSU, no modules) | 20 lb (2 AC PSUs, fan tray) | 14.3 lb (dual AC PSUs, fan tray) | 20 lb (2 AC PSUs, fan tray) |
| CPU | Multicore; count not disclosed | 8-core x86 SoC | 16-core Cisco "secure networking processor" | 8-core (**inferred**) |
| DRAM default / max | 4 GB / 16 GB control plane; 2 GB data plane | 8 GB / 32 GB | 16 GB / 32 GB DDR5 (single DIMM) | 8 GB / 32 GB |
| Storage | 8 GB flash (max 32 GB) | 8 GB onboard + 16 GB M.2 USB; up to 2 TB NVMe | 16 GB; M.2 options to 2 TB SED | 8 GB onboard + 16 GB M.2 USB; up to 2 TB NVMe |
| PSUs | AC, DC, PoE AC; dual hot-swap | Dual hot-swap; 250 W AC default; 500 W AC+PoE; 400 W DC | Two bays; 400 W AC default; 760 W AC+PoE; 500 W DC | Dual hot-swap; 250 W AC default; 500 W AC+PoE; 400 W DC |
| PoE budget | 250 W (500 W Boost) to modules; no front-panel PoE | 250 W redundant active/standby; **500 W dual-PSU active/active Boost without redundancy** | 360 W per 760 W PSU; 720 W Boost with two; UPOE+ on two built-in ports | 250 W redundant active/standby; **500 W dual-PSU active/active Boost without redundancy** |
| Typical power (no modules) | 65 W | 245 W | 55 W | 82 W |
| Max power / heat | Published maxima without PoE: **250 W AC / 437 W DC**; heat unknown | unknown | unknown | unknown |
| Operating temperature | 0–40 °C | 0–40 °C | 0–40 °C to 10,000 ft; 0–45 °C to 6,000 ft | 0–40 °C |
| Secure boot / trust | Hardware secure boot; tamper-proof authentication silicon | Secure Boot, SUDI; TPM not named | Secure Boot, SUDI, tamper detection; TPM not named | Secure Boot, SUDI; TPM not named |
| Crypto hardware | Embedded IPsec acceleration (family) | Intel QAT | In the SoC | Crypto acceleration (family statement) |
| Sources | [ISR4431-DS-1](research-cisco-isr4431-r1.1.0.md#isr4431-ds-1), [ISR4431-HIG-1](research-cisco-isr4431-r1.1.0.md#isr4431-hig-1) | [C8300-4T2X-DS-1](research-cisco-c8300-1n1s-4t2x-r1.1.0.md#c8300-4t2x-ds-1), [C8300-4T2X-WP-1](research-cisco-c8300-1n1s-4t2x-r1.1.0.md#c8300-4t2x-wp-1) | [C8375-DS-1](research-cisco-c8375-e-g2-r1.1.0.md#c8375-ds-1), [C8375-HIG-1](research-cisco-c8375-e-g2-r1.1.0.md#c8375-hig-1) | [C8300-6T-DS-1](research-cisco-c8300-1n1s-6t-r1.1.0.md#c8300-6t-ds-1), [C8300-6T-OG-1](research-cisco-c8300-1n1s-6t-r1.1.0.md#c8300-6t-og-1) |

Typical-power note: the Catalyst 8300 datasheet's Table 11 prints 245 W for
the `C8300-1N1S-4T2X` and 82 W for the `C8300-1N1S-6T`, both "no modules,
single PSU" (checked against the saved PDF during reconciliation). The two
share a chassis, and Cisco gives no reason for the difference. Treat both as
documented but **verify with Cisco** before sizing power or cooling. PSU
ratings are capacity, not draw.

### Ports and slots

| Item | `ISR4431/K9` | `C8300-1N1S-4T2X` | `C8375-E-G2` | `C8300-1N1S-6T` |
| --- | --- | --- | --- | --- |
| Built-in copper | 4 × 10/100/1000 RJ-45 (dual-mode with SFP) | 4 × 10/100/1000 RJ-45 | 4 × 100M/1G/2.5G mGig RJ-45 (no 10M documented) | 4 × 10/100/1000 RJ-45 |
| Built-in SFP | Same 4 ports in SFP mode (one medium at once) | 2 × SFP+ (1G or 10G) | 2 × SFP/SFP+ (1G or 10G) | 2 × SFP (1G only) |
| Built-in 10G | none | 2 | 2 | **none** |
| Ports faster than 10G | none | none | none | none |
| Management Ethernet | Yes (GE0) | **No dedicated out-of-band port; in-band only** | Yes (1G RJ-45 OOB) | **No dedicated out-of-band port; in-band only** |
| NIM / SM / PIM slots | 3 NIM + 1 ISC (PVDM4); **0 SM-X; 0 PIM** | 1 / 1 (single-wide) / 1; up to 3 NIMs with adapter | 1 / 1 (single-wide) / 1 | 1 / 1 (single-wide) / 1; up to 3 NIMs with adapter |
| Cellular (PIM) | n/a (no PIM) | available, not assessed | available, not assessed | available, not assessed |

Sources: [ISR4431-DS-1](research-cisco-isr4431-r1.1.0.md#isr4431-ds-1);
[C8300-4T2X-HIG-1](research-cisco-c8300-1n1s-4t2x-r1.1.0.md#c8300-4t2x-hig-1),
[C8300-4T2X-OG-1](research-cisco-c8300-1n1s-4t2x-r1.1.0.md#c8300-4t2x-og-1);
[C8375-HIG-1](research-cisco-c8375-e-g2-r1.1.0.md#c8375-hig-1),
[C8375-DS-1](research-cisco-c8375-e-g2-r1.1.0.md#c8375-ds-1);
[C8300-6T-HIG-1](research-cisco-c8300-1n1s-6t-r1.1.0.md#c8300-6t-hig-1),
[C8300-6T-OG-1](research-cisco-c8300-1n1s-6t-r1.1.0.md#c8300-6t-og-1).
The ISR4431 file corrects the request: the chassis datasheet shows no SM-X
slot.
C8300 out-of-band management and PoE-mode corrections trace to
[C8300-4T2X-FAQ-1](research-cisco-c8300-1n1s-4t2x-r1.1.0.md#c8300-4t2x-faq-1)
and [C8300-4T2X-SMSW-1](research-cisco-c8300-1n1s-4t2x-r1.1.0.md#c8300-4t2x-smsw-1),
Tables 2–3 and Security feature support.

### Performance

**Not directly comparable across platforms.** The ISR4431 figures have no
packet size. The Catalyst 8300 figures are at 1400 bytes or IMIX. The
C8375-E-G2 figures are at 512 bytes. Release, cipher, tunnel count, and
direction are mostly not disclosed. Values are shown with their conditions and
are not ranked or scored.

| Metric (Cisco "up to") | `ISR4431/K9` | `C8300-1N1S-4T2X` | `C8375-E-G2` | `C8300-1N1S-6T` |
| --- | --- | --- | --- | --- |
| Forwarding | 500 Mbps / 1 Gbps aggregate (licensed); boost CEF "over 4 Gbps" vs "3.4 Gbps" (conflict) | 19.7 Gbps IPv4, 1400 B | 38 Gbps, 512 B | 19.7 Gbps IPv4, 1400 B |
| IPsec | not found | 16.9 Gbps (1400 B); 6.6 Gbps (IMIX 352 B) | 20 Gbps (512 B); FAQ says 30 Gbps (conflict) | 1.9 Gbps (1400 B); 1.9 Gbps (IMIX) |
| SD-WAN IPsec | not found | 17 Gbps (1400 B); 6.3 Gbps (IMIX) | 12 Gbps (512 B, with IPsec+QoS+DPI+FNF) | 2 Gbps (1400 B); 1.8 Gbps (IMIX) |
| Services (DIA + NGFW/IPS/URLF/AMP) | not found | 2.9 Gbps, firewall EMIX, controller, 17.12.2 | 7 Gbps "Threat Protection", EMIX, mode n/d | 2.1 Gbps, firewall EMIX, controller, 17.12.2 |
| Licensed crypto ceiling | 250 Mbps without HSEC; with HSEC actual maximum **not verified**; 1 Gbps is the PERF tier, Boost removes the aggregate shaper | T3 = 20 Gbps aggregate with HSECK9 | Advantage: unthrottled after reload at 17.15.5; authorization required for applicable Day-0 states from 17.18.1a | T2 = **2 Gbps aggregate**, maximum for PID |
| IPsec tunnels | 1,000 without HSEC; with HSEC unknown | 4,000 SVTI (1,000 without HSECK9) | 3,500 (4,000 from 26.2.1) | 4,000 SVTI (1,000 without HSECK9) |
| Routes / NAT sessions | unknown / unknown | 1.6M–4M / 1.2M–2M (DRAM-dependent) | 2M / 1.5M | 1.6M–4M / 1.2M–2M |

Sources: [ISR4431-DS-1](research-cisco-isr4431-r1.1.0.md#isr4431-ds-1);
[C8300-4T2X-DS-1](research-cisco-c8300-1n1s-4t2x-r1.1.0.md#c8300-4t2x-ds-1)
Tables 3–6, [C8300-4T2X-LIC-1](research-cisco-c8300-1n1s-4t2x-r1.1.0.md#c8300-4t2x-lic-1);
[C8375-DS-1](research-cisco-c8375-e-g2-r1.1.0.md#c8375-ds-1) Table 6,
[C8375-FAQ-1](research-cisco-c8375-e-g2-r1.1.0.md#c8375-faq-1),
[C8375-LIC-1](research-cisco-c8375-e-g2-r1.1.0.md#c8375-lic-1);
[C8300-6T-DS-1](research-cisco-c8300-1n1s-6t-r1.1.0.md#c8300-6t-ds-1),
[C8300-6T-LIC-1](research-cisco-c8300-1n1s-6t-r1.1.0.md#c8300-6t-lic-1)
Table 6.

The C8300 tier values (T1 = 500M aggregate with HSECK9, T2 = 2G aggregate,
T3 = 20G aggregate, at 17.14.1a and later) come from the platform licensing
guide's Tables 5–6, checked against the saved PDF during reconciliation. Other
Cisco documents give different tier sizes; both C8300 files record the
conflict and use the platform guide. A C8375-E-G2 UTD regression (CSCww15035:
about 700 Mbps on 26.1/26.2 vs 3.2 Gbps on 17.18.x) is listed as resolved in
26.2.x without a recorded fixed-in release.

### Software basis and ceiling

| Item | `ISR4431/K9` | `C8300-1N1S-4T2X` | `C8375-E-G2` | `C8300-1N1S-6T` |
| --- | --- | --- | --- | --- |
| Cisco-recommended release | 17.9.10 or 17.12.8 | 17.12.8 or 17.15.6 | **17.15.5** (download-page "Suggested Release") | 17.12.8 or 17.15.6 |
| Basis used | 17.12.8 | 17.15.6 | 17.15.5 (below the advisory's first fix, 17.15.6) | 17.15.6 |
| Newest available | 17.12.8 | 26.2.1 | 26.2.1 | 26.2.1 |
| Documented ceiling | **17.12.x** (last train) | **28.2.x** (last train, EOL15950) | none documented | **28.2.x** |
| Basis train support | 17.12.x maintenance ended 2026-03-30; security support to 2027-09-30 | 17.15.x maintenance to 2027-03-30; security support to 2028-09-30 | as model 2 (17.15.x); 26.x: 48 months sustaining from GA | as model 2 |
| Minimum release | n/a | 17.3.2 | 17.15.3 | 17.3.2 |
| Controller mode | Yes (17.12.x; SD-WAN Manager 20.12/20.15/20.18) | Yes (same image) | Yes (min. SD-WAN Manager 20.15.3); also SD-Routing | Yes (same image) |
| Mode change | — | Autonomous → controller erases config | Autonomous → controller erases startup config | — |

Sources: [ISR4431-REL-1](research-cisco-isr4431-r1.1.0.md#isr4431-rel-1),
[ISR4431-REL-3](research-cisco-isr4431-r1.1.0.md#isr4431-rel-3),
[ISR4431-EOL-3](research-cisco-isr4431-r1.1.0.md#isr4431-eol-3);
[C8300-4T2X-REC-1](research-cisco-c8300-1n1s-4t2x-r1.1.0.md#c8300-4t2x-rec-1),
[C8300-4T2X-EOL-3](research-cisco-c8300-1n1s-4t2x-r1.1.0.md#c8300-4t2x-eol-3);
[C8375-SWD-1](research-cisco-c8375-e-g2-r1.1.0.md#c8375-swd-1),
[C8375-REL-1](research-cisco-c8375-e-g2-r1.1.0.md#c8375-rel-1),
[C8375-REL-2](research-cisco-c8375-e-g2-r1.1.0.md#c8375-rel-2),
[C8375-EOL-2](research-cisco-c8375-e-g2-r1.1.0.md#c8375-eol-2),
[C8375-SWLC-1](research-cisco-c8375-e-g2-r1.1.0.md#c8375-swlc-1),
[C8375-SCG-1](research-cisco-c8375-e-g2-r1.1.0.md#c8375-scg-1);
[C8300-6T-RR-1](research-cisco-c8300-1n1s-6t-r1.1.0.md#c8300-6t-rr-1),
[C8300-6T-EOL-1](research-cisco-c8300-1n1s-6t-r1.1.0.md#c8300-6t-eol-1).

### Licensing overview

| Layer | `ISR4431/K9` | `C8300-1N1S-4T2X` / `C8300-1N1S-6T` | `C8375-E-G2` |
| --- | --- | --- | --- |
| Base / feature tiers | Legacy packages (ipbasek9, appxk9, securityk9, uck9) still shown under SLP; DNA Essentials/Advantage with perpetual Network tiers | DNA Essentials or Advantage (3/5/7-year) including perpetual Network Essentials/Advantage; or Catalyst Routing Essentials (7-year, autonomous only) | OS Essentials (perpetual, preloaded); Routing Advantage (84-month subscription) or OS Advantage (perpetual); WAN Essentials/Advantage for SD-WAN/SD-Routing |
| Throughput | 500 Mbps default; 1 Gbps performance license; boost (CEF) | Numeric/tier licenses; 4T2X up to T3 (20G agg.), 6T up to T2 (2G agg.) | No bandwidth tiers |
| Export-controlled crypto | HSECK9 (ISR4K-HSECK9 / DNA-HSEC from 17.6.1) | HSECK9 (`C8000-HSEC`, included with DNA); SLAC needed | HSECK9 **not applicable, not required** |
| Security add-ons | Security license for UTD | UTD IPS/IDS: DNA Essentials or Advantage (family matrix; PID tier inference); AMP/URLF via SD-Routing | Threat (`LIC-SEC-L-T`); URL Filtering and Malware Defense via SD-WAN Manager only |
| Reporting mechanism | SLP (from 17.3.2) | SLP | SLP; also SLR; OS Essentials needs no reporting |
| Orderable now | No (all End-of-Sale) | Yes, with the chassis until 2027-01-31 | Yes |

Sources: [ISR4431-LIC-1](research-cisco-isr4431-r1.1.0.md#isr4431-lic-1),
[ISR4431-LIC-2](research-cisco-isr4431-r1.1.0.md#isr4431-lic-2);
[C8300-4T2X-LIC-1](research-cisco-c8300-1n1s-4t2x-r1.1.0.md#c8300-4t2x-lic-1),
[C8300-4T2X-OG-1](research-cisco-c8300-1n1s-4t2x-r1.1.0.md#c8300-4t2x-og-1),
[C8300-4T2X-DNA-2](research-cisco-c8300-1n1s-4t2x-r1.1.0.md#c8300-4t2x-dna-2),
[C8300-6T-LIC-1](research-cisco-c8300-1n1s-6t-r1.1.0.md#c8300-6t-lic-1);
[C8375-LIC-1](research-cisco-c8375-e-g2-r1.1.0.md#c8375-lic-1),
[C8375-OG-1](research-cisco-c8375-e-g2-r1.1.0.md#c8375-og-1).

### Module families

| Family | `ISR4431/K9` | `C8300-1N1S-4T2X` / `C8300-1N1S-6T` | `C8375-E-G2` |
| --- | --- | --- | --- |
| NIM | 3 slots; GE, MFT T1/E1, voice NIMs | 1 slot (3 with `C-SM-NIM-ADPT`); `C-NIM-1X`, `C-NIM-4X`, `C-NIM-2T`, `C-NIM-1M`, `C-NIM-8T/8M`, `NIM-ES2-*`, voice, serial, DSL | 1 slot; `C-NIM-4X`, `C-NIM-8T/8M`, `C-NIM-WAN-2X/4S` (C8375 only), voice (26.1+), serial; DSL to 17.18.1 only |
| SM | none | 1 single-wide: `C-SM-16P4M2X`, `C-SM-NIM-ADPT`, SM-X voice/PVDM, UCS-E (model 2 lists older UCS-E M2 as absent) | 1 single-wide: `C-SM-16P4M2X`, `C-SM-NIM-ADPT`, SM-X voice; UCS-E not on lists (conflicts with FAQ text) |
| DSP | PVDM4 in ISC slot | `NIM-PVDM-*`, `SM-X-PVDM-*` | **PVDM documented unsupported**; vDSP (software) from 17.18.2 |
| PIM (cellular) | none | available, not assessed | available, not assessed |
| Memory | `MEM-4400-*` (End-of-Sale) | `MEM-C8300-16GB/32GB` | `MEM-C83G2-16GB/32GB` (platform-specific) |

Sources: [ISR4431-DS-1](research-cisco-isr4431-r1.1.0.md#isr4431-ds-1),
[ISR4431-DS-3](research-cisco-isr4431-r1.1.0.md#isr4431-ds-3);
[C8300-4T2X-OG-1](research-cisco-c8300-1n1s-4t2x-r1.1.0.md#c8300-4t2x-og-1),
[C8300-4T2X-DS-1](research-cisco-c8300-1n1s-4t2x-r1.1.0.md#c8300-4t2x-ds-1);
[C8300-6T-DS-1](research-cisco-c8300-1n1s-6t-r1.1.0.md#c8300-6t-ds-1);
[C8375-OG-1](research-cisco-c8375-e-g2-r1.1.0.md#c8375-og-1),
[C8375-FAQ-1](research-cisco-c8375-e-g2-r1.1.0.md#c8375-faq-1),
[C8375-C83DS-1](research-cisco-c8375-e-g2-r1.1.0.md#c8375-c83ds-1).

## Licensing comparison

### Entitlement per capability

Similar tier names don't prove equivalent features. The C8375-E-G2's
"Essentials/Advantage" licenses are a different licensing model from the
Catalyst 8300's DNA/Network tiers. "Not verified" means the model file could
not map the feature to a tier. For the C8300s, tiers come from Cisco's DNA
routing matrix ([C8300-4T2X-MX-1](research-cisco-c8300-1n1s-4t2x-r1.1.0.md#c8300-4t2x-mx-1)), read from the page code with a headless browser. It
names no platforms, so applying it to these PIDs is **inferred**. Columns:
Routing Essentials (RE), DNA/Network Essentials (DE), DNA/Network Advantage
(DA).

| Capability (autonomous unless noted) | `ISR4431/K9` | `C8300-1N1S-4T2X` / `C8300-1N1S-6T` | `C8375-E-G2` |
| --- | --- | --- | --- |
| Base routing, NAT, QoS, VRF-Lite | ipbasek9 / Network Essentials; per-feature tier **not verified** | RE, DE, or DA (all three); carrier-grade NAT and NBAR2 custom packs DA only | OS Essentials |
| Point-to-point IPsec | securityk9 (**inferred**); HSECK9 above 250 Mbps | RE, DE, or DA; HSECK9 above 250 Mbps / 1,000 tunnels | OS Essentials (250 Mbps aggregate cap) |
| DMVPN / FlexVPN / GETVPN | securityk9 (family) | DE or DA (not RE) | Routing Advantage / OS Advantage |
| Zone-based / application firewall | security license | RE, DE, or DA ("L3-L7 firewall") | L3/L4 in Essentials; L7 in Advantage |
| UTD (IPS, URLF, AMP) | security license; 8 GB DRAM (12 GB High profile) | IPS/IDS: DE or DA (not RE). AMP/URLF: "Supported only with SD-Routing" | Threat add-on via CLI; URLF/AMP add-ons need SD-WAN Manager |
| MPLS L3VPN | not verified | DNA / Network Advantage | Routing Advantage / OS Advantage |
| TrustSec (SGT, SXP, SGACL) | IP Base/K9; SG firewall needs Security/K9 | **Conflict:** Network Advantage (GBP matrix) vs. all three tiers (DNA routing matrix); DA assumed | Routing Advantage / OS Advantage |
| CUBE | DNA Essentials (basic) / uck9 | `A-FLEX-3` + DNA Essentials minimum; not with Routing Essentials | Advantage + possible CUBE licenses; 17.18.2+ |
| SRST, voice modules | DNA Advantage / uck9 | `A-FLEX-3` + DNA Advantage minimum | Advantage; 17.18.2+ (modules 26.1/26.2) |
| SD-WAN (controller) | DNA subscription | DNA Essentials (10 VPNs + mgmt) or Advantage | WAN Essentials (10 VPN + 1 mgmt) or WAN Advantage (36-month min.) |
| Crypto above 250 Mbps | HSECK9 | HSECK9 + numeric/tier license | Advantage AUTHORIZED (17.18.1a+ Day-0 enforcement) |

Sources: model files' licensing sections:
[ISR4431 Licensing](research-cisco-isr4431-r1.1.0.md#6-licensing),
[C8300-1N1S-4T2X Licensing](research-cisco-c8300-1n1s-4t2x-r1.1.0.md#licensing),
[C8375-E-G2 Licensing](research-cisco-c8375-e-g2-r1.1.0.md#licensing),
[C8300-1N1S-6T Licensing](research-cisco-c8300-1n1s-6t-r1.1.0.md#licensing).

### Throughput needed at representative WAN bandwidths (illustrative)

Throughput is TBD. This table shows which license each platform would need
**if all WAN traffic were IPsec-encrypted at the given aggregate rate**. It
compares licensed limits only; it is not a measured-performance claim.
Unencrypted (CEF) traffic is documented as unthrottled on the C8300s. Whether
the hardware sustains a rate depends on the traffic mix (see
[Performance](#performance)).

| Aggregate encrypted rate | `ISR4431/K9` (baseline) | `C8300-1N1S-4T2X` | `C8375-E-G2` | `C8300-1N1S-6T` |
| --- | --- | --- | --- | --- |
| ≤ 250 Mbps | securityk9 (inferred), no HSEC; 250 Mbps crypto cap, default 500 Mbps forwarding shaper | 250M or T1 without HSECK9 (250M per direction) | OS Essentials (250 Mbps aggregate) | As model 2 |
| 500 Mbps | HSECK9 plus securityk9; default 500 Mbps shaper capacity; actual IPsec rate unverified | 250M/T1 with HSECK9 (500M aggregate, 17.14.1a+) | Routing/OS Advantage | As model 2 |
| 1 Gbps | HSECK9 plus securityk9 and PERF 1G shaper; actual IPsec rate unverified | 500M numeric + HSECK9 (1G aggregate) | Routing/OS Advantage | As model 2 |
| 2 Gbps | **Not verified**: no HSEC IPsec figure at this rate; PERF 1G is not the Boost maximum | 1G numeric or T2 + HSECK9 (2G aggregate) | Routing/OS Advantage | 1G or T2 + HSECK9 (**ceiling**) |
| 5 Gbps | **Not verified**: no HSEC IPsec figure at this rate; PERF 1G is not the Boost maximum | 2.5G numeric (5G aggregate) + HSECK9; Advantage tier | Routing/OS Advantage | **Not available** |
| 10 Gbps | **Not verified**: no HSEC IPsec figure at this rate; PERF 1G is not the Boost maximum | T3 (20G aggregate) + HSECK9; Advantage tier; hardware IPsec 6.6 Gbps at IMIX | Routing/OS Advantage; hardware 20 Gbps at 512 B ("up to") | **Not available** |

Sources: [ISR4431-DS-1](research-cisco-isr4431-r1.1.0.md#isr4431-ds-1);
[C8300-4T2X-LIC-1](research-cisco-c8300-1n1s-4t2x-r1.1.0.md#c8300-4t2x-lic-1);
[C8375-LIC-1](research-cisco-c8375-e-g2-r1.1.0.md#c8375-lic-1);
[C8300-6T-LIC-1](research-cisco-c8300-1n1s-6t-r1.1.0.md#c8300-6t-lic-1)
Table 6; [C8300-4T2X-MX-1](research-cisco-c8300-1n1s-4t2x-r1.1.0.md#c8300-4t2x-mx-1), [C8300-6T-MX-1](research-cisco-c8300-1n1s-6t-r1.1.0.md#c8300-6t-mx-1).

## Feature and ISE comparison

### Feature matrix

"Yes (family)" = documented for the product family, not this PID by name.

| Feature | `ISR4431/K9` | `C8300-1N1S-4T2X` | `C8375-E-G2` | `C8300-1N1S-6T` |
| --- | --- | --- | --- | --- |
| SD-WAN | Yes, controller; last train 17.12.x | Yes, controller | Yes, controller (also SD-Routing) | Yes, controller |
| IPsec VPN | Yes (family) | Yes | Yes | Yes |
| NAT | Yes (family) | Yes | Yes | Yes |
| QoS | Yes (family) | Yes | Yes | Yes |
| Voice / CUBE | Yes; 4431 on CUBE's End-of-Life platform list | Yes (PVDM DSP modules) | Yes, autonomous only, 17.18.2+; vDSP, no PVDM | Yes (PVDM DSP modules) |
| NGFW / UTD | Yes; DRAM upgrade needed; not with boost | ZBFW yes; IPS/IDS entitled in DE/DA; AMP/URLF SD-Routing only | Yes; 7 Gbps Threat; URLF/AMP via SD-WAN Manager | As model 2 |
| PoE | NIM-ES2-8-P plus PoE PSU, compatibility documented; module EOS 2025-03-05 | Modules only; 250 W redundant / 500 W Boost without redundancy | Built-in UPOE+ on two ports plus modules | Modules only; 250 W redundant / 500 W Boost without redundancy |
| Routing scale | not verified | 1.6M–4M routes | 2M routes | 1.6M–4M routes |
| VRF-Lite | Documented on exact ISR4431 at 16.12.2t; applicability at 17.12.8 inferred; tier unresolved | Yes, 4,000 VRFs | Yes, 4,000 VRFs | Yes, 4,000 VRFs |
| SGT segmentation | Yes (TrustSec Tier I) | Yes (family row, **inferred** for PID) | Entitlement documented; configuration **not verified** | Yes (family row, **inferred** for PID) |
| Multicast Service Reflection | Supported at family/release-note level; exact-PID test at 17.12.8 not located | Supported at family/release-note level; Network Advantage indicated by Cisco Catalyst MSR note; exact-PID test at 17.15.6 not located | Routing Advantage entitlement documented; exact C8375 execution at selected release not directly validated | Supported at family/release-note level; Network Advantage indicated by Cisco Catalyst MSR note; exact-PID test at 17.15.6 not located |

Sources: [ISR4431 Feature support](research-cisco-isr4431-r1.1.0.md#7-feature-support-and-integration);
[C8300-1N1S-4T2X Feature support](research-cisco-c8300-1n1s-4t2x-r1.1.0.md#feature-support-and-integration);
[C8375-E-G2 Feature support](research-cisco-c8375-e-g2-r1.1.0.md#feature-support-and-integration);
[C8300-1N1S-6T Feature support](research-cisco-c8300-1n1s-6t-r1.1.0.md#feature-support-and-integration).
The license tier each feature needs is in
[Entitlement per capability](#entitlement-per-capability).

### ISE integration

| Integration | `ISR4431/K9` | `C8300-1N1S-4T2X` | `C8375-E-G2` | `C8300-1N1S-6T` |
| --- | --- | --- | --- | --- |
| RADIUS device admin | Yes (family) | Yes; 26.2.1 requires Message-Authenticator from ISE | Yes (Essentials); 26.2 adds Message-Authenticator rules | Yes |
| TACACS+ device admin | Yes (family) | Yes, **inferred** for PID; exact controller/minimum release not established | Yes (Essentials); TLS 1.3 from 17.18.1 | Yes, inferred for PID; family matrix entitlement |
| SGT inline tagging | Yes | Yes through `C-NIM-2T/1M/1X`; built-in ports not verified | Not verified | Yes, **inferred** (family row) |
| SXP | Yes (V4; V5 from 17.9.1); 1,800/900 connections | Yes (family row) | **Not verified** (matrix prints "SGX") | Yes, **inferred** |
| SGACL enforcement | Yes | Yes (family row) | Entitlement documented; configuration not verified | Yes, **inferred** |
| 802.1X / MAB | Yes on NIM-ES2-4/-8/-8-P switch ports (IP Base); modules are EOS; exact 17.12.8 validation unresolved | **Yes on C-SM-16P4M2X copper ports**; other modules/ports unverified | 802.1X entitled; ports unverified; MAB unverified | Yes on C-SM-16P4M2X copper ports; other NIMs unverified |
| ISE license tier | not documented | not documented | not documented | GBP matrix: ISE "Advantage" for TrustSec and pxGrid |

Where supported and verified in the model tables, routers hold AAA server
groups and applicable CTS/SXP/SGACL configuration; ISE holds device
definitions and identity/authorization policy. C8375 SXP/SGACL configuration
remains unverified, so a common configuration recipe is not established for
all four.
Sources: the ISE tables in each model file, e.g.
[C8300-6T-GBP-1](research-cisco-c8300-1n1s-6t-r1.1.0.md#c8300-6t-gbp-1),
[C8300-4T2X-TS-1](research-cisco-c8300-1n1s-4t2x-r1.1.0.md#c8300-4t2x-ts-1),
[ISR4431-SEC-4](research-cisco-isr4431-r1.1.0.md#isr4431-sec-4),
[C8375-LFM-1](research-cisco-c8375-e-g2-r1.1.0.md#c8375-lfm-1).

ISR module and VRF-Lite corrections trace to
[ISR4431-MOD-2](research-cisco-isr4431-r1.1.0.md#isr4431-mod-2),
[ISR4431-CFG-9](research-cisco-isr4431-r1.1.0.md#isr4431-cfg-9), and
[ISR4431-EOL-6](research-cisco-isr4431-r1.1.0.md#isr4431-eol-6).
These document compatibility, example release scope and module lifecycle
separately; they do not establish new ISR/module purchase eligibility.

## Offline licensing comparison

Hard requirement: **no internet connectivity for license reporting.** All four
have a documented way to operate. Each still needs an internet-connected
workstation, not the router, to exchange files with Cisco Smart Software
Manager (CSSM).

| Item | `ISR4431/K9` (baseline) | `C8300-1N1S-4T2X` / `C8300-1N1S-6T` | `C8375-E-G2` |
| --- | --- | --- | --- |
| Documented method | SLP "No Connectivity to CSSM and No CSLU" (from 17.3.2) | Same SLP air-gapped topology; CSLU disconnected; SSM On-Prem with manual file sync | At the 17.15.5 basis: SSM On-Prem/CSLU offline sync, listed in the platform licensing guide. From 17.18.1a: **Specific License Reservation (SLR)**, documented with a worked example on this PID |
| Steps | `license smart transport off`; `license smart save usage`; upload on a workstation; `license smart import` the ACK | Same; HSECK9 SLAC by file (on-box request from 17.7.1a) or factory-installed | `license smart reservation request local` → reserve in CSSM → `license smart reservation install file`; factory pre-install possible |
| Recurring cadence | Default policy: subscriptions every 90 days; report within 90 days of change | Same; network-stack-only use: report on change only; SSM On-Prem: file sync at least yearly | SLP via On-Prem/CSLU (basis): cadence **unverified** on this platform (licenses show "CONDITIONALLY-ENFORCED"). SLR (17.18.1a+): none (one-time per device; return/re-reserve on RMA) |
| Crypto entitlement offline | HSECK9 SLAC by file | HSECK9 SLAC by file or factory | Not needed (no HSECK9); but on 17.18.1a+ crypto stays at 250 Mbps until Advantage is AUTHORIZED |
| Missed deadline | Syslog only; feature effect **unresolved** | Syslog only; feature effect **unresolved** | 17.15.x: no Day-0 Enforcement, Advantage unthrottled after reload. 17.18.1a+: 250 Mbps crypto throttle if not authorized. SLR term-license end behavior **unresolved** |
| Conditions | — | — | SLR needs 17.18.1a+ (above the suggested release) and "approval and authorization from Cisco" |
| Admin workload (inferred) | Subscription use: about 90-day file reporting. Unenforced perpetual: conditional first report within 365 days, then on changes within 90 days; use actual device policy | About 90-day cycles for consumed subscriptions; network-stack-only reporting differs; yearly On-Prem sync and one-time HSEC SLAC | At basis: periodic exchange with unverified platform cadence. SLR on 17.18.1a+ removes periodic reporting if approved |
| Eligibility | n/a (not orderable) | **Met (documented)** | **Met, conditional**: periodic offline reporting at the basis; SLR after an upgrade and Cisco approval |

Sources: [ISR4431-LIC-1](research-cisco-isr4431-r1.1.0.md#isr4431-lic-1);
[C8300-4T2X-SLP-1](research-cisco-c8300-1n1s-4t2x-r1.1.0.md#c8300-4t2x-slp-1);
[C8300-6T-SLP-1](research-cisco-c8300-1n1s-6t-r1.1.0.md#c8300-6t-slp-1),
[C8300-6T-ONP-1](research-cisco-c8300-1n1s-6t-r1.1.0.md#c8300-6t-onp-1);
[C8375-LIC-1](research-cisco-c8375-e-g2-r1.1.0.md#c8375-lic-1),
[C8375-SLP-1](research-cisco-c8375-e-g2-r1.1.0.md#c8375-slp-1).

**Inferred:** on the C8375-E-G2, a perpetual OS Advantage license (`R-OS-L-A`)
under SLR avoids the unresolved term-end question. Cisco does not state this
directly.

## Management options

**CLI in autonomous mode remains the baseline.** Central managers are optional
design choices with separate infrastructure, entitlement, reporting and
upgrade requirements. The public-source management review is now complete;
the bounded activation/sizing gaps below remain explicit. Sources were
registered first in the
[C8375 management research](research-cisco-c8375-e-g2-r1.1.0.md#management-platforms-and-disconnected-deployment).
No manager deployment or hardware configuration was lab-tested.

| Item | CLI (autonomous) | Catalyst Center | Catalyst SD-WAN Manager |
| --- | --- | --- | --- |
| Router mode | Autonomous baseline; capabilities remain subject to the selected tier/module | Autonomous management; exact feature coverage follows compatibility matrix | Controller for SD-WAN; autonomous SD-Routing is a separate supported workflow |
| Deployment form | Per-router terminal/SSH access; no central manager appliance | Physical appliance or VA on ESXi; AWS/Azure alternatives exist | Customer-hosted control-component VMs on ESXi/KVM/UCS infrastructure; Cisco-hosted/cloud-delivered alternatives |
| Router entitlement | Valid platform/base and feature licenses | C8300 DNA Essentials/Advantage or Routing Essentials; C8375 Routing/OS Advantage plus LIC-R-OP-CC. ISR compatible, exact current purchase entitlement unresolved and hardware EOS | ISR/C8300 DNA SD-WAN subscriptions; C8375 WAN tiers or applicable Routing/OS Advantage plus LIC-R-OP-SWM for on-prem SD-Routing |
| Manager's own licensing | No additional central manager instance | VA DN-SW-APL-LIC requires Smart Account registration; instance supports On-Prem registration. Physical appliance purchase separate | DNA offers include centralized Manager use; new Secure Router offers differ. Universal extra on-prem Manager SKU not established; quote the selected hosting/offer |
| Internet-disconnected operation | Router SLP/SLAC or eligible SLR as documented above | TAC-enabled air-gap operation and manual package transfer are documented for physical/ESXi. **Fully disconnected VA activation and selected license-server bootstrap remain unverified** | Documented Offline Mode: external-workstation license-summary/report/ACK exchange. Default 90 days; prepaid every three months, postpaid monthly. Applies to supported Manager/edge workflows; exact offer still governs |
| Reporting boundary | Use the router's actual policy and enforcement state | Center 2.3.7.x device License Manager does not support On-Prem SSM **RUM reporting**. Instance registration does not replace autonomous router reporting | On-Prem mode is distinct from Offline Mode and requires local Manager, supported SSM server and 24-hour Manager/server sync; the documented server example connects to CSSM |
| Offline maintenance | Per-device images/configuration and license-file handling | Local DNS/NTP/ISE/device access plus TAC-supplied release-specific upgrade package/checksum. A published 3.x example is not a 2.3.7 upgrade procedure | Local VM/image/serial-list files and certificate workflows; **inferred workload:** local CA renewal, image storage, control-component backups and periodic offline files |
| Alongside ISE | Router AAA/TrustSec/module authentication only where verified | ISE/ERS/pxGrid, trusted certificates, site inventory and policy integration | ISE SGT/IP-binding and identity-firewall integration documented from Manager 20.10.1 / IOS XE 17.10.1a; exact-router enforcement remains governed by each model |
| Benefits (inferred from documented functions) | No central manager operations; direct control of entitled features | Central inventory, image management and assurance | Central provisioning, policy, upgrades and license assignment |
| Drawbacks/workload (inferred) | Repeated per-router work | Appliance/VM operations, extra C8375 add-on, offline bootstrap confirmation and manual upgrades | Local control-plane/certificate operations, periodic file exchange; C8375 voice restrictions and mode-conversion preparation still apply |

Deployment/own-instance evidence:
[C8375-MGMT-CC-DS-1](research-cisco-c8375-e-g2-r1.1.0.md#c8375-mgmt-cc-ds-1),
[C8375-MGMT-CC-VA-1](research-cisco-c8375-e-g2-r1.1.0.md#c8375-mgmt-cc-va-1),
[C8375-MGMT-CC-SYS-1](research-cisco-c8375-e-g2-r1.1.0.md#c8375-mgmt-cc-sys-1),
[C8375-MGMT-SDW-DS-1](research-cisco-c8375-e-g2-r1.1.0.md#c8375-mgmt-sdw-ds-1),
[C8375-MGMT-SDW-FAQ-1](research-cisco-c8375-e-g2-r1.1.0.md#c8375-mgmt-sdw-faq-1).
Router-license evidence:
[C8300-4T2X-FAQ-1](research-cisco-c8300-1n1s-4t2x-r1.1.0.md#c8300-4t2x-faq-1),
[C8300-4T2X-DNA-2](research-cisco-c8300-1n1s-4t2x-r1.1.0.md#c8300-4t2x-dna-2),
[C8375-OG-1](research-cisco-c8375-e-g2-r1.1.0.md#c8375-og-1) Tables 9–10,
and [ISR4431-SDWAN-1](research-cisco-isr4431-r1.1.0.md#isr4431-sdwan-1).
Disconnected/reporting evidence:
[C8375-MGMT-CC-AIR-1](research-cisco-c8375-e-g2-r1.1.0.md#c8375-mgmt-cc-air-1),
[C8375-MGMT-CC-ADM-1](research-cisco-c8375-e-g2-r1.1.0.md#c8375-mgmt-cc-adm-1),
[C8375-MGMT-SDW-SLP-1](research-cisco-c8375-e-g2-r1.1.0.md#c8375-mgmt-sdw-slp-1).
Onboarding/ISE evidence:
[C8375-MGMT-SDW-GS-1](research-cisco-c8375-e-g2-r1.1.0.md#c8375-mgmt-sdw-gs-1),
[C8375-MGMT-CC-SYS-1](research-cisco-c8375-e-g2-r1.1.0.md#c8375-mgmt-cc-sys-1),
[C8375-MGMT-ISE-1](research-cisco-c8375-e-g2-r1.1.0.md#c8375-mgmt-ise-1).

**Model support:** the Catalyst Center **2.3.7.11** public matrix has explicit
rows for all four routers. ISR4431 includes 17.12.x; both C8300 PIDs include
17.15.x; C8375 includes 17.15.x/17.18.x. All four list inventory, topology,
SWIM, PnP and Assurance support at train granularity. C8375 Application
Policy is NA, and its DNA columns N do not override its newer management
offer. The matrix's overbroad later ISR trains do not override its 17.12.x
ceiling ([C8375-MGMT-CC-MX-1](research-cisco-c8375-e-g2-r1.1.0.md#c8375-mgmt-cc-mx-1)).
All four have SD-WAN support within their model-specific release/controller
limits. The matrix confirms ISR4000 family 17.12.x under Manager 20.12.8.1 and
Catalyst 8300 family 17.15.6 under Manager 20.15.6/20.15.6.1; PID application
for the ISR and both C8300 PIDs is a family-level inference. Compatibility
does not equal recommendation. Evidence: [ISR4431-SDWAN-3](research-cisco-isr4431-r1.1.0.md#isr4431-sdwan-3), [C8300-6T-COMP-2](research-cisco-c8300-1n1s-6t-r1.1.0.md#c8300-6t-comp-2), and the shared C8300 controller evidence in each model section. A cloud-hosted service requires
network reachability to that service; it does not meet a fully isolated
manager design. Exact server sizing, appliance activation and cloud-feed
behavior remain requirement/vendor confirmation items rather than unresearched
management sections.

## Optics comparison

Non-exhaustive, from Cisco's Transceiver Module Group (TMG) matrix exports in
each file. The ISR4431 uses the **live Cisco export dated 2026-10-30**, registered as
ISR4431-OPT-2; the older mirror is retained as historical reference only. Min release in parentheses. "—" = no such port type.

### Minimum set

| Item | `ISR4431/K9` built-in (SFP mode) | `C8300-1N1S-4T2X` built-in SFP+ | `C8375-E-G2` built-in SFP/SFP+ | `C8300-1N1S-6T` built-in SFP | C8300 module ports (`C-NIM-4X`) |
| --- | --- | --- | --- | --- | --- |
| 1000BASE-SX | `GLC-SX-MMD` | `GLC-SX-MMD` (17.3.2) | `GLC-SX-MMD` (17.15.3) | `GLC-SX-MMD` (17.3.2) | `GLC-SX-MMD` (17.11.1) |
| 1000BASE-LX/LH | `GLC-LH-SMD` | `GLC-LH-SMD`, `GLC-LX-SM-RGD` | Same (17.15.3) | Same (17.3.2) | Same (17.11.1) |
| 1000BASE-ZX (70 km) | `GLC-ZX-SMD` | `GLC-ZX-SMD` (17.3.2) | `GLC-ZX-SMD` (17.15.3) | `GLC-ZX-SMD` (17.3.2) | `GLC-ZX-SMD` (17.11.1) |
| 1000BASE-T SFP | `GLC-T`, `GLC-TE`, `SFP-GE-T` | `GLC-TE` (1G only) | `GLC-TE` | `GLC-TE` (1G only) | `GLC-TE` (17.18.1; 100M/1G) |
| 10GBASE-SR / LR | — | `SFP-10G-SR`, `-LR` (17.3.2) | `SFP-10G-SR`, `-LR` (17.15.3) | — | `SFP-10G-SR`, `-LR` (17.11.1) |
| 10GBASE-ER (40 km) | — | `SFP-10G-ER` (17.3.2) | `SFP-10G-ER` (17.15.3) | — | `SFP-10G-ER` (17.11.1) |
| 10GBASE-ZR (70 km) | — | **not verified** | `SFP-10G-ZR-I` (17.18.2; above the 17.15.5 basis) | — | `SFP-10G-ZR-I` (17.18.2; above the 17.15.6 basis) |
| 10GBASE-T SFP+ | — | `SFP-10G-T-X` (10G only, 30 m) | `SFP-10G-T-X` (1G/10G, 30 m at 10G) | — | `SFP-10G-T-X` (1G/10G) |
| 10G DAC | — | `SFP-H10GB-CU1M–5M`, `-ACU7M/10M` | `SFP-H10GB-CU2M–5M`, `-ACU7M/10M`; AOC | — | `-ACU7M/10M` |
| 1G DAC | not verified | not verified | not verified | not verified | not verified |

Long-reach restrictions found: only `SFP-10G-ZR-I`'s cold-start note (no
optical traffic below −28 °C) and its 17.18.2 minimum. No distance, power, or
port restriction on ZX/ER/ZR was found for any platform.

### Copper SFPs

| Port type | 1G copper SFP (1000BASE-T) | 10G copper SFP+ (10GBASE-T) |
| --- | --- | --- |
| ISR4431 built-in | **Yes**: `GLC-T`, `GLC-TE`, `SFP-GE-T`; rate listed 10/100/1000 | No port (n/a) |
| C8300-1N1S-4T2X built-in | **Yes**: `GLC-TE`, 1000 Mb/s only (no 100 Mb/s) | **Yes**: `SFP-10G-T-X`, 10 Gb/s only, 30 m |
| C8375-E-G2 built-in | **Yes**: `GLC-TE`; 100 Mb/s not verified | **Yes**: `SFP-10G-T-X`, 1G/10G only, 30 m at 10G |
| C8300-1N1S-6T built-in | **Yes**: `GLC-TE`, 1000 Mb/s only | No SFP+ port (n/a) |
| `C-NIM-4X` (C8300, C8375) | **Yes**: `GLC-TE`, 100M/1G, 17.18.1 | **Yes**: `SFP-10G-T-X`, 1G/10G |
| `C-NIM-1X` (C8300) | Not verified / datasheet says no | **Conflict**: datasheet says no; TMG lists `SFP-10G-T-X` |
| `C-NIM-WAN-2X/4S` (C8375) | **Yes**: `GLC-TE`, 100M/1G | 2X: **Yes** (`SFP-10G-T-X`); 4S: no SFP+ port |

No count, adjacency, or thermal limit for copper SFPs was found on any
platform. The built-in RJ-45 ports meet a 1G copper need on all four without
copper SFPs (the C8375's also do 2.5G). None gives 10G copper without an
`SFP-10G-T-X`.

### Policy, DOM, and faster ports

| Item | `ISR4431/K9` | `C8300-1N1S-4T2X` | `C8375-E-G2` | `C8300-1N1S-6T` |
| --- | --- | --- | --- | --- |
| Third-party optics policy | not verified | not verified; LED flags unsupported SFPs | `show version`: Cisco "may withhold support" for faults traced to third-party optics | not verified; LED flags unsupported SFPs |
| `service unsupported-transceiver` | not verified | not verified | not verified | not verified |
| DOM (fiber optics) | Yes (matrix) | Yes from 17.3.2 | Yes from 17.15.3 | Yes from 17.3.2 |
| DOM display command | not verified | not verified | not verified | not verified |
| Ports faster than 10G | none | none | none | none |

Sources: [ISR4431-OPT-2](research-cisco-isr4431-r1.1.0.md#isr4431-opt-2);
[C8300-4T2X-TMG-1](research-cisco-c8300-1n1s-4t2x-r1.1.0.md#c8300-4t2x-tmg-1),
[C8300-4T2X-TMG-2](research-cisco-c8300-1n1s-4t2x-r1.1.0.md#c8300-4t2x-tmg-2);
[C8375-TMG-1](research-cisco-c8375-e-g2-r1.1.0.md#c8375-tmg-1) through
[C8375-TMG-4](research-cisco-c8375-e-g2-r1.1.0.md#c8375-tmg-4),
[C8375-SCG-1](research-cisco-c8375-e-g2-r1.1.0.md#c8375-scg-1);
[C8300-6T-TMG-1](research-cisco-c8300-1n1s-6t-r1.1.0.md#c8300-6t-tmg-1),
[C8300-6T-TMG-2](research-cisco-c8300-1n1s-6t-r1.1.0.md#c8300-6t-tmg-2),
[C8300-6T-WANMOD-1](research-cisco-c8300-1n1s-6t-r1.1.0.md#c8300-6t-wanmod-1).

**Not reviewed in this research:** CWDM, DWDM, BiDi, and extended-temperature
(industrial) optics are needed but were not reviewed for any platform. They
are carried into [Open questions](#open-questions).

## Module comparison

| Function | `ISR4431/K9` | `C8300-1N1S-4T2X` | `C8375-E-G2` | `C8300-1N1S-6T` |
| --- | --- | --- | --- | --- |
| Voice (analog/digital) | Voice NIMs + PVDM4 in ISC; uck9 or DNA Advantage | Voice NIM/SM-X + `NIM-PVDM`/`SM-X-PVDM`; DNA Advantage | Analog NIM/SM-X from 26.1, BRI/E&M from 26.2; vDSP 17.18.2+; Advantage; autonomous only | As model 2; `C8300-1N1S-6T-V` voice bundle (End-of-Sale 2027-01-31) |
| Extra 1G Ethernet | `NIM-1GE/2GE-CU-SFP` | `C-NIM-2T`, `C-NIM-4X`, switch NIMs | `C-NIM-WAN-4S`, `C-NIM-4X`, `C-NIM-8T/8M` | As model 2 |
| Extra 10G Ethernet | none found | `C-NIM-1X`, `C-NIM-4X` (embedded NIM slot, 17.11.1+), `C-SM-16P4M2X` (L2 uplinks) | `C-NIM-WAN-2X`, `C-NIM-4X`, `C-SM-16P4M2X` | As model 2 (the only 10G path on this model) |
| Compute | none verified | UCS-E listed (older UCS-E M2 absent from the list) | UCS-E **not on lists checked** (conflicts with FAQ text) | As model 2 |
| PoE | NIM-ES2-8-P (EOS 2025-03-05) plus PWR-4430-POE-AC; reference compatibility only | `C-NIM-8M`, `C-NIM-1M`, `C-SM-16P4M2X` + `PWR-CC1-500WAC` | Built-in UPOE+ on 2 ports; `C-NIM-8M`; needs `PWR-CC1-760WAC` | As model 2 |
| External option | Ethernet-attached switch or appliance (not assessed) | Same | Same | Same |

Reuse: about 70 % of ISR 4000 modules carry over to the Catalyst 8300; Cisco
says "most". `C-NIM-1X`, `C-SM-NIM-ADPT`, `C-SM-16P4M2X`, and `C-SM-40P8M2X` do
not work in ISR 4000. The two C8300 models share identical module lists. The
C8375-E-G2 shares a subset with them (`C-NIM-4X/8T/8M`, `C-SM-16P4M2X`,
`C-SM-NIM-ADPT`, voice, and serial). Its memory and SSD PIDs differ.
Sources:
[C8300-4T2X-OG-1](research-cisco-c8300-1n1s-4t2x-r1.1.0.md#c8300-4t2x-og-1),
[C8300-4T2X-OG-2](research-cisco-c8300-1n1s-4t2x-r1.1.0.md#c8300-4t2x-og-2);
[C8300-6T-LANMOD-1](research-cisco-c8300-1n1s-6t-r1.1.0.md#c8300-6t-lanmod-1),
[C8300-6T-SMSW-1](research-cisco-c8300-1n1s-6t-r1.1.0.md#c8300-6t-smsw-1);
[C8375-OG-1](research-cisco-c8375-e-g2-r1.1.0.md#c8375-og-1),
[C8375-FAQ-1](research-cisco-c8375-e-g2-r1.1.0.md#c8375-faq-1);
[ISR4431-DS-3](research-cisco-isr4431-r1.1.0.md#isr4431-ds-3),
[ISR4431-MOD-1](research-cisco-isr4431-r1.1.0.md#isr4431-mod-1).

**Module ordering limit:** NIM-ES2-8/-8-P passed End-of-Sale on
2025-03-05 and NIM-ES2-4 on 2025-04-17. Their compatibility remains useful
reference evidence, but they cannot be selected as new-purchase module
options. Do not infer ISR support from the successor C-NIM names
([C8300-4T2X-EOL-6](research-cisco-c8300-1n1s-4t2x-r1.1.0.md#c8300-4t2x-eol-6),
[C8300-4T2X-EOL-7](research-cisco-c8300-1n1s-4t2x-r1.1.0.md#c8300-4t2x-eol-7)).

## Lifecycle and risk

No support horizon was supplied, so no platform is disqualified on support
dates alone. The new-purchase requirement is a hard filter.

| Platform | Support runway from 2026-10-30 | Risk of buying or keeping | Migration path |
| --- | --- | --- | --- |
| `ISR4431/K9` | ~2 years (LDoS 2028-11-30) | Not purchasable new. Software frozen at 17.12.x; 17.12.x security support ends 2027-09-30, with ad-hoc releases promised to 2028-11. | → C8300 (itself End-of-Sale) → C8375 |
| `C8300-1N1S-4T2X` | ~5.25 years (LDoS 2032-01-31) | Ordering window closes 2027-01-31 (3 months). A multi-site rollout after that date can't add units. The 17.15.x basis loses maintenance 2027-03-30, so a move to 17.18.x/26.x is needed within the support life. | → C8375-E-G2 |
| `C8375-E-G2` | No chassis milestones announced | New platform. Suggested 17.15.5 maintenance ends 2027-03-30. Later releases introduce Day-0 enforcement, but an existing Advantage configuration upgrades into Day-N unthrottled; deployment/authorization state matters. Module list changes by release (DSL/T3 end at 17.18.1; WAN NIMs from 17.18.1; voice from 26.1/26.2). 17.18.x got its EoL notice 2026-10-30. | n/a |
| `C8300-1N1S-6T` | ~5.25 years (LDoS 2032-01-31) | As model 2, plus a 2 Gbps licensed crypto ceiling; the PoE PSU is also End-of-Sale with no replacement. | → C8375-E-G2 |

Sources: lifecycle sections of each model file,
[ISR4431-EOL-3](research-cisco-isr4431-r1.1.0.md#isr4431-eol-3),
[C8300-4T2X-EOL-3](research-cisco-c8300-1n1s-4t2x-r1.1.0.md#c8300-4t2x-eol-3),
[C8375-EOL-1](research-cisco-c8375-e-g2-r1.1.0.md#c8375-eol-1),
[C8375-EOL-3](research-cisco-c8375-e-g2-r1.1.0.md#c8375-eol-3).

## Decision matrix

### Hard requirements

| Requirement | `ISR4431/K9` | `C8300-1N1S-4T2X` | `C8375-E-G2` | `C8300-1N1S-6T` |
| --- | --- | --- | --- | --- |
| Orderable new | **Fails** (End-of-Sale 2023-11-07) | Met until 2027-01-31 | Met | Met until 2027-01-31 |
| Documented way to run licensing with no internet | Documented (moot) | Met | Met, conditional (periodic file exchange at an unverified cadence on 17.15.x; SLR from 17.18.1a with Cisco approval) | Met |
| Identity resolved | Yes | Yes (SKU corrected) | Yes | Yes |
| Eligible for recommendation | **No** (reference baseline) | Yes, time-limited | Yes | Yes, time-limited |

### Weighted scoring (illustrative)

Weights are illustrative: no weights were supplied, and throughput is TBD.
Scale: 1 (weak) to 5 (strong), scored on documented evidence in the model
files. Weighted points = score × weight ÷ 5, so 100 is the maximum. The three new-purchase candidates
are scored on the same seven criteria and weights. ISR4431 has an unknown
HSEC crypto ceiling, so that criterion is **not scored** and no ISR total is
calculated; its remaining scores are reference judgments only. No weights
are renormalized around the gap. Raw
performance figures are **not** scored, because their conditions differ. The
performance criterion uses licensed crypto ceilings, which are documented
license limits.

| Criterion (weight) | `ISR4431/K9` (reference) | `C8300-1N1S-4T2X` | `C8375-E-G2` | `C8300-1N1S-6T` |
| --- | --- | --- | --- | --- |
| Lifecycle runway (20 %) | 1: End-of-Sale; LDoS 2028-11-30 | 3: End-of-Sale 2027-01-31; LDoS 2032-01-31 | 5: no chassis notice; 26.x 48-month sustaining | 3: as model 2 |
| Licensed throughput headroom (15 %) | **Not scored:** HSEC crypto ceiling is unknown; 1 Gbps PERF is not an absolute Boost maximum | 4: T3 20G aggregate; hardware-bound below that | 4: Advantage unthrottled; hardware-bound | 2: 2 Gbps aggregate ceiling |
| Interfaces and optics (15 %) | 1: no 10G | 4: built-in 10G SFP+ (SR/LR/ER, 10G-T); ZR not verified built-in | 4: built-in 10G (SR/LR/ER, 10G-T); 2.5G mGig; UPOE+; ZR above basis (17.18.2) | 2: 10G only via modules; ZR only via `C-NIM-4X` at 17.18.2 |
| Offline licensing clarity and workload (15 %) | 4: documented SLP air-gap, HSECK9 by file | 4: documented SLP air-gap; ~90-day cycles or yearly On-Prem | 3: file exchange at basis with cadence unresolved; SLR one-time but needs 17.18.1a+ and Cisco approval | 4: as model 2 |
| Feature and ISE coverage (15 %) | 3: TrustSec documented; UTD memory/Boost restrictions; last train 17.12 | 3: broad; family tier/SGT conflict; 802.1X/MAB documented on C-SM-16P4M2X | 3: broad; SXP/MAB/configuration gaps; URLF/AMP require Manager | 3: broad; module authentication documented; TACACS+/SGT inferred |
| Modules and expansion (10 %) | 3: 3 NIM + ISC, no SM/PIM | 4: NIM/SM/PIM; broad list incl. PVDM, UCS-E | 2: narrower list; no PVDM; at basis no WAN NIMs and no voice modules | 4: as model 2 |
| Software maturity (10 %) | 2: recommended release exists but train frozen | 5: Cisco-recommended 17.15.6 | 3: Cisco-suggested 17.15.5, but below the advisory's first fix and on a train past End-of-Sale | 5: as model 2 |
| **Weighted total (of 100)** | **Not calculated**: reference-only, one criterion not scored | **75** | **72** | **63** |

Arithmetic (new-purchase candidates only):
C8300-1N1S-4T2X (3×20 + 4×15 + 4×15 + 4×15 + 3×15 + 4×10 + 5×10) ÷ 5 = 75;
C8375-E-G2 (5×20 + 4×15 + 4×15 + 3×15 + 3×15 + 2×10 + 3×10) ÷ 5 = 72;
C8300-1N1S-6T (3×20 + 2×15 + 2×15 + 4×15 + 3×15 + 4×10 + 5×10) ÷ 5 = 63.

The top two are 3 points apart on illustrative weights, too close to decide
between them. The qualitative tradeoff decides it. The C8375-E-G2 wins on
lifecycle. The C8300-1N1S-4T2X wins on software maturity, modules, and
offline-licensing certainty. Scoring the C8375-E-G2 at its suggested 17.15.5
release, rather than 26.2.1, cost it ZR optics, WAN NIMs, and voice modules
at basis. For a **new, multi-site** purchase, the 2027-01-31 ordering cutoff
makes the C8300 a short-term option only, which is why the recommendation
favors the C8375-E-G2.

### Evidence coverage

Qualitative assessment of evidence in the tables above. These labels are
review judgments, not calculated coverage percentages or source counts.
Family-level evidence and unresolved applicability are not promoted to
exact-PID documentation.

| Platform | Coverage | Main weak areas |
| --- | --- | --- |
| `ISR4431/K9` | Moderate | Feature-to-tier mapping (family matrix inferred only), routing scale, release dates |
| `C8300-1N1S-4T2X` | High | Family tier map/SGT conflict; switch modules beyond the documented C-SM; power/DOM gaps |
| `C8375-E-G2` | High | Security status of suggested 17.15.5, SXP/MAB, SLR term-end behavior, offline cadence on 17.15.x, maximum power |
| `C8300-1N1S-6T` | Moderate | TACACS+/SGT inferred for the PID; release dates, pricing, heat/power and exact-PID details remain gaps |

### Sensitivity

- Raising **lifecycle to 30 %** and proportionally scaling the other
  weights to 70 % gives C8375-E-G2 **75.5** versus 4T2X **73.125**.
  A mandatory support horizon past 2032-01-31 would disqualify both C8300s;
  absence of a C8375 chassis notice does not guarantee any future horizon.
- Raising **software maturity** or **modules** (for example, a hard need for
  PVDM DSPs, `C-NIM-1X`, or a supported/orderable UCS-E configuration) favors the C8300-1N1S-4T2X,
  provided all units are ordered before 2027-01-31.
- If Cisco **declines SLR**, or the fleet stays on the suggested 17.15.x
  train, the C8375-E-G2's offline score depends on the unverified SLP cadence.
  Its eligibility stays met only if periodic file exchange is accepted.
- If the fleet selects an exact later release supporting the required
  optics/modules and SLR, C8375-E-G2 can gain those capabilities. ZR/CUBE/SRST
  need the stated 17.18.2 minima; analog voice modules require the relevant
  26.1/26.2 releases. Holding the other scores constant, interfaces 5 and
  modules 3 gives **77**, versus 75 for 4T2X. This scenario does not establish
  a deployment-release recommendation.
- The C8300-1N1S-6T scores lower under these weights. Its licensed
  encrypted ceiling is 2 Gbps and 10G requires modules; suitability depends
  on actual circuit/feature requirements. It shares the C8300 ordering cutoff.

## Deployment inputs to confirm

These are requirements or preferences to confirm with the deployment team. They
are separate from the technical and vendor evidence gaps in [Open
questions](#open-questions).

| Input | Why it matters |
| --- | --- |
| Purchase and rollout dates | The C8300-1N1S-4T2X and C8300-1N1S-6T reach End-of-Sale on 2027-01-31. Confirm whether all units can be ordered by then. |
| Encrypted throughput per site | Determines required license tier and whether the C8300-1N1S-6T's 2 Gbps licensed ceiling is sufficient. Include expected growth and whether figures are aggregate or per direction. |
| Required interfaces, media, and modules | Confirm WAN handoff speeds/types, long-haul optics (including CWDM/DWDM/BiDi if needed), voice, PoE, and any required modules. These determine model fit and which compatibility gaps need follow-up. |
| Required features and integrations | Identify whether TrustSec/SGT, ISE authentication, CUBE/SRST, UCS-E, or other optional features are requirements or merely desirable. This focuses entitlement and platform validation. |
| Management and offline workflow preference | Confirm autonomous CLI versus controller management and preferred Catalyst Center/SD-WAN operations under the no-internet constraint. The reports document alternatives, but the deployment choice affects licensing and operations. |
| Budget or target cost | Pricing is not scored because no quote was available. A budget range or preference for purchase versus subscription would make the comparison more decision-specific. |

## Open questions

| # | Unknown | Decision impact | What would resolve it |
| --- | --- | --- | --- |
| 1 | Will Cisco grant SLR for this deployment (it needs 17.18.1a+), and what happens when a reserved term license ends? | C8375-E-G2 offline eligibility and workload | Cisco account team / licensing (vendor answer) |
| 2 | C8375-E-G2 release choice: Cisco suggests 17.15.5, below the 2026-08 hardening advisory's first fix (17.15.6); will the suggestion move to 17.15.6, and which 17.18.x/26.x release should follow before 2027-03-30? | C8375-E-G2 software basis, security posture, and when SLR/new modules become usable | Cisco TAC; Software Checker (login); download-page re-check |
| 3 | Effect of a missed SLP reporting deadline on C8300/ISR features | Offline workload risk | Cisco licensing documentation or vendor answer |
| 4 | Selected Catalyst Center appliance/VA bootstrap with fully disconnected SSM, offer-specific activation/enforcement, and management sizing | Management deployment choice; public deployment/offline methods now researched | Cisco/TAC confirmation for selected offer plus site/device count |
| 5 | TrustSec SGT tier on the C8300s: Network Advantage (GBP matrix) or all tiers (DNA routing matrix)? IPS/IDS is now mapped to DNA Essentials/Advantage | License tier if SGT is used | Cisco account team / Feature Navigator |
| 6 | C8375 SXP/MAB and exact switch-port features; unverified C8300 modules beyond documented C-SM-16P4M2X; ISR exact-release validation | ISE design | Platform configuration guides / Cisco answer |
| 7 | Third-party optics policy and `service unsupported-transceiver` on all four | Optics cost and TAC support | Cisco TAC |
| 8 | CWDM, DWDM, BiDi, extended-temperature optics — **needed, not reviewed in this research** | Long-haul and site-specific optics | Separate optics review against TMG |
| 9 | C8300 typical power 245 W versus 82 W; remaining maximum power and heat gaps outside the ISR published maxima | Power and cooling sizing | Cisco HIG technical specifications / vendor answer |
| 10 | Whether the C8375-E-G2 supports UCS-E (lists vs FAQ text) | Compute-on-router option | Cisco ordering tool / vendor answer |
| 11 | US pricing for chassis, licenses, and support | Informational (cost is not scored) | Partner or Cisco quote |

## References

This file adds no new factual sources. Every citation above links to an entry
in a model file's `## References` register. Each model file's register and
unresolved list:

- `ISR4431/K9`:
  [References](research-cisco-isr4431-r1.1.0.md#references),
  [References - unresolved](research-cisco-isr4431-r1.1.0.md#references---unresolved)
- `C8300-1N1S-4T2X`:
  [References](research-cisco-c8300-1n1s-4t2x-r1.1.0.md#references),
  [References - unresolved](research-cisco-c8300-1n1s-4t2x-r1.1.0.md#references---unresolved)
- `C8375-E-G2`:
  [References](research-cisco-c8375-e-g2-r1.1.0.md#references),
  [References - unresolved](research-cisco-c8375-e-g2-r1.1.0.md#references---unresolved)
- `C8300-1N1S-6T`:
  [References](research-cisco-c8300-1n1s-6t-r1.1.0.md#references),
  [References - unresolved](research-cisco-c8300-1n1s-6t-r1.1.0.md#references---unresolved)

Two facts were checked directly against saved PDFs during reconciliation: the
Catalyst 8300 typical-power table and the throughput tables. They trace to
[C8300-4T2X-DS-1](research-cisco-c8300-1n1s-4t2x-r1.1.0.md#c8300-4t2x-ds-1)
and [C8300-6T-LIC-1](research-cisco-c8300-1n1s-6t-r1.1.0.md#c8300-6t-lic-1).

Sources recovered after the first run (2026-10-30), with a headless browser
(Playwright Chromium) at the user's direction: the DNA routing matrix tier
ticks ([C8300-4T2X-MX-1](research-cisco-c8300-1n1s-4t2x-r1.1.0.md#c8300-4t2x-mx-1)); the ISR 4000 data sheet PDF,
which corrected the ISR4431's typical power (65 W, not 48 W) and weight
(18.5 lb, not 28.8 lb) ([ISR4431-DS-1](research-cisco-isr4431-r1.1.0.md#isr4431-ds-1)); the EOL14896 and
C8375-E-G2 data sheet PDFs (no changes); and live Cisco optics data for the
ISR4431 replacing a 2022 third-party copy ([ISR4431-OPT-2](research-cisco-isr4431-r1.1.0.md#isr4431-opt-2)).
