"""5–6-cı sinif kitabları üçün ümumi köməkçilər (4-2-dən götürülüb + kəsr/mənfi xanalar)."""
import math
from bookgen import *
import bookgen

def f(n):
    s = str(n)
    if len(s) < 4:
        return s
    out = ''
    while len(s) > 3:
        out = ' ' + s[-3:] + out
        s = s[:-3]
    return s + out


def cmp_col(pairs, size=62):
    return vstack([hstack([txt(a, size), sign_slot(int(size * 1.15)), txt(b, size)], int(size * 0.3)) for a, b in pairs], int(size * 0.35))


bookgen.cmp_row = cmp_col


def numsep(t, ins, slots, stem, sep, disp=None):
    """cavab xanaları arasında ',' (onluq kəsr), '/' (kəsr) və ya ':' (saat)"""
    t.num(ins, slots, stem, disp=disp or sep.join(str(v) for v in slots))
    t.problems[-1]['check']['sep'] = sep


def fr(a, b, size=56, color=INK):
    """kəsr; surət və ya məxrəc BOX ola bilər"""
    def part(v):
        return box(int(size * 1.1), int(size * 1.05)) if v is BOX else txt(str(v), size, color)
    top, bot = part(a), part(b)
    w = max(top.width, bot.width) + 16
    o = blank(w, top.height + bot.height + 16)
    o.alpha_composite(top, ((w - top.width) // 2, 0))
    line = blank(w, 6)
    ImageDraw.Draw(line).rectangle([0, 0, w, 5], fill=color)
    o.alpha_composite(line, (0, top.height + 5))
    o.alpha_composite(bot, ((w - bot.width) // 2, top.height + 13))
    return o


def mixed(w_, a, b, size=56, color=INK):
    return hstack([txt(str(w_), int(size * 1.25), color), fr(a, b, size, color)], 6)


def FX(*toks, size=56):
    parts = []
    for t_ in toks:
        if t_ is BOX:
            parts.append(box(int(size * 1.3), int(size * 1.3)))
        elif isinstance(t_, tuple) and len(t_) == 2:
            parts.append(fr(t_[0], t_[1], size))
        elif isinstance(t_, tuple) and len(t_) == 3:
            parts.append(mixed(*t_, size=size))
        elif isinstance(t_, int):
            parts.append(txt(f(t_), int(size * 1.15), INK))
        elif t_ in ('+', '−', '=', '>', '<', '·', ':', '≈'):
            parts.append(txt(t_, int(size * 1.15), BLUE))
        else:
            parts.append(txt(t_, int(size * 1.0), INK))
    return hstack(parts, int(size * 0.25))


def DEC(*toks, size=62):
    """onluq kəsrli ifadə; BOX2 = '□,□'"""
    parts = []
    for t_ in toks:
        if t_ == 'BOX2':
            parts.append(hstack([box(int(size * 1.3), int(size * 1.3)), txt(',', size, INK), box(int(size * 1.3), int(size * 1.3))], 4))
        elif t_ is BOX:
            parts.append(box(int(size * 1.3), int(size * 1.3)))
        elif t_ in ('+', '−', '=', '>', '<', '·', ':'):
            parts.append(txt(t_, size, BLUE))
        else:
            parts.append(txt(t_, size, INK))
    return hstack(parts, int(size * 0.25))


def tenths(k, n=10, w=420, h=70, color=(102, 187, 106)):
    return frac_bar(n, k, w, h, color)


def wholes(nw, k, n, w=300, h=60, color=(255, 183, 77)):
    bars = [frac_bar(n, n, w, h, color) for _ in range(nw)] + ([frac_bar(n, k, w, h, color)] if k else [])
    return vstack(bars, 10)


def pie(parts_, size=260):
    """parts_ = [(hissə, rəng, yazı)]"""
    im, d = vec(size + 20, size + 20)
    a0 = -90
    c = (size / 2 + 10)
    for frac_, col, lab in parts_:
        a1 = a0 + 360 * frac_
        d.pieslice([10 * S, 10 * S, (size + 10) * S, (size + 10) * S], a0, a1, fill=col, outline=WHITE, width=5 * S)
        mid = math.radians((a0 + a1) / 2)
        if lab:
            d.text(((c + size * 0.28 * math.cos(mid)) * S, (c + size * 0.28 * math.sin(mid)) * S), lab, font=font(30 * S), fill=INK, anchor='mm')
        a0 = a1
    return done(im)


def legend(items, size=34):
    return vstack([hstack([dot_(col, 30), txt(lab, size, INK)], 10) for col, lab in items], 8, 'left')


def dot_(col, size=30):
    im, d = vec(size + 6, size + 6)
    d.rounded_rectangle([3 * S, 3 * S, (size + 3) * S, (size + 3) * S], 6 * S, fill=col, outline=INK, width=2 * S)
    return done(im)


def picto(rows_, icon='🎫', unit=8, size=40):
    lines = []
    for name, k in rows_:
        lines.append(hstack([txt(name, 30, INK), hstack([em(icon, size) for _ in range(k)], 2)], 14))
    lines.append(hstack([em(icon, size), txt('= %d bilet' % unit, 30, GREY)], 8))
    return vstack(lines, 10, 'left')


def stack(hs, a=56, col=(255, 183, 77)):
    depth = len(hs)
    ncol = max(len(r) for r in hs)
    hmax = max(max(r) for r in hs)
    k = 0.5
    W = int(ncol * a + depth * a * k + 20)
    H = int(hmax * a + depth * a * k + 20)
    im, d = vec(W, H)
    top = tuple(min(255, int(c * 1.15)) for c in col)
    side = tuple(int(c * 0.78) for c in col)
    for yi, row_ in enumerate(hs):
        dep = depth - 1 - yi
        for x, hh in enumerate(row_):
            for z in range(hh):
                X = 10 + x * a + dep * a * k
                Y = H - 10 - z * a - dep * a * k
                f_ = [(X, Y), (X + a, Y), (X + a, Y - a), (X, Y - a)]
                t_ = [(X, Y - a), (X + a, Y - a), (X + a + a * k, Y - a - a * k), (X + a * k, Y - a - a * k)]
                s_ = [(X + a, Y), (X + a + a * k, Y - a * k), (X + a + a * k, Y - a - a * k), (X + a, Y - a)]
                for poly__, c in ((s_, side), (t_, top), (f_, col)):
                    d.polygon([(px * S, py * S) for px, py in poly__], fill=c, outline=INK, width=3 * S)
    return done(im)


def box3d(a, b, c, unit=26, col=(144, 202, 249), labels=None):
    """düzbucaqlı paralelepiped; a uzunluq, b en (dərinlik), c hündürlük"""
    k = 0.5
    W, H = a * unit + b * unit * k + 200, c * unit + b * unit * k + 70
    im, d = vec(int(W), int(H))
    X, Y = 110, H - 40
    fr_ = [(X, Y), (X + a * unit, Y), (X + a * unit, Y - c * unit), (X, Y - c * unit)]
    dx, dy = b * unit * k, -b * unit * k
    top_ = [fr_[3], fr_[2], (fr_[2][0] + dx, fr_[2][1] + dy), (fr_[3][0] + dx, fr_[3][1] + dy)]
    side_ = [fr_[1], (fr_[1][0] + dx, fr_[1][1] + dy), (fr_[2][0] + dx, fr_[2][1] + dy), fr_[2]]
    for p_, cc in ((side_, tuple(int(v * 0.8) for v in col)), (top_, tuple(min(255, int(v * 1.1)) for v in col)), (fr_, col)):
        d.polygon([(x * S, y * S) for x, y in p_], fill=cc, outline=INK, width=4 * S)
    if labels:
        la, lb, lc = labels
        d.text(((X + a * unit / 2) * S, (Y + 22) * S), la, font=font(28 * S), fill=INK, anchor='mm')
        d.text(((fr_[1][0] + dx / 2 + 26) * S, (Y + dy / 2 + 4) * S), lb, font=font(28 * S), fill=INK, anchor='lm')
        d.text(((X - 10) * S, (Y - c * unit / 2) * S), lc, font=font(28 * S), fill=INK, anchor='rm')
    return done(im)


def U(val, unit_, size=60):
    return hstack([txt(val, size, INK), txt(unit_, int(size * 0.8), GREY)], 8)


def conv(left, right_unit, size=60):
    """'3 km' = □ m"""
    return hstack([txt(left, size, INK), txt('=', size, BLUE), box(int(size * 2.4), int(size * 1.3)), txt(right_unit, int(size * 0.8), GREY)], 14)


def bigbox(w=220, h=90):
    return box(w, h)




# ---------------------------------------------------------------- 5–6-cı sinif əlavələri
def ck(t, **kw):
    """son tapşırığın yoxlamasına əlavə: frac, neg, raw, pre, suf, sep"""
    t.problems[-1]['check'].update(kw)


def dstr(x):
    """0.125 → '0,125'"""
    return str(x).replace('.', ',')


def frac_num(t, ins, ans, stem, pre=None, suf=None):
    """cavab kəsrdir: ans=(surət, məxrəc) və ya (tam, surət, məxrəc); xanalar üst-üstə"""
    disp = ('%d/%d' % ans) if len(ans) == 2 else ('%d %d/%d' % ans)
    t.num(ins, list(ans), stem, disp=(pre or '') + disp + (suf or ''))
    ck(t, frac=1, **({'pre': pre} if pre else {}), **({'suf': suf} if suf else {}))


def dec_num(t, ins, ans, stem, suf=None):
    """cavab onluq kəsrdir, məs. '0,075': iki xana (tam hissə, vergüldən sonrakı rəqəmlər)"""
    w, fpart = ans.split(',')
    t.num(ins, [w, fpart], stem, disp=ans + (' ' + suf if suf else ''))
    ck(t, sep=',', raw=1, **({'suf': suf} if suf else {}))


def pct_num(t, ins, ans, stem):
    t.num(ins, [ans], stem, disp='%s%%' % ans)
    ck(t, suf='%')


def fline(den, maxv=2, marks=(), w=860, size=30, label_every=None, letters=None):
    """kəsr ədəd oxu: 0..maxv, hər tam den hissəyə bölünüb.
    marks = [(surət, 'A' / BOX / None)] — nöqtə və üstündə hərf və ya boş xana"""
    n = den * maxv
    unit = (w - 80) / n
    H = 150
    im, d = vec(w, H)
    y = 70
    d.line([(30 * S, y * S), ((w - 20) * S, y * S)], fill=INK, width=4 * S)
    d.polygon([((w - 8) * S, y * S), ((w - 26) * S, (y - 9) * S), ((w - 26) * S, (y + 9) * S)], fill=INK)
    for k in range(n + 1):
        x = 40 + k * unit
        big = k % den == 0
        d.line([(x * S, (y - (14 if big else 8)) * S), (x * S, (y + (14 if big else 8)) * S)], fill=INK, width=(4 if big else 2) * S)
        if big:
            d.text((x * S, (y + 40) * S), str(k // den), font=font(size * S), fill=INK, anchor='mm')
    im = done(im)
    for k, lab in marks:
        x = 40 + k * unit
        dd = ImageDraw.Draw(im)
        dd.ellipse([x - 9, y - 9, x + 9, y + 9], fill=RED)
        if lab is BOX:
            b = box(50, 50, width=4, radius=10)
            im.alpha_composite(b, (int(x - 25), 2))
        elif lab:
            tl = txt(lab, size, RED)
            im.alpha_composite(tl, (int(x - tl.width / 2), 4))
    return im


def grid100(k, color=(66, 165, 245), cell=30, cells=None):
    """100 xanalı kvadrat: ilk k xana (sütun-sütun) rənglənir"""
    cs = cells if cells is not None else [(i // 10, i % 10) for i in range(k)]
    return area_grid(cs, 10, 10, cell, color)


def ptable(heads, rows, size=34):
    return tab([heads] + rows, size)


def tiles(k, d, size=30, fill=(220, 237, 200)):
    """k dənə 1/d kartı yan-yana"""
    return hstack([frame(fr(1, d, size), padding=8, color=INK, width=3, radius=6, fill=fill) for _ in range(k)], 0)


def words(s_, size=40):
    return chip(s_, size, fill=(255, 248, 225), outline=GREY)


# ---------------------------------------------------------------- avtomatik cavab (Fraction / Decimal)
from fractions import Fraction as Fr
from decimal import Decimal as Dm


def f2t(x):
    """Fraction → FX işarəsi: tam ədəd, (a, b) və ya (tam, a, b)"""
    x = Fr(x)
    if x.denominator == 1:
        return x.numerator
    w, r = divmod(x.numerator, x.denominator)
    return (r, x.denominator) if w == 0 else (w, r, x.denominator)


def ansbox(x):
    x = Fr(x)
    if x.denominator == 1:
        return [BOX]
    return [(BOX, BOX)] if x < 1 else [BOX, (BOX, BOX)]


def fanswer(t, ins, x, stem):
    x = Fr(x)
    if x.denominator == 1:
        t.num(ins, [x.numerator], stem)
    else:
        w, r = divmod(x.numerator, x.denominator)
        frac_num(t, ins, (r, x.denominator) if w == 0 else (w, r, x.denominator), stem)


def fcalc(t, ins, toks, x, size=58):
    """toks: FX işarələri ('=' və cavab xanası avtomatik əlavə olunur)"""
    fanswer(t, ins, x, FX(*toks, '=', *ansbox(x), size=size))


def dfmt(d):
    d = Dm(d)
    s = format(d.normalize(), 'f') if d != d.to_integral() else str(int(d))
    return s.replace('.', ',')


def danswer(t, ins, d, stem, suf=None):
    s = dfmt(d)
    if ',' in s:
        dec_num(t, ins, s, stem, suf=suf)
    else:
        t.num(ins, [int(s)], stem, disp=s + (' ' + suf if suf else ''))
        if suf:
            ck(t, suf=suf)


def dbox(d):
    return 'BOX2' if ',' in dfmt(d) else BOX


def dcalc(t, ins, toks, d, size=58):
    danswer(t, ins, d, DEC(*toks, '=', dbox(d), size=size))


def ncalc(t, ins, toks, v, size=58, suf=None):
    t.num(ins, [v], FX(*toks, '=', BOX, size=size))
    if suf:
        ck(t, suf=suf)


def story(emojis, toks=None, size=80):
    """mətnli məsələ şəkli: emojilər + (istəsə) cavab sətri"""
    row_ = hstack([em(e, size) for e in emojis], 14)
    return row_ if not toks else vstack([row_, FX(*toks, size=50)], 22)


def sup(base, p):
    """7² kimi"""
    return str(base) + {2: '²', 3: '³'}[p]


# ---------------------------------------------------------------- həndəsə (5-2)
def _arc_lbl(d, cx, cy, r, a0, a1, lab, color=RED, fs=30):
    """bucaq qövsü (dərəcə, saat əqrəbinin əksinə, ekranda y aşağı) və yazı"""
    d.arc([(cx - r) * S, (cy - r) * S, (cx + r) * S, (cy + r) * S], -a1, -a0, fill=color, width=4 * S)
    if lab:
        m = math.radians((a0 + a1) / 2)
        rr = r + 30
        d.text(((cx + rr * math.cos(m)) * S, (cy - rr * math.sin(m)) * S), lab, font=font(fs * S), fill=color, anchor='mm')


def ang(deg, lab=None, L=230, color=BLUE):
    """bucaq: təpə solda, bir şüa üfüqi"""
    W, H = L + 120, int(max(90, L * math.sin(math.radians(min(deg, 90))) + 90)) if deg <= 90 else L + 60
    cx = 60 if deg <= 90 else 60 + int(L * 0.6)
    W = max(W, cx + L + 30)
    cy = H - 40
    im, d = vec(W, H)
    d.line([cx * S, cy * S, (cx + L) * S, cy * S], fill=color, width=6 * S)
    ex, ey = cx + L * math.cos(math.radians(deg)), cy - L * math.sin(math.radians(deg))
    d.line([cx * S, cy * S, ex * S, ey * S], fill=color, width=6 * S)
    if deg == 90:
        q = 22
        d.line([(cx + q) * S, cy * S, (cx + q) * S, (cy - q) * S, cx * S, (cy - q) * S], fill=RED, width=4 * S)
        if lab:
            d.text(((cx + 60) * S, (cy - 60) * S), lab, font=font(30 * S), fill=RED, anchor='mm')
    else:
        _arc_lbl(d, cx, cy, 50, 0, deg, lab)
    d.ellipse([(cx - 6) * S, (cy - 6) * S, (cx + 6) * S, (cy + 6) * S], fill=INK)
    return done(im)


def adj(deg, lab1, lab2, L=230):
    """qonşu bucaqlar: düz xətt və ortadan çıxan şüa; lab1 sağdakı (deg), lab2 soldakı"""
    W, H = 2 * L + 80, int(L * 0.85) + 60
    cx, cy = W // 2, H - 40
    im, d = vec(W, H)
    d.line([(cx - L) * S, cy * S, (cx + L) * S, cy * S], fill=BLUE, width=6 * S)
    ex, ey = cx + L * 0.9 * math.cos(math.radians(deg)), cy - L * 0.9 * math.sin(math.radians(deg))
    d.line([cx * S, cy * S, ex * S, ey * S], fill=BLUE, width=6 * S)
    _arc_lbl(d, cx, cy, 46, 0, deg, lab1, RED)
    _arc_lbl(d, cx, cy, 62, deg, 180, lab2, (46, 125, 50))
    d.ellipse([(cx - 6) * S, (cy - 6) * S, (cx + 6) * S, (cy + 6) * S], fill=INK)
    return done(im)


def cross(deg, labs, L=200):
    """iki düz xəttin kəsişməsi; labs = 4 bucağın yazısı (sağdan başlayaraq saat əqrəbinin əksinə)"""
    W, H = 2 * L + 80, int(2 * L * 0.75) + 40
    cx, cy = W // 2, H // 2
    im, d = vec(W, H)
    for a, col in ((0, BLUE), (deg, PURPLE)):
        dx, dy = L * math.cos(math.radians(a)), L * math.sin(math.radians(a))
        k = 1 if a == 0 else 0.75
        d.line([(cx - dx * k) * S, (cy + dy * k) * S, (cx + dx * k) * S, (cy - dy * k) * S], fill=col, width=6 * S)
    bounds = [0, deg, 180, 180 + deg, 360]
    cols = [RED, (46, 125, 50), RED, (46, 125, 50)]
    for i, lab in enumerate(labs):
        if lab:
            _arc_lbl(d, cx, cy, 40 + 8 * (i % 2), bounds[i], bounds[i + 1], lab, cols[i])
    return done(im)


def poly_l(pts, labs=(), unit=40, color=(187, 222, 251), holes=(), fs=28, extra=()):
    """çoxbucaqlı (vahidlərlə: x sağa, y aşağı); labs = [(x, y, yazı)]; holes = ağ çoxbucaqlılar; extra = [(nöqtələr, rəng)]"""
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    W, H = int(max(xs) * unit) + 160, int(max(ys) * unit) + 110
    im, d = vec(W, H)
    T_ = lambda p: ((80 + p[0] * unit) * S, (50 + p[1] * unit) * S)
    d.polygon([T_(p) for p in pts], fill=color, outline=INK, width=5 * S)
    for pp, col in extra:
        d.polygon([T_(p) for p in pp], fill=col, outline=INK, width=4 * S)
    for h_ in holes:
        d.polygon([T_(p) for p in h_], fill=WHITE, outline=INK, width=4 * S)
    for x, y, s_ in labs:
        d.text(T_((x, y)), s_, font=font(fs * S), fill=BLUE, anchor='mm')
    return done(im)


def rtri(a, b, la, lb, unit=34, color=(255, 236, 179)):
    """düzbucaqlı üçbucaq: katetlər a (üfüqi), b (şaquli)"""
    pts = [(0, 0), (0, b), (a, b)]
    im = poly_l(pts, [(-50 / unit, b / 2, lb), (a / 2, b + 26 / unit, la)], unit, color)
    return im


def prism3(la, lb, lh, unit=1.0, color=(255, 224, 178)):
    """oturacağı düzbucaqlı üçbucaq olan prizma"""
    W, H = 460, 330
    im, d = vec(W, H)
    A, B, C = (90, 280), (300, 280), (90, 170)      # ön üçbucaq (düz bucaq A-da)
    dx, dy = 110, -110
    A2, B2, C2 = [(x + dx, y + dy) for x, y in (A, B, C)]
    P = lambda *q: [(x * S, y * S) for x, y in q]
    side = tuple(int(c * 0.85) for c in color)
    d.polygon(P(B, B2, C2, C), fill=side, outline=INK, width=4 * S)
    d.polygon(P(C, C2, A2, A), fill=tuple(min(255, int(c * 1.05)) for c in color), outline=INK, width=4 * S)
    d.polygon(P(A, B, C), fill=color, outline=INK, width=5 * S)
    d.line(P(A, A2), fill=GREY, width=3 * S)
    d.line(P(A2, B2), fill=GREY, width=3 * S)
    d.line([(A[0] + 16) * S, A[1] * S, (A[0] + 16) * S, (A[1] - 16) * S, A[0] * S, (A[1] - 16) * S], fill=INK, width=3 * S)
    f_ = font(26 * S)
    d.text(((A[0] + B[0]) / 2 * S, (A[1] + 24) * S), la, font=f_, fill=BLUE, anchor='mm')
    d.text(((A[0] - 12) * S, (A[1] + C[1]) / 2 * S), lb, font=f_, fill=BLUE, anchor='rm')
    d.text(((B[0] + B2[0]) / 2 * S + 18 * S, (B[1] + B2[1]) / 2 * S + 10 * S), lh, font=f_, fill=BLUE, anchor='lm')
    return done(im)


# ---------------------------------------------------------------- 6-cı sinif: tam ədədlər, nisbət, koordinatlar
SUPD = str.maketrans('0123456789', '⁰¹²³⁴⁵⁶⁷⁸⁹')


def pw(base, p):
    """2⁵ kimi qüvvət yazısı"""
    return str(base) + str(p).translate(SUPD)


def ms(v):
    """mənfi işarəni tipoqrafik edir: -5 → −5"""
    return str(v).replace('-', '−')


def zans(t, ins, v, stem):
    """tam ədəd cavabı (mənfi ola bilər): klaviaturada − düyməsi var"""
    t.num(ins, [v], stem, disp=ms(v))
    ck(t, neg=1)


def zcalc(t, ins, expr_, v, size=60):
    zans(t, ins, v, FX(expr_, '=', BOX, size=size))


def crd(t, ins, xy, stem):
    """koordinat cavabı (x; y)"""
    t.num(ins, list(xy), stem, disp='(%s; %s)' % (ms(xy[0]), ms(xy[1])))
    ck(t, sep=';', pre='(', suf=')', neg=1)


def rat(t, ins, ab, stem, sep=':'):
    t.num(ins, list(ab), stem, disp=(' %s ' % sep).join(str(v) for v in ab))
    ck(t, sep=sep)


def zline(a, b, marks=(), unit=None, w=860, size=28):
    """tam ədədlər oxu a..b; marks = [(ədəd, 'A' / BOX)]"""
    n = b - a
    unit = unit or (w - 80) / n
    W = int(n * unit + 80)
    im, d = vec(W, 150)
    y = 75
    d.line([(20 * S, y * S), ((W - 14) * S, y * S)], fill=INK, width=4 * S)
    d.polygon([((W - 4) * S, y * S), ((W - 22) * S, (y - 9) * S), ((W - 22) * S, (y + 9) * S)], fill=INK)
    for k in range(n + 1):
        x = 40 + k * unit
        v = a + k
        d.line([(x * S, (y - 10) * S), (x * S, (y + 10) * S)], fill=INK, width=(5 if v == 0 else 3) * S)
        d.text((x * S, (y + 36) * S), ms(v), font=font(size * S), fill=RED if v < 0 else INK, anchor='mm')
    im = done(im)
    dd = ImageDraw.Draw(im)
    for v, lab in marks:
        x = 40 + (v - a) * unit
        dd.ellipse([x - 9, y - 9, x + 9, y + 9], fill=BLUE)
        if lab is BOX:
            im.alpha_composite(box(46, 46, width=4, radius=10), (int(x - 23), 4))
        elif lab:
            tl = txt(lab, 32, BLUE)
            im.alpha_composite(tl, (int(x - tl.width / 2), 6))
    return im


def cgrid(n=5, pts=(), cell=34, poly_=None, color=(187, 222, 251)):
    """dörd rüblü koordinat müstəvisi −n..n; pts = [(x, y, 'A')]"""
    W = 2 * n * cell + 56
    im, d = vec(W, W)
    O = W / 2
    P = lambda x, y: ((O + x * cell) * S, (O - y * cell) * S)
    if poly_:
        d.polygon([P(x, y) for x, y in poly_], fill=color, outline=BLUE, width=4 * S)
    for k in range(-n, n + 1):
        d.line([P(k, -n), P(k, n)], fill=(207, 216, 220), width=2 * S)
        d.line([P(-n, k), P(n, k)], fill=(207, 216, 220), width=2 * S)
    d.line([P(-n - 0.6, 0), P(n + 0.6, 0)], fill=INK, width=4 * S)
    d.line([P(0, -n - 0.6), P(0, n + 0.6)], fill=INK, width=4 * S)
    f_ = font(20 * S)
    for k in range(-n, n + 1):
        if k:
            d.text((P(k, 0)[0], P(k, 0)[1] + 16 * S), ms(k), font=f_, fill=GREY, anchor='mm')
            d.text((P(0, k)[0] - 16 * S, P(0, k)[1]), ms(k), font=f_, fill=GREY, anchor='mm')
    d.text((P(n + 0.6, 0)[0], P(n + 0.6, 0)[1] - 18 * S), 'x', font=font(26 * S), fill=INK, anchor='mm')
    d.text((P(0, n + 0.6)[0] + 18 * S, P(0, n + 0.6)[1]), 'y', font=font(26 * S), fill=INK, anchor='mm')
    d.text((P(0, 0)[0] - 14 * S, P(0, 0)[1] + 16 * S), '0', font=f_, fill=GREY, anchor='mm')
    for x, y, lab in pts:
        cx, cy = P(x, y)
        r = 8 * S
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=RED)
        if lab:
            d.text((cx + 18 * S, cy - 18 * S), lab, font=font(28 * S), fill=RED, anchor='mm')
    return done(im)


# ---------------------------------------------------------------- 6-2: Venn, paralel xətlər, üçbucaq elementləri, dairə, silindr
def venn(a, ab, b, la='A', lb='B', out=None, W=520, H=300):
    im, d = vec(W, H)
    d.rounded_rectangle([4 * S, 4 * S, (W - 4) * S, (H - 4) * S], 18 * S, outline=GREY, width=3 * S)
    r = 105
    c1, c2, cy = W / 2 - 62, W / 2 + 62, H / 2 + 14
    for cx, col in ((c1, (255, 167, 38, 90)), (c2, (66, 165, 245, 90))):
        d.ellipse([(cx - r) * S, (cy - r) * S, (cx + r) * S, (cy + r) * S], fill=col, outline=INK, width=4 * S)
    f_ = font(34 * S)
    for x, v in ((c1 - 55, a), (W / 2, ab), (c2 + 55, b)):
        d.text((x * S, cy * S), str(v), font=f_, fill=INK, anchor='mm')
    d.text(((c1 - 60) * S, 26 * S), la, font=font(26 * S), fill=(230, 81, 0), anchor='mm')
    d.text(((c2 + 60) * S, 26 * S), lb, font=font(26 * S), fill=(21, 101, 192), anchor='mm')
    if out is not None:
        d.text(((W - 16) * S, (H - 26) * S), str(out), font=font(26 * S), fill=INK, anchor='rm')
    return done(im)


def trans(deg, labs, L=230):
    """iki paralel düz xətt (a, b) və kəsən; deg = 1-ci bucaq. labs: {1..8: yazı}. 1 sağ-yuxarı, 2 sol-yuxarı, 3 sol-aşağı, 4 sağ-aşağı (yuxarı kəsişmə); 5–8 aşağı kəsişmədə eyni qayda ilə"""
    W, H = 2 * L + 120, 360
    im, d = vec(W, H)
    y1, y2 = 110, 250
    cx = W / 2
    for y, nm in ((y1, 'a'), (y2, 'b')):
        d.line([(30 * S, y * S), ((W - 30) * S, y * S)], fill=BLUE, width=5 * S)
        d.text(((W - 20) * S, (y - 18) * S), nm, font=font(26 * S), fill=BLUE, anchor='mm')
    k = 1 / math.tan(math.radians(deg))
    xm = (y2 - y1) / 2
    x1, x2 = cx + xm * k, cx - xm * k
    ext = 90
    dx = ext * k
    d.line([((x1 + dx) * S, (y1 - ext) * S), ((x2 - dx) * S, (y2 + ext) * S)], fill=PURPLE, width=5 * S)
    for (px, py), base in (((x1, y1), 0), ((x2, y2), 4)):
        bounds = [(0, deg), (deg, 180), (180, 180 + deg), (180 + deg, 360)]
        for i, (a0, a1) in enumerate(bounds):
            lab = labs.get(base + i + 1)
            if lab:
                _arc_lbl(d, px, py, 30, a0, a1, lab, RED if lab != '?' else (46, 125, 50), 26)
    return done(im)


def tri_el(kind, size=230):
    """üçbucaq ABC və A-dan çəkilmiş median / tənbölən / hündürlük"""
    A, B, C = (0.38, 0.05), (0.0, 0.95), (1.0, 0.95)
    im, d = vec(size + 120, size + 90)
    P = lambda p: ((p[0] * size + 60) * S, (p[1] * size + 40) * S)
    d.polygon([P(A), P(B), P(C)], fill=(255, 243, 224), outline=INK, width=4 * S)
    if kind == 'median':
        M = ((B[0] + C[0]) / 2, B[1])
        for xx in ((B[0] + M[0]) / 2, (M[0] + C[0]) / 2):
            d.line([P((xx, B[1] - 0.04)), P((xx, B[1] + 0.04))], fill=RED, width=3 * S)
    elif kind == 'height':
        M = (A[0], B[1])
        q = 0.05
        d.line([P((M[0] + q, M[1])), P((M[0] + q, M[1] - q)), P((M[0], M[1] - q))], fill=RED, width=3 * S)
    else:
        a_ = math.atan2(B[1] - A[1], B[0] - A[0]); c_ = math.atan2(C[1] - A[1], C[0] - A[0])
        m_ = (a_ + c_) / 2
        tt = (B[1] - A[1]) / math.sin(m_)
        M = (A[0] + tt * math.cos(m_), B[1])
        for a0, a1 in ((a_, m_), (m_, c_)):
            d.arc([P((A[0] - 0.09, A[1] - 0.09)), P((A[0] + 0.09, A[1] + 0.09))], math.degrees(min(a0, a1)), math.degrees(max(a0, a1)), fill=RED, width=3 * S)
    d.line([P(A), P(M)], fill=RED, width=4 * S)
    f_ = font(26 * S)
    for p, nm, dx, dy in ((A, 'A', 0, -0.06), (B, 'B', -0.05, 0.03), (C, 'C', 0.05, 0.03), (M, 'M', 0, 0.08)):
        d.text(P((p[0] + dx, p[1] + dy)), nm, font=f_, fill=INK, anchor='mm')
    return done(im)


def tri_h(la, lh, unit=30, a=8, h=5, off=2.5):
    """üçbucaq: oturacaq a, hündürlük h (qırıq xətt)"""
    pts = [(0, h), (a, h), (off, 0)]
    im = poly_l(pts, [(a / 2, h + 26 / unit, la), (off + 40 / unit, h / 2, lh)], unit, (255, 236, 179))
    dd = ImageDraw.Draw(im)
    x = 80 + off * unit
    for y in range(int(50), int(50 + h * unit), 14):
        dd.line([x, y, x, y + 7], fill=RED, width=3)
    return im


def para(la, lh, unit=30, a=8, h=4, sh=2):
    pts = [(sh, 0), (a + sh, 0), (a, h), (0, h)]
    im = poly_l(pts, [(a / 2, h + 26 / unit, la), (sh + 40 / unit, h / 2, lh)], unit, (200, 230, 201))
    dd = ImageDraw.Draw(im)
    x = 80 + sh * unit
    for y in range(50, int(50 + h * unit), 14):
        dd.line([x, y, x, y + 7], fill=RED, width=3)
    return im


def rhomb(l1, l2, unit=26, d1=8, d2=6):
    pts = [(d1 / 2, 0), (d1, d2 / 2), (d1 / 2, d2), (0, d2 / 2)]
    im = poly_l(pts, [(d1 / 2 + 0.9, d2 / 2 - 0.5, l1), (d1 / 2 + 0.7, d2 * 0.78, l2)], unit, (248, 187, 208))
    dd = ImageDraw.Draw(im)
    T_ = lambda p: (80 + p[0] * unit, 50 + p[1] * unit)
    dd.line([T_((0, d2 / 2)), T_((d1, d2 / 2))], fill=RED, width=3)
    dd.line([T_((d1 / 2, 0)), T_((d1 / 2, d2))], fill=RED, width=3)
    return im


def circ(lab, kind='r', R=110):
    W = 2 * R + 60
    im, d = vec(W, W)
    c = W / 2
    d.ellipse([(c - R) * S, (c - R) * S, (c + R) * S, (c + R) * S], fill=(225, 245, 254), outline=INK, width=5 * S)
    d.ellipse([(c - 5) * S, (c - 5) * S, (c + 5) * S, (c + 5) * S], fill=INK)
    x0 = c if kind == 'r' else c - R
    d.line([(x0 * S, c * S), ((c + R) * S, c * S)], fill=RED, width=4 * S)
    d.text((((x0 + c + R) / 2) * S, (c - 22) * S), lab, font=font(28 * S), fill=RED, anchor='mm')
    return done(im)


def cyl(lr, lh, w=180, h=200, e=34):
    W, H = w + 140, h + 2 * e + 40
    im, d = vec(W, H)
    x0, y0 = 40, 20 + e
    col = (178, 223, 219)
    d.rectangle([x0 * S, y0 * S, (x0 + w) * S, (y0 + h) * S], fill=col)
    d.ellipse([x0 * S, (y0 + h - e) * S, (x0 + w) * S, (y0 + h + e) * S], fill=col, outline=INK, width=4 * S)
    d.rectangle([(x0 + 2) * S, (y0 + h - e) * S, (x0 + w - 2) * S, (y0 + h) * S], fill=col)
    d.line([(x0 * S, y0 * S), (x0 * S, (y0 + h) * S)], fill=INK, width=4 * S)
    d.line([((x0 + w) * S, y0 * S), ((x0 + w) * S, (y0 + h) * S)], fill=INK, width=4 * S)
    d.arc([x0 * S, (y0 + h - e) * S, (x0 + w) * S, (y0 + h + e) * S], 0, 180, fill=INK, width=4 * S)
    d.ellipse([x0 * S, (y0 - e) * S, (x0 + w) * S, (y0 + e) * S], fill=(224, 242, 241), outline=INK, width=4 * S)
    cx = x0 + w / 2
    d.line([(cx * S, y0 * S), ((x0 + w) * S, y0 * S)], fill=RED, width=4 * S)
    d.text(((cx + w / 4) * S, (y0 - 16) * S), lr, font=font(26 * S), fill=RED, anchor='mm')
    d.text(((x0 + w + 12) * S, (y0 + h / 2) * S), lh, font=font(26 * S), fill=BLUE, anchor='lm')
    return done(im)
