"""Yoxlama testi (2-2): 20 tapşırıq. Writes OUT/test_items.json (images as data URIs, audio as text ids)."""
import base64, hashlib, io, json, os, sys
from draw import *
from draw2 import *

OUT = sys.argv[1]
VOICE = {}


def aid(text):
    h = hashlib.md5(text.encode()).hexdigest()[:10]
    VOICE[h] = text
    return h


def uri(im, maxw=900, margin=18):
    o = Image.new('RGB', (im.width + 2 * margin, im.height + 2 * margin), WHITE)
    o.paste(im, (margin, margin), im)
    if o.width > maxw:
        o = o.resize((maxw, round(o.height * maxw / o.width)), Image.LANCZOS)
    b = io.BytesIO()
    o.save(b, 'WEBP', quality=80, method=6)
    return 'data:image/webp;base64,' + base64.b64encode(b.getvalue()).decode()


N = {'s': 'num'}
ITEMS = []


def it(area, skill, ins, hint, disp, img=None, options=None, answer=None, tokens=None, mode='num', **kw):
    d = {'area': area, 'skill': skill, 'ins': ins, 'img': uri(img) if img is not None else None,
         'kind': 'choice' if options else 'slots', 'options': [uri(o, 500, 12) for o in options] if options else None,
         'prefix': None, 'tokens': tokens, 'answer': answer, 'mode': mode, 'disp': disp, 'hint': hint, 'audio': aid(ins)}
    d.update(kw)
    ITEMS.append(d)





def triple(whole, a, b, size=64):
    """ədəd üçlüyü: yuxarıda tam, aşağıda iki hissə; None = boş xana"""
    def cell(v, w, fill):
        return frame(box(int(size * 1.4), int(size * 1.2)) if v is None else txt(str(v), size, INK), 10, ORANGE, 4, 14, fill)
    top = cell(whole, 0, (255, 236, 179))
    low = hstack([cell(a, 0, (255, 248, 225)), cell(b, 0, (255, 248, 225))], 8)
    return vstack([top, low], 6)


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


def coins(vals, size=90):
    return hstack([coin(v, size) for v in vals], 10)


def notes(vals, w=170, h=88):
    return hstack([note(v, w, h) for v in vals], 10)


def tab(rows, size=34):
    return table([[txt(str(c), size, INK) for c in r] for r in rows], int(size * 2))


B3 = (66, 165, 245); R3 = (239, 83, 80); G3 = (102, 187, 106); O3 = (255, 167, 38); P3 = (171, 71, 188); Y3 = (255, 213, 79)


def ch(v, size=60):
    return chip(v, size, WHITE, INK, GREY)


# A. Çıxma (onluğun ayrılması)
it('A', 'İkirəqəmli − birrəqəmli', 'Fərqi tapın.', 'Təkliklər çatmır: 1 onluq ayırın. 14 − 6 = 8.', '28',
   img=tens_ones(3, 4, 90), tokens=[34, '−', 6, '=', N], answer=[28])
it('A', 'İkirəqəmli ədədlərin fərqi', 'Fərqi tapın.', 'Əvvəl təklikləri, sonra onluqları çıxın: 12 − 7, sonra 4 − 2.', '25',
   tokens=[52, '−', 27, '=', N], answer=[25])
it('A', 'Toplama və çıxmanın əlaqəsi', 'Məchul hissəni tapın.', 'Tamdan məlum hissəni çıxın: 60 − 24.', '36',
   img=triple(60, 24, None), tokens=[24, '+', N, '=', 60], answer=[36])
it('A', 'Mötərizəli ifadələr', 'İfadənin qiymətini hesablayın.', 'Əvvəlcə mötərizədəki əməli yerinə yetirin: 12 + 8 = 20.', '30',
   tokens=[50, '−', '(', 12, '+', 8, ')', '=', N], answer=[30])
# B. Vurma və bölmə
it('B', 'Vurma', 'Sətirləri və sütunları sayın. Hasili tapın.', '3 sətir, hər sətirdə 4 ədəd var.', '12',
   img=array('🚗', 3, 4, 46), tokens=[3, '·', 4, '=', N], answer=[12])
it('B', 'Vurma cədvəli', 'Hasili tapın.', 'Beş-beş sayın: 5, 10, 15...', '35',
   tokens=[7, '·', 5, '=', N], answer=[35])
it('B', 'Bölmə', '15 almanı 3 boşqaba bərabər paylayın. Hər boşqaba neçə düşər?', 'Almaları bir-bir boşqablara qoyun.', '5',
   img=plates('🍎', (5, 5, 5), 36), tokens=[15, ':', 3, '=', N], answer=[5])
it('B', 'Vurma və bölmənin əlaqəsi', 'Bölməni yerinə yetirin.', '4 · 6 = 24 olduğunu xatırlayın.', '6',
   tokens=[24, ':', 4, '=', N], answer=[6])
# C. Ədədlər (500-ə qədər). Pullar
it('C', 'Yüzlük, onluq və təklik', 'Kublara uyğun ədədi yazın.', 'Kvadrat – yüzlük, çubuq – onluq, kub – təklik.', '324',
   img=hto(3, 2, 4, 80), tokens=[N], answer=[324])
it('C', '500-ə qədər sayma', 'On-on sayın. Sıranı davam etdirin.', 'Hər dəfə 10 əlavə edin: 270, 280, 290...', '300, 310',
   tokens=[270, 280, 290, N, N], answer=[300, 310])
it('C', 'Pullar', 'Pulları sayın. Cəmi neçə qəpikdir?', 'Böyükdən kiçiyə sayın: 50, 70, 80...', '85',
   img=coins([50, 20, 10, 5], 80), tokens=[N], answer=[85])
it('C', 'Alış-veriş', 'Top 25 manat, kitab 18 manatdır. Hamısı neçə manatdır?', 'Qiymətləri toplayın: 25 + 18.', '43',
   img=hstack([priced('⚽', '25 man'), priced('📘', '18 man')], 30), tokens=[25, '+', 18, '=', N], answer=[43])
# D. Ölçmə: uzunluq, kütlə, tutum
it('D', 'Uzunluq', 'Zolaq neçə santimetrdir?', 'Zolaq 0-dan başlayır. Ucunun altındakı ədədə baxın.', '8',
   img=on_ruler(strip(8, 50, RED), 10, 50), tokens=[N], answer=[8])
it('D', 'Uzunluq', 'Neçə santimetrdir?', '1 metr 100 santimetrdir.', '400',
   tokens=['4 m', '=', N], answer=[400])
it('D', 'Kütlə', 'Tərəzi bərabərdir. Qarpız neçə kiloqramdır?', 'Sağ tərəfdəki çəkiləri toplayın.', '6',
   img=scale([em('🍉', 90)], [weight(5), weight(1)], 0, 480), tokens=[N], answer=[6])
it('D', 'Tutum', '20 l suyu 5 litrlik qablara tökdülər. Neçə qab alındı?', '20-də neçə dəfə 5 var? 5, 10, 15, 20.', '4',
   img=em('🪣', 100), tokens=[20, ':', 5, '=', N], answer=[4])
# E. Saat, hadisələr və məlumatlar
it('E', 'Saat', 'Saat neçə tamamdır?', 'Uzun əqrəb 12-dədir. Qısa əqrəbə baxın.', '7',
   img=clock(7, 200), tokens=[N], answer=[7])
it('E', 'Saat', '«Saat 4-ün yarısıdır». Bunu göstərən saatı seçin.', 'Yarısında uzun əqrəb 6-dadır, qısa əqrəb 3 ilə 4 arasındadır.', '3:30',
   options=[clock(3, 150, 30), clock(4, 150, 30), clock(4, 150)], answer=0)
it('E', 'Təkrarlanan hadisələr', 'Qaydanı tapın. Sonra hansı fiqur gələr?', 'Qayda: dairə, dairə, kvadrat...', 'kvadrat',
   img=hstack([shape(k, 70, c) for k, c in [('circle', B3), ('circle', B3), ('square', R3), ('circle', B3), ('circle', B3)]] + [box(80, 80)], 12),
   options=[shape('circle', 90, B3), shape('square', 90, R3), shape('triangle', 90, Y3)], answer=1)
it('E', 'Diaqram', 'Diaqrama baxın. Neçə uşaq yayı sevir?', 'Sarı sütunun ucuna baxın.', '9',
   img=bars([(txt(n, 24), v) for n, v in [('Yaz', 6), ('Yay', 9), ('Payız', 3), ('Qış', 5)]], maxv=10, unit=26, barw=66, colors=[G3, Y3, O3, B3]),
   tokens=[N], answer=[9])

AREAS = [
    {'code': 'A', 'name': 'Çıxma (onluğun ayrılması)', 'topics': [70, 71, 72, 73, 74], 'home': 'Mağaza oyunu oynayın: «45 qəpik var idi, 18 qəpiklik aldıq. Nə qədər qaldı?» Cavabı toplama ilə yoxlayın.'},
    {'code': 'B', 'name': 'Vurma və bölmə', 'topics': [75, 76, 77, 78, 79, 80], 'home': 'Süfrədə əşyaları sıralarla düzün və vurma ilə sayın. Konfetləri bərabər paylayın – bu bölmədir.'},
    {'code': 'C', 'name': 'Ədədlər (500-ə qədər). Pullar', 'topics': [81, 82, 83, 84], 'home': 'Alış-verişdə qiymətləri birlikdə toplayın. Pulları böyükdən kiçiyə düzüb sayın.'},
    {'code': 'D', 'name': 'Ölçmə: uzunluq, kütlə, tutum', 'topics': [85, 86, 87], 'home': 'Evdə əşyaları xətkeşlə ölçün, mətbəxdə çəkini və litri birlikdə oxuyun.'},
    {'code': 'E', 'name': 'Saat, hadisələr və məlumatlar', 'topics': [88, 89, 90, 91], 'home': 'Gün ərzində saata birlikdə baxın: «Saat neçədir? Yarım saat sonra neçə olacaq?» Ailədə kiçik sorğu keçirin.'},
]
LEVELS = [{'min': 4, 'name': 'Mükəmməl', 'text': 'Bu bacarığı tam mənimsəyib. Növbəti mövzulara keçməyə hazırdır.'},
          {'min': 3, 'name': 'Yaxşı', 'text': 'Əsasən bacarır, kiçik səhvlər var. Səhv olan tapşırığı birlikdə yenidən həll edin.'},
          {'min': 2, 'name': 'İnkişaf edir', 'text': 'Bəzi hissələri bacarır. Mövzu {t} üzrə tapşırıqları təkrar edin.'},
          {'min': 0, 'name': 'Dəstək lazımdır', 'text': 'Bu bacarıq hələ formalaşmayıb. Mövzu {t} əvvəldən, əşyalar və şəkillərlə təkrar edilməlidir.'}]
OVERALL = [{'min': 18, 'name': 'Əla', 'text': 'Uşaq 2-ci sinfin 2-ci hissəsini çox yaxşı mənimsəyib.'},
           {'min': 14, 'name': 'Yaxşı', 'text': 'Uşaq mövzuların çoxunu mənimsəyib. Zəif sahələri qısa təkrarla möhkəmləndirin.'},
           {'min': 10, 'name': 'Orta', 'text': 'Uşaq bəzi mövzularda çətinlik çəkir. «İnkişaf edir» və «Dəstək lazımdır» olan sahələri 1–2 həftə təkrar edin.'},
           {'min': 0, 'name': 'Əlavə dəstək lazımdır', 'text': 'Uşağa əlavə köməklik lazımdır. Müəllimlə birlikdə zəif sahələr üzrə fərdi plan hazırlayın.'}]

assert len(ITEMS) == 20 and all(sum(1 for i in ITEMS if i['area'] == a) == 4 for a in 'ABCDE')
json.dump({'items': ITEMS, 'areas': AREAS, 'levels': LEVELS, 'overall': OVERALL}, open(os.path.join(OUT, 'test_items.json'), 'w'), ensure_ascii=False)
json.dump(VOICE, open(os.path.join(OUT, 'test_voice.json'), 'w'), ensure_ascii=False, indent=0)
print('items', len(ITEMS), 'voice', len(VOICE))
