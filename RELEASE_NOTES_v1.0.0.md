# Polycode Coach v1.0.0 — First Release

**Offline app to learn Python & Java by typing, not watching.**

![demo](demo.gif)

> 37 Python + 36 Java lessons, sandboxed playground, XP/streaks, daily challenges — runs on any Windows PC without Python installed.

## Download

- **PolycodeCoach-v1.0.0.zip** (22 MB) — unzip and double-click `PolycodeCoach/PolycodeCoach.exe` or `run.bat`
- No install, no `pip`. Your progress saves to `%APPDATA%\PolycodeCoach\learning_progress.json` (user-choosable via `Settings → File location`).

## What's inside

- **Learn:** Beginner (9) → Intermediate (9) → Advanced (19 Python / 18 Java) — concepts, practice, debug broken code, fill-in blanks, quizzes, final projects per lesson
- **Playground:** 25 starters (Games, Stories, Math, Tricks, Tools, Writing Code-It-First) + `⌨` Wrap toggle + `🔓 Run anything` (any import) vs safe mode
- **Planning Guide:** Interactive skill-tree-like roadmap — pick `Python`/`Java` track, choose `2/4/6-week` pace, see `Week N — done/total` + `🏆 Week Complete`, click any lesson chip (`✓` done, `●` current) to jump
- **Progress:** XP (+5 practice, +8 debug, +25 project, +25 daily +2 streak bonus at 5-day streak), streak heatmap, level roadmap, `Sandbox` unified tab (`Load into Editor` + `Surprise Me` grid-fitted)
- **Quality:** Soft light/dark/ocean/forest themes, airier spacing, slimmer nav (46px), `Settings → File location` lets you move the save file anywhere

## Run from source

```powershell
python lumixa.py
# or
py lumixa.py
```

## Verify

```powershell
python -m py_compile lumixa.py
python tests/test_learning_progress.py  # 153 passed (fallback to lumixa when learn not present)
```

## For devs (local only)

`learn_python_gui.py` (hot-reload), `build.py`, `watch_build.py`, `generate_guided_hq_gif.py`, `tests/`, `_archive/` are dev-only and not on GitHub user repo — kept locally via `.gitignore`.

## Credits

MIT © 2026 LumixaCoder — built with Tkinter, PyInstaller, Python 3.13.
