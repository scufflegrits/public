---
Title: Changelog — Windows Terminal cheat sheet
Updated: 2026-11-22
Companion: ms-terminal-cheat-sheet
---

# Changelog — Windows Terminal cheat sheet

Changes to `ms-terminal-cheat-sheet.md`, newest first. Sources are collected
in [References](#references).

## r1.0.1 — 2026-11-22

- Safety tools: added `Ctrl+Alt+Shift+P` (Mark tab as PROD) and
  `Ctrl+Alt+Shift+U` (Unmark). Both were tested live on the Windows 11 VM; see
  the settings guide's changelog, r1.0.7.

## r1.0.0 — 2026-11-22

First version: a quick reference for the annotated `settings.json` in this
folder.

- Custom chords, palette-only actions, snippets, the new-tab menu, and profile
  colors were extracted programmatically from `settings.json`, so the sheet
  matches the file exactly. [R1]
- Built-in chords come from Terminal 1.25.3131.0's `defaults.json`. Only
  chords defined there are listed, and `Alt+Shift+D` is called out as missing
  because it exists only in a fresh install's generated `settings.json`.
  [R2]
- The snippets pane, read-only mode, and reopen-closed-tab were tested live on
  the Windows 11 VM (see the settings guide's changelog, r1.0.6).
- Not verified on the VM: middle-click to close a tab, and the exact contents
  of the suggestions UI (`Ctrl+Shift+.`).

## References

- **[R1]** [`settings.json`](settings.json) in this folder, at commit
  `84d7adc`.
- **[R2]** `defaults.json` from the Windows Terminal 1.25.3131.0 package. See
  [R4] in the [settings guide's changelog](ms-terminal-json-settings-CHANGELOG.md#references).
- **[R3]** Actions reference:
  <https://learn.microsoft.com/windows/terminal/customize-settings/actions>
