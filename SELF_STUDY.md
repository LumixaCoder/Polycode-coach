# Learn Polycode Coach On Your Own — No Coach Needed

You said you want to *see* and *learn it yourself* — this is your solo track. Follow in order, 30-60 min each, all in `lumixa.py` + `languages/` + `data/` only. No `pip`.

### 0. One-time setup (5 min)
```powershell
git clone https://github.com/LumixaCoder/Polycode-coach.git
cd Polycode-coach
python lumixa.py  # or py lumixa.py — pick Python/Java in app, do 1 quiz
```
Progress saves to `%APPDATA%\PolycodeCoach\learning_progress.json` (`lumixa.py:4296`). Use `Settings → File location` to move it.

### 1. Map the 17k lines (15 min) — don’t read top-to-bottom
Open `lumixa.py` and jump by `class`:
- `PythonLearnerApp:10403` — window, router `show_frame()`, `F1` hotkey you just added `10446`, `F1/Ctrl+H` → `_toggle_coach_hotkey:11060`
- `SidebarFrame:11286` — 7 primary + `More` dropdown `7006a1d`
- `LearningPage:16449` — scroll `16506 canvas+vsb+inner`, `PanedWindow 16768 left/right`, `dots 16552`, `nav 16597` — **your editor lives here**
- `CoachPanel:13975` — now auto-shown `12` lines `13991`, `F1` toggles it. Chips `13997` call `coach_response:7606`
- `SandboxPage:13474` — free playground, `runtime/python.exe` `build.py:56`
- `ProgressPage:12523` `5` tabs, `SettingsPage:15655` scroll `15734`

**Exercise:** Change `THEMES["light"]["accent"]` near `lumixa.py:300`, save, `python lumixa.py` — see color change. Revert.

### 2. How a lesson works (20 min)
- Canonical data: `languages/python/lessons.py:1` `3682` lines, `languages/java/lessons.py:2704`, shim `lesson_data.py:8`
- `build_lesson_sets():123` returns `{"Beginner":9, "Intermediate":9, "Advanced":19}` — each `lesson{title, unit, steps[], final_project{check}}`
- Step types `lumixa.py:212`:
  - `concept` `16782` (view only, now has Coach `16835`)
  - `practice` `16822` (`check: lambda code: "len(" in code` → `evaluate_code_attempt:6783` via `analyze_code:7257` ast)
  - `debug` `17086` (`broken_code`, `bug_notes`)
  - `fill` `17240` (`template ___`, `expected_output`)
  - `review` `17385`, `example` `17454`, `muscle` `17611` (`type_along_check:4721`)

**Exercise (solo, no Coach):** Add a practice step to `languages/python/lessons.py` `Beginner[0]` after line ~40:
```python
{"type": "practice", "instruction": "Print your name length with len()", "check": lambda c: "len(" in c and "print(" in c, "hint": "Try print(len(name))", "success_msg": "Nice!"},
```
Save, run `python lumixa.py` — your step appears. Delete after.

### 3. Sandbox — your solo lab (20 min)
- `run_user_code:9285` spawns `runtime/python.exe` (`_sandbox_python:8324`) with restricted `__builtins__` (`_restricted_import:7963` blocks `os`, `eval` → `check_blocked_code:8141`). Free run `SandboxPage:13474` toggle `Run anything` `13681` → `unrestricted=True` `9873`.
- `data/` `6` jsons `8420` (`us_states 50`) — `run_user_code` can `open('us_states.json')` `tests:1073`.

**Exercise:** Open `Sandbox` tab → `Games` starter → `Load into Editor` → change `print` loop → `Ctrl+Enter` (`17044`) or `▶ Run`. Break it with `import os` → see `Blocked` `430`. Fix.

### 4. Progress & XP on your own (15 min)
- `default_progress():4413` → `ensure_progress:4466` (`xp`, `streak`, `draft_code`, `language_states`)
- `award_xp:4928` `+5/+8/+25`, `update_streak:4598`, `save_progress:4383` atomic `tmp→rename`, `draft_code` autosave `KeyRelease 16866` + on close `10417`.
- `LearningPage:16836` `_coach_after_miss` only opens Coach after `2` fails — you control it now via `Close Coach` / `F1`.

**Exercise:** Open `learning_progress.json`, note `xp`, complete one `practice` → `+5`, `streak` +1, check file again.

### 5. Build your own zip (10 min, optional)
- `build.py:1-439` `6` steps `build.py:177` → `PyInstaller --onedir` `227` `languages.*.lessons` `205` + `data` `222` → `dist/PolycodeCoach/` + `runtime/` `338` + `run.bat` `361`.
```powershell
python build.py  # 60s, produces dist/PolycodeCoach/PolycodeCoach.exe
# or watch:
python build.py --watch  # rebuilds on save
```

### 6. Self-test without Coach (10 min)
```powershell
python -m pip install pytest
python -m pytest tests -q -k "not test_gui_window_auto_closes"  # 152 passed
# try to break a check: edit a lesson's `check` to `lambda c: False` → pytest fails → revert
```

### 7. Your solo checklist
- [ ] Change a theme, add a step, break/fix sandbox, add `F1` toggle you just used
- [ ] Read `CONTRIBUTING.md:1`, `CODE_OF_CONDUCT.md:1`, `SECURITY.md:1`
- [ ] Push a tag `git tag v1.1.2-test; git push origin v1.1.2-test` → `release.yml:7` auto `.zip` to Releases sidebar (delete test tag after)

Stuck solo? `README.md:37` `What it does` + `SELF_STUDY.md` + `F1` Coach. Want a built-in "Solo Lab" page in the app? I can add a `Solo` tab that lists these exercises with `Open` buttons.
