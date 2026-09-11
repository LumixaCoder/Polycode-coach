import sys
import tempfile
import unittest
import inspect
import json
from pathlib import Path
from datetime import date, timedelta

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import learn_python_gui


class CodeEvaluatorTests(unittest.TestCase):
    def test_builtin_functions_success(self):
        ok, msg = learn_python_gui.evaluate_code_attempt(
            "print(len('hello'))", {"title": "Built-in functions"}
        )
        self.assertTrue(ok)
        self.assertIn("Excellent", msg)

    def test_builtin_functions_hint(self):
        ok, msg = learn_python_gui.evaluate_code_attempt(
            "print('hi')", {"title": "Built-in functions"}
        )
        self.assertFalse(ok)
        self.assertIn("len()", msg)

    def test_keywords_success(self):
        ok, msg = learn_python_gui.evaluate_code_attempt(
            "for i in range(3):\n    print(i)", {"title": "Python keywords"}
        )
        self.assertTrue(ok)
        self.assertIn("Perfect", msg)

    def test_strings_success(self):
        ok, msg = learn_python_gui.evaluate_code_attempt(
            "word.upper()", {"title": "Strings and methods"}
        )
        self.assertTrue(ok)

    def test_lists_success(self):
        ok, msg = learn_python_gui.evaluate_code_attempt(
            "nums = [1, 2, 3]\nfor n in nums:\n    print(n)", {"title": "Lists and ranges"}
        )
        self.assertTrue(ok)

    def test_functions_success(self):
        ok, msg = learn_python_gui.evaluate_code_attempt(
            "def add(a, b):\n    return a + b", {"title": "Functions and returns"}
        )
        self.assertTrue(ok)

    def test_dictionaries_success(self):
        ok, msg = learn_python_gui.evaluate_code_attempt(
            "d = {'key': 'value'}", {"title": "Dictionaries"}
        )
        self.assertTrue(ok)

    def test_modules_success(self):
        ok, msg = learn_python_gui.evaluate_code_attempt(
            "import math", {"title": "Standard library modules"}
        )
        self.assertTrue(ok)

    def test_classes_success(self):
        ok, msg = learn_python_gui.evaluate_code_attempt(
            "class Dog:\n    def __init__(self, name):\n        self.name = name",
            {"title": "Classes and objects"},
        )
        self.assertTrue(ok)

    def test_file_handling_success(self):
        ok, msg = learn_python_gui.evaluate_code_attempt(
            "with open('test.txt', 'w') as f:\n    f.write('hello')",
            {"title": "File handling"},
        )
        self.assertTrue(ok)

    def test_empty_input(self):
        ok, msg = learn_python_gui.evaluate_code_attempt("", {"title": "Built-in functions"})
        self.assertFalse(ok)
        self.assertIn("Type something", msg)

    def test_unknown_lesson_title(self):
        ok, msg = learn_python_gui.evaluate_code_attempt(
            "x = 1", {"title": "Some Future Lesson"}
        )
        self.assertFalse(ok)
        self.assertIn("Try the example", msg)


class ProgressPersistenceTests(unittest.TestCase):
    def test_save_and_load_round_trip(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "progress.json"
            data = {
                "level": "Intermediate",
                "lesson_index": 2,
                "completed_lessons": [0, 1],
                "theme": "dark",
            }
            learn_python_gui.save_progress(path, data)
            loaded = learn_python_gui.load_progress(path)
            self.assertEqual(loaded, data)

    def test_load_missing_file(self):
        loaded = learn_python_gui.load_progress(Path("/nonexistent/path.json"))
        self.assertEqual(loaded, {})

    def test_load_corrupted_file(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "bad.json"
            path.write_text("not valid json {{{", encoding="utf-8")
            loaded = learn_python_gui.load_progress(path)
            self.assertEqual(loaded, {})

    def test_save_creates_parent_dirs(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "nested" / "deep" / "progress.json"
            learn_python_gui.save_progress(path, {"level": "Beginner"})
            loaded = learn_python_gui.load_progress(path)
            self.assertEqual(loaded, {"level": "Beginner"})

    def test_save_is_atomic_and_clean(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "progress.json"
            learn_python_gui.save_progress(path, {"a": 1})
            learn_python_gui.save_progress(path, {"a": 2, "b": [1, 2, 3]})
            loaded = learn_python_gui.load_progress(path)
            self.assertEqual(loaded, {"a": 2, "b": [1, 2, 3]})
            leftover = [p for p in Path(tmpdir).iterdir() if p.suffix == ".tmp"]
            self.assertEqual(leftover, [])

    def test_save_replaces_previous_content_wholesale(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "progress.json"
            learn_python_gui.save_progress(path, {"level": "Advanced", "x": 5})
            learn_python_gui.save_progress(path, {"x": 9})
            loaded = learn_python_gui.load_progress(path)
            self.assertEqual(loaded, {"x": 9})



class ThemeConstantsTests(unittest.TestCase):
    def test_both_themes_have_required_keys(self):
        required = [
            "bg", "panel", "text", "muted", "accent", "card", "border",
            "code_bg", "code_border", "tip_bg", "tip_text",
            "success", "error", "warning",
            "sidebar_bg", "sidebar_text", "sidebar_active",
            "navbar_bg", "navbar_text", "navbar_hover",
            "progress_bg", "progress_fill",
            "xp_text", "xp_bg", "streak_text", "streak_bg",
            "badge_beginner", "badge_intermediate", "badge_advanced",
            "toast_bg", "toast_text", "accent_border", "roadmap_line",
        ]
        for theme_name, theme in learn_python_gui.THEMES.items():
            for key in required:
                self.assertIn(key, theme, f"Missing '{key}' in {theme_name} theme")

    def test_fonts_defined(self):
        self.assertIn("heading_lg", learn_python_gui.FONTS)
        self.assertIn("code", learn_python_gui.FONTS)
        self.assertIn("button", learn_python_gui.FONTS)
        self.assertIn("heading_xl", learn_python_gui.FONTS)
        self.assertIn("badge", learn_python_gui.FONTS)
        self.assertIn("stat_num", learn_python_gui.FONTS)
        self.assertIn("toast", learn_python_gui.FONTS)


class LessonDataTests(unittest.TestCase):
    def test_all_lessons_have_final_project(self):
        app_cls = learn_python_gui.LearningPage
        instance = app_cls.__new__(app_cls)
        lesson_sets = app_cls._build_lesson_sets(instance)
        for level, lessons in lesson_sets.items():
            for i, lesson in enumerate(lessons):
                self.assertIn(
                    "final_project", lesson,
                    f"{level} lesson {i} '{lesson['title']}' missing final_project",
                )
                proj = lesson["final_project"]
                for field in ("title", "description", "steps", "starter_code", "check",
                              "scenario", "start_hints", "starter_snippet"):
                    self.assertIn(
                        field, proj,
                        f"final_project in '{lesson['title']}' missing '{field}'",
                    )

    def test_final_project_checks_reject_stub_code(self):
        app_cls = learn_python_gui.LearningPage
        instance = app_cls.__new__(app_cls)
        lesson_sets = app_cls._build_lesson_sets(instance)
        for level, lessons in lesson_sets.items():
            for i, lesson in enumerate(lessons):
                proj = lesson["final_project"]
                res = proj["check"]("print('hi')")
                ok = res[0] if isinstance(res, tuple) else res
                self.assertFalse(
                    ok,
                    f"final_project in '{lesson['title']}' wrongly accepts stub code; "
                    "it must return (False, msg) via `(True, msg) if cond else (False, msg)`",
                )
                if isinstance(res, tuple):
                    self.assertIsInstance(res[1], str,
                                          f"final_project msg in '{lesson['title']}' must be a clean string")

    def test_all_lessons_have_steps(self):
        app_cls = learn_python_gui.LearningPage
        instance = app_cls.__new__(app_cls)
        lesson_sets = app_cls._build_lesson_sets(instance)
        for level, lessons in lesson_sets.items():
            for i, lesson in enumerate(lessons):
                self.assertIn(
                    "steps", lesson,
                    f"{level} lesson {i} '{lesson['title']}' missing steps",
                )
                steps = lesson["steps"]
                self.assertGreater(len(steps), 0,
                    f"{level} lesson {i} '{lesson['title']}' has no steps")
                for j, s in enumerate(steps):
                    self.assertIn("type", s,
                        f"Step {j} in '{lesson['title']}' missing 'type'")
                    self.assertIn(s["type"], ("concept", "practice", "review", "debug", "fill", "example", "muscle"),
                        f"Step {j} in '{lesson['title']}' has invalid type '{s['type']}'")
                    if s["type"] == "practice":
                        for field in ("instruction", "check", "hint", "success_msg"):
                            self.assertIn(field, s,
                                f"Practice step {j} in '{lesson['title']}' missing '{field}'")
                    elif s["type"] == "concept":
                        for field in ("title", "content"):
                            self.assertIn(field, s,
                                f"Concept step {j} in '{lesson['title']}' missing '{field}'")
                    elif s["type"] == "review":
                        for field in ("question", "options", "answer"):
                            self.assertIn(field, s,
                                f"Review step {j} in '{lesson['title']}' missing '{field}'")
                    elif s["type"] == "debug":
                        for field in ("instruction", "broken_code", "bug_notes", "goal_hint", "check", "success_msg"):
                            self.assertIn(field, s,
                                f"Debug step {j} in '{lesson['title']}' missing '{field}'")
                    elif s["type"] == "fill":
                        for field in ("instruction", "template", "expected_output", "goal_hint", "check", "success_msg"):
                            self.assertIn(field, s,
                                f"Fill step {j} in '{lesson['title']}' missing '{field}'")
                    elif s["type"] == "example":
                        for field in ("code", "instruction"):
                            self.assertIn(field, s,
                                f"Example step {j} in '{lesson['title']}' missing '{field}'")
                    elif s["type"] == "muscle":
                        for field in ("instruction", "target_code"):
                            self.assertIn(field, s,
                                f"Muscle step {j} in '{lesson['title']}' missing '{field}'")

    def test_step_key_helper(self):
        k = learn_python_gui.step_key("Beginner", 0, 2)
        self.assertEqual(k, "Beginner_0_2")

    def test_project_hint_key_helper(self):
        k = learn_python_gui.project_hint_key("Beginner", 1)
        self.assertEqual(k, "Beginner_1_proj_hints")

    def test_quiz_is_correct_choice(self):
        rp = learn_python_gui.ResultPage.__new__(learn_python_gui.ResultPage)
        self.assertTrue(rp._is_correct("10", {"type": "choice", "answer": "10"}))
        self.assertFalse(rp._is_correct("4", {"type": "choice", "answer": "10"}))

    def test_quiz_is_correct_fill_normalized(self):
        rp = learn_python_gui.ResultPage.__new__(learn_python_gui.ResultPage)
        q = {"type": "fill", "answer": "ada", "accept": ["ada"]}
        self.assertTrue(rp._is_correct("  ADA ", q))
        self.assertTrue(rp._is_correct("ada", q))
        self.assertFalse(rp._is_correct("p", q))

    def test_quiz_is_correct_code_check(self):
        rp = learn_python_gui.ResultPage.__new__(learn_python_gui.ResultPage)
        q = {"type": "code", "answer": "print('Hello World')",
             "check": lambda c: "print(" in c and "Hello" in c}
        self.assertTrue(rp._is_correct("print('Hello World')", q))
        self.assertFalse(rp._is_correct("for i in range(3):\n    pass", q))

    def test_ai_hint_empty_code(self):
        h = learn_python_gui.get_ai_hint("", "Variables", {"instruction": "Print hello"})
        self.assertIn("haven't typed anything", h)

    def test_ai_hint_missing_print(self):
        step = {"instruction": "Use print() to show the message", "hint": "x"}
        h = learn_python_gui.get_ai_hint("message = 'hi'", "Strings", step)
        self.assertIn("print()", h)

    def test_ai_hint_missing_len(self):
        step = {"instruction": "Use len() to count characters", "hint": "x"}
        h = learn_python_gui.get_ai_hint("name = 'hello'", "Strings", step)
        self.assertIn("len()", h)

    def test_ai_hint_fallback_when_complete(self):
        step = {"instruction": "Use print() to show the message", "hint": "x"}
        h = learn_python_gui.get_ai_hint("print('hi')", "Strings", step)
        self.assertTrue(h)

    def test_quiz_questions_exist(self):
        app_cls = learn_python_gui.SurveyPage
        instance = app_cls.__new__(app_cls)
        questions = app_cls._build_questions(instance)
        self.assertEqual(len(questions), 6)
        types = set()
        tiers = set()
        for q in questions:
            self.assertIn("prompt", q)
            self.assertIn("answer", q)
            qtype = q.get("type", "choice")
            types.add(qtype)
            tiers.add(q.get("tier", 1))
            self.assertEqual(qtype, "choice")
            self.assertIn("options", q)
            self.assertEqual(len(q["options"]), 4)
        self.assertEqual(types, set(["choice"]))
        self.assertEqual(tiers, set([1, 2, 3]))
        for tier in (1, 2, 3):
            self.assertEqual(sum(1 for q in questions if q.get("tier") == tier), 2)
        for q in questions:
            self.assertIn(q["answer"], q["options"])


class GamificationTests(unittest.TestCase):
    def test_default_progress_has_all_fields(self):
        dp = learn_python_gui.default_progress()
        for key in ("xp", "streak", "last_active_date", "code_check_attempts",
                     "level_history", "performance_log", "completed_steps", "step_index",
                     "project_hints", "project_fail_counts"):
            self.assertIn(key, dp)

    def test_ensure_progress_fills_missing_fields(self):
        p = {"level": "Beginner", "theme": "dark"}
        p = learn_python_gui.ensure_progress(p)
        self.assertEqual(p["xp"], 0)
        self.assertEqual(p["streak"], 0)
        self.assertEqual(p["code_check_attempts"], {})

    def test_award_xp(self):
        p = learn_python_gui.default_progress()
        learn_python_gui.award_xp(p, 25)
        self.assertEqual(p["xp"], 25)
        learn_python_gui.award_xp(p, 10)
        self.assertEqual(p["xp"], 35)

    def test_record_attempt(self):
        p = learn_python_gui.default_progress()
        learn_python_gui.record_attempt(p, "Beginner", 0, True)
        key = learn_python_gui.attempt_key("Beginner", 0)
        self.assertEqual(p["code_check_attempts"][key], [True])
        self.assertTrue(p["performance_log"][key]["first_try"])

    def test_record_attempt_not_first_try(self):
        p = learn_python_gui.default_progress()
        learn_python_gui.record_attempt(p, "Beginner", 0, False)
        learn_python_gui.record_attempt(p, "Beginner", 0, True)
        key = learn_python_gui.attempt_key("Beginner", 0)
        self.assertFalse(p["performance_log"][key]["first_try"])

    def test_record_project_pass(self):
        p = learn_python_gui.default_progress()
        learn_python_gui.record_project_pass(p, "Beginner", 1)
        key = learn_python_gui.attempt_key("Beginner", 1)
        self.assertTrue(p["performance_log"][key]["project_passed"])

    def test_record_project_pass_only_once(self):
        p = learn_python_gui.default_progress()
        first = learn_python_gui.record_project_pass(p, "Beginner", 1)
        second = learn_python_gui.record_project_pass(p, "Beginner", 1)
        self.assertTrue(first)
        self.assertFalse(second)
        key = learn_python_gui.attempt_key("Beginner", 1)
        self.assertTrue(p["performance_log"][key]["project_passed"])

    def test_mark_step_done_only_once(self):
        from types import SimpleNamespace
        lp = learn_python_gui.LearningPage.__new__(learn_python_gui.LearningPage)
        lp.controller = SimpleNamespace(progress=learn_python_gui.default_progress())
        self.assertTrue(lp._mark_step_done("Beginner", 0, 1))
        self.assertFalse(lp._mark_step_done("Beginner", 0, 1))
        self.assertFalse(lp._mark_step_done("Beginner", 0, 1))

    def test_update_streak_first_time(self):
        p = learn_python_gui.default_progress()
        learn_python_gui.update_streak(p)
        self.assertEqual(p["streak"], 1)
        self.assertNotEqual(p["last_active_date"], "")

    def test_update_streak_same_day(self):
        from datetime import date
        p = learn_python_gui.default_progress()
        p["last_active_date"] = date.today().isoformat()
        p["streak"] = 5
        learn_python_gui.update_streak(p)
        self.assertEqual(p["streak"], 5)


class SandboxExecutionTests(unittest.TestCase):
    def test_run_prints_output(self):
        res = learn_python_gui.run_user_code("print('hello from sandbox')", timeout=5)
        self.assertTrue(res["ok"])
        self.assertIn("hello from sandbox", res["output"])
        self.assertEqual(res["blocked"], "")

    def test_run_returns_real_value(self):
        res = learn_python_gui.run_user_code("total = 0\nfor n in range(5):\n    total += n\nprint(total)", timeout=5)
        self.assertTrue(res["ok"])
        self.assertEqual(res["output"].strip(), "10")

    def test_name_error_is_friendly(self):
        res = learn_python_gui.run_user_code("print(missing_name)", timeout=5)
        self.assertFalse(res["ok"])
        self.assertIn("isn't defined", res["explained"])

    def test_syntax_error_detected(self):
        res = learn_python_gui.run_user_code("print(5", timeout=5)
        self.assertFalse(res["ok"])
        self.assertIn("SyntaxError", res["error"])

    def test_blocked_import(self):
        res = learn_python_gui.run_user_code("import os", timeout=5)
        self.assertFalse(res["ok"])
        self.assertIn("Blocked", res["blocked"])

    def test_blocked_eval(self):
        res = learn_python_gui.run_user_code("eval('2+2')", timeout=5)
        self.assertFalse(res["ok"])
        self.assertIn("Blocked", res["blocked"])

    def test_allowed_import_works(self):
        res = learn_python_gui.run_user_code("import math\nprint(math.sqrt(16))", timeout=5)
        self.assertTrue(res["ok"])
        self.assertEqual(res["output"].strip(), "4.0")

    def test_infinite_loop_timeout(self):
        res = learn_python_gui.run_user_code("while True:\n    pass", timeout=1)
        self.assertFalse(res["ok"])
        self.assertIn("loop", res["explained"])

    def test_trace_captures_variables(self):
        res = learn_python_gui.run_user_code("x = 1\ny = x + 1\nprint(y)", timeout=5, trace=True)
        self.assertTrue(res["ok"])
        self.assertGreaterEqual(len(res["trace"]), 2)
        found_y = any(e.get("vars", {}).get("y") for e in res["trace"])
        self.assertTrue(found_y)

    def test_format_trace_steps(self):
        res = learn_python_gui.run_user_code("x = 1\nprint(x)", timeout=5, trace=True)
        text = learn_python_gui.format_trace_steps(res["trace"])
        self.assertIn("line", text)

    def test_multiple_print_output_preserved(self):
        res = learn_python_gui.run_user_code("print('one')\nprint('two')\nprint('three')", timeout=5)
        self.assertTrue(res["ok"])
        self.assertEqual(res["output"].strip(), "one\ntwo\nthree")

    def test_explain_error_nameerror(self):
        msg = learn_python_gui.explain_error("Traceback...\nNameError: name 'x' is not defined")
        self.assertIn("isn't defined", msg)

    def test_explain_error_indentation(self):
        msg = learn_python_gui.explain_error("IndentationError: expected an indented block")
        self.assertIn("Indentation", msg)


class ProgressEventsTests(unittest.TestCase):
    def test_award_xp_records_event(self):
        p = learn_python_gui.default_progress()
        learn_python_gui.award_xp(p, 5, "practice step")
        self.assertEqual(p["xp"], 5)
        self.assertEqual(len(p["events"]), 1)
        self.assertEqual(p["events"][0]["label"], "practice step")
        self.assertEqual(p["events"][0]["xp"], 5)

    def test_award_xp_no_label_still_records(self):
        p = learn_python_gui.default_progress()
        learn_python_gui.award_xp(p, 15)
        self.assertEqual(len(p["events"]), 1)
        self.assertEqual(p["events"][0]["label"], "")

    def test_events_capped(self):
        p = learn_python_gui.default_progress()
        for i in range(520):
            learn_python_gui.award_xp(p, 1)
        self.assertLessEqual(len(p["events"]), 500)

    def test_daily_xp_series(self):
        p = learn_python_gui.default_progress()
        learn_python_gui.award_xp(p, 5, "a")
        learn_python_gui.award_xp(p, 10, "b")
        series = learn_python_gui.daily_xp_series(p)
        self.assertEqual(len(series), 1)
        self.assertEqual(series[0][1], 15)

    def test_roadmap_stats(self):
        p = learn_python_gui.default_progress()
        p["level"] = "Beginner"
        p["completed_lessons"] = [0]
        lesson_sets = {"Beginner": [{"title": "A"}, {"title": "B"}],
                       "Intermediate": [{"title": "C"}],
                       "Advanced": [{"title": "D"}]}
        rows, done, total = learn_python_gui.level_roadmap_stats(p, lesson_sets)
        self.assertEqual(done, 1)
        self.assertEqual(total, 4)
        self.assertEqual(rows[0]["stage"], "current")
        self.assertEqual(rows[1]["stage"], "locked")

    def test_lesson_progress_snapshot(self):
        p = learn_python_gui.default_progress()
        p["level"] = "Beginner"
        p["completed_steps"] = {learn_python_gui.step_key("Beginner", 0, 1): True}
        lesson_sets = {"Beginner": [{"title": "Built-in functions", "steps": [
            {"type": "concept"}, {"type": "practice"}, {"type": "review"}]}]}
        snap = learn_python_gui.lesson_progress_snapshot(p, lesson_sets, "Beginner")
        self.assertEqual(snap[0]["done_steps"], 1)
        self.assertEqual(snap[0]["total_steps"], 2)

    def test_skill_checklist(self):
        p = learn_python_gui.default_progress()
        p["level"] = "Beginner"
        p["completed_lessons"] = [0]
        lesson_sets = {"Beginner": [{"title": "Built-in functions"}, {"title": "Python keywords"}]}
        items = learn_python_gui.skill_checklist(p, lesson_sets, "Beginner")
        self.assertTrue(items[0][1])
        self.assertFalse(items[1][1])

    def test_adaptive_path_empty_when_no_lessons_done(self):
        p = learn_python_gui.default_progress()
        p["level"] = "Beginner"
        lesson_sets = {"Beginner": [{"title": "Built-in functions", "unit": "Core",
                                     "steps": [{"type": "practice"}]}]}
        adv = learn_python_gui.adaptive_path(p, lesson_sets, "Beginner")
        self.assertEqual(adv["focus"], [])
        self.assertEqual(adv["mastery"], "")

    def test_adaptive_path_strong_when_all_first_try(self):
        p = learn_python_gui.default_progress()
        p["level"] = "Beginner"
        p["completed_lessons"] = [0]
        lesson_sets = {"Beginner": [{"title": "Built-in functions", "unit": "Core",
                                     "steps": [{"type": "practice"}]}]}
        learn_python_gui.record_attempt(p, "Beginner", 0, True)
        adv = learn_python_gui.adaptive_path(p, lesson_sets, "Beginner")
        self.assertEqual(adv["mastery"], "Strong")
        self.assertEqual(adv["focus"], [])

    def test_adaptive_path_flags_weak_unit(self):
        p = learn_python_gui.default_progress()
        p["level"] = "Beginner"
        p["completed_lessons"] = [0, 1]
        lesson_sets = {"Beginner": [
            {"title": "Loops lesson", "unit": "Loops", "steps": [{"type": "practice"}]},
            {"title": "Core lesson", "unit": "Core", "steps": [{"type": "practice"}]},
        ]}
        learn_python_gui.record_attempt(p, "Beginner", 0, False)
        learn_python_gui.record_attempt(p, "Beginner", 0, False)
        learn_python_gui.record_attempt(p, "Beginner", 0, True)
        learn_python_gui.record_attempt(p, "Beginner", 1, True)
        adv = learn_python_gui.adaptive_path(p, lesson_sets, "Beginner")
        self.assertEqual(adv["focus"][0]["unit"], "Loops")
        self.assertNotEqual(adv["mastery"], "Strong")
        self.assertEqual(adv["focus"][0]["detail"][0]["index"], 0)


    def test_coach_diagnose_empty(self):
        step = {"instruction": "Print your name"}
        msg = learn_python_gui.coach_diagnose("   ", step, {"ok": True, "output": ""})
        self.assertIn("haven't written", msg)

    def test_coach_diagnose_blocked(self):
        step = {"instruction": "Import math"}
        res = {"ok": False, "blocked": "Blocked: import os is not allowed."}
        msg = learn_python_gui.coach_diagnose("import os", step, res)
        self.assertIn("not allowed", msg)

    def test_coach_diagnose_error(self):
        step = {"instruction": "Print a value"}
        res = {"ok": False, "explained": "The name 'x' isn't defined.", "trace": []}
        msg = learn_python_gui.coach_diagnose("print(x)", step, res)
        self.assertIn("isn't defined", msg)

    def test_coach_diagnose_no_output(self):
        step = {"instruction": "Print the length of your name"}
        res = {"ok": True, "output": ""}
        msg = learn_python_gui.coach_diagnose("name = 'Ada'", step, res)
        self.assertIn("printed nothing", msg)

    def test_coach_response_hint_escalation(self):
        step = {"instruction": "Use len() on a variable", "hint": "Try: print(len(name))"}
        res = {"ok": True, "output": "hi"}
        m0 = learn_python_gui.coach_response("hint", "name = 'Ada'", step, res, 0)
        self.assertIn("tool from the lesson", m0)
        m1 = learn_python_gui.coach_response("hint", "name = 'Ada'", step, res, 1)
        self.assertIn("len(", m1)
        m2 = learn_python_gui.coach_response("hint", "name = 'Ada'", step, res, 2)
        self.assertIn("Try:", m2)


class CoachAnalysisTests(unittest.TestCase):
    def test_analyze_simple_code(self):
        info = learn_python_gui.analyze_code("name = 'Ada'\nprint(len(name))")
        self.assertFalse(info["blank"])
        self.assertFalse(info["only_comments"])
        self.assertIsNone(info["syntax_line"])
        self.assertIn("print", info["name_calls"])
        self.assertIn("len", info["name_calls"])

    def test_analyze_blank_and_comments(self):
        self.assertTrue(learn_python_gui.analyze_code("").__getitem__("blank"))
        comment_only = learn_python_gui.analyze_code("# plan\n# more notes")
        self.assertTrue(comment_only["only_comments"])

    def test_analyze_syntax_error_line(self):
        info = learn_python_gui.analyze_code("print(1\nprint(2)")
        self.assertIsNotNone(info["syntax_line"])

    def test_analyze_structures(self):
        code = "def total(ns):\n    s = 0\n    for n in ns:\n        s += n\n    return s\ntotal([1,2])"
        info = learn_python_gui.analyze_code(code)
        self.assertIn("total", info["defs"])
        self.assertIn("total", info["name_calls"])
        self.assertTrue(info["has_loop"])
        self.assertTrue(info["has_return"])

    def test_coach_hint_specific_missing_loop(self):
        step = {"instruction": "Loop through the list and print each number"}
        msg = learn_python_gui.coach_hint_specific("print('hi')", step, "Beginner")
        self.assertIn("for loop", msg)

    def test_coach_hint_specific_names_function_never_called(self):
        step = {"instruction": "Build a reusable function"}
        code = "def greet(name):\n    print(name)"
        msg = learn_python_gui.coach_hint_specific(code, step, "Intermediate")
        self.assertIn("greet", msg)
        self.assertIn("never called", msg)

    def test_coach_hint_specific_level_voice(self):
        step = {"instruction": "Print your name"}
        b = learn_python_gui.coach_hint_specific("name = 'Ada'", step, "Beginner")
        a = learn_python_gui.coach_hint_specific("name = 'Ada'", step, "Advanced")
        self.assertIn("Small next step", b)
        self.assertIn("Make it exactly right", a)

    def test_coach_hint_specific_syntax_line(self):
        step = {"instruction": "Print a number"}
        msg = learn_python_gui.coach_hint_specific("x = open('f.txt'", step, "")
        self.assertIn("line 1", msg)


class DraftPersistenceTests(unittest.TestCase):
    def test_default_progress_has_drafts(self):
        p = learn_python_gui.default_progress()
        self.assertEqual(p["draft_code"], {})

    def test_ensure_progress_adds_drafts(self):
        p = ensure = learn_python_gui.ensure_progress(learn_python_gui.default_progress())
        self.assertIn("draft_code", ensure)

    def test_project_draft_key_is_stable(self):
        self.assertEqual(learn_python_gui.project_draft_key("Beginner", 2),
                         "Beginner_2_project")

    def test_draft_restored_value_matches_saved(self):
        p = learn_python_gui.default_progress()
        p["draft_code"]["Beginner_0_1"] = "print(len(name))"
        self.assertEqual(p["draft_code"]["Beginner_0_1"], "print(len(name))")


class ReviewSchedulingTests(unittest.TestCase):
    def setUp(self):
        self.p = learn_python_gui.default_progress()
        self.lessons = {"Beginner": [{"title": "Built-in functions",
                                      "review_question": "Q?", "review_answer": "A",
                                      "key_takeaways": "T"}]}

    def test_schedule_sets_first_due_tomorrow(self):
        learn_python_gui.schedule_review(self.p, "Beginner", 0)
        entry = self.p["reviews"]["Beginner_0"]
        self.assertEqual(entry["interval_idx"], 0)
        expected = (learn_python_gui.date.today() + learn_python_gui.timedelta(days=1)).isoformat()
        self.assertEqual(entry["due"], expected)

    def test_schedule_only_once(self):
        self.assertTrue(learn_python_gui.schedule_review(self.p, "Beginner", 0))
        self.assertFalse(learn_python_gui.schedule_review(self.p, "Beginner", 0))

    def test_newly_scheduled_not_due_today(self):
        learn_python_gui.schedule_review(self.p, "Beginner", 0)
        due = learn_python_gui.due_reviews(self.p, self.lessons)
        self.assertEqual(due, [])

    def test_due_when_past_due_date(self):
        learn_python_gui.schedule_review(self.p, "Beginner", 0)
        self.p["reviews"]["Beginner_0"]["due"] = (learn_python_gui.date.today() - learn_python_gui.timedelta(days=1)).isoformat()
        due = learn_python_gui.due_reviews(self.p, self.lessons)
        self.assertEqual(len(due), 1)
        self.assertEqual(due[0]["question"], "Q?")

    def test_grade_correct_increases_interval(self):
        learn_python_gui.schedule_review(self.p, "Beginner", 0)
        self.p["reviews"]["Beginner_0"]["due"] = (learn_python_gui.date.today() - learn_python_gui.timedelta(days=1)).isoformat()
        learn_python_gui.grade_review(self.p, "Beginner", 0, True)
        entry = self.p["reviews"]["Beginner_0"]
        self.assertEqual(entry["interval_idx"], 1)
        expected = (learn_python_gui.date.today() + learn_python_gui.timedelta(days=2)).isoformat()
        self.assertEqual(entry["due"], expected)

    def test_grade_wrong_resets_interval(self):
        learn_python_gui.schedule_review(self.p, "Beginner", 0)
        self.p["reviews"]["Beginner_0"]["interval_idx"] = 4
        learn_python_gui.grade_review(self.p, "Beginner", 0, False)
        entry = self.p["reviews"]["Beginner_0"]
        self.assertEqual(entry["interval_idx"], 0)
        expected = (learn_python_gui.date.today() + learn_python_gui.timedelta(days=1)).isoformat()
        self.assertEqual(entry["due"], expected)


class UnitAndNewLessonsTests(unittest.TestCase):
    def _sets(self):
        return {
            "Beginner": [
                {"title": "Built-in functions", "unit": "Core tools"},
                {"title": "Python keywords", "unit": "Control flow"},
                {"title": "Conditionals and decisions", "unit": "Control flow"},
            ]
        }

    def test_snapshot_includes_unit(self):
        p = learn_python_gui.default_progress()
        p["level"] = "Beginner"
        snap = learn_python_gui.lesson_progress_snapshot(p, self._sets(), "Beginner")
        self.assertEqual(len(snap), 3)
        self.assertEqual([s["unit"] for s in snap], ["Core tools", "Control flow", "Control flow"])

    def test_evaluate_variables_and_numbers(self):
        ok, _ = learn_python_gui.evaluate_code_attempt(
            "score = 5\nprint(score + 1)", {"title": "Variables and numbers"})
        self.assertTrue(ok)

    def test_evaluate_conditionals(self):
        ok, _ = learn_python_gui.evaluate_code_attempt(
            "if age >= 18:\n    print('Adult')", {"title": "Conditionals and decisions"})
        self.assertTrue(ok)

    def test_skill_labels_have_new_lessons(self):
        for title in ("Variables and numbers", "Conditionals and decisions"):
            self.assertIn(title, learn_python_gui.SKILL_LABELS)

    def test_evaluate_sets_and_tuples(self):
        ok, _ = learn_python_gui.evaluate_code_attempt("s = {1, 2, 3}\nprint(len(s))",
                                                       {"title": "Sets and tuples"})
        self.assertTrue(ok)

    def test_evaluate_nested_loops(self):
        ok, _ = learn_python_gui.evaluate_code_attempt(
            "for r in g:\n    for c in r:\n        print(c)", {"title": "Nested loops and data"})
        self.assertTrue(ok)

    def test_evaluate_exception_handling(self):
        ok, _ = learn_python_gui.evaluate_code_attempt(
            "try:\n    x = int('a')\nexcept ValueError:\n    print('bad')",
            {"title": "Exception handling"})
        self.assertTrue(ok)

    def test_evaluate_json(self):
        ok, _ = learn_python_gui.evaluate_code_attempt(
            "import json\nwith open('f.json') as f:\n    d = json.load(f)", {"title": "JSON files"})
        self.assertTrue(ok)

    def test_evaluate_list_comprehension(self):
        ok, _ = learn_python_gui.evaluate_code_attempt(
            "squares = [n * n for n in range(5)]", {"title": "List comprehensions"})
        self.assertTrue(ok)

    def test_skill_labels_have_all_new_lessons(self):
        for title in ("Sets and tuples", "Nested loops and data", "Exception handling",
                      "JSON files", "List comprehensions"):
            self.assertIn(title, learn_python_gui.SKILL_LABELS)

    def test_unit_progress_empty(self):
        p = learn_python_gui.default_progress()
        p["level"] = "Beginner"
        p["completed_lessons"] = []
        up = learn_python_gui.unit_progress(p, self._sets(), "Beginner")
        self.assertEqual(up, [
            {"unit": "Core tools", "done": 0, "total": 1},
            {"unit": "Control flow", "done": 0, "total": 2},
        ])

    def test_unit_progress_counts_done(self):
        p = learn_python_gui.default_progress()
        p["level"] = "Beginner"
        p["completed_lessons"] = [0, 2]
        up = learn_python_gui.unit_progress(p, self._sets(), "Beginner")
        by = {u["unit"]: u for u in up}
        self.assertEqual(by["Core tools"]["done"], 1)
        self.assertEqual(by["Control flow"]["done"], 1)
        self.assertEqual(by["Control flow"]["total"], 2)


class CoachQuizTests(unittest.TestCase):
    def test_quiz_item_for_known_lesson(self):
        item = learn_python_gui.coach_quiz_item("Built-in functions")
        self.assertIn("len(name)", item["code"])

    def test_quiz_item_fallback(self):
        item = learn_python_gui.coach_quiz_item("Whatever title")
        self.assertIn("sum(nums)", item["code"])

    def test_normalize_comparison(self):
        self.assertEqual(learn_python_gui.normalize_answer("  Hello   World "),
                         learn_python_gui.normalize_answer("hello world"))
        self.assertTrue(learn_python_gui.normalize_answer("3") == learn_python_gui.normalize_output("3\n"))

    def test_predictions_from_live_run(self):
        item = learn_python_gui.coach_quiz_item("Python keywords")
        live = learn_python_gui.run_user_code(item["code"], timeout=3)
        out = (live.get("output") or "").strip()
        # range(3) prints 0,1,2 -> live output "0\n1\n2"
        self.assertTrue(learn_python_gui.check_prediction(item, "0 1 2", out))
        self.assertTrue(learn_python_gui.check_prediction(item, "0\n1\n2", out))
        self.assertFalse(learn_python_gui.check_prediction(item, "0 1", out))

    def test_every_lesson_has_quiz_item(self):
        app_cls = learn_python_gui.LearningPage
        instance = app_cls.__new__(app_cls)
        sets = app_cls._build_lesson_sets(instance)
        for level, lessons in sets.items():
            for lesson in lessons:
                code = learn_python_gui.coach_quiz_item(lesson["title"])["code"]
                live = learn_python_gui.run_user_code(code, timeout=3)
                self.assertTrue(live.get("ok"),
                                f"quiz snippet for '{lesson['title']}' errored: {live.get('error')}")


class GuidedHelpTests(unittest.TestCase):
    def test_questions_have_four_ordered_steps(self):
        questions = learn_python_gui.guided_help_questions()
        self.assertEqual([q["id"] for q in questions], ["goal", "blocker", "help", "source"])

    def test_guess_tool_by_instruction(self):
        self.assertIn("len", learn_python_gui._guess_tool({"instruction": "Use len() to count"}))
        self.assertIn("try", learn_python_gui._guess_tool({"instruction": "catch the error with try"}))

    def test_plan_includes_goal_text(self):
        step = {"instruction": "Print the total.", "hint": "use print(total)"}
        plan = learn_python_gui.guided_help_plan(
            {"goal": "I want to add two numbers", "blocker": 0, "help": 0, "source": 1},
            step, None, "x = 1\nprint(x)", {"ok": True, "output": "1\n"})
        self.assertIn("I want to add two numbers", plan)

    def test_plan_uses_lesson_takeaways_when_requested(self):
        step = {"instruction": "Loop over a list.", "hint": "use a for loop"}
        lesson = {"key_takeaways": "\u2022 A takeaway bullet", "example": "print('x')"}
        plan = learn_python_gui.guided_help_plan(
            {"goal": "loop", "blocker": 1, "help": 1, "source": 0},
            step, lesson, "", {"ok": False, "error": "boom"})
        self.assertIn("A takeaway bullet", plan)

    def test_plan_one_line_hint_uses_step_hint(self):
        step = {"instruction": "Do the thing.", "hint": "Try print(x)"}
        plan = learn_python_gui.guided_help_plan(
            {"goal": "", "blocker": 0, "help": 0, "source": 1}, step, None, "", {})
        self.assertIn("Try print(x)", plan)

    def test_glossary_lists_common_tools(self):
        for key in ("print()", "for loop", "json", "try/except"):
            self.assertIn(key, learn_python_gui._GLOSSARY)


class RegressionTests(unittest.TestCase):
    def test_check_prediction_has_no_dead_coach_body(self):
        src = inspect.getsource(learn_python_gui.check_prediction)
        for marker in ('"stuck"', "coach_diagnose", "_COACH_TIP_HINTS", "Give me a hint"):
            self.assertNotIn(marker, src,
                             f"dead coach_response body leaked back into check_prediction ({marker})")

    def test_guided_plan_all_combos_run_clean(self):
        step = {"instruction": "Print the total.", "hint": "use print(total)", "answer": "total"}
        lesson = {"key_takeaways": "\u2022 Takeaway", "example": "print(1)"}
        for blocker in range(4):
            for help_kind in range(4):
                for source in range(3):
                    plan = learn_python_gui.guided_help_plan(
                        {"goal": "add numbers", "blocker": blocker, "help": help_kind, "source": source},
                        step, lesson, "x = 1\nprint(x)", {"ok": True, "output": "1\n"})
                    self.assertIsInstance(plan, str)
                    self.assertTrue(plan.strip())


class NewUXTests(unittest.TestCase):
    def test_rebuild_fonts_scales_up_then_restores(self):
        learn_python_gui.rebuild_fonts(1.0)
        base = learn_python_gui.FONTS["body"][1]
        learn_python_gui.rebuild_fonts(1.25)
        self.assertGreater(learn_python_gui.FONTS["body"][1], base)
        learn_python_gui.rebuild_fonts(1.0)
        self.assertEqual(learn_python_gui.FONTS["body"][1], base)

    def test_default_progress_has_font_and_help_keys(self):
        dp = learn_python_gui.default_progress()
        self.assertEqual(dp["font_size"], "normal")
        self.assertTrue(dp["show_welcome_help"])
        for key in ("small", "normal", "large"):
            self.assertIn(key, learn_python_gui.FONT_SCALES)

    def test_assess_performance_recommends_stay_when_weak(self):
        p = learn_python_gui.default_progress()
        p["level"] = "Beginner"
        p["completed_lessons"] = [0, 1]
        lesson_sets = {"Beginner": [{"title": "A"}, {"title": "B"}]}
        learn_python_gui.record_attempt(p, "Beginner", 0, False)
        learn_python_gui.record_attempt(p, "Beginner", 0, False)
        learn_python_gui.record_attempt(p, "Beginner", 1, False)
        suggestion, reason, count = learn_python_gui.assess_performance(p, "Beginner", lesson_sets)
        self.assertEqual(suggestion, "stay")
        self.assertTrue(reason)
        self.assertEqual(count, 0)

    def test_assess_performance_up_dead_ends_at_advanced(self):
        p = learn_python_gui.default_progress()
        p["level"] = "Advanced"
        p["completed_lessons"] = [0, 1]
        lesson_sets = {"Advanced": [{"title": "A"}, {"title": "B"}]}
        learn_python_gui.record_attempt(p, "Advanced", 0, True)
        learn_python_gui.record_attempt(p, "Advanced", 1, True)
        suggestion, reason, count = learn_python_gui.assess_performance(p, "Advanced", lesson_sets)
        self.assertIsNone(suggestion)
        self.assertIsNone(reason)


class GuiLessonTests(unittest.TestCase):
    def test_skill_labels_have_gui_lessons(self):
        for title in ("GUIs with tkinter", "Buttons and events", "Entry widgets and forms"):
            self.assertIn(title, learn_python_gui.SKILL_LABELS)

    def test_evaluate_gui_lessons_success(self):
        cases = [
            ("GUIs with tkinter", "import tkinter as tk\nroot = tk.Tk()"),
            ("Buttons and events", "btn = tk.Button(root, text='Go', command=run)"),
            ("Entry widgets and forms", "entry = tk.Entry(root)\nvalue = entry.get()"),
        ]
        for title, code in cases:
            ok, _ = learn_python_gui.evaluate_code_attempt(code, {"title": title})
            self.assertTrue(ok, f"{title} was rejected")

    def test_evaluate_gui_lessons_hints(self):
        ok, msg = learn_python_gui.evaluate_code_attempt("print(1)", {"title": "GUIs with tkinter"})
        self.assertFalse(ok)
        self.assertIn("tk.Tk(", msg)

    def test_glossary_has_gui_tools(self):
        for key in ("tkinter", "mainloop()", "tk.Button", "tk.Entry"):
            self.assertIn(key, learn_python_gui._GLOSSARY)

    def test_guess_tool_gui_instruction(self):
        self.assertIn("Label", learn_python_gui._guess_tool({"instruction": "Create a label"}))
        self.assertIn("loop", learn_python_gui._guess_tool({"instruction": "Call root.mainloop()"}))

    def test_tkinter_import_allowed_in_sandbox(self):
        res = learn_python_gui.run_user_code("import tkinter as tk\nprint(tk.__name__)", timeout=5)
        self.assertTrue(res["ok"], res.get("error"))
        self.assertEqual(res["output"].strip(), "tkinter")
        self.assertEqual(res["blocked"], "")

    def test_gui_window_auto_closes(self):
        res = learn_python_gui.run_user_code(
            "import tkinter as tk\nroot = tk.Tk()\nroot.mainloop()\nprint('closed')", timeout=8)
        self.assertTrue(res["ok"], res.get("error"))
        self.assertIn("closed", res["output"])

    def test_quiz_items_are_window_free(self):
        for title in ("GUIs with tkinter", "Buttons and events", "Entry widgets and forms"):
            code = learn_python_gui.coach_quiz_item(title)["code"]
            self.assertNotIn(".Tk()", code, f"quiz for '{title}' must not open a window")
            res = learn_python_gui.run_user_code(code, timeout=5)
            self.assertTrue(res["ok"], f"{title}: {res.get('error')}")

    def test_explain_error_tcl_error(self):
        msg = learn_python_gui.explain_error("TclError: can't invoke \"pack\" command: application has been destroyed")
        self.assertIn("pack", msg)

    def test_default_font_size_constant_is_normal(self):
        self.assertEqual(learn_python_gui.DEFAULT_FONT_SIZE, "normal")
        self.assertIn(learn_python_gui.DEFAULT_FONT_SIZE, learn_python_gui.FONT_SCALES)
        dp = learn_python_gui.default_progress()
        self.assertEqual(dp["font_size"], learn_python_gui.DEFAULT_FONT_SIZE)

    def test_font_scales_are_ordered_around_normal(self):
        scales = learn_python_gui.FONT_SCALES
        self.assertEqual(scales["normal"], 1.0)
        self.assertLess(scales["small"], scales["normal"])
        self.assertGreater(scales["large"], scales["normal"])

    def test_settings_page_class_exists(self):
        import tkinter as tk
        cls = getattr(learn_python_gui, "SettingsPage", None)
        self.assertIsNotNone(cls)
        self.assertTrue(issubclass(cls, tk.Frame))
        for attr in ("refresh", "_size_card", "_theme_card"):
            self.assertIn(attr, cls.__dict__)

    def test_coach_proactive_escalates_and_stays_solution_free(self):
        step = {"instruction": "Print the value of total", "hint": "use print(total)", "answer": "total"}
        code = "a = 5\nb = 3"
        t2 = learn_python_gui.coach_proactive(code, step, 2)
        t3 = learn_python_gui.coach_proactive(code, step, 3)
        t4 = learn_python_gui.coach_proactive(code, step, 4)
        for msg in (t2, t3, t4):
            self.assertTrue(msg.strip())
            self.assertNotIn("print(total)", msg)
        self.assertNotEqual(t2, t3)
        self.assertNotEqual(t3, t4)

    def test_coach_proactive_blank_code_still_guides(self):
        step = {"instruction": "Print the value of total"}
        msg = learn_python_gui.coach_proactive("", step, 3)
        self.assertTrue(msg)
        self.assertNotIn("print(total)", msg)


class RealWorldDataTests(unittest.TestCase):
    DATA_DIR = learn_python_gui._data_dir()
    if DATA_DIR is None:
        DATA_DIR = Path(learn_python_gui.__file__).resolve().parent / "data"
    RECORDS = {"us_states.json": 50, "elements.json": 20, "planets.json": 8, "movies.json": 10, "weather.json": 10, "books.json": 10}

    def setUp(self):
        self.assertIsNotNone(learn_python_gui._data_dir(),
                             "no data/ folder found next to learn_python_gui.py")

    def test_datasets_exist_and_are_valid_json(self):
        for name in learn_python_gui.DATASET_FILES:
            path = self.DATA_DIR / name
            self.assertTrue(path.is_file(), f"missing {name}")
            data = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(len(data), self.RECORDS[name], name)
            for record in data:
                self.assertIsInstance(record, dict, name)
                self.assertTrue(record, f"empty record in {name}")

    def test_states_dataset_fields(self):
        states = json.loads((self.DATA_DIR / "us_states.json").read_text(encoding="utf-8"))
        for state in states:
            for field in ("name", "abbr", "capital", "statehood_year", "region"):
                self.assertIn(field, state)
        self.assertEqual(len({s["abbr"] for s in states}), 50, "abbreviations not unique")

    def test_elements_dataset_fields(self):
        elements = json.loads((self.DATA_DIR / "elements.json").read_text(encoding="utf-8"))
        numbers = []
        for element in elements:
            for field in ("name", "symbol", "atomic_number", "atomic_mass", "category"):
                self.assertIn(field, element)
            numbers.append(element["atomic_number"])
        self.assertEqual(len(set(numbers)), 20, "atomic numbers not unique")

    def test_planets_dataset_fields(self):
        planets = json.loads((self.DATA_DIR / "planets.json").read_text(encoding="utf-8"))
        for planet in planets:
            for field in ("name", "distance_au", "diameter_km", "moons", "year_length_years"):
                self.assertIn(field, planet)

    def test_sandbox_can_read_bundled_datasets(self):
        codes = {
            "us_states.json": ("import json\nwith open('us_states.json') as f:\n"
                               "    d = json.load(f)\nprint(len(d))"),
            "elements.json": ("import json\nwith open('elements.json') as f:\n"
                              "    d = json.load(f)\nprint(len(d))"),
            "planets.json": ("import json\nwith open('planets.json') as f:\n"
                             "    d = json.load(f)\nprint(len(d))"),
        }
        for name, code in codes.items():
            res = learn_python_gui.run_user_code(code, timeout=5)
            self.assertTrue(res.get("ok"), f"{name}: {res.get('error')}")
            self.assertEqual(res["output"].strip(), str(self.RECORDS[name]))

    def _lessons(self):
        app_cls = learn_python_gui.LearningPage
        instance = app_cls.__new__(app_cls)
        return app_cls._build_lesson_sets(instance)["Advanced"]

    def _data_lesson(self, title):
        found = [l for l in self._lessons() if l["title"] == title]
        self.assertEqual(len(found), 1, title)
        return found[0]

    def test_data_lessons_present_and_checks_accept_real_solutions(self):
        solutions = {
            "Loading real data": [
                "import json\nwith open('us_states.json') as f:\n    states = json.load(f)\nprint(len(states))",
                "import json\nwith open('us_states.json') as f:\n    states = json.load(f)\nfor s in states:\n    print(s['name'], s['capital'])",
            ],
            "Filtering and ranking data": [
                "import json\nwith open('elements.json') as f:\n    data = json.load(f)\nfor e in sorted(data, key=lambda x: x['atomic_mass'])[-3:]:\n    print(e['name'])",
                "import json\nwith open('elements.json') as f:\n    data = json.load(f)\nmetals = [e for e in data if 'metal' in e['category']]\nfor e in metals:\n    print(e['name'])",
            ],
            "Summarizing data": [
                "import json\nwith open('planets.json') as f:\n    data = json.load(f)\nbig = max(data, key=lambda p: p['diameter_km'])\nprint(big['name'])",
                "import json\nwith open('planets.json') as f:\n    data = json.load(f)\nvals = [p['distance_au'] for p in data]\navg = sum(vals) / len(data)\nprint(round(avg, 2))",
            ],
        }
        for title, snippets in solutions.items():
            lesson = self._data_lesson(title)
            ok, _ = learn_python_gui.evaluate_code_attempt(snippets[0], {"title": title})
            self.assertTrue(ok, f"{title} real solution rejected by evaluate_code_attempt")
            practice = [s for s in lesson["steps"] if s["type"] == "practice"]
            # Intensive curriculum adds an extra integration practice before review, so at least len(snippets) practices must exist
            self.assertGreaterEqual(len(practice), len(snippets), title)
            for step, code in zip(practice, snippets):
                self.assertTrue(step["check"](code), f"{title} real solution rejected by a practice step check")
                self.assertFalse(step["check"]("print('hi')"), f"{title} accepts stub code")

    def test_data_lesson_final_projects_accept_real_solutions(self):
        projects = {
            "Loading real data": ("import json\nwith open('us_states.json') as f:\n    states = json.load(f)\n"
                                  "regs = {}\nfor s in states:\n    r = s['region']\n    regs[r] = regs.get(r, 0) + 1\n"
                                  "for r in regs:\n    print(r, regs[r])"),
            "Filtering and ranking data": ("import json\nwith open('elements.json') as f:\n    data = json.load(f)\n"
                                           "light = min(data, key=lambda e: e['atomic_mass'])\n"
                                           "heavy = max(data, key=lambda e: e['atomic_mass'])\n"
                                           "print(light['name'], heavy['name'])"),
            "Summarizing data": ("import json\nwith open('planets.json') as f:\n    data = json.load(f)\n"
                                 "big = max(data, key=lambda p: p['diameter_km'])\n"
                                 "avg = sum(p['diameter_km'] for p in data) / len(data)\n"
                                 "moons = max(data, key=lambda p: p['moons'])\n"
                                 "print(big['name'], round(avg, 2), moons['name'])"),
        }
        for title, code in projects.items():
            proj = self._data_lesson(title)["final_project"]
            ok, _ = proj["check"](code)
            self.assertTrue(ok, f"{title} real project rejected")
            self.assertFalse(proj["check"]("print('hi')")[0], f"{title} project accepts stub")

    def test_data_lesson_coach_glossary_and_quiz(self):
        for title in ("Loading real data", "Filtering and ranking data", "Summarizing data"):
            self.assertIn(title, learn_python_gui.SKILL_LABELS)
            self.assertIn(title, learn_python_gui._COACH_QUIZ_BANK)
            item = learn_python_gui.coach_quiz_item(title)
            res = learn_python_gui.run_user_code(item["code"], timeout=5)
            self.assertTrue(res.get("ok"), f"{title}: {res.get('error')}")

    def test_glossary_has_data_tools(self):
        for key in ("json.load()", "sorted()", "min()/max()", "sum()"):
            self.assertIn(key, learn_python_gui._GLOSSARY)

    def test_guess_tool_data_instruction(self):
        self.assertIn("sorted", learn_python_gui._guess_tool(
            {"instruction": "print the three heaviest using sorted()"}))
        self.assertIn("sum", learn_python_gui._guess_tool(
            {"instruction": "print the average distance"}))

    def test_required_tools_detects_data_tools(self):
        self.assertIn("load", learn_python_gui._required_tools("load the file with json.load"))
        self.assertIn("sorted", learn_python_gui._required_tools("sort the data"))
        self.assertIn("max", learn_python_gui._required_tools("largest diameter"))
        self.assertIn("min", learn_python_gui._required_tools("lightest element"))
        self.assertIn("average", learn_python_gui._required_tools("average distance"))
        self.assertTrue(learn_python_gui._has_tool(
            learn_python_gui.analyze_code("data = json.load(f)\nprint(max(data))"),
            "data = json.load(f)\nprint(max(data))", "max"))
        self.assertTrue(learn_python_gui._has_tool(
            learn_python_gui.analyze_code("ranked = sorted(data, key=lambda e: e['atomic_mass'])"),
            "ranked = sorted(data, key=lambda e: e['atomic_mass'])", "sorted"))


class DailyChallengeTests(unittest.TestCase):
    """Determinism, correctness, XP awards, and streak logic for the daily challenge."""

    def test_spec_deterministic_and_valid(self):
        today = date(2026, 7, 21)
        a = learn_python_gui.daily_challenge_spec(today=today)
        b = learn_python_gui.daily_challenge_spec(today=today)
        self.assertIsNotNone(a)
        self.assertEqual(a, b)
        self.assertGreaterEqual(len(a["expected_lines"]), 1)

    def test_spec_rotates_across_dates(self):
        seen_ids = set()
        base = date(2026, 1, 1)
        for i in range(40):
            spec = learn_python_gui.daily_challenge_spec(today=base + timedelta(days=i))
            seen_ids.add(spec["id"])
        self.assertGreaterEqual(len(seen_ids), 5)

    def test_expected_lines_match_datasets(self):
        for offset in range(8):
            spec = learn_python_gui.daily_challenge_spec(today=date(2026, 1, 1) + timedelta(days=offset))
            with self.subTest(spec_id=spec["id"]):
                self.assertGreater(len(spec["expected_lines"]), 0)
                self.assertTrue(
                    learn_python_gui.challenge_matches_output(
                        "\n".join(spec["expected_lines"]), spec
                    )
                )

    def test_grade_challenge_rejects_wrong_output(self):
        spec = learn_python_gui.daily_challenge_spec(today=date(2026, 7, 21))
        code = "print('Venus')"
        self.assertFalse(learn_python_gui.challenge_matches_output(code, spec))

    def test_grade_challenge_accepts_correct_output(self):
        spec = learn_python_gui.daily_challenge_spec(today=date(2026, 7, 21))
        code = "import json\nwith open('" + spec["dataset"] + "') as f:\n    data = json.load(f)\n"
        if spec["id"] == "oldest_states":
            code += "first = sorted(data, key=lambda s: (s['statehood_year'], s['name']))[:5]\nfor s in first:\n    print(s['name'])"
        elif spec["id"] == "heaviest_element":
            code += "heavy = max(data, key=lambda e: e['atomic_mass'])\nprint(heavy['name'], heavy['atomic_mass'])"
        elif spec["id"] == "noble_gases":
            code += "for e in data:\n    if e['category'] == 'noble gas':\n        print(e['symbol'])"
        elif spec["id"] == "biggest_planet":
            code += "big = max(data, key=lambda p: p['diameter_km'])\nprint(big['name'])"
        elif spec["id"] == "average_distance":
            code += "print(round(sum(p['distance_au'] for p in data) / len(data), 2))"
        elif spec["id"] == "longest_years":
            code += "top = sorted(data, key=lambda p: p['year_length_years'], reverse=True)[:3]\nfor p in top:\n    print(p['name'])"
        elif spec["id"] == "heavy_count":
            code += "print(sum(1 for e in data if e['atomic_mass'] > 24))"
        elif spec["id"] == "region_census":
            code += "counts = {}\nfor s in data:\n    r = s['region']\n    counts[r] = counts.get(r, 0) + 1\nfor r in counts:\n    print(r + ': ' + str(counts[r]))"
        res = learn_python_gui.run_user_code(code, timeout=4)
        self.assertTrue(res.get("ok"), f"code error: {res.get('error')}")
        self.assertTrue(learn_python_gui.challenge_matches_output(res.get("output") or "", spec))

    def test_is_daily_done(self):
        today = date(2026, 8, 15)
        p = learn_python_gui.default_progress()
        self.assertFalse(learn_python_gui.is_daily_done(p, today=today))
        learn_python_gui.record_daily_solve(p, today=today)
        self.assertTrue(learn_python_gui.is_daily_done(p, today=today))

    def test_record_daily_solve_awards_xp_once(self):
        today = date(2026, 8, 15)
        p = learn_python_gui.default_progress()
        first = learn_python_gui.record_daily_solve(p, today=today)
        xp_after = p["xp"]
        second = learn_python_gui.record_daily_solve(p, today=today)
        self.assertTrue(first)
        self.assertFalse(second)
        self.assertEqual(p["xp"], xp_after)
        self.assertIn("2026-08-15", p["daily_challenge"]["solved_dates"])

    def test_daily_streak_multi_day(self):
        p = learn_python_gui.default_progress()
        today = date(2026, 8, 15)
        learn_python_gui.record_daily_solve(p, today=today)
        learn_python_gui.record_daily_solve(p, today=today - timedelta(days=1))
        learn_python_gui.record_daily_solve(p, today=today - timedelta(days=2))
        self.assertEqual(learn_python_gui.daily_challenge_streak(p), 3)

    def test_daily_streak_breaks_on_gap(self):
        p = learn_python_gui.default_progress()
        today = date(2026, 8, 15)
        learn_python_gui.record_daily_solve(p, today=today)
        learn_python_gui.record_daily_solve(p, today=today - timedelta(days=1))
        learn_python_gui.record_daily_solve(p, today=today - timedelta(days=3))
        self.assertEqual(learn_python_gui.daily_challenge_streak(p), 2)

    def test_page_class_has_refresh(self):
        self.assertTrue(hasattr(learn_python_gui.DailyChallengePage, "refresh"))


if __name__ == "__main__":
    unittest.main()
