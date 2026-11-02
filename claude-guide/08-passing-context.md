---
title: Passing Context
section: 9
tone: mix
status: reviewed
audience: system engineers new to Claude Code
description: How to pass context to subagents and workflow stages
---

# 9. Passing Context

*Part of the Claude Code Guide*\
Previous: [Agent Teams](07-agent-teams.md) | Next: [Using the Claude Code CLI](09-cli.md)

**Tone**: Mix

Subagents and workflow stages start with limited context. You must pass what they need.

## 9.1 In the prompt

The simplest method. Include the necessary background when you (or Claude) invoke the agent.

```
Use the code-reviewer agent to review the authentication changes.
Context: We recently migrated from sessions to JWT. Focus on token handling.
```

## 9.2 In dynamic workflows

Intermediate results live in script variables and are passed explicitly to later stages.

```javascript
const research = await agent("Find all call sites of the deprecated client");
const changes = await agent(`Update these locations:\n${JSON.stringify(research)}`);
```

`agent()` resolves to `null` when the run is stopped or hits an unrecoverable API error. The example does not handle that; production scripts should check for it.

Reference: https://code.claude.com/docs/en/workflows.md

## 9.3 Via shared files

Write context to a file, then tell the agent to read it. A workflow script has no direct filesystem or shell access (agents read, write, and run commands; the script only coordinates them), so have an agent write the file.

```javascript
// Conceptual
await agent(
  "Write this JSON to context/task.json: " +
  JSON.stringify({ files: [/* ... */], focus: "security" })
);
await agent("Read context/task.json and review the listed files");
```

Useful when the context is large or reused across multiple agents.

Reference: https://code.claude.com/docs/en/workflows.md

## 9.4 With `context: fork`

A fork started with `/subtask`, or by Claude when fork mode is on, inherits the full conversation. A skill with `context: fork` (a skill frontmatter field, not a subagent field) does not: it runs in a new subagent that starts with the skill content as its prompt and does not see conversation history. The name is misleading. Explicit instructions remain clearer than relying on inheritance alone.

Reference: https://code.claude.com/docs/en/sub-agents.md#fork-the-current-conversation ; https://code.claude.com/docs/en/skills.md

## 9.5 What subagents do not receive automatically

- The full parent conversation history (unless it is a fork).
- Results from other subagents (unless the coordinator passes them; subagents that Claude named at spawn time can also message each other with `SendMessage`).

What subagents **do** receive by default: the CLAUDE.md hierarchy and a git status snapshot. The exceptions are Explore and Plan, which skip both by design to stay fast and inexpensive. A custom agent that sets `omitClaudeMd: true` skips only the user, project, and local CLAUDE.md files; managed policy files and the git status snapshot still load.

Reference: https://code.claude.com/docs/en/sub-agents.md
**Rule of thumb**: If the agent needs it, put it in the prompt or pass it through the workflow script.
