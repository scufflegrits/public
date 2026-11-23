---
Title: Windows Terminal settings.json — Sysadmin Configuration Guide
Version: r1.0.7
Updated: 2026-11-22
Reference build: Windows Terminal 1.25 (stable, October 2026; verified on 1.25.3131.0); minimum 1.24
Companion: SSH-Sysadmin-Guide_r1.0.9, vscode-json-settings, starship-powershell-guide
Topics: Windows Terminal, settings.json, JetBrains Mono, Nerd Fonts, ligatures, SSH profiles, ssh_config, built-in SSH profile generator, JSON fragments, new tab menu folders, quake mode, global summon, actions, keybindings, color schemes, themes, production color coding, paste safety, panes, broadcast input, session logging, wt.exe, startupActions, serial console, plink, backup
---

# Windows Terminal settings.json — Sysadmin Configuration Guide

> Covers: hand-editing Windows Terminal's `settings.json` to build a daily
> administration workstation. Topics: the JetBrains Mono font (ligatures,
> weight, line height, Nerd Font variants), one profile per remote server over
> SSH, grouping dozens of hosts into new-tab-menu folders, generated host
> profiles (the built-in SSH generator compared with your own JSON fragment),
> the quake drop-down window, keyboard actions, paste safety, color-coding
> production hosts, multi-pane layouts, broadcast input, session logging, and
> backing up the configuration.
>
> **Reference build:** Windows Terminal 1.25, the current stable release in
> October 2026. Everything here also works on 1.24 except
> `"firstWindowPreference": "persistedLayout"`, which 1.24 doesn't have; use
> `"defaultProfile"` there (see [§6](#startup-and-windows)). Settings whose
> name or behavior changed in a recent release say so where they appear. If a key is
> rejected, the `$schema` validation in VS Code (see
> [§2](#2-locating-and-editing-settingsjson)) shows the name your build
> expects.
>
> SSH itself is covered in the companion `ssh/SSH-Sysadmin-Guide_r1.0.9.md`:
> key generation, the Windows `ssh-agent` service, `~/.ssh/config` syntax, jump
> hosts, and Cisco algorithm quirks. Its §32 and Appendix C give a minimal
> introduction to Windows Terminal SSH profiles, and this guide is the full
> reference built on top of them. The VS Code companion
> (`microsoft/vscode/vscode-json-settings.md`) uses the same JetBrains Mono setup
> for the editor, and the
> [Starship guide](starship-powershell-guide.md) sets up a PowerShell 7
> prompt on top of it.

## Table of Contents

- [1. Overview](#1-overview)
- [2. Locating and Editing settings.json](#2-locating-and-editing-settingsjson)
  - [Opening the file](#opening-the-file)
  - [The defaults file](#the-defaults-file)
  - [Terminal rewrites the file](#terminal-rewrites-the-file)
  - [Editing rules](#editing-rules)
- [3. Anatomy of settings.json](#3-anatomy-of-settingsjson)
- [4. Installing JetBrains Mono](#4-installing-jetbrains-mono)
  - [Choosing a variant](#choosing-a-variant)
  - [Install](#install)
  - [Verify the install and the exact family name](#verify-the-install-and-the-exact-family-name)
- [5. Font Configuration](#5-font-configuration)
  - [Font and text keys](#font-and-text-keys)
  - [Ligatures: on or off?](#ligatures-on-or-off)
- [6. Global Behavior Settings](#6-global-behavior-settings)
  - [Startup and windows](#startup-and-windows)
  - [Copy and paste safety](#copy-and-paste-safety)
  - [Tray, default terminal, and profile sources](#tray-default-terminal-and-profile-sources)
- [7. Color Schemes, Themes, and Environment Color Coding](#7-color-schemes-themes-and-environment-color-coding)
  - [Color schemes (terminal text colors)](#color-schemes-terminal-text-colors)
  - [Color-coding environments](#color-coding-environments)
  - [Themes (window and tab chrome)](#themes-window-and-tab-chrome)
- [8. Local Shell Profiles](#8-local-shell-profiles)
- [9. SSH Profiles](#9-ssh-profiles)
  - [Step 1 — put connection details in ~/.ssh/config](#step-1--put-connection-details-in-sshconfig)
  - [Step 2 — one profile per host](#step-2--one-profile-per-host)
  - [Production profile](#production-profile)
  - [Variations](#variations)
- [10. Organizing Many Hosts with newTabMenu](#10-organizing-many-hosts-with-newtabmenu)
- [11. Generated SSH Profiles](#11-generated-ssh-profiles)
  - [Option A — the built-in SSH generator](#option-a--the-built-in-ssh-generator)
  - [Option B — your own JSON fragment](#option-b--your-own-json-fragment)
  - [Generator script](#generator-script)
- [12. Quake Mode Drop-Down Terminal](#12-quake-mode-drop-down-terminal)
  - [Default behavior](#default-behavior)
  - [Customizing the hotkey and animation](#customizing-the-hotkey-and-animation)
  - [Making it always available](#making-it-always-available)
  - [A dedicated profile in the quake window](#a-dedicated-profile-in-the-quake-window)
- [13. Actions and Keybindings](#13-actions-and-keybindings)
  - [Format](#format)
  - [Recommended additions for admin work](#recommended-additions-for-admin-work)
  - [sendInput — command snippets](#sendinput--command-snippets)
- [14. Panes, Broadcast Input, and Startup Layouts](#14-panes-broadcast-input-and-startup-layouts)
  - [Broadcast input](#broadcast-input)
  - [Startup layout](#startup-layout)
  - [The same layouts from the command line or a desktop shortcut](#the-same-layouts-from-the-command-line-or-a-desktop-shortcut)
- [15. Session Logging and Evidence](#15-session-logging-and-evidence)
- [16. Backup, Version Control, and Portability](#16-backup-version-control-and-portability)
  - [Keep an annotated master copy in git](#keep-an-annotated-master-copy-in-git)
  - [What to keep out of a shared repository](#what-to-keep-out-of-a-shared-repository)
  - [Moving to another machine](#moving-to-another-machine)
- [17. Troubleshooting](#17-troubleshooting)
- [18. Verification Checklist](#18-verification-checklist)
- [Appendix A — Complete Reference settings.json](#appendix-a--complete-reference-settingsjson)
- [Appendix B — Default Keyboard Shortcuts](#appendix-b--default-keyboard-shortcuts)
- [References](#references)

______________________________________________________________________

## 1. Overview

Windows Terminal stores its whole configuration in one JSON file. Every
setting in the Settings UI (`Ctrl+,`) maps to a key in that file. Some useful
options, such as `newTabMenu` folders, `sendInput` actions, and fragment
extensions, are only practical to manage by editing the JSON directly.

The configuration in this guide follows a few principles:

| Principle | Why it matters for a sysadmin |
| -- | -- |
| `~/.ssh/config` holds connection details | A profile is just `ssh <alias>`. `scp`, `sftp`, VS Code, and Ansible share the same definitions. |
| Shared defaults live in `profiles.defaults` | The font, scrollback, and scheme are set once and inherited by every profile. |
| Production looks different | A red tab and a dark-red background make "wrong window" mistakes harder to make. |
| Large host lists are generated | One generator keeps the host list in sync with `~/.ssh/config`. |
| Paste is guarded | A stray newline in a root shell runs a command, so multi-line pastes always ask first. |

______________________________________________________________________

## 2. Locating and Editing settings.json

### Opening the file

| Method | Opens |
| -- | -- |
| `Ctrl+,` | Settings UI |
| `Ctrl+Shift+,` | `settings.json` |
| `Ctrl+Alt+,` | `defaults.json` (read-only) |
| Settings UI → **Open JSON file** | `settings.json` |

**File paths by install type:**

| Install type | Path |
| -- | -- |
| Packaged: Microsoft Store, `winget`, the GitHub `.msixbundle` | `%LOCALAPPDATA%\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json` |
| Windows Terminal Preview | `%LOCALAPPDATA%\Packages\Microsoft.WindowsTerminalPreview_8wekyb3d8bbwe\LocalState\settings.json` |
| Unpackaged: GitHub release `.zip`, Scoop, Chocolatey (per Microsoft's install docs; confirm with the check below) | `%LOCALAPPDATA%\Microsoft\Windows Terminal\settings.json` |
| Portable mode (`.portable` marker next to `WindowsTerminal.exe`) | `settings\settings.json` beside the executable |

Not sure which install you have? List whichever `settings.json` files exist:

```powershell
Get-ChildItem -Path "$env:LOCALAPPDATA\Packages\Microsoft.WindowsTerminal*\LocalState\settings.json",
                    "$env:LOCALAPPDATA\Microsoft\Windows Terminal\settings.json" -ErrorAction SilentlyContinue |
    Select-Object FullName, LastWriteTime
```

### The defaults file

`defaults.json` is read-only and holds every built-in setting, color scheme,
and keybinding. Your `settings.json` holds only your overrides. `defaults.json`
is the authoritative list of action names and default key chords for your
installed version; [Appendix B](#appendix-b--default-keyboard-shortcuts)
summarizes the chords an admin uses most.

### Terminal rewrites the file

Windows Terminal saves `settings.json` from its internal model, which drops
every `//` comment and can reorder keys. Besides a save from the Settings UI,
a rewrite can also happen **when Terminal loads the file**:

- the file contains legacy keys, which Terminal migrates (for example, old
  `"keys"`-inside-`actions` bindings, pre-1.23 setting names, or
  `experimental.rightClickContextMenu`, now `rightClickContextMenu`). A legacy
  binding for a built-in command is moved to `keybindings` and pointed at the
  built-in action ID, such as `Terminal.TogglePaneZoom`;
- `newTabMenu` entries name profiles, and Terminal stores them as GUIDs, so
  `"profile": "pve01"` becomes `"profile": "{a7d1e0b4-…}"` in the live file;
- a new dynamic or fragment profile appears and Terminal adds a stub entry for
  it;
- Terminal adds a generated menu folder, such as the SSH folder in
  [§11](#11-generated-ssh-profiles).

Treat the live `settings.json` as a generated file. Keep an **annotated master
copy** in git and copy it into place when you change it (see
[§16](#16-backup-version-control-and-portability)). The `//` comments in this
guide's examples explain the settings to you. Expect them to disappear from the
live file.

### Editing rules

- **Keep the `$schema` line.** With
  `"$schema": "https://aka.ms/terminal-profiles-schema"` at the top, VS Code
  autocompletes keys and flags misspelled ones. The published schema lags the
  code slightly, so a few newer keys (such as `font.builtinGlyphs`) show
  warnings even though they work.
- **Script against the commented master copy with PowerShell 7.** Windows
  PowerShell 5.1's `ConvertFrom-Json` rejects `//` comments and trailing
  commas; PowerShell 7 accepts comments. Leave trailing commas out of the
  master copy either way.
- **Saving reloads the file immediately.** A syntax error produces a warning
  banner, and Terminal keeps running on the last valid settings.
- **Snapshot before a large edit:**

```powershell
$wt = "$env:LOCALAPPDATA\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json"
Copy-Item $wt "$wt.$(Get-Date -Format yyyyMMdd-HHmmss).bak"
```

- **Generating GUIDs:** `[guid]::NewGuid().ToString('B')` returns the braced
  `{xxxxxxxx-...}` form that Terminal uses.
- **Full reset:** close every Terminal window, then rename `settings.json`.
  Terminal writes a fresh default file the next time it starts.

Reference: <https://learn.microsoft.com/windows/terminal/install#settings-json-file>

______________________________________________________________________

## 3. Anatomy of settings.json

```jsonc
{
    "$schema": "https://aka.ms/terminal-profiles-schema",

    // Global settings (§6, §12): flat keys at the top level
    "defaultProfile": "{...}",
    "theme": "Admin Dark",

    // Commands (§13): what an action does, with an id
    "actions": [ ],
    // Key chords (§13): bind a key to an action id
    "keybindings": [ ],

    // New-tab drop-down layout (§10)
    "newTabMenu": [ ],

    "profiles": {
        // Inherited by every profile, including generated ones (§5)
        "defaults": { },
        // Individual profiles (§8, §9)
        "list": [ ]
    },

    "schemes": [ ],   // terminal color palettes (§7)
    "themes": [ ]     // window and tab chrome (§7)
}
```

**How a profile's settings are resolved:** a key set on the profile wins.
Otherwise the value comes from `profiles.defaults`, then from the built-in
defaults. Dynamic and fragment profiles also inherit `profiles.defaults`.

> **actions vs. keybindings (1.22+):** Each entry in `actions` defines a command
> with an `id`. Each entry in `keybindings` maps a `keys` chord to that `id`.
> Files that still put `"keys"` inside an `actions` entry load fine, but
> Terminal migrates them on load and rewrites the file. All examples here use
> the split format.

______________________________________________________________________

## 4. Installing JetBrains Mono

### Choosing a variant

| Family name (`font.face`) | Ligatures | Nerd Font icons | Use when |
| -- | -- | -- | -- |
| `JetBrains Mono` | Yes | No | Plain shells, no themed prompt |
| `JetBrains Mono NL` | No | No | You want no ligatures without touching font features |
| `JetBrainsMono Nerd Font` | Yes | Yes | Oh My Posh, Starship, or Powerlevel-style prompts |
| `JetBrainsMono Nerd Font Mono` | Yes | Yes, single-cell width | Icons look clipped or overlap the next character |
| `JetBrainsMono Nerd Font Propo` | Yes | Yes, proportional width | Not for a terminal grid; listed so you can skip it |
| `JetBrainsMonoNL Nerd Font` | No | Yes | You want prompt icons without ligatures |

The first two families come from JetBrains. The Nerd Font families come from
the Nerd Fonts project; the names above are those of Nerd Fonts v3.5.1. Each
Nerd Font also has a short legacy name (`JetBrainsMono NF`, `JetBrainsMono NFM`,
`JetBrainsMono NFP`, `JetBrainsMonoNL NF`). Terminal accepts either form in
`font.face`, but the Settings UI font list shows the full name above. Confirm
the names with the check below rather than copying them from this table.

Fonts are rendered on the Windows side. A remote prompt that emits Nerd Font
icons, such as Starship on a Debian host, displays correctly only if the
Windows profile uses a Nerd Font. Nothing has to be installed on the server.
To run Starship in local PowerShell 7 tabs, with or without a Nerd Font, see
the [Starship guide](starship-powershell-guide.md).

### Install

**Option A — Official release:**

1. Download the latest zip from <https://www.jetbrains.com/lp/mono/> or
   <https://github.com/JetBrains/JetBrainsMono/releases>.
1. Extract it and open `fonts\ttf\`, which holds the static fonts. Skip
   `fonts\variable\` unless you plan to use `font.axes`.
1. Select every `.ttf` file, right-click, and choose **Install for all users**.

**Option B — Nerd Font build via Scoop:**

```powershell
scoop bucket add nerd-fonts
scoop install JetBrainsMono-NF          # "JetBrainsMono Nerd Font"
# scoop install JetBrainsMono-NF-Mono   # single-width icon variant
# (the bucket also has JetBrainsMono-NF-Propo, the proportional variant)
```

**Option C — Nerd Font zip:** download `JetBrainsMono.zip` from
<https://github.com/ryanoasis/nerd-fonts/releases> and install it the same way
as in Option A. The zip holds every variant (Nerd Font, Mono, Propo, and the
`NL` versions of each) at every weight; install only the ones you use.

> **Per-user vs. all-users fonts:** Scoop and a plain double-click install
> fonts for the current user only. That's fine if you run elevated tabs as
> the same user. If you elevate with a **separate admin account**, the
> elevated Terminal window runs as that account and uses that account's
> `settings.json` and per-user fonts. In that case, install the font for all
> users and copy your settings to that profile as well.

### Verify the install and the exact family name

`font.face` must match a family name exactly. List the installed names:

```powershell
Add-Type -AssemblyName System.Drawing
(New-Object System.Drawing.Text.InstalledFontCollection).Families |
    Where-Object Name -like '*JetBrains*' | Select-Object -ExpandProperty Name
```

This check uses GDI, so it reports legacy family names. Expect each weight as
its own family (`JetBrains Mono Medium`, `JetBrains Mono NL Thin`, and so on)
and the Nerd Fonts under their short names (`JetBrainsMono NF`,
`JetBrainsMono NFM`, `JetBrainsMonoNL NF`). For `font.face`, use the base
family: `JetBrains Mono`, or a Nerd Font's full name from the table above, which
is what Terminal's Settings UI lists. Its short name also works.

Restart Terminal after installing fonts. Running windows keep the font list
they loaded at startup.

Reference: <https://github.com/JetBrains/JetBrainsMono>

______________________________________________________________________

## 5. Font Configuration

Font settings go in `profiles.defaults`, so every profile inherits them,
including SSH and generated profiles.

```jsonc
"profiles": {
    "defaults": {
        "font": {
            "face": "JetBrains Mono",
            "size": 14,
            "weight": "normal",
            "features": {
                "calt": 1,      // contextual alternates = JetBrains Mono ligatures (=> != >= ->)
                "zero": 1       // slashed zero: 0 vs O in hostnames, serials, keys
            }
        },
        "colorScheme": "Darcula Admin",
        "intenseTextStyle": "bright",
        "cursorShape": "filledBox",
        "padding": "6, 4",
        "historySize": 20000,
        "scrollbarState": "visible"
    }
}
```

### Font and text keys

| Key | Example | Notes |
| -- | -- | -- |
| `font.face` | `"JetBrains Mono"` | Exact installed family name. Use a Nerd Font variant if your prompt needs Nerd Font icons. |
| `font.size` | `11` | Points. Decimals are allowed. Point sizes scale with each monitor's DPI, so you don't need per-monitor values. |
| `font.weight` | `"normal"` | A named weight or a number from 100 to 990. See the list below. |
| `font.features` | `{ "calt": 0 }` | OpenType features. `calt: 0` turns ligatures off, and `zero: 1` gives a slashed zero. |
| `font.axes` | `{ "wght": 450 }` | Variable-font axes. These need the variable TTF to be installed. |
| `font.cellHeight` | `"1.35"` | Line height. A unitless value is a multiple of the font size (like CSS `line-height`). See below. |
| `font.builtinGlyphs` | `true` (default) | (1.21+) Terminal draws box-drawing, block, and Powerline glyphs itself, so `tmux` and `htop` borders join up. |
| `font.colorGlyphs` | `true` (default) | (1.21+) Renders emoji in color. Set it to `false` for monochrome. |
| `intenseTextStyle` | `"bright"` | How bold output (SGR 1) is drawn: `bright`, `bold`, `all`, or `none`. |
| `historySize` | `20000` | Scrollback lines per pane (default 9001). This limits how much `exportBuffer` can capture ([§15](#15-session-logging-and-evidence)). |
| `scrollbarState` | `"visible"` | `visible`, `hidden`, or `always`. |
| `antialiasingMode` | `"grayscale"` | `grayscale` (default), `cleartype`, or `aliased`. ClearType is ignored when the background is transparent or acrylic. |

**Named weights:** `thin`, `extra-light`, `light`, `semi-light`, `normal`,
`medium`, `semi-bold`, `bold`, `extra-bold`, `black`, `extra-black`. JetBrains
Mono `medium` reads well on high-DPI displays.

**Line height:** leave `cellHeight` unset to use the font's natural line
height. Values are multiples of the font size, and most monospace fonts sit
near `1.2` naturally. JetBrains Mono is a little taller than that, so a small
value such as `1.15` makes lines *tighter*, and a value around `1.4` adds
space. `%`, `px`, and `pt` units are also accepted. `font.cellWidth` uses the
same units, but you rarely need it with JetBrains Mono.

**Built-in glyphs:** `builtinGlyphs` and `colorGlyphs` both default to `true`
and aren't yet in the published schema. List them only if you want to set
them to `false`.

### Ligatures: on or off?

JetBrains Mono's ligatures draw `!=`, `>=`, `->`, and `=>` as single glyphs.
Some admins turn them off for shell output, ACLs, and config files, where they
need to see exactly which characters were typed. A `!=` drawn as `≠` is easy
to misread in a firewall rule or an `awk` expression.

```jsonc
"font": { "face": "JetBrains Mono", "features": { "calt": 0 } }
```

As a middle ground, keep ligatures on in local shells and turn them off only
in production SSH profiles. A profile's `font` object is merged with the one in
`profiles.defaults`, so `"font": { "features": { "calt": 0 } }` is all the
profile needs.

Reference: <https://learn.microsoft.com/windows/terminal/customize-settings/profile-appearance>

______________________________________________________________________

## 6. Global Behavior Settings

These keys go at the top level of the file.

### Startup and windows

```jsonc
"defaultProfile": "{574e775e-4f2a-5b96-ac1e-a2962a402336}",   // PowerShell 7
"firstWindowPreference": "persistedLayout",
"initialCols": 140,
"initialRows": 40,
"centerOnLaunch": true,
"windowingBehavior": "useExisting",
"newTabPosition": "afterCurrentTab",
"tabWidthMode": "titleLength",
"warning.confirmCloseAllTabs": true
```

| Key | Value | Why |
| -- | -- | -- |
| `defaultProfile` | a local shell | A new tab or window should never connect to a production host on its own. |
| `firstWindowPreference` | `"persistedLayout"` | Restores tabs and panes, **but not their text**. See the warning below. |
| `windowingBehavior` | `"useExisting"` | `wt` launched from Run or a shortcut opens a tab in the existing window. |
| `newTabPosition` | `"afterCurrentTab"` | A new tab opens next to the tab you're working in. |
| `warning.confirmCloseAllTabs` | `true` | Asks before closing a window that has several tabs (sessions). |

**Start at sign-in:** in 1.25 this is not a `settings.json` key. Turn on
Settings → Startup → **Launch on machine startup**, which enables the
package's Windows startup task (`StartTerminalOnLoginTask`). Terminal drops
a `"startOnUserLogin"` key from the file when it rewrites it. You can also
check or change the task under Windows Settings → Apps → Startup. Starting at sign-in keeps the quake hotkey working
([§12](#12-quake-mode-drop-down-terminal)).

> **Warning — restoring scrollback writes it to disk:** Since 1.21,
> `"persistedWindowLayout"` restores each pane's **text** as well as the
> layout. To do that, it saves scrollback to disk under Terminal's LocalState
> folder. Output from production SSH sessions, including secrets, tokens, and
> config dumps, then sits there in plain text. In 1.25, `persistedWindowLayout`
> is a deprecated alias for `"persistedLayoutAndContent"`, and
> `"persistedLayout"` restores the layout only. **On 1.24, use
> `"defaultProfile"` instead**, because 1.24 has no layout-only option.

> **Key names by version:** 1.22 and earlier use `confirmCloseAllTabs`,
> `multiLinePasteWarning`, and `largePasteWarning`. Version 1.23 renamed them
> to `warning.*`, and Terminal migrates the old names. The 1.26 preview
> replaces `warning.confirmCloseAllTabs` with an enum, `warning.confirmOnClose`.

### Copy and paste safety

```jsonc
"copyOnSelect": false,
"copyFormatting": "none",
"trimBlockSelection": true,
"trimPaste": true,
"warning.multiLinePaste": "always",
"warning.largePaste": true,
"wordDelimiters": " /\\()\"'-:,;<>~!@#$%^&*|+=[]{}?│"
```

| Key | Value | Why |
| -- | -- | -- |
| `copyOnSelect` | `false` | Selecting text to read it shouldn't overwrite the clipboard you are about to paste from. |
| `copyFormatting` | `"none"` | Copies plain text, so ANSI colors aren't carried into tickets or chat as HTML or RTF. |
| `warning.multiLinePaste` | `"always"` | **The key safety net.** It must be `"always"`, not `true`. See the note below. |
| `warning.largePaste` | `true` | Asks before pasting more than 5 KiB. |
| `trimPaste` | `true` | Strips trailing whitespace and newlines from single-line pastes. It is skipped when the shell has bracketed paste on. |
| `wordDelimiters` | see above | Double-click selection boundaries. This list leaves out `.`, so double-clicking selects a whole IP address or FQDN. |

> **Why `"always"`:** Since 1.24, `warning.multiLinePaste` is an enum:
> `automatic`, `always`, or `never`. JSON `true` maps to `automatic`, which
> **skips the warning whenever the shell has turned on bracketed paste**. That
> includes bash 5.1 and later (Debian 13, RHEL 9/10), zsh, and PowerShell's
> PSReadLine. Under `automatic`, a multi-line paste into a remote root bash
> shell gets no prompt. Bracketed paste does keep the shell from running the
> lines as you paste them, but it can't stop you from pressing `Enter`
> afterwards. Use `"always"`.

**Right-click paste:** by default, right-clicking pastes immediately. The
profile setting `"rightClickContextMenu": true` (put it in
`profiles.defaults`) shows a menu instead. Older releases spelled it
`experimental.rightClickContextMenu`; 1.25 migrates that name. If your build
predates the rename, use the old name. That prevents an accidental
right-click from pasting into a root shell.

### Tray, default terminal, and profile sources

```jsonc
"minimizeToNotificationArea": true,
"alwaysShowNotificationIcon": true,
"disabledProfileSources": [ "Windows.Terminal.Azure", "Windows.Terminal.SSH" ]
```

- `minimizeToNotificationArea` sends minimized windows to the system tray, which
  pairs well with quake mode.
- `disabledProfileSources` hides whole groups of auto-generated profiles. Built-in
  sources include:
  - `Windows.Terminal.Wsl`
  - `Windows.Terminal.PowershellCore`
  - `Windows.Terminal.Azure`
  - `Windows.Terminal.VisualStudio`
  - `Windows.Terminal.SSH` — the 1.24+ SSH host generator. Disable it if you
    use your own generator ([§11](#11-generated-ssh-profiles)).
- **Default terminal application:** under Settings → Startup → **Default
  terminal application**, choose **Windows Terminal**. `ssh`, `pwsh`, and `cmd`
  launched from Run, Explorer, or a script then open in Terminal with your
  fonts, instead of in the legacy console host.

Reference: <https://learn.microsoft.com/windows/terminal/customize-settings/startup>
Reference: <https://learn.microsoft.com/windows/terminal/customize-settings/interaction>

______________________________________________________________________

## 7. Color Schemes, Themes, and Environment Color Coding

### Color schemes (terminal text colors)

A scheme defines the 16 ANSI colors plus the foreground, background, cursor,
and selection colors. Add schemes to the top-level `schemes` array, then
reference one by `name` from `colorScheme`. In this guide,
`profiles.defaults` sets `"colorScheme": "Darcula Admin"` for every profile,
and production profiles override it.

```jsonc
"schemes": [
    {
        "name": "Darcula Admin",
        "background": "#1E1F22",
        "foreground": "#BCBEC4",
        "cursorColor": "#CED0D6",
        "selectionBackground": "#214283",
        "black": "#1E1F22",   "brightBlack": "#5A5D63",
        "red": "#F75464",     "brightRed": "#FF7A85",
        "green": "#6AAB73",   "brightGreen": "#8BCB94",
        "yellow": "#E0BB65",  "brightYellow": "#F2D58C",
        "blue": "#56A8F5",    "brightBlue": "#7DBDF8",
        "purple": "#C77DBB",  "brightPurple": "#DB9DD0",
        "cyan": "#2AACB8",    "brightCyan": "#5CCFD9",
        "white": "#BCBEC4",   "brightWhite": "#DFE1E5"
    },
    {
        "name": "Prod Warning",
        "background": "#2A0A0A",
        "foreground": "#E6E6E6",
        "cursorColor": "#FF5555",
        "selectionBackground": "#7A1F1F",
        "black": "#0C0C0C",   "brightBlack": "#767676",
        "red": "#E74856",     "brightRed": "#FF6E7A",
        "green": "#16C60C",   "brightGreen": "#5FE85A",
        "yellow": "#F9F1A5",  "brightYellow": "#FFF8C4",
        "blue": "#3B78FF",    "brightBlue": "#7AA2FF",
        "purple": "#B4009E",  "brightPurple": "#D670C8",
        "cyan": "#61D6D6",    "brightCyan": "#9AE8E8",
        "white": "#CCCCCC",   "brightWhite": "#F2F2F2"
    }
]
```

"Darcula Admin" is a JetBrains-style palette written for this guide. Terminal
also includes built-in schemes, such as `Campbell`, `One Half Dark`,
`Tango Dark`, and `Solarized Dark`, and their values are in `defaults.json`.
You can find many more ready-made schemes at <https://windowsterminalthemes.dev>
and in the `windowsterminal/` folder of
<https://github.com/mbadolato/iTerm2-Color-Schemes>. Paste a scheme's JSON
object straight into `schemes`.

> **Readable colors:** `"adjustIndistinguishableColors": "always"` in
> `profiles.defaults` adjusts any text color that is too close to the
> background. This helps with remote tools that assume a different palette.

### Color-coding environments

Use three signals together, so a production session is obvious even when only
part of the window is visible:

| Signal | Key | Production | Non-production |
| -- | -- | -- | -- |
| Tab color | `tabColor` | `"#B00020"` | `"#2E7D32"` |
| Background | `colorScheme` | `"Prod Warning"` | `"Darcula Admin"` |
| Fixed tab title | `tabTitle` + `suppressApplicationTitle: true` | `"PROD web01"` | `"lab pve01"` |

`suppressApplicationTitle` stops the remote shell from replacing the tab title
with `user@host:~`, which would hide the `PROD` label.

> **Defense in depth:** these colors apply only when you open the session
> **from that profile**. If you type `ssh web01-prod` in a local tab, or hop to
> production from a bastion, the tab stays green or neutral. Also set a red
> prompt (`PS1`) on the production hosts themselves, so the warning travels
> with the shell and not only with the Windows profile. To fix the tab itself,
> mark it as production (below).

#### Mark a tab as production after the fact

For a session that didn't start from a production profile, two actions in
`settings.json` apply the production look to the current tab:

```jsonc
{
    "name": "Mark tab as PROD",
    "command": {
        "action": "multipleActions",
        "actions": [
            { "action": "setTabColor", "color": "#B00020" },
            { "action": "setColorScheme", "colorScheme": "Prod Warning" },
            { "action": "openTabRenamer" }
        ]
    },
    "id": "User.markProd"
},
{
    "name": "Unmark PROD tab",
    "command": {
        "action": "multipleActions",
        "actions": [
            { "action": "setTabColor" },                                  // no color = reset
            { "action": "setColorScheme", "colorScheme": "Darcula Admin" },
            { "action": "renameTab" }                                     // no title = reset
        ]
    },
    "id": "User.unmarkProd"
}
```

Press `ctrl+alt+shift+p` (or pick **Mark tab as PROD** in the Command Palette)
right after you reach production from a local tab or a bastion. The tab turns
red and the focused pane switches to the Prod Warning colors. The tab renamer
then opens, so you can type a title such as `PROD web01`. A title you type
there stays put even when the remote shell or a program sets its own window
title. `ctrl+alt+shift+u` undoes all three. It removes your typed title rather
than restoring an earlier one, so the tab then shows the profile's fixed
`tabTitle`, if it has one, or whatever title the shell has set.

- `setColorScheme` changes only the **focused pane**. In a tab with several
  panes, run it in each pane that needs it.
- The marking lasts for that tab only. Settings and profiles don't change, and
  a new tab or a reopened one starts with its profile's normal look.

### Themes (window and tab chrome)

Themes style the window frame and the tab row. This theme colors each tab with
its terminal's background, so a production tab also shows its dark-red
background color in the tab strip:

```jsonc
"theme": "Admin Dark",
"themes": [
    {
        "name": "Admin Dark",
        "window": { "applicationTheme": "dark", "useMica": false },
        "tabRow": { "background": "#18191CFF", "unfocusedBackground": "#18191CFF" },
        "tab":    { "background": "terminalBackground", "unfocusedBackground": null, "showCloseButton": "hover" }
    }
]
```

A profile's `tabColor` overrides the theme's tab color.

Reference: <https://learn.microsoft.com/windows/terminal/customize-settings/color-schemes>
Reference: <https://learn.microsoft.com/windows/terminal/customize-settings/themes>

______________________________________________________________________

## 8. Local Shell Profiles

Terminal generates PowerShell, Windows PowerShell, Command Prompt, and WSL
profiles automatically; these are called dynamic profiles. To change one, add
an entry with the same `guid` to `profiles.list`, containing only the keys you
want to change.

```jsonc
"profiles": {
    "list": [
        {
            // Dynamic PowerShell 7 profile: override only what differs
            "guid": "{574e775e-4f2a-5b96-ac1e-a2962a402336}",
            "source": "Windows.Terminal.PowershellCore",
            "name": "PowerShell",
            "commandline": "pwsh.exe -NoLogo",
            "startingDirectory": "%USERPROFILE%"
        },
        {
            // Fast-starting shell for the quake window (§12): skips $PROFILE
            "guid": "{0d6f3c55-8b2a-4f7e-a1c4-5e9b2d7f1a01}",
            "name": "PowerShell (quick)",
            "commandline": "pwsh.exe -NoLogo -NoProfile",
            "hidden": true
        },
        {
            // Elevated PowerShell. It always opens in a separate admin window (UAC prompt).
            "guid": "{3f6b1c2e-6a4d-4f0e-9d1a-0b7e5c2a9e11}",
            "name": "PowerShell (Admin)",
            "commandline": "pwsh.exe -NoLogo",
            "elevate": true,
            "icon": "🛡️",
            "tabColor": "#B26A00",
            "startingDirectory": "%SystemRoot%\\System32"
        },
        {
            // Override the dynamic WSL Debian profile: start in the Linux home directory
            "guid": "{<your Debian profile GUID>}",
            "name": "Debian (WSL)",
            "commandline": "wsl.exe -d Debian --cd ~"
        },
        {
            "guid": "{61c54bbd-c2c6-5271-96e7-009a87ff44bf}",
            "name": "Windows PowerShell",
            "hidden": true      // stays usable from actions and `wt -p`, just not listed in the menu
        }
    ]
}
```

- **GUIDs:**
  - The PowerShell 7 GUID shown above is a fixed value that Terminal assigns to
    the best PowerShell 7 install it finds, so it is the same on every machine.
  - The Windows PowerShell GUID is also fixed.
  - WSL GUIDs depend on the distribution name. Copy the GUID from the entry
    Terminal wrote in your own `settings.json`.
- **WSL distribution names:** in `wsl.exe -d <name>`, use the name that
  `wsl -l -v` shows.
- **Icons:** `icon` accepts an emoji, a path to a `.png` or `.ico` file, or an
  `ms-appx:///` URI. How emoji look depends on font fallback and on
  `font.colorGlyphs`. Image files look the same on every machine.

Reference: <https://learn.microsoft.com/windows/terminal/customize-settings/profile-general>

______________________________________________________________________

## 9. SSH Profiles

### Step 1 — put connection details in `~/.ssh/config`

The file is `%USERPROFILE%\.ssh\config`. See the SSH guide, §4 and §28 (the
Windows config file):

```sshconfig
Host pve01 pve02 pve03
    HostName %h.lab.example.net
    User root
    IdentityFile ~/.ssh/id_ed25519_lab

Host pbs01
    HostName pbs01.lab.example.net
    User root
    IdentityFile ~/.ssh/id_ed25519_lab

Host web01-prod
    HostName 10.20.0.11
    User sysadmin
    IdentityFile ~/.ssh/id_ed25519_prod
    ProxyJump bastion-prod

Host bastion-prod
    HostName bastion.prod.example.net
    User sysadmin
    IdentityFile ~/.ssh/id_ed25519_prod

Host core-sw01
    HostName 10.0.0.2
    User netadmin
    IdentityFile ~/.ssh/id_ed25519_net
    # Only if the device's IOS XE release still requires legacy algorithms.
    # See the SSH guide, §17 and Appendix A.3, before adding these.
    # KexAlgorithms +diffie-hellman-group14-sha1
    # HostKeyAlgorithms +ssh-rsa

# Defaults last: ssh_config uses the first value found for each option,
# so specific Host blocks above can override these.
Host *
    ServerAliveInterval 30
    ServerAliveCountMax 4
    IdentitiesOnly yes
```

> **`IdentitiesOnly yes`** means ssh offers only the keys named by
> `IdentityFile` (or `-i`). When neither names a key, it falls back to the
> default key files (`~/.ssh/id_ed25519` and so on). Other keys that are only
> loaded in the agent aren't offered. Give every Host block an `IdentityFile`
> line, or pass `-i` for one-off connections.

> **Keeping an idle SSH connection alive:** `ServerAliveInterval 30` makes
> OpenSSH send an encrypted keepalive after 30 seconds without data from the
> server. `ServerAliveCountMax 4` disconnects if four probes go unanswered.
> The `Host *` block above applies these settings to every SSH alias; use a
> narrower `Host` pattern if only selected servers should receive them. Set the
> interval shorter than the server's idle threshold. This can keep a connection
> alive when the server's inactivity check counts SSH transport traffic. It
> does not simulate keyboard input, reset a shell-level idle timer, or extend a
> fixed session duration. See the OpenSSH [`ssh_config`](https://man.openbsd.org/ssh_config#ServerAliveInterval)
> documentation.

### Step 2 — one profile per host

```jsonc
{
    "guid": "{a7d1e0b4-1c2f-4e0a-9b3d-1f0c2e4a5b01}",
    "name": "pve01",
    "commandline": "%SystemRoot%\\System32\\OpenSSH\\ssh.exe pve01",
    "icon": "🖥️",
    "tabTitle": "lab pve01",
    "suppressApplicationTitle": true,
    "tabColor": "#2E7D32",
    "closeOnExit": "never",
    "bellStyle": ["window", "taskbar"]
}
```

Create one profile like this for each host you open regularly. This guide's
examples also assume profiles named `pve02`, `pve03`, `pbs01`, `web01-prod`,
`bastion-prod`, and `core-sw01`.

| Key | SSH profile value | Why |
| -- | -- | -- |
| `commandline` | full `ssh.exe` path + alias | Guarantees the Windows OpenSSH client, which uses the Windows `ssh-agent` service. See the note below. |
| `closeOnExit` | `"never"` | Keeps the tab and its scrollback open even after a clean `exit`, so you can still read or export the output. The default (`automatic`) closes the tab when the exit code is 0. |
| `tabTitle` + `suppressApplicationTitle` | fixed label | Gives each tab a stable, unambiguous name ([§7](#7-color-schemes-themes-and-environment-color-coding)). |
| `bellStyle` | `["window","taskbar"]` | Flashes the tab and taskbar when a long job finishes. For example, `make; printf '\a'`. |

> **Why the full `ssh.exe` path:** if Git for Windows' Unix tools are on
> `PATH` (an install option, not the default), a bare `ssh` can resolve to
> `Git\usr\bin\ssh.exe`. That client can't use the Windows `ssh-agent`
> service, so it asks for your passphrase every time.

To reconnect a session that has ended, press `Enter` in the pane when
Terminal shows `[process exited with code …]`. Terminal reruns the profile's
command line in the same pane. `Ctrl+D` closes the pane instead.

### Production profile

```jsonc
{
    "guid": "{a7d1e0b4-1c2f-4e0a-9b3d-1f0c2e4a5b10}",
    "name": "web01-prod",
    "commandline": "%SystemRoot%\\System32\\OpenSSH\\ssh.exe web01-prod",
    "icon": "⚠️",
    "tabTitle": "PROD web01",
    "suppressApplicationTitle": true,
    "tabColor": "#B00020",
    "colorScheme": "Prod Warning",
    "font": { "features": { "calt": 0 } },
    "closeOnExit": "never"
}
```

### Variations

**Attach to a persistent tmux session.** A dropped connection then doesn't
kill your long-running job:

```jsonc
"commandline": "%SystemRoot%\\System32\\OpenSSH\\ssh.exe -t pve01 \"tmux new-session -A -s main\""
```

`-t` forces a TTY when a remote command is given. `new-session -A` attaches to
the `main` session if it exists and creates it otherwise. Use `screen -xRR main` on hosts that have only `screen`.

**Run a one-shot command and keep the shell open:**

```jsonc
{
    "name": "pve cluster status",
    "commandline": "%SystemRoot%\\System32\\OpenSSH\\ssh.exe -t pve01 \"pvecm status; pvesm status; exec bash -l\"",
    "closeOnExit": "never"
}
```

**Serial console (Cisco console cable, USB-serial).** Terminal has no built-in
serial support, so use `plink` from PuTTY (`winget install PuTTY.PuTTY`):

```jsonc
{
    "guid": "{a7d1e0b4-1c2f-4e0a-9b3d-1f0c2e4a5b20}",
    "name": "Console COM3 (9600 8N1)",
    "commandline": "plink.exe -serial COM3 -sercfg 9600,8,n,1,N",
    "icon": "🔌",
    "closeOnExit": "never"
}
```

Find the COM port with
`Get-PnpDevice -Class Ports -PresentOnly | Select-Object FriendlyName`. This
also lists USB-serial adapters, which `Win32_SerialPort` often misses. Only
one program can hold a COM port at a time. plink can't send a serial
**Break**, which Cisco ROMMON password recovery needs; for that, use the PuTTY
GUI (**Special Command → Break**).

**One-off target with no `ssh_config` entry.** With `IdentitiesOnly yes`
under `Host *`, name the target's key explicitly, and give the jump host by
its alias:

```jsonc
"commandline": "%SystemRoot%\\System32\\OpenSSH\\ssh.exe -i %USERPROFILE%\\.ssh\\id_ed25519_prod -J bastion-prod sysadmin@10.20.0.11"
```

`-i` applies only to the final host. The bastion hop is a separate ssh
connection that takes its key from the `Host bastion-prod` entry. ssh matches
`Host` patterns against the name as typed, not against `HostName`, so
`-J sysadmin@bastion.prod.example.net` would skip that entry and offer only
the default key files. A permanent `ProxyJump` entry in `~/.ssh/config`
remains the better option.

______________________________________________________________________

## 10. Organizing Many Hosts with newTabMenu

By default, the new-tab drop-down is one flat list, which gets hard to use
with 30 or more hosts. `newTabMenu` replaces it with folders.

```jsonc
"newTabMenu": [
    { "type": "profile", "profile": "PowerShell" },
    { "type": "profile", "profile": "PowerShell (Admin)" },
    { "type": "separator" },
    {
        "type": "folder",
        "name": "Proxmox",
        "icon": "🗄️",
        "entries": [
            { "type": "profile", "profile": "pve01" },
            { "type": "profile", "profile": "pve02" },
            { "type": "profile", "profile": "pve03" },
            { "type": "profile", "profile": "pbs01" }
        ]
    },
    {
        "type": "folder",
        "name": "Production",
        "icon": "⚠️",
        "entries": [
            { "type": "profile", "profile": "web01-prod" },
            { "type": "profile", "profile": "bastion-prod" }
        ]
    },
    {
        "type": "folder",
        "name": "Network",
        "icon": "🌐",
        "entries": [
            { "type": "profile", "profile": "core-sw01" },
            { "type": "profile", "profile": "Console COM3 (9600 8N1)" }
        ]
    },
    { "type": "separator" },
    {
        "type": "folder",
        "name": "Everything else",
        "inline": "never",
        "allowEmpty": false,
        "entries": [ { "type": "remainingProfiles" } ]
    }
]
```

Profiles can be referenced by `name` or `guid`. Names must match exactly. If
a name doesn't match any profile, its menu entry is silently left out.

| Entry type | Purpose |
| -- | -- |
| `profile` | One profile, by `name` or `guid`. |
| `folder` | A submenu. `inline: "auto"` flattens a folder with a single entry. `allowEmpty: false` (the default) hides an empty folder. |
| `separator` | A divider line. |
| `remainingProfiles` | Every profile not listed elsewhere. Use it so new or generated hosts never disappear from the menu. |
| `matchProfiles` | Profiles whose `name`, `commandline`, or `source` exactly matches the value you specify. Regular expressions and partial matches aren't supported. |
| `action` | (1.22+) Runs an action `id` from the menu, such as a saved pane layout. |

`matchProfiles` can select a known profile by its exact name:

```jsonc
{ "type": "folder", "name": "Generated hosts", "entries": [ { "type": "matchProfiles", "name": "ssh pve01" } ] }
```

This only matches the profile named `ssh pve01`; it does not match other
`ssh <alias>` profiles. Because fragment-generated host names vary, this
configuration leaves them to the `Everything else` folder, whose
`remainingProfiles` entry collects every profile not listed elsewhere
(see [§11](#11-generated-ssh-profiles)).

**Command Palette:** press `Ctrl+Shift+P`, choose **New tab…**, then type part
of a host name. With many hosts, this is often faster than any menu.

Reference: <https://learn.microsoft.com/windows/terminal/customize-settings/new-tab-menu>

______________________________________________________________________

## 11. Generated SSH Profiles

Once you have more than a handful of hosts, generate the profiles instead of
writing them by hand. There are two ways to do this. **Choose one.** If you run
both, and also write some profiles by hand, the same host appears two or three
times in the menu.

| Option | Profile names | Prod color coding | Multi-alias `Host a b c` lines | Control |
| -- | -- | -- | -- | -- |
| A — built-in generator (1.24+) | `SSH - <host>` | No | Broken (see below) | None |
| B — your own fragment (this §) | `ssh <alias>` | Yes | Handled | Full (script) |

### Option A — the built-in SSH generator

Starting with 1.24, Terminal reads `%ProgramData%\ssh\ssh_config` and
`~/.ssh/config` itself and creates one `SSH - <host>` profile, with source
`Windows.Terminal.SSH`, for each `Host` block that has a `HostName` line. The
first time it does this, it also adds an **SSH** folder to your `newTabMenu`.

Limitations:

- The generator treats the whole `Host` value as one name. The `Host pve01 pve02 pve03` block in [§9](#9-ssh-profiles) becomes a single broken profile
  that runs `ssh pve01 pve02 pve03`.
- Blocks that have no `HostName` line are skipped.
- There is no per-host styling, so production hosts look the same as
  everything else.
- Adding the SSH folder is one of the changes that makes Terminal rewrite
  `settings.json` ([§2](#terminal-rewrites-the-file)).

> **Observed on 1.25.3131.0:** with `Windows.Terminal.SSH` enabled and the
> [§9](#9-ssh-profiles) `~/.ssh/config` (several blocks with a `HostName` line),
> Terminal generated no `SSH - …` profiles and added no SSH folder;
> `state.json` recorded `"sshFolderGenerated": false`. Check what your build
> produces before you rely on Option A.

Option A is fine for a small `~/.ssh/config` with one alias per block. For
everything else, use Option B and turn the built-in generator off:

```jsonc
"disabledProfileSources": [ "Windows.Terminal.SSH" ]
```

### Option B — your own JSON fragment

**Fragments** are JSON files that Terminal loads in addition to
`settings.json`. A script regenerates the fragment from `~/.ssh/config`, and
your hand-edited settings are never touched.

| Scope | Path |
| -- | -- |
| Current user | `%LOCALAPPDATA%\Microsoft\Windows Terminal\Fragments\<app-name>\*.json` |
| All users | `%ProgramData%\Microsoft\Windows Terminal\Fragments\<app-name>\*.json` |

- In a fragment, `profiles` is a plain array, not the `{ "defaults", "list" }`
  object. Fragments can also contain `schemes` and (1.21+) `actions`.
- Fragment profiles inherit `profiles.defaults`, so they get the JetBrains Mono
  setup automatically.
- Terminal records each fragment profile with `"source"` set to the fragment's
  folder name (`ssh-hosts` for the script below) and adds a stub entry for it
  to `settings.json`.
- **Settings → Extensions** (1.24+) lists each fragment source and can switch it
  on or off. If your generated profiles don't appear, check there first.

### Generator script

Save the script as `Update-WtSshFragment.ps1`. It runs on Windows PowerShell
5.1 and on PowerShell 7. It also works on FIPS-mode systems (as required by
the Windows 11 STIG), because it uses the CSP SHA-256 class rather than MD5.

```powershell
<#
.SYNOPSIS
    Generate a Windows Terminal fragment with one profile per concrete Host alias in ~/.ssh/config.
.NOTES
    Handles several aliases per Host line, "Host=alias", and trailing comments.
    Skips wildcard and negated patterns (*, ?, !). Include directives are not followed.
    GUIDs are derived from the alias, so they stay the same between runs.
#>
[CmdletBinding()]
param(
    [string]$SshConfig    = (Join-Path $env:USERPROFILE '.ssh\config'),
    [string]$ProdPattern  = '(^|[-.])(prod|prd)([-.]|$)',
    [string[]]$Exclude    = @('github.com', 'gitlab.com')   # aliases that aren't shells, or that have hand-written profiles
)

if (-not (Test-Path -LiteralPath $SshConfig)) { throw "ssh config not found: $SshConfig" }

$fragDir  = Join-Path $env:LOCALAPPDATA 'Microsoft\Windows Terminal\Fragments\ssh-hosts'
$fragFile = Join-Path $fragDir 'ssh-hosts.json'
$sshExe   = '%SystemRoot%\System32\OpenSSH\ssh.exe'

# FIPS-safe on .NET Framework (5.1) and .NET (7)
$hasher = New-Object System.Security.Cryptography.SHA256CryptoServiceProvider
function Get-StableGuid([string]$Text) {
    $hash = $hasher.ComputeHash([System.Text.Encoding]::UTF8.GetBytes("wt-ssh-fragment:$Text"))
    ([guid]::new([byte[]]$hash[0..15])).ToString('B')
}

$aliases = foreach ($line in Get-Content -LiteralPath $SshConfig -Encoding UTF8 -ErrorAction Stop) {
    if ($line -match '^\s*Host(?:\s*=\s*|\s+)([^#]+)') {
        $Matches[1].Trim() -split '\s+' | Where-Object { $_ -and $_ -notmatch '[*?!"]' }
    }
}
$aliases = @($aliases | Where-Object { $_ -notin $Exclude } | Sort-Object -Unique)

$vs16       = [string][char]0xFE0F                                # emoji presentation selector
$iconServer = [char]::ConvertFromUtf32(0x1F5A5) + $vs16           # desktop computer
$iconProd   = [string][char]0x26A0 + $vs16                        # warning sign

$profiles = foreach ($alias in $aliases) {
    $isProd = $alias -match $ProdPattern
    $p = [ordered]@{
        guid                     = Get-StableGuid $alias
        name                     = "ssh $alias"
        commandline              = "$sshExe $alias"
        tabTitle                 = $(if ($isProd) { "PROD $alias" } else { $alias })
        suppressApplicationTitle = $true
        icon                     = $(if ($isProd) { $iconProd } else { $iconServer })
        closeOnExit              = 'never'
    }
    if ($isProd) {
        $p.tabColor    = '#B00020'
        $p.colorScheme = 'Prod Warning'
    }
    $p
}

New-Item -ItemType Directory -Force -Path $fragDir | Out-Null
$json = [ordered]@{ profiles = @($profiles) } | ConvertTo-Json -Depth 5
[System.IO.File]::WriteAllText($fragFile, $json, (New-Object System.Text.UTF8Encoding($false)))   # UTF-8, no BOM

Write-Host "Wrote $($aliases.Count) profiles to $fragFile"
```

Run the script after each edit to `~/.ssh/config`, then reopen Terminal or
save `settings.json` to reload. Pass the hosts that already have hand-written
profiles to `-Exclude` so they don't appear twice.

Run it from inside a PowerShell session, not with `pwsh -File`. Under
`-File`, PowerShell passes each argument as a literal string and doesn't build
arrays from comma lists. `-Exclude` would receive only `"github.com,"`, and
`pve01,` would bind by position to `-SshConfig`, so the script would stop with
"ssh config not found".

```powershell
# From a PowerShell 7 or Windows PowerShell 5.1 prompt
.\Update-WtSshFragment.ps1 -Exclude github.com, pve01, pbs01, web01-prod, core-sw01

# Windows PowerShell 5.1 when the execution policy blocks scripts
# (Windows 11's default): allow local scripts for this process only
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\Update-WtSshFragment.ps1 -Exclude github.com, pve01, pbs01, web01-prod, core-sw01

# From cmd.exe, Task Scheduler, or a shortcut: use -Command so the list is parsed
pwsh -NoProfile -Command "& .\Update-WtSshFragment.ps1 -Exclude github.com, pve01, pbs01, web01-prod, core-sw01"

# Check: list the generated profiles
(Get-Content "$env:LOCALAPPDATA\Microsoft\Windows Terminal\Fragments\ssh-hosts\ssh-hosts.json" -Raw -Encoding UTF8 |
    ConvertFrom-Json).profiles | Select-Object name, tabTitle, colorScheme
```

Reference: <https://learn.microsoft.com/windows/terminal/json-fragment-extensions>

______________________________________________________________________

## 12. Quake Mode Drop-Down Terminal

Quake mode opens a terminal that drops down from the top of the screen on a
global hotkey and hides when you press the hotkey again, even if another
application has focus. It is handy for a quick `ping`, `nslookup`, or
`Test-NetConnection` without hunting for the main window.

### Default behavior

Windows Terminal includes a `quakeMode` action, bound by default to
`win+sc(41)`. That chord is `` Win+` `` on a US keyboard; it is bound by scan
code, so it works on every keyboard layout. The quake window:

- is a special window named `_quake`, and only one exists at a time;
- docks to the top of the monitor at full width, and you can resize only its
  bottom edge;
- always runs in **focus mode**, with no tab row. Tabs still work:
  `Ctrl+Shift+T` opens one, `Ctrl+Tab` switches, and the Command Palette works;
- opens the **default profile** when Terminal first creates it.

### Customizing the hotkey and animation

`quakeMode` is shorthand for `globalSummon` with `"name": "_quake"` and a 200
ms drop-down. To tune the summon behavior, define it explicitly. Binding it to
the same chord replaces the default:

```jsonc
"actions": [
    {
        "command": {
            "action": "globalSummon",
            "name": "_quake",
            "dropdownDuration": 150,
            "toggleVisibility": true,
            "monitor": "toMouse",
            "desktop": "toCurrent"
        },
        "id": "User.quakeToggle"
    }
],
"keybindings": [
    { "id": "User.quakeToggle", "keys": "win+sc(41)" }
]
```

| Argument | Values | Effect |
| -- | -- | -- |
| `name` | `"_quake"` | This exact name makes it a quake window. Any other name summons an ordinary named window. |
| `dropdownDuration` | milliseconds; `0` = none | How long the slide-down animation takes. |
| `toggleVisibility` | `true` / `false` | Pressing the hotkey while the window is focused hides it again. |
| `monitor` | `toCurrent`, `toMouse`, `any` | `toMouse` follows the mouse pointer between monitors. |
| `desktop` | `toCurrent`, `onCurrent`, `any` | `toCurrent` moves the window to the active virtual desktop. |

**Hotkey conflicts:** a global hotkey can belong to only one program. If
PowerToys, a screen recorder, or a VPN client already owns the chord, the
binding silently does nothing. Pick another chord, such as
`ctrl+alt+sc(41)`.

### Making it always available

The hotkey is registered by a running Terminal process. To keep it working,
turn on Settings → Startup → **Launch on machine startup**
([§6](#startup-and-windows)) and set:

```jsonc
"minimizeToNotificationArea": true,
"alwaysShowNotificationIcon": true
```

- While any Terminal window exists, including a hidden quake window, the
  hotkey works.
- `"compatibility.allowHeadless": true` keeps the process running after the
  last window closes. Microsoft's documentation still marks it as a preview
  setting, so check that your build honors it.
- `"autoHideWindow": true` hides a window as soon as it loses focus, like a
  classic Quake console. It is a global setting and applies to **every**
  Terminal window, so enable it only if you work almost entirely in the
  quake window.

### A dedicated profile in the quake window

The quake window opens the default profile. To start it with another profile,
such as `PowerShell (quick)` from [§8](#8-local-shell-profiles), create the
quake window from the command line, for example from a shortcut in
`shell:startup`:

```powershell
wt.exe -w _quake new-tab -p "PowerShell (quick)"
```

After that, the hotkey summons and hides that window, which keeps its tabs.

Reference: <https://learn.microsoft.com/windows/terminal/tips-and-tricks>
Reference: <https://learn.microsoft.com/windows/terminal/customize-settings/actions#global-commands>

______________________________________________________________________

## 13. Actions and Keybindings

### Format

```jsonc
"actions": [
    { "command": { "action": "newTab", "profile": "pve01" }, "id": "User.open.pve01" }
],
"keybindings": [
    { "id": "User.open.pve01", "keys": "ctrl+alt+shift+1" },
    { "id": null, "keys": "ctrl+shift+w" }       // unbind a default chord
]
```

- An action without a keybinding still appears in the Command Palette
  (`Ctrl+Shift+P`). Give it a `"name"` to set its label there.
- `"id": null` removes a default binding. Use it when a Terminal chord stops a
  key combination from reaching `tmux`, `vim`, or `nano` on the remote side.
- By convention, user action IDs start with `User.`.
- **`Ctrl+C` and `Ctrl+V` aren't built-in defaults.** A fresh install's
  generated `settings.json` binds them (`Terminal.CopyToClipboard` and
  `Terminal.PasteFromClipboard`), so a file that replaces it leaves them
  unbound. Then `Ctrl+C` always interrupts, even with text selected, and
  `Ctrl+V` goes to the shell: a literal `^V` in bash, and PSReadLine's own paste
  in PowerShell, which skips Terminal's paste warnings. This guide's
  `settings.json` leaves them unbound on purpose and includes commented-out
  lines to restore Windows-style copy and paste:
  `{ "id": "Terminal.CopyToClipboard", "keys": "ctrl+c" }` copies when text is
  selected and interrupts otherwise.
- **Check [Appendix B](#appendix-b--default-keyboard-shortcuts) before choosing
  a chord.** A user binding silently replaces any default on the same chord.

### Recommended additions for admin work

| Chord | Action | Purpose |
| -- | -- | -- |
| `ctrl+alt+shift+1` … `9` | `newTab` with a specific profile | Open your most-used hosts. (`ctrl+alt+1…9` is taken by tab switching.) |
| `ctrl+shift+z` | `togglePaneZoom` | Temporarily maximize one pane. |
| `ctrl+shift+b` | `toggleBroadcastInput` | Type into every pane in the tab ([§14](#14-panes-broadcast-input-and-startup-layouts)). |
| `ctrl+shift+e` | `exportBuffer` | Save the scrollback to a file ([§15](#15-session-logging-and-evidence)). |
| `ctrl+shift+r` | `openTabRenamer` | Rename the tab inline, for example `CHG0012345`. (`renameTab` without a title *resets* the title.) |
| palette only | `copy` with `"singleLine": true` | Copy a wrapped command as one line, without changing the normal `ctrl+shift+c` copy. |
| `ctrl+alt+shift+t` | `Terminal.RestoreLastClosed` (built in) | Reopen the last closed tab or pane after an accidental close. The profile and layout come back and an SSH tab reconnects; the old output does not. |
| `ctrl+alt+shift+r` | `Terminal.ToggleReadOnlyMode` (built in) | Lock a watch-only pane (`journalctl -f`, `tail -f`) against keystrokes and pastes; typing into it shows a "read-only mode is enabled" notice. Also keeps that pane out of broadcast input ([§14](#14-panes-broadcast-input-and-startup-layouts)). |
| `ctrl+alt+shift+p` / `ctrl+alt+shift+u` | `User.markProd` / `User.unmarkProd` (`multipleActions`) | Mark the current tab as production, or undo it ([§7](#mark-a-tab-as-production-after-the-fact)). |
| `ctrl+alt+shift+s` | `Terminal.OpenSnippetsPane` (built in) | Open the snippets pane: your `sendInput` actions ([below](#sendinput--command-snippets)) as a clickable list. They go to the active pane. |

```jsonc
"actions": [
    { "command": { "action": "newTab", "profile": "pve01" }, "id": "User.open.pve01" },
    { "command": { "action": "newTab", "profile": "pbs01" }, "id": "User.open.pbs01" },
    { "command": "togglePaneZoom",                           "id": "User.paneZoom" },
    { "command": "toggleBroadcastInput",                     "id": "User.broadcast" },
    { "command": { "action": "exportBuffer", "path": "" },   "id": "User.exportBuffer" },
    { "command": "openTabRenamer",                           "id": "User.renameTab" },
    {
        "name": "Copy as single line",
        "command": { "action": "copy", "singleLine": true },
        "id": "User.copySingleLine"
    }
],
"keybindings": [
    { "id": "User.open.pve01",   "keys": "ctrl+alt+shift+1" },
    { "id": "User.open.pbs01",   "keys": "ctrl+alt+shift+4" },   // 2 and 3: pve02, pve03 in settings.json
    { "id": "User.paneZoom",     "keys": "ctrl+shift+z" },
    { "id": "User.broadcast",    "keys": "ctrl+shift+b" },
    { "id": "User.exportBuffer", "keys": "ctrl+shift+e" },
    { "id": "User.renameTab",    "keys": "ctrl+shift+r" },
    // Built-in commands with no default chord: bind their built-in IDs directly
    { "id": "Terminal.RestoreLastClosed",  "keys": "ctrl+alt+shift+t" },
    { "id": "Terminal.ToggleReadOnlyMode", "keys": "ctrl+alt+shift+r" },
    { "id": "Terminal.OpenSnippetsPane",   "keys": "ctrl+alt+shift+s" }
]
```

A built-in command that has no default chord doesn't need an `actions` entry:
bind its built-in ID (`Terminal.<Name>`, listed in `defaults.json`) directly
in `keybindings`.

`exportBuffer` with an empty `path` opens a Save dialog. The built-in
`ctrl+shift+k` already clears the scrollback (`clearBuffer`), so it doesn't
need a binding of its own.

### `sendInput` — command snippets

`sendInput` types text into the active pane as if you had typed it, and `\r`
is `Enter`. Leave out the `\r` when you want to check or edit the command
before running it.

```jsonc
"actions": [
    {
        "name": "snip: failed systemd units",
        "command": { "action": "sendInput", "input": "systemctl --failed --no-pager\r" },
        "id": "User.snip.failedUnits"
    },
    {
        "name": "snip: journal errors this boot",
        "command": { "action": "sendInput", "input": "journalctl -b -p err --no-pager | tail -n 50\r" },
        "id": "User.snip.journalErr"
    },
    {
        "name": "snip: disk + inode usage",
        "command": { "action": "sendInput", "input": "df -hT -x tmpfs -x devtmpfs; df -i -x tmpfs -x devtmpfs\r" },
        "id": "User.snip.df"
    },
    {
        "name": "snip: become root (no Enter)",
        "command": { "action": "sendInput", "input": "sudo -i" },
        "id": "User.snip.sudo"
    }
]
```

To use a snippet, open the Command Palette and type `snip`. Snippets go to the
active pane, so check the tab color before running one.

Reference: <https://learn.microsoft.com/windows/terminal/customize-settings/actions>

______________________________________________________________________

## 14. Panes, Broadcast Input, and Startup Layouts

### Broadcast input

`toggleBroadcastInput` (Command Palette: *Toggle broadcast input to all
panes*) sends every keystroke to **all panes in the current tab**. A typical use
is to open one pane per node and run the same read-only check on all of them:

```text
pve01 │ pve02
──────┼──────
pve03 │ pbs01      → broadcast on → "uptime; df -h /" ⏎ → broadcast off
```

> **Warning:** broadcast input does not ask for confirmation. It reaches
> **every** pane in the tab, including any local PowerShell pane. Use it only
> for commands that are safe on every host in the tab, and turn it off before
> anything node-specific. Make production changes with Ansible or a loop that
> stops at the first failure, rather than with broadcast:
> `for h in pve01 pve02 pve03; do ssh "$h" 'cmd' || break; done`.

### Startup layout

`startupActions` runs `wt.exe` sub-commands when a new window opens without
arguments. This example opens a local tab and a four-pane cluster tab:

```jsonc
"startupActions": "new-tab -p \"PowerShell\" ; new-tab -p \"pve01\" --title \"PVE cluster\" ; split-pane -V -p \"pve02\" ; move-focus left ; split-pane -H -p \"pve03\" ; move-focus right ; split-pane -H -p \"pbs01\" ; focus-tab -t 0"
```

- A restored layout takes precedence over `startupActions`. If you use
  `startupActions`, set `firstWindowPreference` to `"defaultProfile"`.
- Profile names must match exactly. An unknown `-p` name opens the **default
  profile** instead, so a misspelled host becomes a local shell. That is
  dangerous when broadcast input is on.

### The same layouts from the command line or a desktop shortcut

```powershell
# Proxmox 2x2 in a new tab of the most recent window
wt.exe -w 0 new-tab -p "pve01" --title "PVE" `; split-pane -V -p "pve02" `; move-focus left `; split-pane -H -p "pve03" `; move-focus right `; split-pane -H -p "pbs01"
```

In PowerShell, write each `;` separator as `` `; ``. In a `.lnk` shortcut
target or in `cmd.exe`, use a plain `;`.

| `wt` option | Meaning |
| -- | -- |
| `-w 0` / `-w <name>` | The most recent window, or a named window (`-w _quake` is the quake window). |
| `new-tab -p "<profile>"` | Opens a tab with that profile. Also accepts `--title`, `--tabColor "#B00020"`, and `--suppressApplicationTitle`. |
| `split-pane -V` / `-H` | Splits side by side (`-V`) or stacked (`-H`). `-s 0.3` sets the new pane's size as a fraction. |
| `move-focus <dir>` | `left`, `right`, `up`, `down`, `first`, `previous`, and more. |
| `focus-tab -t <n>` | Selects a tab by index. |

Reference: <https://learn.microsoft.com/windows/terminal/command-line-arguments>
Reference: <https://learn.microsoft.com/windows/terminal/panes>

______________________________________________________________________

## 15. Session Logging and Evidence

Windows Terminal has **no automatic session log**. When you need a record of a
change window or evidence for a ticket, pick one of these:

| Method | Where it runs | Captures | Notes |
| -- | -- | -- | -- |
| `exportBuffer` (`ctrl+shift+e`, [§13](#13-actions-and-keybindings)) | Terminal | The pane's current scrollback | Limited by `historySize`. Lines that have scrolled out of the buffer are lost. |
| `script -f ~/chg-$(date +%F-%H%M).log` | Remote host | Everything in that shell, as it happens | Run it at the start of the session, and `exit` to stop recording. |
| `tmux pipe-pane -o 'cat >> ~/tmux-#S-#P.log'` | Remote host | One tmux pane, from that point on | Run the same command again to stop. |
| `Start-Transcript -Path <file>` | Local PowerShell | Local PowerShell input and output only | Doesn't see what happens inside an `ssh` session. |

On the remote side, the logs that stay authoritative are still the server's own
sshd and auditd logs, plus any session recording. See the SSH guide's
centralized logging and auditing sections and the Advanced Operations
companion.

> **Remember:** an exported buffer or `script` log can contain secrets that
> were printed to the screen. Store and share it the way you would store and
> share the system's config.

______________________________________________________________________

## 16. Backup, Version Control, and Portability

### Keep an annotated master copy in git

Terminal rewrites the live `settings.json` from time to time
([§2](#terminal-rewrites-the-file)). Keep the master copy, with your comments,
in a git-tracked dotfiles directory, and **copy** it into place:

```powershell
$wt   = "$env:LOCALAPPDATA\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json"
$repo = "$env:USERPROFILE\dotfiles\windows-terminal"

# Deploy: repo → Terminal (snapshot the live file first)
Copy-Item $wt "$wt.$(Get-Date -Format yyyyMMdd-HHmmss).bak"
Copy-Item "$repo\settings.json" $wt -Force

# Capture changes made in the Settings UI: Terminal → repo (merge by hand, comments are gone)
Copy-Item $wt "$repo\settings.live.json" -Force
```

A symbolic link from the live path into the repo also works on 1.22 and later,
because Terminal follows the link when it writes. The cost is that Terminal's
rewrites, including the comment stripping, then land directly in your repo.

### What to keep out of a shared repository

- Internal hostnames and IPs in `commandline` values. If the repo is shared, let
  the fragment generator build the host list from your private
  `~/.ssh/config`, and commit only the script.
- `sendInput` snippets that contain credentials, tokens, or internal URLs.

### Moving to another machine

1. Install Windows Terminal, JetBrains Mono, and, if you use it, PuTTY/plink.
1. Copy `~/.ssh/config` and your keys, then start the `ssh-agent` service. The
   SSH guide covers this in §24–§28.
1. Deploy `settings.json` from the repo, then run `Update-WtSshFragment.ps1`.
1. Fix any WSL profile GUIDs in `profiles.list`, because those GUIDs depend on
   the distribution. The PowerShell 7 and Windows PowerShell GUIDs are the
   same on every machine.

______________________________________________________________________

## 17. Troubleshooting

| Symptom | Likely cause | Fix |
| -- | -- | -- |
| "Unable to find the selected font" banner | `font.face` doesn't match an installed family name exactly | Run the check in [§4](#verify-the-install-and-the-exact-family-name), then restart Terminal. |
| Prompt icons show as boxes or `?` | The profile uses a non-Nerd JetBrains Mono | Use a `JetBrainsMono Nerd Font` family for that profile. |
| Icons clipped or overlapping the next character | Double-width Nerd Font glyphs | Use `JetBrainsMono Nerd Font Mono`. |
| Gaps in `tmux`/`htop` borders | `cellHeight` set lower than the font's natural line height | Remove `cellHeight` or increase it. Check that `builtinGlyphs` isn't set to `false`. |
| Comments vanished from `settings.json` | Terminal rewrote the file on load or on a save from the Settings UI | Expected behavior. Keep the master copy in git ([§16](#16-backup-version-control-and-portability)). |
| JSON error banner | Syntax error | Open the file in VS Code, where the `$schema` highlights the error, or restore the last `.bak`. |
| SSH tab vanishes after `exit` | `closeOnExit` is `automatic` and the exit code was 0 | Set `"closeOnExit": "never"` to keep the output. |
| Info bar: "Termination behavior can be configured in advanced profile settings." | A one-time hint about `closeOnExit` (Settings UI: Profile → Advanced → **Termination behavior**). It is not an error; the session is unaffected | Click **Don't show again**. Terminal records it in `state.json` (`"dismissedMessages": ["closeOnExitInfo"]`), not in `settings.json`, so deploying a new `settings.json` neither brings it back nor can pre-dismiss it. |
| Every host appears two or three times | Built-in generator, fragment, and hand-written profiles together | Choose one approach ([§11](#11-generated-ssh-profiles)) and disable `Windows.Terminal.SSH`. |
| Profile `SSH - pve01 pve02 pve03` | Built-in generator plus a multi-alias `Host` line | Disable `Windows.Terminal.SSH` and use the fragment generator. |
| Passphrase prompt on every connection | Git's `ssh.exe` is running, or the `ssh-agent` service is stopped | Use the full `%SystemRoot%\System32\OpenSSH\ssh.exe` path. Check `Get-Service ssh-agent` (SSH guide §26). |
| Multi-line paste runs without a prompt | `warning.multiLinePaste` is `true` (`automatic`) | Set it to `"always"` ([§6](#copy-and-paste-safety)). |
| Remote `tmux`/`vim` chord does nothing | A Terminal binding catches the chord first | Unbind it with `{ "id": null, "keys": "<chord>" }`. |
| Tab switching with `ctrl+alt+N` stopped working | A user binding replaced the default chord | Move the user binding to `ctrl+alt+shift+N` ([Appendix B](#appendix-b--default-keyboard-shortcuts)). |
| Quake hotkey does nothing | No Terminal process is running, or another program owns the chord | Turn on **Launch on machine startup** and the tray settings ([§12](#making-it-always-available)), or choose another chord. |
| Quake window opens the wrong shell | It uses the default profile | Create it with `wt -w _quake new-tab -p "<profile>"`. |
| Fragment profiles missing | Wrong folder, invalid JSON, or the source is disabled | Check the path, validate with `ConvertFrom-Json`, and check **Settings → Extensions**. |
| Wrong colors in remote `vim`/`less` | The remote `TERM` value doesn't match | `ssh.exe` sends the `TERM` value. Check `echo $TERM` on the host, and don't override it in remote dotfiles. |

______________________________________________________________________

## 18. Verification Checklist

- [ ] `settings.json` opens in VS Code with no schema errors (warnings only for
  known newer keys such as `font.builtinGlyphs`).
- [ ] The font check in [§4](#4-installing-jetbrains-mono) lists the exact
  `font.face` name.
- [ ] Ligatures render in a local tab (`echo '!= -> =>'`) and **do not** render
  in the production profile.
- [ ] Each SSH profile connects, and a deliberately wrong alias leaves the tab
  open with a readable error.
- [ ] Production profiles show a red tab, the `Prod Warning` background, and a
  fixed `PROD` title that survives `cd` on the remote host.
- [ ] Each host appears **once** in the new-tab menu. `Everything else` catches
  unlisted fragment-generated hosts; `matchProfiles` only matches exact values.
  There is no `SSH - …` folder unless you chose Option A.
- [ ] A two-line paste into a remote bash shell triggers the confirmation
  prompt (`warning.multiLinePaste: "always"`).
- [ ] The quake hotkey summons and hides the window and follows the mouse to a
  second monitor.
- [ ] `ctrl+alt+1` still switches to the first tab.
- [ ] After a restart, the restored window shows its tabs but **no** previous
  output (`persistedLayout`). On 1.24, check instead that
  `firstWindowPreference` is `"defaultProfile"` and a new window opens a single
  local tab.
- [ ] The annotated master `settings.json` is committed to the dotfiles repo.

______________________________________________________________________

## Appendix A — Complete Reference settings.json

A working configuration that combines the sections above. It is
comment-free so that strict JSON tools can parse it.

The full annotated version is [`settings.json`](settings.json) beside this
guide. It adds the rest of the example hosts (`pve02`, `pve03`,
`bastion-prod`) with their actions and chords, the `sendInput` snippets, and
the PVE cluster layout action, and its comments point back to the sections
here. The two use the same values and key chords; this appendix leaves out
the extra hosts, which is why `ctrl+alt+shift+2` and `3` are unused here.

Before using it:

- Replace the hosts and generate your own GUIDs for user profiles.
- Add profiles for any other hosts you reference, following the `pve01`
  example. This file defines only the hosts that its menu and bindings use.
- The `sendInput` snippets, the WSL override, and `startupActions` are left
  out. Copy them from [§13](#13-actions-and-keybindings),
  [§8](#8-local-shell-profiles), and [§14](#14-panes-broadcast-input-and-startup-layouts).
- When you run the fragment generator, pass these hand-written hosts to
  `-Exclude`, as shown in [§11](#generator-script).
- On 1.24, change `firstWindowPreference` to `"defaultProfile"`. 1.24 has no
  layout-only restore ([§6](#startup-and-windows)).

```json
{
    "$schema": "https://aka.ms/terminal-profiles-schema",

    "defaultProfile": "{574e775e-4f2a-5b96-ac1e-a2962a402336}",
    "firstWindowPreference": "persistedLayout",
    "initialCols": 140,
    "initialRows": 40,
    "centerOnLaunch": true,
    "windowingBehavior": "useExisting",
    "newTabPosition": "afterCurrentTab",
    "tabWidthMode": "titleLength",
    "warning.confirmCloseAllTabs": true,
    "copyOnSelect": false,
    "copyFormatting": "none",
    "trimBlockSelection": true,
    "trimPaste": true,
    "warning.multiLinePaste": "always",
    "warning.largePaste": true,
    "wordDelimiters": " /\\()\"'-:,;<>~!@#$%^&*|+=[]{}?│",
    "minimizeToNotificationArea": true,
    "alwaysShowNotificationIcon": true,
    "disabledProfileSources": [ "Windows.Terminal.Azure", "Windows.Terminal.SSH" ],
    "theme": "Admin Dark",

    "actions": [
        {
            "command": {
                "action": "globalSummon",
                "name": "_quake",
                "dropdownDuration": 150,
                "toggleVisibility": true,
                "monitor": "toMouse",
                "desktop": "toCurrent"
            },
            "id": "User.quakeToggle"
        },
        { "command": { "action": "newTab", "profile": "pve01" }, "id": "User.open.pve01" },
        { "command": { "action": "newTab", "profile": "pbs01" }, "id": "User.open.pbs01" },
        { "command": { "action": "newTab", "profile": "core-sw01" }, "id": "User.open.coreSw01" },
        { "command": "togglePaneZoom", "id": "User.paneZoom" },
        { "command": "toggleBroadcastInput", "id": "User.broadcast" },
        { "command": { "action": "exportBuffer", "path": "" }, "id": "User.exportBuffer" },
        { "command": "openTabRenamer", "id": "User.renameTab" },
        {
            "name": "Copy as single line",
            "command": { "action": "copy", "singleLine": true },
            "id": "User.copySingleLine"
        },
        {
            "name": "Mark tab as PROD",
            "command": {
                "action": "multipleActions",
                "actions": [
                    { "action": "setTabColor", "color": "#B00020" },
                    { "action": "setColorScheme", "colorScheme": "Prod Warning" },
                    { "action": "openTabRenamer" }
                ]
            },
            "id": "User.markProd"
        },
        {
            "name": "Unmark PROD tab",
            "command": {
                "action": "multipleActions",
                "actions": [
                    { "action": "setTabColor" },
                    { "action": "setColorScheme", "colorScheme": "Darcula Admin" },
                    { "action": "renameTab" }
                ]
            },
            "id": "User.unmarkProd"
        }
    ],

    "keybindings": [
        { "id": "User.quakeToggle", "keys": "win+sc(41)" },
        { "id": "User.open.pve01", "keys": "ctrl+alt+shift+1" },
        { "id": "User.open.pbs01", "keys": "ctrl+alt+shift+4" },
        { "id": "User.open.coreSw01", "keys": "ctrl+alt+shift+5" },
        { "id": "User.paneZoom", "keys": "ctrl+shift+z" },
        { "id": "User.broadcast", "keys": "ctrl+shift+b" },
        { "id": "User.exportBuffer", "keys": "ctrl+shift+e" },
        { "id": "User.renameTab", "keys": "ctrl+shift+r" },
        { "id": "Terminal.RestoreLastClosed", "keys": "ctrl+alt+shift+t" },
        { "id": "Terminal.ToggleReadOnlyMode", "keys": "ctrl+alt+shift+r" },
        { "id": "Terminal.OpenSnippetsPane", "keys": "ctrl+alt+shift+s" },
        { "id": "User.markProd", "keys": "ctrl+alt+shift+p" },
        { "id": "User.unmarkProd", "keys": "ctrl+alt+shift+u" }
    ],

    "newTabMenu": [
        { "type": "profile", "profile": "PowerShell" },
        { "type": "profile", "profile": "PowerShell (Admin)" },
        { "type": "separator" },
        {
            "type": "folder",
            "name": "Proxmox",
            "icon": "🗄️",
            "entries": [
                { "type": "profile", "profile": "pve01" },
                { "type": "profile", "profile": "pbs01" }
            ]
        },
        {
            "type": "folder",
            "name": "Production",
            "icon": "⚠️",
            "entries": [
                { "type": "profile", "profile": "web01-prod" }
            ]
        },
        {
            "type": "folder",
            "name": "Network",
            "icon": "🌐",
            "entries": [
                { "type": "profile", "profile": "core-sw01" },
                { "type": "profile", "profile": "Console COM3 (9600 8N1)" }
            ]
        },
        { "type": "separator" },
        {
            "type": "folder",
            "name": "Everything else",
            "inline": "never",
            "allowEmpty": false,
            "entries": [ { "type": "remainingProfiles" } ]
        }
    ],

    "profiles": {
        "defaults": {
            "font": {
                "face": "JetBrains Mono",
                "size": 14,
                "weight": "normal",
                "features": { "calt": 1, "zero": 1 }
            },
            "colorScheme": "Darcula Admin",
            "intenseTextStyle": "bright",
            "adjustIndistinguishableColors": "always",
            "cursorShape": "filledBox",
            "padding": "6, 4",
            "historySize": 20000,
            "scrollbarState": "visible",
            "bellStyle": [ "window", "taskbar" ],
            "rightClickContextMenu": true
        },
        "list": [
            {
                "guid": "{574e775e-4f2a-5b96-ac1e-a2962a402336}",
                "source": "Windows.Terminal.PowershellCore",
                "name": "PowerShell",
                "commandline": "pwsh.exe -NoLogo",
                "startingDirectory": "%USERPROFILE%"
            },
            {
                "guid": "{0d6f3c55-8b2a-4f7e-a1c4-5e9b2d7f1a01}",
                "name": "PowerShell (quick)",
                "commandline": "pwsh.exe -NoLogo -NoProfile",
                "hidden": true
            },
            {
                "guid": "{3f6b1c2e-6a4d-4f0e-9d1a-0b7e5c2a9e11}",
                "name": "PowerShell (Admin)",
                "commandline": "pwsh.exe -NoLogo",
                "elevate": true,
                "icon": "🛡️",
                "tabColor": "#B26A00",
                "startingDirectory": "%SystemRoot%\\System32"
            },
            {
                "guid": "{61c54bbd-c2c6-5271-96e7-009a87ff44bf}",
                "name": "Windows PowerShell",
                "hidden": true
            },
            {
                "guid": "{a7d1e0b4-1c2f-4e0a-9b3d-1f0c2e4a5b01}",
                "name": "pve01",
                "commandline": "%SystemRoot%\\System32\\OpenSSH\\ssh.exe pve01",
                "icon": "🖥️",
                "tabTitle": "lab pve01",
                "suppressApplicationTitle": true,
                "tabColor": "#2E7D32",
                "closeOnExit": "never"
            },
            {
                "guid": "{a7d1e0b4-1c2f-4e0a-9b3d-1f0c2e4a5b02}",
                "name": "pbs01",
                "commandline": "%SystemRoot%\\System32\\OpenSSH\\ssh.exe pbs01",
                "icon": "💾",
                "tabTitle": "lab pbs01",
                "suppressApplicationTitle": true,
                "tabColor": "#2E7D32",
                "closeOnExit": "never"
            },
            {
                "guid": "{a7d1e0b4-1c2f-4e0a-9b3d-1f0c2e4a5b10}",
                "name": "web01-prod",
                "commandline": "%SystemRoot%\\System32\\OpenSSH\\ssh.exe web01-prod",
                "icon": "⚠️",
                "tabTitle": "PROD web01",
                "suppressApplicationTitle": true,
                "tabColor": "#B00020",
                "colorScheme": "Prod Warning",
                "font": { "features": { "calt": 0 } },
                "closeOnExit": "never"
            },
            {
                "guid": "{a7d1e0b4-1c2f-4e0a-9b3d-1f0c2e4a5b11}",
                "name": "core-sw01",
                "commandline": "%SystemRoot%\\System32\\OpenSSH\\ssh.exe core-sw01",
                "icon": "🌐",
                "tabTitle": "core-sw01",
                "suppressApplicationTitle": true,
                "tabColor": "#1565C0",
                "font": { "features": { "calt": 0 } },
                "closeOnExit": "never"
            },
            {
                "guid": "{a7d1e0b4-1c2f-4e0a-9b3d-1f0c2e4a5b20}",
                "name": "Console COM3 (9600 8N1)",
                "commandline": "plink.exe -serial COM3 -sercfg 9600,8,n,1,N",
                "icon": "🔌",
                "tabColor": "#1565C0",
                "font": { "features": { "calt": 0 } },
                "closeOnExit": "never"
            }
        ]
    },

    "schemes": [
        {
            "name": "Darcula Admin",
            "background": "#1E1F22",
            "foreground": "#BCBEC4",
            "cursorColor": "#CED0D6",
            "selectionBackground": "#214283",
            "black": "#1E1F22",
            "red": "#F75464",
            "green": "#6AAB73",
            "yellow": "#E0BB65",
            "blue": "#56A8F5",
            "purple": "#C77DBB",
            "cyan": "#2AACB8",
            "white": "#BCBEC4",
            "brightBlack": "#5A5D63",
            "brightRed": "#FF7A85",
            "brightGreen": "#8BCB94",
            "brightYellow": "#F2D58C",
            "brightBlue": "#7DBDF8",
            "brightPurple": "#DB9DD0",
            "brightCyan": "#5CCFD9",
            "brightWhite": "#DFE1E5"
        },
        {
            "name": "Prod Warning",
            "background": "#2A0A0A",
            "foreground": "#E6E6E6",
            "cursorColor": "#FF5555",
            "selectionBackground": "#7A1F1F",
            "black": "#0C0C0C",
            "red": "#E74856",
            "green": "#16C60C",
            "yellow": "#F9F1A5",
            "blue": "#3B78FF",
            "purple": "#B4009E",
            "cyan": "#61D6D6",
            "white": "#CCCCCC",
            "brightBlack": "#767676",
            "brightRed": "#FF6E7A",
            "brightGreen": "#5FE85A",
            "brightYellow": "#FFF8C4",
            "brightBlue": "#7AA2FF",
            "brightPurple": "#D670C8",
            "brightCyan": "#9AE8E8",
            "brightWhite": "#F2F2F2"
        }
    ],

    "themes": [
        {
            "name": "Admin Dark",
            "window": { "applicationTheme": "dark", "useMica": false },
            "tabRow": { "background": "#18191CFF", "unfocusedBackground": "#18191CFF" },
            "tab": { "background": "terminalBackground", "unfocusedBackground": null, "showCloseButton": "hover" }
        }
    ]
}
```

______________________________________________________________________

## Appendix B — Default Keyboard Shortcuts

These are the built-in chords an admin uses most, as of 1.25. Your installed
`defaults.json` (`Ctrl+Alt+,`) is the authoritative list for your version.
Check this table before you bind a chord yourself.

| Chord | Action |
| -- | -- |
| `Ctrl+Shift+T` / `Ctrl+Shift+N` | New tab (default profile) / new window |
| `Ctrl+Shift+1` … `9` | New tab with the Nth profile |
| `Ctrl+Shift+D` | Duplicate tab |
| `Ctrl+Shift+Space` | Open the new-tab drop-down |
| `Ctrl+Shift+W` | Close pane (closes the tab if it is the last pane) |
| `Ctrl+Tab` / `Ctrl+Shift+Tab` | Next / previous tab |
| `Ctrl+Alt+1` … `8` / `Ctrl+Alt+9` | Switch to tab 1–8 / to the last tab |
| `Alt+Shift+D` | Duplicate pane, auto direction (in the generated user defaults) |
| `Alt+Shift+plus` / `Alt+Shift+minus` | Duplicate pane to the right / below |
| `Alt+Arrow` | Move focus between panes |
| `Alt+Shift+Arrow` | Resize pane |
| `Ctrl+Shift+P` | Command Palette |
| `Ctrl+Shift+F` | Find in scrollback |
| `Ctrl+Shift+C` / `Ctrl+Shift+V` | Copy / paste. `Ctrl+C` and `Ctrl+V` are **not** built-in defaults; see [§13](#format). |
| `Ctrl+Shift+K` | Clear the buffer |
| `Ctrl+Shift+Up` / `Down`, `PgUp` / `PgDn` | Scroll by line / by page |
| `Ctrl+=` / `Ctrl+-` / `Ctrl+0` | Font size up / down / reset |
| `Win+sc(41)` (`` Win+` `` on US layout) | Quake window |
| `F11` / `Alt+Enter` | Full screen |
| `Ctrl+,` / `Ctrl+Shift+,` / `Ctrl+Alt+,` | Settings UI / `settings.json` / `defaults.json` |

______________________________________________________________________

## References

- Reference: <https://learn.microsoft.com/windows/terminal/install>
- Reference: <https://learn.microsoft.com/windows/terminal/customize-settings/startup>
- Reference: <https://learn.microsoft.com/windows/terminal/customize-settings/interaction>
- Reference: <https://learn.microsoft.com/windows/terminal/customize-settings/profile-general>
- Reference: <https://learn.microsoft.com/windows/terminal/customize-settings/profile-appearance>
- Reference: <https://man.openbsd.org/ssh_config#ServerAliveInterval> (OpenSSH client keepalives)
- Reference: <https://learn.microsoft.com/windows/terminal/customize-settings/actions>
- Reference: <https://learn.microsoft.com/windows/terminal/customize-settings/new-tab-menu>
- Reference: <https://learn.microsoft.com/windows/terminal/customize-settings/appearance#match-profiles> (`matchProfiles` uses exact string matching)
- Reference: <https://learn.microsoft.com/windows/terminal/customize-settings/color-schemes>
- Reference: <https://learn.microsoft.com/windows/terminal/customize-settings/themes>
- Reference: <https://learn.microsoft.com/windows/terminal/json-fragment-extensions>
- Reference: <https://learn.microsoft.com/windows/terminal/command-line-arguments>
- Reference: <https://learn.microsoft.com/windows/terminal/panes>
- Reference: <https://learn.microsoft.com/windows/terminal/tips-and-tricks>
- Reference: <https://raw.githubusercontent.com/microsoft/terminal/main/doc/cascadia/profiles.schema.json>
- Reference: <https://github.com/microsoft/terminal/releases> (1.21–1.25 release notes: content restore, actions/keybindings split, SSH generator, paste-warning enum)
- Reference: <https://github.com/JetBrains/JetBrainsMono>
- Reference: <https://github.com/ryanoasis/nerd-fonts>
