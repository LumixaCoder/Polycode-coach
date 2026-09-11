@echo off
REM Best auto-restart - GUI + background exe watcher (hot-reload is always on)
REM Double-click this, not learn_python_gui.py. Close the app and it restarts in 2s.
REM Press Ctrl+C in THIS console to stop forever.
title Lumixa - Auto-Restart (GUI + Watcher)
echo ========================================================
echo  Lumixa - best wrapper
echo  GUI + dist/Lumixa auto-rebuild on save
echo  Hot-reload 1.5s - just save lesson_data.py / languages/*/lessons.py
echo  Close the app window - it restarts in 2s | Ctrl+C here to stop
echo ========================================================
:loop
echo.
echo [%date% %time%] Starting dev.py (GUI + watcher)...
python dev.py
echo.
echo [%date% %time%] App exited (code %ERRORLEVEL%) - restarting in 2 seconds...
echo Press Ctrl+C now to cancel restart...
timeout /t 2 /nobreak >nul
goto loop
