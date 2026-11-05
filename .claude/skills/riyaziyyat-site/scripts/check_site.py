"""Riyaziyyat saytını yoxlayır: hər mövzuda 10 tapşırıq, səs faylları, istinadlar, hörmətli müraciət.
Run (repo kökündən): python3 .claude/skills/riyaziyyat-site/scripts/check_site.py [REPO]
Çıxış kodu 0 = hər şey qaydasındadır, 1 = problem var (siyahı çap olunur)."""
import hashlib, json, os, re, sys

ROOT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else os.getcwd())
sys.path.insert(0, os.path.join(ROOT, 'tools'))
try:
    from formal import formal
except Exception:
    formal = None

problems = []


def bad(msg):
    problems.append(msg)


def books():
    out = []
    for d in ['.'] + sorted(os.listdir(ROOT)):
        p = os.path.join(ROOT, d, 'data', 'topics.json')
        if os.path.exists(p):
            out.append(d)
    return out


def walk(o):
    if isinstance(o, dict):
        for v in o.values():
            yield from walk(v)
    elif isinstance(o, list):
        for v in o:
            yield from walk(v)
    elif isinstance(o, str):
        yield o


seen_topics = {}
for b in books():
    dd = os.path.join(ROOT, b, 'data')
    name = '1-1' if b == '.' else b
    topics = json.load(open(os.path.join(dd, 'topics.json')))['topics']
    voice = json.load(open(os.path.join(dd, 'voice.json')))
    audio = set(json.load(open(os.path.join(dd, 'audio.json'))))
    files = {f[:-4] for f in os.listdir(os.path.join(ROOT, b, 'audio')) if f.endswith('.mp3')}
    for k, v in voice.items():
        if hashlib.md5(v.encode()).hexdigest()[:10] != k:
            bad(f'{name}: voice.json id {k} does not match its text: {v[:60]}')
    for t in topics:
        n = t['n']
        if n in seen_topics:
            bad(f'{name}: topic {n} also exists in {seen_topics[n]}')
        seen_topics[n] = name
        if len(t['problems']) != 10:
            bad(f'{name}: topic {n} has {len(t["problems"])} problems (need 10)')
        refs = [('concept', t.get('conceptAudio'))] + [(f'problem {i + 1}', p.get('audio')) for i, p in enumerate(t['problems'])]
        for where, a in refs:
            if a not in voice:
                bad(f'{name}: topic {n} {where}: audio id {a} not in voice.json')
            elif a not in audio or a not in files:
                bad(f'{name}: topic {n} {where}: audio {a} missing (audio.json or mp3) – run tools/tts_all.py')
        for p in [t.get('conceptImg')] + [x for p in t['problems'] for x in (p.get('img'), (p.get('web') or {}).get('stem'))] + \
                [o.get('img') for p in t['problems'] for o in ((p.get('web') or {}).get('opts') or []) if isinstance(o, dict)]:
            if p and not os.path.exists(os.path.join(ROOT, b, p)):
                bad(f'{name}: topic {n}: image missing {p}')
    if formal:
        for s in list(walk(topics)) + list(voice.values()):
            # tək söz (məs. fəsil adı «Yaz», «Bulka») cavab variantıdır, əmr deyil
            if not s.startswith(('img/', 'data:')) and re.search(r'[\s.!?:]', s.strip()) and formal(s) != s:
                bad(f'{name}: informal wording: {s[:80]}  →  {formal(s)[:80]}')
    # test page
    tp = os.path.join(ROOT, b, 'test.html')
    if os.path.exists(tp):
        s = open(tp, encoding='utf8').read()
        m = re.search(r'const DATA = (\{.*?\});\n', s, re.S)
        if not m:
            bad(f'{name}: test.html DATA not found')
        else:
            items = json.loads(m.group(1))['items']
            if len(items) != 20:
                bad(f'{name}: test.html has {len(items)} items (need 20)')
            for i, it in enumerate(items):
                a = it.get('audio') or ''
                if not a:
                    bad(f'{name}: test item {i + 1} has no audio')
                elif not a.startswith('data:') and a not in files:
                    bad(f'{name}: test item {i + 1}: audio {a}.mp3 missing')
                if formal:
                    for k in ('ins', 'hint'):
                        if formal(it.get(k, '')) != it.get(k, ''):
                            bad(f'{name}: test item {i + 1} {k} informal: {it[k][:70]}')

for k in ['p_ok1', 'p_ok2', 'p_ok3', 'p_ok4', 'p_no1', 'p_no2']:
    if not os.path.exists(os.path.join(ROOT, 'audio', k + '.mp3')):
        bad(f'praise sound audio/{k}.mp3 missing')

# UI strings in shared code: quoted Azerbaijani strings that formal() would change
if formal:
    ALLOW = {'Cavabın düz və ya səhv olduğu göstərilmir, sakitcə növbəti suala keçir.'}  # «düz» = adjective
    pages = ['app.js', 'hesabat.html'] + [os.path.join(b, f) for b in books() for f in ('index.html', 'test.html')]
    for f in pages:
        p = os.path.join(ROOT, f)
        if not os.path.exists(p):
            continue
        s = open(p, encoding='utf8').read()
        s = re.sub(r'const DATA = \{.*?\};\n', '', s, flags=re.S)
        s = re.sub(r'data:[^"\')\s]+', '', s)
        for m in re.finditer(r"'([^'\n]{2,220})'|>([^<>\n]{2,220})<", s):
            t = next(x for x in m.groups() if x)
            if re.search('[əğıöüçşƏĞÖÜÇŞİ]', t) and t not in ALLOW and formal(t) != t:
                bad(f'{f}: informal UI text: {t[:80]}')

if problems:
    print(f'{len(problems)} problem(s):')
    for p in problems:
        print(' -', p)
    sys.exit(1)
print('OK: books', ', '.join('1-1' if b == '.' else b for b in books()), '· topics', len(seen_topics))
