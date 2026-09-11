"""One-click dev launcher: GUI + auto-update watcher together.

Run:
    python dev.py               # starts GUI with live hot-reload + background exe rebuild
    python dev.py --no-watch    # GUI only (still has hot-reload, but no exe rebuild)
    python dev.py --watch-only  # only watcher, no GUI (same as python watch_build.py)

What it does:
  - Starts the Tkinter app (learn_python_gui.py) with hot-reload enabled
  - In parallel, starts watch_build.py which rebuilds dist/Lumixa/
    on every save (so the frozen exe stays up to date without manual builds)
  - Press Ctrl+C in this terminal or close the GUI to stop both.

Hot-reload vs rebuild:
  - Hot-reload (inside the GUI, ~1.5s): lesson_data.py + languages/*/lessons.py
    changes appear instantly without restart + shows 🔄 toast.
  - Rebuild (watch_build.py, ~15-60s): rebuilds the frozen exe for distribution.
    Needs the GUI closed to overwrite exe (watcher retries automatically).

Alternative shortcuts:
  - python learn_python_gui.py --watch   (GUI spawns watcher itself)
  - python build.py --watch              (build once then watch)
  - python watch_build.py                (watch only)
"""
import argparse
import os
import pathlib
import subprocess
import sys
import time
import signal

# Windowed (pythonw) has no console — avoid crash on print
if sys.stdout is None or sys.stderr is None:
    try:
        _null = open(os.devnull, "w")
        if sys.stdout is None:
            sys.stdout = _null
        if sys.stderr is None:
            sys.stderr = _null
    except Exception:
        pass

ROOT = pathlib.Path(__file__).resolve().parent

def _has_watchdog():
    try:
        import watchdog  # noqa: F401
        return True
    except ImportError:
        return False

def main():
    p = argparse.ArgumentParser(description="Dev launcher: GUI + auto-update")
    p.add_argument("--no-watch", action="store_true", help="Don't start exe rebuild watcher (hot-reload still on)")
    p.add_argument("--watch-only", action="store_true", help="Only start watcher, no GUI")
    p.add_argument("--poll", action="store_true", help="Force poll watcher (no watchdog)")
    args = p.parse_args()

    print("Lumixa - Dev Mode")
    print("================================")
    if not _has_watchdog():
        print("Tip: pip install watchdog  for instant rebuilds (fallback polling is slower).")
    else:
        print("Using watchdog for instant file events.")

    procs = []

    def cleanup(signum=None, frame=None):
        print("\nShutting down dev processes...")
        for proc in procs:
            try:
                if proc.poll() is None:
                    proc.terminate()
                    try:
                        proc.wait(timeout=2)
                    except subprocess.TimeoutExpired:
                        proc.kill()
            except Exception:
                pass
        sys.exit(0)

    signal.signal(signal.SIGINT, cleanup)
    try:
        # Use CREATE_NEW_CONSOLE on Windows for watcher so its output is visible?
        # Keep it simple: inherit stdio so logs interleave.
        if args.watch_only:
            print("\nStarting watcher only (no GUI)... Press Ctrl+C to stop.\n")
            cmd = [sys.executable, str(ROOT / "watch_build.py")]
            if args.poll:
                cmd.append("--poll")
            subprocess.call(cmd, cwd=ROOT)
            return

        watcher = None
        if not args.no_watch:
            print("\n[1/2] Starting auto-rebuild watcher (dist/ will update on save)...")
            w_cmd = [sys.executable, str(ROOT / "watch_build.py")]
            if args.poll:
                w_cmd.append("--poll")
            try:
                watcher_env = os.environ.copy()
                watcher_env["PYTHONLEARNING_WATCHER_EXTERNAL"] = "1"
                watcher = subprocess.Popen(w_cmd, cwd=ROOT, env=watcher_env)
                procs.append(watcher)
                print(f"      Watcher PID {watcher.pid}  (logs below; close GUI or Ctrl+C to stop)")
                time.sleep(0.8)
                if watcher.poll() is not None:
                    print("      Watcher exited early (maybe an error). Continuing with GUI only.")
                    procs.remove(watcher)
                    watcher = None
            except Exception as exc:
                print(f"      Could not start watcher: {exc}")
                watcher = None
        else:
            print("\n[1/2] Skipping watcher (--no-watch). Only hot-reload will be active.")

        print("[2/2] Starting GUI (hot-reload ~1.5s for lesson changes)...")
        print("      Tip: edit lesson_data.py or languages/*/lessons.py and watch for refresh toast")
        print("      Close the GUI to also stop watcher.\n")
        gui_cmd = [sys.executable, str(ROOT / "learn_python_gui.py")]
        # Tell GUI that watcher is already running externally so it doesn't spawn a second one
        gui_env = os.environ.copy()
        if watcher is not None:
            gui_env["PYTHONLEARNING_WATCHER_EXTERNAL"] = "1"
        # GUI already has hot-reload; if watcher running, GUI doesn't need --watch (avoid double spawn)
        # If we didn't start watcher externally, GUI will auto-start its own (now default).
        gui_proc = subprocess.Popen(gui_cmd, cwd=ROOT, env=gui_env)
        procs.append(gui_proc)
        # Wait for GUI to exit
        try:
            gui_proc.wait()
        except KeyboardInterrupt:
            cleanup()
        print("\nGUI closed.")
        cleanup()
    except KeyboardInterrupt:
        cleanup()

if __name__ == "__main__":
    main()
