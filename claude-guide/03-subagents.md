---
title: Subagents
section: 4
status: reviewed
audience: system engineers new to Claude Code
description: Isolation, custom agents, and when to use subagents
---

# 4. Subagents

*Part of the Claude Code Guide*\
Previous: [Built-in Agents](02-built-in-agents.md) | Next: [Skills](04-skills.md)

Subagents are isolated workers that Claude can spawn to handle side tasks. They run in their own context window and return only a summary to the main conversation.

## 4.1 What subagents are and why they exist

A subagent is a separate Claude instance with its own context, system prompt, and tool permissions. Claude delegates work to it; the subagent does the work independently; and only the final result comes back.

They exist primarily to keep the main conversation clean. Research that would otherwise dump dozens of file reads or search results into your session can happen in isolation.

## 4.2 When to use a subagent

Use a subagent when:

- The task is research-heavy and would flood the main conversation with intermediate results.
- You want isolation (the subagent should not see or be affected by the full conversation history).
- The work is self-contained and only the summary matters.
- You need to restrict tools (for example, read-only).

## 4.3 When *not* to use a subagent

Avoid a subagent when:

- The task is simple and tightly coupled to what you are already doing.
- You need back-and-forth iteration with low latency.
- The steps share a lot of context that would be lossy to summarize.
- A skill (inline) would be lighter and sufficient.

## 4.4 Isolation: separate context and summaries

- Each subagent starts with a fresh context (unless it is a fork).
- It does not automatically see the parent conversation history.
- Intermediate tool output stays inside the subagent.
- Only a summary (or final result) returns to the main conversation.

This is the main benefit: your context window stays usable.

## 4.5 Are agent calls separate from the main conversation?

Yes. Agent calls run separately. The main conversation receives the result, but the detailed work does not accumulate in your session.

## 4.6 How long subagent tasks stay in history

Subagent transcripts are stored on disk at `~/.claude/projects/{project}/{sessionId}/subagents/agent-{agentId}.jsonl` and are cleaned up after a default of 30 days (governed by `cleanupPeriodDays`). They do not permanently expand your main conversation history.

Reference: https://code.claude.com/docs/en/sub-agents.md

## 4.7 The Explore agent in depth

Explore is the built-in read-only subagent you will see most often.

- Read-only and uses the main conversation’s model (see 3.1).
- Write and Edit denied.
- Supports thoroughness levels (quick / medium / very thorough).
- Skips CLAUDE.md and git status.
- Claude can delegate to it automatically when it needs to search or understand code without making changes.

## 4.8 Creating your first custom agent

Custom agents are Markdown files with YAML frontmatter.

Location:

- Project: `.claude/agents/your-agent.md`
- Personal: `~/.claude/agents/your-agent.md`

When the same agent name exists in several places, scope priority is: managed settings, then the `--agents` flag, then `.claude/agents/`, then `~/.claude/agents/`, then a plugin’s `agents/` directory.

Minimal example:

```markdown
---
name: code-reviewer
description: Reviews code for bugs and security issues. Use when the user asks for a code review.
tools: Read, Grep, Glob
model: sonnet
---

You are a senior code reviewer.
Focus on bugs, security, and maintainability.
Return findings with file paths and severity.
```

The `description` field is what Claude uses to decide when to invoke the agent.

## 4.9 Example: code-reviewer agent

See the example above. Once the file is in place, you can say “Use the code-reviewer agent to review the latest changes” or simply request a review and let Claude choose it.

Documented defaults worth knowing (these can change between releases): subagents spawned from the main conversation start in the background unless configured otherwise; nesting is allowed up to three layers below the main conversation (`CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH`); and up to 20 subagents run concurrently by default (`CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS`).

Reference: https://code.claude.com/docs/en/sub-agents.md

## 4.10 When agents are invoked

- **Automatic**: Claude matches the task to an agent’s description.
- **Explicit**: You name the agent in your prompt, @-mention it, or start a session with `claude --agent` (or the `agent` setting).
- **Mode-based**: Plan mode prefers the Plan agent; in normal mode, this guide’s heuristic is that pure research goes to Explore (the docs state no mode condition).
- **Skill + fork**: A skill with `context: fork` runs in a fresh, isolated subagent (not a fork of your conversation; see 4.11).

## 4.11 Fork mode and `/subtask`

A fork is a subagent that inherits the current conversation context instead of starting completely fresh.

- Started with `/subtask` followed by a task, or by Claude’s own decision while fork mode is on (the default in recent releases; turn it off with `CLAUDE_CODE_FORK_SUBAGENT=0`).
- A skill with `context: fork` is not a fork: it runs in a fresh subagent that does not see the conversation history.
- Useful when the subagent needs recent conversation context.
- Still returns only a summary.

Reference: https://code.claude.com/docs/en/sub-agents.md

## 4.12 Choosing a model and effort per subagent

A subagent does not have to run on the same model as your main conversation. You can pick a cheaper model for mechanical work and a stronger one, at higher effort, for work that needs careful reasoning.

**Model.** Claude Code chooses a subagent's model in this order, first match wins:

1. The `model` parameter Claude passes for that one invocation. It takes an alias only: `sonnet`, `opus`, `haiku`, or `fable`.
1. The `model` field in the agent definition's frontmatter: an alias, a full model ID, or `inherit` (use the main conversation's model).
1. The `CLAUDE_CODE_SUBAGENT_MODEL` environment variable, when set to a model alias or ID.
1. The main conversation's model.

Before v2.1.251 the environment variable ranked first. Setting `CLAUDE_CODE_SUBAGENT_MODEL_FORCE=1` (v2.1.257 or later) applies the variable to every subagent, teammate, and workflow agent, overriding definitions and per-call choices. If only the `FORCE` variable is set, subagents use the main conversation's model, except the built-in Explore subagent. An installed mod's `agent.spawn` hook can also replace the per-invocation model.

**Effort.** An agent definition can set `effort` in its frontmatter (`low`, `medium`, `high`, `xhigh`, or `max`; the levels available depend on the model). For a non-fork subagent, Claude can also pass an `effort` parameter for one invocation (v2.1.292 or later). Effort resolves in this order: the `CLAUDE_CODE_EFFORT_LEVEL` environment variable, then the per-invocation parameter, then the frontmatter `effort`, then the session's effort level. There is no per-subagent thinking setting: as of v2.1.198 subagents inherit the main conversation's extended thinking configuration (earlier versions ran them with extended thinking off).

**What you can and cannot change.** As this guide reads the docs, model selection applies to the subagent itself; the docs do not describe a way for a subagent to change the parent session's model. You change the session model yourself with `/model` or `claude --model`. A skill's `model` and `effort` frontmatter applies only for the current turn; with `context: fork` the values set the forked subagent's model and effort instead.

**In practice.** Ask for it in the delegation prompt, for example: "Use a subagent on Opus at high effort to draft section 7.6.1, and a Sonnet subagent to apply the review edits." Reasonable splits, following the cost guidance in the docs:

| Work                                                   | Model direction                                 |
| ------------------------------------------------------ | ----------------------------------------------- |
| Mechanical edits, formatting, simple lookups           | Smaller model (`haiku`), lower effort           |
| Most drafting and code changes                         | `sonnet`, default effort                        |
| Conceptual writing, architecture, multi-step reasoning | `opus`, `high` effort (this guide's suggestion) |

Agent teams and dynamic workflows follow similar rules. A teammate's model comes from the spawn prompt, then its subagent definition, then `CLAUDE_CODE_SUBAGENT_MODEL`, then the lead's model, and is fixed when the teammate spawns; the `FORCE` variable skips the first two sources, and an installed `agent.spawn` mod hook or an organization's `availableModels` list can substitute a different model. Teammates inherit the lead's effort level by default. Workflow agents use the same order as subagents, and a model the script names for a stage counts as the per-invocation choice.

Reference: https://code.claude.com/docs/en/sub-agents.md#choose-a-model, https://code.claude.com/docs/en/sub-agents.md#choose-an-effort-level, https://code.claude.com/docs/en/model-config.md, https://code.claude.com/docs/en/costs.md, https://code.claude.com/docs/en/agent-teams.md, https://code.claude.com/docs/en/workflows.md

## 4.13 Best practices and pitfalls

**Best practices**

- Use subagents for noisy research.
- Give clear descriptions so Claude knows when to delegate.
- Restrict tools when you want read-only behavior.
- Pass necessary context explicitly in the prompt.

**Pitfalls**

- Assuming the subagent sees your full history (it doesn’t, unless forked).
- Using a subagent for tightly coupled, iterative work.
- Forgetting that Explore and Plan skip CLAUDE.md.
