"""3-cü sinif riyaziyyat, 1-ci hissə: 25 mövzu (92–116), hər mövzuda 10 tapşırıq.
Run: python3 tools/content31.py [OUTDIR]   (default ~/riyaziyyat/3-1)"""
import os, sys
from bookgen import *

init(sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser('~/riyaziyyat/3-1'))
E = lambda *t: expr2(list(t), 70)


def colsum(t, pairs, op):
    for a, b in pairs:
        r = a + b if op == '+' else a - b
        t.num('Alt-alta %s.' % ('toplayın' if op == '+' else 'çıxın'), [r], vcolx(a, b, '+' if op == '+' else '−'))


def rows(t, ins, pairs, op):
    for a, b in pairs:
        r = a + b if op == '+' else a - b
        t.num(ins, [r], E(str(a), op, str(b), '=', BOX))


# ============================================================ 92
t = T(92, 'Üçrəqəmli ədədlər',
      'Üçrəqəmli ədədlərdə sağdan birinci rəqəm təklikləri, ikinci rəqəm onluqları, üçüncü rəqəm yüzlükləri göstərir: 546 – 5 yüzlük, 4 onluq, 6 təklik.',
      hstack([hto(5, 4, 6, 80), place_table([5, 4, 6])], 30))
for h, tt, o in [(3, 1, 5), (2, 4, 7), (4, 0, 8)]:
    t.num('Kubları sayın. Mərtəbə cədvəlini doldurun: soldan sağa yazın.', [h, tt, o], vstack([hto(h, tt, o, 74), place_table([None, None, None])], 14), disp='%d, %d, %d' % (h, tt, o))
for h, tt, o in [(5, 3, 2), (6, 0, 4)]:
    t.num('Kublara uyğun ədədi yazın.', [h * 100 + tt * 10 + o], vstack([hto(h, tt, o, 70), hstack([arrow(), box(170, 100)], 14)], 14))
t.choice('274 ədədində 7 rəqəmi hansı mərtəbədədir? Dairəyə alın.', ['Yüzlüklər', 'Onluqlar', 'Təkliklər'], 1, stem=txt('274', 90))
t.choice('835 ədədində neçə onluq var? Dairəyə alın.', ['3', '8', '5'], 0)
t.num('Televizor 579 manatdır. Onu neçə 100, neçə 10 və neçə 1 manatlıqla ödəmək olar? Soldan sağa yazın.', [5, 7, 9],
      vstack([hstack([em('📺', 100), txt('579 man', 54, BLUE)], 16), hstack([note(100, 150, 80), box(), note(10, 150, 80), box(), note(1, 150, 80), box()], 10)], 14), disp='5, 7, 9')
t.num('Ən böyük üçrəqəmli ədədi yazın.', [999], hstack([txt('? ? ?', 70, GREY), arrow(), box(170, 100)], 20))
t.num('Ən kiçik üçrəqəmli ədədi yazın.', [100], hstack([txt('? ? ?', 70, GREY), arrow(), box(170, 100)], 20))

# ============================================================ 93
t = T(93, 'Ədədin yazılış formaları',
      'Eyni ədədi sözlərlə, rəqəmlərlə və açıq şəkildə yazmaq olar: altı yüz iyirmi dörd = 624 = 600 + 20 + 4.',
      vstack([txt('altı yüz iyirmi dörd', 48, BLUE), expr2(['624', '=', '600', '+', '20', '+', '4'], 60)], 16))
t.num('Ədədi açıq şəkildə yazın.', [400, 50, 7], E('457', '=', BOX, '+', BOX, '+', BOX), disp='400 + 50 + 7')
t.num('Ədədi açıq şəkildə yazın.', [800, 50, 2], E('852', '=', BOX, '+', BOX, '+', BOX), disp='800 + 50 + 2')
t.num('Ədədi açıq şəkildə yazın.', [300, 9], E('309', '=', BOX, '+', BOX), disp='300 + 9')
for a, b, c in [(500, 10, 9), (600, 30, 2), (100, 0, 7)]:
    toks = [str(a)] + (['+', str(b)] if b else []) + ['+', str(c), '=', BOX]
    t.num('Cəmə uyğun ədədi yazın.', [a + b + c], expr2(toks, 70))
t.choice('«Üç yüz on iki» hansı ədəddir? Dairəyə alın.', ['312', '302', '321'], 0)
t.choice('«İki yüz on bir» hansı ədəddir? Dairəyə alın.', ['211', '201', '210'], 0)
t.choice('620 ədədi sözlərlə necə yazılır? Dairəyə alın.', ['altı yüz iyirmi', 'altı yüz iki', 'altmış iki'], 0)
t.num('1 yüzlük, 0 onluq və 9 təklik hansı ədəddir?', [109], hstack([hto(1, 0, 9, 80), arrow(), box(170, 100)], 20))

# ============================================================ 94
t = T(94, 'Ədədlərin müqayisəsi və sıralama',
      'Əvvəlcə yüzlüklər müqayisə edilir. Yüzlüklər bərabərdirsə, onluqlar, onluqlar da bərabərdirsə, təkliklər müqayisə edilir: 521 > 435, 642 > 637, 763 > 761.',
      vstack([expr2(['521', '>', '435'], 56), expr2(['642', '>', '637'], 56), expr2(['763', '>', '761'], 56)], 10))
t.sign('Ədədləri müqayisə edin. Dairələrə >, < və ya = yazın.', [('412', '421'), ('638', '638'), ('905', '859')], ['<', '=', '>'])
t.sign('Ədədləri müqayisə edin. Dairələrə işarə yazın.', [('299', '301'), ('740', '704'), ('555', '550')], ['<', '>', '>'])
t.choice('Ən böyük ədədi dairəyə alın.', ['192', '160', '184', '96'], 0)
t.choice('Ən kiçik ədədi dairəyə alın.', ['533', '524', '542', '519'], 3)
t.choice('Ədədləri artan sıra ilə düzün: ən kiçikdən başlayaraq toxunun.', ['192', '96', '184', '160'], [1, 3, 2, 0], mode='order', hint='Əvvəlcə ən kiçik ədədə toxunun.', disp='96, 160, 184, 192')
t.choice('Ədədləri azalan sıra ilə düzün: ən böyükdən başlayaraq toxunun.', ['348', '483', '384', '438'], [1, 3, 2, 0], mode='order', hint='Əvvəlcə ən böyük ədədə toxunun.', disp='483, 438, 384, 348')
t.num('Ədəd oxunda boş xanalara uyğun ədədləri yazın.', [973, 977], numline(970, 980, 74, blanks=(973, 977), size=24), disp='973, 977')
t.num('Boş xanaya uyğun ədədi yazın.', [499], E('498', '<', BOX, '<', '500'))
t.num('4, 7 və 2 rəqəmləri ilə ən böyük üçrəqəmli ədədi yazın.', [742], hstack([nchip(4), nchip(7), nchip(2), arrow(), box(170, 100)], 14))
t.num('Lalənin kitabları 192, 160, 96 və 184 səhifədir. Ən qalın kitab neçə səhifədir?', [192], hstack([em('📚', 100), seq([192, 160, 96, 184], 50), arrow(), box(150, 96)], 16))

# ============================================================ 95
t = T(95, 'Yuvarlaqlaşdırma',
      'Ədədi onluqlara qədər yuvarlaqlaşdıranda təkliklərin yerinə 0 yazırıq. Təklik 5-dən kiçikdirsə, onluqlar dəyişmir: 123 ≈ 120. Təklik 5 və ya 5-dən böyükdürsə, onluqlar 1 artır: 268 ≈ 270.',
      vstack([eqbox(['123', '≈', '120'], 60), eqbox(['268', '≈', '270'], 60)], 14))
for n_ in (77, 123, 268, 512, 345):
    t.num('Ədədi onluqlara qədər yuvarlaqlaşdırın.', [int(round(n_ / 10.0 + 1e-9)) * 10 if n_ % 10 != 5 else (n_ // 10 + 1) * 10], eqbox([str(n_), '≈', BOX], 76))
t.num('Ədəd oxuna baxın. 77-yə ən yaxın onluq hansıdır?', [80], vstack([numline(70, 80, 64, marks=(77,), size=26), hstack([arrow(), box()], 12)], 12))
t.num('Ədədi yüzlüklərə qədər yuvarlaqlaşdırın.', [600], eqbox(['608', '≈', BOX], 76))
t.num('Ədədi yüzlüklərə qədər yuvarlaqlaşdırın.', [300], eqbox(['271', '≈', BOX], 76))
t.choice('Şkafda 56 kitab var. Onluqlara qədər yuvarlaqlaşdıranda neçədir? Dairəyə alın.', ['60', '50', '56'], 0, stem=em('📚', 110))
t.choice('Hansı ədədi onluqlara qədər yuvarlaqlaşdıranda 90 alınır? Dairəyə alın.', ['86', '96', '83'], 0)

# ============================================================ 96
t = T(96, 'Üçrəqəmli ədədlərin toplanması',
      'Üçrəqəmli ədədləri toplayanda əvvəlcə təkliklər, sonra onluqlar, axırda yüzlüklər toplanır: 324 + 213 = 537.',
      hstack([vcolx(324, 213, '+', 60, show=True), expr2(['324', '+', '213', '=', '537'], 52)], 30))
colsum(t, [(324, 213), (446, 350), (512, 276), (231, 604)], '+')
rows(t, 'Cəmi tapın.', [(452, 136), (703, 192)], '+')
t.num('Mərtəbələri ayrı-ayrı toplayın.', [524, 534, 537], stacked([['324', '+', '200', '=', BOX], ['524', '+', '10', '=', BOX], ['534', '+', '3', '=', BOX]], 52), disp='524, 534, 537')
t.num('Bir rəfdə 234, o biri rəfdə 152 karandaş var. Cəmi neçə karandaş var?', [386], word(['✏️', '📦'], ['234', '+', '152', '=', BOX]))
t.choice('Hansı misalın cavabı 579-dur? Dairəyə alın.', ['325 + 254', '315 + 254', '325 + 244'], 0)
t.num('Məktəbdə 312 qız və 245 oğlan var. Məktəbdə neçə şagird var?', [557], word(['👧', '👦', '🏫'], ['312', '+', '245', '=', BOX]))

# ============================================================ 97
t = T(97, 'Üçrəqəmli ədədlərin toplanması (yeni onluğun yaranması)',
      'Təkliklərin cəmi 10-dan çox olanda yeni onluq yaranır: 5 + 7 = 12 təklik = 1 onluq 2 təklik. 245 + 127 = 372.',
      hstack([vcolx(245, 127, '+', 60, show=True), expr2(['245', '+', '127', '=', '372'], 52)], 30))
colsum(t, [(245, 127), (318, 6), (436, 248), (527, 165)], '+')
rows(t, 'Cəmi tapın.', [(235, 27), (649, 34)], '+')
t.num('Mağazada 227 yumurta var idi. Daha 115 yumurta gətirdilər. Mağazada neçə yumurta oldu?', [342], word(['🥚', '🏪'], ['227', '+', '115', '=', BOX]))
t.choice('Hansı cəmdə yeni onluq yaranır? Dairəyə alın.', ['356 + 127', '341 + 125', '230 + 452'], 0)
rows(t, 'Cəmi tapın.', [(163, 128)], '+')
t.num('Şəhərə avtobusla 148, qatarla 236 turist gəldi. Cəmi neçə turist gəldi?', [384], word(['🚌', '🚆'], ['148', '+', '236', '=', BOX]))

# ============================================================ 98
t = T(98, 'Üçrəqəmli ədədlərin toplanması (yeni yüzlüyün yaranması)',
      'Onluqların cəmi 10-dan çox olanda yeni yüzlük yaranır: 5 onluq + 7 onluq = 12 onluq = 1 yüzlük 2 onluq. 253 + 172 = 425.',
      hstack([vcolx(253, 172, '+', 60, show=True), expr2(['253', '+', '172', '=', '425'], 52)], 30))
colsum(t, [(253, 172), (461, 384), (372, 195), (184, 341)], '+')
rows(t, 'Cəmi tapın.', [(590, 130), (382, 56)], '+')
t.num('Onluqları toplayın və yüzlüyə çevirin.', [13, 3], stacked([['8', 'onluq', '+', '5', 'onluq', '=', BOX, 'onluq'], ['13', 'onluq', '=', '1', 'yüzlük', '+', BOX, 'onluq']], 44), disp='13, 3')
t.choice('Hansı cəmdə yeni yüzlük yaranır? Dairəyə alın.', ['362 + 154', '312 + 154', '362 + 114'], 0)
t.num('Kitabxanada 470 nağıl və 260 şeir kitabı var. Cəmi neçə kitab var?', [730], word(['📚', '📖'], ['470', '+', '260', '=', BOX]))
rows(t, 'Cəmi tapın.', [(291, 46)], '+')

# ============================================================ 99
t = T(99, 'Üçrəqəmli ədədlərin toplanması (yeni onluq və yüzlüyün yaranması)',
      'Bəzən həm təkliklərdən yeni onluq, həm də onluqlardan yeni yüzlük yaranır: 258 + 167 = 425.',
      hstack([vcolx(258, 167, '+', 60, show=True), expr2(['258', '+', '167', '=', '425'], 52)], 30))
colsum(t, [(258, 167), (379, 246), (486, 157), (195, 238)], '+')
rows(t, 'Cəmi tapın.', [(568, 275), (647, 86)], '+')
t.num('Birinci gün 365, ikinci gün 278 bilet satıldı. Cəmi neçə bilet satıldı?', [643], word(['🎫'], ['365', '+', '278', '=', BOX]))
t.choice('Hansı cəm 500-ə bərabərdir? Dairəyə alın.', ['247 + 253', '247 + 263', '237 + 253'], 0)
rows(t, 'Cəmi tapın.', [(199, 199)], '+')
t.num('Bağda 186 alma və 157 armud ağacı var. Cəmi neçə ağac var?', [343], word(['🍎', '🍐', '🌳'], ['186', '+', '157', '=', BOX]))

# ============================================================ 100
t = T(100, 'Üç və daha çox ədədin toplanması',
      'Üç ədədi alt-alta toplayanda da əvvəlcə təklikləri, sonra onluqları, sonra yüzlükləri toplayırıq: 258 + 419 + 164 = 841.',
      hstack([vcoln([258, 419, 164], 54, show=True), expr2(['258', '+', '419', '+', '164', '=', '841'], 44)], 30))
for ns in ([258, 419, 164], [283, 397, 172], [402, 13, 152]):
    t.num('Alt-alta toplayın.', [sum(ns)], vcoln(ns, 60))
for ns in ([125, 337, 138], [363, 82, 75]):
    t.num('Cəmi tapın.', [sum(ns)], expr2([str(ns[0]), '+', str(ns[1]), '+', str(ns[2]), '=', BOX], 60))
t.num('Cümə günü 150, şənbə 210, bazar günü 230 bilet satıldı. Üç gündə cəmi neçə bilet satıldı?', [590], word(['🎫', '🎭'], ['150', '+', '210', '+', '230', '=', BOX], 54))
t.num('Toplananların yerini dəyişin və asan yolla toplayın.', [447], E('125', '+', '247', '+', '75', '=', BOX))
t.num('Cəmi tapın.', [375], expr2(['100', '+', '200', '+', '50', '+', '25', '=', BOX], 60))
t.choice('Cəmi 300 olan ifadəni dairəyə alın.', ['100 + 150 + 50', '120 + 150 + 50', '100 + 100 + 50'], 0)
t.num('Üç sinifdə 28, 31 və 29 şagird var. Cəmi neçə şagird var?', [88], word(['🏫'], ['28', '+', '31', '+', '29', '=', BOX]))

# ============================================================ 101
t = T(101, 'Toplamanın digər üsulları',
      'Toplananları mərtəbə qiymətlərinə ayırmaq olar: 267 + 128 = (200 + 100) + (60 + 20) + (7 + 8) = 300 + 80 + 15 = 395.',
      vstack([expr2(['267', '+', '128'], 54), expr2(['=', '300', '+', '80', '+', '15', '=', '395'], 54)], 12))
for a, b in [(154, 538), (256, 126), (479, 105)]:
    h_, te_, o_ = (a // 100 + b // 100) * 100, (a // 10 % 10 + b // 10 % 10) * 10, a % 10 + b % 10
    t.num('Toplananları mərtəbələrə ayırın və cəmi tapın.', [h_, te_, o_, a + b],
          vstack([expr2([str(a), '+', str(b)], 56), expr2(['=', BOX, '+', BOX, '+', BOX, '=', BOX], 56)], 12), disp='%d + %d + %d = %d' % (h_, te_, o_, a + b))
rows(t, 'Cəmi tapın.', [(626, 59), (815, 27)], '+')
t.num('Cəmi tapın.', [475], E('128', '+', '216', '+', '131', '=', BOX))
t.num('Birinci toplananı 400-ə tamamlayın və cəmi tapın.', [243, 643], E('398', '+', '245', '=', '400', '+', BOX, '=', BOX), disp='243, 643')
t.num('Birinci toplananı 200-ə tamamlayın və cəmi tapın.', [355, 555], E('199', '+', '356', '=', '200', '+', BOX, '=', BOX), disp='355, 555')
t.choice('438 + 327 cəminə bərabər olanı dairəyə alın.', ['700 + 50 + 15', '700 + 60 + 15', '600 + 50 + 15'], 0)
t.num('Elxan 438 + 327 misalını mərtəbələrə ayırmaqla həll etdi. Cəm neçədir?', [765], vstack([em('🧑\u200d🏫', 90), E('700', '+', '50', '+', '15', '=', BOX)], 12))

# ============================================================ 102
t = T(102, 'Üçrəqəmli ədədlərin çıxılması',
      'Üçrəqəmli ədədləri çıxanda əvvəlcə təkliklər, sonra onluqlar, axırda yüzlüklər çıxılır: 587 − 243 = 344.',
      hstack([vcolx(587, 243, '−', 60, show=True), expr2(['587', '−', '243', '=', '344'], 52)], 30))
colsum(t, [(587, 243), (968, 425), (756, 302), (489, 176)], '−')
rows(t, 'Fərqi tapın.', [(875, 234), (698, 56)], '−')
t.num('Mərtəbələri ayrı-ayrı çıxın.', [387, 347, 344], stacked([['587', '−', '200', '=', BOX], ['387', '−', '40', '=', BOX], ['347', '−', '3', '=', BOX]], 52), disp='387, 347, 344')
t.num('Mağazada 675 kitab var idi. 230 kitab satıldı. Neçə kitab qaldı?', [445], word(['📚', '🏪'], ['675', '−', '230', '=', BOX]))
t.choice('Hansı fərq 321-ə bərabərdir? Dairəyə alın.', ['654 − 333', '654 − 323', '644 − 333'], 0)
t.num('Məktəbdə 548 şagird var. Onlardan 315-i ekskursiyaya getdi. Neçə şagird getmədi?', [233], word(['🏫', '🚌'], ['548', '−', '315', '=', BOX]))

# ============================================================ 103
t = T(103, 'Üçrəqəmli ədədlərin çıxılması (onluğun ayrılması)',
      'Təkliklər çatmayanda azalandan 1 onluq ayırıb təkliklərə əlavə edirik: 352 − 128 = 224.',
      hstack([vcolx(352, 128, '−', 60, show=True), expr2(['352', '−', '128', '=', '224'], 52)], 30))
colsum(t, [(352, 128), (641, 315), (784, 259), (470, 236)], '−')
rows(t, 'Fərqi tapın.', [(563, 47), (830, 18)], '−')
t.num('Fermada 245 toyuq var idi. 18 toyuğu satdılar. Neçə toyuq qaldı?', [227], word(['🐔'], ['245', '−', '18', '=', BOX]))
t.choice('Hansı fərqdə onluq ayırmaq lazımdır? Dairəyə alın.', ['462 − 138', '468 − 132', '469 − 125'], 0)
rows(t, 'Fərqi tapın.', [(391, 7)], '−')
t.num('Lalə 325 səhifəlik kitabın 117 səhifəsini oxudu. Neçə səhifə qaldı?', [208], word(['📖'], ['325', '−', '117', '=', BOX]))

# ============================================================ 104
t = T(104, 'Üçrəqəmli ədədlərin çıxılması (yüzlüyün ayrılması)',
      'Onluqlar çatmayanda azalandan 1 yüzlük ayırıb onluqlara əlavə edirik: 528 − 173 = 355.',
      hstack([vcolx(528, 173, '−', 60, show=True), expr2(['528', '−', '173', '=', '355'], 52)], 30))
colsum(t, [(528, 173), (637, 252), (815, 341), (406, 251)], '−')
rows(t, 'Fərqi tapın.', [(728, 93), (914, 560)], '−')
t.num('Kitabxanada 615 kitab var idi. Şagirdlər 270 kitab götürdü. Neçə kitab qaldı?', [345], word(['📚'], ['615', '−', '270', '=', BOX]))
t.choice('Hansı fərqdə yüzlük ayırmaq lazımdır? Dairəyə alın.', ['548 − 172', '548 − 132', '598 − 172'], 0)
rows(t, 'Fərqi tapın.', [(500, 120)], '−')
t.num('Avtobus 340 km yol getməlidir. O, 190 km getdi. Neçə kilometr qaldı?', [150], word(['🚌', '🛣️'], ['340', '−', '190', '=', BOX]))

# ============================================================ 105
t = T(105, 'Üçrəqəmli ədədlərin çıxılması (onluq və yüzlüyün ayrılması)',
      'Bəzən həm onluq, həm də yüzlük ayırmaq lazım olur: 511 − 188 = 323.',
      hstack([vcolx(511, 188, '−', 60, show=True), expr2(['511', '−', '188', '=', '323'], 52)], 30))
colsum(t, [(511, 188), (723, 456), (902, 347), (640, 275)], '−')
rows(t, 'Fərqi tapın.', [(800, 365), (431, 79)], '−')
t.num('Stadionda 600 yer var. 438 yerdə tamaşaçı oturub. Neçə yer boşdur?', [162], word(['🏟️'], ['600', '−', '438', '=', BOX]))
t.choice('Hansı fərq 189-a bərabərdir? Dairəyə alın.', ['425 − 236', '425 − 246', '415 − 236'], 0)
t.num('Fərqi tapın və toplama ilə yoxlayın.', [148, 148], stacked([['734', '−', '586', '=', BOX], [BOX, '+', '586', '=', '734']], 56), disp='148, 148')
t.num('Bağda 352 gül var idi. 167 gülü dərdilər. Neçə gül qaldı?', [185], word(['🌹'], ['352', '−', '167', '=', BOX]))

# ============================================================ 106
t = T(106, 'Çıxmanın digər üsulları',
      'Azalanın və çıxılanın üzərinə eyni ədədi əlavə etsək, fərq dəyişmir: 173 − 46 = 177 − 50 = 127.',
      vstack([expr2(['173', '−', '46', '=', '177', '−', '50', '=', '127'], 50), txt('+4          +4', 34, ORANGE)], 6))
t.num('Hər iki ədədin üzərinə 13 əlavə edin və fərqi tapın.', [146], E('233', '−', '87', '=', '246', '−', '100', '=', BOX))
t.num('Hər iki ədədin üzərinə 4 əlavə edin və fərqi tapın.', [449, 149], E('445', '−', '296', '=', BOX, '−', '300', '=', BOX), disp='449, 149')
t.num('Hər iki ədədin üzərinə 4 əlavə edin və fərqi tapın.', [686, 326], E('682', '−', '356', '=', BOX, '−', '360', '=', BOX), disp='686, 326')
rows(t, 'Fərqi tapın.', [(62, 39), (500, 187), (910, 675)], '−')
t.num('Samirin atasının 36, əmisinin 42 yaşı var. Onların yaşları arasında neçə il fərq var?', [6], word(['👨', '🧔'], ['42', '−', '36', '=', BOX]))
t.num('Atası ilə əmisinin yaşları arasındakı fərq 4 ildən sonra neçə olacaq?', [6], word(['👨', '🧔'], ['46', '−', '40', '=', BOX]))
t.choice('Hansı bərabərlik doğrudur? Dairəyə alın.', ['511 − 198 = 513 − 200', '511 − 198 = 510 − 200', '511 − 198 = 513 − 196'], 0)
t.num('Hər iki ədədin üzərinə 11 əlavə edin və fərqi tapın.', [283], E('372', '−', '89', '=', '383', '−', '100', '=', BOX))

# ============================================================ 107
t = T(107, 'Təqribi toplama və çıxma',
      'Ədədləri yuvarlaqlaşdırıb cavabı təqribən tapmaq olar: 608 + 271 ≈ 600 + 300 = 900.',
      vstack([eqbox(['608', '+', '271', '≈', '600', '+', '300', '=', '900'], 48), eqbox(['608', '−', '271', '≈', '600', '−', '300', '=', '300'], 48)], 14))
t.num('Ədədləri yüzlüklərə qədər yuvarlaqlaşdırın və təqribi cəmi tapın.', [600, 300, 900], eqbox(['608', '+', '271', '≈', BOX, '+', BOX, '=', BOX], 54), disp='600 + 300 = 900')
t.num('Ədədləri yüzlüklərə qədər yuvarlaqlaşdırın və təqribi cəmi tapın.', [400, 200, 600], eqbox(['375', '+', '225', '≈', BOX, '+', BOX, '=', BOX], 54), disp='400 + 200 = 600')
t.num('Ədədləri onluqlara qədər yuvarlaqlaşdırın və təqribi fərqi tapın.', [640, 260, 380], eqbox(['641', '−', '258', '≈', BOX, '−', BOX, '=', BOX], 54), disp='640 − 260 = 380')
t.num('Ədədləri onluqlara qədər yuvarlaqlaşdırın və təqribi fərqi tapın.', [700, 200, 500], eqbox(['703', '−', '198', '≈', BOX, '−', BOX, '=', BOX], 54), disp='700 − 200 = 500')
t.num('Bankalarda 519 və 383 kürəcik var. Yüzlüklərə qədər yuvarlaqlaşdırın. Təqribən cəmi neçə kürəcik var?', [900], word(['🫙', '🫙'], ['500', '+', '400', '=', BOX]))
t.num('Sarı kürəciklər 519, qırmızılar 383-dür. Sarılar təqribən nə qədər çoxdur?', [100], word(['🟡', '🔴'], ['500', '−', '400', '=', BOX]))
t.choice('298 + 405 cəmi təqribən neçədir? Dairəyə alın.', ['700', '600', '800'], 0)
t.choice('812 − 397 fərqi təqribən neçədir? Dairəyə alın.', ['400', '500', '300'], 0)
t.num('Ədədləri onluqlara qədər yuvarlaqlaşdırın və təqribi cəmi tapın.', [860], eqbox(['510', '+', '351', '≈', '510', '+', '350', '=', BOX], 54))
t.num('Ədədləri onluqlara qədər yuvarlaqlaşdırın və təqribi fərqi tapın.', [110], eqbox(['322', '−', '208', '≈', '320', '−', '210', '=', BOX], 54))

# ============================================================ 108
t = T(108, '6-ya və 7-yə vurma',
      'Ədədi 6-ya vurmaq 6-nı həmin ədəd dəfə toplamaq deməkdir: 4 · 6 = 6 + 6 + 6 + 6 = 24. 7-yə də belə vururuq: 3 · 7 = 21.',
      vstack([mtab([6, 7], list(range(1, 11)), cell=46), expr2(['4', '·', '6', '=', '24'], 52)], 14))
for bl in ([(6, 4), (7, 8)], [(6, 7), (7, 3)]):
    ans = [r * c for r, c in sorted(bl)]
    t.num('Vurma cədvəlində boş xanaları doldurun. Əvvəl yuxarıdakı xananı yazın.', ans, mtab([6, 7], list(range(1, 11)), set(bl), cell=46), disp=', '.join(map(str, ans)))
for a, b in [(6, 8), (7, 6), (6, 9), (7, 7)]:
    t.num('Hasili tapın.', [a * b], E(str(a), '·', str(b), '=', BOX))
t.num('Hər qutuda 6 yumurta var. 5 qutuda neçə yumurta var?', [30], word(['🥚', '📦'], ['5', '·', '6', '=', BOX]))
t.num('Həftədə 7 gün var. 4 həftədə neçə gün var?', [28], word(['🌞', '🌙'], ['4', '·', '7', '=', BOX]))
t.num('Yeddilərlə sayın. Sıranı davam etdirin.', [28, 35], seq([7, 14, 21, BOX, BOX]), disp='28, 35')
t.choice('Hasili 42 olan ifadəni dairəyə alın.', ['6 · 7', '6 · 6', '7 · 5'], 0)

# ============================================================ 109
t = T(109, '8, 9 və 10-a vurma',
      'Ədədi 10-a vuranda sağına 0 yazılır: 7 · 10 = 70. 8-ə və 9-a vuranda da vurma cədvəlindən istifadə edirik: 8 · 3 = 24, 9 · 4 = 36.',
      vstack([mtab([8, 9, 10], list(range(1, 11)), cell=44), expr2(['7', '·', '10', '=', '70'], 52)], 14))
for rs, bl in (([8, 9], [(8, 6), (9, 4)]), ([9, 10], [(9, 7), (10, 8)])):
    ans = [r * c for r, c in sorted(bl)]
    t.num('Vurma cədvəlində boş xanaları doldurun. Əvvəl yuxarıdakı xananı yazın.', ans, mtab(rs, list(range(1, 11)), set(bl), cell=44), disp=', '.join(map(str, ans)))
for a, b in [(8, 7), (9, 6), (10, 9), (8, 8)]:
    t.num('Hasili tapın.', [a * b], E(str(a), '·', str(b), '=', BOX))
t.num('Hörümçəyin 8 ayağı var. 3 hörümçəyin neçə ayağı var?', [24], word(['🕷️', '🕷️', '🕷️'], ['3', '·', '8', '=', BOX]))
t.num('Hər dəstədə 10 qələm var. 7 dəstədə neçə qələm var?', [70], word(['🖊️'], ['7', '·', '10', '=', BOX]))
t.num('Doqquzlarla sayın. Sıranı davam etdirin.', [36, 45], seq([9, 18, 27, BOX, BOX]), disp='36, 45')
t.choice('Hansı bərabərlik doğrudur? Dairəyə alın.', ['9 · 8 = 72', '9 · 8 = 81', '8 · 8 = 72'], 0)

# ============================================================ 110
t = T(110, '2, 3, 4 və 5-ə bölmə',
      'Bölmədə vurmadan istifadə edirik: 4 · 5 = 20 olduğu üçün 20 : 4 = 5 və 20 : 5 = 4.',
      hstack([triple(20, 4, 5), vstack([expr2(['4', '·', '5', '=', '20'], 50), expr2(['20', ':', '4', '=', '5'], 50)], 10)], 30))
for a, b in [(18, 2), (27, 3), (32, 4), (45, 5)]:
    t.num('Bölməni yerinə yetirin.', [a // b], E(str(a), ':', str(b), '=', BOX))
t.num('Vurmadan istifadə edərək bölün.', [8], stacked([['3', '·', '8', '=', '24'], ['24', ':', '3', '=', BOX]], 60))
t.num('Vurmadan istifadə edərək bölün.', [7], stacked([['5', '·', '7', '=', '35'], ['35', ':', '5', '=', BOX]], 60))
t.num('24 qələmi 4 uşağa bərabər payladılar. Hər uşağa neçə qələm düşdü?', [6], word(['✏️', '🧒'], ['24', ':', '4', '=', BOX]))
t.num('30 almanı 5 qaba bərabər qoydular. Hər qabda neçə alma var?', [6], word(['🍎', '🥣'], ['30', ':', '5', '=', BOX]))
t.num('Üçbucağa baxın və bölməni yerinə yetirin.', [9], hstack([triple(36, 4, None), E('36', ':', '4', '=', BOX)], 30))
t.choice('Qisməti 7 olan ifadəni dairəyə alın.', ['21 : 3', '24 : 3', '16 : 2'], 0)

# ============================================================ 111
t = T(111, '6-ya və 7-yə bölmə',
      '6-ya və 7-yə bölmək üçün vurma cədvəlini xatırlayırıq: 6 · 7 = 42, ona görə də 42 : 6 = 7 və 42 : 7 = 6.',
      hstack([triple(42, 6, 7), vstack([expr2(['42', ':', '6', '=', '7'], 50), expr2(['42', ':', '7', '=', '6'], 50)], 10)], 30))
for a, b in [(42, 6), (54, 6), (49, 7), (63, 7)]:
    t.num('Bölməni yerinə yetirin.', [a // b], E(str(a), ':', str(b), '=', BOX))
t.num('Üçbucağa baxın və bölməni yerinə yetirin.', [8], hstack([triple(48, 6, None), E('48', ':', '6', '=', BOX)], 30))
t.num('Üçbucağa baxın və bölməni yerinə yetirin.', [5], hstack([triple(35, 7, None), E('35', ':', '7', '=', BOX)], 30))
t.num('Həftədə 7 gün var. 28 gün neçə həftədir?', [4], word(['🌞', '🌙'], ['28', ':', '7', '=', BOX]))
t.num('36 karandaşı 6 qutuya bərabər yığdılar. Hər qutuda neçə karandaş var?', [6], word(['✏️', '📦'], ['36', ':', '6', '=', BOX]))
t.sign('Hesablayın və müqayisə edin. Dairələrə >, < və ya = yazın.', [('42 : 6', '48 : 6'), ('56 : 7', '64 : 8')], ['<', '='])
t.choice('Qisməti 6 olan ifadəni dairəyə alın.', ['42 : 7', '42 : 6', '49 : 7'], 0)

# ============================================================ 112
t = T(112, '8, 9 və 10-a bölmə',
      'Ədədi 8-ə böləndə elə ədəd tapırıq ki, 8-i ona vuranda bölünən alınsın: 8 · 3 = 24, ona görə 24 : 8 = 3.',
      hstack([triple(24, 8, 3), vstack([expr2(['8', '·', '3', '=', '24'], 50), expr2(['24', ':', '8', '=', '3'], 50)], 10)], 30))
for a, b in [(32, 8), (72, 9), (80, 10), (56, 8)]:
    t.num('Bölməni yerinə yetirin.', [a // b], E(str(a), ':', str(b), '=', BOX))
t.num('Üçbucağa baxın və bölməni yerinə yetirin.', [6], hstack([triple(48, 8, None), E('48', ':', '8', '=', BOX)], 30))
t.num('Üçbucağa baxın və bölməni yerinə yetirin.', [6], hstack([triple(54, 9, None), E('54', ':', '9', '=', BOX)], 30))
t.num('72 ləçəkdən hər gülə 9 ləçək yapışdırdılar. Neçə gül alındı?', [8], word(['🌸'], ['72', ':', '9', '=', BOX]))
t.num('72 ləçəkdən hər gülə 8 ləçək yapışdırsalar, neçə gül alınar?', [9], word(['🌸'], ['72', ':', '8', '=', BOX]))
t.num('90 qəpiyi 10 qəpiklik sikkələrlə ödəmək üçün neçə sikkə lazımdır?', [9], vstack([coins([10, 10, 10], 70), expr2(['90', ':', '10', '=', BOX], 60)], 12))
t.sign('Hesablayın və müqayisə edin. Dairələrə >, < və ya = yazın.', [('64 : 8', '7'), ('48 : 8', '8')], ['>', '<'])

# ============================================================ 113
t = T(113, 'Məchulun tapılması',
      'Məchul vuruğu tapmaq üçün hasil digər vuruğa bölünür: 5 · □ = 35, 35 : 5 = 7. Məchul böləni tapmaq üçün bölünən qismətə bölünür: 35 : □ = 5, 35 : 5 = 7.',
      vstack([expr2(['5', '·', '7', '=', '35'], 54), expr2(['35', ':', '7', '=', '5'], 54)], 12))
for toks, v in [(['3', '·', BOX, '=', '18'], 6), ([BOX, '·', '5', '=', '20'], 4), (['7', '·', BOX, '=', '56'], 8), ([BOX, '·', '9', '=', '27'], 3)]:
    t.num('Məchul vuruğu tapın.', [v], expr2(toks, 76))
for toks, v in [(['25', ':', BOX, '=', '5'], 5), (['21', ':', BOX, '=', '7'], 3), (['36', ':', BOX, '=', '6'], 6)]:
    t.num('Məchul böləni tapın.', [v], expr2(toks, 76))
t.num('Məchul bölünəni tapın.', [32], expr2([BOX, ':', '4', '=', '8'], 76))
t.num('Lalə 24 almanı 3 qaba bərabər yığdı. Hər qabda neçə alma oldu?', [8], word(['🍎', '🥣'], ['3', '·', BOX, '=', '24']))
t.num('Üçbucağa baxın və məchulu tapın.', [7], hstack([triple(42, None, 6), E(BOX, '·', '6', '=', '42')], 30))

# ============================================================ 114
t = T(114, 'Əməllər ardıcıllığı',
      'Mötərizə yoxdursa, əvvəlcə vurma və bölmə, sonra toplama və çıxma soldan sağa yerinə yetirilir: 12 + 8 : 4 = 12 + 2 = 14. Mötərizə varsa, əvvəlcə mötərizədəki əməl yerinə yetirilir.',
      vstack([expr2(['12', '+', '8', ':', '4', '=', '12', '+', '2', '=', '14'], 46), expr2(['(', '10', '−', '2', ')', '·', '4', '=', '32'], 46)], 14))
for toks, v in [(['25', '−', '5', '+', '12', '−', '10'], 22), (['12', ':', '4', '·', '2'], 6), (['13', '−', '5', '+', '7', '−', '10'], 5)]:
    t.num('Soldan sağa hesablayın.', [v], expr2(toks + ['=', BOX], 60))
for toks, v in [(['12', '+', '8', ':', '4'], 14), (['73', '−', '5', '·', '7'], 38), (['3', '·', '9', '+', '12', ':', '6'], 29), (['17', '−', '28', ':', '4', '+', '6', '·', '3'], 28)]:
    t.num('Əvvəlcə vurma və bölməni, sonra toplama və çıxmanı yerinə yetirin.', [v], expr2(toks + ['=', BOX], 54))
t.num('Əvvəlcə mötərizədəki əməli yerinə yetirin.', [32], E('(', '10', '−', '2', ')', '·', '4', '=', BOX))
t.choice('10 − 2 · 4 ifadəsinin qiyməti neçədir? Dairəyə alın.', ['2', '32'], 0, stem=expr2(['10', '−', '2', '·', '4', '=', '?'], 70))
t.num('Soldan sağa hesablayın.', [18], E('54', ':', '9', '·', '3', '=', BOX))

# ============================================================ 115
t = T(115, 'Dəyişəni olan ifadələr',
      'Hərf olan ifadələr hərfi ifadələrdir, hərf isə dəyişəndir: 5 + a. a = 4 olanda 5 + a = 9 olur.',
      vtab([['a', '1', '4', '16'], ['5 + a', '6', '9', '21']]))
t.num('Cədvəli tamamlayın: soldan sağa yazın.', [6, 9, 21], vtab([['a', '1', '4', '16'], ['5 + a', BOX, BOX, BOX]]), disp='6, 9, 21')
t.num('Cədvəli tamamlayın: soldan sağa yazın.', [0, 2, 18], vtab([['d', '3', '5', '21'], ['d − 3', BOX, BOX, BOX]]), disp='0, 2, 18')
t.num('Cədvəli tamamlayın: soldan sağa yazın.', [1, 3, 5], vtab([['b', '7', '21', '35'], ['b : 7', BOX, BOX, BOX]]), disp='1, 3, 5')
t.num('c = 6 olanda ifadənin qiymətini tapın.', [54], eqbox(['9', '·', 'c', '=', BOX], 70))
t.num('m = 40 olanda ifadənin qiymətini tapın.', [25], eqbox(['m', '−', '15', '=', BOX], 70))
t.num('n = 8 olanda ifadənin qiymətini tapın.', [6], eqbox(['48', ':', 'n', '=', BOX], 70))
t.num('Robot daxil olan ədədə 4 əlavə edir. 8 daxil olsa, çıxışda hansı ədəd alınar?', [12], hstack([em('🤖', 110), vtab([['Giriş', '5', '10', '8'], ['Çıxış', '9', '14', BOX]])], 20))
t.num('Robot daxil olan ədədi 3-ə vurur. 7 daxil olsa, çıxışda hansı ədəd alınar?', [21], hstack([em('🤖', 110), vtab([['Giriş', '2', '5', '7'], ['Çıxış', '6', '15', BOX]])], 20))
t.choice('Bankada 5 kürəcik var idi. Bir neçə kürəcik də əlavə etdilər. Hansı ifadə uyğundur? Dairəyə alın.', ['5 + a', '5 − a', '5 · a'], 0, stem=em('🫙', 110))
t.choice('k = 10 olanda hansı ifadənin qiyməti 30-dur? Dairəyə alın.', ['3 · k', 'k + 3', 'k − 3'], 0)

# ============================================================ 116
t = T(116, 'Tənlik',
      'Məchulu olan bərabərlik tənlikdir: x + 1 = 3. Tənliyi həll etmək məchulu tapmaq deməkdir: x = 3 − 1, x = 2.',
      hstack([scale([em('🌾', 80), weight(1)], [weight(3)], 0, 440), vstack([eqbox(['x', '+', '1', '=', '3'], 50), eqbox(['x', '=', '2'], 50)], 10)], 24))
for toks, v in [(['x', '+', '4', '=', '6'], 2), (['y', '−', '5', '=', '2'], 7), (['10', '−', 'n', '=', '3'], 7), (['x', '+', '21', '=', '25'], 4)]:
    t.num('Tənliyi həll edin. Məchulu yazın.', [v], vstack([eqbox(toks, 70), eqbox([toks[0] if toks[0].isalpha() else toks[2], '=', BOX], 70)], 12))
t.num('Tərəzi bərabərdir. Un kisəsi neçə kiloqramdır?', [2], vstack([scale([em('🌾', 90), weight(1)], [weight(3)], 0, 480), eqbox(['x', '+', '1', '=', '3', ',', 'x', '=', BOX], 56)], 12))
t.num('Hansı ədədlə 8-in cəmi 10-a bərabərdir? Tənliyi həll edin.', [2], eqbox(['x', '+', '8', '=', '10', ',', 'x', '=', BOX], 60))
t.num('15-dən hansı ədədi çıxanda 5 alınır? Tənliyi həll edin.', [10], eqbox(['15', '−', 'x', '=', '5', ',', 'x', '=', BOX], 60))
t.num('Hansı ədəddən 7 çıxanda 8 alınır? Tənliyi həll edin.', [15], eqbox(['x', '−', '7', '=', '8', ',', 'x', '=', BOX], 60))
t.choice('Hansı tənlikdə x = 4-dür? Dairəyə alın.', ['9 + x = 13', 'x + 5 = 10', '17 − x = 10'], 0)
t.num('Samir evdən marketə 70 metr getdi. Evdən məktəbə 90 metrdir. Marketdən məktəbə neçə metr qalıb?', [20], vstack([hstack([em('🏠', 80), em('🏪', 80), em('🏫', 80)], 60), eqbox(['70', '+', 'a', '=', '90', ',', 'a', '=', BOX], 56)], 14))

save()
