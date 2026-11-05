"""Tapşırıq mətnlərində əmr formasını hörmətli formaya çevirir (yaz → yazın, say → sayın ...).
Yalnız cümlə/ifadə sonundakı (nöqtə, vergül, iki nöqtə, sual, «və» qarşısında) feillər dəyişir,
belə ki «düz bucaq», «alma» (meyvə) kimi sözlər toxunulmaz qalır.

İstifadə:  python3 tools/formal.py            → dəyişiklik siyahısı (formal_review.tsv)
           python3 tools/formal.py --apply    → data/*.json fayllarını yeniləyir (səs id-ləri də)
"""
import hashlib, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOOKS = ['.', '1-2', '2-1', '2-2']

# 2-ci şəxs təki → 2-ci şəxs cəmi (hörmət)
VERBS = {
    'al': 'alın', 'ayır': 'ayırın', 'azalt': 'azaldın', 'bax': 'baxın', 'başla': 'başlayın',
    'birləşdir': 'birləşdirin', 'böl': 'bölün', 'dəyiş': 'dəyişin', 'doldur': 'doldurun',
    'düzəlt': 'düzəldin', 'düz': 'düzün', 'et': 'edin', 'etdir': 'etdirin', 'get': 'gedin',
    'hesabla': 'hesablayın', 'payla': 'paylayın', 'qrupla': 'qruplayın', 'say': 'sayın',
    'seç': 'seçin', 'tamamla': 'tamamlayın', 'tap': 'tapın', 'topla': 'toplayın',
    'toxun': 'toxunun', 'tullan': 'tullanın', 'yaz': 'yazın', 'yığ': 'yığın', 'çıx': 'çıxın', 'çək': 'çəkin',
    'ölç': 'ölçün',
}
# başqa 2-ci şəxs formaları (hər yerdə)
OTHER = {'çıxdın': 'çıxdınız', 'versən': 'versəniz'}
# bu sözlər vergüldən əvvəl sifət ola bilər («Bucaqlar: düz, iti, kor»)
NO_COMMA = {'düz'}

L = r'A-Za-zƏəĞğİıIiÖöÜüÇçŞş'
WORD = re.compile(r'(?<![' + L + r'])([' + L + r']+)(?![' + L + r'])')


def keep_case(src, dst):
    return dst[0].upper() + dst[1:] if src[:1].isupper() else dst


def formal(text):
    out, pos = [], 0
    for m in WORD.finditer(text):
        w = m.group(1)
        low = w.replace('İ', 'i').replace('I', 'ı').lower()
        rest = text[m.end():]
        nxt = re.match(r'\s*(\S)', rest)
        nxt_ch = nxt.group(1) if nxt else ''
        after_va = re.match(r'\s+və(?![' + L + r'])', rest) is not None
        new = None
        if low in OTHER:
            new = OTHER[low]
        elif low in VERBS and not (low == 'düz' and re.match(r'\s+və\s+əyri', rest)):  # «düz və əyri xətlər» – sifət
            end =not rest.strip() or nxt_ch in '.!?:;)' or after_va or (nxt_ch == ',' and low not in NO_COMMA)
            if end:
                new = VERBS[low]
        if new:
            out.append(text[pos:m.start()])
            out.append(keep_case(w, new))
            pos = m.end()
    out.append(text[pos:])
    return ''.join(out)


def h(text):
    return hashlib.md5(text.encode()).hexdigest()[:10]


def main():
    apply = '--apply' in sys.argv
    review = []
    for b in BOOKS:
        dd = os.path.join(ROOT, b, 'data')
        topics = json.load(open(os.path.join(dd, 'topics.json')))
        voice = json.load(open(os.path.join(dd, 'voice.json')))
        remap = {}
        nvoice = {}
        for k, v in voice.items():
            nv = formal(v)
            nk = h(nv) if nv != v else k
            remap[k] = nk
            nvoice[nk] = nv
            if nv != v:
                review.append((b, 'səs', v, nv))
        for t in topics['topics']:
            for key in ('title', 'concept'):
                if key in t:
                    nv = formal(t[key])
                    if nv != t[key]:
                        review.append((b, key, t[key], nv))
                        t[key] = nv
            if t.get('conceptAudio') in remap:
                t['conceptAudio'] = remap[t['conceptAudio']]
            for p in t['problems']:
                nv = formal(p['ins'])
                if nv != p['ins']:
                    review.append((b, 'mətn', p['ins'], nv))
                    p['ins'] = nv
                if p.get('audio') in remap:
                    p['audio'] = remap[p['audio']]
        if apply:
            json.dump(topics, open(os.path.join(dd, 'topics.json'), 'w'), ensure_ascii=False)
            json.dump(nvoice, open(os.path.join(dd, 'voice.json'), 'w'), ensure_ascii=False, indent=0)
    seen, rows = set(), []
    for r in review:
        if (r[2], r[3]) in seen:
            continue
        seen.add((r[2], r[3]))
        rows.append(r)
    with open(os.path.join(ROOT, 'formal_review.tsv'), 'w') as f:
        f.write('kitab\tnöv\tƏvvəl\tSonra\n')
        for r in rows:
            f.write('\t'.join(r) + '\n')
    print(len(rows), 'fərqli dəyişiklik', '(tətbiq edildi)' if apply else '(yalnız siyahı)')


if __name__ == '__main__':
    main()
