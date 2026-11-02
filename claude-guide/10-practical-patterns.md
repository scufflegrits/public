---
title: Practical Patterns
section: 11
tone: mix
status: reviewed
audience: system engineers new to Claude Code
description: Reusable patterns and when each works
---

# 11. Practical Patterns

*Part of the Claude Code Guide*\
Previous: [Using the Claude Code CLI](09-cli.md) | Next: [Quick Reference](11-quick-reference.md)

**Tone**: Mix

## 11.1 Research → summarize

Use Explore (or a forked skill with `agent: Explore`) to investigate, then return a clean summary to the main conversation. See the [sub-agents docs](https://code.claude.com/docs/en/sub-agents.md) and [skills docs](https://code.claude.com/docs/en/skills.md).

**When it works**: Pure discovery, codebase questions, “where is X handled?”\
**When it doesn’t**: You already know the location and just need a small edit.

## 11.2 Research → implement

1. Research with Explore or Plan (Claude normally delegates to Plan while the session is in plan mode).
1. Main conversation (or General-purpose) uses the summary to make changes.

**When it works**: You need understanding before editing.\
**When it doesn’t**: The change is obvious and localized.

## 11.3 Parallel review

Fan out review tasks with `parallel()` (or multiple subagents), then synthesize. `parallel()` runs a set of agent tasks at the same time and waits for all of them. It is a primitive inside a dynamic workflow script, not a chat command; see the [workflows docs](https://code.claude.com/docs/en/workflows.md).

**When it works**: Many independent files or modules.\
**When it doesn’t**: Reviews depend on each other or share heavy context.

## 11.4 Pipeline with verification

Use `pipeline()` to run one agent per item in a list, then a final verification agent over the results. Like `parallel()`, `pipeline()` is a primitive inside a dynamic workflow script; see the [workflows docs](https://code.claude.com/docs/en/workflows.md).

**When it works**: Many items that each need the same agent treatment.\
**When it doesn’t**: You need all results before any next stage.

## 11.5 Custom agent for code review

Create `.claude/agents/code-reviewer.md` (see Subagents chapter and the [sub-agents docs](https://code.claude.com/docs/en/sub-agents.md)). Invoke explicitly or let Claude match the description.

**When it works**: Repeated review requests with consistent criteria.\
**When it doesn’t**: One-off reviews where a direct prompt is faster.

## 11.6 When each pattern works (and when it doesn’t)

| Pattern               | Works well                      | Avoid when                                                           |
| --------------------- | ------------------------------- | -------------------------------------------------------------------- |
| Research → summarize  | Noisy discovery                 | Tight iteration needed                                               |
| Research → implement  | Approach unclear                | Change is trivial                                                    |
| Parallel review       | Independent items               | Heavy shared context                                                 |
| Pipeline + verify     | One agent per item, then verify | You need every result before continuing (`parallel()` waits for all) |
| Custom reviewer agent | Repeated consistent reviews     | One-off                                                              |
