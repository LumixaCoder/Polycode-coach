"""Python lessons - thin wrapper so languages/python is the canonical import.

This re-exports the existing lesson_data.build_lesson_sets() so the
current 36 Python lessons keep working without duplication. Future
Python edits should happen in lesson_data.py or be moved here.
"""

from lesson_data import build_lesson_sets  # re-export

__all__ = ["build_lesson_sets"]
