# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A documentation-only Markdown guide, "Claude Code Multi-Agent & Workflow Guide", for system engineers new to Claude Code. There is nothing to build or test. This directory is its own git repository (remote `origin` → `git@github.com:scufflegrits/claude-guide.git`, branch `main`) and is also checked out inside the parent `~/projects/guides` workspace, whose `CLAUDE.md` also applies (notably: run `~/.venv/bin/mdformat <file>` after editing any `.md` file, and it needs the `mdformat-gfm` and `mdformat-frontmatter` plugins — the front matter below is why).

## Structure

- `00-README.md` — entry point, status table, and the master table of contents.
- `INDEX.md` — detailed section-level TOC with links into each file (hand-written).
- `PROJECT.md` — project brief: audience, diagram approach. `TODO.md` — current state and open tasks.
- `01`–`12-*.md` — the content chapters, numbered in reading order. `99-appendix.md` — the appendix; `99` keeps it last, so new chapters never force a rename.

**File numbers and heading numbers differ for the early chapters.** File order matches README order, but the heading numbers inside files (`## 7.6.1`, `### 3.1`) are hand-maintained section numbers: `01` covers sections 1–2, `02`–`06` are sections 3–7 (file number + 1; `06` also has its own `## 7.5`), `07-harnesses-and-reliability.md` is section 7.6, `08`–`12` are sections 8–12 (same as the file number), and `99-appendix.md` is section 13. The "(file numbers)" column and phrase in the appendix (13.1, 13.3) mean the file prefixes, not section numbers.

## Conventions

- Every content file starts with YAML front matter: `title`, `section`, `status`, `audience`, `description`. There is no per-file tone field.
- `status` in each file's front matter must stay in sync with the status table in `00-README.md` (skeleton → draft → reviewed/done); `TODO.md` asks for that update whenever a section moves.
- Diagrams are inline Mermaid. Unfinished ones are marked `<!-- DIAGRAM: ... Status: placeholder -->`; fill them in after the surrounding prose stabilises. Follow `../mermaid/mermaid-best-practices.md` for new diagrams, and render-check with `mmdc` (see the parent `CLAUDE.md`'s Mermaid section).
- Renumbering, renaming, or reordering a heading silently breaks the anchor links in `INDEX.md` and in cross-references between files. Update `INDEX.md` in the same edit and verify with `../tools/check_anchors.py <file.md> ...` (it only checks same-file `#anchor` links, so the cross-file links in `INDEX.md` such as `01-getting-oriented.md#11-...` still need a manual check against the target headings).
- Chapters end with a `*Part of the Claude Code Guide*` footer with `Previous:` / `Next:` links; keep them consistent when inserting a chapter.

## Current state

`07-harnesses-and-reliability.md` is fully drafted: 7.6.1–7.6.7 are written and fact-checked and the chapter is `reviewed`; `TODO.md` lists the open work. All other chapters are reviewed (fact-checked against the official docs on 2026-11-01; the 01–12 reports were retired to the gitignored `99_Archive/` and remain in git history from commit `59324b8`; chapter 13's report, `13-harnesses-and-reliability-report.md`, was retired the same way and was last tracked at commit `04e4777`) and their diagrams are real, render-checked Mermaid.
