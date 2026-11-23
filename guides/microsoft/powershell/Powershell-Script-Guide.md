---
Title: PowerShell Script Guide
Version: r1.6.0
Updated: 2026-09-08
Scope: Windows PowerShell 5.1 and PowerShell 7 scripting
Topics: Get-Help, comment-based help, native command arguments, Robocopy, console output, RawUI, pinned footer, Write-Progress, Get-ChildItem -Exclude, Windows Terminal
---

# PowerShell Script Guide

A living reference for PowerShell scripting concepts that come up while working in
this project. Versioned in the front matter above so it can grow over time — each new
topic bumps the revision. This is a human-readable companion to `CLAUDE.md`; `CLAUDE.md` tells
Claude Code the operational rules for this repo, this guide explains the underlying
PowerShell concepts those rules are built on.

## Get-Help and comment-based help

`Get-Help` is PowerShell's built-in cmdlet for retrieving documentation about any
cmdlet, function, script, or concept — the PowerShell equivalent of `man`.

### Where the content comes from

For your own functions and scripts (no compiled binary, no external help file),
`Get-Help` doesn't read separate documentation — it parses **comment-based help**: a
specially-tagged comment block using keywords like `.SYNOPSIS`, `.DESCRIPTION`,
`.PARAMETER`, `.EXAMPLE`, `.OUTPUTS`, and `.NOTES`. This is exactly the `<# ... #>`
block at the top of `Backup-Profile.ps1`, and the one inside each of its functions
(`Resolve-BackupDestination`, `Invoke-FolderMirror`).

### Where the block has to live

- For a **script**, the comment-based help block goes at the very top of the file,
  before `param()`.
- For a **function**, it has to be the *first statement inside the function body* —
  right after `function Name {`, before `param()`.

In both cases, the parser requires `.SYNOPSIS` (or another recognized keyword) to be
the first thing in that block.

### Gotcha: nothing can precede `.SYNOPSIS`

Nothing can precede `.SYNOPSIS` inside (or directly attached to) the help block —
not even a one-line decorative banner merged into the same comment run — or
`Get-Help` silently falls back to a bare auto-generated signature with no synopsis
or parameter text. **No error or warning is given**, which is what makes this easy to
miss.

This is why `Backup-Profile.ps1`'s function banners
(`# Function: Resolve-BackupDestination`) sit *outside and above* the `function`
keyword, as their own separate comment block, while the real `.SYNOPSIS`/
`.PARAMETER`/`.OUTPUTS` block stays untouched as the first statement inside the
function body:

```powershell
# =============================================================================
# Function: Resolve-BackupDestination
# =============================================================================
function Resolve-BackupDestination {
    <#
    .SYNOPSIS
        Validates the destination drive and returns the full backup destination path.
    .PARAMETER DestinationDrive
        Drive letter to back up into, e.g. "D:" or "D:\".
    .OUTPUTS
        System.String - the resolved <DestinationDrive>\<hostname> path.
    #>
    param(
        [Parameter(Mandatory = $true)]
        [string]$DestinationDrive
    )
    ...
}
```

Always confirm with `Get-Help <FunctionName>` (after dot-sourcing the script) any
time a function header changes, the same way you'd re-check
`Get-Help -Full <script>.ps1` after editing the script-level doc comment.

### Related gotcha: a line starting with a period ANYWHERE in the block breaks it too

The rule above ("nothing can precede `.SYNOPSIS`") undersells the actual danger.
Confirmed by direct testing: a line *later* in the block — inside `.DESCRIPTION`
or `.OUTPUTS`, well after a correctly-placed `.SYNOPSIS` — still breaks the whole
help block if its trimmed text happens to start with a period followed by a
letter, because PowerShell's parser reads it as an attempt at an unrecognized
help keyword. This bit `Backup-Profile.ps1`'s `ConvertTo-RobocopyArgumentString`
this session: its `.OUTPUTS` text wrapped onto a line reading (after the leading
whitespace) `.NET Framework - the runtime Windows PowerShell 5.1 uses...`, and
`Get-Help ConvertTo-RobocopyArgumentString` silently fell back to the bare
auto-generated signature — same symptom as the original gotcha, same **no error
or warning given**. A minimal repro:

```powershell
function Test-DotNetLine {
    <#
    .SYNOPSIS
        A minimal repro function.
    .OUTPUTS
        Some text here.
        .NET Framework does something.
    #>
    param()
}
# Get-Help Test-DotNetLine now returns the bare signature, no synopsis at all.
```

The same test with a line starting `.ssh contains your private keys...`
reproduces identically. The fix is just wording: rearrange the sentence so no
wrapped line's first word starts with a period (e.g. "the dotnet-framework
runtime" instead of ".NET Framework", or start the sentence with a different
word before the term). Since this has no error/warning, the only reliable way
to catch it is what this project already does: run `Get-Help <Name>` (or
`-Full` for a script) after any edit to a comment-based help block and actually
read the output, not just re-read the source.

### Using it

| Command | What it shows |
| -- | -- |
| `Get-Help ./Script.ps1` | Just the synopsis + syntax |
| `Get-Help ./Script.ps1 -Full` | Everything: description, all parameters, examples, notes |
| `Get-Help ./Script.ps1 -Examples` | Just the `.EXAMPLE` blocks |
| `Get-Help FunctionName -Parameter Preview` | Just one parameter's description |
| `./Script.ps1 -?` | Shorthand — same as `Get-Help ./Script.ps1` |

`-?` is a special common parameter every PowerShell command already understands, and
it's free the moment a script has a comment-based help block — there's no need for a
custom `--help` flag.

One caveat: for **functions** specifically, `Get-Help FunctionName` only works if the
function has been loaded into the session first (e.g. by dot-sourcing the script:
`. ./Backup-Profile.ps1 -DestinationDrive D: -WhatIf`), since `Get-Help` looks up the
function by name in memory, not by re-parsing a file each time.

## Passing arrays to native commands (Robocopy, etc.)

When you call a native executable (Robocopy, `git`, anything not a PowerShell
cmdlet/function) by splatting an array — `robocopy @robocopyArgs` — PowerShell
already marshals each array element as its own distinct argument, spaces and all.
You do **not** need to wrap an element containing spaces in manual quotes first.

```powershell
$robocopyArgs = @($Source, "C:\Users\me\Documents\Virtual Machines", '/XJ')
robocopy @robocopyArgs   # Robocopy receives "...\Virtual Machines" as ONE argument
```

### Gotcha: manually quoting an array element breaks it

Wrapping an element in literal `"` characters yourself —
`"`"$Path`""` — doesn't add quoting; PowerShell was already going to quote that
argument on your behalf because it contains a space. The literal quote characters
you added become part of the argument's *text*, so the native command receives a
double-quoted string (e.g. `""C:\...\Virtual Machines""`) instead of the path,
and Robocopy/whatever mis-parses it. Verified directly: dumping raw `argv` on both
sides shows the un-quoted array element arriving intact as a single argument, and
the manually-quoted version arriving with literal `"` characters baked into the
value. Let PowerShell's own array-to-native-argument handling do the quoting —
don't second-guess it by adding quotes yourself.

### Related gotcha: a trailing backslash before a closing quote

A path that *ends* in `\` (e.g. `"C:\Source\"`) and also needs quoting (because it
contains a space) is a real, separately-documented Windows/MSVCRT command-line
parsing trap: the trailing `\"` sequence can be read as an escaped literal quote
instead of the string terminator, which is a known history of breakage for
Robocopy specifically on older hosts (Windows PowerShell 5.1 / ISE). It doesn't
apply to anything in `Backup-Profile.ps1` today — `Join-Path` never leaves a
trailing separator on its result, confirmed directly, even when an input segment
already had one — but if a future change builds a path a different way (string
concatenation, a user-supplied value), strip a trailing `\` before passing it to
Robocopy.

## Live console output vs. capturing a native command's output

This section tells the full arc of three successive designs `Backup-Profile.ps1`
went through for running Robocopy, because each fixed a real problem the last
one had, and the reasoning behind each step matters more than just the final
answer.

### Round 1: bare passthrough, broken return value

When a native console app (Robocopy, `git`, anything not a PowerShell
cmdlet/function) is called as a bare, unredirected statement, PowerShell lets it
inherit the real console handles directly. Robocopy's own live per-file
percentage redraw depends on that: it writes a raw carriage return the terminal
itself renders in place, one line staying put while the number climbs. The
problem: called bare *inside a function*, that same output becomes part of the
function's own return value — PowerShell functions return every unconsumed
success-stream write, not just an explicit `return` — corrupting `$exitCode`
into an array instead of an int.

### Round 2: `| Out-Host` fixes the return value, breaks live progress

Piping the native call through `Out-Host` keeps its text out of the function's
return value. But the moment output is captured or piped in *any* way —
`| Out-Host`, `| Out-Null`, `$x = ...` — PowerShell has to redirect the child
process's stdout into a managed pipe to turn it into string objects. Robocopy
detects it's no longer talking to a real console and falls back to printing
every percentage update as its own line instead of redrawing in place. This is
Robocopy's own behavior, not a PowerShell quirk — the same thing happens piping
Robocopy's output in `cmd.exe`. Confirmed directly: this showed up exactly as
described, one line per percentage tick.

### Round 3a: `Start-Process -NoNewWindow` fixes live progress too

`Start-Process -NoNewWindow -Wait -PassThru` never feeds the child's console
output into PowerShell's success stream to begin with — there's nothing for the
enclosing function to accidentally return — so it isn't affected by the Round 1
problem either, and `-NoNewWindow` still lets the child share the current
console, live output included. The exit code comes back cleanly from the
returned `Process` object's `.ExitCode` property. For a script with no other
console-rendering needs, this is the right, final answer.

#### Gotcha (from this stage, still relevant below): `-ArgumentList` doesn't quote for you like a splat does

The "Passing arrays to native commands" section above shows that splatting an
array directly at a native command (`robocopy @robocopyArgs`) already quotes
each element correctly on your behalf — manually adding quotes yourself breaks
it. `Start-Process -ArgumentList`, and later `ProcessStartInfo.Arguments`
(Round 3b below), are the opposite case: on Windows PowerShell 5.1, passing an
array can naively space-join the elements *without* quoting, so a path like
`C:\Users\John Doe\Documents` can arrive as two separate arguments instead of
one. `ProcessStartInfo` on modern .NET has `ArgumentList` (a real collection
that quotes each element for you, solving this) but it's a `netcore-2.1+`/
`net5.0+`-only API — confirmed absent from .NET Framework via Microsoft's own
API reference, so it doesn't exist under Windows PowerShell 5.1 at all. Any
string-based argument path (`Start-Process -ArgumentList` with a single string,
or `ProcessStartInfo.Arguments`) needs its own quoting done first, following
the same rules `CommandLineToArgvW` expects: wrap anything containing
whitespace or a `"` in double quotes, and only double up backslashes when they
immediately precede a quote (or the closing quote itself).
`ConvertTo-RobocopyArgumentString` in `Backup-Profile.ps1` does exactly this —
round-trip verified against an independent argv tokenizer covering spaces,
embedded quotes, trailing backslashes, and an empty argument. The two
invocation styles need opposite handling: a direct splat (`cmd @args`) already
quotes for you — don't add quotes yourself; a string-based argument path does
not — you must.

### Round 3b: a pinned footer needs capturing back — but that's fine now

`Start-Process` passthrough (Round 3a) and a footer pinned to the bottom of the
console are fundamentally incompatible: a footer means the script's own code
has to reposition the cursor to repaint it, and Robocopy's own raw console
writes would be a second, uncoordinated writer to that same cursor — the two
would race and garble the screen. Getting a footer back means capturing
Robocopy's output again, deliberately re-accepting the Round 2 regression this
time, because it no longer matters: once every line is a separately parseable
event anyway (needed to tally dirs/files/bytes for the footer), "one line per
event" is exactly the scrolling display the feature wants, not a defect to work
around.

The capture itself uses `System.Diagnostics.Process`/`ProcessStartInfo`
directly (not `Start-Process`, which has no clean way to hand back a live
readable stream) with `RedirectStandardOutput = $true`, then a **synchronous**
`while (-not $proc.StandardOutput.EndOfStream) { $proc.StandardOutput.ReadLine() }`
loop on the main thread — deliberately not `Register-ObjectEvent`/async reads,
since nothing else needs to run concurrently and a cross-thread console-cursor
write from an event-handler thread would be a real race risk for no benefit.
Confirmed directly that `TextReader.ReadLine()` (the base for `StreamReader`)
treats a lone `\r`, a lone `\n`, or `\r\n` all as line terminators — part of the
documented, unchanged-since-.NET-1.x contract, so this holds under .NET
Framework/PS 5.1 too, and correctly splits Robocopy's per-tick percentage
output even if it's emitted via bare `\r` once non-console.

`StandardError` is deliberately **not** redirected. Robocopy is documented to
write essentially all of its output, including errors, to stdout; redirecting
both streams without an async drain is a classic way to deadlock a `Process`
(the unread stream's pipe buffer fills, the child blocks writing to it, you're
blocked reading the other one) — redirecting only stdout accepts a small,
explicit residual risk (a stray stderr write landing on the console at an
unplanned cursor position) instead of a real deadlock risk.

## The pinned-footer technique: plain RawUI cursor math, not ANSI/VT

> **Superseded** — this whole approach was confirmed broken on Windows
> Terminal and replaced with [`Write-Progress`](#gotcha-write-progress-beats-a-hand-rolled-rawui-footer-for-host-portable-progress).
> Kept below as the record of what was tried and why it didn't hold up.

A footer pinned to the bottom of the console while other content scrolls above
it sounds like it needs a real terminal scroll region (the ANSI/VT `DECSTBM`
sequence). `Backup-Profile.ps1`'s `Show-BackupFooter` deliberately avoids that:
it uses `$Host.UI.RawUI`'s `CursorPosition`/`WindowSize`/`WindowPosition`
properties (part of core PowerShell, unchanged since v1) instead, for one
reason — that's one stable API surface identical on Windows PowerShell 5.1 and
PowerShell 7, on legacy conhost and Windows Terminal alike, with no dependency
on `ENABLE_VIRTUAL_TERMINAL_PROCESSING` being turned on. Mixing VT sequences
with manual `CursorPosition` math is a known source of bugs on some conhost
versions once VT is enabled - committing to one API family avoids that class of
problem entirely.

The mechanism: recompute the footer's target row as
`$rawui.WindowPosition.Y + $rawui.WindowSize.Height - 1` — "wherever the bottom
of the visible window currently is" — on **every** repaint, never cached, since
the window's position within the buffer keeps advancing as content scrolls and
the window can be resized mid-run. Save the cursor position first, move it to
that row, write the footer text, then restore it — inside a `try`/`finally`,
not just a `try`/`catch`, so a failed write can never leave the cursor stuck at
the footer row corrupting the next line of real output. Truncate/pad the
footer text to `WindowSize.Width - 1`, never the literal last column — writing
into it is a known trigger for an unwanted scroll on legacy conhost.

### Gotcha: probe every property you'll actually use, not just "does it throw"

A capability probe for "can this host support X" is only as good as what it
actually exercises. `Test-BackupFooterSupported` checks `$Host.Name` for the
ISE (no real console at all), `[Console]::IsOutputRedirected`, that
`WindowSize` isn't zeroed (some hosts return a zeroed size without throwing,
rather than failing outright — a bare try/catch alone would miss this), that
`CursorPosition` is actually *settable* (not just readable), and that
`$Host.UI.Write()` itself succeeds (a host could support repositioning the
cursor but no-op or fail on the actual write, which cursor-only checks would
never catch). Test every distinct operation you'll depend on later, not a
representative subset — each one is a different way a host can fall short.

## Gotcha: `Get-ChildItem -Recurse -Exclude` does not prune recursion

`-Exclude` reads like it should skip an entire excluded directory, but
confirmed by direct testing (against a real, unmodified directory, no files
created/changed): it only filters the *name* of each item `Get-ChildItem`
would otherwise return — it does **not** stop the recursion from descending
into a directory that matches the exclude pattern.

```powershell
Get-ChildItem -Path /some/dir -Recurse -Force -Exclude "excluded_folder"
# Still returns excluded_folder/some_file.txt - the directory itself is
# skipped from the output, but everything inside it is still walked and
# returned.
```

This matters anywhere you're trying to mirror what a tool like Robocopy's
`/XD` actually does (skip a directory and everything under it) using plain
PowerShell enumeration. `Backup-Profile.ps1`'s `Get-BackupSourceTotal` needs
exactly that — a pre-scan total that matches what Robocopy will actually copy,
excludes included — and using `-Exclude` here would have silently inflated the
count with files inside excluded folders (e.g. `.vscode\extensions\...`) that
Robocopy correctly never touches, permanently overstating the denominator so a
live progress footer driven by that total would never reach 100%.

The fix is a manual walk: a `Stack`-based (or recursive-function) traversal
that checks each subdirectory's full path against the resolved exclude list
**before** pushing it onto the stack to descend into, not after enumerating
its contents. Two more things a naive walk needs to replicate by hand if it's
standing in for Robocopy specifically: skip reparse points yourself (Robocopy's
`/XJ` does this automatically; a plain recursive walk has no protection
against a symlink/junction loop and can hang), and use `-Force` so hidden/
system items are counted the way Robocopy counts them by default.

## Gotcha: a pinned footer can paint successfully yet not appear until the run ends, under Windows Terminal

> **Superseded** — the flush below did not fix it. See
> [Write-Progress beats a hand-rolled RawUI footer](#gotcha-write-progress-beats-a-hand-rolled-rawui-footer-for-host-portable-progress)
> for what actually did.

Bug report against the [pinned-footer technique](#the-pinned-footer-technique-plain-rawui-cursor-math-not-ansivt)
above: on a real run in Windows Terminal, the scrolling Robocopy output (file
names, percentages) updated live the whole time, but the footer line at the
bottom stayed frozen/blank until Robocopy exited — then it snapped straight to
the final numbers. `Tally.FooterFailureCount` never incremented, so
`Show-BackupFooter`'s own write wasn't throwing; the paint was "succeeding" and
still not visibly reaching the screen mid-run.

That symptom — a legacy console API call (`$Host.UI.Write` after moving
`CursorPosition` via `$Host.UI.RawUI`) succeeding but not producing a visible
repaint until the output stream goes idle — matches a known class of Windows
Terminal/ConPTY rendering-lag behavior: ConPTY can defer flushing a translated
write to the terminal while it's still busy processing a fast, continuous
stream of *other* output (here, Robocopy's own scrolling lines). The fix
applied is a single explicit flush right after the footer write:

```powershell
$Host.UI.Write($text)
[Console]::Out.Flush()
```

**Update: confirmed on the next real run that this did not fix it.** The
footer still froze until Robocopy exited. Guessing at ConPTY internals from a
Linux development machine with no Windows Terminal to reproduce against
turned out to be exactly as reliable as that sounds — the next attempt drops
the hand-rolled display entirely rather than patching it again; see the next
section.

## Gotcha: Write-Progress beats a hand-rolled RawUI footer for host-portable progress

Two attempts at a footer built from `$Host.UI.RawUI` cursor math — plain, then
with an added flush — both failed the same way under Windows Terminal. Rather
than try a third RawUI variant (e.g. anchoring to the cursor's current
position instead of `WindowPosition`/`WindowSize`), `Backup-Profile.ps1` was
rewritten to use PowerShell's own **`Write-Progress`** cmdlet instead:

```powershell
Write-Progress -Activity 'Backing up profile' `
    -Status 'Dirs: 12   Files: 340/900   Bytes: 61.2m/108.85m' `
    -PercentComplete 56
# ... later, once the whole run is done:
Write-Progress -Activity 'Backing up profile' -Completed
```

This is the better fix, not just a different guess, for a structural reason:
`Write-Progress` doesn't write to any of PowerShell's six numbered,
redirectable output streams (Success/Error/Warning/Verbose/Debug/
Information) at all — it's a separate mechanism, controlled only by
`$ProgressPreference`, that each PowerShell host (ConsoleHost, the ISE, VS
Code's integrated terminal) renders itself. That removes an entire category
of problem the RawUI approach had:

- **No capability probe needed.** The old `Test-BackupFooterSupported`
  existed only because writing raw cursor-position bytes into a redirected
  stream, or a host with no real console window, would corrupt output or
  throw. `Write-Progress` doesn't touch stdout at all, so it's safe to call
  unconditionally — including under the ISE (previously always disabled) and
  with output redirected (previously always disabled) — a caller who wants it
  silent can still set `$ProgressPreference = 'SilentlyContinue'`.
- **No manual row/width math, so no ConPTY translation-timing bug to hit.**
  The host owns rendering the progress record; this script only ever hands it
  a status string and a percentage.
- **A real completion API.** `-Completed` clears the progress UI explicitly,
  instead of the old approach's implicit "just stop repainting and hope the
  last paint sticks."

**Update: this also froze the same way on a real run.** Not a rendering
problem after all — see the next section for the actual root cause and fix.

## Gotcha: isolate the layer before guessing again — the bug was never in the display code

Three fixes in a row (RawUI footer, added flush, full `Write-Progress`
rewrite) failed identically: nothing visible until the run ends, then a
snap to the final state. Two of those were structurally unrelated rendering
mechanisms. That pattern is itself a signal worth acting on: don't propose a
fourth display-layer fix, go isolate which layer is actually responsible.

Four small standalone tests (no Robocopy, no `Backup-Profile.ps1`), each run
directly in the real Windows Terminal session that reproduced the bug,
nailed it down in order:

1. `Write-Progress` in a loop with `Start-Sleep -Milliseconds 300` between
   calls → updates live. `Write-Progress` itself works.
1. The same loop with **no** sleep at all, ~100 calls finishing in well
   under a second → **no progress bar appeared at all**, not even a stale
   one. PowerShell's console host has its own internal throttle on
   repainting the progress pane, separate from any throttle the script
   writes — an operation that finishes faster than that internal window
   never gets a single paint.
1. The same loop, but with irregular `Start-Sleep` delays (20–150ms,
   mimicking real I/O waits) *and* interleaved `Write-Host` scrolling output
   *and* the script's own 120ms throttle → **live and correct**, progress
   pinned at the bottom while lines scrolled above it.

Test 3 used the exact same throttle/interleaving structure the real script
uses — the only thing it didn't use was the real script's actual mechanism
for getting that timing: a synchronous `$process.StandardOutput.ReadLine()`
loop over Robocopy's redirected stdout pipe. That became the prime suspect,
for two independently well-documented reasons: a Win32 console app's stdio
is typically fully-buffered (not line-buffered) once its output isn't
attached to a real console, and Microsoft's own docs flag synchronous
`Process.StandardOutput` reads as prone to exactly this kind of delayed
delivery, recommending the async `OutputDataReceived`/`BeginOutputReadLine`
pattern instead.

### The naive async fix crashes the whole PowerShell process

The obvious next step — `$process.add_OutputDataReceived({ ... })` with a
scriptblock that just enqueues each line onto a
`[System.Collections.Concurrent.ConcurrentQueue[string]]` for the main
thread to drain later — parses fine, passes `PSScriptAnalyzer`, and looks
correct. Tested against a **real subprocess** (not just a stubbed
`Write-Progress`, since this is exactly the kind of bug that only shows up
against real async I/O), it crashed the entire `pwsh` process:

```
Unhandled exception. System.Management.Automation.PSInvalidOperationException:
There is no Runspace available to run scripts in this thread.
   at System.Management.Automation.ScriptBlock.GetContextFromTLS()
```

.NET invokes a raw event delegate like this on a bare thread-pool thread —
there is no PowerShell runspace attached to it at all, so executing *any*
PowerShell script there, even a single-line scriptblock that only calls
`.Enqueue()`, throws immediately and unhandled. This is exactly the risk
`Backup-Profile.ps1`'s original comment about avoiding "cross-thread console
cursor writes from an event-handler thread" was gesturing at, except the
actual failure mode is worse than a race — it's a hard crash, and it isn't
specific to console/cursor calls; it would hit any PowerShell code at all in
that handler.

**The fix: `Register-ObjectEvent`, not a raw `.add_EventName()` handler.**
`Register-ObjectEvent -InputObject $process -EventName 'OutputDataReceived' -SourceIdentifier $id`
subscribes through PowerShell's own event system instead. No user script
runs on the raw .NET callback thread at all — the engine just records each
event (as a queued `PSEventArgs`), and the main thread retrieves them later
with `Get-Event -SourceIdentifier $id` / `Remove-Event`. Verified against
the same real subprocess: no crash, and lines arrive progressively at
realistic intervals, not in a burst.

**Second bug caught by the same real-subprocess test**: `Get-Event -SourceIdentifier $id` returns *every* currently-queued matching event at
once, as an array, once more than one has arrived since the last poll — not
one event per call. A first draft that did `$evt = Get-Event ...; while ($evt) { ...; $evt = Get-Event ... }` assumed a single item and threw a
type-conversion error on `Remove-Event -EventIdentifier` the first time two
lines queued up between polls (which happened immediately, since Robocopy's
own banner lines print without any delay between them). The fix is a plain
`foreach` over `@(Get-Event ...)`, forcing array context so it behaves the
same whether zero, one, or many events are pending.

**The lesson, restated**: none of this — the crash, or the array bug — was
visible from `ParseFile` or `PSScriptAnalyzer` alone. Both were only caught
by running the actual code against a real child process emitting output
over real wall-clock time. When a fix involves async/event/threading
behavior, "parses clean and looks right" is not evidence it works; run it
against something real before calling it done.

**Still true, and worth repeating from the last two rounds**: this is
unverified on a real Windows Terminal session — no Windows host on this
development machine. What's now checked, beyond the previous round's static
analysis: the actual `Invoke-FolderMirror` function (not a hand-copied
fragment) run against a real subprocess (bash standing in for Robocopy,
since this is Linux) that emits output over real elapsed time with
`Write-Progress` stubbed, confirming progress events arrive progressively
and match the emitter's actual timing, that three consecutive calls leave
zero leaked event subscriptions or queued events, and that both the normal
and previously-broken empty-`-LogFile` (`-WhatIf`) paths complete correctly
end to end. If the display still doesn't show up live on a real run, that
now rules out RawUI, `Write-Progress` itself, and the read mechanism as
categories — the remaining fallback is polling Robocopy's own `/LOG` file
on a timer instead of reading its stdout at all, the pattern both working
reference scripts actually use.
