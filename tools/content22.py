"""2-ci sinif riyaziyyat, 2-ci hissə: 22 mövzu (70–91), hər mövzuda 10 tapşırıq.
Run: python3 content22.py OUTDIR [--topics 70-74]  -> OUTDIR/img/*.webp, OUTDIR/data/topics.json, OUTDIR/data/voice.json"""
import hashlib, json, os, sys
from draw import *
from draw2 import *

OUT = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith('--') else os.path.expanduser('~/riyaziyyat/2-2')
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

os.makedirs(IMG, exist_ok=True)


def triple(whole, a, b, size=64):
    """ədəd üçlüyü: yuxarıda tam, aşağıda iki hissə; None = boş xana"""
    def cell(v, w, fill):
        return frame(box(int(size * 1.4), int(size * 1.2)) if v is None else txt(str(v), size, INK), 10, ORANGE, 4, 14, fill)
    top = cell(whole, 0, (255, 236, 179))
    low = hstack([cell(a, 0, (255, 248, 225)), cell(b, 0, (255, 248, 225))], 8)
    return vstack([top, low], 6)


def word(emojis, tokens, size=58):
    """söz məsələsi: emoji şəkli + ifadə"""
    return vstack([hstack([em(e, 96) for e in emojis], 18), expr2(tokens, size)], 18)


# ============================================================ 70
t = T(70, 'İkirəqəmli ədədlə birrəqəmli ədədin fərqi',
      'Təkliklər çatmayanda azalandan 1 onluq ayırıb təkliklərə əlavə edirik: 34 − 5 = 29.',
      vstack([hstack([label(tens_ones(3, 4, 100), '3 onluq + 4 təklik', 34, INK), arrow(), label(tens_ones(2, 14, 100), '2 onluq + 14 təklik', 34, INK)], 20),
              expr2(['34', '−', '5', '=', '29'], 60)], 18))
t.num('Çöpləri sayın və fərqi tapın.', [24], vstack([tens_ones(3, 2, 110), expr2(['32', '−', '8', '=', BOX], 64)], 16))
t.num('Alt-alta çıxın.', [38], vcol(45, 7, '−'))
t.num('Alt-alta çıxın.', [48], vcol(54, 6, '−'))
for a, b in [(41, 6), (60, 7), (83, 5)]:
    t.num('Fərqi tapın.', [a - b], expr2([str(a), '−', str(b), '=', BOX], 80))
t.num('Ədəd oxunda 7 addım geri gedin. Fərqi yazın.', [36], vstack([numline(30, 45, 56, start=43, jumps=-7), expr2(['43', '−', '7', '=', BOX], 60)], 14))
t.num('Çıxılanı hissələrə ayırın və fərqi tapın: əvvəl 4, sonra 1 çıxın.', [30, 29],
      stacked([['34', '−', '5', '=', '?'], ['34', '−', '4', '=', BOX], ['30', '−', '1', '=', BOX]]), disp='30, 29')
t.num('Bilik yarışında 42 şagird iştirak edirdi. Onlardan 6-sı yarışı tərk etdi. Neçə şagird qaldı?', [36],
      word(['🧑‍🎓', '🏆'], ['42', '−', '6', '=', BOX]))
t.choice('Hansı misalın cavabı 28-dir? Dairəyə alın.', ['35 − 7', '34 − 8', '31 − 4'], 0)

# ============================================================ 71
t = T(71, 'İkirəqəmli ədədlərin fərqi',
      'Əvvəl təklikləri, sonra onluqları çıxırıq. Təkliklər çatmayanda 1 onluq ayırırıq: 43 − 25 = 18.',
      vstack([tens_ones(4, 3, 110), expr2(['43', '−', '25', '=', '18'], 64), txt('13 − 5 = 8,   3 − 2 = 1', 38, BLUE)], 16))
t.num('Çöpləri sayın və fərqi tapın.', [27], vstack([tens_ones(4, 5, 110), expr2(['45', '−', '18', '=', BOX], 64)], 16))
for a, b in [(51, 24), (70, 28), (92, 38)]:
    t.num('Alt-alta çıxın.', [a - b], vcol(a, b, '−'))
for a, b in [(82, 49), (95, 38)]:
    t.num('Fərqi tapın.', [a - b], expr2([str(a), '−', str(b), '=', BOX], 80))
t.num('Çıxılanı onluq və təkliyə ayırın və fərqi tapın.', [23, 18],
      stacked([['43', '−', '25', '=', '?'], ['43', '−', '20', '=', BOX], ['23', '−', '5', '=', BOX]]), disp='23, 18')
t.sign('Hesablayın və müqayisə edin. Dairələrə >, < və ya = yazın.', [('33 − 17', '18'), ('52 − 25', '42 − 15')], ['<', '='])
t.num('Lalənin anası 33 keks bişirdi. Onlardan 16-sı kişmişli, qalanı şokoladlı idi. Neçə şokoladlı keks var idi?', [17],
      word(['🧁', '🍫'], ['33', '−', '16', '=', BOX]))
t.num('Birinci gün Kukla Teatrına 64 şagird getdi. Bu, ikinci gündən 18 nəfər çox idi. İkinci gün neçə şagird getdi?', [46],
      word(['🎭', '🧒'], ['64', '−', '18', '=', BOX]))

# ============================================================ 72
t = T(72, 'Toplama və çıxmanın əlaqəsi',
      'Tam iki hissədən ibarətdir: 28 + 14 = 42. Tamdan bir hissəni çıxsaq, o biri hissə qalır: 42 − 28 = 14.',
      hstack([triple(42, 28, 14), vstack([expr2(['28', '+', '14', '=', '42'], 48), expr2(['42', '−', '28', '=', '14'], 48), expr2(['42', '−', '14', '=', '28'], 48)], 10, 'left')], 40))
t.num('Ədəd üçlüyünə baxın. Boş xanaları doldurun.', [23, 17],
      hstack([triple(40, 17, 23), stacked([['40', '−', '17', '=', BOX], ['40', '−', '23', '=', BOX]], 52)], 36), disp='23, 17')
t.num('Ədəd üçlüyünə baxın. Boş xanaları doldurun.', [91, 37],
      hstack([triple(91, 54, 37), stacked([['54', '+', '37', '=', BOX], ['91', '−', '54', '=', BOX]], 52)], 36), disp='91, 37')
t.num('Məchul hissəni tapın.', [28], hstack([triple(52, None, 24), expr2([BOX, '+', '24', '=', '52'], 60)], 36))
t.num('Məchul tamı tapın.', [76], hstack([triple(None, 60, 16), expr2([BOX, '−', '60', '=', '16'], 60)], 36))
t.num('Məchul hissəni tapın.', [45], hstack([triple(70, None, 25), expr2(['70', '−', BOX, '=', '25'], 60)], 36))
t.num('Məchul hissəni tapın.', [37], hstack([triple(78, 41, None), expr2(['41', '+', BOX, '=', '78'], 60)], 36))
t.num('Çıxın və cavabı toplama ilə yoxlayın.', [38, 38], stacked([['70', '−', '32', '=', BOX], [BOX, '+', '32', '=', '70']]), disp='38, 38')
t.choice('Hansı misal 62 − 9 = 53 cavabını yoxlayır? Dairəyə alın.', ['53 + 9 = 62', '62 + 9 = 71', '53 − 9 = 44'], 0)
t.num('Səbətdə bir neçə yumurta var idi. Əsmər nənə 26 yumurta da əlavə etdi və 34 yumurta oldu. Səbətdə əvvəlcə neçə yumurta var idi?', [8],
      word(['🧺', '🥚'], [BOX, '+', '26', '=', '34']))
t.num('Bilik yarışında 44 şagird iştirak etdi. Onlardan 25-i qız idi. Yarışda neçə oğlan iştirak etdi?', [19],
      word(['👧', '👦'], ['44', '−', '25', '=', BOX]))

# ============================================================ 73
t = T(73, 'Mötərizəli ifadələr',
      'Mötərizədəki əməl birinci yerinə yetirilir: 15 − (9 + 5) = 15 − 14 = 1. Mötərizə yoxdursa, soldan sağa hesablayırıq: 15 − 9 + 5 = 11.',
      vstack([expr2(['15', '−', '(', '9', '+', '5', ')', '=', '15', '−', '14', '=', '1'], 50),
              expr2(['15', '−', '9', '+', '5', '=', '6', '+', '5', '=', '11'], 50)], 22, 'left'))
for toks, v in [(['18', '−', '(', '6', '+', '4', ')'], 8), (['40', '−', '(', '10', '−', '5', ')'], 35), (['20', '+', '(', '26', '−', '6', ')'], 40), (['75', '−', '(', '25', '+', '30', ')'], 20)]:
    t.num('İfadənin qiymətini hesablayın.', [v], expr2(toks + ['=', BOX], 66))
t.num('Əvvəlcə mötərizədəki əməli yerinə yetirin.', [17, 25],
      stacked([['42', '−', '(', '12', '+', '5', ')', '=', '42', '−', BOX], ['42', '−', '17', '=', BOX]], 52), disp='17, 25')
t.num('Soldan sağa hesablayın.', [42], expr2(['32', '−', '10', '+', '20', '=', BOX], 70))
t.num('Soldan sağa hesablayın.', [10], expr2(['48', '−', '8', '−', '10', '−', '20', '=', BOX], 62))
t.choice('Qiyməti 6-ya bərabər olan ifadəni dairəyə alın.', ['9 − 5 − 3', '9 − (5 − 3)', '10 − (5 − 1)'], 2)
t.num('Parkdan evə qədər 90 addımdır. Parkdan aptekə 45, aptekdən marketə 20 addımdır. Marketdən evə neçə addımdır?', [25],
      word(['🌳', '💊', '🏪', '🏠'], ['90', '−', '(', '45', '+', '20', ')', '=', BOX], 54))
t.num('36 kitab var idi. 12 kitabı birinci rəfə, 6 kitabı ikinci rəfə qoydular. Neçə kitab qaldı?', [18],
      word(['📚'], ['36', '−', '(', '12', '+', '6', ')', '=', BOX], 58))

# ============================================================ 74
t = T(74, 'İkiaddımlı məsələlər',
      'Əvvəl birinci sualın cavabını, sonra ikincini tapırıq. 52 qutu şirə var idi, 19 və 26 qutu satıldı: 52 − 19 = 33, 33 − 26 = 7.',
      vstack([hstack([em('🧃', 90), expr2(['52', '−', '19', '=', '33'], 52)], 16), expr2(['33', '−', '26', '=', '7'], 52)], 14))
t.num('Anarın 36 stikeri var idi. O, 9 stikeri Səbinəyə, 8 stikeri Elxana bağışladı. Anarın neçə stikeri qaldı?', [19],
      word(['🦊', '🐸', '🍄'], ['36', '−', '9', '−', '8', '=', BOX]))
t.num('Parkda 35 uşaq oynayırdı. 16 uşaq evə getdi, sonra 9 uşaq da gəldi. Parkda neçə uşaq oldu?', [28],
      word(['🧒', '🛝'], ['35', '−', '16', '+', '9', '=', BOX]))
t.num('Aşpaz bir salata 14 xiyar, o birinə ondan 8 xiyar az doğradı. Əvvəl ikinci salatı, sonra cəmi tapın.', [6, 20],
      vstack([em('🥒', 90), stacked([['14', '−', '8', '=', BOX], ['14', '+', '6', '=', BOX]], 54)], 14), disp='6, 20')
t.num('Lalə 62 kubdan ev qurdu. Kubların 24-ü qırmızı, 8-i ağ, qalanı göy idi. Neçə göy kub var idi?', [30],
      word(['🧱', '🏠'], ['62', '−', '(', '24', '+', '8', ')', '=', BOX], 54))
t.num('Nənə qutabları 3 qaba qoydu, hər qabda 6 qutab var. Uşaqlar 12 qutab yedilər. Neçə qutab qaldı?', [18, 6],
      vstack([hstack([group('🥟', 6, 40, 3) for _ in range(3)], 24), stacked([['6', '+', '6', '+', '6', '=', BOX], ['18', '−', '12', '=', BOX]], 50)], 14), disp='18, 6')
t.num('Həyətdə 32 qırmızı və 18 ağ gül var idi. 7 ağ gülü dərdilər. Həyətdə neçə gül qaldı?', [43],
      word(['🌹', '🌼'], ['32', '+', '18', '−', '7', '=', BOX]))
t.num('Səbətdə 45 alma var idi. Səhər 12, axşam 15 alma götürdülər. Səbətdə neçə alma qaldı?', [18],
      word(['🧺', '🍎'], ['45', '−', '(', '12', '+', '15', ')', '=', BOX], 54))
t.num('Avtobusda 28 sərnişin var idi. Dayanacaqda 9 nəfər düşdü, 14 nəfər mindi. Avtobusda neçə sərnişin oldu?', [33],
      word(['🚌'], ['28', '−', '9', '+', '14', '=', BOX]))
t.choice('Elxanın 50 qəpiyi var idi. O, 20 qəpiyə dəftər, 15 qəpiyə karandaş aldı. Hansı ifadə bu məsələnin həllidir?',
         ['50 − (20 + 15)', '50 + 20 − 15', '20 + 15'], 0)
t.num('Elxanın 50 qəpiyi var idi. O, 20 qəpiyə dəftər, 15 qəpiyə karandaş aldı. Elxanın neçə qəpiyi qaldı?', [15],
      vstack([hstack([coin(20), coin(20), coin(10), blank(30, 10), em('📒', 80), em('✏️', 80)], 12), expr2(['50', '−', '(', '20', '+', '15', ')', '=', BOX], 54)], 16), disp='15 qəpik')


# ------------------------------------------------------------------ 8–11-ci bölmələr üçün köməkçilər
def mult_table(n=5, blanks=(), mark=None, cell=58):
    """vurma cədvəli 1..n; blanks = [(sətir, sütun)] boş xana, mark = rənglənən xana"""
    rows = [[txt('·', 40, BLUE)] + [txt(str(c), 34, BLUE) for c in range(1, n + 1)]]
    for r in range(1, n + 1):
        line = [txt(str(r), 34, BLUE)]
        for c in range(1, n + 1):
            if (r, c) in blanks:
                line.append(box(int(cell * 0.95), int(cell * 0.8)))
            else:
                line.append(txt(str(r * c), 32, RED if mark == (r, c) else INK))
        rows.append(line)
    return table(rows, cell)


def flat(size=96):
    im, d = vec(size, size)
    k = size / 10
    d.rectangle([0, 0, size * S - 1, size * S - 1], fill=(144, 202, 249), outline=(21, 101, 192), width=3 * S)
    for i in range(1, 10):
        d.line([i * k * S, 0, i * k * S, size * S], fill=(21, 101, 192), width=S)
        d.line([0, i * k * S, size * S, i * k * S], fill=(21, 101, 192), width=S)
    return done(im)


def rod(size=96):
    im, d = vec(size // 10 + 2, size)
    k = size / 10
    d.rectangle([0, 0, (size // 10 + 2) * S - 1, size * S - 1], fill=(144, 202, 249), outline=(21, 101, 192), width=2 * S)
    for i in range(1, 10):
        d.line([0, i * k * S, (size // 10 + 2) * S, i * k * S], fill=(21, 101, 192), width=S)
    return done(im)


def unit(size=96):
    k = size // 10 + 2
    im, d = vec(k, k)
    d.rectangle([0, 0, k * S - 1, k * S - 1], fill=(144, 202, 249), outline=(21, 101, 192), width=2 * S)
    return done(im)


def hto(h, t, o, size=96):
    """yüzlük (kvadrat), onluq (çubuq), təklik (kub) blokları"""
    parts = []
    if h:
        parts.append(hstack([flat(size) for _ in range(h)], 8))
    if t:
        parts.append(hstack([rod(size) for _ in range(t)], 6))
    if o:
        parts.append(grid([unit(size) for _ in range(o)], 2, 5))
    return hstack(parts, 28, align='bottom')


def gram(v, size=34):
    return chip('%d q' % v, size, (255, 224, 178), INK, ORANGE)


def unit_expr(tokens, size=60):
    """ədəd + vahid: vahidləri (sm, m, kq, q, l, man, qəp, dəq) boz rəngdə yazır"""
    out = []
    for tk in tokens:
        if tk in ('sm', 'm', 'kq', 'q', 'l', 'man', 'qəp', 'dəq'):
            out.append(txt(tk, int(size * 0.7), GREY))
        else:
            out.append(tk)
    parts = []
    for tk in out:
        if not isinstance(tk, str) and tk is not BOX:
            parts.append(tk)
        else:
            parts.append(expr2([tk], size))
    return hstack(parts, int(size * 0.22))


def coins(vals, size=90):
    return hstack([coin(v, size) for v in vals], 10)


def notes(vals, w=170, h=88):
    return hstack([note(v, w, h) for v in vals], 10)


def tab(rows, size=34):
    return table([[txt(str(c), size, INK) for c in r] for r in rows], int(size * 2))


SWEETS = [['Şirniyyat', 'Şənbə', 'Bazar'], ['Bulka', 27, 25], ['Keks', 20, 24], ['Pirojna', 13, 16]]
PETS = [('Pişik', 8), ('İt', 4), ('Bülbül', 2), ('Tısbağa', 1), ('Dovşan', 3)]
SEASONS = [('Yaz', 6), ('Yay', 9), ('Payız', 3), ('Qış', 5)]


def pet_bars():
    return bars([(txt(n, 24), v) for n, v in PETS], maxv=8, unit=30, barw=64, colors=[O3, B3, Y3, G3, P3])


def season_bars():
    return bars([(txt(n, 24), v) for n, v in SEASONS], maxv=10, unit=28, barw=70, colors=[G3, Y3, O3, B3])


def stickers_picto():
    rows = [[txt('Heyvanlar', 30), row('⭐', 6, 44, 4, 6)], [txt('Maşınlar', 30), row('⭐', 5, 44, 4, 6)], [txt('Təyyarələr', 30), row('⭐', 4, 44, 4, 6)]]
    return vstack([table(rows, 70), hstack([em('⭐', 40), txt('= 2 stiker', 32, BLUE)], 8)], 10)


# ============================================================ 75
t = T(75, 'Vurma',
      'Sətir və sütunlarla düzülmüş əşyaların sayını vurma ilə tapırıq: 3 sətir, hər sətirdə 6 top – 3 · 6 = 18. Vuruqların yerini dəyişəndə hasil dəyişmir: 3 · 4 = 4 · 3.',
      hstack([array('⚽', 3, 6, 44), vstack([expr2(['6', '+', '6', '+', '6', '=', '18'], 44), expr2(['3', '·', '6', '=', '18'], 56)], 12)], 28))
t.num('Təkrar toplamanı vurma ilə yazın.', [18, 18], hstack([array('🍎', 3, 6, 40), stacked([['6', '+', '6', '+', '6', '=', BOX], ['3', '·', '6', '=', BOX]], 50)], 28), disp='18, 18')
for ch, r, c in [('🚗', 3, 4), ('✈️', 3, 2), ('🏀', 3, 5)]:
    t.num('Sətirləri və sütunları sayın. Vurma misalını yazın.', [r, c, r * c], vstack([array(ch, r, c, 48), expr2([BOX, '·', BOX, '=', BOX], 60)], 14), disp='%d · %d = %d' % (r, c, r * c))
t.num('Hasili tapın.', [20], vstack([array('⚽', 4, 5, 40), expr2(['4', '·', '5', '=', BOX], 64)], 14))
t.num('Vuruqların yerini dəyişin. Boş xanaya uyğun ədədi yazın.', [3], expr2(['3', '·', '4', '=', '4', '·', BOX], 76))
t.choice('Hansı ifadə 5 + 5 + 5 + 5 cəminə bərabərdir? Dairəyə alın.', ['4 · 5', '5 + 4', '5 · 5'], 0)
t.num('Kinozalda 5 sıra var, hər sırada 4 oturacaq var. Zalda neçə oturacaq var?', [20], word(['🎬', '💺'], ['5', '·', '4', '=', BOX]))
t.num('Hər qutuda 3 qələm var. 4 qutuda neçə qələm var?', [12], vstack([groups('✏️', (3, 3, 3, 3), 44), expr2(['4', '·', '3', '=', BOX], 60)], 14))
t.choice('Şəkilə uyğun ifadəni dairəyə alın.', ['2 · 5', '2 + 5', '5 − 2'], 0, stem=array('🌸', 2, 5, 52))

# ============================================================ 76
t = T(76, '2-yə və 3-ə vurma',
      'Ədədi 2-yə vurmaq 2-ni həmin ədəd dəfə toplamaq deməkdir: 4 · 2 = 2 + 2 + 2 + 2 = 8.',
      vstack([groups('🍈', (2, 2, 2, 2), 50), expr2(['4', '·', '2', '=', '2', '+', '2', '+', '2', '+', '2', '=', '8'], 46)], 16))
t.num('Hər qrupda 2 ulduz var. Cəmi neçə ulduz var?', [6], vstack([groups('⭐', (2, 2, 2), 50), expr2(['3', '·', '2', '=', BOX], 60)], 14))
t.num('Hər qrupda 2 ulduz var. Cəmi neçə ulduz var?', [10], vstack([groups('⭐', (2, 2, 2, 2, 2), 44), expr2(['5', '·', '2', '=', BOX], 60)], 14))
t.num('Hər qrupda 3 albalı var. Cəmi neçə albalı var?', [12], vstack([groups('🍒', (3, 3, 3, 3), 44), expr2(['4', '·', '3', '=', BOX], 60)], 14))
for a, b in [(7, 2), (6, 3), (9, 2), (8, 3)]:
    t.num('Hasili tapın.', [a * b], expr2([str(a), '·', str(b), '=', BOX], 80))
t.num('İkilərlə sayın. Sıranı davam etdirin.', [8, 10], seq([2, 4, 6, BOX, BOX]), disp='8, 10')
t.num('Üçlərlə sayın. Sıranı davam etdirin.', [12, 15], seq([3, 6, 9, BOX, BOX]), disp='12, 15')
t.num('Samir hər dəfə yeşiyə 2 yemiş qoydu. 7 dəfədən sonra yeşikdə neçə yemiş oldu?', [14], word(['🍈', '📦'], ['7', '·', '2', '=', BOX]))

# ============================================================ 77
t = T(77, '4-ə və 5-ə vurma',
      'Ədədi 4-ə vurmaq 4-ü həmin ədəd dəfə toplamaq deməkdir: 3 · 4 = 4 + 4 + 4 = 12. 5-ə vuranda da belədir: 3 · 5 = 5 + 5 + 5 = 15.',
      vstack([expr2(['3', '·', '4', '=', '4', '+', '4', '+', '4', '=', '12'], 50), expr2(['3', '·', '5', '=', '5', '+', '5', '+', '5', '=', '15'], 50)], 16, 'left'))
t.num('Bir kvadrat üçün 4 çöp lazımdır. 3 kvadrat üçün neçə çöp lazımdır?', [12],
      vstack([hstack([shape('square', 90, WHITE, BROWN) for _ in range(3)], 24), expr2(['3', '·', '4', '=', BOX], 60)], 14))
t.num('Bir əldə 5 barmaq var. 4 əldə neçə barmaq var?', [20], word(['🖐️', '🖐️', '🖐️', '🖐️'], ['4', '·', '5', '=', BOX]))
for a, b in [(6, 4), (8, 5), (9, 4), (7, 5)]:
    t.num('Hasili tapın.', [a * b], expr2([str(a), '·', str(b), '=', BOX], 80))
t.num('Beşlərlə sayın. Sıranı davam etdirin.', [20, 25], seq([5, 10, 15, BOX, BOX]), disp='20, 25')
t.num('Dördlərlə sayın. Sıranı davam etdirin.', [16, 20], seq([4, 8, 12, BOX, BOX]), disp='16, 20')
t.choice('Hansı bərabərlik doğrudur? Dairəyə alın.', ['3 · 4 = 12', '3 · 4 = 7', '4 · 5 = 9'], 0)
t.num('Bir maşının 4 təkəri var. 5 maşının neçə təkəri var?', [20], word(['🚗', '🚗', '🚗', '🚗', '🚗'], ['5', '·', '4', '=', BOX]))

# ============================================================ 78
t = T(78, 'Vurma cədvəli',
      'Vurma cədvəlində sətir və sütunun kəsişdiyi xanada hasil yazılır: 3 · 4 = 12.',
      hstack([mult_table(5, mark=(3, 4), cell=54), expr2(['3', '·', '4', '=', '12'], 56)], 30))
for bl, ans in [([(2, 3), (4, 5)], [6, 20]), ([(3, 3), (5, 4)], [9, 20]), ([(3, 5), (4, 2)], [15, 8])]:
    t.num('Vurma cədvəlində boş xanaları doldurun. Əvvəl yuxarıdakı xananı yazın.', ans, mult_table(5, blanks=bl, cell=46), disp=', '.join(map(str, ans)))
for a, b in [(4, 0), (5, 6), (3, 7)]:
    t.num('Hasili tapın.', [a * b], expr2([str(a), '·', str(b), '=', BOX], 80))
t.num('Hər qrupda 2 banan var. Cəmi neçə banan var?', [10], vstack([groups('🍌', (2, 2, 2, 2, 2), 44), expr2(['5', '·', '2', '=', BOX], 60)], 14))
t.num('Hər qrupda 6 çiyələk var. 3 qrupda neçə çiyələk var?', [18], vstack([groups('🍓', (6, 6, 6), 40, 3), expr2(['3', '·', '6', '=', BOX], 60)], 14))
t.num('Hər qutuda 6 armud var. 4 qutuda neçə armud var?', [24], word(['🍐', '📦'], ['4', '·', '6', '=', BOX]))
t.choice('Hasili 24 olan ifadəni dairəyə alın.', ['4 · 6', '5 · 4', '3 · 9'], 0)

# ============================================================ 79
t = T(79, 'Bölmə',
      'Əşyaları bərabər paylayanda bölmədən istifadə edirik: 15 nöqtə, hər sətirdə 5 nöqtə – 15 : 5 = 3 sətir.',
      hstack([array('🔵', 3, 5, 40), vstack([expr2(['15', '−', '5', '−', '5', '−', '5', '=', '0'], 42), expr2(['15', ':', '5', '=', '3'], 56)], 12)], 28))
t.num('Uşaqlar 24 gülü cərgələrə əkdilər, hər cərgəyə 6 gül. Neçə cərgə alındı?', [4], word(['🌷', '🧒'], ['24', ':', '6', '=', BOX]))
t.num('12 alma 3 boşqaba bərabər paylandı. Hər boşqabda neçə alma var?', [4], vstack([group('🍎', 12, 40, 6), plates('🍎', (0, 0, 0)), expr2(['12', ':', '3', '=', BOX], 60)], 12))
for a, b in [(20, 4), (15, 3), (18, 2), (25, 5)]:
    t.num('Bölməni yerinə yetirin.', [a // b], expr2([str(a), ':', str(b), '=', BOX], 80))
t.num('Təkrar çıxmaya baxın və bölməni tamamlayın.', [3], stacked([['15', '−', '5', '−', '5', '−', '5', '=', '0'], ['15', ':', '5', '=', BOX]], 52))
t.num('Nöqtələri sayın. Bölməyə aid misalları tamamlayın.', [5, 4], hstack([array('🔵', 4, 5, 34), stacked([['20', ':', '4', '=', BOX], ['20', ':', '5', '=', BOX]], 50)], 24), disp='5, 4')
t.num('10 konfeti 2 uşağa bərabər payladılar. Hər uşağa neçə konfet düşdü?', [5], word(['🍬', '👧', '👦'], ['10', ':', '2', '=', BOX]))
t.choice('Hansı şəkildə 12 alma 3 boşqaba bərabər paylanıb? Dairəyə alın.', [plates('🍎', (4, 4, 4), 30), plates('🍎', (5, 4, 3), 30), plates('🍎', (6, 6, 0), 30)], 0, disp='1-ci şəkil')

# ============================================================ 80
t = T(80, 'Vurma və bölmənin əlaqəsi',
      'Vurma və bölmə bir-biri ilə əlaqəlidir: 4 · 5 = 20, 5 · 4 = 20, 20 : 4 = 5, 20 : 5 = 4.',
      hstack([array('🏀', 4, 5, 34), vstack([expr2(['4', '·', '5', '=', '20'], 44), expr2(['20', ':', '4', '=', '5'], 44), expr2(['20', ':', '5', '=', '4'], 44)], 10, 'left')], 28))
for (w, a, b), lines, ans in [((18, 3, 6), [['3', '·', '6', '=', BOX], ['18', ':', '3', '=', BOX]], [18, 6]),
                              ((45, 5, 9), [['5', '·', '9', '=', BOX], ['45', ':', '9', '=', BOX]], [45, 5]),
                              ((27, 3, 9), [['27', ':', '3', '=', BOX], ['27', ':', '9', '=', BOX]], [9, 3])]:
    t.num('Ədəd üçlüyünə əsasən misalları tamamlayın.', ans, hstack([triple(w, a, b), stacked(lines, 52)], 36), disp=', '.join(map(str, ans)))
t.num('Vurmadan istifadə edərək bölün.', [5], stacked([['4', '·', '5', '=', '20'], ['20', ':', '4', '=', BOX]], 60))
t.num('Vurmadan istifadə edərək bölün.', [3], stacked([['3', '·', '7', '=', '21'], ['21', ':', '7', '=', BOX]], 60))
t.num('Məchul vuruğu tapın.', [4], expr2([BOX, '·', '4', '=', '16'], 80))
t.num('Məchul vuruğu tapın.', [6], expr2(['5', '·', BOX, '=', '30'], 80))
t.num('Stikerləri sayın. Vurma və bölməyə aid misalları tamamlayın.', [15, 5], hstack([array('🙂', 3, 5, 40), stacked([['3', '·', '5', '=', BOX], ['15', ':', '3', '=', BOX]], 50)], 24), disp='15, 5')
t.num('Hər qutuya 4 karandaş qoyurlar. 28 karandaş üçün neçə qutu lazımdır?', [7], word(['✏️', '📦'], ['28', ':', '4', '=', BOX]))
t.choice('2 · 7 = 14 olduğunu bilirik. Hansı bölmə doğrudur? Dairəyə alın.', ['14 : 7 = 2', '14 : 2 = 12', '7 : 2 = 14'], 0)

# ============================================================ 81
t = T(81, '500-ə qədər sayma',
      '10 təklik 1 onluq, 10 onluq 1 yüzlük təşkil edir. 123 – yüz iyirmi üç, 223 – iki yüz iyirmi üç.',
      vstack([hstack([label(hto(1, 2, 3, 90), '123', 40, INK), label(hto(2, 2, 3, 90), '223', 40, INK)], 50, 'bottom')], 10))
t.num('Ədəd oxunda boş xanalara uyğun ədədləri yazın.', [203, 207], numline(200, 210, 74, blanks=(203, 207), size=26), disp='203, 207')
t.num('Ədəd oxunda boş xanalara uyğun ədədləri yazın.', [150, 350], numline_step(0, 500, 50, 76, blanks=(150, 350), size=24), disp='150, 350')
t.num('On-on sayın. Sıranı davam etdirin.', [150, 160], seq([120, 130, 140, BOX, BOX], 56), disp='150, 160')
t.num('Yüz-yüz sayın. Sıranı davam etdirin.', [400, 500], seq([100, 200, 300, BOX, BOX], 56), disp='400, 500')
t.num('Əlli-əlli sayın. Sıranı davam etdirin.', [300, 350], seq([150, 200, 250, BOX, BOX], 56), disp='300, 350')
t.num('Bir-bir sayın. Sıranı davam etdirin.', [400, 401], seq([397, 398, 399, BOX, BOX], 56), disp='400, 401')
t.num('Hər ədəddən sonra gələn ədədi tapın.', [240, 310], stacked([['239', '+', '1', '=', BOX], ['309', '+', '1', '=', BOX]]), disp='240, 310')
t.num('Hər ədəddən əvvəl gələn ədədi tapın.', [299, 449], stacked([['300', '−', '1', '=', BOX], ['450', '−', '1', '=', BOX]]), disp='299, 449')
t.choice('Hansı ədəd 200 ilə 300 arasındadır? Dairəyə alın.', ['245', '320', '190'], 0)
t.choice('Ən böyük ədədi dairəyə alın.', ['409', '490', '449'], 1)

# ============================================================ 82
t = T(82, 'Yüzlük, onluq və təklik',
      '238 ədədində 2 yüzlük, 3 onluq və 8 təklik var: 238 = 200 + 30 + 8.',
      vstack([hto(2, 3, 8, 90), expr2(['238', '=', '200', '+', '30', '+', '8'], 54)], 16))
for h, tt, o in [(1, 4, 3), (3, 0, 5)]:
    t.num('Kubları sayın. Neçə yüzlük, onluq və təklik var? Soldan sağa yazın.', [h, tt, o],
          vstack([hto(h, tt, o, 90), hstack([box(), txt('yüzlük', 30, GREY), box(), txt('onluq', 30, GREY), box(), txt('təklik', 30, GREY)], 10)], 16), disp='%d yüzlük, %d onluq, %d təklik' % (h, tt, o))
for h, tt, o in [(2, 5, 6), (4, 1, 0)]:
    t.num('Kublara uyğun ədədi yazın.', [h * 100 + tt * 10 + o], vstack([hto(h, tt, o, 90), hstack([arrow(), box(170, 100)], 14)], 16))
t.num('Ədədi yüzlük, onluq və təkliklərin cəmi kimi yazın.', [300, 40, 7], expr2(['347', '=', BOX, '+', BOX, '+', BOX], 60), disp='300 + 40 + 7')
t.num('Ədədi yüzlük, onluq və təkliklərin cəmi kimi yazın.', [200, 5], expr2(['205', '=', BOX, '+', '0', '+', BOX], 60), disp='200 + 0 + 5')
t.num('Cəmi tapın.', [429], expr2(['400', '+', '20', '+', '9', '=', BOX], 68))
t.num('Cəmi tapın.', [160], expr2(['100', '+', '60', '=', BOX], 76))
t.choice('4 yüzlük, 0 onluq və 6 təklik hansı ədəddir? Dairəyə alın.', ['406', '460', '46'], 0)
t.sign('Ədədləri müqayisə edin. Dairələrə >, < və ya = yazın.', [('258', '285'), ('370', '307'), ('199', '201')], ['<', '>', '<'])

# ============================================================ 83
t = T(83, 'Pullar',
      '1 manat = 100 qəpik. Pulları böyükdən kiçiyə sıralayıb saymaq asandır: 50, 70, 80, 90 qəpik.',
      vstack([coins([50, 20, 10, 10], 96), txt('50 → 70 → 80 → 90 qəpik', 40, BLUE), notes([1], 170, 88), txt('1 manat = 100 qəpik', 40, INK)], 14))
t.num('Pulları sayın. Cəmi neçə qəpikdir?', [35], hstack([coins([20, 10, 5]), arrow(), box(), txt('qəp', 44, BLUE)], 14), disp='35 qəpik')
t.num('Pulları sayın. Cəmi neçə qəpikdir?', [95], hstack([coins([50, 20, 20, 5], 84), arrow(), box(), txt('qəp', 44, BLUE)], 12), disp='95 qəpik')
t.num('Əskinasları sayın. Cəmi neçə manatdır?', [21], vstack([notes([10, 5, 5, 1], 150, 80), hstack([arrow(), box(), txt('man', 44, BLUE)], 12)], 14), disp='21 manat')
t.num('Əskinasları sayın. Cəmi neçə manatdır?', [40], vstack([notes([20, 10, 10], 160, 84), hstack([arrow(), box(), txt('man', 44, BLUE)], 12)], 14), disp='40 manat')
t.num('Əskinasları sayın. Cəmi neçə manatdır?', [250], vstack([notes([100, 100, 50], 160, 84), hstack([arrow(), box(150, 96), txt('man', 44, BLUE)], 12)], 14), disp='250 manat')
t.num('İki 50 qəpiklik neçə qəpikdir?', [100], hstack([coins([50, 50]), arrow(), box(150, 96), txt('qəp', 44, BLUE)], 14), disp='100 qəpik (1 manat)')
t.num('Dörd 50 qəpiklik neçə manatdır?', [2], hstack([coins([50, 50, 50, 50], 80), arrow(), box(), txt('man', 44, BLUE)], 12), disp='2 manat')
t.choice('1 manata bərabər olanı dairəyə alın.', [coins([50, 50], 66), coins([20, 20, 20], 66), coins([10, 10], 66)], 0, disp='iki 50 qəpiklik')
t.num('Samirin 10 manatlıq, 5 manatlıq və 1 manatlıq pulu var. Onun neçə manatı var?', [16], vstack([notes([10, 5, 1], 160, 84), hstack([arrow(), box(), txt('man', 44, BLUE)], 12)], 14), disp='16 manat')
t.sign('Müqayisə edin. Dairələrə >, < və ya = yazın.', [('1 man', '90 qəp'), ('2 man', '200 qəp')], ['>', '='])

# ============================================================ 84
t = T(84, 'Alış-veriş',
      'Bir neçə malın ödəniləcək məbləğini tapmaq üçün qiymətlər toplanır: 9 man + 15 man = 24 man. Eyni maldan bir neçə dənə alanda vururuq: 4 · 2 man = 8 man.',
      vstack([hstack([priced('🧢', '9 man'), priced('🧣', '15 man'), unit_expr(['9', 'man', '+', '15', 'man', '=', '24', 'man'], 44)], 18), unit_expr(['4', '·', '2', 'man', '=', '8', 'man'], 44)], 16))
t.num('Ödəniləcək məbləği tapın.', [56], vstack([hstack([priced('👢', '42 man'), priced('🧤', '14 man')], 30), unit_expr(['42', '+', '14', '=', BOX, 'man'], 60)], 14), disp='56 manat')
t.num('Bir karandaş 9 qəpikdir. 4 karandaş neçə qəpikdir?', [36], vstack([hstack([priced('✏️', '9 qəp', 80) for _ in range(4)], 14), unit_expr(['4', '·', '9', '=', BOX, 'qəp'], 60)], 14), disp='36 qəpik')
t.num('Papaq 9 manat, şərf 15 manatdır. Hamısı neçə manatdır?', [24], vstack([hstack([priced('🧢', '9 man'), priced('🧣', '15 man')], 30), unit_expr(['9', '+', '15', '=', BOX, 'man'], 60)], 14), disp='24 manat')
t.num('Bir keks 2 manatdır. 5 keks neçə manatdır?', [10], vstack([hstack([priced('🧁', '2 man', 70) for _ in range(5)], 10), unit_expr(['5', '·', '2', '=', BOX, 'man'], 60)], 14), disp='10 manat')
t.num('Elxanın 50 manatı var idi. O, 32 manatlıq top aldı. Onun neçə manatı qaldı?', [18], vstack([priced('⚽', '32 man'), unit_expr(['50', '−', '32', '=', BOX, 'man'], 60)], 14), disp='18 manat')
t.num('Kitab 18 manat, dəftər 3 manatdır. Lalə 25 manat verdi. Əvvəl məbləği, sonra qalığı tapın.', [21, 4],
      vstack([hstack([priced('📘', '18 man'), priced('📒', '3 man')], 30), stacked([['18', '+', '3', '=', BOX], ['25', '−', '21', '=', BOX]], 52)], 14), disp='21, 4 manat')
t.num('1 kq alma 3 manat, 1 kq armud 2 manatdır. 2 kq alma və 1 kq armud neçə manatdır?', [8], vstack([hstack([priced('🍎', '3 man'), priced('🍎', '3 man'), priced('🍐', '2 man')], 20), unit_expr(['3', '+', '3', '+', '2', '=', BOX, 'man'], 56)], 14), disp='8 manat')
t.choice('Alıcının 20 manatı var. O, hansını ala bilər? Dairəyə alın.', [priced('⚽', '25 man', 90), priced('🎒', '35 man', 90), priced('📚', '18 man', 90)], 2, disp='kitablar (18 manat)')
t.num('Dondurma 60 qəpik, şirə 30 qəpikdir. Hamısı neçə qəpikdir?', [90], vstack([hstack([priced('🍦', '60 qəp'), priced('🧃', '30 qəp')], 30), unit_expr(['60', '+', '30', '=', BOX, 'qəp'], 60)], 14), disp='90 qəpik')
t.num('Lalə 1 manat verdi və 70 qəpiklik çörək aldı. Ona neçə qəpik qaytarılar?', [30], vstack([priced('🍞', '70 qəp'), unit_expr(['100', '−', '70', '=', BOX, 'qəp'], 60)], 14), disp='30 qəpik')

# ============================================================ 85
t = T(85, 'Uzunluq',
      'Uzunluğu santimetrlə (sm) və metrlə (m) ölçürük. 100 santimetr 1 metrdir: 1 m = 100 sm.',
      vstack([on_ruler(strip(10, 52, BLUE), 12, 52), unit_expr(['1', 'm', '=', '100', 'sm'], 60)], 16))
t.num('Zolaq neçə santimetrdir?', [7], hstack([on_ruler(strip(7, 56, RED), 10, 56), box(), txt('sm', 44, BLUE)], 14), disp='7 sm')
t.num('Karandaş neçə santimetrdir?', [9], hstack([on_ruler(pencil(9, 52), 10, 52), box(), txt('sm', 44, BLUE)], 14), disp='9 sm')
t.num('Neçə metrdir?', [2], unit_expr(['200', 'sm', '=', BOX, 'm'], 70), disp='2 m')
t.num('Neçə metrdir?', [3], unit_expr(['300', 'sm', '=', BOX, 'm'], 70), disp='3 m')
t.num('Neçə santimetrdir?', [500], unit_expr(['5', 'm', '=', BOX, 'sm'], 70), disp='500 sm')
t.num('Hesablayın.', [75], unit_expr(['45', 'sm', '+', '30', 'sm', '=', BOX, 'sm'], 60), disp='75 sm')
t.num('Hesablayın.', [55], unit_expr(['80', 'sm', '−', '25', 'sm', '=', BOX, 'sm'], 60), disp='55 sm')
t.choice('Qapının hündürlüyü təxminən nə qədərdir? Dairəyə alın.', ['2 m', '2 sm', '20 m'], 0, stem=em('🚪', 140))
t.choice('Karandaşın uzunluğu təxminən nə qədərdir? Dairəyə alın.', ['15 sm', '15 m', '150 m'], 0, stem=em('✏️', 120))
t.num('Anar 1 metrlik lentdən 40 santimetr kəsdi. Neçə santimetr lent qaldı?', [60], vstack([em('🎀', 100), unit_expr(['100', 'sm', '−', '40', 'sm', '=', BOX, 'sm'], 56)], 14), disp='60 sm')

# ============================================================ 86
t = T(86, 'Kütlə',
      'Əşyanın ağır və ya yüngül olması onun kütləsindən asılıdır. Kütlə kiloqramla (kq) ölçülür. 1 kq-dan yüngül əşyaların kütləsini qramla (q) ifadə edirik.',
      hstack([label(scale([em('🍉', 90)], [weight(5, 80)], 0, 460), '5 kq', 34, INK), label(scale([em('🍓', 60)], [gram(20)], 0, 360), '20 q', 34, INK)], 30, 'bottom'))
t.num('Tərəzi bərabərdir. Qarpız neçə kiloqramdır?', [5], hstack([scale([em('🍉', 100)], [weight(2), weight(3)], 0, 520), box(), txt('kq', 44, BLUE)], 14), disp='5 kq')
t.num('Tərəzi bərabərdir. Kələm neçə kiloqramdır?', [4], hstack([scale([em('🥬', 90)], [weight(2), weight(2)], 0, 520), box(), txt('kq', 44, BLUE)], 14), disp='4 kq')
t.num('Tərəzi bərabərdir. Karandaş neçə qramdır?', [15], vstack([scale([em('✏️', 80)], [gram(5), gram(5), gram(5)], 0, 520), unit_expr(['3', '·', '5', '=', BOX, 'q'], 56)], 12), disp='15 q')
t.num('Tərəzi bərabərdir. Pozan neçə qramdır?', [19], hstack([scale([em('🧽', 80)], [gram(5), gram(5), gram(5), gram(2), gram(2)], 0, 560), box(), txt('q', 44, BLUE)], 14), disp='19 q')
t.choice('Ağır olanı dairəyə alın.', [em('🍉', 100), em('🍓', 100)], 0, stem=scale([em('🍉', 90)], [em('🍓', 50)], -1, 480), disp='qarpız')
t.num('Hesablayın.', [39], unit_expr(['25', 'kq', '+', '14', 'kq', '=', BOX, 'kq'], 60), disp='39 kq')
t.num('Hesablayın.', [32], unit_expr(['50', 'kq', '−', '18', 'kq', '=', BOX, 'kq'], 60), disp='32 kq')
t.num('Bir səbətdə 12 kq, o birində 9 kq alma var. Cəmi neçə kiloqram alma var?', [21], vstack([hstack([label(em('🧺', 90), '12 kq', 32, INK), label(em('🧺', 90), '9 kq', 32, INK)], 30), unit_expr(['12', '+', '9', '=', BOX, 'kq'], 56)], 14), disp='21 kq')
t.num('Tərəzi bərabər olsun deyə sağ tərəfə neçə kiloqram qoymaq lazımdır?', [3], hstack([scale([weight(5)], [weight(2), box(80, 80)], -1, 520), box(), txt('kq', 44, BLUE)], 14), disp='3 kq')
t.choice('Hansı əşyanın kütləsini qramla ifadə etmək rahatdır? Dairəyə alın.', [em('🍓', 100), em('🍉', 100), em('🛋️', 100)], 0, disp='çiyələk')

# ============================================================ 87
t = T(87, 'Tutum',
      'Qabın tutumu onun nə qədər su, yaxud başqa maye tuta bildiyini göstərir. Tutum litrlə (l) ifadə olunur. 5 stəkan su təxminən 1 litrdir.',
      hstack([row('🥛', 5, 60, 6, 5), txt('≈', 60, BLUE), label(em('🧴', 110), '1 l', 34, INK)], 20))
t.num('Qablarda cəmi neçə litr su var?', [7], vstack([hstack([label(em('🧴', 90), '3 l', 32, INK), label(em('🧴', 100), '4 l', 32, INK)], 30), unit_expr(['3', 'l', '+', '4', 'l', '=', BOX, 'l'], 56)], 14), disp='7 l')
t.num('24 l süd 3 litrlik balonlara töküldü. Neçə balon alındı?', [8], word(['🥛', '🫙'], ['24', ':', '3', '=', BOX]))
t.num('Qazanın tutumu 8 litrdir. Onu 2 litrlik qabla doldurmaq üçün neçə dəfə su tökmək lazımdır?', [4], word(['🍲', '🥤'], ['8', ':', '2', '=', BOX]))
t.num('Qabı 5 dəfə 2 litr su ilə doldurub vedrəyə tökdülər. Vedrədə neçə litr su oldu?', [10], word(['🪣'], ['5', '·', '2', '=', BOX]))
t.num('Mağazaya 90 l süd gətirdilər. Günortaya qədər 47 l, günortadan sonra 35 l satıldı. Neçə litr süd qaldı?', [8], word(['🥛', '🏪'], ['90', '−', '(', '47', '+', '35', ')', '=', BOX], 52))
t.num('Bir fabrik həftədə 64 l, digəri ondan 29 l az yağ işlədir. İkinci fabrik neçə litr yağ işlədir?', [35], word(['🏭', '🧈'], ['64', '−', '29', '=', BOX]))
t.choice('Tutumu ən böyük olan qabı dairəyə alın.', [em('🛁', 110), em('🥛', 110), em('🪣', 110)], 0, disp='vanna')
t.choice('Vedrənin tutumu təxminən nə qədərdir? Dairəyə alın.', ['10 l', '1 l', '100 l'], 0, stem=em('🪣', 130))
t.num('Qabda 10 l su var idi. Əvvəl 3 l, sonra 2 l su götürdülər. Qabda neçə litr su qaldı?', [5], word(['💧'], ['10', '−', '3', '−', '2', '=', BOX]))
t.num('5 stəkan su təxminən 1 litrdir. 3 litr su təxminən neçə stəkandır?', [15], word(['🥛'], ['3', '·', '5', '=', BOX]))

# ============================================================ 88
t = T(88, 'Təkrarlanan hadisələr',
      'Elə hadisələr var ki, mütləq olacaq, ola bilər, yaxud ola bilməz. Gecədən sonra mütləq gündüz olacaq. Sabah hava buludlu ola bilər. Gecə günəş çıxa bilməz.',
      hstack([label(hstack([em('🌙', 70), arrow(50), em('☀️', 70)], 6), 'Mütləq olacaq', 28, GREEN), label(em('🌥️', 90), 'Ola bilər', 28, ORANGE), label(hstack([em('🌃', 80), em('☀️', 56)], 4), 'Ola bilməz', 28, RED)], 30, 'bottom'))
EV = ['Mütləq olacaq', 'Ola bilər', 'Ola bilməz']
t.choice('«Gecədən sonra gündüz olacaq». Bu hadisə necədir? Dairəyə alın.', EV, 0, stem=hstack([em('🌙', 90), arrow(), em('☀️', 90)], 16))
t.choice('«Sabah yağış yağacaq». Bu hadisə necədir? Dairəyə alın.', EV, 1, stem=em('🌧️', 110))
t.choice('«Gecə günəş çıxacaq». Bu hadisə necədir? Dairəyə alın.', EV, 2, stem=hstack([em('🌃', 110)], 10))
BTN = hstack([em('🔴', 70), em('🔴', 70), em('🟡', 70)], 14)
t.choice('Qutuda 2 qırmızı və 1 sarı düymə var. Baxmadan 2 düymə çıxarıldı. «Düymələrdən biri göydür». Bu necədir?', EV, 2, stem=BTN)
t.choice('Qutuda 2 qırmızı və 1 sarı düymə var. Baxmadan 2 düymə çıxarıldı. «Düymələrdən biri qırmızıdır». Bu necədir?', EV, 0, stem=BTN)
t.choice('Qutuda 2 qırmızı və 1 sarı düymə var. Baxmadan 2 düymə çıxarıldı. «Düymələrdən biri sarıdır». Bu necədir?', EV, 1, stem=BTN)
t.choice('Torbada yalnız sarı muncuqlar var. Baxmadan bir muncuq götürüldü. O necə olacaq? Dairəyə alın.', ['Mütləq sarı olacaq', 'Sarı ola bilər', 'Sarı ola bilməz'], 0, stem=hstack([em('🟡', 60) for _ in range(4)], 8))
t.choice('Qaydanı tapın. Sonra hansı muncuq gələr? Dairəyə alın.', [em('🟡', 90), em('🔴', 90), em('🔵', 90)], 0, stem=hstack([em(c, 64) for c in '🔴🟡🔴🟡🔴'] + [box(80, 80)], 10), disp='sarı')
t.choice('Qaydanı tapın. Sonra hansı muncuq gələr? Dairəyə alın.', [em('🔴', 90), em('🔵', 90), em('🟢', 90)], 1, stem=hstack([em(c, 60) for c in '🔵🔵🔴🔵🔵🔴🔵'] + [box(76, 76)], 8), disp='göy')
t.num('Qolbaqda qayda belədir: 2 qırmızı, 1 sarı muncuq. Qayda 4 dəfə təkrarlanır. Qolbaqda neçə muncuq var?', [12],
      vstack([hstack([em(c, 46) for c in '🔴🔴🟡🔴🔴🟡🔴🔴🟡🔴🔴🟡'], 4), expr2(['4', '·', '3', '=', BOX], 60)], 14))

# ============================================================ 89
t = T(89, 'Saat',
      'Qısa əqrəb saatı, uzun əqrəb dəqiqəni göstərir. Uzun əqrəb 12-nin üstündə olanda saat tamamdır, 6-nın üstündə olanda yarısıdır. 1 saat = 60 dəqiqə.',
      hstack([label(clock(1, 200), 'Saat 1 tamamdır', 28, INK), label(clock(1, 200, 30), 'Saat 2-nin yarısıdır', 28, INK)], 40, 'bottom'))
for hh in (2, 9, 11):
    t.num('Saat neçə tamamdır? Qutuya yazın.', [hh], hstack([clock(hh, 230), arrow(), box()], 24), disp='saat %d' % hh)
t.choice('«Saat 5-in yarısıdır». Bunu göstərən saatı dairəyə alın.', [clock(4, 150, 30), clock(5, 150, 30), clock(5, 150)], 0, disp='4:30')
t.choice('«Saat 8-in yarısıdır». Bunu göstərən saatı dairəyə alın.', [clock(8, 150, 30), clock(7, 150, 30), clock(8, 150)], 1, disp='7:30')
t.num('Yarım saat neçə dəqiqədir?', [30], vstack([unit_expr(['1', 'saat', '=', '60', 'dəq'], 52), unit_expr(['yarım saat', '=', BOX, 'dəq'], 52)], 14), disp='30 dəqiqə')
t.num('Saat 3 tamamdır. 2 saat sonra saat neçə olacaq?', [5], hstack([clock(3, 200), arrow(), box()], 20), disp='saat 5')
t.num('Rəsm məşğələsi saat 10 tamamda başlayır və 1 saat davam edir. Məşğələ saat neçədə bitir?', [11], hstack([em('🎨', 100), clock(10, 200), arrow(), box()], 20), disp='saat 11')
t.num('Uzun əqrəb 1-in üstündədir. Saat 10-a neçə dəqiqə işləyib?', [5], hstack([clock(9, 230, 5), arrow(), box(), txt('dəq', 44, BLUE)], 20), disp='5 dəqiqə')
t.choice('Dərs saat 9-un yarısında başladı. Bunu göstərən saatı dairəyə alın.', [clock(8, 150, 30), clock(9, 150, 30), clock(9, 150)], 0, disp='8:30')

# ============================================================ 90
t = T(90, 'Cədvəl, piktoqram, diaqram',
      'Cədvəldə məlumatlar sətir və sütunlarla verilir. Piktoqramda bir işarə bir neçə əşyanı göstərə bilər. Diaqramda sütunun hündürlüyü sayı göstərir.',
      hstack([tab(SWEETS, 30), pet_bars()], 30, 'bottom'))
t.num('Cədvələ baxın. Şənbə günü neçə pirojna satıldı?', [13], hstack([tab(SWEETS), arrow(), box()], 20))
t.num('Cədvələ baxın. Şənbə və bazar günləri cəmi neçə bulka satıldı?', [52], vstack([tab(SWEETS), expr2(['27', '+', '25', '=', BOX], 56)], 14))
t.num('Cədvələ baxın. Bazar günü şənbə günündən neçə keks çox satıldı?', [4], vstack([tab(SWEETS), expr2(['24', '−', '20', '=', BOX], 56)], 14))
t.choice('Cədvələ baxın. Şənbə günü ən çox hansı şirniyyat satıldı? Dairəyə alın.', ['Bulka', 'Keks', 'Pirojna'], 0, stem=tab(SWEETS))
t.num('Piktoqrama baxın. Hər ulduz 2 stikerdir. Samirin neçə heyvan stikeri var?', [12], vstack([stickers_picto(), expr2(['6', '·', '2', '=', BOX], 54)], 12))
t.num('Piktoqrama baxın. Samirin neçə təyyarə stikeri var?', [8], hstack([stickers_picto(), arrow(), box()], 16))
t.num('Piktoqrama baxın. Samirin neçə maşın stikeri var?', [10], hstack([stickers_picto(), arrow(), box()], 16))
t.num('Diaqrama baxın. Neçə uşaq pişiyi sevir?', [8], hstack([pet_bars(), arrow(), box()], 16))
t.num('Diaqrama baxın. Pişiyi sevənlər iti sevənlərdən neçə nəfər çoxdur?', [4], vstack([pet_bars(), expr2(['8', '−', '4', '=', BOX], 52)], 12))
t.choice('Diaqrama baxın. Ən az uşaq hansı heyvanı sevir? Dairəyə alın.', ['Tısbağa', 'Bülbül', 'Dovşan'], 0, stem=pet_bars())

# ============================================================ 91
t = T(91, 'Məlumatları necə toplamalı?',
      'Sorğu keçiririk: hamıya eyni sualı veririk və cavabları cədvəldə cizgilərlə qeyd edirik. Sonra cizgiləri sayıb ədədlə yazırıq.',
      table([[txt('Pişik', 30), tally(8, 56), txt('8', 32)], [txt('İt', 30), tally(4, 56), txt('4', 32)], [txt('Dovşan', 30), tally(3, 56), txt('3', 32)]], 76))
for n, ani in [(8, 'pişiyi'), (4, 'iti'), (7, 'futbolu')]:
    t.num('Cizgiləri sayın. Neçə uşaq %s seçdi?' % ani, [n], hstack([tally(n, 80), arrow(), box()], 20))
t.num('Cədvələ baxın. Sorğuda cəmi neçə uşaq iştirak etdi?', [18], vstack([tab([['Heyvan', 'Uşaq']] + [[a, v] for a, v in PETS], 30), expr2(['8', '+', '4', '+', '2', '+', '1', '+', '3', '=', BOX], 46)], 12))
t.choice('Cizgilərlə 6 hansıdır? Dairəyə alın.', [tally(6, 70), tally(5, 70), tally(8, 70)], 0, disp='1-ci')
t.num('Fəsillər sorğusunun cədvəlinə baxın. Cəmi neçə uşaq iştirak etdi?', [23], vstack([tab([['Fəsil', 'Uşaq']] + [[a, v] for a, v in SEASONS], 30), expr2(['6', '+', '9', '+', '3', '+', '5', '=', BOX], 48)], 12))
t.num('Yayı sevənlər payızı sevənlərdən neçə nəfər çoxdur?', [6], vstack([season_bars(), expr2(['9', '−', '3', '=', BOX], 52)], 12))
t.choice('Ən çox uşaq hansı fəsli sevir? Dairəyə alın.', ['Yay', 'Yaz', 'Qış'], 0, stem=season_bars())
t.num('Diaqrama baxın. Neçə uşaq qışı seçib?', [5], hstack([season_bars(), arrow(), box()], 16))
t.num('Yazı və qışı seçənlər cəmi neçə nəfərdir?', [11], vstack([season_bars(), expr2(['6', '+', '5', '=', BOX], 52)], 12))

# ------------------------------------------------------------------ output
for tp in TOPICS:
    if len(tp.problems) != 10: print('COUNT', tp.n, len(tp.problems))
os.makedirs(os.path.join(OUT, 'data'), exist_ok=True)
json.dump({'topics': [tp.d for tp in TOPICS]}, open(os.path.join(OUT, 'data/topics.json'), 'w'), ensure_ascii=False)
json.dump(VOICE, open(os.path.join(OUT, 'data/voice.json'), 'w'), ensure_ascii=False, indent=0)
print('topics', len(TOPICS), 'voice', len(VOICE))
