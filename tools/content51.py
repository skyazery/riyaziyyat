"""5-ci sinif riyaziyyat, 1-ci hissə: 33 mövzu (191–223), hər mövzuda 10 tapşırıq.
Run: python3 tools/content51.py [OUTDIR]   (default ~/riyaziyyat/5-1)"""
import os, sys
from bookgen import *
init(sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser('~/riyaziyyat/5-1'))
from kit56 import *

OPT = '«Əvvəl tam hissəni, sonra surəti və məxrəci yazın.»'

# ============================================================ 199
t = T(199, 'Düzgün və düzgün olmayan kəsrlər',
      'Surəti məxrəcindən kiçik olan kəsr düzgün kəsrdir: 4/5 < 1. Surəti məxrəcindən böyük və ya ona bərabər olan kəsr düzgün olmayan kəsrdir: 7/5 > 1. Düzgün olmayan kəsri qarışıq ədəd şəklində yazmaq olar: 7/5 = 1 tam 2/5.',
      vstack([tiles(7, 5, 34), FX((7, 5), '=', (1, 2, 5), size=60)], 22))
frac_num(t, 'Kartlara uyğun kəsri yazın.', (6, 5), tiles(6, 5, 34))
t.choice('Hansı kəsr düzgün olmayan kəsrdir? Toxunun.', ['3/4', '9/4', '5/6'], 1)
t.choice('Düzgün kəsrlərin hamısına toxunun.', ['2/3', '7/5', '6/9', '10/3', '15/18'], [0, 2, 4], mode='multi')
frac_num(t, 'Bölmə əməlini adi kəsrlə yazın.', (3, 7), hstack([txt('3 : 7', 64, INK), txt('=', 64, BLUE), fr(BOX, BOX, 56)], 18))
frac_num(t, 'Kəsri ixtisar edin. İxtisar olunmayan kəsri yazın.', (2, 3), FX((8, 12), '=', (BOX, BOX), size=64))
frac_num(t, 'Düzgün olmayan kəsri qarışıq ədəd şəklində yazın. Əvvəl tam hissəni, sonra surəti və məxrəci yazın.', (1, 2, 5),
         vstack([FX((7, 5), '=', BOX, (BOX, BOX), size=64), txt('7 : 5 = 1 (qalıq 2)', 36, GREY)], 18))
frac_num(t, 'Düzgün olmayan kəsri qarışıq ədəd şəklində yazın. Əvvəl tam hissəni, sonra surəti və məxrəci yazın.', (3, 1, 12), FX((37, 12), '=', BOX, (BOX, BOX), size=64))
frac_num(t, 'Qarışıq ədədi düzgün olmayan kəsr şəklində yazın.', (11, 4),
         vstack([FX((2, 3, 4), '=', (BOX, BOX), size=64), txt('4 · 2 + 3 = ?', 36, GREY)], 18))
frac_num(t, 'Ədəd oxunda A nöqtəsinə uyğun düzgün olmayan kəsri yazın.', (7, 3), fline(3, 3, marks=[(7, 'A')]))
frac_num(t, 'Samir 2 almanı 4 dostu arasında bərabər böldü. Hər dostuna almanın hansı hissəsi düşdü? İxtisar olunmuş kəsri yazın.', (1, 2),
         hstack([hstack([em('🍎', 80)] * 2, 6), em('👦', 70), em('👧', 70), em('👦', 70), em('👧', 70)], 16))

# ============================================================ 209
t = T(209, 'Onluq kəsrlər',
      'Onluq kəsrdə vergüldən sonra birinci rəqəm ondabirləri, ikinci rəqəm yüzdəbirləri, üçüncü rəqəm mindəbirləri göstərir: 1,125 = 1 + 0,1 + 0,02 + 0,005. Bu ədəd belə oxunur: bir tam mində yüz iyirmi beş.',
      vstack([tab([['T', ',', 'OB', 'YB', 'MB'], ['1', ',', '1', '2', '5']], 40), FX((1, 125, 1000), '=', '1,125', size=56)], 20))
dec_num(t, 'Adi kəsri onluq kəsr şəklində yazın.', '0,005', hstack([fr(5, 1000, 56), txt('=', 64, BLUE), DEC('BOX2')], 18))
dec_num(t, 'Qarışıq ədədi onluq kəsr şəklində yazın.', '2,003', hstack([mixed(2, 3, 1000, 56), txt('=', 64, BLUE), DEC('BOX2')], 18))
dec_num(t, 'Adi kəsri onluq kəsr şəklində yazın.', '0,349', hstack([fr(349, 1000, 56), txt('=', 64, BLUE), DEC('BOX2')], 18))
dec_num(t, 'Sözlərlə yazılmış ədədi onluq kəsr şəklində yazın: on bir tam mində yüz otuz iki.', '11,132', vstack([words('on bir tam mində yüz otuz iki'), DEC('BOX2')], 24))
frac_num(t, 'Onluq kəsri adi kəsr şəklində yazın.', (7, 1000), hstack([txt('0,007', 64, INK), txt('=', 64, BLUE), fr(BOX, BOX, 56)], 18))
frac_num(t, 'Onluq kəsri qarışıq ədəd şəklində yazın. Əvvəl tam hissəni, sonra surəti və məxrəci yazın.', (1, 199, 1000), hstack([txt('1,199', 64, INK), txt('=', 64, BLUE), box(70, 70), fr(BOX, BOX, 56)], 18))
dec_num(t, 'Mərtəbə cədvəlinə uyğun onluq kəsri yazın.', '23,231',
        vstack([tab([['O', 'T', ',', 'OB', 'YB', 'MB'], ['●●', '●●●', ',', '●●', '●●●', '●']], 38), DEC('BOX2')], 24))
t.choice('37,085 ədədində qırmızı rəqəm hansı mərtəbədədir? Toxunun.', ['ondabirlər', 'yüzdəbirlər', 'mindəbirlər'], 1,
         stem=hstack([txt('37,0', 80, INK), txt('8', 80, RED), txt('5', 80, INK)], 0))
t.choice('Hansı bərabərlik doğru deyil? Toxunun.', ['3,2 = 3,20', '0,69 = 0,609', '21,40 = 21,4'], 1)
dec_num(t, 'Onluq kəsr açıq şəkildə yazılıb. Boş xanaya uyğun onluq kəsri yazın.', '0,08', DEC('4,583', '=', '4', '+', '0,5', '+', 'BOX2', '+', '0,003', size=50))

# ============================================================ 220
t = T(220, 'Faiz, adi kəsr, onluq kəsr',
      'Bir faiz tamın yüzdə bir hissəsidir: 1/100 = 1%. Tamın 100 bərabər hissəsindən 17-si onun 17%-ni təşkil edir. Onluq kəsri faizlə yazmaq üçün onu 100-ə vururuq: 0,43 = 43%.',
      hstack([grid100(17, (255, 138, 61), cell=26), vstack([FX((17, 100), '=', '17%', size=56), txt('0,43 = 43%', 56, INK)], 24)], 30))
pct_num(t, 'Rənglənmiş hissəni faizlə yazın.', 33, hstack([grid100(33), txt('=', 64, BLUE), box(110, 80), txt('%', 60, INK)], 14))
frac_num(t, 'Rənglənmiş hissəyə uyğun adi kəsri yazın.', (47, 100), hstack([grid100(47, (102, 187, 106)), txt('=', 64, BLUE), fr(BOX, BOX, 50)], 14))
pct_num(t, 'Adi kəsri faizlə ifadə edin.', 9, hstack([fr(9, 100, 60), txt('=', 64, BLUE), box(110, 80), txt('%', 60, INK)], 14))
pct_num(t, 'Kəsri məxrəci 100 olan kəsrlə əvəz edin və faizlə ifadə edin.', 65,
        vstack([hstack([fr(13, 20, 60), txt('=', 64, BLUE), fr('13 · 5', '20 · 5', 46), txt('=', 64, BLUE), box(110, 80), txt('%', 60, INK)], 12)], 0))
pct_num(t, 'Kəsri faizlə ifadə edin.', 75, hstack([fr(3, 4, 60), txt('=', 64, BLUE), fr('3 · 25', '4 · 25', 46), txt('=', 64, BLUE), box(110, 80), txt('%', 60, INK)], 12))
pct_num(t, 'Dairə bərabər hissələrə bölünüb. Rənglənmiş hissəni faizlə yazın.', 20, hstack([frac_circle(5, 1, 200, (139, 195, 74)), txt('=', 64, BLUE), box(110, 80), txt('%', 60, INK)], 18))
pct_num(t, 'Onluq kəsri faizlə ifadə edin.', 64, hstack([txt('0,64', 64, INK), txt('=', 64, BLUE), box(110, 80), txt('%', 60, INK)], 14))
t.choice('Ən böyük ədədə toxunun.', ['0,4', '35%', '1/4'], 0)
frac_num(t, 'Faizi adi kəsrlə yazın və ixtisar edin.', (1, 4), hstack([txt('25%', 64, INK), txt('=', 64, BLUE), fr(25, 100, 50), txt('=', 64, BLUE), fr(BOX, BOX, 50)], 14))
dec_num(t, 'Faizi onluq kəsrlə yazın.', '0,18', hstack([txt('18%', 64, INK), txt('=', 64, BLUE), DEC('BOX2')], 14))



# ============================================================ 191
t = T(191, 'Natural ədədlər',
      'Çoxrəqəmli ədədləri oxumaq üçün onu sağdan üç-üç siniflərə ayırırıq: təkliklər, minliklər, milyonlar sinfi. 2 345 607 ədədi belə oxunur: iki milyon üç yüz qırx beş min altı yüz yeddi.',
      vstack([tab([['Milyonlar', 'Minliklər', 'Təkliklər'], ['2', '345', '607']], 40), txt('2 345 607', 70, INK)], 20))
t.num('Ədədi rəqəmlərlə yazın: iki milyon üç yüz qırx min beş yüz.', [2340500], vstack([words('iki milyon üç yüz qırx min beş yüz'), box(260, 90)], 24))
t.num('Yüz minliklər mərtəbəsindəki rəqəmi yazın.', [5], vstack([txt('4 507 093', 80, INK), box(90, 90)], 24))
t.choice('Hansı ədəd «beş milyon qırx min yeddi» kimi oxunur? Toxunun.', ['5 040 007', '5 400 007', '5 004 007'], 0)
t.num('Mərtəbə toplananlarının cəmini yazın.', [3245607], vstack([FX('3 000 000', '+', '200 000', '+', '40 000', size=48), FX('+', '5 000', '+', '600', '+', '7', '=', BOX, size=48)], 16))
t.num('Ən böyük beşrəqəmli ədədi yazın.', [99999], box(240, 90))
t.num('Ən kiçik yeddirəqəmli ədədi yazın.', [1000000], box(260, 90))
t.choice('Hansı ədəddə 7 rəqəmi on minliklər mərtəbəsindədir? Toxunun.', ['3 570 214', '3 705 214', '3 507 214'], 0)
t.num('4, 0, 7, 2, 9 rəqəmlərinin hər birindən bir dəfə istifadə edərək ən böyük beşrəqəmli ədədi yazın.', [97420], vstack([hstack([nchip(v) for v in (4, 0, 7, 2, 9)], 12), box(240, 90)], 24))
t.num('Həmin rəqəmlərlə ən kiçik beşrəqəmli ədədi yazın: 4, 0, 7, 2, 9.', [20479], vstack([hstack([nchip(v) for v in (4, 0, 7, 2, 9)], 12), box(240, 90)], 24))
t.num('Ədədi rəqəmlərlə yazın: bir milyon yüz min on.', [1100010], vstack([words('bir milyon yüz min on'), box(260, 90)], 24))

# ============================================================ 192
t = T(192, 'Natural ədədlərin müqayisəsi',
      'Rəqəmlərinin sayı çox olan natural ədəd böyükdür. Rəqəmlərinin sayı eyni olan ədədləri soldan başlayaraq mərtəbə-mərtəbə müqayisə edirik: 3 456 789 < 3 465 789.',
      vstack([txt('70 001 > 9 999', 60, INK), hstack([txt('3 4', 60, INK), txt('5', 60, RED), txt('6 789 < 3 4', 60, INK), txt('6', 60, RED), txt('5 789', 60, INK)], 0)], 20))
t.sign('Ədədləri müqayisə edin. Dairələrə >, < və ya = yazın.', [('3 456 789', '3 465 789'), ('70 001', '69 999')], ['<', '>'])
t.sign('Ədədləri müqayisə edin. Dairələrə >, < və ya = yazın.', [('2 000 000', '1 999 999'), ('45 300', '45 030')], ['>', '>'])
t.choice('Ədədlərə kiçikdən böyüyə doğru sıra ilə toxunun.', ['54 210', '45 210', '54 120', '45 120'], [3, 1, 2, 0], mode='order', hint='Ədədlərə kiçikdən böyüyə sıra ilə toxunun.')
t.choice('Ən böyük ədədə toxunun.', ['909 090', '990 009', '909 900'], 1)
t.num('Bərabərsizliyin doğru olması üçün boş xanaya uyğun rəqəmi yazın.', [9], hstack([txt('5 7', 70, INK), box(76, 86), txt('3 > 5 789', 70, INK)], 6))
t.num('3 498 və 3 502 ədədləri arasında neçə natural ədəd var?', [3], vstack([hstack([nchip('3 498'), txt('...', 60, GREY), nchip('3 502')], 16), box(110, 90)], 24))
t.choice('Hansı ədəd 450 000 ilə 460 000 arasındadır? Toxunun.', ['455 500', '465 000', '445 900'], 0)
t.choice('Ədədlərə böyükdən kiçiyə doğru sıra ilə toxunun.', ['1 010', '1 100', '1 001', '1 110'], [3, 1, 0, 2], mode='order', hint='Ədədlərə böyükdən kiçiyə sıra ilə toxunun.')
t.num('Rəqəmləri müxtəlif olan ən böyük dördrəqəmli ədədi yazın.', [9876], box(220, 90))
t.choice('Ən kiçik ədədə toxunun.', ['100 000', '99 999', '100 001'], 1)

# ============================================================ 193
t = T(193, 'Natural ədədlərin yuvarlaqlaşdırılması',
      'Ədədi yuvarlaqlaşdırarkən həmin mərtəbədən sağdakı rəqəmə baxırıq. O rəqəm 0, 1, 2, 3, 4-dürsə, mərtəbədəki rəqəm dəyişmir; 5, 6, 7, 8, 9-dursa, bir vahid artır. Sağdakı rəqəmlər sıfırla əvəz olunur: 4 678 ≈ 4 700.',
      hstack([txt('4 6', 70, INK), txt('7', 70, RED), txt('8 ≈ 4 700', 70, INK)], 0))
for n_, place, ans in [(4678, 'onluqlara', 4680), (4678, 'yüzlüklərə', 4700), (35499, 'minliklərə', 35000), (2456789, 'yüz minliklərə', 2500000), (7951, 'yüzlüklərə', 8000)]:
    t.num('Ədədi %s qədər yuvarlaqlaşdırın.' % place, [ans], hstack([txt(f(n_), 70, INK), txt('≈', 70, BLUE), box(230, 90)], 14))
t.choice('Hansı ədəd minliklərə qədər yuvarlaqlaşdırıldıqda 6 000 alınır? Toxunun.', ['5 499', '6 512', '5 620'], 2)
t.num('Qatar 389 km yol getdi. Bu ədədi onluqlara qədər yuvarlaqlaşdırın.', [390], story(['🚆'], ['389', '≈', BOX]))
t.num('Ədədləri yüzlüklərə qədər yuvarlaqlaşdırın və cəmi təxmini hesablayın.', [700], FX('412', '+', '289', '≈', '400', '+', '300', '=', BOX, size=52))
t.num('Ədəd onluqlara qədər yuvarlaqlaşdırılıb və 750 alınıb. Bu ola biləcək ən böyük natural ədədi yazın.', [754], FX(BOX, '≈', 750, size=64))
t.num('Ədəd onluqlara qədər yuvarlaqlaşdırılıb və 750 alınıb. Bu ola biləcək ən kiçik natural ədədi yazın.', [745], FX(BOX, '≈', 750, size=64))

# ============================================================ 194
t = T(194, 'Natural ədədlərin toplanması və çıxılması',
      'Çoxrəqəmli ədədləri toplayarkən və çıxarkən eyni mərtəbələri bir-birinin altında yazırıq və hesablamanı təkliklərdən başlayırıq. Toplananların yerini dəyişdikdə cəm dəyişmir.',
      vstack([txt('345 678 + 254 322 = 600 000', 52, INK), txt('254 322 + 345 678 = 600 000', 52, GREY)], 16))
ncalc(t, 'Hesablayın.', [345678, '+', 254322], 600000, size=52)
ncalc(t, 'Hesablayın.', [1000000, '−', 456789], 543211, size=52)
ncalc(t, 'Hesablayın.', [70305, '−', 8497], 61808)
t.num('Boş xanaya uyğun ədədi yazın.', [26544], FX(BOX, '+', 23456, '=', 50000))
t.num('Boş xanaya uyğun ədədi yazın.', [54500], FX(84300, '−', BOX, '=', 29800))
ncalc(t, 'Əlverişli üsulla hesablayın.', [2375, '+', 1999, '+', 625], 4999)
t.num('Kitabxanada 12 450 kitab var idi. 3 780 kitab gətirildi, 2 150 kitab məktəblərə verildi. Kitabxanada neçə kitab oldu?', [14080], story(['📚', '📦', '🏫'], [BOX, 'kitab']))
t.choice('Hansı cəm 10 000-dən böyükdür? Toxunun.', ['4 567 + 5 432', '6 080 + 3 950', '7 999 + 2 000'], 1)
t.num('Boş xanaya uyğun ədədi yazın.', [456], FX(456, '+', 389, '=', 389, '+', BOX))
t.num('Avtomobil birinci gün 485 km, ikinci gün birinci gündən 127 km az yol getdi. İki gündə neçə km yol getdi?', [843], story(['🚗', '🛣️'], [BOX, 'km']))

# ============================================================ 195
t = T(195, 'Natural ədədin kvadratı və kubu',
      'Ədədin kvadratı onun özünə vurulmasıdır: 5² = 5 · 5 = 25. Ədədin kubu onun üç dəfə özünə vurulmasıdır: 2³ = 2 · 2 · 2 = 8. Kvadratın sahəsi tərəfin kvadratına, kubun həcmi tilin kubuna bərabərdir.',
      vstack([txt('5² = 5 · 5 = 25', 60, INK), txt('2³ = 2 · 2 · 2 = 8', 60, INK)], 18))
for b_, p_, v in [(7, 2, 49), (4, 3, 64), (12, 2, 144), (10, 3, 1000)]:
    ncalc(t, 'Hesablayın.', [sup(b_, p_)], v, size=70)
ncalc(t, 'Hesablayın.', [sup(5, 2), '+', sup(3, 3)], 52, size=64)
t.choice('Hansı ədəd bir natural ədədin kvadratıdır? Toxunun.', ['48', '81', '90'], 1)
t.num('Tərəfi 9 sm olan kvadratın sahəsini tapın.', [81], vstack([rect_sides(4, 4, '9 sm', '9 sm', 34), FX('S', '=', BOX, size=52)], 16)); ck(t, suf='sm²')
t.num('Tili 3 sm olan kubun həcmini tapın.', [27], vstack([box3d(4, 4, 4, 30, labels=('3 sm', '3 sm', '3 sm')), FX('V', '=', BOX, size=52)], 16)); ck(t, suf='sm³')
t.num('Boş xanaya uyğun ədədi yazın.', [11], hstack([box(100, 90), txt('² = 121', 70, INK)], 4))
ncalc(t, 'Hesablayın.', ['(2 + 3)²'], 25, size=70)

# ============================================================ 196
t = T(196, 'Natural ədədlərin vurulması və bölünməsi',
      'Vurmanı yoxlamaq üçün hasili vuruqlardan birinə bölürük. Bölməni yoxlamaq üçün qisməti bölənə vururuq: 9 072 : 9 = 1 008, çünki 1 008 · 9 = 9 072.',
      vstack([txt('9 072 : 9 = 1 008', 60, INK), txt('1 008 · 9 = 9 072', 60, GREY)], 16))
ncalc(t, 'Hesablayın.', [3045, '·', 6], 18270)
ncalc(t, 'Hesablayın.', [248, '·', 35], 8680)
ncalc(t, 'Əlverişli üsulla hesablayın.', [125, '·', 8, '·', 37], 37000)
ncalc(t, 'Hesablayın.', [9072, ':', 9], 1008)
ncalc(t, 'Hesablayın.', [14400, ':', 120], 120)
ncalc(t, 'Hesablayın.', [6384, ':', 24], 266)
t.num('Boş xanaya uyğun ədədi yazın.', [80], FX(BOX, '·', 15, '=', 1200))
t.num('Qalıqlı bölməni yerinə yetirin. Əvvəl qisməti, sonra qalığı yazın.', [14, 2], FX(100, ':', 7, '=', BOX, '(qalıq', BOX, ')', size=54), disp='14 (qalıq 2)')
t.num('Məktəb 24 sinfin hər birinə 32 dəftər aldı. Məktəb cəmi neçə dəftər aldı?', [768], story(['📓', '🏫'], [BOX, 'dəftər']))
t.num('1 260 kitabı hər rəfə 45 kitab olmaqla düzdülər. Neçə rəf lazım oldu?', [28], story(['📚', '🗄️'], [BOX, 'rəf']))

# ============================================================ 197
t = T(197, 'Ədədi ifadələr',
      'Mötərizəsiz ifadədə əvvəl qüvvətə yüksəltmə, sonra vurma və bölmə, ən sonda toplama və çıxma yerinə yetirilir. Mötərizə varsa, əvvəl mötərizənin içindəki əməllər edilir: 48 − 6 · 7 = 6, (48 − 6) · 7 = 294.',
      vstack([txt('48 − 6 · 7 = 6', 60, INK), txt('(48 − 6) · 7 = 294', 60, INK)], 16))
ncalc(t, 'İfadənin qiymətini tapın.', ['48 − 6 · 7'], 6, size=60)
ncalc(t, 'İfadənin qiymətini tapın.', ['(48 − 6) · 7'], 294, size=60)
ncalc(t, 'İfadənin qiymətini tapın.', ['120 : (15 − 3) + 8'], 18, size=56)
ncalc(t, 'İfadənin qiymətini tapın.', ['2³ + 4 · 5'], 28, size=60)
ncalc(t, 'İfadənin qiymətini tapın.', ['100 − 64 : 8 · 3'], 76, size=56)
t.choice('Hansı ifadənin qiyməti 30-a bərabərdir? Toxunun.', ['5 + 5 · 5', '(5 + 1) · 6', '40 − 5 · 3'], 0)
ncalc(t, 'İfadənin qiymətini tapın.', ['3 · (24 − 4²)'], 24, size=60)
t.num('Ana hər kiloqramı 3 manat olan 5 kq alma aldı və satıcıya 20 manat verdi. Ana nə qədər qalıq aldı?', [5], story(['🍎', '💵'], ['20 − 5 · 3', '=', BOX, 'manat'])); ck(t, suf='manat')
t.choice('Hansı ifadənin qiyməti 36-dır? Toxunun.', ['(2 + 4) · 6', '2 + 4 · 6', '2 + (4 · 6)'], 0)
ncalc(t, 'İfadənin qiymətini tapın.', ['7 · 25 · 4 − 600 : 6'], 600, size=52)

# ============================================================ 198
t = T(198, 'Ədədin bölənləri və bölünənləri',
      'Ədədi qalıqsız bölən ədədə onun böləni deyilir: 3 ədədi 12-nin bölənidir. Ədədə qalıqsız bölünən ədədə onun bölünəni deyilir: 12 ədədi 3-ün bölünənidir. Ədədin rəqəmlərinin cəmi 3-ə bölünürsə, ədəd 3-ə; 9-a bölünürsə, ədəd 9-a bölünür.',
      vstack([txt('12 : 3 = 4', 64, INK), txt('12-nin bölənləri: 1, 2, 3, 4, 6, 12', 40, GREY)], 16))
t.choice('36 ədədinin bölənlərinin hamısına toxunun.', ['4', '5', '9', '12', '16', '18'], [0, 2, 3, 5], mode='multi')
t.choice('7-yə qalıqsız bölünən ədədlərin hamısına toxunun.', ['42', '54', '63', '71', '84'], [0, 2, 4], mode='multi')
t.num('15 ədədinin neçə böləni var?', [4], vstack([txt('15', 90, INK), box(100, 90)], 20))
t.num('50-dən kiçik olan və 12-yə bölünən ən böyük ədədi yazın.', [48], box(130, 90))
t.choice('Hansı ədəd həm 2-yə, həm də 5-ə bölünür? Toxunun.', ['255', '520', '352'], 1)
t.choice('Hansı ədəd 3-ə bölünür? Rəqəmlərin cəmini tapın və toxunun.', ['421', '522', '701'], 1)
t.choice('Hansı ədəd 9-a bölünür? Toxunun.', ['3 609', '2 707', '4 505'], 0)
t.num('6 ədədinin 10-dan böyük və 20-dən kiçik neçə bölünəni var?', [2], vstack([txt('6, 12, 18, ...', 60, INK), box(100, 90)], 20))
t.num('Üçrəqəmli ədəd 9-a bölünür. Boş xanaya uyğun rəqəmi yazın.', [3], hstack([txt('1', 80, INK), box(80, 92), txt('5', 80, INK)], 6))
t.num('32 konfeti uşaqlar arasında bərabər paylamaq olur. Uşaqların sayı 5-dən çox, 10-dan azdır. Neçə uşaq var?', [8], story(['🍬', '👧', '👦'], [BOX, 'uşaq']))

# ============================================================ 200
t = T(200, 'Kəsrlərin müqayisəsi və sıralanması',
      'Məxrəcləri müxtəlif olan kəsrləri müqayisə etmək üçün onları ortaq məxrəcə gətiririk: 2/3 = 8/12, 3/4 = 9/12, deməli, 2/3 < 3/4.',
      vstack([FX((2, 3), '=', (8, 12), size=50), FX((3, 4), '=', (9, 12), size=50), FX((2, 3), '<', (3, 4), size=50)], 14))
t.sign('Kəsrləri müqayisə edin. Dairələrə >, < və ya = yazın.', [('5/7', '3/7'), ('2/9', '2/5')], ['>', '<'])
t.sign('Kəsrləri müqayisə edin. Dairələrə >, < və ya = yazın.', [('3/4', '5/8'), ('2/3', '4/6')], ['>', '='])
t.choice('Ən böyük kəsrə toxunun.', ['5/12', '1/2', '7/12'], 2)
t.choice('Kəsrlərə kiçikdən böyüyə doğru sıra ilə toxunun.', ['3/4', '1/2', '5/8', '3/8'], [3, 1, 2, 0], mode='order', hint='Kəsrlərə kiçikdən böyüyə sıra ilə toxunun.')
t.num('Kəsri 12 məxrəcinə gətirin. Boş xanaya surəti yazın.', [8], FX((2, 3), '=', (BOX, 12), size=64))
t.num('Kəsri 12 məxrəcinə gətirin. Boş xanaya surəti yazın.', [9], FX((3, 4), '=', (BOX, 12), size=64))
t.choice('1-dən böyük olan kəsrə toxunun.', ['7/8', '9/8', '8/9'], 1)
t.sign('Qarışıq ədədləri müqayisə edin. Dairələrə >, < və ya = yazın.', [('2 1/3', '1 5/6'), ('3 1/4', '3 1/2')], ['>', '<'])
t.choice('Hansı kəsr 1/2 ilə 1 arasındadır? Toxunun.', ['2/5', '3/4', '1/3'], 1)
t.choice('Aynur yolun 3/5 hissəsini, Elxan isə 7/10 hissəsini getdi. Kim çox yol getdi? Toxunun.', ['Aynur', 'Elxan'], 1, stem=story(['👧', '👦', '🛤️']))

# ============================================================ 201
t = T(201, 'Məxrəcləri müxtəlif olan kəsrlərin toplanması və çıxılması',
      'Məxrəcləri müxtəlif olan kəsrləri toplamaq və ya çıxmaq üçün onları ortaq məxrəcə gətiririk, sonra surətləri toplayır və ya çıxırıq: 1/2 + 1/3 = 3/6 + 2/6 = 5/6.',
      FX((1, 2), '+', (1, 3), '=', (3, 6), '+', (2, 6), '=', (5, 6), size=50))
ADD = 'Hesablayın. Cavabı ixtisar olunmuş kəsr şəklində yazın.'
for a_, op, b_ in [((1, 2), '+', (1, 3)), ((3, 4), '−', (1, 6)), ((2, 5), '+', (3, 10)), ((5, 6), '−', (1, 4)), ((3, 8), '+', (1, 4)), ((7, 9), '−', (1, 3)), ((1, 6), '+', (1, 3))]:
    x = Fr(*a_) + Fr(*b_) if op == '+' else Fr(*a_) - Fr(*b_)
    fcalc(t, ADD, [a_, op, b_], x, size=60)
t.num('1/4 və 1/6 kəsrlərinin ən kiçik ortaq məxrəcini yazın.', [12], hstack([fr(1, 4, 56), fr(1, 6, 56), txt('→', 60, GREY), box(110, 90)], 24))
fanswer(t, 'Bağın 1/3 hissəsinə pomidor, 1/4 hissəsinə xiyar əkildi. Bağın hansı hissəsi əkildi?', Fr(7, 12), story(['🍅', '🥒'], [(1, 3), '+', (1, 4), '=', (BOX, BOX)]))
fanswer(t, 'Bağın 7/12 hissəsi əkilib. Bağın hansı hissəsi boş qalıb?', Fr(5, 12), story(['🌱'], [1, '−', (7, 12), '=', (BOX, BOX)]))

# ============================================================ 202
t = T(202, 'Qarışıq ədədlərin toplanması',
      'Qarışıq ədədləri toplamaq üçün tam hissələri ayrıca, kəsr hissələri ayrıca toplayırıq. Kəsr hissə düzgün olmayan kəsr alınarsa, ondan tam hissə ayırırıq: 3 2/7 + 4 6/7 = 7 8/7 = 8 1/7.',
      FX((3, 2, 7), '+', (4, 6, 7), '=', (7, 8, 7), '=', (8, 1, 7), size=48))
MIX = 'Hesablayın. Cavabı qarışıq ədəd və ya natural ədəd şəklində yazın.'
for a_, b_ in [((2, 1, 5), (1, 3, 5)), ((3, 2, 7), (4, 6, 7)), ((1, 1, 2), (2, 1, 3)), ((2, 3, 4), (1, 5, 8)), (5, (2, 3, 8)), ((4, 2, 3), (1, 3)), ((1, 5, 6), (2, 1, 4)), ((3, 1, 6), (2, 1, 3))]:
    va = Fr(a_) if isinstance(a_, int) else (Fr(a_[0], a_[1]) if len(a_) == 2 else a_[0] + Fr(a_[1], a_[2]))
    vb = Fr(b_) if isinstance(b_, int) else (Fr(b_[0], b_[1]) if len(b_) == 2 else b_[0] + Fr(b_[1], b_[2]))
    fcalc(t, MIX, [a_, '+', b_], va + vb, size=54)
t.choice('Hansı cəm 4-ə bərabərdir? Toxunun.', ['1 1/2 + 2 1/2', '2 1/3 + 1 1/3', '3 1/4 + 1/2'], 0)
fanswer(t, 'Anar birinci gün 2 1/2 km, ikinci gün 3 3/4 km qaçdı. İki gündə neçə km qaçdı?', Fr(25, 4), story(['🏃', '🛣️'], [BOX, (BOX, BOX), 'km']))


def mv(a_):
    return Fr(a_) if isinstance(a_, int) else (Fr(a_[0], a_[1]) if len(a_) == 2 else a_[0] + Fr(a_[1], a_[2]))


# ============================================================ 203
t = T(203, 'Qarışıq ədədlərin çıxılması',
      'Qarışıq ədədləri çıxarkən tam hissələri ayrıca, kəsr hissələri ayrıca çıxırıq. Azalanın kəsr hissəsi kiçikdirsə, onun tam hissəsindən bir vahid ayırırıq: 4 1/4 = 3 5/4, 3 5/4 − 1 3/4 = 2 2/4 = 2 1/2.',
      vstack([FX((4, 1, 4), '=', (3, 5, 4), size=48), FX((3, 5, 4), '−', (1, 3, 4), '=', (2, 1, 2), size=48)], 14))
for a_, b_ in [((5, 4, 7), (2, 1, 7)), (6, (2, 3, 5)), ((4, 1, 4), (1, 3, 4)), ((5, 1, 3), (2, 1, 2)), ((7, 5, 6), (3, 1, 4)), (3, (1, 8)), ((8, 2, 9), 5)]:
    fcalc(t, MIX, [a_, '−', b_], mv(a_) - mv(b_), size=54)
t.num('Boş xanaya uyğun ədədi yazın.', [6], FX((4, 1, 5), '=', (3, BOX, 5), size=64))
fanswer(t, 'Lentin uzunluğu 6 1/2 m idi. Ondan 2 3/4 m kəsdilər. Neçə metr lent qaldı?', Fr(15, 4), story(['🎀', '✂️'], [BOX, (BOX, BOX), 'm']))
fanswer(t, 'Səbətdə 10 kq meyvə var idi. Əvvəl 3 1/2 kq, sonra 2 1/4 kq götürdülər. Səbətdə neçə kiloqram meyvə qaldı?', Fr(17, 4), story(['🧺', '🍐'], [BOX, (BOX, BOX), 'kq']))

# ============================================================ 204
t = T(204, 'Adi kəsrlərin vurulması',
      'Kəsrləri vurmaq üçün surəti surətə, məxrəci məxrəcə vururuq: 2/3 · 4/5 = 8/15. Mümkün olduqda vurmadan əvvəl ixtisar edirik. Kəsri natural ədədə vurduqda surəti həmin ədədə vururuq.',
      FX((2, 3), '·', (4, 5), '=', ('2 · 4', '3 · 5'), '=', (8, 15), size=50))
MUL = 'Hesablayın. Cavabı ixtisar olunmuş şəkildə yazın.'
for a_, b_ in [((2, 3), (4, 5)), ((3, 4), (2, 9)), ((5, 6), (3, 10)), ((3, 7), 14), (4, (5, 12)), ((7, 8), (8, 7))]:
    fcalc(t, MUL, [a_, '·', b_], mv(a_) * mv(b_), size=58)
fcalc(t, MUL, ['(', (2, 3), ')²'], Fr(4, 9), size=58)
t.choice('Hansı hasil 1-dən kiçikdir? Toxunun.', ['3/4 · 5/3', '2/3 · 3/4', '6/5 · 5/4'], 1)
fanswer(t, 'Düzbucaqlının uzunluğu 3/4 m, eni 2/3 m-dir. Onun sahəsini tapın.', Fr(1, 2), vstack([rect_sides(6, 4, '3/4 m', '2/3 m', 30), FX('S', '=', (BOX, BOX), 'm²', size=46)], 14))
fanswer(t, '1 m parça 6 manatdır. 3/4 m parça neçə manatdır?', Fr(9, 2), story(['🧵', '💰'], [6, '·', (3, 4), '=', BOX, (BOX, BOX)]))

# ============================================================ 205
t = T(205, 'Qarışıq ədədlərin vurulması',
      'Qarışıq ədədləri vurmaq üçün onları düzgün olmayan kəsr şəklində yazırıq, sonra kəsrləri vururuq: 1 1/3 · 1 1/2 = 4/3 · 3/2 = 2.',
      FX((1, 1, 3), '·', (1, 1, 2), '=', (4, 3), '·', (3, 2), '=', 2, size=48))
for a_, b_ in [((1, 1, 2), (2, 3)), ((2, 1, 4), 4), ((1, 1, 3), (1, 1, 2)), ((2, 2, 5), (5, 6)), ((3, 1, 2), (2, 1, 7)), ((1, 2, 3), (3, 10)), ((2, 1, 2), (2, 1, 2))]:
    fcalc(t, MUL, [a_, '·', b_], mv(a_) * mv(b_), size=54)
fanswer(t, 'Bir qutu peçenyenin kütləsi 2 1/4 kq-dır. 6 belə qutunun kütləsi nə qədərdir?', Fr(27, 2), story(['📦', '🍪'], [BOX, (BOX, BOX), 'kq']))
fanswer(t, 'Velosipedçi saatda 12 km sürətlə 1 3/4 saat getdi. O, neçə km yol getdi?', 21, story(['🚴', '⏱️'], [BOX, 'km']))
fcalc(t, MUL, [(4, 1, 2), '·', (2, 9)], 1, size=58)

# ============================================================ 206
t = T(206, 'Adi kəsrlərin bölünməsi',
      'Kəsri kəsrə bölmək üçün bölünəni bölənin tərs kəsrinə vururuq: 2/5 : 4/7 = 2/5 · 7/4 = 7/10. 3/4 kəsrinin tərsi 4/3 kəsridir.',
      FX((2, 5), ':', (4, 7), '=', (2, 5), '·', (7, 4), '=', (7, 10), size=50))
DIV = 'Hesablayın. Cavabı ixtisar olunmuş şəkildə yazın.'
for a_, b_ in [((3, 4), (3, 8)), ((2, 5), (4, 7)), ((5, 6), 5), (6, (3, 4)), ((7, 9), (14, 27)), ((8, 15), (4, 5))]:
    fcalc(t, DIV, [a_, ':', b_], mv(a_) / mv(b_), size=58)
frac_num(t, 'Verilən kəsrin tərs kəsrini yazın.', (5, 3), FX((3, 5), '→', (BOX, BOX), size=64))
t.choice('Hansı qismət 1-dən böyükdür? Toxunun.', ['1/2 : 3/4', '3/4 : 1/2', '2/3 : 5/6'], 1)
t.num('3/4 litr şirəni 1/8 litrlik stəkanlara tökdülər. Neçə stəkan doldu?', [6], story(['🧃', '🥛'], [(3, 4), ':', (1, 8), '=', BOX]))
fanswer(t, '2/3 kq konfeti 4 uşağa bərabər payladılar. Hər uşağa neçə kiloqram konfet düşdü?', Fr(1, 6), story(['🍬', '👧', '👦'], [(2, 3), ':', 4, '=', (BOX, BOX)]))

# ============================================================ 207
t = T(207, 'Qarışıq ədədlərin bölünməsi',
      'Qarışıq ədədləri bölmək üçün onları düzgün olmayan kəsr şəklində yazırıq və bölünəni bölənin tərs kəsrinə vururuq: 4 1/2 : 1 1/2 = 9/2 : 3/2 = 9/2 · 2/3 = 3.',
      FX((4, 1, 2), ':', (1, 1, 2), '=', (9, 2), '·', (2, 3), '=', 3, size=48))
for a_, b_ in [((2, 1, 2), 5), ((4, 1, 2), (1, 1, 2)), ((3, 1, 3), (5, 6)), ((1, 3, 4), (2, 1, 3)), (6, (1, 1, 5)), ((5, 1, 4), 3), ((2, 2, 3), (1, 7, 9))]:
    fcalc(t, DIV, [a_, ':', b_], mv(a_) / mv(b_), size=54)
t.num('7 1/2 m məftili 2 1/2 m-lik hissələrə böldülər. Neçə hissə alındı?', [3], story(['🧶', '✂️'], [BOX, 'hissə']))
t.num('Avtomobil 150 km yolu 2 1/2 saata getdi. Onun sürəti saatda neçə km idi?', [60], story(['🚗', '⏱️'], [BOX, 'km/saat']))
fcalc(t, DIV, [(3, 3, 5), ':', (9, 10)], 4, size=58)

# ============================================================ 208
t = T(208, 'Ədədin hissəsinin və hissəsinə görə ədədin tapılması',
      'Ədədin hissəsini tapmaq üçün ədədi həmin kəsrə vururuq: 60-ın 2/3 hissəsi 60 · 2/3 = 40. Hissəsinə görə ədədi tapmaq üçün verilən ədədi kəsrə bölürük: 1/4 hissəsi 12 olan ədəd 12 : 1/4 = 48.',
      vstack([FX(60, '·', (2, 3), '=', 40, size=50), FX(12, ':', (1, 4), '=', 48, size=50)], 16))
t.num('60 ədədinin 2/3 hissəsini tapın.', [40], FX(60, '·', (2, 3), '=', BOX))
t.num('45 ədədinin 3/5 hissəsini tapın.', [27], FX(45, '·', (3, 5), '=', BOX))
t.num('1/4 hissəsi 12 olan ədədi tapın.', [48], FX(12, ':', (1, 4), '=', BOX))
t.num('2/5 hissəsi 18 olan ədədi tapın.', [45], FX(18, ':', (2, 5), '=', BOX))
t.num('Sinifdə 28 şagird var. Onların 3/7 hissəsi qızdır. Sinifdə neçə qız var?', [12], story(['🧑‍🏫', '👧'], [BOX, 'qız']))
t.num('Kitab 240 səhifədir. Onun 5/8 hissəsi oxunub. Neçə səhifə oxunmayıb?', [90], story(['📖'], [BOX, 'səhifə']))
t.num('Elxan pulunun 3/4 hissəsi ilə 15 manata top aldı. Elxanın nə qədər pulu var idi?', [20], story(['⚽', '👦'], [BOX, 'manat']))
t.num('Yolun 2/9 hissəsi 14 km-dir. Bütün yolun uzunluğunu tapın.', [63], story(['🛣️'], [BOX, 'km']))
t.choice('Hansı daha böyükdür? Toxunun.', ['20-nin 3/4 hissəsi', '24-ün 2/3 hissəsi', '30-un 1/2 hissəsi'], 1)
t.num('Bağda 36 ağac var. Onların 5/12 hissəsi alma ağacıdır. Bağda neçə alma ağacı var?', [15], story(['🌳', '🍎'], [BOX, 'ağac']))

# ============================================================ 210
t = T(210, 'Onluq kəsrlərin müqayisəsi və sıralanması',
      'Onluq kəsrləri müqayisə etmək üçün əvvəl tam hissələri, sonra ondabirləri, yüzdəbirləri və s. müqayisə edirik. Onluq kəsrin sağına sıfır yazdıqda kəsr dəyişmir: 0,8 = 0,80.',
      vstack([txt('3,47 < 3,5', 64, INK), txt('0,8 = 0,80', 64, INK)], 16))
t.sign('Onluq kəsrləri müqayisə edin. Dairələrə >, < və ya = yazın.', [('3,47', '3,5'), ('0,80', '0,8')], ['<', '='])
t.sign('Onluq kəsrləri müqayisə edin. Dairələrə >, < və ya = yazın.', [('12,305', '12,35'), ('7,09', '7,1')], ['<', '<'])
t.choice('Ən böyük ədədə toxunun.', ['0,7', '0,69', '0,701'], 2)
t.choice('Ədədlərə kiçikdən böyüyə doğru sıra ilə toxunun.', ['2,15', '2,5', '2,051', '2,105'], [2, 3, 0, 1], mode='order', hint='Ədədlərə kiçikdən böyüyə sıra ilə toxunun.')
t.num('Bərabərsizliyin doğru olması üçün boş xanaya yazıla bilən ən kiçik rəqəmi yazın.', [8], hstack([txt('4,', 70, INK), box(76, 86), txt('7 > 4,86', 70, INK)], 6))
t.choice('Hansı ədəd 3,4 ilə 3,5 arasındadır? Toxunun.', ['3,45', '3,54', '3,05'], 0)
t.choice('Elxanın boyu 1,35 m, Anarın boyu 1,4 m-dir. Kim daha hündürdür? Toxunun.', ['Elxan', 'Anar'], 1, stem=story(['👦', '📏', '👦']))
t.sign('Onluq kəsrləri müqayisə edin. Dairələrə >, < və ya = yazın.', [('0,099', '0,1'), ('6,6', '6,060')], ['<', '>'])
t.choice('Ədədlərə böyükdən kiçiyə doğru sıra ilə toxunun.', ['0,5', '0,55', '0,505', '0,055'], [1, 2, 0, 3], mode='order', hint='Ədədlərə böyükdən kiçiyə sıra ilə toxunun.')
t.choice('Ən kiçik ədədə toxunun.', ['9,99', '10,01', '9,909'], 2)

# ============================================================ 211
t = T(211, 'Onluq kəsrlərin yuvarlaqlaşdırılması',
      'Onluq kəsri yuvarlaqlaşdırarkən həmin mərtəbədən sağdakı rəqəmə baxırıq: 5-dən kiçikdirsə, mərtəbə dəyişmir, 5 və ya ondan böyükdürsə, bir vahid artır. Sağdakı rəqəmlər atılır: 3,47 ≈ 3,5.',
      hstack([txt('3,4', 70, INK), txt('7', 70, RED), txt(' ≈ 3,5', 70, INK)], 0))
for x_, place, ans in [('3,47', 'ondabirlərə', '3,5'), ('12,349', 'yüzdəbirlərə', '12,35'), ('8,6', 'tam hissəyə', '9'), ('0,754', 'ondabirlərə', '0,8'), ('4,0951', 'mindəbirlərə', '4,095'), ('19,52', 'tam hissəyə', '20'), ('0,0461', 'yüzdəbirlərə', '0,05'), ('7,28', 'ondabirlərə', '7,3')]:
    danswer(t, 'Ədədi %s qədər yuvarlaqlaşdırın.' % place, Dm(ans.replace(',', '.')), DEC(x_, '≈', dbox(Dm(ans.replace(',', '.'))), size=64))
t.choice('Hansı ədəd ondabirlərə qədər yuvarlaqlaşdırıldıqda 2,4 alınır? Toxunun.', ['2,45', '2,36', '2,34'], 1)
t.num('Qaçışçı 100 metri 12,68 saniyəyə qaçdı. Bu vaxtı tam saniyələrə qədər yuvarlaqlaşdırın.', [13], story(['🏃', '⏱️'], ['12,68', '≈', BOX]))

# ============================================================ 212
t = T(212, 'Adi kəsrin onluq kəsrə və onluq kəsrin adi kəsrə çevrilməsi',
      'Adi kəsri onluq kəsrə çevirmək üçün onu məxrəci 10, 100, 1000 olan kəsr şəklində yazırıq və ya surəti məxrəcə bölürük: 3/4 = 75/100 = 0,75. Onluq kəsri adi kəsr şəklində yazıb ixtisar edirik: 0,6 = 6/10 = 3/5.',
      vstack([FX((3, 4), '=', (75, 100), '=', '0,75', size=50), FX('0,6', '=', (6, 10), '=', (3, 5), size=50)], 14))
DEC1 = 'Adi kəsri onluq kəsr şəklində yazın.'
for a_, d_ in [((3, 4), '0.75'), ((2, 5), '0.4'), ((7, 20), '0.35'), ((1, 8), '0.125')]:
    danswer(t, DEC1, Dm(d_), hstack([fr(*a_, 60), txt('=', 64, BLUE), DEC('BOX2')], 16))
ADI = 'Onluq kəsri adi kəsr şəklində yazın və ixtisar edin.'
for x_, v in [('0,6', Fr(3, 5)), ('0,25', Fr(1, 4)), ('2,5', Fr(5, 2))]:
    fanswer(t, ADI, v, FX(x_, '=', *ansbox(v), size=62))
danswer(t, 'Qarışıq ədədi onluq kəsr şəklində yazın.', Dm('1.12'), hstack([mixed(1, 3, 25, 58), txt('=', 64, BLUE), DEC('BOX2')], 16))
t.choice('Hansı kəsr onluq kəsrə çevrildikdə 0,5 alınır? Toxunun.', ['5/100', '4/8', '5/9'], 1)
fanswer(t, ADI, Fr(1, 8), FX('0,125', '=', (BOX, BOX), size=62))

# ============================================================ 213
t = T(213, 'Onluq kəsrlərin toplanması və çıxılması',
      'Onluq kəsrləri toplamaq və çıxmaq üçün onları vergül vergülün altında olmaqla yazırıq, natural ədədlər kimi toplayır və ya çıxırıq, cavabda vergülü həmin yerdə qoyuruq: 3,45 + 2,70 = 6,15.',
      vstack([txt('  3,45', 60, INK), txt('+ 2,70', 60, INK), txt('  6,15', 60, BLUE)], 6, 'right'))
CAL = 'Hesablayın.'
for a_, op, b_ in [('3.45', '+', '2.7'), ('12.6', '−', '4.85'), ('0.375', '+', '1.625'), ('10', '−', '3.47'), ('7.08', '+', '12.9')]:
    v = Dm(a_) + Dm(b_) if op == '+' else Dm(a_) - Dm(b_)
    dcalc(t, CAL, [dfmt(Dm(a_)), op, dfmt(Dm(b_))], v, size=60)
danswer(t, 'Boş xanaya uyğun ədədi yazın.', Dm('2.65'), DEC('BOX2', '+', '2,35', '=', '5', size=60))
danswer(t, 'Ana 2,5 kq alma və 1,75 kq armud aldı. Ana cəmi neçə kiloqram meyvə aldı?', Dm('4.25'), vstack([story(['🍎', '🍐']), DEC('BOX2', 'kq', size=50)], 20))
danswer(t, 'Lentin uzunluğu 5,2 m idi. Ondan 1,85 m kəsdilər. Neçə metr lent qaldı?', Dm('3.35'), vstack([story(['🎀', '✂️']), DEC('BOX2', 'm', size=50)], 20))
dcalc(t, CAL, ['8,4', '−', '2,75', '+', '1,35'], Dm('7'), size=56)
t.choice('Hansı cəm 1-ə bərabərdir? Toxunun.', ['0,5 + 0,05', '0,25 + 0,75', '0,9 + 0,01'], 1)

# ============================================================ 214
t = T(214, 'Onluq kəsrlərin 10, 100, 1000-ə vurulması və bölünməsi',
      'Onluq kəsri 10, 100, 1000-ə vurduqda vergülü sıfırların sayı qədər sağa, böldükdə isə sola keçiririk: 3,45 · 10 = 34,5; 7,5 : 100 = 0,075.',
      vstack([txt('3,45 · 10 = 34,5', 60, INK), txt('7,5 : 100 = 0,075', 60, INK)], 16))
for a_, op, b_ in [('3.45', '·', 10), ('0.072', '·', 100), ('5.6', '·', 1000), ('48.3', ':', 10), ('7.5', ':', 100), ('0.9', ':', 1000)]:
    v = Dm(a_) * b_ if op == '·' else Dm(a_) / b_
    dcalc(t, CAL, [dfmt(Dm(a_)), op, f(b_)], v, size=60)
t.num('Boş xanaya uyğun ədədi yazın.', [100], DEC('2,4', '·', BOX, '=', '240', size=62))
danswer(t, 'Boş xanaya uyğun ədədi yazın.', Dm('5.6'), DEC('BOX2', ':', '10', '=', '0,56', size=62))
t.num('Bir dəftər 0,45 manatdır. 100 dəftər neçə manatdır?', [45], story(['📓', '💰'], [BOX, 'manat']))
t.num('Uzunluğu metrlə ifadə edin.', [3700], hstack([txt('3,7 km', 64, INK), txt('=', 64, BLUE), box(200, 86), txt('m', 56, GREY)], 14))

# ============================================================ 215
t = T(215, 'Onluq kəsrin natural ədədə vurulması',
      'Onluq kəsri natural ədədə vurmaq üçün vergülə fikir vermədən vururuq, sonra hasildə sağdan kəsrdəki qədər rəqəmi vergüllə ayırırıq: 0,35 · 6 = 2,10 = 2,1.',
      txt('0,35 · 6 = 2,10 = 2,1', 60, INK))
for a_, b_ in [('2.4', 3), ('0.35', 6), ('1.25', 8), ('4.07', 5), ('0.125', 12), ('3.6', 15)]:
    dcalc(t, CAL, [dfmt(Dm(a_)), '·', str(b_)], Dm(a_) * b_, size=62)
danswer(t, '1 kq alma 1,8 manatdır. 4 kq alma neçə manatdır?', Dm('7.2'), vstack([story(['🍎', '⚖️']), DEC('BOX2', 'manat', size=50)], 20))
danswer(t, 'Kvadratın tərəfi 2,5 sm-dir. Onun perimetrini tapın.', Dm('10'), vstack([rect_sides(4, 4, '2,5 sm', '', 30), FX('P', '=', BOX, 'sm', size=50)], 16))
dcalc(t, CAL, ['6', '·', '0,7'], Dm('4.2'), size=62)
t.choice('Hansı hasil 1-dən böyükdür? Toxunun.', ['0,12 · 8', '0,3 · 4', '0,24 · 4'], 1)

# ============================================================ 216
t = T(216, 'Onluq kəsrlərin vurulması',
      'Onluq kəsrləri vurmaq üçün vergülə fikir vermədən vururuq, sonra hasildə sağdan hər iki vuruqda vergüldən sonra nə qədər rəqəm varsa, o qədər rəqəmi vergüllə ayırırıq: 1,5 · 0,4 = 0,60 = 0,6.',
      txt('1,5 · 0,4 = 0,60 = 0,6', 60, INK))
for a_, b_ in [('0.3', '0.2'), ('1.5', '0.4'), ('2.5', '1.2'), ('0.05', '0.7'), ('3.2', '2.5'), ('1.1', '1.1')]:
    dcalc(t, CAL, [dfmt(Dm(a_)), '·', dfmt(Dm(b_))], Dm(a_) * Dm(b_), size=62)
dcalc(t, CAL, ['0,6²'], Dm('0.36'), size=66)
danswer(t, 'Düzbucaqlının ölçüləri 4,5 m və 2,4 m-dir. Onun sahəsini tapın.', Dm('10.8'), vstack([rect_sides(6, 4, '4,5 m', '2,4 m', 30), DEC('S', '=', 'BOX2', 'm²', size=50)], 16))
danswer(t, '1 litr süd 1,2 manatdır. 2,5 litr süd neçə manatdır?', Dm('3'), story(['🥛', '💰'], [BOX, 'manat']))
t.choice('Hansı hasil 0,12-yə bərabərdir? Toxunun.', ['0,4 · 0,3', '4 · 0,3', '0,4 · 3'], 0)

# ============================================================ 217
t = T(217, 'Onluq kəsrin natural ədədə bölünməsi',
      'Onluq kəsri natural ədədə bölmək üçün natural ədədlər kimi bölürük və tam hissənin bölünməsi qurtaran kimi qismətdə vergül qoyuruq: 8,4 : 4 = 2,1. Lazım olsa, bölünənin sağına sıfır yazırıq: 3 : 8 = 0,375.',
      vstack([txt('8,4 : 4 = 2,1', 60, INK), txt('3 : 8 = 0,375', 60, INK)], 16))
for a_, b_ in [('8.4', 4), ('7.5', 3), ('0.96', 8), ('4.5', 6), ('3', 8), ('12.6', 14), ('0.35', 5)]:
    dcalc(t, CAL, [dfmt(Dm(a_)), ':', str(b_)], Dm(a_) / b_, size=62)
danswer(t, '5 kq kartof 9,5 manatdır. 1 kq kartof neçə manatdır?', Dm('1.9'), vstack([story(['🥔', '⚖️']), DEC('BOX2', 'manat', size=50)], 20))
danswer(t, '7,2 m lenti 6 bərabər hissəyə böldülər. Hər hissənin uzunluğu nə qədərdir?', Dm('1.2'), vstack([story(['🎀', '✂️']), DEC('BOX2', 'm', size=50)], 20))
dcalc(t, 'İfadənin qiymətini tapın.', ['(2,4 + 3,3 + 3,6) : 3'], Dm('3.1'), size=52)

# ============================================================ 218
t = T(218, 'Ədədin onluq kəsrə bölünməsi',
      'Ədədi onluq kəsrə bölmək üçün bölünəndə və böləndə vergülü bölənin vergüldən sonrakı rəqəmlərinin sayı qədər sağa keçiririk və natural ədədə bölürük: 4,8 : 0,6 = 48 : 6 = 8.',
      txt('4,8 : 0,6 = 48 : 6 = 8', 60, INK))
for a_, b_ in [('6', '0.2'), ('4.8', '0.6'), ('0.56', '0.7'), ('1.44', '1.2'), ('3', '0.25'), ('0.09', '0.03'), ('10.5', '1.5')]:
    dcalc(t, CAL, [dfmt(Dm(a_)), ':', dfmt(Dm(b_))], Dm(a_) / Dm(b_), size=62)
t.num('4,5 litr südü 0,25 litrlik stəkanlara tökdülər. Neçə stəkan doldu?', [18], story(['🥛', '🥤'], [BOX, 'stəkan']))
danswer(t, '1,2 kq alma 2,16 manatdır. 1 kq alma neçə manatdır?', Dm('1.8'), vstack([story(['🍎', '💰']), DEC('BOX2', 'manat', size=50)], 20))
t.num('Boş xanaya uyğun ədədi yazın.', [7], DEC(BOX, '·', '0,4', '=', '2,8', size=62))

# ============================================================ 219
t = T(219, 'Adi və onluq kəsrlər üzərində əməllər',
      'Adi və onluq kəsrlər bir ifadədə olarsa, onları eyni şəklə gətiririk: ya hamısını onluq kəsr, ya da hamısını adi kəsr şəklində yazırıq: 1/2 + 0,3 = 0,5 + 0,3 = 0,8.',
      FX((1, 2), '+', '0,3', '=', '0,5', '+', '0,3', '=', '0,8', size=52))
ON = 'Hesablayın. Cavabı onluq kəsr və ya natural ədəd şəklində yazın.'
danswer(t, ON, Dm('0.8'), FX((1, 2), '+', '0,3', '=', BOX, ',', BOX, size=60))
danswer(t, ON, Dm('0.5'), FX((3, 4), '−', '0,25', '=', BOX, ',', BOX, size=60))
danswer(t, ON, Dm('0.5'), FX('0,6', '·', (5, 6), '=', BOX, ',', BOX, size=60))
danswer(t, ON, Dm('10'), FX('2,5', ':', (1, 4), '=', BOX, size=60))
danswer(t, ON, Dm('3.5'), FX((1, 1, 5), '+', '2,3', '=', BOX, ',', BOX, size=60))
danswer(t, ON, Dm('7'), FX('(0,4', '+', (3, 5), ')', '·', 7, '=', BOX, size=56))
danswer(t, ON, Dm('1'), FX('0,75', '·', (4, 3), '=', BOX, size=60))
danswer(t, 'Ana 1/2 kq yağ və 0,75 kq pendir aldı. Ana cəmi neçə kiloqram məhsul aldı? Onluq kəsr şəklində yazın.', Dm('1.25'), vstack([story(['🧈', '🧀']), DEC('BOX2', 'kq', size=50)], 20))
danswer(t, ON, Dm('3'), FX('(3,6', '−', (1, 1, 2), ')', ':', '0,7', '=', BOX, size=52))
t.choice('Hansı kəsr 0,2-yə bərabərdir? Toxunun.', ['1/5', '2/100', '1/2'], 0)

# ============================================================ 221
t = T(221, 'Ədədin faizi',
      'Ədədin faizini tapmaq üçün faizi onluq kəsr şəklində yazıb ədədi ona vururuq: 200-ün 15%-i 200 · 0,15 = 30. Ədədi 100-ə bölüb faizin sayına vurmaq da olar: 200 : 100 · 15 = 30.',
      vstack([txt('200 · 0,15 = 30', 60, INK), txt('200 : 100 · 15 = 30', 52, GREY)], 16))
for n_, p_ in [(200, 15), (80, 25), (60, 10), (350, 4), (45, 20), (1200, 75)]:
    t.num('%s ədədinin %d%%-ni tapın.' % (f(n_), p_), [n_ * p_ // 100], hstack([txt('%d%%' % p_, 64, INK), txt('·', 64, BLUE), txt(f(n_), 64, INK), txt('=', 64, BLUE), box(150, 86)], 14))
t.num('Sinifdə 25 şagird var. Onların 40%-i oğlandır. Sinifdə neçə oğlan var?', [10], story(['🧑‍🏫', '👦'], [BOX, 'oğlan']))
t.num('Velosipedin qiyməti 80 manatdır. Ona 15% endirim edildi. Endirim neçə manatdır?', [12], story(['🚲', '🏷️'], [BOX, 'manat']))
t.choice('Hansı daha böyükdür? Toxunun.', ['50-nin 50%-i', '80-in 25%-i', '200-ün 10%-i'], 0)
danswer(t, '9 ədədinin 50%-ni tapın.', Dm('4.5'), DEC('50%', '·', '9', '=', 'BOX2', size=64))

# ============================================================ 222
t = T(222, 'Faizinə görə ədədin tapılması',
      'Faizinə görə ədədi tapmaq üçün verilən ədədi faizin onluq kəsr şəklinə bölürük: 25%-i 12 olan ədəd 12 : 0,25 = 48. Və ya ədədi faizin sayına bölüb 100-ə vururuq: 12 : 25 · 100 = 48.',
      vstack([txt('12 : 0,25 = 48', 60, INK), txt('12 : 25 · 100 = 48', 52, GREY)], 16))
for p_, v in [(10, 7), (25, 12), (20, 9), (50, 34), (75, 30), (4, 2)]:
    t.num('%d%%-i %d olan ədədi tapın.' % (p_, v), [v * 100 // p_], vstack([txt('%d%% → %d' % (p_, v), 64, INK), FX('100%', '→', BOX, size=64)], 16))
t.num('Kitabın 30%-i 60 səhifədir. Kitab neçə səhifədir?', [200], story(['📖'], [BOX, 'səhifə']))
t.num('Elxan pulunun 40%-ni xərclədi. Bu, 8 manatdır. Elxanın nə qədər pulu var idi?', [20], story(['👦', '💵'], [BOX, 'manat']))
t.num('Yolun 15%-i 45 km-dir. Bütün yolun uzunluğunu tapın.', [300], story(['🛣️'], [BOX, 'km']))
t.choice('Hansı ədədin 10%-i 5-dir? Toxunun.', ['15', '50', '500'], 1)

# ============================================================ 223
t = T(223, 'Kəmiyyətin faizlə artırılması və azaldılması',
      'Ədədi 10% artırmaq üçün onun 110%-ni tapırıq: 80 · 1,1 = 88. Ədədi 25% azaltmaq üçün onun 75%-ni tapırıq: 200 · 0,75 = 150.',
      vstack([txt('80 + 10% = 88', 60, INK), txt('200 − 25% = 150', 60, INK)], 16))
for n_, op, p_ in [(80, '+', 10), (200, '−', 25), (50, '+', 20), (120, '−', 30), (1000, '+', 5)]:
    v = n_ * (100 + p_) // 100 if op == '+' else n_ * (100 - p_) // 100
    t.num('%s ədədini %d%% %s.' % (f(n_), p_, 'artırın' if op == '+' else 'azaldın'), [v], hstack([txt(f(n_), 64, INK), txt(op + ' %d%%' % p_, 64, BLUE), txt('=', 64, BLUE), box(170, 86)], 14))
t.num('Köynəyin qiyməti 40 manat idi. Qiyməti 15% endirildi. Köynəyin yeni qiyməti nə qədərdir?', [34], story(['👕', '🏷️'], [BOX, 'manat']))
t.num('Bağda 60 ağac var idi. Ağacların sayı 20% artdı. Bağda neçə ağac oldu?', [72], story(['🌳'], [BOX, 'ağac']))
pct_num(t, 'Qiymət 100 manatdan 120 manata qalxdı. Qiymət neçə faiz artdı?', 20, vstack([story(['📈'], ['100', '→', '120']), hstack([box(110, 80), txt('%', 60, INK)], 8)], 18))
pct_num(t, 'Qiymət 80 manatdan 60 manata endi. Qiymət neçə faiz azaldı?', 25, vstack([story(['📉'], ['80', '→', '60']), hstack([box(110, 80), txt('%', 60, INK)], 8)], 18))
t.choice('Hansı endirim daha çoxdur? Toxunun.', ['60 manatın 10%-i', '40 manatın 20%-i', '100 manatın 5%-i'], 1)

TOPICS.sort(key=lambda x: x.n)
save()
