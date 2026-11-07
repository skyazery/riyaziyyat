"""3-cü sinif riyaziyyat, 2-ci hissə: 26 mövzu (117–142), hər mövzuda 10 tapşırıq.
Run: python3 tools/content32.py [OUTDIR]   (default ~/riyaziyyat/3-2)"""
import os, sys
from bookgen import *

init(sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser('~/riyaziyyat/3-2'))
E = lambda *t: expr2(list(t), 70)
F = lambda a, b, s=56: frac_txt(a, b, s)
TS = ['Bərabərtərəfli', 'Bərabəryanlı', 'Müxtəliftərəfli']
TA = ['Düzbucaqlı', 'İtibucaqlı', 'Korbucaqlı']
EQUI = [(0, 1), (0.5, 0.13), (1, 1)]
ISO = [(0.12, 1), (0.5, 0.05), (0.88, 1)]
SCAL = [(0, 1), (0.3, 0.1), (1, 1)]
RIGHT = [(0, 1), (0, 0.1), (1, 1)]
OBT = [(0, 0.9), (0.3, 0.45), (1, 0.9)]
SQ, CI, TR, RE = (lambda s=100: shape('square', s, (102, 187, 106))), (lambda s=100: shape('circle', s, (66, 165, 245))), (lambda s=100: shape('triangle', s, (255, 167, 38))), (lambda s=90: shape('rect', s, (171, 71, 188)))

# ============================================================ 117
t = T(117, 'Kəsişən və paralel düz xətlər',
      'Kəsişən düz xətlər bir nöqtədə kəsişir. Paralel düz xətlər kəsişmir. Perpendikulyar düz xətlər düz bucaq əmələ gətirməklə kəsişir.',
      hstack([label(lines_pair('cross', 170), 'kəsişən', 30, INK), label(lines_pair('parallel', 170), 'paralel', 30, INK), label(lines_pair('perp', 170), 'perpendikulyar', 30, INK)], 24, 'bottom'))
LP = ['Paralel', 'Kəsişən', 'Perpendikulyar']
t.choice('Bu düz xətlər necədir? Dairəyə alın.', LP, 0, stem=lines_pair('parallel'))
t.choice('Bu düz xətlər necədir? Dairəyə alın.', LP, 1, stem=lines_pair('cross'))
t.choice('Bu düz xətlər necədir? Dairəyə alın.', LP, 2, stem=lines_pair('perp'))
t.choice('Paralel düz xətləri dairəyə alın.', [lines_pair('cross', 150), lines_pair('parallel', 150), lines_pair('perp', 150)], 1, disp='2-ci şəkil')
t.choice('Perpendikulyar düz xətləri dairəyə alın.', [lines_pair('parallel', 150), lines_pair('perp', 150), lines_pair('cross', 150)], 1, disp='2-ci şəkil')
t.choice('Dəmir yolu relsləri hansı düz xətlərə bənzəyir? Dairəyə alın.', ['Paralel', 'Kəsişən'], 0, stem=em('🛤️', 130))
t.choice('Toxuma milləri hansı düz xətlərə bənzəyir? Dairəyə alın.', ['Kəsişən', 'Paralel'], 0, stem=em('🧶', 120))
t.num('Kəsişən iki düz xəttin neçə ortaq nöqtəsi var?', [1], hstack([lines_pair('cross'), arrow(), box()], 20))
t.num('Perpendikulyar düz xətlər kəsişəndə neçə düz bucaq əmələ gəlir?', [4], hstack([lines_pair('perp'), arrow(), box()], 20))
t.choice('Hansı cümlə doğrudur? Dairəyə alın.', ['Paralel düz xətlər kəsişmir.', 'Paralel düz xətlər bir nöqtədə kəsişir.'], 0)

# ============================================================ 118
t = T(118, 'Müstəvi fiqurlar',
      'Üçbucaqlar tərəflərinə görə bərabərtərəfli, bərabəryanlı və müxtəliftərəfli olur. Bucaqlarına görə isə düzbucaqlı, itibucaqlı və korbucaqlı olur.',
      hstack([label(tri(EQUI, ('5 sm', '5 sm', '5 sm'), 150), 'bərabərtərəfli', 26, INK), label(tri(ISO, ('6 sm', '6 sm', '3 sm'), 150), 'bərabəryanlı', 26, INK), label(tri(SCAL, ('4 sm', '6 sm', '7 sm'), 150), 'müxtəliftərəfli', 26, INK)], 10, 'bottom'))
t.choice('Üçbucağın tərəflərinə baxın. Hansı üçbucaqdır? Dairəyə alın.', TS, 0, stem=tri(EQUI, ('6 sm', '6 sm', '6 sm')))
t.choice('Üçbucağın tərəflərinə baxın. Hansı üçbucaqdır? Dairəyə alın.', TS, 1, stem=tri(ISO, ('7 sm', '7 sm', '3 sm')))
t.choice('Üçbucağın tərəflərinə baxın. Hansı üçbucaqdır? Dairəyə alın.', TS, 2, stem=tri(SCAL, ('5 sm', '7 sm', '8 sm')))
t.choice('Üçbucağın bucaqlarına baxın. Hansı üçbucaqdır? Dairəyə alın.', TA, 0, stem=tri(RIGHT, right=1))
t.choice('Üçbucağın bucaqlarına baxın. Hansı üçbucaqdır? Dairəyə alın.', TA, 1, stem=tri(EQUI))
t.choice('Üçbucağın bucaqlarına baxın. Hansı üçbucaqdır? Dairəyə alın.', TA, 2, stem=tri(OBT))
t.num('Bərabərtərəfli üçbucağın bir tərəfi 6 sm-dir. Üç tərəfinin cəmi neçə santimetrdir?', [18], hstack([tri(EQUI, ('6 sm', '', ''), 150), expr2(['6', '+', '6', '+', '6', '=', BOX], 54)], 16))
t.num('Düzbucaqlı üçbucağın neçə düz bucağı var?', [1], hstack([tri(RIGHT, right=1, size=150), arrow(), box()], 16))
t.num('Bərabəryanlı üçbucağın neçə tərəfi bərabərdir?', [2], hstack([tri(ISO, ('5 sm', '5 sm', ''), 150), arrow(), box()], 16))
t.num('Kvadratın neçə tərəfi bərabərdir?', [4], hstack([SQ(120), arrow(), box()], 16))

# ============================================================ 119
t = T(119, 'Simmetriya və yerdəyişmə',
      'Fiquru düz xətt üzrə qatlayanda hissələri üst-üstə düşürsə, fiqur simmetrikdir. Həmin xətt simmetriya oxu adlanır.',
      hstack([label(sym('🦋', 130), 'simmetrikdir', 30, GREEN), label(sym('🐌', 130, False), 'simmetrik deyil', 30, RED)], 40, 'bottom'))
SY = ['Simmetrikdir', 'Simmetrik deyil']
for ch, ax, a in [('🦋', True, 0), ('🐌', False, 1), ('❤️', True, 0), ('🦒', False, 1)]:
    t.choice('Şəkil simmetrikdirmi? Dairəyə alın.', SY, a, stem=sym(ch, 140, ax))
t.choice('Simmetrik hərfi dairəyə alın.', ['A', 'R', 'F'], 0)
t.choice('Simmetrik hərfi dairəyə alın.', ['N', 'T', 'G'], 1)
t.num('Kvadratın neçə simmetriya oxu var?', [4], hstack([SQ(130), arrow(), box()], 16))
t.num('Kvadrat olmayan düzbucaqlının neçə simmetriya oxu var?', [2], hstack([RE(110), arrow(), box()], 16))
t.choice('Bərabəryanlı üçbucağın neçə simmetriya oxu var? Dairəyə alın.', ['1', '2', '3'], 0, stem=tri(ISO, size=150))
t.num('Bərabərtərəfli üçbucağın neçə simmetriya oxu var?', [3], hstack([tri(EQUI, size=150), arrow(), box()], 16))

# ============================================================ 120
t = T(120, 'Fəza fiqurları',
      'Piramidanın bir oturacağı və üçbucaq şəklində yan üzləri var. Dördbucaqlı piramidanın 5 üzü, 5 təpəsi və 8 tili var.',
      hstack([label(pyramid(150), 'dördbucaqlı piramida', 28, INK), vstack([txt('5 üz', 40, BLUE), txt('5 təpə', 40, BLUE), txt('8 til', 40, BLUE)], 8, 'left')], 30))
t.choice('Piramidanı dairəyə alın.', [solid('cube', 110), pyramid(110), solid('cylinder', 110)], 1, disp='piramida')
t.choice('Silindri dairəyə alın.', [solid('cone', 110), solid('cylinder', 110), solid('sphere', 110)], 1, disp='silindr')
for q, a in [('üzü', 5), ('təpəsi', 5), ('tili', 8)]:
    t.num('Dördbucaqlı piramidanın neçə %s var?' % q, [a], hstack([pyramid(150), arrow(), box()], 16))
t.num('Kubun neçə üzü var?', [6], hstack([solid('cube', 140), arrow(), box()], 16))
t.num('Kubun neçə tili var?', [12], hstack([solid('cube', 140), arrow(), box()], 16))
t.num('Üçbucaqlı piramidanın neçə üzü var?', [4], hstack([txt('üçbucaqlı piramida', 40, BLUE), arrow(), box()], 16))
t.choice('Top hansı fəza fiquruna bənzəyir? Dairəyə alın.', ['Kürə', 'Kub', 'Silindr'], 0, stem=em('⚽', 120))
t.choice('Qutu hansı fəza fiquruna bənzəyir? Dairəyə alın.', ['Kuboid', 'Kürə', 'Konus'], 0, stem=em('📦', 120))

# ============================================================ 121
t = T(121, 'Müstəvi və fəza fiqurlarının əlaqəsi',
      'Fəza fiqurlarının üzləri müstəvi fiqurlardır. Silindrin oturacaqları dairədir, kubun üzləri kvadratdır, piramidanın yan üzləri üçbucaqdır.',
      hstack([label(solid('cylinder', 110), 'dairə', 30, INK), label(solid('cube', 110), 'kvadrat', 30, INK), label(pyramid(110), 'üçbucaq', 30, INK)], 30, 'bottom'))
t.choice('Silindrin oturacağı hansı fiqurdur? Dairəyə alın.', [CI(), SQ(), TR()], 0, stem=solid('cylinder', 120), disp='dairə')
t.choice('Kubun üzləri hansı fiqurdur? Dairəyə alın.', [SQ(), CI(), TR()], 0, stem=solid('cube', 120), disp='kvadrat')
t.choice('Piramidanın yan üzləri hansı fiqurdur? Dairəyə alın.', [TR(), CI(), SQ()], 0, stem=pyramid(120), disp='üçbucaq')
t.choice('Konusun oturacağı hansı fiqurdur? Dairəyə alın.', [CI(), SQ(), TR()], 0, stem=solid('cone', 120), disp='dairə')
t.choice('Kuboidin üzləri hansı fiqurdur? Dairəyə alın.', [RE(), CI(), TR()], 0, stem=solid('cuboid', 110), disp='düzbucaqlı')
t.choice('Stəkana üstdən baxanda hansı fiqur görünür? Dairəyə alın.', [CI(), SQ(), TR()], 0, stem=em('🥛', 120), disp='dairə')
t.choice('Kitaba üstdən baxanda hansı fiqur görünür? Dairəyə alın.', [RE(), CI(), TR()], 0, stem=em('📕', 120), disp='düzbucaqlı')
t.num('Silindrin neçə oturacağı var?', [2], hstack([solid('cylinder', 140), arrow(), box()], 16))
t.num('Üçbucaqlı prizmanın neçə üzü üçbucaq şəklindədir?', [2], hstack([txt('üçbucaqlı prizma', 40, BLUE), arrow(), box()], 16))
t.choice('Hansı fəza fiqurunun bütün üzləri kvadratdır? Dairəyə alın.', ['Kub', 'Kuboid', 'Piramida'], 0)

# ============================================================ 122
t = T(122, 'Vurmanın xassələri',
      'Cəmi ədədə vurmaq üçün hər toplananı bu ədədə vurub hasilləri toplamaq olar: (3 + 9) · 5 = 3 · 5 + 9 · 5 = 15 + 45 = 60.',
      vstack([expr2(['(', '3', '+', '9', ')', '·', '5', '=', '3', '·', '5', '+', '9', '·', '5'], 44), expr2(['=', '15', '+', '45', '=', '60'], 44)], 10))
t.num('Paylama xassəsindən istifadə edin.', [60], stacked([['(', '3', '+', '9', ')', '·', '5', '=', '15', '+', '45'], ['=', BOX]], 50))
t.num('Paylama xassəsindən istifadə edin.', [20], stacked([['(', '8', '−', '3', ')', '·', '4', '=', '32', '−', '12'], ['=', BOX]], 50))
t.num('Paylama xassəsindən istifadə edin.', [8, 48], E('4', '·', '(', '10', '+', '2', ')', '=', '40', '+', BOX, '=', BOX), disp='8, 48')
t.num('Paylama xassəsindən istifadə edin.', [60, 78], E('6', '·', '(', '10', '+', '3', ')', '=', BOX, '+', '18', '=', BOX), disp='60, 78')
t.num('Vuruqların yerini dəyişin.', [7], E('7', '·', '9', '=', '9', '·', BOX))
t.num('Qruplaşdırma xassəsindən istifadə edin.', [70], expr2(['2', '·', '(', '5', '·', '7', ')', '=', '10', '·', '7', '=', BOX], 56))
t.num('Asan yolla hesablayın: əvvəl 5 · 2.', [70], E('5', '·', '7', '·', '2', '=', BOX))
t.num('Asan yolla hesablayın: əvvəl 25 · 4.', [300], E('25', '·', '3', '·', '4', '=', BOX))
t.num('Vuruqlardan biri 0 olanda hasil neçədir?', [0], E('55', '·', '4', '·', '0', '=', BOX))
t.choice('Hansı bərabərlik doğrudur? Dairəyə alın.', ['(4 + 6) · 3 = 4 · 3 + 6 · 3', '(4 + 6) · 3 = 4 + 6 · 3'], 0)

# ============================================================ 123
t = T(123, 'İkirəqəmli ədədin birrəqəmli ədədə vurulması',
      'Alt-alta vuranda əvvəlcə təklikləri, sonra onluqları vururuq: 32 · 4 = 128.',
      hstack([vcolx(32, 4, '·', 60, show=True), expr2(['32', '·', '4', '=', '128'], 52)], 30))
for a, b in [(32, 4), (23, 3), (47, 2), (36, 5)]:
    t.num('Alt-alta vurun.', [a * b], vcolx(a, b, '·'))
for a, b in [(21, 4), (16, 6), (45, 3)]:
    t.num('Hasili tapın.', [a * b], E(str(a), '·', str(b), '=', BOX))
t.num('Vuruğu onluq və təkliyə ayırıb vurun.', [60, 12, 72], stacked([['24', '·', '3', '=', '20', '·', '3', '+', '4', '·', '3'], ['=', BOX, '+', BOX, '=', BOX]], 50), disp='60 + 12 = 72')
t.num('Hər qutuda 24 karandaş var. 4 qutuda neçə karandaş var?', [96], word(['✏️', '📦'], ['24', '·', '4', '=', BOX]))
t.num('Bir bilet 15 manatdır. 6 bilet neçə manatdır?', [90], word(['🎫'], ['15', '·', '6', '=', BOX]))

# ============================================================ 124
t = T(124, 'Üçrəqəmli ədədin birrəqəmli ədədə vurulması',
      'Birrəqəmli ədədi əvvəlcə təkliklərə, sonra onluqlara, axırda yüzlüklərə vururuq: 234 · 2 = 468.',
      hstack([vcolx(234, 2, '·', 60, show=True), expr2(['234', '·', '2', '=', '468'], 52)], 30))
for a, b in [(234, 2), (128, 3), (213, 4), (145, 6)]:
    t.num('Alt-alta vurun.', [a * b], vcolx(a, b, '·'))
for a, b in [(312, 3), (205, 4)]:
    t.num('Hasili tapın.', [a * b], E(str(a), '·', str(b), '=', BOX))
t.num('Vuruğu mərtəbələrə ayırıb vurun.', [300, 90, 6, 396], stacked([['132', '·', '3', '=', BOX, '+', BOX, '+', BOX], ['=', BOX]], 52), disp='300 + 90 + 6 = 396')
t.num('Bir kitab 112 səhifədir. 5 belə kitab neçə səhifədir?', [560], word(['📘'], ['112', '·', '5', '=', BOX]))
t.num('Mağazaya hər gün 125 litr süd gətirilir. 4 gündə neçə litr süd gətirilər?', [500], word(['🥛', '🏪'], ['125', '·', '4', '=', BOX]))
t.choice('Hasili 600 olan ifadəni dairəyə alın.', ['150 · 4', '160 · 4', '125 · 4'], 0)

# ============================================================ 125
t = T(125, 'Qalıqlı bölmə',
      '13 keksi hər boşqaba 3 keks qoymaqla 4 boşqaba paylamaq olar və 1 keks qalar: 13 : 3 = 4 (qalıq 1). Qalıq həmişə böləndən kiçikdir.',
      vstack([hstack([plates('🧁', (3, 3, 3, 3), 30), em('🧁', 50)], 20), expr2(['13', ':', '3', '=', '4', '(q', '1', ')'], 56)], 14))
t.num('13 keksi hər boşqaba 3 keks qoydular. Neçə boşqab alındı və neçə keks qaldı? Soldan sağa yazın.', [4, 1], vstack([group('🧁', 13, 40, 7), E('13', ':', '3', '=', BOX, '(q', BOX, ')')], 12), disp='4 (q 1)')
for a, b in [(17, 5), (23, 4), (29, 6), (40, 7), (50, 8)]:
    t.num('Qalıqlı bölməni yerinə yetirin: əvvəl qisməti, sonra qalığı yazın.', [a // b, a % b], E(str(a), ':', str(b), '=', BOX, '(q', BOX, ')'), disp='%d (q %d)' % (a // b, a % b))
t.num('25 almanı 4 uşağa bərabər payladılar. Hər uşağa neçə alma düşdü, neçə alma qaldı?', [6, 1], word(['🍎', '🧒'], ['25', ':', '4', '=', BOX, '(q', BOX, ')'], 54), disp='6 (q 1)')
t.choice('5-ə böləndə hansı qalıq ola bilməz? Dairəyə alın.', ['6', '4', '2'], 0)
t.choice('19 : 3 = 6 (q 1). Bu düzdürmü? Dairəyə alın.', ['Bəli', 'Xeyr'], 0)
t.num('34 şagird 5 nəfərlik qayıqlara oturdu. Neçə qayıq tam doldu?', [6], word(['🚣', '🧒'], ['34', ':', '5', '=', BOX, '(q', '4', ')'], 54))

# ============================================================ 126
t = T(126, 'İkirəqəmli ədədin birrəqəmli ədədə bölünməsi',
      'Əvvəlcə onluqlar, sonra təkliklər bölünür: 76 : 2 = 38. 7 onluq : 2 = 3 onluq (qalıq 1 onluq), 16 təklik : 2 = 8 təklik.',
      expr2(['76', ':', '2', '=', '38'], 70))
for a, b in [(76, 2), (84, 4), (96, 3), (72, 4), (85, 5), (91, 7)]:
    t.num('Bölməni yerinə yetirin.', [a // b], E(str(a), ':', str(b), '=', BOX))
t.num('Bölünəni onluq və təkliyə ayırıb bölün.', [20, 1, 21], stacked([['84', ':', '4', '=', '80', ':', '4', '+', '4', ':', '4'], ['=', BOX, '+', BOX, '=', BOX]], 50), disp='20 + 1 = 21')
t.num('96 dəftəri 3 sinfə bərabər payladılar. Hər sinfə neçə dəftər düşdü?', [32], word(['📒', '🏫'], ['96', ':', '3', '=', BOX]))
t.num('78 qəpiyi 6 uşağa bərabər payladılar. Hər uşağa neçə qəpik düşdü?', [13], word(['🪙', '🧒'], ['78', ':', '6', '=', BOX]))
t.num('Qalıqlı bölməni yerinə yetirin: əvvəl qisməti, sonra qalığı yazın.', [15, 2], E('47', ':', '3', '=', BOX, '(q', BOX, ')'), disp='15 (q 2)')

# ============================================================ 127
t = T(127, 'Üçrəqəmli ədədin birrəqəmli ədədə bölünməsi',
      'Əvvəlcə yüzlüklər, sonra onluqlar, axırda təkliklər bölünür: 732 : 3 = 244.',
      expr2(['732', ':', '3', '=', '244'], 70))
for a, b in [(732, 3), (846, 2), (936, 4), (525, 5), (648, 6), (714, 7)]:
    t.num('Bölməni yerinə yetirin.', [a // b], E(str(a), ':', str(b), '=', BOX))
t.num('Mərtəbələri ayrı-ayrı bölün.', [200, 20, 221], stacked([['600', ':', '3', '=', BOX], ['60', ':', '3', '=', BOX], ['663', ':', '3', '=', BOX]], 52), disp='200, 20, 221')
t.num('450 kitabı 5 rəfə bərabər düzdülər. Hər rəfdə neçə kitab var?', [90], word(['📚'], ['450', ':', '5', '=', BOX]))
t.num('936 almanı 3 qutuya bərabər yığdılar. Hər qutuda neçə alma var?', [312], word(['🍎', '📦'], ['936', ':', '3', '=', BOX]))
t.choice('Qisməti 120 olan ifadəni dairəyə alın.', ['360 : 3', '240 : 3', '480 : 3'], 0)

# ============================================================ 128
t = T(128, 'Vurma və bölmənin digər üsulları',
      'Vuruğu iki ədədin cəmi və ya fərqi kimi yazıb asan vurmaq olar: 52 · 9 = 450 + 18 = 468, 39 · 6 = 240 − 6 = 234.',
      vstack([expr2(['52', '·', '9', '=', '(', '50', '+', '2', ')', '·', '9', '=', '468'], 44), expr2(['39', '·', '6', '=', '(', '40', '−', '1', ')', '·', '6', '=', '234'], 44)], 12))
t.num('52 = 50 + 2. Hasili tapın.', [18, 468], E('52', '·', '9', '=', '450', '+', BOX, '=', BOX), disp='18, 468')
t.num('39 = 40 − 1. Hasili tapın.', [6, 234], E('39', '·', '6', '=', '240', '−', BOX, '=', BOX), disp='6, 234')
t.num('207 = 200 + 7. Hasili tapın.', [28, 828], E('207', '·', '4', '=', '800', '+', BOX, '=', BOX), disp='28, 828')
t.num('196 = 200 − 4. Hasili tapın.', [12, 588], E('196', '·', '3', '=', '600', '−', BOX, '=', BOX), disp='12, 588')
t.num('Hesablayın.', [0], E('10', '·', '30', '·', '0', '=', BOX))
t.num('41 = 40 + 1. Hasili tapın.', [205], E('41', '·', '5', '=', BOX))
t.num('99 = 100 − 1. Hasili tapın.', [396], E('99', '·', '4', '=', BOX))
t.num('Bölünəni cəm kimi yazıb bölün.', [20, 4, 24], stacked([['96', ':', '4', '=', '(', '80', '+', '16', ')', ':', '4'], ['=', BOX, '+', BOX, '=', BOX]], 50), disp='20 + 4 = 24')
t.num('Maşın hər gün 48 km yol gedir. 5 gündə neçə kilometr gedər?', [240], word(['🚗'], ['48', '·', '5', '=', BOX]))
t.choice('49 · 5 hasilini asan tapmaq üçün hansı yol uyğundur? Dairəyə alın.', ['(50 − 1) · 5', '(40 + 1) · 5', '49 + 5'], 0)

# ============================================================ 129
t = T(129, 'Tam və bərabər hissələr. Kəsr',
      'Tamı bərabər hissələrə bölüb bir hissəni kəsrlə yazırıq. Xəttin altındakı ədəd məxrəcdir: neçə hissəyə bölündüyünü göstərir. Üstdəki ədəd surətdir.',
      hstack([frac_circle(4, 1, 150), F(1, 4, 70), frac_bar(3, 1, 240, 70), F(1, 3, 70)], 24))
t.choice('Rənglənmiş hissəni göstərən kəsri dairəyə alın.', [F(1, 4), F(1, 2), F(1, 3)], 0, stem=frac_circle(4, 1), disp='1/4')
t.choice('Rənglənmiş hissəni göstərən kəsri dairəyə alın.', [F(1, 2), F(1, 3), F(1, 4)], 1, stem=frac_circle(3, 1), disp='1/3')
t.choice('Rənglənmiş hissəni göstərən kəsri dairəyə alın.', [F(1, 6), F(1, 5), F(1, 4)], 0, stem=frac_bar(6, 1), disp='1/6')
t.choice('Hansı fiqur bərabər hissələrə bölünüb? Dairəyə alın.', [frac_bar(4, 0, 260, 70), hstack([frac_bar(1, 0, 70, 70), frac_bar(1, 0, 190, 70)], 0)], 0, disp='1-ci şəkil')
t.num('Dairə neçə bərabər hissəyə bölünüb?', [8], hstack([frac_circle(8, 0), arrow(), box()], 16))
t.num('Neçə hissə rənglənib?', [2], hstack([frac_bar(5, 2), arrow(), box()], 16))
t.num('Kəsrin məxrəci neçədir?', [7], hstack([F(3, 7, 80), arrow(), box()], 16))
t.num('Kəsrin surəti neçədir?', [2], hstack([F(2, 9, 80), arrow(), box()], 16))
t.choice('Pizzanın yarısını göstərən şəkli dairəyə alın.', [frac_circle(2, 1, 120), frac_circle(4, 1, 120), frac_circle(3, 1, 120)], 0, disp='1-ci şəkil')
t.choice('«Beşdə bir» kəsrini dairəyə alın.', [F(1, 5), F(5, 1), F(1, 4)], 0, disp='1/5')

# ============================================================ 130
t = T(130, 'Ədədin hissəsi',
      '7 bayraqdan 3-ü yaşıldır: yaşıl bayraqlar bütün bayraqların yeddidə üç hissəsidir. 8-in yarısını tapmaq üçün 8-i 2-yə bölürük: 8 : 2 = 4.',
      vstack([hstack([em('🟩', 50)] * 3 + [em('🟧', 50)] * 4, 6), hstack([F(3, 7, 54), blank(30, 10), expr2(['8', ':', '2', '=', '4'], 54)], 10)], 14))
t.choice('Armudlar meyvələrin hansı hissəsidir? Dairəyə alın.', [F(2, 5), F(3, 5), F(2, 3)], 0, stem=hstack([em('🍐', 70)] * 2 + [em('🍎', 70)] * 3, 6), disp='2/5')
t.choice('Qırmızı dairələr hansı hissədir? Dairəyə alın.', [F(1, 4), F(1, 3), F(3, 4)], 0, stem=hstack([em('🔴', 70)] + [em('🔵', 70)] * 3, 6), disp='1/4')
for a, b, n_, sf in [(1, 2, 8, '-in'), (1, 3, 12, '-nin'), (1, 4, 20, '-nin'), (1, 5, 30, '-un')]:
    t.num('Ədədin hissəsini tapın.', [n_ // b], hstack([txt(str(n_), 64), txt(sf, 34, GREY), F(a, b, 56), txt('hissəsi:', 34, GREY), E(str(n_), ':', str(b), '=', BOX)], 12))
t.num('18 şarın üçdə biri qırmızıdır. Neçə qırmızı şar var?', [6], word(['🎈'], ['18', ':', '3', '=', BOX]))
t.num('Sinifdə 24 şagird var. Onların yarısı qızdır. Neçə qız var?', [12], word(['👧', '👦'], ['24', ':', '2', '=', BOX]))
t.num('10 qələmin beşdə biri göydür. Neçə göy qələm var?', [2], word(['🖊️'], ['10', ':', '5', '=', BOX]))
t.choice('6-nın yarısı neçədir? Dairəyə alın.', ['3', '2', '12'], 0)

# ============================================================ 131
t = T(131, 'Kəsrlərin müqayisəsi',
      'Məxrəcləri bərabər olan kəsrlərdən surəti böyük olan kəsr böyükdür: 5/6 > 2/6.',
      vstack([hstack([frac_bar(6, 5, 300, 60), F(5, 6, 48)], 16), hstack([frac_bar(6, 2, 300, 60), F(2, 6, 48)], 16)], 12))
t.sign('Kəsrləri müqayisə edin. Dairəyə >, < və ya = yazın.', [('5/6', '2/6')], ['>'], stem=vstack([frac_bar(6, 5, 300, 56), frac_bar(6, 2, 300, 56)], 10))
t.sign('Kəsrləri müqayisə edin. Dairəyə işarə yazın.', [('3/7', '4/7')], ['<'], stem=vstack([frac_bar(7, 3, 300, 56), frac_bar(7, 4, 300, 56)], 10))
t.sign('Kəsrləri müqayisə edin. Dairələrə işarə yazın.', [('2/5', '2/5'), ('7/9', '5/9')], ['=', '>'])
t.sign('Kəsrləri müqayisə edin. Dairələrə işarə yazın.', [('6/13', '9/13'), ('1/4', '3/4')], ['<', '<'])
t.choice('Ən böyük kəsri dairəyə alın.', [F(5, 8), F(3, 8), F(7, 8)], 2, disp='7/8')
t.choice('Ən kiçik kəsri dairəyə alın.', [F(4, 9), F(2, 9), F(8, 9)], 1, disp='2/9')
t.choice('Hansı daha böyükdür: tortun yarısı, yoxsa dörddə biri? Dairəyə alın.', [frac_circle(2, 1, 120), frac_circle(4, 1, 120)], 0, disp='yarısı (1/2)')
t.choice('Kəsrləri artan sıra ilə düzün: ən kiçikdən başlayaraq toxunun.', [F(3, 5), F(1, 5), F(4, 5)], [1, 0, 2], mode='order', hint='Məxrəclər bərabərdir: surətlərə baxın.', disp='1/5, 3/5, 4/5')
t.num('Boş xanaya uyğun surəti yazın.', [6], hstack([F(5, 7, 60), txt('<', 60, BLUE), vstack([box(70, 64), blank(80, 6), txt('7', 56)], 2), txt('<', 60, BLUE), F(7, 7, 60)], 14))
t.choice('Lalə tortun 2/8, Anar isə 5/8 hissəsini yedi. Kim çox yedi? Dairəyə alın.', ['Anar', 'Lalə'], 0, stem=hstack([label(frac_circle(8, 2, 120), 'Lalə', 30, INK), label(frac_circle(8, 5, 120), 'Anar', 30, INK)], 30, 'bottom'))

# ============================================================ 132
H4 = ('Minliklər', 'Yüzlüklər', 'Onluqlar', 'Təkliklər')
t = T(132, 'Dördrəqəmli ədədlər',
      '10 yüzlük 1 minlik təşkil edir. Dördrəqəmli ədədlərdə sağdan dördüncü rəqəm minlikləri göstərir: 2 324 = 2 000 + 300 + 20 + 4.',
      vstack([place_table([2, 3, 2, 4], H4), expr2(['2324', '=', '2000', '+', '300', '+', '20', '+', '4'], 46)], 14))
t.num('Mərtəbə cədvəlinə baxın və ədədi yazın.', [2324], hstack([place_table([2, 3, 2, 4], H4), arrow(), box(200, 100)], 16))
t.num('Mərtəbə cədvəlinə baxın və ədədi yazın.', [5071], hstack([place_table([5, 0, 7, 1], H4), arrow(), box(200, 100)], 16))
t.num('Ədədi açıq şəkildə yazın.', [3000, 400, 50, 6], expr2(['3456', '=', BOX, '+', BOX, '+', BOX, '+', BOX], 56), disp='3000 + 400 + 50 + 6')
t.num('Ədədi açıq şəkildə yazın.', [7000, 80], expr2(['7080', '=', BOX, '+', BOX], 66), disp='7000 + 80')
t.num('Cəmə uyğun ədədi yazın.', [4605], E('4000', '+', '600', '+', '5', '=', BOX))
t.num('Yüz-yüz sayın. Sıranı davam etdirin.', [2700, 2800], seq([2400, 2500, 2600, BOX, BOX], 50), disp='2700, 2800')
t.num('Min-min sayın. Sıranı davam etdirin.', [6000, 7000], seq([3000, 4000, 5000, BOX, BOX], 50), disp='6000, 7000')
t.sign('Ədədləri müqayisə edin. Dairələrə >, < və ya = yazın.', [('4521', '4512'), ('3099', '3100')], ['>', '<'])
t.choice('«İki min üç yüz iyirmi dörd» hansı ədəddir? Dairəyə alın.', ['2324', '2234', '3224'], 0)
t.num('Ən böyük dördrəqəmli ədədi yazın.', [9999], hstack([txt('? ? ? ?', 64, GREY), arrow(), box(200, 100)], 16))

# ============================================================ 133
t = T(133, 'Pullarla hesablamalar',
      '1 manat = 100 qəpik. 2 manat 68 qəpik = 268 qəpik. Hesablamaq üçün manatı qəpiklə ifadə edirik: 268 qəp + 345 qəp = 613 qəp = 6 manat 13 qəpik.',
      vstack([expr2(['1', 'man', '=', '100', 'qəp'], 50), expr2(['2', 'man', '68', 'qəp', '=', '268', 'qəp'], 50)], 12))
for m, q in [(2, 68), (3, 45), (5, 9)]:
    t.num('Qəpiklə ifadə edin.', [m * 100 + q], unit_expr([str(m), 'man', str(q), 'qəp', '=', BOX, 'qəp'], 60), disp='%d qəpik' % (m * 100 + q))
t.num('Manat və qəpiklə ifadə edin: soldan sağa yazın.', [6, 13], unit_expr(['613', 'qəp', '=', BOX, 'man', BOX, 'qəp'], 60), disp='6 man 13 qəp')
t.num('Manat və qəpiklə ifadə edin: soldan sağa yazın.', [4, 50], unit_expr(['450', 'qəp', '=', BOX, 'man', BOX, 'qəp'], 60), disp='4 man 50 qəp')
t.num('Çörək 268 qəpik, süd 345 qəpikdir. Hamısı neçə qəpikdir?', [613], vstack([hstack([priced('🍞', '2 man 68 qəp'), priced('🥛', '3 man 45 qəp')], 30), unit_expr(['268', '+', '345', '=', BOX, 'qəp'], 56)], 14), disp='613 qəpik')
t.num('Süd çörəkdən neçə qəpik bahadır?', [77], vstack([hstack([priced('🥛', '345 qəp'), priced('🍞', '268 qəp')], 30), unit_expr(['345', '−', '268', '=', BOX, 'qəp'], 56)], 14), disp='77 qəpik')
t.num('Lalənin 5 manatı var. O, 3 manat 20 qəpiklik kitab aldı. Neçə qəpiyi qaldı?', [180], vstack([priced('📘', '3 man 20 qəp'), unit_expr(['500', '−', '320', '=', BOX, 'qəp'], 56)], 14), disp='180 qəpik (1 man 80 qəp)')
t.sign('Müqayisə edin. Dairələrə >, < və ya = yazın.', [('3 man 5 qəp', '350 qəp'), ('2 man', '200 qəp')], ['<', '='])
t.choice('Hansı məbləğ 1 manat 50 qəpikdir? Dairəyə alın.', ['150 qəp', '105 qəp', '1500 qəp'], 0)

# ============================================================ 134
t = T(134, 'Gəlir, xərc, qazanc',
      'İşləyib və ya satıb əldə edilən pul gəlirdir. Xərclənən pul xərcdir. Gəlirdən xərci çıxanda qazanc qalır: 150 man − 90 man = 60 man.',
      vstack([expr2(['5', '·', '30', 'man', '=', '150', 'man'], 48), expr2(['150', 'man', '−', '90', 'man', '=', '60', 'man'], 48)], 12))
t.num('Usta hər gün 30 manat qazanır. 5 gündə onun gəliri neçə manat olar?', [150], word(['🧑‍🔧'], ['5', '·', '30', '=', BOX]))
t.num('Mağaza 24 manatlıq 10 kisə un satdı. Mağazanın gəliri neçə manatdır?', [240], word(['🌾', '🏪'], ['10', '·', '24', '=', BOX]))
t.num('Usta 1 detalı 2 manata satır. 56 detaldan neçə manat gəlir əldə edər?', [112], word(['⚙️'], ['56', '·', '2', '=', BOX]))
t.num('Əli usta 1 saata 10 manat alır. 8 saatlıq iş günündə neçə manat qazanar?', [80], word(['🔨'], ['8', '·', '10', '=', BOX]))
t.num('Satıcının gəliri 150 manat, xərci 90 manatdır. Qazancı neçə manatdır?', [60], word(['💵'], ['150', '−', '90', '=', BOX]))
t.num('Ailənin aylıq gəliri 900 manatdır. Ərzağa 350 manat xərclədilər. Neçə manat qaldı?', [550], word(['🏠', '🛒'], ['900', '−', '350', '=', BOX]))
t.num('Lalə 3 rəsmi 15 manatdan satdı. Boyalara 20 manat xərcləmişdi. Əvvəl gəliri, sonra qazancı tapın.', [45, 25], vstack([em('🎨', 90), stacked([['3', '·', '15', '=', BOX], ['45', '−', '20', '=', BOX]], 52)], 12), disp='45, 25')
t.choice('Gəlir 200 manat, xərc 120 manatdır. Qazanc nə qədərdir? Dairəyə alın.', ['80 manat', '320 manat', '120 manat'], 0)
t.choice('Hansı xərcdir? Dairəyə alın.', ['Ərzaq almaq', 'Maaş almaq', 'Rəsm satmaq'], 0)
t.num('Fermer 40 kq pomidoru 3 manatdan satdı. Gəliri neçə manatdır?', [120], word(['🍅'], ['40', '·', '3', '=', BOX]))

# ============================================================ 135
t = T(135, 'Uzunluq',
      'Kiçik uzunluqları millimetrlə ölçürük: 1 sm = 10 mm. Uzunluq vahidləri: 1 dm = 10 sm, 1 m = 10 dm = 100 sm, 1 km = 1000 m.',
      vstack([on_ruler(strip(5, 60, BLUE), 6, 60), unit_expr(['1', 'sm', '=', '10', 'mm'], 50), unit_expr(['1', 'm', '=', '100', 'sm'], 50)], 12))
for toks, v, d_ in [(['3', 'sm', '=', BOX, 'mm'], 30, '30 mm'), (['5', 'dm', '=', BOX, 'sm'], 50, '50 sm'), (['4', 'm', '=', BOX, 'dm'], 40, '40 dm'), (['2', 'km', '=', BOX, 'm'], 2000, '2000 m'), (['2', 'm', '20', 'sm', '=', BOX, 'sm'], 220, '220 sm')]:
    t.num('Vahidləri çevirin.', [v], unit_expr(toks, 60), disp=d_)
t.num('Karandaş neçə santimetr və neçə millimetrdir? Soldan sağa yazın.', [5, 4], vstack([on_ruler(pencil(5.4, 60), 7, 60), unit_expr([BOX, 'sm', BOX, 'mm'], 56)], 12), disp='5 sm 4 mm')
t.num('Hesablayın.', [85], unit_expr(['45', 'mm', '+', '40', 'mm', '=', BOX, 'mm'], 56), disp='85 mm')
t.choice('Buğda dənəsinin uzunluğu təxminən nə qədərdir? Dairəyə alın.', ['6 mm', '6 sm', '6 m'], 0, stem=em('🌾', 110))
t.choice('Şəhərlər arasındakı məsafəni hansı vahidlə ölçürlər? Dairəyə alın.', ['km', 'mm', 'sm'], 0, stem=em('🛣️', 110))
t.num('Lent 1 m idi. Ondan 35 sm kəsdilər. Neçə santimetr qaldı?', [65], vstack([em('🎀', 90), unit_expr(['100', 'sm', '−', '35', 'sm', '=', BOX, 'sm'], 54)], 12), disp='65 sm')

# ============================================================ 136
t = T(136, 'Perimetr və sahə',
      'Çoxbucaqlının tərəflərinin cəmi onun perimetridir: 6 + 3 + 6 + 3 = 18 sm. Fiqurun tutduğu kvadrat xanaların sayı onun sahəsini göstərir.',
      hstack([rect_sides(6, 3, '6 sm', '3 sm', 30), area_grid({(c, r) for c in range(3) for r in range(2)}, 4, 3, 40)], 30))
t.num('Düzbucaqlının perimetrini tapın.', [18], vstack([rect_sides(6, 3, '6 sm', '3 sm', 28), expr2(['6', '+', '3', '+', '6', '+', '3', '=', BOX], 52)], 10), disp='18 sm')
t.num('Kvadratın perimetrini tapın.', [20], vstack([rect_sides(4, 4, '5 sm', '5 sm', 30), expr2(['4', '·', '5', '=', BOX], 56)], 10), disp='20 sm')
t.num('Üçbucağın perimetrini tapın.', [21], hstack([tri(SCAL, ('5 sm', '7 sm', '9 sm'), 170), unit_expr(['=', BOX, 'sm'], 56)], 10), disp='21 sm')
t.num('Beşbucaqlının tərəfləri 5, 6, 3, 4 və 3 sm-dir. Perimetri neçə santimetrdir?', [21], vstack([poly(5, 150, (255, 224, 178)), expr2(['5', '+', '6', '+', '3', '+', '4', '+', '3', '=', BOX], 48)], 10), disp='21 sm')
t.num('Düzbucaqlının perimetrini tapın.', [22], vstack([rect_sides(8, 3, '8 m', '3 m', 26), unit_expr(['=', BOX, 'm'], 56)], 10), disp='22 m')
for cells, cols, rows, a in [({(c, r) for c in range(4) for r in range(2)}, 5, 3, 8), ({(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (0, 2)}, 4, 3, 6), ({(c, r) for c in range(3) for r in range(3)}, 4, 4, 9)]:
    t.num('Fiqurun sahəsi neçə kvadrat xanadır?', [a], hstack([area_grid(cells, cols, rows, 42), arrow(), box()], 16), disp='%d xana' % a)
t.choice('Hansı fiqurun sahəsi böyükdür? Dairəyə alın.', [area_grid({(0, 0), (1, 0), (2, 0), (0, 1)}, 3, 2, 36), area_grid({(0, 0), (1, 0), (0, 1), (1, 1), (2, 1), (2, 0)}, 3, 2, 36)], 1, disp='2-ci fiqur (6 xana)')
t.num('Bağçanın uzunluğu 9 m, eni 4 m-dir. Ətrafına neçə metr hasar lazımdır?', [26], vstack([rect_sides(9, 4, '9 m', '4 m', 24), expr2(['9', '+', '4', '+', '9', '+', '4', '=', BOX], 50)], 10), disp='26 m')

# ============================================================ 137
t = T(137, 'Kütlə',
      '1 kq = 1000 q. Yarım kiloqram 500 qramdır. 1 kq 200 q = 1200 q. Çox ağır yükləri tonla ölçürük: 1 t = 1000 kq.',
      vstack([unit_expr(['1', 'kq', '=', '1000', 'q'], 52), unit_expr(['1', 'kq', '200', 'q', '=', '1200', 'q'], 52)], 12))
for toks, v, d_ in [(['2', 'kq', '=', BOX, 'q'], 2000, '2000 q'), (['2', 'kq', '350', 'q', '=', BOX, 'q'], 2350, '2350 q'), (['5', 'kq', '470', 'q', '=', BOX, 'q'], 5470, '5470 q'), (['6', 'kq', '25', 'q', '=', BOX, 'q'], 6025, '6025 q')]:
    t.num('Qramla ifadə edin.', [v], unit_expr(toks, 58), disp=d_)
t.num('Kiloqram və qramla ifadə edin: soldan sağa yazın.', [3, 250], unit_expr(['3250', 'q', '=', BOX, 'kq', BOX, 'q'], 56), disp='3 kq 250 q')
t.num('Yarım kiloqram neçə qramdır?', [500], unit_expr(['yarım', 'kq', '=', BOX, 'q'], 60), disp='500 q')
t.num('Tərəzi bərabərdir. Çay qutusu neçə qramdır?', [300], hstack([scale([em('🍵', 80), gram(200)], [gram(500)], 0, 480), box(), txt('q', 44, BLUE)], 12), disp='300 q')
t.num('Bir kisədə 25 kq, o birində 18 kq un var. Cəmi neçə kiloqram un var?', [43], word(['🌾', '🌾'], ['25', '+', '18', '=', BOX]))
t.choice('Bir almanın kütləsi təxminən nə qədərdir? Dairəyə alın.', ['200 q', '2 kq', '20 kq'], 0, stem=em('🍎', 110))
t.choice('Hansı çox ağırdır? Dairəyə alın.', ['1 t', '100 kq', '1000 q'], 0)

# ============================================================ 138
t = T(138, 'Tutum',
      'Kiçik qabların tutumunu millilitrlə ölçürük: 1 l = 1000 ml. Yarım litr 500 ml-dir. 2 l 500 ml = 2500 ml.',
      vstack([unit_expr(['1', 'l', '=', '1000', 'ml'], 52), unit_expr(['2', 'l', '500', 'ml', '=', '2500', 'ml'], 52)], 12))
for toks, v, d_ in [(['3', 'l', '=', BOX, 'ml'], 3000, '3000 ml'), (['2', 'l', '500', 'ml', '=', BOX, 'ml'], 2500, '2500 ml'), (['1', 'l', '200', 'ml', '=', BOX, 'ml'], 1200, '1200 ml')]:
    t.num('Millilitrlə ifadə edin.', [v], unit_expr(toks, 58), disp=d_)
t.num('Litr və millilitrlə ifadə edin: soldan sağa yazın.', [4, 750], unit_expr(['4750', 'ml', '=', BOX, 'l', BOX, 'ml'], 56), disp='4 l 750 ml')
t.num('Yarım litr neçə millilitrdir?', [500], unit_expr(['yarım', 'l', '=', BOX, 'ml'], 60), disp='500 ml')
t.choice('Şprisin tutumu təxminən nə qədərdir? Dairəyə alın.', ['5 ml', '5 l', '50 l'], 0, stem=em('💉', 110))
t.choice('Vannanın tutumu təxminən nə qədərdir? Dairəyə alın.', ['200 l', '200 ml', '2 l'], 0, stem=em('🛁', 110))
t.num('Qabda 1 l su var idi. 250 ml su içdilər. Neçə millilitr su qaldı?', [750], word(['🥤'], ['1000', '−', '250', '=', BOX]), disp='750 ml')
t.num('Hər stəkana 200 ml şirə tökdülər. 5 stəkana neçə millilitr şirə töküldü?', [1000], word(['🧃', '🥛'], ['5', '·', '200', '=', BOX]), disp='1000 ml (1 l)')
t.num('24 l süd 3 litrlik balonlara töküldü. Neçə balon alındı?', [8], word(['🥛'], ['24', ':', '3', '=', BOX]))

# ============================================================ 139
t = T(139, 'Saat',
      'Rəqəmsal saatda 12:00-a qədər vaxt günün birinci yarısını, 12:00-dan sonrakı vaxt isə ikinci yarısını göstərir: 13:15 – günortadan sonra saat 1-i 15 dəqiqə keçir.',
      hstack([digital('13:15', 60), clock(1, 180, 15)], 30))
t.num('Rəqəmsal saat neçəni göstərir? Saatı və dəqiqəni soldan sağa yazın.', [7, 24], hstack([digital('07:24', 64), arrow(), box(), txt(':', 60), box()], 12), disp='7:24')
t.num('Rəqəmsal saat neçəni göstərir? Saatı və dəqiqəni soldan sağa yazın.', [21, 34], hstack([digital('21:34', 64), arrow(), box(), txt(':', 60), box()], 12), disp='21:34')
t.choice('13:00 günün hansı yarısıdır? Dairəyə alın.', ['Günortadan sonra', 'Günortaya qədər'], 0, stem=digital('13:00', 64))
t.choice('Saat 3 tamamdır (günortadan sonra). Rəqəmsal saatda necə görünür? Dairəyə alın.', ['15:00', '03:00', '13:00'], 0)
t.num('1 saat neçə dəqiqədir?', [60], unit_expr(['1', 'saat', '=', BOX, 'dəq'], 60), disp='60 dəq')
t.num('Dərs 9:00-da başladı və 45 dəqiqə davam etdi. Dərs neçədə bitdi? Saatı və dəqiqəni yazın.', [9, 45], hstack([digital('09:00', 56), arrow(), box(), txt(':', 56), box()], 12), disp='9:45')
t.num('Film 18:30-da başladı, 20:00-da bitdi. Film neçə dəqiqə davam etdi?', [90], vstack([hstack([digital('18:30', 50), arrow(), digital('20:00', 50)], 12), unit_expr([BOX, 'dəq'], 56)], 12), disp='90 dəqiqə')
t.num('Saat neçə tamamdır?', [4], hstack([clock(4, 200), arrow(), box()], 16), disp='saat 4')
t.num('Uzun əqrəb 3-ün üstündədir. Saat 11-ə neçə dəqiqə işləyib?', [15], hstack([clock(10, 200, 15), arrow(), box(), txt('dəq', 40, BLUE)], 16), disp='15 dəqiqə')
t.choice('Hansı daha uzundur? Dairəyə alın.', ['1 saat', '50 dəqiqə'], 0)

# ============================================================ 140
MONTHS = ['Sen', 'Okt', 'Noy', 'Dek', 'Yan']
EXC = [100, 200, 300, 250, 150]
t = T(140, 'Xətti diaqram',
      'Xətti diaqram kəmiyyətin zamana görə dəyişməsini göstərir: nöqtələr xətlərlə birləşdirilir. Yanvarda ekskursiyaya 150 şagird gedib.',
      line_chart(MONTHS, EXC, 350, 50))
t.num('Diaqrama baxın. Oktyabrda neçə şagird ekskursiyaya gedib?', [200], hstack([line_chart(MONTHS, EXC, 350, 50, 440, 260), arrow(), box(150, 96)], 12))
t.num('Diaqrama baxın. Noyabrda neçə şagird gedib?', [300], hstack([line_chart(MONTHS, EXC, 350, 50, 440, 260), arrow(), box(150, 96)], 12))
t.choice('Hansı ayda ekskursiyaya ən çox şagird gedib? Dairəyə alın.', ['Noyabr', 'Dekabr', 'Sentyabr'], 0, stem=line_chart(MONTHS, EXC, 350, 50, 440, 260))
t.choice('Hansı ayda ən az şagird gedib? Dairəyə alın.', ['Sentyabr', 'Yanvar', 'Oktyabr'], 0, stem=line_chart(MONTHS, EXC, 350, 50, 440, 260))
t.num('Noyabrda sentyabrdan neçə şagird çox gedib?', [200], vstack([line_chart(MONTHS, EXC, 350, 50, 440, 240), expr2(['300', '−', '100', '=', BOX], 52)], 10))
TEMP = [8, 12, 15, 11, 6]
DAYS = ['B.e', 'Ç.a', 'Ç', 'C.a', 'C']
t.num('Havanın temperaturu diaqramda göstərilib. Çərşənbə günü neçə dərəcə olub?', [15], hstack([line_chart(DAYS, TEMP, 20, 5, 440, 260, RED), arrow(), box()], 12))
t.choice('Temperatur hansı gün ən aşağı olub? Dairəyə alın.', ['Cümə', 'Bazar ertəsi', 'Çərşənbə'], 0, stem=line_chart(DAYS, TEMP, 20, 5, 440, 260, RED))
t.num('Çərşənbə axşamı ilə bazar ertəsi arasında temperatur neçə dərəcə fərqlənir?', [4], vstack([line_chart(DAYS, TEMP, 20, 5, 440, 240, RED), expr2(['12', '−', '8', '=', BOX], 52)], 10))
t.choice('Temperatur çərşənbədən cüməyə qədər necə dəyişib? Dairəyə alın.', ['Azalıb', 'Artıb', 'Dəyişməyib'], 0, stem=line_chart(DAYS, TEMP, 20, 5, 440, 260, RED))
t.num('Sentyabr və oktyabrda cəmi neçə şagird ekskursiyaya gedib?', [300], vstack([line_chart(MONTHS, EXC, 350, 50, 440, 240), expr2(['100', '+', '200', '=', BOX], 52)], 10))

# ============================================================ 141
EVN = ['Mümkün deyil', 'Çətin ki, olsun', 'Çox güman ki, olacaq', 'Mütləq olacaq']
BAG = hstack([em('🟦', 56)] * 5 + [em('🟥', 56)], 6)
t = T(141, 'Hadisələr',
      'Hadisə haqqında belə deyirik: «mümkün deyil», «çətin ki, olsun», «çox güman ki, olacaq», «mütləq olacaq». Torbada 5 göy və 1 qırmızı kub var: çıxan kub çox güman ki, göy olacaq.',
      BAG)
t.choice('Torbada 5 göy və 1 qırmızı kub var. Baxmadan bir fiqur çıxarılır. «Çıxan fiqur kürədir» – bu necədir?', EVN, 0, stem=BAG)
t.choice('Torbada 5 göy və 1 qırmızı kub var. «Çıxan kub qırmızıdır» – bu necədir?', EVN, 1, stem=BAG)
t.choice('Torbada 5 göy və 1 qırmızı kub var. «Çıxan kub göydür» – bu necədir?', EVN, 2, stem=BAG)
t.choice('Torbada 5 göy və 1 qırmızı kub var. «Çıxan fiqur kubdur» – bu necədir?', EVN, 3, stem=BAG)
t.choice('Zər atılır. «6 düşəcək» – bu necədir?', EVN, 1, stem=die(6, 110))
t.choice('Zər atılır. «7 düşəcək» – bu necədir?', EVN, 0, stem=die(1, 110))
t.choice('«Yanvardan sonra fevral gələcək» – bu necədir?', EVN, 3, stem=em('🗓️', 110))
t.choice('Qışda «sabah qar yağacaq» – bu necədir?', EVN[1:3], 1, stem=em('🌨️', 110))
t.num('Torbada 5 göy və 1 qırmızı kub var. Cəmi neçə kub var?', [6], hstack([BAG, arrow(), box()], 12))
t.num('Zərin neçə üzü var?', [6], hstack([die(5, 110), arrow(), box()], 12))

# ============================================================ 142
SPORT = [('Futbol', 9), ('Üzgüçülük', 5), ('Basketbol', 4), ('Şahmat', 6)]
t = T(142, 'Məlumatların təsviri. Praktik dərs',
      'Sorğu keçiririk: hamıya eyni sualı veririk, cavabları cədvəldə qeyd edirik və diaqram qururuq. Sonra diaqrama baxıb nəticə çıxarırıq.',
      hstack([tab([['İdman', 'Uşaq']] + [[a, v] for a, v in SPORT], 28), bars([(txt(a[:6], 20), v) for a, v in SPORT], maxv=10, unit=24, barw=60, colors=[G3, B3, O3, P3])], 24, 'bottom'))
TB = tab([['İdman', 'Uşaq']] + [[a, v] for a, v in SPORT], 30)
t.num('Cədvələ baxın. Neçə uşaq futbolu seçib?', [9], hstack([TB, arrow(), box()], 14))
t.num('Sorğuda cəmi neçə uşaq iştirak edib?', [24], vstack([TB, expr2(['9', '+', '5', '+', '4', '+', '6', '=', BOX], 48)], 10))
t.choice('Ən çox uşaq hansı idmanı seçib? Dairəyə alın.', ['Futbol', 'Şahmat', 'Üzgüçülük'], 0, stem=TB)
t.num('Futbolu seçənlər basketbolu seçənlərdən neçə nəfər çoxdur?', [5], vstack([TB, expr2(['9', '−', '4', '=', BOX], 52)], 10))
t.num('Cizgiləri sayın. Neçə uşaq şahmatı seçib?', [6], hstack([tally(6, 80), arrow(), box()], 16))
t.choice('Diaqramda ən hündür sütun hansı idmandır? Dairəyə alın.', ['Futbol', 'Basketbol', 'Üzgüçülük'], 0, stem=bars([(txt(a[:6], 20), v) for a, v in SPORT], maxv=10, unit=24, barw=60, colors=[G3, B3, O3, P3]))
t.num('Üzgüçülük və basketbolu seçənlər cəmi neçə nəfərdir?', [9], vstack([TB, expr2(['5', '+', '4', '=', BOX], 52)], 10))
t.choice('Sorğu üçün hansı sual uyğundur? Dairəyə alın.', ['Ən çox hansı idman növünü sevirsiniz?', '5 + 4 neçədir?', 'Bu gün neçənci gündür?'], 0)
t.num('Sinifdə 28 şagird var. Sorğuda 24 nəfər iştirak edib. Neçə şagird iştirak etməyib?', [4], word(['🏫'], ['28', '−', '24', '=', BOX]))
t.choice('Şahmatı seçənlər üzgüçülüyü seçənlərdən çoxdurmu? Dairəyə alın.', ['Bəli, 1 nəfər çox', 'Xeyr, az', 'Bərabərdir'], 0)

save()
