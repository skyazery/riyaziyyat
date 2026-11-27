"""6-cı sinif riyaziyyat, 2-ci hissə: 23 mövzu (267–289), hər mövzuda 10 tapşırıq.
Run: python3 tools/content62.py [OUTDIR]   (default ~/riyaziyyat/6-2)"""
import math, os, sys
from bookgen import *
init(sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser('~/riyaziyyat/6-2'))
from kit56 import *

CAL = 'Hesablayın.'
PI = Dm('3.14')


def q(*lines_, size=58):
    return vstack([txt(l_, size, INK) if isinstance(l_, str) else l_ for l_ in lines_], 14)


def nb(t, ins, v, stem, suf=None):
    t.num(ins, [v], stem)
    if suf:
        ck(t, suf=suf)


SETA = q('A = {1, 2, 3, 4, 5}', 'B = {4, 5, 6, 7}', size=50)
SETC = q('C = {2, 4, 6, 8, 10}', 'D = {3, 6, 9}', size=50)

# ============================================================ 267
t = T(267, 'Çoxluq',
      'Müəyyən əlamətə görə birləşdirilmiş obyektlər çoxluq, onları təşkil edən obyektlər isə çoxluğun elementləridir: A = {2, 4, 6, 8}. 4 ∈ A yazılışı «4 A çoxluğunun elementidir» deməkdir. Heç bir elementi olmayan çoxluq boş çoxluqdur.',
      q('A = {2, 4, 6, 8}', '4 ∈ A,  5 ∉ A'))
t.choice('Cüt ədədlərin hamısına toxunun.', ['3', '4', '7', '10', '12'], [1, 3, 4], mode='multi')
nb(t, 'Çoxluğun neçə elementi var?', 4, q('A = {2, 4, 6, 8}', box(100, 86)))
t.choice('5 ədədi A çoxluğunun elementidirmi? Toxunun.', ['Bəli', 'Xeyr'], 0, stem=txt('A = {1, 3, 5, 7}', 60, INK))
t.choice('Hansı çoxluq boşdur? Toxunun.', ['{0}', '10-dan kiçik və 20-dən böyük ədədlər', '{1}'], 1)
nb(t, '10-dan kiçik natural ədədlər çoxluğunun neçə elementi var?', 9, box(100, 86))
t.choice('B = {a, b, c} çoxluğunun alt çoxluğuna toxunun.', ['{a, c}', '{a, d}', '{d}'], 0)
nb(t, '{1, 2, 3} çoxluğunun neçə alt çoxluğu var? Boş çoxluğu və çoxluğun özünü də sayın.', 8, box(100, 86))
t.choice('Həftənin «Ç» hərfi ilə başlayan günlərinin hamısına toxunun.', ['Çərşənbə axşamı', 'Cümə', 'Çərşənbə', 'Şənbə'], [0, 2], mode='multi')
nb(t, '20 ədədinin bölənləri çoxluğunun neçə elementi var?', 6, box(100, 86))
t.choice('{3, 5, 7} çoxluğuna bərabər olan çoxluğa toxunun.', ['{7, 5, 3}', '{3, 5}', '{3, 5, 7, 9}'], 0)

# ============================================================ 268
t = T(268, 'Çoxluqlar üzərində əməllər',
      'İki çoxluğun ortaq elementlərindən ibarət çoxluq onların kəsişməsidir: A ∩ B. Hər iki çoxluğun bütün elementlərindən ibarət çoxluq onların birləşməsidir: A ∪ B. A çoxluğunun B-yə daxil olmayan elementləri A \\ B fərqidir.',
      q('A = {1, 2, 3}, B = {2, 3, 4}', 'A ∩ B = {2, 3}', 'A ∪ B = {1, 2, 3, 4}', size=46))
nb(t, 'A ∩ B kəsişməsinin neçə elementi var?', 2, q(SETA, box(100, 86)))
nb(t, 'A ∪ B birləşməsinin neçə elementi var?', 7, q(SETA, box(100, 86)))
t.choice('A ∩ B kəsişməsinin elementlərinin hamısına toxunun.', ['1', '4', '5', '6'], [1, 2], mode='multi', stem=SETA)
t.choice('A \\ B fərqinin elementlərinin hamısına toxunun.', ['1', '2', '3', '4', '6'], [0, 1, 2], mode='multi', stem=SETA)
t.choice('A = {a, b, c}, B = {b, c, d}. A ∩ B kəsişməsinə toxunun.', ['{b, c}', '{a, d}', '{a, b, c, d}'], 0)
t.choice('A = {a, b, c}, B = {b, c, d}. A ∪ B birləşməsinə toxunun.', ['{a, b, c, d}', '{b, c}', '{a, b, c}'], 0)
nb(t, 'C ∩ D kəsişməsinin neçə elementi var?', 1, q(SETC, box(100, 86)))
nb(t, 'C ∪ D birləşməsinin neçə elementi var?', 7, q(SETC, box(100, 86)))
nb(t, 'A – 10-dan kiçik cüt natural ədədlər, B – 10-dan kiçik və 3-ə bölünən natural ədədlər çoxluğudur. A ∩ B kəsişməsinin neçə elementi var?', 1, box(100, 86))
t.choice('Kəsişməsi boş olan çoxluqlara toxunun.', ['{1, 3, 5} və {2, 4, 6}', '{1, 2} və {2, 3}', '{5} və {5, 6}'], 0)

# ============================================================ 269
t = T(269, 'Eyler-Venn diaqramı ilə məsələ həlli',
      'Eyler-Venn diaqramında çoxluqlar dairələrlə göstərilir, ortaq hissə kəsişmədir. Futbol oynayan 17, şahmat oynayan 13 şagirddən 5-i hər ikisini oynayırsa, cəmi 17 + 13 − 5 = 25 şagird var.',
      venn(12, 5, 8, 'Futbol', 'Şahmat'))
V1 = venn(12, 5, 8, 'Futbol', 'Şahmat')
nb(t, 'Diaqrama görə futbol oynayan şagirdlərin hamısı neçə nəfərdir?', 17, V1)
nb(t, 'Diaqrama görə şahmat oynayan şagirdlərin hamısı neçə nəfərdir?', 13, V1)
nb(t, 'Diaqrama görə cəmi neçə şagird var?', 25, V1)
V2 = venn('?', 6, '?', 'İngilis (18)', 'Rus (15)', 'cəmi 30, heç biri: ?')
nb(t, 'Sinifdə 30 şagird var. Diaqrama baxın. Yalnız ingilis dilini öyrənən neçə nəfərdir?', 12, V2)
nb(t, 'Sinifdə 30 şagird var. Diaqrama baxın. Yalnız rus dilini öyrənən neçə nəfərdir?', 9, V2)
nb(t, 'Sinifdə 30 şagird var. Diaqrama baxın. Heç birini öyrənməyən neçə nəfərdir?', 3, V2)
nb(t, '25 şagirdin 14-ü rəsm, 12-si musiqi dərnəyinə gedir. Hər şagird ən azı bir dərnəyə gedir. Neçə şagird hər iki dərnəyə gedir?', 1, venn('', '?', '', 'Rəsm (14)', 'Musiqi (12)'))
nb(t, 'Diaqramda dairələrdən kənarda 6 yazılıb. Cəmi neçə element var?', 20, venn(7, 3, 4, 'A', 'B', 6))
t.choice('Eyler-Venn diaqramında dairələrin ortaq hissəsi nəyi göstərir? Toxunun.', ['A ∩ B', 'A ∪ B', 'A \\ B'], 0, stem=venn('', '★', '', 'A', 'B'))
nb(t, '40 turistdən 25-i Bakıda, 20-si Tbilisidə olub, 8-i heç birində olmayıb. Neçə turist hər iki şəhərdə olub?', 13, venn('', '?', '', 'Bakı (25)', 'Tbilisi (20)', 'heç biri: 8'))

# ============================================================ 270
t = T(270, 'Dəyişəni olan ifadələr',
      'Dəyişənin qiyməti mənfi ədəd, kəsr və ya onluq kəsr də ola bilər. a = −2 olduqda 3a + 10 = 3 · (−2) + 10 = 4.',
      q('a = −2', '3a + 10 = 3 · (−2) + 10 = 4', size=50))
VAL = 'Dəyişənin verilən qiymətində ifadənin qiymətini tapın.'
for cond, ex_, v in [('a = −2', '3a + 10', 4), ('x = 4', 'x² − 3x', 4), ('a = 5, b = −3', '2a + b', 7), ('y = −1', '5 − 2y', 7), ('a = −3', 'a²', 9)]:
    zans(t, VAL, v, q(txt(cond, 52, PURPLE), FX(ex_, '=', BOX, size=58)))
t.choice('«Ədədin 3 mislindən 4 az» ifadəsinə toxunun.', ['3x − 4', '4 − 3x', '3(x − 4)'], 0)
t.choice('İki ardıcıl natural ədədin cəmini göstərən ifadəyə toxunun.', ['n + (n + 1)', '2n', 'n + 2'], 0)
nb(t, VAL, 3, q(hstack([txt('x =', 52, PURPLE), fr(1, 2, 44, PURPLE)], 8), FX('4x + 1', '=', BOX, size=58)))
nb(t, VAL, 3, q(txt('m = 0,5', 52, PURPLE), FX('10m − 2', '=', BOX, size=58)))
t.choice('Düzbucaqlının uzunluğu a, eni b-dir. Perimetri göstərən ifadəyə toxunun.', ['2(a + b)', 'ab', 'a + b'], 0, stem=rect_sides(6, 3, 'a', 'b', 30))

# ============================================================ 271
t = T(271, 'Riyazi ifadələrdə mötərizələrin açılması',
      'Mötərizə qarşısında müsbət ədəd varsa, mötərizədəki hədlərin işarələri dəyişmir: 3(x + 4) = 3x + 12. Mənfi ədəd və ya «−» işarəsi varsa, işarələr əksinə dəyişir: −(x − 7) = −x + 7, −2(a − 5) = −2a + 10.',
      q('3(x + 4) = 3x + 12', '−(x − 7) = −x + 7'))
OP = 'Mötərizəni açın. Boş xanaya uyğun ədədi yazın.'
for toks, v in [(['3(x + 4)', '=', '3x +', BOX], 12), (['−2(a − 5)', '=', '−2a +', BOX], 10), (['5(2y − 3)', '=', BOX, 'y − 15'], 10), (['−(x − 7)', '=', '−x +', BOX], 7),
                (['4 − (x + 3)', '=', BOX, '− x'], 1), (['6(a + 2) − 4a', '=', BOX, 'a + 12'], 2), (['−3(2x + 1)', '=', BOX, 'x − 3'], -6), (['7 − 2(x − 1)', '=', '9 −', BOX, 'x'], 2)]:
    zans(t, OP, v, FX(*toks, size=54))
t.choice('−(a − b) ifadəsinə bərabər olan ifadəyə toxunun.', ['−a + b', '−a − b', 'a − b'], 0)
t.choice('2(x + y) ifadəsinə bərabər olan ifadəyə toxunun.', ['2x + 2y', '2x + y', 'x + 2y'], 0)

# ============================================================ 272
t = T(272, 'Dəyişənli ifadələrin sadələşdirilməsi',
      'İfadəni sadələşdirmək üçün mötərizələri açır, sonra oxşar toplananları toplayırıq: 4(2a − 1) − 3(a − 2) = 8a − 4 − 3a + 6 = 5a + 2.',
      q('4(2a − 1) − 3(a − 2)', '= 8a − 4 − 3a + 6 = 5a + 2', size=50))
SD = 'İfadəni sadələşdirin. Boş xanaya uyğun ədədi yazın.'
for toks, v in [(['5a − 2a + 7a', '=', BOX, 'a'], 10), (['2(x + 3) + 4x', '=', BOX, 'x + 6'], 6), (['8y − (3y − 2)', '=', BOX, 'y + 2'], 5), (['−4m + 9m − m', '=', BOX, 'm'], 4), (['7b − 10b', '=', BOX, 'b'], -3), (['0,5x + 1,5x', '=', BOX, 'x'], 2)]:
    zans(t, SD, v, FX(*toks, size=56))
t.num('İfadəni sadələşdirin. Əvvəl x-in əmsalını, sonra ədədi yazın.', [2, 3], FX('3x + 4 − x − 1', '=', BOX, 'x +', BOX, size=52), disp='2x + 3')
t.num('İfadəni sadələşdirin. Əvvəl a-nın əmsalını, sonra ədədi yazın.', [5, 2], FX('4(2a − 1) − 3(a − 2)', '=', BOX, 'a +', BOX, size=44), disp='5a + 2')
nb(t, 'İfadəni sadələşdirin və a = 4 olduqda qiymətini tapın.', 14, q(txt('a = 4', 52, PURPLE), FX('3(a + 2) − a', '=', BOX, size=56)))
t.choice('Oxşar toplananlara toxunun.', ['3x və −5x', '3x və 3y', '2a və 2'], 0)

# ============================================================ 273
t = T(273, 'Tənliklər',
      'Tənliyi həll edərkən toplananı bir tərəfdən digərinə keçirəndə onun işarəsini dəyişirik: 5x + 4 = 2x + 19, 5x − 2x = 19 − 4, 3x = 15, x = 5.',
      q('5x + 4 = 2x + 19', '3x = 15', txt('x = 5', 58, PURPLE), size=54))
EQ = 'Tənliyi həll edin. Mənfi cavab üçün − düyməsinə toxunun.'
for s_, v in [('3x − 7 = 11', 6), ('5x + 4 = 2x + 19', 5), ('2(x − 3) = 10', 8), ('x + 9 = 4', -5), ('7x = −21', -3), ('4x − 3 = x + 9', 4), ('3(x + 2) = 2x + 11', 5), ('x : 3 = 5', 15), ('0,5x = 3,5', 7)]:
    zans(t, EQ, v, q(s_, FX('x', '=', BOX, size=56), size=56))
t.choice('Hansı ədəd 2x + 5 = 1 tənliyinin köküdür? Toxunun.', ['−2', '2', '3'], 0)

# ============================================================ 274
t = T(274, 'Tənlik qurmaqla məsələ həlli',
      'Naməlum kəmiyyəti x ilə işarə edirik, digər kəmiyyətləri x ilə ifadə edib tənlik qururuq. Məsələn, iki ədədin cəmi 64, biri digərindən 12 çoxdursa: x + (x + 12) = 64, x = 26.',
      q('x + (x + 12) = 64', txt('x = 26', 58, PURPLE), size=54))
nb(t, 'Bir ədədi 4-ə vurub 7 əlavə etdikdə 31 alındı. Bu ədədi tapın.', 6, FX('4x + 7 = 31', '→', 'x =', BOX, size=52))
nb(t, 'İki ədədin cəmi 64-dür. Biri digərindən 12 çoxdur. Kiçik ədədi tapın.', 26, FX('x + (x + 12) = 64', '→', BOX, size=50))
nb(t, 'Ata oğlundan 3 dəfə böyükdür. Onların yaşlarının cəmi 48-dir. Oğul neçə yaşındadır?', 12, story(['👨', '👦'], ['x + 3x = 48', '→', BOX], size=70))
nb(t, 'Düzbucaqlının uzunluğu enindən 2 dəfə çoxdur. Perimetri 36 sm-dir. Enini tapın.', 6, vstack([rect_sides(6, 3, '2x', 'x', 30), FX('x', '=', BOX, 'sm', size=48)], 10))
nb(t, 'Kitab 3 günə oxundu. Hər gün əvvəlki gündən 10 səhifə çox oxundu. Kitab 90 səhifədir. Birinci gün neçə səhifə oxundu?', 20, story(['📖'], ['x + (x + 10) + (x + 20) = 90'], size=60))
nb(t, 'Üç ardıcıl cüt ədədin cəmi 54-dür. Ən kiçiyini tapın.', 16, q('x + (x + 2) + (x + 4) = 54', FX('x', '=', BOX, size=54), size=44))
t.choice('Lalənin x kitabı var, Aynurun kitabları ondan 2 dəfə çoxdur. Birlikdə 18 kitabları var. Uyğun tənliyə toxunun.', ['x + 2x = 18', '2x = 18', 'x + 2 = 18'], 0, stem=story(['👧', '👧', '📚']))
nb(t, 'Lalənin x kitabı var, Aynurun kitabları ondan 2 dəfə çoxdur. Birlikdə 18 kitabları var. Lalənin neçə kitabı var?', 6, FX('x + 2x = 18', '→', 'x =', BOX, size=52))
nb(t, 'Velosipedçi 3 saat x km/saat, sonra 2 saat (x + 2) km/saat sürətlə getdi. Cəmi 64 km yol getdi. x-i tapın.', 12, FX('3x + 2(x + 2) = 64', '→', BOX, size=46))
nb(t, 'Sinifdə qızlar oğlanlardan 4 nəfər çoxdur. Cəmi 28 şagird var. Neçə oğlan var?', 12, story(['👧', '👦'], ['x + (x + 4) = 28', '→', BOX], size=64))

# ============================================================ 275
t = T(275, 'Bərabərsizliklər',
      'Bərabərsizliyi tənlik kimi həll edirik: x + 5 > 9, x > 4. Həllər 4-dən böyük ədədlərdir, ən kiçik tam həll 5-dir. −3 < x < 2 bərabərsizliyinin tam həlləri: −2, −1, 0, 1.',
      q('x + 5 > 9', 'x > 4', zline(-1, 8, [(5, ''), (6, ''), (7, '')])))
BH = 'Bərabərsizliyin istənilən həllini yazın.'
zans(t, 'x + 5 > 9 bərabərsizliyinin ən kiçik tam həllini yazın.', 5, q('x + 5 > 9', box(100, 86)))
zans(t, '2x ≤ 14 bərabərsizliyinin ən böyük tam həllini yazın.', 7, q('2x ≤ 14', box(100, 86)))
zans(t, '3x − 1 < 11 bərabərsizliyinin ən böyük tam həllini yazın.', 3, q('3x − 1 < 11', box(100, 86)))
zans(t, '−3 < x < 2 bərabərsizliyinin neçə tam həlli var?', 4, q('−3 < x < 2', box(100, 86)))
t.choice('x ≥ −1 bərabərsizliyinin həllərinin hamısına toxunun.', ['−3', '−1', '0', '2', '−2'], [1, 2, 3], mode='multi')
t.choice('x > 3 bərabərsizliyinin həlləri ədəd oxunda haradadır? Toxunun.', ['3-dən sağda (3 daxil deyil)', '3-dən solda', '3 daxil olmaqla sağda'], 0)
zans(t, 'x − 4 ≥ −6 bərabərsizliyinin ən kiçik tam həllini yazın.', -2, q('x − 4 ≥ −6', box(100, 86)))
zans(t, '5x > 20 bərabərsizliyinin ən kiçik tam həllini yazın.', 5, q('5x > 20', box(100, 86)))
t.choice('Hansı ədəd 2x + 1 > 7 bərabərsizliyinin həllidir? Toxunun.', ['2', '3', '4'], 2)
zans(t, 'Səbətdə 6 kq-dan az alma var. Almanın kütləsi tam kiloqramdırsa, ən çox neçə kiloqram ola bilər?', 5, story(['🧺', '🍎'], ['x < 6', '→', BOX, 'kq'], size=70))

# ============================================================ 276
t = T(276, 'Üçbucağın medianı, tənböləni və hündürlüyü',
      'Üçbucağın təpəsini qarşı tərəfin orta nöqtəsi ilə birləşdirən parça median, təpədəki bucağı yarıya bölən parça tənbölən, təpədən qarşı tərəfə çəkilən perpendikulyar hündürlükdür. Hər üçbucağın 3 medianı, 3 tənböləni, 3 hündürlüyü var.',
      hstack([tri_el('median', 150), tri_el('bisector', 150), tri_el('height', 150)], 6))
OPTS = [tri_el('median', 130), tri_el('bisector', 130), tri_el('height', 130)]
t.choice('AM parçası median olan şəklə toxunun.', OPTS, 0)
t.choice('AM parçası hündürlük olan şəklə toxunun.', OPTS, 2)
t.choice('AM parçası tənbölən olan şəklə toxunun.', OPTS, 1)
nb(t, 'AM medianıdır, BC = 12 sm. BM parçasının uzunluğunu tapın.', 6, q(tri_el('median', 170), FX('BM', '=', BOX, 'sm', size=48)))
nb(t, 'AM tənböləndir, A bucağı 70°-dir. BAM bucağı neçə dərəcədir?', 35, q(tri_el('bisector', 170), FX('∠BAM', '=', BOX, '°', size=48)))
nb(t, 'AM hündürlükdür. AMB bucağı neçə dərəcədir?', 90, q(tri_el('height', 170), FX('∠AMB', '=', BOX, '°', size=48)))
nb(t, 'Üçbucağın neçə medianı var?', 3, q(tri_el('median', 150), box(100, 80)))
nb(t, 'AM medianıdır, BM = 7 sm. BC tərəfinin uzunluğunu tapın.', 14, q(tri_el('median', 170), FX('BC', '=', BOX, 'sm', size=48)))
t.choice('Median təpəni qarşı tərəfin hansı nöqtəsi ilə birləşdirir? Toxunun.', ['orta nöqtəsi', 'istənilən nöqtəsi', 'təpəsi'], 0)
nb(t, 'AM tənböləndir, BAM bucağı 25°-dir. BAC bucağı neçə dərəcədir?', 50, q(tri_el('bisector', 170), FX('∠BAC', '=', BOX, '°', size=48)))

# ============================================================ 277
t = T(277, 'Üçbucaqların konqruyentlik əlamətləri',
      'İki üçbucaq konqruyentdir, əgər: iki tərəfi və onların arasındakı bucaq bərabərdirsə (TBT); bir tərəfi və ona bitişik iki bucağı bərabərdirsə (BTB); üç tərəfi bərabərdirsə (TTT). Konqruyent üçbucaqların uyğun tərəfləri və bucaqları bərabərdir.',
      q('TBT,  BTB,  TTT', hstack([tri([(0.4, 0.05), (0, 0.9), (1, 0.9)], ('5', '7', '6'), 130), tri([(0.4, 0.05), (0, 0.9), (1, 0.9)], ('5', '7', '6'), 130)], 10)))
ALM = ['TBT', 'BTB', 'TTT']
t.choice('İki üçbucağın iki tərəfi və onların arasındakı bucaq bərabərdir. Bu hansı əlamətdir? Toxunun.', ALM, 0)
t.choice('İki üçbucağın bir tərəfi və ona bitişik iki bucağı bərabərdir. Bu hansı əlamətdir? Toxunun.', ALM, 1)
t.choice('İki üçbucağın üç tərəfi bərabərdir. Bu hansı əlamətdir? Toxunun.', ALM, 2)
TT = tri([(0.4, 0.05), (0, 0.9), (1, 0.9)], ('AB = 5', 'BC = 7', 'AC = 6'), 170)
nb(t, 'ABC və DEF üçbucaqları konqruyentdir: AB = 5 sm, BC = 7 sm, AC = 6 sm. DE tərəfinin uzunluğunu tapın.', 5, q(TT, FX('DE', '=', BOX, 'sm', size=48)))
nb(t, 'ABC və DEF üçbucaqları konqruyentdir: AB = 5 sm, BC = 7 sm, AC = 6 sm. EF tərəfinin uzunluğunu tapın.', 7, q(TT, FX('EF', '=', BOX, 'sm', size=48)))
nb(t, 'ABC və DEF üçbucaqları konqruyentdir, A bucağı 40°-dir. D bucağı neçə dərəcədir?', 40, FX('∠D', '=', BOX, '°', size=56))
t.choice('Konqruyent üçbucaqların perimetrləri haqqında doğru cümləyə toxunun.', ['bərabərdir', 'fərqlidir'], 0)
nb(t, 'ABC və KLM üçbucaqları konqruyentdir. ABC üçbucağının perimetri 24 sm-dir. KLM üçbucağının perimetrini tapın.', 24, FX('P', '=', BOX, 'sm', size=56))
nb(t, 'Kvadratın diaqonalı onu neçə konqruyent üçbucağa bölür?', 2, poly_l([(0, 0), (5, 0), (5, 5), (0, 5)], [], 34, extra=[([(0, 0), (5, 5), (0, 5)], (255, 224, 178))]))
t.choice('Üç bucağı bərabər olan iki üçbucaq mütləq konqruyentdirmi? Toxunun.', ['Bəli', 'Xeyr'], 1)

# ============================================================ 278
t = T(278, 'Düz xətlərin paralelliyi',
      'İki paralel düz xətti üçüncü düz xətt kəsəndə uyğun bucaqlar bərabər olur (∠1 = ∠5), daxili çarpaz bucaqlar bərabər olur (∠3 = ∠5), birtərəfli daxili bucaqların cəmi 180° olur (∠4 + ∠5 = 180°).',
      trans(65, {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8'}))
PB = 'a və b düz xətləri paraleldir. Sual işarəsi olan bucağı tapın.'
for deg_, labs, v in [(65, {1: '65°', 5: '?'}, 65), (70, {3: '70°', 5: '?'}, 70), (70, {4: '110°', 5: '?'}, 70), (60, {1: '60°', 2: '?'}, 120), (125, {2: '55°', 4: '?'}, 55), (132, {6: '48°', 8: '?'}, 48), (75, {1: '75°', 7: '?'}, 75)]:
    nb(t, PB, v, trans(deg_, labs), suf='°')
t.choice('Paralel xətlərdə daxili çarpaz bucaqlar haqqında doğru cümləyə toxunun.', ['bərabərdir', 'cəmi 180°-dir'], 0)
t.choice('Paralel xətlərdə birtərəfli daxili bucaqların cəmi neçə dərəcədir? Toxunun.', ['90°', '180°', '360°'], 1)
t.choice('a və b düz xətlərinin paralel olması üçün 1-ci və 5-ci bucaqlar necə olmalıdır? Toxunun.', ['bərabər', 'cəmi 90°'], 0, stem=trans(65, {1: '1', 5: '5'}))

# ============================================================ 279
t = T(279, 'Üçbucağın bucaqlarının cəmi',
      'Hər üçbucağın bucaqlarının cəmi 180°-dir. İki bucaq 50° və 60°-dirsə, üçüncü bucaq 180° − 50° − 60° = 70°-dir. Bərabərtərəfli üçbucağın hər bucağı 60°-dir.',
      q(tri([(0.4, 0.05), (0, 0.9), (1, 0.9)], size=150), '50° + 60° + 70° = 180°', size=50))
TB = 'Üçbucağın üçüncü bucağını tapın.'
for a_, b_ in [(50, 60), (90, 35), (100, 45)]:
    nb(t, TB, 180 - a_ - b_, q(txt('%d°,  %d°,  ?' % (a_, b_), 60, INK), FX('?', '=', BOX, '°', size=52)))
nb(t, 'Bərabərtərəfli üçbucağın hər bucağı neçə dərəcədir?', 60, tri([(0.5, 0.05), (1, 0.92), (0, 0.92)], size=150), suf='°')
nb(t, 'Bərabəryanlı üçbucağın təpə bucağı 40°-dir. Oturacağa bitişik bucağı tapın.', 70, tri([(0.5, 0), (0.8, 0.95), (0.2, 0.95)], size=160), suf='°')
nb(t, 'Bərabəryanlı üçbucağın oturacağa bitişik bucağı 65°-dir. Təpə bucağını tapın.', 50, tri([(0.5, 0.1), (0.95, 0.95), (0.05, 0.95)], size=160), suf='°')
nb(t, 'Düzbucaqlı üçbucağın iti bucaqlarından biri 28°-dir. Digər iti bucağı tapın.', 62, tri([(0.1, 0.05), (0.1, 0.9), (0.95, 0.9)], size=160, right=1), suf='°')
nb(t, 'Üçbucağın bucaqları x, 2x və 6x-dir. Ən böyük bucağı tapın.', 120, FX('x + 2x + 6x = 180°', size=54), suf='°')
nb(t, 'Üçbucağın daxili bucağı 70°-dir. Ona qonşu olan xarici bucağı tapın.', 110, adj(70, '70°', '?'), suf='°')
t.choice('Üçbucaqda iki kor bucaq ola bilərmi? Toxunun.', ['Bəli', 'Xeyr'], 1)

# ============================================================ 280
t = T(280, 'Üç tərəfinə görə üçbucağın qurulması',
      'Üçbucağın hər tərəfi digər iki tərəfin cəmindən kiçikdir. Ona görə 3, 4, 8 sm-lik parçalardan üçbucaq qurmaq olmaz (3 + 4 < 8), 5, 6, 10 sm-lik parçalardan isə olar. Üçbucağı pərgar və xətkeşlə qururuq.',
      q('5 + 6 > 10  ✓', '3 + 4 < 8  ✗', size=56))
t.choice('Hansı parçalardan üçbucaq qurmaq olar? Toxunun.', ['3, 4 və 8 sm', '5, 6 və 10 sm', '2, 2 və 5 sm'], 1)
t.choice('Hansı parçalardan üçbucaq qurmaq olar? Toxunun.', ['1, 1 və 3 sm', '7, 3 və 4 sm', '4, 5 və 6 sm'], 2)
nb(t, 'Üçbucağın iki tərəfi 5 sm və 9 sm-dir. Üçüncü tərəf tam ədəddir. Onun ola biləcək ən kiçik qiymətini yazın.', 5, q('9 − 5 < x < 9 + 5', box(100, 86), size=50), suf='sm')
nb(t, 'Üçbucağın iki tərəfi 5 sm və 9 sm-dir. Üçüncü tərəf tam ədəddir. Onun ola biləcək ən böyük qiymətini yazın.', 13, q('9 − 5 < x < 9 + 5', box(100, 86), size=50), suf='sm')
nb(t, 'Tərəfləri 6 sm, 8 sm və 9 sm olan üçbucağın perimetrini tapın.', 23, tri([(0.3, 0.05), (0, 0.9), (1, 0.9)], ('6 sm', '9 sm', '8 sm'), 170), suf='sm')
nb(t, 'Bərabəryanlı üçbucağın oturacağı 10 sm, yan tərəfi 8 sm-dir. Perimetrini tapın.', 26, tri([(0.5, 0.05), (1, 0.9), (0, 0.9)], ('8 sm', '10 sm', '8 sm'), 170), suf='sm')
t.choice('Bərabəryanlı üçbucağın yan tərəfləri 3 sm-dir. Oturacaq hansı ola bilər? Toxunun.', ['5 sm', '7 sm', '6 sm'], 0)
nb(t, 'Bərabərtərəfli üçbucağın perimetri 36 sm-dir. Tərəfini tapın.', 12, tri([(0.5, 0.05), (1, 0.92), (0, 0.92)], ('?', '?', '?'), 150), suf='sm')
t.choice('Üçbucağı üç tərəfinə görə qurmaq üçün hansı alətlər lazımdır? Toxunun.', ['pərgar və xətkeş', 'yalnız transportir'], 0)
nb(t, 'Bərabəryanlı üçbucağın yan tərəfləri 7 sm-dir. Oturacaq tam ədəddir. Onun ola biləcək ən böyük qiymətini yazın.', 13, q('x < 7 + 7', box(100, 86), size=54), suf='sm')

# ============================================================ 281
t = T(281, 'Üçbucağın sahəsi',
      'Üçbucağın sahəsi oturacağı ilə hündürlüyü hasilinin yarısına bərabərdir: S = a · h : 2. Oturacağı 10 sm, hündürlüyü 6 sm olan üçbucağın sahəsi 30 sm²-dir.',
      q(tri_h('a', 'h'), 'S = a · h : 2'))
ST = 'Üçbucağın sahəsini tapın.'
for a_, h_ in [(10, 6), (8, 5), (12, 7), (9, 4), (15, 4)]:
    nb(t, ST, a_ * h_ // 2, q(tri_h('%d sm' % a_, '%d sm' % h_, 26 if a_ > 10 else 30), FX('S', '=', BOX, size=46)), suf='sm²')
nb(t, 'Üçbucağın sahəsi 24 sm², oturacağı 8 sm-dir. Hündürlüyünü tapın.', 6, q(tri_h('8 sm', '?'), txt('S = 24 sm²', 46, INK)), suf='sm')
nb(t, 'Üçbucağın sahəsi 35 sm², hündürlüyü 7 sm-dir. Oturacağını tapın.', 10, q(tri_h('?', '7 sm'), txt('S = 35 sm²', 46, INK)), suf='sm')
nb(t, 'Katetləri 6 sm və 9 sm olan düzbucaqlı üçbucağın sahəsini tapın.', 27, rtri(9, 6, '9 sm', '6 sm', 26), suf='sm²')
danswer(t, ST, Dm('17.5'), q(tri_h('7 sm', '5 sm'), DEC('S', '=', 'BOX2', 'sm²', size=46)))
t.choice('Üçbucağın sahəsinin düsturuna toxunun.', ['S = a · h : 2', 'S = a · h', 'S = a + h'], 0)

# ============================================================ 282
t = T(282, 'Paraleloqram və rombun sahəsi',
      'Paraleloqramın sahəsi oturacağı ilə hündürlüyünün hasilinə bərabərdir: S = a · h. Rombun sahəsi diaqonallarının hasilinin yarısına bərabərdir: S = d₁ · d₂ : 2.',
      hstack([para('a', 'h', 24), rhomb('d₁', 'd₂', 22)], 20))
nb(t, 'Paraleloqramın sahəsini tapın.', 40, q(para('8 sm', '5 sm'), FX('S', '=', BOX, size=46)), suf='sm²')
nb(t, 'Paraleloqramın sahəsini tapın.', 72, q(para('12 sm', '6 sm', 24), FX('S', '=', BOX, size=46)), suf='sm²')
nb(t, 'Paraleloqramın sahəsi 48 sm², oturacağı 8 sm-dir. Hündürlüyünü tapın.', 6, q(para('8 sm', '?'), txt('S = 48 sm²', 46, INK)), suf='sm')
nb(t, 'Rombun diaqonalları 8 sm və 6 sm-dir. Sahəsini tapın.', 24, rhomb('8 sm', '6 sm'), suf='sm²')
nb(t, 'Rombun diaqonalları 12 sm və 10 sm-dir. Sahəsini tapın.', 60, rhomb('12 sm', '10 sm'), suf='sm²')
nb(t, 'Rombun tərəfi 7 sm, hündürlüyü 5 sm-dir. Sahəsini tapın.', 35, para('7 sm', '5 sm', 30, 7, 5, 2.5), suf='sm²')
t.choice('Rombun sahəsinin düsturuna toxunun.', ['S = d₁ · d₂ : 2', 'S = d₁ · d₂', 'S = d₁ + d₂'], 0)
nb(t, 'Paraleloqramın sahəsini tapın.', 36, q(para('9 sm', '4 sm'), FX('S', '=', BOX, size=46)), suf='sm²')
nb(t, 'Rombun perimetri 28 sm-dir. Tərəfini tapın.', 7, rhomb('', ''), suf='sm')
nb(t, 'Paraleloqramın qonşu tərəfləri 5 sm və 7 sm-dir. Perimetrini tapın.', 24, para('7 sm', '', 30, 7, 4, 2), suf='sm')

# ============================================================ 283
t = T(283, 'Çevrənin uzunluğu. Dairənin sahəsi',
      'Çevrənin uzunluğu C = 2πr, dairənin sahəsi S = πr² düsturu ilə tapılır. π ədədi təqribən 3,14-ə bərabərdir. Radiusu 5 sm olan çevrənin uzunluğu 2 · 3,14 · 5 = 31,4 sm-dir.',
      hstack([circ('r'), q('C = 2πr', 'S = πr²', 'π ≈ 3,14')], 20))
C_ = 'Çevrənin uzunluğunu tapın (π ≈ 3,14).'
S_ = 'Dairənin sahəsini tapın (π ≈ 3,14).'
danswer(t, C_, 2 * PI * 5, q(circ('r = 5 sm'), DEC('C', '=', 'BOX2', 'sm', size=46)))
danswer(t, C_, PI * 20, q(circ('d = 20 sm', 'd'), DEC('C', '=', 'BOX2', 'sm', size=46)))
danswer(t, S_, PI * 100, q(circ('r = 10 sm'), DEC('S', '=', BOX, 'sm²', size=46)))
danswer(t, S_, PI * 4, q(circ('r = 2 sm'), DEC('S', '=', 'BOX2', 'sm²', size=46)))
danswer(t, C_, 2 * PI * 3, q(circ('r = 3 sm'), DEC('C', '=', 'BOX2', 'sm', size=46)))
nb(t, 'Çevrənin uzunluğu 6,28 sm-dir. Radiusunu tapın (π ≈ 3,14).', 1, q(circ('r = ?'), txt('C = 6,28 sm', 46, INK)), suf='sm')
nb(t, 'Dairənin diametri 8 sm-dir. Radiusunu tapın.', 4, circ('d = 8 sm', 'd'), suf='sm')
danswer(t, S_, PI, q(circ('r = 1 sm'), DEC('S', '=', 'BOX2', 'sm²', size=46)))
t.choice('Çevrənin uzunluğunun düsturuna toxunun.', ['C = 2πr', 'C = πr²', 'C = 2r'], 0)
t.choice('Dairənin sahəsinin düsturuna toxunun.', ['S = πr²', 'S = 2πr', 'S = πd'], 0)

# ============================================================ 284
t = T(284, 'Düzbucaqlı prizma və silindrin səthinin sahəsi',
      'Prizmanın yan səthinin sahəsi oturacağın perimetri ilə hündürlüyün hasilinə bərabərdir. Silindrin yan səthi açılanda düzbucaqlı alınır: S yan = 2πrh. Tam səth = yan səth + iki oturacağın sahəsi: S = 2πr(r + h).',
      hstack([box3d(4, 3, 3, 26, labels=('a', 'b', 'h')), cyl('r', 'h', 130, 150, 26)], 20))
nb(t, 'Düzbucaqlı prizmanın səthinin sahəsini tapın.', 88, q(box3d(6, 4, 2, 30, labels=('6 sm', '4 sm', '2 sm')), FX('S', '=', BOX, 'sm²', size=44)))
nb(t, 'Tili 6 sm olan kubun səthinin sahəsini tapın.', 216, q(box3d(3, 3, 3, 34, labels=('6 sm',) * 3), FX('S', '=', BOX, 'sm²', size=44)))
danswer(t, 'Silindrin yan səthinin sahəsini tapın (π ≈ 3,14).', 2 * PI * 2 * 5, q(cyl('2 sm', '5 sm'), DEC('S', '=', 'BOX2', 'sm²', size=44)))
danswer(t, 'Silindrin tam səthinin sahəsini tapın (π ≈ 3,14).', 2 * PI * 1 * 5, q(cyl('1 sm', '4 sm'), DEC('S', '=', 'BOX2', 'sm²', size=44)))
danswer(t, 'Silindrin yan səthinin sahəsini tapın (π ≈ 3,14).', 2 * PI * 3 * 10, q(cyl('3 sm', '10 sm'), DEC('S', '=', 'BOX2', 'sm²', size=44)))
nb(t, 'Prizmanın oturacağı tərəfləri 3 sm və 4 sm olan düzbucaqlıdır, hündürlüyü 10 sm-dir. Yan səthin sahəsini tapın.', 140, q(box3d(4, 3, 7, 22, labels=('4 sm', '3 sm', '10 sm')), FX('(3 + 4) · 2 · 10', '=', BOX, size=40)), suf='sm²')
t.choice('Silindrin yan səthi açılanda hansı fiqur alınır? Toxunun.', ['düzbucaqlı', 'dairə', 'üçbucaq'], 0, stem=cyl('', ''))
nb(t, 'Silindrin neçə oturacağı var?', 2, q(cyl('', ''), box(100, 80)))
danswer(t, 'Silindrin tam səthinin sahəsini tapın (π ≈ 3,14).', 2 * PI * 5 * 7, q(cyl('5 sm', '2 sm', 200, 90, 30), DEC('S', '=', 'BOX2', 'sm²', size=44)))
nb(t, 'Prizmanın oturacağı tərəfi 5 sm olan kvadrat, hündürlüyü 8 sm-dir. Tam səthin sahəsini tapın.', 210, q(box3d(3, 3, 5, 26, labels=('5 sm', '5 sm', '8 sm')), FX('S', '=', BOX, 'sm²', size=44)))

# ============================================================ 285
t = T(285, 'Düzbucaqlı prizma və silindrin həcmi',
      'Prizmanın və silindrin həcmi oturacağın sahəsi ilə hündürlüyün hasilinə bərabərdir: V = S · h. Silindrin həcmi V = πr²h. Radiusu 2 sm, hündürlüyü 10 sm olan silindrin həcmi 3,14 · 4 · 10 = 125,6 sm³-dir.',
      hstack([box3d(4, 3, 3, 26, labels=('a', 'b', 'h')), cyl('r', 'h', 130, 150, 26), q('V = S · h', 'V = πr²h', size=44)], 16))
nb(t, 'Prizmanın həcmini tapın.', 120, q(box3d(6, 5, 4, 28, labels=('6 sm', '5 sm', '4 sm')), FX('V', '=', BOX, 'sm³', size=44)))
VC = 'Silindrin həcmini tapın (π ≈ 3,14).'
danswer(t, VC, PI * 4 * 10, q(cyl('2 sm', '10 sm'), DEC('V', '=', 'BOX2', 'sm³', size=44)))
danswer(t, VC, PI * 1 * 5, q(cyl('1 sm', '5 sm'), DEC('V', '=', 'BOX2', 'sm³', size=44)))
danswer(t, VC, PI * 100 * 3, q(cyl('10 sm', '3 sm', 220, 80, 30), DEC('V', '=', BOX, 'sm³', size=44)))
nb(t, 'Tili 5 sm olan kubun həcmini tapın.', 125, q(box3d(3, 3, 3, 34, labels=('5 sm',) * 3), FX('V', '=', BOX, 'sm³', size=44)))
nb(t, 'Prizmanın oturacağının sahəsi 12 sm², hündürlüyü 7 sm-dir. Həcmini tapın.', 84, FX('V', '=', '12 · 7', '=', BOX, 'sm³', size=50))
nb(t, 'Prizmanın həcmi 200 sm³, oturacağının tərəfləri 10 sm və 5 sm-dir. Hündürlüyünü tapın.', 4, q(box3d(6, 4, 3, 26, labels=('10 sm', '5 sm', '?')), FX('h', '=', BOX, 'sm', size=44)))
danswer(t, 'Silindr şəkilli qabın radiusu 10 sm, hündürlüyü 20 sm-dir. Ona neçə litr su tutar (π ≈ 3,14)?', PI * 100 * 20 / 1000, q(cyl('10 sm', '20 sm'), DEC('V', '=', 'BOX2', 'l', size=44)))
t.choice('Silindrin həcminin düsturuna toxunun.', ['V = πr²h', 'V = 2πrh', 'V = πrh'], 0)
nb(t, 'Prizmanın oturacağı katetləri 6 sm və 4 sm olan düzbucaqlı üçbucaq, hündürlüyü 10 sm-dir. Həcmini tapın.', 120, q(prism3('6 sm', '4 sm', '10 sm'), FX('V', '=', BOX, 'sm³', size=44)))

# ============================================================ 286
t = T(286, 'Median və moda',
      'Sıraya düzülmüş ədədlərin ortasındakı ədəd mediandır: 2, 4, 6, 7, 9 sırasının medianı 6-dır. Ədədlər cüt saydadırsa, median ortadakı iki ədədin ədədi ortasıdır. Ən çox təkrarlanan ədəd modadır.',
      q('2, 4, 6, 7, 9 → median 6', '3, 5, 5, 7 → moda 5', size=48))
MD = lambda ns: hstack([nchip(v) for v in ns], 10)
nb(t, 'Ədədlər sırasının modasını tapın.', 5, q(MD((3, 5, 5, 7, 8)), FX('Moda', '=', BOX, size=48)))
nb(t, 'Ədədlər sırasının medianını tapın. Əvvəlcə ədədləri sıraya düzün.', 6, q(MD((2, 4, 9, 6, 7)), FX('Median', '=', BOX, size=48)))
danswer(t, 'Ədədlər sırasının medianını tapın.', Dm('6.5'), q(MD((3, 5, 8, 10)), DEC('Median', '=', 'BOX2', size=48)))
nb(t, 'Ədədlər sırasının modasını tapın.', 3, q(MD((1, 2, 2, 3, 3, 3, 4)), FX('Moda', '=', BOX, size=48)))
nb(t, 'Şagirdin qiymətləri: 5, 4, 5, 3, 5, 4. Modanı tapın.', 5, q(MD((5, 4, 5, 3, 5, 4)), FX('Moda', '=', BOX, size=48)))
danswer(t, 'Şagirdin qiymətləri: 5, 4, 5, 3, 5, 4. Medianı tapın.', Dm('4.5'), q(MD((5, 4, 5, 3, 5, 4)), DEC('Median', '=', 'BOX2', size=48)))
nb(t, 'Ədədlərin ədədi ortasını tapın.', 8, q(MD((4, 6, 8, 10, 12)), FX('Orta', '=', BOX, size=48)))
nb(t, 'Satılan ayaqqabıların ölçüləri: 36, 37, 37, 38, 37, 39. Modanı tapın.', 37, q(MD((36, 37, 37, 38, 37, 39)), FX('Moda', '=', BOX, size=48)))
t.choice('Mağaza ən çox satılan ölçünü bilmək istəyir. Hansı göstərici lazımdır? Toxunun.', ['moda', 'median', 'ədədi orta'], 0)
nb(t, 'Ədədlər sırasının medianını tapın.', 40, q(MD((10, 20, 30, 40, 50, 60, 70)), FX('Median', '=', BOX, size=48)))

# ============================================================ 287
t = T(287, 'Təsadüfi hadisə',
      'Mütləq baş verən hadisə yəqin hadisədir, heç vaxt baş verməyən hadisə mümkün olmayan hadisədir, baş verə də bilən, verməyə də bilən hadisə təsadüfi hadisədir. Zəri atanda 1-dən 6-ya qədər 6 nəticə mümkündür.',
      hstack([die(3, 100), die(5, 100), em('🪙', 100)], 20))
HK = ['mümkün olmayan', 'yəqin', 'təsadüfi']
t.choice('Zəri atanda 7 düşməsi hansı hadisədir? Toxunun.', HK, 0, stem=die(6, 100))
t.choice('Zəri atanda 1-dən 6-ya qədər ədəd düşməsi hansı hadisədir? Toxunun.', HK, 1, stem=die(4, 100))
t.choice('Sikkəni atanda gerb düşməsi hansı hadisədir? Toxunun.', HK, 2, stem=em('🪙', 100))
t.choice('Yanvarda Bakıda qar yağması hansı hadisədir? Toxunun.', HK, 2, stem=em('🌨️', 100))
t.choice('Torbada yalnız qırmızı kürələr var. Torbadan göy kürə çıxarmaq hansı hadisədir? Toxunun.', HK, 0, stem=hstack([em('🔴', 60)] * 4, 6))
nb(t, 'Zəri atanda neçə nəticə mümkündür?', 6, q(die(2, 100), box(100, 80)))
nb(t, 'Sikkəni atanda neçə nəticə mümkündür?', 2, q(em('🪙', 100), box(100, 80)))
nb(t, 'Zəri atanda cüt ədəd düşməsi üçün neçə nəticə əlverişlidir?', 3, q(hstack([die(2, 70), die(4, 70), die(6, 70)], 10), box(100, 80)))
nb(t, 'Torbada 3 qırmızı, 5 göy və 2 yaşıl kürə var. Bir kürə çıxarılır. Neçə nəticə mümkündür?', 10, hstack([em('🔴', 44)] * 3 + [em('🔵', 44)] * 5 + [em('🟢', 44)] * 2, 4))
t.choice('Torbada 3 qırmızı və 7 göy kürə var. Hansı hadisə daha çox gözlənilir? Toxunun.', ['qırmızı kürə çıxması', 'göy kürə çıxması'], 1, stem=hstack([em('🔴', 44)] * 3 + [em('🔵', 44)] * 7, 4))

# ============================================================ 288
t = T(288, 'Hadisənin ehtimalı',
      'Hadisənin ehtimalı əlverişli nəticələrin sayının bütün mümkün nəticələrin sayına nisbətidir. Zəri atanda 3 düşməsinin ehtimalı 1/6, cüt ədəd düşməsinin ehtimalı 3/6 = 1/2-dir. Mümkün olmayan hadisənin ehtimalı 0, yəqin hadisənin ehtimalı 1-dir.',
      q(hstack([txt('P =', 56, INK), fr('əlverişli', 'bütün', 40)], 10), FX('P(3)', '=', (1, 6), size=50)))
EH = 'Hadisənin ehtimalını tapın. Kəsri ixtisar edin.'
BAG = hstack([em('🔴', 44)] * 3 + [em('🔵', 44)] * 5 + [em('🟢', 44)] * 2, 4)
for ins, v, stem in [('Zəri atanda 3 düşməsinin ehtimalını tapın.', Fr(1, 6), die(3, 100)),
                     ('Zəri atanda cüt ədəd düşməsinin ehtimalını tapın. Kəsri ixtisar edin.', Fr(1, 2), hstack([die(2, 70), die(4, 70), die(6, 70)], 10)),
                     ('Zəri atanda 4-dən böyük olmayan ədəd düşməsinin ehtimalını tapın. Kəsri ixtisar edin.', Fr(2, 3), hstack([die(k, 56) for k in (1, 2, 3, 4)], 8)),
                     ('Torbada 3 qırmızı, 5 göy və 2 yaşıl kürə var. Qırmızı kürə çıxmasının ehtimalını tapın.', Fr(3, 10), BAG),
                     ('Torbada 3 qırmızı, 5 göy və 2 yaşıl kürə var. Göy kürə çıxmasının ehtimalını tapın. Kəsri ixtisar edin.', Fr(1, 2), BAG),
                     ('Torbada 3 qırmızı, 5 göy və 2 yaşıl kürə var. Yaşıl kürə çıxmasının ehtimalını tapın. Kəsri ixtisar edin.', Fr(1, 5), BAG),
                     ('1-dən 20-yə qədər nömrələnmiş kartlardan biri çəkilir. 3-ə bölünən ədəd çıxmasının ehtimalını tapın. Kəsri ixtisar edin.', Fr(3, 10), q('1, 2, 3, ..., 20', size=50))]:
    fanswer(t, ins, v, vstack([stem, FX('P', '=', (BOX, BOX), size=46)], 12))
nb(t, 'Mümkün olmayan hadisənin ehtimalı neçədir?', 0, FX('P', '=', BOX, size=60))
nb(t, 'Yəqin hadisənin ehtimalı neçədir?', 1, FX('P', '=', BOX, size=60))
t.choice('Hansı hadisənin ehtimalı böyükdür? Toxunun.', ['zəri atanda 6 düşməsi', 'sikkəni atanda gerb düşməsi'], 1)

# ============================================================ 289
t = T(289, 'Məlumatların təsviri',
      'Toplanmış məlumatları tezlik cədvəli, sütunlu, xətti və dairəvi diaqramlarla təsvir edirik. Tezlik cədvəlində hər qiymətin neçə dəfə təkrarlandığı yazılır. Cədvəldən moda, median və ədədi ortanı tapmaq olar.',
      tab([['Qiymət', '2', '3', '4', '5'], ['Şagird', '1', '6', '10', '8']], 36))
FT = tab([['Qiymət', '2', '3', '4', '5'], ['Şagird', '1', '6', '10', '8']], 36)
nb(t, 'Tezlik cədvəlinə görə neçə şagird «4» alıb?', 10, FT)
nb(t, 'Tezlik cədvəlinə görə cəmi neçə şagird var?', 25, FT)
nb(t, 'Tezlik cədvəlinə görə qiymətlərin modası neçədir?', 4, FT)
BR = bars([(txt(d_, 24), v) for d_, v in [('5A', 6), ('5B', 9), ('6A', 4), ('6B', 8)]], 10, 24, 60)
nb(t, 'Diaqramda siniflərdən neçə şagirdin olimpiadaya qatıldığı göstərilib. 6B sinfindən neçə şagird qatılıb?', 8, BR)
nb(t, 'Diaqrama görə 5B sinfindən 6A sinfindən neçə şagird çox qatılıb?', 5, BR)
nb(t, 'Sinifdə 50 şagird var. Diaqrama görə neçə şagird basketbolu seçib?', 20, hstack([pie([(0.4, (255, 167, 38), '40%'), (0.6, (66, 165, 245), '60%')], 200), legend([((255, 167, 38), 'Basketbol'), ((66, 165, 245), 'Voleybol')], 28)], 16))
t.choice('Xətti diaqrama görə temperatur ən çox hansı ayda olub? Toxunun.', ['May', 'İyun', 'İyul'], 2, stem=line_chart(['May', 'İyun', 'İyul', 'Avq'], [18, 24, 28, 26], 30, 5, 520, 280, RED))
t.choice('Bütövün hissələrini göstərmək üçün hansı diaqram daha uyğundur? Toxunun.', ['dairəvi diaqram', 'xətti diaqram', 'sütunlu diaqram'], 0)
zans(t, 'Dörd gündə temperatur 2°, −1°, 3° və 0° olub. Orta temperaturu tapın.', 1, q(MD(('2', '−1', '3', '0')), FX('Orta', '=', BOX, '°', size=48)))
nb(t, 'Piktoqramda bir kitab şəkli 10 kitabı göstərir. Neçə kitab var?', 50, vstack([hstack([em('📘', 64)] * 5, 8), hstack([em('📘', 36), txt('= 10 kitab', 32, GREY)], 8)], 12))

TOPICS.sort(key=lambda x: x.n)
save()
