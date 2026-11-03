---
title: Appendix
section: 13
status: reviewed
audience: system engineers new to Claude Code
description: Glossary, diagram sources, and open items
---

# 13. Appendix

*Part of the Claude Code Guide*\
Previous: [Quick Reference](12-quick-reference.md)

## 13.1 Full Mermaid diagram sources

The inline diagrams in files 01, 02, 05, 06, 07 and 08 are the working sources; each carries its own `%%{init}%%` palette and follows `../mermaid/mermaid-best-practices.md`. They were render-checked with `mmdc` under both ELK and dagre (GitHub renders with dagre).

Diagram locations:

- `01-getting-oriented.md` (mental model, section 2.5)
- `02-built-in-agents.md` (agent selection, section 3.7)
- `05-dynamic-workflows.md` (pipeline vs parallel panels)
- `06-diagrams-and-decisions.md` (how workflows work, pipeline, parallel, agent selection, decision tree)
- `07-harnesses-and-reliability.md` (harness and workflow, section 7.6.1)
- `08-agent-teams.md` (architecture, section 8.2)

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
| `sub-agents.md`              | Built-in agents, custom agents, scopes, frontmatter, forks     | 2, 3, 9, 10                   |
| `skills.md`                  | Skill layout, frontmatter, `context: fork`                     | 4, 11, 12                     |
| `workflows.md`               | Dynamic workflows, `agent()`/`pipeline()`/`parallel()`, limits | 5, 6, 11, 12                  |
| `agent-teams.md`             | Experimental agent teams, enablement, display modes            | 8, 9                          |
| `cross-session-messaging.md` | `SendMessage`, `ListAgents`, peer sessions                     | 8, 9                          |
| `tools-reference.md`         | Tool names, Agent tool behavior                                | 1, 2                          |
| `context-window.md`          | Context window behavior                                        | 1                             |
| `headless.md`                | `-p` / non-interactive mode                                    | 10                            |
| `commands.md`                | Slash commands                                                 | 10                            |

- Project `PROJECT.md` for audience and writing decisions

## 13.4 Open items and future expansions

- Deeper cost modeling examples
- Advanced cross-session messaging patterns
- Additional workflow primitives edge cases
- Version-specific behavior notes
- Additional Mermaid diagrams for sections still being written (7.6.3 onward)

## 13.5 Acronyms and key terms

Terms in 13.2 (Explore, Fork, Pipeline and so on) are Claude Code features and are not repeated here. This section covers the general computing acronyms and the plain-language terms the guide relies on.

### 13.5.1 Acronyms and abbreviations

| Acronym or abbreviation | Full form                          | Meaning in this guide                                                                                        |
| ----------------------- | ---------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| API                     | Application Programming Interface  | The programmatic way to call Claude, as opposed to using the Claude Code terminal interface.                 |
| AWS                     | Amazon Web Services                | One of the cloud platforms through which Claude can be reached (as Bedrock or Claude Platform on AWS).       |
| CLI                     | Command-Line Interface             | The `claude` command run in a terminal; chapter 10 covers its flags.                                         |
| CPU                     | Central Processing Unit            | The processor; relevant when sizing how many agents or sessions a machine can run at once.                   |
| ELK                     | Eclipse Layout Kernel              | The layout engine the guide's Mermaid diagrams request; GitHub renders with dagre instead.                   |
| ID                      | Identifier                         | A unique name or number for an item such as a session or agent.                                              |
| IDE                     | Integrated Development Environment | An editor such as VS Code or JetBrains; one of the places Claude Code runs.                                  |
| JSON                    | JavaScript Object Notation         | Structured text format used for settings files and for workflow output schemas.                              |
| JWT                     | JSON Web Token                     | A signed login token; appears only as the example topic in the context-passing prompts of chapter 9.         |
| LLM                     | Large Language Model               | The kind of AI model behind Claude; "LLM gateway" is a proxy that sits between Claude Code and the model.    |
| MCP                     | Model Context Protocol             | A standard for adding custom tools to Claude Code.                                                           |
| SDK                     | Software Development Kit           | The Agent SDK, a library for running Claude Code's agent loop from your own code (non-interactive).          |
| URL                     | Uniform Resource Locator           | A web address; the guide's `Reference:` lines are URLs into the official docs.                               |
| WSL                     | Windows Subsystem for Linux        | Linux environment on Windows; cross-session messaging supports WSL 2 at the same version as Linux and macOS. |
| YAML                    | YAML Ain't Markup Language         | The format of the frontmatter block at the top of agent and skill files.                                     |

### 13.5.2 Key terms

| Term                 | Plain-language definition                                                                          | How it applies here                                                                                                   |
| -------------------- | -------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| Agentic harness      | The software around a model that gives it tools, context, permissions and a loop to run in.        | Claude Code is the harness and Claude is the model inside it; chapter 7 (7.6) builds its reliability advice on this.  |
| Barrier              | A point where work waits until every parallel task has finished.                                   | `parallel()` is barrier-style: nothing continues until all tasks return.                                              |
| Context window       | The amount of text the model can consider at once, including the conversation so far.              | Subagents and forks keep their work out of your main context window so it does not fill up.                           |
| Fan-out              | Splitting one job into many smaller jobs that run side by side.                                    | Large fan-outs in dynamic workflows multiply token cost (6.10).                                                       |
| Frontmatter          | A YAML block between `---` lines at the top of a Markdown file that configures it.                 | Custom agents, skills and every chapter of this guide use it; 12.4 is the cheat sheet.                                |
| Hook                 | A command that Claude Code runs automatically at a defined event, such as before a tool call.      | Hooks can approve or block actions, including workflow launches in non-interactive runs.                              |
| Non-interactive mode | Running Claude Code once from a script or scheduler with `claude -p` instead of in a live session. | No approval prompts are shown, so permissions must be pre-granted by rule, mode or hook; agent teams are unavailable. |
| Orchestration        | Coordinating several agents: who does what, in what order, and how results are combined.           | Dynamic workflows move the orchestration plan out of the conversation into a script.                                  |
| Permission mode      | The setting that controls which actions Claude may take without asking you.                        | Decides whether a workflow launch prompts you; see the human-checkpoint advice in 7.6.                                |
| Token                | The unit of text a model reads and writes; usage and cost are measured in tokens.                  | Every agent call consumes tokens; agent teams cost more because each teammate is a full session.                      |
| Worktree             | A separate checked-out copy of a git repository's files that shares its history.                   | `isolation: worktree` gives a subagent its own copy so it cannot overwrite your files.                                |
