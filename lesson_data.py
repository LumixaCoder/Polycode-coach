"""Backward compatibility shim - canonical Python lessons now live in languages/python/lessons.py.

Do not edit lessons here. Edit languages/python/lessons.py instead.
This file re-exports build_lesson_sets() so older imports (tests, fallback)
keep working.
"""

from languages.python.lessons import build_lesson_sets

__all__ = ["build_lesson_sets"]
