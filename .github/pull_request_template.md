<!-- Thank you! See CONTRIBUTING.md -->

## What does this PR do?

Fixes #...

## Checklist

- [ ] `python -m py_compile lumixa.py` passes
- [ ] `python -m py_compile languages/python/lessons.py` + `languages/java/lessons.py` passes
- [ ] `python -m pytest tests -q -k "not test_gui_window_auto_closes"` — 152 passed locally (or 153 with window test)
- [ ] Lesson shim still in sync: `python -c "import lesson_data, languages.python.lessons; ..."`
- [ ] Updated docs: `README.md` / `RELEASE_NOTES_v*.md` if user-visible
- [ ] No secrets, no `learning_progress.json` committed

## Screenshots / demo.gif

If UI changed, add before/after or update `demo.gif` via `generate_guided_hq_gif.py`.

## Repro steps

How I tested:

1. `python lumixa.py` → ...
