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


def vcolg(a, b, op='+', size=50):
    """alt-alta toplama/çıxma/vurma; siniflər arasında boşluq, cavab xanası enli"""
    fo = font(size)
    cw = int(fo.getlength('0')) + 6
    gap = int(cw * 0.45)
    res = {'+': a + b, '−': a - b, '·': a * b}[op]
    nd = max(len(str(a)), len(str(b)), len(str(res)))
    xs = []
    x = 0
    for k in range(nd):          # k = sağdan mövqe
        if k and k % 3 == 0:
            x += gap
        x += cw
        xs.append(x)
    w = xs[-1] + cw + 30
    im, d = vec(w + 24, int(size * 3.9))
    ff = font(size * S)
    for r, s_ in enumerate([str(a), str(b)]):
        for k, ch in enumerate(reversed(s_)):
            d.text(((w - xs[k]) * S, (r * size * 1.2 + 4) * S), ch, font=ff, fill=INK)
    d.text((4 * S, (size * 0.62) * S), '×' if op == '·' else op, font=ff, fill=BLUE)
    ly = size * 2.5
    d.line([cw * 0.5 * S, ly * S, (w + 8) * S, ly * S], fill=INK, width=5 * S)
    im = done(im)
    k = len(str(res))
    bw = xs[k - 1] + 22
    bx = box(int(bw), int(size * 1.3))
    im.alpha_composite(bx, (int(w + 12 - bx.width), int(ly + 10)))
    return im


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

# ============================================================ 146
def L(*rows_):
    return vstack([E(*r) for r in rows_], 14, 'left')


t = T(146, 'Çoxrəqəmli ədədlərin toplanması',
      'Çoxrəqəmli ədədləri alt-alta toplayanda eyni mərtəbədəki rəqəmləri bir-birinin altında yazırıq və təkliklərdən başlayırıq. Cəm 10 və ya daha böyük olanda soldakı mərtəbəyə 1 əlavə olunur: 44 134 + 7 628 = 51 762.',
      E(44134, '+', 7628, '=', 51762))
for a, b in [(6255, 542), (54184, 9703), (247916, 35853), (476357, 362652)]:
    t.num('Alt-alta toplayın.', [a + b], vcolg(a, b, '+'), disp=f(a + b))
t.num('Cəmi şifahi tapın.', [12000], E(4000, '+', 8000, '=', BOX), disp='12 000')
t.num('Cəmi şifahi tapın.', [35500], E(32500, '+', 3000, '=', BOX), disp='35 500')
t.num('Cəmi tapın.', [100006], E(99999, '+', 7, '=', BOX), disp='100 006')
t.num('Marian çökəkliyinin dərinliyi 11 034 m, Everest zirvəsinin hündürlüyü 8 848 m-dir. Ən uca zirvə ən dərin nöqtədən neçə metr hündürdür?', [19882],
      vstack([hstack([em('🏔️', 90), txt('8 848 m', 50, BLUE), em('🌊', 80), txt('11 034 m', 50, BLUE)], 14), E(8848, '+', 11034, '=', BOX)], 14), disp='19 882')
t.choice('Hansı cəm düzgün hesablanıb? Dairəyə alın.', ['63 594', '88 227', '63 584'], 0, stem=E(60857, '+', 2737, '='))
t.num('6, 4, 1 və 2 kartları ilə ən böyük və ən kiçik dördrəqəmli ədədləri düzəldin. Onların cəmini yazın.', [7667],
      vstack([hstack([nchip(6), nchip(4), nchip(1), nchip(2)], 12), E(6421, '+', 1246, '=', BOX)], 14), disp='7 667')

# ============================================================ 147
t = T(147, 'Çoxrəqəmli ədədlərin çıxılması',
      'Çoxrəqəmli ədədləri alt-alta çıxanda təkliklərdən başlayırıq. Çıxmaq mümkün olmadıqda soldakı mərtəbədən 1 vahid ayırıb 10 vahid kimi əlavə edirik: 36 235 − 14 363 = 21 872.',
      E(36235, '−', 14363, '=', 21872))
for a, b in [(5687, 3568), (79863, 47973), (588267, 67083), (761426, 661512)]:
    t.num('Alt-alta çıxın.', [a - b], vcolg(a, b, '−'), disp=f(a - b))
t.num('Fərqi tapın.', [1248], E(8000, '−', 6752, '=', BOX), disp='1 248')
t.num('Fərqi şifahi tapın.', [33000], E(38000, '−', 5000, '=', BOX), disp='33 000')
t.num('Fərqi şifahi tapın.', [90000], E(100000, '−', 10000, '=', BOX), disp='90 000')
t.num('1-ci Dünya müharibəsi 1914-cü ildə başlayıb, 1918-ci ildə sona çatıb. Neçə il davam edib?', [4], vstack([hstack([txt('1914', 60, BLUE), arrow(), txt('1918', 60, BLUE)], 14), E(1918, '−', 1914, '=', BOX)], 14))
t.num('Anarın atasının hesabında 18 970 manat var. O, 17 750 manatlıq maşını alsa, nə qədər pulu qalar?', [1220],
      vstack([hstack([em('🚗', 100), txt('17 750 man', 54, BLUE)], 14), E(18970, '−', 17750, '=', BOX)], 14), disp='1 220')
t.choice('54 432 − 22 253 = 32 179. Fərqi hansı toplama ilə yoxlamaq olar? Dairəyə alın.', ['32 179 + 22 253', '32 179 + 54 432', '22 253 + 54 432'], 0)

# ============================================================ 148
t = T(148, 'Toplama və çıxmanın digər üsulları',
      'Əvəzləmə üsulunda toplananlardan birini yuvarlaq ədədə tamamlayırıq: 1 999 + 112 = 2 000 + 111 = 2 111. Fərqdə isə hər iki ədədə eyni ədədi əlavə edirik: 2 312 − 997 = 2 315 − 1 000 = 1 315.',
      L((1999, '+', 112, '=', 2000, '+', 111), (2312, '−', 997, '=', 2315, '−', 1000)))
t.num('Əvəzləmə üsulu ilə hesablayın. Boş xanaya uyğun ədədi yazın.', [111], E(1999, '+', 112, '=', 2000, '+', BOX))
t.num('Əvəzləmə üsulu ilə hesablayın. Boş xanalara uyğun ədədləri yazın.', [3200, 3475], L((274, '+', 3201, '='), (275, '+', BOX, '=', BOX)), disp='3 200, 3 475')
t.num('Əvəzləmə üsulu ilə hesablayın. Boş xanaya uyğun ədədi yazın.', [1000], E(2312, '−', 997, '=', 2315, '−', BOX), disp='1 000')
t.num('Əvəzləmə üsulu ilə hesablayın.', [40404], L((49400, '−', 8996, '='), (49404, '−', 9000, '=', BOX)), disp='40 404')
t.num('Cəmi əvəzləmə üsulu ilə tapın.', [2826], E(427, '+', 2399, '=', BOX), disp='2 826')
t.num('Fərqi əvəzləmə üsulu ilə tapın.', [4228], E(4426, '−', 198, '=', BOX), disp='4 228')
t.num('Cəmi hissə-hissə tapın.', [3779], L((2471, '+', 1308, '='), (2471, '+', 1000, '+', 300, '+', 8, '=', BOX)), disp='3 779')
t.num('Ədədləri yüzlüklərə qədər yuvarlaqlaşdırın və cəmi təqribi tapın.', [1900], L((1527, '+', 394, '≈'), (1500, '+', 400, '=', BOX)), disp='1 900')
t.num('Ədədləri minliklərə qədər yuvarlaqlaşdırın və cəmi təqribi tapın.', [7000], L((4799, '+', 2374, '≈'), (5000, '+', 2000, '=', BOX)), disp='7 000')
t.num('Bir stadion 114 000, digəri 100 024 azarkeş tutur. Birinci stadion təxminən neçə min çox azarkeş tutur?', [14],
      vstack([hstack([em('🏟️', 90), txt('114 000', 50, BLUE), txt('və', 40, GREY), txt('100 024', 50, BLUE)], 14), hstack([box(), txt('min', 50, GREY)], 12)], 14))

# ============================================================ 149
t = T(149, 'Dördrəqəmli ədədin birrəqəmli ədədə vurulması',
      'Alt-alta vuranda təkliklərdən başlayırıq: əvvəl təklikləri, sonra onluqları, yüzlükləri və minlikləri vururuq. Alınan onluqları növbəti mərtəbəyə əlavə edirik: 1 127 · 5 = 5 635.',
      E(1127, '·', 5, '=', 5635))
for a, b in [(903, 2), (3237, 2), (1035, 5), (4931, 8)]:
    t.num('Alt-alta vurun.', [a * b], vcolg(a, b, '·'), disp=f(a * b))
t.num('Hasili tapın.', [2900], E(725, '·', 4, '=', BOX), disp='2 900')
t.num('Hasili tapın.', [10175], E(2035, '·', 5, '=', BOX), disp='10 175')
t.num('Bir soyuducuya 425 dondurma yerləşir. Üç belə soyuducuya neçə dondurma yerləşər?', [1275], vstack([hstack([em('🍦', 90), txt('425', 60, BLUE)], 14), E(425, '·', 3, '=', BOX)], 14), disp='1 275')
t.choice('Hansı hasil düzgündür? Dairəyə alın.', ['13 808', '12 808', '13 208'], 0, stem=E(3452, '·', 4, '='))
t.num('Hasili tapın.', [25266], E(4211, '·', 6, '=', BOX), disp='25 266')
t.num('Fabrik bir gündə 1 250 cüt ayaqqabı hazırlayır. 6 gündə neçə cüt ayaqqabı hazırlayar?', [7500], vstack([hstack([em('👟', 90), txt('1 250', 60, BLUE)], 14), E(1250, '·', 6, '=', BOX)], 14), disp='7 500')

# ============================================================ 150
t = T(150, 'Çoxrəqəmli ədədin birrəqəmli ədədə vurulması',
      'Çoxrəqəmli ədədi birrəqəmli ədədə də eyni qayda ilə vururuq: mərtəbələri sağdan sola ardıcıl vururuq və alınan onluqları növbəti mərtəbəyə əlavə edirik: 21 354 · 3 = 64 062.',
      E(21354, '·', 3, '=', 64062))
for a, b in [(12413, 3), (25106, 4), (103251, 5), (47128, 6)]:
    t.num('Alt-alta vurun.', [a * b], vcolg(a, b, '·'), disp=f(a * b))
t.num('Hasili şifahi tapın.', [90000], E(30000, '·', 3, '=', BOX), disp='90 000')
t.num('Hasili şifahi tapın.', [60000], E(12000, '·', 5, '=', BOX), disp='60 000')
t.num('Hasili şifahi tapın.', [10000], E(2500, '·', 4, '=', BOX), disp='10 000')
t.num('Bir avtomobil 12 500 manatdır. 4 belə avtomobil neçə manatdır?', [50000], vstack([hstack([em('🚙', 90), txt('12 500 man', 54, BLUE)], 14), E(12500, '·', 4, '=', BOX)], 14), disp='50 000')
t.choice('Hasili təqribi tapın. Dairəyə alın.', ['15 000', '12 000', '20 000'], 0, stem=E(4987, '·', 3, '≈'))
t.num('Boş xanaya uyğun ədədi yazın.', [5000], E(BOX, ':', 4, '=', 1250), disp='5 000')

# ============================================================ 151
t = T(151, 'Dördrəqəmli ədədin birrəqəmli ədədə bölünməsi',
      'Sütun şəklində bölmədə ardıcıl olaraq minlikləri, yüzlükləri, onluqları və təklikləri bölürük: 5 384 : 4 = 1 346. Bölünəni hissələrə də ayırmaq olar: 4 000 : 4 + 1 200 : 4 + 160 : 4 + 24 : 4 = 1 000 + 300 + 40 + 6.',
      L((5384, ':', 4, '=', 1346), (1000, '+', 300, '+', 40, '+', 6, '=', 1346)))
t.num('Qisməti tapın.', [1346], E(5384, ':', 4, '=', BOX), disp='1 346')
t.num('Qisməti şifahi tapın.', [3000], E(6000, ':', 2, '=', BOX), disp='3 000')
t.num('Qisməti şifahi tapın.', [2000], E(8000, ':', 4, '=', BOX), disp='2 000')
t.num('Qisməti şifahi tapın.', [700], E(3500, ':', 5, '=', BOX))
t.num('Qisməti tapın.', [912], E(2736, ':', 3, '=', BOX))
t.num('Qisməti tapın.', [1449], E(7245, ':', 5, '=', BOX), disp='1 449')
t.num('Bölünəni hissələrə ayırın. Boş xanalara qismətləri yazın.', [1000, 300, 40, 6],
      vstack([E(5384, ':', 4, '='), E(4000, ':', 4, '+', 1200, ':', 4, '+'), E(160, ':', 4, '+', 24, ':', 4, '='), E(BOX, '+', BOX, '+', BOX, '+', BOX)], 12, 'left'), disp='1 000, 300, 40, 6')
t.num('Anbarda 3 630 tennis topu var. Toplar hərəsində 3 top olmaqla qablara yığıldı. Neçə qab alındı?', [1210], vstack([hstack([em('🎾', 90), txt('3 630', 60, BLUE)], 14), E(3630, ':', 3, '=', BOX)], 14), disp='1 210')
t.choice('Hansı bölmə düzgündür? Dairəyə alın.', ['1 212', '1 221', '1 122'], 0, stem=E(4848, ':', 4, '='))
t.num('Bölməni vurma ilə yoxlayın.', [5384], E(1346, '·', 4, '=', BOX), disp='5 384')

# ============================================================ 152
t = T(152, 'Çoxrəqəmli ədədin birrəqəmli ədədə bölünməsi',
      'Çoxrəqəmli ədədi birrəqəmli ədədə də eyni qayda ilə bölürük. Bölünənin ilk rəqəmi böləndən kiçikdirsə, ilk iki rəqəmi birlikdə bölürük: 25 632 : 8 = 3 204.',
      E(25632, ':', 8, '=', 3204))
for a, b in [(25632, 8), (48630, 6), (72450, 5), (125412, 3)]:
    t.num('Qisməti tapın.', [a // b], E(a, ':', b, '=', BOX), disp=f(a // b))
t.num('Qisməti şifahi tapın.', [20000], E(60000, ':', 3, '=', BOX), disp='20 000')
t.num('Qisməti şifahi tapın.', [90000], E(450000, ':', 5, '=', BOX), disp='90 000')
t.num('Qisməti şifahi tapın.', [9000], E(36000, ':', 4, '=', BOX), disp='9 000')
t.num('Fermer 12 600 kq kartofu 6 maşınla bərabər daşıdı. Hər maşın neçə kiloqram kartof daşıdı?', [2100], vstack([hstack([em('🚚', 90), txt('12 600 kq', 54, BLUE)], 14), E(12600, ':', 6, '=', BOX)], 14), disp='2 100')
t.choice('Qisməti təqribi tapın. Dairəyə alın.', ['4 000', '3 000', '40 000'], 0, stem=E(23950, ':', 6, '≈'))
t.num('Bölməni vurma ilə yoxlayın.', [48630], E(8105, '·', 6, '=', BOX), disp='48 630')

# ============================================================ 153
t = T(153, 'Ədədin bölənləri və bölünənləri',
      'Bir ədədin tam bölündüyü ədədə onun böləni deyilir: 6-nın bölənləri 1, 2, 3 və 6-dır. Bir ədədə tam bölünən ədədlər onun bölünənləridir: 3-ün bölünənləri 3, 6, 9, 12 və s. Yalnız iki böləni olan ədəd sadə ədəddir, məsələn, 7.',
      vstack([hstack([txt('6:', 56, BLUE), seq([1, 2, 3, 6], 50)], 14), hstack([txt('3:', 56, BLUE), seq([3, 6, 9, 12], 50), txt('…', 56)], 14)], 14))
t.choice('12 ədədinin bütün bölənlərinə toxunun.', ['1', '2', '3', '4', '5', '6', '8', '12'], [0, 1, 2, 3, 5, 7], mode='multi', disp='1, 2, 3, 4, 6, 12')
t.choice('32 ədədinin bölənlərinə toxunun.', ['4', '5', '6', '7', '8'], [0, 4], mode='multi', disp='4, 8')
t.choice('Sadə ədədlərə toxunun.', ['2', '9', '11', '15', '23', '49'], [0, 2, 4], mode='multi', disp='2, 11, 23')
t.choice('4-ün bölünənlərinə toxunun.', ['8', '10', '12', '14', '16', '18'], [0, 2, 4], mode='multi', disp='8, 12, 16')
t.num('18 ədədinin neçə böləni var?', [6], hstack([txt('18', 80, BLUE), arrow(), box(), txt('bölən', 46, GREY)], 14))
t.num('Sahəsi 24 m² olan xalçanın bir tərəfi 4 m-dir. Digər tərəfi neçə metrdir?', [6], vstack([rect_sides(6, 4, '?', '4 m', 40), E(24, ':', 4, '=', BOX)], 14))
t.choice('Hansı ədəd 5-in bölünənidir? Dairəyə alın.', ['35', '52', '43'], 0)
t.choice('Hansı ədəd 13-ün bölənidir? Dairəyə alın.', ['13', '3', '4'], 0)
t.num('20-dən kiçik ən böyük sadə ədədi yazın.', [19], hstack([txt('< 20', 66, BLUE), arrow(), box()], 14))
t.num('6-nın 30-dan kiçik ən böyük bölünənini yazın.', [24], hstack([seq([6, 12, 18, BOX], 50), txt('< 30', 56, BLUE)], 14))

# ============================================================ 154
t = T(154, 'Vurma və bölmənin digər üsulları',
      'Vuruğu cəm və ya fərq şəklində yazanda hesablamaq asanlaşır: 994 · 7 = (1 000 − 6) · 7 = 7 000 − 42 = 6 958. Bölünəni də hissələrə ayırmaq olar: 6 324 : 3 = 6 000 : 3 + 300 : 3 + 24 : 3 = 2 108.',
      L((994, '·', 7, '=', 7000, '−', 42, '=', 6958), (6324, ':', 3, '=', 2000, '+', 100, '+', 8)))
t.num('Boş xanalara uyğun ədədləri yazın.', [42, 6958], L((994, '·', 7, '=', '(1 000 − 6) · 7', '='), (7000, '−', BOX, '=', BOX)), disp='42, 6 958')
t.num('Boş xanalara uyğun ədədləri yazın.', [100, 4900], L((1225, '·', 4, '=', '(1 000 + 200 + 25) · 4'), ('=', 4000, '+', 800, '+', BOX, '=', BOX)), disp='100, 4 900')
t.num('Boş xanaya uyğun ədədi yazın.', [1130], L((226, '·', 5, '=', 113, '·', 2, '·', 5), ('=', 113, '·', 10, '=', BOX)), disp='1 130')
t.num('Hasili asan yolla tapın.', [1000], E(125, '·', 8, '=', BOX), disp='1 000')
t.num('Hasili asan yolla tapın.', [2300], E(460, '·', 5, '=', BOX), disp='2 300')
t.num('Boş xanaya uyğun ədədi yazın.', [1400], L((517, '·', 2, '+', 183, '·', 2), ('=', 700, '·', 2, '=', BOX)), disp='1 400')
t.num('İfadənin qiymətini asan yolla tapın.', [3200], E(655, '·', 4, '+', 145, '·', 4, '=', BOX), disp='3 200')
t.num('Boş xanalara uyğun ədədləri yazın.', [1, 799], L((3995, ':', 5, '=', '(4 000 − 5) : 5'), ('=', 800, '−', BOX, '=', BOX)))
t.num('Qisməti hissə-hissə tapın.', [2108], E(6324, ':', 3, '=', BOX), disp='2 108')
t.num('Bir kubun kütləsi 495 qramdır. 3 belə kub neçə qramdır?', [1485], vstack([hstack([em('🧊', 90), txt('495 q', 60, BLUE)], 14), E(495, '·', 3, '=', BOX)], 14), disp='1 485')

# ============================================================ 155
def Q(*toks, size=60):
    """hərfli ifadə: hərflər bənövşəyi, ədədlər siniflərə ayrılmış"""
    parts = []
    for t_ in toks:
        if t_ is BOX:
            parts.append(box(int(size * 1.35), int(size * 1.35)))
        elif isinstance(t_, int):
            parts.append(txt(f(t_), size, INK))
        elif len(t_) == 1 and t_.isalpha():
            parts.append(txt(t_, size, PURPLE))
        elif t_ in ('+', '−', '=', '>', '<', '·', ':', '≈', '(', ')'):
            parts.append(txt(t_, size, BLUE if t_ not in '()' else INK))
        else:
            parts.append(txt(t_, size, INK))
    return hstack(parts, gap=int(size * 0.24))


def QL(*rows_):
    return vstack([Q(*r) for r in rows_], 14, 'left')


t = T(155, 'Ədədi ifadələr',
      'İfadədə mötərizə varsa, əvvəlcə mötərizənin içindəki əməllər yerinə yetirilir. Sonra vurma və bölmə, ən sonda toplama və çıxma: (17 − 35 : 5) · 4 + 15 = 10 · 4 + 15 = 55.',
      QL(('(', 17, '−', 35, ':', 5, ')', '·', 4, '+', 15), ('=', 10, '·', 4, '+', 15, '=', 55)))
for toks, ans in [(('(', 350, '+', 10, ')', ':', 9, '−', 35), 5), (('(', 40, '−', 12, ')', '·', '(', 5, '+', 2, ')'), 196),
                  (('(', 150, '−', 6, ')', ':', 3, '+', 32), 80), ((60, '−', '(', 2, '·', 20, '−', 35, ')'), 55),
                  ((26, '+', 6, '·', 2, '−', 18), 20), ((241, '+', 143, '−', '(', 681, '−', 569, ')'), 272)]:
    t.num('İfadənin qiymətini tapın.', [ans], QL(toks, ('=', BOX)))
t.choice('Bu ifadədə hansı əməl birinci yerinə yetirilir? Dairəyə alın.', ['24 + 15', '30 − 24', '15 : 3'], 0, stem=Q(30, '−', '(', 24, '+', 15, ')', ':', 3, '+', 7))
t.num('Hər xonçaya 5 şəkərbura, 4 paxlava və 2 qoğal qoyuldu. Dörd belə xonçada neçə şirniyyat oldu?', [44], vstack([hstack([em('🍪', 80), em('🥮', 80), em('🥐', 80)], 12), Q('(', 5, '+', 4, '+', 2, ')', '·', 4, '=', BOX)], 14))
t.choice('Birinci bağlamada 3, ikincidə bundan iki dəfə çox yağ paketi var. Bir paket 200 qramdır. Hansı ifadə məsələyə uyğundur? Dairəyə alın.', ['(3 + 3 · 2) · 200', '(3 + 3) · 200', '3 · 2 + 3 · 200'], 0, stem=em('🧈', 100))
t.num('İki bağlamada cəmi neçə qram yağ var?', [1800], QL(('(', 3, '+', 3, '·', 2, ')', '·', 200, '='), (BOX, 'q')), disp='1 800')

# ============================================================ 156
t = T(156, 'Dəyişəni olan ifadələr',
      'Hərfi ifadədə dəyişənin yerinə onun qiymətini yazıb ifadənin qiymətini hesablayırıq: a = 15 və b = 3 olduqda a : 5 + 8 · b − 1 = 15 : 5 + 8 · 3 − 1 = 26.',
      QL(('a', '=', 15, ',', 'b', '=', 3), ('a', ':', 5, '+', 8, '·', 'b', '−', 1, '=', 26)))
t.num('a = 19 və b = 11 olduqda ifadənin qiymətini tapın.', [8], QL(('(', 5, '+', 'a', ')', ':', '(', 'b', '−', 8, ')'), ('=', BOX)))
t.num('a = 44 və b = 15 olduqda ifadənin qiymətini tapın.', [7], QL(('(', 5, '+', 'a', ')', ':', '(', 'b', '−', 8, ')'), ('=', BOX)))
t.num('a = 135 və b = 3 olduqda ifadənin qiymətini tapın.', [171], Q(108, ':', 'b', '+', 'a', '=', BOX))
t.num('m = 4 912 olduqda ifadənin qiymətini tapın.', [169446], QL(('m', '+', 164534), ('=', BOX)), disp='169 446')
t.num('n = 17 500 olduqda ifadənin qiymətini tapın.', [52024], QL((34524, '+', 'n'), ('=', BOX)), disp='52 024')
t.choice('4 · x ifadəsini cəm şəklində necə yazmaq olar? Dairəyə alın.', ['x + x + x + x', 'x + 4', '4 + 4 + 4 + 4'], 0)
t.choice('y + y + y + 2 cəmini hansı ifadə ilə yazmaq olar? Dairəyə alın.', ['3 · y + 2', 'y + 5', '3 + y + 2'], 0)
t.num('Üçbucağın tərəfləri a = 5 sm, b = 4 sm və c = 6 sm-dir. Perimetri neçə santimetrdir?', [15], vstack([tri([(0.0, 1.0), (1.0, 1.0), (0.75, 0.05)], ('c', 'b', 'a'), 220), Q('a', '+', 'b', '+', 'c', '=', BOX)], 14))
t.num('Düzbucaqlının eni a = 3 sm, uzunluğu b = 8 sm-dir. Onun sahəsi a · b neçə kvadrat santimetrdir?', [24], vstack([rect_sides(8, 3, 'b', 'a', 30), Q('a', '·', 'b', '=', BOX)], 14))
t.num('Ox qırmızı hissəyə düşəndə 2 xal, mavi hissəyə düşəndə 5 xal verilir. Ox x = 7 dəfə qırmızı, y = 3 dəfə mavi hissəyə düşdü. Neçə xal toplandı?', [29], vstack([em('🎯', 100), Q(2, '·', 'x', '+', 5, '·', 'y', '=', BOX)], 14))

# ============================================================ 157
t = T(157, 'Tənlik',
      'Məchul vuruğu tapmaq üçün hasili məlum vuruğa bölürük: 3 · x = 12, x = 12 : 3 = 4. Məchul bölünəni tapmaq üçün qisməti bölənə vururuq: x : 2 = 4, x = 8. Məchul böləni tapmaq üçün bölünəni qismətə bölürük: 30 : x = 5, x = 6.',
      QL((3, '·', 'x', '=', 12, '→', 'x', '=', 4), ('x', ':', 2, '=', 4, '→', 'x', '=', 8), (30, ':', 'x', '=', 5, '→', 'x', '=', 6)))
for toks, v, ans in [((7, '·', 'm', '=', 42), 'm', 6), (('a', '·', 6, '=', 54), 'a', 9), ((2, '·', 'z', '=', 972), 'z', 486),
                     (('d', ':', 8, '=', 12), 'd', 96), (('k', ':', 3, '=', 48), 'k', 144), ((35, ':', 'a', '=', 5), 'a', 7),
                     ((64, ':', 'c', '=', 8), 'c', 8), ((7, '·', 'y', '=', 55, '+', 1), 'y', 8)]:
    t.num('Tənliyi həll edin. Məchulu yazın.', [ans], QL(toks, (v, '=', BOX)))
t.num('Lalə uzunluqları eyni olan 4 lenti uc-uca yapışdırdı. Lentin uzunluğu 80 sm oldu. Bir lent neçə santimetrdir?', [20], vstack([hstack([em('🎀', 70)] * 4, 6), QL((4, '·', 'x', '=', 80), ('x', '=', BOX))], 14))
t.num('Hər birində eyni sayda düymə olan 5 qutuda cəmi 75 düymə var. Hər qutuda neçə düymə var?', [15], vstack([em('🔘', 80), QL((5, '·', 'x', '=', 75), ('x', '=', BOX))], 14))

# ============================================================ 158
t = T(158, 'Tənlik qurmaqla məsələ həlli',
      'Məsələdə axtarılan kəmiyyəti x ilə işarə edir, şərtə uyğun tənlik qurub həll edirik. Samir 2 qutu çay aldı və 5 manat üstəgəl 1 manat ödədi: 2 · x = 5 + 1, x = 3. Bir qutu çay 3 manatdır.',
      QL((2, '·', 'x', '=', 5, '+', 1), ('x', '=', 6, ':', 2, '=', 3)))
t.choice('Samir 2 qutu çay aldı. O, kassaya 5 manatlıq və 1 manatlıq verdi. Bir qutu çayın qiymətini tapmaq üçün hansı tənlik uyğundur? Dairəyə alın.', ['2 · x = 5 + 1', 'x + 2 = 6', 'x : 2 = 6'], 0, stem=hstack([em('🍵', 80), em('🍵', 80), note(5, 140, 74), note(1, 140, 74)], 10))
t.num('Tənliyi həll edin. Bir qutu çay neçə manatdır?', [3], QL((2, '·', 'x', '=', 5, '+', 1), ('x', '=', BOX)))
t.num('Yük maşını 3 reysdə cəmi 12 000 kərpic daşıdı. Hər reysdə eyni sayda kərpic daşıdı. Bir reysdə neçə kərpic daşıdı?', [4000], vstack([em('🚚', 90), QL((3, '·', 'x', '=', 12000), ('x', '=', BOX))], 14), disp='4 000')
t.num('Bağban 72 kq almanı yeşiklərə payladı. Hər yeşikdə 9 kq alma oldu. Neçə yeşik alındı?', [8], vstack([em('🍎', 90), QL((72, ':', 'x', '=', 9), ('x', '=', BOX))], 14))
t.num('Kürəciklər 3 uşaq arasında bərabər paylandı. Hər uşağa 18 kürəcik düşdü. Əvvəl qutuda neçə kürəcik var idi?', [54], vstack([em('🔮', 80), QL(('x', ':', 3, '=', 18), ('x', '=', BOX))], 14))
t.num('Müəllim şagirdləri hər birində 7 şagird olmaqla komandalara böldü. 4 komanda alındı. Sinifdə neçə şagird var?', [28], vstack([em('⚽', 80), QL(('x', ':', 7, '=', 4), ('x', '=', BOX))], 14))
t.num('Qabda bir neçə qutab var idi. Nənə 5 qutab əlavə etdi və 4 uşağın hər birinə 3 qutab çatdı. Qabda əvvəl neçə qutab var idi?', [7], vstack([em('🥟', 80), QL(('x', '+', 5, '=', 4, '·', 3), ('x', '=', BOX))], 14))
t.choice('Şagirdlər 6 nəfərlik qruplara bölündü. 8 nəfərlik qruplara bölünsəydilər, 3 qrup alınardı. Hansı tənlik uyğundur? Dairəyə alın.', ['x · 6 = 8 · 3', 'x + 6 = 8 + 3', 'x − 6 = 8 − 3'], 0)
t.num('Tənliyi həll edin. Şagirdlər neçə qrupa bölünmüşdü?', [4], QL(('x', '·', 6, '=', 8, '·', 3), ('x', '=', BOX)))
t.num('Bidonda 18 litr süd var idi. Nənə südü qablara bərabər payladı, hər qabda 3 litr oldu. Neçə qab doldu?', [6], vstack([em('🥛', 80), QL((18, ':', 'x', '=', 3), ('x', '=', BOX))], 14))

# ============================================================ 159
t = T(159, 'Riyazi qanunauyğunluq',
      'Ədədlər müəyyən qayda ilə düzülə bilər: 2, 5, 8, 11 sırasında hər dəfə 3 əlavə olunur, 3, 12, 48, 192 sırasında isə hər ədəd 4-ə vurulur. Qaydanı bilərək növbəti ədədləri tapırıq.',
      vstack([hstack([seq([2, 5, 8, 11], 48), txt('+3', 48, GREEN)], 14), hstack([seq([3, 12, 48, 192], 48), txt('·4', 48, GREEN)], 14)], 14))
t.num('Qaydanı tapın. Növbəti ədədi yazın.', [14], seq([2, 5, 8, 11, BOX], 54))
t.num('Qaydanı tapın. Növbəti ədədi yazın.', [192], seq([3, 12, 48, BOX], 54))
t.num('Qayda: 2-yə vurun və 1 çıxın. Növbəti ədədi yazın.', [17], seq([2, 3, 5, 9, BOX], 54))
t.num('Qayda: 2-yə vurun və 5 əlavə edin. Giriş 5 olanda çıxış neçə olar?', [15], hstack([txt('5', 70, BLUE), arrow(), chip('· 2 + 5', 46), arrow(), box()], 12))
t.num('Qayda: 2-yə vurun və 5 əlavə edin. Giriş 10 olanda çıxış neçə olar?', [25], hstack([txt('10', 70, BLUE), arrow(), chip('· 2 + 5', 46), arrow(), box()], 12))
t.num('Qayda: 4-ə bölün və 3 çıxın. Giriş 36 olanda çıxış neçə olar?', [6], hstack([txt('36', 70, BLUE), arrow(), chip(': 4 − 3', 46), arrow(), box()], 12))
t.num('Bir kitab 3 manatdır. 9 kitab satılanda gəlir neçə manat olar?', [27], vstack([tab([['Kitab', 5, 7, 9], ['Gəlir (man)', 15, 21, '?']], 32), hstack([arrow(), box()], 12)], 14))
t.choice('4, 8, 16, 32 sırasının qaydası hansıdır? Dairəyə alın.', ['2-yə vurun', '4 əlavə edin', '8 əlavə edin'], 0)
t.num('Qaydanı tapın. Növbəti ədədi yazın.', [118200], hstack([seq([f(88200), f(98200), f(108200)], 44), box(250, 92)], 12), disp='118 200')
t.num('Qaydanı tapın. Növbəti ədədi yazın.', [1013217], vstack([seq([f(1313217), f(1213217), f(1113217)], 40), hstack([arrow(), box(300, 92)], 12)], 12), disp='1 013 217')

# ============================================================ 160
t = T(160, 'İkirəqəmli ədədə vurma',
      'İkirəqəmli ədədə vuranda əvvəl təkliklərə, sonra onluqlara vururuq və natamam hasilləri toplayırıq: 243 · 32 = 243 · 2 + 243 · 30 = 486 + 7 290 = 7 776.',
      QL((243, '·', 32, '=', 243, '·', 2, '+', 243, '·', 30), ('=', 486, '+', 7290, '=', 7776)))
for a, b in [(34, 12), (125, 23), (306, 45), (1204, 31)]:
    t.num('Alt-alta vurun.', [a * b], vcolg(a, b, '·'), disp=f(a * b))
t.num('Natamam hasilləri toplayın. Boş xanalara uyğun ədədləri yazın.', [7290, 7776], QL((243, '·', 32, '=', 486, '+', 243, '·', 30), ('=', 486, '+', BOX, '=', BOX)), disp='7 290, 7 776')
t.num('Hasili şifahi tapın.', [1000], Q(25, '·', 40, '=', BOX), disp='1 000')
t.num('Hasili şifahi tapın.', [3600], Q(120, '·', 30, '=', BOX), disp='3 600')
t.num('Bir qutuda 24 karandaş var. 15 qutuda neçə karandaş var?', [360], vstack([em('✏️', 80), Q(24, '·', 15, '=', BOX)], 14))
t.choice('Hasili təqribi tapın. Dairəyə alın.', ['1 000', '800', '10 000'], 0, stem=Q(48, '·', 21, '≈'))
t.num('Kitabın hər səhifəsində 32 sətir var. 125 səhifədə neçə sətir var?', [4000], vstack([em('📖', 80), Q(125, '·', 32, '=', BOX)], 14), disp='4 000')

# ============================================================ 161
t = T(161, 'Üçrəqəmli ədədə vurma',
      'Üçrəqəmli ədədə vuranda üç natamam hasil tapılır və toplanır: 214 · 123 = 214 · 3 + 214 · 20 + 214 · 100 = 642 + 4 280 + 21 400 = 26 322.',
      QL((214, '·', 123, '='), (642, '+', 4280, '+', 21400, '=', 26322)))
for a, b in [(112, 123), (204, 215), (321, 132)]:
    t.num('Alt-alta vurun.', [a * b], vcolg(a, b, '·'), disp=f(a * b))
t.num('Natamam hasilləri toplayın. Boş xanalara uyğun ədədləri yazın.', [21400, 26322], QL((214, '·', 123, '='), (642, '+', 4280, '+', BOX, '=', BOX)), disp='21 400, 26 322')
t.num('Hasili şifahi tapın.', [3000], Q(15, '·', 200, '=', BOX), disp='3 000')
t.num('Hasili şifahi tapın.', [36000], Q(120, '·', 300, '=', BOX), disp='36 000')
t.num('Hasili şifahi tapın.', [10000], Q(25, '·', 400, '=', BOX), disp='10 000')
t.num('Bir bilet 125 manatdır. 104 bilet neçə manatdır?', [13000], vstack([em('🎫', 80), Q(125, '·', 104, '=', BOX)], 14), disp='13 000')
t.choice('Hansı hasil ən böyükdür? Dairəyə alın.', ['301 · 102', '299 · 100', '300 · 101'], 0)
t.num('Fabrik gündə 245 kostyum tikir. 120 gündə neçə kostyum tikər?', [29400], vstack([em('👔', 80), Q(245, '·', 120, '=', BOX)], 14), disp='29 400')

# ============================================================ 162
t = T(162, 'İkirəqəmli ədədin ikirəqəmli ədədə bölünməsi',
      'İkirəqəmli ədədə bölmədə qisməti təxmin edir və vurma ilə yoxlayırıq: 96 : 32 = 3, çünki 32 · 3 = 96. 84 : 14 = 6, çünki 14 · 6 = 84.',
      QL((96, ':', 32, '=', 3, ',', 32, '·', 3, '=', 96), (84, ':', 14, '=', 6, ',', 14, '·', 6, '=', 84)))
for a, b in [(96, 32), (84, 14), (75, 25), (91, 13), (72, 24), (98, 14)]:
    t.num('Qisməti tapın.', [a // b], Q(a, ':', b, '=', BOX, size=70))
t.num('Boş xanaya uyğun ədədi yazın.', [5], Q(16, '·', BOX, '=', 80, size=70))
t.choice('Qisməti tapın. Dairəyə alın.', ['4', '3', '5'], 0, stem=Q(68, ':', 17, '='))
t.num('90 şagird 15 nəfərlik qruplara bölündü. Neçə qrup alındı?', [6], vstack([em('🧒', 80), Q(90, ':', 15, '=', BOX)], 14))
t.num('Kitab 64 səhifədir. Lalə gündə 16 səhifə oxuyur. Kitabı neçə günə oxuyar?', [4], vstack([em('📚', 80), Q(64, ':', 16, '=', BOX)], 14))

# ============================================================ 163
t = T(163, 'Çoxrəqəmli ədədin ikirəqəmli ədədə bölünməsi',
      'Çoxrəqəmli ədədi ikirəqəmli ədədə sütun şəklində bölürük: əvvəl ilk natamam bölünəni seçir, qismətin rəqəmini təxmin edir və vurma ilə yoxlayırıq: 2 448 : 24 = 102.',
      QL((2448, ':', 24, '=', 102), (102, '·', 24, '=', 2448)))
for a, b in [(2448, 24), (1575, 15), (7392, 32), (4368, 21), (11700, 45)]:
    t.num('Qisməti tapın.', [a // b], Q(a, ':', b, '=', BOX, size=64))
t.num('Qisməti şifahi tapın.', [80], Q(4800, ':', 60, '=', BOX, size=64))
t.num('Qisməti şifahi tapın.', [400], Q(36000, ':', 90, '=', BOX, size=64))
t.num('Fabrik 6 720 şokoladı 32 qutuya bərabər yığdı. Hər qutuda neçə şokolad var?', [210], vstack([em('🍫', 80), Q(6720, ':', 32, '=', BOX)], 14))
t.choice('Qisməti təqribi tapın. Dairəyə alın.', ['200', '100', '20'], 0, stem=Q(9216, ':', 48, '≈'))
t.num('Bölməni vurma ilə yoxlayın.', [7392], Q(231, '·', 32, '=', BOX, size=64), disp='7 392')

# ============================================================ 164–170 köməkçi şəkillər
import math


def _lbl(d, x, y, s, size=30, color=INK, anchor='mm'):
    d.text((x * S, y * S), s, font=font(size * S), fill=color, anchor=anchor)


def circle_img(r=110, kind='r', label='', extra=()):
    """çevrə: kind 'r' radius, 'd' diametr, 'chords' OA/BC/DE, 'n' radius sayı (extra=(n,))"""
    pad = 60
    w = h = 2 * r + 2 * pad
    im, d = vec(w, h)
    cx = cy = r + pad
    d.ellipse([(cx - r) * S, (cy - r) * S, (cx + r) * S, (cy + r) * S], outline=BLUE, width=6 * S, fill=(227, 242, 253))
    d.ellipse([(cx - 7) * S, (cy - 7) * S, (cx + 7) * S, (cy + 7) * S], fill=RED)
    if kind == 'r':
        d.line([cx * S, cy * S, (cx + r) * S, cy * S], fill=ORANGE, width=6 * S)
        _lbl(d, cx + r / 2, cy - 26, label, 40, INK)
        _lbl(d, cx - 18, cy + 20, 'O', 28, RED)
    elif kind == 'd':
        d.line([(cx - r) * S, cy * S, (cx + r) * S, cy * S], fill=GREEN, width=6 * S)
        _lbl(d, cx, cy - 28, label, 40, INK)
    elif kind == 'chords':
        a = math.radians(-60)
        ax, ay = cx + r * math.cos(a), cy + r * math.sin(a)
        d.line([cx * S, cy * S, ax * S, ay * S], fill=ORANGE, width=6 * S)
        d.line([(cx - r) * S, cy * S, (cx + r) * S, cy * S], fill=GREEN, width=6 * S)
        b1, b2 = math.radians(120), math.radians(60)
        dx1, dy1 = cx + r * math.cos(b1), cy + r * math.sin(b1)
        dx2, dy2 = cx + r * math.cos(b2), cy + r * math.sin(b2)
        d.line([dx1 * S, dy1 * S, dx2 * S, dy2 * S], fill=PURPLE, width=6 * S)
        for s_, x, y in [('O', cx - 8, cy - 26), ('A', ax + 16, ay - 14), ('B', cx - r - 24, cy), ('C', cx + r + 24, cy), ('D', dx1 - 18, dy1 + 18), ('E', dx2 + 18, dy2 + 18)]:
            _lbl(d, x, y, s_, 30, INK)
    elif kind == 'n':
        for k in range(extra[0]):
            a = math.radians(-90 + 360 * k / extra[0])
            d.line([cx * S, cy * S, (cx + r * math.cos(a)) * S, (cy + r * math.sin(a)) * S], fill=ORANGE, width=5 * S)
    return done(im)


def protractor(deg, R=200):
    """transportir və bucaq: bir tərəf 0°-də, digəri deg-də"""
    pad = 40
    w, h = 2 * R + 2 * pad, R + pad + 50
    im, d = vec(w, h)
    cx, cy = R + pad, R + pad
    d.pieslice([(cx - R) * S, (cy - R) * S, (cx + R) * S, (cy + R) * S], 180, 360, fill=(255, 249, 196), outline=INK, width=4 * S)
    for k in range(0, 181, 10):
        a = math.radians(180 + k)
        r1 = R - (22 if k % 30 == 0 else 12)
        d.line([(cx + R * math.cos(a)) * S, (cy + R * math.sin(a)) * S, (cx + r1 * math.cos(a)) * S, (cy + r1 * math.sin(a)) * S], fill=INK, width=3 * S)
        if k % 30 == 0 and 0 < k < 180:
            rr = R - 44
            _lbl(d, cx + rr * math.cos(math.radians(360 - k)), cy + rr * math.sin(math.radians(360 - k)), str(k), 22, GREY)
    L = R + 20
    d.line([cx * S, cy * S, (cx + L) * S, cy * S], fill=BLUE, width=6 * S)
    a = math.radians(-deg)
    d.line([cx * S, cy * S, (cx + L * math.cos(a)) * S, (cy + L * math.sin(a)) * S], fill=BLUE, width=6 * S)
    d.arc([(cx - 40) * S, (cy - 40) * S, (cx + 40) * S, (cy + 40) * S], 360 - deg, 360, fill=ORANGE, width=5 * S)
    d.ellipse([(cx - 8) * S, (cy - 8) * S, (cx + 8) * S, (cy + 8) * S], fill=RED)
    return done(im)


def coord(pts=(), n=6, cell=58, poly_=None):
    """koordinat şəbəkəsi 0..n; pts = [(ad, x, y)], poly_ = təpələr siyahısı"""
    pad = 50
    w = h = n * cell + 2 * pad
    im, d = vec(w, h)
    ox, oy = pad, h - pad
    for k in range(n + 1):
        d.line([(ox + k * cell) * S, (oy) * S, (ox + k * cell) * S, (oy - n * cell) * S], fill=LIGHT, width=3 * S)
        d.line([ox * S, (oy - k * cell) * S, (ox + n * cell) * S, (oy - k * cell) * S], fill=LIGHT, width=3 * S)
        _lbl(d, ox + k * cell, oy + 24, str(k), 24, GREY)
        if k:
            _lbl(d, ox - 22, oy - k * cell, str(k), 24, GREY)
    d.line([ox * S, oy * S, (ox + n * cell + 10) * S, oy * S], fill=INK, width=4 * S)
    d.line([ox * S, oy * S, ox * S, (oy - n * cell - 10) * S], fill=INK, width=4 * S)
    if poly_:
        P = [((ox + x * cell) * S, (oy - y * cell) * S) for x, y in poly_]
        d.polygon(P, fill=(255, 224, 178), outline=ORANGE, width=5 * S)
    for nm, x, y in pts:
        px, py = ox + x * cell, oy - y * cell
        d.ellipse([(px - 9) * S, (py - 9) * S, (px + 9) * S, (py + 9) * S], fill=RED)
        _lbl(d, px + 20, py - 20, nm, 30, RED)
    return done(im)


SHAPE_COL = {3: (255, 167, 38), 4: (66, 165, 245), 5: (102, 187, 106), 6: (171, 71, 188), 0: (239, 83, 80)}


def shape(n, size=90, col=None):
    if n == 0:
        im, d = vec(size + 8, size + 8)
        d.ellipse([4 * S, 4 * S, (size + 4) * S, (size + 4) * S], fill=col or SHAPE_COL[0], outline=INK, width=4 * S)
        return done(im)
    return poly(n, size, col or SHAPE_COL[n], rot=(-math.pi / 4 if n == 4 else None))


def dot(col, size=70):
    im, d = vec(size + 8, size + 8)
    d.ellipse([4 * S, 4 * S, (size + 4) * S, (size + 4) * S], fill=col, outline=INK, width=4 * S)
    return done(im)


def pattern(items, size=84):
    return hstack(items + [box(size + 10, size + 10)], 14)


def net(cells, cell=56, col=(144, 202, 249)):
    """açılış: cells = [(sütun, sətir)]"""
    cols = max(c for c, _ in cells) + 1
    rows_ = max(r for _, r in cells) + 1
    im, d = vec(cols * cell + 10, rows_ * cell + 10)
    for c, r in cells:
        d.rectangle([(5 + c * cell) * S, (5 + r * cell) * S, (5 + (c + 1) * cell) * S, (5 + (r + 1) * cell) * S], fill=col, outline=INK, width=4 * S)
    return done(im)


def pyramid_net(cell=90):
    w = cell * 3 + 10
    im, d = vec(w, w)
    x0 = y0 = 5 + cell
    d.rectangle([x0 * S, y0 * S, (x0 + cell) * S, (y0 + cell) * S], fill=(255, 224, 130), outline=INK, width=4 * S)
    tri_ = [[(x0, y0), (x0 + cell, y0), (x0 + cell / 2, y0 - cell)], [(x0, y0 + cell), (x0 + cell, y0 + cell), (x0 + cell / 2, y0 + 2 * cell)],
            [(x0, y0), (x0, y0 + cell), (x0 - cell, y0 + cell / 2)], [(x0 + cell, y0), (x0 + cell, y0 + cell), (x0 + 2 * cell, y0 + cell / 2)]]
    for t_ in tri_:
        d.polygon([(x * S, y * S) for x, y in t_], fill=(255, 183, 77), outline=INK, width=4 * S)
    return done(im)


def cylinder_net(w=200, h=120):
    r = 40
    im, d = vec(w + 10, h + 4 * r + 20)
    x0, y0 = 5, 2 * r + 10
    d.rectangle([x0 * S, y0 * S, (x0 + w) * S, (y0 + h) * S], fill=(165, 214, 167), outline=INK, width=4 * S)
    for cy_ in (y0 - r, y0 + h + r):
        d.ellipse([(x0 + w / 2 - r) * S, (cy_ - r) * S, (x0 + w / 2 + r) * S, (cy_ + r) * S], fill=(129, 199, 132), outline=INK, width=4 * S)
    return done(im)


def stack(hs, a=56, col=(255, 183, 77)):
    """kublardan fiqur; hs = [arxa sıra, ..., ön sıra], hər sıra sütunların hündürlükləri (qıyıq proyeksiya)"""
    depth = len(hs)
    ncol = max(len(r) for r in hs)
    hmax = max(max(r) for r in hs)
    k = 0.5
    W = int(ncol * a + depth * a * k + 20)
    H = int(hmax * a + depth * a * k + 20)
    im, d = vec(W, H)
    top = tuple(min(255, int(c * 1.15)) for c in col)
    side = tuple(int(c * 0.78) for c in col)
    for yi, row_ in enumerate(hs):          # arxadan önə
        dep = depth - 1 - yi
        for x, hh in enumerate(row_):
            for z in range(hh):
                X = 10 + x * a + dep * a * k
                Y = H - 10 - z * a - dep * a * k
                f_ = [(X, Y), (X + a, Y), (X + a, Y - a), (X, Y - a)]
                t_ = [(X, Y - a), (X + a, Y - a), (X + a + a * k, Y - a - a * k), (X + a * k, Y - a - a * k)]
                s_ = [(X + a, Y), (X + a + a * k, Y - a * k), (X + a + a * k, Y - a - a * k), (X + a, Y - a)]
                for poly__, c in ((s_, side), (t_, top), (f_, col)):
                    d.polygon([(px * S, py * S) for px, py in poly__], fill=c, outline=INK, width=3 * S)
    return done(im)


def view(heights, a=40, col=(144, 202, 249)):
    """önündən görünüş: sütunların hündürlükləri"""
    ncol, hmax = len(heights), max(heights)
    im, d = vec(ncol * a + 10, hmax * a + 10)
    for x, hh in enumerate(heights):
        for z in range(hh):
            d.rectangle([(5 + x * a) * S, (5 + (hmax - z - 1) * a) * S, (5 + (x + 1) * a) * S, (5 + (hmax - z) * a) * S], fill=col, outline=INK, width=3 * S)
    return done(im)


def topview(grid_, a=40, col=(165, 214, 167)):
    rows_, ncol = len(grid_), len(grid_[0])
    im, d = vec(ncol * a + 10, rows_ * a + 10)
    for r, row_ in enumerate(grid_):
        for c, v in enumerate(row_):
            if v:
                d.rectangle([(5 + c * a) * S, (5 + r * a) * S, (5 + (c + 1) * a) * S, (5 + (r + 1) * a) * S], fill=col, outline=INK, width=3 * S)
    return done(im)


# ============================================================ 164
t = T(164, 'Sadə həndəsi fiqurlar. Çevrə',
      'Çevrənin bütün nöqtələri mərkəzdən eyni məsafədədir. Mərkəzi çevrənin nöqtəsi ilə birləşdirən parça radiusdur. Mərkəzdən keçən və çevrənin iki nöqtəsini birləşdirən parça diametrdir. Diametr radiusdan 2 dəfə böyükdür.',
      hstack([circle_img(100, 'r', 'r'), circle_img(100, 'd', 'd')], 30))
t.num('Çevrənin radiusu 4 sm-dir. Diametri neçə santimetrdir?', [8], hstack([circle_img(100, 'r', '4 sm'), arrow(), box(), txt('sm', 46, GREY)], 12))
t.num('Çevrənin diametri 10 sm-dir. Radiusu neçə santimetrdir?', [5], hstack([circle_img(100, 'd', '10 sm'), arrow(), box(), txt('sm', 46, GREY)], 12))
t.num('Çevrənin radiusu 7 sm-dir. Diametri neçə santimetrdir?', [14], hstack([circle_img(100, 'r', '7 sm'), arrow(), box(), txt('sm', 46, GREY)], 12))
t.choice('Şəkildə hansı parça diametrdir? Dairəyə alın.', ['BC', 'OA', 'DE'], 0, stem=circle_img(120, 'chords'))
t.choice('Şəkildə hansı parça radiusdur? Dairəyə alın.', ['DE', 'BC', 'OA'], 2, stem=circle_img(120, 'chords'))
t.num('Çevrədə neçə radius çəkilib?', [5], hstack([circle_img(110, 'n', extra=(5,)), arrow(), box()], 14))
t.choice('Dördbucaqlılara toxunun.', [shape(4), shape(3), rhombus(90, (255, 202, 40)), shape(5), shape(4, 90, (239, 154, 154))], [0, 2, 4], mode='multi', disp='1-ci, 3-cü, 5-ci şəkil')
t.num('Kvadratın içində çevrə çəkilib. Çevrə kvadratın tərəflərinə toxunur və diametri 6 sm-dir. Kvadratın tərəfi neçə santimetrdir?', [6], hstack([frame(circle_img(80, 'd', '6 sm'), 0, INK, 5, 0), arrow(), box(), txt('sm', 46, GREY)], 12))
t.choice('Təkərin diametri 60 sm-dir. Radiusu neçədir? Dairəyə alın.', ['30 sm', '120 sm', '60 sm'], 0, stem=em('🛞', 110))
t.num('Çevrənin diametri 18 sm-dir. Radiusu neçə santimetrdir?', [9], hstack([circle_img(100, 'd', '18 sm'), arrow(), box(), txt('sm', 46, GREY)], 12))

# ============================================================ 165
t = T(165, 'Bucaq. Bucağın ölçüsü',
      'Bucaqlar dərəcə ilə ölçülür. Düz bucaq 90°-dir. 90°-dən kiçik bucaq iti bucaq, 90°-dən böyük, amma 180°-dən kiçik bucaq kor bucaqdır. Açıq bucaq 180°-dir.',
      hstack([vstack([angle_img(45, 160), txt('iti', 36, BLUE)], 6), vstack([angle_img(90, 160), txt('düz', 36, BLUE)], 6), vstack([angle_img(135, 160), txt('kor', 36, BLUE)], 6)], 30, align='bottom'))
for deg, ans in [(40, 0), (90, 1), (130, 2)]:
    t.choice('Bu hansı bucaqdır? Dairəyə alın.', ['İti', 'Düz', 'Kor'], ans, stem=angle_img(deg, 220))
t.choice('İti bucaqlara toxunun.', [angle_img(30, 140), angle_img(120, 140), angle_img(60, 140), angle_img(90, 140), angle_img(150, 140), angle_img(75, 140)], [0, 2, 5], mode='multi', disp='1-ci, 3-cü, 6-cı şəkil')
t.num('Düz bucaq neçə dərəcədir?', [90], hstack([angle_img(90, 180), arrow(), box(), txt('°', 60, GREY)], 12))
t.num('Açıq bucaq neçə dərəcədir?', [180], hstack([angle_img(180, 180), arrow(), box(), txt('°', 60, GREY)], 12))
t.num('Düz bucağı iki bərabər hissəyə böldük. Hər hissə neçə dərəcədir?', [45], hstack([expr2(['90°', ':', '2', '='], 60), box(), txt('°', 60, GREY)], 12))
t.num('Saat 3:00-da əqrəblər arasındakı bucaq neçə dərəcədir?', [90], hstack([em('🕒', 120), arrow(), box(), txt('°', 60, GREY)], 12))
t.choice('Ən böyük bucaq hansıdır? Dairəyə alın.', [angle_img(70, 150), angle_img(150, 150), angle_img(100, 150)], 1)
t.num('Açıq bucaqdan 60°-lik bucağı ayırdıq. Qalan bucaq neçə dərəcədir?', [120], hstack([expr2(['180°', '−', '60°', '='], 60), box(), txt('°', 60, GREY)], 12))

# ============================================================ 166
t = T(166, 'Bucağın ölçülməsi. Transportir',
      'Bucağı transportirlə ölçürük. Transportirin mərkəzini bucağın təpəsinə qoyur, sıfır xəttini bucağın bir tərəfi ilə üst-üstə salırıq. Bucağın digər tərəfinin keçdiyi bölgü bucağın ölçüsünü göstərir.',
      protractor(60))
for deg in (30, 60, 120, 150, 90, 45):
    t.num('Transportirə baxın. Bucaq neçə dərəcədir?', [deg], vstack([protractor(deg, 190), hstack([box(), txt('°', 60, GREY)], 8)], 10))
t.num('İki bucağın cəmini tapın.', [75], hstack([expr2(['30°', '+', '45°', '='], 64), box(), txt('°', 60, GREY)], 12))
t.choice('120°-lik bucaq hansı bucaqdır? Dairəyə alın.', ['Kor', 'İti', 'Düz'], 0)
t.num('Fərqi tapın.', [55], hstack([expr2(['90°', '−', '35°', '='], 64), box(), txt('°', 60, GREY)], 12))
t.choice('Hansı şəkildə 60°-lik bucaq var? Dairəyə alın.', [protractor(100, 120), protractor(60, 120), protractor(30, 120)], 1)

# ============================================================ 167
t = T(167, 'Koordinat şəbəkəsi',
      'Koordinat şəbəkəsində nöqtənin yerini iki ədədlə göstəririk: əvvəlcə üfüqi ox üzrə sağa, sonra şaquli ox üzrə yuxarı sayırıq. A (3; 2) nöqtəsi sağa 3, yuxarı 2 vahiddir.',
      coord([('A', 3, 2)], 5, 56))
for nm, x, y in [('A', 3, 2), ('B', 5, 4), ('C', 1, 5), ('D', 4, 0)]:
    t.num('%s nöqtəsinin koordinatlarını yazın: əvvəl sağa, sonra yuxarı sayın.' % nm, [x, y], coord([(nm, x, y)]), disp='(%d; %d)' % (x, y))
t.choice('(2; 4) koordinatlı nöqtə hansıdır? Dairəyə alın.', ['K', 'L', 'M'], 0, stem=coord([('K', 2, 4), ('L', 4, 2), ('M', 2, 2)]))
t.choice('(5; 1) koordinatlı nöqtə hansıdır? Dairəyə alın.', ['P', 'R', 'T'], 1, stem=coord([('P', 1, 5), ('R', 5, 1), ('T', 5, 5)]))
t.num('A (1; 2) nöqtəsindən 3 vahid sağa getdik. Yeni nöqtənin birinci koordinatı neçədir?', [4], coord([('A', 1, 2), ('?', 4, 2)]))
t.num('Kvadratın təpələri (1; 1), (4; 1), (4; 4) və (1; 4) nöqtələridir. Kvadratın tərəfi neçə vahiddir?', [3], coord(poly_=[(1, 1), (4, 1), (4, 4), (1, 4)]))
t.choice('Hansı nöqtə üfüqi ox üzərindədir? Dairəyə alın.', ['A', 'B', 'C'], 0, stem=coord([('A', 3, 0), ('B', 0, 3), ('C', 2, 2)]))
t.num('Düzbucaqlının təpələri (0; 0), (5; 0), (5; 2) və (0; 2) nöqtələridir. Sahəsi neçə kvadrat vahiddir?', [10], coord(poly_=[(0, 0), (5, 0), (5, 2), (0, 2)]))

# ============================================================ 168
t = T(168, 'Həndəsi ornamentlər',
      'Ornament fiqurların müəyyən qayda ilə təkrarlanması, sürüşdürülməsi və simmetrik yerləşdirilməsi ilə yaranır. Azərbaycan xalçalarında belə naxışlar çoxdur.',
      hstack([shape(3, 70), shape(4, 70), shape(3, 70), shape(4, 70), shape(3, 70), shape(4, 70)], 10))
t.choice('Qaydanı tapın. Növbəti fiqur hansıdır? Dairəyə alın.', [shape(4), shape(3), shape(0)], 0, stem=pattern([shape(3, 70), shape(4, 70), shape(3, 70), shape(4, 70), shape(3, 70)], 70))
R_, B_, G_ = (239, 83, 80), (66, 165, 245), (102, 187, 106)
t.choice('Qaydanı tapın. Növbəti dairə hansı rəngdədir? Dairəyə alın.', [dot(B_), dot(R_), dot(G_)], 0, stem=pattern([dot(R_, 56), dot(B_, 56), dot(B_, 56), dot(R_, 56), dot(B_, 56), dot(B_, 56), dot(R_, 56)], 56))
t.choice('Qaydanı tapın. Növbəti fiqur hansıdır? Dairəyə alın.', [shape(5), shape(3), shape(4)], 0, stem=pattern([shape(3, 66), shape(4, 66), shape(5, 66), shape(3, 66), shape(4, 66)], 66))
t.choice('Ox hər dəfə saat əqrəbi istiqamətində dörddə bir dövr fırlanır. Növbəti ox hansıdır? Dairəyə alın.', [em('➡️', 90), em('⬅️', 90), em('⬇️', 90)], 0, stem=pattern([em('⬆️', 74), em('➡️', 74), em('⬇️', 74), em('⬅️', 74), em('⬆️', 74)], 74))
t.num('Ornamentin bir sətrində 4 kvadrat var. 6 belə sətirdə neçə kvadrat olar?', [24], vstack([hstack([shape(4, 56)] * 4, 8), expr2(['4', '·', '6', '=', BOX], 60)], 14))
t.num('Naxışda 2 sarı və 1 qırmızı romb növbə ilə təkrarlanır. 12 rombun neçəsi qırmızıdır?', [4], vstack([hstack([rhombus(56, (255, 202, 40)), rhombus(56, (255, 202, 40)), rhombus(56, R_)] * 2, 6), hstack([txt('12 →', 56, BLUE), box()], 10)], 14))
t.choice('Simmetrik hərflərə toxunun.', ['A', 'F', 'H', 'L', 'T', 'R'], [0, 2, 4], mode='multi', disp='A, H, T')
t.num('Qaydanı tapın. Növbəti fiqurda neçə kvadrat olar?', [9], hstack([seq([1, 3, 5, 7, BOX], 56)], 10))
t.num('Xalçada hər naxış 3 rombdan ibarətdir. 8 naxışda neçə romb var?', [24], vstack([hstack([rhombus(60, R_), rhombus(60, B_), rhombus(60, G_)], 8), expr2(['3', '·', '8', '=', BOX], 60)], 14))
t.choice('Qaydanı tapın. Növbəti fiqur hansıdır? Dairəyə alın.', [shape(0, 46), shape(0, 90)], 0, stem=pattern([shape(0, 80), shape(0, 40), shape(0, 40), shape(0, 80), shape(0, 40), shape(0, 40), shape(0, 80)], 80), disp='kiçik dairə')

# ============================================================ 169
CROSS = [(1, 0), (0, 1), (1, 1), (2, 1), (3, 1), (1, 2)]
GRID23 = [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1)]
ROW6 = [(k, 0) for k in range(6)]
STAIR = [(0, 0), (1, 0), (1, 1), (2, 1), (2, 2), (3, 2)]
t = T(169, 'Fəza fiqurlarının açılışı',
      'Fəza fiqurunun bütün üzlərini müstəvi üzərinə açsaq, onun açılışı alınır. Kubun açılışı 6 bərabər kvadratdan, düzbucaqlı paralelepipedin açılışı isə 6 düzbucaqlıdan ibarətdir.',
      hstack([cube_marked(150, False), arrow(), net(CROSS, 50)], 20))
t.choice('Hansı açılışdan kub qurmaq olar? Dairəyə alın.', [net(GRID23, 44), net(CROSS, 44), net(ROW6, 30)], 1)
t.num('Kubun açılışında neçə kvadrat var?', [6], hstack([net(CROSS, 50), arrow(), box()], 14))
t.num('Kubun neçə tili var?', [12], hstack([cube_marked(150, False), arrow(), box()], 14))
t.num('Kubun neçə təpəsi var?', [8], hstack([cube_marked(150, True), arrow(), box()], 14))
t.choice('Bu açılış hansı fiqurundur? Dairəyə alın.', ['Piramida', 'Kub', 'Silindr'], 0, stem=pyramid_net(80))
t.choice('Bu açılış hansı fiqurundur? Dairəyə alın.', ['Silindr', 'Konus', 'Kub'], 0, stem=cylinder_net())
t.num('Kubun bir üzünün sahəsi 4 kv. sm-dir. Bütün üzlərinin sahəsi neçə kvadrat santimetrdir?', [24], vstack([net(CROSS, 46), expr2(['4', '·', '6', '=', BOX], 60)], 14))
t.choice('Hansı açılışdan kub qurmaq olar? Dairəyə alın.', [net(ROW6, 30), net(GRID23, 44), net(STAIR, 40)], 2)
t.num('Kubun neçə üzü var?', [6], hstack([cube_marked(150, False), arrow(), box()], 14))
t.num('Düzbucaqlı paralelepipedin neçə üzü var?', [6], hstack([em('📦', 120), arrow(), box()], 14))

# ============================================================ 170
t = T(170, 'Fiqurların müxtəlif tərəflərdən görünüşü',
      'Kublardan qurulmuş fiqura önündən, yanından və yuxarıdan baxanda müxtəlif şəkillər görürük. Önündən görünüşdə hər sütunda neçə kub olduğunu sayırıq.',
      hstack([stack([[1, 2, 3]]), arrow(), view([1, 2, 3])], 20))
t.num('Fiqur neçə kubdan qurulub?', [4], hstack([stack([[2, 1, 1]]), arrow(), box()], 14))
t.num('Fiqur neçə kubdan qurulub?', [6], hstack([stack([[3, 2, 1]]), arrow(), box()], 14))
t.choice('Fiqurun önündən görünüşü hansıdır? Dairəyə alın.', [view([1, 2, 3]), view([3, 2, 1]), view([2, 2, 2])], 0, stem=stack([[1, 2, 3]]))
t.choice('Fiqurun önündən görünüşü hansıdır? Dairəyə alın.', [view([1, 2, 1]), view([2, 2, 1]), view([2, 1, 2])], 2, stem=stack([[2, 1, 2]]))
t.choice('Fiqurun yuxarıdan görünüşü hansıdır? Dairəyə alın.', [topview([[1, 1, 0], [1, 1, 1]]), topview([[1, 1, 1], [1, 1, 1]]), topview([[0, 1, 1], [1, 1, 1]])], 0, stem=stack([[1, 1, 0], [1, 1, 1]]))
t.num('Fiqur neçə kubdan qurulub? Arxa sıradakı kublar önündəkilərdən hündürdür.', [6], hstack([stack([[2, 2], [1, 1]]), arrow(), box()], 14))
t.num('Fiqura önündən baxanda neçə kvadrat görünür?', [6], hstack([stack([[3, 1, 2]]), arrow(), box()], 14))
t.num('Fiqura yuxarıdan baxanda neçə kvadrat görünür?', [3], hstack([stack([[1, 2, 1]]), arrow(), box()], 14))
t.choice('Hansı fiqur 5 kubdan qurulub? Dairəyə alın.', [stack([[2, 2, 1]], 40), stack([[2, 1, 1]], 40), stack([[3, 2, 1]], 40)], 0)
t.num('Fiqurdan 1 kub götürdük. Neçə kub qaldı?', [6], hstack([stack([[3, 2, 2]]), expr2(['−', '1', '='], 60), box()], 14))

#@@NEXT

save()
