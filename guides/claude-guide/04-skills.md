---
title: Skills
section: 5
status: reviewed
audience: system engineers new to Claude Code
description: Skills vs subagents, context fork, and practical examples
---

# 5. Skills

*Part of the Claude Code Guide*\
Previous: [Subagents](03-subagents.md) | Next: [Dynamic Workflows](05-dynamic-workflows.md)

Skills are reusable instructions, knowledge, or workflows that Claude can load. They differ from subagents: skills add content to a context, while subagents are isolated workers that return a summary.

## 5.1 What skills are

A skill is a directory containing a `SKILL.md` file with instructions Claude can follow. Skills can be:

- Reference material
- Repeatable procedures
- Invocable workflows (for example, `/deploy`)

By default, a skill runs **inline** in the current context. You can also configure it to run in isolation.

Skill locations:

| Scope    | Path                                     |
| -------- | ---------------------------------------- |
| Project  | `.claude/skills/<skill-name>/SKILL.md`   |
| Personal | `~/.claude/skills/<skill-name>/SKILL.md` |
| Plugin   | `<plugin>/skills/<skill-name>/SKILL.md`  |

The older single-file format, `.claude/commands/<name>.md`, still works. Claude uses each skill's `description` to decide when to apply it, and you can also invoke a skill directly as `/skill-name`.

Reference: https://code.claude.com/docs/en/skills.md

## 5.2 Skills vs subagents

| Aspect         | Skill                                       | Subagent                                         |
| -------------- | ------------------------------------------- | ------------------------------------------------ |
| What it is     | Reusable instructions or workflow           | Isolated worker                                  |
| Context impact | Adds to the current context (unless forked) | Uses a separate context; only summary returns    |
| Best for       | Reference material, repeatable checklists   | Noisy research, parallel work, tool restrictions |
| Isolation      | Optional (`context: fork`)                  | Default                                          |

Skills and subagents solve different problems and are often used together.

## 5.3 When to use skills

Use a skill when:

- You have a repeatable procedure or checklist.
- You want reusable instructions that can apply in the main conversation or inside an agent.
- The content is reference material Claude should load when relevant.
- You do not need strong isolation (or you will use `context: fork` when you do).

## 5.4 When to create a skill

Create a skill when:

- You find yourself repeating the same instructions.
- A procedure should be consistent across sessions or projects.
- You want Claude to be able to invoke a named workflow.
- The knowledge is stable enough to live in a file.

## 5.5 `context: fork` vs main (inline)

- **Inline (default)**: The skill’s instructions are loaded into the current context (main conversation or the agent that invoked it).
- **`context: fork`**: The skill runs in an isolated subagent. Claude Code starts a new subagent of the type named in `agent` (default `general-purpose`) and gives it the skill content as its prompt. The subagent does **not** see your conversation history; a forked skill does not run in a fork of the current conversation. Any context it needs must come through the skill's arguments or content. It returns only a summary.

Forked skills run in the background by default (`background: true`), so the result arrives as a completion notification. Set `background: false` to have the invoking turn wait for the result.

Reference: https://code.claude.com/docs/en/skills.md

Fork is useful when the skill would otherwise add too much noise or when you want the work isolated.

## 5.6 Why inline is not the default for everything

Inline is the default because many skills are lightweight instructions or reference material that benefit from being in the current context. Forking everything would add unnecessary overhead. Use `context: fork` when isolation or cleanliness matters more than shared context.

## 5.7 Using skills and subagents together

Common patterns:

- A skill with `context: fork` and `agent: Explore` for isolated research.
- A custom subagent that has skills preloaded (the subagent `skills` field injects the full content of the listed skills at startup; built-in agents do not preload skills).
- An inline skill that describes a procedure, with a subagent handling the noisy parts.

`agent` accepts the built-in `Explore`, `Plan`, and `general-purpose` agents, or a custom agent from `.claude/agents/`. Other frontmatter fields you may meet include `disable-model-invocation`, `user-invocable`, and `arguments`.

Example frontmatter for a forked research skill:

```yaml
---
name: deep-research
description: Research a topic thoroughly and return a clean summary
context: fork
agent: Explore
---
```

## 5.8 Practical fork example

```markdown
---
name: deep-research
description: Research a topic thoroughly across the codebase and return a clean summary
context: fork
agent: Explore
---

Research $ARGUMENTS thoroughly:
1. Find relevant files using Glob and Grep
2. Read and analyze the code
3. Summarize findings with specific file paths and line numbers
4. Note any risks, open questions, or related areas
```

When invoked, this runs on the Explore agent in isolation (read-only) and returns only the summary, delivered as a background completion notification unless `background: false` is set. `$ARGUMENTS` expands to the arguments as typed; `$ARGUMENTS[N]` and `$N` select individual arguments.

## 5.9 Best practices and pitfalls

**Best practices**

- Keep skills focused.
- Use `context: fork` when the skill does heavy research or produces verbose output.
- Make the description clear so Claude knows when to use the skill.
- Prefer skills for procedures; prefer subagents for isolated workers.

**Pitfalls**

- Putting too much into an inline skill (it consumes context).
- Using a skill when a subagent’s isolation would be cleaner.
- Forgetting that a forked skill never inherits conversation history: it sees only the skill content, so pass necessary context explicitly through arguments or the skill body.
