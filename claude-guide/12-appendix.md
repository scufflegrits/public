---
title: Appendix
section: 13
tone: mix
status: reviewed
audience: system engineers new to Claude Code
description: Glossary, diagram sources, and open items
---

# 13. Appendix

*Part of the Claude Code Guide*\
Previous: [Quick Reference](11-quick-reference.md)

**Tone**: Mix

## 13.1 Full Mermaid diagram sources

The inline diagrams in chapters 01, 02, 05, 06, 07 and 13 are the working sources; each carries its own `%%{init}%%` palette and follows `../mermaid/mermaid-best-practices.md`. They were render-checked with `mmdc` under both ELK and dagre (GitHub renders with dagre).

Diagram locations:

- `01-getting-oriented.md` (mental model, section 2.5)
- `02-built-in-agents.md` (agent selection, section 3.7)
- `05-dynamic-workflows.md` (pipeline vs parallel panels)
- `06-diagrams-and-decisions.md` (how workflows work, pipeline, parallel, agent selection, decision tree)
- `07-agent-teams.md` (architecture, section 8.2)
- `13-harnesses-and-reliability.md` (harness and workflow, section 7.6.1)

## 13.2 Glossary

- **Explore**: Read-only research agent.
- **Plan**: Read-only agent used in plan mode.
- **General-purpose**: Full-tool subagent.
- **Subagent**: Isolated worker that returns a summary.
- **Skill**: Reusable instructions (inline or forked).
- **Fork**: Subagent that inherits the full conversation, system prompt, tools, and model. Its tool calls stay out of the main context, and only its final result returns.
- **Dynamic workflow**: JavaScript script written by Claude and run by a background runtime that coordinates many subagents via `agent()`, `pipeline()`, and `parallel()`.
- **Agent team**: Experimental peer sessions with shared task list and messaging. Disabled by default; enable with `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`. Requires an interactive session (not `-p`).
- **Pipeline**: Workflow primitive `pipeline()` that runs one agent per item in a list.
- **Parallel**: Workflow primitive `parallel()` that runs agent tasks at the same time and waits for all of them (barrier-style fan-out).

## 13.3 Further reading

Sources used in this guide, all under `https://code.claude.com/docs/en/`. Last verified 2026-11-01. Individual claims also carry inline `Reference:` lines.

| Page                         | Covers                                                         | Used mainly in (file numbers) |
| ---------------------------- | -------------------------------------------------------------- | ----------------------------- |
| `overview.md`                | Where Claude Code runs (terminal, IDE, desktop, web)           | 1                             |
| `sub-agents.md`              | Built-in agents, custom agents, scopes, frontmatter, forks     | 2, 3, 8, 9                    |
| `skills.md`                  | Skill layout, frontmatter, `context: fork`                     | 4, 10, 11                     |
| `workflows.md`               | Dynamic workflows, `agent()`/`pipeline()`/`parallel()`, limits | 5, 6, 10, 11                  |
| `agent-teams.md`             | Experimental agent teams, enablement, display modes            | 7, 8                          |
| `cross-session-messaging.md` | `SendMessage`, `ListAgents`, peer sessions                     | 7, 8                          |
| `tools-reference.md`         | Tool names, Agent tool behavior                                | 1, 2                          |
| `context-window.md`          | Context window behavior                                        | 1                             |
| `headless.md`                | `-p` / non-interactive mode                                    | 9                             |
| `commands.md`                | Slash commands                                                 | 9                             |

- Project `PROJECT.md` for tone and writing decisions

## 13.4 Open items and future expansions

- Deeper cost modeling examples
- Advanced cross-session messaging patterns
- Additional workflow primitives edge cases
- Version-specific behavior notes
- Additional Mermaid diagrams for sections still being written (7.6.3 onward)
