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

# ------------------------------------------------------------------ output
for tp in TOPICS:
    if len(tp.problems) != 10: print('COUNT', tp.n, len(tp.problems))
os.makedirs(os.path.join(OUT, 'data'), exist_ok=True)
json.dump({'topics': [tp.d for tp in TOPICS]}, open(os.path.join(OUT, 'data/topics.json'), 'w'), ensure_ascii=False)
json.dump(VOICE, open(os.path.join(OUT, 'data/voice.json'), 'w'), ensure_ascii=False, indent=0)
print('topics', len(TOPICS), 'voice', len(VOICE))
