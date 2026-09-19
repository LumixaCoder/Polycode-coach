# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.1.x   | :white_check_mark: |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

We support the latest `main` and the latest two tagged releases (`v1.1.1` is current). Older zips are still downloadable from `../../releases` but won’t receive patches.

## Reporting a Vulnerability

Polycode Coach runs student code in a restricted subprocess (`lumixa.py:run_user_code`) with a blocklist (`os`, `eval`, etc.) and an embedded `runtime/python.exe` fallback. If you find a sandbox escape, arbitrary file write, or XSS via lesson content:

1. **Do not open a public issue.**
2. Email **treytonzadra@gmail.com** with `Subject: [PolycodeCoach Security] <brief>` and include:
   - Repro code / steps
   - Expected vs actual behavior
   - Python version + OS + `build_info.json` `tag` if from zip
3. Or use GitHub `Security → Report a vulnerability` (private advisory).

You’ll get an acknowledgment within 72h, triage within 7 days. We’ll keep you updated and credit you (unless you prefer anonymity) when a fix ships.

## What to report

- Sandbox bypass (`import os` should be `Blocked` `tests/test_learning_progress.py:430`)
- Path traversal via `Settings → File location` (`%APPDATA%\PolycodeCoach\learning_progress.json` `README.md:17`)
- Code injection via `data/*.json` or `languages/*/lessons.py`

## Out of scope

- Social engineering, physical access, or DoS via infinite loops (those time out correctly `tests/test_learning_progress.py:445`).

Thanks for keeping learners safe!
