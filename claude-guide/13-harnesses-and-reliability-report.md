# Fact-check report: 13-harnesses-and-reliability.md (section 7.6)

Chapter status: **reviewed** (all of 7.6.1 to 7.6.7 drafted, fact-checked, and corrected, 2026-11-01 and 2026-11-02). This file is the record for the whole chapter; the chapter 01 to 12 reports each cover one file.

## Overview

Every section was drafted by an Opus subagent at high effort, then checked claim by claim by the `claude-code-guide` agent against the raw docs at `code.claude.com/docs/en/<page>.md`. That agent cannot write files, so the reports below were saved from its returned text. Fetches return summarized page text, so quotes are the fetch tool's rendering, not byte-verified copies. Corrections were applied before each commit.

| Section                                  | Checked    |  Claims | Confirmed | Incorrect | Unverifiable | Editorial |
| ---------------------------------------- | ---------- | ------: | --------: | --------: | -----------: | --------: |
| 7.6.1 Harness vs workflow                | 2026-11-01 |      23 |        16 |         1 |            3 |         3 |
| 7.6.2 Reliability                        | 2026-11-01 |      23 |        18 |         0 |            1 |         4 |
| 7.6.3 Contract-first                     | 2026-11-01 |      23 |        12 |         1 |            6 |         4 |
| 7.6.4 Map-driven                         | 2026-11-01 |      39 |        30 |         2 |            3 |         4 |
| 7.6.5 Features vs harness ideas          | 2026-11-01 |      59 |        46 |         2 |            3 |         8 |
| 7.6.6 Best practices and pitfalls        | 2026-11-02 |      30 |        17 |         2 |            1 |        10 |
| 7.6.7 Open questions and further reading | 2026-11-02 |      41 |        29 |         3 |            5 |         4 |
| **Total**                                |            | **238** |   **168** |    **11** |       **22** |    **37** |

"Unverifiable" mostly means the docs are silent; those items are worded as undocumented in the chapter, and the real open ones are collected in 7.6.7.

### Corrections made after a section's own check

A later section sometimes exposed an error in an earlier one. These were fixed in the chapter, not only logged here:

- **Schema validation timing (7.6.2, 7.6.3):** an early draft said the schema is validated "before the subagent starts". It is checked before the start only for provable contradictions; output is validated when the agent returns, with retries.
- **Listing guard (7.6.3, found during 7.6.4):** the worked script gained a failure exit for a null or empty role list so it matches the 7.6.4 map.
- **Forked skill and validation wording (7.6.5, found during 7.6.6):** a `context: fork` skill also gets its agent type's startup context but not the conversation; `claude -p --json-schema` is validated too; a timed-out `command` or `http` `PreToolUse` hook does not block unless `onFailure: "block"` (v2.1.295 or later).
- **`Workflow(name)` scope (7.6.2, found during 7.6.7):** the docs say "one saved workflow by name"; bundled and plugin coverage is an open question.
- **File sharing (7.6.5, 7.6.6, found during 7.6.7):** a subagent starts in the main conversation's working directory; one shared checkout is the guide's assumption.
- **Appendix 13.3:** the "Used mainly in" column uses file numbers; the header now says so.

### Still open

The undocumented behaviors the chapter could not settle are listed in 7.6.7 (`pipeline()` ordering and overlap, schema failure inside `pipeline()`, `Workflow(name)` scope, concurrent same-file edits, null final value, nested schema `items`, the `parallel()` form). Re-check them when the docs change.

Per-section reports follow.

## Fact-check: 7.6.1 Difference between a harness and a workflow (2026-11-01)

Checked 2026-11-01 against the official Claude Code docs. Scope: section 7.6.1 only (written before the rest of the chapter).

### Summary

- Claims checked: 23
- CONFIRMED: 16
- INCORRECT: 1
- UNVERIFIABLE: 3
- EDITORIAL (labeled framing, checked only for overstatement): 3

### Findings and resolution

| #   | Claim                                                                             | Verdict                | Notes                                                                                                                                                           | Status after edit |
| --- | --------------------------------------------------------------------------------- | ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| 1   | "Harness" is not a Claude Code feature, setting, or command                       | CONFIRMED              | The docs glossary has an "Agentic harness" entry naming Claude Code as the harness.                                                                             | Reworded, cited   |
| 2   | "Harness" is a general industry term from agent engineering                       | UNVERIFIABLE           | Origin not verifiable; Anthropic's docs use the term.                                                                                                           | Reworded          |
| 3   | Harness definition (tools, context, permissions, loop, verification)              | CONFIRMED              | Consistent with the glossary; verification is the guide's addition.                                                                                             | Cited             |
| 4   | Workflow definition; script-held vs lead-held plans                               | CONFIRMED              | Matches the workflows page comparison table.                                                                                                                    | No change         |
| 5   | "In this guide's framing, Claude Code itself is a harness"                        | EDITORIAL              | The glossary says "Claude Code is the harness; Claude is the model inside it", so the qualifier understated official usage.                                     | Qualifier dropped |
| 6   | Built-in tools: file operations, search, shell, web, Agent and Skill              | CONFIRMED              | On macOS and Linux, search runs through `find` and `grep` in Bash.                                                                                              | No change         |
| 7   | Permission rules and hooks                                                        | CONFIRMED              |                                                                                                                                                                 | No change         |
| 8   | Separate context window per subagent                                              | CONFIRMED              |                                                                                                                                                                 | No change         |
| 9   | Background runtime executes workflow scripts                                      | CONFIRMED              | The docs call it the workflow runtime; counting it as harness is the guide's reading.                                                                           | No change         |
| 10  | A dynamic workflow script is a workflow run by Claude Code's runtime              | CONFIRMED              |                                                                                                                                                                 | No change         |
| 11  | The script only coordinates; agents read, write, run commands                     | CONFIRMED              |                                                                                                                                                                 | No change         |
| 12  | 16 concurrent agents by default                                                   | CONFIRMED (incomplete) | Lower on machines with fewer CPUs; `CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS` accepts 1 to 256 (v2.1.269 or later).                                           | Qualified         |
| 13  | At most 1,000 agents per run                                                      | CONFIRMED              |                                                                                                                                                                 | No change         |
| 14  | The §6.12 limits are "harness limits"                                             | UNVERIFIABLE           | The docs call them runtime constraints.                                                                                                                         | Reworded          |
| 15  | A custom agent's `tools:` list is a harness constraint                            | CONFIRMED              |                                                                                                                                                                 | No change         |
| 16  | Each review agent has its own context; file contents never reach the conversation | CONFIRMED              |                                                                                                                                                                 | No change         |
| 17  | `claude -p` workflow launch needs a rule, mode, or hook                           | INCORRECT (incomplete) | Also allowed by host approval (`--permission-prompt-tool`, SDK `canUseTool`); the hook does not start a workflow in plan mode; the Agent SDK behaves like `-p`. | Corrected         |
| 18  | `pipeline()` keeps null results and the script drops them                         | CONFIRMED              |                                                                                                                                                                 | No change         |
| 19  | A saved workflow can be rerun as `/<name>`                                        | CONFIRMED              |                                                                                                                                                                 | No change         |
| 20  | "In this guide's framing, also a skill's steps"                                   | EDITORIAL              | The workflows page treats skills as Claude-driven and reserves script-driven for dynamic workflows.                                                             | Note added        |
| 21  | Fault and fix location table                                                      | UNVERIFIABLE           | Editorial reasoning, not a product claim.                                                                                                                       | No change         |
| 22  | Harness "rarely changes; set per project or user"                                 | EDITORIAL              | Labeled as the guide's suggestion.                                                                                                                              | No change         |
| 23  | Fairness of describing "harness" as a term                                        | CONFIRMED              | Understated: the glossary, the Managed Agents overview, and Anthropic's dynamic workflows post all use the term.                                                | Reworded, cited   |

Not checked: internal cross-references (6.12, 4.8, 6.7, 9.3, 10.1, 7.6.2).

### Sources

- https://code.claude.com/docs/en/glossary#agentic-harness
- https://code.claude.com/docs/en/workflows.md
- https://code.claude.com/docs/en/tools-reference.md
- https://code.claude.com/docs/en/sub-agents.md
- https://code.claude.com/docs/en/env-vars.md

## Fact-check: 7.6.2 Agent harnessing and reliability (2026-11-01)

Checked 2026-11-01 against the official Claude Code docs (workflows, sub-agents, headless, permission-modes, tools-reference, glossary).

### Summary

- Items checked: 23
- CONFIRMED: 18 (four needed qualifications)
- INCORRECT: 0
- OUTDATED: 0
- UNVERIFIABLE: 1 (the guide's own review history, checked locally against the 9.5 text and `08-passing-context-report.md`, now in git history and `99_Archive/`)
- EDITORIAL: 4 (the four reliability tests, the effort-to-stakes advice, the narrow-rule-over-bypass preference, the Plan mode sentence)

### Qualifications and edits applied

| Item                                                     | Finding                                                                                                                                                                                                                                                                        | Resolution                            |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------- |
| Stalled agent yields `null` in `parallel()`/`pipeline()` | Confirmed, but a stalled agent first restarts from the same prompt up to five times (six attempts total).                                                                                                                                                                      | Added                                 |
| `stallMs` option                                         | Exists; sets the stall window in milliseconds.                                                                                                                                                                                                                                 | Explained                             |
| `schema` returns structured output                       | Confirmed in principle, but the first wording was wrong (see the 7.6.3 report): the schema is checked before the subagent starts only for provable contradictions; output is validated after the run and fails the call after five attempts (`MAX_STRUCTURED_OUTPUT_RETRIES`). | Added                                 |
| 1,000-agent cap and `Large workflow` warning             | Confirmed; the warning is advisory and does not stop the run.                                                                                                                                                                                                                  | Added                                 |
| Approval prompt not shown headless                       | Confirmed for `claude -p` and the Agent SDK; an unapproved launch is denied; a hook approval does not start a workflow in plan mode; host callbacks also approve.                                                                                                              | Rewritten                             |
| `Workflow(name)` allow rules                             | Name-scoped rules cover saved, bundled or plugin workflows only; a one-off script needs the bare `Workflow` rule.                                                                                                                                                              | Added                                 |
| Narrow rule preferred over bypass mode                   | Editorial; bypass mode is meant for isolated environments and ignores allow rules.                                                                                                                                                                                             | Reworded as advice                    |
| Plan mode "suits work where the approach matters"        | Editorial; the docs describe plan mode only as research and proposal without edits until approval.                                                                                                                                                                             | Replaced with the documented behavior |
| Subagents do not see the parent conversation             | Confirmed; a fork is the exception.                                                                                                                                                                                                                                            | Fork note added                       |
| Custom agent `tools:` restricts tools; Explore read-only | Confirmed; `Workflow` is removed from every subagent's tool list; Explore also skips CLAUDE.md.                                                                                                                                                                                | Added                                 |
| Saved workflows rerun as `/<name>`                       | Confirmed.                                                                                                                                                                                                                                                                     | No change                             |
| Reference URLs                                           | All three cited resolve; `permission-modes.md`, `tools-reference.md` and `glossary.md` also resolve.                                                                                                                                                                           | Added to the Reference line           |

## Fact-check: 7.6.3 Contract-first approach (2026-11-01)

Checked 2026-11-01 against the official Claude Code docs (workflows, sub-agents, skills, permission-modes, tools-reference, glossary).

### Summary

- Items checked: 23
- CONFIRMED: 12
- INCORRECT: 1
- OUTDATED: 0
- UNVERIFIABLE: 6
- EDITORIAL: 4

### Findings and resolution

| #   | Claim                                                             | Verdict                                | Notes                                                                                                  | Status after edit                        |
| --- | ----------------------------------------------------------------- | -------------------------------------- | ------------------------------------------------------------------------------------------------------ | ---------------------------------------- |
| 1   | `agent(prompt, { schema })` call form                             | CONFIRMED                              | Documented, with `label` and `stallMs` as other options.                                               | No change                                |
| 2   | Schema uses `type`, `properties`, `items`, `required`             | CONFIRMED / UNVERIFIABLE (nested form) | The docs example uses a flat array of strings; nested objects inside `items` and `enum` are not shown. | Caveat added to the snippet              |
| 3   | `pipeline(list, item => agent(...))`                              | CONFIRMED                              |                                                                                                        | No change                                |
| 4   | `await agent()` with a schema returns a parsed object             | UNVERIFIABLE                           | Implied by the docs example (`found.files`), never stated.                                             | Left as is; name-matching design is safe |
| 5   | `pipeline()` results follow input order                           | UNVERIFIABLE                           | Undocumented.                                                                                          | Statement added that the docs are silent |
| 6   | The schema is validated before the subagent starts                | INCORRECT                              | Only a provable self-contradiction is caught before the start; output is validated after the run.      | Corrected here and in 7.6.2              |
| 7   | Validation retried up to five times                               | CONFIRMED (wording)                    | The docs say the call fails after five attempts; `MAX_STRUCTURED_OUTPUT_RETRIES` changes the count.    | Reworded                                 |
| 8   | `pipeline()` keeps `null` results                                 | CONFIRMED                              |                                                                                                        | No change                                |
| 9   | A stalled agent restarts up to five times                         | CONFIRMED                              | Six attempts in total.                                                                                 | No change                                |
| 10  | `stallMs` in the "On failure" row                                 | CONFIRMED / EDITORIAL                  | It only sets the stall window; it is not a failure policy.                                             | Reworded                                 |
| 11  | A `context: fork` skill gets only its content and arguments       | CONFIRMED (caveat)                     | The skill content is the prompt; the `agent` field sets model, tools and permissions.                  | No change needed                         |
| 12  | `$ARGUMENTS` substitution                                         | CONFIRMED                              |                                                                                                        | No change                                |
| 13  | A custom agent's `description` drives delegation                  | CONFIRMED                              |                                                                                                        | No change                                |
| 14  | `model` and `tools` frontmatter fields                            | CONFIRMED                              |                                                                                                        | No change                                |
| 15  | A custom agent's free-text output format is validated by nothing  | CONFIRMED by absence                   | A statement about documented behavior.                                                                 | Worded "as far as the docs describe"     |
| 16  | Tools and permission rules are enforced; prompt text is a request | CONFIRMED / EDITORIAL                  | The "request" framing is the guide's own.                                                              | Labelled "in this guide's framing"       |
| 17  | A workflow script has no direct filesystem or shell access        | CONFIRMED                              |                                                                                                        | No change                                |
| 18  | Rerunning `pipeline()` on the missing roles                       | EDITORIAL                              | Script logic, not a documented feature.                                                                | Labelled as such                         |
| 19  | Subagents do not see the parent conversation unless forked        | CONFIRMED                              |                                                                                                        | No change                                |
| 20  | Snippet header "Illustrative; exact signatures may differ"        | EDITORIAL                              | The signatures are documented; only the nested schema and return shape are unverified.                 | Header narrowed                          |
| 21  | Reference URLs                                                    | CONFIRMED                              | `workflows.md`, `sub-agents.md` and `skills.md` resolve.                                               | No change                                |

### Sources

- https://code.claude.com/docs/en/workflows.md
- https://code.claude.com/docs/en/sub-agents.md
- https://code.claude.com/docs/en/skills.md
- https://code.claude.com/docs/en/permission-modes.md
- https://code.claude.com/docs/en/tools-reference.md

## Fact-check: 7.6.4 Map-driven approach (2026-11-01)

Checked 2026-11-01 against the official Claude Code docs (workflows, headless, permission-modes, sub-agents, glossary). `permission-modes.md` and `sub-agents.md` were truncated at about 100,000 characters in the fetch; the unread tail was not needed for these claims.

### Summary

- Claims checked: 39
- CONFIRMED: 30
- INCORRECT: 2
- OUTDATED: 0
- UNVERIFIABLE: 3
- EDITORIAL: 4
- Reference URLs: 2 checked, both resolve

### Findings and resolution

| Item                                                          | Verdict                   | Notes                                                                                                                                                                                    | Status after edit         |
| ------------------------------------------------------------- | ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- |
| "The docs do not describe how items are scheduled"            | INCORRECT (overstated)    | The docs give a default cap of 16 concurrent agents and a start stagger of up to 5 seconds for agents sharing a prompt-cache prefix; item start order and result order are undocumented. | Rewritten                 |
| "The schema is validated after the run"                       | INCORRECT (minor)         | The result is checked against the schema when the agent returns, and retried until the five-attempt limit; there is no separate post-run pass.                                           | Rewritten                 |
| `pipeline()` runs one agent per item                          | CONFIRMED (qualification) | An item's callback can start more than one agent.                                                                                                                                        | Qualified                 |
| Result available once `pipeline()` returns; nulls kept        | CONFIRMED                 |                                                                                                                                                                                          | No change                 |
| `parallel()` waits for every task                             | CONFIRMED                 |                                                                                                                                                                                          | No change                 |
| `phase()`, `log()`, `args`                                    | CONFIRMED                 |                                                                                                                                                                                          | No change                 |
| `Large workflow` warning                                      | CONFIRMED (incomplete)    | More than 25 agents or a projected total above 1.5 million tokens; advisory; a chosen size guideline replaces the 25-agent threshold; `ultracode` suppresses it.                         | Token trigger added       |
| Directly awaited agent that stalls ends the run with an error | CONFIRMED                 | Up to five restarts, six attempts.                                                                                                                                                       | No change                 |
| Stalled agent inside `pipeline()` gives `null`                | CONFIRMED                 |                                                                                                                                                                                          | No change                 |
| Only the final answer returns to the main conversation        | CONFIRMED (refinement)    | Progress is visible in `/workflows` and the task panel but is not in Claude's context.                                                                                                   | Refined                   |
| How a script's return value is delivered                      | UNVERIFIABLE              | Not specified for custom scripts.                                                                                                                                                        | Not claimed               |
| Approval prompt by permission mode; absent in `claude -p`     | CONFIRMED (incomplete)    | The launch needs an allow rule, auto or bypass mode, a `PreToolUse` hook that returns allow, or a host approval.                                                                         | Added                     |
| Final `agent()` call yields `null`: "the script returns null" | UNVERIFIABLE              | The docs do not say how the run reports a null final value.                                                                                                                              | Reworded                  |
| Listing agent returns `null`: "nothing to fan out"            | EDITORIAL                 | The failure on `listed.roles` is JavaScript behavior, not documented Claude Code behavior.                                                                                               | Labelled as design advice |
| Human checkpoint outside the script                           | EDITORIAL (supported)     | The docs say there is no mid-run user input and advise running each stage as its own workflow for sign-off.                                                                              | Added                     |
| Script has no direct filesystem or shell access               | CONFIRMED                 |                                                                                                                                                                                          | No change                 |
| "Headless" wording                                            | EDITORIAL                 | The glossary now calls it non-interactive mode.                                                                                                                                          | Replaced                  |
| Reference URLs                                                | CONFIRMED                 | Both resolve; anchored workflows links and `permission-modes.md` added.                                                                                                                  | Updated                   |

### Sources

- https://code.claude.com/docs/en/workflows.md
- https://code.claude.com/docs/en/headless.md
- https://code.claude.com/docs/en/permission-modes.md
- https://code.claude.com/docs/en/glossary.md

## Fact-check: 7.6.5 How Claude Code features relate to harness ideas (2026-11-01)

Checked by the `claude-code-guide` agent against the raw docs (sub-agents, skills, hooks, memory, workflows, agent-teams, permission-modes). Limits: WebFetch returns summarized text; the tail of the skills page, hooks beyond about 200k characters, and model-config were not read.

**59 claims: 46 confirmed (5 with suggested qualifiers), 2 incorrect, 3 unverifiable, 8 editorial.**

### Incorrect or misleading (fixed)

- Hooks were said to "hold whatever the prompt says". A timed-out `PreToolUse` command, http or mcp_tool hook does not block the call unless set to fail closed (`onFailure: "block"`, v2.1.295 or later). Now stated.
- "The lead still decides what to assign" is wrong: the lead can assign tasks, or teammates self-claim the next unassigned, unblocked task. Fixed, and the experimental / off-by-default qualifier (`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`) added.
- "All three isolate context windows, not files" ignored `isolation: worktree`. Reworded to "None of the three isolates files by default", with the worktree exception.

### Qualifiers added

- 16 concurrent agents: fewer on machines with fewer CPUs; `CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS` changes it.
- CLAUDE.md in subagents: a custom subagent can set `omitClaudeMd`.
- Relaunching a stopped run: same session, or after `claude --resume`.
- Mermaid claim scoped to "the Claude Code docs pages reviewed for this guide".
- "Claude Code does not compare findings with the files" now says "as far as the docs describe".
- Guide-opinion statements (naming the agent removes the routing guess; nothing tells you which layer failed) are labeled as the guide's advice or judgment.
- Reference line extended with permission-modes and the workflows anchors for limits, stalls and resume.

### Left as is

- "`CLAUDE_CODE_EFFORT_LEVEL` outranks every other effort source" was unverifiable on model-config; it matches the order stated in 4.12.
- Approval prompt in Auto mode appears on first launch only; not added.

## Fact-check: 7.6.6 Best practices and pitfalls (2026-11-02)

Checked by the `claude-code-guide` agent against the raw docs (workflows, sub-agents, skills, hooks, memory, agent-teams, headless, permission-modes). Pages were read in chunks and fetch results are summaries.

**30 claims: 17 confirmed (7 with qualifiers), 2 incorrect, 1 unverifiable, 10 editorial.**

### Incorrect (fixed here and in 7.6.5)

- "Sees only the skill content and its arguments" for a `context: fork` skill: the subagent also gets its agent type's startup context (CLAUDE.md, and git status unless Explore or Plan). It still does not see the conversation. Fixed in 7.6.5 and 7.6.6.
- "Only a workflow `schema` is validated": `claude -p --json-schema` validates structured output too. Custom agent and skill frontmatter have no output-schema field. The workflow schema is validated when the agent returns, with retries, not "after the run". Fixed in 7.6.5 and 7.6.6.

### Qualifiers added

- Hook timeout: applies to `command` and `http` hooks; the call continues through the normal permission flow; `onFailure: "block"` needs v2.1.295 or later (7.6.5 and 7.6.6).
- Mid-run input: the script takes none, but a run pauses for agent permission prompts and usage-limit waits.
- Reruns: same orchestration, agent outputs still vary.
- File isolation: the docs do not say whether agents share files; "one checkout" is the guide's assumption.
- `claude -p`: the launch is evaluated against permission rules and denied unless pre-approved.
- `pipeline()` order: "the workflow docs do not state".
- `Workflow(name)` is described for saved workflows.
- Reference line gained permission-modes.md.

### Not changed

- Worktree detail (branches from the default branch, can be passed per call), `/fork`, and the `Large workflow` thresholds were optional and left out.
- Agent-team env var not repeated; it is in 8.4 and 7.6.5.

## Fact-check: 7.6.7 Open questions and further reading (2026-11-02)

Checked by the `claude-code-guide` agent against the raw docs (workflows, sub-agents, memory, hooks, agent-teams, skills; headless and permission-modes only partly).

**41 claims: 29 confirmed (3 are confirmed absences), 3 incorrect, 4 editorial, 5 unverifiable (undocumented, kept as open questions).**

### Incorrect (fixed)

- "Show up in `git diff`" for project-scope agent memory: new files are untracked, so they appear in `git status`. Fixed.
- "16-agent default cap": it is 16 concurrent agents, not a total. Fixed.
- "Two agents writing the same file is not described": the agent teams page warns that two teammates editing one file leads to overwrites. The docs say nothing for concurrent subagents or workflow agents. Split accordingly.

### Other changes

- Source label for `Workflow(<name>)` corrected to workflows docs, "Approve the plan before it runs" (not a headless section).
- Agent teams: experimental / off-by-default caveat added at first mention.
- Stop-hook cap: added the reset-on-tool-call rule and `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP`.
- Auto memory: note types listed (user, feedback, project, reference) and what it skips.
- `pipeline()` order: added that the resume section defines replay order only.
- Schema-failure test marked hard to reproduce; `Workflow(name)` test now names rule forms and Manual mode; null-final-value test says what to look at.
- `/workflow-authoring`: "may document some of these; not read by this guide; only when dynamic workflows are enabled".

### Related fixes in other sections

- 7.6.2 permissions row: `Workflow(name)` now says "one saved workflow by name", with bundled/plugin coverage pointed at 7.6.7.
- 7.6.5 and 7.6.6: file sharing wording now cites the docs' "starts in the main conversation's current working directory" and labels one shared checkout as the guide's assumption.
- Appendix 13.3: the "Used mainly in" column uses file numbers; the header now says so.

### Left as is

- Optional extras: `local`/`user` memory paths, `autoMemoryDirectory`, worktree base-branch detail, auto memory off in self-hosted environments.
