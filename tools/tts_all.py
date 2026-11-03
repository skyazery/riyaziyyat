"""Bütün kitabların səsləri: az-AZ-BanuNeural, ton +17Hz, normal sürət (tts21.py ilə eyni qayda).
Əvvəldəki səssizlik kəsilir, sonda 0.2 s qalır; mövzu girişinin (concept) əvvəlinə salamlama əlavə olunur.
Yalnız çatışmayan faylları yaradır, data/audio.json-u yeniləyir, istifadə olunmayan köhnə faylları silir.
Yoxlama testlərindəki (test.html) səsləri də mətnə görə yeniləyir.

Run: python3 tools/tts_all.py [--praise]   (ffmpeg: PATH-da və ya imageio-ffmpeg paketi)
"""
import asyncio, base64, hashlib, json, os, re, shutil, subprocess, sys, tempfile
import edge_tts

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOOKS = ['.', '1-2', '2-1']
VOICE, PITCH, RATE = 'az-AZ-BanuNeural', '+17Hz', '+0%'
GREET = os.path.join(ROOT, 'tools', 'greet.mp3')  # salamlama (1-2, mövzu 29 girişinin ilk 3.95 s)
GREET_OLD = os.path.join(ROOT, '1-2', 'audio', '4fb7a9b7b8.mp3')
# cavabdan sonra tərif səsləri (app.js: p_ok1–4, p_no1–2)
PRAISE = {
    'p_ok1': 'Əla!',
    'p_ok2': 'Afərin! Düz cavab verdiniz!',
    'p_ok3': 'Düzdür!',
    'p_ok4': 'Çox yaxşı! Belə davam edin!',
    'p_no1': 'Yenə cəhd edin.',
    'p_no2': 'Bir də diqqətlə baxın.',
}
TRIM = 'silenceremove=start_periods=1:start_threshold=-50dB,areverse,silenceremove=start_periods=1:start_threshold=-50dB,areverse'

try:
    FF = shutil.which('ffmpeg') or __import__('imageio_ffmpeg').get_ffmpeg_exe()
except Exception:
    sys.exit('ffmpeg tapılmadı: pip install imageio-ffmpeg')

tmp = tempfile.mkdtemp()


def ff(*args):
    subprocess.run([FF, '-v', 'error', '-y', *args], check=True)


if not os.path.exists(GREET):
    ff('-i', GREET_OLD, '-t', '3.95', '-ar', '24000', '-ac', '1', '-b:a', '48k', GREET)
greet_wav = os.path.join(tmp, 'greet.wav')
ff('-i', GREET, '-ar', '24000', '-ac', '1', greet_wav)


def finish(raw, out, with_greet):
    clean = raw + '.wav'
    ff('-i', raw, '-af', TRIM + ',apad=pad_dur=0.2', '-ar', '24000', '-ac', '1', clean)
    if with_greet:
        ff('-i', greet_wav, '-i', clean, '-filter_complex', '[0:a][1:a]concat=n=2:v=0:a=1', '-ar', '24000', '-ac', '1', '-b:a', '48k', out)
    else:
        ff('-i', clean, '-ar', '24000', '-ac', '1', '-b:a', '48k', out)


async def synth(sem, text, out, with_greet=False):
    async with sem:
        raw = os.path.join(tmp, os.path.basename(out) + '.raw.mp3')
        for attempt in range(5):
            try:
                await asyncio.wait_for(edge_tts.Communicate(text, VOICE, pitch=PITCH, rate=RATE).save(raw), 60)
                break
            except Exception as e:
                if attempt == 4:
                    print('FAIL', out, e)
                    return 'fail'
                await asyncio.sleep(2 + attempt * 3)
    await asyncio.to_thread(finish, raw, out, with_greet)
    return 'ok'


def aid(text):
    return hashlib.md5(text.encode()).hexdigest()[:10]


async def main():
    sem = asyncio.Semaphore(6)
    jobs = []
    plan = []
    for b in BOOKS:
        dd, ad = os.path.join(ROOT, b, 'data'), os.path.join(ROOT, b, 'audio')
        voice = json.load(open(os.path.join(dd, 'voice.json')))
        concepts = {t['conceptAudio'] for t in json.load(open(os.path.join(dd, 'topics.json')))['topics']}
        for k, v in voice.items():
            out = os.path.join(ad, k + '.mp3')
            if not os.path.exists(out):
                jobs.append(synth(sem, v, out, k in concepts))
        plan.append((b, dd, ad, voice))
    if '--praise' in sys.argv:  # tərif səslərini yenidən yarat
        for k, v in PRAISE.items():
            jobs.append(synth(sem, v, os.path.join(ROOT, 'audio', k + '.mp3')))
    # yoxlama testləri: səs data URI (1-1, 1-2) və ya id (2-1)
    tests = []
    for b in BOOKS:
        f = os.path.join(ROOT, b, 'test.html')
        s = open(f, encoding='utf8').read()
        m = re.search(r'const DATA = (\{.*?\});\n', s, re.S)
        data = json.loads(m.group(1))
        for i, item in enumerate(data['items']):
            a = item.get('audio') or ''
            if a.startswith('data:'):
                out = os.path.join(tmp, 'test_%s_%d.mp3' % (b.replace('.', 'b11'), i))
                jobs.append(synth(sem, item['ins'], out))
                tests.append((f, i, out))
            elif a:
                k = aid(item['ins'])
                out = os.path.join(ROOT, b, 'audio', k + '.mp3')
                if not os.path.exists(out):
                    jobs.append(synth(sem, item['ins'], out))
                tests.append((f, i, k))
    print('işlər:', len(jobs))
    res = await asyncio.gather(*jobs)
    print({r: res.count(r) for r in set(res)})
    if 'fail' in res:
        sys.exit('Bəzi səslər alınmadı – yenidən işə salın (hazır olanlar saxlanılıb).')
    # test.html-ləri yenilə
    by_file = {}
    for f, i, v in tests:
        by_file.setdefault(f, []).append((i, v))
    test_ids = {}
    for f, lst in by_file.items():
        s = open(f, encoding='utf8').read()
        m = re.search(r'const DATA = (\{.*?\});\n', s, re.S)
        data = json.loads(m.group(1))
        for i, v in lst:
            if v.endswith('.mp3'):
                data['items'][i]['audio'] = 'data:audio/mpeg;base64,' + base64.b64encode(open(v, 'rb').read()).decode()
            else:
                data['items'][i]['audio'] = v
                test_ids.setdefault(os.path.dirname(f), set()).add(v)
        s = s[:m.start(1)] + json.dumps(data, ensure_ascii=False) + s[m.end(1):]
        open(f, 'w', encoding='utf8').write(s)
    # audio.json və köhnə fayllar
    for b, dd, ad, voice in plan:
        keep = set(voice) | test_ids.get(os.path.join(ROOT, b) if b != '.' else ROOT, set())
        ids = sorted(k for k in voice if os.path.exists(os.path.join(ad, k + '.mp3')))
        json.dump(ids, open(os.path.join(dd, 'audio.json'), 'w'))
        removed = 0
        for fn in os.listdir(ad):
            if re.fullmatch(r'[0-9a-f]{10}\.mp3', fn) and fn[:-4] not in keep:
                os.remove(os.path.join(ad, fn))
                removed += 1
        print(b, 'səs:', len(ids), '· silindi:', removed)


asyncio.run(main())
