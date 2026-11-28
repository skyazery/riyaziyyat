"""1-2 kitabının qısa video dərsləri (mövzu 29–49). Run: python3 tools/lessons12.py"""
from lessons import *

B = '1-2'
E = em

# 29 Fiqurlar
L = Lesson(B, 29)
L.scene('Üçbucağın 3 tərəfi və 3 təpəsi var.', [(L.layer([(shape('tri', 200, BLUE), 220, 200)]), 0.05, 'pop'), (L.layer([(dot(RED, 14), 220, 104), (dot(RED, 14), 324, 304), (dot(RED, 14), 124, 304)]), 0.6, 'pop')])
L.scene('Kvadratın 4 tərəfi bərabərdir.', [(L.layer([(shape('square', 180, GREEN), 580, 200)]), 0.1, 'pop'), (L.layer([(T('4 bərabər tərəf', 36, GREEN), 580, 330)]), 0.55, 'fade')], keep=True)
L.scene('Dairənin isə təpəsi yoxdur.', [(L.layer([(shape('circle', 170, RED), 400, 470)]), 0.15, 'pop')], keep=True)
fin(L); L.save()

# 30 Fəza fiqurları
L = Lesson(B, 30)
L.scene('Zar kub formasındadır. Qutu – kuboid.', [(L.layer([(E('🎲', 150), 200, 190), (T('kub', 44, BLUE), 200, 300)]), 0.05, 'pop'), (L.layer([(E('📦', 160), 580, 190), (T('kuboid', 44, BLUE), 580, 300)]), 0.5, 'pop')])
L.scene('Top kürədir. Banka silindr, dondurma qabı isə konusdur.', [(L.layer([(E('⚽', 120), 160, 450), (T('kürə', 40, RED), 160, 540)]), 0.05, 'pop'), (L.layer([(E('🥫', 120), 400, 450), (T('silindr', 40, RED), 400, 540)]), 0.4, 'pop'), (L.layer([(E('🍦', 120), 640, 450), (T('konus', 40, RED), 640, 540)]), 0.72, 'pop')], keep=True)
fin(L); L.save()

# 31 Tam, yarı
L = Lesson(B, 31)


def half(cut=True, sep=0):
    im = Image.new('RGBA', (300 + sep, 300), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    if not cut:
        d.ellipse([0, 0, 296, 296], fill=(250, 200, 80, 255), outline=ORANGE + (255,), width=6)
    else:
        d.pieslice([0, 0, 296, 296], 90, 270, fill=(250, 200, 80, 255), outline=ORANGE + (255,), width=6)
        d.pieslice([sep + 4, 0, sep + 300, 296], 270, 90, fill=(250, 200, 80, 255), outline=ORANGE + (255,), width=6)
    for px, py in [(.3, .3), (.62, .25), (.25, .6), (.38, .42), (.7, .6), (.4, .78), (.72, .8)]:
        x = px * 296 + (sep if px > .5 else 0)
        d.ellipse([x - 16, py * 296 - 16, x + 16, py * 296 + 16], fill=RED + (255,))
    return im


L.scene('Bu, tam pizzadır.', [(L.layer([(half(cut=False), 400, 240)]), 0.1, 'pop'), (L.layer([(T('tam', 56, BLUE), 400, 450)]), 0.5, 'pop', 1.4)])
L.scene('Onu 2 bərabər hissəyə bölürük.', [(L.layer([(half(sep=60), 400, 240)]), 0.3, 'fade')])
L.scene('Hər hissə yarıdır.', [(L.layer([(half(sep=60), 400, 240)]), 0.0, 'fade'), (L.layer([(T('yarı', 50, RED), 270, 450), (T('yarı', 50, RED), 530, 450)]), 0.3, 'pop')])
fin(L); L.save()

# 32 Toplama (ədəd oxu)
L = Lesson(B, 32)
nl, X = nline(10, 20)
L.scene('12 üstəgəl 3 neçə edir?', [(L.layer(eq_items(['12', '+', '3', '=', '?'], 100, 80)), 0.1, 'pop'), (L.layer([(nl, 400, 300)]), 0.3, 'fade'), (L.layer([(dot(BLUE, 16), X(12), 330)]), 0.6, 'pop')])
L.scene('Toplayanda ədəd oxunda sağa gedirik: 3 addım.', seq([L.layer([(hop(X, v, v + 1), 400, 300)]) for v in (12, 13, 14)], 0.4, 0.9, 'fade'), keep=True)
L.scene('15-ə çatdıq: 12 üstəgəl 3 bərabərdir 15.', [(L.layer([(dot(RED, 16), X(15), 330)]), 0.05, 'pop'), (L.layer(eq_items(['12', '+', '3', '=', '15'], 500, 90)), 0.4, 'pop')], keep=True)
fin(L); L.save()

# 33 10-a tamamlamaqla toplama
L = Lesson(B, 33)
F = frame10()
fx, fy, cell = 300, 300, 84
cpos = lambda i: (fx - 2 * cell + (i % 5) * cell, fy - cell / 2 + (i // 5) * cell)
red, blue = dot(RED), dot(BLUE)
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
L.scene('Deməli, 8 üstəgəl 5 bərabərdir 13. İndi siz cəhd edin!', [(L.layer(eq_items(['8', '+', '5', '=', '13'], 300, 110)), 0.05, 'pop'), (L.layer([(em('🦊', 140), W / 2, 480)]), 0.62, 'pop')])
L.save()

# 34 Üç ədəd: əvvəlcə 10
L = Lesson(B, 34)
L.scene('6 üstəgəl 4 üstəgəl 5 neçə edir?', [(L.layer(eq_items(['6', '+', '4', '+', '5'], 120, 90)), 0.1, 'pop')])
L.scene('Əvvəlcə 10 düzəldirik: 6 üstəgəl 4 bərabərdir 10.', [(L.layer([(ring(330, 130, GREEN), 285, 120)]), 0.1, 'pop'), (L.layer(eq_items(['6', '+', '4', '=', '10'], 300, 80)), 0.45, 'pop')], keep=True)
L.scene('Sonra 10 üstəgəl 5 bərabərdir 15.', [(L.layer(eq_items(['10', '+', '5', '=', '15'], 450, 80)), 0.2, 'pop')], keep=True)
fin(L); L.save()

# 35 Çıxma (ədəd oxu)
L = Lesson(B, 35)
nl, X = nline(10, 20)
L.scene('14 çıx 3 neçə edir?', [(L.layer(eq_items(['14', '−', '3', '=', '?'], 100, 80)), 0.1, 'pop'), (L.layer([(nl, 400, 300)]), 0.3, 'fade'), (L.layer([(dot(BLUE, 16), X(14), 330)]), 0.6, 'pop')])
L.scene('Çıxanda ədəd oxunda sola gedirik: 3 addım.', seq([L.layer([(hop(X, v, v - 1, color=PURPLE), 400, 300)]) for v in (14, 13, 12)], 0.4, 0.9, 'fade'), keep=True)
L.scene('11-ə çatdıq: 14 çıx 3 bərabərdir 11.', [(L.layer([(dot(RED, 16), X(11), 330)]), 0.05, 'pop'), (L.layer(eq_items(['14', '−', '3', '=', '11'], 500, 90)), 0.4, 'pop')], keep=True)
fin(L); L.save()

# 36 10-a qədər azaltmaqla çıxma
L = Lesson(B, 36)
nl, X = nline(5, 15)
L.scene('13 çıx 4 neçə edir?', [(L.layer(eq_items(['13', '−', '4', '=', '?'], 100, 80)), 0.1, 'pop'), (L.layer([(nl, 400, 300)]), 0.3, 'fade'), (L.layer([(dot(BLUE, 16), X(13), 330)]), 0.6, 'pop')])
L.scene('Əvvəlcə 3 çıxırıq və 10-a çatırıq.', [(L.layer([(hop(X, 13, 10, color=PURPLE, label='−3'), 400, 300)]), 0.3, 'fade'), (L.layer([(dot(GREEN, 16), X(10), 330)]), 0.7, 'pop')], keep=True)
L.scene('Sonra daha 1 çıxırıq: 9 qalır. 13 çıx 4 bərabərdir 9.', [(L.layer([(hop(X, 10, 9, color=ORANGE, label='−1'), 400, 300)]), 0.1, 'fade'), (L.layer([(dot(RED, 16), X(9), 330)]), 0.35, 'pop'), (L.layer(eq_items(['13', '−', '4', '=', '9'], 500, 90)), 0.6, 'pop')], keep=True)
fin(L); L.save()

# 37 Toplama və çıxmanın əlaqəsi
L = Lesson(B, 37)
L.scene('9, 7 və 16 – bir ailədir.', [(L.layer(numcards([9, 7, 16], 110, dx=180)), 0.2, 'pop')])
L.scene('9 üstəgəl 7 bərabərdir 16. 7 üstəgəl 9 da 16-dır.', [(L.layer([(T('9 + 7 = 16', 50, BLUE), 205, 290)]), 0.1, 'pop'), (L.layer([(T('7 + 9 = 16', 50, BLUE), 595, 290)]), 0.55, 'pop')], keep=True)
L.scene('16 çıx 9 bərabərdir 7. 16 çıx 7 bərabərdir 9.', [(L.layer([(T('16 – 9 = 7', 50, PURPLE), 205, 430)]), 0.1, 'pop'), (L.layer([(T('16 – 7 = 9', 50, PURPLE), 595, 430)]), 0.55, 'pop')], keep=True)
fin(L); L.save()

# 38 100-ə qədər sayma


def hundred(hl=()):
    im = Image.new('RGBA', (520, 520), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    c = 51
    for i in range(100):
        r, k = divmod(i, 10)
        x, y = 5 + k * c, 5 + r * c
        v = i + 1
        d.rectangle([x, y, x + c, y + c], fill=((255, 230, 150) if v in hl else (255, 255, 255)) + (255,), outline=GREY + (255,), width=2)
        d.text((x + c / 2, y + c / 2), str(v), font=font(20), fill=((RED if v in hl else INK)) + (255,), anchor='mm')
    return im


L = Lesson(B, 38)
L.scene('Yüzlük kartda 1-dən 100-ə qədər ədədlər var.', [(L.layer([(hundred(), 400, 300)]), 0.1, 'fade')])
L.scene('On-on sayaq: 10, 20, 30, 40, 50, 60, 70, 80, 90, 100.', [(L.layer([(hundred(range(10, 101, 10)), 400, 300)]), 0.1, 'fade')])
fin(L); L.save()

# 39 Onluq və təklik
L = Lesson(B, 39)
L.scene('47 ədədinə baxaq.', [(L.layer([(T('47', 150, INK), 400, 120)]), 0.1, 'pop')])
L.scene('Soldakı rəqəm onluqdur: 4 onluq.', [(L.layer(blocks(4, 0, 160, 340, 26)), 0.15, 'pop'), (L.layer([(T('4 onluq', 44, BLUE), 210, 515)]), 0.6, 'pop')], keep=True)
L.scene('Sağdakı rəqəm təklikdir: 7 təklik.', [(L.layer([(unit(26), 470 + (i % 4) * 40, 300 + (i // 4) * 40) for i in range(7)]), 0.15, 'pop'), (L.layer([(T('7 təklik', 44, ORANGE), 530, 515)]), 0.6, 'pop')], keep=True)
fin(L); L.save()

# 40 Qəpik, manat
L = Lesson(B, 40)
cv = [1, 3, 5, 10, 20, 50]
L.scene('Sikkələr: 1, 3, 5, 10, 20 və 50 qəpik.', seq([L.layer([(coin(v, 52), x, 180)]) for v, (x, _) in zip(cv, row(6, 0, dx=125))], 0.15, 0.9))
L.scene('1 manat 100 qəpikdir.', [(L.layer([(label('1 manat = 100 qəpik', 56, GREEN), 400, 420)]), 0.15, 'pop')], keep=True)
fin(L); L.save()

# 41 Alış-veriş
L = Lesson(B, 41)
L.scene('Topun qiyməti 30 qəpikdir.', [(L.layer([(E('⚽', 150), 220, 200), (label('30 q', 54, RED), 220, 330)]), 0.1, 'pop')])
L.scene('Biz 50 qəpik veririk.', [(L.layer([(coin(50, 70), 560, 200)]), 0.2, 'fly')], keep=True)
L.scene('Satıcı qalığı qaytarır: 50 çıx 30 bərabərdir 20 qəpik.', [(L.layer([(coin(20, 60), 560, 360)]), 0.2, 'fly'), (L.layer([(T('50 – 30 = 20', 70, BLUE), 400, 500)]), 0.5, 'pop')], keep=True)
fin(L); L.save()

# 42 Uzun, qısa
L = Lesson(B, 42)


def _pencil(n, cell):
    L_ = n * cell  # qələmin bütün uzunluğu (ucu da daxil)
    im = Image.new('RGBA', (L_ + 2, 50), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rectangle([0, 8, L_ - 38, 42], fill=(250, 200, 40, 255), outline=INK + (255,), width=3)
    d.polygon([(L_ - 38, 8), (L_, 25), (L_ - 38, 42)], fill=(240, 210, 170, 255), outline=INK + (255,))
    return im


L.scene('Yuxarıdakı qələm uzundur, aşağıdakı qələm qısadır.', [(L.layer([(_pencil(8, 56), 100 + (8 * 56 + 2) / 2, 150)]), 0.05, 'fly'), (L.layer([(_pencil(4, 56), 100 + (4 * 56 + 2) / 2, 300)]), 0.45, 'fly')])
L.scene('Kublarla ölçək: uzun qələm 8 kub, qısa qələm 4 kubdur.', [(L.layer([(unit(50, BLUE), 128 + i * 56, 210) for i in range(8)] + [(T('8', 56, BLUE), 680, 210)]), 0.25, 'pop'), (L.layer([(unit(50, BLUE), 128 + i * 56, 360) for i in range(4)] + [(T('4', 56, BLUE), 400, 360)]), 0.6, 'pop')], keep=True)
L.scene('Ağac hündürdür, kol isə alçaqdır.', [(L.layer([(E('🌳', 160), 620, 465), (E('🌿', 80), 740, 505)]), 0.2, 'pop')], keep=True)
fin(L); L.save()

# 43 Santimetr


def ruler(n=10, cm=60):
    im = Image.new('RGBA', (n * cm + 40, 90), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, n * cm + 38, 88], 8, fill=(255, 240, 190, 255), outline=INK + (255,), width=3)
    for i in range(n + 1):
        x = 20 + i * cm
        d.line([(x, 0), (x, 34)], fill=INK + (255,), width=3)
        d.text((x, 58), str(i), font=font(26), fill=INK + (255,), anchor='mm')
    return im


L = Lesson(B, 43)
L.scene('Uzunluğu santimetrlə ölçürük. Bu, xətkeşdir.', [(L.layer([(ruler(), 400, 360)]), 0.1, 'fly')])
L.scene('Xətkeşin 0-ını qələmin ucuna qoyuruq.', [(L.layer([(_pencil(6, 60), 100 + (6 * 60 + 2) / 2, 285)]), 0.2, 'fly'), (L.layer([(ring(80, 140, RED), 100, 330)]), 0.6, 'pop', 0.95)], keep=True)
L.scene('Qələm 6 santimetrdir.', [(L.layer([(ring(80, 140, RED), 460, 330), (label('6 sm', 60, RED), 460, 160)]), 0.2, 'pop')], keep=True)
fin(L); L.save()

# 44 Ağır, yüngül


def scale(tilt):
    im, d = canvas()
    d.polygon([(400, 330), (360, 470), (440, 470)], fill=GREY + (255,))
    a = math.radians(tilt)
    lx, ly = 400 - 230 * math.cos(a), 330 - 230 * math.sin(a)
    rx, ry = 400 + 230 * math.cos(a), 330 + 230 * math.sin(a)
    d.line([(lx, ly), (rx, ry)], fill=INK + (255,), width=10)
    for x, y in [(lx, ly), (rx, ry)]:
        d.line([(x - 70, y + 50), (x + 70, y + 50)], fill=INK + (255,), width=8)
        d.line([(x, y), (x - 70, y + 50)], fill=INK + (255,), width=3)
        d.line([(x, y), (x + 70, y + 50)], fill=INK + (255,), width=3)
    return im, (lx, ly), (rx, ry)


L = Lesson(B, 44)
sc, lp, rp = scale(-14)
L.scene('Tərəzinin bir tərəfində qarpız, o biri tərəfində alma var.', [(L.layer([(sc, 400, 300)]), 0.05, 'fade'), (L.layer([(E('🍉', 110), lp[0], lp[1] - 10)]), 0.4, 'pop'), (L.layer([(E('🍎', 70), rp[0], rp[1] + 15)]), 0.7, 'pop')])
L.scene('Ağır tərəf aşağı enir. Qarpız ağırdır, alma yüngüldür.', [(L.layer([(label('ağır', 44, RED), lp[0], lp[1] - 110), (label('yüngül', 44, GREEN), rp[0], rp[1] - 70)]), 0.4, 'pop')], keep=True)
L.scene('Kütləni kiloqramla ölçürük.', [(L.layer([(label('kq', 70, BLUE), 400, 110)]), 0.3, 'pop')], keep=True)
fin(L); L.save()

# 45 Tutum


def glass(level, w=110, h=180, color=BLUE):
    im = Image.new('RGBA', (w + 10, h + 10), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    if level:
        d.rectangle([8, 5 + h * (1 - level), w, h], fill=tuple(int(v * 0.4 + 255 * 0.6) for v in color) + (255,))
    d.line([(5, 5), (5, h + 3), (w + 3, h + 3), (w + 3, 5)], fill=INK + (255,), width=6)
    return im


L = Lesson(B, 45)
L.scene('Bu iki qabdan hansı çox su tutur?', [(L.layer([(glass(0, 120, 160), 230, 260), (glass(0, 200, 240), 560, 220)]), 0.1, 'pop')])
L.scene('Kiçik qab 2 stəkan, böyük qab 5 stəkan su tutur.', [(L.layer([(glass(1, 120, 160), 230, 260)]), 0.1, 'fade'), (L.layer([(glass(1, 200, 240), 560, 220)]), 0.5, 'fade'), (L.layer([(E('🥛', 62), 200 + i * 60, 385) for i in range(2)] + [(E('🥛', 62), 440 + i * 60, 385) for i in range(5)] + [(T('2 stəkan', 40, BLUE), 230, 450), (T('5 stəkan', 40, BLUE), 560, 450)]), 0.6, 'pop')], keep=True)
L.scene('Çox su tutan qabın tutumu böyükdür. Tutumu litrlə ölçürük.', [(L.layer([(ring(250, 270, GREEN), 560, 225)]), 0.2, 'pop'), (L.layer([(label('litr', 54, GREEN), 400, 70)]), 0.7, 'pop')], keep=True)
fin(L); L.save()

# 46 Gün, həftə, ay
L = Lesson(B, 46)
L.scene('Günün vaxtları: səhər, günorta, axşam, gecə.', seq([L.layer([(E(e, 110), x, 160), (T(s, 34, BLUE), x, 260)]) for e, s, (x, _) in zip(['🌅', '☀️', '🌇', '🌙'], ['səhər', 'günorta', 'axşam', 'gecə'], row(4, 0, dx=180))], 0.2, 0.9))
L.scene('Həftədə 7 gün var.', [(L.layer([(label('1 həftə = 7 gün', 54, PURPLE), 400, 380)]), 0.2, 'pop')], keep=True)
L.scene('İldə 12 ay və 4 fəsil var.', [(L.layer([(E(e, 60), x, 500) for e, (x, _) in zip(['🌸', '🌻', '🍂', '❄️'], row(4, 0, dx=110))]), 0.4, 'pop')], keep=True)
fin(L); L.save()

# 47 Saat
L = Lesson(B, 47)
L.scene('Saatın qısa və uzun əqrəbi var.', [(L.layer([(clock(7, 0, 340), 400, 250)]), 0.1, 'pop')])
L.scene('Uzun əqrəb 12-nin üstündədir. Deməli, saat tamamdır.', [(L.layer([(ring(80, 80, BLUE), 400, 120)]), 0.25, 'pop')], keep=True)
L.scene('Qısa əqrəb 7-ni göstərir. Bu saat 7-dir.', [(L.layer([(ring(80, 80, RED), 335, 363)]), 0.25, 'pop'), (L.layer([(label('7:00', 56, RED), 620, 420)]), 0.6, 'pop')], keep=True)
fin(L); L.save()

# 48 Cədvəl, piktoqram
L = Lesson(B, 48)
rows_ = [('🍎', 4), ('🍌', 2), ('🍐', 5)]
L.scene('Piktoqramda hər şəkil bir meyvəni göstərir.', seq([L.layer([(E(e, 60), 160 + i * 70, 120 + k * 90) for i in range(n)]) for k, (e, n) in enumerate(rows_)], 0.2, 0.9))
L.scene('Almalar 4, bananlar 2, armudlar 5-dir.', seq([L.layer([(T(str(n), 56, RED), 620, 120 + k * 90)]) for k, (e, n) in enumerate(rows_)], 0.15, 0.85), keep=True)
L.scene('Cədvəldə saymaq üçün cizgi qoyuruq: 5 cizgi belə olur.', [(L.layer([(tally(5, 70), 400, 480)]), 0.5, 'pop')], keep=True)
fin(L); L.save()

# 49 Diaqram
L = Lesson(B, 49)
bs = [(3, '🍎', RED), (5, '🍌', (240, 180, 40)), (2, '🍐', GREEN)]
xs = [240, 400, 560]
L.scene('Diaqramda hər meyvənin sütunu var.', [(L.layer([(E(e, 64), x, 520) for (n, e, c), x in zip(bs, xs)]), 0.1, 'pop')] + seq([L.layer([(bar(n * 70, 90, c), x, 470 - n * 35)]) for (n, e, c), x in zip(bs, xs)], 0.35, 0.9, 'fly'))
L.scene('Sütun nə qədər hündürdürsə, say o qədər çoxdur.', [(L.layer([(ring(130, 400, ORANGE), 400, 280)]), 0.3, 'pop')], keep=True)
L.scene('Banan ən çoxdur: 5.', [(L.layer([(T('5', 70, ORANGE), 510, 150)]), 0.3, 'pop')], keep=True)
fin(L); L.save()
