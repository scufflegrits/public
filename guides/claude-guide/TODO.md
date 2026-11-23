# TODO — Claude Code Multi-Agent & Workflow Guide

## Current state

All content chapters (files 01-12) and the appendix (`99-appendix.md`) are drafted, fact-checked against the official docs, and marked `reviewed` in both the README status table and each file's front matter. The harnesses chapter (`07-harnesses-and-reliability.md`, numbered 7.6) is complete: 7.6.1-7.6.7. Its fact-check record, `13-harnesses-and-reliability-report.md`, and the reports for the other chapters are in the gitignored `99_Archive/` and in git history (01-12 from commit `59324b8`; the chapter 13 report, last tracked at commit `04e4777`).

## Immediate next step

None required. The open work below is optional; pick items as needed.

## Open work

- [ ] Review and tighten best-practices / pitfalls subsections across files (the fact-checks fixed accuracy, not length or overlap)
- [ ] Expand practical examples where they are still thin (especially workflows and fork examples)
- [ ] Decide final depth for agent teams (currently kept light)
- [ ] Check 11.4's "When it doesn't" line ("You need all results before any next stage") against 7.6.4's wording, so it doesn't read as a `pipeline()` streaming claim
- [ ] Appendix 13.3: the "Used mainly in" column uses file numbers (now in reading order, but offset from section numbers for files 02-06); consider switching it to section numbers, or keep the header note
- [ ] Re-check the undocumented behaviors listed in 7.6.7 when the docs change (`pipeline()` ordering, schema failure inside `pipeline()`, `Workflow(name)` scope, concurrent same-file edits, null final value, nested schema `items`, the `parallel()` form)
- [ ] When a section is renumbered or reordered, regenerate `INDEX.md` and run `check_anchors.py`

## Optional / later

- [ ] Add deeper cost-modeling examples (appendix placeholder)
- [ ] Expand cross-session messaging patterns
- [ ] Version-specific behavior notes
- [ ] Consider a short "When not to use these features" callout if not already strong enough
- [ ] Advanced patterns: 7.6.7 covers self-prompting and learning systems briefly. A longer treatment (critique-revise loops, evaluation feedback, storing lessons) would need its own section or appendix and a decision to broaden the guide's scope

## Workflow used for the harnesses chapter

Draft with an Opus subagent at high effort (see 4.12), fact-check with the `claude-code-guide` agent against the raw docs, apply corrections, run `mdformat` and `check_anchors.py`, update the notes, and commit after the user approves. The fact-check agent cannot write files, so the reports were saved from its returned text.

## Done

- [x] File skeletons and first-draft content for core chapters
- [x] YAML front matter on content files; status in front matter matches the README table (checked 2026-11-02)
- [x] Detailed `INDEX.md`, regenerated from chapter headings (7.6.7 heading anchor updated)
- [x] `PROJECT.md` with audience and writing decisions
- [x] Replace Mermaid diagram placeholders with full diagrams (2026-11-01): `01`, `02`, `05`, `06`, `08`, plus two in `07-harnesses-and-reliability.md`
- [x] Fact-check chapters 01-12 twice and apply corrections (2026-11-01)
- [x] Add 4.12 "Choosing a model and effort per subagent"
- [x] Resolve the numbering collision: chapter 13 renumbered from 7.5 to 7.6 (7.6.1-7.6.7); `06-diagrams-and-decisions.md` keeps its own `## 7.5`
- [x] Draft and fact-check 7.6.1-7.6.7 (2026-11-01 and 2026-11-02); chapter 13 promoted to `reviewed`
- [x] Retire the chapter 01-12 reports to `99_Archive/`
- [x] Retire the chapter 13 report to `99_Archive/` (2026-11-02)
- [x] Remove the per-file `tone` field and the visible "Tone" line (2026-11-02): it had no effect; every file was `mix`

______________________________________________________________________

*Last updated: 2026-11-02*
