# Cisco Router Model Research

This project compares four Cisco routers for a new, multi-site enterprise
branch and WAN-edge deployment in the United States. It documents hardware,
IOS XE support, lifecycle, licensing (including offline license reporting),
features, management options, and module and optics compatibility. The
comparison is conditional where deployment requirements such as throughput,
WAN media, and budget remain undecided.

## Start here

1. Read the [comparison and recommendation](research-cisco-router-comparison-r1.1.0.md).
2. Use the individual model reports for evidence and platform-specific detail:

   - [Cisco ISR4431/K9](research-cisco-isr4431-r1.1.0.md) — lifecycle baseline; no longer orderable new.
   - [Cisco C8300-1N1S-4T2X](research-cisco-c8300-1n1s-4t2x-r1.1.0.md)
   - [Cisco C8375-E-G2](research-cisco-c8375-e-g2-r1.1.0.md)
   - [Cisco C8300-1N1S-6T](research-cisco-c8300-1n1s-6t-r1.1.0.md)

The comparison is compiled from those four reports and their registered
sources. Each report contains its own research status, software basis, source
register, evidence gaps, and references.

## Supporting material

- [`reference/`](reference/) contains source documents and dated text companions
  used by the reports. PDF companions preserve extracted page text and are
  identified as plain-text extraction, not semantic table conversion.

## Research scope and date

The research cutoff is **2026-10-30 (America/Chicago)**; some completion
follow-up sources were accessed on 2026-10-31 UTC. Check each report's status
and source register for the exact basis and access date. Findings are tied to
the stated Cisco IOS XE release and operating mode; Cisco software support,
licensing, product lifecycle, and compatibility information can change.

The ISR4431 is retained as a reference baseline, while the three current
platforms are evaluated for new purchase. This material supports a selection
decision; it does not replace confirmation of exact configuration, regional
availability, current pricing, or licensing with Cisco or an authorized
reseller.

## Editing conventions

- Keep Markdown tables compact: use one space around each cell (`| cell |
  cell |`) and short separator rows (`| --- | --- |`). Do not pad cells to
  align pipes by column width.
