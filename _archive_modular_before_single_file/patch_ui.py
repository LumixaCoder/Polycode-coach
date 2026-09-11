import pathlib

def add_imports(path, imports):
    p = pathlib.Path(path)
    text = p.read_text(encoding="utf-8")
    # Find first line after docstring+initial imports, insert imports there
    # Simplest: replace header that ends with blank line after initial imports
    # We'll look for first class/def and insert imports before it
    # Check if imports already present
    missing = []
    for imp in imports:
        if imp.split()[-1] not in text and imp not in text:
            missing.append(imp)
    if not missing:
        print(f"no missing for {path}")
        return
    # Insert after the initial header imports block (after first blank line after imports)
    # Find position after header docstring and imports
    lines = text.splitlines()
    # Find last import line index
    last_import_idx = -1
    for i, line in enumerate(lines):
        if line.strip().startswith("import ") or line.strip().startswith("from "):
            last_import_idx = i
    if last_import_idx >= 0:
        # insert after last_import_idx
        insert_at = last_import_idx + 1
        new_lines = lines[:insert_at] + [""] + missing + [""] + lines[insert_at:]
        new_text = "\n".join(new_lines)
        p.write_text(new_text, encoding="utf-8")
        print(f"patched {path} with {len(missing)} imports")
    else:
        # no imports yet, insert after docstring
        # find end of docstring
        # simple: after first triple quote closing
        p.write_text(text.replace('"""', '"""\n' + "\n".join(missing), 1), encoding="utf-8")
        print(f"patched {path} fallback")

# Patch widgets
add_imports("app/ui/widgets.py", [
    "from app.config import FONTS, SP",
    "from app.coach import check_prediction, coach_quiz_item, coach_response, guided_help_plan, guided_help_questions",
    "from app.languages import current_language",
    "from app.progress import save_progress",
    "from app.projects import step_key",
    "from app.execution.utils import run_code_for_language",
    "from app.gamification import award_xp",
    "from app.progress import _get_completed_for_level",
])

# Patch app
add_imports("app/ui/app.py", [
    "from app.config import DEFAULT_FONT_SIZE, FONTS, FONT_SCALES, LANGUAGE_META, SP, SUPPORTED_LANGUAGES, THEMES, rebuild_fonts",
    "from app.gamification import _DIFFICULTY_COLOR, _DIFFICULTY_LABEL, award_xp, badge_by_id, difficulty_stars, newly_awarded_badges",
    "from app.languages import _ensure_language_states, _load_language_state, _save_current_language_state, build_lesson_sets, current_language, get_lesson_sets_for_language",
    "from app.progress import AUTOSAVE_INTERVAL_MS, PROGRESS_FILE, _HOT_RELOAD_POLL_MS, _auto_complete_levels_up_to, _dev_watched_paths, _enable_dpi_awareness, _is_frozen, _maybe_spawn_background_watcher, _snapshot_mtimes, default_progress, ensure_progress, load_progress, save_progress, update_streak",
    "from app.ui.widgets import SidebarFrame, confetti_burst, show_toast, style_button",
    "from app.ui.pages.language_selection import LanguageSelectionPage",
    "from app.ui.pages.welcome import WelcomePage",
    "from app.ui.pages.survey import SurveyPage",
    "from app.ui.pages.result import ResultPage",
    "from app.ui.pages.progress import ProgressPage",
    "from app.ui.pages.review import ReviewQueuePage",
    "from app.ui.pages.skilltree import SkillTreePage",
    "from app.ui.pages.daily import DailyChallengePage",
    "from app.ui.pages.learning import LearningPage",
    "from app.ui.pages.badges import BadgesPage",
    "from app.ui.pages.sandbox import SandboxPage",
    "from app.ui.pages.settings import SettingsPage",
    "from app.ui.pages.planning import PlanningGuidePage",
])

# Patch learning
add_imports("app/ui/pages/learning.py", [
    "from app.config import FONTS, SP, SUPPORTED_LANGUAGES",
    "from app.coach import coach_diagnose, coach_hint_specific, coach_proactive",
    "from app.evaluation import assess_performance, record_attempt, record_project_pass",
    "from app.execution.utils import run_code_for_language",
    "from app.execution.python_sandbox import format_trace_steps",
    "from app.gamification import award_xp",
    "from app.languages import build_lesson_sets, current_language, get_lesson_sets_for_language",
    "from app.progress import save_progress, update_streak",
    "from app.projects import GUIDANCE_LEVEL_META, GUIDANCE_LOCKED, _derive_hint_levels, _derive_milestones_condensed, _derive_required_concepts, _derive_requirements, _ensure_project_variants, attempt_key, enrich_project_with_guidance, get_active_project_variant, get_project_guidance_level, get_project_variant_index, project_draft_key, project_hint_key, rotate_project_variant, set_project_guidance_level, step_key",
    "from app.reviews import due_reviews, schedule_review",
    "from app.ui.widgets import CoachPanel, RoundedCard, SyntaxEditor, add_divider, highlight_syntax, show_toast, style_button",
])

# Patch other pages - add minimal safe imports
add_imports("app/ui/pages/language_selection.py", [
    "from app.config import FONTS, LANGUAGE_META, SP, SUPPORTED_LANGUAGES",
    "from app.languages import get_lesson_sets_for_language",
    "from app.ui.widgets import style_button",
])
add_imports("app/ui/pages/welcome.py", [
    "from app.config import FONTS, LANGUAGE_META, SP, SUPPORTED_LANGUAGES",
    "from app.gamification import _count_lessons",
    "from app.languages import current_language",
    "from app.ui.widgets import add_divider, show_toast, style_button",
])
add_imports("app/ui/pages/survey.py", [
    "from app.config import FONTS, LANGUAGE_META, SP, SUPPORTED_LANGUAGES",
    "from app.languages import current_language",
    "from app.ui.widgets import style_button",
])
add_imports("app/ui/pages/result.py", [
    "from app.config import FONTS, SP",
    "from app.languages import current_language",
    "from app.ui.widgets import style_button",
])
add_imports("app/ui/pages/progress.py", [
    "from app.config import FONTS, SP",
    "from app.gamification import daily_xp_series",
    "from app.reviews import due_reviews",
    "from app.skills import adaptive_path, lesson_progress_snapshot, lesson_strength_desc, level_roadmap_stats, skill_checklist, unit_progress",
    "from app.ui.widgets import RoundedCard, RoundedProgress, draw_xp_chart, show_toast, style_button",
])
add_imports("app/ui/pages/badges.py", [
    "from app.config import FONTS, SP",
    "from app.gamification import BADGES, _DIFFICULTY_COLOR, _DIFFICULTY_LABEL, awarded_badge_ids, difficulty_stars",
    "from app.ui.widgets import RoundedCard, RoundedProgress, style_button",
])
add_imports("app/ui/pages/sandbox.py", [
    "from app.config import FONTS, LANGUAGE_META, SP, SUPPORTED_LANGUAGES",
    "from app.execution.utils import run_code_for_language",
    "from app.languages import current_language",
    "from app.progress import save_progress",
    "from app.ui.widgets import SyntaxEditor, show_toast, style_button",
])
add_imports("app/ui/pages/review.py", [
    "from app.config import FONTS, SP",
    "from app.gamification import award_xp",
    "from app.progress import save_progress",
    "from app.reviews import due_reviews, grade_review",
    "from app.ui.widgets import show_toast, style_button",
])
add_imports("app/ui/pages/skilltree.py", [
    "from app.config import DEFAULT_FONT_SIZE, FONTS, FONT_SCALES, LANGUAGE_META, SP, SUPPORTED_LANGUAGES",
    "from app.languages import current_language, get_lesson_sets_for_language",
    "from app.progress import _get_completed_for_level",
    "from app.ui.widgets import style_button",
])
add_imports("app/ui/pages/daily.py", [
    "from app.config import FONTS, SP",
    "from app.challenges.daily import challenge_matches_output, daily_challenge_spec, daily_challenge_streak, format_countdown, is_daily_done, record_daily_solve, seconds_until_midnight",
    "from app.challenges.datasets import DAILY_CHALLENGE_XP",
    "from app.coach import coach_diagnose, coach_hint_specific, coach_proactive",
    "from app.execution.utils import run_code_for_language",
    "from app.languages import current_language",
    "from app.progress import save_progress",
    "from app.ui.widgets import CoachPanel, SyntaxEditor, add_divider, show_toast, style_button",
])
add_imports("app/ui/pages/settings.py", [
    "from app.config import DEFAULT_FONT_SIZE, FONTS, LANGUAGE_META, SP, SUPPORTED_LANGUAGES, THEMES",
    "from app.languages import current_language",
    "from app.progress import save_progress",
    "from app.ui.widgets import RoundedCard, RoundedProgress, show_toast, style_button",
])
add_imports("app/ui/pages/planning.py", [
    "from app.config import FONTS, SP",
    "from app.languages import get_lesson_sets_for_language",
    "from app.ui.widgets import RoundedCard, style_button",
])

print("ui patches done")
