# Project Brief — Claude Code Multi-Agent & Workflow Guide

## Goal

Create a practical, self-contained guide for system engineers who are new to Claude Code. The guide covers multi-agent features, workflows, skills, and decision frameworks.

## Primary audience

System engineers with little or no prior Claude Code experience.

## Front matter

All content files include lightweight YAML front matter:

- title, section, tone, status, audience, description

Tone can be overridden per file by editing the `tone` field.

## Diagram approach

- Inline Mermaid diagrams.
- First-draft placeholders are acceptable and marked with `<!-- DIAGRAM: ... Status: placeholder -->`.
- Fill real diagrams after surrounding prose is stable.

## Writing order (suggested)

1. Skeleton (done)
1. High-leverage: `02-built-in-agents.md`, `03-subagents.md`, `06-diagrams-and-decisions.md`
1. Supporting: `04-skills.md`, `05-dynamic-workflows.md`, `08-passing-context.md`
1. Patterns and polish: `10-practical-patterns.md`, `11-quick-reference.md`
1. Remaining files as needed

## Status

See status table in `00-README.md`.

## New section

- 7.6 Agent Harnesses, Workflows, and Reliability (`13-harnesses-and-reliability.md`)
  - Includes separate subsections for Contract-first (7.6.3) and Map-driven (7.6.4) approaches.
