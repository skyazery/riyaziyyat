"""1-ci sinif riyaziyyat, 2-ci hissə: 21 mövzu (29–49), hər mövzuda 10 tapşırıq.
Run: python3 content.py OUTDIR   -> OUTDIR/img/*.webp, OUTDIR/data/topics.json, OUTDIR/data/voice.json"""
import hashlib, json, os, sys
from draw import *

OUT = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/riyaziyyat/1-2'
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


TOPICS = []


def T(*a):
    t = Topic(*a)
    TOPICS.append(t)
    return t


SH = {'triangle': 'üçbucaq', 'circle': 'dairə', 'square': 'kvadrat', 'rect': 'düzbucaqlı'}


def sh(k, c=BLUE, s=100, **kw):
    return shape(k, s, c, **kw)


def mixed(spec, s=80, cols=None):
    return frame(grid([sh(k, COLORS[c], s) for k, c in spec], cols or len(spec), 22), 20)


# ============================================================ 29
t = T(29, 'Üçbucaq, dairə, kvadrat, düzbucaqlı',
      'Üçbucağın 3 tərəfi və 3 təpəsi var. Kvadratın 4 tərəfi bərabərdir. Dairənin təpəsi yoxdur.',
      hstack([label(sh('triangle', RED, 120), 'üçbucaq'), label(sh('circle', BLUE, 120), 'dairə'), label(sh('square', GREEN, 120), 'kvadrat'), label(sh('rect', YELLOW, 110), 'düzbucaqlı')], 50, 'bottom'))
t.choice('Üçbucağı dairəyə al.', [sh('square', GREEN), sh('triangle', RED), sh('circle', BLUE), sh('rect', YELLOW, 90)], 1, disp='üçbucaq')
t.choice('Kvadratı dairəyə al.', [sh('circle', ORANGE), sh('rect', PURPLE, 90), sh('square', BLUE), sh('triangle', GREEN)], 2, disp='kvadrat')
t.choice('Düzbucaqlını dairəyə al.', [sh('triangle', YELLOW), sh('square', RED), sh('circle', GREEN), sh('rect', BLUE, 90)], 3, disp='düzbucaqlı')
t.choice('Təkər hansı fiqura oxşayır? Dairəyə al.', [sh('triangle', ORANGE), sh('circle', ORANGE), sh('square', ORANGE)], 1, stem=em('🛞', 150), disp='dairə')
t.num('Neçə üçbucaq var? Say və qutuya yaz.', [4], hstack([mixed([('triangle', 'red'), ('circle', 'blue'), ('triangle', 'green'), ('square', 'yellow'), ('triangle', 'orange'), ('circle', 'purple'), ('triangle', 'blue'), ('square', 'red')], 80, 4), arrow(), box()], 30))
t.num('Neçə kvadrat var? Say və qutuya yaz.', [3], hstack([mixed([('square', 'green'), ('rect', 'blue'), ('circle', 'red'), ('square', 'yellow'), ('triangle', 'purple'), ('rect', 'orange'), ('square', 'pink'), ('circle', 'green')], 80, 4), arrow(), box()], 30))
t.num('Neçə dairə var? Say və qutuya yaz.', [5], hstack([mixed([('circle', 'red'), ('square', 'blue'), ('circle', 'yellow'), ('circle', 'green'), ('triangle', 'orange'), ('circle', 'purple'), ('rect', 'pink'), ('circle', 'blue')], 80, 4), arrow(), box()], 30))
t.num('Üçbucağın neçə təpəsi var? Qutuya yaz.', [3], hstack([triangle_vertices(200), arrow(), box()], 30))
t.num('Kvadratın neçə tərəfi var? Qutuya yaz.', [4], hstack([square_sides(180), arrow(), box()], 30))
t.choice('Bütün üçbucaqları dairəyə al.', [sh('triangle', RED, 90), sh('circle', BLUE, 90), sh('square', GREEN, 90), sh('triangle', YELLOW, 70), sh('rect', ORANGE, 70), sh('triangle', PURPLE, 100), sh('circle', RED, 70), sh('square', BLUE, 70)], [0, 3, 5], mode='multi', disp='3 üçbucaq')

# ============================================================ 30
B3 = (66, 165, 245); R3 = (239, 83, 80); G3 = (102, 187, 106); O3 = (255, 167, 38); P3 = (171, 71, 188)
t = T(30, 'Fəza fiqurları', 'Fəza fiqurları: kub, kuboid, kürə, silindr, konus.',
      hstack([label(solid('cube', 110, B3), 'kub'), label(solid('cuboid', 100, R3), 'kuboid'), label(solid('sphere', 110, G3), 'kürə'), label(solid('cylinder', 110, O3), 'silindr'), label(solid('cone', 110, P3), 'konus')], 36, 'bottom'))
t.choice('Kubu dairəyə al.', [solid('sphere', 110, G3), solid('cube', 110, B3), solid('cylinder', 110, O3)], 1, disp='kub')
t.choice('Kürəni dairəyə al.', [solid('cone', 110, P3), solid('cuboid', 95, R3), solid('sphere', 110, G3)], 2, disp='kürə')
t.choice('Silindri dairəyə al.', [solid('cylinder', 110, O3), solid('cube', 110, B3), solid('cone', 110, P3)], 0, disp='silindr')
t.choice('Konusu dairəyə al.', [solid('sphere', 110, R3), solid('cylinder', 110, G3), solid('cone', 110, O3)], 2, disp='konus')
t.choice('Kuboidi dairəyə al.', [solid('cube', 110, G3), solid('cuboid', 95, P3), solid('cylinder', 110, B3)], 1, disp='kuboid')
t.choice('Top hansı fiqura oxşayır? Dairəyə al.', [solid('cube', 100, B3), solid('sphere', 100, B3), solid('cone', 100, B3)], 1, stem=em('⚽', 140), disp='kürə')
t.choice('Zər hansı fiqura oxşayır? Dairəyə al.', [solid('cylinder', 100, R3), solid('cone', 100, R3), solid('cube', 100, R3)], 2, stem=em('🎲', 140), disp='kub')
t.choice('Silindr formasında olan əşyanı dairəyə al.', [em('🎁', 120), em('🥫', 120), em('🏀', 120)], 1, stem=solid('cylinder', 100, O3), disp='konserv qutusu')
t.choice('Kub formasında olan əşyaların hamısını dairəyə al.', [em('🎲', 100), em('⚽', 100), em('🧊', 100), em('🥫', 100), em('🍦', 100)], [0, 2], mode='multi', stem=solid('cube', 90, B3), disp='zər, buz')
t.num('Neçə kub var? Say və qutuya yaz.', [3], hstack([frame(grid([solid('cube', 70, B3), solid('sphere', 70, G3), solid('cube', 70, R3), solid('cone', 70, P3), solid('cylinder', 70, O3), solid('cube', 70, G3)], 3, 24), 18), arrow(), box()], 30))

# ============================================================ 31
t = T(31, 'Tam, yarı', 'Tamı 2 bərabər hissəyə bölürük. Hər hissə yarıdır.',
      hstack([label(sh('circle', O3, 140), 'tam'), arrow(), label(sh('circle', O3, 140, split=0.5), '2 bərabər hissə'), arrow(), label(sh('circle', O3, 140, half='half'), 'yarı')], 30, 'bottom'))
t.choice('Hansı fiqur 2 bərabər hissəyə bölünüb? Dairəyə al.', [sh('circle', G3, 110, split=0.3), sh('circle', G3, 110, split=0.5), sh('circle', G3, 110, split=0.75)], 1)
t.choice('Hansı fiqur 2 bərabər hissəyə bölünüb? Dairəyə al.', [sh('square', B3, 110, split='diag'), sh('square', B3, 110, split='horiz_bad'), sh('square', B3, 110, split=0.25)], 0)
t.choice('Hansı fiqur 2 bərabər hissəyə bölünüb? Dairəyə al.', [sh('rect', R3, 90, split=0.7), sh('rect', R3, 90, split='horiz_bad'), sh('rect', R3, 90, split=0.5)], 2)
t.choice('Hansı fiqur 2 bərabər hissəyə bölünüb? Dairəyə al.', [sh('triangle', P3, 110, split='tri_bad'), sh('triangle', P3, 110, split='tri')], 1)
t.choice('Yarısı rənglənmiş fiquru dairəyə al.', [sh('circle', R3, 110, half='quarter'), sh('circle', R3, 110, half='half'), sh('circle', R3, 110, half='most')], 1)
t.num('8 konfeti 2 uşağa bərabər böl. Hər uşağa neçə konfet düşər?', [4], hstack([frame(row('🍬', 8, 60, 8, 4), 14), arrow(), vstack([em('👦', 70), box()], 8), vstack([em('👧', 70), box(color=GREY)], 8)], 30), disp='4')
t.num('10 çiçəyin yarısı neçədir?', [5], hstack([frame(row('🌷', 10, 60, 8, 5), 14), arrow(), box()], 30))
t.num('Aynur 3 almanı yarıya böldü. Neçə yarı oldu?', [6], hstack([frame(row('🍎', 3, 90, 30), 16), arrow(), box()], 30))
t.num('12 topun yarısı neçədir?', [6], hstack([frame(row('⚽', 12, 56, 8, 6), 14), arrow(), box()], 30))
t.num('4 yarı alma var. Tam neçə alma olar?', [2], hstack([frame(hstack([sh('circle', R3, 80, half='half') for _ in range(4)], 18), 14), arrow(), box()], 30))

# ============================================================ 32
t = T(32, 'Ədədlərin toplanması', 'Toplayanda ədəd oxunda sağa gedirik: 12 + 3 = 15.',
      vstack([numline(10, 20, 56, start=12, jumps=3, marks=(15,)), expr(['12', '+', '3', '=', '15'], 60)], 10))
t.num('Şəkilə uyğun ifadəni yaz: toplanan + toplanan = cəm.', [10, 3, 13], vstack([hstack([dots_frame(10), txt('+', 60, BLUE), dots_row(3, RED, 50)], 20), expr([BOX, '+', BOX, '=', BOX], 60)], 24), disp='10 + 3 = 13')
t.num('Şəkilə uyğun ifadəni yaz: toplanan + toplanan = cəm.', [12, 5, 17], vstack([hstack([vstack([dots_frame(10), dots_row(2, BLUE, 44)], 10, 'left'), txt('+', 60, BLUE), dots_row(5, RED, 44)], 20), expr([BOX, '+', BOX, '=', BOX], 60)], 24), disp='12 + 5 = 17')
for a, b in [(15, 3), (10, 4), (12, 6), (17, 3)]:
    t.num('Cəmi tap.', [a + b], expr([str(a), '+', str(b), '=', BOX], 80))
t.num('Ədəd oxunda 13 ədədindən 4 addım sağa get. Cəmi yaz.', [17], vstack([numline(10, 20, 60, start=13), expr(['13', '+', '4', '=', BOX], 60)], 16))
t.num('Ədəd oxunda 11 ədədindən 5 addım sağa get. Cəmi yaz.', [16], vstack([numline(10, 20, 60, start=11), expr(['11', '+', '5', '=', BOX], 60)], 16))
t.num('Səbətdə 12 alma var idi. Samir daha 4 alma qoydu. Hamısı neçə oldu?', [16], hstack([group('🍎', 12, 50, 6), txt('+', 60, BLUE), group('🍎', 4, 50, 2), txt('=', 60, BLUE), box()], 18))
t.num('Cəmi tap.', [19], expr(['14', '+', '5', '=', BOX], 80))

# ============================================================ 33
t = T(33, '10-a tamamlamaqla toplama', 'Əvvəlcə 10-a tamamlayırıq: 8 + 5 = 8 + 2 + 3 = 10 + 3 = 13.',
      vstack([hstack([dots_frame(8, 2), dots_frame(0, 3)], 24), expr(['8', '+', '5', '=', '8', '+', '2', '+', '3', '=', '13'], 52)], 18))
t.num('10 olması üçün neçə lazımdır?', [4], vstack([dots_frame(6), expr(['6', '+', BOX, '=', '10'], 70)], 16))
t.num('10 olması üçün neçə lazımdır?', [3], vstack([dots_frame(7), expr(['7', '+', BOX, '=', '10'], 70)], 16))
t.num('Əvvəlcə 10-a tamamla. Boş xanaları doldur.', [3, 13], vstack([hstack([dots_frame(8, 2), dots_frame(0, 3)], 24), expr(['8', '+', '5', '=', '8', '+', '2', '+', BOX, '=', BOX], 54)], 18), disp='3, 13')
t.num('Əvvəlcə 10-a tamamla. Boş xanaları doldur.', [3, 13], vstack([hstack([dots_frame(9, 1), dots_frame(0, 3)], 24), expr(['9', '+', '4', '=', '9', '+', '1', '+', BOX, '=', BOX], 54)], 18), disp='3, 13')
t.num('Əvvəlcə 10-a tamamla. Boş xanaları doldur.', [2, 12], vstack([hstack([dots_frame(7, 3), dots_frame(0, 2)], 24), expr(['7', '+', '5', '=', '7', '+', '3', '+', BOX, '=', BOX], 54)], 18), disp='2, 12')
t.num('Dairələri say və cəmi yaz.', [12], vstack([hstack([dots_frame(8, 2), dots_frame(0, 2)], 24), expr(['8', '+', '4', '=', BOX], 64)], 16))
t.num('Dairələri say və cəmi yaz.', [17], vstack([hstack([dots_frame(9, 1), dots_frame(0, 7)], 24), expr(['9', '+', '8', '=', BOX], 64)], 16))
t.num('Cəmi tap.', [11], vstack([hstack([dots_frame(6, 4), dots_frame(0, 1)], 24), expr(['6', '+', '5', '=', BOX], 64)], 16))
t.num('Rəfə 10 kitab sığır. Lalənin 13 kitabı var. Aşağı rəfə neçə kitab qalar?', [3], hstack([frame(row('📕', 13, 54, 4, 5), 14), arrow(), vstack([frame(row('📕', 10, 40, 2), 8), frame(blank(420, 40), 8)], 6), arrow(), box()], 20))
t.num('Cəmi tap.', [13], expr(['7', '+', '6', '=', BOX], 80))

# ============================================================ 34
t = T(34, 'Toplamanın digər üsulları', 'Üç ədədi toplayanda əvvəlcə 10 düzəldirik: 6 + 4 = 10, 10 + 5 = 15.',
      vstack([expr(['6', '+', '5', '+', '4', '=', '15'], 60), hstack([dots_frame(6, 4), txt('+', 60, BLUE), dots_row(5, RED, 44)], 20)], 18))
for a in (6, 7, 8):
    t.num('İkiqatı tap.', [2 * a], vstack([hstack([dots_row(a, BLUE, 34, 6), dots_row(a, RED, 34, 6)], 30), expr([str(a), '+', str(a), '=', BOX], 70)], 18))
t.num('İkiqatdan 1 artıq. Boş xanaları doldur.', [13], expr(['6', '+', '7', '=', '6', '+', '6', '+', '1', '=', BOX], 56))
t.num('Əvvəlcə 10 düzəlt, sonra topla.', [14], expr(['7', '+', '4', '+', '3', '=', BOX], 72))
t.num('Əvvəlcə 10 düzəlt, sonra topla.', [18], expr(['6', '+', '8', '+', '4', '=', BOX], 72))
t.num('Cəmi tap.', [15], vstack([row('🖐️', 3, 90, 20), expr(['5', '+', '5', '+', '5', '=', BOX], 64)], 14))
t.num('Toplananların yerini dəyiş. Boş xanaları doldur.', [4, 16], expr(['4', '+', '12', '=', '12', '+', BOX, '=', BOX], 60), disp='4, 16')
t.num('Ədəd oxuna bax. Neçə addım atıldı? Qutuya yaz.', [4], vstack([numline(10, 20, 56, start=11, jumps=4, marks=(15,)), expr(['11', '+', BOX, '=', '15'], 60)], 16))
t.num('Zərlərdəki xalları topla.', [15], vstack([hstack([die(6), die(4), die(5)], 30), expr(['6', '+', '4', '+', '5', '=', BOX], 64)], 18))

# ============================================================ 35
t = T(35, 'Ədədlərin çıxılması', 'Çıxanda ədəd oxunda sola gedirik: 14 − 3 = 11.',
      vstack([numline(10, 20, 56, start=14, jumps=-3, marks=(11,)), expr(['14', '−', '3', '=', '11'], 60)], 10))
t.num('Şəkilə uyğun ifadəni yaz: azalan − çıxılan = fərq.', [14, 4, 10], vstack([crossed('🧊', 14, 4, 54, 7), expr([BOX, '−', BOX, '=', BOX], 60)], 20), disp='14 − 4 = 10')
for a, b in [(15, 5), (17, 10), (18, 8), (16, 3), (13, 10)]:
    t.num('Fərqi tap.', [a - b], expr([str(a), '−', str(b), '=', BOX], 80))
t.num('Ədəd oxunda 17 ədədindən 4 addım sola get. Fərqi yaz.', [13], vstack([numline(10, 20, 60, start=17), expr(['17', '−', '4', '=', BOX], 60)], 16))
t.num('Ədəd oxunda 19 ədədindən 5 addım sola get. Fərqi yaz.', [14], vstack([numline(10, 20, 60, start=19), expr(['19', '−', '5', '=', BOX], 60)], 16))
t.num('Çəmənlikdə 18 kəpənək var idi. 10 kəpənək uçdu. Neçə kəpənək qaldı?', [8], vstack([crossed('🦋', 18, 10, 50, 9), expr(['18', '−', '10', '=', BOX], 60)], 16))
t.num('Fərqi tap.', [13], expr(['15', '−', '2', '=', BOX], 80))

# ============================================================ 36
t = T(36, '10-a qədər azaltmaqla çıxma', 'Əvvəlcə 10-a qədər azaldırıq: 13 − 4 = 13 − 3 − 1 = 10 − 1 = 9.',
      vstack([hstack([dots_frame(10, cross=1), dots_frame(3, cross=3)], 24), expr(['13', '−', '4', '=', '13', '−', '3', '−', '1', '=', '9'], 50)], 18))
t.num('10 qalması üçün neçə çıxmaq lazımdır?', [2], expr(['12', '−', BOX, '=', '10'], 80))
t.num('10 qalması üçün neçə çıxmaq lazımdır?', [8], expr(['18', '−', BOX, '=', '10'], 80))
for a, b, c in [(13, 4, 3), (14, 5, 4), (15, 7, 5)]:
    t.num('Əvvəlcə 10-a qədər azalt. Boş xanaları doldur.', [b - c, a - b], expr([str(a), '−', str(b), '=', str(a), '−', str(c), '−', BOX, '=', BOX], 54), disp='%d, %d' % (b - c, a - b))
t.num('Dairələrə bax və fərqi tap.', [9], vstack([hstack([dots_frame(9, 1, cross=1), dots_frame(1, cross=1)], 24), expr(['11', '−', '2', '=', BOX], 64)], 16))
t.num('Fərqi tap.', [7], expr(['12', '−', '5', '=', BOX], 80))
t.num('Fərqi tap.', [9], expr(['16', '−', '7', '=', BOX], 80))
t.num('Yarışa 11 velosipedçi başladı. 3 velosipedçi dayandı. Neçə velosipedçi qaldı?', [8], vstack([crossed('🚴', 11, 3, 56, 11), expr(['11', '−', '3', '=', BOX], 60)], 16))
t.num('Məchul çıxılanı tap.', [8], expr(['15', '−', BOX, '=', '7'], 80))


# ============================================================ 37
def triple(whole, a, b, s=48):
    def circ(v, col):
        im, d = vec(110, 110)
        d.ellipse([4 * S, 4 * S, 106 * S, 106 * S], fill=col, outline=INK, width=4 * S)
        im = done(im)
        if v == 'None':
            return box(110, 110, BLUE, 5, 55)
        tt = txt(v, s)
        im.alpha_composite(tt, ((110 - tt.width) // 2, (110 - tt.height) // 2))
        return im
    return vstack([circ(str(whole), (255, 224, 130)), hstack([circ(str(a), (187, 222, 251)), circ(str(b), (187, 222, 251))], 60)], 14)


def family(w, a, b):
    return vstack([expr([str(a), '+', str(b), '=', BOX], 46), expr([str(b), '+', str(a), '=', BOX], 46), expr([str(w), '−', str(a), '=', BOX], 46), expr([str(w), '−', str(b), '=', BOX], 46)], 12, 'left')


t = T(37, 'Toplama və çıxmanın əlaqəsi', 'Ədəd üçlüyü: 9 + 7 = 16, 7 + 9 = 16, 16 − 9 = 7, 16 − 7 = 9.',
      hstack([triple(16, 9, 7), vstack([expr(['9', '+', '7', '=', '16'], 44), expr(['7', '+', '9', '=', '16'], 44), expr(['16', '−', '9', '=', '7'], 44), expr(['16', '−', '7', '=', '9'], 44)], 10, 'left')], 50))
for w, a, b in [(15, 8, 7), (13, 9, 4), (17, 10, 7)]:
    t.num('Ədəd üçlüyünə bax. Dörd ifadəni tamamla.', [w, w, b, a], hstack([triple(w, a, b), family(w, a, b)], 50), disp='%d, %d, %d, %d' % (w, w, b, a))
t.num('Toplamaya bax və çıxmanı tamamla.', [9], vstack([expr(['9', '+', '6', '=', '15'], 60), expr(['15', '−', '6', '=', BOX], 60)], 16))
t.num('Toplamaya bax və çıxmanı tamamla.', [5], vstack([expr(['8', '+', '5', '=', '13'], 60), expr(['13', '−', '8', '=', BOX], 60)], 16))
t.num('Məchul toplananı tap.', [6], expr(['9', '+', BOX, '=', '15'], 80))
t.num('Məchul çıxılanı tap.', [7], expr(['17', '−', BOX, '=', '10'], 80))
t.num('Tam 14. Bir hissə 6. O biri hissəni yaz.', [8], hstack([triple(14, 6, None), arrow(), box()], 30))
t.num('Lalə 7 çiçəyi Aynura verdi, 9 çiçəyi vazaya qoydu. Neçə çiçək dərmişdi?', [16], hstack([group('🌷', 7, 50, 4), txt('+', 60, BLUE), group('🌷', 9, 50, 5), txt('=', 60, BLUE), box()], 18))
t.num('Tam 18. Bir hissə 9. O biri hissəni yaz.', [9], hstack([triple(18, 9, None), arrow(), box()], 30))

# ============================================================ 38
t = T(38, '100-ə qədər sayma', 'Yüzlük kartda 1-dən 100-ə qədər ədədlər var. On-on sayırıq: 10, 20, 30...',
      hundred(1, 10, (), 52))


def seq(tokens, size=60):
    return hstack([box(int(size * 1.5), int(size * 1.35)) if v is BOX else chip(str(v), size - 6, WHITE, INK, GREY) for v in tokens], 14)


t.num('İki-iki say. Boş xanalara yaz.', [8, 12], seq([2, 4, 6, BOX, 10, BOX]))
t.num('Beş-beş say. Boş xanalara yaz.', [20, 30], seq([5, 10, 15, BOX, 25, BOX]))
t.num('On-on say. Boş xanalara yaz.', [30, 50], seq([10, 20, BOX, 40, BOX, 60]))
t.num('Yüzlük karta bax. Boş xanalara yaz.', [44, 47], hundred(41, 2, (44, 47)))
t.num('53 ədədinin qonşularını yaz.', [52, 54], seq([BOX, 53, BOX], 70), disp='52 və 54')
t.num('Yüzlük kartda 53-ün üstündə və altında hansı ədədlər var?', [43, 63], hundred(41, 3, (43, 63)), disp='43 və 63')
t.num('İrəli say. Boş xanalara yaz.', [69, 70], seq([67, 68, BOX, BOX, 71]))
t.num('Geri say. Boş xanalara yaz.', [89, 87], seq([90, BOX, 88, BOX, 86]))
t.num('Samir hər gün 5 səhifə oxuyur. 4 gündə neçə səhifə oxuyar? Beş-beş say.', [20], hstack([hstack([vstack([em('📖', 80), txt('5', 44)], 4) for _ in range(4)], 24), arrow(), box()], 24))
t.choice('Ən böyük ədədi dairəyə al.', ['38', '83', '58', '80'], 1)

# ============================================================ 39
t = T(39, 'Onluq və təklik', 'Ədədin sağdakı rəqəmi təklik, soldakı rəqəmi onluqdur: 47 = 4 onluq və 7 təklik.',
      vstack([tens_ones(4, 7, 120), hstack([txt('47', 80), txt('=', 64, BLUE), txt('4 onluq, 7 təklik', 44, BLUE)], 20)], 20))


def onluq_slots():
    return hstack([box(), txt('onluq', 40, BLUE), box(), txt('təklik', 40, BLUE)], 16)


for a, b in [(3, 5), (5, 2), (2, 8)]:
    t.num('Neçə onluq və neçə təklik var? Yaz.', [a, b], vstack([tens_ones(a, b, 110), onluq_slots()], 20), disp='%d onluq, %d təklik' % (a, b))
for a, b in [(4, 6), (6, 1), (3, 0)]:
    t.num('Çöpləri say. Bir dəstə – 10 çöp. Ədədi yaz.', [10 * a + b], hstack([tens_ones(a, b, 110), arrow(), box()], 24))
t.num('Anar yumurtaları 10-luq qutulara yığdı. 3 qutu doldu, 8 yumurta artıq qaldı. Neçə yumurta var idi?', [38], hstack([vstack([frame(row('🥚', 10, 36, 2), 6) for _ in range(3)], 8), frame(row('🥚', 8, 36, 2, 4), 6), arrow(), box()], 20))
t.num('Ədədi onluq və təkliyə ayır.', [7, 2], hstack([txt('72', 80), txt('=', 64, BLUE), onluq_slots()], 18), disp='7 onluq, 2 təklik')
t.choice('5 onluq və 3 təklik hansı ədəddir? Dairəyə al.', ['35', '53', '8'], 1, stem=tens_ones(5, 3, 90))
t.choice('Hansı şəkil 24 ədədini göstərir? Dairəyə al.', [tens_ones(2, 4, 80), tens_ones(4, 2, 80), tens_ones(2, 2, 80)], 0, stem=chip('24', 60))

# ============================================================ 40
t = T(40, 'Qəpik, manat', '1 manat 100 qəpikdir. Sikkələr: 1, 3, 5, 10, 20 və 50 qəpik.',
      vstack([hstack([coin(v, 100) for v in (1, 3, 5, 10, 20, 50)], 16), hstack([note(v, 170, 90) for v in (1, 5, 10, 20)], 16)], 24))


def coins(vals, s=100):
    return hstack([coin(v, s) for v in vals], 14)


for vals in [(10, 5), (20, 10, 3), (10, 10, 3), (50, 20, 1)]:
    t.num('Sikkələri topla. Cəmi neçə qəpikdir?', [sum(vals)], hstack([coins(vals), arrow(), box(), txt('qəp', 44, BLUE)], 20), disp='%d qəpik' % sum(vals))
t.choice('Hansı qrupda pul çoxdur? Dairəyə al.', [frame(coins((5, 5, 5), 80), 12), frame(coins((20,), 80), 12)], 1, disp='2-ci qrup (20 qəpik)')
t.num('8 qəpik düzəlt. Hansı sikkə çatmır?', [3], hstack([coin(5), txt('+', 64, BLUE), box(), txt('=', 64, BLUE), txt('8 qəp', 56)], 16))
t.num('11 qəpik düzəlt. Hansı sikkə çatmır?', [1], hstack([coin(10), txt('+', 64, BLUE), box(), txt('=', 64, BLUE), txt('11 qəp', 56)], 16))
t.num('Əskinasları topla. Cəmi neçə manatdır?', [16], hstack([note(10, 180, 95), note(5, 180, 95), note(1, 180, 95), arrow(), box(), txt('man', 44, BLUE)], 14), disp='16 manat')
t.choice('20 qəpikliyi dairəyə al.', [coin(10, 110), coin(20, 110), coin(50, 110)], 1, disp='20 qəpik')
t.num('Samirdə üç 5 qəpiklik var. Cəmi neçə qəpikdir?', [15], hstack([coins((5, 5, 5)), arrow(), box(), txt('qəp', 44, BLUE)], 20), disp='15 qəpik')

# ============================================================ 41
t = T(41, 'Alış-veriş', 'Malın qiyməti üstündə yazılır. Çox pul versən, qalığı qaytarırlar.',
      hstack([priced('🍦', '7 qəp'), txt('←', 70, BLUE), coin(10, 100), arrow(), coins((3,), 100)], 24))
t.num('Dondurma 10 qəpik, alma 6 qəpikdir. İkisi birlikdə neçə qəpikdir?', [16], hstack([priced('🍦', '10 qəp'), txt('+', 64, BLUE), priced('🍎', '6 qəp'), txt('=', 64, BLUE), box(), txt('qəp', 44, BLUE)], 18), disp='16 qəpik')
t.num('Alma 6 qəpik, armud 7 qəpikdir. 2 alma və 1 armud neçə qəpikdir?', [19], hstack([priced('🍎', '6 qəp', 90), priced('🍎', '6 qəp', 90), priced('🍐', '7 qəp', 90), txt('=', 64, BLUE), box(), txt('qəp', 44, BLUE)], 18), disp='19 qəpik')
t.num('Şokolad 7 qəpikdir. Lalə 10 qəpik verdi. Ona neçə qəpik qaytarılar?', [3], hstack([priced('🍫', '7 qəp'), coin(10, 100), arrow(), box(), txt('qəp', 44, BLUE)], 22), disp='3 qəpik')
t.num('Dəftər 16 qəpikdir. Lalə 20 qəpik verdi. Ona neçə qəpik qaytarılar?', [4], hstack([priced('📒', '16 qəp'), coin(20, 100), arrow(), box(), txt('qəp', 44, BLUE)], 22), disp='4 qəpik')
t.choice('Səbinənin 15 qəpiyi var. Hansını ala bilər? Dairəyə al.', [priced('🧸', '18 qəp'), priced('🎈', '12 qəp'), priced('🪁', '20 qəp')], 1, stem=coins((10, 5)), disp='şar (12 qəpik)')
t.choice('Ən ucuz dondurmanı dairəyə al.', [priced('🍦', '9 qəp'), priced('🍨', '8 qəp'), priced('🍧', '10 qəp')], 1, disp='8 qəpik')
t.num('Kitab 8 manatdır. Anar 3 manat, Samir 3 manat verdi. Səbinə neçə manat əlavə etməlidir?', [2], hstack([priced('📘', '8 man'), txt('=', 64, BLUE), txt('3', 60), txt('+', 60, BLUE), txt('3', 60), txt('+', 60, BLUE), box()], 16), disp='2 manat')
t.num('Top 12 manat, kukla 7 manatdır. Top kukladan neçə manat bahadır?', [5], hstack([priced('⚽', '12 man'), priced('🪆', '7 man'), arrow(), box(), txt('man', 44, BLUE)], 22), disp='5 manat')
t.num('Ayaqqabı 19 manatdır. Elxanın 6 manatı var. Anası neçə manat əlavə etməlidir?', [13], hstack([priced('👟', '19 man'), note(5, 150, 80), note(1, 150, 80), arrow(), box(), txt('man', 44, BLUE)], 18), disp='13 manat')
t.num('Qələm 5 qəpikdir. 3 qələm neçə qəpikdir?', [15], hstack([priced('✏️', '5 qəp', 80), priced('✏️', '5 qəp', 80), priced('✏️', '5 qəp', 80), txt('=', 64, BLUE), box(), txt('qəp', 44, BLUE)], 16), disp='15 qəpik')

# ============================================================ 42
U = 52
t = T(42, 'Uzun, qısa', 'Uzunluğu müqayisə edirik: uzun – qısa, hündür – alçaq. Kublarla ölçə bilərik.',
      vstack([hstack([pencil(7, U, (66, 165, 245)), txt('uzun', 34, BLUE)], 16), hstack([pencil(4, U, (239, 83, 80)), txt('qısa', 34, BLUE)], 16)], 16, 'left'))
t.choice('Uzun karandaşı dairəyə al.', [pencil(4, 44, (102, 187, 106)), pencil(7, 44, (66, 165, 245))], 1, disp='2-ci karandaş')
t.choice('Qısa lenti dairəyə al.', [strip(6, 40, RED), strip(3, 40, PURPLE), strip(5, 40, GREEN)], 1)
t.choice('Hündür ağacı dairəyə al.', [em('🌲', 90), em('🌲', 170), em('🌲', 120)], 1)
t.choice('Alçaq evi dairəyə al.', [em('🏠', 150), em('🏠', 80), em('🏠', 120)], 1)
t.num('Karandaş neçə kub uzunluğundadır? Say və yaz.', [7], hstack([vstack([pencil(7, U, (255, 202, 40)), cubes(7, U)], 6, 'left'), arrow(), box()], 24))
t.num('Diş fırçası neçə kub uzunluğundadır? Say və yaz.', [6], hstack([vstack([hstack([strip(4.4, U, (77, 182, 172), 24), strip(1.6, U, WHITE, 40)], 0), cubes(6, U, (171, 71, 188))], 6, 'left'), arrow(), box()], 24))
t.num('Göy karandaş 5 kub, qırmızı karandaş 7 kubdur. Qırmızı karandaş neçə kub uzundur?', [2], hstack([vstack([pencil(5, 44, (66, 165, 245)), cubes(5, 44), pencil(7, 44, (239, 83, 80)), cubes(7, 44)], 4, 'left'), arrow(), box()], 24))
t.choice('Zolaqları uzundan qısaya düz: ardıcıl toxun.', [strip(4, 40, GREEN), strip(7, 40, RED), strip(2, 40, BLUE)], [1, 0, 2], mode='order', hint='Əvvəlcə ən uzun zolağa, sonra ortaya, sonra ən qısaya toxun.', disp='qırmızı, yaşıl, göy')
t.choice('Ən qısa karandaşı dairəyə al.', [pencil(6, 40, (171, 71, 188)), pencil(3, 40, (171, 71, 188)), pencil(5, 40, (171, 71, 188))], 1)
t.num('Lent 9 kubdur. 4 kubunu kəsdilər. Neçə kub qaldı?', [5], hstack([vstack([strip(9, 46, PINK), cubes(9, 46)], 6, 'left'), arrow(), expr(['9', '−', '4', '=', BOX], 56)], 20))

# ============================================================ 43
CM = 56
t = T(43, 'Santimetr', 'Uzunluğu santimetrlə ölçürük. Xətkeşin 0-ını əşyanın ucuna qoyuruq.',
      hstack([on_ruler(pencil(6, CM, (255, 202, 40)), 10, CM), arrow(), txt('6 sm', 64, BLUE)], 20))
for L, col in [(5, RED), (8, BLUE), (3, GREEN), (10, PURPLE), (6, ORANGE)]:
    t.num('Xətkeşlə ölç. Zolaq neçə santimetrdir?', [L], hstack([on_ruler(strip(L, CM, col), 12, CM), box(), txt('sm', 44, BLUE)], 14), disp='%d sm' % L)
t.num('8 sm və 5 sm zolağı uc-uca qoydular. Cəmi neçə santimetr oldu?', [13], vstack([hstack([label(strip(8, 40, RED), '8 sm'), label(strip(5, 40, BLUE), '5 sm')], 0, 'bottom'), hstack([expr(['8', '+', '5', '=', BOX], 56), txt('sm', 44, BLUE)], 12)], 16), disp='13 sm')
t.num('Lent 12 sm idi. 4 sm kəsdilər. Neçə santimetr qaldı?', [8], vstack([label(strip(12, 40, PINK), '12 sm'), hstack([expr(['12', '−', '4', '=', BOX], 56), txt('sm', 44, BLUE)], 12)], 16), disp='8 sm')
t.choice('Hansı zolaq 4 santimetrdir? Dairəyə al.', [strip(6, 40, RED), strip(4, 40, BLUE), strip(3, 40, GREEN)], 1, stem=on_ruler(vstack([strip(6, CM, RED, 26), strip(4, CM, BLUE, 26), strip(3, CM, GREEN, 26)], 8, 'left'), 8, CM), disp='göy zolaq')
t.num('Qırmızı zolaq 7 sm, göy zolaq 4 sm-dir. Qırmızı zolaq neçə santimetr uzundur?', [3], hstack([vstack([label(strip(7, 40, RED), '7 sm'), label(strip(4, 40, BLUE), '4 sm')], 10, 'left'), arrow(), box(), txt('sm', 44, BLUE)], 18), disp='3 sm')
t.num('Karandaş neçə santimetrdir? Xətkeşlə ölç.', [9], hstack([on_ruler(pencil(9, CM, (102, 187, 106)), 12, CM), box(), txt('sm', 44, BLUE)], 14), disp='9 sm')

# ============================================================ 44
t = T(44, 'Ağır, yüngül', 'Tərəzinin ağır tərəfi aşağı enir. Kütləni kiloqramla ölçürük.',
      hstack([label(scale([em('🍉', 90)], [em('🍎', 50)], -1, 480), 'qarpız ağırdır'), label(scale([weight(2, 70)], [em('🍍', 80)], 0, 480), 'ananas 2 kq')], 30, 'bottom'))
t.choice('Ağır olanı dairəyə al.', [em('🍉', 100), em('🍓', 100)], 0, stem=scale([em('🍉', 90)], [em('🍓', 50)], -1, 480), disp='qarpız')
t.choice('Yüngül olanı dairəyə al.', [em('🧸', 100), em('📚', 100)], 0, stem=scale([em('🧸', 80)], [em('📚', 90)], 1, 480), disp='ayıcıq')
t.choice('Ayı 6 kub, tülkü 4 kub ağırlığındadır. Ağır olanı dairəyə al.', [em('🐻', 100), em('🦊', 100)], 0, stem=hstack([vstack([em('🐻', 110), cubes(6, 44)], 10), vstack([em('🦊', 110), cubes(4, 44)], 10)], 60, 'bottom'), disp='ayı')
t.num('Tərəzi bərabərdir. Qarpız neçə kiloqramdır?', [5], hstack([scale([em('🍉', 100)], [weight(2), weight(3)], 0, 520), box(), txt('kq', 44, BLUE)], 14), disp='5 kq')
t.num('Tərəzi bərabərdir. Kələm neçə kiloqramdır?', [3], hstack([scale([em('🥬', 90)], [weight(2), weight(1)], 0, 520), box(), txt('kq', 44, BLUE)], 14), disp='3 kq')
t.num('Bir səbətdə 5 kq, o birində 3 kq alma var. Cəmi neçə kiloqramdır?', [8], hstack([label(em('🧺', 110), '5 kq', 34), label(em('🧺', 110), '3 kq', 34), arrow(), box(), txt('kq', 44, BLUE)], 20), disp='8 kq')
t.num('Yaşıl almalar 7 kq, sarı almalar 4 kq-dır. Yaşıl almalar neçə kiloqram ağırdır?', [3], hstack([label(row('🍏', 3, 60, 4), '7 kq', 34), label(row('🍋', 2, 60, 4), '4 kq', 34), arrow(), box(), txt('kq', 44, BLUE)], 24), disp='3 kq')
t.num('Tərəzi bərabər olsun deyə sağ tərəfə neçə kiloqram qoymaq lazımdır?', [2], hstack([scale([weight(5)], [weight(3), box(80, 80)], -1, 520), box(), txt('kq', 44, BLUE)], 14), disp='2 kq')
t.choice('Ən ağır qutunu dairəyə al.', [label(em('📦', 100), '3 kq', 36, INK), label(em('📦', 100), '7 kq', 36, INK), label(em('📦', 100), '5 kq', 36, INK)], 1, disp='7 kq')
t.choice('Ən yüngül qutunu dairəyə al.', [label(em('🎁', 100), '6 kq', 36, INK), label(em('🎁', 100), '4 kq', 36, INK), label(em('🎁', 100), '2 kq', 36, INK)], 2, disp='2 kq')

# ============================================================ 45
t = T(45, 'Tutum', 'Qabın tutumunu suqabı və ya litrlə ölçürük. Çox su tutan qabın tutumu böyükdür.',
      hstack([vstack([bucket(0.8, (255, 202, 40)), hstack([glass(1, 40, 60) for _ in range(4)], 6)], 10), vstack([bucket(1.1, (239, 83, 80)), hstack([glass(1, 40, 60) for _ in range(6)], 6)], 10)], 50, 'bottom'))
t.choice('Ən çox su tutan vedrəni dairəyə al.', [bucket(0.7, B3), bucket(1.2, B3), bucket(0.95, B3)], 1)
t.choice('Ən az su tutan qazanı dairəyə al.', [pot(0.9), pot(0.6), pot(1.1)], 1)
t.choice('Dolu stəkanı dairəyə al.', [glass(0.3, 90, 130), glass(0.0, 90, 130), glass(0.95, 90, 130)], 2)
t.num('Sarı vedrə 4, qırmızı vedrə 6 suqabı su tutur. Qırmızı vedrə neçə suqabı çox tutur?', [2], hstack([label(bucket(0.8, (255, 202, 40)), '4', 40, INK), label(bucket(1.0, (239, 83, 80)), '6', 40, INK), arrow(), box()], 24))
t.num('Qazan neçə suqabı su tutur? Say və yaz.', [5], hstack([pot(1.0), txt('=', 64, BLUE), hstack([glass(1, 50, 74) for _ in range(5)], 10), arrow(), box()], 18))
t.num('Bidonda 10 litr süd var idi. 7 litrini boşaltdılar. Neçə litr qaldı?', [3], hstack([em('🥛', 120), expr(['10', '−', '7', '=', BOX], 60), txt('l', 48, BLUE)], 20), disp='3 litr')
t.num('Vedrəyə 5 litr su tökdülər, sonra daha 5 litr. Cəmi neçə litr oldu?', [10], hstack([bucket(0.9, B3), expr(['5', '+', '5', '=', BOX], 60), txt('l', 48, BLUE)], 20), disp='10 litr')
t.num('Hər şüşədə 2 litr su var. 4 şüşədə neçə litr var? İki-iki say.', [8], hstack([hstack([label(em('🍶', 90), '2 l', 32, INK) for _ in range(4)], 18), arrow(), box(), txt('l', 48, BLUE)], 20), disp='8 litr')
t.num('Samovar 12 litrdir. İçinə 10 litr su tökdülər. Daha neçə litr lazımdır?', [2], hstack([label(em('🫖', 120), '12 l', 34, INK), expr(['10', '+', BOX, '=', '12'], 60), txt('l', 48, BLUE)], 20), disp='2 litr')
t.choice('Stəkanları doludan boşa düz: ardıcıl toxun.', [glass(0.5, 80, 120), glass(0.95, 80, 120), glass(0.15, 80, 120)], [1, 0, 2], mode='order', hint='Əvvəlcə ən dolu stəkana, sonra ortadakına, sonra ən boş stəkana toxun.', disp='dolu, yarı, az')

# ============================================================ 46
DAYS = ['B.e.', 'Ç.a.', 'Ç.', 'C.a.', 'C.', 'Ş.', 'B.']
t = T(46, 'Gün, həftə, ay', 'Günün vaxtları: səhər, günorta, axşam, gecə. Həftədə 7 gün, ildə 12 ay və 4 fəsil var.',
      vstack([hstack([label(em('🌅', 90), 'səhər', 28), label(em('☀️', 90), 'günorta', 28), label(em('🌇', 90), 'axşam', 28), label(em('🌙', 90), 'gecə', 28)], 30, 'bottom'),
              hstack([label(em('🌸', 80), 'yaz', 28), label(em('🏖️', 80), 'yay', 28), label(em('🍂', 80), 'payız', 28), label(em('⛄', 80), 'qış', 28)], 30, 'bottom')], 24))
t.choice('Səhəri göstərən şəkli dairəyə al.', [em('🌙', 110), em('🌅', 110), em('🌇', 110)], 1, disp='səhər')
t.choice('Gecəni göstərən şəkli dairəyə al.', [em('☀️', 110), em('🌅', 110), em('🌙', 110)], 2, disp='gecə')
t.choice('Günün vaxtlarını sıra ilə düz: səhər, günorta, axşam. Ardıcıl toxun.', [em('🌇', 110), em('🌅', 110), em('☀️', 110)], [1, 2, 0], mode='order', hint='Əvvəlcə səhərə, sonra günortaya, sonra axşama toxun.', disp='səhər, günorta, axşam')
t.num('Həftədə neçə gün var? Say və yaz.', [7], hstack([hstack([chip(d_, 30, (255, 243, 224), INK, ORANGE) for d_ in DAYS], 8), arrow(), box()], 16))
t.num('İldə neçə ay var? Say və yaz.', [12], hstack([grid([em('🗓️', 60) for _ in range(12)], 6, 10), arrow(), box()], 20))
t.num('İldə neçə fəsil var? Say və yaz.', [4], hstack([em('🌸', 90), em('🏖️', 90), em('🍂', 90), em('⛄', 90), arrow(), box()], 20))
t.choice('Qış fəslini göstərən şəkli dairəyə al.', [em('🌸', 110), em('⛄', 110), em('🍂', 110)], 1, disp='qış')
t.choice('Yay fəslini göstərən şəkli dairəyə al.', [em('🏖️', 110), em('🍂', 110), em('⛄', 110)], 0, disp='yay')
t.num('Aynur həftədə 4 gün rəsm dərnəyinə gedir. Həftədə neçə gün getmir?', [3], vstack([hstack([chip(d_, 28, (200, 230, 201) if k in (0, 1, 3, 5) else WHITE, INK, GREEN if k in (0, 1, 3, 5) else GREY) for k, d_ in enumerate(DAYS)], 6), expr(['7', '−', '4', '=', BOX], 54)], 20))
t.num('Hər fəsildə 3 ay var. 2 fəsildə neçə ay var?', [6], hstack([vstack([em('🌸', 70), row('🗓️', 3, 46, 4)], 6), vstack([em('🏖️', 70), row('🗓️', 3, 46, 4)], 6), arrow(), box()], 24))

# ============================================================ 47
t = T(47, 'Saat', 'Uzun əqrəb 12-nin üstündə olanda saat tamamdır. Bu saat 7-dir.',
      hstack([clock(7, 240), vstack([txt('saat 7', 60), txt('qısa əqrəb – 7', 30, RED), txt('uzun əqrəb – 12', 30, BLUE)], 10, 'left')], 40))
for hh in (3, 8, 11, 6):
    t.num('Saat neçədir? Qutuya yaz.', [hh], hstack([clock(hh, 230), arrow(), box()], 24), disp='saat %d' % hh)
t.choice('Saat 2-ni göstərən saatı dairəyə al.', [clock(10, 150), clock(2, 150), clock(5, 150)], 1, disp='saat 2')
t.choice('Saat 9-u göstərən saatı dairəyə al.', [clock(9, 150), clock(3, 150), clock(12, 150)], 0, disp='saat 9')
t.num('İndi saat 5-dir. 3 saat sonra saat neçə olar?', [8], hstack([clock(5, 200), expr(['5', '+', '3', '=', BOX], 56)], 24), disp='saat 8')
t.num('İndi saat 10-dur. 2 saat əvvəl saat neçə idi?', [8], hstack([clock(10, 200), expr(['10', '−', '2', '=', BOX], 56)], 24), disp='saat 8')
t.num('Qatar saat 8-də yola düşdü, saat 12-də çatdı. Yolda neçə saat oldu?', [4], vstack([hstack([em('🚆', 110), clock(8, 190), arrow(), clock(12, 190)], 20), expr(['12', '−', '8', '=', BOX], 60)], 16))
t.num('Dərnək saat 5-də başlayır, saat 7-də bitir. Neçə saat davam edir?', [2], hstack([clock(5, 180), arrow(), clock(7, 180), expr(['7', '−', '5', '=', BOX], 54)], 18))

# ============================================================ 48
FR = [('🍒', 5), ('🍑', 3), ('🍓', 6)]


def picto(rows, s=56):
    return table([[em(e, 64), row(e, n, s, 6)] for e, n in rows], 84)


t = T(48, 'Cədvəl, piktoqram', 'Piktoqramda hər şəkil bir əşyanı göstərir. Cədvəldə saymaq üçün cizgi qoyuruq.',
      hstack([picto([('🍎', 4), ('🍐', 2)], 46), table([[em('⚽', 54), tally(7, 56)], [em('🏀', 54), tally(3, 56)]], 76)], 40))
pc = picto(FR)
t.num('Piktoqrama bax. Neçə çiyələk var?', [6], hstack([pc, arrow(), box()], 20))
t.num('Piktoqrama bax. Neçə albalı var?', [5], hstack([pc, arrow(), box()], 20))
t.num('Piktoqrama bax. Çiyələk ərikdən neçə çoxdur?', [3], vstack([pc, expr(['6', '−', '3', '=', BOX], 56)], 16))
t.choice('Hansı meyvə ən çoxdur? Dairəyə al.', [em('🍒', 100), em('🍑', 100), em('🍓', 100)], 2, stem=pc, disp='çiyələk')
t.choice('Hansı meyvə ən azdır? Dairəyə al.', [em('🍒', 100), em('🍑', 100), em('🍓', 100)], 1, stem=pc, disp='ərik')
tb = table([[em('⚽', 64), tally(7)], [em('🏖️', 64), tally(4)], [em('🎠', 64), tally(3)]], 90)
t.num('Cədvələ bax. Neçə uşaq futbol oynayır? Cizgiləri say.', [7], hstack([tb, arrow(), box()], 20))
t.num('Cədvələ bax. Neçə uşaq qum meydançasındadır?', [4], hstack([tb, arrow(), box()], 20))
t.num('Cədvələ bax. Cəmi neçə uşaq var?', [14], vstack([tb, expr(['7', '+', '4', '+', '3', '=', BOX], 54)], 16))
fish = picto([('🐟', 4), ('🐠', 6), ('🐡', 2)])
t.choice('Hansı balıq ən çoxdur? Dairəyə al.', [em('🐟', 100), em('🐠', 100), em('🐡', 100)], 1, stem=fish, disp='zolaqlı balıq')
t.num('Zolaqlı balıq kirpi balıqdan neçə çoxdur?', [4], vstack([fish, expr(['6', '−', '2', '=', BOX], 56)], 16))

# ============================================================ 49
KIDS = [('👦', 'Anar', 5), ('👧', 'Lalə', 7), ('🧒', 'Samir', 3), ('👱', 'Elxan', 0)]
KC = [BLUE, PINK, ORANGE, GREEN]
t = T(49, 'Diaqram', 'Diaqramda sütun nə qədər hündürdürsə, say o qədər çoxdur.',
      bars([(em('🍎', 54), 6), (em('🍌', 54), 4), (em('🍇', 54), 8)], 10, 30, colors=[RED, YELLOW, PURPLE]))
kd = bars([(label(em(e, 60), nm, 24, INK), v) for e, nm, v in KIDS], 8, 38, colors=KC)
t.num('Diaqrama bax. Lalə neçə top saldı?', [7], hstack([kd, arrow(), box()], 20))
t.num('Diaqrama bax. Anar neçə top saldı?', [5], hstack([kd, arrow(), box()], 20))
t.choice('Kim ən çox top saldı? Dairəyə al.', [em(e, 100) for e, _, _ in KIDS], 1, stem=kd, disp='Lalə')
t.choice('Kim heç top sala bilmədi? Dairəyə al.', [em(e, 100) for e, _, _ in KIDS], 3, stem=kd, disp='Elxan')
t.num('Uşaqlar cəmi neçə top saldılar?', [15], vstack([kd, expr(['5', '+', '7', '+', '3', '+', '0', '=', BOX], 50)], 16))
fd = bars([(em('🍎', 56), 6), (em('🍌', 56), 4), (em('🍇', 56), 8), (em('🍐', 56), 2)], 10, 32, colors=[RED, YELLOW, PURPLE, GREEN])
t.num('Diaqrama bax. Neçə uşaq üzümü sevir?', [8], hstack([fd, arrow(), box()], 20))
t.choice('Ən çox sevilən meyvəni dairəyə al.', [em('🍎', 100), em('🍌', 100), em('🍇', 100), em('🍐', 100)], 2, stem=fd, disp='üzüm')
t.num('Almanı sevənlər armudu sevənlərdən neçə çoxdur?', [4], vstack([fd, expr(['6', '−', '2', '=', BOX], 56)], 16))
t.num('Bananı və armudu sevənlər birlikdə neçədir?', [6], vstack([fd, expr(['4', '+', '2', '=', BOX], 56)], 16))
t.choice('Hansı diaqram 3 alma və 5 armud göstərir? Dairəyə al.',
         [bars([(em('🍎', 40), 3), (em('🍐', 40), 5)], 6, 22, 50, colors=[RED, GREEN]), bars([(em('🍎', 40), 5), (em('🍐', 40), 3)], 6, 22, 50, colors=[RED, GREEN]), bars([(em('🍎', 40), 3), (em('🍐', 40), 3)], 6, 22, 50, colors=[RED, GREEN])], 0,
         stem=hstack([row('🍎', 3, 60, 6), row('🍐', 5, 60, 6)], 40))

# ------------------------------------------------------------------ output
for tp in TOPICS:
    if len(tp.problems) != 10: print('COUNT', tp.n, len(tp.problems))
os.makedirs(os.path.join(OUT, 'data'), exist_ok=True)
json.dump({'topics': [tp.d for tp in TOPICS]}, open(os.path.join(OUT, 'data/topics.json'), 'w'), ensure_ascii=False)
json.dump(VOICE, open(os.path.join(OUT, 'data/voice.json'), 'w'), ensure_ascii=False, indent=0)
print('topics', len(TOPICS), 'voice', len(VOICE))
