#!/usr/bin/env python3
"""Generate the 12 keycap legend SVGs, a preview sheet and a relegendable-cap print sheet.

Run from the repo root:  python3 keycaps/generate_icons.py
Outputs (all overwritten): keycaps/svg/, keycaps/outlined/, keycaps/png/,
keycaps/sheet-preview.{svg,png}, keycaps/print-sheet-a4.{svg,pdf}.
Outlining and rasterising need Inkscape 1.x on PATH.
"""
import math
import pathlib
import shutil
import subprocess

ROOT = pathlib.Path(__file__).resolve().parent
LEGEND_MM = 12  # printed legend size; fits the ~12.7 mm top of a DSA/XDA 1u cap
INK = "#111111"
ACCENT = "#D97757"  # Claude orange, used only on key 1 in the colour variant
SW = 6.5  # stroke width in a 100-unit box: 0.78 mm at 12 mm, well above UV/print minimums
FONT = "DejaVu Sans Mono"


def rays():
    out = []
    for i in range(12):
        a = math.radians(i * 30 - 90)
        r1, r2 = 7, (27 if i % 2 == 0 else 19)
        out.append(f'<line x1="{50 + r1 * math.cos(a):.2f}" y1="{40 + r1 * math.sin(a):.2f}" '
                   f'x2="{50 + r2 * math.cos(a):.2f}" y2="{40 + r2 * math.sin(a):.2f}"/>')
    return "".join(out)


def gear():
    pts = []
    teeth, ro, ri = 8, 25, 19
    for i in range(teeth * 4):
        a = math.radians(i * 360 / (teeth * 4) - 90 + 360 / teeth / 8)
        r = ro if i % 4 in (1, 2) else ri
        pts.append(f"{50 + r * math.cos(a):.2f},{40 + r * math.sin(a):.2f}")
    return f'<polygon points="{" ".join(pts)}"/><circle cx="50" cy="40" r="7"/>'


def arrow_arc(cx, cy, r, start, end, head=True):
    """Arc from start to end degrees (clockwise in screen space if end > start), with arrowhead at end."""
    a0, a1 = math.radians(start), math.radians(end)
    x0, y0 = cx + r * math.cos(a0), cy + r * math.sin(a0)
    x1, y1 = cx + r * math.cos(a1), cy + r * math.sin(a1)
    sweep = 1 if end > start else 0
    large = 1 if abs(end - start) > 180 else 0
    s = f'<path d="M{x0:.2f} {y0:.2f} A{r} {r} 0 {large} {sweep} {x1:.2f} {y1:.2f}"/>'
    if head:
        # tangent direction at the end point
        t = a1 + (math.pi / 2 if sweep else -math.pi / 2)
        for da in (math.radians(150), math.radians(-150)):
            hx, hy = x1 + 10 * math.cos(t + da), y1 + 10 * math.sin(t + da)
            s += f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{hx:.2f}" y2="{hy:.2f}"/>'
    return s


# Key number, slug, label, icon body (stroke-only unless noted). Order matches key-layout.md.
KEYS = [
    (1, "claude", "claude", rays()),
    (2, "talk", "talk",
     '<rect x="40" y="12" width="20" height="32" rx="10"/>'
     '<path d="M30 36 a20 20 0 0 0 40 0"/><line x1="50" y1="56" x2="50" y2="64"/>'
     '<line x1="40" y1="65" x2="60" y2="65"/>'),
    (3, "config", "/config", gear()),
    (4, "compact", "/compact",
     '<line x1="26" y1="40" x2="74" y2="40"/>'
     '<line x1="50" y1="12" x2="50" y2="31"/><polyline points="41,23 50,32 59,23"/>'
     '<line x1="50" y1="68" x2="50" y2="49"/><polyline points="41,57 50,48 59,57"/>'),
    (5, "model", "/model",
     '<rect x="34" y="24" width="32" height="32" rx="4"/><rect x="44" y="34" width="12" height="12" rx="1"/>'
     + "".join(f'<line x1="{x}" y1="14" x2="{x}" y2="24"/><line x1="{x}" y1="56" x2="{x}" y2="66"/>'
               f'<line x1="24" y1="{x - 10}" x2="34" y2="{x - 10}"/><line x1="66" y1="{x - 10}" x2="76" y2="{x - 10}"/>'
               for x in (42, 58))),
    (6, "usage", "/usage",
     '<path d="M22 54 A28 28 0 0 1 78 54"/><line x1="50" y1="54" x2="66" y2="36"/>'
     '<circle cx="50" cy="54" r="4" fill="INK" stroke="none"/>'
     '<line x1="22" y1="62" x2="78" y2="62"/>'),
    # Counter-clockwise arrow (undo), arrowhead at the top-left end.
    (7, "rewind", "rewind", arrow_arc(50, 40, 22, 120, -150)),
    (8, "repos", "~/repos",
     '<path d="M20 24 h20 l6 7 h34 v31 h-60 z"/><line x1="20" y1="38" x2="80" y2="38"/>'),
    (9, "esc", "esc",
     '<polygon points="39,14 61,14 76,29 76,51 61,66 39,66 24,51 24,29"/>'
     '<rect x="40" y="30" width="20" height="20" rx="2" fill="INK" stroke="none"/>'),
    (10, "mode", "⇧tab",
     arrow_arc(50, 40, 22, 200, 340) + arrow_arc(50, 40, 22, 20, 160)),
    (11, "clear", "/clear",
     '<path d="M30 14 h28 l12 12 v40 h-40 z"/><polyline points="58,14 58,26 70,26"/>'
     '<line x1="50" y1="34" x2="50" y2="56"/><line x1="39" y1="45" x2="61" y2="45"/>'),
    (12, "resume", "/resume",
     '<line x1="22" y1="22" x2="50" y2="22"/><line x1="22" y1="40" x2="44" y2="40"/>'
     '<line x1="22" y1="58" x2="50" y2="58"/>'
     '<polygon points="58,26 80,40 58,54" fill="INK" stroke-linejoin="round"/>'),
]


def body(icon, label, accent=False):
    colour = ACCENT if accent else INK
    icon = icon.replace('"INK"', f'"{colour}"')
    size = 13 if len(label) <= 7 else 11.5
    return (f'<g fill="none" stroke="{colour}" stroke-width="{SW}" stroke-linecap="round" '
            f'stroke-linejoin="round">{icon}</g>'
            f'<text x="50" y="91" text-anchor="middle" font-family="{FONT}" font-weight="bold" '
            f'font-size="{size}" fill="{INK}">{label}</text>')


def svg(inner, w_mm=LEGEND_MM, h_mm=LEGEND_MM, vb="0 0 100 100"):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w_mm}mm" height="{h_mm}mm" '
            f'viewBox="{vb}">{inner}</svg>\n')


def write(p, text):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text)


def main():
    for d in ("svg", "outlined", "png"):
        shutil.rmtree(ROOT / d, ignore_errors=True)
    names = []
    for n, slug, label, icon in KEYS:
        name = f"{n:02d}-{slug}"
        names.append(name)
        write(ROOT / "svg" / f"{name}.svg", svg(body(icon, label, accent=(n == 1))))
        write(ROOT / "svg" / "mono" / f"{name}.svg", svg(body(icon, label)))

    # Preview: 3x4 grid of caps, order as on the pad (row-major, key 1 top-left).
    cells = []
    for i, (n, slug, label, icon) in enumerate(KEYS):
        x, y = (i % 3) * 120 + 10, (i // 3) * 120 + 10
        cells.append(f'<g transform="translate({x},{y})"><rect x="-6" y="-6" width="112" height="112" rx="14" '
                     f'fill="#F3EFE6" stroke="#C9C2B4" stroke-width="2"/>{body(icon, label, accent=(n == 1))}</g>')
    write(ROOT / "sheet-preview.svg",
          svg('<rect width="380" height="500" fill="#FFFFFF"/>' + "".join(cells), 76, 100, "-10 -10 380 500"))

    # A4 print sheet for relegendable caps: each legend in a 14 mm square with a cut outline.
    # Units are mm. Two copies of the set so a misprint or a test fit costs nothing.
    cut, pitch = 14, 20
    items = []
    for copy in range(2):
        for i, (n, slug, label, icon) in enumerate(KEYS):
            col, row = i % 6, i // 6 + copy * 3
            x, y = 20 + col * pitch, 30 + row * pitch
            items.append(f'<rect x="{x}" y="{y}" width="{cut}" height="{cut}" fill="none" stroke="#999" '
                         f'stroke-width="0.15" stroke-dasharray="0.8 0.8"/>'
                         f'<g transform="translate({x + 1.5},{y + 1.5}) scale(0.11)">{body(icon, label, accent=(n == 1))}</g>')
    items.append(f'<text x="20" y="20" font-family="{FONT}" font-size="4" fill="#333">Claude-Pad legends: '
                 f'print at 100% (no fit-to-page), cut on dashed 14 mm squares, trim to the cap window.</text>'
                 f'<line x1="20" y1="180" x2="70" y2="180" stroke="#000" stroke-width="0.3"/>'
                 f'<text x="20" y="186" font-family="{FONT}" font-size="3.5">50 mm check line</text>')
    write(ROOT / "print-sheet-a4.svg", svg("".join(items), 210, 297, "0 0 210 297"))

    if shutil.which("inkscape"):
        for name in names:
            for sub, src in (("", "svg"), ("mono/", "svg/mono")):
                f = ROOT / src / f"{name}.svg"
                out = ROOT / "outlined" / sub / f"{name}.svg"
                out.parent.mkdir(parents=True, exist_ok=True)
                subprocess.run(["inkscape", str(f), "--export-text-to-path", "--export-plain-svg",
                                f"--export-filename={out}"], check=True, capture_output=True)
            (ROOT / "png").mkdir(exist_ok=True)
            subprocess.run(["inkscape", str(ROOT / "svg" / f"{name}.svg"), "-w", "600", "-h", "600",
                            f"--export-filename={ROOT / 'png' / (name + '.png')}"], check=True, capture_output=True)
        subprocess.run(["inkscape", str(ROOT / "sheet-preview.svg"), "-w", "1140",
                        f"--export-filename={ROOT / 'sheet-preview.png'}"], check=True, capture_output=True)
        subprocess.run(["inkscape", str(ROOT / "print-sheet-a4.svg"), "--export-text-to-path",
                        f"--export-filename={ROOT / 'print-sheet-a4.pdf'}"], check=True, capture_output=True)


if __name__ == "__main__":
    main()
