"""Yoxlama testi (2-1): 20 tapşırıq. Writes OUT/test_items.json (images as data URIs, audio as text ids)."""
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



# A. Ədədlər: müqayisə və sıralama (100-ə qədər)
it('A', 'Ədədlərin müqayisəsi', 'Ən böyük ədədi seç.', 'Əvvəlcə onluqlara bax: hansında onluq çoxdur?', '85',
   options=[chip(v, 64, WHITE, INK, GREY) for v in ('58', '85', '80', '55')], answer=1)
it('A', 'Ədədlərin müqayisəsi', 'Boş xanaya uyğun ədədi yaz.', '47-dən böyük, 49-dan kiçik ədəd.', '48',
   tokens=[47, '<', N, '<', 49], answer=[48])
it('A', 'Sıralama', 'Beş-beş geri say. Sıranı davam etdir.', 'Hər dəfə 5 çıx: 70, 65, 60...', '55, 50',
   tokens=[70, 65, 60, N, N], answer=[55, 50])
it('A', 'Onluq və təklik', 'Ədədi yaz.', 'Dəstələri on-on, sonra tək çöpləri say.', '63',
   img=tens_ones(6, 3, 90), tokens=[N], answer=[63])
# B. Toplama (100-ə qədər)
it('B', 'İkirəqəmli + birrəqəmli', 'Cəmi tap.', 'Təkliyi təkliyə əlavə et: 2 + 6. Onluqlar dəyişmir.', '48',
   tokens=[42, '+', 6, '=', N], answer=[48])
it('B', 'Onluqların toplanması', 'Cəmi tap.', '3 onluq + 5 onluq = ? onluq.', '80',
   img=numline_step(0, 100, 10, 54, start=30, hops=5), tokens=[30, '+', 50, '=', N], answer=[80])
it('B', 'Yeni onluğun yaranması', 'Əvvəlcə 40-a tamamla, sonra topla.', '38 + 2 = 40. Sonra 3 də əlavə et.', '43',
   tokens=[38, '+', 5, '=', N], answer=[43])
it('B', 'İkirəqəmli ədədlərin toplanması', 'Cəmi tap.', 'Təkliklər: 7 + 6 = 13. Onluqlar: 40 + 30 = 70. Sonra 70 + 13.', '83',
   tokens=[47, '+', 36, '=', N], answer=[83])
# C. Çıxma (100-ə qədər)
it('C', 'İkirəqəmli − birrəqəmli', 'Fərqi tap.', 'Təklikdən təklik çıx: 7 − 4.', '63',
   tokens=[67, '−', 4, '=', N], answer=[63])
it('C', 'Onluqların çıxılması', 'Fərqi tap.', '9 onluq − 3 onluq = ? onluq.', '60',
   img=bundles_crossed(9, 3, 60, 5), tokens=[90, '−', 30, '=', N], answer=[60])
it('C', 'İkirəqəmli ədədlərin fərqi', 'Fərqi tap.', 'Təkliklər: 6 − 3. Onluqlar: 80 − 40.', '43',
   tokens=[86, '−', 43, '=', N], answer=[43])
it('C', 'Məsələ', 'Ağacda 48 alma var idi. 15 almanı dərdilər. Neçə alma qaldı?', '48 − 15 = ?', '33',
   img=em('🍎', 90), tokens=[48, '−', 15, '=', N], answer=[33])
# D. Vurma və bölmə
it('D', 'Təkrar toplama', 'Təkrar toplamanı vurma ilə yaz.', 'Neçə dəfə 4 toplanıb? Say.', '3',
   img=groups('🍓', (4, 4, 4), 44), tokens=[4, '+', 4, '+', 4, '=', 4, '·', N], answer=[3])
it('D', 'Vurma', 'Hasili tap.', 'Hər əldə 5 barmaq var. Beş-beş say.', '10',
   img=hstack([em('🖐️', 90), em('🖐️', 90)], 24), tokens=[5, '·', 2, '=', N], answer=[10])
it('D', 'Bölmə', '12 konfeti 3 boşqaba bərabər payla. Hər boşqaba neçə düşər?', 'Konfetləri bir-bir boşqablara qoy.', '4',
   img=plates('🍬', (4, 4, 4), 40), tokens=[12, ':', 3, '=', N], answer=[4])
it('D', 'Tək və cüt ədədlər', 'Cüt ədədi seç.', 'Cüt ədədin sonu 0, 2, 4, 6 və ya 8 olur.', '36',
   options=[chip(v, 64, WHITE, INK, GREY) for v in ('15', '23', '36', '41')], answer=2)
# E. Həndəsi fiqurlar
it('E', 'Bucaq', 'Düz bucağı seç.', 'Düz bucaq kvadratın küncü kimidir.', 'düz bucaq',
   options=[angle_img(45, 130), angle_img(90, 130), angle_img(130, 130)], answer=1)
it('E', 'Çoxbucaqlı', 'Fiqurun neçə bucağı var?', 'Təpələri bir-bir say.', '5',
   img=poly(5, 160, (102, 187, 106)), tokens=[N], answer=[5])
it('E', 'Üz, til və təpə', 'Kubun neçə təpəsi var?', 'Qırmızı nöqtələri say. Arxada gizlənən nöqtəni də unutma.', '8',
   img=cube_marked(160), tokens=[N], answer=[8])
it('E', 'Qruplaşdırma', 'Artıq olan fiquru seç.', 'Fiqurların formasına bax.', 'dairə',
   options=[shape('square', 90, (66, 165, 245)), shape('square', 90, (239, 83, 80)), shape('circle', 90, (66, 165, 245)), shape('square', 90, (255, 213, 79))], answer=2)

AREAS = [
    {'code': 'A', 'name': 'Ədədlər: müqayisə və sıralama', 'topics': [50, 51], 'home': 'Evdə iki ədəd deyin və «Hansı böyükdür?» deyə soruşun. Əvvəlcə onluqları, sonra təklikləri müqayisə edin.'},
    {'code': 'B', 'name': 'Toplama (100-ə qədər)', 'topics': [52, 53, 54, 67, 68, 69], 'home': 'Çöpləri 10-luq dəstələrə bağlayıb toplayın: əvvəlcə dəstələri, sonra tək çöpləri sayın.'},
    {'code': 'C', 'name': 'Çıxma (100-ə qədər)', 'topics': [55, 56, 57], 'home': 'Mağaza oyunu oynayın: «30 qəpiyin var, 20 qəpiklik aldın. Nə qədər qaldı?»'},
    {'code': 'D', 'name': 'Vurma və bölmə', 'topics': [58, 59, 60, 61, 62], 'home': 'Süfrədə meyvələri boşqablara bərabər paylayın. Corabları cüt-cüt sayın: iki-iki.'},
    {'code': 'E', 'name': 'Həndəsi fiqurlar', 'topics': [63, 64, 65, 66], 'home': 'Evdə düz bucaqlı əşyalar tapın (kitab, pəncərə). Qutunun üzlərini, tillərini və təpələrini birlikdə sayın.'},
]
LEVELS = [{'min': 4, 'name': 'Mükəmməl', 'text': 'Bu bacarığı tam mənimsəyib. Növbəti mövzulara keçməyə hazırdır.'},
          {'min': 3, 'name': 'Yaxşı', 'text': 'Əsasən bacarır, kiçik səhvlər var. Səhv olan tapşırığı birlikdə yenidən həll edin.'},
          {'min': 2, 'name': 'İnkişaf edir', 'text': 'Bəzi hissələri bacarır. Mövzu {t} üzrə tapşırıqları təkrar edin.'},
          {'min': 0, 'name': 'Dəstək lazımdır', 'text': 'Bu bacarıq hələ formalaşmayıb. Mövzu {t} əvvəldən, əşyalar və şəkillərlə təkrar edilməlidir.'}]
OVERALL = [{'min': 18, 'name': 'Əla', 'text': 'Uşaq 2-ci sinfin 1-ci hissəsini çox yaxşı mənimsəyib. 2-ci hissəyə keçmək olar.'},
           {'min': 14, 'name': 'Yaxşı', 'text': 'Uşaq mövzuların çoxunu mənimsəyib. Zəif sahələri qısa təkrarla möhkəmləndirin.'},
           {'min': 10, 'name': 'Orta', 'text': 'Uşaq bəzi mövzularda çətinlik çəkir. «İnkişaf edir» və «Dəstək lazımdır» olan sahələri 1–2 həftə təkrar edin.'},
           {'min': 0, 'name': 'Əlavə dəstək lazımdır', 'text': 'Uşağa əlavə köməklik lazımdır. Müəllimlə birlikdə zəif sahələr üzrə fərdi plan hazırlayın.'}]

assert len(ITEMS) == 20 and all(sum(1 for i in ITEMS if i['area'] == a) == 4 for a in 'ABCDE')
json.dump({'items': ITEMS, 'areas': AREAS, 'levels': LEVELS, 'overall': OVERALL}, open(os.path.join(OUT, 'test_items.json'), 'w'), ensure_ascii=False)
json.dump(VOICE, open(os.path.join(OUT, 'test_voice.json'), 'w'), ensure_ascii=False, indent=0)
print('items', len(ITEMS), 'voice', len(VOICE))
