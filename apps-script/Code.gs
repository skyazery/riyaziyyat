/**
 * 1-ci sinif riyaziyyat – şagird idarəsi (Google Apps Script)
 *
 * 이 코드는 선생님의 구글 시트에 붙여 넣어 쓰는 프로그램입니다.
 *  - 학생 명단(Şagirdlər)에서 학생마다 고유 코드·개인 링크·왓츠앱 보내기 링크를 만듭니다.
 *  - 학습지 사이트(test.html)가 보낸 시험 답안을 여기서 채점해 결과(Nəticələr) 탭에 저장합니다.
 *  - 학생당 1번만 저장되고, 저장되는 순간 선생님 텔레그램으로 알림을 보냅니다.
 *
 * 개인정보(생년월일, 전화번호)는 이 시트 안에만 있고, 사이트에는 학생 이름만 전달됩니다.
 */

/* ---------------- 설정 ---------------- */
const SH_STUDENTS = 'Şagirdlər';
const SH_RESULTS = 'Nəticələr';
const SH_SETTINGS = 'Ayarlar';
const DONE = 'Tamamlandı';

// Şagirdlər 탭 열 순서 (1부터)
const C = { NAME: 1, BIRTH: 2, PHONE: 3, CODE: 4, LINK: 5, WA: 6, STATUS: 7, DATE: 8 };
const STUDENT_HEADERS = ['Ad (이름)', 'Doğum tarixi (생년월일)', 'Valideyn telefonu (부모 전화)', 'Kod (코드)', 'Şəxsi link (개인 링크)', 'WhatsApp (보내기)', 'Test (테스트)', 'Test tarixi (날짜)'];
const RESULT_HEADERS = ['Tarix (날짜)', 'Kod', 'Ad (이름)', 'Doğum tarixi', 'Bal (점수)', 'Nəticə (등급)', 'A', 'B', 'C', 'D', 'E', 'Səhv (틀린 문제)', 'Kömək (힌트 사용)', 'Cavablar (답안 기록)'];

/* ---------------- 시험 정답 (test.html 의 20문제와 같은 순서) ---------------- */
const KEY = [
  { a: 'A', k: 'choice', ans: 1 }, { a: 'A', k: 'choice', ans: 2 }, { a: 'A', k: 'choice', ans: 1 }, { a: 'A', k: 'choice', ans: 3 },
  { a: 'B', ans: [7] }, { a: 'B', ans: [15] }, { a: 'B', ans: [18] }, { a: 'B', ans: [13, 16] },
  { a: 'C', k: 'choice', ans: 1 }, { a: 'C', ans: ['>', '<'] }, { a: 'C', ans: [1, 3, 6, 9] }, { a: 'C', ans: [7, 9] },
  { a: 'D', ans: [3] }, { a: 'D', ans: [7] }, { a: 'D', ans: [9] }, { a: 'D', ans: [4] },
  { a: 'E', ans: [5] }, { a: 'E', ans: [3] }, { a: 'E', ans: [5] }, { a: 'E', ans: [6] }
];
const AREAS = ['A', 'B', 'C', 'D', 'E'];
const OVERALL = [[18, 'Əla'], [14, 'Yaxşı'], [10, 'Orta'], [0, 'Əlavə dəstək lazımdır']];

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
    st.getRange(1, 1, 1, STUDENT_HEADERS.length).setValues([STUDENT_HEADERS]).setFontWeight('bold').setBackground('#FFF0C2');
    st.setFrozenRows(1);
    st.getRange('B:C').setNumberFormat('@'); // 생년월일·전화번호를 글자 그대로 저장
    st.setColumnWidths(1, 8, 150);
  }
  let rs = ss.getSheetByName(SH_RESULTS) || ss.insertSheet(SH_RESULTS, 1);
  if (!rs.getRange(1, 1).getValue()) {
    rs.getRange(1, 1, 1, RESULT_HEADERS.length).setValues([RESULT_HEADERS]).setFontWeight('bold').setBackground('#E3F7EA');
    rs.setFrozenRows(1);
  }
  let se = ss.getSheetByName(SH_SETTINGS) || ss.insertSheet(SH_SETTINGS, 2);
  if (!se.getRange(1, 1).getValue()) {
    se.getRange(1, 1, 3, 3).setValues([
      ['SAYT_LINKI', 'https://skyazery.github.io/riyaziyyat/', '학습지 사이트 주소'],
      ['TELEGRAM_BOT_TOKEN', '', 'BotFather 에게 받은 봇 토큰 (다른 사람에게 보여 주지 마세요)'],
      ['TELEGRAM_CHAT_ID', '', '메뉴 「텔레그램: 내 채팅 ID 찾기」로 자동 입력']
    ]);
    se.getRange('A1:A3').setFontWeight('bold');
    se.setColumnWidth(2, 380);
  }
  SpreadsheetApp.getUi().alert('준비 완료! Şagirdlər 탭에 학생 이름·생년월일·부모 전화번호를 적고 「② 새 학생 링크 만들기」를 누르세요.');
}

/* ---------------- 학생 링크 만들기 ---------------- */
function makeLinks() {
  const st = sheet_(SH_STUDENTS);
  const site = setting_('SAYT_LINKI') || 'https://skyazery.github.io/riyaziyyat/';
  const last = st.getLastRow();
  if (last < 2) { SpreadsheetApp.getUi().alert('Şagirdlər 탭 2번째 줄부터 학생을 적어 주세요.'); return; }
  const rows = st.getRange(2, 1, last - 1, 8).getValues();
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
        '\n\nTapşırıqları istədiyiniz qədər həll edə bilərsiniz. Ən sonda olan yoxlama testi isə yalnız bir dəfə edilir.' +
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
  if (p.action === 'student') return json_(studentInfo_(cleanCode_(p.s)));
  return json_({ ok: true, app: 'riyaziyyat' });
}

function doPost(e) {
  let body = {};
  try { body = JSON.parse(e.postData.contents); } catch (err) { return json_({ ok: false, error: 'bad' }); }
  if (body.action !== 'submit') return json_({ ok: false, error: 'bad' });
  const code = cleanCode_(body.s);
  const lock = LockService.getScriptLock();
  lock.waitLock(20000);
  try {
    const found = findStudent_(code);
    if (!found) return json_({ ok: false, error: 'notfound' });
    if (found.status === DONE) {
      // 이미 시험을 봤으면 새 답안은 저장하지 않고 처음 결과를 돌려줍니다
      return json_(Object.assign({ already: true }, studentInfo_(code)));
    }
    const ans = sanitizeAns_(body.ans);
    const hints = (Array.isArray(body.hints) ? body.hints : []).map(Number).filter(n => n >= 0 && n < KEY.length);
    const sc = score_(ans);
    const now = new Date();
    const tz = Session.getScriptTimeZone();
    const dateStr = Utilities.formatDate(now, tz, 'dd.MM.yyyy');
    const birth = fmtBirth_(found.birth);
    sheet_(SH_RESULTS).appendRow([
      Utilities.formatDate(now, tz, 'yyyy-MM-dd HH:mm'), code, found.name, birth, sc.total, sc.level,
      sc.per.A, sc.per.B, sc.per.C, sc.per.D, sc.per.E,
      sc.wrong.length ? sc.wrong.join(', ') : '-', hints.length,
      JSON.stringify({ ans: ans, hints: hints, date: dateStr })
    ]);
    const st = sheet_(SH_STUDENTS);
    st.getRange(found.row, C.STATUS).setValue(DONE);
    st.getRange(found.row, C.DATE).setValue(dateStr);
    SpreadsheetApp.flush();
    notify_(found.name, birth, sc, hints.length);
    return json_({ ok: true, name: found.name, done: true, result: { ans: ans, hints: hints, date: dateStr } });
  } finally {
    lock.releaseLock();
  }
}

function studentInfo_(code) {
  const f = findStudent_(code);
  if (!f) return { ok: false, error: 'notfound' };
  const out = { ok: true, name: f.name, done: f.status === DONE };
  if (out.done) out.result = lastResult_(code);
  return out;
}

function findStudent_(code) {
  if (!code) return null;
  const st = sheet_(SH_STUDENTS);
  const last = st.getLastRow();
  if (last < 2) return null;
  const rows = st.getRange(2, 1, last - 1, 8).getValues();
  for (let i = 0; i < rows.length; i++) {
    if (String(rows[i][C.CODE - 1]).trim().toUpperCase() === code) {
      return { row: i + 2, name: String(rows[i][C.NAME - 1]).trim(), birth: rows[i][C.BIRTH - 1], status: String(rows[i][C.STATUS - 1]).trim() };
    }
  }
  return null;
}

function lastResult_(code) {
  const rs = sheet_(SH_RESULTS);
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
function sanitizeAns_(raw) {
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

function score_(ans) {
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
function notify_(name, birth, sc, hints) {
  const text = '📊 ' + name + (birth ? ' (' + birth + ')' : '') + '\n' +
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
