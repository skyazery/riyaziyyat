"""Kitab generatorları üçün ümumi hissə: Topic, köməkçi şəkillər. content31.py / content32.py istifadə edir.
İstifadə:  from bookgen import *;  init(OUTDIR);  t = T(n, başlıq, izah, şəkil); t.num(...); ...;  save()"""
import hashlib, json, os, sys
from draw import *
from draw2 import *

OUT = IMG = None
VOICE = {}


def aid(text):
    h = hashlib.md5(text.encode()).hexdigest()[:10]
    VOICE[h] = text
    return h


def ordn(k):
    n = k + 1
    suf = {1: 'ci', 2: 'ci', 3: 'cü', 4: 'cü', 5: 'ci', 6: 'cı', 7: 'ci', 8: 'ci'}[n]
    return '%d-%s' % (n, suf)


class Topic:
    def __init__(self, n, title, concept, cimg):
        self.n, self.title, self.concept = n, title, concept
        self.problems = []
        path = 'img/t%02d_c.webp' % n
        finish(cimg, os.path.join(OUT, path), maxw=1100)
        self.d = {'n': n, 'title': title, 'concept': concept, 'conceptImg': path, 'conceptAudio': aid(concept), 'problems': self.problems}

    def _p(self):
        return 't%02d_%02d' % (self.n, len(self.problems) + 1)

    def num(self, ins, slots, stem, disp=None):
        """write-answer problem; stem image must show the boxes"""
        base = self._p()
        path = 'img/%s.webp' % base
        finish(stem, os.path.join(OUT, path))
        disp = disp or ', '.join(str(v) for v in slots)
        self.problems.append({'img': path, 'ins': ins, 'ans': disp, 'icon': 'write', 'check': {'mode': 'num', 'slots': list(slots)}, 'web': None, 'audio': aid(ins)})

    def choice(self, ins, opts, ans, stem=None, disp=None, mode='choice', hint=None, osize=None):
        """opts: list of images or str (text option). ans: index (choice) or list (multi/order)"""
        base = self._p()
        web = {'mode': mode, 'stem': None, 'opts': []}
        full = []
        if stem is not None:
            sp = 'img/%s_s.webp' % base
            finish(stem, os.path.join(OUT, sp))
            web['stem'] = sp
            full.append(stem)
        row_ = []
        for k, o in enumerate(opts):
            if isinstance(o, str):
                web['opts'].append({'t': o})
                oi = chip(o, 56, fill=WHITE, outline=GREY)
            else:
                op = 'img/%s_o%d.webp' % (base, k)
                finish(o, os.path.join(OUT, op), margin=14, maxw=600)
                web['opts'].append({'img': op})
                oi = o
            row_.append(vstack([oi, txt(str(k + 1), 30, GREY)], 6))
        full.append(hstack(row_, 40, align='bottom'))
        web['ans'] = ans
        if hint:
            web['hint'] = hint
        path = 'img/%s.webp' % base
        finish(vstack(full, 30), os.path.join(OUT, path))
        if disp is None:
            if mode == 'choice':
                disp = opts[ans] if isinstance(opts[ans], str) else ordn(ans) + ' şəkil'
            elif mode == 'multi':
                disp = ', '.join(ordn(i) for i in ans)
            else:
                disp = ', '.join(ordn(i) for i in ans)
        self.problems.append({'img': path, 'ins': ins, 'ans': disp, 'icon': 'circle', 'check': None, 'web': web, 'audio': aid(ins)})


    def sign(self, ins, pairs, ans, stem=None):
        """>, <, = problem: pairs [(a, b)], ans list of signs; the picture shows the pairs with empty circles"""
        base = self._p()
        path = 'img/%s.webp' % base
        im = cmp_row(pairs) if stem is None else vstack([stem, cmp_row(pairs)], 24)
        finish(im, os.path.join(OUT, path))
        disp = ', '.join('%s %s %s' % (a, g, b) for (a, b), g in zip(pairs, ans))
        self.problems.append({'img': path, 'ins': ins, 'ans': disp, 'icon': 'write', 'check': {'mode': 'sign', 'slots': list(ans), 'pairs': [[str(a), str(b)] for a, b in pairs]}, 'web': None, 'audio': aid(ins)})


TOPICS = []


def T(*a):
    t = Topic(*a)
    TOPICS.append(t)
    return t


def seq(tokens, size=60):
    return hstack([box(int(size * 1.5), int(size * 1.35)) if v is BOX else chip(str(v), size - 6, WHITE, INK, GREY) for v in tokens], 14)


def nchip(v, size=56):
    return chip(str(v), size, WHITE, INK, GREY)


def stacked(rows_, size=58):
    return vstack([expr2(r, size) for r in rows_], 16, 'left')


def two_rows(top, bottom, op='+'):
    """addend pictures in two rows (keeps images narrow so numbers stay big)"""
    return vstack([hstack([blank(44, 10), top], 14), hstack([txt(op, 56, BLUE), bottom], 14)], 12, 'left')


def cartons(n, size=30):
    return hstack([frame(row('🥚', 10, size, 2, 5), 6) for _ in range(n)], 10)


B3 = (66, 165, 245); R3 = (239, 83, 80); G3 = (102, 187, 106); O3 = (255, 167, 38); P3 = (171, 71, 188); Y3 = (255, 213, 79)



def init(out):
    """çıxış qovluğu (məs. ~/riyaziyyat/3-1)"""
    global OUT, IMG
    OUT = out
    IMG = os.path.join(OUT, 'img')
    os.makedirs(IMG, exist_ok=True)
    os.makedirs(os.path.join(OUT, 'data'), exist_ok=True)


def save():
    for tp in TOPICS:
        if len(tp.problems) != 10:
            print('COUNT', tp.n, len(tp.problems))
    json.dump({'topics': [tp.d for tp in TOPICS]}, open(os.path.join(OUT, 'data/topics.json'), 'w'), ensure_ascii=False)
    json.dump(VOICE, open(os.path.join(OUT, 'data/voice.json'), 'w'), ensure_ascii=False, indent=0)
    print('topics', len(TOPICS), 'voice', len(VOICE))


def triple(whole, a, b, size=64):
    """ədəd üçlüyü: yuxarıda tam, aşağıda iki hissə; None = boş xana"""
    def cell(v, w, fill):
        return frame(box(int(size * 1.4), int(size * 1.2)) if v is None else txt(str(v), size, INK), 10, ORANGE, 4, 14, fill)
    top = cell(whole, 0, (255, 236, 179))
    low = hstack([cell(a, 0, (255, 248, 225)), cell(b, 0, (255, 248, 225))], 8)
    return vstack([top, low], 6)


def word(emojis, tokens, size=58):
    """söz məsələsi: emoji şəkli + ifadə"""
    return vstack([hstack([em(e, 96) for e in emojis], 18), expr2(tokens, size)], 18)


# ------------------------------------------------------------------ 8–11-ci bölmələr üçün köməkçilər
def mult_table(n=5, blanks=(), mark=None, cell=58):
    """vurma cədvəli 1..n; blanks = [(sətir, sütun)] boş xana, mark = rənglənən xana"""
    rows = [[txt('·', 40, BLUE)] + [txt(str(c), 34, BLUE) for c in range(1, n + 1)]]
    for r in range(1, n + 1):
        line = [txt(str(r), 34, BLUE)]
        for c in range(1, n + 1):
            if (r, c) in blanks:
                line.append(box(int(cell * 0.95), int(cell * 0.8)))
            else:
                line.append(txt(str(r * c), 32, RED if mark == (r, c) else INK))
        rows.append(line)
    return table(rows, cell)


def flat(size=96):
    im, d = vec(size, size)
    k = size / 10
    d.rectangle([0, 0, size * S - 1, size * S - 1], fill=(144, 202, 249), outline=(21, 101, 192), width=3 * S)
    for i in range(1, 10):
        d.line([i * k * S, 0, i * k * S, size * S], fill=(21, 101, 192), width=S)
        d.line([0, i * k * S, size * S, i * k * S], fill=(21, 101, 192), width=S)
    return done(im)


def rod(size=96):
    im, d = vec(size // 10 + 2, size)
    k = size / 10
    d.rectangle([0, 0, (size // 10 + 2) * S - 1, size * S - 1], fill=(144, 202, 249), outline=(21, 101, 192), width=2 * S)
    for i in range(1, 10):
        d.line([0, i * k * S, (size // 10 + 2) * S, i * k * S], fill=(21, 101, 192), width=S)
    return done(im)


def unit(size=96):
    k = size // 10 + 2
    im, d = vec(k, k)
    d.rectangle([0, 0, k * S - 1, k * S - 1], fill=(144, 202, 249), outline=(21, 101, 192), width=2 * S)
    return done(im)


def hto(h, t, o, size=96):
    """yüzlük (kvadrat), onluq (çubuq), təklik (kub) blokları"""
    parts = []
    if h:
        parts.append(hstack([flat(size) for _ in range(h)], 8))
    if t:
        parts.append(hstack([rod(size) for _ in range(t)], 6))
    if o:
        parts.append(grid([unit(size) for _ in range(o)], 2, 5))
    return hstack(parts, 28, align='bottom')


def gram(v, size=34):
    return chip('%d q' % v, size, (255, 224, 178), INK, ORANGE)


def unit_expr(tokens, size=60):
    """ədəd + vahid: vahidləri (sm, m, kq, q, l, man, qəp, dəq) boz rəngdə yazır"""
    out = []
    for tk in tokens:
        if tk in ('mm', 'sm', 'dm', 'm', 'km', 'kq', 'q', 't', 'l', 'ml', 'man', 'qəp', 'dəq', 'saat'):
            out.append(txt(tk, int(size * 0.7), GREY))
        else:
            out.append(tk)
    parts = []
    for tk in out:
        if not isinstance(tk, str) and tk is not BOX:
            parts.append(tk)
        else:
            parts.append(expr2([tk], size))
    return hstack(parts, int(size * 0.22))


def coins(vals, size=90):
    return hstack([coin(v, size) for v in vals], 10)


def notes(vals, w=170, h=88):
    return hstack([note(v, w, h) for v in vals], 10)


def tab(rows, size=34):
    return table([[txt(str(c), size, INK) for c in r] for r in rows], int(size * 2))


SWEETS = [['Şirniyyat', 'Şənbə', 'Bazar'], ['Bulka', 27, 25], ['Keks', 20, 24], ['Pirojna', 13, 16]]
PETS = [('Pişik', 8), ('İt', 4), ('Bülbül', 2), ('Tısbağa', 1), ('Dovşan', 3)]
SEASONS = [('Yaz', 6), ('Yay', 9), ('Payız', 3), ('Qış', 5)]


def pet_bars():
    return bars([(txt(n, 24), v) for n, v in PETS], maxv=8, unit=30, barw=64, colors=[O3, B3, Y3, G3, P3])


def season_bars():
    return bars([(txt(n, 24), v) for n, v in SEASONS], maxv=10, unit=28, barw=70, colors=[G3, Y3, O3, B3])


def stickers_picto():
    rows = [[txt('Heyvanlar', 30), row('⭐', 6, 44, 4, 6)], [txt('Maşınlar', 30), row('⭐', 5, 44, 4, 6)], [txt('Təyyarələr', 30), row('⭐', 4, 44, 4, 6)]]
    return vstack([table(rows, 70), hstack([em('⭐', 40), txt('= 2 stiker', 32, BLUE)], 8)], 10)




# ------------------------------------------------------------------ 3-cü sinif üçün köməkçilər
def vcolx(a, b, op='+', size=52, ans_digits=None, show=False):
    """alt-alta toplama/çıxma/vurma (3–4 rəqəm); cavab xanası nəticənin rəqəm sayı qədər enlidir"""
    f = font(size)
    cw = int(f.getlength('0')) + 8
    res = {'+': a + b, '−': a - b, '·': a * b}[op]
    nd = max(len(str(a)), len(str(b)), len(str(res)))
    w = cw * (nd + 1) + 34
    im, d = vec(w + 24, int(size * 3.9))
    ff = font(size * S)
    for r, s in enumerate([str(a), str(b)]):
        for k, ch in enumerate(reversed(s)):
            x = w - (k + 1) * cw
            d.text((x * S, (r * size * 1.2 + 4) * S), ch, font=ff, fill=INK)
    d.text((4 * S, (size * 0.62) * S), '×' if op == '·' else op, font=ff, fill=BLUE)
    ly = size * 2.5
    d.line([cw * 0.5 * S, ly * S, (w + 8) * S, ly * S], fill=INK, width=5 * S)
    if show:  # mövzu girişi: cavab yaşıl rəqəmlərlə
        for k, ch in enumerate(reversed(str(res))):
            d.text(((w - (k + 1) * cw) * S, (ly + 10) * S), ch, font=ff, fill=GREEN)
        return done(im)
    im = done(im)
    k = ans_digits or len(str(res))
    bx = box(int(cw * k + 22), int(size * 1.3))
    im.alpha_composite(bx, (w - bx.width + 10, int(ly + 10)))
    return im


def place_table(vals, heads=('Yüzlüklər', 'Onluqlar', 'Təkliklər'), size=34):
    """mərtəbə cədvəli; vals elementi None olanda boş xana"""
    row2 = [box(int(size * 1.8), int(size * 1.6)) if v is None else txt(str(v), size + 6, INK) for v in vals]
    return table([[txt(h, size - 8, BLUE) for h in heads], row2], int(size * 2.1))


def frac_circle(n, k, size=150, color=(255, 167, 38)):
    im, d = vec(size, size)
    s = size * S
    pad = 6 * S
    for i in range(n):
        a0, a1 = -90 + 360 * i / n, -90 + 360 * (i + 1) / n
        d.pieslice([pad, pad, s - pad, s - pad], a0, a1, fill=color if i < k else WHITE, outline=INK, width=4 * S)
    return done(im)


def frac_bar(n, k, w=360, h=70, color=(102, 187, 106)):
    im, d = vec(w, h)
    cw = (w - 8) / n
    for i in range(n):
        x0 = 4 + i * cw
        d.rectangle([x0 * S, 4 * S, (x0 + cw) * S, (h - 4) * S], fill=color if i < k else WHITE, outline=INK, width=4 * S)
    return done(im)


def frac_txt(a, b, size=60, color=INK):
    """kəsr: surət üstdə, məxrəc altda"""
    top, bot = txt(str(a), size, color), txt(str(b), size, color)
    w = max(top.width, bot.width) + 16
    im, d = vec(w, top.height + bot.height + 14)
    done_im = done(im)
    o = blank(w, top.height + bot.height + 14)
    o.alpha_composite(top, ((w - top.width) // 2, 0))
    line = blank(w, 6)
    ImageDraw.Draw(line).rectangle([0, 0, w, 5], fill=color)
    o.alpha_composite(line, (0, top.height + 4))
    o.alpha_composite(bot, ((w - bot.width) // 2, top.height + 12))
    return o


def lines_pair(kind, size=220):
    """iki düz xətt: 'parallel', 'cross' (kəsişən), 'perp' (perpendikulyar)"""
    im, d = vec(size, size)
    s = size * S
    lw = 6 * S
    if kind == 'parallel':
        d.line([0.1 * s, 0.32 * s, 0.9 * s, 0.22 * s], fill=BLUE, width=lw)
        d.line([0.1 * s, 0.72 * s, 0.9 * s, 0.62 * s], fill=RED, width=lw)
    elif kind == 'cross':
        d.line([0.1 * s, 0.2 * s, 0.9 * s, 0.8 * s], fill=BLUE, width=lw)
        d.line([0.15 * s, 0.75 * s, 0.85 * s, 0.35 * s], fill=RED, width=lw)
    else:
        d.line([0.5 * s, 0.08 * s, 0.5 * s, 0.92 * s], fill=BLUE, width=lw)
        d.line([0.08 * s, 0.5 * s, 0.92 * s, 0.5 * s], fill=RED, width=lw)
        q = 0.07 * s
        d.line([0.5 * s, 0.5 * s - q, 0.5 * s + q, 0.5 * s - q], fill=INK, width=3 * S)
        d.line([0.5 * s + q, 0.5 * s - q, 0.5 * s + q, 0.5 * s], fill=INK, width=3 * S)
    return done(im)


def tri(pts, labels=(), size=220, color=(255, 236, 179), right=None):
    """üçbucaq; pts 0..1 koordinatları, labels = tərəflərin yazıları (0-1, 1-2, 2-0), right = düz bucaq təpəsi"""
    im, d = vec(size + 170, size + 80)
    P = [((x * size + 85) * S, (y * size + 30) * S) for x, y in pts]
    d.polygon(P, fill=color, outline=INK, width=5 * S)
    if right is not None:
        x, y = P[right]
        dx = 14 * S if P[(right + 1) % 3][0] > x or P[(right + 2) % 3][0] > x else -14 * S
        dy = -14 * S if P[(right + 1) % 3][1] < y or P[(right + 2) % 3][1] < y else 14 * S
        d.line([x + dx, y, x + dx, y + dy, x, y + dy], fill=INK, width=3 * S)
    f = font(26 * S)
    for i, lab in enumerate(labels):
        if not lab:
            continue
        (x0, y0), (x1, y1) = P[i], P[(i + 1) % 3]
        cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
        gx = sum(p[0] for p in P) / 3
        gy = sum(p[1] for p in P) / 3
        ox, oy = cx + (cx - gx) * 0.55, cy + (cy - gy) * 0.55
        tw = d.textlength(lab, font=f)
        d.text((ox - tw / 2, oy - 16 * S), lab, font=f, fill=BLUE)
    return done(im)


def sym(ch, size=130, axis=True):
    """emoji/fiqur və (istəyə görə) qırıq simmetriya oxu"""
    e = em(ch, size)
    if axis:
        d = ImageDraw.Draw(e)
        for y in range(0, size, 14):
            d.line([size // 2, y, size // 2, min(size, y + 8)], fill=RED, width=3)
    return e


def rect_sides(w, h, lw, lh, unit=26, color=(187, 222, 251)):
    """düzbucaqlı (və ya kvadrat) – tərəflərin uzunluğu yazılıb"""
    W, H = w * unit, h * unit
    im, d = vec(W + 170, H + 90)
    d.rectangle([60 * S, 30 * S, (60 + W) * S, (30 + H) * S], fill=color, outline=INK, width=5 * S)
    f = font(26 * S)
    tw = d.textlength(lw, font=f)
    d.text(((60 + W / 2) * S - tw / 2, (36 + H) * S), lw, font=f, fill=BLUE)
    d.text(((66 + W) * S, (30 + H / 2 - 14) * S), lh, font=f, fill=BLUE)
    return done(im)


def area_grid(cells, cols, rows, cell=36, color=(255, 183, 77)):
    """kvadrat torda rənglənmiş fiqur; cells = [(sütun, sətir)]"""
    im, d = vec(cols * cell + 8, rows * cell + 8)
    for r in range(rows):
        for c in range(cols):
            x, y = 4 + c * cell, 4 + r * cell
            d.rectangle([x * S, y * S, (x + cell) * S, (y + cell) * S], fill=color if (c, r) in cells else WHITE, outline=(176, 190, 197), width=2 * S)
    return done(im)


def digital(t, size=70):
    tx = txt(t, size, (0, 230, 118))
    im, d = vec(tx.width + 50, tx.height + 34)
    d.rounded_rectangle([0, 0, (tx.width + 50) * S, (tx.height + 34) * S], 16 * S, fill=(38, 50, 56))
    o = done(im)
    o.alpha_composite(tx, (25, 17))
    return o


def line_chart(labels, vals, maxv, step, w=560, h=300, color=BLUE):
    left, bottom, top = 70, 50, 20
    im, d = vec(w, h)
    f = font(20 * S)
    pw, ph = w - left - 20, h - bottom - top
    for v in range(0, maxv + 1, step):
        y = top + ph - v / maxv * ph
        d.line([left * S, y * S, (left + pw) * S, y * S], fill=(225, 228, 235), width=2 * S)
        tw = d.textlength(str(v), font=f)
        d.text(((left - 10) * S - tw, (y - 12) * S), str(v), font=f, fill=INK)
    n = len(vals)
    pts = []
    for i, (lab, v) in enumerate(zip(labels, vals)):
        x = left + pw * (i + 0.5) / n
        y = top + ph - v / maxv * ph
        pts.append((x * S, y * S))
        tw = d.textlength(lab, font=f)
        d.text((x * S - tw / 2, (top + ph + 12) * S), lab, font=f, fill=INK)
    d.line(pts, fill=color, width=5 * S)
    for x, y in pts:
        d.ellipse([x - 8 * S, y - 8 * S, x + 8 * S, y + 8 * S], fill=color)
    d.line([left * S, top * S, left * S, (top + ph) * S, (left + pw) * S, (top + ph) * S], fill=INK, width=3 * S)
    return done(im)


def mtab(rows, cols, blanks=(), cell=50):
    """vurma cədvəlinin parçası: rows/cols siyahıları"""
    head = [txt('·', 36, BLUE)] + [txt(str(c), 30, BLUE) for c in cols]
    out = [head]
    for r in rows:
        line = [txt(str(r), 30, BLUE)]
        for c in cols:
            line.append(box(int(cell * 1.15), int(cell * 0.8)) if (r, c) in blanks else txt(str(r * c), 28, INK))
        out.append(line)
    return table(out, cell)


def tri_mul(top, a, b, size=64):
    """vurma–bölmə üçbucağı: yuxarıda hasil, aşağıda vuruqlar; None = boş"""
    return triple(top, a, b, size)


def eqbox(tokens, size=64):
    """tənlik: 'x' göy rəngdə"""
    parts = []
    for t_ in tokens:
        if t_ is BOX:
            parts.append(box(int(size * 1.35), int(size * 1.35)))
        elif t_ in ('x', 'y', 'n', 'm', 'a', 'b', 'c', 'd'):
            parts.append(txt(t_, size, PURPLE))
        elif t_ in ('+', '−', '=', '>', '<', '·', ':', '≈'):
            parts.append(txt(t_, size, BLUE))
        else:
            parts.append(txt(t_, size, INK))
    return hstack(parts, gap=int(size * 0.28))


def notes2(vals, w=150, h=80):
    return hstack([note(v, w, h) for v in vals], 8)


def vcoln(nums, size=50, show=False):
    """alt-alta üç və daha çox ədədin toplanması"""
    f = font(size)
    cw = int(f.getlength('0')) + 8
    res = sum(nums)
    nd = max(len(str(x)) for x in nums + [res])
    w = cw * (nd + 1) + 34
    im, d = vec(w + 24, int(size * (1.3 * len(nums) + 1.6)))
    ff = font(size * S)
    for r, s_ in enumerate(map(str, nums)):
        for k, ch in enumerate(reversed(s_)):
            d.text(((w - (k + 1) * cw) * S, (r * size * 1.2 + 4) * S), ch, font=ff, fill=INK)
    d.text((4 * S, (size * 1.2 * (len(nums) - 1) - size * 0.6) * S), '+', font=ff, fill=BLUE)
    ly = size * 1.2 * len(nums) + 6
    d.line([cw * 0.5 * S, ly * S, (w + 8) * S, ly * S], fill=INK, width=5 * S)
    if show:
        for k, ch in enumerate(reversed(str(res))):
            d.text(((w - (k + 1) * cw) * S, (ly + 10) * S), ch, font=ff, fill=GREEN)
        return done(im)
    im = done(im)
    bx = box(int(cw * len(str(res)) + 22), int(size * 1.3))
    im.alpha_composite(bx, (w - bx.width + 10, int(ly + 10)))
    return im


def vtab(rows, size=34):
    """dəyişən cədvəli: hər hücrə str, int və ya BOX"""
    cells = [[box(int(size * 1.6), int(size * 1.4)) if c is BOX else txt(str(c), size, PURPLE if (j == 0) else INK) for j, c in enumerate(r)] for r in rows]
    return table(cells, int(size * 2))
