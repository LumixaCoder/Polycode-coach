"""Language registry for the Learning Coach.

Each supported language lives in languages/<lang>/lessons.py and
exposes a build_lesson_sets() function with the same shape as
lesson_data.build_lesson_sets().
"""

SUPPORTED_LANGUAGES = ["python", "java"]

LANGUAGE_META = {
    "python": {
        "name": "Python",
        "icon": "\U0001F40D",  # snake
        "color": "#4f46e5",
        "accent": "#6366f1",
        "desc": "Easy to start, great for data, automation and apps",
        "tag": "Beginner-friendly",
        "file_ext": "py",
    },
    "java": {
        "name": "Java",
        "icon": "\u2615",  # coffee
        "color": "#ea580c",
        "accent": "#fb923c",
        "desc": "Object-oriented, strong for apps and enterprise jobs",
        "tag": "Popular for jobs",
        "file_ext": "java",
    },
}


def get_lesson_sets(language):
    """Return {level: [lessons]} for the given language.

    Falls back to Python if the language is unknown so old paths keep working.
    """
    lang = (language or "python").lower()
    if lang == "java":
        from languages.java.lessons import build_lesson_sets as build_java
        return build_java()
    # default / python
    try:
        from languages.python.lessons import build_lesson_sets as build_py
        return build_py()
    except Exception:
        # ultimate fallback to legacy file
        from lesson_data import build_lesson_sets as build_legacy
        return build_legacy()


def language_display(language):
    meta = LANGUAGE_META.get(language or "python", LANGUAGE_META["python"])
    return f"{meta['icon']} {meta['name']}"


def is_valid_language(language):
    return (language or "").lower() in SUPPORTED_LANGUAGES
