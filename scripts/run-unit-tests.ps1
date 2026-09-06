param(
    [string[]]$TestArgs = @()
)

$repoRoot = Split-Path -Parent $PSScriptRoot
$venvPython = Join-Path $repoRoot ".venv\Scripts\python.exe"

if (Test-Path $venvPython) {
    $python = $venvPython
} else {
    $python = "python"
}

& $python -m pytest (Join-Path $repoRoot "tests") @TestArgs
exit $LASTEXITCODE