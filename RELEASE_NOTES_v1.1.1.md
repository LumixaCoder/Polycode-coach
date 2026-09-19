# Polycode Coach v1.1.1 — Scrollbar Hotfix

**Same v1.1.0 features, now fully scrollable on small windows.**

![demo](demo.gif)

> 37 Python + 36 Java lessons, Memory Mode + Reflex + Mistake Analytics — no clipping on 900×600.

## Download

- **PolycodeCoach-v1.1.1.zip** (22 MB) — unzip and double-click `PolycodeCoach/PolycodeCoach.exe` or `run.bat`
- No install, no `pip`. Your progress saves to `%APPDATA%\PolycodeCoach\learning_progress.json` (move via `Settings → File location`).

## Fixed in v1.1.1

- **LearningPage scroll** `lumixa.py:16503` — header / progress bar `16544` / dots `16550` / `PanedWindow` `16564` / `nav` `16583` + success/warning banners `16660`/`16716` now live inside `scroll_outer → canvas + vsb → inner` with `_enable_mousewheel:10307` (`scrollregion` on `Configure`). Tall lessons never clip; wheel + vertical bar work.
- **SettingsPage scroll** `lumixa.py:15665` — all 9 cards (`Default text size`, `Theme`, `Language`, `Sound`, `Focus`, `Weekly`, `Backup & Restore`, `File location`, `Reset`) wrapped in same canvas+vsb+inner; `_card:15734` now uses `parent = getattr(self,'_scroll_inner',self)` so cards scroll inside `inner`. Preferences never clip on `minsize 900×600` `lumixa.py:10403`.
- Carry-over: `ProgressPage` already had `_scrolled:12534` / `_tab_scrolled:12618`, `SurveyPage` `canvas:12112`, `Sandbox` `deferred bottom pack` `13519` for Run buttons — no change.

## Carry-over from v1.1.0

- **Memory Mode** `15356` See 10/20/30s → Hide → Retype, 50% line+50% char → A-F + XP; **Reflex 0-1000**, **Mistake top-5**, **Retention %**, 7 primary + `More` tabs `7006a1d`, DrillHub filter persist `14560`, demo 29-frame HQ.

## Verify

```powershell
python -m py_compile lumixa.py
python -m pytest tests -q  # 153 passed
```

## Credits

MIT © 2026 LumixaCoder — built with Tkinter, PyInstaller, Python 3.13.
