# Polycode Coach v1.1.0 — Memory Mode + Reflex

**Offline app to learn Python & Java by typing — now with true recall training.**

![demo](demo.gif)

> 37 Python + 36 Java lessons, sandboxed playground, XP/streaks, daily challenges — runs on any Windows PC without Python installed. New: memorize → hide → retype, scored Code Reflex.

## Download

- **PolycodeCoach-v1.1.0.zip** (22 MB) — unzip and double-click `PolycodeCoach/PolycodeCoach.exe` or `run.bat`
- No install, no `pip`. Your progress saves to `%APPDATA%\PolycodeCoach\learning_progress.json` (user-choosable via `Settings → File location`).

## What's new in v1.1.0

- **Memory Mode** (`lumixa.py:15356`, primary tab) — Recall Training: see snippet → timer hides it (10s/20s/30s) → retype from memory → graded 50% line-exact + 50% char accuracy → A-F + XP. `record_memory_attempt` tracks `memory_stats` + `memory_attempts`.
- **Code Reflex Score** — 0–1000 rolling score on `Progress → Reflex` tab, derived from memory accuracy + muscle reps + typing. Canvas sparkline + level label.
- **Mistake Analytics + Retention Dashboard** — `mistake_analytics` classifies errors (`NameError`, `Indent`, …) → top 5 + targeted drills on `Progress → Mistakes`; `Retention (%)` per concept on `Progress → Retention` from `review` + `drill_reviews` + `memory_stats`.
- **Tabs fit window** — 7 primary + `More` dropdown (Review / Drills / Skill Tree / Badges / Planning) so every feature fits 1060×740 (`lumixa.py:9164`).
- **Drill Hub polish** — filter persists via `self._level_filter` (`lumixa.py:14560`), header clarifies `≠ Drills (visible + 3× + notes, 1/2/4/7d) vs Memory (hide-timed + graded)`.
- **Sandbox Run always visible** — deferred packing `side="bottom"` for editor/input/unrestricted/btn rows (`lumixa.py:13519` / `13660` / `13724`); pane heights `360/310` + `180/120` so Run buttons never clip offscreen.
- **Demo refresh** — `demo.gif` 29-frame HQ 900px 2.4MB full tour now covers Memory Mode (See → Hide → Retype) + all tabs (`demo_preview.png` updated).

## Carry-over from v1.0.0

- **Learn:** Beginner (9) → Intermediate (9) → Advanced (19 Python / 18 Java) — concepts, practice, debug broken code, fill-in blanks, quizzes, final projects per lesson
- **Playground:** 25 starters (Games, Stories, Math, Tricks, Tools, Writing Code-It-First) + `⌨` Wrap toggle + `🔓 Run anything` (any import) vs safe mode
- **Planning Guide:** Interactive roadmap — pick `Python`/`Java` track, choose `2/4/6-week` pace, see `Week N — done/total` + `🏆 Week Complete`, click any lesson chip (`✓` done, `●` current) to jump
- **Progress:** XP (+5 practice, +8 debug, +25 project, +25 daily +2 streak bonus at 5-day streak), streak heatmap, level roadmap, `Sandbox` unified tab (`Load into Editor` + `Surprise Me`)
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
python -m pytest tests -q  # 153 passed
```

## For devs (local only)

`learn_python_gui.py` (hot-reload), `build.py`, `watch_build.py`, `generate_guided_hq_gif.py`, `tests/`, `_archive/` are dev-only and not on GitHub user repo — kept locally via `.gitignore`.

## Credits

MIT © 2026 LumixaCoder — built with Tkinter, PyInstaller, Python 3.13.
