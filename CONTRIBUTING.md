# Contributing to Polycode Coach

Thanks for helping make Polycode Coach better! This app is a Tkinter desktop app (`lumixa.py` ~18k LOC + `languages/python/lessons.py` / `languages/java/lessons.py` + `data/*.json`).

## Quick start (Windows, macOS, Linux)

No dependencies — stdlib only. Optional `pytest` for tests.

```powershell
# 1. Clone
git clone https://github.com/LumixaCoder/Polycode-coach.git
cd Polycode-coach

# 2. Run from source
python lumixa.py
# or
py lumixa.py

# 3. Run tests (exclude headless-flaky Tk test on CI)
python -m pip install pytest
python -m pytest tests -q -k "not test_gui_window_auto_closes"  # 152 passed locally; 153 with window test
```

## Project layout

- `lumixa.py` — main app (single-file, see `lesson_data.py` shim)
- `languages/python/lessons.py` / `languages/java/lessons.py` — 37 Python (9/9/19) + 36 Java (9/9/18) lessons
- `data/` — bundled datasets (`us_states.json` 50, `elements.json` 20, `planets.json` 8, etc.)
- `languages/` — per-language lesson sets
- `tests/test_learning_progress.py` — 153 tests (code eval, sandbox, gamification, UI)
- `build.py` / `watch_build.py` / `PolycodeCoach.spec` — PyInstaller build (not on GitHub, local only per `.gitignore`)

## How to contribute

1. **Open an issue first** for big changes — use `Bug report` or `Feature request` templates.
2. Fork → branch `feat/my-feature` or `fix/my-bug`.
3. Make focused commits. Keep `lumixa.py` line wraps readable; run:
   ```powershell
   python -m py_compile lumixa.py
   python -m py_compile languages/python/lessons.py
   python -m py_compile languages/java/lessons.py
   python -m pytest tests -q
   ```
4. Update docs if you change lessons/XP/badges — `README.md` levels table, `RELEASE_NOTES_v*.md`.
5. Push and open a PR against `main` — fill the PR template.

## Lesson authoring (quick)

Each lesson in `languages/python/lessons.py:build_lesson_sets()` is:

```python
{
  "title": "Built-in functions",
  "unit": "Core tools",
  "steps": [
    {"type": "concept", "title": "...", "content": "..."},
    {"type": "practice", "instruction": "Use len()", "check": lambda code: "len(" in code, ...},
    {"type": "debug", "broken_code": "...", "bug_notes": "...", "check": ...},
    {"type": "fill", "template": "def foo(___):\n    ___", "check": ...},
    {"type": "review", "question": "...", "options": [...], "answer": "..."},
    # also: example, muscle, memory
  ],
  "final_project": {"title": "...", "description": "...", "starter_code": "...", "check": ...}
}
```

Run `python -c "import lesson_data, languages.python.lessons; a=lesson_data.build_lesson_sets(); b=languages.python.lessons.build_lesson_sets(); print({k: len(v) for k,v in a.items()})"` — shim `lesson_data.py` must stay in sync.

## Release process (maintainers)

- Bump `README.md` Download link + create `RELEASE_NOTES_vX.Y.Z.md`.
- Tag and push: `git tag v1.2.0; git push origin v1.2.0` — `.github/workflows/release.yml` auto-builds `PolycodeCoach-vX.Y.Z.zip` + `.sha256` via PyInstaller on `windows-latest` and publishes to **Releases** sidebar.
- Manual dispatch: `Actions → release → Run workflow → tag: v1.2.0`.

## Code style

- No `pip` deps for app runtime; keep imports stdlib (`tkinter`, `ast`, `json`, `pathlib`).
- Sandboxed code runs in `runtime/python.exe` (embedded 3.13.14) — never `eval` user input inline.
- Keep UI responsive; use `PanedWindow` + `canvas+vsb+inner` for scrolling (see `lumixa.py:16503` LearningPage fix).

## Questions?

Open a Discussion or issue — we love first-time contributors!
