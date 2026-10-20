/**
 * 1-ci sinif riyaziyyat – şagird idarəsi (Google Apps Script)
 *
 * 이 코드는 선생님의 구글 시트에 붙여 넣어 쓰는 프로그램입니다.
 *  - 학생 명단(Şagirdlər)에서 학생마다 고유 코드·개인 링크·왓츠앱 보내기 링크를 만듭니다.
 *  - 학습지 사이트(1-1권: test.html, 1-2권: 1-2/test.html)가 보낸 시험 답안을 채점해 결과 탭에 저장합니다.
 *  - 시험은 책마다 학생당 1번만 저장되고, 저장되는 순간 선생님 텔레그램으로 알림을 보냅니다.
 *  - 레벨테스트(Səviyyə testi) 결과로 책마다 학생의 시작 단원을 정하고, 선생님이 시트에서 바꿀 수 있습니다.
 *
 * Şagirdlər 탭 칸:  A~F 학생 정보 · G~K 1-1권 · L~P 1-2권
 * 개인정보(생년월일, 전화번호)는 이 시트 안에만 있고, 사이트에는 학생 이름만 전달됩니다.
 */

/* ---------------- 설정 ---------------- */
const SH_STUDENTS = 'Şagirdlər';
const SH_SETTINGS = 'Ayarlar';
const DONE = 'Tamamlandı';

// Şagirdlər 탭 열 순서 (1부터)
const C = { NAME: 1, BIRTH: 2, PHONE: 3, CODE: 4, LINK: 5, WA: 6 };
const NCOL = 16;
const BASE_HEADERS = ['Ad (이름)', 'Doğum tarixi (생년월일)', 'Valideyn telefonu (부모 전화)', 'Kod (코드)', 'Şəxsi link (개인 링크)', 'WhatsApp (보내기)'];
const LEVEL_HEADERS = ['Tarix (날짜)', 'Kod', 'Ad (이름)', 'Doğum tarixi', 'Başlanğıc mövzu (시작 단원)', 'Mövzu adı', 'Bölmələr (단계별)', 'Düz / sual (정답 수)', 'Cavablar (기록)'];
const RESULT_HEADERS = ['Tarix (날짜)', 'Kod', 'Ad (이름)', 'Doğum tarixi', 'Bal (점수)', 'Nəticə (등급)', 'A', 'B', 'C', 'D', 'E', 'Səhv (틀린 문제)', 'Kömək (힌트 사용)', 'Cavablar (답안 기록)'];
const AREAS = ['A', 'B', 'C', 'D', 'E'];
const OVERALL = [[18, 'Əla'], [14, 'Yaxşı'], [10, 'Orta'], [0, 'Əlavə dəstək lazımdır']];

/* ---------------- 책별 설정 ----------------
   col: 그 책의 칸 번호 (시험 상태, 시험 날짜, 시작 단원, 레벨테스트 날짜, 재응시 허용)
   key: test.html 의 20문제 정답 (같은 순서)
   lvAll: 레벨테스트에서 모든 단계를 통과했을 때의 값 (마지막 단원 + 1)
   lvSections: 사이트의 6개 단계 (첫 단원, 마지막 단원) */
const BOOKS = {
  '1-1': {
    name: '1-1', color: '#FFE2C2',
    col: { STATUS: 7, DATE: 8, LV_START: 9, LV_DATE: 10, LV_RETRY: 11 },
    results: 'Nəticələr', level: 'Səviyyə', first: 1,
    key: [
      { a: 'A', k: 'choice', ans: 1 }, { a: 'A', k: 'choice', ans: 2 }, { a: 'A', k: 'choice', ans: 1 }, { a: 'A', k: 'choice', ans: 3 },
      { a: 'B', ans: [7] }, { a: 'B', ans: [15] }, { a: 'B', ans: [18] }, { a: 'B', ans: [13, 16] },
      { a: 'C', k: 'choice', ans: 1 }, { a: 'C', ans: ['>', '<'] }, { a: 'C', ans: [1, 3, 6, 9] }, { a: 'C', ans: [7, 9] },
      { a: 'D', ans: [3] }, { a: 'D', ans: [7] }, { a: 'D', ans: [9] }, { a: 'D', ans: [4] },
      { a: 'E', ans: [5] }, { a: 'E', ans: [3] }, { a: 'E', ans: [5] }, { a: 'E', ans: [6] }
    ],
    lvAll: 29,
    lvSections: [[1, 2], [3, 8], [9, 12], [13, 18], [19, 23], [24, 28]],
    topics: ["Əşyanın yeri", "Əşyanın əlaməti", "10-a qədər sayma", "0, 1 və 2 ədədləri", "3, 4 və 5 ədədləri", "6, 7 və 8 ədədləri", "9 və 10 ədədləri", "Sıra sayları", "Azdır, çoxdur", "Ədədlərin müqayisəsi", "Ədəd oxu", "Sıralama", "Ədəd üçlüyü", "Əlavə etmək, artırmaq", "Ədədlərin toplanması", "Ədəd oxu üzərində toplama", "Üç toplananlı ifadələr", "Toplamanın digər üsulları", "Azaltmaq, çıxmaq", "Ədədlərin çıxılması", "Ədəd oxu üzərində çıxma", "Toplama və çıxmanın əlaqəsi", "Məchulun tapılması", "20-yə qədər sayma", "İrəli və geri sayma", "Onluq və təklik", "Ədədlərin müqayisəsi (20-yə qədər)", "Sıralama (20-yə qədər)"]
  },
  '1-2': {
    name: '1-2', color: '#D7F0FF',
    col: { STATUS: 12, DATE: 13, LV_START: 14, LV_DATE: 15, LV_RETRY: 16 },
    results: 'Nəticələr 1-2', level: 'Səviyyə 1-2', first: 29,
    key: [
      { a: 'A', k: 'choice', ans: 2 }, { a: 'A', k: 'choice', ans: 2 }, { a: 'A', k: 'choice', ans: 1 }, { a: 'A', ans: [5] },
      { a: 'B', ans: [17] }, { a: 'B', ans: [13] }, { a: 'B', ans: [16] }, { a: 'B', ans: [15] },
      { a: 'C', ans: [12] }, { a: 'C', ans: [8] }, { a: 'C', ans: [8] }, { a: 'C', ans: [7] },
      { a: 'D', ans: [15, 25] }, { a: 'D', ans: [3, 6] }, { a: 'D', ans: [35] }, { a: 'D', ans: [4] },
      { a: 'E', k: 'choice', ans: 1 }, { a: 'E', ans: [7] }, { a: 'E', ans: [4] }, { a: 'E', ans: [5] }
    ],
    lvAll: 50,
    lvSections: [[29, 31], [32, 34], [35, 37], [38, 41], [42, 47], [48, 49]],
    topics: ["Üçbucaq, dairə, kvadrat, düzbucaqlı", "Fəza fiqurları", "Tam, yarı", "Ədədlərin toplanması", "10-a tamamlamaqla toplama", "Toplamanın digər üsulları", "Ədədlərin çıxılması", "10-a qədər azaltmaqla çıxma", "Toplama və çıxmanın əlaqəsi", "100-ə qədər sayma", "Onluq və təklik", "Qəpik, manat", "Alış-veriş", "Uzun, qısa", "Santimetr", "Ağır, yüngül", "Tutum", "Gün, həftə, ay", "Saat", "Cədvəl, piktoqram", "Diaqram"]
  }
};

function book_(b) { return BOOKS[String(b || '1-1')] || BOOKS['1-1']; }
function topicName_(bk, n) { return bk.topics[n - bk.first] || ''; }

/* ---------------- 시트 메뉴 ---------------- */
function onOpen() {
  SpreadsheetApp.getUi().createMenu('📐 학생 관리')
    .addItem('① 처음 설정 (탭 만들기)', 'setup')
    .addItem('② 새 학생 링크 만들기', 'makeLinks')
    .addSeparator()
    .addItem('텔레그램: 내 채팅 ID 찾기', 'findTelegramChat')
    .addItem('텔레그램: 시험 메시지 보내기', 'testTelegram')
    .addToUi();
}

function setup() {
  const ss = SpreadsheetApp.getActive();
  let st = ss.getSheetByName(SH_STUDENTS) || ss.insertSheet(SH_STUDENTS, 0);
  if (!st.getRange(1, 1).getValue()) {
    st.getRange(1, 1, 1, BASE_HEADERS.length).setValues([BASE_HEADERS]).setFontWeight('bold').setBackground('#FFF0C2');
    st.setFrozenRows(1);
    st.getRange('B:C').setNumberFormat('@'); // 생년월일·전화번호를 글자 그대로 저장
    st.setColumnWidths(1, 6, 150);
  }
  // 책마다 5칸 (예전에 만든 시트에도 빈 칸에만 추가됩니다)
  Object.keys(BOOKS).forEach(id => {
    const bk = BOOKS[id], c = bk.col;
    const heads = ['Test ' + id + ' (테스트)', 'Test tarixi ' + id + ' (날짜)', 'Başlanğıc mövzu ' + id + ' (시작 단원)', 'Səviyyə tarixi ' + id + ' (레벨테스트 날짜)', 'Yenidən ' + id + ' (레벨테스트 재응시)'];
    if (!st.getRange(1, c.STATUS).getValue() || id === '1-1') {
      st.getRange(1, c.STATUS, 1, 5).setValues([heads]).setFontWeight('bold').setBackground(bk.color);
    }
    st.setColumnWidths(c.STATUS, 5, 160);
    st.getRange(2, c.LV_RETRY, Math.max(1, st.getMaxRows() - 1), 1).insertCheckboxes();
    let rs = ss.getSheetByName(bk.results) || ss.insertSheet(bk.results);
    if (!rs.getRange(1, 1).getValue()) {
      rs.getRange(1, 1, 1, RESULT_HEADERS.length).setValues([RESULT_HEADERS]).setFontWeight('bold').setBackground('#E3F7EA');
      rs.setFrozenRows(1);
    }
    let lv = ss.getSheetByName(bk.level) || ss.insertSheet(bk.level);
    if (!lv.getRange(1, 1).getValue()) {
      lv.getRange(1, 1, 1, LEVEL_HEADERS.length).setValues([LEVEL_HEADERS]).setFontWeight('bold').setBackground(bk.color);
      lv.setFrozenRows(1);
    }
  });
  let se = ss.getSheetByName(SH_SETTINGS) || ss.insertSheet(SH_SETTINGS);
  if (!se.getRange(1, 1).getValue()) {
    se.getRange(1, 1, 3, 3).setValues([
      ['SAYT_LINKI', 'https://skyazery.github.io/riyaziyyat/', '학습지 사이트 주소'],
      ['TELEGRAM_BOT_TOKEN', '', 'BotFather 에게 받은 봇 토큰 (다른 사람에게 보여 주지 마세요)'],
      ['TELEGRAM_CHAT_ID', '', '메뉴 「텔레그램: 내 채팅 ID 찾기」로 자동 입력']
    ]);
    se.getRange('A1:A3').setFontWeight('bold');
    se.setColumnWidth(2, 380);
  }
  SpreadsheetApp.getUi().alert('준비 완료! Şagirdlər 탭에 학생 이름·생년월일·부모 전화번호를 적고 「② 새 학생 링크 만들기」를 누르세요.\n\n' +
    '칸 안내: G~K = 1-1권, L~P = 1-2권.\n' +
    '「시작 단원」칸은 학생이 레벨테스트를 보면 자동으로 채워집니다. 숫자를 직접 바꾸면 그 단원부터 시작하고(1-1권 1~28, 1-2권 29~49), 비우면 레벨테스트를 다시 봅니다. 「재응시」칸에 체크하면 한 번 더 볼 수 있습니다.');
}

/* ---------------- 학생 링크 만들기 ---------------- */
function makeLinks() {
  const st = sheet_(SH_STUDENTS);
  const site = setting_('SAYT_LINKI') || 'https://skyazery.github.io/riyaziyyat/';
  const last = st.getLastRow();
  if (last < 2) { SpreadsheetApp.getUi().alert('Şagirdlər 탭 2번째 줄부터 학생을 적어 주세요.'); return; }
  const rows = st.getRange(2, 1, last - 1, NCOL).getValues();
  const used = {};
  rows.forEach(r => { if (r[C.CODE - 1]) used[String(r[C.CODE - 1])] = true; });
  let made = 0;
  rows.forEach((r, i) => {
    const name = String(r[C.NAME - 1]).trim();
    if (!name) return;
    const row = i + 2;
    let code = String(r[C.CODE - 1]).trim();
    if (!code) {
      do { code = newCode_(); } while (used[code]);
      used[code] = true;
      st.getRange(row, C.CODE).setValue(code);
      made++;
    }
    const link = site.replace(/\/?$/, '/') + '?s=' + code;
    st.getRange(row, C.LINK).setValue(link);
    const phone = waPhone_(r[C.PHONE - 1]);
    const cell = st.getRange(row, C.WA);
    if (phone) {
      const msg = 'Salam! Bu, ' + name + ' üçün riyaziyyat tapşırıqlarının şəxsi linkidir:\n' + link +
        '\n\nLinki ilk dəfə açanda qısa səviyyə testi olacaq – uşağın hansı mövzudan başlamalı olduğunu göstərir.' +
        '\nTapşırıqları istədiyiniz qədər həll edə bilərsiniz. Hər hissənin sonunda olan yoxlama testi isə yalnız bir dəfə edilir.' +
        '\n2-ci hissə də eyni linkdən açılır (səhifənin aşağısında).' +
        '\nNəticəni sonra da bu linklə görə bilərsiniz. Xahiş edirik, linki başqası ilə paylaşmayın.';
      const url = 'https://wa.me/' + phone + '?text=' + encodeURIComponent(msg);
      cell.setRichTextValue(SpreadsheetApp.newRichTextValue().setText('💬 Göndər').setLinkUrl(url).build());
    } else {
      cell.setValue('전화번호 확인');
    }
  });
  SpreadsheetApp.getUi().alert('새 링크 ' + made + '개를 만들었어요. F칸의 「💬 Göndər」를 누르면 왓츠앱이 열립니다.');
}

function newCode_() {
  const A = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789'; // 헷갈리는 글자(0,O,1,I) 제외
  let s = '';
  for (let i = 0; i < 6; i++) s += A.charAt(Math.floor(Math.random() * A.length));
  return s;
}

// 조지아 번호 → 왓츠앱 형식 (예: 555 12 34 56 → 995555123456)
function waPhone_(v) {
  let d = String(v || '').replace(/\D/g, '');
  if (!d) return '';
  if (d.indexOf('00') === 0) d = d.slice(2);
  if (d.charAt(0) === '0') d = d.slice(1);
  if (d.length === 9) d = '995' + d;
  return d.length >= 10 ? d : '';
}

/* ---------------- 사이트와 주고받기 ---------------- */
function doGet(e) {
  const p = (e && e.parameter) || {};
  if (p.action === 'student') return json_(studentInfo_(cleanCode_(p.s), book_(p.b)));
  return json_({ ok: true, app: 'riyaziyyat' });
}

function doPost(e) {
  let body = {};
  try { body = JSON.parse(e.postData.contents); } catch (err) { return json_({ ok: false, error: 'bad' }); }
  const bk = book_(body.b);
  if (body.action === 'level') return saveLevel_(body, bk);
  if (body.action !== 'submit') return json_({ ok: false, error: 'bad' });
  const code = cleanCode_(body.s);
  const lock = LockService.getScriptLock();
  lock.waitLock(20000);
  try {
    const found = findStudent_(code, bk);
    if (!found) return json_({ ok: false, error: 'notfound' });
    if (found.status === DONE) {
      // 이미 시험을 봤으면 새 답안은 저장하지 않고 처음 결과를 돌려줍니다
      return json_(Object.assign({ already: true }, studentInfo_(code, bk)));
    }
    const ans = sanitizeAns_(body.ans, bk.key);
    const hints = (Array.isArray(body.hints) ? body.hints : []).map(Number).filter(n => n >= 0 && n < bk.key.length);
    const sc = score_(ans, bk.key);
    const now = new Date();
    const tz = Session.getScriptTimeZone();
    const dateStr = Utilities.formatDate(now, tz, 'dd.MM.yyyy');
    const birth = fmtBirth_(found.birth);
    sheet_(bk.results).appendRow([
      Utilities.formatDate(now, tz, 'yyyy-MM-dd HH:mm'), code, found.name, birth, sc.total, sc.level,
      sc.per.A, sc.per.B, sc.per.C, sc.per.D, sc.per.E,
      sc.wrong.length ? sc.wrong.join(', ') : '-', hints.length,
      JSON.stringify({ ans: ans, hints: hints, date: dateStr })
    ]);
    const st = sheet_(SH_STUDENTS);
    st.getRange(found.row, bk.col.STATUS).setValue(DONE);
    st.getRange(found.row, bk.col.DATE).setValue(dateStr);
    SpreadsheetApp.flush();
    notify_(bk, found.name, birth, sc, hints.length);
    return json_({ ok: true, name: found.name, done: true, result: { ans: ans, hints: hints, date: dateStr } });
  } finally {
    lock.releaseLock();
  }
}

function studentInfo_(code, bk) {
  const f = findStudent_(code, bk);
  if (!f) return { ok: false, error: 'notfound' };
  const out = { ok: true, name: f.name, done: f.status === DONE, level: levelInfo_(f, bk) };
  if (out.done) out.result = lastResult_(code, bk);
  return out;
}

/* ---------------- 레벨테스트 저장 ---------------- */
function levelInfo_(f, bk) {
  const start = parseInt(f.lvStart, 10);
  const ok = start >= bk.first && start <= bk.lvAll;
  return { done: ok, start: ok ? start : null, date: fmtBirth_(f.lvDate), retry: f.lvRetry === true };
}

function saveLevel_(body, bk) {
  const code = cleanCode_(body.s);
  const start = parseInt(body.start, 10);
  if (!(start >= bk.first && start <= bk.lvAll)) return json_({ ok: false, error: 'bad' });
  const log = (Array.isArray(body.log) ? body.log : []).slice(0, 12)
    .map(e => (Array.isArray(e) ? [Number(e[0]) || 0, Number(e[1]) || 0, e[2] ? 1 : 0] : null))
    .filter(e => e && e[0] >= bk.first && e[0] < bk.lvAll);
  const lock = LockService.getScriptLock();
  lock.waitLock(20000);
  try {
    const found = findStudent_(code, bk);
    if (!found) return json_({ ok: false, error: 'notfound' });
    const cur = levelInfo_(found, bk);
    if (cur.done && !cur.retry) return json_({ ok: true, already: true, level: cur });
    const now = new Date();
    const tz = Session.getScriptTimeZone();
    const dateStr = Utilities.formatDate(now, tz, 'dd.MM.yyyy');
    const birth = fmtBirth_(found.birth);
    const steps = levelSteps_(log, bk);
    const right = log.filter(e => e[2]).length;
    const all = start >= bk.lvAll;
    const tname = all ? 'Hamısı keçildi (모든 단원 통과)' : topicName_(bk, start);
    sheet_(bk.level).appendRow([
      Utilities.formatDate(now, tz, 'yyyy-MM-dd HH:mm'), code, found.name, birth, all ? 'Hamısı' : start, tname,
      steps, right + ' / ' + log.length, JSON.stringify(log)
    ]);
    const st = sheet_(SH_STUDENTS);
    st.getRange(found.row, bk.col.LV_START).setValue(start);
    st.getRange(found.row, bk.col.LV_DATE).setValue(dateStr);
    st.getRange(found.row, bk.col.LV_RETRY).setValue(false);
    SpreadsheetApp.flush();
    sendTelegram_('🧭 레벨테스트 ' + bk.name + '권 · ' + found.name + (birth ? ' (' + birth + ')' : '') + '\n' +
      (all ? '모든 단계 통과 → 복습 후 최종 테스트 가능' : '시작 단원: Mövzu ' + start + '. ' + tname) + '\n' +
      steps + '\n정답 ' + right + ' / ' + log.length + (cur.done ? ' · 재응시' : ''));
    return json_({ ok: true, level: { done: true, start: start, date: dateStr, retry: false } });
  } finally {
    lock.releaseLock();
  }
}

// 단계별 결과: 예) "1✓ 2✓ 3✗" (단계 = 사이트의 6개 bölmə)
function levelSteps_(log, bk) {
  const res = {};
  log.forEach(e => {
    const i = bk.lvSections.findIndex(r => e[0] >= r[0] && e[0] <= r[1]);
    if (i < 0) return;
    res[i] = (res[i] === undefined ? true : res[i]) && !!e[2];
  });
  return Object.keys(res).map(Number).sort((a, b) => a - b).map(i => (i + 1) + (res[i] ? '✓' : '✗')).join(' ') || '-';
}

function findStudent_(code, bk) {
  if (!code) return null;
  const st = sheet_(SH_STUDENTS);
  const last = st.getLastRow();
  if (last < 2) return null;
  const rows = st.getRange(2, 1, last - 1, NCOL).getValues();
  const c = bk.col;
  for (let i = 0; i < rows.length; i++) {
    if (String(rows[i][C.CODE - 1]).trim().toUpperCase() === code) {
      const r = rows[i];
      return { row: i + 2, name: String(r[C.NAME - 1]).trim(), birth: r[C.BIRTH - 1], status: String(r[c.STATUS - 1]).trim(),
        lvStart: r[c.LV_START - 1], lvDate: r[c.LV_DATE - 1], lvRetry: r[c.LV_RETRY - 1] };
    }
  }
  return null;
}

function lastResult_(code, bk) {
  const rs = SpreadsheetApp.getActive().getSheetByName(bk.results);
  if (!rs) return null;
  const last = rs.getLastRow();
  if (last < 2) return null;
  const rows = rs.getRange(2, 1, last - 1, RESULT_HEADERS.length).getValues();
  for (let i = rows.length - 1; i >= 0; i--) {
    if (String(rows[i][1]) === code) {
      try { return JSON.parse(rows[i][RESULT_HEADERS.length - 1]); } catch (e) { return null; }
    }
  }
  return null;
}

/* ---------------- 채점 ---------------- */
function sanitizeAns_(raw, KEY) {
  const out = {};
  if (!raw || typeof raw !== 'object') return out;
  KEY.forEach((it, k) => {
    const v = raw[k];
    if (v === undefined || v === null) return;
    if (it.k === 'choice') { if (typeof v === 'number') out[k] = v; }
    else if (Array.isArray(v)) out[k] = v.slice(0, it.ans.length).map(x => (x === null ? null : String(x).slice(0, 3)));
  });
  return out;
}

function score_(ans, KEY) {
  const per = { A: 0, B: 0, C: 0, D: 0, E: 0 };
  const wrong = [];
  let total = 0;
  KEY.forEach((it, k) => {
    const a = ans[k];
    let ok = false;
    if (a !== undefined) ok = it.k === 'choice' ? a === it.ans : it.ans.every((v, j) => String(a[j]) === String(v));
    if (ok) { per[it.a]++; total++; } else wrong.push(k + 1);
  });
  const level = OVERALL.find(o => total >= o[0])[1];
  return { total: total, per: per, wrong: wrong, level: level };
}

/* ---------------- 텔레그램 ---------------- */
function notify_(bk, name, birth, sc, hints) {
  const text = '📊 ' + bk.name + '권 시험 · ' + name + (birth ? ' (' + birth + ')' : '') + '\n' +
    sc.total + '/20 · ' + sc.level + '\n' +
    AREAS.map(a => a + ' ' + sc.per[a] + '/4').join(' · ') + '\n' +
    '틀린 문제: ' + (sc.wrong.length ? sc.wrong.join(', ') : '없음') + ' · 힌트: ' + hints;
  sendTelegram_(text);
}

function sendTelegram_(text) {
  const token = setting_('TELEGRAM_BOT_TOKEN'), chat = setting_('TELEGRAM_CHAT_ID');
  if (!token || !chat) return false;
  try {
    const r = UrlFetchApp.fetch('https://api.telegram.org/bot' + token + '/sendMessage',
      { method: 'post', payload: { chat_id: chat, text: text }, muteHttpExceptions: true });
    return r.getResponseCode() === 200;
  } catch (e) { return false; }
}

function findTelegramChat() {
  const ui = SpreadsheetApp.getUi();
  const token = setting_('TELEGRAM_BOT_TOKEN');
  if (!token) { ui.alert('Ayarlar 탭 B2 칸에 봇 토큰을 먼저 넣어 주세요.'); return; }
  const r = UrlFetchApp.fetch('https://api.telegram.org/bot' + token + '/getUpdates', { muteHttpExceptions: true });
  const data = JSON.parse(r.getContentText() || '{}');
  if (!data.ok) { ui.alert('토큰이 맞지 않아요. BotFather 에게 받은 토큰을 다시 확인해 주세요.'); return; }
  const msgs = (data.result || []).map(u => u.message || u.my_chat_member || u.channel_post).filter(Boolean);
  if (!msgs.length) { ui.alert('텔레그램에서 내 봇을 열고 /start 또는 아무 메시지를 보낸 뒤 다시 눌러 주세요.'); return; }
  const chat = msgs[msgs.length - 1].chat;
  sheet_(SH_SETTINGS).getRange('B3').setValue(String(chat.id));
  ui.alert('채팅 ID 저장 완료: ' + (chat.title || chat.first_name || '') + '\n이제 「텔레그램: 시험 메시지 보내기」로 확인해 보세요.');
}

function testTelegram() {
  const ok = sendTelegram_('✅ 학생 관리 알림 연결 완료! 시험 결과가 여기로 옵니다.');
  SpreadsheetApp.getUi().alert(ok ? '텔레그램을 확인해 보세요!' : '보내지 못했어요. Ayarlar 탭의 토큰과 채팅 ID를 확인해 주세요.');
}

/* ---------------- 도우미 ---------------- */
function sheet_(name) {
  const s = SpreadsheetApp.getActive().getSheetByName(name);
  if (!s) throw new Error('「' + name + '」 탭이 없어요. 메뉴 ① 처음 설정을 먼저 눌러 주세요.');
  return s;
}

function setting_(key) {
  const s = SpreadsheetApp.getActive().getSheetByName(SH_SETTINGS);
  if (!s) return '';
  const rows = s.getRange(1, 1, Math.max(1, s.getLastRow()), 2).getValues();
  for (const r of rows) if (String(r[0]).trim() === key) return String(r[1]).trim();
  return '';
}

function cleanCode_(s) {
  const c = String(s || '').trim().toUpperCase();
  return /^[A-Z0-9]{6}$/.test(c) ? c : '';
}

function fmtBirth_(v) {
  if (v instanceof Date) return Utilities.formatDate(v, Session.getScriptTimeZone(), 'dd.MM.yyyy');
  return String(v || '').trim();
}

function json_(o) {
  return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON);
}
