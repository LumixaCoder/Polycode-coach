# Feature Brainstorm — Notes

Use this file to collect ideas for things to add to the app. Keep entries short
and actionable. Anything here is fair game — no idea is too small.

## Big-picture ideas

- [ ] Make the daily challenge optionally pick an even bigger streak bonus
- [x] Add practice targets / weekly goal tracking — weekly_goal + weekly_progress (Monday reset), bar on Progress + Settings `learn_python_gui.py:837-841, 6890-6915`
- [x] Let users build a tiny game (guess the number, mad libs) as a guided project — Sandbox starters already cover this (Guess My Number, Mad Libs) + 3 new: Quiz Game / To-Do / Calculator `learn_python_gui.py:6863-6905`

## Sandbox / playground

- [x] More starter projects (quiz game, to-do list, mini calculator) — 20 → 23 projects `learn_python_gui.py:6863`
- [x] "Save my code" so work in the playground isn't lost — sandbox_code autosave 1.5s + Ctrl+S + language-specific `learn_python_gui.py:6995-7010`
- [x] Show sample input/outputs for each project before loading — sample_io field + preview in _show_info `learn_python_gui.py:6907-6930, 7128`

## Lessons & content

- [x] More practice steps inside each lesson (currently debug/fill/typing) — infra exists (5 types), quantity still expandable — DONE 2026-09-09: audit shows 7 steps/lesson (concept/practice/concept/practice/debug/practice/review) for all 9 Beginner + 9 Intermediate + 19 Advanced; each has debug/fill + integration practice `learn_python_gui.py:110+`
- [x] Backup & restore progress (export/import JSON) — Backup & restore card in Settings with filedialog + ensure_progress + full UI refresh `learn_python_gui.py:84,10370-10440`
- [x] A "what am I supposed to type?" primer for each feature — _GLOSSARY + guided_help_plan already; now per-step primer via coach `learn_python_gui.py:2450-2475`
- [x] More datasets for the data lessons (movies, weather, books?) — 3 → 6 datasets `data/movies.json, weather.json, books.json` + 3 new daily challenges `learn_python_gui.py:3180, 3325-3337`

## Motivation & progress

- [x] Bigger celebration animations when hitting milestones — confetti_burst big=True (120 pieces, longer) + sound + legendary check `learn_python_gui.py:4604-4670, 5259`
- [x] A leaderboard view of your own stats over time — XP chart + stats chips + heatmap + weekly bar on ProgressPage `learn_python_gui.py:6658-6735, 6750-6785`
- [x] Tempo / focus mode (hide results until you hit "check") — focus_mode toggle in Settings `learn_python_gui.py:8335-8347` (hides auto-output when ON)

## UI / polish

- [x] More color themes — light/dark + ocean/forest (4 total) `learn_python_gui.py:79-188`
- [x] Sound effects toggle — sound_enabled + winsound beep on celebrate `learn_python_gui.py:509-643, 8335`
- [x] Keyboard shortcuts (Ctrl+Enter to run code, Ctrl+S to save) — Ctrl+Enter everywhere + global Ctrl+S/Cmd+S `learn_python_gui.py:4705-4720, 6995-7010`

## Ideas the user mentioned (capture here as they come up)

-

## Decided / being built now

-

## Popular coding-site features we could borrow

- [x] Contribution heatmap calendar (GitHub / freeCodeCamp style) — data already exists (daily solves + XP) — 20-week canvas on ProgressPage `learn_python_gui.py:6750-6785`
- [x] Hidden test-case grading: one function checked against many inputs (LeetCode / Codewars / SoloLearn) — grade_hidden_tests() utility `learn_python_gui.py:863-885` + daily challenge expected_lines harness
- [x] 3-level progressive hints: nudge -> specific -> full answer (Codewars / Exercism) — coach_response stage 0-2 already done `learn_python_gui.py:2320-2330`
- [x] Plain-English error panel that re-explains common tracebacks (Codecademy) — explain_error() done `learn_python_gui.py:2830`
- [x] Type-along project mode — build a whole project by typing every line (freeCodeCamp) — type_along_check() validator `learn_python_gui.py:886-900`
- [x] Completion certificate per level, printable/PDF (freeCodeCamp) — per-level .txt certificate on ProgressPage `learn_python_gui.py:6790-6825`
- [x] Weekly quests with progress bars (Duolingo / Codecademy) — weekly_goal + progress bar + Settings selector `learn_python_gui.py:6885-6915, 6768`
- [x] Streak-freeze item you can earn/spend (Duolingo) — streak_freezes every 7 days, consumed on gap `learn_python_gui.py:770-800, 852-862`
- [x] Skill-tree / path view of the course (Duolingo) — SkillTreePage canvas already done `learn_python_gui.py:7480+`
- [x] Personal leaderboard / stats-over-time view (Duolingo / SoloLearn) — XP chart + badges + ProgressPage stats `learn_python_gui.py:6658-6735`
- [x] Sample input(feature): let sandbox code use input() with supplied answers (Codecademy / Replit) — sandbox_inputs box + _make_input() mock `learn_python_gui.py:2858-2880, 6995-7050`