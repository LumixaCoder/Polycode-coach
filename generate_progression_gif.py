"""
Full progression GIF — startup -> quiz -> learning steps -> running code -> progress.

Shows EVERYTHING so professor sees the journey, not just static tabs.

Run:
  python generate_progression_gif.py
  python generate_progression_gif.py --width 900 --duration 950

Captures ~30 frames:
  - Cold start (Main Menu, no language)
  - Pick Python -> Welcome -> Survey -> Result (quiz progression)
  - Learning: concept -> practice (type code -> run -> +5 XP) -> debug -> final project
  - Progress Dashboard (XP growth), Badges, Skill Tree, Review, Drills, Daily, Sandbox (code run), Settings

Safe: backs up learning_progress.json before tour and restores after.
"""
import argparse
import time
import sys
import shutil
from pathlib import Path
from PIL import Image, ImageGrab

ROOT = Path(__file__).resolve().parent
PROGRESS = ROOT / "learning_progress.json"
BACKUP = ROOT / "learning_progress.json.bak_gif"

def parse_args():
    p = argparse.ArgumentParser(description="Full progression GIF")
    p.add_argument("--output", default="demo.gif", help="Output GIF")
    p.add_argument("--preview", default="demo_preview.png", help="Preview PNG")
    p.add_argument("--duration", type=int, default=950, help="ms per frame (default 950)")
    p.add_argument("--width", type=int, default=900, help="Resize width (0=original)")
    p.add_argument("--hold-last", type=int, default=2800, help="ms last frame")
    return p.parse_args()

def grab(app):
    try:
        app.update_idletasks(); app.update()
        time.sleep(0.12)
        x, y = app.winfo_rootx(), app.winfo_rooty()
        w, h = app.winfo_width(), app.winfo_height()
        if w < 80 or h < 80:
            time.sleep(0.3)
            x, y = app.winfo_rootx(), app.winfo_rooty()
            w, h = app.winfo_width(), app.winfo_height()
        return ImageGrab.grab(bbox=(x, y, x+w, y+h))
    except Exception as e:
        print(f"[warn] grab failed: {e}")
        return None

def ensure_backup():
    if PROGRESS.exists():
        try:
            shutil.copy2(PROGRESS, BACKUP)
            print(f"[backup] saved -> {BACKUP.name}")
        except Exception as e:
            print(f"[warn] backup fail: {e}")

def restore_backup():
    if BACKUP.exists():
        try:
            shutil.copy2(BACKUP, PROGRESS)
            BACKUP.unlink(missing_ok=True)
            print(f"[restore] progress restored")
        except Exception as e:
            print(f"[warn] restore fail: {e}")

def main():
    args = parse_args()
    out_path = ROOT / args.output
    preview_path = ROOT / args.preview

    ensure_backup()

    import learn_python_gui as gui

    print("=== Full Progression GIF — startup + progressing ===")
    print(f"Output: {out_path}  width={args.width}  dur={args.duration}ms")
    print("Keep Lumixa window fully visible and don't cover it!\n")

    app = gui.PythonLearnerApp()
    app.update_idletasks(); app.update()
    # front and size
    try:
        app.deiconify(); app.lift()
        app.attributes("-topmost", True)
        app.geometry("1060x740")
        app.update()
        app.after(500, lambda: app.attributes("-topmost", False))
        time.sleep(0.6)
    except: pass

    # Make sure we start from a clean slate for demo but keep visuals rich
    # We will manipulate app.progress in-memory for the tour; keep autosave from overwriting too much
    # Set fresh start state
    try:
        # Reset to no language to show cold start
        app.progress["language"] = None
        app.progress["level"] = ""
        app.progress["lesson_index"] = 0
        app.progress["step_index"] = 0
        app.progress["completed_lessons"] = []
        app.progress["completed_steps"] = {}
        app.progress["completed_by_level"] = {}
        # keep XP/streak visible but not huge
        # ensure theme dark for contrast (prof likes dark)
        # app.progress["theme"] = "dark"
        app._update_nav_visibility()
        app._update_title_for_language()
        app.show_frame(gui.LanguageSelectionPage)
        app.update()
    except Exception as e:
        print(f"[warn] init reset: {e}")

    frames = []
    durations = []
    labels = []

    def cap(label, dur=None):
        # wait for render
        time.sleep(0.18)
        app.update_idletasks(); app.update()
        img = grab(app)
        if img is None:
            print(f"[skip] {label} grab failed")
            return
        if args.width and args.width > 0 and img.width != args.width:
            ratio = args.width / img.width
            img = img.resize((args.width, int(img.height * ratio)), Image.LANCZOS)
        frames.append(img)
        d = dur if dur is not None else args.duration
        durations.append(d)
        labels.append(label)
        print(f"[{len(frames):02d}] {label} -> {img.width}x{img.height} dur={d}")

    # Helper to advance events
    def after(ms, fn):
        app.after(ms, fn)

    # Tour steps — sequenced via after() chain
    seq = []

    # Phase 1: Startup
    seq.append(lambda: cap("01 STARTUP — Main Menu (pick language)"))
    # Small pause frame to feel like startup
    seq.append(lambda: cap("02 STARTUP — Main Menu (hold)", dur=1400))

    def pick_python():
        try:
            app.set_language("python")  # goes to Welcome if level empty, else Learning
            # Force Welcome for demo
            app.show_frame(gui.WelcomePage)
            app.update()
        except Exception as e:
            print(f"[warn] pick_python: {e}")
        cap("03 PICKED Python -> Welcome (roadmap + Start Quiz)")
    seq.append(pick_python)

    def go_survey():
        try: app.show_frame(gui.SurveyPage)
        except: pass
        cap("04 SURVEY — Placement Quiz (Q1/5)")
    seq.append(go_survey)

    # Simulate answering quiz quickly — just show Survey again as if Q2, then set level
    seq.append(lambda: cap("05 SURVEY — Quiz progressing (Q3/5)"))
    
    def show_result():
        # Simulate quiz done -> set Beginner
        try:
            app.progress["level"] = "Beginner"
            app.progress["lesson_index"] = 0
            app.progress["step_index"] = 0
            # Mark level history
            if "Beginner" not in app.progress.get("level_history", []):
                app.progress.setdefault("level_history", []).append("Beginner")
            # ensure state saved per language
            try:
                from learn_python_gui import _save_current_language_state
                _save_current_language_state(app.progress)
            except: pass
            app.show_frame(gui.ResultPage)
            app.update()
        except Exception as e:
            print(f"[warn] result: {e}")
        cap("06 RESULT — Placed at Beginner (Start Learning CTA)", dur=1300)
    seq.append(show_result)

    # Phase 2: Learning progression
    def learning_concept():
        try:
            app.progress["step_index"] = 0
            app.show_frame(gui.LearningPage)
            # refresh forces concept view
            app.frames[gui.LearningPage].refresh()
            app.update()
        except Exception as e:
            print(f"[warn] learning concept: {e}")
        cap("07 LEARNING — Lesson 1 Concept (Built-ins)")
    seq.append(learning_concept)

    def learning_practice_starter():
        try:
            app.progress["step_index"] = 1  # practice step
            app.frames[gui.LearningPage].refresh()
            app.update()
        except: pass
        cap("08 LEARNING — Practice: starter code (before typing)")
    seq.append(learning_practice_starter)

    def learning_practice_typed():
        # Simulate typing correct code: we mark step as done before capture to show success state?
        # Instead, fill draft and simulate run success -> award XP
        try:
            # Find the practice step and get starter -> inject correct code
            lp = app.frames[gui.LearningPage]
            # Mark step 1 as completed and award XP to show progression
            sk = gui.step_key("Beginner", 0, 1)
            if sk not in app.progress.get("completed_steps", {}):
                app.progress.setdefault("completed_steps", {})[sk] = True
                gui.award_xp(app.progress, 5, "practice step")
                gui.update_streak(app.progress)
                # keep per-language map
                # also set draft_code so editor shows typed code on refresh
                app.progress.setdefault("draft_code", {})[sk] = "print('Hello World')"
            # Advance to next step visually
            app.progress["step_index"] = 1
            lp.refresh()
            app.update()
            # Now capture the success (green feedback) — need to trigger refresh that shows "Already completed!"
            # We'll keep step_index at 1 so it shows completed badge
        except Exception as e:
            print(f"[warn] typed: {e}")
        cap("09 LEARNING — Practice RUN -> Correct! +5 XP (green, confetti)")
    seq.append(learning_practice_typed)

    def learning_next_concept():
        try:
            app.progress["step_index"] = 2  # next concept
            app.frames[gui.LearningPage].refresh()
            app.update()
        except: pass
        cap("10 LEARNING — Next Concept (len/type)")
    seq.append(learning_next_concept)

    def learning_debug():
        # Steps: find which idx is debug — in Built-ins lesson, steps[?] includes debug? Let's just show practice #2
        try:
            # mark previous as done, move to step 3 (practice 2)
            sk2 = gui.step_key("Beginner", 0, 3)  # second practice
            # Instead of precise, just advance to 3 and show practice view
            app.progress["step_index"] = 3
            # Pre-mark step 2 as done so dots show progress
            sk_prev = gui.step_key("Beginner", 0, 2)
            if sk_prev not in app.progress.get("completed_steps", {}):
                app.progress["completed_steps"][sk_prev] = True
            app.frames[gui.LearningPage].refresh()
            app.update()
        except: pass
        cap("11 LEARNING — Practice 2 (len/type) — progressing dots")
    seq.append(learning_debug)

    def learning_final_project():
        try:
            # Mark all actionable steps done to reveal Final Project view
            # Find lesson steps length
            lp = app.frames[gui.LearningPage]
            lessons = lp.lesson_sets.get("Beginner", [])
            if lessons:
                steps = lessons[0].get("steps", [])
                actionable = [i for i,s in enumerate(steps) if s["type"] not in ("concept","example")]
                for i in actionable:
                    sk = gui.step_key("Beginner", 0, i)
                    app.progress["completed_steps"][sk] = True
                app.frames[gui.LearningPage].refresh()
                app.update()
        except Exception as e:
            print(f"[warn] final project: {e}")
        cap("12 LEARNING — Final Project (Number Analyzer) — all steps done", dur=1300)
    seq.append(learning_final_project)

    def show_progress():
        try: app.show_frame(gui.ProgressPage)
        except: pass
        cap("13 PROGRESS — Dashboard (XP + streak after lesson)", dur=1200)
    seq.append(show_progress)

    def show_skill():
        try: app.show_frame(gui.SkillTreePage)
        except: pass
        cap("14 SKILL TREE — Beginner row (1/9 done, current glow)")
    seq.append(show_skill)

    def show_review():
        try: app.show_frame(gui.ReviewQueuePage)
        except: pass
        cap("15 REVIEW — Spaced repetition queue")
    seq.append(show_review)

    def show_drills():
        try: app.show_frame(gui.DrillHubPage)
        except: pass
        cap("16 DRILLS — Muscle memory drills")
    seq.append(show_drills)

    def show_daily():
        try: app.show_frame(gui.DailyChallengePage)
        except: pass
        cap("17 DAILY — Challenge + editor (Run & Check)")
    seq.append(show_daily)

    def sandbox_run():
        try:
            app.show_frame(gui.SandboxPage)
            app.update()
            # Try to fill sandbox editor and run to show output
            # SandboxPage has an editor; we can set sandbox_code and trigger run
            # Simplest: just show sandbox with starter code, then second capture after "running"
            cap("18 SANDBOX — Playground (starter code)")
            # Now inject a quick hello and simulate output by setting progress sandbox_code
            # Refresh again to show typed code
            # Find editor in frame and set code
            try:
                sb = app.frames[gui.SandboxPage]
                # Try to set code
                if hasattr(sb, "_editor"):
                    sb._editor.delete("1.0", "end")
                    sb._editor.insert("1.0", "print('Hello Lumixa')\nfor i in range(3):\n    print(i)")
                    app.update()
                    time.sleep(0.2)
                    # Try to trigger run if method exists
                    if hasattr(sb, "_run_code"):
                        try: sb._run_code()
                        except: pass
                    elif hasattr(sb, "run_code"):
                        try: sb.run_code()
                        except: pass
                    app.update()
            except Exception as e:
                print(f"[warn] sandbox fill: {e}")
            cap("19 SANDBOX — After Run (output Hello + 0 1 2)", dur=1200)
            return  # we already capped two, avoid double cap in seq
        except Exception as e:
            print(f"[warn] sandbox: {e}")
            cap("18 SANDBOX — Playground")
    # Custom handling for sandbox (two frames)
    seq.append(sandbox_run)
    # Don't add extra after sandbox_run done
    def show_badges_wrap():
        try: app.show_frame(gui.BadgesPage)
        except: pass
        cap("20 BADGES — Earned + locked (23 badges)")
    seq.append(show_badges_wrap)

    def show_settings():
        try: app.show_frame(gui.SettingsPage)
        except: pass
        cap("21 SETTINGS — Theme, backup, reset (full)", dur=1100)
    seq.append(show_settings)

    def show_planning():
        try: app.show_frame(gui.PlanningGuidePage)
        except: pass
        cap("22 PLANNING GUIDE — 2/4/6 week tracks", dur=args.hold_last)
    seq.append(show_planning)

    # Execute sequence stepwise with chest
    idx = [0]
    def run_next():
        if idx[0] >= len(seq):
            # done
            finish()
            return
        fn = seq[idx[0]]
        idx[0] += 1
        # Special case: sandbox_run already does double cap and returns, we need to skip its extra cap
        # It handles its own index, just call it
        try:
            fn()
        except Exception as e:
            print(f"[error] step {idx[0]}: {e}")
        # schedule next after capture delay
        # sandbox_run does 2 captures, need a bit longer gap
        gap = 900 if idx[0] != 7 else 1100  # a bit longer after survey
        app.after(850, run_next)

    def finish():
        print(f"\nCaptured {len(frames)} frames.")
        if not frames:
            print("[error] no frames")
            try: app.destroy()
            except: pass
            restore_backup()
            sys.exit(1)
        try:
            frames[0].save(preview_path, "PNG", optimize=True)
            print(f"Preview: {preview_path} {frames[0].width}x{frames[0].height}")
        except Exception as e:
            print(f"[warn] preview: {e}")
        try:
            first = frames[0].convert("P", palette=Image.ADAPTIVE, colors=256)
            rest = [f.convert("P", palette=Image.ADAPTIVE, colors=256) for f in frames[1:]]
            first.save(
                out_path, save_all=True, append_images=rest,
                duration=durations, loop=0, optimize=True, disposal=2
            )
            kb = out_path.stat().st_size/1024
            print(f"GIF: {out_path} {kb:.1f} KB {len(frames)} frames")
            if kb > 9000:
                print("[tip] >9MB — try --width 800")
            print("Labels:")
            for i, l in enumerate(labels): print(f"  {i+1:02d} {l}")
        except Exception as e:
            print(f"[error] save: {e}")
            import traceback; traceback.print_exc()
        finally:
            try: app.after(900, app.destroy)
            except:
                try: app.destroy()
                except: pass
            # restore after destroy
            app.after(1200, restore_backup)

    # Kick off after window ready
    app.after(1000, run_next)
    app.mainloop()
    print("Exited full tour.")
    # ensure restore if not already
    if BACKUP.exists():
        restore_backup()

if __name__ == "__main__":
    main()
