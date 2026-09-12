# Polycode Coach — Code Learning Coach

![demo](demo.gif)
<p align="center"><em>Full guided tour (32s, 900px, 28 frames) — Cold start → Pick Python → Welcome → Placement Quiz → Result (Beginner) → Learning: Concept → Practice (type → Run → +5 XP) → Debug (broken → Coach hint → Fix +8 XP) → Final Project → Progress (XP/streak/heatmap) → Skill Tree → Review → Drills → Daily Challenge → Sandbox Cards → Sandbox Run (output) → Badges → Settings → Planning Guide — cursor + callouts, global palette</em></p>

A Tkinter app that assesses your level in Python & Java, then walks you through
interactive lessons with hands-on code practice, quizzes, final projects,
spaced review, and progress/XP tracking. Add more languages via `languages/<id>/lessons.py`.

> **New here?** Download → `python learn_python_gui.py` → pick language → quiz → start coding. No `pip install` needed (stdlib only, `watchdog` optional). See `CODEMAP.md` for where code lives.

## Run the GUI

1. Open PowerShell in the project folder.
2. Run:

```powershell
python learn_python_gui.py
```

If `python` is not available, try:

```powershell
py learn_python_gui.py
```

## What it does

- Welcome screen with stats and roadmap
- A 5-question level quiz (Beginner / Intermediate / Advanced)
- Step-by-step lessons: concepts, guided practice, and quick checks
- **Three kinds of hands-on practice** — write code from scratch, **debug broken code** that's handed to you, and **fill in the blanks** of a real template (you complete the missing pieces)
- A sandboxed code playground (student code runs in a restricted subprocess)
- A "Coach" panel: hints, error diagnosing, prediction quizzes, guided help
- **Code-savvy hints** — the Coach reads your actual code (with Python's `ast`)
  and gives tips specific to what you wrote: it names the piece you're missing
  ("add a for loop", "you defined `greet` but never called it"), lists what you
  already got right, and scales its wording to your level (Beginner gets tiny,
  one-step nudges; Advanced gets "make it exactly right").
- **Code drafts autosave** — whatever you type in the practice or final-project
  editor is saved shortly after you stop typing, again on the periodic autosave,
  and on exit, so reopening the app puts your exact code back with nothing
  retyped.
- Final projects per lesson with progressive starting hints
- XP, streaks, level roadmap, and progress dashboard
- Spaced-repetition review queue
- **Adaptive coaching** — the Progress page reads your performance log and
  highlights the units you found hardest, with a "Strengthen" button to jump
  straight back to a weak lesson
- **Autosave** — progress is saved atomically (crash-safe) after every step,
  lesson, project, and review, plus a periodic backup and a final save on close
- Light/dark themes and fullscreen

## The Goal of the App

The goal is simple: go from a complete beginner to a confident Python programmer
by actually writing code, not just reading about it.

Here is the journey:

1. **Take the placement quiz** — 5 quick questions that figure out where you
   should start (Beginner, Intermediate, or Advanced). Don't worry about
   "failing" — it just places you at the level that's right for you.
2. **Work through the lessons** — each lesson is a series of steps (concepts,
   guided examples, quizzes, and hands-on practice). You type real code and run
   it to see if it works.
3. **Complete each lesson's Final Project** — a bigger challenge that pulls
   together everything you just learned.
4. **Keep your streak alive** — do at least one activity each day (a lesson,
   a review, or the daily challenge).
5. **Solve the daily challenge** — a fresh problem every day, and it's tuned to
   your current level and lesson topic, so it stretches you where you already are
   (pure-code problems plus the bundled dataset challenges).
6. **Revisit your reviews** — spaced repetition re-surfaces lessons you
   found hard so the material actually sticks.
7. **Pass the level quiz** to unlock the next level (Beginner → Intermediate →
   Advanced) and keep going until you've finished every lesson.

## How to Earn XP

XP is your overall score and levels you up through the app. You earn it from
basically everything you do:

| Activity | XP |
|---|---|
| Complete a practice step | +5 |
| Pass a "debug the broken code" step | +8 |
| Pass a "fill in the blank" step | +8 |
| Answer a quiz question correctly | +3 |
| Complete a full lesson | +10 |
| Pass a final project | +25 |
| Pass a level quiz (level up) | +15 |
| Solve the daily challenge | +8 |

Keep an eye on the **Progress** page — it tracks your XP, streak, and which
units you found hardest.

## Levels (the Roadmap)

As your XP and completed lessons grow, you unlock new levels:

- **Beginner** — variables, numbers, strings, conditions, lists, loops,
  functions, and reading/fixing broken code. The foundation of everything.
- **Intermediate** — dictionaries, sets, list comprehensions, file I/O,
  error handling, f-strings for real formatting, and more advanced patterns.
- **Advanced** — decorators, generators, regular expressions, testing with
  `assert`, recursion and algorithm thinking, and real-world project design.

Once you finish **every** lesson in a level, it's time to tackle the next one.

## The 23 Achievements (and How to Get Each)

Badges are earned **automatically** as you progress — you never have to claim
them. The **Achievements** page shows all 23, with a difficulty rating on each
(★ = Easy, ★★★★★ = Legendary), and these were deliberately tuned to be a real
challenge — most require weeks of consistent work, not an afternoon. Here's the
full list and how to earn each one:

| Badge | How to earn | Difficulty |
|---|---|---|
| 📚 **First Steps** | Complete your very first practice step | ★ Easy |
| 🎓 **Graduate** | Finish every step in a lesson and click "Complete Lesson" | ★★ Easy |
| 🎯 **Sharpshooter** | Solve your first daily coding challenge | ★★ Easy |
| 🔍 **Recall** | Complete your first spaced review session | ★★ Easy |
| ⭐ **Century** | Learn 100 total XP | ★★ Easy |
| 🏅 **Half-Dozen** | Complete 6 full lessons | ★★★ Medium |
| 📦 **Builder** | Pass your first final project | ★★★ Medium |
| 🏃 **Step Sprinter** | Complete 50 individual practice/debug/fill steps | ★★★ Medium |
| 📅 **Daily Driver** | Solve 5 different daily challenges (5 separate days) | ★★★ Medium |
| 🔥 **On Fire** | Keep a 5-day learning streak | ★★★ Medium |
| 🚩 **Fortnight Warrior** | Keep a 14-day learning streak | ★★★★ Hard |
| 🧼 **Clean Build** | Pass a final project WITHOUT using any hint | ★★★★ Hard |
| 🧠 **Mind Sharpener** | Complete 10 spaced reviews | ★★★★ Hard |
| 🌱 **Foundation** | Complete every Beginner lesson | ★★★★ Hard |
| 🌟 **Star Collector** | Earn 1,500 total XP | ★★★★ Hard |
| 🏗️ **Project Purist** | Complete the final project of every Beginner lesson | ★★★★ Hard |
| 🧩 **Solver** | Solve 15 daily challenges (15 separate days) | ★★★★★ Legendary |
| 🏁 **Marathoner** | Complete 20 lessons across all levels | ★★★★★ Legendary |
| 🔥 **Unbreakable** | Keep a 30-day learning streak | ★★★★★ Legendary |
| 👑 **Python Crown** | Earn 5,000 total XP | ★★★★★ Legendary |
| 🏆 **Grand Builder** | Complete the final project of every Intermediate AND Advanced lesson | ★★★★★ Legendary |
| 💪 **Rising Star** | Complete every Intermediate lesson | ★★★★★ Legendary |
| 🚀 **Python Master** | Complete every Advanced lesson | ★★★★★ Legendary |

Tough ones to plan around:

- **Streaks (🔥, 🚩, Unbreakable)** are the real consistency test — one missed
  day resets them to zero. Protect your streak by doing even one quick review
  per day.
- **Clean Build** rewards self-sufficiency — every hint you reveal locks you
  out of it for that project.
- **Python Crown / Grand Builder** are endgame goals that basically require
  finishing the entire curriculum and keeping up with dailies and reviews over
  a long stretch.

**Bonus features to help you get everything:**

- **🛝 Playground (Sandbox)** — a free, ungraded code editor for experimenting.
  Try anything here without affecting your progress.
- **💡 Project Playground** — inside the Sandbox tab you'll find 20 ready-to-run
  starter projects in five categories (🎲 Games, 📖 Stories, 🧮 Math, 🪄 Code
  Tricks, 🛠 Real Tools). Pick a starting idea, hit **Load into Editor**, run it,
  or press **🎲 Surprise Me** to get a random project. Every starter finishes
  with a "make it yours" list of fun ways to tweak it.
- **🎉 Celebrations** — when you complete a lesson, or project, level up, or
  earn a new badge, the app celebrates with a confetti burst so you know you
  nailed it.

## Project structure

- `lumixa.py` — **USER EDITION — Polycode Coach** (clean, for users) — Tkinter app without hot-reload/watcher. This is what `build.py` freezes to `dist/PolycodeCoach/PolycodeCoach.exe`.
- `learn_python_gui.py` — **DEV EDITION — Lumixa** (for you) — same app + **live hot-reload** (polls lesson_data + languages/*/lessons.py every ~1.5s) and `--watch` auto-watcher. Keep editing here; `lumixa.py` is generated from it.
- `lesson_data.py` — the lesson, step, and final-project content (legacy fallback;
  per-language `languages/<id>/lessons.py` is preferred).
- `languages/` — per-language lesson modules (`python/lessons.py`, `java/lessons.py`,
  add more by creating `languages/<new>/lessons.py` + entry in `SUPPORTED_LANGUAGES`).
- `data/` — bundled datasets (`us_states.json`, `elements.json`, `planets.json`).
- `tests/test_learning_progress.py` — unit tests for evaluation, progress,
  sandbox, review scheduling, and lesson data.
- `build.py` — builds a distributable folder app with PyInstaller, bundles
  `data/` + `languages/` + embeddable Python runtime, writes `build_info.json`,
  and logs every build to `builds.log`. Supports `python build.py --watch`.
- `watch_build.py` — **auto-update watcher** (recursive, debounced, watchdog-aware).
  Watches all `.py` + `data/*.json` + `languages/**/*.py` and rebuilds on save.
  Uses `watchdog` if installed, otherwise polling. `python watch_build.py --help` for options.
- `dev.py` + `run_dev.bat` — **one-click dev launcher**: starts GUI with hot-reload
  *and* background exe watcher together. Recommended: `python dev.py` or double-click `run_dev.bat`.
- `PolycodeCoach.spec` — user build (Polycode Coach, from `lumixa.py`) + `Lumixa.spec` — dev build (Lumixa, from `learn_python_gui.py`) — both include `data` + `languages` + hiddenimports.
- `builds.log` — a readable history of every build: when it ran, how long it
  took, what changed, and whether it succeeded.

## Run the tests

```powershell
python -m pytest tests -q
```

## Build a distributable app

```powershell
python build.py
```

This produces `dist/Lumixa/` containing `Lumixa.exe`, a
`runtime/` Python interpreter (used by the sandbox), and a `run.bat` launcher.
Progress is saved to `%APPDATA%\Lumixa\learning_progress.json`.

## Auto-update while you code (no commands needed)

The app now **auto-updates every time you save a change** — two layers:

### 1) Live hot-reload (instant, no restart)

When you run from source (`python learn_python_gui.py`), the GUI polls
`lesson_data.py` + `languages/*/lessons.py` + `data/*.json` every ~1.5s.
Save a lesson file and within ~2s you get a `🔄 Auto-updated: ... reloaded`
toast and the new content appears — no restart, no rebuild.

- Works automatically, no flags needed
- Disable with `python learn_python_gui.py --no-hot-reload`

### 2) Auto-rebuild the frozen exe (dist/Lumixa)

For the distributable exe, use one of:

```powershell
# Recommended: one command starts GUI + watcher together
python dev.py
# or double-click run_dev.bat

# Or separately:
python watch_build.py              # watch & rebuild on every save
python learn_python_gui.py --watch # GUI spawns watcher in background
python build.py --watch            # build once then watch
```

Details:

- **What it watches (recursive):** all `.py` (including `languages/**/*.py`),
  `data/*.json`, `*.spec` — ignores `.venv`, `build`, `dist`, `__pycache__`,
  `.git`, `*.pyc`, `builds.log`, etc.
- **Debounce:** waits ~2.0s after your last save to settle, then builds
  (tune with `watch_build.py --debounce 1.0 --poll-interval 0.5`)
- **Backends:** uses `watchdog` (native OS events) if installed
  (`pip install watchdog` for instant, low-CPU), otherwise efficient polling
- **Output:** `dist/Lumixa/` (exe + runtime + data + languages)
  plus `build_info.json` with timestamp/trigger; `builds.log` history
- **If rebuild fails** (exe still running → Windows lock): close the app and
  save any file again to retry; watcher retries automatically
- **Stop:** `Ctrl+C` in watcher terminal, or close the GUI (dev.py stops both)

To review your build history, open `builds.log` in the project folder.
Verbose watcher: `python watch_build.py --verbose` (or `--poll` to force polling).
