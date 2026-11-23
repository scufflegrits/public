---
title: Using the Claude Code CLI
section: 10
status: reviewed
audience: system engineers new to Claude Code
description: Interactive vs headless and enabling experimental features
---

# 10. Using the Claude Code CLI

*Part of the Claude Code Guide*\
Previous: [Passing Context](09-passing-context.md) | Next: [Practical Patterns](11-practical-patterns.md)

## 10.1 Interactive vs headless (`claude -p`)

- **Interactive** (`claude`): Full support for subagents, skills, dynamic workflows, and agent teams. Agent teams are disabled until you set the variable in 10.2, and on Pro, dynamic workflows must be turned on from the Dynamic workflows row in `/config`.
- **Headless** (`claude -p`): Subagents and workflows work. Agent teams do not (they require an interactive session). No approval prompt is shown for workflows in `-p`, so launching one needs a `Workflow` or `Workflow(name)` allow rule, auto or bypass permissions mode, or a `PreToolUse` hook that returns allow; otherwise the launch is denied.

Reference: https://code.claude.com/docs/en/workflows.md ; https://code.claude.com/docs/en/headless.md

## 10.2 Enabling experimental features

Agent teams (experimental):

```bash
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1
claude
```

Or set the variable in `settings.json` under `env`.

Reference: https://code.claude.com/docs/en/agent-teams.md

## 10.3 Practical notes for system engineers

- Custom agents live in `.claude/agents/` (project) or `~/.claude/agents/` (personal). Other sources are the `--agents` flag, managed settings, and plugin `agents/` directories.
- Skills live in `.claude/skills/<name>/SKILL.md` (project) or `~/.claude/skills/<name>/SKILL.md` (personal), plus nested subdirectory `.claude/skills` folders, `--add-dir` directories, plugins, and the managed location.
- You primarily interact through one terminal session even when background agents or workflows are running.
- Check the status table in the project README for which guide sections are drafted.
