"""
HQ Tour GIF — full app, high quality, no crop

Fixes:
- No downscale blur: captures at native 1060x740 (width=0) or 960 if needed
- Global palette (not per-frame ADAPTIVE) for consistent colors + dithering
- Thinner overlay (22px bottom) or optional no overlay to show full app
- Ensures window fits screen 1280x800 and is centered
- Waits for render, filters black frames
"""
import argparse, time, sys, shutil
from pathlib import Path
from PIL import Image, ImageGrab, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
PROGRESS = ROOT / "learning_progress.json"
BACKUP = ROOT / "learning_progress.json.bak_hq"

def parse_args():
    p = argparse.ArgumentParser(description="HQ tour GIF")
    p.add_argument("--output", default="demo.gif")
    p.add_argument("--preview", default="demo_preview.png")
    p.add_argument("--duration", type=int, default=1100, help="ms per frame (longer for readability)")
    p.add_argument("--width", type=int, default=0, help="0=original 1060, 960=high, 800=small")
    p.add_argument("--hold-last", type=int, default=3000)
    p.add_argument("--no-overlay", action="store_true", help="if set, skip bottom bar to show full app")
    return p.parse_args()

def is_black(img):
    try:
        small = img.resize((32,32))
        if small.mode != "RGB": small = small.convert("RGB")
        pixels = list(small.getdata())
        avg = sum(sum(px)/3 for px in pixels)/len(pixels)
        black = sum(1 for px in pixels if max(px)<30)/len(pixels)
        return avg < 12 and black > 0.85
    except: return False

def grab_clean(app, retries=4):
    for attempt in range(retries):
        try:
            app.update_idletasks(); app.update()
            time.sleep(0.14)
            x,y = app.winfo_rootx(), app.winfo_rooty()
            w,h = app.winfo_width(), app.winfo_height()
            if w < 200 or h < 200:
                time.sleep(0.35); continue
            try:
                if not app.winfo_viewable():
                    time.sleep(0.3); continue
            except: pass
            img = ImageGrab.grab(bbox=(x,y,x+w,y+h))
            if is_black(img):
                if attempt < retries-1:
                    time.sleep(0.35); continue
                return None
            return img
        except Exception as e:
            if attempt < retries-1:
                time.sleep(0.35); continue
            print(f"[warn] grab {e}")
            return None
    return None

def add_overlay(img, label, idx, total, thin=True):
    try:
        draw = ImageDraw.Draw(img, "RGBA")
        w,h = img.size
        bar_h = 22 if thin else 36
        # semi-transparent bottom bar - thinner to show more app
        draw.rectangle([0, h-bar_h, w, h], fill=(15,23,42,210))
        # dots
        dot_r = 3
        gap = 12
        dots_w = total * gap
        start_x = (w - dots_w)//2
        y_dot = h - 9 if thin else h - 14
        for i in range(total):
            cx = start_x + i*gap + 4
            fill = (99,102,241) if i <= idx else (71,85,105)
            outline = (255,255,255) if i==idx else fill
            draw.ellipse([cx-dot_r, y_dot-dot_r, cx+dot_r, y_dot+dot_r], fill=fill, outline=outline, width=1)
        try: font = ImageFont.load_default()
        except: font = None
        counter = f"{idx+1:02d}/{total:02d}"
        draw.text((8, h-17 if thin else h-28), counter, fill=(148,163,184), font=font)
        txt = label[:72]
        try:
            bbox = draw.textbbox((0,0), txt, font=font)
            tw = bbox[2]-bbox[0]
        except: tw = len(txt)*6
        tx = max(50, (w - tw)//2)
        draw.text((tx, h-17 if thin else h-28), txt, fill=(226,232,240), font=font)
        # top bar thin
        draw.rectangle([0,0,w,18], fill=(15,23,42,160))
        draw.text((8,2), "Lumixa \u2022 Polycode Coach \u2022 Full Tour (HQ)", fill=(148,163,184), font=font)
        return img
    except Exception as e:
        print(f"[warn] overlay {e}")
        return img

def ensure_backup():
    if PROGRESS.exists():
        try: shutil.copy2(PROGRESS, BACKUP); print(f"[backup] -> {BACKUP.name}")
        except Exception as e: print(f"[warn] backup {e}")

def restore_backup():
    if BACKUP.exists():
        try: shutil.copy2(BACKUP, PROGRESS); BACKUP.unlink(missing_ok=True); print("[restore] progress restored")
        except Exception as e: print(f"[warn] restore {e}")

def main():
    args = parse_args()
    out_path = ROOT / args.output
    preview_path = ROOT / args.preview
    if out_path.exists():
        try: shutil.copy2(out_path, ROOT / "demo_hq_backup.gif"); print("[backup] old demo -> demo_hq_backup.gif")
        except: pass
    ensure_backup()
    import learn_python_gui as gui

    print("=== HQ Tour GIF — full app, high quality ===")
    print(f"Output: {out_path} width={'original' if args.width==0 else args.width} dur={args.duration} no_overlay={args.no_overlay}")
    print("Keep window fully visible!\n")

    app = gui.PythonLearnerApp()
    app.update_idletasks(); app.update()
    # Center window on screen 1280x800
    try:
        # Use 1060x740 which fits 1280x800 with margin
        app.geometry("1060x740")
        app.update()
        # Center
        sw = app.winfo_screenwidth()
        sh = app.winfo_screenheight()
        w = 1060; h = 740
        x = (sw - w)//2
        y = (sh - h)//2 - 10  # slight up for taskbar
        # Ensure visible
        x = max(0, x); y = max(0, y)
        app.geometry(f"{w}x{h}+{x}+{y}")
        app.deiconify(); app.lift()
        app.attributes("-topmost", True)
        app.update()
        app.after(500, lambda: app.attributes("-topmost", False))
        for _ in range(20):
            app.update()
            if app.winfo_viewable() and app.winfo_width() > 300:
                break
            time.sleep(0.12)
        time.sleep(0.9)
    except Exception as e:
        print(f"[warn] window setup {e}")

    # Fresh state
    try:
        app.progress["language"] = None
        app.progress["level"] = ""
        app.progress["lesson_index"] = 0
        app.progress["step_index"] = 0
        app.progress["completed_lessons"] = []
        app.progress["completed_steps"] = {}
        app.progress["completed_by_level"] = {}
        app.progress["xp"] = 12
        app._update_nav_visibility()
        app._update_title_for_language()
        app.show_frame(gui.LanguageSelectionPage)
        app.update(); time.sleep(0.4)
    except Exception as e:
        print(f"[warn] init {e}")

    # Warmup until not black
    print("[warmup] waiting for window...")
    for attempt in range(12):
        img = grab_clean(app)
        if img is not None and not is_black(img):
            print(f"[warmup] ready {img.size} after {attempt+1} tries")
            break
        print(f"[warmup] try {attempt+1}/12 black, retry")
        time.sleep(0.35)
        app.update()
    else:
        print("[warn] warmup still black")

    frames = []
    durations = []
    labels = []
    total_est = 22

    def cap(label, dur=None):
        app.update_idletasks(); app.update()
        time.sleep(0.12)
        img = grab_clean(app)
        if img is None or is_black(img):
            print(f"[skip BLACK] {label}")
            return False
        # Resize only if width requested and different
        if args.width and args.width>0 and img.width != args.width:
            ratio = args.width / img.width
            new_h = int(img.height * ratio)
            # Use LANCZOS for downscale, NEAREST for upscale - but we only downscale
            img = img.resize((args.width, new_h), Image.LANCZOS)
        # else keep original 1060x740 for HQ
        idx = len(frames)
        if not args.no_overlay:
            img = add_overlay(img, label, idx, total_est, thin=True)
        frames.append(img)
        d = dur if dur is not None else args.duration
        durations.append(d)
        labels.append(label)
        print(f"[{len(frames):02d}/{total_est}] {label} -> {img.width}x{img.height} dur={d}")
        return True

    seq = []
    seq.append(lambda: cap("01 OPEN — Main Menu (choose language)"))
    seq.append(lambda: cap("02 OPEN — Main Menu (hold)", dur=1400))
    def pick_python():
        try:
            app.set_language("python")
            app.show_frame(gui.WelcomePage); app.update()
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
        cap("06 RESULT — Placed Beginner -> Start Learning", dur=1400)
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
        cap("09 PRACTICE — Typing… print('Hello", dur=500)
    seq.append(type_a)
    def type_b():
        try:
            sk = gui.step_key("Beginner",0,1)
            app.progress["draft_code"][sk]="print('Hello World')"
            app.frames[gui.LearningPage].refresh(); app.update()
        except: pass
        cap("10 PRACTICE — Typing… print('Hello World')", dur=600)
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
        cap("11 PRACTICE — Run -> Correct! +5 XP", dur=1300)
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
        cap("13 PROGRESS — Dashboard (XP + streak)", dur=1300)
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
                app.update(); time.sleep(0.25)
                if hasattr(sb,"_run_code"):
                    try: sb._run_code()
                    except: pass
                app.update()
        except Exception as e:
            print(f"[warn] sandbox2 {e}")
        cap("19 SANDBOX — Run -> output Hello 0 1 2", dur=1300)
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
            if result is False:
                print(f"[retry] black at step {idx[0]}, retry 600ms")
                idx[0]-=1
                app.after(600, run_next)
                return
        except Exception as e:
            print(f"[error] step {idx[0]} {e}")
            import traceback; traceback.print_exc()
        app.after(850, run_next)

    def finish():
        print(f"\nCaptured {len(frames)} frames HQ.")
        if not frames:
            print("[error] no frames")
            try:
                app.destroy()
            except:
                pass
            restore_backup()
            sys.exit(1)
        try:
            frames[0].save(preview_path,"PNG",optimize=True)
            print(f"Preview: {preview_path} {frames[0].width}x{frames[0].height}")
        except Exception as e:
            print(f"[warn] preview {e}")
        try:
            # HQ palette: build global palette from all frames for consistent colors
            # Create a merged image for palette generation (sample every 2nd frame to keep memory low)
            print("[palette] building global palette...")
            # Combine frames into one tall image for palette extraction
            # Use first 6 frames to sample palette (covers dark/light themes)
            sample_frames = frames[::2]  # ~11 frames sample
            # Create a mosaic for palette
            # Instead, quantize using median cut globally: convert first frame to RGB and quantize, then remap others
            # Better: use PIL's quantize with method 2 (median cut) on a montage
            # Build montage
            max_w = max(f.width for f in sample_frames)
            total_h = sum(f.height for f in sample_frames)
            # Cap montage size to avoid huge memory: resize samples to half if needed
            montage = Image.new("RGB", (max_w, min(total_h, 4000)))
            y = 0
            for f in sample_frames:
                if y + f.height > montage.height: break
                # paste
                rgb = f.convert("RGB")
                montage.paste(rgb, (0, y))
                y += f.height
            # Quantize montage to 256 colors
            paletted_montage = montage.quantize(colors=256, method=Image.MEDIANCUT, dither=Image.NONE)
            palette = paletted_montage.getpalette()
            # Apply palette to all frames with dithering
            quantized_frames = []
            for f in frames:
                # Quantize using global palette
                q = f.convert("RGB").quantize(palette=paletted_montage, dither=Image.FLOYDSTEINBERG)
                quantized_frames.append(q)
            first = quantized_frames[0]
            rest = quantized_frames[1:]
            # Save with global palette
            first.save(out_path, save_all=True, append_images=rest, duration=durations, loop=0, optimize=False, disposal=2)
            kb = out_path.stat().st_size/1024
            print(f"GIF HQ: {out_path} {kb:.1f} KB {len(frames)} frames {frames[0].width}x{frames[0].height}")
            for i,l in enumerate(labels): print(f"  {i+1:02d} {l}")
            if kb > 10000:
                print("[tip] >10MB — consider --width 960 to reduce")
            elif kb < 4000:
                print("[tip] HQ good size for GitHub (<8MB)")
        except Exception as e:
            print(f"[error] save HQ {e}"); import traceback; traceback.print_exc()
            # Fallback: old per-frame method
            try:
                first = frames[0].convert("P", palette=Image.ADAPTIVE, colors=256)
                rest = [f.convert("P", palette=Image.ADAPTIVE, colors=256) for f in frames[1:]]
                first.save(out_path, save_all=True, append_images=rest, duration=durations, loop=0, optimize=True, disposal=2)
                print(f"[fallback] saved with per-frame palette {out_path.stat().st_size/1024:.1f} KB")
            except Exception as e2:
                print(f"[error] fallback also failed {e2}")
        finally:
            try: app.after(900, app.destroy)
            except:
                try: app.destroy()
                except: pass
            app.after(1200, restore_backup)

    app.after(1000, run_next)
    app.mainloop()
    print("HQ done — full app, high quality")
    if BACKUP.exists(): restore_backup()

if __name__=="__main__":
    main()
