"""6-cı sinif riyaziyyat, 1-ci hissə: 23 mövzu (244–266), hər mövzuda 10 tapşırıq.
Run: python3 tools/content61.py [OUTDIR]   (default ~/riyaziyyat/6-1)"""
import math, os, sys
from bookgen import *
init(sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser('~/riyaziyyat/6-1'))
from kit56 import *

CAL = 'Hesablayın.'
WB = 'Boş xanaya uyğun ədədi yazın.'


def q(*lines_, size=58):
    """bir neçə sətirlik şəkil: sətirlər str və ya şəkil"""
    return vstack([txt(l_, size, INK) if isinstance(l_, str) else l_ for l_ in lines_], 14)


def nb(t, ins, v, stem, suf=None):
    t.num(ins, [v], stem)
    if suf:
        ck(t, suf=suf)


# ============================================================ 244
t = T(244, 'Natural ədədin qüvvəti',
      'Eyni vuruqların hasilini qısa yazmaq üçün qüvvətdən istifadə edirik: 2 · 2 · 2 · 2 · 2 = 2⁵. Burada 2 qüvvətin əsası, 5 isə qüvvət üstüdür. 2⁵ = 32.',
      q('2 · 2 · 2 · 2 · 2 = 2⁵ = 32'))
for e_, v in [(pw(2, 5), 32), (pw(3, 4), 81), (pw(10, 5), 100000), (pw(1, 7), 1)]:
    ncalc(t, CAL, [e_], v, size=70)
ncalc(t, CAL, [pw(2, 3) + ' · 5'], 40, size=64)
ncalc(t, CAL, [pw(5, 2) + ' + ' + pw(2, 4)], 41, size=64)
t.num('Qüvvət üstünü tapın. Boş xanaya uyğun ədədi yazın.', [6], hstack([txt('2', 90, INK), vstack([box(56, 56), blank(10, 40)], 0), txt('= 64', 90, INK)], 4, align='top'))
t.choice('Hansı yazılış 3 · 3 · 3 · 3 · 3 hasilinə bərabərdir? Toxunun.', [pw(3, 5), pw(5, 3), '3 · 5'], 0)
ncalc(t, CAL, ['(2 + 1)³'], 27, size=70)
ncalc(t, CAL, [pw(10, 3) + ' − ' + pw(10, 2)], 900, size=64)

# ============================================================ 245
t = T(245, 'Sadə və mürəkkəb ədədlər',
      'Yalnız iki böləni (1 və özü) olan natural ədəd sadə ədəddir: 2, 3, 5, 7, 11. İkidən çox böləni olan ədəd mürəkkəb ədəddir: 4, 6, 9. 1 nə sadə, nə mürəkkəbdir. Mürəkkəb ədədi sadə vuruqlara ayırmaq olar: 60 = 2² · 3 · 5.',
      q('2, 3, 5, 7, 11, 13, ...', '60 = 2² · 3 · 5'))
t.choice('Sadə ədədlərin hamısına toxunun.', ['2', '9', '11', '15', '17', '21'], [0, 2, 4], mode='multi')
t.choice('Mürəkkəb ədədlərin hamısına toxunun.', ['13', '25', '29', '33', '37'], [1, 3], mode='multi')
nb(t, '20-dən kiçik neçə sadə ədəd var?', 8, box(100, 86))
nb(t, 'Ən kiçik sadə ədədi yazın.', 2, box(100, 86))
nb(t, 'Ədəd sadə vuruqlara ayrılıb. Boş xanaya uyğun sadə ədədi yazın.', 5, FX('60 = 2² · 3 ·', BOX, size=60))
nb(t, 'Ədəd sadə vuruqlara ayrılıb. Boş xanaya uyğun sadə ədədi yazın.', 3, FX('84 = 2² ·', BOX, '· 7', size=60))
t.num('Ədəd sadə vuruqlara ayrılıb. Qüvvət üstünü yazın.', [3], hstack([txt('72 = 2', 80, INK), vstack([box(50, 50), blank(10, 36)], 0), txt('· 3²', 80, INK)], 4, align='top'))
t.choice('1 ədədi haqqında doğru cümləyə toxunun.', ['sadədir', 'mürəkkəbdir', 'nə sadə, nə mürəkkəb'], 2)
nb(t, '30 ədədinin neçə müxtəlif sadə böləni var?', 3, q('30 = 2 · 3 · 5', box(100, 86)))
nb(t, 'Ən kiçik ikirəqəmli sadə ədədi yazın.', 11, box(110, 86))

# ============================================================ 246
t = T(246, 'Ən böyük ortaq bölən (ƏBOB)',
      'İki ədədin hər ikisini bölən ən böyük ədəd onların ən böyük ortaq bölənidir. ƏBOB(12, 18) = 6. ƏBOB-u 1 olan ədədlər qarşılıqlı sadə ədədlərdir: 8 və 9.',
      q('12: 1, 2, 3, 4, 6, 12', '18: 1, 2, 3, 6, 9, 18', 'ƏBOB(12, 18) = 6', size=46))
for a_, b_ in [(12, 18), (24, 36), (15, 28), (45, 60), (16, 40), (100, 75)]:
    nb(t, 'Ədədlərin ən böyük ortaq bölənini tapın.', math.gcd(a_, b_), FX('ƏBOB(%d, %d)' % (a_, b_), '=', BOX, size=56))
t.choice('Qarşılıqlı sadə ədədlərə toxunun.', ['8 və 9', '6 və 9', '10 və 15'], 0)
nb(t, '24 alma və 36 armudu bərabər paketlərə qalıqsız yığmaq lazımdır. Ən çox neçə paket olar?', 12, story(['🍎', '🍐', '🛍️'], [BOX, 'paket']))
nb(t, '18 qırmızı və 27 ağ güldən eyni buketlər düzəltmək lazımdır. Ən çox neçə buket olar?', 9, story(['🌹', '🌷', '💐'], [BOX, 'buket']))
nb(t, 'Ədədlərin ən böyük ortaq bölənini tapın.', 7, FX('ƏBOB(14, 21, 35)', '=', BOX, size=56))

# ============================================================ 247
t = T(247, 'Ən kiçik ortaq bölünən (ƏKOB)',
      'İki ədədin hər birinə bölünən ən kiçik natural ədəd onların ən kiçik ortaq bölünənidir. ƏKOB(4, 6) = 12, çünki 12 həm 4-ə, həm də 6-ya bölünür.',
      q('4: 4, 8, 12, 16, ...', '6: 6, 12, 18, ...', 'ƏKOB(4, 6) = 12', size=48))
for a_, b_ in [(4, 6), (6, 8), (5, 7), (12, 18), (9, 15), (8, 16)]:
    nb(t, 'Ədədlərin ən kiçik ortaq bölünənini tapın.', a_ * b_ // math.gcd(a_, b_), FX('ƏKOB(%d, %d)' % (a_, b_), '=', BOX, size=56))
nb(t, 'Ədədlərin ən kiçik ortaq bölünənini tapın.', 12, FX('ƏKOB(2, 3, 4)', '=', BOX, size=56))
nb(t, 'Avtobuslardan biri 10 dəqiqədən, digəri 15 dəqiqədən bir dayanacağa gəlir. İkisi birlikdə gəldi. Neçə dəqiqədən sonra yenə birlikdə gələcəklər?', 30, story(['🚌', '🚍', '⏱️'], [BOX, 'dəqiqə']))
nb(t, 'Uşaqları 6 nəfərlik və ya 8 nəfərlik qruplara qalıqsız bölmək olur. Ən azı neçə uşaq var?', 24, story(['👧', '👦', '👧'], [BOX, 'uşaq']))
nb(t, 'ƏBOB(12, 18) və ƏKOB(12, 18) ədədlərinin hasilini tapın.', 216, FX('6 · 36', '=', BOX, size=60))

# ============================================================ 248
t = T(248, 'Nisbət',
      'İki ədədin qismətinə bu ədədlərin nisbəti deyilir: 12 : 4 = 3. Nisbətin hər iki həddini eyni ədədə vurduqda və ya böldükdə nisbət dəyişmir: 15 : 25 = 3 : 5.',
      q('12 : 4 = 3', '15 : 25 = 3 : 5'))
nb(t, 'Nisbəti tapın.', 3, FX('12 : 4', '=', BOX, size=64))
rat(t, 'Nisbəti ixtisar edin. Hər iki həddi yazın.', (3, 5), FX('15 : 25', '=', BOX, ':', BOX, size=60))
rat(t, 'Nisbəti ixtisar edin. Hər iki həddi yazın.', (3, 2), FX('18 : 12', '=', BOX, ':', BOX, size=60))
rat(t, 'Sinifdə 12 oğlan və 16 qız var. Oğlanların sayının qızların sayına nisbətini ixtisar olunmuş şəkildə yazın.', (3, 4), story(['👦', '👧'], [BOX, ':', BOX]))
rat(t, 'Sinifdə 12 oğlan və 16 qız var. Qızların sayının bütün şagirdlərin sayına nisbətini yazın.', (4, 7), story(['👧', '🏫'], [BOX, ':', BOX]))
t.choice('Hansı nisbət 2 : 3 nisbətinə bərabərdir? Toxunun.', ['4 : 6', '3 : 2', '2 : 5'], 0)
nb(t, WB, 20, FX(BOX, ': 5 = 4', size=64))
nb(t, 'Nisbəti natural ədədlərin nisbəti ilə əvəz edin. Boş xanaya uyğun ədədi yazın.', 4, FX('0,5 : 2', '=', '1 :', BOX, size=60))
nb(t, 'Nisbəti natural ədədlərin nisbəti ilə əvəz edin. Boş xanaya uyğun ədədi yazın.', 2, FX((1, 2), ':', (1, 3), '=', '3 :', BOX, size=60))
nb(t, 'Qırmızı və göy kürəciklərin sayı 2 : 5 nisbətindədir. 6 qırmızı kürəcik var. Neçə göy kürəcik var?', 15, story(['🔴', '🔵'], [BOX, 'göy']))

# ============================================================ 249
t = T(249, 'Kəmiyyətlərin nisbəti',
      'Kəmiyyətlərin nisbətini tapmaq üçün onları eyni vahidlə ifadə edirik: 1 m : 25 sm = 100 sm : 25 sm = 4. 2 kq : 500 q = 2 000 q : 500 q = 4.',
      q('1 m : 25 sm = 100 : 25 = 4', size=52))
for l_, v in [('1 m : 25 sm', 4), ('2 kq : 500 q', 4), ('1 saat : 20 dəq', 3), ('1 l : 250 ml', 4)]:
    nb(t, 'Kəmiyyətləri eyni vahidlə ifadə edin və nisbəti tapın.', v, FX(l_, '=', BOX, size=56))
nb(t, 'Kəmiyyətlərin nisbətini tapın. Boş xanaya uyğun ədədi yazın.', 5, FX('3 m : 60 sm', '=', BOX, ': 1', size=56))
for l_, v in [('40 sm : 2 m', 5), ('500 m : 2 km', 4), ('30 dəq : 2 saat', 4), ('750 q : 1,5 kq', 2)]:
    nb(t, 'Kəmiyyətlərin nisbətini tapın. Boş xanaya uyğun ədədi yazın.', v, FX(l_, '=', '1 :', BOX, size=56))
t.choice('1 m : 10 sm nisbəti nəyə bərabərdir? Toxunun.', ['1 : 10', '10 : 1', '1 : 1'], 1)

# ============================================================ 250
t = T(250, 'Kəmiyyətin verilən nisbətdə bölünməsi',
      'Ədədi 3 : 5 nisbətində bölmək üçün onu 3 + 5 = 8 bərabər hissəyə bölürük. 40 : 8 = 5, deməli, hissələr 3 · 5 = 15 və 5 · 5 = 25-dir.',
      vstack([hstack([frac_bar(3, 3, 180, 50, (255, 167, 38)), frac_bar(5, 5, 300, 50, (66, 165, 245))], 0), txt('40 = 15 + 25', 56, INK)], 14))
for n_, a_, b_ in [(40, 3, 5), (60, 1, 2), (72, 4, 5)]:
    k = n_ // (a_ + b_)
    rat(t, '%d ədədini %d : %d nisbətində bölün. Hər iki hissəni yazın.' % (n_, a_, b_), (a_ * k, b_ * k), FX(n_, '→', BOX, 'və', BOX, size=60), sep='və')
nb(t, 'Elxan və Anar 30 manatı 2 : 3 nisbətində böldülər. Anar neçə manat aldı?', 18, story(['👦', '👦', '💵'], [BOX, 'manat']))
nb(t, 'Ərik və şəftəlinin kütlələri 3 : 4 nisbətindədir. Cəmi 28 kq meyvə var. Ərik neçə kiloqramdır?', 12, story(['🍑', '🧺'], [BOX, 'kq']))
nb(t, 'Üçbucağın bucaqları 1 : 2 : 3 nisbətindədir. Bucaqların cəmi 180°-dir. Ən böyük bucağı tapın.', 90, tri([(0.1, 0.05), (0.1, 0.9), (1.0, 0.9)], size=160, right=1)); ck(t, suf='°')
nb(t, 'Uzunluğu 35 sm olan parçanı 2 : 5 nisbətində iki hissəyə böldülər. Kiçik hissənin uzunluğunu tapın.', 10, FX(35, ':', 7, '·', 2, '=', BOX, 'sm', size=56))
danswer(t, 'Su və şirə 5 : 1 nisbətində qarışdırıldı. 3 litr içki alındı. Neçə litr şirə var?', Dm('0.5'), vstack([story(['🧃', '💧']), DEC('BOX2', 'l', size=50)], 10))
nb(t, '120 şagird qızlar və oğlanlar 7 : 5 nisbətindədir. Neçə qız var?', 70, story(['👧', '👦'], [BOX, 'qız']))
nb(t, 'Rəfdəki kitablar 2 : 3 : 5 nisbətindədir. Cəmi 50 kitab var. Ən çox kitab olan qrupda neçə kitab var?', 25, story(['📚'], [BOX, 'kitab']))

# ============================================================ 251
t = T(251, 'Tənasüb',
      'İki nisbətin bərabərliyi tənasübdür: 2 : 5 = 8 : 20. Tənasübdə kənar hədlərin hasili orta hədlərin hasilinə bərabərdir: 2 · 20 = 5 · 8. Bu xassə ilə naməlum həddi tapırıq.',
      q('2 : 5 = 8 : 20', '2 · 20 = 5 · 8 = 40'))
for s_, v in [('2 : 5 = x : 20', 8), ('x : 9 = 4 : 6', 6), ('3 : x = 12 : 16', 4), ('15 : 10 = 6 : x', 4), ('x : 7 = 6 : 14', 3), ('1,5 : x = 3 : 4', 2), ('0,2 : 0,5 = x : 10', 4)]:
    nb(t, 'Tənasübün naməlum həddini tapın.', v, q(s_, FX('x', '=', BOX, size=58)))
t.choice('Hansı bərabərlik tənasübdür? Toxunun.', ['2 : 3 = 4 : 6', '2 : 3 = 3 : 2', '1 : 2 = 2 : 3'], 0)
nb(t, 'Kənar hədlərin hasilini tapın.', 40, q('4 : 5 = 8 : 10', FX('4 · 10', '=', BOX, size=58)))
nb(t, '3 dəftər 6 manatdır. 7 belə dəftər neçə manatdır? Tənasüb qurun.', 14, story(['📓'], ['3 : 6 = 7 : x', '→', BOX, 'manat'], size=70))

# ============================================================ 252
t = T(252, 'Miqyas',
      'Miqyas xəritədəki məsafənin həqiqi məsafəyə nisbətidir. 1 : 100 000 miqyası xəritədə 1 sm-in həqiqətdə 100 000 sm, yəni 1 km olduğunu göstərir.',
      q('1 : 100 000', '1 sm → 1 km'))
nb(t, 'Xəritənin miqyası 1 : 100 000-dir. Xəritədə 3 sm olan məsafə həqiqətdə neçə km-dir?', 3, story(['🗺️'], [BOX, 'km']))
nb(t, 'Planın miqyası 1 : 1 000-dir. Planda 5 sm olan məsafə həqiqətdə neçə metrdir?', 50, story(['📐'], [BOX, 'm']))
nb(t, 'Planın miqyası 1 : 200-dür. Uzunluğu 6 m olan otaq planda neçə santimetr olar?', 3, story(['🏠'], [BOX, 'sm']))
nb(t, 'Xəritədə 4 sm həqiqətdə 20 km-dir. Xəritənin miqyasını tapın.', 500000, FX('1 :', BOX, size=60))
nb(t, 'Modelin miqyası 1 : 50-dir. Modeldə 10 sm olan hissə həqiqətdə neçə metrdir?', 5, story(['🚗'], [BOX, 'm']))
t.choice('Hansı miqyas əşyanı daha böyük göstərir? Toxunun.', ['1 : 100', '1 : 10 000'], 0)
nb(t, 'Xəritənin miqyası 1 : 2 000 000-dur. Xəritədə 5 sm olan məsafə həqiqətdə neçə km-dir?', 100, story(['🗺️'], [BOX, 'km']))
nb(t, 'İki şəhər arasındakı məsafə 150 km-dir. Miqyası 1 : 5 000 000 olan xəritədə bu məsafə neçə santimetr olar?', 3, story(['🏙️', '🏙️'], [BOX, 'sm']))
nb(t, 'Şəklin miqyası 10 : 1-dir. Şəkildə böcəyin uzunluğu 5 sm-dir. Böcəyin həqiqi uzunluğu neçə millimetrdir?', 5, story(['🐞'], [BOX, 'mm']))
nb(t, 'Xəritənin miqyası 1 : 300 000-dir. Xəritədə 2 sm olan məsafə həqiqətdə neçə km-dir?', 6, story(['🗺️'], [BOX, 'km']))

# ============================================================ 253
t = T(253, 'Düz mütənasib asılılıq',
      'Bir kəmiyyət neçə dəfə artanda digəri də o qədər dəfə artırsa, onlar düz mütənasibdir. Məsələn, alınan malın miqdarı və dəyəri: 1 kq 3 manatdırsa, 5 kq 15 manatdır.',
      tab([['kq', '1', '2', '5'], ['manat', '3', '6', '15']], 40))
nb(t, '1 kq alma 3 manatdır. 5 kq alma neçə manatdır?', 15, story(['🍎'], [BOX, 'manat']))
nb(t, 'Cədvəldə düz mütənasib kəmiyyətlər verilib. Boş xanaya uyğun ədədi yazın.', 12, table([[txt('x', 38), txt('1', 38), txt('2', 38), txt('3', 38)], [txt('y', 38), txt('4', 38), txt('8', 38), box(70, 64)]], 80))
nb(t, 'Avtomobil 2 saatda 120 km yol getdi. Eyni sürətlə 5 saatda neçə km gedər?', 300, story(['🚗'], [BOX, 'km']))
nb(t, '4 kq alma 10 manatdır. 6 kq alma neçə manatdır?', 15, story(['🍏'], [BOX, 'manat']))
nb(t, '3 m parça 12 manatdır. 8 m parça neçə manatdır?', 32, story(['🧵'], [BOX, 'manat']))
t.choice('Hansı kəmiyyətlər düz mütənasibdir? Toxunun.', ['malın miqdarı və dəyəri', 'eyni yolda sürət və vaxt', 'fəhlələrin sayı və işin müddəti'], 0)
nb(t, '5 dəftər 4 manatdır. 15 dəftər neçə manatdır?', 12, story(['📓'], [BOX, 'manat']))
nb(t, 'y = 7x düsturu ilə verilən asılılıqda x = 3 olduqda y-i tapın.', 21, q('y = 7x', FX('y', '=', BOX, size=58)))
nb(t, 'Printer 2 dəqiqədə 30 səhifə çap edir. 10 dəqiqədə neçə səhifə çap edər?', 150, story(['🖨️'], [BOX, 'səhifə']))
nb(t, '4 nəfərlik resept üçün 200 q un lazımdır. 6 nəfər üçün neçə qram un lazımdır?', 300, story(['🥣'], [BOX, 'q']))

# ============================================================ 254
t = T(254, 'Tərs mütənasib asılılıq',
      'Bir kəmiyyət neçə dəfə artanda digəri o qədər dəfə azalırsa, onlar tərs mütənasibdir. Məsələn, eyni işi 4 fəhlə 6 günə görürsə, 8 fəhlə 3 günə görər.',
      tab([['fəhlə', '4', '8'], ['gün', '6', '3']], 40))
nb(t, '4 fəhlə işi 6 günə görür. 8 fəhlə həmin işi neçə günə görər?', 3, story(['👷', '👷'], [BOX, 'gün']))
nb(t, 'Avtomobil saatda 60 km sürətlə yolu 4 saata gedir. Saatda 80 km sürətlə neçə saata gedər?', 3, story(['🚗'], [BOX, 'saat']))
nb(t, '3 nasos hovuzu 12 saata doldurur. 4 nasos neçə saata doldurar?', 9, story(['💧', '🏊'], [BOX, 'saat']))
nb(t, 'Cədvəldə tərs mütənasib kəmiyyətlər verilib. Boş xanaya uyğun ədədi yazın.', 3, table([[txt('x', 38), txt('1', 38), txt('2', 38), txt('4', 38)], [txt('y', 38), txt('12', 38), txt('6', 38), box(70, 64)]], 80))
nb(t, 'Konfetləri hər pakete 6 dənə qoysaq, 20 paket olur. Hər pakete 8 dənə qoysaq, neçə paket olar?', 15, story(['🍬', '🛍️'], [BOX, 'paket']))
t.choice('Hansı kəmiyyətlər tərs mütənasibdir? Toxunun.', ['eyni yolda sürət və vaxt', 'qələmlərin sayı və qiyməti', 'kvadratın tərəfi və perimetri'], 0)
nb(t, 'Düzbucaqlının sahəsi 24 sm²-dir. Eni 4 sm olarsa, uzunluğu neçə santimetrdir?', 6, rect_sides(6, 4, '?', '4 sm', 30))
nb(t, '5 maşın yükü 12 reysə daşıyır. 6 maşın neçə reysə daşıyar?', 10, story(['🚚'], [BOX, 'reys']))
nb(t, 'y = 36 : x düsturu ilə verilən asılılıqda x = 9 olduqda y-i tapın.', 4, q('y = 36 : x', FX('y', '=', BOX, size=58)))
nb(t, 'Ərzaq 10 nəfərə 15 gün çatır. 15 nəfərə neçə gün çatar?', 10, story(['🥫', '👥'], [BOX, 'gün']))

# ============================================================ 255
t = T(255, 'Nisbətin faizlə ifadəsi',
      'Bir ədədin digərinin neçə faizi olduğunu tapmaq üçün onların nisbətini 100%-ə vururuq: 3 : 4 = 0,75 = 75%. 25 şagirddən 15-i 15 : 25 · 100% = 60%-dir.',
      q('3 : 4 = 0,75 = 75%'))
for l_, v in [('3 : 4', 75), ('1 : 5', 20), ('7 : 20', 35)]:
    pct_num(t, 'Nisbəti faizlə ifadə edin.', v, FX(l_, '=', BOX, '%', size=60))
pct_num(t, 'Sinifdə 25 şagird var, onlardan 15-i qızdır. Qızlar şagirdlərin neçə faizidir?', 60, vstack([story(['👧', '🏫']), hstack([box(110, 80), txt('%', 60, INK)], 8)], 14))
pct_num(t, 'Testdə 40 sual var idi. Lalə 34 suala düz cavab verdi. O, sualların neçə faizinə düz cavab verdi?', 85, vstack([story(['📝']), hstack([box(110, 80), txt('%', 60, INK)], 8)], 14))
pct_num(t, '12 ədədi 48 ədədinin neçə faizidir?', 25, FX('12 : 48', '=', BOX, '%', size=60))
pct_num(t, '45 ədədi 50 ədədinin neçə faizidir?', 90, FX('45 : 50', '=', BOX, '%', size=60))
pct_num(t, 'Bağda 80 ağac var, onlardan 32-si alma ağacıdır. Alma ağacları neçə faizdir?', 40, vstack([story(['🌳', '🍎']), hstack([box(110, 80), txt('%', 60, INK)], 8)], 14))
t.choice('1 : 2 nisbəti neçə faizdir? Toxunun.', ['50%', '20%', '12%'], 0)
pct_num(t, 'Anar 500 manatdan 150 manat xərclədi. O, pulunun neçə faizini xərclədi?', 30, vstack([story(['💵']), hstack([box(110, 80), txt('%', 60, INK)], 8)], 14))

# ============================================================ 256
t = T(256, 'Kəmiyyətin dəyişməsinin faizlə ifadəsi',
      'Kəmiyyətin neçə faiz dəyişdiyini tapmaq üçün dəyişməni ilkin qiymətə bölüb 100%-ə vururuq. 50 manat 60 manat oldusa, 10 : 50 · 100% = 20% artıb.',
      q('50 → 60', '10 : 50 = 20%'))
for a_, b_ in [(50, 60), (80, 60), (200, 250), (40, 34), (1000, 1100), (60, 48)]:
    pct_num(t, 'Kəmiyyət şəkildəki kimi dəyişdi. Neçə faiz %s?' % ('artdı' if b_ > a_ else 'azaldı'), abs(b_ - a_) * 100 // a_, vstack([txt('%s → %s' % (f(a_), f(b_)), 60, INK), hstack([box(110, 80), txt('%', 60, INK)], 8)], 14))
pct_num(t, 'Köynəyin qiyməti 120 manatdan 90 manata endi. Qiymət neçə faiz azaldı?', 25, vstack([story(['👕'], ['120', '→', '90']), hstack([box(110, 80), txt('%', 60, INK)], 8)], 14))
pct_num(t, 'Dərnəkdə 25 şagird var idi, indi 30 şagird var. Şagirdlərin sayı neçə faiz artdı?', 20, vstack([story(['🎨'], ['25', '→', '30']), hstack([box(110, 80), txt('%', 60, INK)], 8)], 14))
t.choice('Qiymət 100 manatdan 150 manata qalxdı. Doğru cümləyə toxunun.', ['50% artdı', '150% artdı', '50% azaldı'], 0)
pct_num(t, 'Kitabın qiyməti 75 manatdan 90 manata qalxdı. Qiymət neçə faiz artdı?', 20, vstack([story(['📕'], ['75', '→', '90']), hstack([box(110, 80), txt('%', 60, INK)], 8)], 14))

# ============================================================ 257
t = T(257, 'Tam ədədlər',
      'Natural ədədlər, onların əksi olan mənfi ədədlər və sıfır tam ədədlərdir: ..., −3, −2, −1, 0, 1, 2, 3, ... Ədəd oxunda mənfi ədədlər sıfırdan solda yerləşir. 5 və −5 əks ədədlərdir.',
      zline(-5, 5))
INS = 'Ədədi yazın. Mənfi ədəd üçün əvvəlcə − düyməsinə toxunun.'
zans(t, 'Hava sıfırdan 5 dərəcə aşağıdır. Temperaturu ədədlə yazın. Əvvəlcə − düyməsinə toxunun.', -5, story(['🌡️', '❄️'], [BOX, '°']))
zans(t, 'Xəzər dənizinin səviyyəsi okean səviyyəsindən 28 m aşağıdır. Bunu ədədlə yazın.', -28, story(['🌊'], [BOX, 'm']))
zans(t, '−7 ədədinin əksini yazın.', 7, FX('−(−7)', '=', BOX, size=64))
zans(t, '12 ədədinin əksini yazın.', -12, FX('12', '→', BOX, size=64))
zans(t, 'Ədəd oxunda A nöqtəsinə uyğun ədədi yazın.', -3, zline(-6, 6, [(-3, 'A')]))
t.choice('Mənfi ədədlərin hamısına toxunun.', ['−4', '0', '5', '−11', '8'], [0, 3], mode='multi')
t.choice('0 ədədi haqqında doğru cümləyə toxunun.', ['müsbətdir', 'mənfidir', 'nə müsbət, nə mənfi'], 2)
zans(t, 'Ədəd oxunda 0-dan 6 vahid sola gedin. Hansı ədədə çatdınız?', -6, zline(-7, 3, [(0, '')]))
zans(t, '−2 ilə 3 arasında neçə tam ədəd var?', 4, zline(-3, 4, [(-2, ''), (3, '')]))
zans(t, 'Ən böyük mənfi tam ədədi yazın.', -1, box(110, 86))

# ============================================================ 258
t = T(258, 'Tam ədədlərin müqayisəsi',
      'Ədəd oxunda sağdakı ədəd soldakından böyükdür. Hər müsbət ədəd sıfırdan və mənfi ədəddən böyükdür. İki mənfi ədəddən mütləq qiyməti kiçik olan böyükdür: −2 > −7.',
      vstack([zline(-7, 3, [(-7, ''), (-2, '')]), txt('−2 > −7', 60, INK)], 10))
t.sign('Ədədləri müqayisə edin. Dairələrə >, < və ya = yazın.', [('−5', '3'), ('−2', '−7')], ['<', '>'])
t.sign('Ədədləri müqayisə edin. Dairələrə >, < və ya = yazın.', [('0', '−4'), ('−10', '−1')], ['>', '<'])
t.choice('Ən böyük ədədə toxunun.', ['−3', '−8', '−1'], 2)
t.choice('Ədədlərə kiçikdən böyüyə doğru sıra ilə toxunun.', ['3', '−5', '0', '−2'], [1, 3, 2, 0], mode='order', hint='Ədədlərə kiçikdən böyüyə sıra ilə toxunun.')
t.choice('Ən kiçik ədədə toxunun.', ['−12', '−21', '−2'], 1)
zans(t, '−4 ilə 0 arasında neçə tam ədəd var?', 3, zline(-5, 1, [(-4, ''), (0, '')]))
t.choice('Hansı şəhərdə daha soyuqdur? Toxunun.', ['Bakı: −2°', 'Moskva: −15°', 'Tbilisi: 1°'], 1, stem=story(['❄️', '🌡️']))
zans(t, '−6-dan böyük olan ən kiçik tam ədədi yazın.', -5, zline(-8, 0, [(-6, '')]))
t.choice('Ədədlərə böyükdən kiçiyə doğru sıra ilə toxunun.', ['−1', '−10', '4', '0'], [2, 3, 0, 1], mode='order', hint='Ədədlərə böyükdən kiçiyə sıra ilə toxunun.')
t.sign('Ədədləri müqayisə edin. Dairələrə >, < və ya = yazın.', [('−15', '−51'), ('−9', '0')], ['>', '<'])

# ============================================================ 259
t = T(259, 'Ədədin mütləq qiyməti',
      'Ədədin mütləq qiyməti ədəd oxunda həmin nöqtədən sıfıra qədər olan məsafədir: |−8| = 8, |8| = 8, |0| = 0. Mütləq qiymət heç vaxt mənfi olmur.',
      q('|−8| = 8', '|8| = 8'))
for e_, v in [('|−8|', 8), ('|15|', 15), ('|0|', 0), ('|−7| + |3|', 10), ('|−12| − |−5|', 7), ('|−3| · |−4|', 12)]:
    zcalc(t, CAL, e_, v, size=64)
zans(t, 'Mütləq qiyməti 6 olan mənfi ədədi yazın.', -6, FX('|', BOX, '| = 6', size=64))
t.choice('Hansı ədədin mütləq qiyməti ən böyükdür? Toxunun.', ['−9', '7', '−4'], 0)
t.sign('Müqayisə edin. Dairələrə >, < və ya = yazın.', [('|−5|', '3'), ('|−2|', '|2|')], ['>', '='])
zans(t, 'Ədəd oxunda −9 nöqtəsi sıfırdan neçə vahid uzaqdadır?', 9, zline(-10, 1, [(-9, '')]))

# ============================================================ 260
t = T(260, 'Tam ədədlərin toplanması',
      'İşarələri eyni olan ədədləri toplamaq üçün mütləq qiymətləri toplayıb ortaq işarəni yazırıq: −5 + (−3) = −8. İşarələri müxtəlif olanda böyük mütləq qiymətdən kiçiyi çıxıb, böyüyün işarəsini yazırıq: −7 + 4 = −3.',
      q('−5 + (−3) = −8', '−7 + 4 = −3'))
ZI = 'Hesablayın. Mənfi cavab üçün əvvəlcə − düyməsinə toxunun.'
for e_, v in [('−5 + (−3)', -8), ('−7 + 4', -3), ('9 + (−6)', 3), ('−12 + 12', 0), ('−15 + (−20)', -35), ('8 + (−13)', -5), ('−3 + 5 + (−6)', -4), ('−25 + 40', 15)]:
    zcalc(t, ZI, e_, v)
zans(t, 'Səhər temperatur −4° idi. Günortaya qədər 9° artdı. Günorta temperatur neçə dərəcə oldu?', 5, story(['🌡️', '☀️'], ['−4 + 9 =', BOX, '°']))
t.choice('Hansı cəm mənfidir? Toxunun.', ['−7 + 10', '5 + (−9)', '−2 + 2'], 1)

# ============================================================ 261
t = T(261, 'Tam ədədlərin çıxılması',
      'Bir ədəddən digərini çıxmaq üçün azalana çıxılanın əksini əlavə edirik: 3 − 8 = 3 + (−8) = −5; 5 − (−3) = 5 + 3 = 8.',
      q('3 − 8 = 3 + (−8) = −5', '5 − (−3) = 5 + 3 = 8', size=52))
for e_, v in [('3 − 8', -5), ('−4 − 6', -10), ('5 − (−3)', 8), ('−7 − (−2)', -5), ('−10 − (−10)', 0), ('0 − 9', -9), ('−15 − 5', -20)]:
    zcalc(t, ZI, e_, v)
zans(t, 'Gündüz temperatur 6°, gecə isə −5° idi. Fərq neçə dərəcədir?', 11, story(['☀️', '🌙'], ['6 − (−5) =', BOX, '°']))
zans(t, 'Dağın zirvəsi dəniz səviyyəsindən 1 200 m yuxarıda, çuxurun dibi 40 m aşağıdadır. Onların hündürlükləri arasındakı fərqi tapın.', 1240, story(['⛰️', '🕳️'], ['1 200 − (−40) =', BOX, 'm'], size=70))
t.choice('8 − (−2) ifadəsi hansı ifadəyə bərabərdir? Toxunun.', ['8 + 2', '8 − 2', '−8 − 2'], 0)

# ============================================================ 262
t = T(262, 'Tam ədədlərin vurulması və bölünməsi',
      'İşarələri eyni olan ədədlərin hasili və qisməti müsbət, işarələri müxtəlif olanların hasili və qisməti mənfidir: −6 · (−3) = 18, −4 · 5 = −20, −36 : 4 = −9.',
      q('(−) · (−) = (+)', '(−) · (+) = (−)'))
for e_, v in [('−4 · 5', -20), ('−6 · (−3)', 18), ('7 · (−8)', -56), ('−36 : 4', -9), ('−42 : (−6)', 7), ('48 : (−12)', -4), ('(−2)³', -8), ('(−1) · (−1) · (−1) · (−1)', 1), ('−5 · (−2) · (−3)', -30)]:
    zcalc(t, ZI, e_, v, size=56)
t.choice('Hansı hasil müsbətdir? Toxunun.', ['−3 · 4', '(−3) · (−4)', '3 · (−4)'], 1)

# ============================================================ 263
t = T(263, 'Tam ədədlər üzərində əməllər',
      'Tam ədədlərlə ifadələrdə əməllərin ardıcıllığı natural ədədlərdəki kimidir: əvvəl mötərizə, sonra vurma və bölmə, sonra toplama və çıxma: −3 · 4 + 10 = −12 + 10 = −2.',
      q('−3 · 4 + 10 = −12 + 10 = −2', size=52))
for e_, v in [('−3 · 4 + 10', -2), ('(−8 + 2) · 3', -18), ('20 : (−5) − 3', -7), ('−2 · (−3) − 10', -4), ('(−4)² − 7', 9), ('−15 : 3 + (−2) · 4', -13), ('−6 + 6 · (−2)', -18)]:
    zcalc(t, 'İfadənin qiymətini tapın.', e_, v, size=54)
zans(t, 'Tənliyi həll edin.', -4, q('x + 7 = 3', FX('x', '=', BOX, size=58)))
zans(t, 'Tənliyi həll edin.', -8, q('2x = −16', FX('x', '=', BOX, size=58)))
zans(t, 'Hesabda 20 manat borc var idi (−20). Hesaba 50 manat qoyuldu. Hesabda nə qədər pul oldu?', 30, story(['💳'], ['−20 + 50 =', BOX, 'manat'], size=70))

# ============================================================ 264
t = T(264, 'Düzbucaqlı koordinat sistemi',
      'Koordinat müstəvisində hər nöqtənin iki koordinatı var: absis (x) və ordinat (y). A(3; 2) nöqtəsinə çatmaq üçün başlanğıcdan 3 vahid sağa, 2 vahid yuxarı gedirik. Oxlar müstəvini dörd rübə bölür.',
      cgrid(4, [(3, 2, 'A(3; 2)')], 36))
CR = 'Nöqtənin koordinatlarını yazın: əvvəl x, sonra y.'
for x_, y_, L_ in [(3, 2, 'A'), (-4, 1, 'B'), (-2, -3, 'C'), (0, -4, 'D')]:
    crd(t, CR, (x_, y_), cgrid(5, [(x_, y_, L_)], 30))
Q4 = ['I', 'II', 'III', 'IV']
t.choice('M(−3; 5) nöqtəsi hansı rübdədir? Toxunun.', Q4, 1, stem=cgrid(5, [], 22))
t.choice('N(4; −2) nöqtəsi hansı rübdədir? Toxunun.', Q4, 3, stem=cgrid(5, [], 22))
t.choice('Koordinatları (−1; 3) olan nöqtəyə uyğun hərfə toxunun.', ['A', 'B', 'C'], 2, stem=cgrid(5, [(3, -1, 'A'), (-3, 1, 'B'), (-1, 3, 'C')], 30))
zans(t, 'x oxu üzərində olan hər nöqtənin ordinatı neçədir?', 0, cgrid(4, [(3, 0, 'P'), (-2, 0, 'Q')], 30))
zans(t, 'A(5; −7) nöqtəsinin absisini yazın.', 5, FX('A(5; −7)', '→', 'x =', BOX, size=56))
zans(t, 'A(5; −7) nöqtəsinin ordinatını yazın.', -7, FX('A(5; −7)', '→', 'y =', BOX, size=56))

# ============================================================ 265
t = T(265, 'Koordinat sistemində məsafə',
      'Eyni üfüqi xətt üzərindəki nöqtələr arasındakı məsafə absislərin fərqinin mütləq qiymətinə bərabərdir: A(−3; 4) və B(5; 4) arasındakı məsafə |5 − (−3)| = 8. Şaquli xətt üzərində ordinatların fərqini tapırıq.',
      cgrid(5, [(-3, 4, 'A'), (5, 4, 'B')], 30, poly_=None))
DS = 'Nöqtələr arasındakı məsafəni tapın (vahidlə).'
for a_, b_ in [((1, 2), (5, 2)), ((-3, 4), (5, 4)), ((2, -1), (2, 5)), ((-4, -2), (-4, 3)), ((-5, 1), (4, 1))]:
    d_ = abs(a_[0] - b_[0]) + abs(a_[1] - b_[1])
    zans(t, DS, d_, vstack([cgrid(5, [(a_[0], a_[1], 'A'), (b_[0], b_[1], 'B')], 26), FX('AB', '=', BOX, size=48)], 8))
zans(t, 'Düzbucaqlının təpələri (1; 1), (5; 1), (5; 4), (1; 4) nöqtələridir. Perimetrini tapın.', 14, vstack([cgrid(5, [], 26, poly_=[(1, 1), (5, 1), (5, 4), (1, 4)]), FX('P', '=', BOX, size=48)], 8))
zans(t, 'Düzbucaqlının təpələri (1; 1), (5; 1), (5; 4), (1; 4) nöqtələridir. Sahəsini tapın.', 12, vstack([cgrid(5, [], 26, poly_=[(1, 1), (5, 1), (5, 4), (1, 4)]), FX('S', '=', BOX, size=48)], 8))
zans(t, 'A(3; 4) nöqtəsindən x oxuna qədər məsafə neçə vahiddir?', 4, cgrid(5, [(3, 4, 'A')], 26))
zans(t, 'A(3; 4) nöqtəsindən y oxuna qədər məsafə neçə vahiddir?', 3, cgrid(5, [(3, 4, 'A')], 26))
zans(t, 'Kvadratın təpələri (−2; −2), (2; −2), (2; 2), (−2; 2) nöqtələridir. Sahəsini tapın.', 16, vstack([cgrid(4, [], 28, poly_=[(-2, -2), (2, -2), (2, 2), (-2, 2)]), FX('S', '=', BOX, size=48)], 8))

# ============================================================ 266
t = T(266, 'Koordinat sistemində simmetriya və yerdəyişmə',
      'A(3; 2) nöqtəsinin x oxuna nəzərən simmetriki (3; −2), y oxuna nəzərən simmetriki (−3; 2), başlanğıc nöqtəyə nəzərən simmetriki (−3; −2) nöqtəsidir. Nöqtəni sağa sürüşdürəndə absis artır, yuxarı sürüşdürəndə ordinat artır.',
      cgrid(4, [(3, 2, 'A'), (3, -2, ''), (-3, 2, ''), (-3, -2, '')], 34))
crd(t, 'A(3; 2) nöqtəsinə x oxuna nəzərən simmetrik olan nöqtənin koordinatlarını yazın.', (3, -2), cgrid(4, [(3, 2, 'A')], 30))
crd(t, 'A(3; 2) nöqtəsinə y oxuna nəzərən simmetrik olan nöqtənin koordinatlarını yazın.', (-3, 2), cgrid(4, [(3, 2, 'A')], 30))
crd(t, 'A(3; 2) nöqtəsinə koordinat başlanğıcına nəzərən simmetrik olan nöqtənin koordinatlarını yazın.', (-3, -2), cgrid(4, [(3, 2, 'A')], 30))
crd(t, 'B(−4; 1) nöqtəsini 5 vahid sağa sürüşdürün. Yeni nöqtənin koordinatlarını yazın.', (1, 1), cgrid(5, [(-4, 1, 'B')], 28))
crd(t, 'C(2; 3) nöqtəsini 4 vahid aşağı sürüşdürün. Yeni nöqtənin koordinatlarını yazın.', (2, -1), cgrid(5, [(2, 3, 'C')], 28))
crd(t, 'D(−1; −2) nöqtəsini 3 vahid yuxarı və 2 vahid sola sürüşdürün. Yeni nöqtənin koordinatlarını yazın.', (-3, 1), cgrid(5, [(-1, -2, 'D')], 28))
t.choice('Hansı hərfin şaquli simmetriya oxu var? Toxunun.', ['A', 'F', 'G'], 0)
zans(t, '(5; −6) nöqtəsinə x oxuna nəzərən simmetrik olan nöqtənin ordinatını yazın.', 6, FX('(5; −6)', '→', '(5;', BOX, ')', size=56))
crd(t, 'E(0; 4) nöqtəsinə koordinat başlanğıcına nəzərən simmetrik olan nöqtənin koordinatlarını yazın.', (0, -4), cgrid(5, [(0, 4, 'E')], 28))
t.choice('Nöqtəni y oxuna nəzərən simmetrik köçürəndə hansı koordinatın işarəsi dəyişir? Toxunun.', ['absis', 'ordinat', 'hər ikisi'], 0)

for tp in TOPICS:  # koordinat torları: şəkil böyük qalsın
    if tp.n in (264, 265, 266):
        for p_ in tp.problems:
            if p_['check']:
                p_['check']['big'] = 1
TOPICS.sort(key=lambda x: x.n)
save()
