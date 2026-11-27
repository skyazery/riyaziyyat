"""1-1 kitabının qısa video dərsləri (mövzu 1–28). Run: python3 tools/lessons11.py"""
from lessons import *

B = '1-1'
E = lambda ch, s=100: em(ch, s)


def numcards(vals, y, dx=150, size=80, color=INK):
    xs = [x for x, _ in row(len(vals), y, dx=dx)]
    return [(card(str(v), size, color), x, y) for v, x in zip(vals, xs)]


def card(s, size=80, color=INK):
    t = txt(s, size, color)
    im = Image.new('RGBA', (t.width + 50, t.height + 40), (0, 0, 0, 0))
    ImageDraw.Draw(im).rounded_rectangle([2, 2, im.width - 3, im.height - 3], 18, fill=(255, 255, 255, 255), outline=GREY + (255,), width=4)
    im.alpha_composite(t, (25, 20))
    return im


def pairlines(top, bot, n, color=GREEN):
    im, d = canvas()
    for i in range(n):
        d.line([top[i], bot[i]], fill=color + (255,), width=6)
    return im


# 1 Əşyanın yeri
L = Lesson(B, 1)
bx = E('📦', 160)
L.scene('Top qutunun üstündədir.', [(L.layer([(bx, 400, 400)]), 0.0, 'fade'), (L.layer([(E('⚽', 110), 400, 250)]), 0.3, 'fly')])
L.scene('İndi top qutunun altındadır.', [(L.layer([(bx, 400, 230), (E('⚽', 110), 400, 420)]), 0.2, 'fade')])
L.scene('Pişik qutunun solunda, it isə sağındadır.', [(L.layer([(bx, 400, 320)]), 0.0, 'fade'), (L.layer([(E('🐱', 120), 180, 330)]), 0.2, 'fly'), (L.layer([(E('🐶', 120), 620, 330)]), 0.6, 'fly')])
L.scene('Alma səbətin içindədir.', [(L.layer([(E('🧺', 220), 400, 340)]), 0.0, 'fade'), (L.layer([(E('🍎', 90), 400, 290)]), 0.4, 'pop')])
fin(L); L.save()

# 2 Əşyanın əlaməti
L = Lesson(B, 2)
cols = [(RED, 200), ((250, 200, 30), 400), (BLUE, 600)]
L.scene('Əşyaların rəngi var: qırmızı, sarı, göy.', seq([L.layer([(shape('circle', 130, c), x, 150)]) for c, x in cols], 0.3, 0.8))
L.scene('Forması var: dairə, üçbucaq, kvadrat.', seq([L.layer([(shape(k, 130, PURPLE), x, 330)]) for k, x in [('circle', 200), ('tri', 400), ('square', 600)]], 0.3, 0.8), keep=True)
L.scene('Ölçüsü var: böyük top və kiçik top.', [(L.layer([(E('⚽', 130), 300, 490)]), 0.35, 'pop'), (L.layer([(E('⚽', 60), 500, 510)]), 0.75, 'pop')], keep=True)
fin(L); L.save()

# 3 10-a qədər sayma
L = Lesson(B, 3)
pos = row(6, 200, dx=115)
L.scene('Gəlin ulduzları sayaq.', seq([L.layer([(E('⭐', 90), x, y)]) for x, y in pos], 0.2, 0.8))
L.scene('1, 2, 3, 4, 5, 6.', seq([L.layer([(T(str(i + 1), 64, BLUE), x, 310)]) for i, (x, _) in enumerate(pos)], 0.05, 0.85), keep=True)
L.scene('Son ədəd 6-dır. Deməli, 6 ulduz var.', [(L.layer([(T('6', 150, RED), 400, 470)]), 0.25, 'pop')], keep=True)
fin(L); L.save()

# 4 0, 1, 2
L = Lesson(B, 4)
xs = [170, 400, 630]
L.scene('Boşqabda heç nə yoxdur. Bu, 0-dır.', [(L.layer([(plate(0, 190), xs[0], 230)]), 0.05, 'pop'), (L.layer([(T('0', 110, RED), xs[0], 420)]), 0.7, 'pop')])
L.scene('Bir alma var. Bu, 1-dir.', [(L.layer([(plate(1, 190), xs[1], 230)]), 0.05, 'pop'), (L.layer([(T('1', 110, RED), xs[1], 420)]), 0.6, 'pop')], keep=True)
L.scene('İki alma var. Bu, 2-dir.', [(L.layer([(plate(2, 190), xs[2], 230)]), 0.05, 'pop'), (L.layer([(T('2', 110, RED), xs[2], 420)]), 0.6, 'pop')], keep=True)
fin(L); L.save()


def countrows(L, emoji, counts, size, dx, ys, say):
    for k, (n, y, s) in enumerate(zip(counts, ys, say)):
        lay = [L.layer([(E(emoji, size), x, y) for x, _ in row(n, y, x0=230, dx=dx)])]
        lay.append(L.layer([(T(str(n), 96, RED), 100, y)]))
        L.scene(s, [(lay[0], 0.05, 'fly'), (lay[1], 0.6, 'pop')], keep=k > 0)


# 5 3, 4, 5
L = Lesson(B, 5)
countrows(L, '🐦', [3, 4, 5], 90, 110, [130, 300, 470], ['Burada 3 quş var.', 'Burada 4 quş var.', 'Burada isə 5 quş var.'])
fin(L); L.save()

# 6 6, 7, 8
L = Lesson(B, 6)
countrows(L, '🐟', [6, 7, 8], 66, 72, [130, 300, 470], ['Burada 6 balıq var.', 'Burada 7 balıq var.', 'Burada isə 8 balıq var.'])
fin(L); L.save()

# 7 9 və 10
L = Lesson(B, 7)
F = frame10()
cp = lambda i: (400 - 2 * 84 + (i % 5) * 84, 260 - 42 + (i // 5) * 84)
L.scene('Qutuda 9 top var.', [(L.layer([(F, 400, 260)]), 0.0, 'fade'), (L.layer([(dot(RED), *cp(i)) for i in range(9)]), 0.25, 'pop'), (L.layer([(T('9', 110, RED), 400, 470)]), 0.6, 'pop')])
L.scene('Daha 1 top qoyduq: 10 oldu. Qutu doldu.', [(L.layer([(F, 400, 260)] + [(dot(RED), *cp(i)) for i in range(9)]), 0.0, 'fade'), (L.layer([(dot(BLUE), *cp(9))]), 0.1, 'fly'), (L.layer([(T('10', 110, GREEN), 400, 470)]), 0.45, 'pop')])
fin(L); L.save()

# 8 Sıra sayları
L = Lesson(B, 8)
an = ['🐶', '🐱', '🐰', '🐻']
xs = [270, 400, 530, 660]
L.scene('Bayraqdan başlayıb sayırıq.', [(L.layer([(E('🏁', 110), 120, 240)]), 0.05, 'pop'), (L.layer([(E(a, 100), x, 240) for a, x in zip(an, xs)]), 0.4, 'fly')])
L.scene('Birinci, ikinci, üçüncü, dördüncü.', seq([L.layer([(T(s, 40, BLUE), x, 340)]) for s, x in zip(['1-ci', '2-ci', '3-cü', '4-cü'], xs)], 0.05, 0.8), keep=True)
L.scene('Dovşan üçüncüdür.', [(L.layer([(ring(140, 260), xs[2], 280)]), 0.3, 'pop')], keep=True)
fin(L); L.save()

# 9 Azdır, çoxdur
L = Lesson(B, 9)
tp = row(5, 160, dx=130)
bp = row(3, 420, x0=tp[0][0], dx=130)
L.scene('5 dovşan və 3 kök var.', [(L.layer([(E('🐰', 100), x, y) for x, y in tp]), 0.1, 'pop'), (L.layer([(E('🥕', 90), x, y) for x, y in bp]), 0.5, 'pop')])
L.scene('Onları cüt-cüt birləşdirək.', seq([L.layer([(pairlines([(tp[i][0], tp[i][1] + 55)], [(bp[i][0], bp[i][1] - 55)], 1), 400, 300)]) for i in range(3)], 0.3, 0.8, 'fade'), keep=True)
L.scene('2 dovşana kök çatmadı. Dovşanlar çoxdur, köklər azdır.', [(L.layer([(ring(270, 140), (tp[3][0] + tp[4][0]) / 2, 160)]), 0.1, 'pop')], keep=True)
fin(L); L.save()

# 10 Ədədlərin müqayisəsi
L = Lesson(B, 10)
A = E('🍎', 80)
L.scene('Solda 5 alma, sağda 3 alma var.', [(L.layer([(A, x, y) for x, y in grid(5, 3, 180, 90, 90, x0=110)]), 0.1, 'pop'), (L.layer([(A, x, y) for x, y in grid(3, 2, 180, 90, 90, x0=560)]), 0.5, 'pop')])
eq = eq_items(['5', '>', '3'], 470, 110)
L.scene('5 ədədi 3-dən böyükdür.', [(L.layer([eq[0]]), 0.1, 'pop'), (L.layer([eq[1]]), 0.4, 'pop'), (L.layer([eq[2]]), 0.6, 'pop')], keep=True)
L.scene('Ağzı açıq tərəf böyük ədədə baxır.', [(L.layer([(ring(130, 160), eq[1][1], 470)]), 0.3, 'pop')], keep=True)
fin(L); L.save()

# 11 Ədəd oxu
L = Lesson(B, 11)
nl, X = nline(0, 10)
L.scene('Ədəd oxunda ədədlər sıra ilə düzülür.', [(L.layer([(nl, 400, 300)]), 0.1, 'fade')])
L.scene('Sağa getdikcə ədədlər böyüyür: 3, 4, 5, 6.', seq([L.layer([(dot(BLUE, 16), X(v), 330)]) for v in (3, 4, 5, 6)], 0.4, 0.9) + [(L.layer([(T('→', 90, ORANGE), 600, 200)]), 0.1, 'fly')], keep=True)
fin(L); L.save()

# 12 Sıralama
L = Lesson(B, 12)
L.scene('Kartlar qarışıqdır: 5, 2, 8, 4.', [(L.layer(numcards([5, 2, 8, 4], 130)), 0.1, 'pop')])
L.scene('Artma sırası: kiçikdən böyüyə – 2, 4, 5, 8.', seq([L.layer([c]) for c in numcards([2, 4, 5, 8], 300, color=GREEN)], 0.4, 0.95), keep=True)
L.scene('Azalma sırası: böyükdən kiçiyə – 8, 5, 4, 2.', seq([L.layer([c]) for c in numcards([8, 5, 4, 2], 470, color=ORANGE)], 0.4, 0.95), keep=True)
fin(L); L.save()

# 13 Ədəd üçlüyü
L = Lesson(B, 13)


def bond(top, l, r):
    im, d = canvas()
    d.line([(400, 170), (250, 380)], fill=GREY + (255,), width=6)
    d.line([(400, 170), (550, 380)], fill=GREY + (255,), width=6)
    for (x, y), v, c in [((400, 150), top, RED), ((250, 400), l, BLUE), ((550, 400), r, BLUE)]:
        d.ellipse([x - 70, y - 70, x + 70, y + 70], fill=(255, 255, 255, 255), outline=c + (255,), width=7)
        d.text((x, y), str(v), font=font(80), fill=c + (255,), anchor='mm')
    return im


L.scene('6 top var: 4 qırmızı və 2 göy.', [(L.layer([(dot(RED, 28), x, 300) for x, _ in row(4, 0, x0=170, dx=75)] + [(dot(BLUE, 28), x, 300) for x, _ in row(2, 0, x0=520, dx=75)]), 0.1, 'pop')])
L.scene('6 – tamdır. 4 və 2 – onun hissələridir.', [(L.layer([(bond(6, 4, 2), 400, 300)]), 0.1, 'fade')])
L.scene('Deməli, 6 ədədi 4 və 2-dən ibarətdir.', [(L.layer([(T('6 = 4 və 2', 56, INK), 400, 525)]), 0.3, 'pop')], keep=True)
fin(L); L.save()

# 14 Əlavə etmək, artırmaq
L = Lesson(B, 14)
fp = row(5, 260, dx=120)
L.scene('Akvariumda 3 balıq var idi.', seq([L.layer([(E('🐟', 100), x, y)]) for x, y in fp[:3]], 0.2, 0.7))
L.scene('2 balıq da gəldi.', seq([L.layer([(E('🐠', 100), x, y)]) for x, y in fp[3:]], 0.15, 0.5, 'fly'), keep=True)
L.scene('İndi 5 balıq oldu.', [(L.layer([(T('3 və 2 – 5', 80, BLUE), 400, 460)]), 0.3, 'pop')], keep=True)
fin(L); L.save()

# 15 Ədədlərin toplanması
L = Lesson(B, 15)
A = em('🍎', 104)
xs = [130, 250, 370, 540, 660]
ap = [L.layer([(A, x, 170)]) for x in xs]
L.scene('Burada 3 alma var.', [(ap[0], 0.1, 'pop'), (ap[1], 0.35, 'pop'), (ap[2], 0.6, 'pop')])
L.scene('Daha 2 alma gətirdik.', [(ap[3], 0.25, 'fly'), (ap[4], 0.5, 'fly')], keep=True)
nums = [L.layer([(txt(str(i + 1), 64, BLUE), x, 290)]) for i, x in enumerate(xs)]
L.scene('Sayaq: 1, 2, 3, 4, 5. Cəmi 5 alma oldu.', [(nums[i], 0.12 + i * 0.11, 'pop') for i in range(5)], keep=True)
eq = eq_items(['3', '+', '2', '=', '5'], 470)
L.scene('Belə yazırıq: 3 üstəgəl 2 bərabərdir 5.', [(L.layer([eq[i]]), 0.18 + i * 0.13, 'pop') for i in range(5)], keep=True)
fin(L); L.save()

# 16 Ədəd oxu üzərində toplama
L = Lesson(B, 16)
nl, X = nline(0, 10)
L.scene('3 üstəgəl 4-ü ədəd oxunda tapaq.', [(L.layer([(nl, 400, 300)]), 0.0, 'fade'), (L.layer([(dot(BLUE, 16), X(3), 330)]), 0.4, 'pop'), (L.layer(eq_items(['3', '+', '4', '=', '?'], 90, 80)), 0.1, 'pop')])
L.scene('3-dən başlayıb sağa 4 addım atırıq.', seq([L.layer([(hop(X, v, v + 1), 400, 300)]) for v in (3, 4, 5, 6)], 0.35, 0.9, 'fade'), keep=True)
L.scene('7-yə çatdıq: 3 üstəgəl 4 bərabərdir 7.', [(L.layer([(dot(RED, 16), X(7), 330)]), 0.05, 'pop'), (L.layer(eq_items(['3', '+', '4', '=', '7'], 500, 90)), 0.4, 'pop')], keep=True)
fin(L); L.save()

# 17 Üç toplananlı ifadələr
L = Lesson(B, 17)
st = E('⭐', 70)
g = [(2, 130), (3, 360), (1, 600)]
L.scene('2 ulduz, 3 ulduz və 1 ulduz var.', seq([L.layer([(st, x, 150) for x, _ in row(n, 0, x0=x0, dx=75)]) for n, x0 in g], 0.1, 0.75))
L.scene('Əvvəlcə 2 üstəgəl 3 bərabərdir 5.', [(L.layer(eq_items(['2', '+', '3', '=', '5'], 320, 80)), 0.2, 'pop')], keep=True)
L.scene('Sonra 5 üstəgəl 1 bərabərdir 6.', [(L.layer(eq_items(['5', '+', '1', '=', '6'], 450, 80)), 0.2, 'pop')], keep=True)
fin(L); L.save()

# 18 Toplamanın digər üsulları
L = Lesson(B, 18)
L.scene('İkiqat: 3 üstəgəl 3 bərabərdir 6.', [(L.layer([(dot(RED, 26), x, 120) for x, _ in row(3, 0, dx=70)]), 0.05, 'pop'), (L.layer([(dot(RED, 26), x, 190) for x, _ in row(3, 0, dx=70)]), 0.25, 'pop'), (L.layer(eq_items(['3', '+', '3', '=', '6'], 280, 72)), 0.5, 'pop')])
F = frame10(70)
cp = lambda i: (400 - 2 * 70 + (i % 5) * 70, 430 - 35 + (i // 5) * 70)
L.scene('10-a tamamlama: 7 üstəgəl 3 bərabərdir 10.', [(L.layer([(F, 400, 430)] + [(dot(RED, 24), *cp(i)) for i in range(7)]), 0.05, 'fade'), (L.layer([(dot(BLUE, 24), *cp(i)) for i in range(7, 10)]), 0.45, 'fly'), (L.layer([(T('10', 80, GREEN), 680, 430)]), 0.8, 'pop')], keep=True)
fin(L); L.save()

# 19 Azaltmaq, çıxmaq
L = Lesson(B, 19)
ap = [L.layer([(E('🍎', 100), x, 230)]) for x, _ in row(5, 0, dx=120)]
L.scene('5 alma var idi.', seq(ap, 0.1, 0.7))
L.scene('2 almanı yedik.', [(L.layer([(E('🍎', 100), x, 230) for x, _ in row(5, 0, dx=120)[3:]] + [(T('✕', 110, RED), x, 230) for x, _ in row(5, 0, dx=120)[3:]]), 0.2, 'pop')], keep=True)
L.scene('3 alma qaldı.', [(L.layer([(T('5 – 2 = 3', 90, BLUE), 400, 430)]), 0.2, 'pop')], keep=True)
fin(L); L.save()

# 20 Ədədlərin çıxılması
L = Lesson(B, 20)
bl = row(5, 220, dx=120)
L.scene('5 şar var idi.', [(L.layer([(E('🎈', 110), x, y) for x, y in bl]), 0.1, 'pop')])
L.scene('3 şar uçdu.', [(L.layer([(E('🎈', 110), x, y) for x, y in bl[:2]]), 0.0, 'fade'), (L.layer([(E('🎈', 90), x, y - 140) for x, y in bl[2:]]), 0.15, 'fly')])
eq = eq_items(['5', '−', '3', '=', '2'], 430, 100)
L.scene('5 çıx 3 bərabərdir 2. Azalan, çıxılan və fərq.', [(L.layer([e]), 0.05 + i * 0.1, 'pop') for i, e in enumerate(eq)] + [(L.layer([(T('azalan', 30, GREY), eq[0][1], 520), (T('çıxılan', 30, GREY), eq[2][1], 520), (T('fərq', 30, GREY), eq[4][1], 520)]), 0.6, 'fade')], keep=True)
fin(L); L.save()

# 21 Ədəd oxu üzərində çıxma
L = Lesson(B, 21)
nl, X = nline(0, 10)
L.scene('9 çıx 3-ü ədəd oxunda tapaq.', [(L.layer([(nl, 400, 300)]), 0.0, 'fade'), (L.layer([(dot(BLUE, 16), X(9), 330)]), 0.4, 'pop'), (L.layer(eq_items(['9', '−', '3', '=', '?'], 90, 80)), 0.1, 'pop')])
L.scene('9-dan başlayıb sola 3 addım atırıq.', seq([L.layer([(hop(X, v, v - 1, color=PURPLE), 400, 300)]) for v in (9, 8, 7)], 0.35, 0.9, 'fade'), keep=True)
L.scene('6-ya çatdıq: 9 çıx 3 bərabərdir 6.', [(L.layer([(dot(RED, 16), X(6), 330)]), 0.05, 'pop'), (L.layer(eq_items(['9', '−', '3', '=', '6'], 500, 90)), 0.4, 'pop')], keep=True)
fin(L); L.save()

# 22 Toplama və çıxmanın əlaqəsi


def domino(a, b, cell=120):
    im = Image.new('RGBA', (2 * cell + 12, cell + 12), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([3, 3, 2 * cell + 8, cell + 8], 18, fill=(255, 255, 255, 255), outline=INK + (255,), width=5)
    d.line([(cell + 6, 12), (cell + 6, cell)], fill=INK + (255,), width=4)
    P = {1: [(.5, .5)], 2: [(.28, .28), (.72, .72)], 3: [(.25, .25), (.5, .5), (.75, .75)], 4: [(.28, .28), (.72, .28), (.28, .72), (.72, .72)], 5: [(.25, .25), (.75, .25), (.5, .5), (.25, .75), (.75, .75)]}
    for k, v in enumerate((a, b)):
        for px, py in P[v]:
            x, y = 6 + k * cell + px * cell, 6 + py * cell
            d.ellipse([x - 11, y - 11, x + 11, y + 11], fill=INK + (255,))
    return im


L = Lesson(B, 22)
L.scene('Domino daşında 3 və 5 nöqtə var.', [(L.layer([(domino(3, 5), 400, 120)]), 0.1, 'pop')])
L.scene('3 üstəgəl 5 bərabərdir 8. 5 üstəgəl 3 də 8-dir.', [(L.layer([(T('3 + 5 = 8', 52, BLUE), 205, 300)]), 0.1, 'pop'), (L.layer([(T('5 + 3 = 8', 52, BLUE), 595, 300)]), 0.55, 'pop')], keep=True)
L.scene('8 çıx 3 bərabərdir 5. 8 çıx 5 bərabərdir 3.', [(L.layer([(T('8 – 3 = 5', 52, PURPLE), 205, 430)]), 0.1, 'pop'), (L.layer([(T('8 – 5 = 3', 52, PURPLE), 595, 430)]), 0.55, 'pop')], keep=True)
L.scene('Bir domino – dörd ifadə.', [(L.layer([(ring(760, 270), 400, 365)]), 0.2, 'pop')], keep=True)
fin(L); L.save()

# 23 Məchulun tapılması
L = Lesson(B, 23)
L.scene('3 alma görünür, bir neçəsi dəsmalın altındadır. Cəmi 5 almadır.', [(L.layer([(E('🍎', 90), x, 200) for x, _ in row(3, 0, x0=140, dx=105)]), 0.05, 'pop'), (L.layer([(E('🧣', 170), 570, 210)]), 0.35, 'fly'), (L.layer(eq_items(['3', '+', '?', '=', '5'], 420, 96)), 0.7, 'pop')])
L.scene('Dəsmalın altında neçə alma var? 5 çıx 3 bərabərdir 2.', [(L.layer([(E('🍎', 90), x, 200) for x, _ in row(3, 0, x0=140, dx=105)] + [(E('🧣', 110), 720, 110)] + eq_items(['3', '+', '?', '=', '5'], 420, 96)), 0.0, 'fade'), (L.layer([(E('🍎', 90), 500, 200), (E('🍎', 90), 600, 200), (ring(230, 130, GREEN), 550, 200)]), 0.4, 'pop')])
L.scene('Gizlənən ədəd 2-dir: 3 üstəgəl 2 bərabərdir 5.', [(L.layer(eq_items(['3', '+', '2', '=', '5'], 525, 64)), 0.3, 'pop')], keep=True)
fin(L); L.save()

# 24 20-yə qədər sayma
L = Lesson(B, 24)
F = frame10(64)
c1 = lambda i, x0: (x0 - 2 * 64 + (i % 5) * 64, 240 - 32 + (i // 5) * 64)
L.scene('Birinci qutuda 10 top var.', [(L.layer([(F, 220, 240)] + [(dot(RED, 22), *c1(i, 220)) for i in range(10)]), 0.1, 'pop'), (L.layer([(T('10', 72, GREEN), 220, 360)]), 0.6, 'pop')])
L.scene('10-dan sonra sayırıq: 11, 12, 13, 14.', [(L.layer([(F, 580, 240)]), 0.0, 'fade')] + seq([L.layer([(dot(BLUE, 22), *c1(i, 580)), (T(str(11 + i), 48, BLUE), 470 + i * 75, 360)]) for i in range(4)], 0.3, 0.9), keep=True)
L.scene('20-yə qədər belə davam edirik.', [(L.layer([(T('11  12  13  14  15  16  17  18  19  20', 30, INK), 400, 500)]), 0.2, 'fade')], keep=True)
fin(L); L.save()

# 25 İrəli və geri sayma
L = Lesson(B, 25)
nl, X = nline(10, 20)
L.scene('İrəli sayanda ədədlər artır: 12, 13, 14, 15.', [(L.layer([(nl, 400, 300)]), 0.0, 'fade')] + seq([L.layer([(hop(X, v, v + 1), 400, 300)]) for v in (12, 13, 14)], 0.4, 0.9, 'fade'))
L.scene('Geri sayanda azalır: 15, 14, 13, 12.', [(L.layer([(nl, 400, 300)]), 0.0, 'fade')] + seq([L.layer([(hop(X, v, v - 1, color=PURPLE), 400, 300)]) for v in (15, 14, 13)], 0.35, 0.9, 'fade'))
fin(L); L.save()

# 26 Onluq və təklik
L = Lesson(B, 26)
L.scene('10 çöpü bir dəstə bağlayırıq. Bu, 1 onluqdur.', [(L.layer(blocks(1, 0, 260, 250, 28)), 0.2, 'pop'), (L.layer([(T('1 onluq', 44, BLUE), 220, 450)]), 0.7, 'pop')])
L.scene('Daha 4 çöp var. Bunlar 4 təklikdir.', [(L.layer([(unit(28), 420 + (i % 2) * 44, 180 + (i // 2) * 44) for i in range(4)]), 0.2, 'pop'), (L.layer([(T('4 təklik', 44, ORANGE), 470, 450)]), 0.6, 'pop')], keep=True)
L.scene('14 – 1 onluq və 4 təklikdir.', [(L.layer([(T('14', 120, RED), 650, 260)]), 0.2, 'pop')], keep=True)
fin(L); L.save()

# 27 Ədədlərin müqayisəsi (20-yə qədər)
L = Lesson(B, 27)
L.scene('15 – 1 onluq və 5 təklik. 12 – 1 onluq və 2 təklik.', [(L.layer(blocks(1, 5, 140, 230, 24) + [(T('15', 70, RED), 190, 420)]), 0.05, 'pop'), (L.layer(blocks(1, 2, 520, 230, 24) + [(T('12', 70, RED), 560, 420)]), 0.5, 'pop')])
L.scene('Onluqlar bərabərdir. Təkliklərə baxırıq: 5 böyükdür 2-dən.', [(L.layer([(ring(110, 170, GREEN), 236, 215), (ring(110, 120, GREEN), 600, 190)]), 0.45, 'pop')], keep=True)
L.scene('Deməli, 15 ədədi 12-dən böyükdür.', [(L.layer(eq_items(['15', '>', '12'], 515, 72)), 0.3, 'pop')], keep=True)
fin(L); L.save()

# 28 Sıralama (20-yə qədər)
L = Lesson(B, 28)
L.scene('Bu ədədləri sıraya düzək: 17, 11, 19, 14.', [(L.layer(numcards([17, 11, 19, 14], 170, dx=170)), 0.3, 'pop')])
L.scene('Kiçikdən böyüyə: 11, 14, 17, 19.', seq([L.layer([c]) for c in numcards([11, 14, 17, 19], 400, dx=170, color=GREEN)], 0.3, 0.9), keep=True)
fin(L); L.save()
