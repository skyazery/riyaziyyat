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
