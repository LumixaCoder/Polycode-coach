import pathlib, ast, textwrap

SRC = pathlib.Path("learn_python_gui.py").read_text(encoding="utf-8")
tree = ast.parse(SRC)
# Get source lines for fallback
lines = SRC.splitlines()

def get_segment(node):
    seg = ast.get_source_segment(SRC, node)
    if seg is None:
        # fallback slice by lineno
        start = node.lineno-1
        end = node.end_lineno if hasattr(node, 'end_lineno') else start+1
        seg = "\n".join(lines[start:end])
    return seg

# Mapping: name -> module path relative to app/
ASSIGN_MAP = {
    "SUPPORTED_LANGUAGES": "app/config.py",
    "LANGUAGE_META": "app/config.py",
    "THEMES": "app/config.py",
    "LEVEL_ORDER": "app/config.py",
    "LANGUAGE_SPECIFIC_KEYS": "app/config.py",
    "_BASE_FONTS": "app/config.py",
    "FONTS": "app/config.py",
    "FONT_SCALES": "app/config.py",
    "DEFAULT_FONT_SIZE": "app/config.py",
    "SP": "app/config.py",
    "PROGRESS_FILE": "app/progress.py",
    "AUTOSAVE_INTERVAL_MS": "app/progress.py",
    "_HOT_RELOAD_POLL_MS": "app/progress.py",
    "BADGES": "app/gamification.py",
    "_DIFFICULTY_LABEL": "app/gamification.py",
    "_DIFFICULTY_COLOR": "app/gamification.py",
    "SKILL_LABELS": "app/skills.py",
    "REVIEW_INTERVALS": "app/reviews.py",
    "GUIDANCE_LOCKED": "app/projects.py",
    "GUIDANCE_LEVEL_META": "app/projects.py",
    "HINT_TIER_TITLES": "app/projects.py",
    "_ALT_CONTEXTS": "app/projects.py",
    "_COACH_TIP_HINTS": "app/coach.py",
    "_REQUIRED_TOOL_TIPS": "app/coach.py",
    "_COACH_QUIZ_BANK": "app/coach.py",
    "_GLOSSARY": "app/coach.py",
    "_ALLOWED_IMPORTS": "app/execution/python_sandbox.py",
    "_GUI_AUTOCLOSE_MS": "app/execution/python_sandbox.py",
    "_TRACE_SENTINEL": "app/execution/python_sandbox.py",
    "_TRACE_MAX_STEPS": "app/execution/python_sandbox.py",
    "_WORKER_SRC": "app/execution/python_sandbox.py",
    "DATASET_FILES": "app/challenges/datasets.py",
    "DAILY_CHALLENGE_XP": "app/challenges/datasets.py",
    "_TOPIC_KEYWORDS": "app/challenges/daily.py",
    "_JAVA_DAILY_STARTERS": "app/challenges/daily.py",
    "_JDK_CACHE": "app/execution/java_sandbox.py",
    "_JAVA_BLOCKED_PATTERNS": "app/execution/java_sandbox.py",
    "_PY_KEYWORDS": "app/ui/widgets.py",
    "_PY_BUILTINS": "app/ui/widgets.py",
    "_JAVA_KEYWORDS": "app/ui/widgets.py",
    "_JAVA_BUILTINS": "app/ui/widgets.py",
    "_STRING_RE": "app/ui/widgets.py",
    "_COMMENT_RE": "app/ui/widgets.py",
    "_JAVA_COMMENT_RE": "app/ui/widgets.py",
    "_NUM_RE": "app/ui/widgets.py",
    "_WORD_RE": "app/ui/widgets.py",
    "_DEF_RE": "app/ui/widgets.py",
    "_JAVA_CLASS_RE": "app/ui/widgets.py",
    "SANDBOX_CATEGORIES": "app/ui/pages/sandbox.py",
    "SANDBOX_PROJECTS": "app/ui/pages/sandbox.py",
    "SANDBOX_PROJECTS_JAVA": "app/ui/pages/sandbox.py",
    # alias build_lesson_sets is actually Assign linking to _legacy
    "build_lesson_sets": "app/languages.py",
}

FUNC_MAP = {
    # config-related funcs
    "rebuild_fonts": "app/config.py",
    # languages
    "get_lesson_sets_for_language": "app/languages.py",
    "current_language": "app/languages.py",
    "_ensure_language_states": "app/languages.py",
    "_save_current_language_state": "app/languages.py",
    "_load_language_state": "app/languages.py",
    "switch_language": "app/languages.py",
    # progress
    "_default_progress_path": "app/progress.py",
    "_enable_dpi_awareness": "app/progress.py",
    "_is_frozen": "app/progress.py",
    "_dev_watched_paths": "app/progress.py",
    "_snapshot_mtimes": "app/progress.py",
    "_maybe_spawn_background_watcher": "app/progress.py",
    "save_progress": "app/progress.py",
    "load_progress": "app/progress.py",
    "default_progress": "app/progress.py",
    "ensure_progress": "app/progress.py",
    "_level_idx": "app/progress.py",
    "_is_level_skipped": "app/progress.py",
    "_auto_complete_levels_up_to": "app/progress.py",
    "_get_completed_for_level": "app/progress.py",
    "update_streak": "app/progress.py",
    "_update_weekly_progress": "app/progress.py",
    "_increment_weekly_activity": "app/progress.py",
    "_update_heatmap": "app/progress.py",
    "_earn_streak_freeze_if_eligible": "app/progress.py",
    # gamification
    "grade_hidden_tests": "app/gamification.py",
    "type_along_check": "app/gamification.py",
    "award_xp": "app/gamification.py",
    "_count_completed_steps": "app/gamification.py",
    "_count_passed_projects": "app/gamification.py",
    "_count_lessons": "app/gamification.py",
    "_count_reviews_done": "app/gamification.py",
    "_all_projects_passed": "app/gamification.py",
    "_no_hint_projects_passed": "app/gamification.py",
    "_hint_key_used": "app/gamification.py",
    "difficulty_stars": "app/gamification.py",
    "_level_fully_done": "app/gamification.py",
    "awarded_badge_ids": "app/gamification.py",
    "newly_awarded_badges": "app/gamification.py",
    "badge_by_id": "app/gamification.py",
    "daily_xp_series": "app/gamification.py",
    # skills
    "level_roadmap_stats": "app/skills.py",
    "unit_progress": "app/skills.py",
    "lesson_progress_snapshot": "app/skills.py",
    "skill_checklist": "app/skills.py",
    "adaptive_path": "app/skills.py",
    "_empty_adaptive": "app/skills.py",
    "lesson_strength_desc": "app/skills.py",
    # reviews
    "review_key": "app/reviews.py",
    "review_schedule": "app/reviews.py",
    "schedule_review": "app/reviews.py",
    "grade_review": "app/reviews.py",
    "due_reviews": "app/reviews.py",
    "due_reviews_count": "app/reviews.py",
    # projects
    "attempt_key": "app/projects.py",
    "step_key": "app/projects.py",
    "project_hint_key": "app/projects.py",
    "project_draft_key": "app/projects.py",
    "project_guidance_key": "app/projects.py",
    "_locked_guidance_for_level": "app/projects.py",
    "get_project_guidance_level": "app/projects.py",
    "set_project_guidance_level": "app/projects.py",
    "_derive_required_concepts": "app/projects.py",
    "_derive_requirements": "app/projects.py",
    "_derive_hint_levels": "app/projects.py",
    "_derive_milestones_condensed": "app/projects.py",
    "enrich_project_with_guidance": "app/projects.py",
    "project_variant_key": "app/projects.py",
    "get_project_variant_index": "app/projects.py",
    "set_project_variant_index": "app/projects.py",
    "rotate_project_variant": "app/projects.py",
    "_make_variant_project": "app/projects.py",
    "_ensure_project_variants": "app/projects.py",
    "get_active_project_variant": "app/projects.py",
    "apply_guidance_enrichment": "app/projects.py",
    # evaluation
    "record_attempt": "app/evaluation.py",
    "record_project_pass": "app/evaluation.py",
    "assess_performance": "app/evaluation.py",
    "evaluate_code_attempt": "app/evaluation.py",
    # coach
    "get_ai_hint": "app/coach.py",
    "analyze_code": "app/coach.py",
    "_level_voice": "app/coach.py",
    "_required_tools": "app/coach.py",
    "_has_tool": "app/coach.py",
    "coach_hint_specific": "app/coach.py",
    "coach_diagnose": "app/coach.py",
    "coach_response": "app/coach.py",
    "coach_proactive": "app/coach.py",
    "coach_quiz_item": "app/coach.py",
    "normalize_answer": "app/coach.py",
    "normalize_output": "app/coach.py",
    "check_prediction": "app/coach.py",
    "guided_help_questions": "app/coach.py",
    "_guess_tool": "app/coach.py",
    "guided_help_plan": "app/coach.py",
    # execution python
    "check_blocked_code": "app/execution/python_sandbox.py",
    "parse_trace_output": "app/execution/python_sandbox.py",
    "_error_line_number": "app/execution/python_sandbox.py",
    "explain_error": "app/execution/python_sandbox.py",
    "format_trace_steps": "app/execution/python_sandbox.py",
    "_sandbox_python": "app/execution/python_sandbox.py",
    # draw_xp_chart is UI but used in progress page - put in widgets
    "draw_xp_chart": "app/ui/widgets.py",
    "_data_dir": "app/challenges/datasets.py",
    "_load_dataset": "app/challenges/datasets.py",
    "_build_challenge_specs": "app/challenges/daily.py",
    "_match_topic": "app/challenges/daily.py",
    "_guess_level": "app/challenges/daily.py",
    "_lesson_position": "app/challenges/daily.py",
    "_pick_area": "app/challenges/daily.py",
    "_level_aligned_challenge": "app/challenges/daily.py",
    "_javaify_spec": "app/challenges/daily.py",
    "daily_challenge_spec": "app/challenges/daily.py",
    "seconds_until_midnight": "app/challenges/daily.py",
    "format_countdown": "app/challenges/daily.py",
    "daily_challenge_reset_seconds": "app/challenges/daily.py",
    "_norm_challenge_lines": "app/challenges/daily.py",
    "challenge_matches_output": "app/challenges/daily.py",
    "grade_challenge_output": "app/challenges/daily.py",
    "daily_challenge_solved_dates": "app/challenges/daily.py",
    "is_daily_done": "app/challenges/daily.py",
    "daily_challenge_streak": "app/challenges/daily.py",
    "record_daily_solve": "app/challenges/daily.py",
    "run_user_code": "app/execution/python_sandbox.py",
    "_is_jdk_available": "app/execution/java_sandbox.py",
    "explain_java_error": "app/execution/java_sandbox.py",
    "_java_blocked_message": "app/execution/java_sandbox.py",
    "_lint_java_when_no_jdk": "app/execution/java_sandbox.py",
    "run_java_code": "app/execution/java_sandbox.py",
    "_strip_for_check": "app/execution/utils.py",
    "_robust_check": "app/execution/utils.py",
    "_wrap_lesson_checks": "app/execution/utils.py",
    "run_code_for_language": "app/execution/utils.py",
    "style_button": "app/ui/widgets.py",
    "add_divider": "app/ui/widgets.py",
    "draw_round_rect": "app/ui/widgets.py",
    "highlight_syntax": "app/ui/widgets.py",
    "_off_str": "app/ui/widgets.py",
    "confetti_burst": "app/ui/widgets.py",
    "show_toast": "app/ui/widgets.py",
    "_difficulty_dots": "app/ui/pages/sandbox.py",
    "_level_index": "app/ui/pages/daily.py",
}

CLASS_MAP = {
    "RoundedCard": "app/ui/widgets.py",
    "RoundedProgress": "app/ui/widgets.py",
    "SyntaxEditor": "app/ui/widgets.py",
    "PythonLearnerApp": "app/ui/app.py",
    "SidebarFrame": "app/ui/widgets.py",  # will move to sidebar later but keep with widgets for now
    "LanguageSelectionPage": "app/ui/pages/language_selection.py",
    "WelcomePage": "app/ui/pages/welcome.py",
    "SurveyPage": "app/ui/pages/survey.py",
    "ResultPage": "app/ui/pages/result.py",
    "ProgressPage": "app/ui/pages/progress.py",
    "BadgesPage": "app/ui/pages/badges.py",
    "SandboxPage": "app/ui/pages/sandbox.py",
    "CoachPanel": "app/ui/widgets.py", # also widget
    "ReviewQueuePage": "app/ui/pages/review.py",
    "SkillTreePage": "app/ui/pages/skilltree.py",
    "DailyChallengePage": "app/ui/pages/daily.py",
    "SettingsPage": "app/ui/pages/settings.py",
    "PlanningGuidePage": "app/ui/pages/planning.py",
    "LearningPage": "app/ui/pages/learning.py",
}

# Collect modules
modules = {}
# Ensure all target modules have entry
for m in set(list(ASSIGN_MAP.values()) + list(FUNC_MAP.values()) + list(CLASS_MAP.values())):
    modules.setdefault(m, [])

# Helper to get name for assign nodes (handle multiple assigns like _WORKER_SRC duplicated)
# For duplicate names, we need to handle second occurrence separately - we'll collect all assigns with same name and put both in same module
# For _WORKER_SRC there are two assigns same name; we'll include both
for node in tree.body:
    if isinstance(node, ast.Assign):
        # get first name
        names = [t.id for t in node.targets if isinstance(t, ast.Name)]
        key = names[0] if names else None
        if key in ASSIGN_MAP:
            target = ASSIGN_MAP[key]
            modules[target].append(node)
        elif key:
            print(f"WARNING unmapped Assign {key} at {node.lineno}")
    elif isinstance(node, ast.FunctionDef):
        key = node.name
        if key in FUNC_MAP:
            modules[FUNC_MAP[key]].append(node)
        else:
            print(f"WARNING unmapped Function {key} at {node.lineno}")
    elif isinstance(node, ast.ClassDef):
        key = node.name
        if key in CLASS_MAP:
            modules[CLASS_MAP[key]].append(node)
        else:
            print(f"WARNING unmapped Class {key} at {node.lineno}")
    elif isinstance(node, (ast.Import, ast.ImportFrom, ast.Expr)):
        # skip top-level imports+docstrings; we'll add per-module headers manually
        pass
    else:
        print(f"WARNING unhandled node {type(node).__name__} at line {getattr(node,'lineno', '?')}")

for mod, nodes in modules.items():
    print(f"{mod:35s} -> {len(nodes)} nodes")

# Check unmapped: we already printed
