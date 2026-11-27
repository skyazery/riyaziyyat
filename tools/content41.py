"""4-cü sinif riyaziyyat, 1-ci hissə: 28 mövzu (143–170), hər mövzuda 10 tapşırıq.
Run: python3 tools/content41.py [OUTDIR]   (default ~/riyaziyyat/4-1)"""
import os, sys
from bookgen import *

init(sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser('~/riyaziyyat/4-1'))
import bookgen


def cmp_col(pairs, size=62):
    """müqayisə cütləri alt-alta (çoxrəqəmli ədədlər yan-yana sığmır)"""
    rows_ = [hstack([txt(a, size), sign_slot(int(size * 1.15)), txt(b, size)], int(size * 0.3)) for a, b in pairs]
    return vstack(rows_, int(size * 0.35))


bookgen.cmp_row = cmp_col


def f(n):
    """325236 → '325 236' (şəkillərdə siniflər arasında boşluq)"""
    s = str(n)
    if len(s) < 4:
        return s
    out = ''
    while len(s) > 3:
        out = ' ' + s[-3:] + out
        s = s[:-3]
    return s + out


E = lambda *t: expr2([x if x is BOX or not isinstance(x, int) else f(x) for x in t], 60)
HEADS6 = ('Yüzminl.', 'Onminl.', 'Minl.', 'Yüzl.', 'Onl.', 'Təkl.')
CLS_COL = [(255, 236, 179)] * 3 + [(187, 222, 251)] * 3


def class_table(vals, size=30, values=None):
    """iki sinifli mərtəbə cədvəli: Minliklər sinfi | Təkliklər sinfi"""
    cells = [box(int(size * 1.6), int(size * 1.5)) if v is None else txt(str(v), size + 26, INK) for v in vals]
    rows_ = [[txt(h, size - 8, BLUE) for h in HEADS6], cells]
    if values:
        rows_.append([txt(f(v), size - 12, GREY) for v in values])
    tb = table(rows_, int(size * 2.6))
    head = hstack([chip('Minliklər sinfi', size - 4, (255, 236, 179), INK, ORANGE), chip('Təkliklər sinfi', size - 4, (187, 222, 251), INK, BLUE)], 30)
    return vstack([head, tb], 10)


def big(n, size=70, color=BLUE):
    return txt(f(n), size, color)


# ============================================================ 143
t = T(143, 'Çoxrəqəmli ədədlər',
      'Çoxrəqəmli ədədlərdə rəqəmlər sağdan üç-üç qruplaşdırılır. Hər qrup sinif adlanır: təkliklər sinfi və minliklər sinfi. 325 236 ədədində 3 yüzminlik, 2 onminlik, 5 minlik, 2 yüzlük, 3 onluq və 6 təklik var.',
      vstack([class_table([3, 2, 5, 2, 3, 6], 30, [300000, 20000, 5000, 200, 30, 6]), txt('325 236', 66, BLUE)], 14))
t.num('Mərtəbə cədvəlinə baxın. Ədədi rəqəmlərlə yazın.', [439527], vstack([class_table([4, 3, 9, 5, 2, 7], 30), hstack([arrow(), box(330, 100)], 14)], 16), disp='439 527')
t.num('Mərtəbə cədvəlinə baxın. Ədədi rəqəmlərlə yazın.', [702338], vstack([class_table([7, 0, 2, 3, 3, 8], 30), hstack([arrow(), box(330, 100)], 14)], 16), disp='702 338')
t.num('Cəmə uyğun ədədi yazın.', [325236], vstack([E(300000, '+', 20000, '+', 5000, '+'), E(200, '+', 30, '+', 6, '=', BOX)], 14, 'left'), disp='325 236')
t.num('Ədədi açıq şəkildə yazanda boş xanaya hansı ədəd yazılır?', [80], vstack([E(457088, '='), E(400000, '+', 50000, '+', 7000, '+', BOX, '+', 8)], 14, 'left'))
t.choice('«İyirmi beş min üç yüz» hansı ədəddir? Dairəyə alın.', ['25 300', '25 030', '250 300'], 0)
t.choice('«Altı yüz otuz üç min iki yüz on bir» hansı ədəddir? Dairəyə alın.', ['633 211', '630 211', '633 201'], 0)
t.choice('712 635 ədədində 1 rəqəmi hansı mərtəbədədir? Dairəyə alın.', ['Onminliklər', 'Minliklər', 'Yüzminliklər'], 0, stem=hstack([txt('7', 80), txt('1', 80, RED), txt('2 635', 80)], 4))
t.num('Boş xanaya uyğun ədədi yazın: 15 000-də neçə minlik var?', [15], hstack([big(15000, 70, INK), txt('=', 70, BLUE), box(), txt('minlik', 50, GREY)], 16))
t.num('Qanunauyğunluğu tapın. Növbəti ədədi yazın.', [40312], hstack([seq([f(37312), f(38312), f(39312)], 46), box(260, 96)], 14), disp='40 312')
t.num('Ən böyük altırəqəmli ədədi yazın.', [999999], hstack([txt('? ? ? ? ? ?', 60, GREY), arrow(), box(330, 100)], 20), disp='999 999')

# ============================================================ 144
t = T(144, 'Müqayisə və sıralama',
      'Rəqəmlərinin sayı çox olan ədəd böyükdür: 10 042 > 9 435. Rəqəmlərinin sayı eyni olanda müqayisə ən yüksək mərtəbədən başlanır: 14 328 < 14 426, çünki 3 yüzlük 4 yüzlükdən azdır.',
      vstack([E(10042, '>', 9435), hstack([txt('14 ', 60), txt('3', 60, RED), txt('28', 60), txt('<', 60, BLUE), txt('14 ', 60), txt('4', 60, RED), txt('26', 60)], 6)], 14))
t.sign('Ədədləri müqayisə edin. Dairələrə >, < və ya = yazın.', [('6 741', '30 737'), ('73 038', '73 083')], ['<', '<'])
t.sign('Ədədləri müqayisə edin. Dairələrə işarə yazın.', [('677 011', '667 011'), ('999 999', '1 000 000')], ['>', '<'])
cities = tab([['Şəhər', 'Məsafə (km)'], ['İstanbul', '1 794'], ['Mayami', '11 058'], ['London', '4 440'], ['Tehran', '542']], 30)
t.choice('Cədvəldə Bakıdan şəhərlərə qədər uçuş məsafəsi verilib. Bakıya ən yaxın şəhər hansıdır? Dairəyə alın.', ['İstanbul', 'Mayami', 'London', 'Tehran'], 3, stem=hstack([em('✈️', 90), cities], 20))
t.choice('Ən böyük ədədi dairəyə alın.', ['22 105', '21 305', '181 321'], 2)
t.choice('Ən kiçik ədədi dairəyə alın.', ['76 345', '76 353', '67 844'], 2)
t.choice('Ədədləri artan sıra ilə düzün: ən kiçikdən başlayaraq toxunun.', ['3 429', '16 003', '6 045'], [0, 2, 1], mode='order', hint='Əvvəlcə ən kiçik ədədə toxunun.', disp='3 429, 6 045, 16 003')
t.choice('Ədədləri azalan sıra ilə düzün: ən böyükdən başlayaraq toxunun.', ['986 121', '548 622', '846 212'], [0, 2, 1], mode='order', hint='Əvvəlcə ən böyük ədədə toxunun.', disp='986 121, 846 212, 548 622')
planets = tab([['Planet', 'Dövr (gün)'], ['Saturn', '10 759'], ['Neptun', '60 182'], ['Yupiter', '4 355']], 30)
t.choice('Günəşə yaxın planet onun ətrafında dövrü daha az gündə vurur. Hansı planet Günəşə ən yaxındır? Dairəyə alın.', ['Saturn', 'Neptun', 'Yupiter'], 2, stem=hstack([em('🪐', 90), planets], 20))
t.num('Boş xanaya uyğun ədədi yazın.', [100000], E(99999, '<', BOX, '<', 100001), disp='100 000')
t.num('9, 0, 4, 7 və 2 rəqəmləri ilə ən böyük beşrəqəmli ədədi yazın. Rəqəmlər təkrarlanmır.', [97420], hstack([nchip(9), nchip(0), nchip(4), nchip(7), nchip(2), arrow(), box(260, 100)], 12), disp='97 420')

# ============================================================ 145
t = T(145, 'Yuvarlaqlaşdırma',
      'Yuvarlaqlaşdırılacaq mərtəbədəki rəqəmin sağındakı rəqəmə baxırıq. Bu rəqəm 5-dən kiçikdirsə, mərtəbədəki rəqəm dəyişmir, 5 və ya 5-dən böyükdürsə, 1 artır. Sağdakı bütün rəqəmlər sıfırla əvəz olunur: 32 318 ≈ 32 000, 276 925 ≈ 280 000.',
      vstack([eqbox(['32 318', '≈', '32 000'], 56), eqbox(['276 925', '≈', '280 000'], 56)], 14))
for n_, ans, where in [(18799, 19000, 'minliklərə'), (23983, 24000, 'minliklərə'), (55350, 55000, 'minliklərə'),
                       (56185, 60000, 'onminliklərə'), (211462, 210000, 'onminliklərə'), (6823, 6800, 'yüzlüklərə'), (479208, 500000, 'yüzminliklərə')]:
    t.num('Ədədi %s qədər yuvarlaqlaşdırın.' % where, [ans], eqbox([f(n_), '≈', BOX], 66), disp=f(ans))
t.choice('Hansı ədədi onminliklərə qədər yuvarlaqlaşdıranda 50 000 alınır? Dairəyə alın.', ['44 532', '49 096', '55 350'], 1)
t.num('Ayla Yer arasındakı ən yaxın məsafə 363 300 km-dir. Bu ədədi minliklərə qədər yuvarlaqlaşdırın.', [363000], vstack([hstack([em('🌍', 90), txt('363 300 km', 54, BLUE), em('🌙', 70)], 16), eqbox(['363 300', '≈', BOX], 60)], 14), disp='363 000')
t.choice('Stadion 6 750 tamaşaçı tutur. Bu ədədi minliklərə qədər yuvarlaqlaşdırın. Dairəyə alın.', ['7 000', '6 000', '6 800'], 0, stem=hstack([em('🏟️', 100), txt('6 750', 66, BLUE)], 16))

save()
