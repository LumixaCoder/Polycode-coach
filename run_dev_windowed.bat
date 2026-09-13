@echo off
REM Dev Portal — windowed (no terminal stays open)
REM Double-click this to open the DEV portal (hot-reload) without a console.
REM Uses pythonw so the black window closes immediately. Fallback to python if needed.

if exist "%~dp0.venv\Scripts\pythonw.exe" (
    start "" "%~dp0.venv\Scripts\pythonw.exe" "%~dp0learn_python_gui.py"
    exit /b
)
where pythonw >nul 2>&1
if %errorlevel%==0 (
    start "" pythonw "%~dp0learn_python_gui.py"
) else (
    start "" python "%~dp0learn_python_gui.py"
)
exit
