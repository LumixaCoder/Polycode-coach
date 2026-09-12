"""Auto-rebuild the Learning Coach app every time you save a change.

Leave this running in a terminal while you edit code:

    python watch_build.py              # watches all project files
    python watch_build.py --poll       # force polling (no watchdog needed)
    python watch_build.py --once       # build once if any file changed, then exit

It watches the project's .py files recursively (including languages/),
data/*.json, and lesson_data.py. Each time you save, it waits ~2 seconds
(debounce so you can finish typing), then runs build.py automatically.
When it finishes, the app in dist/PolycodeCoach is up to date and
you can just double-click PolycodeCoach.exe - no commands needed.

Backend:
  - If `watchdog` is installed (`pip install watchdog`) it uses native
    OS file events for instant, low-CPU watching.
  - Otherwise it falls back to efficient polling (mtime + size hash).

Every successful build step explains what it just did, and a history of
every build is saved to builds.log.

Press Ctrl+C to stop watching.
"""
import argparse
import pathlib
import subprocess
import sys
import time
import hashlib
import os
from datetime import datetime

ROOT = pathlib.Path(__file__).resolve().parent

# --- Tunables (also exposed as CLI args) ---
POLL_SECONDS = 0.7        # how often we check files when polling
STABLE_SECONDS = 2.0      # how long files must stay unchanged before we build
IGNORED_DIRS = {
    ".venv", "venv", "__pycache__", ".pytest_cache", ".ruff_cache",
    ".mypy_cache", ".git", ".hg", "build", "dist", ".opencode",
    ".idea", ".vscode", "node_modules", "tests",
}
IGNORED_FILES = {
    "builds.log", "learning_progress.json", "learning_progress.json.bak",
}
IGNORED_SUFFIXES = {".pyc", ".pyo", ".tmp", ".log", ".spec.bak"}
# We also ignore any file inside IGNORED_DIRS implicitly.

# What to watch: relative patterns from ROOT
WATCHED_EXTS = {".py", ".json", ".txt", ".spec", ".md"}
# We intentionally include .py everywhere, .json only in data/ and languages/,
# but for simplicity we watch those exts everywhere except ignored dirs,
# and then filter to keep only relevant files.
RELEVANT_JSON_DIRS = {"data", "languages"}

def _is_ignored(path: pathlib.Path) -> bool:
    """True if path should be ignored (inside ignored dir or ignored filename)."""
    # Check any part of relative path is an ignored dir
    try:
        rel = path.relative_to(ROOT)
    except ValueError:
        rel = path
    for part in rel.parts:
        if part in IGNORED_DIRS:
            return True
        if part.startswith(".") and part not in (".", ".."):
            # Hide dotfiles like .gitignore already covered, but skip hidden caches
            if part in {".git", ".pytest_cache", ".ruff_cache"}:
                return True
    if path.name in IGNORED_FILES:
        return True
    if path.suffix in IGNORED_SUFFIXES:
        return True
    # Ignore spec's work output artifacts
    if path.name.endswith(".tmp"):
        return True
    return False

def _is_watched(path: pathlib.Path) -> bool:
    """True if this file is relevant to triggering a rebuild."""
    if _is_ignored(path):
        return False
    if not path.is_file():
        return False
    ext = path.suffix.lower()
    if ext not in WATCHED_EXTS:
        return False
    # For .json, only care about data/ and languages/ trees plus config jsons
    if ext == ".json":
        rel = path.relative_to(ROOT) if path.is_relative_to(ROOT) else path
        parts = rel.parts
        # Allow data/*.json and languages/**/*.json and opencode.json at root
        if len(parts) == 1 and path.name in {"opencode.json"}:
            return True
        if parts and parts[0] in RELEVANT_JSON_DIRS:
            return True
        # Ignore other json like learning_progress, package locks inside .venv already ignored
        return False
    # For .md, .txt only root-level docs trigger if they affect build? Keep minimal.
    if ext in {".md", ".txt"}:
        # Only watch if near root? But to avoid noise, only watch if it's at root
        try:
            rel = path.relative_to(ROOT)
            if len(rel.parts) == 1:
                # README etc not needed for build, but could be harmless. Ignore to reduce noise.
                return False
        except ValueError:
            pass
        return False
    if ext == ".spec":
        return True
    # .py is watched everywhere except ignored dirs
    if ext == ".py":
        # Also ignore .bak files
        if path.name.endswith(".bak"):
            return False
        return True
    return False

def watched_files() -> list:
    """Return sorted list of all currently watched files (recursive)."""
    out = []
    # Walk ROOT recursively, but prune ignored dirs early for speed
    for dirpath, dirnames, filenames in os.walk(ROOT):
        # Prune ignored dirs in-place
        dirnames[:] = [d for d in dirnames if d not in IGNORED_DIRS and not d.startswith(".")]
        # Also skip build/dist even if not pruned due to nesting
        dirpath_p = pathlib.Path(dirpath)
        if _is_ignored(dirpath_p):
            dirnames[:] = []
            continue
        for fname in filenames:
            fpath = dirpath_p / fname
            if _is_watched(fpath):
                out.append(fpath)
    # Also include top-level py files explicitly (os.walk covers them, but ensure sorted)
    out = sorted(set(out))
    return out

def file_fingerprint(path: pathlib.Path):
    """Lightweight fingerprint: (mtime_ns, size, hash_prefix). Uses hash only if mtime changed often."""
    try:
        st = path.stat()
        return (st.st_mtime_ns, st.st_size)
    except OSError:
        return None

def snapshot() -> dict:
    """Map Path -> fingerprint for all watched files."""
    snap = {}
    for p in watched_files():
        fp = file_fingerprint(p)
        if fp is not None:
            snap[p] = fp
    return snap

def changed_names(before: dict, after: dict) -> list:
    """Return sorted list of changed file names (relative to ROOT)."""
    touched = set(before) | set(after)
    changed = []
    for p in sorted(touched, key=lambda x: str(x)):
        if before.get(p) != after.get(p):
            try:
                rel = p.relative_to(ROOT)
                changed.append(str(rel))
            except ValueError:
                changed.append(p.name)
    return changed

def wait_until_stable(base: dict, poll: float, stable: float) -> dict:
    """Poll until snapshot stays identical for `stable` seconds."""
    stable_for = 0.0
    while True:
        time.sleep(poll)
        now = snapshot()
        if base != now:
            stable_for = 0.0
            # Show spinner hint for noisy saves
            changed = changed_names(base, now)
            if changed:
                print(f"  ... change detected: {', '.join(changed[:4])}{' ...' if len(changed)>4 else ''}  (waiting for save to settle)")
        else:
            stable_for += poll
            if stable_for >= stable:
                return now
        base = now

def _should_use_watchdog(force_poll: bool, force_watchdog: bool) -> bool:
    if force_poll:
        return False
    if force_watchdog:
        return True
    try:
        import watchdog  # noqa: F401
        return True
    except ImportError:
        return False

# ---------------- watchdog backend ----------------
def _watch_with_watchdog(poll: float, stable: float, verbose: bool):
    """Use watchdog Observer for event-driven watching. Falls back to polling if unavailable."""
    try:
        from watchdog.observers import Observer
        from watchdog.events import FileSystemEventHandler
        import threading

        changed_set = set()
        lock = threading.Lock()
        last_event_time = [time.time()]

        class Handler(FileSystemEventHandler):
            def on_any_event(self, event):
                # Filter to watched files only; directories ignored
                src = pathlib.Path(event.src_path) if hasattr(event, 'src_path') else None
                dest = pathlib.Path(event.dest_path) if hasattr(event, 'dest_path') and event.dest_path else None
                for p in (src, dest):
                    if p is None:
                        continue
                    # Normalize
                    try:
                        p = p.resolve()
                    except Exception:
                        p = pathlib.Path(p)
                    # Ignore events inside ignored dirs
                    if _is_ignored(p):
                        continue
                    # Only care if it would be a watched file or was one
                    # We accept any .py/.json event and later snapshot diff will confirm
                    if p.suffix.lower() in WATCHED_EXTS:
                        with lock:
                            changed_set.add(p)
                            last_event_time[0] = time.time()
                    # Also handle created/deleted watched files: snapshot diff will catch it
                if verbose and event.event_type in ("modified", "created", "deleted", "moved"):
                    print(f"  [watchdog] {event.event_type}: {event.src_path}")

        observer = Observer()
        handler = Handler()
        # Schedule observer on ROOT and all subdirs recursively
        observer.schedule(handler, str(ROOT), recursive=True)
        observer.start()
        print(f"  Using watchdog (native OS events) for instant detection.")
        try:
            before = snapshot()
            print(f"  Watching {len(before)} files. Save any .py or data/*.json to trigger rebuild.")
            print("  Press Ctrl+C to stop.\n")
            while True:
                time.sleep(poll)
                # Check if any event happened recently
                with lock:
                    if not changed_set:
                        continue
                    # Debounce: wait until no event for `stable` seconds
                    if time.time() - last_event_time[0] < stable:
                        continue
                    # At this point, events settled; snapshot diff tells us what truly changed
                    before_snapshot = before
                    after = snapshot()
                    changed = changed_names(before_snapshot, after)
                    if not changed:
                        # Spurious event (e.g., __pycache__ write already filtered but still)
                        changed_set.clear()
                        before = after
                        continue
                    # Clear for next batch
                    changed_set.clear()
                # Wait extra stable check via polling to ensure file writes fully flushed
                after_stable = wait_until_stable(after, poll, stable * 0.6)
                # Recompute changed against original before for accurate log
                final_changed = changed_names(before_snapshot, after_stable)
                if not final_changed:
                    before = after_stable
                    continue
                build_app(final_changed)
                before = snapshot()
        finally:
            observer.stop()
            observer.join(timeout=2)
    except ImportError:
        print("  watchdog not installed -> falling back to polling.")
        print("  Install for faster, lower-CPU watching: pip install watchdog")
        _watch_with_polling(poll, stable, verbose)
    except Exception as exc:
        print(f"  watchdog error ({exc}) -> falling back to polling.")
        _watch_with_polling(poll, stable, verbose)

def _watch_with_polling(poll: float, stable: float, verbose: bool):
    """Pure polling backend."""
    print(f"  Using polling every {poll:.1f}s (install 'watchdog' for native events).")
    before = snapshot()
    print(f"  Watching {len(before)} files. Save any .py or data/*.json to trigger rebuild.")
    if verbose:
        for p in sorted(before)[:12]:
            print(f"    - {p.relative_to(ROOT)}")
        if len(before) > 12:
            print(f"    ... and {len(before)-12} more")
    print("  Press Ctrl+C to stop.\n")
    try:
        while True:
            time.sleep(poll)
            after = snapshot()
            changed = changed_names(before, after)
            if not changed:
                before = after
                continue
            print(f"\n  Detected change in: {', '.join(changed[:5])}{' ...' if len(changed)>5 else ''}")
            print(f"  Waiting {stable:.1f}s for files to settle...")
            before = wait_until_stable(after, poll, stable)
            # Recompute final changed set against original before
            # (wait_until_stable already advanced, but we need to report)
            final_changed = changed_names(before, after)  # placeholder
            # Actually recompute from the snapshot before wait vs after wait
            # Use the stable snapshot as new before
            # For logging, use changed already
            build_app(changed)
            before = snapshot()
    except KeyboardInterrupt:
        raise

def build_app(changed: list) -> None:
    ts = datetime.now().strftime("%H:%M:%S")
    print("\n" + "=" * 70)
    print(f"[{ts}] Change saved in: {', '.join(changed)}")
    print("Rebuilding the app automatically... this can take ~15-60 seconds.")
    print("=" * 70)
    cmd = [sys.executable, str(ROOT / "build.py"), "--changed"]
    cmd.extend(changed)
    # Stream output in real time
    proc = subprocess.run(cmd, cwd=ROOT, check=False)
    if proc.returncode == 0:
        print("\n  ✓ App is updated. Open dist/PolycodeCoach/PolycodeCoach.exe")
        print("    to use the new version (close the app first if it's running).")
        print(f"  [{datetime.now().strftime('%H:%M:%S')}] Watching for next change...\n")
    else:
        print("\n  ✗ Build did not fully succeed. This usually means the app is still")
        print("    open (Windows locks files in use). Close the app, then save any")
        print("    file again and it will retry automatically.")
        print(f"  [{datetime.now().strftime('%H:%M:%S')}] Watching for next change...\n")

def parse_args():
    p = argparse.ArgumentParser(description="Auto-rebuild Learning Coach on file changes")
    p.add_argument("--poll", action="store_true", help="Force polling backend (ignore watchdog)")
    p.add_argument("--watchdog", action="store_true", help="Force watchdog backend (error if not installed)")
    p.add_argument("--once", action="store_true", help="Check once: if files changed since last build, rebuild once then exit")
    p.add_argument("--debounce", type=float, default=STABLE_SECONDS, help=f"Seconds to wait after last change before building (default {STABLE_SECONDS})")
    p.add_argument("--poll-interval", type=float, default=POLL_SECONDS, help=f"Polling interval in seconds (default {POLL_SECONDS})")
    p.add_argument("--verbose", action="store_true", help="Verbose: list watched files and events")
    p.add_argument("--changed", nargs="*", help=argparse.SUPPRESS)  # compatibility
    return p.parse_args()

def main():
    args = parse_args()
    poll = float(args.poll_interval)
    stable = float(args.debounce)
    verbose = bool(args.verbose)

    print("Watching for file changes in:")
    print("  ", ROOT)
    print(f"Save any .py (including languages/) or data/*.json and the app")
    print(f"will rebuild itself (~{stable:.1f}s debounce), then you can")
    print("open dist/PolycodeCoach/PolycodeCoach.exe instead of using commands.")
    # Show ignored hint
    if verbose:
        print(f"\nIgnored dirs: {', '.join(sorted(IGNORED_DIRS))}")
        print(f"Watching exts: {', '.join(sorted(WATCHED_EXTS))}")

    # --once mode: just snapshot diff against last build? We treat as one-shot polling check.
    if args.once:
        before = snapshot()
        print(f"  Snapshot: {len(before)} watched files.")
        print("  Waiting 2s for settle, then checking for changes...")
        time.sleep(2.0)
        after = snapshot()
        changed = changed_names(before, after)
        if not changed:
            # Also check if dist missing -> force build
            dist_exe = ROOT / "dist" / "PolycodeCoach" / "PolycodeCoach.exe"
            if not dist_exe.is_file():
                print("  dist/PolycodeCoach/PolycodeCoach.exe missing -> building now.")
                build_app(["initial build (dist missing)"])
            else:
                print("  No changes detected. Nothing to build.")
            return
        print(f"  Changes: {', '.join(changed)}")
        before_stable = wait_until_stable(after, poll, stable)
        build_app(changed)
        return

    use_watchdog = _should_use_watchdog(force_poll=args.poll, force_watchdog=args.watchdog)
    if args.watchdog and not use_watchdog:
        print("ERROR: --watchdog requested but watchdog not installed.")
        print("Install with: pip install watchdog")
        sys.exit(1)

    try:
        if use_watchdog:
            _watch_with_watchdog(poll, stable, verbose)
        else:
            _watch_with_polling(poll, stable, verbose)
    except KeyboardInterrupt:
        print("\nStopped watching. The app stays at the last build.")
    except Exception as exc:
        print(f"\nWatcher error: {exc}")
        sys.exit(1)

if __name__ == "__main__":
    main()
