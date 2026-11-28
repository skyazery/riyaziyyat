"""2-2 kitabının qısa video dərsləri (mövzu 70–91). Run: python3 tools/lessons22.py"""
from lessons import *

B = '2-2'
E = em


def col(a, b, op, y=170, size=80):
    out = [(T(str(v), size, INK), 470, y + k * 95) for k, v in enumerate((a, b))]
    out.append((T(op, size, BLUE), 350, y + 50))
    im = Image.new('RGBA', (220, 10), (0, 0, 0, 0))
    ImageDraw.Draw(im).rectangle([0, 2, 219, 8], fill=INK + (255,))
    out.append((im, 440, y + 150))
    return out


ONES, TENS = 500, 440  # sütunda təkliklər və onluqlar

# 70 34 − 5
L = Lesson(B, 70)
L.scene('34 çıx 5 neçə edir?', [(L.layer(eq_items(['34', '−', '5', '=', '?'], 80, 80)), 0.05, 'pop'), (L.layer(blocks(3, 4, 200, 310, 24, 8)), 0.45, 'pop')])
L.scene('4 təklikdən 5 çıxmaq olmur. 1 onluğu 10 təkliyə açırıq.', [(L.layer(blocks(2, 0, 200, 310, 24, 8) + [(unit(24), 330 + (i % 5) * 32, 230 + (i // 5) * 32) for i in range(14)]), 0.45, 'fade')])
L.scene('14 çıx 5 bərabərdir 9. Cavab: 34 çıx 5 bərabərdir 29.', [(L.layer([(T('✕', 30, RED), 330 + (i % 5) * 32, 230 + (i // 5) * 32) for i in range(9, 14)]), 0.1, 'pop'), (L.layer(eq_items(['34', '−', '5', '=', '29'], 500, 72)), 0.55, 'pop')], keep=True)
fin(L); L.save()

# 71 43 − 25
L = Lesson(B, 71)
L.scene('43 çıx 25-i sütunla hesablayaq.', [(L.layer(col(43, 25, '−')), 0.3, 'pop')])
L.scene('3-dən 5 çıxmaq olmur. 1 onluq ayırırıq: 13 çıx 5 bərabərdir 8.', [(L.layer([(ring(62, 300, ORANGE), ONES, 220), (T('•', 60, RED), TENS, 105)]), 0.15, 'pop'), (L.layer([(T('8', 80, GREEN), ONES - 3, 380)]), 0.75, 'pop')], keep=True)
L.scene('Onluqlar: 3 çıx 2 bərabərdir 1. Cavab 18.', [(L.layer([(ring(62, 300, BLUE), TENS, 220)]), 0.1, 'pop'), (L.layer([(T('1', 80, GREEN), TENS - 3, 380)]), 0.5, 'pop')], keep=True)
fin(L); L.save()

# 72 Hissə və tam


def partbar(a, b, w=560, y=0):
    im = Image.new('RGBA', (w + 10, 90), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    wa = w * a / (a + b)
    d.rectangle([5, 5, 5 + wa, 85], fill=(180, 210, 250, 255), outline=BLUE + (255,), width=5)
    d.rectangle([5 + wa, 5, 5 + w, 85], fill=(250, 210, 170, 255), outline=ORANGE + (255,), width=5)
    d.text((5 + wa / 2, 45), str(a), font=font(44), fill=INK + (255,), anchor='mm')
    d.text((5 + wa + (w - wa) / 2, 45), str(b), font=font(44), fill=INK + (255,), anchor='mm')
    return im


def whole(n, w=560):
    im = Image.new('RGBA', (w + 10, 90), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rectangle([5, 5, 5 + w, 85], fill=(200, 235, 200, 255), outline=GREEN + (255,), width=5)
    d.text((5 + w / 2, 45), str(n), font=font(44), fill=INK + (255,), anchor='mm')
    return im


L = Lesson(B, 72)
L.scene('Tam iki hissədən ibarətdir: 28 və 14.', [(L.layer([(whole(42), 400, 120)]), 0.05, 'pop'), (L.layer([(partbar(28, 14), 400, 220)]), 0.45, 'pop')])
L.scene('28 üstəgəl 14 bərabərdir 42.', [(L.layer(eq_items(['28', '+', '14', '=', '42'], 360, 70)), 0.2, 'pop')], keep=True)
L.scene('Tamdan bir hissəni çıxsaq, o biri hissə qalır: 42 çıx 28 bərabərdir 14.', [(L.layer(eq_items(['42', '−', '28', '=', '14'], 480, 70)), 0.45, 'pop')], keep=True)
fin(L); L.save()

# 73 Mötərizə
L = Lesson(B, 73)
L.scene('15 çıx 9 üstəgəl 5. Burada 9 üstəgəl 5 mötərizədədir.', [(L.layer([(T('15 −', 90, INK), 165, 140), (T('(9 + 5)', 90, INK), 490, 140)]), 0.1, 'pop')])
L.scene('Mötərizədəki əməl birinci yerinə yetirilir: 9 üstəgəl 5 bərabərdir 14.', [(L.layer([(ring(380, 130, ORANGE), 490, 140)]), 0.2, 'pop'), (L.layer([(T('14', 64, ORANGE), 490, 250)]), 0.75, 'pop')], keep=True)
L.scene('Sonra 15 çıx 14 bərabərdir 1.', [(L.layer(eq_items(['15', '−', '14', '=', '1'], 420, 84)), 0.2, 'pop')], keep=True)
fin(L); L.save()

# 74 İkiaddımlı məsələlər
L = Lesson(B, 74)
L.scene('52 qutu şirə var idi.', [(L.layer([(E('🧃', 90), 140, 130), (T('52', 72, INK), 260, 130)]), 0.1, 'pop')])
L.scene('Əvvəl 19 qutu, sonra 26 qutu satıldı.', [(L.layer([(label('−19', 56, RED), 450, 130)]), 0.15, 'pop'), (L.layer([(label('−26', 56, RED), 620, 130)]), 0.6, 'pop')], keep=True)
L.scene('Birinci addım: 52 çıx 19 bərabərdir 33.', [(L.layer([(T('1)  52 − 19 = 33', 64, BLUE), 400, 300)]), 0.3, 'pop')], keep=True)
L.scene('İkinci addım: 33 çıx 26 bərabərdir 7. 7 qutu qaldı.', [(L.layer([(T('2)  33 − 26 = 7', 64, GREEN), 400, 430)]), 0.2, 'pop')], keep=True)
fin(L); L.save()

# 75 Vurma (sətir, sütun)
L = Lesson(B, 75)
L.scene('Toplar 3 sətirdə düzülüb.', seq([L.layer([(dot(RED, 26), 180 + c * 75, 140 + r * 85) for c in range(6)]) for r in range(3)], 0.15, 0.75))
L.scene('Hər sətirdə 6 top var.', [(L.layer([(T('6', 50, BLUE), 680, 140 + r * 85) for r in range(3)]), 0.3, 'fade')], keep=True)
L.scene('3 vur 6 bərabərdir 18.', [(L.layer(eq_items(['3', '·', '6', '=', '18'], 470, 90)), 0.1, 'pop')], keep=True)
fin(L); L.save()

# 76 2-yə vurma
L = Lesson(B, 76)
L.scene('4 vur 2 nə deməkdir?', [(L.layer(eq_items(['4', '·', '2', '=', '?'], 100, 84)), 0.1, 'pop')])
L.scene('2-ni 4 dəfə toplayırıq.', seq([L.layer([(plate(2, 150), 130 + k * 180, 260)]) for k in range(4)], 0.2, 0.85))
L.scene('2 üstəgəl 2 üstəgəl 2 üstəgəl 2 bərabərdir 8.', [(L.layer(eq_items(['2', '+', '2', '+', '2', '+', '2', '=', '8'], 400, 70, 16)), 0.1, 'fade'), (L.layer(eq_items(['4', '·', '2', '=', '8'], 510, 72)), 0.8, 'pop')], keep=True)
fin(L); L.save()

# 77 4-ə və 5-ə vurma
L = Lesson(B, 77)
L.scene('3 vur 4: 4-ü 3 dəfə toplayırıq.', seq([L.layer([(dot(GREEN, 22), 140 + k * 220 + (i % 2) * 55, 120 + (i // 2) * 55) for i in range(4)]) for k in range(3)], 0.3, 0.8))
L.scene('4 üstəgəl 4 üstəgəl 4 bərabərdir 12.', [(L.layer(eq_items(['3', '·', '4', '=', '4', '+', '4', '+', '4', '=', '12'], 280, 56, 12)), 0.1, 'fade')], keep=True)
L.scene('5-ə vuranda da belədir: 3 vur 5 bərabərdir 15.', [(L.layer(eq_items(['3', '·', '5', '=', '5', '+', '5', '+', '5', '=', '15'], 420, 56, 12)), 0.3, 'fade')], keep=True)
fin(L); L.save()

# 78 Vurma cədvəli


def mtable(hr=None, hc=None):
    im, d = canvas()
    c = 58
    x0, y0 = 400 - 3 * c, 60
    for r in range(6):
        for k in range(6):
            x, y = x0 + k * c, y0 + r * c
            v = r * k if r and k else (k or r or '·')
            hl = (hr == r and k <= (hc or 0)) or (hc == k and r <= (hr or 0))
            fill = (255, 230, 150) if hl else ((230, 240, 255) if r == 0 or k == 0 else (255, 255, 255))
            if r == hr and k == hc:
                fill = (255, 190, 120)
            d.rectangle([x, y, x + c, y + c], fill=fill + (255,), outline=GREY + (255,), width=2)
            d.text((x + c / 2, y + c / 2), str(v), font=font(26), fill=(RED if r == hr and k == hc else INK) + (255,), anchor='mm')
    return im


L = Lesson(B, 78)
L.scene('Bu, vurma cədvəlidir.', [(L.layer([(mtable(), 400, 300)]), 0.1, 'fade')])
L.scene('3 sətrini və 4 sütununu tapırıq.', [(L.layer([(mtable(3, 4), 400, 300)]), 0.3, 'fade')])
L.scene('Kəsişdiyi xanada hasil yazılıb: 3 vur 4 bərabərdir 12.', [(L.layer([(mtable(3, 4), 400, 300)]), 0.0, 'fade'), (L.layer(eq_items(['3', '·', '4', '=', '12'], 470, 72)), 0.45, 'pop')])
fin(L); L.save()

# 79 Bölmə
L = Lesson(B, 79)
L.scene('15 nöqtə var.', [(L.layer([(dot(BLUE, 22), x, y) for x, y in grid(15, 8, 120, 70, 60)]), 0.1, 'pop')])
L.scene('Hər sətirə 5 nöqtə qoyuruq.', [(L.layer([(dot(BLUE, 22), 260 + c * 70, 120 + r * 80) for r in range(3) for c in range(5)]), 0.3, 'fade')])
L.scene('3 sətir alındı: 15 böl 5 bərabərdir 3.', [(L.layer([(T(str(r + 1), 44, RED), 180, 120 + r * 80) for r in range(3)]), 0.1, 'pop'), (L.layer(eq_items(['15', ':', '5', '=', '3'], 470, 84)), 0.5, 'pop')], keep=True)
fin(L); L.save()

# 80 Vurma və bölmənin əlaqəsi
L = Lesson(B, 80)
L.scene('4 sətir, hər sətirdə 5 ulduz: 20 ulduz.', [(L.layer([(E('⭐', 46), 280 + c * 60, 60 + r * 55) for r in range(4) for c in range(5)]), 0.1, 'pop')])
L.scene('4 vur 5 bərabərdir 20. 5 vur 4 də 20-dir.', [(L.layer([(T('4 · 5 = 20', 52, BLUE), 205, 330)]), 0.1, 'pop'), (L.layer([(T('5 · 4 = 20', 52, BLUE), 595, 330)]), 0.55, 'pop')], keep=True)
L.scene('20 böl 4 bərabərdir 5. 20 böl 5 bərabərdir 4.', [(L.layer([(T('20 : 4 = 5', 52, PURPLE), 205, 450)]), 0.1, 'pop'), (L.layer([(T('20 : 5 = 4', 52, PURPLE), 595, 450)]), 0.55, 'pop')], keep=True)
fin(L); L.save()

# 81 500-ə qədər sayma
L = Lesson(B, 81)
L.scene('10 təklik 1 onluq edir.', [(L.layer([(unit(22), 80 + i * 30, 100) for i in range(10)]), 0.05, 'pop'), (L.layer([(T('=', 56, BLUE), 420, 100), (rod(16), 480, 100)]), 0.6, 'pop')])
L.scene('10 onluq 1 yüzlük edir.', [(L.layer([(rod(16), 80 + i * 26, 300) for i in range(10)]), 0.05, 'pop'), (L.layer([(T('=', 56, BLUE), 420, 300), (flat(16), 560, 300)]), 0.6, 'pop')], keep=True)
L.scene('123 – yüz iyirmi üç. 223 – iki yüz iyirmi üç.', [(L.layer([(label('123 – yüz iyirmi üç', 40, RED), 400, 445)]), 0.05, 'pop'), (L.layer([(label('223 – iki yüz iyirmi üç', 40, RED), 400, 515)]), 0.55, 'pop')], keep=True)
fin(L); L.save()

# 82 Yüzlük, onluq, təklik
L = Lesson(B, 82)
L.scene('238 ədədinə baxaq.', [(L.layer([(T('238', 130, INK), 400, 90)]), 0.1, 'pop')])
L.scene('2 yüzlük, 3 onluq və 8 təklik.', [(L.layer([(flat(15), 120, 320), (flat(15), 290, 320)]), 0.05, 'pop'), (L.layer([(rod(15), 410 + i * 24, 320) for i in range(3)]), 0.35, 'pop'), (L.layer([(unit(15), 520 + (i % 4) * 22, 280 + (i // 4) * 22) for i in range(8)]), 0.65, 'pop')], keep=True)
L.scene('238 bərabərdir 200 üstəgəl 30 üstəgəl 8.', [(L.layer(eq_items(['238', '=', '200', '+', '30', '+', '8'], 500, 60, 14)), 0.2, 'fade')], keep=True)
fin(L); L.save()

# 83 Pullar
L = Lesson(B, 83)
L.scene('1 manat 100 qəpikdir.', [(L.layer([(label('1 manat = 100 qəpik', 54, GREEN), 400, 90)]), 0.1, 'pop')])
L.scene('Pulları böyükdən kiçiyə düzürük: 50, 20, 10, 10.', seq([L.layer([(coin(v, 60), x, 260)]) for v, (x, _) in zip([50, 20, 10, 10], row(4, 0, dx=160))], 0.3, 0.9))
L.scene('Sayırıq: 50, 70, 80, 90 qəpik.', seq([L.layer([(T(s, 50, BLUE), x, 380)]) for s, (x, _) in zip(['50', '70', '80', '90'], row(4, 0, dx=160))], 0.2, 0.85), keep=True)
fin(L); L.save()

# 84 Alış-veriş
L = Lesson(B, 84)
L.scene('Kitab 9 manat, top 15 manatdır.', [(L.layer([(E('📘', 120), 220, 150), (label('9 man', 44, RED), 220, 260)]), 0.05, 'pop'), (L.layer([(E('⚽', 120), 580, 150), (label('15 man', 44, RED), 580, 260)]), 0.5, 'pop')])
L.scene('Hər ikisinə nə qədər ödəyirik? Qiymətləri toplayırıq.', [(L.layer([(T('+', 80, BLUE), 400, 160)]), 0.6, 'pop')], keep=True)
L.scene('9 manat üstəgəl 15 manat bərabərdir 24 manat.', [(L.layer([(T('9 + 15 = 24 man', 72, GREEN), 400, 430)]), 0.2, 'pop')], keep=True)
fin(L); L.save()

# 85 Uzunluq
L = Lesson(B, 85)
L.scene('Qısa əşyaları santimetrlə ölçürük.', [(L.layer([(E('✏️', 90), 200, 150), (label('15 sm', 44, BLUE), 200, 250)]), 0.3, 'pop')])
L.scene('Uzun əşyaları isə metrlə ölçürük.', [(L.layer([(E('🚪', 160), 580, 160), (label('2 m', 44, GREEN), 580, 290)]), 0.3, 'pop')], keep=True)
L.scene('100 santimetr 1 metrdir.', [(L.layer([(label('1 m = 100 sm', 70, RED), 400, 450)]), 0.2, 'pop')], keep=True)
fin(L); L.save()

# 86 Kütlə
L = Lesson(B, 86)
L.scene('Kütlə kiloqramla ölçülür.', [(L.layer([(label('kiloqram – kq', 56, BLUE), 400, 90)]), 0.15, 'pop')])
L.scene('Alma 1 kiloqramdan yüngüldür.', [(L.layer([(E('🍎', 110), 200, 260), (label('< 1 kq', 44, GREEN), 200, 370)]), 0.2, 'pop')], keep=True)
L.scene('Qarpız 1 kiloqramdan ağırdır.', [(L.layer([(E('🍉', 140), 600, 260), (label('> 1 kq', 44, RED), 600, 370)]), 0.2, 'pop')], keep=True)
fin(L); L.save()

# 87 Tutum
L = Lesson(B, 87)
L.scene('Tutum litrlə ölçülür.', [(L.layer([(label('litr – l', 56, BLUE), 400, 80)]), 0.15, 'pop')])
L.scene('5 stəkan su 1 litrlik qabı doldurur.', seq([L.layer([(E('🥛', 70), 110 + i * 85, 260)]) for i in range(5)], 0.1, 0.55) + [(L.layer([(T('=', 70, BLUE), 560, 260), (E('🫙', 130), 680, 250), (label('1 l', 40, BLUE), 680, 360)]), 0.75, 'pop')], keep=True)
fin(L); L.save()

# 88 Hadisələr
L = Lesson(B, 88)
L.scene('Gecədən sonra mütləq gündüz olacaq.', [(L.layer([(E('🌙', 90), 150, 120), (T('→', 60, INK), 250, 120), (E('☀️', 90), 350, 120), (label('mütləq', 40, GREEN), 600, 120)]), 0.2, 'pop')])
L.scene('Sabah yağış yağa bilər.', [(L.layer([(E('🌧️', 100), 250, 290), (label('ola bilər', 40, ORANGE), 600, 290)]), 0.2, 'pop')], keep=True)
L.scene('Pişik uça bilməz. Bu, ola bilməz.', [(L.layer([(E('🐱', 100), 250, 460), (label('ola bilməz', 40, RED), 600, 460)]), 0.2, 'pop')], keep=True)
fin(L); L.save()

# 89 Saat
L = Lesson(B, 89)
L.scene('Qısa əqrəb saatı, uzun əqrəb dəqiqəni göstərir.', [(L.layer([(clock(3, 0, 300), 220, 260)]), 0.1, 'pop')])
L.scene('Uzun əqrəb 12-nin üstündədir: saat 3-dür.', [(L.layer([(label('3:00', 54, RED), 220, 470)]), 0.5, 'pop')], keep=True)
L.scene('Uzun əqrəb 6-nın üstündədir: saat 3-ün yarısıdır.', [(L.layer([(clock(3, 30, 300), 580, 260)]), 0.1, 'pop'), (L.layer([(label('3:30', 54, RED), 580, 470)]), 0.6, 'pop')], keep=True)
fin(L); L.save()

# 90 Piktoqram, diaqram
L = Lesson(B, 90)
L.scene('Piktoqramda bir işarə bir neçə əşyanı göstərə bilər.', [(L.layer([(E('🍎', 70), 200, 110), (T('= 2 alma', 50, INK), 380, 110)]), 0.4, 'pop')])
L.scene('3 işarə – 6 alma.', [(L.layer([(E('🍎', 60), 160 + i * 75, 250) for i in range(3)] + [(T('= 6', 56, RED), 470, 250)]), 0.2, 'pop')], keep=True)
L.scene('Diaqramda sütunun hündürlüyü sayı göstərir.', [(L.layer([(bar(h, 70, c), x, 520 - h / 2) for h, c, x in [(120, RED, 300), (180, BLUE, 400), (80, GREEN, 500)]]), 0.3, 'fly')], keep=True)
fin(L); L.save()

# 91 Sorğu
L = Lesson(B, 91)
L.scene('Sorğu keçiririk: hamıya eyni sualı veririk – hansı meyvəni sevirsiniz?', [(L.layer([(E('🧒', 80), x, 100) for x, _ in row(5, 0, dx=110)]), 0.1, 'pop'), (L.layer([(label('?', 50, ORANGE), 400, 190)]), 0.5, 'pop')])
L.scene('Cavabları cədvəldə cizgilərlə qeyd edirik.', [(L.layer([(E('🍎', 60), 220, 300), (tally(3, 50), 360, 300), (E('🍌', 60), 220, 380), (tally(2, 50), 345, 380)]), 0.4, 'pop')], keep=True)
L.scene('Sonra cizgiləri sayırıq: alma 3, banan 2.', [(L.layer([(T('3', 56, RED), 620, 300), (T('2', 56, RED), 620, 380)]), 0.4, 'pop')], keep=True)
fin(L); L.save()
