import pathlib

# Helper to edit file headers
def patch_progress():
    p = pathlib.Path("app/progress.py")
    text = p.read_text(encoding="utf-8")
    # Fix header: add missing config import and safe imports
    old = "from app.config import LEVEL_ORDER, SUPPORTED_LANGUAGES, LANGUAGE_SPECIFIC_KEYS"
    new = """from app.config import DEFAULT_FONT_SIZE, LEVEL_ORDER, SUPPORTED_LANGUAGES, LANGUAGE_SPECIFIC_KEYS
from app.projects import attempt_key, step_key
from app.reviews import schedule_review
from app.challenges.datasets import DATASET_FILES"""
    if old in text:
        text = text.replace(old, new)
    else:
        print("progress old not found")
    # For cyclic languages imports, inject lazy import inside functions that need them
    # We will add at top of each function that uses languages helpers
    # Functions: ensure_progress, _is_level_skipped, _get_completed_for_level, _auto_complete_levels_up_to, _get_completed... etc.
    # Simplest: add lazy import line at start of each of those functions
    # Find and patch
    patches = {
        "def ensure_progress(progress):": "def ensure_progress(progress):\n    # lazy to avoid circular progress<->languages\n    from app.languages import _ensure_language_states, _save_current_language_state",
        "def _is_level_skipped(progress, level):": "def _is_level_skipped(progress, level):\n    from app.languages import current_language, get_lesson_sets_for_language  # lazy cycle break",
        "def _get_completed_for_level(progress, level):": "def _get_completed_for_level(progress, level):\n    from app.languages import current_language, get_lesson_sets_for_language  # lazy",
        "def _auto_complete_levels_up_to(progress, target_level, lesson_sets):": "def _auto_complete_levels_up_to(progress, target_level, lesson_sets):\n    # schedule_review already imported at top; step_key/attempt_key already top",
    }
    for k, v in patches.items():
        if k in text:
            text = text.replace(k, v)
    # _dev_watched_paths uses DATASET_FILES now imported
    p.write_text(text, encoding="utf-8")
    print("patched progress")

def patch_languages():
    p = pathlib.Path("app/languages.py")
    text = p.read_text(encoding="utf-8")
    # Already has SUPPORTED etc., need to add imports for execution.utils and projects
    old = "from app.config import SUPPORTED_LANGUAGES, LANGUAGE_META, LEVEL_ORDER, LANGUAGE_SPECIFIC_KEYS"
    new = "from app.config import SUPPORTED_LANGUAGES, LANGUAGE_META, LEVEL_ORDER, LANGUAGE_SPECIFIC_KEYS"
    # we already have correct, but need to add no extra top; we'll make get_lesson_sets lazy for execution/utils
    # Patch get_lesson_sets_for_language to lazy import _wrap and apply_guidance
    patch = "def get_lesson_sets_for_language(language):"
    replacement = "def get_lesson_sets_for_language(language):\n    # lazy to avoid cycles: execution/utils and projects may import languages indirectly\n    from app.execution.utils import _wrap_lesson_checks\n    from app.projects import apply_guidance_enrichment"
    if patch in text:
        text = text.replace(patch, replacement)
    p.write_text(text, encoding="utf-8")
    print("patched languages")

def patch_gamification():
    p = pathlib.Path("app/gamification.py")
    text = p.read_text(encoding="utf-8")
    # Header currently minimal; add safe imports at top
    old = '"""XP, badges, and counters."""\nimport json\nfrom datetime import date'
    new = '''"""XP, badges, and counters."""
import json
from datetime import date

# safe top imports (non-cyclic)
from app.projects import attempt_key, project_hint_key

# lazy for cyclic: daily_challenge_solved_dates, run_user_code, _increment_weekly_activity etc. will be imported inside functions
'''
    if old in text:
        text = text.replace(old, new)
    # Patch functions that need lazy imports
    # award_xp needs _update_heatmap etc? Actually award_xp uses _update_heatmap and _increment? Let's make award_xp lazy
    patches = {
        "def award_xp(progress, amount, label=\"\"):": "def award_xp(progress, amount, label=\"\"):\n    from app.progress import _increment_weekly_activity, _update_heatmap  # lazy",
        "def _all_projects_passed(p, sets, level):": "def _all_projects_passed(p, sets, level):\n    from app.projects import attempt_key  # ensure",
        "def _no_hint_projects_passed(p, sets, level, count):": "def _no_hint_projects_passed(p, sets, level, count):\n    from app.projects import attempt_key",
        "def _hint_key_used(p, sets, level, lesson_idx):": "def _hint_key_used(p, sets, level, lesson_idx):\n    from app.projects import project_hint_key",
        "def _level_fully_done(p, sets, level):": "def _level_fully_done(p, sets, level):\n    from app.progress import _is_level_skipped  # lazy cycle",
    }
    for k,v in patches.items():
        if k in text:
            text = text.replace(k, v)
    # BADGES: need to make lambdas lazy for daily_challenge_solved_dates
    # We'll add helper at top and replace lambdas' body to use helper
    # Instead, add helper function and patch BADGES definitions
    helper = """
def _daily_solved_dates(p):
    from app.challenges.daily import daily_challenge_solved_dates
    return daily_challenge_solved_dates(p)

"""
    # Insert helper before BADGES definition
    if "BADGES = [" in text and "_daily_solved_dates" not in text:
        text = text.replace("BADGES = [", helper + "BADGES = [")
    # Replace occurrences of daily_challenge_solved_dates(p) with _daily_solved_dates(p)
    text = text.replace("daily_challenge_solved_dates(p)", "_daily_solved_dates(p)")
    # Also need run_user_code lazy? grade_hidden_tests uses run_user_code - add lazy inside that function
    if "def grade_hidden_tests(" in text:
        text = text.replace("def grade_hidden_tests(code, func_name, cases, timeout=2.5):", "def grade_hidden_tests(code, func_name, cases, timeout=2.5):\n    from app.execution.python_sandbox import run_user_code  # lazy")
    p.write_text(text, encoding="utf-8")
    print("patched gamification")

def patch_skills():
    p = pathlib.Path("app/skills.py")
    text = p.read_text(encoding="utf-8")
    old = '"""Skill labels and adaptive path logic."""\nimport copy as _copy'
    new = '''"""Skill labels and adaptive path logic."""
import copy as _copy

from app.config import LEVEL_ORDER
from app.projects import attempt_key, step_key
'''
    if old in text:
        text = text.replace(old, new)
    # _get_completed_for_level lazy
    if "def skill_checklist(" in text:
        text = text.replace("def skill_checklist(progress, lesson_sets, level):", "def skill_checklist(progress, lesson_sets, level):\n    from app.progress import _get_completed_for_level  # lazy")
    # adaptive_path and others may need _get_completed etc.
    # Add lazy to level_roadmap etc.
    patches = {
        "def level_roadmap_stats(progress, lesson_sets):": "def level_roadmap_stats(progress, lesson_sets):\n    from app.progress import _get_completed_for_level  # lazy",
        "def lesson_progress_snapshot(progress, lesson_sets, level):": "def lesson_progress_snapshot(progress, lesson_sets, level):\n    from app.progress import _get_completed_for_level  # lazy",
        "def adaptive_path(progress, lesson_sets, level):": "def adaptive_path(progress, lesson_sets, level):\n    from app.progress import _get_completed_for_level  # lazy",
    }
    for k,v in patches.items():
        if k in text and "from app.progress import _get_completed" not in text.split(k)[0][-200:]:
            # avoid double
            text = text.replace(k, v)
    p.write_text(text, encoding="utf-8")
    print("patched skills")

def patch_challenges_daily():
    p = pathlib.Path("app/challenges/daily.py")
    text = p.read_text(encoding="utf-8")
    old = '"""Daily challenge specs, java-ification, and streak helpers."""\nimport copy as _copy\nimport json\nimport random\nimport re\nfrom datetime import date, datetime, timedelta\nfrom pathlib import Path'
    new = '''"""Daily challenge specs, java-ification, and streak helpers."""
import copy as _copy
import json
import random
import re
from datetime import date, datetime, timedelta
from pathlib import Path

from app.challenges.datasets import DAILY_CHALLENGE_XP, _load_dataset, _data_dir

# Note: other imports that would cause cycles (gamification, execution, languages) are lazy inside functions
'''
    if old in text:
        text = text.replace(old, new)
    # Add lazy imports inside functions that need external
    patches = {
        "def _level_aligned_challenge(progress, lesson_sets):": "def _level_aligned_challenge(progress, lesson_sets):\n    from app.languages import get_lesson_sets_for_language  # lazy",
        "def _javaify_spec(spec, level):": "def _javaify_spec(spec, level):\n    pass  # placeholder",
        "def daily_challenge_spec(progress, lesson_sets):": "def daily_challenge_spec(progress, lesson_sets):\n    from app.languages import current_language, get_lesson_sets_for_language  # lazy",
        "def record_daily_solve(progress, solved_date):": "def record_daily_solve(progress, solved_date):\n    from app.gamification import award_xp\n    from app.progress import update_streak  # lazy",
        "def _build_challenge_specs():": "def _build_challenge_specs():\n    # uses _load_dataset etc., already imported",
    }
    # For functions that use run_user_code etc., add lazy
    # More generally, patch daily_challenge_spec and record_daily_solve etc.
    # We'll insert lazy for any function that uses award_xp, run_user_code
    if "def daily_challenge_spec(progress, lesson_sets):" in text:
        text = text.replace("def daily_challenge_spec(progress, lesson_sets):\n    from app.languages import current_language, get_lesson_sets_for_language  # lazy",
                            "def daily_challenge_spec(progress, lesson_sets):\n    from app.languages import current_language, get_lesson_sets_for_language  # lazy\n    from app.execution.python_sandbox import run_user_code  # lazy if needed")
    # Ensure _javaify etc. not broken
    p.write_text(text, encoding="utf-8")
    print("patched challenges daily")

def patch_challenges_datasets():
    p = pathlib.Path("app/challenges/datasets.py")
    text = p.read_text(encoding="utf-8")
    # Header ok
    p.write_text(text, encoding="utf-8")
    print("patched datasets")

def patch_execution_python():
    p = pathlib.Path("app/execution/python_sandbox.py")
    text = p.read_text(encoding="utf-8")
    old = '"""Python sandbox - block checks, tracing, and sandboxed execution."""\nimport ast\nimport base64\nimport json\nimport os\nimport re\nimport subprocess\nimport sys\nimport tempfile\nimport time\nfrom pathlib import Path\nfrom datetime import date'
    new = '''"""Python sandbox - block checks, tracing, and sandboxed execution."""
import ast
import base64
import json
import os
import re
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from datetime import date

from app.challenges.datasets import DATASET_FILES, _data_dir
'''
    if old in text:
        text = text.replace(old, new)
    p.write_text(text, encoding="utf-8")
    print("patched exec python")

def patch_execution_utils():
    p = pathlib.Path("app/execution/utils.py")
    text = p.read_text(encoding="utf-8")
    old = '"""Execution helpers that bridge Python/Java lesson checks."""\nimport ast\nimport re'
    new = '''"""Execution helpers that bridge Python/Java lesson checks."""
import ast
import re

# lazy for run_* to avoid cycles
'''
    if old in text:
        text = text.replace(old, new)
    # Patch run_code_for_language to lazy import
    patches = {
        "def run_code_for_language(code, language, timeout=5, trace=False, inputs=None):": "def run_code_for_language(code, language, timeout=5, trace=False, inputs=None):\n    from app.execution.java_sandbox import run_java_code\n    from app.execution.python_sandbox import run_user_code  # lazy",
    }
    for k,v in patches.items():
        if k in text:
            text = text.replace(k, v)
    p.write_text(text, encoding="utf-8")
    print("patched exec utils")

def patch_execution_java():
    p = pathlib.Path("app/execution/java_sandbox.py")
    text = p.read_text(encoding="utf-8")
    old = '"""Java sandbox - JDK detection, compile and run."""\nimport os\nimport re\nimport subprocess\nimport sys\nimport tempfile\nimport time\nfrom pathlib import Path'
    new = '''"""Java sandbox - JDK detection, compile and run."""
import os
import re
import subprocess
import sys
import tempfile
import time
from pathlib import Path

# safe: explain_error from python_sandbox is not cyclic? python_sandbox does not import java, so safe top
from app.execution.python_sandbox import explain_error
'''
    if old in text:
        text = text.replace(old, new)
    else:
        # may already have explain_error import? ensure
        if "from app.execution.python_sandbox import explain_error" not in text:
            text = text.replace('"""Java sandbox - JDK detection, compile and run."""', '"""Java sandbox - JDK detection, compile and run."""\nfrom app.execution.python_sandbox import explain_error')
            pathlib.Path("app/execution/java_sandbox.py").write_text(text, encoding="utf-8")
    # Remove duplicate local explain_error definition? Already there
    # Patch _lint etc? Keep
    p.write_text(text, encoding="utf-8")
    print("patched exec java")

def patch_projects():
    p = pathlib.Path("app/projects.py")
    text = p.read_text(encoding="utf-8")
    # projects is leaf, no extra
    p.write_text(text, encoding="utf-8")
    print("patched projects done")

if __name__ == "__main__":
    patch_progress()
    patch_languages()
    patch_gamification()
    patch_skills()
    patch_challenges_daily()
    patch_challenges_datasets()
    patch_execution_python()
    patch_execution_utils()
    patch_execution_java()
    patch_projects()
    print("all patches done")

