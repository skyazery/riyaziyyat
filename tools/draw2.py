"""Extra drawing primitives for 2-1 (2-ci sinif, 1-ci hissə). Same style as draw.py."""
import math
from PIL import ImageDraw
from draw import *


def expr2(tokens, size=72, boxw=None):
    """like expr(), plus '·' (vurma), ':' (bölmə) and '<' '>' in blue"""
    parts = []
    for t in tokens:
        if t is BOX:
            parts.append(box(boxw or int(size * 1.35), int(size * 1.35)))
        elif t in ('+', '−', '=', '>', '<', '·', ':'):
            parts.append(txt(t, size, BLUE))
        else:
            parts.append(txt(t, size, INK))
    return hstack(parts, gap=int(size * 0.28))


def sign_slot(size=80):
    """round empty slot for > < = (drawn as a circle, like the workbook)"""
    im, d = vec(size, size)
    d.ellipse([3 * S, 3 * S, (size - 3) * S, (size - 3) * S], outline=BLUE, width=5 * S, fill=WHITE)
    return done(im)


def cmp_row(pairs, size=70):
    ims = []
    for a, b in pairs:
        ims.append(hstack([txt(a, size), sign_slot(int(size * 1.15)), txt(b, size)], int(size * 0.25)))
    return hstack(ims, int(size * 0.9))


def numline_step(a, b, step, unit=60, start=None, hops=0, blanks=(), marks=(), size=28, hop=None):
    """number line with a tick every `step`; hops = number of jumps of size `hop` (default step), sign = direction"""
    n = (b - a) // step
    w, h = n * unit + 90, 170
    im, d = vec(w, h)
    y, x0 = 110, 44
    d.line([(x0 - 20) * S, y * S, (x0 + n * unit + 24) * S, y * S], fill=INK, width=4 * S)
    tip = (x0 + n * unit + 30) * S
    d.polygon([(tip, y * S), (tip - 16 * S, (y - 9) * S), (tip - 16 * S, (y + 9) * S)], fill=INK)
    f = font(size * S)
    xv = lambda v: x0 + (v - a) / step * unit
    for i in range(n + 1):
        v = a + i * step
        x = xv(v)
        d.line([x * S, (y - 10) * S, x * S, (y + 10) * S], fill=INK, width=4 * S)
        if v in blanks:
            d.rounded_rectangle([(x - 24) * S, (y + 18) * S, (x + 24) * S, (y + 58) * S], 8 * S, outline=BLUE, width=4 * S, fill=WHITE)
        else:
            col = RED if v in marks else INK
            tw = d.textlength(str(v), font=f)
            d.text((x * S - tw / 2, (y + 18) * S), str(v), font=f, fill=col)
    if start is not None:
        hp = hop or step
        sx = xv(start)
        d.ellipse([(sx - 9) * S, (y - 9) * S, (sx + 9) * S, (y + 9) * S], fill=RED)
        sgn = 1 if hops >= 0 else -1
        for k in range(abs(hops)):
            xa = xv(start + sgn * k * hp)
            xb = xv(start + sgn * (k + 1) * hp)
            lo, hi = min(xa, xb), max(xa, xb)
            d.arc([lo * S, (y - 64) * S, hi * S, (y + 24) * S], 180, 360, fill=ORANGE, width=5 * S)
            d.polygon([(xb * S, (y - 24) * S), ((xb - 9 * sgn) * S, (y - 38) * S), ((xb + 5 * sgn) * S, (y - 40) * S)], fill=ORANGE)
    return done(im)


def vcol(a, b, op='+', size=70):
    """column (alt-alta) addition/subtraction with an answer box"""
    f = font(size)
    cw = int(f.getlength('0')) + 6
    w = cw * 3 + 30
    lines = [str(a), str(b)]
    im, d = vec(w + 20, int(size * 3.9))
    ff = font(size * S)
    for r, s in enumerate(lines):
        for k, ch in enumerate(reversed(s)):
            x = w - (k + 1) * cw
            d.text((x * S, (r * size * 1.2 + 4) * S), ch, font=ff, fill=INK)
    d.text((2 * S, (size * 0.62) * S), op, font=ff, fill=BLUE)
    ly = size * 2.5
    d.line([cw * 0.6 * S, ly * S, (w + 6) * S, ly * S], fill=INK, width=5 * S)
    im = done(im)
    bx = box(int(cw * 2 + 22), int(size * 1.3))
    im.alpha_composite(bx, (w - bx.width + 8, int(ly + 10)))
    return im


def bundles_crossed(n, k, h=140, cols=None):
    """n bundles of 10 sticks; the last k crossed out in red (cols: wrap into rows)"""
    ims = []
    for i in range(n):
        b = bundle(h)
        if i >= n - k:
            d = ImageDraw.Draw(b)
            d.line([2, b.height - 4, b.width - 2, 4], fill=RED, width=7)
        ims.append(b)
    return grid(ims, cols or n, 12)


def sticks_crossed(t, o, k, h=140):
    """t bundles + o loose sticks; last k loose sticks crossed"""
    parts = [bundle(h) for _ in range(t)]
    for i in range(o):
        s = stick(h)
        if i >= o - k:
            s = s.copy()
            d = ImageDraw.Draw(s)
            d.line([0, s.height * 0.62, s.width, s.height * 0.38], fill=RED, width=6)
            s2 = blank(s.width + 16, s.height)
            s2.alpha_composite(s, (8, 0))
            ImageDraw.Draw(s2).line([0, s.height * 0.65, s2.width, s.height * 0.35], fill=RED, width=6)
            s = s2
        parts.append(s)
    return hstack(parts, 10)


def groups(ch, sizes, size=56, cols=None, gap=22):
    """several framed groups of an emoji, e.g. sizes=(3,3,3)"""
    return hstack([frame(row(ch, n, size, 6, cols or min(n, 3)), 12) for n in sizes], gap)


def plates(ch, counts, size=44):
    """equal sharing: plates with items on them"""
    out = []
    for n in counts:
        content = row(ch, n, size, 4, 3) if n else blank(size, size)
        pw = max(content.width + 50, 150)
        ph = content.height + 46
        im, d = vec(pw, ph)
        d.ellipse([4 * S, (ph * 0.35) * S, (pw - 4) * S, (ph - 4) * S], fill=(236, 239, 241), outline=GREY, width=4 * S)
        im = done(im)
        im.alpha_composite(content, ((pw - content.width) // 2, 6))
        out.append(im)
    return hstack(out, 20, 'bottom')


def array(ch, rows, cols, size=52):
    return frame(grid([em(ch, size) for _ in range(rows * cols)], cols, 8), 14)


# ---------------------------------------------------------------- lines and angles
def line_img(kind, w=230, h=120, color=INK):
    im, d = vec(w, h)
    lw = 7 * S
    if kind == 'straight':
        pts = [(16, h - 20), (w - 16, 20)]
        d.line([(x * S, y * S) for x, y in pts], fill=color, width=lw)
        for x, y in pts:
            d.ellipse([(x - 8) * S, (y - 8) * S, (x + 8) * S, (y + 8) * S], fill=RED)
    elif kind == 'curve':
        pts = [(16 + t * (w - 32), h / 2 + math.sin(t * math.pi * 1.6) * (h / 2 - 16)) for t in [i / 60 for i in range(61)]]
        d.line([(x * S, y * S) for x, y in pts], fill=color, width=lw, joint='curve')
    elif kind == 'wave':
        pts = [(16 + t * (w - 32), h / 2 + math.sin(t * math.pi * 4) * (h / 2 - 22)) for t in [i / 80 for i in range(81)]]
        d.line([(x * S, y * S) for x, y in pts], fill=color, width=lw, joint='curve')
    elif kind == 'broken':
        pts = [(16, h - 20), (w * 0.35, 22), (w * 0.62, h - 26), (w - 16, 26)]
        d.line([(x * S, y * S) for x, y in pts], fill=color, width=lw, joint='curve')
    elif kind == 'arc':
        d.arc([16 * S, 16 * S, (w - 16) * S, (h * 2 - 30) * S], 190, 350, fill=color, width=lw)
    elif kind == 'parallel':
        for y in (h * 0.3, h * 0.7):
            d.line([20 * S, y * S, (w - 20) * S, y * S], fill=color, width=lw)
    return done(im)


def angle_img(deg, size=200, color=BLUE, mark=True):
    """two rays from one vertex: one horizontal to the right, one at `deg` degrees; canvas fits both rays"""
    L = size * 0.75
    a = math.radians(deg)
    ex, ey = L * math.cos(a), -L * math.sin(a)
    pad = 22
    minx, maxx = min(0, ex), L
    miny = min(0, ey)
    w, h = int(maxx - minx + 2 * pad), int(-miny + 2 * pad)
    im, d = vec(w, h)
    vx, vy = pad - minx, h - pad
    for px, py in ((vx + L, vy), (vx + ex, vy + ey)):
        d.line([vx * S, vy * S, px * S, py * S], fill=color, width=7 * S)
    d.ellipse([(vx - 8) * S, (vy - 8) * S, (vx + 8) * S, (vy + 8) * S], fill=RED)
    if mark:
        if deg == 90:
            q = 26
            d.line([(vx + q) * S, vy * S, (vx + q) * S, (vy - q) * S, vx * S, (vy - q) * S], fill=ORANGE, width=5 * S)
        else:
            r = 34
            d.arc([(vx - r) * S, (vy - r) * S, (vx + r) * S, (vy + r) * S], 360 - deg, 360, fill=ORANGE, width=5 * S)
    return done(im)


# ---------------------------------------------------------------- polygons
def poly(n, size=120, color=BLUE, outline=INK, rot=None):
    im, d = vec(size + 8, size + 8)
    c = (size / 2 + 4) * S
    r = size / 2 * S
    rot = -math.pi / 2 if rot is None else rot
    pts = [(c + r * math.cos(rot + 2 * math.pi * k / n), c + r * math.sin(rot + 2 * math.pi * k / n)) for k in range(n)]
    d.polygon(pts, fill=color, outline=outline, width=5 * S)
    return done(im)


def rhombus(size=120, color=BLUE):
    w, h = int(size * 1.25), size
    im, d = vec(w + 8, h + 8)
    o = 4 * S
    d.polygon([(o + w * S / 2, o), (o + w * S, o + h * S / 2), (o + w * S / 2, o + h * S), (o, o + h * S / 2)], fill=color, outline=INK, width=5 * S)
    return done(im)


def corners(kind, size=170, color=(255, 236, 179)):
    """polygon with right-angle markers (square / rect)"""
    im = shape(kind, size, color)
    d = ImageDraw.Draw(im)
    W, H = im.width - 8, im.height - 8
    q = 18
    for (x, y, sx, sy) in [(4, 4, 1, 1), (4 + W, 4, -1, 1), (4, 4 + H, 1, -1), (4 + W, 4 + H, -1, -1)]:
        d.line([(x + sx * q, y + 3 * sy), (x + sx * q, y + sy * q), (x + 3 * sx, y + sy * q)], fill=RED, width=4)
    return im


def house(size=260):
    """roof (triangle) + body (square) + door (rect) + 2 windows (squares)"""
    w, h = size, int(size * 1.15)
    im, d = vec(w, h)
    roofh = h * 0.38
    d.polygon([(w / 2 * S, 4 * S), ((w - 6) * S, roofh * S), (6 * S, roofh * S)], fill=(239, 83, 80), outline=INK, width=5 * S)
    bx0, bx1 = w * 0.12, w * 0.88
    d.rectangle([bx0 * S, roofh * S, bx1 * S, (h - 4) * S], fill=(255, 236, 179), outline=INK, width=5 * S)
    dw, dh = w * 0.2, h * 0.3
    d.rectangle([(w / 2 - dw / 2) * S, (h - 4 - dh) * S, (w / 2 + dw / 2) * S, (h - 4) * S], fill=(141, 98, 64), outline=INK, width=4 * S)
    ws = w * 0.17
    for x in (bx0 + w * 0.06, bx1 - w * 0.06 - ws):
        d.rectangle([x * S, (roofh + h * 0.08) * S, (x + ws) * S, (roofh + h * 0.08 + ws) * S], fill=(129, 212, 250), outline=INK, width=4 * S)
    return done(im)


def pyramid(size=140, color=(255, 202, 40)):
    """square pyramid, slight perspective"""
    w, h = int(size * 1.2), size
    im, d = vec(w, h)
    apex = (w * 0.5, 6)
    fl, fr = (8, h * 0.82), (w * 0.68, h - 6)
    br, bl = (w - 8, h * 0.6), (w * 0.36, h * 0.48)
    sc = lambda p: (p[0] * S, p[1] * S)
    d.polygon([sc(apex), sc(fl), sc(fr)], fill=color, outline=INK, width=4 * S)
    shade = tuple(int(c * 0.8) for c in color)
    d.polygon([sc(apex), sc(fr), sc(br)], fill=shade, outline=INK, width=4 * S)
    for a_, b_ in [(fl, bl), (bl, br), (apex, bl)]:
        x0, y0 = a_
        x1, y1 = b_
        for t in range(0, 20, 2):
            d.line([sc((x0 + (x1 - x0) * t / 20, y0 + (y1 - y0) * t / 20)), sc((x0 + (x1 - x0) * (t + 1) / 20, y0 + (y1 - y0) * (t + 1) / 20))], fill=GREY, width=3 * S)
    return done(im)


def cube_marked(size=200, dots=True, color=(66, 165, 245)):
    """cube (same projection as draw.solid) with dashed hidden edges and, optionally, red vertex dots"""
    im = pad(solid('cube', size, color), 10)
    d = ImageDraw.Draw(im)
    fw = fh = size * 0.92
    dx, dy = size * 0.3, size * 0.28
    x0, y0 = 14, dy + 14
    hid = (x0 + dx, y0 + fh - dy)
    for p in [(x0, y0 + fh), (x0 + dx, y0 - dy), (x0 + fw + dx, y0 + fh - dy)]:
        for t in range(0, 20, 2):
            a = (hid[0] + (p[0] - hid[0]) * t / 20, hid[1] + (p[1] - hid[1]) * t / 20)
            b = (hid[0] + (p[0] - hid[0]) * (t + 1) / 20, hid[1] + (p[1] - hid[1]) * (t + 1) / 20)
            d.line([a, b], fill=INK, width=2)
    if dots:
        pts = [(x0, y0), (x0 + fw, y0), (x0 + fw, y0 + fh), (x0, y0 + fh), (x0 + dx, y0 - dy), (x0 + fw + dx, y0 - dy), (x0 + fw + dx, y0 + fh - dy), hid]
        for x, y in pts:
            d.ellipse([x - 7, y - 7, x + 7, y + 7], fill=RED)
    return im


def venn(left, right, both, outside=(), size=70, labels=('', '')):
    """two overlapping circles; each argument is a list of small images"""
    W, H = 640, 360
    im, d = vec(W, H)
    r = 150
    cl, cr = (220, 190), (420, 190)
    d.ellipse([(cl[0] - r) * S, (cl[1] - r) * S, (cl[0] + r) * S, (cl[1] + r) * S], outline=RED, width=6 * S)
    d.ellipse([(cr[0] - r) * S, (cr[1] - r) * S, (cr[0] + r) * S, (cr[1] + r) * S], outline=BLUE, width=6 * S)
    im = done(im)

    def place(items, cx, cy, cols):
        if not items:
            return
        g = grid(items, cols, 10)
        im.alpha_composite(g, (int(cx - g.width / 2), int(cy - g.height / 2)))
    place(left, 140, 190, 1 if len(left) <= 2 else 2)
    place(both, 320, 190, 1)
    place(right, 500, 190, 1 if len(right) <= 2 else 2)
    out = [im]
    if labels[0] or labels[1]:
        out = [hstack([txt(labels[0], 34, RED), blank(160, 10), txt(labels[1], 34, BLUE)], 20), im]
    return vstack(out, 6)
