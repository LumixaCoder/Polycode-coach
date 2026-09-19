# Polycode Coach — Code Learning Coach

![demo](demo.gif)
<p align="center"><em>Full guided tour (35s, 900px, 29 frames) — Cold start → Pick Python → Welcome → Placement Quiz → Result (Beginner) → Learning: Concept → Practice (type → Run → +5 XP) → Debug (broken → Coach hint → Fix +8 XP) → Final Project → Progress (XP/streak/heatmap) → Skill Tree → Review → Drills → Daily Challenge → Memory Mode (See → Hide → Retype) → Sandbox Cards → Sandbox Run (output) → Badges → Settings → Planning Guide — cursor + callouts, global palette</em></p>

A Tkinter app that assesses your level in Python & Java, then walks you through
interactive lessons with hands-on code practice, quizzes, final projects,
spaced review, and progress/XP tracking.

> **New here?** Download → run `lumixa.py` → pick language → quiz → start coding. No `pip install` needed (stdlib only).

## Download (Windows, no install)

**Latest release:** [PolycodeCoach-v1.1.0.zip](https://github.com/LumixaCoder/Polycode-coach/releases/latest/download/PolycodeCoach-v1.1.0.zip) (22 MB) — unzip and double-click `PolycodeCoach/PolycodeCoach.exe` or `run.bat`. No Python needed.

- See [all releases](../../releases) · [v1.1.0 notes](../../releases/tag/v1.1.0) · [SHA256](../../releases/download/v1.1.0/PolycodeCoach-v1.1.0.zip.sha256)
- Your progress saves to `%APPDATA%\PolycodeCoach\learning_progress.json` (move it via `Settings → File location`).

> **For devs:** pushing a tag `v*` (e.g., `git tag v1.0.1; git push origin v1.0.1`) auto-builds the zip on GitHub Actions (`.github/workflows/release.yml`) and attaches it to the Release — no manual upload needed. See `RELEASE_NOTES_v1.1.0.md` for what's in v1.1.0.

## Run the GUI

If you have the built app, double-click `dist/PolycodeCoach/PolycodeCoach.exe` (or `run.bat`).

From source, open PowerShell in the project folder and run:

```powershell
python lumixa.py
```

If `python` is not available, try:

```powershell
py lumixa.py
```

## What it does

- Welcome screen with stats and roadmap (streak nudge + quick actions)
- A 6-question tiered placement quiz (2 easy / 2 medium / 2 hard → Beginner / Intermediate / Advanced)
- Step-by-step lessons: 37 Python (9/9/19) + 36 Java (9/9/18) — concepts, guided practice, and quick checks
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
- XP, streaks, level roadmap, and progress dashboard — now with 5 tabs: **Overview, Activity (heatmap), Reflex (0-1000 score), Mistakes (top 5 + targeted practice), Retention (% mastery)**
- Spaced-repetition review queue + **Drill Hub** (muscle-memory reps, visible notes, 3× perfect retypes, 1/2/4/7-day spacing) + **Memory Mode** (timed recall: See → Hide → Retype, 10s/20s/30s, 50% line + 50% char accuracy, Code Reflex score)
- **Adaptive coaching** — the Progress page reads your performance log and
  highlights the units you found hardest, with a "Strengthen" button to jump
  straight back to a weak lesson — plus **Mistake Analytics** that classifies your errors and suggests drills
- **Autosave** — progress is saved atomically (crash-safe) after every step,
  lesson, project, and review, plus a periodic backup and a final save on close
- Light/dark themes and fullscreen — tabs now organized as 7 primary + **More** dropdown (Review/Drills/Skill Tree/Badges/Planning) so every feature fits 1060×740

## The Goal of the App

The goal is simple: go from a complete beginner to a confident Python *and* Java programmer
by actually writing code, not just reading about it.

Here is the journey:

1. **Take the placement quiz** — 6 tiered questions (2 easy / 2 medium / 2 hard) that figure out where you
   should start (Beginner / Intermediate / Advanced). Don't worry about
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
   found hard so the material actually sticks. For muscle memory, use **Drills** (visible with notes, 3 perfect retypes, then 1/2/4/7-day spacing) — and for true recall, try **Memory Mode** (See → Hide → Retype, 10s/20s/30s timed, scored 50% line + 50% char).
7. **Track mastery on Progress** — 5 tabs: **Overview, Activity (heatmap), Reflex (0–1000 Code Reflex score), Mistakes (top 5 + targeted drills), Retention (% per concept)**. The **Skill Tree** shows your visual roadmap; **Badges** (23) and **Planning Guide** (2/4/6-week tracks) keep you motivated and organized.
8. **Pass the level quiz** to unlock the next level (Beginner → Intermediate →
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

- **Beginner (9 lessons)** — variables, numbers, strings, conditions, lists, loops,
  functions, and reading/fixing broken code. The foundation of everything.
- **Intermediate (9 lessons)** — dictionaries, sets, list comprehensions, file I/O,
  error handling, f-strings for real formatting, and more advanced patterns.
- **Advanced (19 Python / 18 Java)** — decorators, generators, regular expressions, testing with
  `assert`, recursion and algorithm thinking, and real-world project design.

Python has 37 total lessons, Java 36 (GUI/tkinter track is Python-only). Once you finish **every** lesson in a level, it's time to tackle the next one. Switch languages anytime via Main Menu — progress, XP, streak and badges are shared globally, lesson progress is per-language (`language_states`).

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
- **💡 Project Playground** — inside the Sandbox tab you'll find 25 ready-to-run
  starter projects in six categories (🎲 Games, 📖 Stories, 🧮 Math, 🪄 Code
  Tricks, 🛠 Real Tools, 📝 Writing). Pick a starting idea, hit **Load into Editor**, run it,
  or press **🎲 Surprise Me** to get a random project. Two `Writing` starters are **Code-It-First**: they do nothing until you fill the `TODO`s — then paste any sentence in `user_text` or the `Input` box and `Run` to see your fixer work. Every starter finishes
  with a "make it yours" list of fun ways to tweak it.
- **🎉 Celebrations** — when you complete a lesson, or project, level up, or
  earn a new badge, the app celebrates with a confetti burst so you know you
  nailed it.

## Where is my progress saved?

Progress saves automatically after every step, lesson, and review — and again when you close the app. No manual saving needed.

- File location: `%APPDATA%\PolycodeCoach\learning_progress.json`
- Backup & Restore: open **Settings → Backup & Restore** to export a copy or import one on a new PC. Your streak, XP, badges, and per-language lesson progress carry over.

## Tips

- Switch languages anytime via **Main Menu** — XP, streak, and badges are shared; lesson progress is per-language.
- Use **Playground** to experiment freely — nothing there is graded.
- Keep your streak alive with a quick **Review** or **Daily Challenge** if you are short on time.
