@echo off
setlocal

powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0scripts\init-db.ps1" %*
exit /b %ERRORLEVEL%