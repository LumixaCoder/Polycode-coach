# Support

## Getting help

- **New here?** See `README.md:12` Download → unzip `PolycodeCoach-v1.1.1.zip` → double-click `PolycodeCoach.exe`.
- **Bug or feature?** Open an issue with the templates (Bug report / Feature request).
- **Question / how-to?** Open a GitHub Discussion (enable via `Settings → Discussions` if not yet) or ask in Issues with label `question`.

## Common fixes

| Problem | Fix |
|---|---|
| `learning_progress.json` lost | Check `%APPDATA%\PolycodeCoach\` (`README.md:17`) or `Settings → Backup & Restore`. |
| Zip won’t run | Keep `runtime/`, `data/`, `languages/` next to `PolycodeCoach.exe` (`release.yml:106`). |
| Code times out | Infinite loop guard is 1–5s `tests/test_learning_progress.py:445` — add a `break`. |
| `tkinter` window won’t open | Run `python lumixa.py` not the zip; ensure `runtime/` embedded Python is intact. |

## Versions

Include `Settings → About → build_info.json` `tag` + `python_version` when filing issues.

We aim to respond within 3 days.
