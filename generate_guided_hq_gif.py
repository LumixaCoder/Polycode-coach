"""
Guided HQ Tour GIF — GitHub-Optimal (900px) + cursor guide.

What it does:
 - Captures Lumixa at 1060x740 then LANCZOS downscale to 900px (GitHub README max ~838px, crisp without browser blur)
 - Global palette (median-cut montage) + Floyd-Steinberg dithering for sharp colors
 - Draws a realistic cursor arrow + halo + click ripple at the key UI element per frame
 - Draws a callout bubble with an arrow that explains "where everything is"
 - Thin top/bottom overlay with progress dots (does not hide app)
 - Covers MORE of the project: 28 frames including Debug->Coach->Fix, Final Project, XP heatmap, Skill Tree,
   Sandbox Project Cards, theme toggle, etc.

Run (GitHub optimal defaults):
  python generate_guided_hq_gif.py
  python generate_guided_hq_gif.py --output demo.gif --width 900 --duration 1100
  python generate_guided_hq_gif.py --width 0  # native 1060 (larger, heavier)
  python generate_guided_hq_gif.py --no-cursor  # plain HQ without cursor (debug)

If ImageGrab fails (headless/RDP) it falls back to a synthetic high-quality mock
so you still get a demo.gif with cursor guide (not black). For real screenshots, run locally with window visible.
Target: 900x~629, 27-28 frames, ~3.5-5.5 MB, 1100ms/frame, loop 0 — perfect for GitHub README.
"""
import argparse, time, sys, shutil, math, random, warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning)
from pathlib import Path
from PIL import Image, ImageGrab, ImageDraw, ImageFont, ImageFilter, ImageEnhance
# DPI awareness for Windows — ensures winfo_rootx matches ImageGrab physical pixels
try:
    import ctypes
    try: ctypes.windll.shcore.SetProcessDpiAwareness(2)  # Per-monitor DPI aware
    except: 
        try: ctypes.windll.shcore.SetProcessDpiAwareness(1)
        except: ctypes.windll.user32.SetProcessDPIAware()
except: pass

ROOT = Path(__file__).resolve().parent
PROGRESS = ROOT / "learning_progress.json"
BACKUP = ROOT / "learning_progress.json.bak_guided_hq"
OUT_DEFAULT = ROOT / "demo.gif"
PREVIEW_DEFAULT = ROOT / "demo_preview.png"

# ------------------------------------------------------------------
# Args
# ------------------------------------------------------------------
def parse_args():
    p = argparse.ArgumentParser(description="Guided HQ tour GIF with cursor — GitHub optimal (900px)")
    p.add_argument("--output", default="demo.gif")
    p.add_argument("--preview", default="demo_preview.png")
    p.add_argument("--duration", type=int, default=1100, help="ms per normal frame")
    p.add_argument("--width", type=int, default=900, help="900=GitHub optimal, 960=high, 0=native 1060, 800=small (GitHub max ~838px)")
    p.add_argument("--hold-last", type=int, default=3200, help="ms hold on last frame")
    p.add_argument("--no-cursor", action="store_true", help="disable cursor overlay (plain HQ)")
    p.add_argument("--no-overlay", action="store_true", help="disable top/bottom bars")
    p.add_argument("--dpi-fix", action="store_true", help="unused legacy flag")
    return p.parse_args()

# ------------------------------------------------------------------
# Font helpers — try to load a sharp TTF, fallback to default
# ------------------------------------------------------------------
def load_font(size, bold=False):
    # Try Segoe UI (Windows), then Arial, then load_default
    candidates = []
    if bold:
        candidates = ["segoeuib.ttf", "arialbd.ttf", "DejaVuSans-Bold.ttf"]
    else:
        candidates = ["segoeui.ttf", "arial.ttf", "DejaVuSans.ttf"]
    # Also check Windows fonts folder
    font_dirs = [Path("C:/Windows/Fonts"), Path("/usr/share/fonts"), Path(str(ROOT))]
    for name in candidates:
        for d in font_dirs:
            fp = d / name
            if fp.exists():
                try:
                    return ImageFont.truetype(str(fp), size)
                except: pass
        # try direct name (Pillow can find via system)
        try:
            return ImageFont.truetype(name, size)
        except: pass
    try:
        return ImageFont.load_default()
    except:
        return None

FONT_SM = load_font(11, bold=False)
FONT_MD = load_font(13, bold=False)
FONT_MD_BOLD = load_font(13, bold=True)
FONT_LG_BOLD = load_font(15, bold=True)
FONT_CALL = load_font(12, bold=False)
FONT_CALL_BOLD = load_font(12, bold=True)
FONT_COUNT = load_font(11, bold=True)

# ------------------------------------------------------------------
# Image grab helpers with black-frame filtering (like HQ)
# ------------------------------------------------------------------
def is_black(img):
    try:
        small = img.resize((32,32))
        if small.mode != "RGB": small = small.convert("RGB")
        # use get_flattened_data if available (Pillow 13+), fallback to getdata
        try:
            pixels = list(small.get_flattened_data())
            # get_flattened_data returns flat bytes; chunk into RGB tuples
            if pixels and isinstance(pixels[0], int):
                pixels = [tuple(pixels[i:i+3]) for i in range(0, len(pixels), 3)]
            else:
                pixels = list(small.getdata())
        except:
            pixels = list(small.getdata())
        avg = sum(sum(px)/3 for px in pixels)/len(pixels)
        black = sum(1 for px in pixels if max(px) < 30)/len(pixels)
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
                    time.sleep(0.30); continue
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

# ------------------------------------------------------------------
# Synthetic fallback: create a high-quality mock frame if grab fails
# (so demo.gif is never black and still shows cursor guide)
# ------------------------------------------------------------------
def make_synthetic_frame(label, idx, total, width=1060, height=740, cursor=None, callout=None):
    # Create a gradient background like app's dark theme + panels to look classy
    img = Image.new("RGBA", (width, height), (15,23,42,255))
    draw = ImageDraw.Draw(img, "RGBA")
    # subtle vertical gradient
    for y in range(height):
        t = y/height
        r = int(15 + (30-15)*t)
        g = int(23 + (41-23)*t)
        b = int(42 + (59-42)*t)
        draw.line([(0,y),(width,y)], fill=(r,g,b))
    # Add a centered card to mimic app UI
    margin = 32
    card_x0, card_y0 = margin, 48
    card_x1, card_y1 = width-margin, height-56
    # card shadow
    draw.rounded_rectangle([card_x0+3, card_y0+6, card_x1+3, card_y1+6], radius=18, fill=(0,0,0,38))
    draw.rounded_rectangle([card_x0, card_y0, card_x1, card_y1], radius=18, fill=(30,41,59,255), outline=(71,85,105,120))
    # header bar
    draw.rounded_rectangle([card_x0, card_y0, card_x1, card_y0+64], radius=18, fill=(51,65,85,255))
    # fix bottom corners of header (redraw bottom edge rect)
    draw.rectangle([card_x0, card_y0+40, card_x1, card_y0+64], fill=(51,65,85))
    # title
    try: font_title = load_font(20, bold=True)
    except: font_title = FONT_LG_BOLD
    draw.text((card_x0+22, card_y0+18), label.split("—")[-1].strip()[:56], fill=(248,250,252), font=font_title)
    # placeholder icon + text
    draw.rounded_rectangle([card_x0+22, card_y0+86, card_x0+86, card_y0+150], radius=12, fill=(71,85,105))
    # lines mimicking content
    y = card_y0+96
    for w in [420, 380, 320, 260]:
        draw.rounded_rectangle([110, y, 110+w, y+10], radius=5, fill=(100,116,139,120))
        y += 18
    # editor mock at bottom
    ed_x0, ed_y0 = card_x0+22, card_y1-170
    ed_x1, ed_y1 = card_x1-22, card_y1-22
    draw.rounded_rectangle([ed_x0, ed_y0, ed_x1, ed_y1], radius=12, fill=(15,23,42), outline=(71,85,105))
    draw.text((ed_x0+12, ed_y0+10), "print('Hello World')\nfor i in range(3):\n    print(i)", fill=(226,232,240), font=FONT_SM)
    # output mock
    draw.rounded_rectangle([ed_x1-220, ed_y0+10, ed_x1-10, ed_y1-10], radius=8, fill=(30,41,59), outline=(71,85,105,80))
    draw.text((ed_x1-210, ed_y0+16), "▶ Output\nHello World\n0\n1\n2", fill=(94,234,212), font=FONT_SM)
    return img.convert("RGB")

# ------------------------------------------------------------------
# Cursor drawing (high-quality)
# ------------------------------------------------------------------
def draw_halo(img, cx, cy, radius=36, color=(99,102,241,70)):
    """Soft halo behind cursor to draw attention."""
    if cx is None or cy is None:
        return
    draw = ImageDraw.Draw(img, "RGBA")
    # outer glow (largest, most transparent)
    for r, alpha in [(radius+18, 18), (radius+10, 32), (radius, 70)]:
        bbox = [cx-r, cy-r, cx+r, cy+r]
        draw.ellipse(bbox, fill=(color[0], color[1], color[2], alpha), outline=None)

def draw_cursor_arrow(img, cx, cy, click=False, scale=1.0):
    """Draw a crisp macOS-style arrow with shadow at (cx,cy)=tip."""
    if cx is None or cy is None:
        return
    draw = ImageDraw.Draw(img, "RGBA")
    # Arrow shape relative to tip (tip at 0,0)
    # Classic arrow ~ 20x24
    # Points in order around shape
    base = [(0,0), (15,7), (7,11), (9,18), (4,16.5), (0,10)]  # tip at origin
    s = scale
    pts = [(cx + x*s, cy + y*s) for x,y in base]
    # shadow (offset 1.5px)
    shadow = [(x+1.7, y+1.7) for x,y in pts]
    draw.polygon(shadow, fill=(0,0,0,92))
    # main white fill with dark outline
    draw.polygon(pts, fill=(255,255,255,255), outline=(15,23,42,255))
    # Also draw a thin inner outline for crispness (slightly inset)
    # Add highlight dot at base? Not needed
    if click:
        # ripple + inner dot
        # inner purple dot at tip+6,6
        dot_x, dot_y = cx+3.5, cy+3.5
        draw.ellipse([dot_x-5, dot_y-5, dot_x+5, dot_y+5], fill=(99,102,241,255), outline=(255,255,255,255), width=2)
        # ripples around cursor tip
        for r, a, w in [(16, 72, 2), (26, 38, 2), (34, 16, 1.5)]:
            draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(99,102,241, a), width=int(w))
        # also a small glow at click point
        draw.ellipse([cx-9, cy-9, cx+9, cy+9], fill=(99,102,241,28))

def draw_callout(img, cx, cy, text, sub=None):
    """Draw a callout bubble offset from cursor with leader line."""
    if cx is None or cy is None or not text:
        return
    draw = ImageDraw.Draw(img, "RGBA")
    W,H = img.size
    # Measure text
    font = FONT_CALL
    font_b = FONT_CALL_BOLD
    # support "heading • detail" split by "→" or "•"
    # We'll just render single line; if too long, wrap manually
    max_chars = 44
    txt = text.strip()
    # Wrap if needed
    lines = []
    if len(txt) > max_chars:
        words = txt.split()
        cur = ""
        for w in words:
            if len(cur) + len(w) + 1 <= max_chars:
                cur = (cur + " " + w).strip()
            else:
                if cur: lines.append(cur)
                cur = w
        if cur: lines.append(cur)
    else:
        lines = [txt]
    if sub:
        # add second line smaller
        lines.append(sub)

    # compute box size
    pad_x, pad_y = 12, 9
    line_h = 16
    # measure widest line
    max_w = 0
    for l in lines:
        try:
            bbox = draw.textbbox((0,0), l, font=font if l != lines[0] else font_b)
            w = bbox[2]-bbox[0]
        except:
            w = len(l)*7
        max_w = max(max_w, w)
    box_w = max_w + pad_x*2 + 8  # 8 for accent strip
    box_h = len(lines)*line_h + pad_y*2 + (2 if len(lines)>1 else 0)
    # Decide position: offset to bottom-right normally, flip if out of bounds
    # default: to right and slightly below cursor
    bx = cx + 22
    by = cy + 18
    # Flip horizontally if would go off right
    if bx + box_w > W - 10:
        bx = cx - box_w - 22
    # Flip vertically if off bottom (keep above bottom bar)
    bottom_limit = H - 44
    if by + box_h > bottom_limit:
        by = cy - box_h - 22
    # Clamp top
    top_limit = 28
    if by < top_limit:
        by = top_limit
    # Clamp left
    if bx < 8:
        bx = 8
    if bx + box_w > W - 8:
        bx = W - box_w - 8

    # Draw shadow
    draw.rounded_rectangle([bx+2.5, by+2.5, bx+box_w+2.5, by+box_h+2.5], radius=10, fill=(0,0,0,42))
    # Main bubble — white with subtle border
    draw.rounded_rectangle([bx, by, bx+box_w, by+box_h], radius=10, fill=(255,255,255,250), outline=(203,213,225,120), width=1)
    # Left accent bar (indigo)
    draw.rounded_rectangle([bx, by, bx+5, by+box_h], radius=5, fill=(99,102,241,255))
    # Icon circle maybe? Add a small target icon on accent?
    # Text lines
    y_text = by + pad_y
    for i, l in enumerate(lines):
        use_b = font_b if i==0 else font
        col = (15,23,42,255) if i==0 else (51,65,85,255)
        draw.text((bx+14, y_text), l, fill=col, font=use_b)
        y_text += line_h
    # Leader line from cursor tip to bubble edge
    # Find closest point on bubble rect to cursor
    closest_x = max(bx, min(cx, bx+box_w))
    closest_y = max(by, min(cy, by+box_h))
    # Don't draw line if cursor inside bubble (shouldn't happen)
    dist = math.hypot(cx - closest_x, cy - closest_y)
    if dist > 8:
        # draw line with slight curve? straight is fine
        draw.line([cx, cy, closest_x, closest_y], fill=(99,102,241,230), width=2)
        # small dot at bubble edge
        draw.ellipse([closest_x-3, closest_y-3, closest_x+3, closest_y+3], fill=(99,102,241), outline=(255,255,255), width=1)
    # tiny dot at cursor already drawn later

def add_bars(img, label, idx, total, thin=True):
    """Top + bottom bars (HQ style)."""
    draw = ImageDraw.Draw(img, "RGBA")
    W,H = img.size
    bar_h = 24 if thin else 36
    # bottom bar
    draw.rectangle([0, H-bar_h, W, H], fill=(15,23,42,218))
    # progress dots
    dot_r = 3.5
    gap = 12
    dots_w = total * gap
    start_x = (W - dots_w)//2
    y_dot = H - 9 if thin else H - 15
    for i in range(total):
        cx = start_x + i*gap + gap//2
        if i == idx:
            fill = (129,140,248)
            outline = (255,255,255)
            r = 4.2
        elif i < idx:
            fill = (99,102,241)
            outline = (99,102,241)
            r = dot_r
        else:
            fill = (71,85,105)
            outline = (71,85,105)
            r = dot_r
        draw.ellipse([cx-r, y_dot-r, cx+r, y_dot+r], fill=fill, outline=outline, width=1 if i==idx else 0)
    # fonts
    try:
        small_font = FONT_SM
        med_font = FONT_MD
    except:
        small_font = ImageFont.load_default()
        med_font = small_font
    # step counter bottom-left
    counter = f"{idx+1:02d}/{total:02d}"
    draw.text((10, H-17 if thin else H-28), counter, fill=(148,163,184), font=small_font)
    # centered label
    txt = label[:74]
    try:
        bbox = draw.textbbox((0,0), txt, font=small_font)
        tw = bbox[2]-bbox[0]
    except:
        tw = len(txt)*6
    tx = max(56, (W - tw)//2)
    draw.text((tx, H-17 if thin else H-28), txt, fill=(226,232,240), font=small_font)
    # top bar
    draw.rectangle([0,0,W,22], fill=(15,23,42,170))
    draw.text((10,3), "Lumixa  •  Polycode Coach  •  Full Tour (HQ + Guided)", fill=(148,163,184), font=small_font)
    # also tiny lumixa branding left pad?
    return img

def add_guided_overlay(img, label, idx, total, cursor_frac=None, cursor_px=None,
                       callout=None, callout_sub=None, click=False, thin=True, no_cursor=False, no_bars=False):
    """Combine bars + halo + cursor + callout onto img. Returns new RGB image."""
    # Ensure RGBA for compositing
    if img.mode != "RGBA":
        img = img.convert("RGBA")
    W,H = img.size
    # Work copy
    base = img.copy()
    # Bars first (so cursor draws on top)
    if not no_bars:
        base = add_bars(base, label, idx, total, thin=thin)

    # Determine cursor pixel coords
    cx = cy = None
    if not no_cursor:
        if cursor_px is not None:
            cx, cy = cursor_px
            # clamp
            cx = max(0, min(W-1, int(cx)))
            cy = max(0, min(H-1, int(cy)))
        elif cursor_frac is not None:
            fx, fy = cursor_frac
            cx = int(W * fx)
            cy = int(H * fy)
            # adjust for bars: ensure not hidden under bottom bar
            if cy > H-32:
                cy = H-42
            if cy < 24:
                cy = 30

        # Draw halo first, then callout, then cursor (topmost)
        if cx is not None:
            # halo soft (behind callout)
            overlay = Image.new("RGBA", (W,H), (0,0,0,0))
            draw_halo(overlay, cx, cy, radius=32)
            base = Image.alpha_composite(base, overlay)
            # callout next
            if callout:
                # create temp overlay to composite callout (since draw_callout uses RGBA)
                tmp = Image.new("RGBA", (W,H), (0,0,0,0))
                # need to draw callout onto tmp then composite
                # but draw_callout expects an image to draw onto; we can draw onto tmp's Draw
                # We'll instead draw callout directly onto base (it uses ImageDraw with RGBA, safe)
                # So we call draw_callout on base
                draw_callout(base, cx, cy, callout, sub=callout_sub)
            # cursor last
            cursor_layer = Image.new("RGBA", (W,H), (0,0,0,0))
            draw_cursor_arrow(cursor_layer, cx, cy, click=click, scale=1.0)
            base = Image.alpha_composite(base, cursor_layer)

    # Convert back to RGB for GIF (no alpha)
    return base.convert("RGB")

# ------------------------------------------------------------------
# Progress backup
# ------------------------------------------------------------------
def ensure_backup():
    if PROGRESS.exists():
        try: shutil.copy2(PROGRESS, BACKUP); print(f"[backup] -> {BACKUP.name}")
        except Exception as e: print(f"[warn] backup {e}")

def restore_backup():
    if BACKUP.exists():
        try: shutil.copy2(BACKUP, PROGRESS); BACKUP.unlink(missing_ok=True); print("[restore] progress restored")
        except Exception as e: print(f"[warn] restore {e}")

# ------------------------------------------------------------------
# Dynamic widget finder (optional, for pixel-perfect cursor)
# ------------------------------------------------------------------
def find_center_of_text(app, cls, needle):
    """Search inside app.frames[cls] for any widget with text containing needle."""
    try:
        frm = app.frames.get(cls)
        if not frm: return None
        found = []
        def rec(w):
            try:
                # check text via cget
                if "text" in w.keys():
                    try:
                        txt = str(w.cget("text"))
                        if needle.lower() in txt.lower():
                            found.append(w)
                            return True
                    except: pass
                # also check for tk.Button with child label? ignore
            except: pass
            try:
                for ch in w.winfo_children():
                    if rec(ch): return True
            except: pass
            return False
        rec(frm)
        if not found:
            return None
        w = found[0]
        if not w.winfo_exists(): return None
        # ensure mapped
        try:
            ax, ay = app.winfo_rootx(), app.winfo_rooty()
            wx, wy = w.winfo_rootx(), w.winfo_rooty()
            ww, wh = w.winfo_width(), w.winfo_height()
            if ww < 4 or wh < 4:
                return None
            return (wx - ax + ww//2, wy - ay + wh//2)
        except:
            return None
    except:
        return None
    return None

def find_editor_center(app, cls):
    try:
        frm = app.frames.get(cls)
        if not frm: return None
        # Look for SyntaxEditor instance
        import learn_python_gui as gui
        target = None
        def rec(w):
            nonlocal target
            if target: return
            # Check class name
            try:
                if w.__class__.__name__ == "SyntaxEditor":
                    target = w
                    return
            except: pass
            try:
                for ch in w.winfo_children():
                    rec(ch)
                    if target: return
            except: pass
        rec(frm)
        if target:
            ax, ay = app.winfo_rootx(), app.winfo_rooty()
            wx, wy = target.winfo_rootx(), target.winfo_rooty()
            ww, wh = target.winfo_width(), target.winfo_height()
            if ww < 10: return None
            return (wx - ax + ww//2, wy - ay + 38)  # near top of editor
    except: pass
    return None

# ------------------------------------------------------------------
# Main
# ------------------------------------------------------------------
def main():
    # Fix Windows cp1252 console for unicode arrows/checkmarks
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except: pass
    args = parse_args()
    out_path = ROOT / args.output
    preview_path = ROOT / args.preview
    if out_path.exists():
        try: shutil.copy2(out_path, ROOT / "demo_guided_backup.gif"); print("[backup] old demo -> demo_guided_backup.gif")
        except: pass
    ensure_backup()
    import learn_python_gui as gui

    print("=== Guided HQ Tour GIF — full app + cursor (GitHub 900px) ===")
    print(f"Output: {out_path}  width={'native' if args.width==0 else args.width}  dur={args.duration}  no_cursor={args.no_cursor}")
    print("Keep window fully visible! Centered 1060x740.\n")

    app = gui.PythonLearnerApp()
    app.update_idletasks(); app.update()
    # Disable welcome help popup for clean recording
    try: app.progress["show_welcome_help"] = False
    except: pass
    # Center window — keep topmost ON for entire capture so VS Code never covers it
    try:
        app.geometry("1060x740")
        app.update()
        sw = app.winfo_screenwidth(); sh = app.winfo_screenheight()
        w,h = 1060,740
        x = (sw - w)//2
        y = (sh - h)//2 - 10
        x = max(0,x); y = max(0,y)
        app.geometry(f"{w}x{h}+{x}+{y}")
        app.deiconify(); app.lift()
        try: app.focus_force()
        except: pass
        app.attributes("-topmost", True)
        app.update()
        # Do NOT drop topmost — keep it pinned above VS Code the whole tour
        # Re-assert every 400ms for first 2s to beat window manager
        for _ in range(5):
            app.lift(); app.attributes("-topmost", True); app.update(); time.sleep(0.15)
        for _ in range(22):
            app.update()
            if app.winfo_viewable() and app.winfo_width() > 300:
                break
            time.sleep(0.12)
        time.sleep(0.9)
        # Verify we have focus before warmup
        try:
            import ctypes
            hwnd = ctypes.windll.user32.GetForegroundWindow()
            # SetForegroundWindow for Tk hwnd
            try: ctypes.windll.user32.SetForegroundWindow(app.winfo_id())
            except: pass
        except: pass
        app.lift(); app.attributes("-topmost", True); app.update()
    except Exception as e:
        print(f"[warn] window setup {e}")

    # Fresh demo state (clean startup)
    try:
        app.progress["language"] = None
        app.progress["level"] = ""
        app.progress["lesson_index"] = 0
        app.progress["step_index"] = 0
        app.progress["completed_lessons"] = []
        app.progress["completed_steps"] = {}
        app.progress["completed_by_level"] = {}
        app.progress["xp"] = 12
        app.progress["streak"] = 1
        # ensure dark theme for consistency
        app.progress["theme"] = "dark"
        app.theme_name = "dark"
        from learn_python_gui import THEMES
        app.theme = THEMES["dark"]
        app.configure(bg=app.theme["navbar_bg"])
        app._update_nav_visibility()
        app._update_title_for_language()
        # ensure sidebar refreshed
        try: app.sidebar.refresh()
        except: pass
        app.show_frame(gui.LanguageSelectionPage)
        app.update(); time.sleep(0.45)
    except Exception as e:
        print(f"[warn] init fresh {e}")

    # Warmup until not black
    print("[warmup] waiting for window...")
    for attempt in range(14):
        im = grab_clean(app)
        if im is not None and not is_black(im):
            print(f"[warmup] ready {im.size} after {attempt+1}")
            break
        print(f"[warmup] try {attempt+1}/14 retry")
        time.sleep(0.35); app.update()
    else:
        print("[warn] warmup still black — will use synthetic fallback for any failed grabs")

    frames = []
    durations = []
    labels = []
    total_est = 28  # for dots

    # Helper to capture with guided overlay
    # Uses closure over frames/durations/labels
    def cap(label, *, cursor_frac=None, callout=None, callout_sub=None, dur=None, click=False, finder=None):
        # Always re-assert topmost before each grab so VS Code never bleeds in
        try: app.lift(); app.attributes("-topmost", True); app.update_idletasks(); app.update()
        except: pass
        time.sleep(0.12)
        img = grab_clean(app)
        used_synthetic = False
        if img is None or is_black(img):
            print(f"[warn] grab failed for '{label}' — using synthetic mock")
            img = make_synthetic_frame(label, len(frames), total_est, width=1060, height=740, cursor=cursor_frac, callout=callout)
            used_synthetic = True
        # Optionally resize (keep HQ native unless width requested)
        if args.width and args.width>0 and img.width != args.width:
            ratio = args.width / img.width
            new_h = int(img.height * ratio)
            img = img.resize((args.width, new_h), Image.LANCZOS)
        # refine cursor pixel via dynamic finder if available and not synthetic
        cursor_px = None
        if finder is not None and not used_synthetic:
            try:
                px = finder(app, img)
                if px and len(px)==2:
                    # px is already image-relative (we computed wx-ax)
                    # need to scale if we resized img
                    if args.width and args.width>0:
                        # original width was ~1060, now args.width. Scale
                        orig_w = 1060
                        scale = args.width / orig_w
                        px = (px[0]*scale, px[1]*scale)
                    cursor_px = px
            except Exception as e:
                print(f"[warn] finder {e}")
        idx = len(frames)
        if args.no_cursor:
            # plain HQ bars only
            img = add_guided_overlay(img, label, idx, total_est, cursor_frac=None, cursor_px=None, callout=None, click=False, thin=True, no_cursor=True, no_bars=args.no_overlay)
        else:
            img = add_guided_overlay(img, label, idx, total_est, cursor_frac=cursor_frac, cursor_px=cursor_px, callout=callout, callout_sub=callout_sub, click=click, thin=True, no_cursor=False, no_bars=args.no_overlay)
        frames.append(img)
        d = dur if dur is not None else args.duration
        durations.append(d)
        labels.append(label)
        try:
            print(f"[{len(frames):02d}/{total_est}] {label} -> {img.width}x{img.height} dur={d}  cursor={cursor_frac or cursor_px}  {'SYNTH' if used_synthetic else 'GRAB'}")
        except UnicodeEncodeError:
            print(f"[{len(frames):02d}/{total_est}] {label.encode('ascii','replace').decode()} -> {img.width}x{img.height} dur={d}")
        return True

    # ------------------------------------------------------------------
    # Finder lambdas (capture precise button positions when possible)
    # ------------------------------------------------------------------
    def finder_python(app, img):
        return find_center_of_text(app, gui.LanguageSelectionPage, "Python")
    def finder_welcome_quiz(app, img):
        # Try "Placement Quiz" or "Start" or "Quiz"
        for needle in ["Start Quiz", "Take Quiz", "Placement Quiz", "Continue"]:
            p = find_center_of_text(app, gui.WelcomePage, needle)
            if p: return p
        return None
    def finder_survey_next(app, img):
        for needle in ["Next", "Submit", "Check"]:
            p = find_center_of_text(app, gui.SurveyPage, needle)
            if p: return p
        return None
    def finder_result_start(app, img):
        for needle in ["Start Learning", "Begin", "Learning"]:
            p = find_center_of_text(app, gui.ResultPage, needle)
            if p: return p
        return None
    def finder_learning_next(app, img):
        for needle in ["Next", "Continue", "Complete"]:
            p = find_center_of_text(app, gui.LearningPage, needle)
            if p: return p
        return None
    def finder_run(app, img):
        for needle in ["Run", "Check", "✓"]:
            p = find_center_of_text(app, gui.LearningPage, needle)
            if p: return p
        # fallback to editor center then offset to run button area (~+220, +70)
        ec = find_editor_center(app, gui.LearningPage)
        if ec:
            return (ec[0]+210, ec[1]+58)
        return None
    def finder_coach(app, img):
        for needle in ["Coach", "Hint", "Ask"]:
            p = find_center_of_text(app, gui.LearningPage, needle)
            if p: return p
        return None
    def finder_sandbox_run(app, img):
        for needle in ["Run", "►"]:
            p = find_center_of_text(app, gui.SandboxPage, needle)
            if p: return p
        return None

    # ------------------------------------------------------------------
    # Sequence — 28 frames, shows MORE of the project
    # ------------------------------------------------------------------
    seq = []

    # 01-02 Main Menu
    seq.append(lambda: cap("01 OPEN — Main Menu (choose language)", cursor_frac=(0.34,0.52), callout="Main Menu — Pick your language", callout_sub="Python or Java • per-language progress"))
    seq.append(lambda: cap("02 MENU — Hover Java (then Python)", cursor_frac=(0.66,0.52), callout="Java also available — same app, new lessons", callout_sub="Each language has its own track", dur=1200))
    def pick_python_step():
        try:
            app.set_language("python")
            app.show_frame(gui.WelcomePage); app.update()
        except: pass
        cap("03 PICKED Python → Welcome (roadmap)", cursor_frac=(0.54,0.74), callout="Python selected → Roadmap appears", callout_sub="Welcome shows your journey ahead", dur=1200, finder=finder_welcome_quiz)
    seq.append(pick_python_step)
    seq.append(lambda: (app.show_frame(gui.SurveyPage), app.update(), cap("04 SURVEY — Placement Quiz Q1/5", cursor_frac=(0.44,0.46), callout="Placement Quiz — 5 questions find level", callout_sub="Beginner / Intermediate / Advanced", finder=finder_survey_next))[2])
    seq.append(lambda: cap("05 SURVEY — Answering Q3/5", cursor_frac=(0.50,0.60), callout="Click an answer → instant feedback", callout_sub="Quiz adapts — don't worry about failing", dur=1000))
    def result_step():
        try:
            app.progress["level"]="Beginner"; app.progress["lesson_index"]=0; app.progress["step_index"]=0
            if "Beginner" not in app.progress.get("level_history",[]): app.progress.setdefault("level_history",[]).append("Beginner")
            try:
                from learn_python_gui import _save_current_language_state; _save_current_language_state(app.progress)
            except: pass
            app.show_frame(gui.ResultPage); app.update()
        except: pass
        cap("06 RESULT — Placed Beginner → Start Learning", cursor_frac=(0.52,0.70), callout="Placed at Beginner — Start Learning CTA", callout_sub="+15 XP for completing quiz", dur=1450, finder=finder_result_start)
    seq.append(result_step)

    def lc_concept():
        try:
            app.progress["step_index"]=0
            app.show_frame(gui.LearningPage)
            app.frames[gui.LearningPage].refresh(); app.update()
        except: pass
        cap("07 LEARNING — Concept: print / len / type", cursor_frac=(0.52,0.36), callout="Concept card — read, see example", callout_sub="Syntax-highlighted • Next to continue", finder=finder_learning_next)
    seq.append(lc_concept)

    def pr_starter():
        try:
            app.progress["step_index"]=1
            app.frames[gui.LearningPage].refresh(); app.update()
        except: pass
        cap("08 PRACTICE — Starter code in editor", cursor_frac=(0.42,0.56), callout="Practice — Starter code in editor", callout_sub="SyntaxEditor with live highlighting", finder=lambda a,i: find_editor_center(a, gui.LearningPage))
    seq.append(pr_starter)

    def type_mid():
        try:
            sk = gui.step_key("Beginner",0,1)
            app.progress.setdefault("draft_code",{})[sk]="print('Hello"
            app.frames[gui.LearningPage].refresh(); app.update()
        except: pass
        cap("09 PRACTICE — Typing: print('Hello", cursor_frac=(0.40,0.56), callout="Type your code — autosaves as you go", callout_sub="Draft kept on exit & crash-safe", dur=550)
    seq.append(type_mid)

    def type_done():
        try:
            sk = gui.step_key("Beginner",0,1)
            app.progress["draft_code"][sk]="print('Hello World')"
            app.frames[gui.LearningPage].refresh(); app.update()
        except: pass
        cap("10 PRACTICE — Done: print('Hello World')", cursor_frac=(0.72,0.68), callout="Finished typing → Hit Run to check", callout_sub="Run is sandbox-safe (restricted Python)", dur=650, click=True, finder=finder_run)
    seq.append(type_done)

    def run_ok():
        try:
            sk = gui.step_key("Beginner",0,1)
            if sk not in app.progress.get("completed_steps",{}):
                app.progress.setdefault("completed_steps",{})[sk]=True
                gui.award_xp(app.progress,5,"practice step"); gui.update_streak(app.progress)
                app.progress["draft_code"][sk]="print('Hello World')"
            app.progress["step_index"]=1
            app.frames[gui.LearningPage].refresh(); app.update()
        except Exception as e:
            print(f"[warn] run_ok {e}")
        cap("11 PRACTICE — Run → Correct! +5 XP ✓", cursor_frac=(0.50,0.74), callout="Green ✓ +5 XP + confetti burst!", callout_sub="XP levels you up — see Progress", dur=1350, finder=finder_run)
    seq.append(run_ok)

    def next_concept_step():
        try:
            app.progress["step_index"]=2
            app.frames[gui.LearningPage].refresh(); app.update()
        except: pass
        cap("12 LEARNING — Next Concept: len() & type()", cursor_frac=(0.50,0.42), callout="Step dots & progress bar show path", callout_sub="Sidebar: click any lesson to jump", finder=finder_learning_next)
    seq.append(next_concept_step)

    # Debug flow — Reading and fixing code lesson (index 5)
    def debug_broken_step():
        try:
            app.progress["lesson_index"]=5  # Reading and fixing code
            app.progress["step_index"]=2  # debug step
            app.progress["level"]="Beginner"
            app.frames[gui.LearningPage].refresh(); app.update()
        except Exception as e:
            print(f"[warn] debug_broken {e}")
        cap("13 DEBUG — Broken code: grerting typo", cursor_frac=(0.36,0.58), callout="Debug challenge — broken code given", callout_sub="Red NameError until you fix it", finder=lambda a,i: find_editor_center(a, gui.LearningPage))
    seq.append(debug_broken_step)

    def coach_hint_step():
        # remain on same debug view, show coach
        cap("14 COACH — Hint: 'Did you mean greeting?'", cursor_frac=(0.76,0.58), callout="Coach reads your code via AST", callout_sub="'Add a for loop' / names what you missed", click=False, finder=finder_coach, dur=1200)
    seq.append(coach_hint_step)

    def debug_fixed_step():
        try:
            sk = gui.step_key("Beginner",5,2)
            if sk not in app.progress.get("completed_steps",{}):
                app.progress.setdefault("completed_steps",{})[sk]=True
                gui.award_xp(app.progress,8,"debug fix"); gui.update_streak(app.progress)
                app.progress.setdefault("draft_code",{})[sk]="greeting = 'Hello'\nname = 'Ada'\nprint(greeting + name)"
            app.progress["step_index"]=2
            app.frames[gui.LearningPage].refresh(); app.update()
        except Exception as e:
            print(f"[warn] debug_fixed {e}")
        cap("15 DEBUG — Fixed → Run → +8 XP ✓", cursor_frac=(0.70,0.68), callout="Fixed typo → Run → +8 XP (harder)", callout_sub="Debug/XP more than practice (+5)", dur=1250, click=True, finder=finder_run)
    seq.append(debug_fixed_step)

    def final_proj_step():
        try:
            app.progress["lesson_index"]=0
            lessons = app.frames[gui.LearningPage].lesson_sets.get("Beginner",[])
            if lessons:
                steps = lessons[0].get("steps",[])
                actionable = [i for i,s in enumerate(steps) if s["type"] not in ("concept","example")]
                for i in actionable:
                    sk = gui.step_key("Beginner",0,i)
                    app.progress["completed_steps"][sk]=True
                app.frames[gui.LearningPage].refresh(); app.update()
        except: pass
        cap("16 FINAL PROJECT — Number Analyzer", cursor_frac=(0.52,0.48), callout="Final Project per lesson — bigger build", callout_sub="3 progressive hints • +25 XP", dur=1250)
    seq.append(final_proj_step)

    def prog_step():
        try: app.show_frame(gui.ProgressPage)
        except: pass
        cap("17 PROGRESS — XP + streak + heatmap", cursor_frac=(0.52,0.30), callout="Progress Dashboard — XP & level", callout_sub="Heatmap & Strengthen weak units", dur=1350)
    seq.append(prog_step)

    def skill_step():
        try: app.show_frame(gui.SkillTreePage)
        except: pass
        cap("18 SKILL TREE — 1/9 Beginner glowing", cursor_frac=(0.50,0.42), callout="Skill Tree — visual roadmap", callout_sub="Current node glows • done = check", dur=1100)
    seq.append(skill_step)

    def review_step():
        try: app.show_frame(gui.ReviewQueuePage)
        except: pass
        cap("19 REVIEW — Spaced repetition queue", cursor_frac=(0.48,0.52), callout="Review — SM-2 resurfaces hard lessons", callout_sub="Keeps knowledge sticky long-term")
    seq.append(review_step)

    def drills_step():
        try: app.show_frame(gui.DrillHubPage)
        except: pass
        cap("20 DRILLS — Muscle-memory reps", cursor_frac=(0.52,0.52), callout="Drills — speed & recall", callout_sub="Timed • filtered by unit")
    seq.append(drills_step)

    def daily_step():
        try: app.show_frame(gui.DailyChallengePage)
        except: pass
        cap("21 DAILY — Challenge + dataset editor", cursor_frac=(0.40,0.62), callout="Daily Challenge — fresh daily +8 XP", callout_sub="Tuned to your level • with datasets", finder=lambda a,i: find_editor_center(a, gui.DailyChallengePage) or (0.40,0.62))
    seq.append(daily_step)

    def sandbox_cards():
        try: app.show_frame(gui.SandboxPage); app.update()
        except: pass
        cap("22 SANDBOX — 20 Project Cards", cursor_frac=(0.50,0.40), callout="Sandbox Project Playground — 20 starters", callout_sub="Games • Stories • Math • Tools • Load", dur=1100)
    seq.append(sandbox_cards)

    def sandbox_run_step():
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
            print(f"[warn] sandbox_run {e}")
        cap("23 SANDBOX — Run → Hello + 0 1 2", cursor_frac=(0.72,0.66), callout="Try anything — Run shows live output", callout_sub="Unrestricted & safe • copy datasets", dur=1350, click=True, finder=finder_sandbox_run)
    seq.append(sandbox_run_step)

    def badges_step():
        try: app.show_frame(gui.BadgesPage)
        except: pass
        cap("24 BADGES — 23 achievements", cursor_frac=(0.30,0.46), callout="23 Badges — Easy → Legendary ★★★★★", callout_sub="Hover to see how to earn each")
    seq.append(badges_step)

    def settings_theme():
        try: app.show_frame(gui.SettingsPage)
        except: pass
        cap("25 SETTINGS — Theme & font size", cursor_frac=(0.78,0.30), callout="Settings — Dark/Light + font scale", callout_sub="Small/Normal/Large • instant retheme", dur=1050)
    seq.append(settings_theme)

    def settings_backup():
        # same page, different target
        cap("26 SETTINGS — Backup & Restore", cursor_frac=(0.52,0.62), callout="Backup & Restore your JSON", callout_sub="Atomic saves + periodic backup • safe")
    seq.append(settings_backup)

    def planning_step():
        try: app.show_frame(gui.PlanningGuidePage)
        except: pass
        cap("27 PLANNING — 2/4/6 week tracks", cursor_frac=(0.50,0.48), callout="Planning Guide — 2/4/6 week tracks", callout_sub="Optional • not required to finish", dur=1400)
    seq.append(planning_step)

    seq.append(lambda: cap("28 END — Lumixa ready • full tour complete", cursor_frac=None, callout=None, dur=args.hold_last))

    # Run sequence
    idx=[0]
    def run_next():
        if idx[0] >= len(seq):
            finish()
            return
        fn = seq[idx[0]]; idx[0]+=1
        try:
            fn()
        except Exception as e:
            print(f"[error] step {idx[0]} {e}")
            import traceback; traceback.print_exc()
        # next frame after 850ms (lets UI settle)
        app.after(860, run_next)

    def finish():
        print(f"\nCaptured {len(frames)} frames (guided HQ).")
        if not frames:
            print("[error] no frames")
            try: app.destroy()
            except: pass
            restore_backup(); sys.exit(1)
        # Preview (first frame, with bars but not too busy)
        try:
            frames[0].save(preview_path, "PNG", optimize=True)
            print(f"Preview: {preview_path} {frames[0].width}x{frames[0].height}")
        except Exception as e:
            print(f"[warn] preview {e}")
        try:
            print("[palette] building global palette (guided HQ)...")
            # Build montage from every 2nd frame
            sample = frames[::2]
            # limit montage height to avoid huge memory
            max_w = max(f.width for f in sample)
            total_h = sum(f.height for f in sample)
            cap_h = min(total_h, 4000)
            montage = Image.new("RGB", (max_w, cap_h))
            y=0
            for f in sample:
                if y + f.height > cap_h: break
                montage.paste(f.convert("RGB"), (0,y))
                y += f.height
            paletted = montage.quantize(colors=256, method=Image.MEDIANCUT, dither=Image.NONE)
            qframes = []
            for f in frames:
                q = f.convert("RGB").quantize(palette=paletted, dither=Image.FLOYDSTEINBERG)
                qframes.append(q)
            first = qframes[0]
            rest = qframes[1:]
            first.save(out_path, save_all=True, append_images=rest, duration=durations, loop=0, optimize=False, disposal=2)
            kb = out_path.stat().st_size/1024
            print(f"GIF GUIDED HQ: {out_path} {kb:.1f} KB {len(frames)} frames {frames[0].width}x{frames[0].height}")
            for i,l in enumerate(labels):
                try: print(f"  {i+1:02d} {l}")
                except UnicodeEncodeError: print(f"  {i+1:02d} {l.encode('ascii','replace').decode()}")
            # GitHub optimal thresholds for 900px
            if kb > 9000:
                print("[tip] >9MB — heavy for GitHub, try --width 800 or reduce frames")
            elif kb > 6500:
                print("[tip] >6.5MB — okay but consider --width 800 for faster load")
            elif 3500 <= kb <= 6500:
                print("[tip] perfect size for GitHub (3.5-6.5MB)!")
            elif kb < 3500:
                print("[tip] very small — good for fast README load")
        except Exception as e:
            print(f"[error] HQ save failed {e}"); import traceback; traceback.print_exc()
            try:
                first = frames[0].convert("P", palette=Image.ADAPTIVE, colors=256)
                rest = [f.convert("P", palette=Image.ADAPTIVE, colors=256) for f in frames[1:]]
                first.save(out_path, save_all=True, append_images=rest, duration=durations, loop=0, optimize=True, disposal=2)
                print(f"[fallback] saved {out_path.stat().st_size/1024:.1f} KB")
            except Exception as e2:
                print(f"[error] fallback {e2}")
        finally:
            try: app.after(900, app.destroy)
            except:
                try: app.destroy()
                except: pass
            app.after(1200, restore_backup)

    app.after(1050, run_next)
    app.mainloop()
    print("Guided HQ done — full app, cursor guide, high quality")
    if BACKUP.exists(): restore_backup()

if __name__=="__main__":
    main()
