# CODEMAP — Polycode Coach

> **One file, 15,387 lines, 32 sections.** Use this map + `Ctrl+F SECTION XX` to jump.
> Every `SECTION` banner lists `Original: app/...` so you can grep either way.

## How to look through the code (3 ways)
1. **By SECTION** — `Ctrl+F` `SECTION 29` (Settings) or `SECTION 10c` (run_user_code)
2. **By original file** — `Ctrl+F` `Original: app/ui/pages/settings`
3. **By symbol** — `Ctrl+F` `def _backup_card` or `class SettingsPage`

```
learn_python_gui.py
  ├─ 00   IMPORTS           ~66
  ├─ 00b  LESSON DATA        91  build_lesson_sets() — 37 lessons (9/9/19) embedded; fallback lesson_data.py
  ├─ 01   LANGUAGE REGISTRY 3802  SUPPORTED_LANGUAGES, LANGUAGE_META, get_lesson_sets_for_language()
  ├─ 02   THEMES & FONTS    3873  THEMES (light/dark/ocean/forest), FONTS, SP, rebuild_fonts()
  ├─ 03   PROGRESS          4258  save/load_progress (atomic .tmp), default/ensure, streak, heatmap, weekly
  ├─ 04   GAMIFICATION      4684  BADGES 23, award_xp, newly_awarded_badges, daily_xp_series
  ├─ 05   SKILLS            5146  SKILL_LABELS, adaptive_path, level_roadmap_stats
  ├─ 06   REVIEWS           5407  REVIEW_INTERVALS, schedule_review, grade_review, due_reviews
  ├─ 07   PROJECTS          5492  enrich_project_with_guidance, variant rotation
  ├─ 08   EVALUATION        5820  record_attempt, assess_performance, evaluate_code_attempt
  ├─ 09   COACH             6257  analyze_code, coach_hint_specific, coach_diagnose, _GLOSSARY
  ├─ 10a  PYTHON SANDBOX    7032  check_blocked_code, _sandbox_python, _WORKER_SRC
  ├─ 10b  XP CHART          7366  draw_xp_chart (canvas sparkline)
  ├─ 11   DATASETS          7402  _data_dir, _load_dataset (data/*.json)
  ├─ 12   DAILY ENGINE      7443  daily_challenge_spec, grade_challenge_output
  ├─ 10c  RUNNER            8284  run_user_code (sandbox subprocess) ★
  ├─ 13   JAVA SANDBOX      8370  run_java_code, _is_jdk_available
  ├─ 14   UTILS             8674  _strip_for_check, run_code_for_language (bridge)
  ├─ 15   WIDGETS           8789  RoundedCard, RoundedProgress, SyntaxEditor, confetti_burst, show_toast
  ├─ 16   ROOT APP          9164  PythonLearnerApp (hot-reload 1.5s, autosave, menubar, show_frame)
  ├─ 17   SIDEBAR           9899  SidebarFrame (lesson dots, stats, roadmap)
  ├─ 18   Lang Selection   10131  LanguageSelectionPage — Main Menu grid
  ├─ 19   Welcome          10346  WelcomePage
  ├─ 20   Survey           10568  SurveyPage — 6 tiered questions
  ├─ 21   Result           10842  ResultPage — _is_correct()
  ├─ 22   Progress         11016  ProgressPage — roadmap, heatmap, weekly bar
  ├─ 23   Badges           11413  BadgesPage
  ├─ 24   Sandbox          11567  SandboxPage — 23 starters + inputs
  ├─ 25   CoachPanel       12081  CoachPanel widget
  ├─ 26   Review Queue     12310  ReviewQueuePage
  ├─ 27   Skill Tree       12458  SkillTreePage (canvas path)
  ├─ 28   Daily Challenge  12710  DailyChallengePage
  ├─ 29   Settings         13165  SettingsPage — size/theme/sound/focus/weekly/BACKUP & RESTORE/reset
  │                              _backup_card -> _export_progress / _import_progress (organized 2026-09-09)
  ├─ 30   Planning Guide   13585  PlanningGuidePage
  ├─ 31   Learning Core    13681  LearningPage — concept/practice/debug/fill/review + final_project ★
  └─ 32   __main__         15347  argparse --watch/--no-hot-reload, _enable_dpi_awareness, mainloop
```

## Block style (every helper now follows this)

```python
# ------------------------------------------------------------------
# 29a — Backup & Restore — UI + helpers (so scan order = read order)
# ------------------------------------------------------------------
def _backup_card(self, t):
    """Build the Backup & Restore card (Settings).

    What's happening:
      1. Card shell via _card()
      2. Button row — Export and Import
      3. Footer hint — where progress lives on disk
    """
    # --- 1) Card shell -------------------------------------------------
    ...

def _export_progress(self):
    """Export: ask path -> atomic save_progress -> toast
    Steps: a) asksaveasfilename  b) save_progress(.tmp)  c) toast/error
    """
```

*Search `BLOCK STYLE` in header `learn_python_gui.py:1` for the template. When you add a helper, put it right under its `SECTION`'s sub-banner.*

## Key flows to trace

- **Startup:** `__main__:15347` -> `_enable_dpi_awareness` -> `load_progress:611` -> `ensure_progress` -> `PythonLearnerApp:9164` -> `show_frame(LanguageSelectionPage:10131)`
- **Lesson loop:** `LearningPage:13681` -> `SyntaxEditor:8789` -> `Run` -> `run_code_for_language:8674` -> `check_blocked_code:7032` -> `_sandbox_python:7032` -> `evaluate_code_attempt:5820` -> `award_xp:4684` or `coach_diagnose:6257`
- **Progress:** `save_progress:4258` (mkdir + .tmp + os.replace + .bak) called on every step, lesson, review, autosave `9164`, and `WM_DELETE_WINDOW`
- **Build:** `build.py:244` PyInstaller --onedir + --add-data data/languages + runtime/ embed `3.13.14`

## Where to edit

- **Lessons:** `SECTION 00b:91` `build_lesson_sets()` — or `languages/python/lessons.py` (dynamic import preferred)
- **New theme:** `SECTION 02:3873` add to `THEMES` + `FONTS`
- **New badge:** `SECTION 04:4684` `BADGES` list (23 today)
- **New setting toggle:** `SECTION 29:13165` `SettingsPage` — copy `_sound_card`/`_backup_card` pattern
- **Sandbox allowlist:** `SECTION 10a:7032` `_ALLOWED_IMPORTS`

## Split option (if single file feels heavy)

- `app/` modular layout lives in `_archive_modular_before_single_file/app/` (68 files, already generated).
- To re-split from *current* file: `python _archive_modular_before_single_file/generate_modules.py` (uses current `learn_python_gui.py` including Backup card).
- Shim keeps `import learn_python_gui` working: `app/ui/app.py:9164` is real code, `learn_python_gui.py` re-exports.

## Verify

```powershell
python -m py_compile learn_python_gui.py
python -m pytest tests -q   # 153 passed
```

*Generated 2026-09-09 — lines pinned from `map_sec.py` audit.*
