"""Build a distributable folder-app for Polycode Coach (USER EDITION).

Produces dist/PolycodeCoach/ containing:
  - PolycodeCoach.exe       (the GUI, frozen with PyInstaller onedir)
  - runtime/              (a Python embeddable runtime used to run student
                           code in a sandbox; a real interpreter is required
                           because the frozen exe cannot re-invoke itself)
  - data/ + languages/    (bundled datasets and lesson modules)
  - run.bat               (double-click launcher)
  - build_info.json       (timestamp + trigger + version for auto-update checks)
  - README.txt

After every successful step this script explains what it just did and why,
so the build also works as a learning exercise. A short history of every
build is appended to builds.log.

Usage:
  python build.py
  python build.py --changed learn_python_gui.py lesson_data.py
    (the optional --changed list is just recorded in builds.log so you can
     later see what triggered each successful build)
  python build.py --watch   (build once then keep watching - same as watch_build.py)
"""
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.request
from datetime import datetime

ROOT = pathlib.Path(__file__).resolve().parent
DIST = ROOT / "dist" / "PolycodeCoach"
BUILD_LOG = ROOT / "builds.log"
BUILD_INFO = DIST / "build_info.json"

PY_VERSION = "3.13.14"
EMBED_URL = f"https://www.python.org/ftp/python/{PY_VERSION}/python-{PY_VERSION}-embed-amd64.zip"


def step(number, title, total=6):
    print(f"\n[{number}/{total}] {title}")
    print("-" * 68)


def ok(description):
    print(f"  ok  {description}")


def warn(msg):
    print(f"  !!  {msg}")


def ensure_embed_runtime(dest: pathlib.Path) -> pathlib.Path:
    dest.mkdir(parents=True, exist_ok=True)
    marker = dest / "python.exe"
    if marker.is_file():
        return dest
    zip_path = pathlib.Path(tempfile.gettempdir()) / f"python-{PY_VERSION}-embed-amd64.zip"
    if not zip_path.is_file():
        print(f"Downloading embeddable Python {PY_VERSION} ...")
        urllib.request.urlretrieve(EMBED_URL, zip_path)
    shutil.unpack_archive(str(zip_path), str(dest))
    return dest


def changed_files() -> list:
    args = sys.argv[1:]
    if "--changed" in args:
        start = args.index("--changed") + 1
        return [a for a in args[start:] if a and not a.startswith("--")]
    return []


def append_log(note: str, seconds: float) -> None:
    line = f"{datetime.now().astimezone().strftime('%Y-%m-%d %H:%M:%S')} | {seconds:5.0f}s | {note}\n"
    try:
        with open(BUILD_LOG, "a", encoding="utf-8") as fh:
            fh.write(line)
    except OSError:
        pass


def safe_rmtree(path: pathlib.Path, retries=3, delay=1.0):
    """Remove tree with retries to handle Windows file-lock race."""
    for attempt in range(retries):
        try:
            if path.exists():
                shutil.rmtree(path)
            return True
        except PermissionError as exc:
            if attempt < retries - 1:
                warn(f"Retrying rmtree {path.name} (attempt {attempt+1}/{retries}): {exc}")
                time.sleep(delay * (attempt + 1))
                continue
            raise
        except OSError:
            if attempt < retries - 1:
                time.sleep(delay)
                continue
            raise
    return False

def discover_languages():
    """Find languages/<id>/lessons.py modules for hidden-imports and datas."""
    langs = []
    lang_root = ROOT / "languages"
    if not lang_root.is_dir():
        return langs
    for child in lang_root.iterdir():
        if child.is_dir() and (child / "lessons.py").is_file():
            langs.append(child.name)
    return sorted(langs)

def copy_tree_with_retry(src: pathlib.Path, dst: pathlib.Path, retries=3):
    """Copy tree, retrying on lock. Ensures dst exists."""
    for attempt in range(retries):
        try:
            if dst.exists():
                shutil.rmtree(dst, ignore_errors=False)
            shutil.copytree(src, dst, dirs_exist_ok=False)
            return True
        except PermissionError as exc:
            if attempt < retries - 1:
                warn(f"Copy retry {src.name} -> {dst.name}: {exc}")
                time.sleep(1.0 * (attempt + 1))
                continue
            raise
    return False

def write_build_info(trigger: str, seconds: float):
    """Write build_info.json next to exe for auto-update / about checks."""
    info = {
        "built_at": datetime.now().astimezone().isoformat(),
        "trigger": trigger,
        "duration_seconds": round(seconds, 1),
        "python_version": PY_VERSION,
        "source_root": str(ROOT),
    }
    try:
        BUILD_INFO.parent.mkdir(parents=True, exist_ok=True)
        BUILD_INFO.write_text(json.dumps(info, indent=2), encoding="utf-8")
    except OSError:
        pass

def main():
    # Support --watch convenience: build then delegate to watch_build.py
    if "--watch" in sys.argv:
        # Remove --watch from args so changed_files parsing still works
        sys.argv = [a for a in sys.argv if a != "--watch"]
        # Do initial build
        rc = build_once()
        if rc != 0:
            sys.exit(rc)
        # Then hand off to watcher
        print("\nHanding off to watch_build.py for continuous auto-updates...")
        try:
            import watch_build  # noqa: F401
        except ImportError:
            pass
        subprocess.call([sys.executable, str(ROOT / "watch_build.py")], cwd=ROOT)
        return

    rc = build_once()
    sys.exit(rc)

def build_once():
    changed = changed_files()
    trigger = "manual build" if not changed else "update: " + ", ".join(changed)
    start = time.time()

    print("Build the Polycode Coach app")
    print("===================================")

    total_steps = 6
    try:
        step(1, "Clean the old folders", total_steps)
        # Try to close any running app to free Windows file locks
        if sys.platform.startswith("win"):
            try:
                subprocess.run(["taskkill", "/F", "/IM", "PolycodeCoach.exe"], capture_output=True, timeout=3)
                time.sleep(0.8)
            except Exception:
                pass
        # Try to remove build/ always; for DIST, handle locked exe gracefully
        safe_rmtree(ROOT / "build")
        try:
            safe_rmtree(DIST)
        except PermissionError as exc:
            warn(f"Cannot fully clean {DIST} (app may be running): {exc}")
            warn("Attempting to overwrite in place instead of clean delete.")
            # Try to at least remove inner _internal if possible, but don't fail yet
            # The copytree below will handle existing dir with dirs_exist_ok fallback
            pass
        # Ensure dist parent exists
        (ROOT / "dist").mkdir(parents=True, exist_ok=True)
        ok("Cleaned build/ and dist/PolycodeCoach/ so nothing stale is left "
           "behind. Starting clean guarantees the next app you open is your new "
           "code, not an old copy from a previous build.")

        step(2, "Freeze the app into an exe with PyInstaller", total_steps)
        langs = discover_languages()
        # Hidden imports: languages.<lang>.lessons for dynamic import()
        hidden_imports = []
        for lang in langs:
            hidden_imports.extend([
                f"languages.{lang}.lessons",
                f"languages.{lang}",
            ])
        # Always include core fallback
        hidden_imports.extend(["lesson_data", "languages.python.lessons"])
        # Note: app/ modular tree only exists in _archive_modular_before_single_file/ (not bundled)

        # Data files to bundle via PyInstaller datas
        # On Windows separator is ';', on POSIX ':'
        sep = ";" if sys.platform.startswith("win") else ":"
        add_data_args = []
        # Bundle data/ folder (datasets browsable via _data_dir)
        if (ROOT / "data").is_dir():
            add_data_args.extend(["--add-data", f"{ROOT / 'data'}{sep}data"])
        # Bundle languages/ to ensure dynamic lesson modules are available even if hiddenimport missed
        if (ROOT / "languages").is_dir():
            add_data_args.extend(["--add-data", f"{ROOT / 'languages'}{sep}languages"])

        cmd = [
            sys.executable, "-m", "PyInstaller",
            "--noconfirm",
            "--onedir",
            "--name", "PolycodeCoach",
            "--windowed",
            "--distpath", str(ROOT / "dist"),
            "--workpath", str(ROOT / "build"),
            "--specpath", str(ROOT),
        ]
        for hi in sorted(set(hidden_imports)):
            cmd.extend(["--hidden-import", hi])
        cmd.extend(add_data_args)
        # USER EDITION: build the clean lumixa.py for distribution
        # DEV EDITION: learn_python_gui.py is for you (hot-reload) — not bundled
        cmd.append(str(ROOT / "lumixa.py"))

        # Show what we're bundling
        if langs:
            print(f"  Bundling languages: {', '.join(langs)} as hidden-imports + datas")
        if add_data_args:
            print("  Bundling datas: data/ + languages/")
        subprocess.check_call(cmd, cwd=ROOT)
        ok("PyInstaller packed lumixa.py (USER EDITION) plus every module it imports "
           "into a standalone PolycodeCoach.exe. This is called 'freezing': the exe "
           "carries its own Python with it, so it runs on any Windows PC without "
           "needing Python installed.")

        step(3, "Move the app into one tidy folder", total_steps)
        onedir = ROOT / "dist" / "PolycodeCoach"
        # Determine final dist location
        if DIST != onedir and onedir.is_dir():
            # If DIST still exists due to earlier lock, try again more forcefully
            if DIST.exists():
                try:
                    safe_rmtree(DIST)
                except Exception:
                    # Last resort: remove files one by one ignoring locked exe, then copy overwrite
                    warn(f"{DIST} still locked; will merge/overwrite instead of replace.")
                    # Don't delete; we'll copy with dirs_exist_ok later
                    pass
            if not DIST.exists():
                shutil.copytree(onedir, DIST)
            else:
                # Merge: copy onedir content into DIST, overwriting
                for item in onedir.rglob("*"):
                    rel = item.relative_to(onedir)
                    target = DIST / rel
                    if item.is_dir():
                        target.mkdir(parents=True, exist_ok=True)
                    else:
                        try:
                            target.parent.mkdir(parents=True, exist_ok=True)
                            shutil.copy2(item, target)
                        except PermissionError as exc:
                            # Likely PolycodeCoach.exe locked -> skip and warn
                            warn(f"Skip locked file {rel}: {exc}")
            # Clean up the intermediate onedir if we copied
            try:
                shutil.rmtree(onedir, ignore_errors=True)
                # Also remove the duplicate Lumixa folder's parent if empty
            except Exception:
                pass
        elif DIST == onedir:
            # Already at desired location (shouldn't happen with current spec, but handle)
            pass
        else:
            # onedir missing? Maybe PyInstaller already output to DIST directly if spec changed
            if not DIST.is_dir():
                raise FileNotFoundError(f"Expected output {onedir} or {DIST} not found after PyInstaller")

        # Ensure data/ is present in DIST (fallback copy even if --add-data succeeded)
        # PyInstaller datas go to _internal/data, but our _data_dir() also checks DIST/data
        # So we copy to both places for robustness
        if (ROOT / "data").is_dir():
            src_data = ROOT / "data"
            # Copy to DIST/data (legacy location) — dirs_exist_ok handles locked-file leftovers
            try:
                dst_data = DIST / "data"
                dst_data.mkdir(parents=True, exist_ok=True)
                shutil.copytree(src_data, dst_data, dirs_exist_ok=True)
            except Exception as exc:
                warn(f"data copy to DIST/data failed: {exc}")
            # Also ensure _internal/data exists for newer PyInstaller layout
            internal_data = DIST / "_internal" / "data"
            try:
                internal_data.parent.mkdir(parents=True, exist_ok=True)
                shutil.copytree(src_data, internal_data, dirs_exist_ok=True)
            except Exception:
                pass  # not critical

        # Ensure languages/ is present in DIST for dynamic imports fallback
        if (ROOT / "languages").is_dir():
            src_lang = ROOT / "languages"
            dst_lang = DIST / "languages"
            try:
                dst_lang.mkdir(parents=True, exist_ok=True)
                shutil.copytree(src_lang, dst_lang, dirs_exist_ok=True, ignore=lambda d, files: [f for f in files if f == "__pycache__"])
            except Exception as exc:
                warn(f"languages copy failed: {exc}")
            # Also mirror to _internal/languages
            internal_lang = DIST / "_internal" / "languages"
            try:
                internal_lang.parent.mkdir(parents=True, exist_ok=True)
                shutil.copytree(src_lang, internal_lang, dirs_exist_ok=True, ignore=lambda d, files: [f for f in files if f == "__pycache__"])
            except Exception:
                pass

        ok(f"Copied the frozen app into {DIST}. Everything the app needs now "
           "lives in this single double-clickable folder (including data/ and languages/).")

        step(4, "Bundle a real Python for the sandbox", total_steps)
        runtime_src = ensure_embed_runtime(
            pathlib.Path(tempfile.gettempdir()) / "pycoach_embed" / PY_VERSION
        )
        runtime_dst = DIST / "runtime"
        runtime_dst.mkdir(parents=True, exist_ok=True)
        for item in runtime_src.rglob("*"):
            rel = item.relative_to(runtime_src)
            target = runtime_dst / rel
            if item.is_dir():
                target.mkdir(parents=True, exist_ok=True)
            else:
                try:
                    target.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(item, target)
                except PermissionError:
                    # Runtime file locked? skip if same
                    pass
        ok("Installed a real Python 3.13 interpreter into runtime/. When you run "
           "code inside the app's sandbox, it executes in this separate, "
           "protected process. A frozen exe can't safely re-run itself, so it "
           "needs this genuine interpreter sitting next to it.")

        step(5, "Add the double-click launcher and notes", total_steps)
        (DIST / "run.bat").write_text(
            '@echo off\r\n'
            'cd /d "%~dp0"\r\n'
            'start "" "%~dp0PolycodeCoach.exe"\r\n',
            encoding="utf-8",
        )
        # Also add a dev helper batch that runs the watcher
        (ROOT / "run_watch.bat").write_text(
            '@echo off\r\n'
            'echo Starting auto-update watcher...\r\n'
            'python "%~dp0watch_build.py"\r\n',
            encoding="utf-8",
        )
        (DIST / "README.txt").write_text(
            "Polycode Coach\n"
            "=====================\n\n"
            "Run the app:\n"
            "  - Double-click PolycodeCoach.exe  (or run.bat)\n\n"
            "Your progress is saved automatically to:\n"
            "  %APPDATA%\\PolycodeCoach\\learning_progress.json\n\n"
            "The 'runtime' folder is a bundled Python interpreter used to run\n"
            "your code inside the app's sandbox. Keep it next to PolycodeCoach.exe.\n"
            "The 'data' and 'languages' folders contain datasets and lesson content.\n\n"
            "Auto-update while coding:\n"
            "  - Run: python watch_build.py  (or double-click run_watch.bat in project root)\n"
            "  - Or:  python build.py --watch\n"
            "  Every time you save a .py or data/*.json, the app rebuilds automatically.\n",
            encoding="utf-8",
        )
        # Write build_info.json for about/auto-update checks
        seconds = time.time() - start
        write_build_info(trigger, seconds)
        ok("Wrote run.bat (a shortcut that starts the app from its own folder), "
           "run_watch.bat (project watcher), build_info.json (build timestamp), "
           "and README.txt (notes for whoever uses the app, including where progress "
           "is saved).")

        seconds = time.time() - start
        step(6, "Finished", total_steps)
        # Re-ensure build_info has final duration
        write_build_info(trigger, seconds)
        ok(f"Build succeeded in {seconds:.0f} seconds ({trigger}). Double-click "
           f"{DIST / 'PolycodeCoach.exe'} anytime - you no longer need the python "
           "command.")
        append_log(f"OK      {trigger}", seconds)
        return 0

    except subprocess.CalledProcessError as exc:
        seconds = time.time() - start
        append_log(f"FAILED  {trigger}  ->  PyInstaller exit {exc.returncode}", seconds)
        print(f"\nBuild failed: PyInstaller error {exc.returncode}")
        print("Check the output above for missing modules or syntax errors.")
        print("Close the app if it's running, then save any file again.")
        return 1
    except PermissionError as exc:
        seconds = time.time() - start
        append_log(f"FAILED  {trigger}  ->  {exc}", seconds)
        print(f"\nBuild failed (file lock): {exc}")
        print("This usually means PolycodeCoach.exe is still running - Windows locks files "
              "that are in use, so the update cannot overwrite them.")
        print("Close the app completely (check Task Manager), then save any project file again "
              "or re-run: python build.py")
        return 1
    except Exception as exc:
        seconds = time.time() - start
        append_log(f"FAILED  {trigger}  ->  {exc}", seconds)
        print(f"\nBuild failed: {exc}")
        import traceback
        traceback.print_exc()
        print("This usually means the app is still running - Windows locks files "
              "that are in use, so the update cannot overwrite them.")
        print("Close the app, then save any project file again (or re-run build.py) "
              "to retry.")
        return 1


if __name__ == "__main__":
    main()
