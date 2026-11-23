---
Title: Changelog — Starship prompt in Windows Terminal guide
Updated: 2026-11-22
Companion: starship-powershell-guide
---

# Changelog — Starship prompt in Windows Terminal guide

Changes to `starship-powershell-guide.md`, newest first. Each entry says what
changed, why, and how it was checked. Sources are collected in
[References](#references).

## r1.0.1 — 2026-11-22

Verified on a Windows 11 test VM: Windows 11 24H2 (build 26100.9974), Starship
**1.27.0** (WinGet `Starship.Starship`), PowerShell 7.7.0, Windows Terminal
1.25.3131.0.

### Corrected

- **§5 and §6: `starship preset … -o` does not overwrite an existing file.**
  Starship 1.27.0 stops with "Error saving file, use --force to overwrite
  existing configuration file". So §5 failed whenever a `starship.toml`
  already existed, and §6 always failed, because §5 had just created one.
  Added `--force` to both commands (`-f, --force  Forcibly overwrite the output file if it already exists`), plus a note in §5. The backup step still runs
  first. [R1] [R2]

### Added

- Front matter: `Reference build` names the verified versions; version r1.0.1.

### Verified unchanged

- §3: `winget install --id Starship.Starship` installs
  `C:\Program Files\starship\bin\starship.exe`, which `Get-Command starship`
  finds. `winget upgrade --id Starship.Starship` reports "No available
  upgrade found" when current. [R3]
- §4: `$PROFILE` resolves to
  `Documents\PowerShell\Microsoft.PowerShell_profile.ps1`. The guide's
  create-and-open steps work, and `Invoke-Expression (&starship init powershell)`
  replaces the `prompt` function in a new `pwsh` session. [R4] [R5]
- §5 and §6: the timestamped backup name works. `no-nerd-font` and
  `nerd-font-symbols` are valid preset names (`starship preset --list`). [R2]
- §7: the `[character]` example parses and renders `>` as the prompt
  character.
- §8: `starship explain` lists the active modules.
- §9: on this VM, `LocalMachine` is `RemoteSigned`, so the profile script runs
  unsigned.
- §6 font names: see the Windows Terminal guide's changelog for the Nerd Fonts
  v3.5.1 family names and how Terminal resolves them.

### Not verified

- How the prompt looks in Terminal: glyph rendering with plain JetBrains Mono
  vs. a Nerd Font. The test VM's RDP session did not render Terminal's window
  content to screen capture.

## r1.0.0 — 2026-11-22

First version (`89dbda7`). Later the same day it moved to
`microsoft/terminal/`, and the revision suffix was dropped from the filename
(`51b0f07`, `f658403`, `9299222`).

## References

- **[R1] Starship CLI help:** `starship preset --help` (Starship 1.27.0, commit
  `f8e4e21`), run on the VM.
- **[R2] Starship presets.** <https://starship.rs/presets/>,
  <https://starship.rs/presets/no-nerd-font>,
  <https://starship.rs/presets/nerd-font>
- **[R3] WinGet.** `winget install` and `winget upgrade` output on the VM;
  <https://learn.microsoft.com/windows/package-manager/winget/>
- **[R4] PowerShell profiles.**
  <https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_profiles>
- **[R5] Starship install and init.** <https://starship.rs/guide/>
