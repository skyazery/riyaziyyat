# Data formats

## `BOOK` config (in each book's `index.html`)

```js
const BOOK={id:'2-1',praise:'../audio/',first:50,last:69,key:'riyaziyyat-2-1-progress',logo:'📙',
  title:'2-ci sinif riyaziyyat',sub:'Mövzu 50–69 · şəkilli və səsli tapşırıqlar',part:'1',partName:'1-ci hissə',
  sections:[['Ədədlərin müqayisəsi. Sıralama',50,51], ...],      // [name, first topic, last topic]
  icons:{50:'⚖️', ...},                                          // one emoji per topic
  lvq:[[[50,5],[51,6]], ...],   // placement test: per section 2 × [topic, problem index from 0]
  allText:'...', footer:'...',
  other:{id:'1-2',href:'../1-2/',label:'...',text:'...',next:true?}};  // object or list
const KITAB=BOOK.id;
```

`key` is the localStorage key for progress; never rename it for an existing book (children lose stars).

## `topics.json`

```json
{"topics":[{"n":4,"title":"0, 1 və 2 ədədləri","concept":"0 – heç nə yoxdur. ...",
  "conceptImg":"img/t04_c.webp","conceptAudio":"<id>",
  "problems":[ /* exactly 10 */ ]}]}
```

A problem:

| field | meaning |
|---|---|
| `img` | full picture (`img/tNN_KK.webp`), also used on the teacher page |
| `ins` | instruction shown and spoken (formal register) |
| `ans` | answer text for "show answer" and the teacher page |
| `icon` | `write` / `circle` / `draw` / `connect` – notebook hint when not checkable on screen |
| `check` | on-screen typed answer: `{"mode":"num","slots":[7]}` or `{"mode":"sign","slots":[">"],"pairs":[["5","3"]]}` |
| `web` | on-screen tap answer: `{"mode":"choice"|"multi"|"order"|"match"|"dots", "stem":img, "opts":[{"t":"2"}|{"img":...}], "ans":..., "hint"?: "..."}` |
| `audio` | id of the spoken instruction |

Neither `check` nor `web` → "write in the notebook" with a reveal button and self-assessment.
`web.hint` is display-only (no audio) but still formal.

## `voice.json` / `audio.json`

`voice.json` maps id → spoken text. The spoken text is usually `ins` itself; in 1-1 some entries
are a spoken version (e.g. `3 + 3 = 6` → `3 üstəgəl 3 bərabərdir 6`). The id is always
`hashlib.md5(spoken_text.encode()).hexdigest()[:10]`. `audio.json` is the sorted list of ids whose mp3
exists — `tools/tts_all.py` rewrites it.

## Test pages

`<book>/test.html` contains `const DATA = {"items":[...],"areas":...,"levels":...,"overall":...};`.
Each item: `area` (A–E), `skill`, `ins`, `hint`, `kind` (`choice`/`slots`/…), `answer`, `disp`,
`audio` (data URI in 1-1/1-2, id in 2-1). The answer key also lives in `apps-script/Code.gs`
(`BOOKS[id].key`, same order) — if an answer changes, change both.

## Praise sounds

`audio/p_ok1-4.mp3` (correct) and `audio/p_no1-2.mp3` (try again); texts are in `PRAISE` in
`tools/tts_all.py`; regenerate with `python3 tools/tts_all.py --praise`.
