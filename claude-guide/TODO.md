# TODO — Claude Code Multi-Agent & Workflow Guide

## Immediate next step

**Chapter 13 (7.6) is fully drafted and fact-checked.** Its status is `reviewed` (README table and front matter). Optional wrap-up below.

### Why

- 7.6.7 collects the open questions and the self-prompting / learning outline (kept below for reference).
- Optional wrap-up: tone pass.

### Suggested writing order for section 7.6

1. ~~7.6.1 Difference between a harness and a workflow~~ (done, fact-checked 2026-11-01)
1. ~~7.6.2 Agent harnessing and reliability~~ (done, fact-checked 2026-11-01)
1. ~~7.6.3 Contract-first approach~~ (done, fact-checked 2026-11-01)
1. ~~7.6.4 Map-driven approach~~ (done, fact-checked 2026-11-01)
1. ~~7.6.5 How Claude Code features relate to harness ideas~~ (done, fact-checked 2026-11-01)
1. ~~7.6.6 Best practices and pitfalls~~ (done, fact-checked 2026-11-02)
1. ~~7.6.7 Open questions and further reading~~ (done, fact-checked 2026-11-02)

Workflow used so far: draft with an Opus subagent at high effort (see 4.12), then fact-check with the `claude-code-guide` agent against the official docs, apply corrections, run mdformat and `check_anchors.py`, commit.

## Content still needed

- [ ] Draft the rest of `13-harnesses-and-reliability.md` (7.6.1-7.6.7 done)
- [x] Replace Mermaid diagram placeholders with full diagrams (2026-11-01), in:
  - `01-getting-oriented.md`
  - `02-built-in-agents.md`
  - `05-dynamic-workflows.md`
  - `06-diagrams-and-decisions.md`
  - `07-agent-teams.md`
- [x] Fact-check chapters 01-12 against the official docs and apply corrections (2026-11-01; the per-chapter reports are in git history, commit `59324b8` and later, and on disk in the ignored `99_Archive/`; chapter 13's report is `13-harnesses-and-reliability-report.md`)
- [ ] Review and tighten best-practices / pitfalls subsections across files
- [ ] Expand practical examples where they are still thin (especially workflows and fork examples)
- [ ] Decide final depth for agent teams (currently kept light)

## Polish and consistency

- [x] Verify all internal links and anchor links in `INDEX.md` still resolve (index regenerated from chapter headings; 97 links checked)
- [x] Resolve the numbering collision: chapter 13 renumbered from 7.5 to 7.6 (7.6.1-7.6.7) so `06-diagrams-and-decisions.md` keeps its own `## 7.5`
- [ ] Confirm YAML front matter is consistent after any renumbering
- [ ] Update status column in `00-README.md` as sections move from skeleton → partial → draft → reviewed (chapters 01-12 are Reviewed; 13 is Partial)
- [ ] Tone pass: note any files that should shift from “mix” toward engineer-to-engineer or tutorial

## Optional / later

- [ ] Add deeper cost-modeling examples (appendix placeholder)
- [ ] Expand cross-session messaging patterns
- [ ] Version-specific behavior notes
- [ ] Consider a short “When not to use these features” callout if not already strong enough

## Proposed advanced outline (for 7.6.7 or a future section)

These topics are related to harnesses and reliability but go beyond the current practical scope of the guide. Outline if we decide to expand:

### Self-prompting systems

- What “a system that prompts itself” means
- How dynamic workflows and agent teams already approximate this
- Patterns: lead agent generates follow-up tasks, script-driven recursion, verification loops that spawn new agents
- Limits and risks (runaway loops, cost, loss of human oversight)
- Claude Code primitives that support it (`agent()`, workflows, agent teams)

### Agents that remember, self-correct, and improve

- **Remember**: persistent notes, shared files, agent memory folders, cross-session messaging vs. true long-term memory
- **Fix their own mistakes**: verification agents, critique-revise loops, explicit success criteria in contracts
- **Get sharper with every run**: evaluation feedback, storing lessons, refining prompts/skills over time
- Practical Claude Code approximations vs. full self-improving systems
- When these patterns help vs. when they add fragility

### Recommendation

Keep the above as an optional expansion under 7.6.7 or a clearly marked “Advanced patterns” appendix unless the guide’s scope is intentionally broadened.

## Done

- [x] File skeletons and first-draft content for core chapters
- [x] YAML front matter on content files
- [x] Detailed `INDEX.md`
- [x] `PROJECT.md` with tone and writing decisions
- [x] New section 7.6 skeleton created (originally numbered 7.5)
- [x] Status tracking in README

______________________________________________________________________

*Last updated: 2026-11-01*
