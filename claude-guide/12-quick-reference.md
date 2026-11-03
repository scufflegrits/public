---
title: Quick Reference
section: 12
status: reviewed
audience: system engineers new to Claude Code
description: Comparison tables, cheat sheets, and common pitfalls
---

# 12. Quick Reference

*Part of the Claude Code Guide*\
Previous: [Practical Patterns](11-practical-patterns.md) | Next: [Appendix](99-appendix.md)

## 12.1 Agent comparison table

| Agent             | Write access | Best for                   | Notes                                                                                                                                        |
| ----------------- | ------------ | -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Explore           | No           | Fast research              | Skips CLAUDE.md                                                                                                                              |
| Plan              | No           | Research in plan mode      | Skips CLAUDE.md                                                                                                                              |
| General-purpose   | Yes          | Research + changes         | Full tools                                                                                                                                   |
| Main conversation | Yes          | Coordination & simple work | Your primary session                                                                                                                         |
| Custom agent      | Configurable | Specialized tasks          | Defined in `.claude/agents/` (project); also `~/.claude/agents/` (user), `--agents` CLI flag, managed settings, plugin `agents/` directories |

## 12.2 Pipeline vs parallel

|          | Pipeline                     | Parallel                |
| -------- | ---------------------------- | ----------------------- |
| Behavior | One agent per item in a list | Barrier (wait for all)  |
| Best for | Many items, same treatment   | Fan-out then synthesize |

Both `pipeline()` and `parallel()` are primitives inside a dynamic workflow script, not chat commands. Both resolve only after their agents finish.

## 12.3 Skills vs subagents

|           | Skill                       | Subagent         |
| --------- | --------------------------- | ---------------- |
| Isolation | Optional (fork)             | Default          |
| Returns   | Depends (inline or summary) | Summary          |
| Best for  | Reusable instructions       | Isolated workers |

## 12.4 Frontmatter cheat sheet

**Custom agent**:

```yaml
---
name: my-agent
description: When Claude should use this agent
tools: Read, Grep, Glob
model: sonnet
effort: medium
---
```

Claude can also pass `model` per invocation, and `effort` per invocation for non-fork subagents (v2.1.292 or later). See 4.12 for the precedence order.

**Skill with fork**:

```yaml
---
name: my-skill
description: What this skill does
context: fork
agent: Explore
---
```

If `agent` is omitted when `context: fork` is set, the default is general-purpose.

## 12.5 Common prompts

- “Use the Explore agent to find all usages of X.”
- “Use the code-reviewer agent to review the latest changes.”
- “Research this in isolation and return a summary.”
- “Use a workflow to audit the codebase and cross-check findings.”

Asking for “a workflow” (or typing the `ultracode` keyword yourself at an interactive prompt) opts into a dynamic workflow; the keyword does not trigger in `-p` mode, scheduled tasks, or relayed prompts; `/workflows` and `/deep-research` are related commands described in the workflows docs.

## 12.6 Common pitfalls

- Expecting Explore or Plan to edit files.
- Assuming subagents see full conversation history.
- Using agent teams for simple work.
- Over-engineering with a workflow when one subagent suffices.
- Forgetting to pass needed context explicitly.
