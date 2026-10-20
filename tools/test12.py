"""Yoxlama testi (1-2): 20 tapşırıq. Writes OUT/test_items.json (images as data URIs, audio as text ids)."""
import base64, hashlib, io, json, os, sys
from draw import *

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


# A. Həndəsi fiqurlar
it('A', 'Fiqurlar', 'Kvadratı seç.', 'Kvadratın 4 tərəfi var və hamısı bərabərdir.', 'kvadrat',
   options=[shape('circle', 100, ORANGE), shape('rect', 90, ORANGE), shape('square', 100, ORANGE), shape('triangle', 100, ORANGE)], answer=2)
it('A', 'Fəza fiqurları', 'Kürəni seç.', 'Kürə top kimi yumrudur.', 'kürə',
   options=[solid('cube', 100, (66, 165, 245)), solid('cone', 100, (66, 165, 245)), solid('sphere', 100, (66, 165, 245))], answer=2)
it('A', 'Tam, yarı', 'Hansı fiqur 2 bərabər hissəyə bölünüb? Seç.', 'Hər iki hissə eyni böyüklükdə olmalıdır.', '2-ci fiqur',
   options=[shape('circle', 100, (102, 187, 106), split=0.3), shape('square', 100, (102, 187, 106), split=0.5), shape('triangle', 100, (102, 187, 106), split='tri_bad')], answer=1)
it('A', 'Yarı', '10 almanın yarısı neçədir?', '10 almanı iki bərabər qrupa böl.', '5',
   img=frame(row('🍎', 10, 64, 8, 5), 14), tokens=[N], answer=[5])
# B. Toplama
it('B', 'Toplama', 'Cəmi tap.', '13-dən 4 addım irəli say: 14, 15, 16, 17.', '17',
   img=numline(10, 20, 56, start=13), tokens=[13, '+', 4, '=', N], answer=[17])
it('B', '10-a tamamlamaqla toplama', 'Əvvəlcə 10-a tamamla, sonra topla.', '8 + 2 = 10. Qalan 3-ü də əlavə et.', '13',
   img=hstack([dots_frame(8, 2), dots_frame(0, 3)], 24), tokens=[8, '+', 5, '=', N], answer=[13])
it('B', '10-a tamamlamaqla toplama', 'Cəmi tap.', '9 + 1 = 10. Sonra 6 da əlavə et.', '16',
   tokens=[9, '+', 7, '=', N], answer=[16])
it('B', 'Üç ədədin cəmi', 'Əvvəlcə 10 düzəlt, sonra topla.', '6 + 4 = 10. Sonra 10 + 5.', '15',
   tokens=[6, '+', 5, '+', 4, '=', N], answer=[15])
# C. Çıxma
it('C', 'Çıxma', 'Fərqi tap.', '17-dən 5 addım geri say.', '12',
   img=numline(10, 20, 56, start=17), tokens=[17, '−', 5, '=', N], answer=[12])
it('C', '10-a qədər azaltmaqla çıxma', 'Əvvəlcə 10-a qədər azalt, sonra çıx.', '14 − 4 = 10. Sonra 10 − 2.', '8',
   img=hstack([dots_frame(10, cross=2), dots_frame(4, cross=4)], 24), tokens=[14, '−', 6, '=', N], answer=[8])
it('C', 'Toplama və çıxmanın əlaqəsi', 'Toplamaya bax və çıxmanı tamamla.', '8 + 7 = 15. Deməli, 15 − 7 = 8.', '8',
   img=expr(['8', '+', '7', '=', '15'], 60), tokens=[15, '−', 7, '=', N], answer=[8])
it('C', 'Məchulun tapılması', 'Məchul toplananı tap.', '9-a neçə əlavə etsək, 16 olar?', '7',
   tokens=[9, '+', N, '=', 16], answer=[7])
# D. 100-ə qədər ədədlər və pullar
it('D', '100-ə qədər sayma', 'Beş-beş say. Boş xanalara yaz.', 'Hər dəfə 5 əlavə et: 5, 10, 15...', '15, 25',
   tokens=[5, 10, N, 20, N], answer=[15, 25])
it('D', 'Onluq və təklik', 'Neçə onluq və neçə təklik var? Yaz.', 'Bir dəstədə 10 çöp var. Dəstələri, sonra tək çöpləri say.', '3 onluq, 6 təklik',
   img=tens_ones(3, 6, 110), tokens=[N, 'onluq', N, 'təklik'], answer=[3, 6])
it('D', 'Qəpik', 'Sikkələri topla. Cəmi neçə qəpikdir?', 'Əvvəlcə 20 və 10-u topla, sonra 5-i əlavə et.', '35 qəpik',
   img=hstack([coin(20), coin(10), coin(5)], 14), tokens=[N, 'qəp'], answer=[35])
it('D', 'Alış-veriş', 'Şokolad 6 qəpikdir. 10 qəpik verdin. Neçə qəpik qaytarılar?', '10 − 6 = ?', '4 qəpik',
   img=hstack([priced('🍫', '6 qəp'), coin(10, 100)], 30), tokens=[10, '−', 6, '=', N], answer=[4])
# E. Ölçmə, vaxt, məlumat
it('E', 'Uzun, qısa', 'Uzun karandaşı seç.', 'Karandaşların uclarını müqayisə et.', '2-ci karandaş',
   options=[pencil(4, 40, (102, 187, 106)), pencil(7, 40, (66, 165, 245)), pencil(5, 40, (239, 83, 80))], answer=1)
it('E', 'Santimetr', 'Xətkeşlə ölç. Zolaq neçə santimetrdir?', 'Zolaq 0-dan başlayır. Ucunun altındakı ədədə bax.', '7 sm',
   img=on_ruler(strip(7, 56, RED), 10, 56), tokens=[N, 'sm'], answer=[7])
it('E', 'Saat', 'Saat neçədir?', 'Qısa qırmızı əqrəbə bax.', 'saat 4',
   img=clock(4, 220), tokens=[N], answer=[4])
it('E', 'Piktoqram', 'Piktoqrama bax. Neçə alma var?', 'Alma sırasındakı şəkilləri say.', '5',
   img=table([[em('🍎', 60), row('🍎', 5, 52, 6)], [em('🍐', 60), row('🍐', 3, 52, 6)]], 80), tokens=[N], answer=[5])

AREAS = [
    {'code': 'A', 'name': 'Həndəsi fiqurlar', 'topics': [29, 30, 31], 'home': 'Evdə əşyaların formasını birlikdə tapın: top – kürə, qutu – kub, boşqab – dairə. Almanı iki bərabər yarıya bölün.'},
    {'code': 'B', 'name': 'Toplama (20-yə qədər)', 'topics': [32, 33, 34], 'home': 'Düymələrlə 10-a tamamlama oyunu oynayın: «8 düymə var, 10 olması üçün neçə lazımdır?»'},
    {'code': 'C', 'name': 'Çıxma (20-yə qədər)', 'topics': [35, 36, 37], 'home': '15 əşyadan bir neçəsini götürüb «Neçə qaldı?» deyə soruşun. Əvvəlcə 10 qalana qədər götürün.'},
    {'code': 'D', 'name': 'Ədədlər (100-ə qədər) və pullar', 'topics': [38, 39, 40, 41], 'home': 'Çöpləri 10-luq dəstələrə bağlayıb sayın. Sikkələrlə «mağaza» oynayın.'},
    {'code': 'E', 'name': 'Ölçmə, vaxt və məlumatlar', 'topics': [42, 43, 44, 45, 46, 47, 48, 49], 'home': 'Xətkeşlə əşyaları ölçün, saatda tam saatları birlikdə oxuyun, evdəki meyvələri sayıb şəkillə cədvəl çəkin.'},
]
LEVELS = [{'min': 4, 'name': 'Mükəmməl', 'text': 'Bu bacarığı tam mənimsəyib. Növbəti mövzulara keçməyə hazırdır.'},
          {'min': 3, 'name': 'Yaxşı', 'text': 'Əsasən bacarır, kiçik səhvlər var. Səhv olan tapşırığı birlikdə yenidən həll edin.'},
          {'min': 2, 'name': 'İnkişaf edir', 'text': 'Bəzi hissələri bacarır. Mövzu {t} üzrə tapşırıqları təkrar edin.'},
          {'min': 0, 'name': 'Dəstək lazımdır', 'text': 'Bu bacarıq hələ formalaşmayıb. Mövzu {t} əvvəldən, əşyalar və şəkillərlə təkrar edilməlidir.'}]
OVERALL = [{'min': 18, 'name': 'Əla', 'text': 'Uşaq 1-ci sinfin 2-ci hissəsini çox yaxşı mənimsəyib. 2-ci sinfə keçmək olar.'},
           {'min': 14, 'name': 'Yaxşı', 'text': 'Uşaq mövzuların çoxunu mənimsəyib. Zəif sahələri qısa təkrarla möhkəmləndirin.'},
           {'min': 10, 'name': 'Orta', 'text': 'Uşaq bəzi mövzularda çətinlik çəkir. «İnkişaf edir» və «Dəstək lazımdır» olan sahələri 1–2 həftə təkrar edin.'},
           {'min': 0, 'name': 'Əlavə dəstək lazımdır', 'text': 'Uşağa əlavə köməklik lazımdır. Müəllimlə birlikdə zəif sahələr üzrə fərdi plan hazırlayın.'}]

assert len(ITEMS) == 20 and all(sum(1 for i in ITEMS if i['area'] == a) == 4 for a in 'ABCDE')
json.dump({'items': ITEMS, 'areas': AREAS, 'levels': LEVELS, 'overall': OVERALL}, open(os.path.join(OUT, 'test_items.json'), 'w'), ensure_ascii=False)
json.dump(VOICE, open(os.path.join(OUT, 'test_voice.json'), 'w'), ensure_ascii=False, indent=0)
print('items', len(ITEMS), 'voice', len(VOICE))
