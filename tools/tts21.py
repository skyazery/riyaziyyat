"""Səslər (2-1): az-AZ-BanuNeural, ton +17Hz, normal sürət; əvvəldəki səssizlik kəsilir, sonda 0.2 s qalır.
Mövzu girişinin səsinin əvvəlinə 1-ci və 2-ci hissədəki salamlama əlavə olunur.
Run: python3 tts21.py BOOKDIR [extra_voice.json ...]   (BOOKDIR/data/voice.json, BOOKDIR/data/topics.json)"""
import asyncio, json, os, subprocess, sys, tempfile
import certifi
certifi.where = lambda: os.environ.get('SSL_CERT_FILE', '/root/.ccr/ca-bundle.crt')
import edge_tts

BOOK = sys.argv[1]
ROOT = os.path.dirname(os.path.abspath(BOOK.rstrip('/')))
VOICE, PITCH, RATE = 'az-AZ-BanuNeural', '+17Hz', '+0%'
GREET_SRC = os.path.join(ROOT, '1-2', 'audio', '4fb7a9b7b8.mp3')  # 1-2, mövzu 29 girişi: salamlama 0–3.95 s
OUTDIR = os.path.join(BOOK, 'audio')
os.makedirs(OUTDIR, exist_ok=True)

voice = json.load(open(os.path.join(BOOK, 'data', 'voice.json')))
for extra in sys.argv[2:]:
    voice.update(json.load(open(extra)))
concepts = {t['conceptAudio'] for t in json.load(open(os.path.join(BOOK, 'data', 'topics.json')))['topics']}
TRIM = 'silenceremove=start_periods=1:start_threshold=-50dB,areverse,silenceremove=start_periods=1:start_threshold=-50dB,areverse'
tmp = tempfile.mkdtemp()
greet = os.path.join(tmp, 'greet.wav')
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', GREET_SRC, '-t', '3.95', '-ar', '24000', '-ac', '1', greet], check=True)


def finish(raw, out, with_greet):
    clean = raw + '.wav'
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', raw, '-af', TRIM + ',apad=pad_dur=0.2', '-ar', '24000', '-ac', '1', clean], check=True)
    if with_greet:
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', greet, '-i', clean, '-filter_complex', '[0:a][1:a]concat=n=2:v=0:a=1',
                        '-ar', '24000', '-ac', '1', '-b:a', '48k', out], check=True)
    else:
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', clean, '-ar', '24000', '-ac', '1', '-b:a', '48k', out], check=True)


async def one(sem, k, text):
    out = os.path.join(OUTDIR, k + '.mp3')
    if os.path.exists(out):
        return 'skip'
    async with sem:
        raw = os.path.join(tmp, k + '.mp3')
        for attempt in range(4):
            try:
                await edge_tts.Communicate(text, VOICE, pitch=PITCH, rate=RATE).save(raw)
                break
            except Exception as e:
                if attempt == 3:
                    print('FAIL', k, e)
                    return 'fail'
                await asyncio.sleep(2 + attempt * 3)
    await asyncio.to_thread(finish, raw, out, k in concepts)
    return 'ok'


async def main():
    sem = asyncio.Semaphore(6)
    res = await asyncio.gather(*[one(sem, k, v) for k, v in voice.items()])
    print({r: res.count(r) for r in set(res)})
    ids = sorted(k for k in voice if os.path.exists(os.path.join(OUTDIR, k + '.mp3')))
    json.dump(ids, open(os.path.join(BOOK, 'data', 'audio.json'), 'w'))
    print('audio.json', len(ids))

asyncio.run(main())
