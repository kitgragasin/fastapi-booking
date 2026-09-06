@echo off
setlocal

powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0scripts\run-checks.ps1" %*
exit /b %ERRORLEVEL%