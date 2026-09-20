# Security & Bug Reporting

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.2.x   | :white_check_mark: |
| 1.1.x   | :white_check_mark: |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

We support `main` and the latest `v1.2.0` zip (`README.md:14`). Older zips stay downloadable at `../../releases` but won’t be patched.

## For everyone — report any bug, we’ll fix it

Found a crash, wrong Coach hint, lesson check too strict, UI clipping, streak/XP bug, or anything broken? **We want the report — no account or coding needed.**

**Easiest (public, preferred for bugs):**
1. `Issues → New issue → Bug report` (template `bug_report.yml:1`) — fill version `v1.2.0` / OS / repro steps + snippet. Or `Feature request` if it’s an idea.
2. Include `Settings → About → build_info.json` `tag`, screenshot/`demo.gif` frame, and what you expected.

**Private / sensitive (security):**
Polycode Coach runs student code in `lumixa.py:run_user_code:9285` with blocklist (`os`, `eval` → `check_blocked_code:8141`) + `runtime/python.exe` `build.py:56`. If you find a sandbox escape, file write, or XSS via `data/*.json` / `languages/*/lessons.py`:

1. **Do not open a public issue** for the sensitive details.
2. Email **treytonzadra@gmail.com** with `Subject: [PolycodeCoach Bug] <brief>` *or* `Security → Report a vulnerability` (private advisory).
3. Include repro code/steps, expected vs actual, Python/OS, `build_info.json` tag.

You’ll get a thank-you within 72h, triage within 7 days. We’ll keep you posted and credit you if you want. Public bug reports get a comment + closing issue when fixed — you’ll see the fix in the next `RELEASE_NOTES_v*.md`.

## What to report (examples)

- **Any bug:** crash (`CoachPanel:13975` not showing before `262982d`), `LearningPage:16449` scroll clip `16506`, `ProgressPage:12523` XP wrong, lesson `check` rejects correct code `languages/python/lessons.py:123`
- **Security:** sandbox bypass (`import os` should be `Blocked` `tests/test_learning_progress.py:430`), path traversal `Settings → File location` `%APPDATA%` `README.md:17`, code injection via `data/*.json`
- **Out of scope:** social engineering, physical access, infinite loops (they time out `tests:445`)

Thanks for helping us make it better for the next learner — every report makes the next zip better!
