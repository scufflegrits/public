---
Title: Changelog — VS Code settings reference
Updated: 2026-11-22
Companion: vscode-json-settings
---

# Changelog — VS Code settings reference

Changes to `vscode-json-settings.md` and the annotated `settings.json` beside
it, newest first. Each entry says what changed, why, and how it was checked.
Sources are collected in [References](#references).

## r1.1.2 — 2026-11-22

Verified on a Windows 11 test VM: Windows 11 24H2 (build 26100.9974), with
Visual Studio Code **1.146.0** (commit `69047191`) installed machine-wide
through WinGet (`Microsoft.VisualStudioCode`). The guide's reference build
stays 1.140.0; 1.146.0 was the current release when checked.

### Changed

- Front matter: `Reference build` records that the settings keys and extension
  IDs were re-checked on 1.146.0; version r1.1.2. No content corrections were
  needed.

### Verified unchanged

- **Setting keys.** Every setting key in the guide's JSON examples and in the
  annotated `settings.json` (about 150 keys) was checked against VS Code
  1.146.0:
  - Most appear verbatim in VS Code's workbench code, or in the
    `contributes.configuration` of a bundled or installed extension. [R1]
  - The nine `editor.*` keys that don't appear verbatim (for example
    `editor.cursorSurroundingLines`, `editor.linkedEditing`,
    `editor.smoothScrolling`) are registered under their bare option names,
    and VS Code adds the `editor.` prefix at runtime. [R1]
  - The other unmatched strings are not settings (file names, domains, git's
    `safe.directory`).
- **Extension IDs.** All 24 extension IDs the guide names install from the
  Marketplace with `code --install-extension`: the 21 in §13 plus
  `emilast.logfilehighlighter`, `johnpapa.vscode-peacock`, and
  `mhutchie.git-graph`. [R2]
- **Policies (§12).** The policy names `UpdateMode`, `TelemetryLevel`,
  `EnableFeedback`, `AllowedExtensions`, `ExtensionsAutoUpdate`,
  `ExtensionsAutoUpdateDelay`, `ChatAgentMode`, and `ChatMCP` exist in 1.146.0.
  No policy covers `chat.disableAIFeatures`. The ADMX/ADML templates ship in a
  `policies` folder of the installation. [R3]
- **JSON.** The annotated `settings.json` parses as JSONC.

### Not verified

- Visual and interactive behavior: font rendering, ligatures, the window title
  and color tips, Remote - SSH connections to a host.
- Linux-only paths (`/etc/vscode/policy.json`, `~/.config/Code/User`): the test
  machine was Windows.

## r1.1.1 — 2026-11-22

Committed with the annotated `settings.json` (`efd95c8`). It replaced r1.0.2;
an intermediate r1.1.0 was never committed. Later the same day the guide was
moved to `microsoft/vscode/` and the revision suffix was dropped from the
filename (`51b0f07`, `9299222`).

## r1.0.2 — 2026-10-05

Added §18, Power-user settings (`c73d70e`).

## r1.0.1 — 2026-10-05

Multi-agent review fixes (`a74af85`), the TOC expanded to linked subsections
(`09b7892`), and a clarification that JetBrains Mono ligatures live in `calt`
(`46356a8`).

## r1.0.0 — 2026-10-05

First version (`f47c261`).

## References

- **[R1] VS Code 1.146.0 sources.** String search of
  `resources\app\out\**\*.js` (including `workbench.desktop.main.js`) and of
  every bundled extension's `package.json` under
  `C:\Program Files\Microsoft VS Code\`, and of each installed extension's
  `package.json` under `%USERPROFILE%\.vscode\extensions\`. Settings reference:
  <https://code.visualstudio.com/docs/reference/default-settings>
- **[R2] Extension install.**
  `"C:\Program Files\Microsoft VS Code\bin\code.cmd" --install-extension <id>`
  for each ID, on the VM. Marketplace: <https://marketplace.visualstudio.com/vscode>
- **[R3] Policy names.** The `policy:{name:"…"}` registrations in
  `workbench.desktop.main.js` (59 names in 1.146.0), and the `policies` folder
  in the installation. <https://code.visualstudio.com/docs/setup/enterprise>
