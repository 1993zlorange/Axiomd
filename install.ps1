param(
    [ValidateSet("ai4programming", "ai4science", "all")]
    [string]$Profile = "all",

    [string]$CodexHome,

    [switch]$IncludeOptional,
    [switch]$Check,
    [switch]$Uninstall,
    [switch]$Prune,
    [switch]$Force,
    [switch]$DryRun
)

$ErrorActionPreference = "Stop"
$python = Get-Command -Name "python" -ErrorAction SilentlyContinue
if (-not $python) {
    $pyLauncher = Get-Command -Name "py" -ErrorAction SilentlyContinue
    if ($pyLauncher) {
        $python = $pyLauncher
        $arguments = @("-3", (Join-Path $PSScriptRoot "scripts\install.py"))
    }
} else {
    $arguments = @((Join-Path $PSScriptRoot "scripts\install.py"))
}

if (-not $python) {
    throw "Python 3.11+ is required. Install Python or run scripts/install.py with your preferred interpreter."
}

$arguments += @("--profile", $Profile)
if ($CodexHome) { $arguments += @("--codex-home", $CodexHome) }
if ($IncludeOptional) { $arguments += "--include-optional" }
if ($Check) { $arguments += "--check" }
if ($Uninstall) { $arguments += "--uninstall" }
if ($Prune) { $arguments += "--prune" }
if ($Force) { $arguments += "--force" }
if ($DryRun) { $arguments += "--dry-run" }

& $python.Source @arguments
exit $LASTEXITCODE
