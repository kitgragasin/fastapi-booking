param(
    [switch]$Reset
)

$repoRoot = Split-Path -Parent $PSScriptRoot
$venvPython = Join-Path $repoRoot ".venv\Scripts\python.exe"

if (Test-Path $venvPython) {
    $python = $venvPython
} else {
    $python = "python"
}

$env:PYTHONPATH = $repoRoot

if ($Reset) {
    $env:FASTAPI_BOOKING_RESET_DB = "1"
}

& $python -m app
exit $LASTEXITCODE