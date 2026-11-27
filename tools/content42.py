"""4-cü sinif riyaziyyat, 2-ci hissə: 20 mövzu (171–190), hər mövzuda 10 tapşırıq.
Run: python3 tools/content42.py [OUTDIR]   (default ~/riyaziyyat/4-2)"""
import math, os, sys
from bookgen import *

init(sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser('~/riyaziyyat/4-2'))
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


# ============================================================ 171
t = T(171, 'Bərabər kəsrlər',
      'Kəsrin surət və məxrəcini sıfırdan fərqli eyni ədədə vurduqda və ya böldükdə ona bərabər kəsr alınır: 2/3 = 4/6, 9/12 = 3/4. Kəsrin surət və məxrəcini eyni ədədə bölmək kəsri ixtisar etmək deməkdir.',
      vstack([FX((2, 3), '=', (4, 6)), hstack([frac_bar(3, 2, 360, 56), ], 0), frac_bar(6, 4, 360, 56)], 14))
for a, b, c, dd, ans, where in [(4, 5, BOX, 10, 8, 0), (3, 4, BOX, 12, 9, 0), (10, 12, 5, BOX, 6, 1), (12, 20, 3, BOX, 5, 1), (3, 4, BOX, 16, 12, 0), (5, 7, 30, BOX, 42, 1)]:
    t.num('Bərabər kəsr alınması üçün boş xanaya uyğun ədədi yazın.', [ans], FX((a, b), '=', (c, dd), size=64))
t.choice('Hansı kəsr ikidə birə bərabərdir? Dairəyə alın.', ['4/8', '3/5', '2/6'], 0, stem=fr(1, 2, 64))
t.choice('Digər ikisinə bərabər olmayan kəsri tapın. Dairəyə alın.', ['6/10', '8/20', '3/5'], 1)
numsep(t, 'Kəsri ixtisar edin. İxtisar olunmayan kəsri yazın: əvvəl surəti, sonra məxrəci.', [2, 3], FX((24, 36), '=', (BOX, BOX), size=64), '/', disp='2/3')
t.choice('Rənglənmiş hissələr bərabərdirmi? Dairəyə alın.', ['Bəli', 'Xeyr'], 0, stem=hstack([frac_circle(4, 2, 160), frac_circle(2, 1, 160)], 40))

# ============================================================ 172
t = T(172, 'Kəsrlərin müqayisəsi',
      'Məxrəcləri eyni olan kəsrlərdən surəti böyük olan kəsr böyükdür: 5/8 > 3/8. Surətləri eyni olan kəsrlərdən məxrəci kiçik olan kəsr böyükdür: 1/3 > 1/5.',
      vstack([FX((5, 8), '>', (3, 8)), FX((1, 3), '>', (1, 5))], 16))
t.sign('Kəsrləri müqayisə edin. Dairələrə >, < və ya = yazın.', [('5/8', '3/8'), ('2/9', '7/9')], ['>', '<'])
t.sign('Kəsrləri müqayisə edin. Dairələrə işarə yazın.', [('1/3', '1/5'), ('3/4', '3/7')], ['>', '>'])
t.sign('Kəsrləri müqayisə edin. Dairələrə işarə yazın.', [('1/2', '2/4'), ('2/10', '1/10')], ['=', '>'])
t.choice('Ən böyük kəsri dairəyə alın.', ['3/10', '7/10', '5/10'], 1)
t.choice('Ən kiçik kəsri dairəyə alın.', ['1/2', '1/6', '1/4'], 1)
t.choice('Kəsrləri artan sıra ilə düzün: ən kiçikdən başlayaraq toxunun.', ['5/9', '2/9', '8/9'], [1, 0, 2], mode='order', hint='Əvvəlcə ən kiçik kəsrə toxunun.', disp='2/9, 5/9, 8/9')
t.choice('Lalə pitsanın 3/8 hissəsini, Samir 5/8 hissəsini yedi. Kim çox yedi? Dairəyə alın.', ['Samir', 'Lalə', 'Bərabər'], 0, stem=em('🍕', 110))
t.choice('Hansı şəkildə rənglənmiş hissə böyükdür? Dairəyə alın.', [frac_bar(4, 3, 300, 60), frac_bar(4, 1, 300, 60)], 0)
t.num('Bərabərsizlik doğru olsun deyə boş xanaya ən kiçik ədədi yazın.', [6], FX((BOX, 7), '>', (5, 7), size=64))
t.sign('Kəsri 1 ilə müqayisə edin. Dairələrə işarə yazın.', [('7/7', '1'), ('3/5', '1')], ['=', '<'])

# ============================================================ 173
t = T(173, 'Məxrəcləri bərabər olan kəsrlərin toplanması və çıxılması',
      'Məxrəcləri eyni olan kəsrləri topladıqda surətləri toplayır, çıxdıqda isə surətləri çıxırıq. Məxrəc dəyişmir: 2/7 + 3/7 = 5/7, 5/9 − 2/9 = 3/9.',
      vstack([FX((2, 7), '+', (3, 7), '=', (5, 7)), FX((5, 9), '−', (2, 9), '=', (3, 9))], 16))
for toks, ans in [(((2, 7), '+', (3, 7), '=', (BOX, 7)), 5), (((1, 5), '+', (3, 5), '=', (BOX, 5)), 4), (((5, 9), '−', (2, 9), '=', (BOX, 9)), 3),
                  (((7, 10), '−', (4, 10), '=', (BOX, 10)), 3), (((3, 8), '+', (4, 8), '=', (BOX, 8)), 7), ((1, '−', (3, 8), '=', (BOX, 8)), 5),
                  (((4, 12), '+', (5, 12), '+', (2, 12), '=', (BOX, 12)), 11)]:
    t.num('Hesablayın. Boş xanaya surəti yazın.', [ans], FX(*toks, size=60))
t.num('Lalə tortun 2/6 hissəsini, Samir 3/6 hissəsini yedi. Birlikdə tortun neçə altıda birini yedilər?', [5], vstack([em('🎂', 100), FX((2, 6), '+', (3, 6), '=', (BOX, 6))], 14))
t.num('Pitsanın 5/8 hissəsi qalmışdı. Uşaqlar 3/8 hissəsini yedi. Pitsanın neçə səkkizdə biri qaldı?', [2], vstack([em('🍕', 100), FX((5, 8), '−', (3, 8), '=', (BOX, 8))], 14))
t.choice('Cəmi tapın. Dairəyə alın.', ['4/5', '4/10', '2/10'], 0, stem=FX((2, 5), '+', (2, 5), '='))

# ============================================================ 174
t = T(174, 'Qarışıq ədədlər',
      'Tam və kəsr hissələrdən ibarət ədədlər qarışıq ədədlərdir. 1 2/7 ədədi 1 tam və 2/7 kəsr hissəsindən ibarətdir: 1 2/7 = 1 + 2/7. Belə oxunur: bir tam yeddidə iki.',
      vstack([FX((1, 2, 7), '=', 1, '+', (2, 7)), wholes(1, 2, 7, 360, 50)], 14))
t.choice('Şəkilə uyğun qarışıq ədəd hansıdır? Dairəyə alın.', [mixed(2, 1, 3), mixed(1, 2, 3), mixed(3, 1, 2)], 0, stem=wholes(2, 1, 3))
t.choice('Şəkilə uyğun qarışıq ədəd hansıdır? Dairəyə alın.', [mixed(1, 1, 4), mixed(1, 3, 4), mixed(2, 3, 4)], 1, stem=hstack([frac_circle(4, 4, 150), frac_circle(4, 3, 150)], 20))
t.num('Qarışıq ədədin tam hissəsini yazın.', [3], hstack([mixed(3, 1, 2, 70), arrow(), box()], 14))
t.num('Qarışıq ədədin kəsr hissəsinin surətini yazın.', [2], hstack([mixed(5, 2, 3, 70), arrow(), box()], 14))
t.num('Boş xanaya uyğun ədədi yazın.', [2], FX((1, 2, 7), '=', 1, '+', (BOX, 7), size=64))
t.num('Boş xanaya uyğun ədədi yazın.', [8], FX(2, '=', (BOX, 4), size=64))
t.num('Qarışıq ədədi kəsr şəklində yazın. Boş xanaya surəti yazın.', [7], FX((1, 3, 4), '=', (BOX, 4), size=64))
t.num('Kəsri qarışıq ədəd şəklində yazın. Boş xanaya kəsr hissəsinin surətini yazın.', [1], FX((9, 4), '=', (2, BOX, 4), size=64) if False else hstack([fr(9, 4, 64), txt('=', 72, BLUE), txt('2', 80, INK), fr(BOX, 4, 64)], 14))
t.choice('«İki tam doqquzda dörd» hansı ədəddir? Dairəyə alın.', [mixed(2, 4, 9), mixed(4, 2, 9), mixed(2, 9, 4)], 0)
t.choice('Ən böyük ədədi dairəyə alın.', [mixed(1, 1, 3), mixed(2, 1, 5), mixed(1, 4, 5)], 1)

# ============================================================ 175
t = T(175, 'Onluq kəsrlər',
      'Məxrəci 10 və 100 olan kəsrləri onluq kəsr şəklində yazmaq olar: 1/10 = 0,1; 4/10 = 0,4; 2 3/10 = 2,3. Tam hissədən sonra vergül qoyulur. Vergüldən sonra birinci mərtəbə ondabirlər, ikinci mərtəbə yüzdəbirlər mərtəbəsidir.',
      vstack([FX((4, 10), '=', '0,4'), FX((2, 3, 10), '=', '2,3'), tenths(4)], 14))
for a_, b_, w_, ans in [(3, 10, 0, [0, 3]), (7, 10, 0, [0, 7]), (3, 10, 2, [2, 3]), (2, 10, 1, [1, 2])]:
    stem = hstack([fr(a_, b_, 64) if not w_ else mixed(w_, a_, b_, 64), txt('=', 72, BLUE), DEC('BOX2')], 14)
    numsep(t, 'Onluq kəsr şəklində yazın: vergüldən əvvəl tam hissəni, sonra ondabirləri yazın.', ans, stem, ',', disp='%d,%d' % tuple(ans))
t.num('Boş xanaya uyğun ədədi yazın.', [4], hstack([txt('0,4', 72), txt('=', 72, BLUE), fr(BOX, 10, 64)], 14))
t.num('Boş xanaya uyğun ədədi yazın.', [25], hstack([txt('0,25', 72), txt('=', 72, BLUE), fr(BOX, 100, 64)], 14))
numsep(t, 'Şəkildə rənglənmiş hissəni onluq kəsrlə yazın.', [0, 6], vstack([tenths(6), DEC('BOX2')], 16), ',', disp='0,6')
t.choice('«İki tam onda üç» necə yazılır? Dairəyə alın.', ['2,3', '3,2', '20,3'], 0)
t.num('1 ədədində neçə dənə 0,1 var?', [10], hstack([txt('1 = □ · 0,1', 64).copy() if False else txt('1', 72, INK), txt('=', 72, BLUE), box(), txt('· 0,1', 64, INK)], 14))
t.choice('3,7 ədədində 7 rəqəmi hansı mərtəbədədir? Dairəyə alın.', ['Ondabirlər', 'Təkliklər', 'Yüzdəbirlər'], 0, stem=hstack([txt('3,', 90), txt('7', 90, RED)], 0))

# ============================================================ 176
t = T(176, 'Onluq kəsrlərin müqayisəsi',
      'Onluq kəsrləri müqayisə edərkən əvvəlcə tam hissələri, onlar bərabər olduqda ondabirləri, sonra yüzdəbirləri müqayisə edirik: 2,5 > 1,9; 0,7 > 0,4; 3,45 < 3,48.',
      vstack([DEC('2,5', '>', '1,9'), DEC('0,7', '>', '0,4'), DEC('3,45', '<', '3,48')], 12))
t.sign('Ədədləri müqayisə edin. Dairələrə >, < və ya = yazın.', [('2,5', '1,9'), ('0,7', '0,4')], ['>', '>'])
t.sign('Ədədləri müqayisə edin. Dairələrə işarə yazın.', [('3,45', '3,48'), ('0,5', '0,50')], ['<', '='])
t.sign('Ədədləri müqayisə edin. Dairələrə işarə yazın.', [('1,2', '1,02'), ('4,3', '4,6')], ['>', '<'])
t.choice('Ən böyük ədədi dairəyə alın.', ['0,8', '0,35', '0,6'], 0)
t.choice('Ən kiçik ədədi dairəyə alın.', ['2,1', '1,9', '2,05'], 1)
t.choice('Ədədləri artan sıra ilə düzün: ən kiçikdən başlayaraq toxunun.', ['1,5', '0,9', '1,25'], [1, 2, 0], mode='order', hint='Əvvəlcə ən kiçik ədədə toxunun.', disp='0,9, 1,25, 1,5')
t.choice('Lalənin boyu 1,25 m, Samirin boyu 1,32 m-dir. Kim hündürdür? Dairəyə alın.', ['Samir', 'Lalə'], 0, stem=hstack([em('👧', 90), txt('1,25 m', 50, BLUE), em('👦', 90), txt('1,32 m', 50, BLUE)], 12))
t.choice('Hansı ədəd 1-dən böyükdür? Dairəyə alın.', ['1,1', '0,9', '0,99'], 0)
numsep(t, 'Boş xanalara uyğun onluq kəsri yazın.', [0, 5], DEC('0,4', '<', 'BOX2', '<', '0,6'), ',', disp='0,5')
t.choice('Ən böyük ədədi dairəyə alın.', ['5,07', '5,7', '5,17'], 1)

# ============================================================ 177
t = T(177, 'Onluq kəsrlərin toplanması və çıxılması',
      'Onluq kəsrləri alt-alta toplayanda və ya çıxanda vergülü vergülün altında yazır və natural ədədlər kimi hesablayırıq. Cavabda vergülü eyni yerdə qoyuruq: 2,4 + 1,3 = 3,7; 5,6 − 2,3 = 3,3.',
      vstack([DEC('2,4', '+', '1,3', '=', '3,7'), DEC('5,6', '−', '2,3', '=', '3,3')], 14))
for a_, op, b_, ans in [('2,4', '+', '1,3', [3, 7]), ('0,5', '+', '0,3', [0, 8]), ('1,6', '+', '2,3', [3, 9]), ('4,8', '−', '1,5', [3, 3]),
                        ('6,9', '−', '2,4', [4, 5]), ('3,7', '+', '1,5', [5, 2]), ('5,2', '−', '1,8', [3, 4]), ('12,5', '+', '7,3', [19, 8])]:
    numsep(t, 'Hesablayın. Vergüldən əvvəl tam hissəni, sonra ondabirləri yazın.', ans, DEC(a_, op, b_, '=', 'BOX2'), ',', disp='%d,%d' % tuple(ans))
numsep(t, 'Lalə 1,5 kq alma və 2,3 kq armud aldı. Cəmi neçə kiloqram meyvə aldı?', [3, 8], vstack([hstack([em('🍎', 80), em('🍐', 80)], 10), DEC('1,5', '+', '2,3', '=', 'BOX2')], 14), ',', disp='3,8')
numsep(t, 'Lent 4,5 m idi. Ondan 1,2 m kəsdilər. Neçə metr qaldı?', [3, 3], vstack([em('🎀', 90), DEC('4,5', '−', '1,2', '=', 'BOX2')], 14), ',', disp='3,3')

# ============================================================ 178
t = T(178, 'Pullar və onluq kəsrlər',
      '1 manat 100 qəpikdir. Qəpikləri manatla onluq kəsr şəklində yazmaq olar: 50 qəpik = 0,50 manat; 2 manat 35 qəpik = 2,35 manat.',
      vstack([txt('1 manat = 100 qəpik', 54, BLUE), txt('2 man 35 qəp = 2,35 man', 54, INK)], 14))
numsep(t, 'Manatla onluq kəsr şəklində yazın: vergüldən əvvəl manatı, sonra qəpiyi yazın.', [2, 35], hstack([txt('2 man 35 qəp', 56), txt('=', 64, BLUE), DEC('BOX2'), txt('man', 46, GREY)], 12), ',', disp='2,35')
numsep(t, 'Manatla onluq kəsr şəklində yazın.', [5, 80], hstack([txt('5 man 80 qəp', 56), txt('=', 64, BLUE), DEC('BOX2'), txt('man', 46, GREY)], 12), ',', disp='5,80')
numsep(t, 'Manatla onluq kəsr şəklində yazın.', [7, 25], hstack([txt('7 man 25 qəp', 56), txt('=', 64, BLUE), DEC('BOX2'), txt('man', 46, GREY)], 12), ',', disp='7,25')
t.num('Boş xanaya uyğun ədədi yazın.', [45], hstack([txt('3,45 man = 3 man', 56), box(), txt('qəp', 46, GREY)], 12))
t.num('1 manat neçə qəpikdir?', [100], hstack([txt('1 man =', 60), box(170, 96), txt('qəp', 46, GREY)], 12))
t.num('2,50 manat neçə qəpikdir?', [250], hstack([txt('2,50 man =', 60), box(170, 96), txt('qəp', 46, GREY)], 12))
t.num('450 qəpik neçə manat və neçə qəpikdir? Soldan sağa yazın.', [4, 50], hstack([txt('450 qəp =', 56), box(), txt('man', 40, GREY), box(), txt('qəp', 40, GREY)], 10), disp='4 manat 50 qəpik')
t.choice('Ən böyük məbləği dairəyə alın.', ['3,50 man', '3,05 man', '300 qəp'], 0)
t.num('1 manat, 50 qəpik və 20 qəpik birlikdə neçə qəpikdir?', [170], hstack([coins([1], 80) if False else em('🪙', 80), txt('1 man + 50 qəp + 20 qəp =', 44), box(150, 90)], 10))
t.choice('Dəftər 0,80 manatdır. Bu neçə qəpikdir? Dairəyə alın.', ['80', '8', '800'], 0, stem=em('📓', 100))

# ============================================================ 179
t = T(179, 'Pullarla hesablamalar',
      'Pullarla hesablamada manatı manata, qəpiyi qəpiyə toplayırıq. 100 qəpik yığılanda onu 1 manata çeviririk: 2 man 60 qəp + 1 man 70 qəp = 4 man 30 qəp.',
      vstack([txt('2 man 60 qəp + 1 man 70 qəp', 48), txt('= 4 man 30 qəp', 48, BLUE)], 10))
t.num('Toplayın. Soldan sağa manatı və qəpiyi yazın.', [4, 30], vstack([txt('2 man 60 qəp + 1 man 70 qəp =', 46), hstack([box(), txt('man', 40, GREY), box(), txt('qəp', 40, GREY)], 10)], 12), disp='4 manat 30 qəpik')
numsep(t, 'Hesablayın.', [5, 75], DEC('3,40', '+', '2,35', '=', 'BOX2'), ',', disp='5,75')
numsep(t, 'Hesablayın.', [3, 75], DEC('5,00', '−', '1,25', '=', 'BOX2'), ',', disp='3,75')
t.num('Bir çörək 0,60 manatdır. 3 çörək neçə qəpikdir?', [180], vstack([em('🍞', 90), hstack([txt('60 qəp · 3 =', 56), box(150, 90), txt('qəp', 40, GREY)], 10)], 12))
t.num('Lalə 10 manat verib 6,50 manatlıq kitab aldı. Ona nə qədər qalıq qaytarıldı? Soldan sağa yazın.', [3, 50], vstack([em('📗', 90), hstack([box(), txt('man', 40, GREY), box(), txt('qəp', 40, GREY)], 10)], 12), disp='3 manat 50 qəpik')
t.num('Dəftər 1,20 manat, qələm 0,80 manatdır. Birlikdə neçə manatdır?', [2], vstack([hstack([em('📓', 80), em('🖊️', 80)], 10), hstack([txt('1,20 + 0,80 =', 56), box(), txt('man', 40, GREY)], 10)], 12))
t.num('2 kq alma 3,60 manatdır. 1 kq alma neçə qəpikdir?', [180], vstack([em('🍎', 90), hstack([txt('360 qəp : 2 =', 56), box(150, 90), txt('qəp', 40, GREY)], 10)], 12))
t.choice('Samirin 15 manatı var. O, hansını ala bilər? Dairəyə alın.', ['Top', 'Kitab', 'Oyuncaq'], 0, stem=tab([['Top', '12,50 man'], ['Kitab', '16,20 man'], ['Oyuncaq', '15,90 man']], 32))
t.num('Lalə hər gün 0,50 manat yığır. 10 gündə neçə manat yığar?', [5], vstack([em('🐷', 90), hstack([txt('0,50 · 10 =', 56), box(), txt('man', 40, GREY)], 10)], 12))
numsep(t, 'Bir bilet 1,20 manatdır. 3 bilet neçə manatdır?', [3, 60], vstack([em('🎫', 90), DEC('1,20', '·', '3', '=', 'BOX2')], 12), ',', disp='3,60')

# ============================================================ 180
EXP = [['Xərclər', 'Yan', 'Fev', 'Mar', 'Apr'], ['Ərzaq', 320, 330, 380, 300], ['Kommunal', 110, 115, 103, 95], ['Telefon', 3, 3, 3, 3],
       ['Mobil danışıq', 27, 30, 32, 28], ['İnternet', 30, 30, 30, 30]]
t = T(180, 'Dəyişən və dəyişməyən xərclər',
      'Məbləği aydan-aya dəyişən xərclər dəyişən xərclərdir: ərzaq, elektrik, qaz. Məbləği dəyişməyən xərclər isə dəyişməyən xərclərdir: internet, telefonun abunə haqqı, kirayə.',
      tab(EXP, 28))
t.choice('Cədvəldə hansı xərc dəyişməyəndir? Dairəyə alın.', ['İnternet', 'Ərzaq', 'Kommunal'], 0, stem=tab(EXP, 26))
t.choice('Dəyişən xərclərə toxunun.', ['Ərzaq', 'Telefon abunə haqqı', 'Qaz', 'Kirayə', 'Geyim'], [0, 2, 4], mode='multi', disp='Ərzaq, Qaz, Geyim')
t.num('Ərzaq xərci fevralda yanvara görə neçə manat artıb?', [10], vstack([tab(EXP[:2], 30), expr2(['330', '−', '320', '=', BOX], 60)], 14))
t.num('Ərzaq xərci aprelda marta görə neçə manat azalıb?', [80], vstack([tab(EXP[:2], 30), expr2(['380', '−', '300', '=', BOX], 60)], 14))
t.num('İnternet hər ay 30 manatdır. 4 ayda neçə manat ödənilir?', [120], vstack([em('🌐', 90), expr2(['30', '·', '4', '=', BOX], 60)], 14))
t.num('Telefonun abunə haqqı ayda 3 manatdır. 12 ayda neçə manat ödənilir?', [36], vstack([em('📱', 90), expr2(['3', '·', '12', '=', BOX], 60)], 14))
t.num('Aprel ayında kommunal xərclər 82, telefon 3, internet 20, nəqliyyat 72 manat olub. Bu xərclərin cəmi neçə manatdır?', [177], expr2(['82', '+', '3', '+', '20', '+', '72', '=', BOX], 56))
t.choice('Hansı ayda ərzaq xərci ən çox olub? Dairəyə alın.', ['Mart', 'Yanvar', 'Aprel'], 0, stem=tab(EXP[:2], 32))
t.num('Mobil danışıq xərcləri 4 ayda cəmi neçə manat olub?', [117], vstack([tab([EXP[0], EXP[4]], 30), expr2(['27', '+', '30', '+', '32', '+', '28', '=', BOX], 52)], 14))
t.num('Ailənin aylıq gəliri 1 200 manat, xərci 950 manatdır. Ailə nə qədər pul qənaət edir?', [250], vstack([em('💰', 90), expr2(['1 200', '−', '950', '=', BOX], 60)], 14))

# ============================================================ 181
t = T(181, 'Uzunluq',
      '1 km = 1 000 m, 1 m = 100 sm, 1 sm = 10 mm. Böyük vahidi kiçik vahidlə ifadə etmək üçün vururuq: 3 km = 3 000 m, 5 m = 500 sm.',
      vstack([txt('1 km = 1 000 m', 54, BLUE), txt('1 m = 100 sm', 54, BLUE), txt('1 sm = 10 mm', 54, BLUE)], 10))
for left, ru, ans in [('3 km', 'm', 3000), ('4 m', 'sm', 400), ('7 sm', 'mm', 70), ('2 km 500 m', 'm', 2500), ('3 m 25 sm', 'sm', 325), ('6 000 m', 'km', 6)]:
    t.num('Uzunluğu %s ilə ifadə edin.' % {'m': 'metr', 'sm': 'santimetr', 'mm': 'millimetr', 'km': 'kilometr'}[ru], [ans], conv(left, ru), disp=f(ans))
t.choice('Ən böyük uzunluğu dairəyə alın.', ['1 km', '900 m', '9 000 sm'], 0)
road = tab([['A – B', '3 km 200 m'], ['B – C', '950 m'], ['C – D', '2 km 870 m']], 30)
t.num('Birinci yol A, B, C nöqtələrindən keçib D-yə çatır. Yolun uzunluğu neçə metrdir?', [7020], vstack([road, hstack([txt('3 200 + 950 + 2 870 =', 46), box(220, 90), txt('m', 40, GREY)], 10)], 12), disp='7 020')
t.num('İkinci yol: 1 km 780 m və 5 km 900 m. Bu yolun uzunluğu neçə metrdir?', [7680], hstack([txt('1 780 + 5 900 =', 50), box(220, 90), txt('m', 40, GREY)], 10), disp='7 680')
t.num('Birinci yol 7 020 m, ikinci yol 7 680 m-dir. Birinci yol neçə metr qısadır?', [660], expr2(['7 680', '−', '7 020', '=', BOX], 60))

# ============================================================ 182
t = T(182, 'Perimetr',
      'Fiqurun perimetri onun bütün tərəflərinin uzunluqlarının cəmidir. Düzbucaqlının perimetri: P = (a + b) · 2. Kvadratın perimetri: P = a · 4.',
      hstack([rect_sides(6, 4, '6 sm', '4 sm', 30), txt('P = (6 + 4) · 2 = 20 sm', 44, BLUE)], 20))
t.num('Düzbucaqlının perimetrini tapın.', [20], vstack([rect_sides(6, 4, '6 sm', '4 sm', 32), hstack([txt('P =', 56), box(), txt('sm', 46, GREY)], 10)], 12))
t.num('Kvadratın perimetrini tapın.', [20], vstack([rect_sides(5, 5, '5 sm', '5 sm', 32), hstack([txt('P =', 56), box(), txt('sm', 46, GREY)], 10)], 12))
t.num('Üçbucağın perimetrini tapın.', [12], vstack([tri([(0.0, 1.0), (1.0, 1.0), (0.0, 0.25)], ('4 sm', '5 sm', '3 sm'), 200), hstack([txt('P =', 56), box(), txt('sm', 46, GREY)], 10)], 12))
t.num('Düzbucaqlının uzunluğu 12 sm, eni 5 sm-dir. Perimetri neçə santimetrdir?', [34], vstack([rect_sides(12, 5, '12 sm', '5 sm', 22), hstack([txt('P =', 56), box(), txt('sm', 46, GREY)], 10)], 12))
t.num('Kvadratın perimetri 36 sm-dir. Tərəfi neçə santimetrdir?', [9], expr2(['36', ':', '4', '=', BOX], 64))
t.num('Düzbucaqlının perimetri 30 sm, uzunluğu 10 sm-dir. Eni neçə santimetrdir?', [5], vstack([expr2(['30', ':', '2', '=', '15'], 54), expr2(['15', '−', '10', '=', BOX], 54)], 10))
t.num('Bağçanın uzunluğu 25 m, eni 15 m-dir. Onun ətrafına neçə metr hasar çəkmək lazımdır?', [80], vstack([em('🌳', 90), expr2(['(25 + 15) · 2', '=', BOX], 56)], 12))
t.choice('Hansı fiqurun perimetri böyükdür? Dairəyə alın.', [rect_sides(6, 2, '6 sm', '2 sm', 26), rect_sides(5, 5, '5 sm', '5 sm', 26)], 1)
t.num('Altıbucaqlının hər tərəfi 4 sm-dir. Perimetri neçə santimetrdir?', [24], hstack([poly(6, 150, (171, 71, 188)), txt('4 sm', 46, INK), arrow(), box()], 12))
t.num('Kvadratın tərəfi 15 sm-dir. Perimetri neçə santimetrdir?', [60], expr2(['15', '·', '4', '=', BOX], 64))

# ============================================================ 183
t = T(183, 'Sahə',
      'Sahə kvadrat vahidlərlə ölçülür: kvadrat santimetr, kvadrat metr. Düzbucaqlının sahəsi uzunluğu ilə eninin hasilinə bərabərdir: S = a · b. Kvadratın sahəsi: S = a · a.',
      hstack([area_grid([(c, r) for c in range(4) for r in range(3)], 4, 3, 40), txt('S = 4 · 3 = 12', 50, BLUE)], 20))
t.num('Fiqurun sahəsi neçə kvadrat vahiddir? Kvadratları sayın.', [12], hstack([area_grid([(c, r) for c in range(4) for r in range(3)], 5, 4, 44), arrow(), box()], 14))
t.num('Düzbucaqlının sahəsini tapın.', [35], vstack([rect_sides(7, 5, '7 sm', '5 sm', 30), hstack([txt('S =', 56), box(), txt('kv. sm', 40, GREY)], 10)], 12))
t.num('Kvadratın sahəsini tapın.', [36], vstack([rect_sides(6, 6, '6 sm', '6 sm', 28), hstack([txt('S =', 56), box(), txt('kv. sm', 40, GREY)], 10)], 12))
t.num('Düzbucaqlının uzunluğu 12 m, eni 10 m-dir. Sahəsi neçə kvadrat metrdir?', [120], expr2(['12', '·', '10', '=', BOX], 64))
t.num('Düzbucaqlının sahəsi 48 kv. sm, uzunluğu 8 sm-dir. Eni neçə santimetrdir?', [6], expr2(['48', ':', '8', '=', BOX], 64))
t.num('Otağın uzunluğu 6 m, eni 4 m-dir. Otağın sahəsi neçə kvadrat metrdir?', [24], vstack([em('🛋️', 90), expr2(['6', '·', '4', '=', BOX], 60)], 12))
t.num('Bağın sahəsi 200 kv. m, eni 10 m-dir. Uzunluğu neçə metrdir?', [20], vstack([em('🌷', 90), expr2(['200', ':', '10', '=', BOX], 60)], 12))
t.choice('Hansı fiqurun sahəsi böyükdür? Dairəyə alın.', [area_grid([(c, r) for c in range(3) for r in range(4)], 3, 4, 34), area_grid([(c, r) for c in range(5) for r in range(2)], 5, 2, 34)], 0)
L_ = [(c, r) for c in range(4) for r in range(2)] + [(0, 2), (1, 2)]
t.num('Fiqurun sahəsi neçə kvadrat vahiddir?', [10], hstack([area_grid(L_, 5, 4, 44), arrow(), box()], 14))
t.num('1 kv. m neçə kvadrat santimetrdir?', [10000], vstack([txt('1 m = 100 sm', 50, GREY), hstack([txt('1 kv. m = 100 · 100 =', 50), box(240, 90), txt('kv. sm', 40, GREY)], 10)], 12), disp='10 000')

# ============================================================ 184
t = T(184, 'Kütlə və tutum',
      '1 t = 1 000 kq, 1 kq = 1 000 q, 1 l = 1 000 ml. Böyük vahidi kiçik vahidlə ifadə etmək üçün 1 000-ə vururuq: 3 kq = 3 000 q, 2 l = 2 000 ml.',
      vstack([txt('1 t = 1 000 kq', 54, BLUE), txt('1 kq = 1 000 q', 54, BLUE), txt('1 l = 1 000 ml', 54, BLUE)], 10))
for left, ru, ans in [('3 kq', 'q', 3000), ('2 t', 'kq', 2000), ('4 l', 'ml', 4000), ('2 kq 500 q', 'q', 2500), ('5 000 q', 'kq', 5), ('1 l 250 ml', 'ml', 1250)]:
    t.num('Boş xanaya uyğun ədədi yazın.', [ans], conv(left, ru), disp=f(ans))
t.choice('Ən ağır olanı dairəyə alın.', ['1 kq', '900 q', '950 q'], 0)
t.num('Bir paket un 2 kq-dır. 6 paket un neçə kiloqramdır?', [12], vstack([em('🛍️', 90), expr2(['2', '·', '6', '=', BOX], 60)], 12))
t.num('Bidonda 10 l süd var idi. 2 l 500 ml süd satıldı. Neçə millilitr süd qaldı?', [7500], vstack([em('🥛', 90), expr2(['10 000', '−', '2 500', '=', BOX], 56)], 12), disp='7 500')
t.num('Stəkana 250 ml su sığır. 1 l su neçə stəkana sığar?', [4], vstack([em('🥤', 90), expr2(['1 000', ':', '250', '=', BOX], 60)], 12))

# ============================================================ 185
t = T(185, 'Həcm',
      'Həcm kub vahidlərlə ölçülür: kub santimetr, kub metr. Düzbucaqlı paralelepipedin həcmi uzunluğu, eni və hündürlüyünün hasilinə bərabərdir: V = a · b · c.',
      hstack([box3d(4, 3, 2, 30, labels=('4 sm', '3 sm', '2 sm')), txt('V = 4 · 3 · 2 = 24', 46, BLUE)], 20))
t.num('Fiqur neçə kub vahiddən qurulub?', [6], hstack([stack([[2, 2, 2]]), arrow(), box()], 14))
t.num('Düzbucaqlı paralelepipedin həcmini tapın.', [24], vstack([box3d(4, 3, 2, 28, labels=('4 sm', '3 sm', '2 sm')), hstack([txt('V =', 56), box(), txt('kub sm', 40, GREY)], 10)], 12))
t.num('Düzbucaqlı paralelepipedin həcmini tapın.', [30], vstack([box3d(5, 2, 3, 28, labels=('5 sm', '2 sm', '3 sm')), hstack([txt('V =', 56), box(), txt('kub sm', 40, GREY)], 10)], 12))
t.num('Kubun tili 3 sm-dir. Həcmi neçə kub santimetrdir?', [27], vstack([box3d(3, 3, 3, 30, (255, 183, 77), labels=('3 sm', '3 sm', '3 sm')), expr2(['3', '·', '3', '·', '3', '=', BOX], 56)], 12))
t.num('Paralelepipedin həcmi 60 kub sm, uzunluğu 5 sm, eni 4 sm-dir. Hündürlüyü neçə santimetrdir?', [3], vstack([expr2(['5', '·', '4', '=', '20'], 54), expr2(['60', ':', '20', '=', BOX], 54)], 10))
t.num('Qutunun uzunluğu 10 sm, eni 5 sm, hündürlüyü 4 sm-dir. Həcmi neçə kub santimetrdir?', [200], vstack([em('📦', 90), expr2(['10', '·', '5', '·', '4', '=', BOX], 56)], 12))
t.num('Kubun tili 2 sm-dir. Həcmi neçə kub santimetrdir?', [8], expr2(['2', '·', '2', '·', '2', '=', BOX], 64))
t.choice('Hansı paralelepipedin həcmi böyükdür? Dairəyə alın.', ['3 · 3 · 3', '5 · 2 · 2', '4 · 2 · 3'], 0)
t.num('Akvariumun uzunluğu 50 sm, eni 20 sm, hündürlüyü 30 sm-dir. Həcmi neçə kub santimetrdir?', [30000], vstack([em('🐠', 90), expr2(['50', '·', '20', '·', '30', '=', BOX], 54)], 12), disp='30 000')
t.num('1 kub dm neçə kub santimetrdir?', [1000], vstack([txt('1 dm = 10 sm', 50, GREY), hstack([txt('10 · 10 · 10 =', 54), box(220, 90)], 10)], 12), disp='1 000')

# ============================================================ 186
t = T(186, 'Zaman',
      '1 sutka = 24 saat, 1 saat = 60 dəqiqə, 1 dəqiqə = 60 saniyə, 1 il = 12 ay. Zaman vahidlərini də çevirmək olar: 2 saat = 120 dəqiqə.',
      vstack([txt('1 sutka = 24 saat', 50, BLUE), txt('1 saat = 60 dəq', 50, BLUE), txt('1 dəq = 60 san', 50, BLUE)], 10))
for left, ru, ans in [('2 saat', 'dəq', 120), ('3 dəq', 'san', 180), ('2 sutka', 'saat', 48), ('1 saat 15 dəq', 'dəq', 75), ('3 il', 'ay', 36), ('180 dəq', 'saat', 3)]:
    t.num('Boş xanaya uyğun ədədi yazın.', [ans], conv(left, ru))
numsep(t, 'Dərs saat 8:30-da başladı və 45 dəqiqə davam etdi. Dərs saat neçədə bitdi? Saatı və dəqiqəni yazın.', [9, 15], vstack([digital('08:30'), hstack([box(), txt(':', 70, INK), box()], 6)], 14), ':', disp='09:15')
t.num('Film saat 19:00-da başladı və 20:40-da bitdi. Film neçə dəqiqə çəkdi?', [100], vstack([hstack([digital('19:00', 56), arrow(), digital('20:40', 56)], 12), hstack([box(), txt('dəq', 46, GREY)], 10)], 12))
t.choice('Ən uzun vaxtı dairəyə alın.', ['2 saat', '100 dəqiqə', '1 saat 50 dəqiqə'], 0)
t.num('2 həftə neçə gündür?', [14], hstack([em('📅', 100), txt('7 · 2 =', 60), box()], 12))

# ============================================================ 187
t = T(187, 'Sürət',
      'Sürət vahid zamanda qət olunan yoldur. Yolu tapmaq üçün sürəti zamana vururuq: 60 km/saat · 3 saat = 180 km. Sürəti tapmaq üçün yolu zamana, zamanı tapmaq üçün isə yolu sürətə bölürük.',
      vstack([em('🚗', 90), txt('60 km/saat · 3 saat = 180 km', 46, BLUE)], 10))
t.num('Avtomobilin sürəti 60 km/saatdır. 3 saatda neçə kilometr yol gedər?', [180], vstack([em('🚗', 90), hstack([txt('60 · 3 =', 60), box(), txt('km', 46, GREY)], 10)], 12))
t.num('Avtobusun sürəti 80 km/saatdır. 2 saatda neçə kilometr yol gedər?', [160], vstack([em('🚌', 90), hstack([txt('80 · 2 =', 60), box(), txt('km', 46, GREY)], 10)], 12))
t.num('Maşın 4 saatda 240 km yol getdi. Onun sürəti neçə km/saatdır?', [60], vstack([em('🚙', 90), hstack([txt('240 : 4 =', 60), box(), txt('km/saat', 40, GREY)], 10)], 12))
t.num('Qatarın sürəti 100 km/saatdır. O, 300 km yolu neçə saata gedər?', [3], vstack([em('🚆', 90), hstack([txt('300 : 100 =', 60), box(), txt('saat', 40, GREY)], 10)], 12))
t.num('Velosipedçi saatda 15 km gedir. 4 saatda neçə kilometr gedər?', [60], vstack([em('🚴', 90), expr2(['15', '·', '4', '=', BOX], 60)], 12))
t.num('Piyada 3 saatda 12 km getdi. Onun sürəti neçə km/saatdır?', [4], vstack([em('🚶', 90), expr2(['12', ':', '3', '=', BOX], 60)], 12))
t.num('Qatar 450 km yolu 90 km/saat sürətlə neçə saata gedər?', [5], vstack([em('🚄', 90), expr2(['450', ':', '90', '=', BOX], 60)], 12))
t.choice('Hansı daha sürətli gedir? Dairəyə alın.', ['Saatda 70 km', '2 saatda 120 km', '3 saatda 180 km'], 0)
t.num('Avtomobil 2 saatda 140 km getdi. Eyni sürətlə 5 saatda neçə kilometr gedər?', [350], vstack([expr2(['140', ':', '2', '=', '70'], 54), expr2(['70', '·', '5', '=', BOX], 54)], 10))
t.num('İki şəhər arasındakı məsafə 360 km-dir. Avtobus saatda 60 km gedir. Neçə saata çatar?', [6], vstack([em('🏙️', 90), expr2(['360', ':', '60', '=', BOX], 60)], 12))

# ============================================================ 188
TIX = [('Parter', 10), ('Amfiteatr', 8), ('Loja', 5)]
DR = [['', 'Çay', 'Kofe'], ['Şəkərli', 12, 7], ['Şəkərsiz', 8, 5]]
t = T(188, 'Cədvəl. Piktoqram',
      'Məlumatları cədvəl və piktoqramla təsvir edirik. Piktoqramda bir şəkil bir neçə vahidi göstərə bilər. Məsələn, bir bilet şəkli 8 bilet deməkdir.',
      picto(TIX))
for name, k in TIX:
    t.num('Piktoqrama baxın. %s yerlərinə neçə bilet satılıb?' % name, [k * 8], vstack([picto(TIX), hstack([txt('%d · 8 =' % k, 56), box()], 10)], 12))
t.num('Cəmi neçə bilet satılıb?', [184], vstack([picto(TIX), expr2(['80', '+', '64', '+', '40', '=', BOX], 54)], 12))
t.num('Zal 250 tamaşaçı tutur. 184 bilet satılıb. Neçə bilet satılmayıb?', [66], expr2(['250', '−', '184', '=', BOX], 60))
t.choice('Hansı yerlərə ən az bilet satılıb? Dairəyə alın.', ['Loja', 'Parter', 'Amfiteatr'], 0, stem=picto(TIX))
t.num('Cədvələ baxın. Cəmi neçə çay sifariş olunub?', [20], vstack([tab(DR, 32), expr2(['12', '+', '8', '=', BOX], 56)], 12))
t.num('Cəmi neçə kofe sifariş olunub?', [12], vstack([tab(DR, 32), expr2(['7', '+', '5', '=', BOX], 56)], 12))
t.num('Şəkərli içkilər şəkərsiz içkilərdən neçə çoxdur?', [6], vstack([tab(DR, 32), expr2(['19', '−', '13', '=', BOX], 56)], 12))
t.choice('Hansı içki ən çox sifariş olunub? Dairəyə alın.', ['Şəkərli çay', 'Şəkərsiz kofe', 'Şəkərli kofe'], 0, stem=tab(DR, 32))

# ============================================================ 189
C1, C2, C3, C4 = (66, 165, 245), (255, 167, 38), (102, 187, 106), (239, 83, 80)
SPORT = pie([(0.5, C1, ''), (0.25, C2, ''), (0.25, C3, '')], 240)
SPORT_L = legend([(C1, 'Futbol – 1/2'), (C2, 'Basketbol – 1/4'), (C3, 'Üzgüçülük – 1/4')], 30)
t = T(189, 'Dairəvi diaqram',
      'Dairəvi diaqramda bütöv dairə bütün məlumatı, sektorlar isə onun hissələrini göstərir. Məsələn, sinifdə 24 şagird var və dairənin yarısı futbolu göstərir. 24-ün yarısı 12-dir, deməli, 12 şagird futbolu seçib.',
      hstack([SPORT, SPORT_L], 20))
t.num('Sinifdə 24 şagird var. Diaqrama görə neçə şagird futbolu seçib?', [12], vstack([hstack([SPORT, SPORT_L], 16), expr2(['24', ':', '2', '=', BOX], 56)], 12))
t.num('Neçə şagird basketbolu seçib?', [6], vstack([hstack([SPORT, SPORT_L], 16), expr2(['24', ':', '4', '=', BOX], 56)], 12))
t.num('Neçə şagird üzgüçülüyü seçib?', [6], vstack([hstack([SPORT, SPORT_L], 16), expr2(['24', '−', '12', '−', '6', '=', BOX], 52)], 12))
t.choice('Hansı idman növünü ən çox şagird seçib? Dairəyə alın.', ['Futbol', 'Basketbol', 'Üzgüçülük'], 0, stem=hstack([SPORT, SPORT_L], 16))
TREES = pie([(1 / 3, C4, ''), (1 / 3, C3, ''), (1 / 3, C2, '')], 220)
t.num('Bağda 30 ağac var. Onların üçdə biri alma ağacıdır. Neçə alma ağacı var?', [10], vstack([hstack([TREES, legend([(C4, 'Alma'), (C3, 'Armud'), (C2, 'Gilas')], 30)], 16), expr2(['30', ':', '3', '=', BOX], 56)], 12))
t.num('Rəfdə 40 kitab var. Onların dörddə biri nağıl kitabıdır. Neçə nağıl kitabı var?', [10], vstack([em('📚', 90), expr2(['40', ':', '4', '=', BOX], 60)], 12))
ABCD = pie([(0.5, C1, 'A'), (0.25, C2, 'B'), (0.125, C3, 'C'), (0.125, C4, 'D')], 240)
t.choice('Diaqramda hansı hissə dairənin dörddə biridir? Dairəyə alın.', ['A', 'B', 'C'], 1, stem=ABCD)
t.num('Ailənin gəliri 800 manatdır. Diaqrama görə gəlirin yarısı ərzağa xərclənir. Ərzağa neçə manat xərclənir?', [400], vstack([pie([(0.5, C3, 'Ərzaq'), (0.25, C2, ''), (0.25, C1, '')], 220), expr2(['800', ':', '2', '=', BOX], 56)], 12))
t.num('Gəlirin dörddə biri kommunal xərclərə gedir. Bu neçə manatdır?', [200], expr2(['800', ':', '4', '=', BOX], 64))
t.choice('Dairənin yarısı neçə dörddə birə bərabərdir? Dairəyə alın.', ['2', '4', '1'], 0, stem=hstack([frac_circle(2, 1, 150), txt('=', 60, BLUE), frac_circle(4, 2, 150)], 14))

# ============================================================ 190
MON = ['Yan', 'Fev', 'Mar', 'Apr', 'May']
TEMP = [5, 10, 15, 20, 25]
INC = [100, 110, 120, 110, 130]
TCH = line_chart(MON, TEMP, 30, 5, 560, 300, RED)
ICH = line_chart(MON, INC, 140, 10, 560, 340, BLUE)
t = T(190, 'Xətti diaqram',
      'Xətti diaqram kəmiyyətin zamanla necə dəyişdiyini göstərir. Nöqtələri birləşdirən xətt yuxarı qalxırsa, kəmiyyət artır, aşağı enirsə, azalır.',
      TCH)
t.num('Diaqrama baxın. Martda havanın temperaturu neçə dərəcə olub?', [15], vstack([TCH, hstack([box(), txt('°', 60, GREY)], 8)], 10))
t.num('Mayda havanın temperaturu neçə dərəcə olub?', [25], vstack([TCH, hstack([box(), txt('°', 60, GREY)], 8)], 10))
t.num('Fevraldan marta temperatur neçə dərəcə artıb?', [5], vstack([TCH, expr2(['15', '−', '10', '=', BOX], 54)], 10))
t.choice('Hansı ayda hava ən isti olub? Dairəyə alın.', ['May', 'Yanvar', 'Mart'], 0, stem=TCH)
t.num('Yanvarla may arasında temperatur fərqi neçə dərəcədir?', [20], vstack([TCH, expr2(['25', '−', '5', '=', BOX], 54)], 10))
t.num('Diaqramda şirkətin gəliri min manatla verilib. Fevralda gəlir neçə min manat olub?', [110], vstack([ICH, hstack([box(), txt('min manat', 40, GREY)], 8)], 10))
t.num('Aprelda gəlir marta görə neçə min manat azalıb?', [10], vstack([ICH, expr2(['120', '−', '110', '=', BOX], 54)], 10))
t.choice('Hansı ayda gəlir əvvəlki aya görə azalıb? Dairəyə alın.', ['Aprel', 'Mart', 'May'], 0, stem=ICH)
t.num('Ən böyük və ən kiçik gəlir arasındakı fərq neçə min manatdır?', [30], vstack([ICH, expr2(['130', '−', '100', '=', BOX], 54)], 10))
t.choice('Diaqramda xətt yuxarı qalxırsa, bu nə deməkdir? Dairəyə alın.', ['Artım', 'Azalma', 'Dəyişmir'], 0)

save()
