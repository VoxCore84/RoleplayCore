# Restart the shared VoxCore/CalmCore hook daemon (127.0.0.1:19484) without holding the calling tool.
# Usage (from the PowerShell tool or a pwsh window):  pwsh -File tools/daemon_restart.ps1 [-Quiet]
# Why: `pythonw daemon_shim.py` from the Bash tool and `Start-Process -Wait` both block until the
# daemon child exits (session 288b, 2026-09-22). This script spawns detached and polls /health.
param([switch]$Quiet)
$base = 'http://127.0.0.1:19484'
$shim = Join-Path $PSScriptRoot '..\.claude\hooks\daemon_shim.py'
try { Invoke-RestMethod -Method Post -Uri "$base/shutdown" -TimeoutSec 3 | Out-Null } catch { }
Start-Sleep -Seconds 2
Start-Process pythonw -ArgumentList "`"$shim`"" -WindowStyle Hidden
for ($i = 0; $i -lt 10; $i++) {
    Start-Sleep -Seconds 1
    try {
        $h = Invoke-RestMethod -Uri "$base/health" -TimeoutSec 2
        if (-not $Quiet) { $h | ConvertTo-Json -Compress }
        exit 0
    } catch { }
}
Write-Error "hook daemon did not answer within 10 s"
exit 1
