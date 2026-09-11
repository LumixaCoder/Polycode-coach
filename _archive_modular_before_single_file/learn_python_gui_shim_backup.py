"""Shim that preserves `import learn_python_gui` while delegating to modular `app/` package.

This file replaces the original 11k-line monolith. All real code lives in `app/`.
The shim re-exports every public name so `tests/test_learning_progress.py` and
`build.py` keep working without changes, and `python learn_python_gui.py`
still launches the GUI via `app.ui.app.PythonLearnerApp`.

Why a shim instead of deleting the file?
- `PyInstaller` spec and `tests` import `learn_python_gui` by name.
- Keeping the filename avoids config churn.
- Debugging is now `app/<area>.py:line` instead of `learn_python_gui.py:9384`.

Use `learn_python_gui.py.orig` if you ever need the pre-split monolith.
"""
import sys
import importlib
from pathlib import Path
from datetime import date, datetime, timedelta
import tkinter as tk
