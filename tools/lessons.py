"""Qısa video dərslər (mövzudan əvvəl ~30 s): hər səhnə = səs + üst-üstə düşən şəkil qatları.
Qatlar eyni ölçüdə (800×600, şəffaf) çəkilir, app.js onları səsə uyğun vaxtda göstərir.
Köməkçilər; dərslərin özü tools/lessons11.py, lessons12.py, lessons21.py, lessons22.py-dadır."""
import hashlib, json, math, os, sys
from PIL import Image, ImageDraw
sys.path.insert(0, os.path.dirname(__file__))
from draw import txt, em, font, INK, BLUE, RED, GREEN, ORANGE, PURPLE, GREY

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
W, H = 800, 600
OPS = {'+': BLUE, '=': BLUE, '·': BLUE, '−': BLUE, '?': ORANGE}


def aid(text):
    return hashlib.md5(text.encode()).hexdigest()[:10]


class Lesson:
    def __init__(self, book, n):
        self.book, self.n, self.scenes, self.k = book, n, [], 0
        self.dir = os.path.join(ROOT, book if book != '1-1' else '.')
        d = os.path.join(self.dir, 'img', 'lesson')
        os.makedirs(d, exist_ok=True)
        for f in os.listdir(d):  # köhnə qatlar
            if f.startswith('l%d_' % n):
                os.remove(os.path.join(d, f))

    def layer(self, items):
        """items: [(şəkil, x, y)] – (x, y) şəklin mərkəzidir"""
        im = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        for pic, x, y in items:
            im.alpha_composite(pic, (int(x - pic.width / 2), int(y - pic.height / 2)))
        self.k += 1
        name = 'img/lesson/l%d_%02d.webp' % (self.n, self.k)
        im.save(os.path.join(self.dir, name), 'WEBP', quality=88, method=4)
        return name

    def scene(self, say, layers, keep=False):
        """layers: [(qat, an, effekt[, gizlənmə anı])] – an səsin uzunluğunun hissəsidir (0..1)"""
        sc = {'say': say, 'audio': aid(say), 'keep': keep, 'layers': []}
        for L in layers:
            d = {'src': L[0], 'at': L[1], 'fx': L[2]}
            if len(L) > 3:
                d['out'] = L[3]
            sc['layers'].append(d)
        self.scenes.append(sc)

    def save(self):
        p = os.path.join(self.dir, 'data', 'lessons.json')
        data = json.load(open(p)) if os.path.exists(p) else {}
        old = data.get(str(self.n), {}).get('scenes', [])
        data[str(self.n)] = {'scenes': self.scenes}
        json.dump(data, open(p, 'w'), ensure_ascii=False, indent=1)
        vp = os.path.join(self.dir, 'data', 'voice.json')
        voice = json.load(open(vp))
        tp = json.load(open(os.path.join(self.dir, 'data', 'topics.json')))
        tp = tp['topics'] if isinstance(tp, dict) else tp
        used = {t['conceptAudio'] for t in tp} | {p.get('audio') for t in tp for p in t['problems']}
        others = {s['audio'] for k, v in data.items() if k != str(self.n) for s in v['scenes']}
        for s in old:  # bu dərsin köhnə mətnləri
            if s['audio'] not in used and s['audio'] not in others:
                voice.pop(s['audio'], None)
        for s in self.scenes:
            voice[s['audio']] = s['say']
        json.dump(voice, open(vp, 'w'), ensure_ascii=False, indent=1)
        print(self.book, self.n, len(self.scenes), 'səhnə')


def big(s, size=96, color=INK):
    return txt(s, size, OPS.get(s, color))


def eq_items(parts, y, size=96, gap=26):
    """bərabərliyin hissələri yan-yana, ortada; [(şəkil, x, y)] siyahısı"""
    pics = [big(p, size) for p in parts]
    total = sum(p.width for p in pics) + gap * (len(pics) - 1)
    x = (W - total) / 2
    out = []
    for p in pics:
        out.append((p, x + p.width / 2, y))
        x += p.width + gap
    return out


def dot(color, r=30):
    im = Image.new('RGBA', (2 * r + 4, 2 * r + 4), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.ellipse([2, 2, 2 * r + 2, 2 * r + 2], fill=color + (255,), outline=(255, 255, 255, 255), width=3)
    return im


def frame10(cell=84):
    """boş onluq qutu (2 × 5)"""
    im = Image.new('RGBA', (5 * cell + 8, 2 * cell + 8), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    for r in range(2):
        for c in range(5):
            d.rounded_rectangle([4 + c * cell, 4 + r * cell, 4 + (c + 1) * cell, 4 + (r + 1) * cell], 10, fill=(255, 255, 255, 255), outline=INK + (255,), width=4)
    return im


def plate(n_apples, size=150):
    im = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.ellipse([4, size * 0.18, size - 4, size - 4], fill=(255, 255, 255, 255), outline=GREY + (255,), width=5)
    d.ellipse([size * 0.18, size * 0.32, size * 0.82, size * 0.84], outline=(225, 228, 234, 255), width=4)
    a = em('🍎', int(size * 0.34))
    pos = [(0.34, 0.56), (0.66, 0.56)] if n_apples == 2 else [(0.5, 0.42), (0.3, 0.64), (0.7, 0.64)][:n_apples]
    for px, py in pos:
        im.alpha_composite(a, (int(px * size - a.width / 2), int(py * size - a.height / 2)))
    return im


FOX = lambda: [(em('🦊', 220), W / 2, 250), (txt('İndi siz!', 64, ORANGE), W / 2, 450), (em('⭐', 70), W / 2 - 220, 170), (em('⭐', 56), W / 2 + 230, 210)]



# ---------------------------------------------------------------- tez yazmaq üçün
def T(s, size=72, color=INK):
    return txt(s, size, color)


def seq(layers, a=0.1, b=0.75, fx='pop'):
    """qatları səsin a..b hissəsinə bərabər yaymaq"""
    n = len(layers)
    if n == 1:
        return [(layers[0], a, fx)]
    return [(L_, a + (b - a) * i / (n - 1), fx) for i, L_ in enumerate(layers)]


def row(n, y, x0=None, dx=110):
    x0 = W / 2 - dx * (n - 1) / 2 if x0 is None else x0
    return [(x0 + i * dx, y) for i in range(n)]


def grid(n, cols, y0, dx=100, dy=100, x0=None):
    x0 = W / 2 - dx * (cols - 1) / 2 if x0 is None else x0
    return [(x0 + (i % cols) * dx, y0 + (i // cols) * dy) for i in range(n)]


def canvas():
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    return im, ImageDraw.Draw(im)


def shape(kind, size=150, color=BLUE, fill=True):
    im = Image.new('RGBA', (size + 8, size + 8), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    c = color + (255,)
    f = tuple(min(255, int(v * 0.35 + 255 * 0.65)) for v in color) + (255,) if fill else None
    s = size
    if kind == 'tri':
        d.polygon([(s / 2 + 4, 4), (s + 4, s + 4), (4, s + 4)], fill=f, outline=c, width=6)
    elif kind == 'circle':
        d.ellipse([4, 4, s + 4, s + 4], fill=f, outline=c, width=6)
    elif kind == 'square':
        d.rectangle([4, 4, s + 4, s + 4], fill=f, outline=c, width=6)
    elif kind == 'rect':
        d.rectangle([4, s * 0.25 + 4, s + 4, s * 0.75 + 4], fill=f, outline=c, width=6)
    return im


def nline(a, b, y=330, x0=70, x1=730, marks=(), size=34):
    """ədəd oxu qatı və nöqtənin x-i üçün funksiya"""
    im, d = canvas()
    ux = (x1 - x0) / (b - a)
    X = lambda v: x0 + (v - a) * ux
    d.line([(x0 - 20, y), (x1 + 30, y)], fill=INK + (255,), width=5)
    d.polygon([(x1 + 44, y), (x1 + 26, y - 10), (x1 + 26, y + 10)], fill=INK + (255,))
    for v in range(a, b + 1):
        d.line([(X(v), y - 12), (X(v), y + 12)], fill=INK + (255,), width=4)
        d.text((X(v), y + 36), str(v), font=font(size), fill=(RED if v in marks else INK) + (255,), anchor='mm')
    return im, X


def hop(X, v0, v1, y=330, color=ORANGE, label=None):
    im, d = canvas()
    xa, xb = X(v0), X(v1)
    hgt = 26 + abs(xb - xa) * 0.25
    d.arc([min(xa, xb), y - hgt * 2, max(xa, xb), y + 2], 180, 360, fill=color + (255,), width=6)
    tip = xb
    up = -1 if xb > xa else 1
    d.polygon([(tip, y - 2), (tip - 12 * (1 if xb > xa else -1), y - 18), (tip + 4 * (1 if xb > xa else -1), y - 20)], fill=color + (255,))
    if label:
        d.text(((xa + xb) / 2, y - hgt - 22), label, font=font(30), fill=color + (255,), anchor='mm')
    return im


def rod(cell=26, color=BLUE):
    """onluq çubuq (10 kub)"""
    im = Image.new('RGBA', (cell + 6, 10 * cell + 6), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    for i in range(10):
        d.rectangle([3, 3 + i * cell, 3 + cell, 3 + (i + 1) * cell], fill=tuple(int(v * 0.4 + 255 * 0.6) for v in color) + (255,), outline=color + (255,), width=3)
    return im


def unit(cell=26, color=ORANGE):
    im = Image.new('RGBA', (cell + 6, cell + 6), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rectangle([3, 3, 3 + cell, 3 + cell], fill=tuple(int(v * 0.4 + 255 * 0.6) for v in color) + (255,), outline=color + (255,), width=3)
    return im


def flat(cell=18, color=GREEN):
    """yüzlük lövhə (10×10)"""
    im = Image.new('RGBA', (10 * cell + 6, 10 * cell + 6), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    for r in range(10):
        for c in range(10):
            d.rectangle([3 + c * cell, 3 + r * cell, 3 + (c + 1) * cell, 3 + (r + 1) * cell], fill=tuple(int(v * 0.4 + 255 * 0.6) for v in color) + (255,), outline=color + (255,), width=2)
    return im


def blocks(tens, ones, x, y, cell=26, gap=12):
    """onluq çubuqlar və təkliklər: [(şəkil, x, y)]"""
    out = []
    R = rod(cell)
    for i in range(tens):
        out.append((R, x + i * (cell + gap), y))
    U = unit(cell)
    ux = x + tens * (cell + gap) + 20
    for i in range(ones):
        out.append((U, ux + (i % 2) * (cell + 8), y - 4 * cell + (i // 2) * (cell + 8)))
    return out


def clock(h, m=0, size=300):
    im = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    c, r = size / 2, size / 2 - 6
    d.ellipse([6, 6, size - 6, size - 6], fill=(255, 255, 255, 255), outline=INK + (255,), width=7)
    for k in range(1, 13):
        a = math.radians(k * 30 - 90)
        d.text((c + (r - 34) * math.cos(a), c + (r - 34) * math.sin(a)), str(k), font=font(30), fill=INK + (255,), anchor='mm')
    am = math.radians(m * 6 - 90)
    ah = math.radians((h % 12 + m / 60) * 30 - 90)
    d.line([(c, c), (c + (r - 40) * math.cos(am), c + (r - 40) * math.sin(am))], fill=BLUE + (255,), width=8)
    d.line([(c, c), (c + (r - 85) * math.cos(ah), c + (r - 85) * math.sin(ah))], fill=RED + (255,), width=11)
    d.ellipse([c - 9, c - 9, c + 9, c + 9], fill=INK + (255,))
    return im


def coin(v, r=58, color=(240, 180, 40)):
    im = Image.new('RGBA', (2 * r + 6, 2 * r + 6), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.ellipse([3, 3, 2 * r + 3, 2 * r + 3], fill=color + (255,), outline=tuple(int(x * 0.7) for x in color) + (255,), width=5)
    d.text((r + 3, r - 6), str(v), font=font(int(r * 0.75)), fill=(255, 255, 255, 255), anchor='mm')
    d.text((r + 3, r + r * 0.5), 'q', font=font(int(r * 0.35)), fill=(255, 255, 255, 255), anchor='mm')
    return im


def bar(hgt, w=70, color=BLUE):
    im = Image.new('RGBA', (w, hgt + 4), (0, 0, 0, 0))
    ImageDraw.Draw(im).rounded_rectangle([0, 0, w - 1, hgt + 3], 8, fill=color + (255,))
    return im


def tally(n, size=60, color=INK):
    """cizgilər: 5-lik dəstələr"""
    w = int(size * 0.28)
    groups = [5] * (n // 5) + ([n % 5] if n % 5 else [])
    W_ = sum(w * min(g, 4) + 24 for g in groups) + 10
    im = Image.new('RGBA', (W_, size + 10), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    x = 5
    for g in groups:
        for i in range(min(g, 4)):
            d.line([(x + i * w, 5), (x + i * w, size + 5)], fill=color + (255,), width=6)
        if g == 5:
            d.line([(x - 6, size - 5), (x + 3 * w + 6, 15)], fill=RED + (255,), width=6)
        x += w * min(g, 4) + 24
    return im


def ring(w, h, color=ORANGE):
    im = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    ImageDraw.Draw(im).rounded_rectangle([3, 3, w - 3, h - 3], 26, outline=color + (255,), width=6)
    return im


def L1(L, items):
    """bir neçə şəkli bir qatda"""
    return L.layer(items)


def fin(L, say='İndi siz cəhd edin!'):
    L.scene(say, [(L.layer(FOX()), 0.05, 'pop')])


def card(s, size=80, color=INK):
    """ağ kart üstündə ədəd"""
    t = txt(s, size, color)
    im = Image.new('RGBA', (t.width + 50, t.height + 40), (0, 0, 0, 0))
    ImageDraw.Draw(im).rounded_rectangle([2, 2, im.width - 3, im.height - 3], 18, fill=(255, 255, 255, 255), outline=GREY + (255,), width=4)
    im.alpha_composite(t, (25, 20))
    return im


def numcards(vals, y, dx=150, size=80, color=INK):
    return [(card(str(v), size, color), x, y) for v, (x, _) in zip(vals, row(len(vals), y, dx=dx))]


def box(w, h, color=GREY, fill=(255, 255, 255)):
    im = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    ImageDraw.Draw(im).rounded_rectangle([3, 3, w - 3, h - 3], 14, fill=fill + (255,), outline=color + (255,), width=5)
    return im


def label(s, size=40, color=INK, pad=14):
    """ağ fonlu yazı"""
    t = txt(s, size, color)
    im = Image.new('RGBA', (t.width + 2 * pad, t.height + 2 * pad), (0, 0, 0, 0))
    ImageDraw.Draw(im).rounded_rectangle([0, 0, im.width - 1, im.height - 1], 12, fill=(255, 255, 255, 235))
    im.alpha_composite(t, (pad, pad))
    return im
