"""Drawing primitives for the 1-2 worksheet images (style matches the 1-1 images:
white paper, DejaVu Sans Bold numbers, blue operators, dark rounded answer boxes, Noto emoji)."""
import io, math, os
from functools import lru_cache
from PIL import Image, ImageDraw, ImageFont
import cairosvg

EMOJI_DIR = os.environ.get('NOTO_SVG', 'noto-emoji/2D/svg')  # git clone https://github.com/googlefonts/noto-emoji
FONT_B = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
FONT_R = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'

INK = (51, 58, 64)
BLUE = (30, 136, 229)
GREY = (176, 181, 190)
LIGHT = (227, 230, 239)
RED = (229, 57, 53)
GREEN = (67, 160, 71)
YELLOW = (253, 216, 53)
ORANGE = (251, 140, 0)
PURPLE = (126, 87, 194)
PINK = (236, 64, 122)
BROWN = (141, 98, 64)
WHITE = (255, 255, 255)
COLORS = {'red': RED, 'blue': BLUE, 'green': GREEN, 'yellow': YELLOW, 'orange': ORANGE, 'purple': PURPLE, 'pink': PINK}

S = 2  # supersampling for vector drawing


def blank(w, h):
    return Image.new('RGBA', (int(w), int(h)), (0, 0, 0, 0))


@lru_cache(maxsize=None)
def font(size, bold=True):
    return ImageFont.truetype(FONT_B if bold else FONT_R, int(size))


def txt(s, size=60, color=INK, bold=True):
    f = font(size, bold)
    l, t, r, b = f.getbbox(str(s))
    asc, desc = f.getmetrics()
    im = blank(r - l + 4, asc + desc + 4)
    ImageDraw.Draw(im).text((2 - l, 2), str(s), font=f, fill=color)
    return im


@lru_cache(maxsize=None)
def _emoji(ch, size):
    cps = [c for c in ch if ord(c) != 0xFE0F]
    name = 'emoji_u' + '_'.join('%04x' % ord(c) for c in cps) + '.svg'
    p = os.path.join(EMOJI_DIR, name)
    if not os.path.exists(p):
        raise FileNotFoundError('emoji %r (%s)' % (ch, name))
    png = cairosvg.svg2png(url=p, output_width=size, output_height=size, unsafe=True)
    return Image.open(io.BytesIO(png)).convert('RGBA')


def em(ch, size=90):
    return _emoji(ch, int(size)).copy()


def pad(im, l, t=None, r=None, b=None):
    t = l if t is None else t
    r = l if r is None else r
    b = t if b is None else b
    o = blank(im.width + l + r, im.height + t + b)
    o.alpha_composite(im, (l, t))
    return o


def hstack(ims, gap=20, align='center'):
    ims = [i for i in ims if i is not None]
    if not ims:
        return blank(1, 1)
    w = sum(i.width for i in ims) + gap * (len(ims) - 1)
    h = max(i.height for i in ims)
    o = blank(w, h)
    x = 0
    for i in ims:
        y = (h - i.height) // 2 if align == 'center' else (h - i.height if align == 'bottom' else 0)
        o.alpha_composite(i, (x, y))
        x += i.width + gap
    return o


def vstack(ims, gap=20, align='center'):
    ims = [i for i in ims if i is not None]
    w = max(i.width for i in ims)
    h = sum(i.height for i in ims) + gap * (len(ims) - 1)
    o = blank(w, h)
    y = 0
    for i in ims:
        x = (w - i.width) // 2 if align == 'center' else 0
        o.alpha_composite(i, (x, y))
        y += i.height + gap
    return o


def grid(ims, cols, gap=12):
    rows = [hstack(ims[i:i + cols], gap) for i in range(0, len(ims), cols)]
    return vstack(rows, gap, align='left')


def vec(w, h):
    """supersampled vector canvas; call done() to downsample"""
    im = blank(w * S, h * S)
    return im, ImageDraw.Draw(im)


def done(im):
    return im.resize((im.width // S, im.height // S), Image.LANCZOS)


def frame(content, padding=18, color=GREY, width=3, radius=22, fill=None):
    w, h = content.width + 2 * padding, content.height + 2 * padding
    im, d = vec(w, h)
    d.rounded_rectangle([width * S, width * S, (w - width) * S, (h - width) * S], radius * S, outline=color, width=width * S, fill=fill)
    im = done(im)
    im.alpha_composite(content, (padding, padding))
    return im


def box(w=96, h=96, color=INK, width=6, radius=18):
    im, d = vec(w, h)
    d.rounded_rectangle([width * S / 2, width * S / 2, (w - width / 2) * S, (h - width / 2) * S], radius * S, outline=color, width=width * S, fill=WHITE)
    return done(im)


BOX = object()


def expr(tokens, size=72, boxw=None):
    """tokens: numbers/strings, '+', '−', '=', BOX"""
    parts = []
    for t in tokens:
        if t is BOX:
            parts.append(box(boxw or int(size * 1.35), int(size * 1.35)))
        elif t in ('+', '−', '=', '>', '<'):
            parts.append(txt(t, size, BLUE))
        else:
            parts.append(txt(t, size, INK))
    return hstack(parts, gap=int(size * 0.28))


def finish(im, path, margin=24, maxw=1000):
    o = Image.new('RGB', (im.width + 2 * margin, im.height + 2 * margin), WHITE)
    o.paste(im, (margin, margin), im)
    if o.width > maxw:
        o = o.resize((maxw, round(o.height * maxw / o.width)), Image.LANCZOS)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    o.save(path, 'WEBP', quality=82, method=6)
    return path


# ---------------------------------------------------------------- counting / groups
def row(ch, n, size=80, gap=8, cols=None):
    if n == 0:
        return blank(size, size)
    ims = [em(ch, size) for _ in range(n)]
    return grid(ims, cols or n, gap)


def group(ch, n, size=70, cols=5):
    return frame(row(ch, n, size, 8, cols), 14)


def crossed(ch, n, k, size=70, cols=None):
    """n emoji, last k crossed out"""
    ims = []
    for i in range(n):
        e = em(ch, size)
        if i >= n - k:
            d = ImageDraw.Draw(e)
            d.line([4, size - 4, size - 4, 4], fill=RED, width=max(5, size // 12))
        ims.append(e)
    return grid(ims, cols or n, 8)


def dots_frame(red=0, blue=0, empty=None, cell=64, cross=0):
    """ten frame 2x5. red first then blue, rest empty. cross: last k filled crossed"""
    total = 10
    w, h = 5 * cell + 24, 2 * cell + 24
    im, d = vec(w, h)
    d.rounded_rectangle([3 * S, 3 * S, (w - 3) * S, (h - 3) * S], 14 * S, outline=GREY, width=4 * S, fill=WHITE)
    filled = red + blue
    for i in range(total):
        r_, c_ = divmod(i, 5)
        cx, cy = 12 + c_ * cell + cell / 2, 12 + r_ * cell + cell / 2
        rr = cell * 0.36
        box_ = [(cx - rr) * S, (cy - rr) * S, (cx + rr) * S, (cy + rr) * S]
        if i < red:
            d.ellipse(box_, fill=RED)
        elif i < filled:
            d.ellipse(box_, fill=BLUE)
        else:
            d.ellipse(box_, outline=GREY, width=4 * S)
        if cross and filled - cross <= i < filled:
            d.line([(cx - rr) * S, (cy + rr) * S, (cx + rr) * S, (cy - rr) * S], fill=INK, width=6 * S)
    return done(im)


def dots_row(n, color=BLUE, d_=44, gap=10):
    w = n * d_ + (n - 1) * gap
    im, d = vec(max(w, 1), d_)
    for i in range(n):
        x = i * (d_ + gap)
        d.ellipse([x * S, 0, (x + d_) * S, d_ * S], fill=color)
    return done(im)


# ---------------------------------------------------------------- number line
def numline(a, b, unit=56, start=None, jumps=0, blanks=(), marks=(), size=30):
    n = b - a
    w, h = n * unit + 80, 170
    im, d = vec(w, h)
    y = 110
    x0 = 40
    d.line([x0 * S - 20 * S, y * S, (x0 + n * unit + 24) * S, y * S], fill=INK, width=4 * S)
    tip = (x0 + n * unit + 30) * S
    d.polygon([(tip, y * S), (tip - 16 * S, (y - 9) * S), (tip - 16 * S, (y + 9) * S)], fill=INK)
    f = font(size * S)
    for i in range(n + 1):
        x = x0 + i * unit
        d.line([x * S, (y - 10) * S, x * S, (y + 10) * S], fill=INK, width=4 * S)
        v = a + i
        if v in blanks:
            d.rounded_rectangle([(x - 20) * S, (y + 18) * S, (x + 20) * S, (y + 58) * S], 8 * S, outline=BLUE, width=4 * S, fill=WHITE)
        else:
            col = RED if v in marks else INK
            tw = d.textlength(str(v), font=f)
            d.text((x * S - tw / 2, (y + 18) * S), str(v), font=f, fill=col)
    if start is not None:
        sx = x0 + (start - a) * unit
        d.ellipse([(sx - 9) * S, (y - 9) * S, (sx + 9) * S, (y + 9) * S], fill=RED)
        step = 1 if jumps >= 0 else -1
        for k in range(abs(jumps)):
            xa = x0 + (start - a + k * step) * unit
            xb = xa + step * unit
            lo, hi = min(xa, xb), max(xa, xb)
            d.arc([lo * S, (y - 60) * S, hi * S, (y + 20) * S], 180, 360, fill=ORANGE, width=5 * S)
            # arrow head at xb
            d.polygon([(xb * S, (y - 22) * S), ((xb - 9 * step) * S, (y - 36) * S), ((xb + 5 * step) * S, (y - 38) * S)], fill=ORANGE)
    return done(im)


# ---------------------------------------------------------------- 2D shapes
def shape(kind, size=110, color=BLUE, outline=INK, half=None, split=None):
    w = int(size * 1.6) if kind == 'rect' else size
    h = size
    im, d = vec(w + 8, h + 8)
    o = 4 * S
    W, H = w * S, h * S
    lw = 5 * S
    if kind == 'circle':
        d.ellipse([o, o, o + W, o + H], fill=color, outline=outline, width=lw)
    elif kind in ('square', 'rect'):
        d.rectangle([o, o, o + W, o + H], fill=color, outline=outline, width=lw)
    elif kind == 'triangle':
        d.polygon([(o + W / 2, o), (o + W, o + H), (o, o + H)], fill=color, outline=outline, width=lw)
    if half:  # shade left half grey-out other half: half='left' leaves left coloured, right white
        # paint right half white with outline intact
        mask, md = vec(w + 8, h + 8)
        if kind == 'circle':
            md.ellipse([o, o, o + W, o + H], fill=(255, 255, 255, 255))
        elif kind == 'triangle':
            md.polygon([(o + W / 2, o), (o + W, o + H), (o, o + H)], fill=(255, 255, 255, 255))
        else:
            md.rectangle([o, o, o + W, o + H], fill=(255, 255, 255, 255))
        frac = {'half': 0.5, 'quarter': 0.25, 'most': 0.75}[half]
        cut = o + W * frac
        md.rectangle([0, 0, cut, mask.height], fill=(0, 0, 0, 0))
        white = Image.new('RGBA', mask.size, (255, 255, 255, 255))
        im = Image.composite(white, im, mask.split()[3])
        d = ImageDraw.Draw(im)
        if kind == 'circle':
            d.ellipse([o, o, o + W, o + H], outline=outline, width=lw)
        elif kind == 'triangle':
            d.polygon([(o + W / 2, o), (o + W, o + H), (o, o + H)], outline=outline, width=lw)
        else:
            d.rectangle([o, o, o + W, o + H], outline=outline, width=lw)
        if kind != 'triangle':
            d.line([cut, o, cut, o + H], fill=outline, width=lw)
    if split is not None:  # split = fraction position of vertical line (0.5 equal)
        if split == 'diag' and kind == 'square':
            d.line([o, o, o + W, o + H], fill=outline, width=lw)
        elif split == 'tri':
            d.line([o + W / 2, o, o + W / 2, o + H], fill=outline, width=lw)
        elif split == 'tri_bad':
            d.line([o + W / 2, o, o + W * 0.8, o + H], fill=outline, width=lw)
        elif split == 'horiz_bad':
            d.line([o, o + H * 0.3, o + W, o + H * 0.3], fill=outline, width=lw)
        elif split == 'horiz':
            d.line([o, o + H * 0.5, o + W, o + H * 0.5], fill=outline, width=lw)
        else:
            x = o + W * split
            if kind == 'circle':
                # chord inside circle
                r = W / 2
                dx = x - (o + r)
                dy = math.sqrt(max(r * r - dx * dx, 0))
                d.line([x, o + r - dy, x, o + r + dy], fill=outline, width=lw)
            else:
                d.line([x, o, x, o + H], fill=outline, width=lw)
    return done(im)


def triangle_vertices(size=200):
    im = shape('triangle', size, (187, 222, 251))
    d = ImageDraw.Draw(im)
    o = 4
    for (x, y) in [(o + size / 2, o), (o + size, o + size), (o, o + size)]:
        d.ellipse([x - 9, y - 9, x + 9, y + 9], fill=RED)
    return im


def square_sides(size=180):
    im = shape('square', size, (200, 230, 201), outline=INK)
    d = ImageDraw.Draw(im)
    o = 4
    cols = [RED, BLUE, ORANGE, PURPLE]
    pts = [(o, o), (o + size, o), (o + size, o + size), (o, o + size)]
    for k in range(4):
        d.line([pts[k], pts[(k + 1) % 4]], fill=cols[k], width=9)
    return im


# ---------------------------------------------------------------- 3D shapes
def _shade(c, f):
    return tuple(max(0, min(255, int(v * f))) for v in c)


def solid(kind, size=130, color=(66, 165, 245)):
    w = int(size * (1.7 if kind == 'cuboid' else 1.25))
    h = int(size * 1.25)
    im, d = vec(w, h)
    lw = 4 * S
    s = size * S
    if kind in ('cube', 'cuboid'):
        fw = (size * (1.35 if kind == 'cuboid' else 0.92)) * S
        fh = size * 0.92 * S
        dx, dy = size * 0.3 * S, size * 0.28 * S
        x0, y0 = 4 * S, dy + 4 * S
        front = [(x0, y0), (x0 + fw, y0), (x0 + fw, y0 + fh), (x0, y0 + fh)]
        top = [(x0, y0), (x0 + dx, y0 - dy), (x0 + fw + dx, y0 - dy), (x0 + fw, y0)]
        side = [(x0 + fw, y0), (x0 + fw + dx, y0 - dy), (x0 + fw + dx, y0 + fh - dy), (x0 + fw, y0 + fh)]
        d.polygon(front, fill=color, outline=INK, width=lw)
        d.polygon(top, fill=_shade(color, 1.25), outline=INK, width=lw)
        d.polygon(side, fill=_shade(color, 0.75), outline=INK, width=lw)
    elif kind == 'sphere':
        r = s * 0.55
        cx, cy = w * S / 2, h * S / 2
        for k in range(30, 0, -1):
            f = k / 30
            col = _shade(color, 0.7 + 0.5 * (1 - f))
            ox, oy = -r * 0.35 * (1 - f), -r * 0.35 * (1 - f)
            d.ellipse([cx - r * f + ox, cy - r * f + oy, cx + r * f + ox, cy + r * f + oy], fill=col)
        d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=INK, width=lw)
    elif kind == 'cylinder':
        rw, eh = s * 0.45, s * 0.16
        cx = w * S / 2
        top, bot = 8 * S + eh, h * S - 8 * S - eh
        d.rectangle([cx - rw, top, cx + rw, bot], fill=_shade(color, 0.9))
        d.ellipse([cx - rw, bot - eh, cx + rw, bot + eh], fill=_shade(color, 0.9), outline=INK, width=lw)
        d.rectangle([cx - rw + lw, top, cx + rw - lw, bot], fill=_shade(color, 0.9))
        d.line([cx - rw, top, cx - rw, bot], fill=INK, width=lw)
        d.line([cx + rw, top, cx + rw, bot], fill=INK, width=lw)
        d.ellipse([cx - rw, top - eh, cx + rw, top + eh], fill=_shade(color, 1.2), outline=INK, width=lw)
    elif kind == 'cone':
        rw, eh = s * 0.48, s * 0.15
        cx = w * S / 2
        apex = 6 * S
        bot = h * S - 8 * S - eh
        d.ellipse([cx - rw, bot - eh, cx + rw, bot + eh], fill=_shade(color, 0.85), outline=INK, width=lw)
        d.polygon([(cx, apex), (cx + rw, bot), (cx - rw, bot)], fill=_shade(color, 0.95))
        d.line([cx, apex, cx + rw, bot], fill=INK, width=lw)
        d.line([cx, apex, cx - rw, bot], fill=INK, width=lw)
    return done(im)


# ---------------------------------------------------------------- tens & ones
def stick(h=150, w=9):
    im, d = vec(w + 4, h)
    d.rounded_rectangle([2 * S, 0, (w + 2) * S, h * S], 5 * S, fill=BROWN)
    return done(im)


def bundle(h=150):
    sticks = hstack([stick(h) for _ in range(10)], gap=1)
    im = sticks.copy()
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, h // 2 - 12, im.width - 1, h // 2 + 12], 8, fill=ORANGE, outline=(230, 81, 0), width=2)
    return im


def tens_ones(t, o, h=140):
    parts = [bundle(h) for _ in range(t)] + ([hstack([stick(h) for _ in range(o)], 8)] if o else [])
    return hstack(parts, 22)


def tens_dots(t, o, cell=26):
    """t columns of ten dots + o single dots"""
    cols = []
    for _ in range(t):
        im, d = vec(cell + 8, cell * 10 + 8)
        d.rounded_rectangle([0, 0, (cell + 8) * S - 1, (cell * 10 + 8) * S - 1], 8 * S, outline=GREY, width=3 * S)
        for k in range(10):
            y = 4 + k * cell
            d.ellipse([(4 + 3) * S, (y + 3) * S, (4 + cell - 3) * S, (y + cell - 3) * S], fill=BLUE)
        cols.append(done(im))
    if o:
        im, d = vec(cell + 8, cell * 10 + 8)
        for k in range(o):
            y = 4 + (9 - k) * cell
            d.ellipse([(4 + 3) * S, (y + 3) * S, (4 + cell - 3) * S, (y + cell - 3) * S], fill=RED)
        cols.append(done(im))
    return hstack(cols, 14, align='bottom')


# ---------------------------------------------------------------- money
COPPER = (205, 127, 50)
GOLD = (240, 190, 50)


def coin(v, size=110):
    im, d = vec(size, size)
    col = COPPER if v in (1, 3, 5) else GOLD
    s = size * S
    d.ellipse([2 * S, 2 * S, s - 2 * S, s - 2 * S], fill=col, outline=_shade(col, 0.7), width=6 * S)
    d.ellipse([12 * S, 12 * S, s - 12 * S, s - 12 * S], outline=_shade(col, 0.85), width=3 * S)
    f = font(size * 0.42 * S)
    tw = d.textlength(str(v), font=f)
    d.text(((s - tw) / 2, s * 0.17), str(v), font=f, fill=(80, 50, 10))
    f2 = font(size * 0.2 * S)
    tw = d.textlength('qəp', font=f2)
    d.text(((s - tw) / 2, s * 0.6), 'qəp', font=f2, fill=(80, 50, 10))
    return done(im)


NOTE_COL = {1: (158, 158, 158), 5: (124, 179, 66), 10: (239, 108, 0), 20: (126, 87, 194), 50: (255, 179, 0), 100: (66, 165, 245)}


def note(v, w=210, h=110):
    im, d = vec(w, h)
    col = NOTE_COL.get(v, (100, 181, 246))
    d.rounded_rectangle([2 * S, 2 * S, (w - 2) * S, (h - 2) * S], 12 * S, fill=_shade(col, 1.15), outline=_shade(col, 0.6), width=4 * S)
    d.rounded_rectangle([12 * S, 12 * S, (w - 12) * S, (h - 12) * S], 8 * S, outline=_shade(col, 0.8), width=2 * S)
    k = h / 110
    f = font(46 * k * S)
    f2 = font(24 * k * S)
    s = str(v)
    tw, tw2 = d.textlength(s, font=f), d.textlength('man', font=f2)
    x = (w * S - tw - tw2 - 8 * S) / 2
    d.text((x, 24 * k * S), s, font=f, fill=(40, 40, 40))
    d.text((x + tw + 8 * S, 44 * k * S), 'man', font=f2, fill=(40, 40, 40))
    return done(im)


def tag(label, size=40, color=(255, 236, 179)):
    t = txt(label, size, INK)
    return frame(t, 10, color=ORANGE, width=3, radius=12, fill=color)


def priced(ch, label, esize=110):
    return vstack([em(ch, esize), tag(label)], 8)


# ---------------------------------------------------------------- length
def pencil(cm, unit=60, color=(255, 202, 40), h=40):
    L = int(cm * unit)
    im, d = vec(L, h)
    tipw = min(unit * 0.9, L * 0.25)
    body = L - tipw
    d.rectangle([0, 0, body * S, h * S], fill=color, outline=INK, width=3 * S)
    d.rectangle([0, 0, 14 * S, h * S], fill=(239, 154, 154), outline=INK, width=3 * S)
    d.polygon([(body * S, 0), (L * S, h * S / 2), (body * S, h * S)], fill=(255, 224, 178), outline=INK, width=3 * S)
    d.polygon([((L - tipw * 0.3) * S, (h / 2 - h * 0.15) * S), (L * S, h * S / 2), ((L - tipw * 0.3) * S, (h / 2 + h * 0.15) * S)], fill=INK)
    return done(im)


def strip(cm, unit=60, color=RED, h=34):
    L = int(cm * unit)
    im, d = vec(L, h)
    d.rounded_rectangle([0, 0, L * S - 1, h * S - 1], 6 * S, fill=color, outline=_shade(color, 0.7), width=3 * S)
    return done(im)


def cubes(n, unit=60, color=(255, 167, 38)):
    ims = []
    for _ in range(n):
        im, d = vec(unit, unit)
        d.rectangle([1 * S, 1 * S, (unit - 1) * S, (unit - 1) * S], fill=color, outline=_shade(color, 0.6), width=3 * S)
        ims.append(done(im))
    return hstack(ims, 0)


def ruler(maxcm=12, unit=60):
    w, h = maxcm * unit + 40, 90
    im, d = vec(w, h)
    d.rounded_rectangle([0, 0, w * S - 1, h * S - 1], 8 * S, fill=(255, 241, 118), outline=(190, 160, 30), width=3 * S)
    f = font(24 * S)
    for i in range(maxcm + 1):
        x = 20 + i * unit
        d.line([x * S, 0, x * S, 34 * S], fill=INK, width=3 * S)
        if i < maxcm:
            xm = x + unit / 2
            d.line([xm * S, 0, xm * S, 18 * S], fill=INK, width=2 * S)
        tw = d.textlength(str(i), font=f)
        d.text((x * S - tw / 2, 44 * S), str(i), font=f, fill=INK)
    return done(im)


def on_ruler(obj, maxcm=12, unit=60):
    r = ruler(maxcm, unit)
    o = blank(r.width, obj.height + 10 + r.height)
    o.alpha_composite(obj, (20, 0))
    o.alpha_composite(r, (0, obj.height + 10))
    return o


# ---------------------------------------------------------------- weight / capacity
def weight(kg, size=90):
    w, h = size, int(size * 0.85)
    im, d = vec(w, h)
    d.ellipse([(w * 0.35) * S, 0, (w * 0.65) * S, (h * 0.3) * S], outline=(84, 110, 122), width=6 * S)
    d.polygon([(w * 0.18 * S, h * 0.25 * S), (w * 0.82 * S, h * 0.25 * S), (w * S, h * S - 2), (0, h * S - 2)], fill=(96, 125, 139))
    f = font(size * 0.26 * S)
    s = '%d kq' % kg
    tw = d.textlength(s, font=f)
    d.text(((w * S - tw) / 2, h * 0.45 * S), s, font=f, fill=WHITE)
    return done(im)


def scale(left, right, tilt=0, width=620):
    """left/right: lists of images. tilt: -1 left down, 1 right down, 0 balanced"""
    L = hstack(left, 6, align='bottom') if left else blank(10, 10)
    R = hstack(right, 6, align='bottom') if right else blank(10, 10)
    panw = max(L.width, R.width, 170) + 30
    width = max(width, panw * 2 + 120)
    top = max(L.height, R.height) + 40
    h = top + 230
    im, d = vec(width, h)
    cx = width / 2
    beam_y = top + 60
    off = 34 * tilt
    lx, rx = panw / 2 + 10, width - panw / 2 - 10
    ly, ry = beam_y - off, beam_y + off
    # base + post
    d.polygon([((cx - 70) * S, (h - 6) * S), ((cx + 70) * S, (h - 6) * S), ((cx + 30) * S, (h - 40) * S), ((cx - 30) * S, (h - 40) * S)], fill=(121, 85, 72))
    d.rectangle([(cx - 9) * S, beam_y * S, (cx + 9) * S, (h - 40) * S], fill=(141, 110, 99))
    d.line([lx * S, ly * S, rx * S, ry * S], fill=(93, 64, 55), width=12 * S)
    d.ellipse([(cx - 14) * S, (beam_y - 14) * S, (cx + 14) * S, (beam_y + 14) * S], fill=(255, 193, 7))
    pans = []
    for (px, py, I) in ((lx, ly, L), (rx, ry, R)):
        pan_y = py + 70
        d.line([px * S, py * S, (px - panw / 2 + 10) * S, pan_y * S], fill=GREY, width=3 * S)
        d.line([px * S, py * S, (px + panw / 2 - 10) * S, pan_y * S], fill=GREY, width=3 * S)
        d.chord([(px - panw / 2) * S, (pan_y - 26) * S, (px + panw / 2) * S, (pan_y + 26) * S], 0, 180, fill=(176, 190, 197), outline=(96, 125, 139), width=3 * S)
        pans.append((px, pan_y, I))
    im = done(im)
    for (px, pan_y, I) in pans:
        im.alpha_composite(I, (int(px - I.width / 2), int(pan_y - I.height)))
    return im


def glass(frac, w=80, h=120):
    im, d = vec(w, h)
    top_w, bot_w = w - 6, w * 0.7
    def xat(y, side):
        t = y / h
        half = (top_w + (bot_w - top_w) * t) / 2
        return w / 2 + side * half
    if frac > 0:
        y0 = h - 4 - (h - 10) * frac
        d.polygon([(xat(y0, -1) * S, y0 * S), (xat(y0, 1) * S, y0 * S), (xat(h - 4, 1) * S, (h - 4) * S), (xat(h - 4, -1) * S, (h - 4) * S)], fill=(100, 181, 246))
    d.line([(xat(2, -1) * S, 2 * S), (xat(h - 4, -1) * S, (h - 4) * S), (xat(h - 4, 1) * S, (h - 4) * S), (xat(2, 1) * S, 2 * S)], fill=INK, width=4 * S, joint='curve')
    return done(im)


def pot(scale_=1.0, color=(176, 190, 197)):
    w, h = int(150 * scale_), int(110 * scale_)
    im, d = vec(w + 40, h + 20)
    d.rounded_rectangle([20 * S, 14 * S, (w + 20) * S, (h + 14) * S], 18 * S, fill=color, outline=INK, width=4 * S)
    d.rectangle([4 * S, 30 * S, 22 * S, 44 * S], fill=INK)
    d.rectangle([(w + 18) * S, 30 * S, (w + 36) * S, 44 * S], fill=INK)
    d.rectangle([14 * S, 6 * S, (w + 26) * S, 18 * S], fill=_shade(color, 0.8), outline=INK, width=3 * S)
    return done(im)


def bucket(scale_=1.0, color=(239, 83, 80)):
    w, h = int(120 * scale_), int(120 * scale_)
    im, d = vec(w, h + 20)
    d.arc([w * 0.12 * S, 0, w * 0.88 * S, (h * 0.55) * S], 180, 360, fill=INK, width=4 * S)
    d.polygon([(4 * S, h * 0.25 * S), ((w - 4) * S, h * 0.25 * S), (w * 0.85 * S, (h + 16) * S), (w * 0.15 * S, (h + 16) * S)], fill=color, outline=INK, width=4 * S)
    return done(im)


# ---------------------------------------------------------------- time
def clock(hh, size=220, mm=0):
    im, d = vec(size, size)
    s = size * S
    c = s / 2
    d.ellipse([4 * S, 4 * S, s - 4 * S, s - 4 * S], fill=WHITE, outline=INK, width=8 * S)
    f = font(size * 0.105 * S)
    for k in range(1, 13):
        a = math.radians(k * 30 - 90)
        x, y = c + math.cos(a) * s * 0.31, c + math.sin(a) * s * 0.31
        tw = d.textlength(str(k), font=f)
        d.text((x - tw / 2, y - size * 0.065 * S), str(k), font=f, fill=INK)
    for k in range(60):
        a = math.radians(k * 6 - 90)
        r1 = s * (0.44 if k % 5 else 0.42)
        d.line([c + math.cos(a) * r1, c + math.sin(a) * r1, c + math.cos(a) * s * 0.46, c + math.sin(a) * s * 0.46], fill=INK, width=2 * S)
    ah = math.radians((hh % 12) * 30 + mm * 0.5 - 90)
    am = math.radians(mm * 6 - 90)
    d.line([c, c, c + math.cos(ah) * s * 0.22, c + math.sin(ah) * s * 0.22], fill=RED, width=12 * S)
    d.line([c, c, c + math.cos(am) * s * 0.34, c + math.sin(am) * s * 0.34], fill=BLUE, width=8 * S)
    d.ellipse([c - 10 * S, c - 10 * S, c + 10 * S, c + 10 * S], fill=INK)
    return done(im)


# ---------------------------------------------------------------- data
def tally(n, h=70):
    groups = []
    while n > 0:
        k = min(5, n)
        n -= k
        w = 4 * 18 + 20
        im, d = vec(w, h)
        for i in range(min(k, 4)):
            x = 10 + i * 18
            d.line([x * S, 4 * S, x * S, (h - 4) * S], fill=INK, width=5 * S)
        if k == 5:
            d.line([2 * S, (h - 12) * S, (w - 4) * S, 12 * S], fill=RED, width=5 * S)
        groups.append(done(im))
    return hstack(groups, 16)


def table(rows, cellh=96):
    """rows: list of [image, image, ...]; draws grid"""
    ncol = max(len(r) for r in rows)
    colw = [max(r[c].width for r in rows if c < len(r)) + 30 for c in range(ncol)]
    W = sum(colw) + 6
    H = cellh * len(rows) + 6
    im, d = vec(W, H)
    d.rectangle([3 * S, 3 * S, (W - 3) * S, (H - 3) * S], fill=WHITE, outline=INK, width=4 * S)
    x = 3
    for c in colw[:-1]:
        x += c
        d.line([x * S, 3 * S, x * S, (H - 3) * S], fill=INK, width=3 * S)
    for k in range(1, len(rows)):
        y = 3 + k * cellh
        d.line([3 * S, y * S, (W - 3) * S, y * S], fill=INK, width=3 * S)
    im = done(im)
    for k, r in enumerate(rows):
        x = 3
        for c, cell in enumerate(r):
            im.alpha_composite(cell, (int(x + 15 if c else x + (colw[c] - cell.width) / 2), int(3 + k * cellh + (cellh - cell.height) / 2)))
            x += colw[c]
    return im


def bars(items, maxv=10, unit=34, barw=70, color=BLUE, colors=None):
    """items: list of (label_image, value). vertical bar chart with gridlines"""
    n = len(items)
    gap = 50
    left = 60
    W = left + n * (barw + gap) + 20
    H = maxv * unit + 30
    im, d = vec(W, H)
    f = font(24 * S)
    for v in range(maxv + 1):
        y = 10 + (maxv - v) * unit
        d.line([left * S, y * S, (W - 10) * S, y * S], fill=LIGHT if v else INK, width=(2 if v else 4) * S)
        if v % (1 if maxv <= 10 else 2) == 0:
            tw = d.textlength(str(v), font=f)
            d.text(((left - 12) * S - tw, (y - 14) * S), str(v), font=f, fill=INK)
    d.line([left * S, 10 * S, left * S, (10 + maxv * unit) * S], fill=INK, width=4 * S)
    for k, (_, v) in enumerate(items):
        x = left + gap / 2 + k * (barw + gap)
        if v:
            col = colors[k] if colors else color
            d.rectangle([x * S, (10 + (maxv - v) * unit) * S, (x + barw) * S, (10 + maxv * unit) * S], fill=col)
    chart = done(im)
    labels = blank(W, max(i.height for i, _ in items) + 8)
    for k, (lab, _) in enumerate(items):
        x = left + gap / 2 + k * (barw + gap) + barw / 2
        labels.alpha_composite(lab, (int(x - lab.width / 2), 8))
    return vstack([chart, labels], 0)


def hundred(start, rows=2, blanks=(), cell=72, cols=10):
    W, H = cols * cell + 6, rows * cell + 6
    im, d = vec(W, H)
    f = font(28 * S)
    for k in range(rows * cols):
        r_, c_ = divmod(k, cols)
        v = start + k
        x, y = 3 + c_ * cell, 3 + r_ * cell
        d.rectangle([x * S, y * S, (x + cell) * S, (y + cell) * S], fill=WHITE if v not in blanks else (255, 248, 225), outline=GREY, width=3 * S)
        if v in blanks:
            d.rounded_rectangle([(x + 10) * S, (y + 10) * S, (x + cell - 10) * S, (y + cell - 10) * S], 8 * S, outline=BLUE, width=4 * S)
        else:
            tw = d.textlength(str(v), font=f)
            d.text(((x + cell / 2) * S - tw / 2, (y + cell / 2 - 17) * S), str(v), font=f, fill=INK)
    return done(im)


def label(im, s, size=30, color=BLUE):
    return vstack([im, txt(s, size, color)], 6)


def arrow(w=90, color=INK):
    im, d = vec(w, 40)
    d.line([0, 20 * S, (w - 20) * S, 20 * S], fill=color, width=8 * S)
    d.polygon([((w - 26) * S, 4 * S), (w * S, 20 * S), ((w - 26) * S, 36 * S)], fill=color)
    return done(im)


def chip(s, size=40, fill=(225, 245, 254), color=INK, outline=BLUE):
    return frame(txt(s, size, color), 12, color=outline, width=3, radius=14, fill=fill)


def die(n, size=110):
    im, d = vec(size, size)
    s = size * S
    d.rounded_rectangle([3 * S, 3 * S, s - 3 * S, s - 3 * S], 18 * S, fill=WHITE, outline=INK, width=6 * S)
    P = {1: [(.5, .5)], 2: [(.27, .27), (.73, .73)], 3: [(.27, .27), (.5, .5), (.73, .73)], 4: [(.27, .27), (.73, .27), (.27, .73), (.73, .73)],
         5: [(.27, .27), (.73, .27), (.5, .5), (.27, .73), (.73, .73)], 6: [(.27, .25), (.73, .25), (.27, .5), (.73, .5), (.27, .75), (.73, .75)]}[n]
    r = s * 0.085
    for x, y in P:
        d.ellipse([x * s - r, y * s - r, x * s + r, y * s + r], fill=INK)
    return done(im)
