---
Title: Starship Prompt in Windows Terminal — PowerShell 7 Guide
Version: r1.0.1
Updated: 2026-11-22
Scope: Windows 11, Windows Terminal, PowerShell 7, Starship
Reference build: Starship 1.27.0, PowerShell 7.7.0, Windows 11 24H2 (build 26100)
Companion: ms-terminal-json-settings
Topics: Starship, PowerShell 7, Windows Terminal, prompt, winget, PowerShell profile, JetBrains Mono, Nerd Fonts, starship.toml, troubleshooting
---

# Starship Prompt in Windows Terminal — PowerShell 7 Guide

> Install Starship on Windows, load it from the PowerShell 7 profile used by
> Windows Terminal, and choose symbols that render with JetBrains Mono. This
> guide uses the shared `JetBrains Mono` 14-point setup from the companion
> Windows Terminal guide. It also explains how to switch to a Nerd Font if you
> prefer icon-heavy prompt styles.

## Table of Contents

- [1. What Starship changes](#1-what-starship-changes)
- [2. Prerequisites](#2-prerequisites)
- [3. Install Starship](#3-install-starship)
- [4. Initialize Starship in PowerShell 7](#4-initialize-starship-in-powershell-7)
- [5. Configure symbols for JetBrains Mono](#5-configure-symbols-for-jetbrains-mono)
- [6. Optional: use a Nerd Font](#6-optional-use-a-nerd-font)
- [7. Customize the prompt](#7-customize-the-prompt)
- [8. Verify the setup](#8-verify-the-setup)
- [9. Troubleshooting](#9-troubleshooting)
- [10. Remove or disable Starship](#10-remove-or-disable-starship)
- [References](#references)

______________________________________________________________________

## 1. What Starship changes

Starship replaces PowerShell's prompt display with a configurable prompt. It
can show the current directory, Git branch and working-tree state, command
status, and detected language or tool versions.

Windows Terminal hosts PowerShell, but Starship is installed and initialized
for the shell. The Terminal profile does not install Starship. This setup
changes the local PowerShell prompt; an SSH session uses the prompt configured
on the remote host.

______________________________________________________________________

## 2. Prerequisites

- Windows 11 with Windows Terminal installed.
- PowerShell 7 (`pwsh`). Check the version in a Terminal tab:

```powershell
$PSVersionTable.PSVersion
```

- The Windows Package Manager command `winget`, included with App Installer.
- A Terminal font. The companion guide's shared default is `JetBrains Mono`,
  size `14`:
  [Windows Terminal settings guide](ms-terminal-json-settings.md#5-font-configuration).

The Starship documentation recommends a Nerd Font for its icon symbols. This
guide first configures Starship's **No Nerd Fonts** preset, so the standard
JetBrains Mono family can be used without relying on Nerd Font private-use
glyphs. If you prefer those icons, see [§6](#6-optional-use-a-nerd-font).

______________________________________________________________________

## 3. Install Starship

Open PowerShell 7 and install the current package from WinGet:

```powershell
winget install --id Starship.Starship
```

Close and reopen Windows Terminal so the updated `PATH` is available. Confirm
that PowerShell can find Starship:

```powershell
starship --version
Get-Command starship
```

If WinGet reports that the package is already installed, use
`winget upgrade --id Starship.Starship` to update it.

______________________________________________________________________

## 4. Initialize Starship in PowerShell 7

PowerShell loads commands in its profile script when a new session starts.
Find the profile path for the PowerShell session running in Windows Terminal:

```powershell
$PROFILE
```

Create the profile directory and file if needed, then open the file:

```powershell
$profileDirectory = Split-Path -Parent $PROFILE
New-Item -ItemType Directory -Force -Path $profileDirectory | Out-Null
if (-not (Test-Path -LiteralPath $PROFILE)) {
    New-Item -ItemType File -Path $PROFILE | Out-Null
}
notepad $PROFILE
```

Keep any existing profile content. Add this line at the end:

```powershell
Invoke-Expression (&starship init powershell)
```

Save the file and open a new PowerShell tab. If another prompt tool such as
Oh My Posh also changes the prompt, disable its prompt initialization or choose
which prompt you want; avoid initializing two prompt engines in the same
session.

______________________________________________________________________

## 5. Configure symbols for JetBrains Mono

Create Starship's configuration directory and save the official preset that
avoids Nerd Font-only symbols:

```powershell
$starshipConfigDirectory = Join-Path $HOME '.config'
New-Item -ItemType Directory -Force -Path $starshipConfigDirectory | Out-Null
$starshipConfig = Join-Path $starshipConfigDirectory 'starship.toml'

# Back up an existing config before replacing it with the preset.
# The timestamp keeps earlier backups from being overwritten.
if (Test-Path -LiteralPath $starshipConfig) {
    Copy-Item -LiteralPath $starshipConfig -Destination "$starshipConfig.$(Get-Date -Format yyyyMMdd-HHmmss).bak"
}

starship preset no-nerd-font --force -o $starshipConfig
```

`--force` lets the preset replace an existing `starship.toml`. Without it,
Starship 1.27 stops with "use --force to overwrite existing configuration
file". The backup above runs first, so nothing is lost.

The config file is normally at `$HOME\.config\starship.toml`. The preset
changes symbols used by Starship modules so they don't depend on Nerd Font
glyphs. It does not change Windows Terminal's font setting. Keep the Terminal
profile set to `JetBrains Mono` at 14 points as in the companion guide.

______________________________________________________________________

## 6. Optional: use a Nerd Font

Choose this path if you want Starship themes with Nerd Font icons or Powerline
symbols:

1. Install a JetBrains Mono Nerd Font build with Scoop or from the Nerd Fonts
   zip, as described in the companion guide's
   [install options](ms-terminal-json-settings.md#install). Its
   [variant table](ms-terminal-json-settings.md#choosing-a-variant)
   explains the `Nerd Font` and `Nerd Font Mono` families.

1. Confirm the exact installed family name with the
   [font check](ms-terminal-json-settings.md#verify-the-install-and-the-exact-family-name);
   it can vary between Nerd Fonts releases.

1. In Windows Terminal, open **Settings → PowerShell → Appearance** and set
   the font face to that family. Keep the size at `14`. Alternatively, add a
   `font` override to the PowerShell profile in `settings.json`.

1. Restart the PowerShell tab or Terminal so it loads the installed font.

1. To use Starship's Nerd Font symbols preset, back up your current
   `starship.toml`, then run:

   ```powershell
   $starshipConfig = Join-Path (Join-Path $HOME '.config') 'starship.toml'
   if (Test-Path -LiteralPath $starshipConfig) {
       Copy-Item -LiteralPath $starshipConfig -Destination "$starshipConfig.$(Get-Date -Format yyyyMMdd-HHmmss).bak"
   }
   starship preset nerd-font-symbols --force -o $starshipConfig
   ```

With the standard `JetBrains Mono` face, some private-use Nerd Font symbols
may appear as boxes or blank spaces. Switch the Terminal profile to the Nerd
Font variant to render them.

______________________________________________________________________

## 7. Customize the prompt

Starship reads TOML from `$HOME\.config\starship.toml`. Open it in Notepad:

```powershell
notepad (Join-Path $HOME '.config\starship.toml')
```

For example, to choose a green `>` prompt character on success and a red one
after a failed command, edit the existing `[character]` section or add it if
the file does not already have one:

```toml
[character]
success_symbol = '[>](bold green)'
error_symbol = '[>](bold red)'
```

Starship can also display information from tools installed on the local
machine, such as Git, Python, or Node.js. Modules are generally shown when
their relevant context is detected—for example, the Git branch module inside
a Git repository. See the official
[configuration reference](https://starship.rs/config/) for module options and
the [presets catalog](https://starship.rs/presets/) for ready-made styles.

______________________________________________________________________

## 8. Verify the setup

- [ ] `starship --version` reports an installed version.
- [ ] `$PROFILE` points to the PowerShell profile you edited.
- [ ] A newly opened PowerShell tab displays the Starship prompt.
- [ ] `starship explain` describes the prompt modules currently shown.
- [ ] In a Git repository, the prompt shows the branch and relevant status.
- [ ] Symbols render correctly with the selected Terminal font.

______________________________________________________________________

## 9. Troubleshooting

| Symptom | Likely cause | Fix |
| -- | -- | -- |
| `starship` is not recognized | Terminal was open during installation, or Starship isn't on `PATH` | Restart Terminal; check `Get-Command starship` and the WinGet package installation. |
| Starship works when initialized manually but not in new tabs | The wrong profile file was edited, or it doesn't load | Check `$PROFILE`, ensure the init line is saved there, and inspect `Get-ExecutionPolicy -List` if PowerShell reports that scripts are blocked. |
| Old prompt still appears | Another prompt tool initializes after Starship | Remove or reorder the other prompt initialization so Starship runs last, or disable the other prompt tool. |
| Icons appear as boxes | The config uses Nerd Font symbols with a non-Nerd font | Use the No Nerd Fonts preset, or select an installed Nerd Font in the Terminal profile. |
| No Git branch appears | Current directory is not in a Git repository, or Git isn't available | Run `git status` in a repository and check `Get-Command git`. |
| Prompt displays unexpected module details | Starship detects a tool or project file in the current directory | Use `starship explain`, then disable or customize the relevant module in `starship.toml`. |

______________________________________________________________________

## 10. Remove or disable Starship

To disable Starship but keep it installed, remove or comment out this line in
the PowerShell profile:

```powershell
Invoke-Expression (&starship init powershell)
```

Open a new PowerShell tab to return to the normal PowerShell prompt. To remove
the package, use:

```powershell
winget uninstall --id Starship.Starship
```

Your `starship.toml` remains in `$HOME\.config`; remove it separately if you
no longer need the configuration.

______________________________________________________________________

## References

- Reference: <https://starship.rs/guide/> (installation and PowerShell initialization)
- Reference: <https://starship.rs/config/> (configuration file and modules)
- Reference: <https://starship.rs/presets/no-nerd-font> (No Nerd Fonts preset)
- Reference: <https://starship.rs/presets/nerd-font> (Nerd Font Symbols preset)
- Reference: <https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_profiles?view=powershell-7.5> (PowerShell profiles)
- Reference: <https://learn.microsoft.com/windows/terminal/customize-settings/profile-appearance> (Terminal profile font settings)
- Reference: <https://github.com/ryanoasis/nerd-fonts> (Nerd Fonts project)
