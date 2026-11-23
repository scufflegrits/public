---
Title: VS Code Settings Reference for System Administrators
Version: r1.1.2
Updated: 2026-11-22
Reference build: Visual Studio Code 1.140.0 (2026-09-30); settings keys and extension IDs re-checked on 1.146.0
Companion: SSH-Sysadmin-Guide_r1.0.9, ms-terminal-json-settings
Topics: VS Code, settings.json, line endings, LF, CRLF, EditorConfig, gitattributes, encoding, whitespace, JetBrains Mono, fonts, ligatures, integrated terminal, Remote - SSH, git, telemetry, AI features, proxy, offline, extensions, profiles, Settings Sync, keybindings, snippets, tasks, Debian 13, RHEL 8, RHEL 9, RHEL 10, Windows 11
---

# VS Code Settings Reference for System Administrators

> A single reference for setting up Visual Studio Code for sysadmin work:
> LF line endings everywhere, clean whitespace and encoding, JetBrains Mono
> with ligatures, a sensible integrated terminal, Remote - SSH, and the
> privacy, update, proxy, and extension settings that matter when you manage
> servers. It covers the Linux desktop (Debian 13, RHEL 8/9/10) and Windows 11.
>
> **Reference build:** VS Code **1.140.0** (released 2026-09-30). The core
> setting keys and built-in defaults quoted here were checked against that
> build. Extension settings (Remote - SSH, EditorConfig, and others) come from
> each extension's own documentation, and an extension can change them on its
> own release schedule.
>
> **Connecting with Remote - SSH** (installing the extension, connecting,
> port forwarding, picking `ssh.exe` on Windows, basic troubleshooting) is
> covered in the companion `SSH-Sysadmin-Guide_r1.0.9.md`, §11 (Linux) and §33
> (Windows). This guide does not repeat that material. It covers the editor
> side: what to set, where to set it, and why.
>
> The fastest route is [Appendix A](#appendix-a-complete-baseline-settingsjson),
> a complete annotated `settings.json` you can paste in and trim. The numbered
> sections explain each group of settings in it. For everything at once, the
> file `settings.json` next to this guide is the full configuration: the
> Appendix A baseline plus the extras from §5–§18, ready to copy or symlink
> from a dotfiles repository (§14).
> [§19](#19-verification-checklist) checks that a deployed configuration does
> what this guide says.
>
> The companion `microsoft/terminal/ms-terminal-json-settings.md` sets up
> Windows Terminal with the same JetBrains Mono font, paste safety, and
> production color coding.

______________________________________________________________________

## Table of Contents

- [1. How VS Code settings work](#1-how-vs-code-settings-work)
  - [Principles behind this configuration](#principles-behind-this-configuration)
  - [Settings are JSON with comments](#settings-are-json-with-comments)
  - [Scopes and precedence](#scopes-and-precedence)
  - [Language identifiers](#language-identifiers)
- [2. Installing VS Code and the `code` CLI](#2-installing-vs-code-and-the-code-cli)
  - [Debian 13](#debian-13)
  - [RHEL 8 / 9 / 10](#rhel-8--9--10)
  - [Windows 11](#windows-11)
  - [The `code` command line](#the-code-command-line)
- [3. Line endings: LF everywhere](#3-line-endings-lf-everywhere)
  - [The short answer](#the-short-answer)
  - [What `files.eol` does not do](#what-fileseol-does-not-do)
  - [Git configuration](#git-configuration)
  - [Exceptions that genuinely need CRLF](#exceptions-that-genuinely-need-crlf)
  - [Finding and converting existing CRLF files](#finding-and-converting-existing-crlf-files)
  - [Why this matters on servers](#why-this-matters-on-servers)
- [4. Encoding and whitespace hygiene](#4-encoding-and-whitespace-hygiene)
  - [Encoding](#encoding)
  - [Final newline and trailing whitespace](#final-newline-and-trailing-whitespace)
  - [Make invisible characters visible](#make-invisible-characters-visible)
- [5. Fonts: JetBrains Mono](#5-fonts-jetbrains-mono)
  - [Install: Debian 13](#install-debian-13)
  - [Install: RHEL 8 / 9 / 10](#install-rhel-8--9--10)
  - [Install: Windows 11](#install-windows-11)
  - [Configure the editor](#configure-the-editor)
  - [Use it everywhere, not just the editor](#use-it-everywhere-not-just-the-editor)
- [6. Ligatures and OpenType features](#6-ligatures-and-opentype-features)
  - [Editor](#editor)
  - [Integrated terminal](#integrated-terminal)
  - [Should you use them?](#should-you-use-them)
- [7. Editor ergonomics](#7-editor-ergonomics)
  - [Indentation](#indentation)
  - [Layout and visual aids](#layout-and-visual-aids)
  - [Editing behaviour](#editing-behaviour)
  - [File associations](#file-associations)
- [8. Integrated terminal](#8-integrated-terminal)
  - [Default shell profiles](#default-shell-profiles)
  - [Behaviour](#behaviour)
  - [Keys that the terminal should keep](#keys-that-the-terminal-should-keep)
- [9. Remote - SSH: settings beyond the basics](#9-remote---ssh-settings-beyond-the-basics)
  - [Remote host requirements](#remote-host-requirements)
  - [Recommended user settings](#recommended-user-settings)
  - [Per-host settings (Remote/Machine scope)](#per-host-settings-remotemachine-scope)
  - [Editing root-owned files](#editing-root-owned-files)
  - [Know which host you are on](#know-which-host-you-are-on)
  - [Remote Tunnels bypass your SSH controls](#remote-tunnels-bypass-your-ssh-controls)
  - [Clean up old servers](#clean-up-old-servers)
- [10. Git integration](#10-git-integration)
- [11. Privacy, telemetry, updates, and AI features](#11-privacy-telemetry-updates-and-ai-features)
  - [Telemetry](#telemetry)
  - [Updates](#updates)
  - [AI features](#ai-features)
  - [Workspace Trust](#workspace-trust)
  - [Managed (enforced) settings](#managed-enforced-settings)
- [12. Proxies, internal CAs, and offline hosts](#12-proxies-internal-cas-and-offline-hosts)
  - [Corporate proxy](#corporate-proxy)
  - [Internal / TLS-inspecting CA](#internal--tls-inspecting-ca)
  - [Air-gapped or no-internet environments](#air-gapped-or-no-internet-environments)
- [13. Extensions for sysadmin work](#13-extensions-for-sysadmin-work)
  - [Core](#core)
  - [Languages and linting](#languages-and-linting)
  - [Utilities](#utilities)
  - [Managing extensions](#managing-extensions)
- [14. Profiles, Settings Sync, and keeping config in git](#14-profiles-settings-sync-and-keeping-config-in-git)
  - [Profiles](#profiles)
  - [Settings Sync](#settings-sync)
  - [Keeping config in git instead](#keeping-config-in-git-instead)
- [15. Keybindings, snippets, and tasks](#15-keybindings-snippets-and-tasks)
  - [Keybindings](#keybindings)
  - [Snippets](#snippets)
  - [Tasks](#tasks)
- [16. Tips and tricks](#16-tips-and-tricks)
  - [Colour-code production windows](#colour-code-production-windows)
  - [Lock what you shouldn't edit](#lock-what-you-shouldnt-edit)
  - [Undo a bad save with Local History](#undo-a-bad-save-with-local-history)
  - [Compare anything](#compare-anything)
  - [Search across many files](#search-across-many-files)
  - [Multi-cursor editing for config files](#multi-cursor-editing-for-config-files)
  - [Other useful commands](#other-useful-commands)
- [17. Troubleshooting](#17-troubleshooting)
  - [General approach](#general-approach)
  - [Specific problems](#specific-problems)
  - [Reset](#reset)
- [18. Power-user settings](#18-power-user-settings)
  - [Nest config backups under the file they belong to (safety)](#nest-config-backups-under-the-file-they-belong-to-safety)
  - [Readable tab names for Ansible roles](#readable-tab-names-for-ansible-roles)
  - [A sound when a long command fails or finishes (safety)](#a-sound-when-a-long-command-fails-or-finishes-safety)
  - [No accidental drag-and-drop moves (safety)](#no-accidental-drag-and-drop-moves-safety)
  - [Make unsaved changes obvious (safety)](#make-unsaved-changes-obvious-safety)
  - [Terminal tabs that show where you are](#terminal-tabs-that-show-where-you-are)
  - [Smaller ones worth having](#smaller-ones-worth-having)
- [19. Verification Checklist](#19-verification-checklist)
- [Appendix A: Complete baseline `settings.json`](#appendix-a-complete-baseline-settingsjson)
- [Appendix B: `.editorconfig` and `.gitattributes` templates](#appendix-b-editorconfig-and-gitattributes-templates)
  - [`.editorconfig`](#editorconfig)
  - [`.gitattributes`](#gitattributes)
- [Appendix C: File locations](#appendix-c-file-locations)
- [Appendix D: Command and shortcut quick reference](#appendix-d-command-and-shortcut-quick-reference)

______________________________________________________________________

## 1. How VS Code settings work

### Principles behind this configuration

The configuration in this guide follows a few principles:

| Principle | Why it matters for a sysadmin |
| -- | -- |
| LF everywhere | A CR in a script or config breaks shebangs, heredocs, and parsers on the server (§3). |
| What you see is what is in the file | Stray Unicode, invisible spaces, and ligatures in the shell can hide the character that breaks a config (§4, §6). |
| Nothing rewrites a live config behind your back | Auto save, format on save, and drag-and-drop stay off, so a file changes only when you save it deliberately (§7, §18). |
| Paste is guarded | A multi-line paste into a root shell always asks first (§8). |
| You always know which host you are on | The remote name is in every window title, and production windows are red (§9, §16). |
| Nothing phones home or updates itself mid-change | Telemetry and AI features are off, and VS Code and extensions update only when you choose (§11). |
| The configuration is versioned | `settings.json` lives in a dotfiles repository, with its comments, like any other config (§14). |

### Settings are JSON with comments

Every option in the Settings UI (`Ctrl+,`) is stored as a key in a JSON file.
The file is **JSONC**: `//` and `/* */` comments are allowed, and a trailing
comma only produces a warning. Comment your settings. Six months from now
you won't remember why a value is set.

To edit the JSON directly:

- `Ctrl+Shift+P` → **Preferences: Open User Settings (JSON)**
- Or click the **Open Settings (JSON)** icon (a page with a curly arrow) at the
  top right of the Settings UI.

To make `Ctrl+,` always open the JSON file instead of the UI:

```jsonc
"workbench.settings.editor": "json"
```

### Scopes and precedence

Settings are applied in layers. A later layer overrides an earlier one:

| Order | Scope | Where it lives | Typical use |
| -- | -- | -- | -- |
| 1 | Default | Built into VS Code and each extension | Never edited |
| 2 | User | `settings.json` in your user profile (see Appendix C) | Your personal preferences, on every machine |
| 3 | Remote (Machine) | `~/.vscode-server/data/Machine/settings.json` on host | Per-remote-host overrides (paths, watchers) |
| 4 | Workspace | `.vscode/settings.json`, or the `.code-workspace` file | Project rules shared with the team via git |
| 5 | Workspace folder | `.vscode/settings.json` in each folder of a multi-root | Per-folder rules in a multi-root workspace |
| — | Language-specific | `"[yaml]": { ... }` blocks at any scope above | Overrides for one language, beating plain keys |
| — | Policy (Group Policy) | Windows ADMX / managed policy | Enforced by an administrator, cannot be overruled |

A few points that cause confusion:

- **Language-specific blocks win over plain keys, even from a narrower
  scope.** If your user settings say `"[yaml]": {"editor.tabSize": 2}`, YAML
  files get 2 even when a workspace's `.vscode/settings.json` sets a plain
  `"editor.tabSize": 4`. To override it, the workspace needs its own `[yaml]`
  block.
- **Some built-in language defaults already exist.** In 1.140.0, VS Code ships
  these defaults:
  `[shellscript]` → `files.eol: "\n"`; `[yaml]` → spaces, tab size 2;
  `[makefile]` and `[go]` → tabs; `[plaintext]` → invisible and ambiguous
  Unicode highlighting **off** (so text pasted into a `.txt` file gets no
  warning boxes; see §4); `[markdown]` → word wrap on, quick suggestions off,
  and Unicode highlighting relaxed. Your user settings override them.
- **Some settings cannot be set at the workspace level.** Settings marked
  *application* or *machine* scope (update mode, telemetry, proxy, and others)
  are ignored in `.vscode/settings.json`. The Settings UI notes this when it
  applies.
- **Find where a value comes from.** In the Settings UI, a modified setting
  shows a coloured bar and a note such as *"Also modified in: Workspace"*.

### Language identifiers

Language-specific blocks use the **language ID**, not the file extension. The
ones sysadmins use most:

| Files | Language ID |
| -- | -- |
| `*.sh`, `*.bash`, shebang `#!/bin/bash` | `shellscript` |
| `*.ps1`, `*.psm1`, `*.psd1` | `powershell` |
| `*.bat`, `*.cmd` | `bat` |
| `*.yml`, `*.yaml` | `yaml` (`ansible` with that ext.) |
| `*.json` / `settings.json`, `*.jsonc` | `json` / `jsonc` |
| `*.md` | `markdown` |
| `*.ini`, `*.conf` (often) | `ini` / `properties` |
| `*.py` | `python` |
| `Makefile` | `makefile` |
| `Dockerfile`, `Containerfile` | `dockerfile` |
| `ssh_config` (with Remote - SSH) | `ssh_config` |

To check the ID of the open file, look at the language name in the status bar
at the bottom right. Click it to change it, or run
**Change Language Mode** (`Ctrl+K M`).

______________________________________________________________________

## 2. Installing VS Code and the `code` CLI

Use Microsoft's package repository rather than a downloaded `.deb`/`.rpm`. The
system package manager then handles updates.

### Debian 13

Debian 13 uses deb822 `.sources` files:

```bash
sudo apt install -y wget gpg
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > /tmp/microsoft.gpg
sudo install -D -o root -g root -m 644 /tmp/microsoft.gpg /usr/share/keyrings/microsoft.gpg
rm /tmp/microsoft.gpg

sudo tee /etc/apt/sources.list.d/vscode.sources > /dev/null <<'EOF'
Types: deb
URIs: https://packages.microsoft.com/repos/code
Suites: stable
Components: main
Architectures: amd64 arm64 armhf
Signed-By: /usr/share/keyrings/microsoft.gpg
EOF

sudo apt update
sudo apt install -y code
```

The `code` package's install script also offers to add a Microsoft
repository entry. If a `packages.microsoft.com/repos/code` entry already
exists, as it does after the step above, the script detects it and doesn't
prompt or write a second one. Without one, it asks (debconf question
`code/add-microsoft-repo`), and a non-interactive install writes the entry
without asking. To pre-answer the question, for example in an automated
build:

```bash
echo "code code/add-microsoft-repo boolean false" | sudo debconf-set-selections
```

### RHEL 8 / 9 / 10

```bash
sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
sudo tee /etc/yum.repos.d/vscode.repo > /dev/null <<'EOF'
[code]
name=Visual Studio Code
baseurl=https://packages.microsoft.com/yumrepos/vscode
enabled=1
autorefresh=1
type=rpm-md
gpgcheck=1
gpgkey=https://packages.microsoft.com/keys/microsoft.asc
EOF

sudo dnf check-update
sudo dnf install -y code
```

### Windows 11

```powershell
# Machine-wide install (needs an elevated prompt); adds `code` to PATH
winget install --id Microsoft.VisualStudioCode --scope machine

# Per-user install (no elevation)
winget install --id Microsoft.VisualStudioCode --scope user
```

If you run the installer by hand, tick **Add "Open with Code" action to
Windows Explorer file context menu**, **…directory context menu**, and **Add
to PATH**.

### The `code` command line

The `code` CLI is one of VS Code's most useful sysadmin features and is easy to
overlook. Inside a Remote - SSH session, the integrated terminal has its own
`code` that opens files in the window you are connected from.

| Command | What it does |
| -- | -- |
| `code .` | Open the current directory as a folder |
| `code -r file` | Open in the most recent window (reuse) instead of a new one |
| `code -g file:120:5` | Open at line 120, column 5 |
| `code -d left right` | Diff two files |
| `code -m mine theirs base result` | Three-way merge |
| `code --wait file` | Block until the tab is closed (for `EDITOR`, `git`, `sudoedit`) |
| `cmd \| code -` | Read stdin into a new editor tab (`journalctl -u sshd \| code -`) |
| `code --list-extensions --show-versions` | Inventory installed extensions |
| `code --install-extension <id>` | Install by ID or from a `.vsix` file path |
| `code --uninstall-extension <id>` | Remove an extension |
| `code --profile "Sysadmin"` | Open with a named profile (see §14) |
| `code --disable-extensions` | Start with all extensions off (troubleshooting) |
| `code --status` | Print process, CPU, and memory diagnostics for running windows |
| `code --version` | Version, commit hash, and architecture |
| `code --user-data-dir /tmp/vsc --extensions-dir /tmp/vsc-ext` | Fully isolated throwaway instance |

Make VS Code your editor for git and the shell:

```bash
git config --global core.editor "code --wait"
export VISUAL="code --wait"     # in ~/.bashrc; many tools check VISUAL before EDITOR
```

______________________________________________________________________

## 3. Line endings: LF everywhere

### The short answer

```jsonc
"files.eol": "\n"
```

Put that in your **user** settings on every machine, Windows included. The
values are `"\n"` (LF), `"\r\n"` (CRLF), and `"auto"` (the default: CRLF on
Windows, LF elsewhere).

### What `files.eol` does not do

This is the part most guides leave out. **`files.eol` only sets the line ending
for new files.** When VS Code opens an existing file, it detects the line
endings already there and keeps them. A CRLF file stays CRLF no matter what
`files.eol` says.

The current file's line ending is shown in the status bar (`LF` or `CRLF`).
Click it, or run **Change End of Line Sequence**, to convert that one file, then
save.

So "always LF" needs three layers, not one:

| Layer | Controls | Section |
| -- | -- | -- |
| `files.eol` | New files created in VS Code | This section |
| `.editorconfig` | New and existing files, in any EditorConfig-aware editor | [Appendix B](#appendix-b-editorconfig-and-gitattributes-templates) |
| `.gitattributes` + git config | What git writes to your working tree and stores in the repo | Below and Appendix B |

On Windows, **git is the usual reason CRLF keeps coming back**. The Git for
Windows installer defaults to `core.autocrlf=true`, which converts LF to CRLF
on every checkout. VS Code then opens those CRLF files and, correctly, keeps
them as CRLF.

### Git configuration

```bash
# All platforms: never add CR on checkout; strip CR from text files on commit.
git config --global core.autocrlf input

# Check what is set and where it comes from
git config --show-origin --get-all core.autocrlf
```

On Windows, the equivalent choice in the Git for Windows installer is
**"Checkout as-is, commit Unix-style line endings"**. A system-level
`core.autocrlf=true` in `C:\Program Files\Git\etc\gitconfig` is overridden by
your `--global` value, but check with `--show-origin` anyway.

Global git config is per user and per machine. A **`.gitattributes` file in the
repository** is the reliable fix, because it travels with the repo and applies
to everyone who clones it:

```gitattributes
* text=auto eol=lf
*.bat text eol=crlf
*.cmd text eol=crlf
```

A full template is in [Appendix B](#appendix-b-editorconfig-and-gitattributes-templates).

### Exceptions that genuinely need CRLF

| File type | Why |
| -- | -- |
| `*.bat`, `*.cmd` | `cmd.exe` mis-parses labels and `GOTO` targets in LF batch files |
| Windows `.reg` exports | `regedit` expects CRLF (and often UTF-16LE). Leave them as exported. |
| Authenticode-signed `.ps1` | The signature covers the exact bytes. Changing line endings after signing invalidates it. Keep signed scripts byte-for-byte, or mark them `-text` in `.gitattributes`. |
| Some appliance imports | A few vendor web UIs and serial-console paste buffers want CRLF. Convert when you export. |

Unsigned PowerShell scripts are fine with LF on Windows PowerShell 5.1 and
PowerShell 7.

Use a language-specific override so VS Code creates these files with CRLF:

```jsonc
"files.eol": "\n",
"[bat]": {
    "files.eol": "\r\n"
}
```

### Finding and converting existing CRLF files

```bash
# List text files containing CR (skip binaries with -I, skip .git)
grep -rlI $'\r' --exclude-dir=.git .

# `file` reports "with CRLF line terminators"
file -- *.sh

# Convert in place (dos2unix: Debian `apt install dos2unix`, RHEL `dnf install dos2unix`)
dos2unix script.sh
# or without dos2unix
sed -i 's/\r$//' script.sh
```

In a git repository, `git ls-files --eol` shows, for each file, the line
endings in the index (`i/`), in the working tree (`w/`), and the attribute
in force (`attr/`):

```bash
git ls-files --eol | grep 'w/crlf'     # CRLF files on disk
git ls-files --eol | grep 'i/crlf'     # CRLF files committed to the repo
```

After you add `.gitattributes`, re-normalize what is already committed:

```bash
git add --renormalize .
git status            # shows files whose stored line endings changed
git commit -m "Normalize line endings to LF"
```

PowerShell 7 (Windows), one file:

```powershell
$p = '.\script.sh'
(Get-Content -Raw $p) -replace "`r`n", "`n" | Set-Content -NoNewline -Encoding utf8NoBOM $p
```

Don't use Windows PowerShell 5.1 for this. Its `Set-Content -Encoding UTF8`
writes a byte-order mark, which breaks shebang lines (see §4).

### Why this matters on servers

A CRLF shell script fails with errors that don't point at the cause:

```text
$ ./deploy.sh
-bash: ./deploy.sh: /bin/bash^M: bad interpreter: No such file or directory
```

The same stray `\r` breaks anything a shell reads: sourced environment files
(`$'\r': command not found`), variables whose values end in `\r` (paths that
"don't exist"), cron entries (the command name ends in `\r`), and heredocs.
In each case the `\r` is invisible. Running `cat -A` shows it as `^M` before
the `$`.

Some parsers, including OpenSSH (`sshd_config`, `ssh_config`) and systemd
unit files, treat `\r` as whitespace and accept CRLF files. Tested with
`sshd -T -f` and `systemd-analyze verify`, both accepted a CRLF file without
complaint. So an error message won't always catch the problem. Check line
endings before you deploy, not after something fails.

______________________________________________________________________

## 4. Encoding and whitespace hygiene

### Encoding

```jsonc
"files.encoding": "utf8",          // default; never "utf8bom" for Linux files
"files.autoGuessEncoding": false   // default; see below
```

- **Never save Linux files with a BOM.** A UTF-8 byte-order mark (`EF BB BF`) in
  front of `#!/bin/bash` stops the kernel from recognizing the shebang. Many
  config parsers also reject it. The status bar shows `UTF-8 with BOM` when a
  file has one. Click it → **Save with Encoding** → **UTF-8** to remove it.
- `files.autoGuessEncoding` is useful when you open old Windows-1252 or
  Latin-1 files often (legacy Windows exports, old network-device configs).
  Detection is a guess, so limit it with
  `"files.candidateGuessEncodings": ["utf8", "windows1252", "iso88591"]`.
  Otherwise leave it off and use **Reopen with Encoding** (status bar) when
  needed.

**Exception: Windows PowerShell 5.1.** It reads a `.ps1` file without a
BOM as ANSI (the system code page), so non-ASCII text (accented letters,
box-drawing characters, em dashes) comes out garbled. For scripts that must
run on 5.1 **and** contain non-ASCII characters, save PowerShell files with a
BOM. PowerShell 7 doesn't need this.

```jsonc
"[powershell]": { "files.encoding": "utf8bom" }
```

### Final newline and trailing whitespace

```jsonc
"files.insertFinalNewline": true,     // POSIX text files end with \n
"files.trimFinalNewlines": true,      // ...but exactly one
"files.trimTrailingWhitespace": true,
"[markdown]": {
    "files.trimTrailingWhitespace": false   // two trailing spaces = <br> in Markdown
}
```

A missing final newline causes real problems: `cat file1 file2` joins the last
line of one file to the first line of the next, `read` loops in shell skip the
last line, and some tools ignore the final line of a config file.

To trim whitespace **without** formatting the rest of the file, use
`Ctrl+K Ctrl+X` (**Trim Trailing Whitespace**).

Careful with whitespace in someone else's file: if a file you are fixing has
trailing whitespace throughout, saving it trims every line and the diff for a
one-line change becomes a whole-file diff. Use **Save without Formatting** (Linux: `Ctrl+K S`; Windows:
`Ctrl+K Ctrl+Shift+S`, because `Ctrl+K S` is Save All there) to save only your change, or turn trimming off for that workspace.

### Make invisible characters visible

Text pasted from web pages, chat apps, PDFs, or ticket systems often brings
along characters that look like ordinary spaces and quotes but are not. Those
characters break configs in ways that are hard to see.

| Character | Looks like | Breaks |
| -- | -- | -- |
| U+00A0 non-breaking space | space | YAML indentation, shell word splitting, `sshd_config` keywords |
| U+200B zero-width space | nothing | Hostnames, keys, any token it ends up inside |
| U+2018/2019, U+201C/201D | `'` `"` | Shell quoting, JSON, YAML |
| U+2013/2014 en/em dash | `-` | Command-line options: `–-force` is not `--force` |
| Tab where spaces expected | spaces | YAML (tabs are illegal for indentation), Python |

```jsonc
"editor.renderWhitespace": "boundary",   // dots/arrows for leading, trailing, and multiple spaces; "all" shows every one
"editor.renderControlCharacters": true,  // default
"editor.unicodeHighlight.invisibleCharacters": true,  // default; boxes zero-width and other invisible characters
"editor.unicodeHighlight.ambiguousCharacters": true,  // default; boxes characters that look like ASCII (Cyrillic а, smart quotes)
"[shellscript]": { "editor.unicodeHighlight.nonBasicASCII": true },
"[yaml]":        { "editor.unicodeHighlight.nonBasicASCII": true },
"[ini]":         { "editor.unicodeHighlight.nonBasicASCII": true },
"[powershell]":  { "editor.unicodeHighlight.nonBasicASCII": true }
```

`nonBasicASCII` highlights **any** non-ASCII character. That is useful in
scripts and configs, where non-ASCII characters are almost always a mistake,
but too noisy for Markdown or prose, so the example enables it per language.

In a trusted workspace, `nonBasicASCII` doesn't check comments
(`editor.unicodeHighlight.includeComments` defaults to
`"inUntrustedWorkspace"`). Set `"editor.unicodeHighlight.includeComments": true`
in the same blocks to check comments too.

Remember that `[plaintext]` turns invisible and ambiguous highlighting off by
default (§1). If you paste into a scratch `.txt` file to inspect something,
switch the language mode (`Ctrl+K M`) or override `[plaintext]`.

When VS Code highlights a character, hover over it for its code point and a
one-click fix.

______________________________________________________________________

## 5. Fonts: JetBrains Mono

JetBrains Mono is designed for code. It has a tall x-height, clearly
distinguished `0`/`O`, `1`/`l`/`I`, and `rn`/`m`, and optional ligatures (§6). It
is free under the SIL Open Font License.

There are three families to choose from:

| Family | Use |
| -- | -- |
| `JetBrains Mono` | The normal font, with ligatures available |
| `JetBrains Mono NL` | "No Ligatures" build. Choose it to rule out ligatures entirely (and ignore §6). |
| `JetBrainsMono Nerd Font` | Third-party patched build with icon glyphs for shell prompts (Starship, oh-my-posh) |

### Install: Debian 13

```bash
sudo apt install fonts-jetbrains-mono
fc-list | grep -i "JetBrains Mono" | head -3
```

The Debian package (2.304 in Debian 13) installs static TTFs: Thin through
ExtraBold, with italics. It does not include the NL family.

### Install: RHEL 8 / 9 / 10

**RHEL 10:** EPEL 10 packages it:

```bash
sudo dnf install -y epel-release      # or the EPEL 10 release RPM from Fedora
sudo dnf install -y jetbrains-mono-fonts
sudo dnf install -y jetbrains-mono-nl-fonts   # optional: the no-ligatures family
```

**RHEL 8 and 9:** EPEL doesn't carry it. Install the upstream release
system-wide:

```bash
VER=2.304
curl -fLO "https://github.com/JetBrains/JetBrainsMono/releases/download/v${VER}/JetBrainsMono-${VER}.zip"
sudo mkdir -p /usr/local/share/fonts/jetbrains-mono
sudo unzip -j -o "JetBrainsMono-${VER}.zip" 'fonts/ttf/*.ttf' -d /usr/local/share/fonts/jetbrains-mono
sudo chmod 644 /usr/local/share/fonts/jetbrains-mono/*.ttf
sudo fc-cache -f
fc-list | grep -i "JetBrains Mono" | head -3
```

For your account only, use `~/.local/share/fonts/` and run `fc-cache -f` without
`sudo`. Check the releases page for a newer version before using `VER=2.304`.

### Install: Windows 11

1. Download the latest `JetBrainsMono-<version>.zip` from
   `https://github.com/JetBrains/JetBrainsMono/releases`.
1. Extract it and open `fonts\ttf\`.
1. Select all the `.ttf` files → right-click → **Install for all users**. (Plain
   **Install** is per-user. Some apps that run elevated don't see per-user fonts.)
1. **Fully quit and restart VS Code.** It reads the font list at startup.

The `ttf` folder holds the static fonts, including the `JetBrainsMonoNL-*`
no-ligatures family. Selecting every file there installs both families, which
is harmless. The `variable` folder holds a variable font, which is optional. Install one or the other, not both, so Windows doesn't
show duplicate families.

### Configure the editor

```jsonc
"editor.fontFamily": "'JetBrains Mono', 'Cascadia Mono', Consolas, 'DejaVu Sans Mono', monospace",
"editor.fontSize": 14,
"editor.lineHeight": 1.5,          // a value under 8 is a multiplier of fontSize; 8 or more is pixels
"editor.fontWeight": "normal",     // "300" (Light) or "500" (Medium) if that weight is installed
"editor.letterSpacing": 0
```

- `editor.fontFamily` takes a CSS font list. **Quote names that contain spaces.**
  The fallbacks after JetBrains Mono apply on any machine where it is
  missing (Cascadia Mono on Windows 11, DejaVu Sans Mono on most Linux).
- On Linux, `fc-match "JetBrains Mono"` must return
  `JetBrainsMono-Regular.ttf`. If it returns DejaVu or another font, the
  name or the font cache is wrong (`fc-cache -f`).
- If the font isn't applied, the name is usually wrong. Use the **family**
  name exactly as `fc-list` (Linux) or the Fonts settings page (Windows)
  reports it: `JetBrains Mono`, with a space.
- `Ctrl+=` / `Ctrl+-` zoom the **whole window**, not just the editor font.
  `"editor.mouseWheelZoom": true` makes `Ctrl`+scroll change only the editor
  font size.

### Use it everywhere, not just the editor

Several parts of VS Code have their own font setting. Some fall back to
something other than the editor font if you leave them unset: the debug
console uses VS Code's built-in monospace font, and the source control
commit box uses the UI font. CodeLens and inlay hints already follow
`editor.fontFamily` when left empty, so those two lines are optional:

```jsonc
"terminal.integrated.fontFamily": "'JetBrains Mono', monospace",   // or the Nerd Font for prompt icons
"terminal.integrated.fontSize": 14,
"debug.console.fontFamily": "'JetBrains Mono', monospace",
"scm.inputFontFamily": "editor",                                   // commit message box
"markdown.preview.fontFamily": "-apple-system, 'Segoe UI', 'Noto Sans', sans-serif",  // keep previews proportional
"editor.codeLensFontFamily": "'JetBrains Mono', monospace",
"editor.inlayHints.fontFamily": "'JetBrains Mono', monospace"
```

`terminal.integrated.fontFamily` falls back to `editor.fontFamily` when empty.
Set it explicitly if you use a Nerd Font for your prompt in the terminal but
the plain font in the editor.

______________________________________________________________________

## 6. Ligatures and OpenType features

Ligatures combine character sequences such as `->`, `=>`, `!=`, `>=`, `===`,
`<=>`, and `::` into single glyphs. The underlying characters don't change.
Copy, search, and the cursor still treat `!=` as two characters.

### Editor

```jsonc
"editor.fontLigatures": true
```

`editor.fontLigatures` takes either a boolean or a CSS `font-feature-settings`
string. `true` turns on both ligature features (`liga` and `calt`). The string
form lets you turn individual OpenType features on or off:

```jsonc
// Ligatures plus a slashed zero
"editor.fontLigatures": "'calt', 'zero'",

// Ligatures OFF but slashed zero ON (the boolean can't express this)
"editor.fontLigatures": "'calt' off, 'zero'"
```

JetBrains Mono has a full set of code ligatures: 153 ligature glyphs in
version 2.304, for `->`, `=>`, `!=`, `>=`, `===`, `::`, `/*`, and more. Fonts
can put ligatures in either of two OpenType features: `liga` (standard
ligatures) or `calt` (contextual alternates). JetBrains Mono puts all of
them in `calt` and has no `liga` feature, so `'calt'` is the one to name in
the string form. `true` works as well, because it turns on both.

Features in the JetBrains Mono 2.304 TTFs (read from the font files in the
Debian package with fontTools):

| Feature | Effect |
| -- | -- |
| `calt` | Contextual alternates. In JetBrains Mono, this is what produces the code ligatures. |
| `zero` | Slashed zero instead of the default dotted zero |
| `ss01`–`ss02` | Stylistic sets (alternate letterforms) |
| `ss19`, `ss20` | Further stylistic sets |
| `cv01`–`cv12`, `cv14`–`cv20`, `cv99` | Per-character variants (alternate `l`, `g`, `r`, and others) |
| `case`, `frac`, `sups`, `subs` | Case-sensitive punctuation, fractions, superscript, subscript |

The README in the JetBrains Mono repository shows each `ssNN`/`cvNN` with a
picture. Try them in the string form and keep the ones you like.

### Integrated terminal

The terminal has its own ligature settings, off by default:

```jsonc
"terminal.integrated.fontLigatures.enabled": true,
"terminal.integrated.fontLigatures.featureSettings": "\"calt\" on, \"zero\" on"
```

Terminal ligatures come from an xterm.js add-on that reads the font file
directly. If VS Code can't read the font file, the terminal draws only a fixed
list of common ligatures, set in
`terminal.integrated.fontLigatures.fallbackLigatures`.

### Should you use them?

Opinions differ, and both sides have a case:

- **For:** operators such as `!=`, `>=`, `=>` read as one symbol, and arrows and
  comparisons are quicker to scan.
- **Against:** in shell, `2>&1`, `<<-`, `|&`, `>>=`, and `www` can render in
  unexpected ways. When you are checking a command character by character
  before running it as root, you want to see exactly what you typed.

A sensible compromise: ligatures on in the editor, off in the terminal. You
can also turn them off for shell scripts only:

```jsonc
"editor.fontLigatures": true,
"[shellscript]": {
    "editor.fontLigatures": "'calt' off, 'zero'"
}
```

______________________________________________________________________

## 7. Editor ergonomics

### Indentation

```jsonc
"editor.insertSpaces": true,
"editor.tabSize": 4,
"editor.detectIndentation": true,   // default; matches an existing file's style
"[yaml]":       { "editor.tabSize": 2 },
"[json]":       { "editor.tabSize": 2 },
"[jsonc]":      { "editor.tabSize": 2 },
"[makefile]":   { "editor.insertSpaces": false },   // already the built-in default; listed for clarity
"[powershell]": { "editor.tabSize": 4 }
```

With `editor.detectIndentation` on, VS Code reads the file and uses its
existing indentation, overriding your settings. That's what you want when
editing someone else's config. The status bar shows the detected setting
(`Spaces: 4` or `Tab Size: 4`). Click it to convert the file's indentation.

### Layout and visual aids

```jsonc
"editor.rulers": [80, 120],
"editor.wordWrap": "off",                 // configs: off; set "on" per language for prose
"editor.minimap.enabled": false,          // frees horizontal space; little use for config files
"editor.stickyScroll.enabled": true,      // pins the enclosing function/block header at the top
"editor.guides.bracketPairs": "active",   // vertical guide for the bracket pair the cursor is in
"editor.bracketPairColorization.enabled": true,   // default
"editor.cursorBlinking": "solid",
"editor.cursorSmoothCaretAnimation": "off",
"editor.smoothScrolling": false,
"workbench.tree.indent": 16,              // deeper indent in the Explorer for /etc-style trees
"workbench.tree.renderIndentGuides": "always",
"breadcrumbs.enabled": true
```

Sticky scroll is especially useful in long YAML (Ansible plays, Kubernetes
manifests) and in large shell scripts. It shows which block you are in.

### Editing behaviour

```jsonc
"editor.formatOnSave": false,             // see note
"editor.formatOnSaveMode": "modifications", // if enabled: format only changed lines (needs git)
"editor.linkedEditing": true,             // rename matching HTML/XML tags together
"editor.emptySelectionClipboard": true,   // default; Ctrl+C with no selection copies the whole line
"editor.copyWithSyntaxHighlighting": false, // paste plain text into tickets and email
"editor.acceptSuggestionOnEnter": "smart",
"editor.multiCursorModifier": "alt",      // default; Alt+click adds a cursor
"files.autoSave": "off",
"workbench.editor.enablePreview": true    // single-click opens a temporary tab (italic title)
```

- **Format on save** is excellent in your own repositories, where a formatter
  is part of the workflow. On a production host's `/etc`, it can reformat a
  vendor file you only meant to change by one line. Enable it per workspace or
  per language, not globally.
- **Auto save** is risky on live configs. Some services watch their config
  directory and reload on change, and some tools (`visudo`, `nginx -t` habits)
  assume you validate **before** the file is written. A half-typed file saved
  on a timer can take a service down. Keep `files.autoSave` off, or use
  `"onFocusChange"` at most.

### File associations

Many config files don't have an extension VS Code recognizes. Map them:

```jsonc
"files.associations": {
    "*.conf": "ini",               // a reasonable default; override per path below
    "**/nginx/**/*.conf": "nginx", // requires an nginx syntax extension
    "*.service": "ini",
    "*.timer": "ini",
    "*.socket": "ini",
    "*.network": "ini",
    "**/sudoers.d/*": "ini",
    "*.j2": "jinja",               // requires a Jinja extension
    "**/inventory/*": "ini",
    "*.repo": "ini",
    "*.sources": "properties",     // deb822 apt sources
    "Containerfile": "dockerfile",
    "Containerfile.*": "dockerfile"
}
```

Patterns without a `/` match by file name. Patterns with a `/` match the full
path, so prefix them with `**/`.

______________________________________________________________________

## 8. Integrated terminal

### Default shell profiles

```jsonc
"terminal.integrated.defaultProfile.linux": "bash",
"terminal.integrated.defaultProfile.windows": "PowerShell",   // picks PowerShell 7 (pwsh) if installed
```

To add a profile, or change how an existing one starts, define it under
`terminal.integrated.profiles.<os>`:

```jsonc
"terminal.integrated.profiles.windows": {
    "PowerShell": {
        "source": "PowerShell",
        "args": ["-NoLogo"]
    },
    "Git Bash": {
        "source": "Git Bash"
    },
    "Debian (WSL)": {
        "path": "C:\\Windows\\System32\\wsl.exe",
        "args": ["-d", "Debian"]
    }
},
"terminal.integrated.profiles.linux": {
    "bash": { "path": "bash", "args": ["-l"] },          // login shell: reads ~/.bash_profile
    "root shell": { "path": "sudo", "args": ["-i"] }
}
```

Pick a profile from the `+` dropdown in the terminal panel, or run
**Terminal: Create New Terminal (With Profile)**.

### Behaviour

```jsonc
"terminal.integrated.scrollback": 10000,              // default 1000 is short for log output
"terminal.integrated.enablePersistentSessions": true, // default; terminals survive a window reload
"terminal.integrated.shellIntegration.enabled": true, // default; command markers, exit-code dots, Ctrl+Up/Down jumps
"terminal.integrated.enableMultiLinePasteWarning": "always",
"terminal.integrated.copyOnSelection": false,
"terminal.integrated.rightClickBehavior": "default",  // "paste" mimics PuTTY; risky with a root shell
"terminal.integrated.cursorStyle": "block",
"terminal.integrated.confirmOnExit": "hasChildProcesses",
"terminal.integrated.confirmOnKill": "always",
"terminal.integrated.stickyScroll.enabled": true      // pins the running command's line at the top
```

- **Multi-line paste warning: set it to `"always"`.** When a clipboard holding several commands is pasted into a root shell
  that lacks bracketed paste (for example bash before 5.1, as on RHEL 8),
  every line runs immediately. The default `"auto"` hides the warning whenever
  the shell reports bracketed paste, so `"always"` keeps it on everywhere.
- **Shell integration** adds a gutter mark next to each command (blue for
  success, red for failure), `Ctrl+Up`/`Ctrl+Down` to jump between commands,
  and **Run Recent Command** (`Ctrl+Alt+R`) for searchable history. It works
  automatically for bash, zsh, fish, and PowerShell.
- **Right-click to paste** feels familiar if you come from PuTTY, but a
  mis-click pastes into whatever shell has focus. Use `"default"` (context
  menu). The built-in default differs by OS: `"default"` on Linux, but
  `"copyPaste"` on Windows (right-click pastes when nothing is selected).
  Setting it explicitly is what stops paste-on-right-click on Windows.

### Keys that the terminal should keep

By default VS Code captures some shortcuts before the shell sees them. If
`Ctrl+R` (reverse history search), `Ctrl+P`, or `Ctrl+E` don't reach bash, it is
VS Code keeping them. The fix:

```jsonc
"terminal.integrated.commandsToSkipShell": [
    "-workbench.action.quickOpen"          // leading "-" = let the shell have it (Ctrl+P and Ctrl+E go to bash)
],
"terminal.integrated.allowChords": false   // Ctrl+K in the terminal goes to the shell (kill-line), not a chord
```

`Ctrl+R` reaches the shell already in 1.140.0, unless screen-reader
(accessibility) mode is on, where it opens **Run Recent Command**. If it
doesn't, check that and whether an extension has bound it.

______________________________________________________________________

## 9. Remote - SSH: settings beyond the basics

The companion SSH guide (§11 Linux, §33 Windows) covers installation,
connecting, `remote.SSH.path`, `remote.SSH.remotePlatform`, port forwarding, and
basic troubleshooting. This section adds the settings and techniques you need
once you use Remote - SSH every day across many hosts.

### Remote host requirements

The VS Code server that Remote - SSH installs on the target host needs
**kernel 4.18 or later, glibc 2.28 or later, and libstdc++ 3.4.25 or later**
(check with `strings /usr/lib64/libstdc++.so.6 | grep GLIBCXX_3.4.25`). RHEL 8+ and Debian 10+
meet that. RHEL 7 and CentOS 7 do not, and connections to them fail. For those,
edit over plain `ssh` + `vim`, or mount the remote filesystem with SFTP
(`sshfs`) and edit locally.

The server needs `bash`, `tar`, and either `curl` or `wget` on the remote host,
plus a writable, **executable** home directory (or see `serverInstallPath`
below).

### Recommended user settings

```jsonc
"remote.SSH.connectTimeout": 30,             // seconds; raise it for jump hosts, MFA prompts, slow links
"remote.SSH.showLoginTerminal": true,        // see password/MFA/host-key prompts instead of a silent hang
"remote.SSH.useLocalServer": false,          // see the companion SSH guide for the trade-off
"remote.SSH.localServerDownload": "auto",    // "always" for hosts without internet access (§12)
"remote.SSH.lockfilesInTmp": true,           // needed when $HOME is on NFS

"remote.SSH.defaultExtensions": [
    "timonwong.shellcheck",
    "redhat.vscode-yaml",
    "editorconfig.editorconfig"
],
"remote.SSH.serverInstallPath": {
    "small-root-host": "/opt/vscode-users"   // per host alias; install somewhere other than ~/.vscode-server
},
"remote.downloadExtensionsLocally": false,   // true: the client downloads extensions and pushes them to the host
"remote.autoForwardPorts": true,
"remote.restoreForwardedPorts": true
```

| Setting | When to change it |
| -- | -- |
| `remote.SSH.connectTimeout` | ProxyJump chains, MFA/TOTP prompts, or high-latency links time out at the default |
| `remote.SSH.showLoginTerminal` | Always on while you are troubleshooting. Prompts are visible instead of hidden. |
| `remote.SSH.lockfilesInTmp` | Home directories on NFS, where VS Code's lock files misbehave |
| `remote.SSH.serverInstallPath` | `/home` is `noexec` (a common STIG/CIS control), small, or quota-limited. Point at an exec-capable path. |
| `remote.SSH.localServerDownload` | Remote host can't reach `update.code.visualstudio.com`. The client downloads and copies the server. |
| `remote.downloadExtensionsLocally` | Remote host can't reach the Marketplace. The client downloads extensions and copies them over. |
| `remote.SSH.enableAgentForwarding` | Leave at the default (`true`). It only lets a `ForwardAgent yes` in `~/.ssh/config` take effect in VS Code's remote terminals and git. `ForwardAgent` (OpenSSH default `no`) still decides per host; setting this to `false` breaks forwarding even where you enabled it. |

On hardened hosts, `noexec` on `/home` is the most common reason the server
fails to start: the log shows `Permission denied` when it runs `node`. Point
`serverInstallPath` at a directory the user owns on an exec-capable filesystem.

A `noexec` `/tmp` (another common CIS/STIG control) breaks installs too: the
extension writes its install script to the remote temp directory and runs it
from there. Set `TMPDIR` to an exec-capable directory in the remote shell
profile, or ask for an exception.

**Remote host behind a proxy:** `remote.SSH.httpProxy` and
`remote.SSH.httpsProxy` set `http_proxy`/`https_proxy` for the server's
install and launch. Each takes a string or a per-host object, for example
`{ "dbhost": "http://proxy.example.internal:3128" }`. A change applies only
after **Remote-SSH: Kill VS Code Server on Host…**. With
`"remote.SSH.useCurlAndWgetConfigurationFiles": true`, the installer also
honours the host's `.curlrc`/`.wgetrc`.

### Per-host settings (Remote/Machine scope)

Once connected, run **Preferences: Open Remote Settings (JSON) (SSH: host)**.
That file (`~/.vscode-server/data/Machine/settings.json` on the remote host)
applies only to sessions on that host. Use it for settings that depend on
paths or the system:

```jsonc
// Remote settings on a log server
{
    "files.watcherExclude": {
        "/var/log/**": true,
        "**/.git/objects/**": true,
        "**/node_modules/**": true
    },
    "search.exclude": {
        "/var/log/journal/**": true,
        "**/*.gz": true
    },
    "terminal.integrated.defaultProfile.linux": "bash"
}
```

**File watching is the biggest performance issue with remote folders.** When
you open `/` or `/var`, VS Code tries to watch every file under it, and on a
busy host that can use noticeable CPU. Open the narrowest folder that works
(`/etc/nginx`, not `/etc`), and add `files.watcherExclude` entries for busy
directories.

### Editing root-owned files

VS Code can't save a file your SSH user can't write. Options, safest first:

1. **`sudoedit` with VS Code as the editor.** Run this from the integrated
   terminal of the remote session:

   ```bash
   SUDO_EDITOR="code --wait" sudoedit /etc/ssh/sshd_config
   ```

   `sudoedit` copies the file to a temporary file you own, opens it in your
   VS Code window, and when you close the tab, copies it back as root. You
   edit unprivileged, it works with `sudo` logging and policy, and the original
   is never half-written. Add `export SUDO_EDITOR="code --wait"` to the remote
   `~/.bashrc` (inside `if [ "$TERM_PROGRAM" = "vscode" ]`) to make it
   automatic.

1. **Edit a copy, validate, then install it:**

   ```bash
   cp /etc/nginx/nginx.conf ~/nginx.conf      # edit ~/nginx.conf in VS Code
   sudo nginx -t -c ~/nginx.conf && sudo install -m 644 ~/nginx.conf /etc/nginx/nginx.conf
   ```

1. **Local files only: Retry as Sudo.** On a Linux desktop, saving a local
   file you can't write offers **Retry as Sudo…** (**Overwrite as Sudo…** for
   a read-only file). This doesn't help over Remote - SSH; use `sudoedit`
   there. Never run `sudo code`: VS Code refuses to run as root without
   extra flags, and it leaves root-owned files in your profile.

1. **Connect as root.** Avoid this. It bypasses `sudo` auditing, the server
   and its extensions run as root, and most hardened `sshd_config` files set
   `PermitRootLogin no` anyway.

For network/SSH/firewall changes made this way, use the dead-man's-switch
technique in `proxmox-ve/prevent-lockout-and-revert-guide-r1.0.1.md` so a
mistake reverts itself.

### Know which host you are on

When you have six remote windows open, it is easy to type into the wrong one.
Put the host in the window title:

```jsonc
"window.title": "${remoteName}${separator}${rootName}${separator}${activeEditorShort}${dirty}"
```

For production hosts, colour the window too (see
[§16](#colour-code-production-windows)).

### Remote Tunnels bypass your SSH controls

`code tunnel` (or **Remote Tunnels: Turn on Remote Tunnel Access…**) gives
browser or desktop access to a host through Microsoft's dev tunnels relay,
over outbound HTTPS. It needs no inbound port, and for the same reason it
goes around your SSH hardening, bastion hosts, and session logging. Treat it
as a remote-access method that needs approval. Where it isn't allowed, block
the dev tunnels domains that Microsoft documents at your egress proxy.

### Clean up old servers

Each VS Code update installs a new server on every host you connect to. The old
ones stay until removed:

```bash
du -sh ~/.vscode-server
ls ~/.vscode-server/cli/servers/
```

Run **Remote-SSH: Uninstall VS Code Server from Host** from the client, or
delete `~/.vscode-server` on the host with no VS Code session open. It is
reinstalled on the next connection.

______________________________________________________________________

## 10. Git integration

```jsonc
"git.autofetch": false,                     // true fetches every 3 min; noisy with many remote windows
"git.confirmSync": true,                    // default; ask before push+pull
"git.enableSmartCommit": false,             // don't silently commit all changes when nothing is staged
"git.openRepositoryInParentFolders": "prompt",
"git.inputValidation": true,                // warn on long subject lines
"git.blame.editorDecoration.enabled": false,  // inline blame on the current line (built in)
"git.blame.statusBarItem.enabled": true,      // blame for the current line in the status bar
"diffEditor.ignoreTrimWhitespace": false,   // show whitespace-only changes; they matter in YAML and Makefiles
"diffEditor.renderSideBySide": true,
"diffEditor.hideUnchangedRegions.enabled": true   // collapse unchanged lines in long config diffs
```

- **`diffEditor.ignoreTrimWhitespace: false`** matters. With the default
  (`true`), a diff can look clean while a tab-vs-spaces or trailing-whitespace
  change is about to be committed.
- **`git.openRepositoryInParentFolders`**: if you open a subfolder such as
  `/etc/nginx` on a host that uses `etckeeper`, VS Code finds `/etc/.git` in
  a parent folder. `"prompt"` (the default) asks before adding it to Source
  Control. Opening `/etc` itself always opens the repository.
- **`etckeeper` and ownership:** `/etc/.git` is owned by root. A non-root
  VS Code session gets git's *dubious ownership* error, and Source Control
  shows nothing. Run `sudo etckeeper vcs …` or `sudo git -C /etc …` from the
  terminal rather than adding `/etc` to `safe.directory` for your user.
- Built-in **inline blame** (`git.blame.*`) covers what most people install
  GitLens for. Try it before adding an extension.

Line-ending git config is in [§3](#3-line-endings-lf-everywhere).

______________________________________________________________________

## 11. Privacy, telemetry, updates, and AI features

### Telemetry

```jsonc
"telemetry.telemetryLevel": "off",     // "all" | "error" | "crash" | "off"
"telemetry.feedback.enabled": false,
"workbench.enableExperiments": false,  // no A/B experiment flags fetched from Microsoft
"workbench.settings.enableNaturalLanguageSearch": false   // Settings search stays local
```

`telemetry.telemetryLevel` controls VS Code's own telemetry, and well-behaved
extensions respect it. Some extensions have a separate telemetry setting of
their own. Search the Settings UI for `telemetry` to find them all.

### Updates

```jsonc
"update.mode": "manual",              // "none" | "manual" | "start" | "default"
"update.showReleaseNotes": true,
"extensions.autoUpdate": "off",       // "on" (default) | "off"; a legacy false still means off
"extensions.autoCheckUpdates": true
```

- On Linux, when VS Code comes from the `apt`/`dnf` repository (§2), the
  **package manager** installs updates. `update.mode` only controls whether and when VS Code checks for them.
- `"manual"` turns off automatic background checks. VS Code finds an update
  only when you run **Help → Check for Updates**, so nothing downloads or
  restarts in the middle of a change window. `"start"` checks once at
  startup, and `"none"` turns updates off entirely.
- Turning off extension auto-update is a reasonable change-control choice.
  Extensions run with your privileges on your machine and on every remote host
  you connect to. A compromised extension update is a supply-chain risk. Review
  updates in the Extensions view (**Show Outdated Extensions**) and apply them
  deliberately.
- A middle ground: leave auto-update on but hold back new extension versions
  for a few days with `"extensions.autoUpdateDelay": 72` (hours; default 12).
  A malicious release is often pulled before the delay runs out.

### AI features

VS Code 1.140.0 builds in AI chat and inline suggestions (GitHub Copilot). To
turn off all of it, including the chat panel and the Command Center entry
point:

```jsonc
"chat.disableAIFeatures": true
```

If you use AI features, remember that whatever is open (configs, scripts, log
excerpts) may be sent to the provider as context. Check your organization's
policy before using them on production configs or anything containing
secrets. Turning them off only for a sensitive workspace is a reasonable
middle ground: set `chat.disableAIFeatures` in that workspace's settings.

### Workspace Trust

```jsonc
"security.workspace.trust.enabled": true,             // default; keep it
"security.workspace.trust.untrustedFiles": "prompt"
```

Workspace Trust opens unfamiliar folders in **Restricted Mode**: tasks, debug
configurations, and workspace settings that run code are disabled until you
trust the folder. Keep it on. A cloned repository's `.vscode/tasks.json` or
`settings.json` can run commands. Trust only folders you would run `make` in.

Before you trust a folder from someone else, read its `.vscode/settings.json`
for settings that point at an executable path (for example
`*.path` or `terminal.integrated.profiles.*`).

### Managed (enforced) settings

VS Code can enforce some settings as **policies**. Enforced settings appear
greyed out with a "managed by your organization" note. Policies are keyed by
**policy name**, not setting ID. Examples in 1.140.0:

| Policy name | Setting |
| -- | -- |
| `UpdateMode` | `update.mode` |
| `TelemetryLevel` | `telemetry.telemetryLevel` |
| `EnableFeedback` | `telemetry.feedback.enabled` |
| `AllowedExtensions` | `extensions.allowed` |
| `ExtensionsAutoUpdate` | `extensions.autoUpdate` |
| `ExtensionsAutoUpdateDelay` | `extensions.autoUpdateDelay` |

- **Windows:** Group Policy. The ADMX/ADML templates ship in the `policies`
  folder of the VS Code download.

- **Linux:** VS Code reads `/etc/vscode/policy.json` (root-owned; deploy it
  with Ansible or similar), using the same policy names:

  ```json
  {
      "UpdateMode": "none",
      "TelemetryLevel": "off",
      "ExtensionsAutoUpdate": "off"
  }
  ```

`chat.disableAIFeatures` has **no** policy in 1.140.0. To enforce limits on
AI features, use the `Chat*` policies (for example `ChatAgentMode`,
`ChatMCP`) or your GitHub Copilot organization policy, and deploy
`chat.disableAIFeatures` in user settings through configuration management
(see §14).

______________________________________________________________________

## 12. Proxies, internal CAs, and offline hosts

### Corporate proxy

```jsonc
"http.proxy": "http://proxy.example.internal:3128",
"http.noProxy": ["localhost", "127.0.0.1", ".example.internal"],
"http.proxySupport": "override",    // "off" | "on" | "fallback" | "override"
"http.proxyStrictSSL": true,         // keep true; see internal CA below
"http.systemCertificates": true      // default; trust the OS certificate store
```

VS Code also honours `HTTP_PROXY`/`HTTPS_PROXY`/`NO_PROXY` environment variables
when it is started from a shell that sets them.

### Internal / TLS-inspecting CA

If a TLS-inspecting proxy re-signs traffic, you'll see errors such as
`unable to get local issuer certificate`. The fix is to **add the CA to the OS
trust store**. Don't set `http.proxyStrictSSL: false`, which turns off
certificate checking for everything.

```bash
# Debian 13
sudo cp corp-root-ca.crt /usr/local/share/ca-certificates/ && sudo update-ca-certificates
# RHEL 8/9/10
sudo cp corp-root-ca.crt /etc/pki/ca-trust/source/anchors/ && sudo update-ca-trust
```

On Windows, import the CA into **Local Computer → Trusted Root Certification
Authorities** (usually done by Group Policy). With
`http.systemCertificates: true`, VS Code picks it up after a restart.

On Linux, the Chromium side of VS Code also uses your NSS certificate
database. `certutil` is in `libnss3-tools` on Debian and `nss-tools` on RHEL.
Initialize the database once if it does not already exist, then add the CA:

```bash
mkdir -p "$HOME/.pki/nssdb"
certutil -N -d "sql:$HOME/.pki/nssdb" --empty-password  # run once; skip if already initialized
certutil -A -d "sql:$HOME/.pki/nssdb" -t "C,," -n corp-root -i corp-root-ca.crt
```

### Air-gapped or no-internet environments

| Need | Approach |
| -- | -- |
| VS Code itself | Mirror the `packages.microsoft.com` repository (apt/dnf), or copy the `.deb`/`.rpm`/installer across. |
| Extensions on the client | On a connected machine, download the `.vsix` from the extension's Marketplace page (**Download Extension**). Then on the offline machine: `code --install-extension ./name.vsix`. |
| Server on a remote host with no internet | `"remote.SSH.localServerDownload": "always"`: the client downloads the server and copies it over SSH. |
| Extensions on a remote host with no internet | `"remote.downloadExtensionsLocally": true`: the client downloads and pushes them. |
| Both client and host offline | Pre-stage the server tarball for the client's exact commit (`code --version` line 2) on the host. This depends on the build; follow the Remote - SSH docs for the current layout. |

The server version **must match the client's commit hash exactly**. After you
update the client, every remote host needs the matching server.

______________________________________________________________________

## 13. Extensions for sysadmin work

Install an extension with
`code --install-extension <id>` or `Ctrl+P` → `ext install <id>`. The IDs below
are publisher-qualified. Check the publisher before installing, because
look-alike extensions exist.

### Core

| Extension ID | Purpose |
| -- | -- |
| `ms-vscode-remote.remote-ssh` | Remote - SSH (companion SSH guide §11/§33) |
| `ms-vscode-remote.remote-ssh-edit` | Syntax highlighting and completion for `~/.ssh/config` (`ssh_config`). Installed with Remote - SSH. |
| `ms-vscode.remote-explorer` | Remote Explorer side bar (installed with Remote - SSH) |
| `ms-vscode-remote.remote-wsl` | WSL targets from Windows |
| `editorconfig.editorconfig` | Applies `.editorconfig` (LF, charset, indent). VS Code does not do this natively. |

### Languages and linting

| Extension ID | Purpose |
| -- | -- |
| `timonwong.shellcheck` | ShellCheck diagnostics as you type. Needs `shellcheck` installed (`apt`/`dnf`). |
| `mkhl.shfmt` | Shell formatter using `shfmt` |
| `redhat.vscode-yaml` | YAML validation with JSON Schema (Kubernetes, GitHub Actions, compose) |
| `redhat.ansible` | Ansible language server, `ansible-lint` integration |
| `ms-vscode.powershell` | PowerShell language server, PSScriptAnalyzer, debugger |
| `ms-python.python` | Python (adds Pylance and the debugger) |
| `charliermarsh.ruff` | Fast Python linter and formatter |
| `hashicorp.terraform` | Terraform / HCL |
| `tamasfe.even-better-toml` | TOML |
| `davidanson.vscode-markdownlint` | Markdown linting |
| `bierner.markdown-mermaid` | Not needed on 1.140: Mermaid rendering in the Markdown preview is now built in |
| `ms-azuretools.vscode-containers` | Container Tools: Dockerfile/Containerfile and compose support, container explorer |

### Utilities

| Extension ID | Purpose |
| -- | -- |
| `mechatroner.rainbow-csv` | Column colouring and SQL-like queries over CSV/TSV exports |
| `ms-vscode.hexeditor` | Hex editor (find BOMs, stray `\r`, binary headers) |
| `usernamehw.errorlens` | Show diagnostics inline at the end of the line |
| `streetsidesoftware.code-spell-checker` | Spelling in comments and Markdown |
| `johnpapa.vscode-peacock` | Colour each workspace window (alternative to §16's manual approach) |
| `mhutchie.git-graph` | Commit graph view. Unmaintained since 2021; the built-in Source Control **Graph** view covers most uses. |
| `emilast.logfilehighlighter` | Syntax highlighting for `.log` files (levels, timestamps, GUIDs, IPs) |

For Cisco IOS/IOS XE configs, search the Marketplace for "Cisco IOS". Several
community syntax extensions exist. Check the publisher and recent updates
before choosing one.

### Managing extensions

```bash
# Inventory with versions, for change records
code --list-extensions --show-versions > vscode-extensions.txt

# Reinstall from a list
grep -v '^#' vscode-extensions.txt | cut -d@ -f1 | xargs -n1 code --install-extension

# Remote host: list extensions installed in the remote server (run in the remote terminal)
code --list-extensions
```

Recommend extensions for a repository by committing `.vscode/extensions.json`.
VS Code prompts anyone who opens the folder:

```jsonc
{
    "recommendations": [
        "editorconfig.editorconfig",
        "timonwong.shellcheck",
        "redhat.vscode-yaml"
    ],
    "unwantedRecommendations": []
}
```

Keep extensions to a minimum. Each one is code with your privileges, it slows
startup, and it is installed again on every remote host. Use **Profiles** (§14)
to keep, for example, a heavy Python or Terraform set out of your everyday
profile.

______________________________________________________________________

## 14. Profiles, Settings Sync, and keeping config in git

### Profiles

A **profile** is a named set of settings, keybindings, snippets, tasks,
extensions, and UI state. Switch between them per window.

- `Ctrl+Shift+P` → **Profiles: New Profile** (start from an empty profile,
  copy the current one, or use a template).
- A folder or workspace remembers the profile it was last opened with.
- `code --profile "Sysadmin" /etc/ansible` opens that folder with that profile.
- **Profiles: Export Profile** writes a `.code-profile` file, or a GitHub gist,
  that someone else can import.

A useful set: **Default** (minimal, for everyday editing), **Sysadmin** (Remote-SSH, ShellCheck, YAML, Ansible, PowerShell), **Docs** (Markdown, spell check), **Presentation** (large font, no minimap, high-contrast
theme, for screen sharing).

### Settings Sync

**Settings Sync** (gear icon → **Backup and Sync Settings**) syncs settings,
keybindings, snippets, extensions, and profiles through a Microsoft or GitHub
account.

```jsonc
"settingsSync.ignoredSettings": [
    "remote.SSH.path",                 // differs between Windows and Linux
    "remote.SSH.configFile",
    "terminal.integrated.profiles.windows",
    "http.proxy"
],
"settingsSync.ignoredExtensions": []
```

`settingsSync.ignoredSettings` keeps machine-specific values out of sync.
Settings Sync stores data with Microsoft or GitHub, so check your organization's
policy before using it on a work machine.

### Keeping config in git instead

If Settings Sync isn't allowed, or you'd rather track changes yourself, keep
the files in a dotfiles repository and symlink them:

```bash
# Linux
CFG=~/.config/Code/User
mkdir -p ~/dotfiles/vscode
for f in settings.json keybindings.json; do
    mv "$CFG/$f" ~/dotfiles/vscode/ 2>/dev/null
    ln -sf ~/dotfiles/vscode/$f "$CFG/$f"
done
# Move an existing real snippets directory first, or ln creates snippets/snippets
[ -d "$CFG/snippets" ] && [ ! -L "$CFG/snippets" ] && mv "$CFG/snippets" ~/dotfiles/vscode/
ln -sfn ~/dotfiles/vscode/snippets "$CFG/snippets"
code --list-extensions > ~/dotfiles/vscode/extensions.txt
```

```powershell
# Windows: symbolic links need Developer Mode or an elevated prompt
$cfg = "$env:APPDATA\Code\User"
New-Item -ItemType SymbolicLink -Path "$cfg\settings.json" -Target "$HOME\dotfiles\vscode\settings.json" -Force
```

Since settings files allow comments, the dotfiles copy can carry its own
change notes. To keep one file across Linux and Windows, put OS-specific values
in `settingsSync.ignoredSettings` and keep them per machine, or rely on the
per-OS keys (`*.linux`, `*.windows`) where VS Code provides them.

______________________________________________________________________

## 15. Keybindings, snippets, and tasks

### Keybindings

Open with `Ctrl+K Ctrl+S` (UI) or **Preferences: Open Keyboard Shortcuts
(JSON)**. Useful additions (`keybindings.json`):

```jsonc
[
    // Change line endings of the current file (no default binding)
    { "key": "ctrl+k ctrl+e", "command": "workbench.action.editor.changeEOL" },

    // Run the selected line(s) in the terminal: copy a command from a runbook and execute it
    { "key": "ctrl+alt+enter", "command": "workbench.action.terminal.runSelectedText",
      "when": "editorTextFocus && editorHasSelection" },

    // Jump focus between editor and terminal
    { "key": "ctrl+alt+;", "command": "workbench.action.terminal.focus", "when": "!terminalFocus" },
    { "key": "ctrl+alt+;", "command": "workbench.action.focusActiveEditorGroup", "when": "terminalFocus" }
]
```

Avoid `Ctrl+Alt+T` on GNOME (the Debian 13 and RHEL default desktop): the
desktop takes it to open a terminal, so VS Code never receives it.

**Run Selected Text** is a good way to work through a Markdown runbook: open the
runbook, select a command, press the key, and it runs in the active terminal,
which can be a Remote - SSH session. The runbook stays the record of what you
ran.

### Snippets

**Snippets: Configure Snippets** → `shellscript.json`:

```jsonc
{
    "Strict bash header": {
        "prefix": "bashstrict",
        "body": [
            "#!/usr/bin/env bash",
            "# ${1:Description}",
            "set -euo pipefail",
            "IFS=$'\\n\\t'",
            "",
            "$0"
        ],
        "description": "Bash script header with strict mode"
    },
    "Root check": {
        "prefix": "needroot",
        "body": [
            "if [[ \\$EUID -ne 0 ]]; then",
            "    echo \"Run as root\" >&2",
            "    exit 1",
            "fi"
        ]
    }
}
```

`$1`, `$2` are tab stops and `$0` is the final cursor position. A literal `$`
in the body is written as `\\$`.

### Tasks

`.vscode/tasks.json` runs commands from **Run Task** (`Ctrl+Shift+P` →
**Tasks: Run Task**), with output in the terminal panel and, when a problem
matcher is set, errors in the Problems panel:

```jsonc
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "shellcheck: current file",
            "type": "shell",
            "command": "shellcheck -f gcc '${file}'",
            "problemMatcher": {
                "owner": "shellcheck",
                "fileLocation": "absolute",
                "pattern": {
                    "regexp": "^(.*):(\\d+):(\\d+):\\s+(error|warning|note):\\s+(.*)$",
                    "file": 1, "line": 2, "column": 3, "severity": 4, "message": 5
                }
            },
            "group": "test"
        },
        {
            "label": "mdformat: current file",
            "type": "shell",
            "command": "~/.venv/bin/mdformat '${file}'",
            "problemMatcher": []
        },
        {
            "label": "ansible: syntax check",
            "type": "shell",
            "command": "ansible-playbook --syntax-check '${file}'",
            "problemMatcher": []
        }
    ]
}
```

`shellcheck -f gcc` prints `file:line:col: severity: message`, and the inline
problem matcher turns that into entries in the Problems panel that you can
click through to each line. That works even without the ShellCheck
extension. VS Code has no built-in `$gcc` matcher (it comes with the C/C++
extension), so define the pattern in the task as shown.

______________________________________________________________________

## 16. Tips and tricks

### Colour-code production windows

Colour the title bar and status bar per workspace, so a production session
can't be mistaken for a lab one. Save a local **workspace file** (for example
`~/workspaces/prod-web01.code-workspace`). It can point at a remote folder and
carries its own settings:

```jsonc
{
    "folders": [
        { "uri": "vscode-remote://ssh-remote+prod-web01/etc/nginx" }
    ],
    "settings": {
        "workbench.colorCustomizations": {
            "titleBar.activeBackground": "#8b0000",
            "titleBar.activeForeground": "#ffffff",
            "statusBar.background": "#8b0000",
            "statusBar.foreground": "#ffffff"
        },
        "window.title": "PROD ${separator}${remoteName}${separator}${activeEditorShort}${dirty}"
    }
}
```

Open it with `code ~/workspaces/prod-web01.code-workspace`. Title-bar colours need
`"window.titleBarStyle": "custom"`, which is the default on Windows and on
current Linux builds.

### Lock what you shouldn't edit

```jsonc
"files.readonlyInclude": {
    "**/99_Archive/**": true,
    "**/*.lock": true
},
"files.readonlyFromPermissions": true     // show files you can't write as read-only
```

Read-only files open with a lock icon. **Toggle Active Editor Read-only in
Session** overrides that for the current session when you do need to edit one.

### Undo a bad save with Local History

VS Code keeps a copy of every file each time you save it
(`workbench.localHistory.enabled`, on by default), even outside git. Open the
**Timeline** view at the bottom of the Explorer, or run **Local History: Find
Entry to Restore**, to compare against or restore an earlier version of a
config file. Over Remote - SSH, the history is stored on the remote host.

### Compare anything

- Two files: select both in the Explorer → right-click → **Compare Selected**.

- File against clipboard: **File: Compare Active File with Clipboard**. Handy for
  checking a vendor's suggested config against yours.

- Two hosts' configs: copy them to temporary files first, then diff:

  ```bash
  ssh host1 cat /etc/ssh/sshd_config > /tmp/host1.sshd_config
  ssh host2 cat /etc/ssh/sshd_config > /tmp/host2.sshd_config
  code -d /tmp/host1.sshd_config /tmp/host2.sshd_config
  ```

  Bash process substitution (`code -d <(ssh …) <(ssh …)`) doesn't work: the
  `code` command passes the `/dev/fd/NN` paths to the VS Code process that's
  already running, and that process can't read another process's pipes.

### Search across many files

- `Ctrl+Shift+F` supports regular expressions (`Alt+R`), include/exclude
  globs, and **replace across files** with a preview.
- In the search box, `\r\n` (or just `\r`) finds CRLF line endings (`\r$`
  does not: VS Code runs ripgrep in CRLF mode, where `$` already matches
  before `\r\n`), and `[^\x00-\x7F]` finds
  non-ASCII characters (with regex on).
- `"search.useIgnoreFiles": true` (default) honours `.gitignore`. Turn it off
  per search with the **Use Exclude Settings and Ignore Files** toggle when you
  need to search ignored files (build output, archives).

### Multi-cursor editing for config files

- `Alt+click`: add a cursor.
- `Ctrl+Alt+Up/Down` (Windows) / `Shift+Alt+Up/Down` (Linux): add a cursor on
  the line above or below (column editing).
- `Ctrl+D`: select the next occurrence of the current word. `Ctrl+Shift+L`:
  select all occurrences.
- `Shift+Alt+drag`: box (column) selection, for editing a column in an aligned
  table such as `/etc/hosts` or `fstab`.

### Other useful commands

| Command | Use |
| -- | -- |
| **Sort Lines Ascending** | Host lists, allowlists |
| **Delete Duplicate Lines** | De-duplicate IP lists |
| **Join Lines** (no default key on Linux/Windows; `Ctrl+J` is Toggle Panel) | Join wrapped lines |
| **Transform to Uppercase / Lowercase** | MAC addresses, hostnames |
| **Fold All** / **Unfold All** (`Ctrl+K Ctrl+0` / `Ctrl+K Ctrl+J`) | Long YAML |
| **Toggle Word Wrap** (`Alt+Z`) | Read one long log line without changing settings |
| **Developer: Inspect Editor Tokens and Scopes** | Why something is (or isn't) highlighted |

______________________________________________________________________

## 17. Troubleshooting

### General approach

1. **Is it an extension?** Run **Help: Start Extension Bisect**. VS Code
   disables half your extensions at a time and asks whether the problem is
   still there until it finds the culprit. Or start with
   `code --disable-extensions`.
1. **Is it a setting?** Start a clean, isolated instance:
   `code --user-data-dir /tmp/vsc-clean --extensions-dir /tmp/vsc-clean-ext`.
   If the problem is gone, it's in your profile.
1. **Logs:** **Developer: Show Logs…** (main, window, extension host, remote).
   **Output** panel (`Ctrl+Shift+U` on Windows, `Ctrl+K Ctrl+H` on Linux) → pick the source from the dropdown, for
   example **Remote - SSH**.
1. **Process and memory use:** **Developer: Open Process Explorer**, or
   `code --status`.

### Specific problems

| Symptom | Cause and fix |
| -- | -- |
| Files still open as `CRLF` despite `files.eol: "\n"` | They already contain CRLF (`files.eol` affects new files only). Usually git `core.autocrlf=true` on Windows. Fix per §3, then `git add --renormalize .`. |
| `.editorconfig` is ignored | VS Code needs the `editorconfig.editorconfig` extension. Also check `root = true` and section glob syntax. |
| Font setting has no effect | Family name wrong or not quoted. Font installed after VS Code started: quit fully (all windows) and restart. On Linux, run `fc-cache -f`. |
| Ligatures in the editor but not the terminal | The terminal has its own setting, `terminal.integrated.fontLigatures.enabled`. If VS Code can't read the font file, only the `fontLigatures.fallbackLigatures` list renders. |
| Bold text in the terminal looks wrong | Set `terminal.integrated.fontWeightBold` to a weight you have installed (for example `"bold"` or `"700"`). |
| Remote - SSH hangs on "Setting up SSH Host" | Turn on `remote.SSH.showLoginTerminal` to see the prompt it is waiting at. Also check `noexec` on `$HOME` (§9), disk space, and the SSH guide's §11 checklist. |
| Remote connection fails after a client update | Server for the new commit can't download on the host. Use `remote.SSH.localServerDownload: "always"`. |
| High CPU on the remote host | File watcher on a large tree. Open a narrower folder, add `files.watcherExclude` in Remote settings (§9). |
| `Ctrl+P`/`Ctrl+K`/`Ctrl+E` don't reach bash | VS Code keeps them. See "Keys that the terminal should keep" in §8. |
| Settings change has no effect | Overridden at a higher scope (workspace, folder, language block, or policy). The Settings UI shows "Also modified in…". |
| "Unable to watch for file changes" (Linux) | inotify watch limit reached. Raise it: `echo 'fs.inotify.max_user_watches=524288' \| sudo tee /etc/sysctl.d/90-vscode.conf && sudo sysctl --system`, or narrow the tree with `files.watcherExclude`. |
| Large log opens with highlighting and folding off | Expected: `editor.largeFileOptimizations`. For multi-gigabyte logs use `less` or `journalctl` instead. |
| Settings Sync or GitHub sign-in doesn't stay signed in (Linux) | No usable keyring (KDE, minimal window managers, headless sessions). In **Preferences: Configure Runtime Arguments** (`argv.json`), set `"password-store": "gnome-libsecret"` (or `"kwallet6"`), and install `gnome-keyring`/`libsecret`. |
| `settings.json` shows red squiggles but still works | JSONC tolerates trailing commas with a warning. A missing comma or quote **does** break the rest of the file. Check the Problems panel. |

### Reset

Close VS Code first.

| Reset | Linux | Windows |
| -- | -- | -- |
| User settings and keybindings | Move `settings.json` and `keybindings.json` in `~/.config/Code/User/` aside | Move `settings.json` and `keybindings.json` in `%APPDATA%\Code\User\` aside |
| All user data | Move `~/.config/Code` aside | Move `%APPDATA%\Code` aside |
| All extensions | Move `~/.vscode/extensions` aside | Move `%USERPROFILE%\.vscode\extensions` aside |
| Remote server on a host | `rm -rf ~/.vscode-server` (on the host) | Same, on the remote host |

Move directories aside (`mv ~/.config/Code ~/.config/Code.bak`) rather than
deleting them, so you can copy settings back afterwards.

______________________________________________________________________

## 18. Power-user settings

Settings that are off or set differently by default and are particularly
useful for sysadmin work. Each key below was checked against the 1.140.0
build. The four marked **(safety)** are also in
[Appendix A](#appendix-a-complete-baseline-settingsjson).

### Nest config backups under the file they belong to (safety)

A package update that can't overwrite a config you've changed leaves a copy
next to it: `.rpmnew`/`.rpmsave` on RHEL, `.dpkg-dist`/`.dpkg-old` on Debian.
Those are easy to miss in a directory listing, and an unmerged `.rpmnew` is
how a security fix in a default config quietly never reaches you. File
nesting shows them as an expandable child of the real file in the Explorer:

```jsonc
"explorer.fileNesting.enabled": true,
"explorer.fileNesting.expand": false,      // collapsed: an expand arrow on sshd_config = something to merge
"explorer.fileNesting.patterns": {
    "*": "${capture}.rpmnew, ${capture}.rpmsave, ${capture}.dpkg-dist, ${capture}.dpkg-old, ${capture}.dpkg-new, ${capture}.ucf-dist, ${capture}.bak, ${capture}.orig, ${capture}~"
}
```

Each key is a parent pattern with at most one `*`. `${capture}` in the value
stands for whatever the `*` matched, so with `"*"` it is the parent's full
file name: `sshd_config.rpmnew` nests under `sshd_config`. Nesting only
changes the Explorer view; the files stay where they are.

To list the same files from the command line:

```bash
sudo find /etc \( -name '*.rpmnew' -o -name '*.rpmsave' -o -name '*.dpkg-*' -o -name '*.ucf-*' \) 2>/dev/null
```

### Readable tab names for Ansible roles

In an Ansible repository every role has a `tasks/main.yml`, a
`handlers/main.yml`, and a `defaults/main.yml`, so ten open tabs all say
`main.yml`. Custom labels name each tab after its role:

```jsonc
"workbench.editor.customLabels.patterns": {
    "**/roles/*/tasks/main.yml":    "${dirname(1)}/tasks",
    "**/roles/*/handlers/main.yml": "${dirname(1)}/handlers",
    "**/roles/*/defaults/main.yml": "${dirname(1)}/defaults",
    "**/roles/*/vars/main.yml":     "${dirname(1)}/vars",
    "**/roles/*/meta/main.yml":     "${dirname(1)}/meta"
}
```

`roles/webserver/tasks/main.yml` then shows as **webserver/tasks**.
`${dirname}` is the file's own folder (`tasks`), `${dirname(1)}` the one above
it (`webserver`), and so on. `${filename}` and `${extname}` are also
available. Custom labels are on by default
(`workbench.editor.customLabels.enabled`); patterns are the only thing to
add.

The same idea works for other repeated names, for example
`"**/host_vars/*/main.yml": "${dirname} vars"`.

### A sound when a long command fails or finishes (safety)

Start a long `dnf upgrade`, `rsync`, or Ansible run, switch to something
else, and VS Code plays a sound when the command exits with an error or a
task finishes:

```jsonc
"accessibility.signals.terminalCommandFailed": { "sound": "on" },
"accessibility.signals.taskCompleted":         { "sound": "on" },
"accessibility.signals.taskFailed":            { "sound": "on" }
```

`terminalCommandFailed` relies on shell integration (§8), which is how VS
Code knows a command's exit code. It works in Remote - SSH terminals too.
There is also `accessibility.signals.terminalCommandSucceeded` if you want a
sound for success as well.

### No accidental drag-and-drop moves (safety)

One slip of the mouse in the Explorer can move a directory, such as dragging
`/etc/nginx/sites-enabled` into `conf.d` on a live host. In an editor, a drag
moves the selected text. Turn both off:

```jsonc
"explorer.enableDragAndDrop": false,
"editor.dragAndDrop": false
```

You can still move files with cut and paste (`Ctrl+X` / `Ctrl+V` in the
Explorer), which takes two deliberate steps.

### Make unsaved changes obvious (safety)

```jsonc
"workbench.editor.highlightModifiedTabs": true
```

Modified tabs get a coloured border along the top, not just the small dot
that replaces the close button. A config edited but never saved on a remote
host is easy to leave behind when you close the laptop. Hot exit (`files.hotExit`, on by
default) keeps the unsaved text in VS Code, but the service is still running the old file.

### Terminal tabs that show where you are

```jsonc
"terminal.integrated.tabs.title": "${process}${separator}${sequence}",
"terminal.integrated.tabs.description": "${cwd}"
```

`${sequence}` is the title the shell or program sets (often `user@host:dir`
from your prompt). `${cwd}` is the current directory, which shell integration
reports. The description appears beside the title in the terminal tabs list
when there is room, and in the tab's hover.

### Smaller ones worth having

```jsonc
"diffEditor.experimental.showMoves": true,       // show a moved block as a move, not delete + add
"editor.cursorSurroundingLines": 5,              // keep 5 lines visible above/below the cursor
"workbench.editor.limit.enabled": true,          // cap open tabs; the least recently used tab closes
"workbench.editor.limit.value": 12,
"window.autoDetectColorScheme": true,            // follow the OS light/dark setting...
"workbench.preferredDarkColorTheme": "Default Dark Modern",
"workbench.preferredLightColorTheme": "Default Light Modern",
"terminal.integrated.suggest.enabled": true,     // completion suggestions in the terminal (commands, paths, flags)
"editor.unicodeHighlight.allowedCharacters": {   // characters you use on purpose: don't flag them (§4)
    "—": true,
    "→": true
}
```

- **`diffEditor.experimental.showMoves`**: when you reorder sections of a
  config (moving a `Match` block to the end of `sshd_config`, for example),
  the diff shows the block once, with a line linking its old and new
  positions.
- **`workbench.editor.limit.*`**: unsaved tabs are never closed by the limit,
  so this only tidies up tabs you finished with.
- **`terminal.integrated.suggest.enabled`**: suggestions come from shell
  integration and work in bash, zsh, fish, and PowerShell. It is a
  workspace-restricted setting, so it applies only in trusted workspaces.
- **`editor.unicodeHighlight.allowedCharacters`**: keep the list short. Each
  character you add is no longer flagged anywhere, including in configs where
  it would be a mistake.

______________________________________________________________________

## 19. Verification Checklist

Run through this after deploying `settings.json` on a new machine, or after a
large change to it.

- [ ] `code --version` reports 1.140.0 or later, and **Preferences: Open User
  Settings (JSON)** shows no errors in the Problems panel (`Ctrl+Shift+M`).
- [ ] A new untitled file shows `LF` and `UTF-8` in the status bar, on Windows
  too ([§3](#3-line-endings-lf-everywhere), [§4](#4-encoding-and-whitespace-hygiene)).
- [ ] `git config --show-origin --get-all core.autocrlf` returns `input`
  ([§3](#git-configuration)).
- [ ] Saving a file adds exactly one final newline and strips trailing spaces,
  except in Markdown.
- [ ] A pasted non-breaking space or smart quote in a `.sh` or `.yml` file is
  boxed by Unicode highlighting ([§4](#make-invisible-characters-visible)).
- [ ] On Linux, `fc-match "JetBrains Mono"` returns `JetBrainsMono-Regular.ttf`,
  and the editor shows a slashed zero ([§5](#configure-the-editor)).
- [ ] `!=` and `->` render as ligatures in a Markdown or JSON file, but **not**
  in a shell script or the integrated terminal ([§6](#6-ligatures-and-opentype-features)).
  The shell-script exception comes from the `[shellscript]` block in the
  full `settings.json`; the Appendix A baseline keeps editor ligatures on
  everywhere.
- [ ] A two-line paste into the integrated terminal triggers the confirmation
  prompt, and right-click opens a menu instead of pasting
  ([§8](#behaviour)).
- [ ] `Ctrl+P` and `Ctrl+K` in the terminal reach bash instead of opening Quick
  Open or starting a chord ([§8](#keys-that-the-terminal-should-keep); full
  `settings.json` only).
- [ ] A Remote - SSH window shows the host name in its title bar, and the
  login terminal appears while it connects ([§9](#9-remote---ssh-settings-beyond-the-basics)).
- [ ] A production `.code-workspace` opens with a red title bar and status bar
  and a `PROD` title ([§16](#colour-code-production-windows)).
- [ ] **Help → Check for Updates** is the only way an update starts, and the
  Extensions view does not auto-update anything ([§11](#updates)).
- [ ] No chat panel or Copilot entry point appears, unless you removed
  `chat.disableAIFeatures` on purpose ([§11](#ai-features)).
- [ ] A copy of `sshd_config.rpmnew` (or `.dpkg-dist`) nests under
  `sshd_config` in the Explorer, and dragging a folder in the Explorer does
  nothing ([§18](#18-power-user-settings)).
- [ ] A command that exits non-zero in the terminal plays the failure sound.
- [ ] The annotated `settings.json` is committed to your dotfiles repository
  and the live file is a copy of it or a symlink to it ([§14](#keeping-config-in-git-instead)).

______________________________________________________________________

## Appendix A: Complete baseline `settings.json`

A complete user `settings.json` using the recommendations above. Paste it into
**Preferences: Open User Settings (JSON)**, then remove what you don't want.
Values that match the 1.140.0 defaults are included where stating them makes
the intent clear. They are labelled `(default)`.

This is the baseline. The file `settings.json` next to this guide is the full
configuration: everything below plus the extras from the numbered sections
(terminal profiles and key handoff, Remote - SSH tuning, read-only locks,
Ansible tab labels, Settings Sync exclusions, and the rest of §18), with
deployment notes in its header.

```jsonc
{
    // ───────────────────────── Settings editor ─────────────────────────
    "workbench.settings.editor": "json",

    // ───────────────────────── Line endings (§3) ─────────────────────────
    "files.eol": "\n",                         // new files: LF on every OS
    "[bat]": { "files.eol": "\r\n" },          // cmd.exe needs CRLF

    // ───────────────────────── Encoding & whitespace (§4) ─────────────────
    "files.encoding": "utf8",                  // (default) never utf8bom on Linux
    "files.autoGuessEncoding": false,          // (default)
    "files.insertFinalNewline": true,
    "files.trimFinalNewlines": true,
    "files.trimTrailingWhitespace": true,
    "editor.renderWhitespace": "boundary",
    "editor.renderControlCharacters": true,    // (default)
    "editor.unicodeHighlight.invisibleCharacters": true,   // (default)
    "editor.unicodeHighlight.ambiguousCharacters": true,   // (default)

    // ───────────────────────── Fonts (§5) ─────────────────────────
    "editor.fontFamily": "'JetBrains Mono', 'Cascadia Mono', Consolas, 'DejaVu Sans Mono', monospace",
    "editor.fontSize": 14,
    "editor.lineHeight": 1.5,
    "editor.mouseWheelZoom": true,
    "terminal.integrated.fontFamily": "'JetBrains Mono', monospace",
    "terminal.integrated.fontSize": 14,
    "debug.console.fontFamily": "'JetBrains Mono', monospace",
    "scm.inputFontFamily": "editor",

    // ───────────────────────── Ligatures (§6) ─────────────────────────
    "editor.fontLigatures": "'calt', 'zero'",  // ligatures + slashed zero
    "terminal.integrated.fontLigatures.enabled": false,    // exact characters in the shell

    // ───────────────────────── Editor (§7) ─────────────────────────
    "editor.insertSpaces": true,
    "editor.tabSize": 4,
    "editor.detectIndentation": true,          // (default)
    "editor.rulers": [80, 120],
    "editor.wordWrap": "off",
    "editor.minimap.enabled": false,
    "editor.stickyScroll.enabled": true,
    "editor.guides.bracketPairs": "active",
    "editor.cursorBlinking": "solid",
    "editor.smoothScrolling": false,
    "editor.formatOnSave": false,              // enable per workspace/language
    "editor.copyWithSyntaxHighlighting": false,
    "editor.linkedEditing": true,
    "files.autoSave": "off",                   // never auto-save live configs
    "workbench.tree.indent": 16,
    "workbench.tree.renderIndentGuides": "always",
    "files.associations": {
        "*.service": "ini",
        "*.timer": "ini",
        "*.socket": "ini",
        "*.repo": "ini",
        "Containerfile": "dockerfile"
    },

    // ───────────────────────── Per-language (§3, §4, §6, §7) ─────────────
    "[markdown]": {
        "files.trimTrailingWhitespace": false,
        "editor.wordWrap": "on"                // (default via built-in markdown)
    },
    "[yaml]": {
        "editor.tabSize": 2,                   // (default)
        "editor.unicodeHighlight.nonBasicASCII": true
    },
    "[json]":  { "editor.tabSize": 2 },
    "[jsonc]": { "editor.tabSize": 2 },
    "[shellscript]": {
        "editor.unicodeHighlight.nonBasicASCII": true
    },
    "[powershell]": {
        "editor.unicodeHighlight.nonBasicASCII": true
    },

    // ───────────────────────── Terminal (§8) ─────────────────────────
    "terminal.integrated.defaultProfile.linux": "bash",
    "terminal.integrated.defaultProfile.windows": "PowerShell",
    "terminal.integrated.scrollback": 10000,
    "terminal.integrated.enableMultiLinePasteWarning": "always",
    "terminal.integrated.copyOnSelection": false,
    "terminal.integrated.rightClickBehavior": "default",
    "terminal.integrated.cursorStyle": "block",
    "terminal.integrated.confirmOnKill": "always",
    "terminal.integrated.stickyScroll.enabled": true,

    // ───────────────────────── Remote - SSH (§9; basics in SSH guide §11/§33) ──
    "remote.SSH.connectTimeout": 30,
    "remote.SSH.showLoginTerminal": true,
    "remote.SSH.useLocalServer": false,
    "remote.SSH.lockfilesInTmp": true,

    "remote.SSH.defaultExtensions": [
        "timonwong.shellcheck",
        "redhat.vscode-yaml",
        "editorconfig.editorconfig"
    ],
    // Windows only:
    // "remote.SSH.path": "C:\\Windows\\System32\\OpenSSH\\ssh.exe",

    // ───────────────────────── Window (§9, §16) ─────────────────────────
    "window.title": "${remoteName}${separator}${rootName}${separator}${activeEditorShort}${dirty}",
    "window.restoreWindows": "all",

    // ───────────────────────── Git & diff (§10) ─────────────────────────
    "git.autofetch": false,
    "git.enableSmartCommit": false,
    "git.openRepositoryInParentFolders": "prompt",
    "git.blame.statusBarItem.enabled": true,
    "diffEditor.ignoreTrimWhitespace": false,
    "diffEditor.hideUnchangedRegions.enabled": true,

    // ───────────────────────── Privacy & updates (§11) ─────────────────
    "telemetry.telemetryLevel": "off",
    "telemetry.feedback.enabled": false,
    "workbench.enableExperiments": false,
    "workbench.settings.enableNaturalLanguageSearch": false,
    "update.mode": "manual",
    "extensions.autoUpdate": "off",
    "chat.disableAIFeatures": true,            // remove if you use Copilot/chat
    "security.workspace.trust.enabled": true,  // (default)

    // ───────────────────────── Misc ─────────────────────────
    "workbench.startupEditor": "none",
    "explorer.confirmDelete": true,            // (default)
    "explorer.compactFolders": false,          // show /etc/nginx/conf.d as three levels

    // ───────────────────────── Power-user safety (§18) ─────────────────
    "explorer.fileNesting.enabled": true,
    "explorer.fileNesting.expand": false,
    "explorer.fileNesting.patterns": {
        "*": "${capture}.rpmnew, ${capture}.rpmsave, ${capture}.dpkg-dist, ${capture}.dpkg-old, ${capture}.dpkg-new, ${capture}.ucf-dist, ${capture}.bak, ${capture}.orig, ${capture}~"
    },
    "accessibility.signals.terminalCommandFailed": { "sound": "on" },
    "accessibility.signals.taskCompleted": { "sound": "on" },
    "accessibility.signals.taskFailed": { "sound": "on" },
    "explorer.enableDragAndDrop": false,
    "editor.dragAndDrop": false,
    "workbench.editor.highlightModifiedTabs": true
}
```

______________________________________________________________________

## Appendix B: `.editorconfig` and `.gitattributes` templates

Commit both at the root of every repository you control. Together with
`files.eol` they make "always LF" hold for every editor and every clone.

### `.editorconfig`

Requires the `editorconfig.editorconfig` extension in VS Code. Neovim (0.9
and later) and JetBrains IDEs support it natively. Vim 9 ships it as an
optional package: add `packadd! editorconfig` to `~/.vimrc`.

The VS Code extension can turn trimming on but not off:
`trim_trailing_whitespace = false` does **not** override
`files.trimTrailingWhitespace: true`. Keep the `[markdown]` override from §4.
The extension applies `end_of_line`, `insert_final_newline`, and
`trim_trailing_whitespace` when you save.

```ini
# https://editorconfig.org
root = true

[*]
charset = utf-8
end_of_line = lf
insert_final_newline = true
trim_trailing_whitespace = true
indent_style = space
indent_size = 4

[*.{yml,yaml,json,jsonc,toml}]
indent_size = 2

[*.md]
trim_trailing_whitespace = false

[{Makefile,*.mk}]
indent_style = tab

[*.go]
indent_style = tab

[*.{bat,cmd}]
end_of_line = crlf
```

### `.gitattributes`

```gitattributes
# Normalize all text to LF in the repo and in working trees, on every OS
* text=auto eol=lf

# Windows batch files must be CRLF
*.bat  text eol=crlf
*.cmd  text eol=crlf

# Authenticode-signed scripts: store byte-for-byte, never convert
# (uncomment and adjust the path if you keep signed scripts here)
# signed/*.ps1  -text

# regedit exports are UTF-16LE with CRLF: keep them byte-for-byte
*.reg  -text diff

# Binary files: no conversion, no textual diff
*.png  binary
*.jpg  binary
*.gif  binary
*.ico  binary
*.zip  binary
*.gz   binary
*.tgz  binary
*.pdf  binary
*.vsix binary
*.der  binary
*.p12  binary
*.pfx  binary
```

After adding `.gitattributes` to an existing repository, run
`git add --renormalize .` and commit (§3).

______________________________________________________________________

## Appendix C: File locations

| Item | Linux | Windows |
| -- | -- | -- |
| User settings | `~/.config/Code/User/settings.json` | `%APPDATA%\Code\User\settings.json` |
| Keybindings | `~/.config/Code/User/keybindings.json` | `%APPDATA%\Code\User\keybindings.json` |
| User snippets | `~/.config/Code/User/snippets/` | `%APPDATA%\Code\User\snippets\` |
| Profiles | `~/.config/Code/User/profiles/<id>/` | `%APPDATA%\Code\User\profiles\<id>\` |
| Extensions | `~/.vscode/extensions/` | `%USERPROFILE%\.vscode\extensions\` |
| Logs | `~/.config/Code/logs/` | `%APPDATA%\Code\logs\` |
| Workspace settings | `<folder>/.vscode/settings.json` | same |
| Workspace tasks | `<folder>/.vscode/tasks.json` | same |
| Recommended extensions | `<folder>/.vscode/extensions.json` | same |
| Remote server (on host) | `~/.vscode-server/` | `%USERPROFILE%\.vscode-server\` (Windows SSH hosts) |
| Remote Machine settings | `~/.vscode-server/data/Machine/settings.json` | same, under the remote user's profile |
| Runtime arguments (`argv.json`) | `~/.vscode/argv.json` | `%USERPROFILE%\.vscode\argv.json` |
| Enforced policies | `/etc/vscode/policy.json` | Group Policy (registry) |
| SSH config read by Remote - SSH | `~/.ssh/config` | `%USERPROFILE%\.ssh\config` |
| Installation (package) | `/usr/share/code/` | `C:\Program Files\Microsoft VS Code\` (machine) or `%LOCALAPPDATA%\Programs\Microsoft VS Code\` (user) |

Insiders builds use `Code - Insiders` and `.vscode-insiders` in place of `Code`
and `.vscode`. They are separate, so the two can run side by side.

______________________________________________________________________

## Appendix D: Command and shortcut quick reference

Shortcuts are the defaults on both Linux and Windows unless a row gives one
for each. Every command is also available
through `Ctrl+Shift+P` (or `F1`) by name.

| Shortcut | Command / action |
| -- | -- |
| `Ctrl+Shift+P` / `F1` | Command Palette |
| `Ctrl+P` | Quick Open file (type `:` for line, `@` for symbol) |
| `Ctrl+,` | Settings |
| `Ctrl+K Ctrl+S` | Keyboard shortcuts |
| `` Ctrl+` `` | Toggle integrated terminal |
| `` Ctrl+Shift+` `` | New terminal |
| `Ctrl+Shift+E` / `F` / `G` / `X` | Explorer / Search / Source Control / Extensions |
| `Ctrl+Shift+U` (Windows) / `Ctrl+K Ctrl+H` (Linux) | Output panel (extension and Remote - SSH logs) |
| `Ctrl+Shift+M` | Problems panel |
| `Ctrl+K M` | Change language mode |
| `Ctrl+K Ctrl+X` | Trim trailing whitespace |
| `Ctrl+K S` (Linux) / `Ctrl+K Ctrl+Shift+S` (Windows) | Save without formatting |
| `Ctrl+Shift+I` (Linux) / `Shift+Alt+F` (Windows) | Format document |
| `Ctrl+/` | Toggle line comment |
| `Alt+Z` | Toggle word wrap |
| `Alt+Up` / `Alt+Down` | Move line up/down |
| `Shift+Alt+Up/Down` (Windows) / `Ctrl+Shift+Alt+Up/Down` (Linux) | Copy line up/down |
| `Ctrl+Shift+K` | Delete line |
| `Ctrl+D` / `Ctrl+Shift+L` | Select next occurrence / all occurrences |
| `Ctrl+Alt+Up/Down` (Windows) / `Shift+Alt+Up/Down` (Linux) | Add cursor above/below |
| `Ctrl+G` | Go to line |
| `Ctrl+Shift+O` | Go to symbol in file |
| `Ctrl+K V` | Markdown preview to the side |
| `Ctrl+K Ctrl+0` / `Ctrl+K Ctrl+J` | Fold all / unfold all |
| `Ctrl+Alt+R` (terminal) | Run recent command (shell integration) |
| `Ctrl+Up` / `Ctrl+Down` (terminal) | Jump to previous/next command |

| Command Palette entry | Use |
| -- | -- |
| **Change End of Line Sequence** | Convert the current file between LF and CRLF (§3) |
| **Change File Encoding** | Reopen or save with a different encoding (§4) |
| **Preferences: Open User Settings (JSON)** | Edit user `settings.json` directly |
| **Preferences: Open Remote Settings (JSON)** | Edit per-host settings while connected (§9) |
| **Preferences: Open Workspace Settings (JSON)** | Edit `.vscode/settings.json` |
| **Remote-SSH: Connect to Host…** | Connect (companion SSH guide §11) |
| **Remote-SSH: Show Log** | Diagnose connection problems |
| **Remote-SSH: Uninstall VS Code Server from Host** | Clean up old servers on a host (§9) |
| **Profiles: New Profile** / **Export Profile** | Manage profiles (§14) |
| **Help: Start Extension Bisect** | Find a misbehaving extension (§17) |
| **Developer: Reload Window** | Restart the window without closing it |
| **Developer: Open Process Explorer** | CPU and memory per process (§17) |
| **File: Compare Active File with Clipboard** | Diff the file against a pasted snippet (§16) |
| **Terminal: Run Selected Text in Active Terminal** | Run commands from a runbook (§15) |
