"""2-ci sinif riyaziyyat, 1-ci hissə: 20 mövzu (50–69), hər mövzuda 10 tapşırıq.
Run: python3 content.py OUTDIR   -> OUTDIR/img/*.webp, OUTDIR/data/topics.json, OUTDIR/data/voice.json"""
import hashlib, json, os, sys
from draw import *
from draw2 import *

OUT = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/riyaziyyat/2-1'
IMG = os.path.join(OUT, 'img')
VOICE = {}


def aid(text):
    h = hashlib.md5(text.encode()).hexdigest()[:10]
    VOICE[h] = text
    return h


def ordn(k):
    n = k + 1
    suf = {1: 'ci', 2: 'ci', 3: 'cü', 4: 'cü', 5: 'ci', 6: 'cı', 7: 'ci', 8: 'ci'}[n]
    return '%d-%s' % (n, suf)


class Topic:
    def __init__(self, n, title, concept, cimg):
        self.n, self.title, self.concept = n, title, concept
        self.problems = []
        path = 'img/t%02d_c.webp' % n
        finish(cimg, os.path.join(OUT, path), maxw=1100)
        self.d = {'n': n, 'title': title, 'concept': concept, 'conceptImg': path, 'conceptAudio': aid(concept), 'problems': self.problems}

    def _p(self):
        return 't%02d_%02d' % (self.n, len(self.problems) + 1)

    def num(self, ins, slots, stem, disp=None):
        """write-answer problem; stem image must show the boxes"""
        base = self._p()
        path = 'img/%s.webp' % base
        finish(stem, os.path.join(OUT, path))
        disp = disp or ', '.join(str(v) for v in slots)
        self.problems.append({'img': path, 'ins': ins, 'ans': disp, 'icon': 'write', 'check': {'mode': 'num', 'slots': list(slots)}, 'web': None, 'audio': aid(ins)})

    def choice(self, ins, opts, ans, stem=None, disp=None, mode='choice', hint=None, osize=None):
        """opts: list of images or str (text option). ans: index (choice) or list (multi/order)"""
        base = self._p()
        web = {'mode': mode, 'stem': None, 'opts': []}
        full = []
        if stem is not None:
            sp = 'img/%s_s.webp' % base
            finish(stem, os.path.join(OUT, sp))
            web['stem'] = sp
            full.append(stem)
        row_ = []
        for k, o in enumerate(opts):
            if isinstance(o, str):
                web['opts'].append({'t': o})
                oi = chip(o, 56, fill=WHITE, outline=GREY)
            else:
                op = 'img/%s_o%d.webp' % (base, k)
                finish(o, os.path.join(OUT, op), margin=14, maxw=600)
                web['opts'].append({'img': op})
                oi = o
            row_.append(vstack([oi, txt(str(k + 1), 30, GREY)], 6))
        full.append(hstack(row_, 40, align='bottom'))
        web['ans'] = ans
        if hint:
            web['hint'] = hint
        path = 'img/%s.webp' % base
        finish(vstack(full, 30), os.path.join(OUT, path))
        if disp is None:
            if mode == 'choice':
                disp = opts[ans] if isinstance(opts[ans], str) else ordn(ans) + ' şəkil'
            elif mode == 'multi':
                disp = ', '.join(ordn(i) for i in ans)
            else:
                disp = ', '.join(ordn(i) for i in ans)
        self.problems.append({'img': path, 'ins': ins, 'ans': disp, 'icon': 'circle', 'check': None, 'web': web, 'audio': aid(ins)})


    def sign(self, ins, pairs, ans, stem=None):
        """>, <, = problem: pairs [(a, b)], ans list of signs; the picture shows the pairs with empty circles"""
        base = self._p()
        path = 'img/%s.webp' % base
        im = cmp_row(pairs) if stem is None else vstack([stem, cmp_row(pairs)], 24)
        finish(im, os.path.join(OUT, path))
        disp = ', '.join('%s %s %s' % (a, g, b) for (a, b), g in zip(pairs, ans))
        self.problems.append({'img': path, 'ins': ins, 'ans': disp, 'icon': 'write', 'check': {'mode': 'sign', 'slots': list(ans), 'pairs': [[str(a), str(b)] for a, b in pairs]}, 'web': None, 'audio': aid(ins)})


TOPICS = []


def T(*a):
    t = Topic(*a)
    TOPICS.append(t)
    return t


def seq(tokens, size=60):
    return hstack([box(int(size * 1.5), int(size * 1.35)) if v is BOX else chip(str(v), size - 6, WHITE, INK, GREY) for v in tokens], 14)


def nchip(v, size=56):
    return chip(str(v), size, WHITE, INK, GREY)


def stacked(rows_, size=58):
    return vstack([expr2(r, size) for r in rows_], 16, 'left')


def two_rows(top, bottom, op='+'):
    """addend pictures in two rows (keeps images narrow so numbers stay big)"""
    return vstack([hstack([blank(44, 10), top], 14), hstack([txt(op, 56, BLUE), bottom], 14)], 12, 'left')


def cartons(n, size=30):
    return hstack([frame(row('🥚', 10, size, 2, 5), 6) for _ in range(n)], 10)


B3 = (66, 165, 245); R3 = (239, 83, 80); G3 = (102, 187, 106); O3 = (255, 167, 38); P3 = (171, 71, 188); Y3 = (255, 213, 79)

# ============================================================ 50
t = T(50, 'Ədədlərin müqayisəsi', 'Əvvəlcə onluqları müqayisə edirik. Onluqlar bərabərdirsə, təklikləri müqayisə edirik: 47 < 52, 63 > 61.',
      vstack([hstack([label(tens_dots(4, 7, 22), '47', 40, INK), txt('<', 80, BLUE), label(tens_dots(5, 2, 22), '52', 40, INK)], 30), txt('4 onluq < 5 onluq', 36, BLUE)], 16))
t.sign('Nöqtələri say və ədədləri müqayisə et. Dairəyə >, < və ya = işarəsini yaz. Bir sütunda 10 nöqtə var.', [('35', '53')], ['<'], stem=hstack([tens_dots(3, 5, 20), blank(80, 10), tens_dots(5, 3, 20)], 20))
t.sign('Nöqtələri say və ədədləri müqayisə et. Dairəyə işarə yaz.', [('64', '46')], ['>'], stem=hstack([tens_dots(6, 4, 20), blank(80, 10), tens_dots(4, 6, 20)], 20))
t.sign('Ədədləri müqayisə et. Dairələrə >, < və ya = yaz.', [('29', '31'), ('58', '52'), ('70', '70')], ['<', '>', '='])
t.sign('Ədədləri müqayisə et. Dairələrə işarə yaz.', [('84', '48'), ('66', '69'), ('91', '19')], ['>', '<', '>'])
t.sign('Onluq və təklikləri müqayisə et. Dairəyə işarə yaz.', [('45', '50')], ['<'], stem=hstack([chip('4 onluq 5 təklik', 36, (255, 243, 224), INK, ORANGE), blank(40, 10), chip('5 onluq 0 təklik', 36, (255, 243, 224), INK, ORANGE)], 20))
t.choice('Ən böyük ədədi dairəyə al.', ['67', '76', '59', '70'], 1)
t.choice('Ən kiçik ədədi dairəyə al.', ['38', '83', '33', '80'], 2)
t.num('Ədəd oxuna bax. 50-dən 3 vahid böyük ədədi yaz.', [53], vstack([numline(50, 56, 70, start=50, jumps=3), expr2(['50', '+', '3', '=', BOX], 56)], 14))
t.choice('Səbinə 27 balıqqulağı yığdı. Anar ondan çox yığdı. Anarın vedrəsini dairəyə al.', [label(em('🪣', 90), '19', 40, INK), label(em('🪣', 90), '25', 40, INK), label(em('🪣', 90), '32', 40, INK)], 2, stem=label(em('🐚', 110), 'Səbinə – 27', 34, INK), disp='32')
t.num('Boş xanaya uyğun ədədi yaz.', [39], expr2(['38', '<', BOX, '<', '40'], 76))

# ============================================================ 51
t = T(51, 'Sıralama', 'Artan sıra: kiçikdən böyüyə – 23, 35, 48. Azalan sıra: böyükdən kiçiyə – 48, 35, 23.',
      vstack([hstack([txt('artan', 34, GREEN), seq([23, 35, 48], 54)], 16), hstack([txt('azalan', 34, RED), seq([48, 35, 23], 54)], 16)], 16, 'left'))
t.num('Ədəd oxunda boş xanalara uyğun ədədləri yaz.', [30, 70], numline_step(0, 100, 10, 62, blanks=(30, 70)), disp='30, 70')
t.num('Ədəd oxunda boş xanalara uyğun ədədləri yaz.', [43, 47], numline(40, 50, 66, blanks=(43, 47)), disp='43, 47')
t.choice('Ədədləri artan sıra ilə düz: ən kiçikdən başlayaraq toxun.', ['54', '38', '71'], [1, 0, 2], mode='order', hint='Əvvəlcə ən kiçik ədədə, sonra ortadakına, sonra ən böyüyə toxun.', disp='38, 54, 71')
t.choice('Ədədləri azalan sıra ilə düz: ən böyükdən başlayaraq toxun.', ['64', '82', '59', '27'], [1, 0, 2, 3], mode='order', hint='Əvvəlcə ən böyük ədədə toxun.', disp='82, 64, 59, 27')
t.choice('Artan sıranı pozan ədədi dairəyə al.', ['42', '45', '30', '55', '68'], 2)
t.choice('Azalan sıranı pozan ədədi dairəyə al.', ['64', '58', '68', '42', '31'], 2)
t.num('On-on say. Sıranı davam etdir.', [53, 63], seq([23, 33, 43, BOX, BOX]), disp='53, 63')
t.num('Beş-beş geri say. Sıranı davam etdir.', [80, 75], seq([95, 90, 85, BOX, BOX]), disp='80, 75')
t.num('Uşaqlar 32, 29 və 43 daş topladılar. Anar ən çox topladı. Anar neçə daş topladı?', [43], hstack([label(em('👦', 90), 'Anar', 30, INK), seq([32, 29, 43], 54), arrow(), box()], 20))
t.num('Yüzlük karta bax. Boş xanalara uyğun ədədləri yaz.', [66, 74], hundred(61, 2, (66, 74)), disp='66, 74')

# ============================================================ 52
t = T(52, 'İkirəqəmli ədədlə birrəqəmli ədədin toplanması', 'Təkliyi təkliyə əlavə edirik, onluqlar dəyişmir: 32 + 4 = 36.',
      vstack([two_rows(tens_ones(3, 2, 80), tens_ones(0, 4, 80)), expr2(['32', '+', '4', '=', '36'], 60)], 16))
t.num('Çöpləri say və cəmi tap.', [48], vstack([two_rows(tens_ones(4, 3, 76), tens_ones(0, 5, 76)), expr2(['43', '+', '5', '=', BOX], 64)], 16))
t.num('Ədəd oxunda 5 addım irəli get. Cəmi yaz.', [27], vstack([numline(20, 30, 62, start=22, jumps=5), expr2(['22', '+', '5', '=', BOX], 60)], 14))
for a, b in [(33, 4), (72, 6), (51, 7), (84, 5)]:
    t.num('Cəmi tap.', [a + b], expr2([str(a), '+', str(b), '=', BOX], 80))
t.num('Alt-alta topla.', [69], vcol(61, 8))
t.num('Əvvəlcə təklikləri, sonra onluqları topla.', [8, 68], stacked([['65', '+', '3', '=', '?'], ['5', '+', '3', '=', BOX], ['60', '+', '8', '=', BOX]]), disp='8, 68')
t.num('Elxan kitabın 32 səhifəsini oxudu. Lalə ondan 6 səhifə çox oxudu. Lalə neçə səhifə oxudu?', [38], hstack([em('📖', 110), expr2(['32', '+', '6', '=', BOX], 60)], 24))
t.num('Bidonda 23 litr süd var idi. Daha 5 litr süd tökdülər. Bidonda neçə litr süd oldu?', [28], hstack([em('🥛', 110), expr2(['23', '+', '5', '=', BOX], 60), txt('l', 48, BLUE)], 20), disp='28 litr')

# ============================================================ 53
t = T(53, 'Onluqların toplanması', 'Onluqları toplayırıq: 3 onluq + 2 onluq = 5 onluq. 30 + 20 = 50.',
      vstack([two_rows(tens_ones(3, 0, 80), tens_ones(2, 0, 80)), expr2(['30', '+', '20', '=', '50'], 60)], 16))
t.num('Dəstələri say və cəmi tap. Bir dəstədə 10 çöp var.', [60], vstack([two_rows(tens_ones(2, 0, 76), tens_ones(4, 0, 76)), expr2(['20', '+', '40', '=', BOX], 64)], 16))
t.num('Hər qutuda 10 yumurta var. Cəmi neçə yumurta var?', [50], vstack([two_rows(cartons(3), cartons(2)), expr2(['30', '+', '20', '=', BOX], 64)], 16))
t.num('Ədəd oxunda on-on irəli get. Cəmi yaz.', [80], vstack([numline_step(0, 100, 10, 60, start=30, hops=5), expr2(['30', '+', '50', '=', BOX], 60)], 14))
for a, b in [(40, 30), (60, 20)]:
    t.num('Cəmi tap.', [a + b], expr2([str(a), '+', str(b), '=', BOX], 80))
t.num('Əvvəlcə onluqları topla, sonra təkliyi əlavə et.', [70, 76], stacked([['26', '+', '50', '=', '?'], ['20', '+', '50', '=', BOX], ['70', '+', '6', '=', BOX]]), disp='70, 76')
t.num('Cəmi tap.', [77], expr2(['37', '+', '40', '=', BOX], 80))
t.num('Alt-alta topla.', [75], vcol(45, 30))
t.num('Elxan 30, Səbinə 26 bayraq hazırladı. Onlar cəmi neçə bayraq hazırladılar?', [56], hstack([label(em('🚩', 90), '30', 36, INK), label(em('🚩', 90), '26', 36, INK), expr2(['30', '+', '26', '=', BOX], 56)], 20))
t.num('Aynur 70 bal topladı. Lalə ondan 20 bal çox topladı. Lalə neçə bal topladı?', [90], hstack([em('🏅', 100), expr2(['70', '+', '20', '=', BOX], 60)], 24))

# ============================================================ 54
t = T(54, 'İkirəqəmli ədədlərin toplanması', 'Təklikləri təkliklərə, onluqları onluqlara əlavə edirik: 46 + 21 = 67.',
      vstack([two_rows(tens_ones(4, 6, 76), tens_ones(2, 1, 76)), expr2(['46', '+', '21', '=', '67'], 60)], 16))
t.num('Çöpləri say və cəmi tap.', [56], vstack([two_rows(tens_ones(3, 2, 76), tens_ones(2, 4, 76)), expr2(['32', '+', '24', '=', BOX], 64)], 16))
t.num('Ədədləri onluq və təkliklərə ayır. Boş xanaları doldur.', [7, 60, 67], stacked([['46', '+', '21', '=', '?'], ['6', '+', '1', '=', BOX], ['40', '+', '20', '=', BOX], ['60', '+', '7', '=', BOX]], 54), disp='7, 60, 67')
for a, b in [(34, 45), (62, 36), (23, 51), (15, 42)]:
    t.num('Cəmi tap.', [a + b], expr2([str(a), '+', str(b), '=', BOX], 80))
t.num('Alt-alta topla.', [77], vcol(53, 24))
t.num('Bir səbətdə 33 kq, o birində 26 kq alma var. Cəmi neçə kiloqram alma var?', [59], hstack([label(em('🧺', 100), '33 kq', 32, INK), label(em('🧺', 100), '26 kq', 32, INK), expr2(['33', '+', '26', '=', BOX], 54)], 18), disp='59 kq')
t.num('Dayanacaqda 21 maşın var idi. Daha 18 maşın gəldi. Dayanacaqda neçə maşın oldu?', [39], hstack([em('🚗', 100), expr2(['21', '+', '18', '=', BOX], 60)], 24))
t.choice('Cəmi 68 olan ifadəni dairəyə al.', ['42 + 25', '35 + 33', '51 + 16'], 1)

# ============================================================ 55
t = T(55, 'İkirəqəmli ədədlə birrəqəmli ədədin fərqi', 'Təklikdən təklik çıxırıq, onluqlar dəyişmir: 46 − 3 = 43.',
      vstack([sticks_crossed(4, 6, 3, 100), expr2(['46', '−', '3', '=', '43'], 60)], 16))
t.num('Şəkildə 27 çöp var. 4 çöpü götürdülər. Neçə çöp qaldı?', [23], vstack([sticks_crossed(2, 7, 4, 90), expr2(['27', '−', '4', '=', BOX], 60)], 16))
t.num('Ədəd oxunda 3 addım geri get. Fərqi yaz.', [43], vstack([numline(40, 50, 62, start=46, jumps=-3), expr2(['46', '−', '3', '=', BOX], 60)], 14))
for a, b in [(58, 5), (79, 7), (64, 4), (97, 6)]:
    t.num('Fərqi tap.', [a - b], expr2([str(a), '−', str(b), '=', BOX], 80))
t.num('Alt-alta çıx.', [83], vcol(86, 3, '−'))
t.num('Təklikdən təklik çıx. Onluqlar dəyişmir.', [3, 73], stacked([['78', '−', '5', '=', '?'], ['8', '−', '5', '=', BOX], ['70', '+', '3', '=', BOX]]), disp='3, 73')
t.num('Ağacda 37 quş var idi. 5 quş uçdu. Neçə quş qaldı?', [32], hstack([em('🐦', 100), expr2(['37', '−', '5', '=', BOX], 60)], 24))
t.num('Mağazada 49 top var idi. 6 top satıldı. Neçə top qaldı?', [43], hstack([em('⚽', 100), expr2(['49', '−', '6', '=', BOX], 60)], 24))

# ============================================================ 56
t = T(56, 'Onluqların çıxılması', 'Onluqdan onluq çıxırıq: 7 onluq − 3 onluq = 4 onluq. 70 − 30 = 40.',
      vstack([bundles_crossed(7, 3, 80, 4), expr2(['70', '−', '30', '=', '40'], 60)], 16))
t.num('5 dəstədən 2 dəstəni götürdülər. Neçə çöp qaldı?', [30], vstack([bundles_crossed(5, 2, 80, 3), expr2(['50', '−', '20', '=', BOX], 64)], 16))
t.num('Ədəd oxunda on-on geri get. Fərqi yaz.', [50], vstack([numline_step(0, 100, 10, 60, start=80, hops=-3), expr2(['80', '−', '30', '=', BOX], 60)], 14))
for a, b in [(60, 10), (90, 40), (70, 50)]:
    t.num('Fərqi tap.', [a - b], expr2([str(a), '−', str(b), '=', BOX], 80))
t.num('Əvvəlcə onluqları çıx, sonra təkliyi əlavə et.', [30, 37], stacked([['57', '−', '20', '=', '?'], ['50', '−', '20', '=', BOX], ['30', '+', '7', '=', BOX]]), disp='30, 37')
t.num('Fərqi tap.', [56], expr2(['86', '−', '30', '=', BOX], 80))
t.num('Alt-alta çıx.', [34], vcol(94, 60, '−'))
t.num('Qutuda 80 karandaş var idi. 30 karandaşı payladılar. Neçə karandaş qaldı?', [50], hstack([em('✏️', 100), expr2(['80', '−', '30', '=', BOX], 60)], 24))
t.num('Məchul çıxılanı tap.', [30], expr2(['90', '−', BOX, '=', '60'], 80))

# ============================================================ 57
t = T(57, 'İkirəqəmli ədədlərin fərqi', 'Təklikdən təklik, onluqdan onluq çıxırıq: 68 − 25 = 43.',
      vstack([bundles_crossed(6, 2, 70, 3), sticks_crossed(0, 8, 5, 70), expr2(['68', '−', '25', '=', '43'], 60)], 12))
t.num('Şəkildə 57 çöp var. 23 çöpü götürdülər. Neçə çöp qaldı?', [34], vstack([bundles_crossed(5, 2, 70, 3), sticks_crossed(0, 7, 3, 70), expr2(['57', '−', '23', '=', BOX], 64)], 12))
t.num('Ədədləri onluq və təkliklərə ayır. Boş xanaları doldur.', [3, 40, 43], stacked([['68', '−', '25', '=', '?'], ['8', '−', '5', '=', BOX], ['60', '−', '20', '=', BOX], ['40', '+', '3', '=', BOX]], 54), disp='3, 40, 43')
for a, b in [(79, 34), (86, 52), (95, 41), (67, 23)]:
    t.num('Fərqi tap.', [a - b], expr2([str(a), '−', str(b), '=', BOX], 80))
t.num('Alt-alta çıx.', [43], vcol(88, 45, '−'))
t.num('Kitabda 48 səhifə var. Aynur 25 səhifəni oxudu. Neçə səhifə qaldı?', [23], hstack([em('📖', 100), expr2(['48', '−', '25', '=', BOX], 60)], 24))
t.num('Bağda 76 gül var idi. 34 gülü dərdilər. Neçə gül qaldı?', [42], hstack([em('🌹', 100), expr2(['76', '−', '34', '=', BOX], 60)], 24))
t.num('Toplamaya bax və fərqi tap.', [43], vstack([expr2(['43', '+', '25', '=', '68'], 60), expr2(['68', '−', '25', '=', BOX], 60)], 16))

# ============================================================ 58
t = T(58, 'Təkrar toplama', 'Bərabər qrupları toplayırıq: 3 + 3 + 3 + 3 = 12. Hər qrupda 3 alma, 4 qrup var.',
      vstack([groups('🍎', (3, 3, 3, 3), 46), expr2(['3', '+', '3', '+', '3', '+', '3', '=', '12'], 54)], 16))
t.num('Qrupları topla.', [6], vstack([groups('🍐', (2, 2, 2), 56), expr2(['2', '+', '2', '+', '2', '=', BOX], 60)], 16))
t.num('Qrupları topla.', [20], vstack([groups('🌸', (5, 5, 5, 5), 40), expr2(['5', '+', '5', '+', '5', '+', '5', '=', BOX], 56)], 16))
t.num('Neçə qrup var? Hər qrupda neçə çiyələk var?', [3, 4], vstack([groups('🍓', (4, 4, 4), 50), hstack([box(), txt('qrup', 40, BLUE), box(), txt('hər qrupda', 40, BLUE)], 14)], 18), disp='3 qrup, hər qrupda 4')
t.num('Ədəd oxunda üç-üç irəli get. Cəmi yaz.', [9], vstack([numline_step(0, 12, 1, 54, start=0, hops=3, hop=3), expr2(['3', '+', '3', '+', '3', '=', BOX], 60)], 14))
t.num('Corabları cüt-cüt say: iki-iki. Cəmi neçə corab var?', [10], vstack([groups('🧦', (2, 2, 2, 2, 2), 64, 2, 16), expr2(['2', '+', '2', '+', '2', '+', '2', '+', '2', '=', BOX], 56)], 16))
t.num('Hər üçbucağın 3 təpəsi var. 5 üçbucağın neçə təpəsi var?', [15], vstack([hstack([shape('triangle', 80, Y3) for _ in range(5)], 16), expr2(['3', '+', '3', '+', '3', '+', '3', '+', '3', '=', BOX], 50)], 16))
t.num('Cəmi tap.', [30], expr2(['10', '+', '10', '+', '10', '=', BOX], 72))
t.choice('Hansı şəkildə qruplar bərabərdir? Dairəyə al.', [groups('🍋', (3, 3, 3), 36, 3, 10), groups('🍋', (3, 2, 4), 36, 3, 10), groups('🍋', (2, 3, 3), 36, 3, 10)], 0, disp='1-ci şəkil (3, 3, 3)')
t.num('Hər maşının 4 təkəri var. 3 maşının neçə təkəri var?', [12], vstack([hstack([label(em('🚗', 100), '4', 36, INK) for _ in range(3)], 24), expr2(['4', '+', '4', '+', '4', '=', BOX], 60)], 16))
t.num('Cəmi tap.', [25], expr2(['5', '+', '5', '+', '5', '+', '5', '+', '5', '=', BOX], 60))

# ============================================================ 59
t = T(59, 'Vurma', 'Bərabər qrupları vurma ilə yazırıq: 3 + 3 + 3 + 3 = 3 · 4 = 12. Hər qrupda 3, cəmi 4 qrup.',
      vstack([groups('🍎', (3, 3, 3, 3), 46), expr2(['3', '+', '3', '+', '3', '+', '3', '=', '3', '·', '4', '=', '12'], 48)], 16))
t.num('Təkrar toplamanı vurma ilə yaz.', [2, 10], vstack([groups('🍬', (5, 5), 50), expr2(['5', '+', '5', '=', '5', '·', BOX, '=', BOX], 58)], 16), disp='5 · 2 = 10')
t.num('Ulduzları say. Hasili tap.', [12], vstack([array('⭐', 3, 4, 50), expr2(['4', '+', '4', '+', '4', '=', '4', '·', '3', '=', BOX], 50)], 16))
t.num('Hasili tap.', [8], vstack([groups('🍒', (2, 2, 2, 2), 48), expr2(['2', '·', '4', '=', BOX], 70)], 16))
t.num('Hasili tap.', [10], vstack([hstack([em('🖐️', 100), em('🖐️', 100)], 30), expr2(['5', '·', '2', '=', BOX], 70)], 16))
t.num('Hasili tap.', [9], vstack([groups('🐞', (3, 3, 3), 50), expr2(['3', '·', '3', '=', BOX], 70)], 16))
t.num('Vurma ilə yaz və hasili tap.', [5, 10], vstack([groups('🍪', (2, 2, 2, 2, 2), 50, 2, 14), expr2(['2', '+', '2', '+', '2', '+', '2', '+', '2'], 56), expr2(['=', '2', '·', BOX, '=', BOX], 64)], 14), disp='2 · 5 = 10')
t.num('Ədəd oxunda dörd-dörd irəli get. Hasili yaz.', [16], vstack([numline_step(0, 16, 1, 52, start=0, hops=4, hop=4, size=26), expr2(['4', '·', '4', '=', BOX], 64)], 14))
t.choice('Hər qrupda 3 əşya olan 2 qrupu dairəyə al.', [groups('🍊', (3, 3), 40, 3, 10), groups('🍊', (2, 2, 2), 40, 3, 10), groups('🍊', (3, 3, 3), 40, 3, 10)], 0, stem=expr2(['3', '·', '2'], 64), disp='1-ci şəkil')
t.num('Bir velosipedin 2 təkəri var. 4 velosipedin neçə təkəri var?', [8], vstack([hstack([label(em('🚲', 90), '2', 34, INK) for _ in range(4)], 18), expr2(['2', '·', '4', '=', BOX], 64)], 16))
t.num('Bir qutuda 5 qələm var. 3 qutuda neçə qələm var?', [15], vstack([groups('✏️', (5, 5, 5), 40), expr2(['5', '·', '3', '=', BOX], 64)], 16))

# ============================================================ 60
t = T(60, 'Bərabər paylama. Bölmə', '12 konfeti 3 uşağa bərabər paylayırıq. Hər uşağa 4 konfet düşür: 12 : 3 = 4.',
      vstack([plates('🍬', (4, 4, 4), 44), expr2(['12', ':', '3', '=', '4'], 60)], 16))
t.choice('Konfetlər hansı şəkildə bərabər paylanıb? Dairəyə al.', [plates('🍬', (2, 2, 2), 34), plates('🍬', (3, 1, 2), 34), plates('🍬', (2, 3, 2), 34)], 0, disp='1-ci şəkil')
t.num('8 almanı 2 boşqaba bərabər payla. Hər boşqaba neçə alma düşər?', [4], vstack([frame(row('🍎', 8, 50, 6, 8), 12), plates('🍎', (0, 0), 40), expr2(['8', ':', '2', '=', BOX], 64)], 14))
t.num('9 topu 3 uşağa bərabər payla. Hər uşağa neçə top düşər?', [3], vstack([frame(row('⚽', 9, 46, 6, 9), 12), hstack([em('👦', 70), em('👧', 70), em('🧒', 70)], 40), expr2(['9', ':', '3', '=', BOX], 64)], 14))
t.num('10 karandaşı 5 qutuya bərabər payla. Hər qutuya neçə karandaş düşər?', [2], vstack([frame(row('✏️', 10, 44, 6, 10), 12), expr2(['10', ':', '5', '=', BOX], 64)], 14))
t.num('Şəkilə bax və bölməni tamamla.', [3], vstack([plates('🍪', (3, 3, 3, 3), 38), expr2(['12', ':', '4', '=', BOX], 64)], 14))
t.num('Şəkilə bax və bölməni tamamla.', [3], vstack([plates('🍓', (3, 3), 44), expr2(['6', ':', '2', '=', BOX], 64)], 14))
t.num('Şəkilə bax və bölməni tamamla.', [5], vstack([plates('🍇', (5, 5, 5), 38), expr2(['15', ':', '3', '=', BOX], 64)], 14))
t.num('20 balığı 4 akvariuma bərabər payla. Hər akvariumda neçə balıq olar?', [5], vstack([groups('🐟', (5, 5, 5, 5), 34), expr2(['20', ':', '4', '=', BOX], 64)], 14))
t.num('16 qələmi 2 qutuya bərabər payla. Hər qutuya neçə qələm düşər?', [8], vstack([frame(row('🖊️', 16, 38, 4, 8), 12), expr2(['16', ':', '2', '=', BOX], 64)], 14))
t.choice('6 uşaq 2 komandaya bərabər bölündü. Hər komandada neçə uşaq var?', ['2', '3', '4'], 1, stem=frame(row('🧒', 6, 60, 8, 6), 12))

# ============================================================ 61
t = T(61, 'Təkrar çıxma', 'Hər dəfə 2 çıxırıq: 8 − 2 − 2 − 2 − 2 = 0. Dörd dəfə çıxdıq: 8 : 2 = 4.',
      vstack([numline_step(0, 8, 1, 60, start=8, hops=-4, hop=2), expr2(['8', ':', '2', '=', '4'], 60)], 12))
t.num('6 ananası 2-2 qruplara böl. Neçə qrup alınar?', [3], hstack([groups('🍍', (2, 2, 2), 54), arrow(), box()], 20))
t.num('9 heyvanı 3-3 qruplara böl. Neçə qrup alınar?', [3], hstack([hstack([frame(row('🐑', 3, 46, 6), 10), frame(row('🐐', 3, 46, 6), 10), frame(row('🐄', 3, 46, 6), 10)], 16), arrow(), box()], 20))
t.num('12-dən dörd-dörd çıx. Neçə dəfə çıxdın? Bölməni tamamla.', [3], vstack([numline_step(0, 12, 1, 54, start=12, hops=-3, hop=4), expr2(['12', ':', '4', '=', BOX], 64)], 12))
t.num('16-dan dörd-dörd çıx. Bölməni tamamla.', [4], vstack([numline_step(0, 16, 1, 44, start=16, hops=-4, hop=4, size=24), expr2(['16', ':', '4', '=', BOX], 64)], 12))
t.num('18-dən üç-üç çıx. Bölməni tamamla.', [6], vstack([numline_step(0, 18, 1, 40, start=18, hops=-6, hop=3, size=22), expr2(['18', ':', '3', '=', BOX], 64)], 12))
t.num('Təkrar çıxmaya bax. Bölməni tamamla.', [2], vstack([expr2(['10', '−', '5', '−', '5', '=', '0'], 60), expr2(['10', ':', '5', '=', BOX], 64)], 14))
t.num('Corabları cüt-cüt yığ. Neçə cüt alınar?', [4], vstack([groups('🧦', (2, 2, 2, 2), 50), expr2(['8', ':', '2', '=', BOX], 64)], 14))
t.num('20 manatı 5 manatlıqlarla düzəlt. Neçə əskinas lazımdır?', [4], vstack([hstack([note(5, 150, 80) for _ in range(4)], 12), expr2(['20', ':', '5', '=', BOX], 64)], 14))
t.num('Barmaqları beş-beş say. Bölməni tamamla.', [3], vstack([hstack([em('🖐️', 90) for _ in range(3)], 20), expr2(['15', ':', '5', '=', BOX], 64)], 14))
t.choice('Hansı təkrar çıxma 12 : 3 bölməsini göstərir? Dairəyə al.', ['12 − 3 − 3 − 3 − 3 = 0', '12 − 4 − 4 − 4 = 0', '12 − 2 − 2 = 8'], 0)

# ============================================================ 62
t = T(62, 'Tək və cüt ədədlər', 'Cüt ədədlərin hamısı ikilərə bölünür: 2, 4, 6, 8. Tək ədədlərdə biri cütsüz qalır: 1, 3, 5, 7.',
      hstack([label(frame(row('🧦', 6, 46, 6, 2), 10), 'cüt – 6', 32), label(frame(row('🧦', 5, 46, 6, 2), 10), 'tək – 5', 32)], 50, 'bottom'))
t.choice('Cüt sayda ulduz olan qrupu dairəyə al.', [frame(row('⭐', 5, 36, 4, 2), 8), frame(row('⭐', 6, 36, 4, 2), 8), frame(row('⭐', 7, 36, 4, 2), 8)], 1, disp='6 ulduz')
t.choice('Tək sayda dairə olan qrupu dairəyə al.', [frame(grid([shape('circle', 34, B3) for _ in range(4)], 2, 6), 8), frame(grid([shape('circle', 34, B3) for _ in range(8)], 2, 6), 8), frame(grid([shape('circle', 34, B3) for _ in range(9)], 2, 6), 8)], 2, disp='9 dairə')
t.choice('Bütün cüt ədədləri dairəyə al.', ['12', '7', '18', '25', '30', '9'], [0, 2, 4], mode='multi', disp='12, 18, 30')
t.choice('Bütün tək ədədləri dairəyə al.', ['31', '44', '57', '60', '73'], [0, 2, 4], mode='multi', disp='31, 57, 73')
t.num('Cüt ədədləri davam etdir.', [8, 10], seq([2, 4, 6, BOX, BOX]), disp='8, 10')
t.num('Tək ədədləri davam etdir.', [7, 9], seq([1, 3, 5, BOX, BOX]), disp='7, 9')
t.num('Corabları cüt-cüt düz. Neçə cüt alınar?', [4], hstack([frame(row('🧦', 8, 50, 6, 4), 12), arrow(), box()], 20))
t.choice('15 tək ədəddir, yoxsa cüt?', ['tək', 'cüt'], 0, stem=frame(row('🍬', 15, 40, 4, 5), 10))
t.choice('24 tək ədəddir, yoxsa cüt?', ['tək', 'cüt'], 1, stem=chip('24', 64))
t.num('36-nın qonşu cüt ədədlərini yaz.', [34, 38], seq([BOX, 36, BOX], 70), disp='34 və 38')

# ============================================================ 63
t = T(63, 'Xətt, bucaq', 'Xətlər düz və əyri olur. İki düz xətt bir nöqtədən çıxanda bucaq əmələ gəlir. Bucaqlar: düz, iti, kor.',
      vstack([hstack([label(line_img('straight', 180, 100), 'düz xətt', 28), label(line_img('curve', 180, 100), 'əyri xətt', 28)], 40, 'bottom'),
              hstack([label(angle_img(90, 150), 'düz bucaq', 28), label(angle_img(50, 150), 'iti bucaq', 28), label(angle_img(130, 150), 'kor bucaq', 28)], 30, 'bottom')], 20))
t.choice('Əyri xətti dairəyə al.', [line_img('straight'), line_img('curve'), line_img('broken')], 1, disp='əyri xətt')
t.choice('Düz xətti dairəyə al.', [line_img('wave'), line_img('arc'), line_img('straight')], 2, disp='düz xətt')
t.choice('Bütün əyri xətləri dairəyə al.', [line_img('curve', 170, 90), line_img('straight', 170, 90), line_img('wave', 170, 90), line_img('broken', 170, 90), line_img('arc', 170, 90)], [0, 2, 4], mode='multi', disp='1-ci, 3-cü, 5-ci')
t.choice('Hansı şəkildə bucaq var? Dairəyə al.', [line_img('parallel'), angle_img(60, 140, mark=False), line_img('curve')], 1, disp='2-ci şəkil')
t.choice('Düz bucağı dairəyə al.', [angle_img(45, 150), angle_img(90, 150), angle_img(135, 150)], 1, disp='düz bucaq')
t.choice('İti bucağı dairəyə al.', [angle_img(90, 150), angle_img(140, 150), angle_img(40, 150)], 2, disp='iti bucaq')
t.choice('Kor bucağı dairəyə al.', [angle_img(125, 150), angle_img(55, 150), angle_img(90, 150)], 0, disp='kor bucaq')
t.num('Şəkildə neçə bucaq var? Say və yaz.', [3], hstack([frame(grid([angle_img(70, 110, mark=False), line_img('curve', 140, 80), angle_img(90, 110, mark=False), angle_img(130, 110, mark=False), line_img('wave', 140, 80)], 3, 16), 14), arrow(), box()], 20))
t.num('Üçbucağın neçə bucağı var?', [3], hstack([shape('triangle', 180, Y3), arrow(), box()], 24))
t.num('Kvadratın neçə düz bucağı var?', [4], hstack([corners('square', 170), arrow(), box()], 24))

# ============================================================ 64
t = T(64, 'Çoxbucaqlı', 'Çoxbucaqlının neçə bucağı varsa, o qədər də tərəfi var: üçbucaq, dördbucaqlı, beşbucaqlı, altıbucaqlı.',
      hstack([label(poly(3, 100, R3), 'üçbucaq', 26), label(shape('square', 90, Y3), 'dördbucaqlı', 26), label(poly(5, 100, G3), 'beşbucaqlı', 26), label(poly(6, 100, B3), 'altıbucaqlı', 26)], 26, 'bottom'))
t.num('Fiqurun neçə bucağı var? Say və yaz.', [5], hstack([poly(5, 180, G3), arrow(), box()], 24))
t.num('Fiqurun neçə bucağı var? Say və yaz.', [6], hstack([poly(6, 180, B3), arrow(), box()], 24))
t.choice('Beşbucaqlını dairəyə al.', [shape('square', 100, O3), poly(5, 110, O3), poly(6, 110, O3)], 1, disp='beşbucaqlı')
t.choice('Altıbucaqlını dairəyə al.', [poly(6, 110, P3), poly(3, 110, P3), poly(5, 110, P3)], 0, disp='altıbucaqlı')
t.choice('Dördbucaqlı olmayan fiquru dairəyə al.', [shape('square', 90, B3), shape('rect', 70, B3), poly(5, 100, B3), rhombus(90, B3)], 2, disp='beşbucaqlı')
t.choice('Bütün dördbucaqlıları dairəyə al.', [shape('square', 80, G3), poly(3, 90, G3), shape('rect', 60, G3), poly(6, 90, G3), rhombus(80, G3)], [0, 2, 4], mode='multi', disp='kvadrat, düzbucaqlı, romb')
t.num('Neçə üçbucaq var? Say və yaz.', [3], hstack([frame(grid([poly(3, 70, R3), poly(5, 70, G3), shape('square', 64, Y3), poly(3, 70, B3), poly(6, 70, P3), poly(3, 70, O3)], 3, 16), 14), arrow(), box()], 20))
t.choice('Rombu dairəyə al.', [shape('rect', 70, Y3), rhombus(90, Y3), shape('square', 90, Y3)], 1, disp='romb')
t.num('Evin şəklində neçə üçbucaq və neçə dördbucaqlı var?', [1, 4], hstack([house(230), vstack([hstack([poly(3, 50, R3), box(80, 80)], 12), hstack([shape('square', 46, Y3), box(80, 80)], 12)], 14, 'left')], 40), disp='1 üçbucaq, 4 dördbucaqlı')
t.num('Hər üçbucağın 3 bucağı var. 3 üçbucağın cəmi neçə bucağı var?', [9], vstack([hstack([poly(3, 90, c) for c in (R3, G3, B3)], 20), expr2(['3', '+', '3', '+', '3', '=', BOX], 60)], 16))

# ============================================================ 65
t = T(65, 'Üz, til və təpə', 'Kubun 6 üzü, 12 tili və 8 təpəsi var. Təpələr – qırmızı nöqtələr, tillər – xətlər, üzlər – kvadratlar.',
      hstack([cube_marked(190), vstack([txt('6 üz', 44, BLUE), txt('12 til', 44, INK), txt('8 təpə', 44, RED)], 12, 'left')], 40))
t.num('Kubun neçə üzü var?', [6], hstack([cube_marked(180, dots=False), arrow(), box()], 24))
t.num('Qırmızı nöqtələri say. Kubun neçə təpəsi var?', [8], hstack([cube_marked(180), arrow(), box()], 24))
t.num('Xətləri say. Kubun neçə tili var?', [12], hstack([cube_marked(180, dots=False), arrow(), box()], 24))
t.choice('Müstəvi fiquru dairəyə al.', [solid('cube', 100, B3), shape('square', 100, B3), solid('sphere', 100, B3)], 1, disp='kvadrat')
t.choice('Fəza fiqurunu dairəyə al.', [shape('triangle', 100, O3), shape('circle', 100, O3), solid('cylinder', 100, O3)], 2, disp='silindr')
t.num('Piramidanın neçə təpəsi var?', [5], hstack([pyramid(180), arrow(), box()], 24))
t.num('Piramidanın neçə üzü var? Altını da say.', [5], hstack([pyramid(180, (129, 199, 132)), arrow(), box()], 24))
t.choice('Kürənin təpəsi varmı?', ['var', 'yoxdur'], 1, stem=solid('sphere', 140, G3))
t.num('Neçə kub var? Say və yaz.', [3], hstack([frame(grid([solid('cube', 70, B3), solid('sphere', 70, G3), solid('cube', 70, R3), pyramid(70), solid('cylinder', 70, O3), solid('cube', 70, Y3)], 3, 20), 14), arrow(), box()], 20))
t.choice('Təpəsi olan bütün fiqurları dairəyə al.', [solid('cube', 90, B3), solid('sphere', 90, G3), solid('cone', 90, P3), solid('cylinder', 90, O3), pyramid(90)], [0, 2, 4], mode='multi', disp='kub, konus, piramida')

# ============================================================ 66
C_ = {'r': R3, 'b': B3, 'y': Y3, 'g': G3}


def shp(k, c, s=70):
    return shape(k, s, C_[c]) if k != 'rect' else shape(k, int(s * 0.7), C_[c])


t = T(66, 'Qruplaşdırma', 'Əşyaları əlamətinə görə qruplaşdırırıq: rənginə, formasına və ölçüsünə görə.',
      hstack([label(frame(grid([shp('circle', 'r', 56), shp('square', 'r', 56), shp('triangle', 'r', 56)], 3, 12), 12), 'qırmızılar', 28, RED),
              label(frame(grid([shp('circle', 'b', 56), shp('circle', 'y', 56), shp('circle', 'g', 56)], 3, 12), 12), 'dairələr', 28)], 40, 'bottom'))
t.choice('Bütün qırmızı fiqurları seç.', [shp('circle', 'r'), shp('square', 'b'), shp('triangle', 'r'), shp('circle', 'y'), shp('square', 'r')], [0, 2, 4], mode='multi', disp='3 qırmızı fiqur')
t.choice('Bütün üçbucaqları seç.', [shp('triangle', 'g'), shp('circle', 'g'), shp('triangle', 'b'), shp('square', 'y'), shp('triangle', 'y')], [0, 2, 4], mode='multi', disp='3 üçbucaq')
t.choice('Artıq olanı dairəyə al.', [em('🍎', 100), em('🍐', 100), em('🍌', 100), em('🚗', 100)], 3, disp='maşın')
t.choice('Artıq olan fiquru dairəyə al.', [shp('triangle', 'b', 90), shp('triangle', 'b', 90), shp('square', 'b', 90), shp('triangle', 'b', 90)], 2, disp='kvadrat')
MIX = [('circle', 'b'), ('square', 'y'), ('circle', 'r'), ('triangle', 'g'), ('circle', 'y'), ('square', 'b'), ('circle', 'g'), ('square', 'r'), ('triangle', 'y')]
mix = frame(grid([shp(k, c, 62) for k, c in MIX], 3, 16), 14)
t.num('Formasına görə qrupla. Neçə dairə və neçə kvadrat var?', [4, 3], hstack([mix, vstack([hstack([shp('circle', 'g', 44), box(80, 80)], 12), hstack([shp('square', 'g', 44), box(80, 80)], 12)], 14, 'left')], 30), disp='4 dairə, 3 kvadrat')
t.num('Rənginə görə qrupla. Neçə sarı və neçə göy fiqur var?', [3, 2], hstack([mix, vstack([hstack([shp('circle', 'y', 44), box(80, 80)], 12), hstack([shp('circle', 'b', 44), box(80, 80)], 12)], 14, 'left')], 30), disp='3 sarı, 2 göy')
vn = venn([shp('square', 'r', 50), shp('triangle', 'r', 50), shp('square', 'r', 50)], [shp('circle', 'b', 50), shp('circle', 'y', 50)], [shp('circle', 'r', 50), shp('circle', 'r', 50)], labels=('qırmızı', 'dairə'))
t.num('Ortada həm qırmızı, həm də dairə olan fiqurlar var. Ortada neçə fiqur var?', [2], hstack([vn, arrow(), box()], 16))
t.num('Neçə fiqur yalnız qırmızıdır, dairə deyil?', [3], hstack([vn, arrow(), box()], 16))
t.choice('Bu qrupa hansı uyğundur? Dairəyə al.', [em('🍇', 100), em('⚽', 100), em('🚲', 100)], 0, stem=frame(row('🍓', 1, 70) if False else hstack([em('🍓', 70), em('🍊', 70), em('🍉', 70)], 14), 12), disp='üzüm')
t.choice('Böyük fiqurlar qrupuna hansı uyğundur? Dairəyə al.', [shp('circle', 'g', 40), shp('triangle', 'g', 110), shp('square', 'g', 40)], 1, stem=frame(hstack([shp('square', 'b', 110), shp('circle', 'r', 110)], 16), 12), disp='böyük üçbucaq')

# ============================================================ 67
t = T(67, 'İkirəqəmli ədədlə birrəqəmli ədədin toplanması', '10 təklik 1 onluq edir. Əvvəlcə onluğa tamamlayırıq: 47 + 5 = 47 + 3 + 2 = 50 + 2 = 52.',
      vstack([hstack([dots_frame(7, 3), dots_frame(0, 2)], 24), expr2(['47', '+', '5', '=', '47', '+', '3', '+', '2', '=', '52'], 46)], 16))
t.num('Neçə onluq və neçə təklik var?', [1, 3], vstack([hstack([dots_frame(10), dots_frame(3)], 24), hstack([txt('13 təklik =', 44, INK), box(), txt('onluq', 38, BLUE), box(), txt('təklik', 38, BLUE)], 12)], 18), disp='1 onluq, 3 təklik')
t.num('Təklikləri topla. Cəmi onluq və təkliyə ayır.', [15, 1, 5], vstack([expr2(['7', '+', '8', '=', BOX], 60), hstack([box(), txt('onluq', 38, BLUE), box(), txt('təklik', 38, BLUE)], 12)], 18), disp='15 = 1 onluq, 5 təklik')
t.num('Əvvəlcə 40-a tamamla, sonra topla.', [42], vstack([two_rows(tens_ones(3, 8, 70), tens_ones(0, 4, 70)), vstack([expr2(['38', '+', '4'], 58), expr2(['=', '38', '+', '2', '+', '2', '=', BOX], 58)], 10, 'left')], 16))
t.num('Əvvəlcə 60-a tamamla, sonra topla.', [63], vstack([expr2(['57', '+', '6'], 66), expr2(['=', '57', '+', '3', '+', '3', '=', BOX], 66)], 12, 'left'))
for a, b in [(29, 5), (46, 8), (68, 7), (85, 9)]:
    t.num('Cəmi tap.', [a + b], expr2([str(a), '+', str(b), '=', BOX], 80))
t.num('Alt-alta topla.', [43], vcol(36, 7))
t.num('Samir 41 almanı səbətə yığdı, 9 alma yerdə qaldı. Samir neçə alma dərmişdi?', [50], hstack([label(em('🧺', 100), '41', 36, INK), label(row('🍎', 3, 50, 6), '9', 36, INK), expr2(['41', '+', '9', '=', BOX], 56)], 20))

# ============================================================ 68
t = T(68, 'İkirəqəmli ədədlərin toplanması', 'Təklikləri toplayırıq: 9 + 3 = 12, yəni 1 onluq 2 təklik. Onluğu onluqlara əlavə edirik: 29 + 53 = 82.',
      vstack([two_rows(tens_ones(2, 9, 70), tens_ones(5, 3, 70)), expr2(['29', '+', '53', '=', '82'], 60)], 16))
t.num('Çöpləri say və cəmi tap.', [82], vstack([two_rows(tens_ones(2, 9, 70), tens_ones(5, 3, 70)), expr2(['29', '+', '53', '=', BOX], 64)], 16))
t.num('Təklikləri, sonra onluqları topla. Boş xanaları doldur.', [12, 60, 72], stacked([['47', '+', '25', '=', '?'], ['7', '+', '5', '=', BOX], ['40', '+', '20', '=', BOX], ['60', '+', '12', '=', BOX]], 54), disp='12, 60, 72')
for a, b in [(36, 48), (59, 23), (27, 45), (64, 19)]:
    t.num('Cəmi tap.', [a + b], expr2([str(a), '+', str(b), '=', BOX], 80))
t.num('Alt-alta topla.', [85], vcol(38, 47))
t.num('Alt-alta topla.', [84], vcol(49, 35))
t.num('Birinci gün 28, ikinci gün 35 ağac əkdilər. Cəmi neçə ağac əkdilər?', [63], hstack([em('🌳', 100), expr2(['28', '+', '35', '=', BOX], 60)], 24))
t.num('Lalənin 45, Aynurun 37 stikeri var. Onların cəmi neçə stikeri var?', [82], hstack([em('⭐', 90), expr2(['45', '+', '37', '=', BOX], 60)], 24))

# ============================================================ 69
t = T(69, 'Üç toplananlı ifadələr', 'Üç ədədi toplayanda əvvəlcə tam onluq düzəldən ədədləri toplayırıq: 26 + 15 + 4 = 30 + 15 = 45.',
      vstack([expr2(['26', '+', '15', '+', '4', '=', '45'], 60), expr2(['26', '+', '4', '=', '30'], 46), expr2(['30', '+', '15', '=', '45'], 46)], 12))
t.num('Asan yolla topla: əvvəlcə 10 düzəlt.', [18], vstack([hstack([dots_frame(7, 3), dots_frame(0, 8)], 20), expr2(['7', '+', '8', '+', '3', '=', BOX], 64)], 16))
t.num('Asan yolla topla: əvvəlcə 25 + 5.', [39], expr2(['25', '+', '9', '+', '5', '=', BOX], 72))
t.num('Asan yolla topla: əvvəlcə 36 + 4.', [52], expr2(['36', '+', '12', '+', '4', '=', BOX], 72))
t.num('Asan yolla topla: əvvəlcə 18 + 2.', [40], expr2(['18', '+', '20', '+', '2', '=', BOX], 72))
t.num('Cəmi tap.', [60], expr2(['10', '+', '20', '+', '30', '=', BOX], 72))
t.num('Cəmi tap.', [69], expr2(['13', '+', '24', '+', '32', '=', BOX], 72))
t.num('Sikkələri topla. Cəmi neçə qəpikdir?', [45], hstack([coin(20), coin(20), coin(5), arrow(), box(), txt('qəp', 44, BLUE)], 16), disp='45 qəpik')
t.num('Üç səbətdə 12, 15 və 8 alma var. Cəmi neçə alma var?', [35], vstack([hstack([label(em('🧺', 90), '12', 34, INK), label(em('🧺', 90), '15', 34, INK), label(em('🧺', 90), '8', 34, INK)], 30), expr2(['12', '+', '15', '+', '8', '=', BOX], 56)], 16))
t.num('Toplananların yerini dəyiş və asan yolla topla.', [36], vstack([expr2(['7', '+', '26', '+', '3'], 66), expr2(['=', '7', '+', '3', '+', '26', '=', BOX], 66)], 12, 'left'))
t.choice('Hansı ifadənin cəmi 50-dir? Dairəyə al.', ['20 + 25 + 5', '30 + 15 + 4', '10 + 30 + 9'], 0)

# ------------------------------------------------------------------ output
for tp in TOPICS:
    if len(tp.problems) != 10: print('COUNT', tp.n, len(tp.problems))
os.makedirs(os.path.join(OUT, 'data'), exist_ok=True)
json.dump({'topics': [tp.d for tp in TOPICS]}, open(os.path.join(OUT, 'data/topics.json'), 'w'), ensure_ascii=False)
json.dump(VOICE, open(os.path.join(OUT, 'data/voice.json'), 'w'), ensure_ascii=False, indent=0)
print('topics', len(TOPICS), 'voice', len(VOICE))
