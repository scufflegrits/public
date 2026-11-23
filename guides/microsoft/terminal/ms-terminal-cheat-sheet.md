---
Title: Windows Terminal Cheat Sheet — settings.json Edition
Version: r1.0.1
Updated: 2026-11-22
Reference build: Windows Terminal 1.25 (verified on 1.25.3131.0)
Scope: Key bindings, mouse, menus, and commands for the annotated settings.json in this folder
Companion: ms-terminal-json-settings
Topics: Windows Terminal, keyboard shortcuts, key bindings, copy and paste, panes, tabs, broadcast input, read-only mode, snippets, quake mode, wt.exe, SSH profiles
---

# Windows Terminal Cheat Sheet — settings.json Edition

> What you can press, click, and type with the annotated
> [`settings.json`](settings.json) in this folder deployed as your live
> Terminal settings. Built-in chords come from Terminal 1.25's `defaults.json`.
> The custom ones come from `settings.json`, and are marked ★ in the tables.
> For why each setting is chosen, see the
> [Windows Terminal settings guide](ms-terminal-json-settings.md).

## Contents

- [Copy and paste](#copy-and-paste)
- [Tabs](#tabs)
- [Panes](#panes)
- [Hosts and profiles](#hosts-and-profiles)
- [Command Palette, snippets, and layouts](#command-palette-snippets-and-layouts)
- [Safety tools](#safety-tools)
- [Scrolling, search, and view](#scrolling-search-and-view)
- [Quake window](#quake-window)
- [When a session ends](#when-a-session-ends)
- [Command line: wt.exe](#command-line-wtexe)
- [Settings files](#settings-files)
- [Optional bindings in settings.json](#optional-bindings-in-settingsjson)

______________________________________________________________________

## Copy and paste

Highlighting copies (`copyOnSelect: true`), and `Ctrl+C` always interrupts.

| Do this | Result |
| -- | -- |
| Highlight with the mouse | Copies the selection immediately, as plain text |
| Double-click | Selects a word. An IP address or FQDN counts as one word |
| Triple-click | Selects the line |
| `Shift`+click | Extends the selection |
| `Alt`+drag | Block (rectangle) selection, with trailing spaces trimmed |
| `Ctrl+Shift+C` / `Ctrl+Insert` / `Enter` | Copy the selection |
| `Ctrl+Shift+A` | Select all |
| `Ctrl+Shift+M` | Mark mode: select with the keyboard |
| `Ctrl+Shift+V` / `Shift+Insert` | Paste. Multi-line pastes always ask first, and pastes over 5 KiB warn |
| Right-click | Context menu (Copy, Paste, …). It does not paste immediately |
| Palette → **Copy as single line** ★ | Copy a wrapped command without its line breaks |
| `Ctrl+C` | **Always interrupts** the running command, even with text selected |
| `Ctrl+V` | Not Terminal's paste: a literal `^V` in bash, PSReadLine's own paste in PowerShell (no warning) |

## Tabs

New tabs open at the **end** of the tab row (`newTabPosition: afterLastTab`).

| Keys | Action |
| -- | -- |
| `Ctrl+Shift+T` | New tab, default profile (PowerShell) |
| `Ctrl+Shift+Space` | Open the new-tab menu (folders: Lab, Proxmox, Production, Network, …) |
| `Ctrl+Shift+1` … `9` | New tab with the Nth profile |
| `Ctrl+Shift+N` | New window |
| `Ctrl+Shift+D` | Duplicate the current tab |
| `Ctrl+Tab` / `Ctrl+Shift+Tab` | Next / previous tab |
| `Ctrl+Alt+1` … `8` | Go to tab 1–8 |
| `Ctrl+Alt+9` | Go to the last tab |
| `Ctrl+Shift+R` ★ | Rename the tab inline (for example `CHG0012345`) |
| `Ctrl+Shift+W` | Close the pane, and the tab if it was the last pane |
| Middle-click a tab | Close it |
| `Ctrl+Alt+Shift+T` ★ | **Reopen the last closed tab or pane**. Same profile and layout; old output is not restored |

The **X** on a tab appears only when you hover over it (`showCloseButton: "hover"`). Closing a window with several tabs asks first.

## Panes

| Keys | Action |
| -- | -- |
| `Alt+Shift+plus` | Split right (duplicate the current profile) |
| `Alt+Shift+-` | Split down (duplicate the current profile) |
| `Alt+←` `→` `↑` `↓` | Move focus between panes |
| `Ctrl+Alt+←` | Focus the previously used pane |
| `Alt+Shift+←` `→` `↑` `↓` | Resize the pane |
| `Ctrl+Shift+Z` ★ | Zoom: temporarily maximize the pane, then restore it |
| `Ctrl+Shift+W` | Close the pane |

`Alt+Shift+D` (split in the "best" direction) is **not** bound. It exists only
in the `settings.json` a fresh install generates.

## Hosts and profiles

| Keys | Opens | Tab |
| -- | -- | -- |
| `Ctrl+Alt+Shift+1` ★ | `pve01` | green, "lab pve01" |
| `Ctrl+Alt+Shift+2` ★ | `pve02` | green |
| `Ctrl+Alt+Shift+3` ★ | `pve03` | green |
| `Ctrl+Alt+Shift+4` ★ | `pbs01` | green |
| `Ctrl+Alt+Shift+5` ★ | `core-sw01` | blue; ligatures off |
| New-tab menu → **Lab** → `devdeb` | Debian 13 at 192.168.0.31, key `%USERPROFILE%\.ssh\id_ed25519`, keepalives every 30 s | green, "lab devdeb" |

**Tab colors:**

- **Green:** lab hosts.
- **Red tab, dark-red background, "PROD" title, ligatures off:** production
  (`web01-prod`, `bastion-prod`).
- **Blue:** network devices and the COM3 serial console.
- **Orange:** `PowerShell (Admin)`, which opens in a separate elevated window.

Profiles with no key (such as `devdeb`, the production hosts, and the serial
console) open from the new-tab menu, or from the Command Palette's **New tab**
list.

## Command Palette, snippets, and layouts

| Keys | Action |
| -- | -- |
| `Ctrl+Shift+P` | Command Palette. Type to filter |
| `Ctrl+Alt+Shift+S` ★ | **Snippets pane**: the `snip:` commands as a clickable list |
| `Ctrl+Shift+.` | Suggestions (shell history and snippets) |

Snippets ★ are in the palette as `snip:` and in the snippets pane. They type
into the **active pane**, so check the tab color first:

| Snippet | Types | Runs |
| -- | -- | -- |
| failed systemd units | `systemctl --failed --no-pager` | yes |
| journal errors this boot | `journalctl -b -p err --no-pager \| tail -n 50` | yes |
| disk + inode usage | `df -hT -x tmpfs -x devtmpfs; df -i -x tmpfs -x devtmpfs` | yes |
| PVE cluster + storage status | `pvecm status; pvesm status` | yes |
| start session log (script) | `script -f ~/chg-<date>-<time>.log` | yes |
| become root (no Enter) | `sudo -i` | **no**, press `Enter` yourself |

**Layout: PVE cluster 2x2** ★ (in the palette, and in the new-tab menu under
**Proxmox**) opens a tab split into `pve01`, `pve02`, `pve03`, and `pbs01`.

## Safety tools

| Keys | Action | Use it for |
| -- | -- | -- |
| `Ctrl+Shift+B` ★ | **Broadcast input** on or off: typing goes to every pane in the tab | Read-only checks on several nodes at once. Turn it off before anything host-specific |
| `Ctrl+Alt+Shift+R` ★ | **Read-only mode** on or off for the focused pane. Typing shows "read only mode is enabled" | Watch-only panes (`journalctl -f`, `tail -f`), and keeping a pane out of a broadcast |
| `Ctrl+Shift+E` ★ | **Export the scrollback** to a file (Save dialog) | Evidence for a change ticket. Limited to the last 20,000 lines |
| `Ctrl+Shift+K` | Clear the scrollback | Starting a clean capture |
| `Ctrl+Alt+Shift+T` ★ | Reopen the last closed tab or pane | Undoing an accidental close |
| `Ctrl+Alt+Shift+P` ★ | **Mark tab as PROD**: red tab and Prod Warning colors on the focused pane, then type a title | A production session opened from a local tab or a bastion |
| `Ctrl+Alt+Shift+U` ★ | Unmark: normal tab color and colors; drops the typed title (the tab shows the shell's or profile's title again) | Leaving production in that tab |

## Scrolling, search, and view

| Keys | Action |
| -- | -- |
| `Ctrl+Shift+↑` / `↓` | Scroll one line |
| `Ctrl+Shift+PgUp` / `PgDn` | Scroll one page |
| `Ctrl+Shift+Home` / `End` | Top / bottom of the scrollback |
| `Ctrl+Shift+F` | Find in the scrollback |
| `Ctrl+=` / `Ctrl+-` / `Ctrl+0` | Font size up / down / reset |
| `F11` or `Alt+Enter` | Full screen |
| `Alt+Space` | Window system menu |

## Quake window

| Keys | Action |
| -- | -- |
| `` Win+` `` ★ | Drop down the quake window or hide it. It follows the mouse to the active monitor and moves to the current desktop, with a 150 ms animation |

The quake window opens the default profile. To make it open the fast,
profile-less shell instead, start it once with:

```powershell
wt.exe -w _quake new-tab -p "PowerShell (quick)"
```

To keep the hotkey working after sign-in, turn on Settings → Startup →
**Launch on machine startup**.

## When a session ends

SSH tabs keep their output after the connection ends (`closeOnExit: "never"`):

| Message | Meaning |
| -- | -- |
| `[process exited with code 0 …]` | Normal logout |
| `[process exited with code 255 …]` | ssh could not connect or log in; read the lines above it |

| Keys | Action |
| -- | -- |
| `Enter` | Reconnect: run the profile's command again in the same pane |
| `Ctrl+D` | Close the pane |

The "Termination behavior can be configured…" banner is a one-time hint. Click
**Don't show again** to dismiss it for good.

## Command line: wt.exe

In PowerShell, write each `;` separator between `wt` subcommands as `` `; ``.
In `cmd.exe` or a shortcut, use a plain `;`.

```powershell
# New tab in the current window with a host profile
wt.exe -w 0 new-tab -p "devdeb"

# Proxmox 2x2 in a new tab
wt.exe -w 0 new-tab -p "pve01" --title "PVE" `; split-pane -V -p "pve02" `; move-focus left `; split-pane -H -p "pve03" `; move-focus right `; split-pane -H -p "pbs01"

# A one-off tab with its own color and title
wt.exe -w 0 new-tab -p "PowerShell" --title "scratch" --tabColor "#5A5D63"
```

| Option | Meaning |
| -- | -- |
| `-w 0` / `-w <name>` | Most recent window / a named window (`_quake` is the quake window) |
| `new-tab -p "<profile>"` | Open a profile. Add `--title`, `--tabColor`, `--suppressApplicationTitle` |
| `split-pane -V` / `-H` | Split side by side / stacked. `-s 0.3` sets the new pane's size |
| `move-focus <dir>` | `left`, `right`, `up`, `down`, `first`, `previous` |
| `focus-tab -t <n>` | Select a tab by index |

## Settings files

| Keys | Opens |
| -- | -- |
| `Ctrl+,` | Settings UI |
| `Ctrl+Shift+,` | `settings.json` (the live copy, which Terminal rewrites and strips of comments) |
| `Ctrl+Alt+,` | `defaults.json`, read-only: the authoritative list of built-in chords |

Edit the annotated master [`settings.json`](settings.json) in git, then copy it
into place:
`%LOCALAPPDATA%\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json`.

## Optional bindings in settings.json

These are commented out in `settings.json`. To turn one on, uncomment its line;
nothing else needs to change.

| Line | Effect |
| -- | -- |
| `{ "id": "Terminal.CopyToClipboard", "keys": "ctrl+c" },` | `Ctrl+C` copies when text is selected, and interrupts otherwise |
| `{ "id": "Terminal.PasteFromClipboard", "keys": "ctrl+v" },` | `Ctrl+V` pastes through Terminal, with the paste warnings |
| `{ "id": null, "keys": "ctrl+shift+w" },` | Frees `Ctrl+Shift+W` for remote `tmux` or `vim`. Close panes from the tab menu instead |
