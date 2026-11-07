---
name: riyaziyyat-site
description: How to change the Riyaziyyat Dostu math worksheet site (skyazery/riyaziyyat, GitHub Pages) without breaking it — editing or adding problems, topics and whole books (1-1, 1-2, 2-1, 2-2, 3-1, 3-2), changing on-screen wording, regenerating the Azerbaijani TTS audio, design/UI changes in app.js/app.css, the test and teacher pages, and deploying through main. Use this whenever the user works on this repository or talks about the worksheet site, 학습지, mövzu, tapşırıq, səs (audio), 새 책/새 권, 문구 수정, 디자인 수정, or putting changes "on the real site", even if they don't name files. Also use it before touching apps-script/Code.gs because the sheet program and the site must stay in step.
---

# Riyaziyyat Dostu – worksheet site

A static site for Azerbaijani-speaking 1st–2nd graders in Georgia: picture worksheets with a
fox teacher who reads every instruction aloud, a placement test, a final test, a parent report and
a teacher page. It is served by GitHub Pages from `main` of `skyazery/riyaziyyat`; the teacher's
Google Sheet (Apps Script in `apps-script/Code.gs`) stores students, logs and reports.

The owner is a non-developer who speaks Korean with Claude. Explain in plain Korean, keep jargon
out, and say clearly what is live and what is not.

## Map of the repo

| Path | What it is |
|---|---|
| `index.html`, `1-2/`, `2-1/`, `2-2/`, `3-1/`, `3-2/` `index.html` | One page per book. Only a `BOOK={...}` config differs (id, first/last topic, sections, icons, `lvq` placement questions, links to other books). |
| `app.js`, `app.css`, `base.css`, `sagird.js` | Shared code for all books. One change here changes every book. |
| `<book>/data/topics.json` | Topics → 10 problems each (`ins` text, `img`, `check` or `web`, `audio` id). |
| `<book>/data/voice.json` | audio id → the exact text that was spoken. |
| `<book>/data/audio.json` | list of audio ids that have an mp3 (the app only plays ids listed here). |
| `<book>/audio/<id>.mp3`, `audio/p_ok1-4.mp3`, `audio/p_no1-2.mp3` | Spoken instructions; praise sounds (root only). |
| `<book>/test.html` | Final test; items in `const DATA = {...}` (1-1 and 1-2 embed audio as data URIs, 2-1 uses ids). |
| `<book>/muellim.html` | Teacher page (answers, guidance). Generated, but plain HTML. |
| `hesabat.html`, `qeydiyyat.html` | Parent report, parent consent form. |
| `tools/content.py` (1-2), `tools/content21.py` (2-1), `content22.py` (2-2), `content31.py`/`content32.py` (3rd grade, helpers in `bookgen.py`) + `draw.py`, `draw2.py` | Generators that draw images and write topics.json/voice.json. There is **no generator for 1-1** — edit its JSON directly. |
| `tools/test12.py`, `test21.py`, `build_test21.py`, `build_muellim21.py` | Test / teacher page generators (paths inside are hardcoded to `/home/claude/riyaziyyat`; pass or patch paths before running). |
| `tools/formal.py` | Converts informal imperatives to the formal form. |
| `tools/tts_all.py` | Makes missing audio, updates audio.json, deletes unused mp3s, refreshes test audio. |
| `apps-script/Code.gs` | The teacher sheet program. Copy-pasted into the sheet by the owner, not deployed by git. |

Details on file formats: `references/data-format.md`. Adding a whole new book: `references/new-book.md`.

## House rules (and why)

1. **Formal register everywhere.** Every instruction, hint, button and message addresses the reader
   with the polite plural: `yazın, sayın, toxunun, baxın, başlayın, dinləyin, edin, gedin, düzün,
   tapdınız, çalışdınız, bilərsiniz, sizi`. The owner asked for this explicitly. After writing any
   Azerbaijani text, run it through `tools/formal.py` (`from formal import formal`) or check by eye.
   Things that look like verbs but are not: `düz bucaq/düz xətt` (adjective), `alma` (apple),
   `5 çıx 3` (minus, spoken). Quoted speech a parent says to a child inside «…» on teacher/parent
   pages stays as written.
2. **Text and audio must match.** An audio id is `md5(text)[:10]` of the spoken text. If you change
   an `ins`/`concept` text, its spoken text in `voice.json` must change too, the id changes, and a new
   mp3 is needed. Never leave a problem whose text says one thing and whose voice says another, and
   never hand-edit ids. The safe sequence: edit text → `python3 tools/formal.py --apply` (it rewrites
   ids for changed texts) → `python3 tools/tts_all.py`. Many problems share one sentence and one
   audio id; when only one of them should change, give that problem the new text and id and leave
   the others pointing at the old id (tts_all keeps every mp3 that is still referenced).
3. **Audio is made one way only:** `tools/tts_all.py` — voice `az-AZ-BanuNeural`, pitch `+17Hz`,
   normal rate, silence trimmed, 0.2 s tail, and concept (topic intro) audio gets the greeting from
   `tools/greet.mp3` in front. Needs `pip install --user -U edge-tts imageio-ffmpeg` (ask the user
   before installing; an old edge-tts gets HTTP 403). Run it in the background; ~400 files take a few
   minutes. It must end with `{'ok': N}` and no `fail`; if anything fails, rerun (finished files are kept).
4. **10 problems per topic, topics numbered across books** (1-1: 1–28, 1-2: 29–49, 2-1: 50–69, 2-2: 70–91, 3-1: 92–116, 3-2: 117–142).
   The Apps Script, placement test and reports rely on these numbers.
5. **Shared code, three books.** A change to `app.js`/`app.css` must be checked in every book.
   Keep `app.js` dependency-free and readable for the owner; comments in Azerbaijani like the rest.
6. **Design language:** warm cream background, Nunito 600–900, rounded cards (20–26px), chunky
   buttons with a darker bottom shadow, book colours (1-1 blue, 1-2 green, 2-1 orange, 2-2 purple, 3-1 teal, 3-2 pink), green =
   done/correct, amber `#F0A020` = today/active, dashed grey = locked. On a phone (375×812) the
   picture, answer box and number pad of a problem must fit on one screen without scrolling — that is
   why the teacher card is a one-line `.teach.mini` on problems. Respect `prefers-reduced-motion`
   and dark mode tokens in `base.css`. Show mockups to the owner before large visual changes.
7. **Children use phones.** Big tap targets (≥52px), no hover-only UI, nothing important below the
   sticky bottom bar (`showFb()` scrolls feedback into view), and a wrong answer must be easy to
   retype (the keypad replaces the old digit after a wrong check).
8. **Privacy:** the site only ever receives the student's name from the sheet. Don't add anything
   that sends phone numbers, birth dates or other data to the site or a third party.

## Workflow

Work on a branch (`git switch -c <topic>`), never straight on `main`.

1. **Understand the request** in the owner's words; if wording in Azerbaijani is involved, show the
   exact before → after sentences.
2. **Make the change** with the rules above. For generated books (1-2, 2-1, 2-2, 3-1, 3-2) change the generator
   string too, so a future regeneration doesn't bring the old text back.
3. **Regenerate audio** if any spoken text changed (rule 2–3).
4. **Run the checker:** `python3 .claude/skills/riyaziyyat-site/scripts/check_site.py` — it fails on
   missing audio, wrong problem counts, broken references and informal verbs left in data or UI.
5. **Look at it in a browser at phone size.** Serve the repo locally
   (`python3 -m http.server 8765 --bind 127.0.0.1 --directory ~/riyaziyyat`, or a `.claude/launch.json`
   entry for the built-in browser), set the viewport to mobile (375×812), and for each touched book
   open home, a topic intro, a number problem (try a wrong answer, then the right one), and a tap
   problem. Check the console for errors. Put fake progress in `localStorage[BOOK.key]` to see
   done/today/locked cards, and set `sessionStorage['riyaziyyat-lv-auto-'+BOOK.id]='1'` to skip the
   automatic placement test.
6. **Commit** with an Azerbaijani message in the repo's style (short title, bullet body) and the
   co-author line from the session. Push the branch.
7. **Go live only when the owner says so:** merge the branch into `main` and push; GitHub Pages
   updates in about a minute. Then verify the live site actually serves the change (fetch a changed
   file with a cache-busting query) before saying it is live. Tell the owner that phones may need a
   refresh.

## When Code.gs is involved

The sheet program is pasted by the owner into Extensions → Apps Script and published with
**Deploy → Manage deployments → edit (pencil) → New version** (a "New deployment" changes the URL in
`sagird.js` and breaks the site). Keep its JSON replies (`ok`, `error`, `daily`, `level`, …)
backward compatible with `sagird.js`/`app.js`. `pbcopy` does not reach the owner's clipboard from
this environment, so don't claim you copied anything; open the file in TextEdit (`open -e apps-script/Code.gs`) so they
can ⌘A ⌘C, and tell them to search for a new function name to confirm the paste. A new book needs
changes there too (see `references/new-book.md`).

## Reporting back

End with a short Korean summary: what changed, where it can be seen, whether it is live, and what
was not verified (for example "audio generated but not listened to"). When many Azerbaijani
sentences changed, give the owner a before/after list (TSV) to proofread.
