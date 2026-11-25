---
Title: Changelog — Windows Terminal settings.json guide
Updated: 2026-11-22
Companion: ms-terminal-json-settings
---

# Changelog — Windows Terminal settings.json guide

Changes to `ms-terminal-json-settings.md` and the annotated `settings.json`
beside it, newest first. Each entry says what changed, why, and how it was
checked. Sources are collected in [References](#references); `[Rn]` tags in
the entries point to them.

## Unreleased

- Keep ordinary minimized Terminal windows on the taskbar so the taskbar
  button restores the existing tabs. Set `minimizeToNotificationArea` to
  `false` in `settings.json` and the guide.

## r1.0.7 — 2026-11-22

### Added

- §7: a new subsection, "Mark a tab as production after the fact". Two
  `multipleActions` commands in `settings.json` and Appendix A close the gap
  the defense-in-depth note describes: a production session that didn't start
  from a PROD profile.
  - `ctrl+alt+shift+p`, **Mark tab as PROD**: `setTabColor` `#B00020`,
    `setColorScheme` "Prod Warning" on the focused pane, then `openTabRenamer`.
  - `ctrl+alt+shift+u`, **Unmark PROD tab**: `setTabColor` with no color,
    `setColorScheme` "Darcula Admin", and `renameTab` with no title.
- §13 table and the cheat sheet list both chords.
- Evidence:
  - `multipleActions`, `setTabColor`, and `setColorScheme` exist in Terminal
    1.25.3131.0's settings model. Neither chord clashes with a
    `defaults.json` or user binding. Both colour schemes the actions name
    exist. `settings.json` parses as strict JSON (as shipped and with its
    optional lines uncommented), and Appendix A parses. [R2] [R4]
  - Tested live on the Windows 11 VM with the file deployed. The user pressed
    the keys in RDP. Each step was checked by capturing Terminal's window
    (`PrintWindow` with `PW_RENDERFULLCONTENT`) and reading the tab names
    through UI Automation:
    - **Mark:** the tab turned red, the pane background turned Prod Warning
      dark red, and the typed title (`prod`) appeared.
    - **Title test:** after `$Host.UI.RawUI.WindowTitle = "app-set-title"`,
      the tab still read `prod`, so the typed title survives a
      shell-set title.
    - **Unmark:** the tab colour and Darcula Admin background came back, and
      the tab showed the shell's title (`app-set-title`). Unmark drops the
      typed title rather than restoring an earlier one; §7 now says so.
  - Not tested: a multi-pane tab (the `setColorScheme` focused-pane caveat in
    §7 comes from the action's documented scope).

## r1.0.6 — 2026-11-22

### Added

- §13, Appendix A, and `settings.json`: key bindings for three built-in
  commands that have no default chord:
  - `ctrl+alt+shift+t`: `Terminal.RestoreLastClosed` reopens the last closed
    tab or pane, a safety net for an accidental close.
  - `ctrl+alt+shift+r`: `Terminal.ToggleReadOnlyMode` locks a watch-only pane
    and keeps it out of broadcast input.
  - `ctrl+alt+shift+s`: `Terminal.OpenSnippetsPane` lists the `sendInput`
    snippets as a clickable pane.
  - They're bound by built-in ID directly in `keybindings`, with no `actions`
    entry; §13 now explains that pattern.
  - Evidence: all three IDs are defined in Terminal 1.25.3131.0's
    `defaults.json` with no chord. None of the three chords clashes with a
    `defaults.json` binding or another user binding (checked
    programmatically; the only default replaced is the guide's existing,
    intentional quake binding on `win+sc(41)`). `settings.json` parses as
    strict JSON, both as shipped and with its optional lines uncommented, and
    Appendix A parses. [R4]
  - Verified in a running Terminal (1.25.3131.0 on the Windows 11 VM, with
    the updated `settings.json` deployed as the live file; keys pressed by
    the user in the RDP session):
    - `ctrl+alt+shift+s` opens the snippets pane, which lists the
      `sendInput` actions defined in `settings.json`; clicking one types it
      into the active pane.
    - `ctrl+alt+shift+r` locks the pane; typing into it shows an information
      notice, "read only mode is enabled". §13 now mentions the notice.
    - `ctrl+alt+shift+t` reopens a closed tab without its previous output, as
      §13 states.
    - No settings error banner when Terminal started with the file.
    - Not verified: reopening a closed SSH tab, because the `devdeb` key
      (`%USERPROFILE%\.ssh\id_ed25519`) isn't on the test VM.

## r1.0.5 — 2026-11-22

### Corrected

- **Appendix B said "`Ctrl+C` copies only when text is selected".** That
  holds only when `ctrl+c` is bound to `Terminal.CopyToClipboard`, and that
  binding comes from the `settings.json` a fresh install generates, not from
  the built-in `defaults.json`. The guide's own `settings.json` replaces the
  generated file, so with it `Ctrl+C` always interrupts and `Ctrl+V` goes to
  the shell. Appendix B now says so and links to §13.
  - Evidence: Terminal 1.25.3131.0's `defaults.json` binds copy to
    `ctrl+shift+c`, `ctrl+insert`, and `enter`, and paste to `ctrl+shift+v`
    and `shift+insert`, with no `ctrl+c` or `ctrl+v`. The VM's generated
    `settings.json` added `{"id": "Terminal.CopyToClipboard", "keys": "ctrl+c"}`
    and `{"id": "Terminal.PasteFromClipboard", "keys": "ctrl+v"}`. [R1] [R4]

### Added

- §13 Format: a note explaining the above, and that the guide's
  `settings.json` leaves both keys unbound on purpose.
- `settings.json`: a comment block explaining why `Ctrl+C`/`Ctrl+V` are
  unbound, plus commented-out bindings that restore Windows-style copy and
  paste. The optional lines (these two and the existing `ctrl+shift+w` unbind
  example) now sit before the last `keybindings` entry, each with its own
  trailing comma, so uncommenting is the only edit needed. Checked by parsing
  the file as strict JSON both as shipped and with all three lines uncommented.

## settings.json only — 2026-11-22 (guide text unchanged, still r1.0.4)

Changes to the annotated `settings.json`, made for the author's homelab use.
They depart from the guide's recommendations where noted.

- Added a **Lab** new-tab folder and a `devdeb` profile (Debian 13 at
  192.168.0.31) that uses `%USERPROFILE%\.ssh\id_ed25519`, styled like the
  other lab hosts (`a7ec3b4`). The key and address are on the command line, so
  no `~/.ssh/config` entry is needed; a comment shows the equivalent §9 alias
  block.
- `devdeb` sends SSH keepalives: `-o ServerAliveInterval=30 -o ServerAliveCountMax=4 -o TCPKeepAlive=yes`. These are the same interval and
  count as the guide's §9 `Host *` block. The comment explains that they keep
  idle NAT and firewall state alive and drop a dead link after about 2 minutes,
  but don't override a server-side `TMOUT` or sshd `ClientAlive*` limits. [R12]
- `copyOnSelect` is now `true`: highlighting copies immediately. **This
  departs from the guide's §6 recommendation (`false`)**, and a comment in the
  file says so. The paste guards (`warning.multiLinePaste: "always"`,
  `warning.largePaste`, `trimPaste`) are unchanged.
- `newTabPosition` is now `"afterLastTab"` (Terminal's default): new tabs open
  at the end of the tab row instead of next to the active tab. **This departs
  from the guide's §6 recommendation (`"afterCurrentTab"`)**, and a comment in
  the file says so.

## r1.0.4 — 2026-11-22

### Added

- §17 troubleshooting: a row for the "Termination behavior can be configured
  in advanced profile settings." info bar. It's a one-time hint about
  `closeOnExit`, not an error. Dismissing it with **Don't show again** is
  stored in `state.json` as `"dismissedMessages": ["closeOnExitInfo"]`, not in
  `settings.json`.
  - Evidence: the info-bar text and `CloseOnExitInfoBar` are in
    `TerminalApp.dll`; `dismissedMessages`, `closeOnExitInfo`,
    `keyboardServiceWarning`, and `setAsDefault` are in
    `Microsoft.Terminal.Settings.Model.dll` (1.25.3131.0). The VM's
    `state.json` had no `dismissedMessages` entry while the banner was still
    showing. The user reported the banner in a PowerShell tab whose session
    was unaffected. [R2] [R11]

## r1.0.3 — 2026-11-22

Verified against a Windows 11 test VM: Windows 11 24H2 (build 26100.9974),
Windows Terminal **1.25.3131.0** (Store package), PowerShell 7.7.0 and 5.1,
JetBrains Mono v2.304, Nerd Fonts v3.5.1.

### Corrected

- **`startOnUserLogin` is not a `settings.json` key in 1.25.** Removed it from
  §6, §12, the troubleshooting table, Appendix A, and `settings.json`. Start at
  sign-in is now described as Settings → Startup → **Launch on machine
  startup**, the package's Windows startup task `StartTerminalOnLoginTask`.
  - Evidence: Terminal dropped the key when it rewrote the deployed file. The
    key name is absent from `Microsoft.Terminal.Settings.Model.dll`, while the
    package manifest declares the startup task and `resources.pri` holds the
    UI label. [R1] [R2] [R3]
- **`experimental.rightClickContextMenu` is now `rightClickContextMenu`.**
  Updated §6, Appendix A, and `settings.json`, and noted that 1.25 migrates
  the old name.
  - Evidence: Terminal rewrote the key to `rightClickContextMenu` on load. [R1]
- **Appendix B:** `Ctrl+Alt+9` switches to the *last* tab, not tab 9
  (`Terminal.SwitchToLastTab`). The table now says `Ctrl+Alt+1` … `8` for tabs
  1–8 and `Ctrl+Alt+9` for the last tab, and `settings.json` notes it. [R4]
- **§4 font check:** the System.Drawing command reports GDI legacy names: each
  weight as its own family (`JetBrains Mono Medium`), and the Nerd Fonts under
  short names (`JetBrainsMono NF`, `NFM`, `NFP`, `JetBrainsMonoNL NF`), not the
  names in the variant table. Added an explanation of what the output means
  and which name to put in `font.face`.
  - Evidence: ran the guide's command in PowerShell 7.7 and 5.1. Read name IDs
    1 and 16 from the font files. Queried DirectWrite (Terminal's font API):
    its family list shows the full names (`JetBrainsMono Nerd Font`, …), and
    `FindFamilyName` resolves both the full and the short names. [R5] [R6]

### Added

- §4 variant table: `JetBrainsMono Nerd Font Propo` row. The Nerd Fonts names
  are now stated as those of v3.5.1, with their short legacy names.
- §4 install: the Scoop bucket also has `JetBrainsMono-NF-Propo`; the Nerd Font
  zip holds every variant and weight. [R7] [R6]
- §2 rewrite triggers: `newTabMenu` profile names are stored as GUIDs in the
  live file; a legacy `keys`-in-`actions` binding for a built-in command is
  re-pointed at the built-in action ID (`Terminal.TogglePaneZoom`). [R1]
- §11 Option A: an "observed on 1.25.3131.0" note. With `Windows.Terminal.SSH`
  enabled and the §9 `~/.ssh/config`, Terminal generated no `SSH - …`
  profiles, and `state.json` recorded `"sshFolderGenerated": false`. The
  guide's Option A description is kept, with a prompt to check your build.
- §11 Option B: Terminal records fragment profiles with `"source"` set to the
  fragment folder name (`ssh-hosts`) and adds stub entries for them. [R1]
- Front matter: `Reference build` names the verified build; version r1.0.3.

### Verified unchanged

- `defaults.json` key chords match Appendix B (apart from the `Ctrl+Alt+9`
  fix), including `win+sc(41)` for quake mode and `alt+shift+d` in the
  generated user defaults. Default `historySize` is 9001. [R4]
- Key and enum names used by the guide exist in the 1.25 settings model:
  `persistedLayout`, `persistedLayoutAndContent`, `persistedWindowLayout`,
  `warning.multiLinePaste`, `warning.largePaste`,
  `warning.confirmCloseAllTabs`, `compatibility.allowHeadless`,
  `autoHideWindow`, `builtinGlyphs`, `colorGlyphs`, `cellHeight`,
  `remainingProfiles`, `matchProfiles`, `allowEmpty`, `dropdownDuration`,
  `toggleVisibility`, `toMouse`, `onCurrent`, `exportBuffer`,
  `toggleBroadcastInput`, `togglePaneZoom`, `openTabRenamer`, `singleLine`,
  `Windows.Terminal.SSH`. `warning.confirmOnClose` is absent from 1.25, as the
  guide says (1.26 preview). [R2] [R8]
- The published schema at `aka.ms/terminal-profiles-schema` still types
  `warning.multiLinePaste` as a boolean; the `main` branch schema has the
  `automatic`/`always`/`never` enum the guide describes. [R8] [R9]
- The dynamic PowerShell 7 profile GUID is
  `{574e775e-4f2a-5b96-ac1e-a2962a402336}` and the Windows PowerShell GUID is
  `{61c54bbd-c2c6-5271-96e7-009a87ff44bf}`, as stated. [R1]
- The legacy `keys`-inside-`actions` format is migrated to `keybindings` on
  load and the file is rewritten; comments are stripped. [R1]
- `Update-WtSshFragment.ps1` (§11), extracted verbatim from the guide:
  - Same output and the same GUIDs on PowerShell 7.7.0 and 5.1.
  - Handles multi-alias `Host` lines and `Host=alias # comment`.
  - Skips `*`, `?`, and `!` patterns.
  - Detects `-prod` and `-prd` names.
  - Writes UTF-8 without a BOM.
- The FIPS claim for the generator holds. With the Windows FIPS policy enabled,
  .NET Framework blocks `MD5CryptoServiceProvider` and `SHA256Managed` but
  allows `SHA256CryptoServiceProvider`, and the generator runs on both
  PowerShell versions. [R10]
- The `pwsh -File` pitfall in §11 is real: `-File` passes `-Exclude a, b` as a
  single string.
- Terminal loads the fragment: its profiles appear in the live file with
  source `ssh-hosts`. [R1]
- The Scoop `nerd-fonts` bucket and the `JetBrainsMono-NF` and
  `JetBrainsMono-NF-Mono` manifests exist. [R7]

### Not verified

- Visual behavior: ligature rendering, tab and background colors, the
  multi-line paste dialog, the quake animation, the right-click menu. The test
  VM's RDP session did not render Terminal's window content to screen capture.
- Windows Terminal 1.24 behavior (only 1.25 was installed).
- The serial console profile (no COM port on the VM).

## r1.0.2 — 2026-11-22

Review fixes, commit `89dbda7`:

- §9: the one-off jump host example now uses `-J bastion-prod`.
- §9: corrected the `IdentitiesOnly` note.
- Appendix A aligned with the annotated `settings.json`: the same chords, and
  ligatures off for `core-sw01` and the serial console.
- §2 editing rules: script against the master copy with PowerShell 7.
- Added links to the VS Code and Starship guides.

Later commits the same day moved the guide to `microsoft/terminal/` and
dropped the revision suffix from the filename (`51b0f07`, `f658403`,
`9299222`).

## r1.0.1 — 2026-10-05

Multi-agent review fixes (`13dd207`), plus a TOC expanded to linked
subsections (`4317030`).

## r1.0.0 — 2026-10-05

First version (`5d274c2`).

## References

- **[R1] Live settings rewrite test.** On the VM, the guide's `settings.json`
  (and variants) was copied to
  `%LOCALAPPDATA%\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json`.
  The file Terminal wrote back was then compared key by key, and `state.json`
  in the same folder was read.
- **[R2] Settings model strings.** String search of
  `Microsoft.Terminal.Settings.Model.dll`, `TerminalApp.dll`, and
  `Microsoft.Terminal.Settings.Editor.dll` from the 1.25.3131.0 package folder
  (`C:\Program Files\WindowsApps\Microsoft.WindowsTerminal_1.25.3131.0_x64__8wekyb3d8bbwe\`).
- **[R3] Package manifest and resources.** `AppxManifest.xml`
  (`windows.startupTask`, TaskId `StartTerminalOnLoginTask`, enabled=false) and
  `resources.pri` (label "Launch on machine startup") in the same folder. See
  also <https://learn.microsoft.com/windows/terminal/customize-settings/startup>.
- **[R4] `defaults.json`** from the 1.25.3131.0 package folder (actions,
  keybindings, and profile defaults).
- **[R5] DirectWrite query.** `IDWriteFactory::GetSystemFontCollection`,
  `IDWriteFontCollection::FindFamilyName`, and the family name enumeration,
  called from PowerShell on the VM.
  <https://learn.microsoft.com/windows/win32/api/dwrite/nf-dwrite-idwritefontcollection-findfamilyname>
- **[R6] Font files.** OpenType `name` table IDs 1 (family) and 16
  (typographic family) read from `JetBrainsMono-Regular.ttf` (v2.304) and
  `JetBrainsMonoNerdFont*-Regular.ttf` (Nerd Fonts v3.5.1).
  <https://github.com/JetBrains/JetBrainsMono/releases>,
  <https://github.com/ryanoasis/nerd-fonts/releases>,
  <https://learn.microsoft.com/typography/opentype/spec/name>
- **[R7] Scoop bucket.** <https://github.com/matthewjberger/scoop-nerd-fonts>
  (manifests `JetBrainsMono-NF.json`, `JetBrainsMono-NF-Mono.json`, and
  `JetBrainsMono-NF-Propo.json`), registered as `nerd-fonts` in
  <https://github.com/ScoopInstaller/Scoop/blob/master/buckets.json>.
- **[R8] Published schema.** <https://aka.ms/terminal-profiles-schema>, fetched
  2026-11-22.
- **[R9] Main-branch schema.**
  <https://raw.githubusercontent.com/microsoft/terminal/main/doc/cascadia/profiles.schema.json>,
  fetched 2026-11-22.
- **[R10] FIPS policy.**
  `HKLM\SYSTEM\CurrentControlSet\Control\Lsa\FipsAlgorithmPolicy\Enabled`, set
  to 1 for the test and restored to 0 afterwards.
  <https://learn.microsoft.com/windows/security/security-foundations/certification/fips-140-validation>
- **[R11] `state.json`.**
  `%LOCALAPPDATA%\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\state.json`,
  read on the VM; it holds application state such as `generatedProfiles`,
  `persistedWindowLayouts`, `sshFolderGenerated`, and `dismissedMessages`.
- **[R12] OpenSSH client options.** `ServerAliveInterval`,
  `ServerAliveCountMax`, and `TCPKeepAlive` in ssh_config(5):
  <https://man.openbsd.org/ssh_config#ServerAliveInterval>
