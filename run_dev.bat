@echo off
REM One-click dev launcher: starts GUI + auto-update watcher together.
REM Just double-click this file, or run `python dev.py` in a terminal.
echo Starting dev mode (GUI + auto-update)...
python "%~dp0dev.py"
pause
