@echo off
REM Lumixa — double-click this to start without a terminal window staying open.
REM Uses pythonw (windowed) so the console closes immediately after launch.
REM Prefers .venv\Scripts\pythonw.exe if present, else system pythonw, else python.

if exist "%~dp0.venv\Scripts\pythonw.exe" (
    start "" "%~dp0.venv\Scripts\pythonw.exe" "%~dp0lumixa.pyw"
    exit /b
)
where pythonw >nul 2>&1
if %errorlevel%==0 (
    start "" pythonw "%~dp0lumixa.pyw"
) else (
    start "" python "%~dp0lumixa.py"
)
exit
