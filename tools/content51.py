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

save()
