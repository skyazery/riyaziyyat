"""5-ci sinif riyaziyyat, 2-ci hissə: 20 mövzu (224–243), hər mövzuda 10 tapşırıq.
Run: python3 tools/content52.py [OUTDIR]   (default ~/riyaziyyat/5-2)"""
import os, sys
from bookgen import *
init(sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser('~/riyaziyyat/5-2'))
from kit56 import *

CAL = 'Hesablayın.'
EQ = 'Tənliyi həll edin. Kökünü yazın.'


def deg(t, ins, v, stem):
    t.num(ins, [v], stem)
    ck(t, suf='°')


def ex(*toks, size=58):
    return eqbox(list(toks), size)


# ============================================================ 224
t = T(224, 'Dəyişəni olan ifadələr',
      'Hərflə işarə olunmuş və müxtəlif qiymətlər ala bilən kəmiyyətə dəyişən deyilir. Dəyişənin yerinə ədəd yazıb ifadənin qiymətini tapırıq: a = 5 olduqda 3a + 4 = 3 · 5 + 4 = 19. 3a yazılışı 3 · a deməkdir.',
      vstack([txt('a = 5', 60, PURPLE), txt('3a + 4 = 3 · 5 + 4 = 19', 56, INK)], 16))
VAL = 'Dəyişənin verilən qiymətində ifadənin qiymətini tapın.'
for cond, expr_, v in [('a = 5', '3a + 4', 19), ('x = 12', '60 − 2x', 36), ('a = 3, b = 4', '2a + 5b', 26), ('y = 7', 'y² + 1', 50), ('n = 4', '(n + 6) · 3', 30), ('m = 10', 'm : 2 + m', 15)]:
    t.num(VAL, [v], vstack([txt(cond, 52, PURPLE), FX(expr_, '=', BOX, size=60)], 16))
t.choice('Bir dəftər x manatdır. 5 dəftər neçə manatdır? Uyğun ifadəyə toxunun.', ['x + 5', '5x', 'x : 5'], 1, stem=story(['📓']))
t.choice('Elxan a yaşındadır. Anar ondan 3 yaş böyükdür. Anarın yaşını göstərən ifadəyə toxunun.', ['a − 3', '3a', 'a + 3'], 2, stem=story(['👦', '👦']))
t.choice('Kvadratın tərəfi a-dır. Onun perimetrini göstərən ifadəyə toxunun.', ['a²', '4a', 'a + 4'], 1, stem=rect_sides(4, 4, 'a', 'a', 30))
danswer(t, VAL, Dm('10'), vstack([txt('a = 2,5', 52, PURPLE), FX('4a', '=', BOX, size=60)], 16))

# ============================================================ 225
t = T(225, 'Birdəyişənli ifadələrin sadələşdirilməsi',
      'Eyni hərf hissəsi olan toplananlar oxşar toplananlardır. Onları toplayanda əmsalları toplayırıq: 3x + 5x = 8x. Mötərizəni açmaq üçün mötərizə qarşısındakı ədədi hər toplanana vururuq: 4(x + 3) = 4x + 12.',
      vstack([txt('3x + 5x = 8x', 60, INK), txt('4(x + 3) = 4x + 12', 60, INK)], 16))
SAD = 'İfadəni sadələşdirin. Boş xanaya uyğun ədədi yazın.'
for toks, v in [(['3x + 5x', '=', BOX, 'x'], 8), (['9a − 4a', '=', BOX, 'a'], 5), (['2y + 7 + 3y', '=', BOX, 'y + 7'], 5), (['4(x + 3)', '=', '4x +', BOX], 12),
                (['5(2a − 1)', '=', BOX, 'a − 5'], 10), (['6m + m − 2m', '=', BOX, 'm'], 5), (['12b − 5b + b', '=', BOX, 'b'], 8)]:
    t.num(SAD, [v], FX(*toks, size=58))
t.num('İfadəni sadələşdirin. Əvvəl x-in əmsalını, sonra ədədi yazın.', [4, 10], FX('3x + 2 + x + 8', '=', BOX, 'x +', BOX, size=52), disp='4x + 10')
t.choice('Hansı ifadə 7a-ya bərabərdir? Toxunun.', ['3a + 4a', '3a + 4', '7 + a'], 0)
t.num('Əvvəl sadələşdirin, sonra x = 6 olduqda ifadənin qiymətini tapın.', [30], vstack([txt('x = 6', 52, PURPLE), FX('2x + 3x', '=', BOX, size=60)], 16))

# ============================================================ 226
t = T(226, 'Bərabərlik və tənlik',
      'Dəyişəni olan bərabərliyə tənlik deyilir. Tənliyi doğru bərabərliyə çevirən ədəd onun köküdür. 3x + 5 = 26 tənliyində: 3x = 26 − 5 = 21, x = 21 : 3 = 7. Yoxlama: 3 · 7 + 5 = 26.',
      vstack([txt('3x + 5 = 26', 60, INK), txt('3x = 21', 56, GREY), txt('x = 7', 60, PURPLE)], 12))
for toks, v in [('x + 15 = 42', 27), ('x − 18 = 35', 53), ('7x = 63', 9), ('x : 4 = 12', 48), ('3x + 5 = 26', 7), ('2x − 7 = 13', 10), ('5x + 3x = 64', 8), ('100 − x = 64', 36), ('2(x + 3) = 22', 8)]:
    t.num(EQ, [v], vstack([txt(toks, 64, INK), FX('x', '=', BOX, size=60)], 16))
t.choice('Hansı ədəd 4x − 3 = 17 tənliyinin köküdür? Toxunun.', ['4', '5', '6'], 1)

# ============================================================ 227
t = T(227, 'Tənlik qurmaqla məsələ həlli',
      'Məsələni tənliklə həll etmək üçün naməlum kəmiyyəti x ilə işarə edirik, şərtə görə tənlik qurur və onu həll edirik. Bir ədədin 3 mislinə 12 əlavə etdikdə 45 alınırsa: 3x + 12 = 45, x = 11.',
      vstack([txt('3x + 12 = 45', 60, INK), txt('x = 11', 60, PURPLE)], 14))
t.num('Bir ədədin 3 mislinə 12 əlavə etdikdə 45 alındı. Bu ədədi tapın.', [11], FX('3x + 12 = 45', '→', 'x =', BOX, size=52))
t.num('Anar Elxandan 4 yaş böyükdür. Onların yaşlarının cəmi 26-dır. Elxan neçə yaşındadır?', [11], story(['👦', '👦'], ['x + (x + 4) = 26', '→', BOX], size=70))
t.num('Düzbucaqlının uzunluğu enindən 3 sm çoxdur. Perimetri 26 sm-dir. Düzbucaqlının enini tapın.', [5], vstack([rect_sides(6, 3, 'x + 3', 'x', 30), FX('x', '=', BOX, 'sm', size=50)], 14))
t.num('3 eyni dəftər və 5 manatlıq bir kitab birlikdə 11 manatdır. Bir dəftər neçə manatdır?', [2], story(['📓', '📓', '📓', '📕'], ['3x + 5 = 11', '→', BOX, 'manat'], size=70))
t.choice('Səbətdə x alma var idi. 7 alma götürdülər, 18 alma qaldı. Uyğun tənliyə toxunun.', ['x + 7 = 18', 'x − 7 = 18', '7x = 18'], 1, stem=story(['🧺', '🍎']))
t.num('İki ədədin cəmi 50-dir. Onlardan biri digərindən 4 dəfə böyükdür. Kiçik ədədi tapın.', [10], FX('x + 4x = 50', '→', 'x =', BOX, size=52))
t.num('Üç ardıcıl natural ədədin cəmi 45-dir. Onlardan ən kiçiyini tapın.', [14], vstack([txt('x + (x + 1) + (x + 2) = 45', 44, INK), FX('x', '=', BOX, size=56)], 14))
t.num('Aynurun konfetləri Lalənin konfetlərindən 2 dəfə çoxdur. Birlikdə 24 konfetləri var. Lalənin neçə konfeti var?', [8], story(['👧', '👧', '🍬'], ['x + 2x = 24', '→', BOX], size=70))
t.choice('Bir ədədi 5-ə vurub hasildən 3 çıxdıqda 32 alınır. Uyğun tənliyə toxunun.', ['5x − 3 = 32', '5(x − 3) = 32', 'x − 3 · 5 = 32'], 0)
t.num('Bir ədədi 5-ə vurub hasildən 3 çıxdıqda 32 alınır. Bu ədədi tapın.', [7], FX('5x − 3 = 32', '→', 'x =', BOX, size=52))

# ============================================================ 228
t = T(228, 'Bərabərsizliklər',
      'Dəyişəni olan bərabərsizliyi doğru edən ədədlər onun həlləridir. x > 5 bərabərsizliyinin həlləri 5-dən böyük ədədlərdir. ≤ işarəsi «kiçik və ya bərabər», ≥ işarəsi «böyük və ya bərabər» deməkdir.',
      vstack([txt('x > 5:  6, 7, 8, ...', 56, INK), txt('x ≤ 4:  ..., 2, 3, 4', 56, INK)], 14))
t.choice('x > 5 bərabərsizliyinin həllərinin hamısına toxunun.', ['3', '5', '6', '8', '10'], [2, 3, 4], mode='multi')
t.choice('x ≤ 4 bərabərsizliyinin həllərinin hamısına toxunun.', ['2', '4', '5', '0', '7'], [0, 1, 3], mode='multi')
t.num('x < 7 bərabərsizliyinin neçə natural həlli var?', [6], vstack([txt('x < 7', 70, INK), box(100, 88)], 16))
t.num('x > 12 bərabərsizliyinin ən kiçik natural həllini yazın.', [13], vstack([txt('x > 12', 70, INK), box(110, 88)], 16))
t.num('3 < x < 9 bərabərsizliyini ödəyən neçə natural ədəd var?', [5], vstack([txt('3 < x < 9', 70, INK), box(100, 88)], 16))
t.choice('«x ədədi 10-dan böyük deyil» cümləsini necə yazmaq olar? Toxunun.', ['x < 10', 'x ≤ 10', 'x ≥ 10'], 1)
t.choice('Yol nişanına görə sürət saatda 30 km-dən çox olmamalıdır. Uyğun bərabərsizliyə toxunun.', ['v ≤ 30', 'v < 30', 'v ≥ 30'], 0, stem=chip('30', 80, fill=WHITE, outline=RED))
t.num('2x < 14 bərabərsizliyinin ən böyük natural həllini yazın.', [6], vstack([txt('2x < 14', 70, INK), box(100, 88)], 16))
t.num('x + 5 > 11 bərabərsizliyinin ən kiçik natural həllini yazın.', [7], vstack([txt('x + 5 > 11', 70, INK), box(100, 88)], 16))
t.choice('Hansı ədəd 2,5 < x < 3 bərabərsizliyinin həllidir? Toxunun.', ['2,4', '2,8', '3,1'], 1)

# ============================================================ 229
t = T(229, 'Asılı və asılı olmayan dəyişənlər',
      'Bir kəmiyyət digərindən asılı ola bilər. y = 10x düsturunda x asılı olmayan dəyişəndir, y isə x-dən asılı dəyişəndir: x = 3 olduqda y = 30. Məsələn, gedilən yol sürətdən və zamandan asılıdır: S = v · t.',
      vstack([txt('y = 10x', 64, PURPLE), tab([['x', '1', '2', '3'], ['y', '10', '20', '30']], 40)], 16))
t.num('y = 10x düsturuna görə x = 4 olduqda y-in qiymətini tapın.', [40], vstack([txt('y = 10x', 60, PURPLE), FX('x = 4', '→', 'y =', BOX, size=56)], 14))
t.num('y = 3x + 2 düsturuna görə x = 5 olduqda y-in qiymətini tapın.', [17], vstack([txt('y = 3x + 2', 60, PURPLE), FX('x = 5', '→', 'y =', BOX, size=56)], 14))
t.num('Cədvəl y = 2x + 1 düsturu ilə doldurulub. Boş xanaya uyğun ədədi yazın.', [7], vstack([txt('y = 2x + 1', 56, PURPLE), table([[txt('x', 38), txt('1', 38), txt('2', 38), txt('3', 38)], [txt('y', 38), txt('3', 38), txt('5', 38), box(70, 64)]], 80)], 16))
t.choice('Kvadratın perimetri onun tərəfindən asılıdır. Uyğun düstura toxunun.', ['P = a + 4', 'P = 4a', 'P = a²'], 1)
t.num('S = v · t düsturuna görə v = 60 km/saat, t = 3 saat olduqda yolu tapın.', [180], vstack([txt('S = v · t', 60, PURPLE), FX('S', '=', BOX, 'km', size=56)], 14))
t.choice('y = 5x düsturunda asılı dəyişən hansıdır? Toxunun.', ['x', 'y'], 1, stem=txt('y = 5x', 70, PURPLE))
t.num('y = 20 − x düsturuna görə x = 8 olduqda y-in qiymətini tapın.', [12], vstack([txt('y = 20 − x', 60, PURPLE), FX('x = 8', '→', 'y =', BOX, size=56)], 14))
t.num('Bir bilet 5 manatdır. x biletin qiyməti y = 5x düsturu ilə tapılır. 7 bilet neçə manatdır?', [35], story(['🎫'], ['y = 5 · 7 =', BOX, 'manat'], size=70))
t.num('y = 4x düsturuna görə y = 36 olduqda x-in qiymətini tapın.', [9], vstack([txt('y = 4x', 60, PURPLE), FX('y = 36', '→', 'x =', BOX, size=56)], 14))
t.choice('Cədvələ uyğun düstura toxunun.', ['y = x + 2', 'y = 3x', 'y = x + 3'], 1, stem=tab([['x', '1', '2', '3'], ['y', '3', '6', '9']], 40))

# ============================================================ 230
t = T(230, 'Konqruyent bucaqlar. Bucağın tənböləni',
      'Dərəcə ölçüləri bərabər olan bucaqlar konqruyent bucaqlardır. Bucağın təpəsindən çıxıb onu iki bərabər bucağa bölən şüa bucağın tənbölənidir: 80°-li bucağın tənböləni onu 40°-li iki bucağa bölür.',
      ang(80, '80°'))
deg(t, 'Tənbölən 80°-li bucağı iki bərabər hissəyə bölür. Hər hissə neçə dərəcədir?', 40, hstack([ang(80, '80°'), txt('→', 60, GREY), FX(BOX, '+', BOX, size=50)], 20))
deg(t, 'Tənbölənin ayırdığı bucaq 35°-dir. Bütün bucaq neçə dərəcədir?', 70, ang(70, '?'))
t.choice('Konqruyent bucaqların hər ikisinə toxunun.', [ang(45, '45°', 150), ang(60, '60°', 150), ang(45, '45°', 150), ang(30, '30°', 150)], [0, 2], mode='multi')
deg(t, 'AOB bucağı 120°-dir. OC şüası onun tənbölənidir. AOC bucağı neçə dərəcədir?', 60, ang(120, '120°'))
t.choice('Düz bucaq neçə dərəcədir? Toxunun.', ['90°', '180°', '45°'], 0, stem=ang(90, None))
deg(t, 'Açıq bucağın tənbölənindən alınan hər bucaq neçə dərəcədir?', 90, adj(90, '?', '?'))
t.choice('130°-li bucaq hansı növ bucaqdır? Toxunun.', ['iti', 'düz', 'kor'], 2, stem=ang(130, '130°'))
t.choice('40°-li bucaq hansı növ bucaqdır? Toxunun.', ['iti', 'düz', 'kor'], 0, stem=ang(40, '40°'))
deg(t, 'AOB bucağı AOC bucağından 2 dəfə böyükdür. AOC bucağı 25°-dir. AOB bucağı neçə dərəcədir?', 50, ang(50, '?'))
deg(t, 'Tənbölən bucağı 45°-li iki bucağa böldü. Bütün bucaq neçə dərəcədir?', 90, ang(90, '?'))

# ============================================================ 231
t = T(231, 'Qonşu və qarşılıqlı bucaqlar',
      'Bir tərəfi ortaq, digər tərəfləri bir düz xətt əmələ gətirən bucaqlar qonşu bucaqlardır, onların cəmi 180°-dir. İki düz xətt kəsişəndə qarşı-qarşıya duran bucaqlar qarşılıqlı bucaqlardır, onlar bərabərdir.',
      hstack([adj(70, '70°', '110°', 180), cross(40, ['40°', '140°', '40°', '140°'], 160)], 30))
deg(t, 'Qonşu bucaqlardan biri 70°-dir. Digərini tapın.', 110, adj(70, '70°', '?'))
deg(t, 'Qonşu bucaqlardan biri 125°-dir. Digərini tapın.', 55, adj(125, '125°', '?'))
deg(t, 'İki düz xətt kəsişib. Sual işarəsi olan bucağı tapın.', 40, cross(40, ['40°', '', '?', '']))
deg(t, 'İki düz xətt kəsişib. Sual işarəsi olan bucağı tapın.', 140, cross(40, ['40°', '?', '', '']))
t.choice('Qonşu bucaqların cəmi neçə dərəcədir? Toxunun.', ['90°', '180°', '360°'], 1)
deg(t, 'Qonşu bucaqlardan biri digərindən 4 dəfə böyükdür. Kiçik bucağı tapın.', 36, FX('x + 4x = 180°', size=56))
deg(t, 'Qonşu bucaqlar bərabərdir. Hər biri neçə dərəcədir?', 90, adj(90, '?', '?'))
deg(t, 'İki düz xəttin kəsişməsindən alınan dörd bucağın cəmi neçə dərəcədir?', 360, cross(50, ['1', '2', '3', '4']))
deg(t, 'Qarşılıqlı bucaqların cəmi 100°-dir. Onların hər biri neçə dərəcədir?', 50, cross(50, ['?', '', '?', '']))
t.choice('Qarşılıqlı bucaqlar haqqında doğru cümləyə toxunun.', ['bərabərdir', 'cəmi 180°-dir', 'cəmi 90°-dir'], 0)

# ============================================================ 232
t = T(232, 'Düzbucaqlı üçbucağın sahəsi',
      'Düzbucaqlının diaqonalı onu iki bərabər düzbucaqlı üçbucağa bölür. Ona görə düzbucaqlı üçbucağın sahəsi katetlərinin hasilinin yarısına bərabərdir: S = a · b : 2. Katetləri 6 sm və 4 sm olan üçbucağın sahəsi 12 sm²-dir.',
      hstack([poly_l([(0, 0), (6, 0), (6, 4), (0, 4)], [], 30, (227, 242, 253), extra=[([(0, 0), (0, 4), (6, 4)], (255, 224, 178))]), txt('S = 6 · 4 : 2 = 12', 46, INK)], 20))
ST = 'Düzbucaqlı üçbucağın sahəsini tapın.'
for a_, b_ in [(6, 4), (8, 5), (10, 7), (9, 6), (12, 5)]:
    t.num(ST, [a_ * b_ // 2], vstack([rtri(a_, b_, '%d sm' % a_, '%d sm' % b_, 26 if a_ > 8 else 32), FX('S', '=', BOX, size=50)], 10)); ck(t, suf='sm²')
t.num('Düzbucaqlının sahəsi 40 sm²-dir. Diaqonal onu iki üçbucağa bölür. Hər üçbucağın sahəsi neçə sm²-dir?', [20], poly_l([(0, 0), (8, 0), (8, 5), (0, 5)], [(4, 2.5, '40 sm²')], 30, (227, 242, 253), extra=[([(0, 0), (8, 5), (0, 5)], (255, 224, 178))])); ck(t, suf='sm²')
t.num('Düzbucaqlı üçbucağın sahəsi 24 sm², bir kateti 6 sm-dir. Digər kateti tapın.', [8], vstack([rtri(6, 8, '6 sm', '?', 26), txt('S = 24 sm²', 46, INK)], 10)); ck(t, suf='sm')
t.choice('Düzbucaqlı üçbucağın sahəsinin düsturuna toxunun.', ['S = a · b', 'S = a · b : 2', 'S = a + b'], 1)
danswer(t, ST, Dm('7.5'), vstack([rtri(5, 3, '5 sm', '3 sm', 34), DEC('S', '=', 'BOX2', 'sm²', size=50)], 10))
t.num('Rənglənmiş üçbucağın sahəsini tapın.', [12], poly_l([(0, 0), (0, 4), (6, 4)], [(3, 4.7, '6 sm'), (-1.2, 2, '4 sm')], 40, (255, 205, 210))); ck(t, suf='sm²')

# ============================================================ 233
t = T(233, 'Mürəkkəb fiqurların sahəsi',
      'Mürəkkəb fiqurun sahəsini tapmaq üçün onu düzbucaqlılara və düzbucaqlı üçbucaqlara bölürük, hissələrin sahələrini toplayırıq. Bəzən böyük düzbucaqlının sahəsindən kəsilmiş hissənin sahəsini çıxmaq daha asandır.',
      poly_l([(0, 0), (8, 0), (8, 3), (5, 3), (5, 6), (0, 6)], [(4, -0.6, '8'), (-0.7, 3, '6'), (6.5, 3.6, '3'), (8.7, 1.5, '3')], 30))
SA = 'Fiqurun sahəsini tapın. Ölçülər santimetrlədir.'
t.num(SA, [42], poly_l([(0, 0), (8, 0), (8, 4), (5, 4), (5, 6), (0, 6)], [(4, -0.6, '8'), (-0.7, 3, '6'), (6.5, 4.6, '3'), (8.7, 2, '4')], 32)); ck(t, suf='sm²')
t.num(SA, [46], poly_l([(0, 0), (10, 0), (13, 4), (0, 4)], [(5, -0.6, '10'), (-0.7, 2, '4'), (11.5, 4.6, '3')], 26, extra=[([(10, 0), (13, 4), (10, 4)], (255, 224, 178))])); ck(t, suf='sm²')
t.num(SA, [26], poly_l([(0, 0), (6, 0), (6, 3), (4, 3), (4, 5), (0, 5)], [(3, -0.6, '6'), (-0.7, 2.5, '5'), (5, 3.6, '2'), (6.7, 1.5, '3')], 36)); ck(t, suf='sm²')
t.num('Rənglənmiş hissənin sahəsini tapın. Ölçülər santimetrlədir.', [24], poly_l([(0, 0), (8, 0), (8, 4), (0, 4)], [(4, -0.6, '8'), (-0.7, 2, '4'), (2, 4.6, '4')], 32, extra=[([(0, 0), (4, 4), (0, 4)], WHITE)])); ck(t, suf='sm²')
t.num(SA, [23], poly_l([(0, 0), (5, 0), (5, 1), (9, 1), (9, 3), (0, 3)], [(2.5, -0.6, '5'), (-0.7, 1.5, '3'), (7, 0.4, '4'), (9.7, 2, '2')], 34)); ck(t, suf='sm²')
t.num('Evin şəklinin sahəsini tapın. Ölçülər santimetrlədir.', [33], poly_l([(0, 3), (3, 0), (6, 3), (6, 7), (0, 7)], [(3, 7.6, '6'), (-0.7, 5, '4'), (1.1, 1.2, '3'), (3.4, 1.8, '3')], 30, extra=[([(0, 3), (3, 0), (3, 3)], (255, 205, 210)), ([(3, 0), (6, 3), (3, 3)], (255, 205, 210))])); ck(t, suf='sm²')
t.num('Uzunluğu 20 m, eni 15 m olan bağda ölçüləri 5 m və 4 m olan ev var. Bağın qalan hissəsinin sahəsi neçə m²-dir?', [280], poly_l([(0, 0), (10, 0), (10, 7.5), (0, 7.5)], [(5, -0.6, '20 m'), (-1.2, 3.75, '15 m'), (2.5, 3, '5 × 4')], 28, (200, 230, 201), holes=[[(1.25, 2), (3.75, 2), (3.75, 4), (1.25, 4)]])); ck(t, suf='m²')
t.num('Tərəfi 10 sm olan kvadratın ortasından tərəfi 4 sm olan kvadrat kəsildi. Qalan hissənin sahəsini tapın.', [84], poly_l([(0, 0), (10, 0), (10, 10), (0, 10)], [(5, -0.6, '10'), (5, 5, '4')], 22, holes=[[(3, 3), (7, 3), (7, 7), (3, 7)]])); ck(t, suf='sm²')
t.num(SA, [32], poly_l([(0, 0), (5, 0), (11, 4), (0, 4)], [(2.5, -0.6, '5'), (-0.7, 2, '4'), (8, 4.6, '6')], 28, extra=[([(5, 0), (11, 4), (5, 4)], (255, 224, 178))])); ck(t, suf='sm²')
t.choice('Fiqurun sahəsini tapmaq üçün hansı yol düzgündür? Toxunun.', ['8 · 6 − 3 · 3', '8 · 6 + 3 · 3', '8 + 6 + 3 + 3'], 0,
         stem=poly_l([(0, 0), (8, 0), (8, 3), (5, 3), (5, 6), (0, 6)], [(4, -0.6, '8'), (-0.7, 3, '6'), (6.5, 3.6, '3'), (8.7, 1.5, '3')], 26))

# ============================================================ 234
t = T(234, 'Paralel və perpendikulyar düz xətlər',
      'Bir müstəvi üzərində kəsişməyən düz xətlər paralel düz xətlərdir: a ∥ b. Düz bucaq altında kəsişən düz xətlər perpendikulyar düz xətlərdir: a ⊥ b. Düzbucaqlının qarşı tərəfləri paralel, qonşu tərəfləri perpendikulyardır.',
      hstack([lines_pair('parallel', 200), lines_pair('perp', 200)], 40))
t.choice('Paralel düz xətlərə toxunun.', [lines_pair('cross', 170), lines_pair('parallel', 170), lines_pair('perp', 170)], 1)
t.choice('Perpendikulyar düz xətlərə toxunun.', [lines_pair('parallel', 170), lines_pair('cross', 170), lines_pair('perp', 170)], 2)
deg(t, 'Perpendikulyar düz xətlər kəsişəndə neçə dərəcəlik bucaq alınır?', 90, lines_pair('perp', 200))
t.choice('Kvadratın qonşu tərəfləri necədir? Toxunun.', ['paraleldir', 'perpendikulyardır'], 1, stem=rect_sides(4, 4, '', '', 34))
t.choice('Düzbucaqlının qarşı tərəfləri necədir? Toxunun.', ['paraleldir', 'perpendikulyardır'], 0, stem=rect_sides(6, 3, '', '', 34))
t.choice('a ∥ b və b ∥ c-dir. a və c düz xətləri necədir? Toxunun.', ['paraleldir', 'perpendikulyardır', 'kəsişir'], 0)
t.choice('Bir müstəvidə a ⊥ b və c ⊥ b-dir. a və c düz xətləri necədir? Toxunun.', ['paraleldir', 'perpendikulyardır', 'kəsişir'], 0)
t.num('Düzbucaqlıda neçə cüt paralel tərəf var?', [2], vstack([rect_sides(6, 3, '', '', 34), box(100, 86)], 12))
t.num('Kvadratda neçə cüt perpendikulyar tərəf var?', [4], vstack([rect_sides(4, 4, '', '', 34), box(100, 86)], 12))
t.choice('Hansı hərfdə perpendikulyar xətlər var? Toxunun.', ['T', 'V', 'O'], 0)

# ============================================================ 235
t = T(235, 'Üçbucaqların növləri və çəkilməsi',
      'Bucaqlarına görə üçbucaqlar iti bucaqlı, düzbucaqlı və korbucaqlı olur. Tərəflərinə görə: üç tərəfi bərabər olan bərabərtərəfli, iki tərəfi bərabər olan bərabəryanlı, tərəfləri müxtəlif olan müxtəliftərəfli üçbucaqdır.',
      hstack([tri([(0.5, 0), (1, 0.9), (0, 0.9)], size=150), tri([(0, 0), (0, 0.9), (1, 0.9)], size=150, right=1), tri([(0.15, 0.3), (1.2, 0.9), (0, 0.9)], size=150)], 10))
TRI = [tri([(0.5, 0.05), (0.95, 0.9), (0.05, 0.9)], size=140), tri([(0.1, 0.05), (0.1, 0.9), (0.95, 0.9)], size=140, right=1), tri([(0.25, 0.4), (1.2, 0.9), (0, 0.9)], size=140)]
t.choice('Düzbucaqlı üçbucağa toxunun.', TRI, 1)
t.choice('Korbucaqlı üçbucağa toxunun.', TRI, 2)
KIND = ['bərabərtərəfli', 'bərabəryanlı', 'müxtəliftərəfli']
t.choice('Tərəfləri 5 sm, 5 sm və 5 sm olan üçbucaq hansı üçbucaqdır? Toxunun.', KIND, 0, stem=tri([(0.5, 0.05), (1, 0.92), (0, 0.92)], ('5 sm', '5 sm', '5 sm'), 170))
t.choice('Tərəfləri 4 sm, 4 sm və 6 sm olan üçbucaq hansı üçbucaqdır? Toxunun.', KIND, 1, stem=tri([(0.5, 0.2), (1, 0.92), (0, 0.92)], ('4 sm', '6 sm', '4 sm'), 170))
t.choice('Tərəfləri 3 sm, 4 sm və 5 sm olan üçbucaq hansı üçbucaqdır? Toxunun.', KIND, 2, stem=tri([(0, 0.1), (0, 0.9), (0.75, 0.9)], ('3 sm', '4 sm', '5 sm'), 170, right=1))
t.num('Bərabəryanlı üçbucağın yan tərəfi 7 sm, oturacağı 4 sm-dir. Perimetrini tapın.', [18], vstack([tri([(0.5, 0), (0.8, 0.95), (0.2, 0.95)], ('7 sm', '4 sm', '7 sm'), 170), FX('P', '=', BOX, 'sm', size=50)], 10))
t.num('Bərabərtərəfli üçbucağın perimetri 27 sm-dir. Onun tərəfini tapın.', [9], vstack([tri([(0.5, 0.05), (1, 0.92), (0, 0.92)], ('?', '?', '?'), 160), FX('a', '=', BOX, 'sm', size=50)], 10))
t.choice('Hansı üç parçadan üçbucaq qurmaq olar? Toxunun.', ['2, 3 və 7 sm', '4, 5 və 6 sm', '1, 2 və 3 sm'], 1)
t.num('Düzbucaqlı üçbucaqda neçə düz bucaq var?', [1], vstack([tri([(0.1, 0.05), (0.1, 0.9), (0.95, 0.9)], size=150, right=1), box(100, 86)], 12))
t.num('Üçbucağın tərəfləri 6 sm, 8 sm və 10 sm-dir. Onun perimetrini tapın.', [24], vstack([tri([(0, 0.05), (0, 0.9), (0.8, 0.9)], ('6 sm', '8 sm', '10 sm'), 160, right=1), FX('P', '=', BOX, 'sm', size=50)], 10))

# ============================================================ 236
t = T(236, 'Kub və kuboidin səthinin sahəsi',
      'Kubun 6 bərabər kvadrat üzü var: səthinin sahəsi S = 6a². Kuboidin (düzbucaqlı paralelepipedin) qarşı üzləri bərabərdir: S = 2(ab + bc + ac). Ölçüləri 4, 3, 2 sm olan kuboidin səthinin sahəsi 2(12 + 6 + 8) = 52 sm²-dir.',
      hstack([box3d(3, 3, 3, 30, labels=('a', 'a', 'a')), box3d(4, 3, 2, 30, labels=('a', 'b', 'c'))], 20))
SS = 'Səthinin sahəsini tapın.'
for a_ in (3, 5):
    t.num(SS, [6 * a_ * a_], vstack([box3d(3, 3, 3, 32, labels=('%d sm' % a_,) * 3), FX('S', '=', BOX, 'sm²', size=48)], 10))
for a_, b_, c_ in [(4, 3, 2), (5, 4, 3), (6, 2, 1)]:
    t.num(SS, [2 * (a_ * b_ + b_ * c_ + a_ * c_)], vstack([box3d(a_, b_, c_, 34, labels=('%d sm' % a_, '%d sm' % b_, '%d sm' % c_)), FX('S', '=', BOX, 'sm²', size=48)], 10))
t.num('Kubun neçə üzü var?', [6], vstack([box3d(3, 3, 3, 34), box(100, 86)], 10))
t.num('Kubun bir üzünün sahəsi 16 sm²-dir. Onun səthinin sahəsini tapın.', [96], vstack([box3d(3, 3, 3, 34), FX('S', '=', BOX, 'sm²', size=48)], 10))
t.num('Kubun səthinin sahəsi 24 sm²-dir. Onun tilini tapın.', [2], vstack([box3d(3, 3, 3, 34, labels=('?', '', '')), FX('a', '=', BOX, 'sm', size=48)], 10))
t.num('Kuboidin neçə tili var?', [12], vstack([box3d(5, 3, 2, 34), box(100, 86)], 10))
t.num('Ölçüləri 10 dm, 6 dm və 4 dm olan qutunu kağızla örtmək lazımdır. Neçə dm² kağız lazımdır?', [248], vstack([story(['🎁']), FX(BOX, 'dm²', size=50)], 10))

# ============================================================ 237
t = T(237, 'Üçbucaqlı prizmanın səthinin sahəsi',
      'Oturacağı düzbucaqlı üçbucaq olan düz prizmanın 2 üçbucaq oturacağı və 3 düzbucaqlı yan üzü var. Səthin sahəsi = 2 · oturacağın sahəsi + oturacağın perimetri · hündürlük.',
      prism3('4 sm', '3 sm', '10 sm'))
PS = 'Prizmanın səthinin sahəsini tapın. Oturacağın tərəfləri: %d sm, %d sm, %d sm.'
for a_, b_, c_, h_ in [(4, 3, 5, 10), (8, 6, 10, 5), (12, 5, 13, 2), (8, 6, 10, 4)]:
    t.num(PS % (b_, a_, c_), [a_ * b_ + (a_ + b_ + c_) * h_], vstack([prism3('%d sm' % a_, '%d sm' % b_, '%d sm' % h_), FX('S', '=', BOX, 'sm²', size=48)], 10))
t.num('Prizmanın oturacağı katetləri 4 sm və 3 sm olan düzbucaqlı üçbucaqdır. Oturacağın sahəsini tapın.', [6], vstack([rtri(4, 3, '4 sm', '3 sm', 40), FX('S', '=', BOX, 'sm²', size=48)], 10))
t.num('Oturacağın tərəfləri 3 sm, 4 sm, 5 sm, hündürlük 10 sm-dir. Yan səthin sahəsini tapın.', [120], vstack([prism3('4 sm', '3 sm', '10 sm'), FX('(3 + 4 + 5) · 10', '=', BOX, size=46)], 10))
t.num('Üçbucaqlı prizmanın neçə üzü var?', [5], vstack([prism3('', '', ''), box(100, 86)], 10))
t.num('Üçbucaqlı prizmanın neçə təpəsi var?', [6], vstack([prism3('', '', ''), box(100, 86)], 10))
t.num('Üçbucaqlı prizmanın neçə tili var?', [9], vstack([prism3('', '', ''), box(100, 86)], 10))
t.choice('Düz prizmanın yan üzləri hansı fiqurdur? Toxunun.', ['düzbucaqlı', 'üçbucaq', 'dairə'], 0, stem=prism3('', '', ''))

# ============================================================ 238
t = T(238, 'Düz prizmanın həcmi',
      'Düz prizmanın həcmi oturacağın sahəsi ilə hündürlüyün hasilinə bərabərdir: V = S · h. Kuboidin həcmi V = a · b · c, kubun həcmi V = a³. Ölçüləri 5, 4, 3 sm olan kuboidin həcmi 60 sm³-dir.',
      hstack([box3d(5, 4, 3, 30, labels=('5 sm', '4 sm', '3 sm')), txt('V = 5 · 4 · 3 = 60', 44, INK)], 20))
VV = 'Həcmini tapın.'
t.num(VV, [60], vstack([box3d(5, 4, 3, 34, labels=('5 sm', '4 sm', '3 sm')), FX('V', '=', BOX, 'sm³', size=48)], 10))
t.num(VV, [64], vstack([box3d(4, 4, 4, 30, labels=('4 sm',) * 3), FX('V', '=', BOX, 'sm³', size=48)], 10))
t.num('Prizmanın həcmini tapın. Oturacaq düzbucaqlı üçbucaqdır.', [60], vstack([prism3('4 sm', '3 sm', '10 sm'), FX('V', '=', BOX, 'sm³', size=48)], 10))
t.num('Prizmanın həcmini tapın. Oturacaq düzbucaqlı üçbucaqdır.', [120], vstack([prism3('8 sm', '6 sm', '5 sm'), FX('V', '=', BOX, 'sm³', size=48)], 10))
t.num('Prizmanın oturacağının sahəsi 15 sm², hündürlüyü 6 sm-dir. Həcmini tapın.', [90], FX('V', '=', '15 · 6', '=', BOX, 'sm³', size=50))
t.num('Kuboidin həcmi 120 sm³, uzunluğu 6 sm, eni 5 sm-dir. Hündürlüyünü tapın.', [4], vstack([box3d(6, 5, 4, 30, labels=('6 sm', '5 sm', '?')), FX('c', '=', BOX, 'sm', size=48)], 10))
t.num('Akvariumun ölçüləri 50 sm, 30 sm və 40 sm-dir. Onun həcmi neçə sm³-dir?', [60000], vstack([story(['🐠']), FX('V', '=', BOX, 'sm³', size=48)], 10))
t.num('Kubun həcmi 27 sm³-dir. Onun tilini tapın.', [3], vstack([box3d(3, 3, 3, 34, labels=('?', '', '')), FX('a', '=', BOX, 'sm', size=48)], 10))
t.choice('Kuboidin həcminin düsturuna toxunun.', ['V = a · b · c', 'V = a + b + c', 'V = 2(ab + bc + ac)'], 0)
t.num('Fiqur 1 sm³-lik kublardan düzəlib. Onun həcmi neçə sm³-dir?', [12], vstack([stack([[2, 2, 2], [2, 2, 2]], 48), box(110, 86)], 10))

# ============================================================ 239
t = T(239, 'Sahə vahidləri',
      'Sahə vahidləri: 1 m² = 100 dm², 1 dm² = 100 sm², 1 m² = 10 000 sm². Torpaq sahələri ar və hektarla ölçülür: 1 ar = 100 m², 1 ha = 100 ar = 10 000 m², 1 km² = 100 ha.',
      vstack([txt('1 m² = 100 dm²', 52, INK), txt('1 dm² = 100 sm²', 52, INK), txt('1 ha = 10 000 m²', 52, INK)], 10))
CV = 'Boş xanaya uyğun ədədi yazın.'
for l_, r_, v in [('1 m²', 'dm²', 100), ('1 dm²', 'sm²', 100), ('1 m²', 'sm²', 10000), ('5 m²', 'dm²', 500), ('300 sm²', 'dm²', 3), ('1 ha', 'm²', 10000), ('1 km²', 'ha', 100), ('2 ha', 'ar', 200), ('4 m² 25 dm²', 'dm²', 425)]:
    t.num(CV, [v], hstack([txt(l_, 60, INK), txt('=', 60, BLUE), box(200, 86), txt(r_, 52, GREY)], 14))
t.choice('Sinif otağının sahəsini hansı vahidlə ölçmək rahatdır? Toxunun.', ['sm²', 'm²', 'km²'], 1, stem=story(['🏫']))

# ============================================================ 240
t = T(240, 'Həcm vahidləri',
      'Həcm vahidləri: 1 dm³ = 1 000 sm³, 1 m³ = 1 000 dm³. Mayelərin həcmi litrlə ölçülür: 1 l = 1 dm³ = 1 000 ml.',
      vstack([txt('1 dm³ = 1 000 sm³', 52, INK), txt('1 m³ = 1 000 dm³', 52, INK), txt('1 l = 1 dm³ = 1 000 ml', 52, INK)], 10))
for l_, r_, v in [('1 dm³', 'sm³', 1000), ('1 m³', 'dm³', 1000), ('1 l', 'dm³', 1), ('3 dm³', 'sm³', 3000), ('5 000 sm³', 'l', 5), ('2 m³', 'l', 2000), ('1 l', 'ml', 1000), ('2,5 l', 'ml', 2500)]:
    t.num(CV, [v], hstack([txt(l_, 60, INK), txt('=', 60, BLUE), box(200, 86), txt(r_, 52, GREY)], 14))
t.num('Akvariumun ölçüləri 40 sm, 25 sm və 30 sm-dir. Ona neçə litr su tutar?', [30], vstack([story(['🐟']), FX('40 · 25 · 30 = 30 000 sm³', '=', BOX, 'l', size=40)], 10))
t.choice('Çaydana neçə su tutar? Uyğun cavaba toxunun.', ['2 ml', '2 l', '2 m³'], 1, stem=story(['🫖']))

# ============================================================ 241
t = T(241, 'Ədədi orta',
      'Bir neçə ədədin ədədi ortasını tapmaq üçün onların cəmini ədədlərin sayına bölürük: 4, 6 və 8 ədədlərinin ədədi ortası (4 + 6 + 8) : 3 = 6.',
      txt('(4 + 6 + 8) : 3 = 6', 60, INK))
AO = 'Ədədlərin ədədi ortasını tapın.'
for nums in [(4, 6, 8), (10, 15, 20, 35), (7, 9, 11, 13, 15)]:
    t.num(AO, [sum(nums) // len(nums)], vstack([hstack([nchip(v) for v in nums], 12), FX('Orta', '=', BOX, size=50)], 16))
t.num('Şagirdin qiymətləri: 5, 4, 5, 3, 3. Orta qiyməti tapın.', [4], vstack([hstack([nchip(v) for v in (5, 4, 5, 3, 3)], 12), FX('Orta', '=', BOX, size=50)], 16))
t.num('Üç gündə hava 12°, 15° və 18° olub. Orta temperaturu tapın.', [15], vstack([story(['🌡️']), FX('Orta', '=', BOX, '°', size=50)], 10))
t.num('Üç ədədin ədədi ortası 9-dur. Bu ədədlərin cəmini tapın.', [27], FX('Cəm', '=', BOX, size=56))
t.num('Velosipedçi 4 gündə 8, 12, 10 və 14 km yol getdi. O, gündə orta hesabla neçə km yol getdi?', [11], vstack([story(['🚴']), FX(BOX, 'km', size=50)], 10))
t.num('Ədədi ortası 5 olan üç ədəddən ikisi 4 və 6-dır. Üçüncü ədədi tapın.', [5], hstack([nchip(4), nchip(6), box(100, 86)], 14))
danswer(t, AO, Dm('3.5'), vstack([hstack([nchip(v) for v in ('2,5', '3,5', '4,5')], 12), DEC('Orta', '=', 'BOX2', size=50)], 16))
t.choice('Hansı ədədlərin ədədi ortası 10-dur? Toxunun.', ['8, 10, 14', '5, 10, 15', '9, 10, 12'], 1)

# ============================================================ 242
C1, C2, C3, C4 = (255, 167, 38), (66, 165, 245), (102, 187, 106), (239, 83, 80)
t = T(242, 'Dairəvi diaqram',
      'Dairəvi diaqram bütövün hissələrini göstərir. Bütün dairə 100%-dir, yarısı 50%, dörddə biri 25%. Dairə 360° olduğuna görə 1% 3,6°-yə uyğundur: 50% → 180°, 25% → 90°.',
      hstack([pie([(0.5, C1, '50%'), (0.25, C2, '25%'), (0.25, C3, '25%')], 230)], 0))
t.num('Diaqramda sinifdəki 40 şagirdin sevdiyi idman növü göstərilib. Neçə şagird futbolu seçib?', [10], hstack([pie([(0.25, C1, '25%'), (0.5, C2, '50%'), (0.25, C3, '25%')], 220), legend([(C1, 'Futbol'), (C2, 'Üzgüçülük'), (C3, 'Şahmat')], 30)], 20))
t.num('Fermada 600 heyvan var. Onların 50%-i qoyundur. Neçə qoyun var?', [300], hstack([pie([(0.5, C3, '50%'), (0.3, C1, '30%'), (0.2, C2, '20%')], 220), legend([(C3, 'Qoyun'), (C1, 'İnək'), (C2, 'Keçi')], 30)], 20))
pct_num(t, 'Diaqramdakı naməlum hissə neçə faizdir?', 25, pie([(0.5, C1, '50%'), (0.25, C2, '25%'), (0.25, C3, '?')], 230))
pct_num(t, 'Dairənin dörddə bir hissəsi neçə faizdir?', 25, frac_circle(4, 1, 200, C2))
t.num('Kitabxanada 180 kitab var. Onların 10%-i ensiklopediyadır. Neçə ensiklopediya var?', [18], hstack([pie([(0.1, C4, ''), (0.9, C2, '90%')], 200), legend([(C4, 'Ensiklopediya – 10%'), (C2, 'Digər')], 30)], 20))
t.choice('Diaqrama görə ən çox satılan meyvəyə toxunun.', ['Alma', 'Armud', 'Heyva'], 0, stem=hstack([pie([(0.45, C4, '45%'), (0.35, C3, '35%'), (0.2, C1, '20%')], 200), legend([(C4, 'Alma'), (C3, 'Armud'), (C1, 'Heyva')], 30)], 20))
deg(t, 'Diaqramda 50%-lik hissəyə neçə dərəcəlik bucaq uyğun gəlir?', 180, pie([(0.5, C1, '50%'), (0.5, C2, '')], 200))
deg(t, 'Diaqramda 25%-lik hissəyə neçə dərəcəlik bucaq uyğun gəlir?', 90, pie([(0.25, C1, '25%'), (0.75, C2, '')], 200))
t.num('Ailənin aylıq xərci 600 manatdır. Onun 30%-i qidaya xərclənir. Qidaya neçə manat xərclənir?', [180], hstack([pie([(0.3, C1, '30%'), (0.7, C2, '')], 200), legend([(C1, 'Qida'), (C2, 'Digər')], 30)], 20))
pct_num(t, 'Diaqramdakı naməlum hissə neçə faizdir?', 45, pie([(0.2, C1, '20%'), (0.35, C2, '35%'), (0.45, C3, '?')], 230))

# ============================================================ 243
t = T(243, 'Məlumatların təsviri',
      'Məlumatları cədvəl, sütunlu diaqram, xətti diaqram və dairəvi diaqramla təsvir edirik. Sütunlu diaqram kəmiyyətləri müqayisə etmək, xətti diaqram dəyişməni göstərmək, dairəvi diaqram bütövün hissələrini göstərmək üçün əlverişlidir.',
      bars([(txt('B.e', 26), 4), (txt('Ç.a', 26), 7), (txt('Ç', 26), 5), (txt('C.a', 26), 8)], 10, 22, 56))
DAYS = [(txt(d_, 26), v) for d_, v in [('B.e', 6), ('Ç.a', 9), ('Ç', 4), ('C.a', 7), ('C', 10)]]
BAR = bars(DAYS, 10, 26, 56)
t.num('Diaqramda hər gün satılan tortların sayı göstərilib. Çərşənbə axşamı neçə tort satılıb?', [9], BAR)
t.num('Diaqrama görə cümə günü bazar ertəsindən neçə tort çox satılıb?', [4], BAR)
t.num('Diaqrama görə beş gündə cəmi neçə tort satılıb?', [36], BAR)
t.choice('Diaqrama görə ən az tort hansı gün satılıb? Toxunun.', ['B.e', 'Ç', 'C.a'], 1, stem=BAR)
t.num('Cədvələ görə 5A və 5B siniflərində cəmi neçə qız var?', [27], tab([['', '5A', '5B'], ['Qız', 14, 13], ['Oğlan', 12, 15]], 36))
t.choice('Ayların temperaturu hansı ayda ən çox artıb? Toxunun.', ['Mart', 'Aprel', 'May'], 1, stem=line_chart(['Fev', 'Mar', 'Apr', 'May'], [2, 6, 14, 18], 20, 2, 520, 280, RED))
t.choice('Bütövün hissələrini göstərmək üçün hansı diaqram daha uyğundur? Toxunun.', ['dairəvi diaqram', 'xətti diaqram'], 0)
t.choice('Temperaturun gün ərzində dəyişməsini göstərmək üçün hansı diaqram daha uyğundur? Toxunun.', ['dairəvi diaqram', 'xətti diaqram'], 1)
t.num('Piktoqramda bir alma şəkli 5 almanı göstərir. Səbətdə neçə alma var?', [20], vstack([hstack([em('🍎', 70)] * 4, 8), hstack([em('🍎', 40), txt('= 5 alma', 34, GREY)], 8)], 14))
t.num('Cədvələ görə üç gündə orta hesabla neçə şagird kitabxanaya gəlib?', [15], tab([['Gün', 'B.e', 'Ç.a', 'Ç'], ['Şagird', 12, 18, 15]], 36))

TOPICS.sort(key=lambda x: x.n)
save()
