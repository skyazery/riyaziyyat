# Adding a new book (e.g. 2-2 or 3-1)

Plan it with the owner first: the textbook chapter list (topics follow «Riyaziyyat N» order), the
topic numbers (continue after the last book: 2-1 ends at 69, so 2-2 starts at 70), sections
(about 6, used by the placement test), and the colour.

## Site

1. **Generator:** copy `tools/content21.py` to `tools/contentNN.py`. Reuse `draw.py`/`draw2.py`
   primitives (`expr2`, `tens_ones`, `numline`, `chip`, `em`, `label`, …) and the `Topic` helpers
   `num`, `choice`, `sign`. Write every instruction in the formal register from the start. Each topic
   needs exactly 10 problems (the script prints `COUNT` otherwise) and a concept sentence + picture.
   Mix screen-checkable problems (`num`, `choice`) with notebook ones. Run:
   `python3 tools/contentNN.py ~/riyaziyyat/N-M` → `img/`, `data/topics.json`, `data/voice.json`.
2. **Page:** copy `2-1/index.html` to `N-M/index.html` and change the `BOOK` config (id, first, last,
   key `riyaziyyat-N-M-progress`, title, sub, part, sections, icons, `lvq`, footer, `other`). Add a
   link back from the previous book's `other` (with `next:true` on the forward link).
3. **Book colour:** add `.bk-N-M{--bk1:…;--bk2:…;--bk3:…;--bkink:…}` in `app.css`.
4. **Audio:** add the book folder to `BOOKS` in `tools/tts_all.py` (and `tools/formal.py`), then
   `python3 tools/formal.py` (should report 0 changes) and `python3 tools/tts_all.py`.
5. **Final test:** copy `tools/test21.py` → `testNN.py` (20 items, areas A–E × 4) and
   `build_test21.py` → `build_testNN.py`; fix the hardcoded `/home/claude/riyaziyyat` paths. Run
   tts_all again so the test audio exists.
6. **Teacher page:** adapt `build_muellim21.py`.
7. **README:** add the book section.

## Teacher sheet (apps-script/Code.gs)

The sheet must know the book or the site will refuse to send results (`sagird.js` checks that the
server replies with the same `b`).

- Add `BOOKS['N-M']` with `name`, `color`, `col` (5 new columns after the last used one: STATUS,
  DATE, LV_START, LV_DATE, LV_RETRY), `results` / `level` tab names, `first`, `key` (the 20 test
  answers in test order), `lvAll` (last topic + 1), `lvSections` (same as the page's sections),
  `topics` (titles in order).
- Raise `NCOL` to cover the new columns; update the header comment of the Şagirdlər columns.
- `bookByTopic_()` and the tab order list in `tidySheets()` name the books explicitly — add the new
  one.
- `ALL_TOPICS` is computed automatically.
- Give the owner the new file (open it in TextEdit), and remind them: paste, save, then
  **Deploy → Manage deployments → edit → New version**, then run menu ① 처음 설정 once so the new
  columns/tabs are created.

## Verify

Run `scripts/check_site.py`, open every page of the new book at phone size, take the placement test
once, finish one topic, and open the test page with a personal link (`?s=CODE`) only on a test
student — results are saved in the real sheet and the test can be taken once.
