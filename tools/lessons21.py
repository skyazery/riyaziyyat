"""2-1 kitabının qısa video dərsləri (mövzu 50–69). Run: python3 tools/lessons21.py"""
from lessons import *

B = '2-1'
E = em


def tens_ones(a, x, y, cell=22, lab=True, color=RED):
    t, o = divmod(a, 10)
    out = blocks(t, o, x, y, cell, 8)
    if lab:
        out.append((T(str(a), 64, color), x + (t * (cell + 8)) / 2 + 20, y + 5 * cell + 50))
    return out


def col(a, b, op, res=None, y=170, size=80, color=INK):
    """sütunla toplama/çıxma: [(şəkil, x, y)]"""
    out = []
    x1 = 470
    for k, v in enumerate((a, b)):
        out.append((T(str(v), size, color), x1, y + k * 95))
    out.append((T(op, size, BLUE), x1 - 120, y + 50))
    im = Image.new('RGBA', (220, 10), (0, 0, 0, 0))
    ImageDraw.Draw(im).rectangle([0, 2, 219, 8], fill=INK + (255,))
    out.append((im, x1 - 30, y + 150))
    if res is not None:
        out.append((T(str(res), size, GREEN), x1, y + 210))
    return out


def colres(res, y=170, size=80):
    return [(T(str(res), size, GREEN), 470, y + 210)]


# 50 Müqayisə
L = Lesson(B, 50)
L.scene('47 və 52 ədədlərini müqayisə edək.', [(L.layer(tens_ones(47, 130, 230)), 0.1, 'pop'), (L.layer(tens_ones(52, 470, 230)), 0.45, 'pop')])
L.scene('Əvvəlcə onluqlara baxırıq: 4 onluq 5 onluqdan azdır.', [(L.layer([(ring(140, 300, ORANGE), 190, 230), (ring(180, 300, ORANGE), 545, 230)]), 0.4, 'pop')], keep=True)
L.scene('Deməli, 47 kiçikdir 52-dən.', [(L.layer(eq_items(['47', '<', '52'], 515, 64)), 0.3, 'pop')], keep=True)
fin(L); L.save()

# 51 Sıralama
L = Lesson(B, 51)
L.scene('Ədədlər: 35, 48, 23.', [(L.layer(numcards([35, 48, 23], 130, dx=200)), 0.2, 'pop')])
L.scene('Artan sıra – kiçikdən böyüyə: 23, 35, 48.', seq([L.layer([c]) for c in numcards([23, 35, 48], 300, dx=200, color=GREEN)], 0.35, 0.9), keep=True)
L.scene('Azalan sıra – böyükdən kiçiyə: 48, 35, 23.', seq([L.layer([c]) for c in numcards([48, 35, 23], 470, dx=200, color=ORANGE)], 0.35, 0.9), keep=True)
fin(L); L.save()

# 52 32 + 4
L = Lesson(B, 52)
L.scene('32 üstəgəl 4 neçə edir?', [(L.layer(eq_items(['32', '+', '4', '=', '?'], 80, 80)), 0.05, 'pop'), (L.layer(blocks(3, 2, 200, 300, 24, 8)), 0.45, 'pop')])
L.scene('Təkliyi təkliyə əlavə edirik: 2 üstəgəl 4 bərabərdir 6.', [(L.layer([(unit(24, GREEN), 480 + (i % 2) * 32, 300 - 4 * 24 + (i // 2) * 32) for i in range(4)]), 0.15, 'fly'), (L.layer([(T('2 + 4 = 6', 48, ORANGE), 600, 470)]), 0.6, 'pop')], keep=True)
L.scene('Onluqlar dəyişmir: 32 üstəgəl 4 bərabərdir 36.', [(L.layer(eq_items(['32', '+', '4', '=', '36'], 515, 64)), 0.4, 'pop')], keep=True)
fin(L); L.save()

# 53 Onluqların toplanması
L = Lesson(B, 53)
L.scene('3 onluq üstəgəl 2 onluq.', [(L.layer(blocks(3, 0, 180, 250, 26)), 0.05, 'pop'), (L.layer(blocks(2, 0, 480, 250, 26, 12)), 0.5, 'pop')])
L.scene('Bərabərdir 5 onluq.', [(L.layer([(T('5 onluq', 60, BLUE), 400, 450)]), 0.3, 'pop')], keep=True)
L.scene('Yəni 30 üstəgəl 20 bərabərdir 50.', [(L.layer(eq_items(['30', '+', '20', '=', '50'], 515, 64)), 0.2, 'pop')], keep=True)
fin(L); L.save()

# 54 46 + 21
L = Lesson(B, 54)
L.scene('46 üstəgəl 21-i sütunla toplayaq.', [(L.layer(col(46, 21, '+')), 0.3, 'pop')])
L.scene('Təklikləri toplayırıq: 6 üstəgəl 1 bərabərdir 7.', [(L.layer([(ring(62, 300, ORANGE), 500, 220)]), 0.1, 'pop'), (L.layer([(T('7', 80, GREEN), 497, 380)]), 0.65, 'pop')], keep=True)
L.scene('Onluqları toplayırıq: 4 üstəgəl 2 bərabərdir 6. Cavab 67.', [(L.layer([(ring(62, 300, BLUE), 440, 220)]), 0.1, 'pop'), (L.layer([(T('6', 80, GREEN), 443, 380)]), 0.5, 'pop')], keep=True)
fin(L); L.save()

# 55 46 − 3
L = Lesson(B, 55)
L.scene('46 çıx 3 neçə edir?', [(L.layer(eq_items(['46', '−', '3', '=', '?'], 80, 80)), 0.05, 'pop'), (L.layer(blocks(4, 6, 200, 300, 24, 8)), 0.45, 'pop')])
L.scene('Təklikdən təklik çıxırıq: 6 çıx 3 bərabərdir 3.', [(L.layer([(T('✕', 40, RED), 352 + (i % 2) * 32, 300 - 4 * 24 + (i // 2) * 32) for i in range(3, 6)]), 0.3, 'pop'), (L.layer([(T('6 – 3 = 3', 48, ORANGE), 600, 300)]), 0.6, 'pop')], keep=True)
L.scene('Onluqlar dəyişmir: 46 çıx 3 bərabərdir 43.', [(L.layer(eq_items(['46', '−', '3', '=', '43'], 515, 64)), 0.4, 'pop')], keep=True)
fin(L); L.save()

# 56 Onluqların çıxılması
L = Lesson(B, 56)
L.scene('7 onluq var.', [(L.layer(blocks(7, 0, 200, 250, 26)), 0.1, 'pop')])
L.scene('3 onluğu götürürük. 4 onluq qaldı.', [(L.layer([(T('✕', 44, RED), 200 + i * 38, 250) for i in range(4, 7)]), 0.15, 'pop'), (L.layer([(T('4 onluq', 56, BLUE), 400, 450)]), 0.6, 'pop')], keep=True)
L.scene('Yəni 70 çıx 30 bərabərdir 40.', [(L.layer(eq_items(['70', '−', '30', '=', '40'], 515, 64)), 0.2, 'pop')], keep=True)
fin(L); L.save()

# 57 68 − 25
L = Lesson(B, 57)
L.scene('68 çıx 25-i sütunla hesablayaq.', [(L.layer(col(68, 25, '−')), 0.3, 'pop')])
L.scene('Təklikdən təklik çıxırıq: 8 çıx 5 bərabərdir 3.', [(L.layer([(ring(62, 300, ORANGE), 500, 220)]), 0.1, 'pop'), (L.layer([(T('3', 80, GREEN), 497, 380)]), 0.65, 'pop')], keep=True)
L.scene('Onluqdan onluq çıxırıq: 6 çıx 2 bərabərdir 4. Cavab 43.', [(L.layer([(ring(62, 300, BLUE), 440, 220)]), 0.1, 'pop'), (L.layer([(T('4', 80, GREEN), 443, 380)]), 0.5, 'pop')], keep=True)
fin(L); L.save()

# 58 Təkrar toplama
L = Lesson(B, 58)
px = [130, 310, 490, 670]
L.scene('4 boşqab var. Hər boşqabda 3 alma.', seq([L.layer([(plate(3), x, 170)]) for x in px], 0.1, 0.6))
L.scene('Bərabər qrupları toplayırıq.', seq([L.layer([(T('3', 56, BLUE), x, 280)]) for x in px], 0.2, 0.8), keep=True)
L.scene('3 üstəgəl 3 üstəgəl 3 üstəgəl 3 bərabərdir 12.', [(L.layer(eq_items(['3', '+', '3', '+', '3', '+', '3', '=', '12'], 430, 72, 18)), 0.1, 'fade')], keep=True)
fin(L); L.save()

# 59 Vurma
L = Lesson(B, 59)
pl = [L.layer([(plate(3), x, 170)]) for x in px]
L.scene('Hər boşqabda 3 alma var.', [(pl[0], 0.1, 'pop'), (L.layer([(txt('3', 56, BLUE), px[0], 280)]), 0.6, 'pop')])
lab = [L.layer([(txt('3', 56, BLUE), x, 280)]) for x in px[1:]]
L.scene('Belə 4 boşqab var.', [(pl[1], 0.15, 'pop'), (lab[0], 0.15, 'pop'), (pl[2], 0.35, 'pop'), (lab[1], 0.35, 'pop'), (pl[3], 0.55, 'pop'), (lab[2], 0.55, 'pop')], keep=True)
eq = eq_items(['3', '+', '3', '+', '3', '+', '3', '=', '12'], 400, 72, 18)
L.scene('Toplayaq: 3 üstəgəl 3 üstəgəl 3 üstəgəl 3 bərabərdir 12.', [(L.layer(eq[:7]), 0.1, 'fade'), (L.layer(eq[7:]), 0.78, 'pop')], keep=True)
m = eq_items(['3', '·', '4', '=', '12'], 520, 92)
L.scene('Qısa yazırıq: 3 vur 4 bərabərdir 12. Hər qrupda 3, cəmi 4 qrup.', [(L.layer(m[:3]), 0.08, 'pop'), (L.layer(m[3:]), 0.38, 'pop')], keep=True)
fin(L); L.save()

# 60 Bölmə
L = Lesson(B, 60)
kids = [180, 400, 620]
L.scene('12 konfeti 3 uşağa bərabər paylayırıq.', [(L.layer([(E('🍬', 56), x, y) for x, y in grid(12, 6, 90, 70, 60)]), 0.05, 'pop'), (L.layer([(E(e, 100), x, 290) for e, x in zip(['👦', '👧', '🧒'], kids)]), 0.5, 'pop')])
L.scene('Hər uşağa bir-bir veririk.', [(L.layer([(E(e, 100), x, 290) for e, x in zip(['👦', '👧', '🧒'], kids)]), 0.0, 'fade')] + seq([L.layer([(E('🍬', 50), x - 45 + (r % 2) * 90, 400 + (r // 2) * 60) for x in kids]) for r in range(4)], 0.2, 0.85, 'fly'))
L.scene('Hər uşağa 4 konfet düşdü: 12 böl 3 bərabərdir 4.', [(L.layer(eq_items(['12', ':', '3', '=', '4'], 90, 80)), 0.3, 'pop')], keep=True)
fin(L); L.save()

# 61 Təkrar çıxma
L = Lesson(B, 61)
nl, X = nline(0, 8)
L.scene('8-dən hər dəfə 2 çıxırıq.', [(L.layer([(nl, 400, 300)]), 0.05, 'fade'), (L.layer([(dot(BLUE, 16), X(8), 330)]), 0.5, 'pop')])
L.scene('8, 6, 4, 2, 0. Dörd dəfə çıxdıq.', seq([L.layer([(hop(X, v, v - 2, color=PURPLE, label=str(k + 1)), 400, 300)]) for k, v in enumerate((8, 6, 4, 2))], 0.1, 0.75, 'fade'), keep=True)
L.scene('Deməli, 8 böl 2 bərabərdir 4.', [(L.layer(eq_items(['8', ':', '2', '=', '4'], 500, 90)), 0.3, 'pop')], keep=True)
fin(L); L.save()

# 62 Tək və cüt
L = Lesson(B, 62)


def pairs(n, x, y, c=BLUE):
    return [(dot(c, 22), x + (i // 2) * 60, y + (i % 2) * 55) for i in range(n)]


L.scene('6 topu cüt-cüt düzək. Hamısının cütü var. 6 – cüt ədəddir.', [(L.layer(pairs(6, 120, 140)), 0.1, 'pop'), (L.layer([(T('6 – cüt', 54, BLUE), 560, 165)]), 0.7, 'pop')])
L.scene('7 topu düzək. Biri cütsüz qaldı. 7 – tək ədəddir.', [(L.layer(pairs(7, 120, 330, RED)), 0.1, 'pop'), (L.layer([(ring(70, 70, ORANGE), 300, 330)]), 0.45, 'pop'), (L.layer([(T('7 – tək', 54, RED), 560, 355)]), 0.75, 'pop')], keep=True)
L.scene('Cüt ədədlər: 2, 4, 6, 8. Tək ədədlər: 1, 3, 5, 7.', [(L.layer([(T('2  4  6  8', 44, BLUE), 220, 520), (T('1  3  5  7', 44, RED), 580, 520)]), 0.2, 'pop')], keep=True)
fin(L); L.save()

# 63 Xətt, bucaq


def lines(kind):
    im, d = canvas()
    c = INK + (255,)
    if kind == 'xett':
        d.line([(80, 150), (330, 150)], fill=c, width=7)
        pts = [(470 + i * 8, 150 + 40 * math.sin(i / 5)) for i in range(32)]
        d.line(pts, fill=c, width=7, joint='curve')
    else:
        for x0, ang, col_ in [(110, 90, GREEN), (360, 45, BLUE), (615, 125, RED)]:
            y0 = 470
            a = math.radians(ang)
            d.line([(x0, y0), (x0 + 160, y0)], fill=col_ + (255,), width=7)
            d.line([(x0, y0), (x0 + 150 * math.cos(a), y0 - 150 * math.sin(a))], fill=col_ + (255,), width=7)
            d.ellipse([x0 - 9, y0 - 9, x0 + 9, y0 + 9], fill=INK + (255,))
    return im


L = Lesson(B, 63)
L.scene('Xətlər düz və əyri olur.', [(L.layer([(lines('xett'), 400, 300)]), 0.1, 'fade'), (L.layer([(T('düz', 40, INK), 205, 220), (T('əyri', 40, INK), 590, 220)]), 0.55, 'pop')])
L.scene('İki düz xətt bir nöqtədən çıxanda bucaq əmələ gəlir.', [(L.layer([(lines('bucaq'), 400, 300)]), 0.3, 'fade')], keep=True)
L.scene('Bucaqlar: düz, iti, kor.', seq([L.layer([(T(s, 40, c), x, 540)]) for s, c, x in [('düz', GREEN, 180), ('iti', BLUE, 430), ('kor', RED, 640)]], 0.3, 0.85), keep=True)
fin(L); L.save()

# 64 Çoxbucaqlı


def poly(n, r=90, color=BLUE):
    im = Image.new('RGBA', (2 * r + 10, 2 * r + 10), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    pts = [(r + 5 + r * math.cos(math.radians(-90 + 360 * k / n)), r + 5 + r * math.sin(math.radians(-90 + 360 * k / n))) for k in range(n)]
    d.polygon(pts, fill=tuple(int(v * 0.35 + 255 * 0.65) for v in color) + (255,), outline=color + (255,), width=6)
    return im


L = Lesson(B, 64)
ns = [(3, 'üçbucaq', BLUE), (4, 'dördbucaqlı', GREEN), (5, 'beşbucaqlı', ORANGE), (6, 'altıbucaqlı', PURPLE)]
xs = [110, 300, 500, 690]
L.scene('Üçbucaq, dördbucaqlı, beşbucaqlı, altıbucaqlı.', seq([L.layer([(poly(n, 80, c), x, 200), (T(s, 26, c), x, 310)]) for (n, s, c), x in zip(ns, xs)], 0.1, 0.85))
L.scene('Neçə bucağı varsa, o qədər də tərəfi var.', seq([L.layer([(T(str(n), 64, RED), x, 420)]) for (n, s, c), x in zip(ns, xs)], 0.35, 0.9), keep=True)
fin(L); L.save()

# 65 Üz, til, təpə


def cube(hl):
    im, d = canvas()
    s, o = 220, 90
    F = [(250, 220), (250 + s, 220), (250 + s, 220 + s), (250, 220 + s)]
    Bk = [(x + o, y - o) for x, y in F]
    if 'uz' in hl:
        d.polygon(F, fill=(180, 210, 250, 255))
    for P in (F, Bk):
        d.polygon(P, outline=(BLUE if 'til' in hl else INK) + (255,), width=6)
    for a, b in zip(F, Bk):
        d.line([a, b], fill=(BLUE if 'til' in hl else INK) + (255,), width=6)
    if 'tepe' in hl:
        for x, y in F + Bk:
            d.ellipse([x - 13, y - 13, x + 13, y + 13], fill=RED + (255,))
    return im


L = Lesson(B, 65)
L.scene('Kubun 6 üzü var. Üzlər kvadratdır.', [(L.layer([(cube({'uz'}), 400, 300)]), 0.1, 'fade'), (L.layer([(label('6 üz', 50, BLUE), 140, 120)]), 0.5, 'pop')])
L.scene('12 tili var. Tillər – xətlərdir.', [(L.layer([(cube({'uz', 'til'}), 400, 300)]), 0.1, 'fade'), (L.layer([(label('12 til', 50, BLUE), 140, 220)]), 0.5, 'pop')], keep=True)
L.scene('8 təpəsi var. Təpələr – qırmızı nöqtələr.', [(L.layer([(cube({'uz', 'til', 'tepe'}), 400, 300)]), 0.1, 'fade'), (L.layer([(label('8 təpə', 50, RED), 140, 320)]), 0.5, 'pop')], keep=True)
fin(L); L.save()

# 66 Qruplaşdırma
L = Lesson(B, 66)
items = [('circle', RED), ('square', BLUE), ('tri', RED), ('circle', BLUE), ('square', RED), ('tri', BLUE)]
L.scene('Fiqurlar qarışıqdır.', [(L.layer([(shape(k, 90, c), x, 150) for (k, c), (x, _) in zip(items, row(6, 0, dx=115))]), 0.2, 'pop')])
L.scene('Rənginə görə qruplaşdıraq: qırmızılar bir yerə, göylər bir yerə.', [(L.layer([(shape(k, 80, c), 110 + i * 95, 340) for i, (k, c) in enumerate([x for x in items if x[1] == RED])]), 0.35, 'fly'), (L.layer([(shape(k, 80, c), 500 + i * 95, 340) for i, (k, c) in enumerate([x for x in items if x[1] == BLUE])]), 0.65, 'fly')], keep=True)
L.scene('Formasına və ölçüsünə görə də qruplaşdıra bilərik.', [(L.layer([(ring(330, 140, RED), 205, 340), (ring(330, 140, BLUE), 595, 340)]), 0.15, 'pop'), (L.layer([(T('rəng · forma · ölçü', 44, PURPLE), 400, 500)]), 0.5, 'pop')], keep=True)
fin(L); L.save()

# 67 47 + 5
L = Lesson(B, 67)
nl, X = nline(45, 55)
L.scene('47 üstəgəl 5 neçə edir?', [(L.layer(eq_items(['47', '+', '5', '=', '?'], 100, 80)), 0.1, 'pop'), (L.layer([(nl, 400, 300)]), 0.3, 'fade'), (L.layer([(dot(BLUE, 16), X(47), 330)]), 0.6, 'pop')])
L.scene('Əvvəlcə 3 əlavə edib 50-yə çatırıq.', [(L.layer([(hop(X, 47, 50, label='+3'), 400, 300)]), 0.3, 'fade'), (L.layer([(dot(GREEN, 16), X(50), 330)]), 0.7, 'pop')], keep=True)
L.scene('Sonra qalan 2-ni: 52. 47 üstəgəl 5 bərabərdir 52.', [(L.layer([(hop(X, 50, 52, color=PURPLE, label='+2'), 400, 300)]), 0.1, 'fade'), (L.layer([(dot(RED, 16), X(52), 330)]), 0.3, 'pop'), (L.layer(eq_items(['47', '+', '5', '=', '52'], 500, 90)), 0.55, 'pop')], keep=True)
fin(L); L.save()

# 68 29 + 53
L = Lesson(B, 68)
L.scene('29 üstəgəl 53-ü sütunla toplayaq.', [(L.layer(col(29, 53, '+')), 0.3, 'pop')])
L.scene('Təkliklər: 9 üstəgəl 3 bərabərdir 12. 2-ni yazırıq, 1 onluğu yuxarı qoyuruq.', [(L.layer([(ring(62, 300, ORANGE), 500, 220)]), 0.05, 'pop'), (L.layer([(T('2', 80, GREEN), 497, 380)]), 0.45, 'pop'), (L.layer([(T('1', 44, RED), 443, 100)]), 0.75, 'fly')], keep=True)
L.scene('Onluqlar: 2 üstəgəl 5 üstəgəl 1 bərabərdir 8. Cavab 82.', [(L.layer([(ring(62, 360, BLUE), 440, 190)]), 0.1, 'pop'), (L.layer([(T('8', 80, GREEN), 443, 380)]), 0.6, 'pop')], keep=True)
fin(L); L.save()

# 69 26 + 15 + 4
L = Lesson(B, 69)
L.scene('26 üstəgəl 15 üstəgəl 4.', [(L.layer(eq_items(['26', '+', '15', '+', '4'], 120, 84)), 0.1, 'pop')])
L.scene('Tam onluq düzəldən ədədləri tapırıq: 26 üstəgəl 4 bərabərdir 30.', [(L.layer([(ring(130, 120, GREEN), 170, 120), (ring(110, 120, GREEN), 655, 120)]), 0.2, 'pop'), (L.layer(eq_items(['26', '+', '4', '=', '30'], 300, 72)), 0.55, 'pop')], keep=True)
L.scene('Sonra 30 üstəgəl 15 bərabərdir 45.', [(L.layer(eq_items(['30', '+', '15', '=', '45'], 450, 72)), 0.2, 'pop')], keep=True)
fin(L); L.save()
