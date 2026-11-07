"""Yoxlama testləri üçün ümumi hissə (3-1, 3-2): it() tapşırıq əlavə edir, save() test_items.json yazır."""
import base64, hashlib, io, json, os
from bookgen import *

VOICE = {}
N = {'s': 'num'}
ITEMS = []


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


def it(area, skill, ins, hint, disp, img=None, options=None, answer=None, tokens=None, mode='num', **kw):
    d = {'area': area, 'skill': skill, 'ins': ins, 'img': uri(img) if img is not None else None,
         'kind': 'choice' if options else 'slots', 'options': [uri(o, 500, 12) for o in options] if options else None,
         'prefix': None, 'tokens': tokens, 'answer': answer, 'mode': mode, 'disp': disp, 'hint': hint, 'audio': aid(ins)}
    d.update(kw)
    ITEMS.append(d)


LEVELS = [{'min': 4, 'name': 'Mükəmməl', 'text': 'Bu bacarığı tam mənimsəyib. Növbəti mövzulara keçməyə hazırdır.'},
          {'min': 3, 'name': 'Yaxşı', 'text': 'Əsasən bacarır, kiçik səhvlər var. Səhv olan tapşırığı birlikdə yenidən həll edin.'},
          {'min': 2, 'name': 'İnkişaf edir', 'text': 'Bəzi hissələri bacarır. Mövzu {t} üzrə tapşırıqları təkrar edin.'},
          {'min': 0, 'name': 'Dəstək lazımdır', 'text': 'Bu bacarıq hələ formalaşmayıb. Mövzu {t} əvvəldən, əşyalar və şəkillərlə təkrar edilməlidir.'}]


def overall(part):
    return [{'min': 18, 'name': 'Əla', 'text': 'Uşaq 3-cü sinfin %s çox yaxşı mənimsəyib.' % part},
            {'min': 14, 'name': 'Yaxşı', 'text': 'Uşaq mövzuların çoxunu mənimsəyib. Zəif sahələri qısa təkrarla möhkəmləndirin.'},
            {'min': 10, 'name': 'Orta', 'text': 'Uşaq bəzi mövzularda çətinlik çəkir. «İnkişaf edir» və «Dəstək lazımdır» olan sahələri 1–2 həftə təkrar edin.'},
            {'min': 0, 'name': 'Əlavə dəstək lazımdır', 'text': 'Uşağa əlavə köməklik lazımdır. Müəllimlə birlikdə zəif sahələr üzrə fərdi plan hazırlayın.'}]


def save_test(out, areas, part):
    assert len(ITEMS) == 20 and all(sum(1 for i in ITEMS if i['area'] == a) == 4 for a in 'ABCDE'), len(ITEMS)
    os.makedirs(out, exist_ok=True)
    json.dump({'items': ITEMS, 'areas': areas, 'levels': LEVELS, 'overall': overall(part)}, open(os.path.join(out, 'test_items.json'), 'w'), ensure_ascii=False)
    json.dump(VOICE, open(os.path.join(out, 'test_voice.json'), 'w'), ensure_ascii=False, indent=0)
    print('items', len(ITEMS), 'voice', len(VOICE))
