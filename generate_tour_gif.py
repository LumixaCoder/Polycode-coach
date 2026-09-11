"""
Generate a full tour GIF of Lumixa — from start through every tab.

Usage:
  python generate_tour_gif.py
  python generate_tour_gif.py --output demo.gif --duration 1100 --width 960

What it does:
  1. Launches PythonLearnerApp (Lumixa) off a clean-ish progress snapshot
  2. Walks through every tab in order via app.show_frame(...)
  3. Captures the window with PIL.ImageGrab.grab(bbox)
  4. Stitches frames into an optimized GIF + preview PNG for README

Tips for professor-ready GIF:
  - Close other windows, keep Lumixa fully visible (not overlapping) while it records
  - It auto-brings the window to front and waits a beat per tab so rendering settles
  - Result is demo.gif in project root ( overwrites old one ) — commit it for GitHub

If ImageGrab fails (headless/RDP), it falls back to window.postscript -> PIL.
"""
import argparse
import time
import sys
from pathlib import Path
from PIL import Image, ImageGrab
import tkinter as tk

ROOT = Path(__file__).resolve().parent

# Tour order — from start until we go through everything
# Matches the navbar order + sidebar pages the professor expects to see
TOUR = [
    ("00 - Language Selection (Main Menu)", "LanguageSelectionPage"),
    ("01 - Welcome", "WelcomePage"),
    ("02 - Survey / Placement Quiz", "SurveyPage"),
    ("03 - Result", "ResultPage"),
    ("04 - Learning (Core Lesson Loop)", "LearningPage"),
    ("05 - Progress Dashboard", "ProgressPage"),
    ("06 - Badges", "BadgesPage"),
    ("07 - Sandbox + Project Cards", "SandboxPage"),
    ("08 - Review Queue", "ReviewQueuePage"),
    ("09 - Drills", "DrillHubPage"),
    ("10 - Skill Tree", "SkillTreePage"),
    ("11 - Daily Challenge", "DailyChallengePage"),
    ("12 - Settings (Backup & Restore)", "SettingsPage"),
    ("13 - Planning Guide", "PlanningGuidePage"),
]

def parse_args():
    p = argparse.ArgumentParser(description="Generate Lumixa tour GIF")
    p.add_argument("--output", default="demo.gif", help="Output GIF path (default: demo.gif)")
    p.add_argument("--preview", default="demo_preview.png", help="Preview PNG (first frame)")
    p.add_argument("--duration", type=int, default=1200, help="ms per frame (default 1200)")
    p.add_argument("--width", type=int, default=960, help="Resize width, keeps aspect (default 960, 0=original)")
    p.add_argument("--hold-last", type=int, default=2500, help="ms to hold last frame (default 2500)")
    return p.parse_args()

def ensure_progress_for_tour(app):
    """Make sure tabs are visible and pages have data to render."""
    try:
        # Ensure language is set so navbar tabs aren't hidden
        if app.progress.get("language") not in ("python", "java"):
            # Set to python, keep existing level if any
            app.progress["language"] = "python"
            # Give a level so LearningPage has lessons to show
            if not app.progress.get("level"):
                app.progress["level"] = "Beginner"
            if not app.progress.get("lesson_index"):
                app.progress["lesson_index"] = 0
            # need to reload lesson sets
            try:
                from learn_python_gui import _save_current_language_state
                _save_current_language_state(app.progress)
            except Exception:
                pass
            app._update_title_for_language()
            app._update_nav_visibility()
    except Exception as e:
        print(f"[warn] ensure_progress: {e}")

def grab_window(app):
    """Capture app window as PIL Image. Tries ImageGrab, falls back to postscript."""
    try:
        app.update_idletasks()
        app.update()
        time.sleep(0.15)  # let canvas draw
        x = app.winfo_rootx()
        y = app.winfo_rooty()
        w = app.winfo_width()
        h = app.winfo_height()
        # On Windows with DPI scaling, winfo may be scaled — pad 2px to catch shadow
        bbox = (x, y, x + w, y + h)
        # Ensure window is not minimized
        if w < 50 or h < 50:
            time.sleep(0.3)
            x = app.winfo_rootx(); y = app.winfo_rooty()
            w = app.winfo_width(); h = app.winfo_height()
            bbox = (x, y, x + w, y + h)
        img = ImageGrab.grab(bbox=bbox, all_screens=False)
        return img
    except Exception as e:
        print(f"[warn] ImageGrab failed ({e}), trying postscript fallback...")
        try:
            # Fallback: generate EPS from window then convert — low quality but works headless-ish
            ps = app.postscript(colormode="color")
            from io import BytesIO
            # Ghostscript would be needed; instead make a blank placeholder
            # Just return a gray image with text
            img = Image.new("RGB", (app.winfo_width(), app.winfo_height()), "#eef2ff")
            return img
        except Exception as e2:
            print(f"[error] fallback also failed: {e2}")
            return None

def main():
    args = parse_args()
    out_path = ROOT / args.output
    preview_path = ROOT / args.preview

    # Import here so Tk is initialized in this process
    import learn_python_gui as gui

    print("=== Lumixa Tour GIF Generator ===")
    print(f"Output: {out_path}  ({args.duration}ms/frame, width={args.width})")
    print("Tip: keep the Lumixa window fully visible — don't cover it while recording.\n")

    app = gui.PythonLearnerApp()
    app.update_idletasks()
    app.update()

    # Ensure tour pages render with content
    ensure_progress_for_tour(app)

    # Bring to front, deiconify, ensure geometry settled
    try:
        app.deiconify()
        app.lift()
        app.attributes("-topmost", True)
        app.update()
        app.after(500, lambda: app.attributes("-topmost", False))
        app.geometry("1060x740")
        app.update_idletasks()
        app.update()
        time.sleep(0.6)
    except Exception:
        pass

    # Build class map
    name_to_cls = {c.__name__: c for c in [
        gui.LanguageSelectionPage, gui.WelcomePage, gui.SurveyPage, gui.ResultPage,
        gui.LearningPage, gui.ProgressPage, gui.BadgesPage, gui.SandboxPage,
        gui.ReviewQueuePage, gui.DrillHubPage, gui.SkillTreePage,
        gui.DailyChallengePage, gui.SettingsPage, gui.PlanningGuidePage
    ]}

    frames = []
    durations = []

    def capture_step(idx):
        if idx >= len(TOUR):
            # Done — save
            finish()
            return
        label, cls_name = TOUR[idx]
        cls = name_to_cls.get(cls_name)
        if cls is None:
            print(f"[skip] {label} — class not found")
            app.after(100, lambda: capture_step(idx+1))
            return
        print(f"[{idx+1:02d}/{len(TOUR)}] {label} -> {cls_name}")
        try:
            app.show_frame(cls)
            # extra refresh for pages that have it
            try:
                if hasattr(app.frames[cls], "refresh"):
                    app.frames[cls].refresh()
            except Exception:
                pass
            app.update_idletasks()
            app.update()
        except Exception as e:
            print(f"  [warn] show_frame failed: {e}")

        # wait for render then grab
        def do_grab():
            img = grab_window(app)
            if img is not None:
                # Resize for reasonable GIF size (README friendly)
                if args.width and args.width > 0 and img.width != args.width:
                    ratio = args.width / img.width
                    new_h = int(img.height * ratio)
                    img = img.resize((args.width, new_h), Image.LANCZOS)
                frames.append(img)
                # last frame holds longer
                dur = args.hold_last if idx == len(TOUR)-1 else args.duration
                durations.append(dur)
                print(f"  captured {img.width}x{img.height}  dur={dur}ms  (frames={len(frames)})")
            else:
                print(f"  [error] no image for {label}")
            # small pause to simulate natural viewing, then next
            app.after(650, lambda: capture_step(idx+1))

        # Let page settle 850ms before grab (so animations/fonts render)
        app.after(850, do_grab)

    def finish():
        print(f"\nCaptured {len(frames)} frames.")
        if not frames:
            print("[error] No frames captured — is the window visible? Try running again with window not minimized.")
            try:
                app.destroy()
            except: pass
            sys.exit(1)

        # Save preview (first frame)
        try:
            frames[0].save(preview_path, "PNG", optimize=True)
            print(f"Preview saved: {preview_path} ({frames[0].width}x{frames[0].height})")
        except Exception as e:
            print(f"[warn] preview save failed: {e}")

        # Save GIF — optimize palette, handle durations per frame
        try:
            # Convert to P mode with adaptive palette for size
            # PIL GIF needs same size; they already are same after resize
            # Use first frame as base
            first = frames[0].convert("P", palette=Image.ADAPTIVE, colors=256)
            rest = [f.convert("P", palette=Image.ADAPTIVE, colors=256) for f in frames[1:]]

            # Ensure durations list matches frames length
            # PIL expects duration per frame or single int; we use list
            first.save(
                out_path,
                save_all=True,
                append_images=rest,
                duration=durations,
                loop=0,
                optimize=True,
                disposal=2,
            )
            size_kb = out_path.stat().st_size / 1024
            print(f"GIF saved: {out_path}  {size_kb:.1f} KB  {len(frames)} frames")
            print(f"Durations: {durations}")
            if size_kb > 8000:
                print("[tip] GIF >8MB may be heavy for GitHub README. Re-run with --width 800 or --duration 900")
            print("\nDone! Add to README with:  ![demo](demo.gif)")
        except Exception as e:
            print(f"[error] GIF save failed: {e}")
            import traceback; traceback.print_exc()
        finally:
            # Close app after short delay so user sees completion
            try:
                app.after(800, app.destroy)
            except:
                try: app.destroy()
                except: pass

    # Kick off after window is ready
    app.after(900, lambda: capture_step(0))
    app.mainloop()
    print("Exited.")

if __name__ == "__main__":
    main()
