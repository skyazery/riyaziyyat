"""Qısa video dərslər (mövzudan əvvəl ~30 s): hər səhnə = səs + üst-üstə düşən şəkil qatları.
Qatlar eyni ölçüdə (800×600, şəffaf) çəkilir, app.js onları səsə uyğun vaxtda göstərir.
Run: python3 tools/lessons.py   → <kitab>/img/lesson/*.webp, <kitab>/data/lessons.json, voice.json-a səs mətnləri"""
import hashlib, json, os, sys
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
        os.makedirs(os.path.join(self.dir, 'img', 'lesson'), exist_ok=True)

    def layer(self, items):
        """items: [(şəkil, x, y)] – (x, y) şəklin mərkəzidir"""
        im = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        for pic, x, y in items:
            im.alpha_composite(pic, (int(x - pic.width / 2), int(y - pic.height / 2)))
        self.k += 1
        name = 'img/lesson/l%d_%02d.webp' % (self.n, self.k)
        im.save(os.path.join(self.dir, name), 'WEBP', quality=88, method=6)
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
        data[str(self.n)] = {'scenes': self.scenes}
        json.dump(data, open(p, 'w'), ensure_ascii=False, indent=1)
        vp = os.path.join(self.dir, 'data', 'voice.json')
        voice = json.load(open(vp))
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
    pos = [(0.5, 0.42), (0.3, 0.64), (0.7, 0.64)][:n_apples]
    for px, py in pos:
        im.alpha_composite(a, (int(px * size - a.width / 2), int(py * size - a.height / 2)))
    return im


FOX = lambda: [(em('🦊', 220), W / 2, 250), (txt('İndi siz!', 64, ORANGE), W / 2, 450), (em('⭐', 70), W / 2 - 220, 170), (em('⭐', 56), W / 2 + 230, 210)]

# ============================================================ 1-1 · 15 Ədədlərin toplanması
L = Lesson('1-1', 15)
A = em('🍎', 104)
xs = [130, 250, 370, 540, 660]
ap = [L.layer([(A, x, 170)]) for x in xs]
L.scene('Burada 3 alma var.', [(ap[0], 0.1, 'pop'), (ap[1], 0.35, 'pop'), (ap[2], 0.6, 'pop')])
L.scene('Daha 2 alma gətirdik.', [(ap[3], 0.25, 'fly'), (ap[4], 0.5, 'fly')], keep=True)
nums = [L.layer([(txt(str(i + 1), 64, BLUE), x, 290)]) for i, x in enumerate(xs)]
L.scene('Sayaq: 1, 2, 3, 4, 5. Cəmi 5 alma oldu.', [(nums[i], 0.12 + i * 0.11, 'pop') for i in range(5)], keep=True)
eq = eq_items(['3', '+', '2', '=', '5'], 470)
L.scene('Belə yazırıq: 3 üstəgəl 2 bərabərdir 5.', [(L.layer([eq[i]]), 0.18 + i * 0.13, 'pop') for i in range(5)], keep=True)
L.scene('İndi siz cəhd edin!', [(L.layer(FOX()), 0.05, 'pop')])
L.save()

# ============================================================ 1-2 · 33 10-a tamamlamaqla toplama
L = Lesson('1-2', 33)
F = frame10()
fx, fy, cell = 300, 300, 84
cpos = lambda i: (fx - 2 * cell + (i % 5) * cell, fy - cell / 2 + (i // 5) * cell)
red = dot(RED)
blue = dot(BLUE)
top = eq_items(['8', '+', '5', '=', '?'], 80, 84)
L.scene('8 üstəgəl 5 neçə edir?', [(L.layer(top[:3]), 0.05, 'pop'), (L.layer(top[3:]), 0.5, 'pop')])
fr = L.layer([(F, fx, fy)])
r5 = L.layer([(red, *cpos(i)) for i in range(5)])
r3 = L.layer([(red, *cpos(i)) for i in range(5, 8)])
L.scene('Onluq qutuya 8 qırmızı top qoyaq.', [(fr, 0.0, 'fade'), (r5, 0.3, 'pop'), (r3, 0.6, 'pop')], keep=True)
side = [(640, 230), (720, 230), (640, 310), (720, 310), (680, 390)]
b5 = L.layer([(blue, x, y) for x, y in side])
b2in = L.layer([(blue, *cpos(8)), (blue, *cpos(9))])
b3 = L.layer([(blue, x, y) for x, y in side[2:]])
ten = L.layer([(txt('10', 72, GREEN), fx, fy + 140)])
L.scene('5 göy topdan 2-sini qutuya qoyuruq. Qutu doldu: 10 oldu.', [(b5, 0.05, 'pop', 0.42), (b2in, 0.42, 'fly'), (b3, 0.42, 'fade'), (ten, 0.78, 'pop')], keep=True)
eq = eq_items(['10', '+', '3', '=', '13'], 530, 80)
L.scene('Qalan 3-ü də əlavə edirik: 10 üstəgəl 3 bərabərdir 13.', [(L.layer([e]), 0.32 + i * 0.12, 'pop') for i, e in enumerate(eq)], keep=True)
fin = eq_items(['8', '+', '5', '=', '13'], 300, 110)
L.scene('Deməli, 8 üstəgəl 5 bərabərdir 13. İndi siz cəhd edin!', [(L.layer(fin), 0.05, 'pop'), (L.layer([(em('🦊', 140), W / 2, 480)]), 0.62, 'pop')])
L.save()

# ============================================================ 2-1 · 59 Vurma
L = Lesson('2-1', 59)
px = [130, 310, 490, 670]
pl = [L.layer([(plate(3), x, 170)]) for x in px]
L.scene('Hər boşqabda 3 alma var.', [(pl[0], 0.1, 'pop'), (L.layer([(txt('3', 56, BLUE), px[0], 280)]), 0.6, 'pop')])
lab = [L.layer([(txt('3', 56, BLUE), x, 280)]) for x in px[1:]]
L.scene('Belə 4 boşqab var.', [(pl[1], 0.15, 'pop'), (lab[0], 0.15, 'pop'), (pl[2], 0.35, 'pop'), (lab[1], 0.35, 'pop'), (pl[3], 0.55, 'pop'), (lab[2], 0.55, 'pop')], keep=True)
eq = eq_items(['3', '+', '3', '+', '3', '+', '3', '=', '12'], 400, 72, 18)
L.scene('Toplayaq: 3 üstəgəl 3 üstəgəl 3 üstəgəl 3 bərabərdir 12.', [(L.layer(eq[:7]), 0.1, 'fade'), (L.layer(eq[7:]), 0.78, 'pop')], keep=True)
m = eq_items(['3', '·', '4', '=', '12'], 520, 92)
L.scene('Qısa yazırıq: 3 vur 4 bərabərdir 12. Hər qrupda 3, cəmi 4 qrup.', [(L.layer(m[:3]), 0.08, 'pop'), (L.layer(m[3:]), 0.38, 'pop')], keep=True)
L.scene('İndi siz cəhd edin!', [(L.layer(FOX()), 0.05, 'pop')])
L.save()
