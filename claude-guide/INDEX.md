---
title: Index
section: index
tone: mix
status: done
audience: system engineers new to Claude Code
description: Detailed clickable table of contents
---

# Index

Detailed table of contents with links to sections.

## 1–2. Getting Oriented

- [1.1 What Claude Code is](01-getting-oriented.md#11-what-claude-code-is)
- [1.2 The basic interaction model (you + one conversation)](01-getting-oriented.md#12-the-basic-interaction-model-you--one-conversation)
- [1.3 Why multi-agent and workflow features exist](01-getting-oriented.md#13-why-multi-agent-and-workflow-features-exist)
- [1.4 The core problem: context limits and coordination](01-getting-oriented.md#14-the-core-problem-context-limits-and-coordination)
- [1.5 How this guide is organized](01-getting-oriented.md#15-how-this-guide-is-organized)
- [2.1 The main conversation](01-getting-oriented.md#21-the-main-conversation)
- [2.2 Tools Claude can use](01-getting-oriented.md#22-tools-claude-can-use)
- [2.3 Context window basics](01-getting-oriented.md#23-context-window-basics)
- [2.4 Isolation vs. shared context](01-getting-oriented.md#24-isolation-vs-shared-context)
- [2.5 A simple mental model of agents and workflows](01-getting-oriented.md#25-a-simple-mental-model-of-agents-and-workflows)

## 3. Built-in Agents

- [3.1 Explore agent](02-built-in-agents.md#31-explore-agent)
- [3.2 Plan agent](02-built-in-agents.md#32-plan-agent)
- [3.3 General-purpose agent](02-built-in-agents.md#33-general-purpose-agent)
- [3.4 How Claude decides which agent to use](02-built-in-agents.md#34-how-claude-decides-which-agent-to-use)
- [3.5 Write access differences](02-built-in-agents.md#35-write-access-differences)
- [3.6 Other built-in helpers](02-built-in-agents.md#36-other-built-in-helpers)
- [3.7 Agent selection flowchart](02-built-in-agents.md#37-agent-selection-flowchart)
- [3.8 Best practices and pitfalls](02-built-in-agents.md#38-best-practices-and-pitfalls)

## 4. Subagents

- [4.1 What subagents are and why they exist](03-subagents.md#41-what-subagents-are-and-why-they-exist)
- [4.2 When to use a subagent](03-subagents.md#42-when-to-use-a-subagent)
- [4.3 When *not* to use a subagent](03-subagents.md#43-when-not-to-use-a-subagent)
- [4.4 Isolation: separate context and summaries](03-subagents.md#44-isolation-separate-context-and-summaries)
- [4.5 Are agent calls separate from the main conversation?](03-subagents.md#45-are-agent-calls-separate-from-the-main-conversation)
- [4.6 How long subagent tasks stay in history](03-subagents.md#46-how-long-subagent-tasks-stay-in-history)
- [4.7 The Explore agent in depth](03-subagents.md#47-the-explore-agent-in-depth)
- [4.8 Creating your first custom agent](03-subagents.md#48-creating-your-first-custom-agent)
- [4.9 Example: code-reviewer agent](03-subagents.md#49-example-code-reviewer-agent)
- [4.10 When agents are invoked](03-subagents.md#410-when-agents-are-invoked)
- [4.11 Fork mode and `/subtask`](03-subagents.md#411-fork-mode-and-subtask)
- [4.12 Choosing a model and effort per subagent](03-subagents.md#412-choosing-a-model-and-effort-per-subagent)
- [4.13 Best practices and pitfalls](03-subagents.md#413-best-practices-and-pitfalls)

## 5. Skills

- [5.1 What skills are](04-skills.md#51-what-skills-are)
- [5.2 Skills vs subagents](04-skills.md#52-skills-vs-subagents)
- [5.3 When to use skills](04-skills.md#53-when-to-use-skills)
- [5.4 When to create a skill](04-skills.md#54-when-to-create-a-skill)
- [5.5 `context: fork` vs main (inline)](04-skills.md#55-context-fork-vs-main-inline)
- [5.6 Why inline is not the default for everything](04-skills.md#56-why-inline-is-not-the-default-for-everything)
- [5.7 Using skills and subagents together](04-skills.md#57-using-skills-and-subagents-together)
- [5.8 Practical fork example](04-skills.md#58-practical-fork-example)
- [5.9 Best practices and pitfalls](04-skills.md#59-best-practices-and-pitfalls)

## 6. Dynamic Workflows

- [6.1 What dynamic workflows are](05-dynamic-workflows.md#61-what-dynamic-workflows-are)
- [6.2 Difference from agent teams](05-dynamic-workflows.md#62-difference-from-agent-teams)
- [6.3 Core primitives: `agent()`, `pipeline()`, `parallel()`, `phase()`](05-dynamic-workflows.md#63-core-primitives-agent-pipeline-parallel-phase)
- [6.4 The `pipeline()` function](05-dynamic-workflows.md#64-the-pipeline-function)
- [6.5 The `parallel()` function](05-dynamic-workflows.md#65-the-parallel-function)
- [6.6 Pros and cons of pipeline vs parallel](05-dynamic-workflows.md#66-pros-and-cons-of-pipeline-vs-parallel)
- [6.7 Simple workflow example](05-dynamic-workflows.md#67-simple-workflow-example)
- [6.8 Passing context between stages](05-dynamic-workflows.md#68-passing-context-between-stages)
- [6.9 When a script should own the plan](05-dynamic-workflows.md#69-when-a-script-should-own-the-plan)
- [6.10 Cost and token implications](05-dynamic-workflows.md#610-cost-and-token-implications)
- [6.11 Best practices and pitfalls](05-dynamic-workflows.md#611-best-practices-and-pitfalls)
- [6.12 Limits and availability](05-dynamic-workflows.md#612-limits-and-availability)

## 7. Diagrams and Decision Frameworks

- [7.1 How dynamic workflows work](06-diagrams-and-decisions.md#71-how-dynamic-workflows-work)
- [7.2 Pipeline vs parallel diagrams](06-diagrams-and-decisions.md#72-pipeline-vs-parallel-diagrams)
- [7.3 Agent selection flowchart](06-diagrams-and-decisions.md#73-agent-selection-flowchart)
- [7.4 Decision tree: which tool when](06-diagrams-and-decisions.md#74-decision-tree-which-tool-when)
- [7.5 Quick decision summary](06-diagrams-and-decisions.md#75-quick-decision-summary)

## 7.6 Agent Harnesses, Workflows, and Reliability

- [7.6.1 Difference between a harness and a workflow](13-harnesses-and-reliability.md#761-difference-between-a-harness-and-a-workflow)
- [7.6.2 Agent harnessing and reliability](13-harnesses-and-reliability.md#762-agent-harnessing-and-reliability)
- [7.6.3 Contract-first approach](13-harnesses-and-reliability.md#763-contract-first-approach)
- [7.6.4 Map-driven approach](13-harnesses-and-reliability.md#764-map-driven-approach)
- [7.6.5 How Claude Code features relate to harness ideas](13-harnesses-and-reliability.md#765-how-claude-code-features-relate-to-harness-ideas)
- [7.6.6 Best practices and pitfalls](13-harnesses-and-reliability.md#766-best-practices-and-pitfalls)
- [7.6.7 Open questions and further reading](13-harnesses-and-reliability.md#767-open-questions-and-further-reading)

## 8. Agent Teams

- [8.1 What agent teams are](07-agent-teams.md#81-what-agent-teams-are)
- [8.2 Architecture (lead, teammates, task list, mailbox)](07-agent-teams.md#82-architecture-lead-teammates-task-list-mailbox)
- [8.3 Difference from subagents](07-agent-teams.md#83-difference-from-subagents)
- [8.4 Enabling agent teams](07-agent-teams.md#84-enabling-agent-teams)
- [8.5 Limitations and experimental status](07-agent-teams.md#85-limitations-and-experimental-status)
- [8.6 When to use teams](07-agent-teams.md#86-when-to-use-teams)
- [8.7 When *not* to use teams](07-agent-teams.md#87-when-not-to-use-teams)
- [8.8 Cross-session messaging](07-agent-teams.md#88-cross-session-messaging)
- [8.9 Best practices and pitfalls](07-agent-teams.md#89-best-practices-and-pitfalls)

## 9. Passing Context

- [9.1 In the prompt](08-passing-context.md#91-in-the-prompt)
- [9.2 In dynamic workflows](08-passing-context.md#92-in-dynamic-workflows)
- [9.3 Via shared files](08-passing-context.md#93-via-shared-files)
- [9.4 With `context: fork`](08-passing-context.md#94-with-context-fork)
- [9.5 What subagents do not receive automatically](08-passing-context.md#95-what-subagents-do-not-receive-automatically)

## 10. Using the Claude Code CLI

- [10.1 Interactive vs headless (`claude -p`)](09-cli.md#101-interactive-vs-headless-claude--p)
- [10.2 Enabling experimental features](09-cli.md#102-enabling-experimental-features)
- [10.3 Practical notes for system engineers](09-cli.md#103-practical-notes-for-system-engineers)

## 11. Practical Patterns

- [11.1 Research → summarize](10-practical-patterns.md#111-research--summarize)
- [11.2 Research → implement](10-practical-patterns.md#112-research--implement)
- [11.3 Parallel review](10-practical-patterns.md#113-parallel-review)
- [11.4 Pipeline with verification](10-practical-patterns.md#114-pipeline-with-verification)
- [11.5 Custom agent for code review](10-practical-patterns.md#115-custom-agent-for-code-review)
- [11.6 When each pattern works (and when it doesn’t)](10-practical-patterns.md#116-when-each-pattern-works-and-when-it-doesnt)

## 12. Quick Reference

- [12.1 Agent comparison table](11-quick-reference.md#121-agent-comparison-table)
- [12.2 Pipeline vs parallel](11-quick-reference.md#122-pipeline-vs-parallel)
- [12.3 Skills vs subagents](11-quick-reference.md#123-skills-vs-subagents)
- [12.4 Frontmatter cheat sheet](11-quick-reference.md#124-frontmatter-cheat-sheet)
- [12.5 Common prompts](11-quick-reference.md#125-common-prompts)
- [12.6 Common pitfalls](11-quick-reference.md#126-common-pitfalls)

## 13. Appendix

- [13.1 Full Mermaid diagram sources](12-appendix.md#131-full-mermaid-diagram-sources)
- [13.2 Glossary](12-appendix.md#132-glossary)
- [13.3 Further reading](12-appendix.md#133-further-reading)
- [13.4 Open items and future expansions](12-appendix.md#134-open-items-and-future-expansions)

______________________________________________________________________

[Back to README](00-README.md)
