"""
Clean Tour GIF — starts officially open, no black screens, no terminal.

Fixes black frames by:
- waiting for window to be viewable and non-black before any capture
- retrying grabs that are still black
- discarding any black frames automatically
- starting sequence only after app is fully rendered (Language Selection)

Run:
  python generate_clean_gif.py
  python generate_clean_gif.py --width 900 --duration 900
"""
import argparse
import time
import sys
import shutil
from pathlib import Path
from PIL import Image, ImageGrab, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
PROGRESS = ROOT / "learning_progress.json"
BACKUP = ROOT / "learning_progress.json.bak_gif_clean"

def parse_args():
    p = argparse.ArgumentParser(description="Clean tour GIF - no black screens")
    p.add_argument("--output", default="demo.gif")
    p.add_argument("--preview", default="demo_preview.png")
    p.add_argument("--duration", type=int, default=900)
    p.add_argument("--width", type=int, default=900)
    p.add_argument("--hold-last", type=int, default=2800)
    return p.parse_args()

def is_black_image(img, thresh_avg=15, black_ratio_thresh=0.80):
    """Detect black/empty frames (grab before window mapped)."""
    try:
        small = img.resize((32, 32))
        if small.mode != "RGB":
            small = small.convert("RGB")
        # Use get_flattened_data if available, fallback to getdata
        try:
            pixels = list(small.get_flattened_data())
            # get_flattened_data returns flat list? Actually need to handle
            # For RGB, it returns R,G,B flat. Convert to tuples
            # Simpler use getdata
            pixels = list(small.getdata())
        except:
            pixels = list(small.getdata())
        avg = sum(sum(px)/3 for px in pixels) / len(pixels)
        black = sum(1 for px in pixels if max(px) < 30) / len(pixels)
        return avg < thresh_avg and black > black_ratio_thresh
    except Exception:
        return False

def grab_clean(app, retries=5, delay=0.35):
    """Grab window, retry if black or too small."""
    for attempt in range(retries):
        try:
            app.update_idletasks()
            app.update()
            time.sleep(0.12)
            x, y = app.winfo_rootx(), app.winfo_rooty()
            w, h = app.winfo_width(), app.winfo_height()
            if w < 80 or h < 80:
                time.sleep(0.3)
                x, y = app.winfo_rootx(), app.winfo_rooty()
                w, h = app.winfo_width(), app.winfo_height()
            # If window not viewable, wait
            try:
                if not app.winfo_viewable():
                    time.sleep(0.3)
                    continue
            except:
                pass
            if w < 100 or h < 100:
                time.sleep(delay)
                continue
            img = ImageGrab.grab(bbox=(x, y, x + w, y + h))
            if is_black_image(img):
                # Wait and retry - window not yet painted
                if attempt < retries - 1:
                    time.sleep(delay)
                    continue
                else:
                    # last attempt still black - discard
                    return None
            return img
        except Exception as e:
            if attempt < retries - 1:
                time.sleep(delay)
                continue
            print(f"[warn] grab_clean failed: {e}")
            return None
    return None

def add_overlay(img, label, idx, total):
    try:
        draw = ImageDraw.Draw(img, "RGBA")
        w, h = img.size
        bar_h = 36
        draw.rectangle([0, h - bar_h, w, h], fill=(15, 23, 42, 230))
        dot_r = 4
        gap = 14
        dots_w = total * gap
        start_x = (w - dots_w) // 2
        y_dot = h - 14
        for i in range(total):
            cx = start_x + i * gap + 5
            fill = (99, 102, 241) if i <= idx else (71, 85, 105)
            outline = (255, 255, 255) if i == idx else fill
            draw.ellipse([cx - dot_r, y_dot - dot_r, cx + dot_r, y_dot + dot_r], fill=fill, outline=outline, width=1)
        try:
            font = ImageFont.load_default()
        except:
            font = None
        counter = f"{idx+1:02d}/{total:02d}"
        draw.text((12, h - 28), counter, fill=(148, 163, 184), font=font)
        txt = label[:68]
        try:
            bbox = draw.textbbox((0, 0), txt, font=font)
            tw = bbox[2] - bbox[0]
        except:
            tw = len(txt) * 6
        tx = max(60, (w - tw)//2)
        draw.text((tx, h - 28), txt, fill=(226, 232, 240), font=font)
        draw.rectangle([0, 0, w, 22], fill=(15, 23, 42, 180))
        draw.text((10, 4), "Lumixa \u2022 Polycode Coach \u2022 Full Tour", fill=(148, 163, 184), font=font)
        return img
    except Exception as e:
        print(f"[warn] overlay {e}")
        return img

def ensure_backup():
    if PROGRESS.exists():
        try:
            shutil.copy2(PROGRESS, BACKUP)
            print(f"[backup] -> {BACKUP.name}")
        except Exception as e:
            print(f"[warn] backup {e}")

def restore_backup():
    if BACKUP.exists():
        try:
            shutil.copy2(BACKUP, PROGRESS)
            BACKUP.unlink(missing_ok=True)
            print("[restore] progress restored")
        except Exception as e:
            print(f"[warn] restore {e}")

def main():
    args = parse_args()
    out_path = ROOT / args.output
    preview_path = ROOT / args.preview
    # backup old demo.gif if exists
    old_demo = out_path
    if old_demo.exists():
        bak = ROOT / "demo_black_backup.gif"
        try:
            shutil.copy2(old_demo, bak)
            print(f"[backup] old demo.gif -> {bak.name} ({bak.stat().st_size/1024:.0f} KB)")
        except Exception as e:
            print(f"[warn] demo backup {e}")
    ensure_backup()
    import learn_python_gui as gui

    print("=== Clean Tour GIF — no black, starts officially open ===")
    print(f"Output: {out_path} width={args.width} dur={args.duration}ms")
    print("Keep Lumixa window fully visible, don't cover it!\n")

    app = gui.PythonLearnerApp()
    app.update_idletasks()
    app.update()
    # Setup window — ensure visible, topmost briefly, stable geometry
    try:
        app.deiconify()
        app.lift()
        app.attributes("-topmost", True)
        app.geometry("1060x740")
        app.update()
        app.after(500, lambda: app.attributes("-topmost", False))
        # Wait for window to be viewable
        for _ in range(20):
            app.update()
            if app.winfo_viewable() and app.winfo_width() > 300:
                break
            time.sleep(0.15)
        time.sleep(0.8)  # extra settle for DPI/fonts
    except Exception as e:
        print(f"[warn] window setup {e}")

    # Fresh start for clean demo — but keep XP visible
    try:
        app.progress["language"] = None
        app.progress["level"] = ""
        app.progress["lesson_index"] = 0
        app.progress["step_index"] = 0
        app.progress["completed_lessons"] = []
        app.progress["completed_steps"] = {}
        app.progress["completed_by_level"] = {}
        app.progress["xp"] = 12
        # Ensure nav reflects no language yet (tabs hidden)
        app._update_nav_visibility()
        app._update_title_for_language()
        app.show_frame(gui.LanguageSelectionPage)
        app.update()
        time.sleep(0.5)
    except Exception as e:
        print(f"[warn] init {e}")

    # WARMUP — wait until grab is not black before starting sequence
    print("[warmup] waiting for window to render (no black frames)...")
    warmup_ok = False
    for attempt in range(12):
        img = grab_clean(app, retries=3)
        if img is not None and not is_black_image(img):
            print(f"[warmup] window ready after {attempt+1} tries ({img.size})")
            warmup_ok = True
            break
        else:
            print(f"[warmup] try {attempt+1}/12 still not ready (black or None), retrying...")
            time.sleep(0.35)
            app.update()
    if not warmup_ok:
        print("[warn] warmup still black after 12 tries — will filter black frames during capture")

    frames = []
    durations = []
    labels = []
    total_est = 22  # updated count for dots (no black startup frames)

    def cap(label, dur=None):
        # limit black retries inside grab_clean
        app.update_idletasks()
        app.update()
        time.sleep(0.15)
        img = grab_clean(app, retries=4)
        if img is None:
            print(f"[skip BLACK] {label} — discarded black frame")
            return False
        if is_black_image(img):
            print(f"[skip BLACK2] {label} — still black after grab")
            return False
        if args.width and args.width > 0 and img.width != args.width:
            ratio = args.width / img.width
            img = img.resize((args.width, int(img.height * ratio)), Image.LANCZOS)
        idx = len(frames)
        img = add_overlay(img, label, idx, total_est)
        frames.append(img)
        d = dur if dur is not None else args.duration
        durations.append(d)
        labels.append(label)
        print(f"[{len(frames):02d}/{total_est}] {label} -> {img.width}x{img.height} dur={d}")
        return True

    seq = []

    # Clean sequence — starts officially open at Language Selection, no terminal
    seq.append(lambda: cap("01 OPEN — Main Menu (choose language)"))
    seq.append(lambda: cap("02 OPEN — Main Menu (hold)", dur=1200))
    def pick_python():
        try:
            app.set_language("python")
            app.show_frame(gui.WelcomePage)
            app.update()
        except: pass
        cap("03 PICKED Python -> Welcome (roadmap)")
    seq.append(pick_python)
    seq.append(lambda: (app.show_frame(gui.SurveyPage), app.update(), cap("04 SURVEY — Placement Quiz Q1/5"))[2])
    seq.append(lambda: cap("05 SURVEY — Q3/5 progressing"))
    def result():
        try:
            app.progress["level"]="Beginner"; app.progress["lesson_index"]=0; app.progress["step_index"]=0
            if "Beginner" not in app.progress.get("level_history",[]): app.progress.setdefault("level_history",[]).append("Beginner")
            try:
                from learn_python_gui import _save_current_language_state; _save_current_language_state(app.progress)
            except: pass
            app.show_frame(gui.ResultPage); app.update()
        except: pass
        cap("06 RESULT — Placed Beginner -> Start Learning", dur=1200)
    seq.append(result)
    def lc0():
        try:
            app.progress["step_index"]=0
            app.show_frame(gui.LearningPage)
            app.frames[gui.LearningPage].refresh(); app.update()
        except: pass
        cap("07 LEARNING — Lesson 1 Concept (print/len/type)")
    seq.append(lc0)
    def pr_starter():
        try:
            app.progress["step_index"]=1
            app.frames[gui.LearningPage].refresh(); app.update()
        except: pass
        cap("08 PRACTICE — Starter code (before typing)")
    seq.append(pr_starter)
    def type_a():
        try:
            sk = gui.step_key("Beginner",0,1)
            app.progress.setdefault("draft_code",{})[sk]="print('Hello"
            app.frames[gui.LearningPage].refresh(); app.update()
        except: pass
        cap("09 PRACTICE — Typing… print('Hello", dur=400)
    seq.append(type_a)
    def type_b():
        try:
            sk = gui.step_key("Beginner",0,1)
            app.progress["draft_code"][sk]="print('Hello World')"
            app.frames[gui.LearningPage].refresh(); app.update()
        except: pass
        cap("10 PRACTICE — Typing… print('Hello World')", dur=500)
    seq.append(type_b)
    def run_correct():
        try:
            sk = gui.step_key("Beginner",0,1)
            if sk not in app.progress.get("completed_steps",{}):
                app.progress.setdefault("completed_steps",{})[sk]=True
                gui.award_xp(app.progress,5,"practice step"); gui.update_streak(app.progress)
                app.progress["draft_code"][sk]="print('Hello World')"
            app.progress["step_index"]=1
            app.frames[gui.LearningPage].refresh(); app.update()
        except Exception as e:
            print(f"[warn] run_correct {e}")
        cap("11 PRACTICE — Run -> Correct! +5 XP", dur=1100)
    seq.append(run_correct)
    def next_concept():
        try:
            app.progress["step_index"]=2
            app.frames[gui.LearningPage].refresh(); app.update()
        except: pass
        cap("12 LEARNING — Concept: len() & type()")
    seq.append(next_concept)
    def prog():
        try: app.show_frame(gui.ProgressPage)
        except: pass
        cap("13 PROGRESS — Dashboard (XP + streak)", dur=1100)
    seq.append(prog)
    def skill():
        try: app.show_frame(gui.SkillTreePage)
        except: pass
        cap("14 SKILL TREE — 1/9 Beginner done")
    seq.append(skill)
    def review():
        try: app.show_frame(gui.ReviewQueuePage)
        except: pass
        cap("15 REVIEW — Spaced repetition")
    seq.append(review)
    def drills():
        try: app.show_frame(gui.DrillHubPage)
        except: pass
        cap("16 DRILLS — Muscle memory")
    seq.append(drills)
    def daily():
        try: app.show_frame(gui.DailyChallengePage)
        except: pass
        cap("17 DAILY — Challenge + editor")
    seq.append(daily)
    def sandbox1():
        try: app.show_frame(gui.SandboxPage); app.update()
        except: pass
        cap("18 SANDBOX — Playground")
    seq.append(sandbox1)
    def sandbox2():
        try:
            sb = app.frames[gui.SandboxPage]
            if hasattr(sb,"_editor"):
                sb._editor.delete("1.0","end")
                sb._editor.insert("1.0","print('Hello Lumixa')\nfor i in range(3):\n    print(i)")
                app.update(); time.sleep(0.2)
                if hasattr(sb,"_run_code"):
                    try: sb._run_code()
                    except: pass
                app.update()
        except Exception as e:
            print(f"[warn] sandbox2 {e}")
        cap("19 SANDBOX — Run -> output", dur=1100)
    seq.append(sandbox2)
    def badges():
        try: app.show_frame(gui.BadgesPage)
        except: pass
        cap("20 BADGES — 23 badges")
    seq.append(badges)
    def settings():
        try: app.show_frame(gui.SettingsPage)
        except: pass
        cap("21 SETTINGS — Backup & restore")
    seq.append(settings)
    def planning():
        try: app.show_frame(gui.PlanningGuidePage)
        except: pass
        cap("22 PLANNING — 2/4/6 week tracks", dur=args.hold_last)
    seq.append(planning)

    idx=[0]
    def run_next():
        if idx[0]>=len(seq):
            finish()
            return
        fn = seq[idx[0]]; idx[0]+=1
        try: 
            result = fn()
            # if cap returned False (black), retry same label once after delay
            if result is False:
                print(f"[retry] black frame for step {idx[0]}, retrying in 600ms")
                idx[0]-=1  # step back to retry same? Actually next call will be same index-1, so adjust
                # we already incremented, so decrement to retry
                # if we retried, next run_next will call same fn again
                app.after(600, run_next)
                return
        except Exception as e:
            print(f"[error] step {idx[0]} {e}")
            import traceback; traceback.print_exc()
        app.after(820, run_next)

    def finish():
        print(f"\nCaptured {len(frames)} frames (filtered black).")
        if not frames:
            print("[error] no frames"); 
            try: app.destroy()
            except: pass
            restore_backup(); sys.exit(1)
        try:
            frames[0].save(preview_path,"PNG",optimize=True)
            print(f"Preview: {preview_path} {frames[0].width}x{frames[0].height}")
        except Exception as e:
            print(f"[warn] preview {e}")
        try:
            first = frames[0].convert("P", palette=Image.ADAPTIVE, colors=256)
            rest = [f.convert("P", palette=Image.ADAPTIVE, colors=256) for f in frames[1:]]
            first.save(out_path, save_all=True, append_images=rest, duration=durations, loop=0, optimize=True, disposal=2)
            kb = out_path.stat().st_size/1024
            print(f"GIF: {out_path} {kb:.1f} KB {len(frames)} frames")
            for i,l in enumerate(labels): print(f"  {i+1:02d} {l}")
            if kb>9500: print("[tip] >9.5MB — use --width 800")
        except Exception as e:
            print(f"[error] save {e}"); import traceback; traceback.print_exc()
        finally:
            try: app.after(900, app.destroy)
            except:
                try: app.destroy()
                except: pass
            app.after(1200, restore_backup)

    app.after(1000, run_next)
    app.mainloop()
    print("Clean tour done — starts officially open, no black, no terminal")
    if BACKUP.exists(): restore_backup()

if __name__=="__main__":
    main()
