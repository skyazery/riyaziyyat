/**
 * 1-ci sinif riyaziyyat – şagird idarəsi (Google Apps Script)
 *
 * 이 코드는 선생님의 구글 시트에 붙여 넣어 쓰는 프로그램입니다.
 *  - 학생 명단(Şagirdlər)에서 학생마다 고유 코드·개인 링크·왓츠앱 보내기 링크를 만듭니다.
 *  - 학습지 사이트(1-1권: test.html, 1-2권: 1-2/test.html)가 보낸 시험 답안을 채점해 결과 탭에 저장합니다.
 *  - 시험은 책마다 학생당 1번만 저장되고, 저장되는 순간 선생님 텔레그램으로 알림을 보냅니다.
 *  - 레벨테스트(Səviyyə testi) 결과로 책마다 학생의 시작 단원을 정하고, 선생님이 시트에서 바꿀 수 있습니다.
 *  - 부모가 동의서(qeydiyyat.html)를 내면 Qeydiyyat 탭에 동의 기록이 남고, Şagirdlər 탭에 학생이
 *    자동으로 추가되며(코드·개인 링크·왓츠앱 보내기 링크까지), 선생님 텔레그램으로 알림이 갑니다.
 *  - 학생이 주제(10문제)를 끝낼 때마다 Gündəlik 탭에 기록됩니다. 개인 링크로 공부하는 학생은
 *    새 주제가 하루 GUNDELIK_LIMIT개(Ayarlar 탭, 기본 1)씩 열리고, 밀렸으면 하루 그 2배까지 따라잡을 수 있습니다.
 *  - 📋 현황판: 학생마다 상태(잘하고 있음/살펴보기/연락 필요)·최근 7일·진도·정답률. 매시간 자동으로 새로 고침.
 *  - 🔍 학생 보기: 이름을 고르면 그 학생 정보와 최근 기록이 나옴.
 *  - 메뉴 「주간 리포트 만들기」(일요일 저녁) / 「월간 리포트 만들기」(월말)를 누르면 Hesabatlar 탭에 학생별 줄이 생깁니다.
 *    선생님 한마디를 적고 「💬 Göndər」를 누르면 부모님께 리포트 링크(hesabat.html)를 왓츠앱으로 보냅니다.
 *
 * Şagirdlər 탭 칸:  A~F 학생 정보 · G~K 1-1권 · L~P 1-2권 · Q 학년 · R 부모 이름
 * 개인정보(생년월일, 전화번호)는 이 시트 안에만 있고, 사이트에는 학생 이름만 전달됩니다.
 */

/* ---------------- 설정 ---------------- */
const SERVICE_NAME = 'Riyaziyyat Dostu';
const SH_STUDENTS = 'Şagirdlər';
const SH_SETTINGS = 'Ayarlar';
const SH_REG = 'Qeydiyyat';
const SH_DAILY = 'Gündəlik';
const TZ_LOCAL = 'Asia/Tbilisi'; // 하루가 바뀌는 기준 (학습지 사이트와 같아야 함)
const DAILY_HEADERS = ['Tarix (날짜)', 'Saat (시각)', 'Kod', 'Ad (이름)', 'Kitab (책)', 'Mövzu (주제)', 'Mövzu adı',
  'Ulduz (첫 시도 정답)', 'Tapşırıq (채점 문제 수)', 'Növ (새/복습/시작만)',
  'İkinci cəhddə düz (2번째 시도 정답)', 'Cavabı göstərildi (정답 봄)', 'Səhv tapşırıqlar (틀린 문제 번호)',
  'Dəftər düz/səhv/qeydsiz (공책 자기평가)', 'Vaxt, dəq (걸린 시간·분)', 'Həll etdi (푼 문제 수)'];
const K_NEW = 'Yeni (새 주제)', K_REV = 'Təkrar (복습)', K_START = 'Başladı (끝내지 못함)';
const SH_REPORTS = 'Hesabatlar';
const REPORT_HEADERS = ['Dövr (기간)', 'Növ (종류)', 'Kod', 'Ad (이름)', 'Oxuduğu gün (공부한 날)', 'Yeni mövzu (새 주제)',
  'Müəllimin qeydi (선생님 한마디 – 직접 입력)', 'Hesabat linki (리포트 링크)', 'WhatsApp (보내기)'];
const AYLAR = ['yanvar', 'fevral', 'mart', 'aprel', 'may', 'iyun', 'iyul', 'avqust', 'sentyabr', 'oktyabr', 'noyabr', 'dekabr'];
const DONE = 'Tamamlandı';

// Şagirdlər 탭 열 순서 (1부터)
const C = { NAME: 1, BIRTH: 2, PHONE: 3, CODE: 4, LINK: 5, WA: 6, GRADE: 17, PARENT: 18 };
const NCOL = 16;
const REG_HEADERS = ['Tarix (제출 시각)', 'Şagirdin adı (이름)', 'Soyadı (성)', 'Doğum tarixi (생년월일)', 'Sinif (학년)',
  'Valideyn (부모 이름)', 'Telefon (전화)', 'Valideyn təsdiqi (보호자 확인)', 'Razılıq 1 (정보 이용)', 'Razılıq 2 (결과 저장·발송)',
  'Razılıq 3 – reklam (홍보, 선택)', 'Kod (코드)', 'Qeyd (메모)'];
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
    .addItem('📋 현황판 새로 고침', 'refreshPanelNow')
    .addItem('🎨 시트 보기 좋게 정리 (처음 한 번)', 'tidySheets')
    .addSeparator()
    .addItem('📊 주간 리포트 만들기 (이번 주)', 'makeWeeklyReports')
    .addItem('📅 월간 리포트 만들기', 'makeMonthlyReports')
    .addItem('⏰ 리포트 텔레그램 알림 켜기', 'reminderOn')
    .addItem('🔕 리포트 텔레그램 알림 끄기', 'reminderOff')
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
  // 동의서 화면에 보일 연락처 (예전 시트에는 없으면 맨 아래에 추가)
  if (!hasSetting_('ELAQE_NOMRESI')) {
    se.appendRow(['ELAQE_NOMRESI', '', '동의서에 보일 왓츠앱 번호 (예: +995 555 12 34 56)']);
    se.getRange(se.getLastRow(), 1).setFontWeight('bold');
  }
  if (!hasSetting_('GUNDELIK_LIMIT')) {
    se.appendRow(['GUNDELIK_LIMIT', 1, '하루에 열리는 새 주제 수 (0 = 제한 없음). 밀린 학생은 하루 이 수의 2배까지 따라잡기']);
    se.getRange(se.getLastRow(), 1).setFontWeight('bold');
  }
  setupRegistration_(ss);
  setupDaily_(ss);
  setupReports_(ss);
  SpreadsheetApp.getUi().alert('준비 완료! Şagirdlər 탭에 학생 이름·생년월일·부모 전화번호를 적고 「② 새 학생 링크 만들기」를 누르세요.\n\n' +
    '동의서(qeydiyyat.html)로 등록한 학생은 자동으로 추가되고 링크도 자동으로 만들어집니다. Ayarlar 탭 ELAQE_NOMRESI 칸에 연락처를 넣어 주세요.\n\n' +
    '칸 안내: G~K = 1-1권, L~P = 1-2권, Q = 학년, R = 부모 이름.\n' +
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
    writeLinks_(st, row, name, r[C.PHONE - 1], code, site);
  });
  SpreadsheetApp.getUi().alert('새 링크 ' + made + '개를 만들었어요. F칸의 「💬 Göndər」를 누르면 왓츠앱이 열립니다.');
}

// 한 학생 줄에 개인 링크(E칸)와 왓츠앱 보내기 링크(F칸)를 씁니다
function writeLinks_(st, row, name, phoneRaw, code, site) {
  const link = site.replace(/\/?$/, '/') + '?s=' + code;
  st.getRange(row, C.LINK).setValue(link);
  const phone = waPhone_(phoneRaw);
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
  if (p.action === 'info') return json_({ ok: true, name: SERVICE_NAME, phone: setting_('ELAQE_NOMRESI') });
  if (p.action === 'report') return json_(reportData_(cleanCode_(p.s), String(p.h || '')));
  return json_({ ok: true, app: 'riyaziyyat' });
}

function doPost(e) {
  let body = {};
  try { body = JSON.parse(e.postData.contents); } catch (err) { return json_({ ok: false, error: 'bad' }); }
  if (body.action === 'register') return saveRegister_(body);
  const bk = book_(body.b);
  if (body.action === 'level') return saveLevel_(body, bk);
  if (body.action === 'topic' || body.action === 'start' || body.action === 'progress') return saveTopic_(body, bk);
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
    return json_({ ok: true, b: bk.name, name: found.name, done: true, result: { ans: ans, hints: hints, date: dateStr } });
  } finally {
    lock.releaseLock();
  }
}

function studentInfo_(code, bk) {
  const f = findStudent_(code, bk);
  if (!f) return { ok: false, error: 'notfound' };
  const out = { ok: true, b: bk.name, name: f.name, done: f.status === DONE, level: levelInfo_(f, bk), daily: dailyInfo_(code) };
  if (out.done) out.result = lastResult_(code, bk);
  return out;
}

/* ---------------- 매일 기록(Gündəlik) ----------------
   사이트가 주제를 끝낼 때마다 보냅니다. 새 주제(시작 단원 이상, 처음 끝낸 것)는 「Yeni」, 나머지는 「Təkrar」.
   사이트는 이 기록으로 하루에 열 수 있는 새 주제 수를 계산합니다. */
function setupDaily_(ss) {
  let dg = ss.getSheetByName(SH_DAILY) || ss.insertSheet(SH_DAILY);
  // 예전에 만든 탭에는 새 칸 제목이 없으므로 마지막 칸 제목이 없으면 제목 줄을 다시 씁니다
  if (!dg.getRange(1, DAILY_HEADERS.length).getValue()) {
    dg.getRange(1, 1, 1, DAILY_HEADERS.length).setValues([DAILY_HEADERS]).setFontWeight('bold').setBackground('#E8F1FF');
    dg.setFrozenRows(1);
    dg.getRange('A:B').setNumberFormat('@');
  }
  return dg;
}

function dailyLimit_() {
  if (!hasSetting_('GUNDELIK_LIMIT')) return 1;
  const v = parseInt(setting_('GUNDELIK_LIMIT'), 10);
  return v >= 0 ? v : 1;
}

// 이 학생의 기록: new = 새 주제를 끝낸 [날짜, 책, 주제] 목록 (사이트가 열림 계산에 씀)
function dailyRows_(code) {
  const dg = SpreadsheetApp.getActive().getSheetByName(SH_DAILY);
  if (!dg || dg.getLastRow() < 2) return [];
  return dg.getRange(2, 1, dg.getLastRow() - 1, DAILY_HEADERS.length).getValues()
    .map(dailyRow_).filter(r => r.code === code);
}

function dailyRow_(r, i) {
  return { row: i + 2, code: String(r[2]), d: fmtDay_(r[0]), t: String(r[1]), b: String(r[4]), n: Number(r[5]), name: String(r[6]),
    kind: String(r[9]), isNew: String(r[9]).indexOf('Yeni') === 0, start: String(r[9]).indexOf('Başladı') === 0,
    stars: Number(r[7]) || 0, total: Number(r[8]) || 0, second: Number(r[10]) || 0, shown: Number(r[11]) || 0,
    wrong: String(r[12] || ''), min: Number(r[14]) || 0, done: String(r[15] || '') };
}

function dailyInfo_(code) {
  const rows = dailyRows_(code);
  return { limit: dailyLimit_(), today: Utilities.formatDate(new Date(), TZ_LOCAL, 'yyyy-MM-dd'),
    news: rows.filter(r => r.isNew).map(r => [r.d, r.b, r.n]),
    days: Array.from(new Set(rows.map(r => r.d))).length };
}

function fmtDay_(v) {
  if (v instanceof Date) return Utilities.formatDate(v, TZ_LOCAL, 'yyyy-MM-dd');
  return String(v || '').trim();
}

function int_(v, lo, hi) { const n = parseInt(v, 10); return isNaN(n) ? lo : Math.max(lo, Math.min(hi, n)); }

function dayOf_(body, now) {
  // 인터넷이 없어서 늦게 보낸 기록은 실제로 푼 날짜(최근 7일 안)로 저장
  const today = Utilities.formatDate(now, TZ_LOCAL, 'yyyy-MM-dd');
  const m = /^(\d{4})-(\d{2})-(\d{2})$/.exec(String(body.d || ''));
  if (m) {
    const diff = (Date.parse(today) - Date.parse(m[0])) / 864e5;
    if (diff >= 0 && diff <= 7) return m[0];
  }
  return today;
}

// 사이트가 보낸 자세한 기록 (2번째 시도 정답, 정답 본 수, 틀린 문제, 공책 자기평가, 시간, 푼 문제 수)
function extras_(x, total) {
  x = x && typeof x === 'object' ? x : {};
  const wrong = (Array.isArray(x.wrong) ? x.wrong : []).map(v => parseInt(v, 10)).filter(v => v >= 1 && v <= 20).slice(0, 20);
  const self = Array.isArray(x.self) ? x.self : [];
  const min = Math.max(0, Math.min(180, Number(x.min) || 0));
  return [int_(x.second, 0, total || 20), int_(x.shown, 0, total || 20), wrong.length ? wrong.join(', ') : '-',
    int_(self[0], 0, 20) + ' / ' + int_(self[1], 0, 20) + ' / ' + int_(self[2], 0, 20),
    Math.round(min * 10) / 10, int_(x.done, 0, 20) + ' / ' + int_(x.count, 0, 20)];
}

/* action: 'start' – 주제 문제를 시작함(「시작만」 줄), 'progress' – 끝내지 않고 나감(그 줄을 고침),
           'topic' – 주제를 끝냄(같은 날 「시작만」 줄이 있으면 그 줄을 완료 기록으로 바꿈) */
function saveTopic_(body, bk) {
  const code = cleanCode_(body.s);
  const n = parseInt(body.n, 10);
  const last = bk.first + bk.topics.length - 1;
  if (!(n >= bk.first && n <= last)) return json_({ ok: false, error: 'bad' });
  const act = body.action;
  const total = int_(body.total, 0, 20);
  const stars = Math.min(total, int_(body.stars, 0, 20));
  const lock = LockService.getScriptLock();
  lock.waitLock(20000);
  try {
    const found = findStudent_(code, bk);
    if (!found) return json_({ ok: false, error: 'notfound' });
    const dg = setupDaily_(SpreadsheetApp.getActive());
    const now = new Date();
    const day = dayOf_(body, now);
    const rows = dailyRows_(code);
    const open = rows.filter(r => r.b === bk.name && r.n === n && r.d === day && r.start).pop();
    const write = (row, kind, st, tot, ex) => {
      dg.getRange(row, 1, 1, 2).setNumberFormat('@');
      dg.getRange(row, 1, 1, DAILY_HEADERS.length).setValues([[
        day, Utilities.formatDate(now, TZ_LOCAL, 'HH:mm'), code, found.name,
        bk.name, n, topicName_(bk, n), st, tot, kind].concat(ex)]);
    };
    const ex = extras_(body.x, total);
    if (act === 'start' || act === 'progress') {
      if (act === 'start' && open) return json_({ ok: true });
      if (act === 'progress' && !open) return json_({ ok: true });
      write(open ? open.row : dg.getLastRow() + 1, K_START, stars, total, ex);
      SpreadsheetApp.flush();
      return json_({ ok: true });
    }
    const start = levelInfo_(found, bk).start;
    const before = rows.some(r => r.b === bk.name && r.n === n && !r.start);
    const isNew = start != null && n >= start && !before;
    write(open ? open.row : dg.getLastRow() + 1, isNew ? K_NEW : K_REV, stars, total, ex);
    SpreadsheetApp.flush();
    return json_({ ok: true, isNew: isNew, daily: dailyInfo_(code) });
  } finally {
    lock.releaseLock();
  }
}

/* ---------------- 주간·월간 리포트 ----------------
   기간 열쇠: 주간 'w-YYYY-MM-DD'(그 주 월요일), 월간 'm-YYYY-MM'.
   hesabat.html?s=코드&h=열쇠 가 action=report 로 이 학생의 기록 전체를 받아 화면에서 계산합니다. */
function setupReports_(ss) {
  let rp = ss.getSheetByName(SH_REPORTS) || ss.insertSheet(SH_REPORTS);
  if (!rp.getRange(1, 1).getValue()) {
    rp.getRange(1, 1, 1, REPORT_HEADERS.length).setValues([REPORT_HEADERS]).setFontWeight('bold').setBackground('#EFE9FF');
    rp.setFrozenRows(1);
    rp.getRange('A:A').setNumberFormat('@');
    rp.setColumnWidth(7, 360);
    rp.getRange('G:G').setWrap(true);
  }
  return rp;
}

function ymd_(dt) { return dt.toISOString().slice(0, 10); }
function addDays_(day, k) { const d = new Date(day + 'T00:00:00Z'); d.setUTCDate(d.getUTCDate() + k); return ymd_(d); }

// 열쇠 → { kind, key, from, to, label }
function period_(h) {
  let m = /^w-(\d{4}-\d{2}-\d{2})$/.exec(h);
  if (m) {
    const from = m[1], to = addDays_(from, 6);
    const f = from.split('-'), t = to.split('-');
    const label = f[1] === t[1] ? (+f[2]) + '–' + (+t[2]) + ' ' + AYLAR[+t[1] - 1]
      : (+f[2]) + ' ' + AYLAR[+f[1] - 1] + ' – ' + (+t[2]) + ' ' + AYLAR[+t[1] - 1];
    return { kind: 'w', key: h, from: from, to: to, label: label };
  }
  m = /^m-(\d{4})-(\d{2})$/.exec(h);
  if (m) {
    const y = +m[1], mo = +m[2];
    const last = new Date(Date.UTC(y, mo, 0)).getUTCDate();
    return { kind: 'm', key: h, from: m[1] + '-' + m[2] + '-01', to: m[1] + '-' + m[2] + '-' + String(last).padStart(2, '0'),
      label: AYLAR[mo - 1] + ' ' + y };
  }
  return null;
}

function todayLocal_() { return Utilities.formatDate(new Date(), TZ_LOCAL, 'yyyy-MM-dd'); }
function thisWeekKey_() {
  const t = todayLocal_(), dow = new Date(t + 'T00:00:00Z').getUTCDay(); // 0=bazar(일)
  return 'w-' + addDays_(t, -((dow + 6) % 7));
}
// 25일 이후에 누르면 이번 달, 그 전에 누르면 지난달
function monthKey_() {
  const t = todayLocal_(), y = +t.slice(0, 4), mo = +t.slice(5, 7), d = +t.slice(8, 10);
  if (d >= 25) return 'm-' + t.slice(0, 7);
  const p = new Date(Date.UTC(y, mo - 2, 1));
  return 'm-' + p.toISOString().slice(0, 7);
}

function reportNote_(key, code) {
  const rp = SpreadsheetApp.getActive().getSheetByName(SH_REPORTS);
  if (!rp || rp.getLastRow() < 2) return '';
  const rows = rp.getRange(2, 1, rp.getLastRow() - 1, 7).getValues();
  for (let i = rows.length - 1; i >= 0; i--) if (String(rows[i][0]) === key && String(rows[i][2]) === code) return String(rows[i][6] || '').trim();
  return '';
}

function reportData_(code, h) {
  if (!code) return { ok: false, error: 'notfound' };
  const per = period_(h) || period_(thisWeekKey_());
  const f = findStudent_(code, BOOKS['1-1']);
  if (!f) return { ok: false, error: 'notfound' };
  const st = sheet_(SH_STUDENTS);
  const grade = String(st.getRange(f.row, C.GRADE).getValue() || '').trim();
  const levels = {};
  Object.keys(BOOKS).forEach(id => {
    const L = levelInfo_(findStudent_(code, BOOKS[id]), BOOKS[id]);
    levels[id] = { start: L.start, date: L.date };
  });
  const rows = dailyRows_(code).map(r => [r.d, r.t, r.b, r.n, r.name, r.start ? 's' : r.isNew ? 'n' : 'r',
    r.stars, r.total, r.second, r.shown, r.wrong, r.min, r.done]);
  return { ok: true, name: f.name, grade: grade, period: per, today: todayLocal_(), levels: levels, rows: rows,
    note: reportNote_(per.key, code), limit: dailyLimit_(), phone: setting_('ELAQE_NOMRESI') };
}

function makeWeeklyReports() { makeReports_(thisWeekKey_()); }
function makeMonthlyReports() { makeReports_(monthKey_()); }

function makeReports_(key, silent) {
  const ss = SpreadsheetApp.getActive();
  const per = period_(key);
  const st = sheet_(SH_STUDENTS);
  const rp = setupReports_(ss);
  const dg = setupDaily_(ss);
  const site = (setting_('SAYT_LINKI') || 'https://skyazery.github.io/riyaziyyat/').replace(/\/?$/, '/');
  const last = st.getLastRow();
  if (last < 2) { if (!silent) SpreadsheetApp.getUi().alert('학생이 없어요.'); return null; }
  const studs = st.getRange(2, 1, last - 1, C.CODE).getValues()
    .map(r => ({ name: String(r[C.NAME - 1]).trim(), phone: r[C.PHONE - 1], code: String(r[C.CODE - 1]).trim() }))
    .filter(x => x.name && x.code);
  const all = dg.getLastRow() >= 2 ? dg.getRange(2, 1, dg.getLastRow() - 1, DAILY_HEADERS.length).getValues().map(dailyRow_) : [];
  const existing = {};
  if (rp.getLastRow() >= 2) rp.getRange(2, 1, rp.getLastRow() - 1, 3).getValues()
    .forEach((r, i) => { if (String(r[0]) === key) existing[String(r[2])] = i + 2; });
  let made = 0;
  const summary = [];
  studs.forEach(x => {
    const mine = all.filter(r => r.code === x.code && r.d >= per.from && r.d <= per.to);
    const days = new Set(mine.map(r => r.d)).size;
    const news = mine.filter(r => r.isNew).length;
    summary.push({ name: x.name, days: days, news: news });
    const link = site + 'hesabat.html?s=' + x.code + '&h=' + key;
    const first = x.name.split(' ')[0];
    let msg;
    if (per.kind === 'w') {
      msg = days ? 'Salam! ' + first + ' üçün bu həftənin (' + per.label + ') riyaziyyat hesabatı hazırdır: ' + days + ' gün oxudu, ' + news + ' yeni mövzu öyrəndi.'
        : 'Salam! ' + first + ' bu həftə (' + per.label + ') riyaziyyat tapşırıqlarını etməyib. Gəlin, sabahdan yenə hər gün 10 dəqiqə oxuyaq! 🦊';
    } else {
      msg = 'Salam! ' + first + ' üçün ' + per.label.split(' ')[0] + ' ayının riyaziyyat hesabatı hazırdır: ' + days + ' gün oxudu, ' + news + ' yeni mövzu öyrəndi.';
    }
    msg += '\nƏtraflı hesabat: ' + link;
    const row = existing[x.code] || Math.max(rp.getLastRow(), 1) + 1;
    rp.getRange(row, 1).setNumberFormat('@');
    rp.getRange(row, 1, 1, 6).setValues([[key, per.kind === 'w' ? 'Həftəlik (주간) ' + per.label : 'Aylıq (월간) ' + per.label, x.code, x.name, days, news]]);
    rp.getRange(row, 8).setValue(link);
    const phone = waPhone_(x.phone);
    const cell = rp.getRange(row, 9);
    if (phone) cell.setRichTextValue(SpreadsheetApp.newRichTextValue().setText('💬 Göndər').setLinkUrl('https://wa.me/' + phone + '?text=' + encodeURIComponent(msg)).build());
    else cell.setValue('전화번호 확인');
    if (!existing[x.code]) made++;
  });
  if (silent) return { per: per, list: summary };
  rp.activate();
  SpreadsheetApp.getUi().alert((per.kind === 'w' ? '주간' : '월간') + ' 리포트 (' + per.label + '): 학생 ' + studs.length + '명' + (made < studs.length ? ' (새 줄 ' + made + '개)' : '') + '\n\n' +
    'G칸에 선생님 한마디를 적으면 리포트에 바로 나옵니다 (비워 두면 여우 선생님 자동 응원 문장).\n' +
    'I칸 「💬 Göndər」를 누르면 왓츠앱이 열립니다.');
  return { per: per, list: summary };
}

/* ---------------- 리포트 텔레그램 알림 ----------------
   일요일 REMIND_HOUR시: 이번 주 리포트 줄을 미리 만들고 선생님 텔레그램으로 알림
   매일 REMIND_HOUR시에 확인해서 그달 마지막 날이면: 월간 리포트 줄을 만들고 알림 */
const REMIND_HOUR = 19;

function reminderOn() {
  const ui = SpreadsheetApp.getUi();
  if (!setting_('TELEGRAM_BOT_TOKEN') || !setting_('TELEGRAM_CHAT_ID')) {
    ui.alert('Ayarlar 탭에 텔레그램 봇 토큰과 채팅 ID가 먼저 있어야 해요.'); return;
  }
  deleteReminders_();
  ScriptApp.newTrigger('weeklyReminder').timeBased().onWeekDay(ScriptApp.WeekDay.SUNDAY).atHour(REMIND_HOUR).inTimezone(TZ_LOCAL).create();
  ScriptApp.newTrigger('monthEndCheck').timeBased().everyDays(1).atHour(REMIND_HOUR).inTimezone(TZ_LOCAL).create();
  sendTelegram_('⏰ 리포트 알림을 켰어요!\n· 매주 일요일 ' + REMIND_HOUR + '시쯤: 주간 리포트\n· 매달 마지막 날 ' + REMIND_HOUR + '시쯤: 월간 리포트');
  ui.alert('알림을 켰어요. 매주 일요일과 매달 마지막 날 저녁 ' + REMIND_HOUR + '시쯤 텔레그램으로 알려 드려요. (텔레그램에 확인 메시지를 보냈어요)');
}

function reminderOff() {
  const n = deleteReminders_();
  SpreadsheetApp.getUi().alert(n ? '리포트 알림을 껐어요.' : '켜져 있는 알림이 없어요.');
}

function deleteReminders_() {
  let n = 0;
  ScriptApp.getProjectTriggers().forEach(t => {
    if (['weeklyReminder', 'monthEndCheck'].indexOf(t.getHandlerFunction()) >= 0) { ScriptApp.deleteTrigger(t); n++; }
  });
  return n;
}

function weeklyReminder() { remind_(thisWeekKey_()); }

function monthEndCheck() {
  const t = todayLocal_();
  if (addDays_(t, 1).slice(8, 10) === '01') remind_('m-' + t.slice(0, 7));
}

function remind_(key) {
  const r = makeReports_(key, true);
  const url = SpreadsheetApp.getActive().getUrl();
  if (!r) { sendTelegram_('📊 리포트 보낼 날이에요. 아직 학생이 없어요.'); return; }
  const w = r.per.kind === 'w';
  const did = r.list.filter(x => x.days > 0), not = r.list.filter(x => !x.days);
  const lines = [
    (w ? '📊 주간 리포트 보낼 시간이에요! (' : '📅 월간 리포트 보낼 시간이에요! (') + r.per.label + ')',
    '',
    '공부한 학생 ' + did.length + ' / ' + r.list.length + '명'
  ];
  did.slice().sort((a, b) => b.days - a.days).forEach(x => lines.push('✅ ' + x.name + ' – ' + x.days + '일, 새 주제 ' + x.news + '개'));
  not.forEach(x => lines.push('⚪ ' + x.name + ' – 이번 ' + (w ? '주' : '달') + ' 안 함'));
  lines.push('', '① 시트 Hesabatlar 탭을 여세요: ' + url,
    '② 하고 싶은 말은 G칸에 적고 (안 적어도 돼요)',
    '③ I칸 「💬 Göndər」를 누르면 부모님께 왓츠앱이 열려요.');
  sendTelegram_(lines.join('\n'));
}

/* ---------------- 동의서(Qeydiyyat) 저장 ----------------
   qeydiyyat.html 이 보낸 내용을 확인하고
   ① Qeydiyyat 탭에 동의 기록  ② Şagirdlər 탭에 학생 추가(코드·링크 자동)  ③ 텔레그램 알림 */
function setupRegistration_(ss) {
  let rg = ss.getSheetByName(SH_REG) || ss.insertSheet(SH_REG);
  if (!rg.getRange(1, 1).getValue()) {
    rg.getRange(1, 1, 1, REG_HEADERS.length).setValues([REG_HEADERS]).setFontWeight('bold').setBackground('#FDE7EF');
    rg.setFrozenRows(1);
    rg.getRange('D:D').setNumberFormat('@');
    rg.getRange('G:G').setNumberFormat('@');
  }
  const st = ss.getSheetByName(SH_STUDENTS);
  if (st && !st.getRange(1, C.GRADE).getValue()) {
    st.getRange(1, C.GRADE, 1, 2).setValues([['Sinif (학년)', 'Valideyn (부모 이름)']]).setFontWeight('bold').setBackground('#FDE7EF');
    st.setColumnWidths(C.GRADE, 2, 140);
  }
  return rg;
}

function cleanText_(v, max) {
  return String(v == null ? '' : v).replace(/\s+/g, ' ').trim().slice(0, max || 60);
}

// 'YYYY-MM-DD' → 'dd.MM.yyyy' (만 4~15살 범위만 받음, 초1~6학년)
function cleanBirth_(v) {
  const m = /^(\d{4})-(\d{2})-(\d{2})$/.exec(String(v || '').trim());
  if (!m) return '';
  const y = +m[1], mo = +m[2], d = +m[3];
  const dt = new Date(y, mo - 1, d);
  if (dt.getFullYear() !== y || dt.getMonth() !== mo - 1 || dt.getDate() !== d) return '';
  const age = (new Date() - dt) / (365.25 * 24 * 3600 * 1000);
  if (age < 4 || age > 15) return '';
  return m[3] + '.' + m[2] + '.' + m[1];
}

function saveRegister_(body) {
  if (body.hp) return json_({ ok: true }); // 자동 스팸 프로그램이 숨은 칸을 채운 경우: 저장하지 않음
  const nameOk = s => s.length >= 2 && /^[\p{L}][\p{L} '’\-]*$/u.test(s);
  const ad = cleanText_(body.ad), soyad = cleanText_(body.soyad), parent = cleanText_(body.valideyn, 80);
  const birth = cleanBirth_(body.dogum);
  const grade = ['1', '2', '3', '4', '5', '6'].indexOf(String(body.sinif)) >= 0 ? String(body.sinif) : '';
  const gradeName = grade ? grade + ({ '3': '-cü', '4': '-cü', '6': '-cı' }[grade] || '-ci') + ' sinif' : '';
  const wa = waPhone_(body.telefon);
  const c = Array.isArray(body.razi) ? body.razi.map(x => x === true) : [];
  const bad = [];
  if (!nameOk(ad)) bad.push('ad');
  if (!nameOk(soyad)) bad.push('soyad');
  if (!birth) bad.push('dogum');
  if (!grade) bad.push('sinif');
  if (parent.length < 2) bad.push('valideyn');
  if (!/^995\d{9}$/.test(wa)) bad.push('telefon');
  if (!(c[0] && c[1] && c[2])) bad.push('razi');
  if (bad.length) return json_({ ok: false, error: 'invalid', fields: bad });

  const phone = '+995 ' + wa.slice(3, 6) + ' ' + wa.slice(6, 8) + ' ' + wa.slice(8, 10) + ' ' + wa.slice(10, 12);
  const full = ad + ' ' + soyad;
  const lock = LockService.getScriptLock();
  lock.waitLock(20000);
  try {
    const ss = SpreadsheetApp.getActive();
    const rg = setupRegistration_(ss);
    const st = sheet_(SH_STUDENTS);
    const site = setting_('SAYT_LINKI') || 'https://skyazery.github.io/riyaziyyat/';
    const last = st.getLastRow();
    const rows = last >= 2 ? st.getRange(2, 1, last - 1, C.CODE).getValues() : [];
    const used = {};
    let dupRow = 0, code = '', lastNamed = 1; // 재응시 체크박스가 시트 끝까지 있어서 이름이 있는 마지막 줄을 따로 찾습니다
    rows.forEach((r, i) => {
      if (String(r[C.NAME - 1]).trim()) lastNamed = i + 2;
      if (r[C.CODE - 1]) used[String(r[C.CODE - 1])] = true;
      if (!dupRow && String(r[C.NAME - 1]).trim().toLowerCase() === full.toLowerCase() && fmtBirth_(r[C.BIRTH - 1]) === birth) {
        dupRow = i + 2; code = String(r[C.CODE - 1]).trim();
      }
    });
    let note = '';
    if (dupRow) {
      note = 'Təkrar qeydiyyat (이미 ' + dupRow + '번째 줄에 있음)';
      if (!code) {
        do { code = newCode_(); } while (used[code]);
        st.getRange(dupRow, C.CODE).setValue(code);
        writeLinks_(st, dupRow, full, st.getRange(dupRow, C.PHONE).getValue() || phone, code, site);
      }
    } else {
      do { code = newCode_(); } while (used[code]);
      const row = lastNamed + 1;
      st.getRange(row, C.BIRTH, 1, 2).setNumberFormat('@');
      st.getRange(row, 1, 1, C.CODE).setValues([[full, birth, phone, code]]);
      st.getRange(row, C.GRADE, 1, 2).setValues([[gradeName, parent]]);
      Object.keys(BOOKS).forEach(id => st.getRange(row, BOOKS[id].col.LV_RETRY).insertCheckboxes());
      writeLinks_(st, row, full, phone, code, site);
    }
    const tz = Session.getScriptTimeZone();
    const r0 = rg.getLastRow() + 1;
    rg.getRange(r0, 4).setNumberFormat('@');
    rg.getRange(r0, 7).setNumberFormat('@');
    rg.getRange(r0, 1, 1, REG_HEADERS.length).setValues([[
      Utilities.formatDate(new Date(), tz, 'yyyy-MM-dd HH:mm'), ad, soyad, birth, gradeName, parent, phone,
      'Bəli', 'Bəli', 'Bəli', c[3] ? 'Bəli' : 'Xeyr', code, note
    ]]);
    SpreadsheetApp.flush();
    sendTelegram_('📝 새 동의서 · ' + full + ' (' + grade + '학년, ' + birth + ')\n' +
      '부모: ' + parent + ' · 홍보 동의: ' + (c[3] ? '예' : '아니오') + '\n' +
      (dupRow ? '⚠️ 이미 등록된 학생입니다 (' + dupRow + '번째 줄)\n' : '') +
      '→ Şagirdlər 탭 F칸 「💬 Göndər」로 개인 링크를 보내 주세요.');
    return json_({ ok: true });
  } finally {
    lock.releaseLock();
  }
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

function hasSetting_(key) {
  const s = SpreadsheetApp.getActive().getSheetByName(SH_SETTINGS);
  if (!s) return false;
  return s.getRange(1, 1, Math.max(1, s.getLastRow()), 1).getValues().some(r => String(r[0]).trim() === key);
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


/* ================= 📋 현황판 · 🔍 학생 보기 · 탭 정리 =================
   보기 전용 탭입니다. 데이터(Şagirdlər, Gündəlik …)는 바꾸지 않고 읽기만 합니다. */
const SH_PANEL = '📋 현황판';
const SH_DETAIL = '🔍 학생 보기';
const ALL_TOPICS = 49;
const COL = { brand: '#5145E6', brandSoft: '#ECEAFF', sun: '#FFF4D6', sunInk: '#9A5B00', ok: '#1E8E3E', okSoft: '#E6F4EA',
  warn: '#B06000', warnSoft: '#FEF7E0', bad: '#C5221F', badSoft: '#FCE8E6', grey: '#BDC1C6', muted: '#5F6368', edit: '#FFF8C5' };
const STATUS = { bad: ['연락 필요', COL.bad, COL.badSoft], warn: ['살펴보기', COL.warn, COL.warnSoft], ok: ['잘하고 있음', COL.ok, COL.okSoft] };

function bookByTopic_(n) { return n >= BOOKS['1-2'].first ? BOOKS['1-2'] : BOOKS['1-1']; }

// 학생 한 명의 요약 (현황판·학생 보기가 같이 씀)
function studentSummary_(stu, rows, today) {
  const comp = rows.filter(r => !r.start);
  const levels = {};
  Object.keys(BOOKS).forEach(id => {
    const bk = BOOKS[id], c = bk.col;
    const start = parseInt(stu.raw[c.LV_START - 1], 10);
    levels[id] = { start: start >= bk.first && start <= bk.lvAll ? start : null, date: fmtBirth_(stu.raw[c.LV_DATE - 1]), test: String(stu.raw[c.STATUS - 1]).trim() === DONE, testDate: fmtBirth_(stu.raw[c.DATE - 1]) };
  });
  const known = new Set(comp.map(r => r.n));
  Object.keys(BOOKS).forEach(id => { const L = levels[id].start; if (L != null) for (let n = BOOKS[id].first; n < Math.min(L, BOOKS[id].lvAll); n++) known.add(n); });
  let next = null;
  if (levels['1-1'].start != null) {
    outer: for (const id of Object.keys(BOOKS)) {
      const bk = BOOKS[id], from = Math.max(bk.first, levels[id].start != null ? levels[id].start : bk.first);
      for (let n = from; n < bk.lvAll; n++) if (!known.has(n)) { next = n; break outer; }
    }
    if (next == null) next = 'all';
  }
  const days7 = []; for (let k = 6; k >= 0; k--) days7.push(addDays_(today, -k));
  const week = days7.map(d => { const rs = rows.filter(r => r.d === d); return rs.some(r => !r.start) ? 1 : rs.length ? 0.5 : 0; });
  const w = rows.filter(r => r.d >= days7[0] && r.d <= today), wc = w.filter(r => !r.start);
  const tt = wc.reduce((a, r) => a + r.total, 0), ss = wc.reduce((a, r) => a + r.stars, 0);
  const wdays = new Set(w.map(r => r.d)).size;
  // 레벨 테스트 본 날도 「공부한 날」로 봅니다
  const lvDays = Object.keys(levels).map(id => levels[id].date).filter(Boolean).map(d => d.split('.').reverse().join('-'));
  const actDays = rows.map(r => r.d).concat(lvDays);
  const last = actDays.length ? actDays.reduce((m, d) => (d > m ? d : m), actDays[0]) : null;
  const ago = last ? Math.round((Date.parse(today) - Date.parse(last)) / 864e5) : null;
  const acc = tt ? Math.round(ss / tt * 100) : null;
  const allT = comp.reduce((a, r) => a + r.total, 0), allS = comp.reduce((a, r) => a + r.stars, 0);
  let status, why;
  if (levels['1-1'].start == null) { status = 'bad'; why = '레벨 테스트 전'; }
  else if (ago == null || ago >= 3) { status = 'bad'; why = ago == null ? '아직 시작 안 함' : ago + '일째 쉼'; }
  else if (ago === 2 || (acc != null && acc < 70)) { status = 'warn'; why = ago === 2 ? '2일째 쉼' : '정답률 낮음'; }
  else { status = 'ok'; why = ''; }
  return { levels, known: known.size, done: new Set(comp.map(r => r.n)).size, reviews: comp.filter(r => r.kind.indexOf('Təkrar') === 0).length,
    next, week, wdays, newWeek: w.filter(r => r.isNew).length, acc, accAll: allT ? Math.round(allS / allT * 100) : null,
    min: wdays ? Math.round(w.reduce((a, r) => a + r.min, 0) / wdays) : null, last, ago, status, why };
}

function nextLabel_(next) {
  if (next == null) return '레벨 테스트 전';
  if (next === 'all') return '모든 주제 끝 → 최종 테스트';
  return 'Mövzu ' + next + '. ' + topicName_(bookByTopic_(next), next);
}
function agoLabel_(ago) { return ago == null ? '—' : ago === 0 ? '오늘' : ago === 1 ? '어제' : ago + '일 전'; }

function readStudents_() {
  const st = sheet_(SH_STUDENTS), last = st.getLastRow();
  if (last < 2) return [];
  const w = Math.max(C.PARENT, NCOL);
  return st.getRange(2, 1, last - 1, w).getValues().map((r, i) => ({
    row: i + 2, raw: r, name: String(r[C.NAME - 1]).trim(), birth: fmtBirth_(r[C.BIRTH - 1]), phone: String(r[C.PHONE - 1] || '').trim(),
    code: String(r[C.CODE - 1]).trim(), link: String(r[C.LINK - 1] || '').trim(), grade: String(r[C.GRADE - 1] || '').trim(), parent: String(r[C.PARENT - 1] || '').trim()
  })).filter(x => x.name);
}
function readDaily_() {
  const dg = SpreadsheetApp.getActive().getSheetByName(SH_DAILY);
  if (!dg || dg.getLastRow() < 2) return [];
  return dg.getRange(2, 1, dg.getLastRow() - 1, DAILY_HEADERS.length).getValues().map(dailyRow_).filter(r => r.code);
}
function link_(text, url) { return SpreadsheetApp.newRichTextValue().setText(text).setLinkUrl(url).build(); }

function refreshPanelNow() { refreshPanel(); SpreadsheetApp.getActive().getSheetByName(SH_PANEL).activate(); }

function refreshPanel() {
  const ss = SpreadsheetApp.getActive();
  const today = todayLocal_();
  const studs = readStudents_(), daily = readDaily_();
  const list = studs.map(x => ({ x, s: studentSummary_(x, daily.filter(r => r.code === x.code), today) }));
  const order = { bad: 0, warn: 1, ok: 2 };
  list.sort((a, b) => order[a.s.status] - order[b.s.status] || a.x.name.localeCompare(b.x.name));
  let sh = ss.getSheetByName(SH_PANEL);
  if (!sh) { sh = ss.insertSheet(SH_PANEL, 0); }
  sh.getRange(1, 1, sh.getMaxRows(), sh.getMaxColumns()).breakApart();
  sh.clear();
  const NC = 12, widths = [96, 170, 84, 110, 140, 132, 80, 250, 150, 92, 84, 76];
  widths.forEach((w, i) => sh.setColumnWidth(i + 1, w));
  sh.setHiddenGridlines(true);
  // 제목
  const now = Utilities.formatDate(new Date(), TZ_LOCAL, 'yyyy-MM-dd HH:mm');
  sh.getRange(1, 1, 1, NC).merge().setValue('📋 학생 현황판 · Riyaziyyat Dostu').setFontSize(18).setFontWeight('bold').setBackground(COL.sun).setFontColor('#1F2433').setVerticalAlignment('middle');
  sh.getRange(2, 1, 1, NC).merge().setValue(now + ' 기준 · 매시간 자동으로 새로 고쳐져요 · 바로 새로 고치려면 메뉴 「📐 학생 관리 → 📋 현황판 새로 고침」')
    .setFontColor(COL.sunInk).setBackground(COL.sun).setFontSize(10);
  sh.setRowHeight(1, 40);
  // 숫자 카드
  const kp = [
    [studs.length, '전체 학생', null],
    [list.filter(o => o.s.ago === 0).length, '오늘 공부한 학생', 'ok'],
    [list.filter(o => o.s.wdays > 0).length, '최근 7일 공부한 학생', null],
    [list.filter(o => o.s.status === 'bad').length, '연락이 필요한 학생', 'bad'],
    [list.reduce((a, o) => a + o.s.newWeek, 0), '최근 7일 새 주제 합계', null],
    [list.filter(o => o.s.acc != null).length ? Math.round(list.filter(o => o.s.acc != null).reduce((a, o) => a + o.s.acc, 0) / list.filter(o => o.s.acc != null).length) + '%' : '—', '최근 7일 평균 정답률', null]];
  kp.forEach((k, i) => {
    const c = i * 2 + 1, bg = k[2] === 'ok' ? COL.okSoft : k[2] === 'bad' ? COL.badSoft : '#F8F9FA', fg = k[2] === 'ok' ? COL.ok : k[2] === 'bad' ? COL.bad : '#202124';
    sh.getRange(4, c, 1, 2).merge().setValue(k[0]).setFontSize(22).setFontWeight('bold').setFontColor(fg).setBackground(bg).setHorizontalAlignment('left');
    sh.getRange(5, c, 1, 2).merge().setValue(k[1]).setFontSize(10).setFontColor(COL.muted).setBackground(bg);
  });
  sh.setRowHeight(4, 38);
  // 표
  const H = ['상태', '이름', '학년', '부모님', '왓츠앱', '최근 7일 (6일 전→오늘)', '마지막 공부', '지금 주제', '진도 (49주제)', '최근 7일 정답률', '하루 평균', '개인 링크'];
  const hr = 7;
  sh.getRange(hr, 1, 1, NC).setValues([H]).setBackground(COL.brand).setFontColor('#FFFFFF').setFontWeight('bold').setFontSize(10).setWrap(true).setVerticalAlignment('middle');
  sh.setRowHeight(hr, 34);
  sh.setFrozenRows(hr);
  if (!list.length) { sh.getRange(hr + 1, 1, 1, NC).merge().setValue('아직 학생이 없어요. 동의서로 등록하면 여기에 나와요.').setFontColor(COL.muted); return; }
  const vals = list.map(o => [STATUS[o.s.status][0] + (o.s.why ? '\n' + o.s.why : ''), o.x.name, o.x.grade || '—', o.x.parent || '—', '', '',
    agoLabel_(o.s.ago), nextLabel_(o.s.next), '', o.s.acc == null ? '—' : o.s.acc / 100, o.s.min == null ? '—' : o.s.min + '분', '']);
  const body = sh.getRange(hr + 1, 1, list.length, NC);
  body.setValues(vals).setVerticalAlignment('middle').setFontSize(10);
  sh.getRange(hr + 1, 10, list.length, 1).setNumberFormat('0%').setHorizontalAlignment('right');
  sh.getRange(hr + 1, 11, list.length, 1).setHorizontalAlignment('right');
  sh.getRange(hr + 1, 1, list.length, 1).setWrap(true).setFontWeight('bold').setHorizontalAlignment('center');
  sh.getRange(hr + 1, 2, list.length, 1).setFontWeight('bold');
  list.forEach((o, i) => {
    const r = hr + 1 + i, stc = STATUS[o.s.status];
    sh.setRowHeight(r, 34);
    sh.getRange(r, 1).setBackground(stc[2]).setFontColor(stc[1]);
    if (i % 2) sh.getRange(r, 2, 1, NC - 1).setBackground('#F8F9FA');
    // 왓츠앱
    const ph = waPhone_(o.x.phone);
    if (ph) sh.getRange(r, 5).setRichTextValue(link_('💬 ' + ph.slice(3, 6) + ' ' + ph.slice(6, 8) + ' ' + ph.slice(8, 10) + ' ' + ph.slice(10), 'https://wa.me/' + ph));
    else sh.getRange(r, 5).setValue('전화번호 확인').setFontColor(COL.bad);
    // 최근 7일 점
    const txt = o.s.week.map(v => (v === 1 ? '●' : v ? '◐' : '○')).join(' ');
    let rt = SpreadsheetApp.newRichTextValue().setText(txt);
    o.s.week.forEach((v, k) => {
      const color = v === 1 ? COL.ok : v ? '#E37400' : COL.grey;
      rt = rt.setTextStyle(k * 2, k * 2 + 1, SpreadsheetApp.newTextStyle().setForegroundColor(color).setFontSize(13).build());
    });
    sh.getRange(r, 6).setRichTextValue(rt.build());
    if (o.s.ago == null || o.s.ago >= 3) sh.getRange(r, 7).setFontColor(COL.bad).setFontWeight('bold');
    else if (o.s.ago === 2) sh.getRange(r, 7).setFontColor(COL.warn).setFontWeight('bold');
    // 진도 막대
    sh.getRange(r, 9).setFormula('=SPARKLINE(' + o.s.known + ',{"charttype","bar";"max",' + ALL_TOPICS + ';"color1","' + COL.brand + '"})');
    sh.getRange(r, 9).setNote(o.s.known + ' / ' + ALL_TOPICS + ' 주제 (레벨 테스트로 아는 주제 포함)');
    if (o.s.acc != null && o.s.acc < 70) sh.getRange(r, 10).setFontColor(COL.warn).setFontWeight('bold');
    if (o.x.link) sh.getRange(r, 12).setRichTextValue(link_('열기', o.x.link));
  });
  // 안내
  const lg = hr + list.length + 2;
  sh.getRange(lg, 1, 1, NC).merge().setValue('● 주제를 끝낸 날   ◐ 시작만 한 날   ○ 안 한 날   ·   연락 필요: 3일 이상 쉼 또는 레벨 테스트 전   ·   살펴보기: 2일째 쉼 또는 최근 정답률 70% 미만')
    .setFontColor(COL.muted).setFontSize(9);
  // 학생 보기 드롭다운도 최신으로
  try { updateDetailList_(); renderDetail_(); } catch (e) {}
}

/* ---------- 🔍 학생 보기 ---------- */
function setupDetail_() {
  const ss = SpreadsheetApp.getActive();
  let sh = ss.getSheetByName(SH_DETAIL);
  if (!sh) sh = ss.insertSheet(SH_DETAIL, 1);
  sh.setHiddenGridlines(true);
  [110, 220, 24, 86, 250, 90, 70, 60, 60, 110, 60].forEach((w, i) => sh.setColumnWidth(i + 1, w));
  sh.getRange(1, 1, 1, 11).merge().setValue('🔍 학생 보기 – 이름을 고르면 기록이 바로 나와요').setFontSize(16).setFontWeight('bold').setBackground(COL.sun).setFontColor('#1F2433');
  sh.setRowHeight(1, 36);
  sh.getRange(3, 1).setValue('학생 선택 ▸').setFontWeight('bold').setHorizontalAlignment('right');
  sh.getRange(3, 2).setBackground(COL.brandSoft).setFontColor(COL.brand).setFontWeight('bold').setFontSize(12)
    .setBorder(true, true, true, true, false, false, COL.brand, SpreadsheetApp.BorderStyle.SOLID_MEDIUM);
  updateDetailList_();
  return sh;
}
function updateDetailList_() {
  const sh = SpreadsheetApp.getActive().getSheetByName(SH_DETAIL);
  if (!sh) return;
  const names = readStudents_().map(x => x.name).sort((a, b) => a.localeCompare(b));
  const cell = sh.getRange(3, 2);
  if (!names.length) { cell.clearDataValidations(); return; }
  cell.setDataValidation(SpreadsheetApp.newDataValidation().requireValueInList(names, true).setAllowInvalid(false).build());
  if (!cell.getValue() || names.indexOf(String(cell.getValue())) < 0) cell.setValue(names[0]);
}
// 드롭다운을 바꾸면 자동 실행 (간단 트리거)
function onEdit(e) {
  try {
    if (e && e.range && e.range.getSheet().getName() === SH_DETAIL && e.range.getRow() === 3 && e.range.getColumn() === 2) renderDetail_();
  } catch (err) {}
}
function renderDetail_() {
  const sh = SpreadsheetApp.getActive().getSheetByName(SH_DETAIL);
  if (!sh) return;
  const name = String(sh.getRange(3, 2).getValue()).trim();
  const area = sh.getRange(5, 1, Math.max(sh.getMaxRows() - 4, 1), 11);
  area.clear(); area.breakApart();
  const x = readStudents_().find(s => s.name === name);
  if (!x) { sh.getRange(5, 1).setValue('학생을 골라 주세요.').setFontColor(COL.muted); return; }
  const today = todayLocal_();
  const rows = readDaily_().filter(r => r.code === x.code);
  const s = studentSummary_(x, rows, today);
  const stc = STATUS[s.status];
  const reg = (function () {
    const rg = SpreadsheetApp.getActive().getSheetByName(SH_REG);
    if (!rg || rg.getLastRow() < 2) return '';
    const v = rg.getRange(2, 1, rg.getLastRow() - 1, 12).getValues().filter(r => String(r[11]) === x.code);
    return v.length ? String(v[0][0]).slice(0, 10) : '';
  })();
  const L1 = s.levels['1-1'], L2 = s.levels['1-2'];
  const info = [
    ['상태', stc[0] + (s.why ? ' (' + s.why + ')' : '')],
    ['학년', x.grade || '—'], ['생년월일', x.birth || '—'], ['부모님', x.parent || '—'], ['왓츠앱', ''],
    ['등록일', reg || '—'], ['코드', x.code || '—'],
    ['레벨 테스트', L1.start == null ? '아직' : (L1.date || '') + ' → ' + (L1.start >= BOOKS['1-1'].lvAll ? '1권 전부 통과' : 'Mövzu ' + L1.start + '부터')],
    ['지금 주제', nextLabel_(s.next)],
    ['진도', s.known + ' / ' + ALL_TOPICS + ' 주제 (직접 끝낸 주제 ' + s.done + '개, 복습 ' + s.reviews + '번)'],
    ['마지막 공부', agoLabel_(s.ago) + (s.last ? ' (' + s.last + ')' : '')],
    ['최근 7일', s.wdays + '일 공부 · 정답률 ' + (s.acc == null ? '—' : s.acc + '%') + ' · 하루 평균 ' + (s.min == null ? '—' : s.min + '분')],
    ['전체 정답률', s.accAll == null ? '—' : s.accAll + '%'],
    ['최종 테스트', (L1.test ? '1권 완료 (' + L1.testDate + ')' : '1권 아직') + ' · ' + (L2.test ? '2권 완료 (' + L2.testDate + ')' : '2권 아직')]];
  sh.getRange(5, 1, 1, 2).merge().setValue('학생 정보').setFontWeight('bold').setBackground(COL.sun).setFontColor(COL.sunInk);
  sh.getRange(6, 1, info.length, 2).setValues(info).setVerticalAlignment('middle').setWrap(true).setFontSize(10)
    .setBorder(true, true, true, true, true, true, '#E2E3E3', SpreadsheetApp.BorderStyle.SOLID);
  sh.getRange(6, 1, info.length, 1).setFontColor(COL.muted);
  sh.getRange(6, 2).setFontColor(stc[1]).setBackground(stc[2]).setFontWeight('bold');
  const ph = waPhone_(x.phone);
  if (ph) sh.getRange(10, 2).setRichTextValue(link_('💬 ' + ph.slice(3, 6) + ' ' + ph.slice(6, 8) + ' ' + ph.slice(8, 10) + ' ' + ph.slice(10), 'https://wa.me/' + ph));
  if (x.link) sh.getRange(5 + info.length + 2, 1, 1, 2).merge().setRichTextValue(link_('🔗 이 학생의 학습지 열기', x.link));
  // 최근 기록 (최신 30줄)
  const H = ['날짜', '주제', '종류', '첫 시도', '2번째', '정답 봄', '틀린 문제', '시간'];
  sh.getRange(5, 4, 1, H.length).setValues([H]).setBackground(COL.brand).setFontColor('#FFFFFF').setFontWeight('bold').setFontSize(10);
  const recent = rows.slice().sort((a, b) => (b.d + b.t).localeCompare(a.d + a.t)).slice(0, 30);
  if (!recent.length) { sh.getRange(6, 4, 1, H.length).merge().setValue('아직 공부 기록이 없어요.').setFontColor(COL.muted); return; }
  const vals = recent.map(r => [r.d.slice(5).replace('-', '.') + ' ' + r.t, 'Mövzu ' + r.n + '. ' + r.name,
    r.start ? '시작만 (' + (r.done || '-').replace(/\s/g, '') + ')' : r.isNew ? '새 주제' : '복습',
    r.start ? '—' : r.stars + '/' + r.total, r.start ? '—' : r.second, r.start ? '—' : r.shown, r.wrong || '-', r.min ? r.min + '분' : '—']);
  sh.getRange(6, 4, vals.length, H.length).setValues(vals).setFontSize(10).setVerticalAlignment('middle')
    .setBorder(true, true, true, true, true, true, '#E2E3E3', SpreadsheetApp.BorderStyle.SOLID);
  recent.forEach((r, i) => {
    const c = sh.getRange(6 + i, 6);
    if (r.isNew) c.setBackground(COL.okSoft).setFontColor(COL.ok).setFontWeight('bold');
    else if (r.start) c.setBackground(COL.warnSoft).setFontColor(COL.warn);
    if (!r.start && r.total && r.stars / r.total < 0.7) sh.getRange(6 + i, 7).setFontColor(COL.warn).setFontWeight('bold');
  });
}

/* ---------- 🎨 탭 정리 (처음 한 번) ---------- */
function tidySheets() {
  const ss = SpreadsheetApp.getActive();
  setupDaily_(ss); setupReports_(ss); setupRegistration_(ss);
  setupDetail_();
  refreshPanel();
  const order = [
    [SH_PANEL, '#5145E6'], [SH_DETAIL, '#E8790C'], [SH_STUDENTS, '#F6A623'], [SH_REPORTS, '#8E6CEF'], [SH_DAILY, '#3BA6F5'],
    [SH_REG, '#E35D7F'], [BOOKS['1-1'].level, '#9AA0A6'], [BOOKS['1-2'].level, '#9AA0A6'], [BOOKS['1-1'].results, '#9AA0A6'], [BOOKS['1-2'].results, '#9AA0A6'],
    [SH_SETTINGS, '#5F6368']];
  let pos = 1;
  order.forEach(([name, color]) => {
    const sh = ss.getSheetByName(name);
    if (!sh) return;
    sh.setTabColor(color);
    ss.setActiveSheet(sh); ss.moveActiveSheet(pos++);
    if (name === SH_PANEL || name === SH_DETAIL || name === SH_SETTINGS) return;
    // 제목 줄 고정 · 줄무늬 · 필터
    sh.setFrozenRows(1);
    const lastCol = Math.max(sh.getLastColumn(), 1);
    try { if (!sh.getBandings().length) sh.getRange(1, 1, sh.getMaxRows(), lastCol).applyRowBanding(SpreadsheetApp.BandingTheme.LIGHT_GREY, true, false); } catch (e) {}
    try { if (!sh.getFilter()) sh.getRange(1, 1, sh.getMaxRows(), lastCol).createFilter(); } catch (e) {}
    sh.getRange(1, 1, 1, lastCol).setWrap(true).setVerticalAlignment('middle').setFontWeight('bold');
    sh.setRowHeight(1, 42);
  });
  // 원장님이 직접 고치는 칸은 노란색 + 설명
  const st = ss.getSheetByName(SH_STUDENTS);
  if (st) {
    Object.keys(BOOKS).forEach(id => {
      const c = BOOKS[id].col;
      [c.LV_START, c.LV_RETRY].forEach(col => {
        st.getRange(2, col, Math.max(st.getMaxRows() - 1, 1), 1).setBackground(COL.edit);
        st.getRange(1, col).setNote(col === c.LV_START ? '✏️ 직접 고칠 수 있어요: 숫자를 바꾸면 그 주제부터 시작, 비우면 레벨 테스트를 다시 봐요.' : '✏️ 체크하면 레벨 테스트를 한 번 더 볼 수 있어요.');
      });
    });
    st.setColumnWidth(C.NAME, 170); st.setColumnWidth(C.LINK, 220);
  }
  const rp = ss.getSheetByName(SH_REPORTS);
  if (rp) { rp.getRange(2, 7, Math.max(rp.getMaxRows() - 1, 1), 1).setBackground(COL.edit); rp.getRange(1, 7).setNote('✏️ 선생님 한마디를 여기에 적으면 리포트에 바로 나와요.'); }
  const se = ss.getSheetByName(SH_SETTINGS);
  if (se) se.getRange(1, 2, Math.max(se.getLastRow(), 1), 1).setBackground(COL.edit);
  // 매시간 자동 새로 고침
  if (!ScriptApp.getProjectTriggers().some(t => t.getHandlerFunction() === 'refreshPanel')) {
    ScriptApp.newTrigger('refreshPanel').timeBased().everyHours(1).create();
  }
  ss.getSheetByName(SH_PANEL).activate();
  SpreadsheetApp.getUi().alert('정리 완료! 🎨\n\n· 📋 현황판: 학생별 상태 (매시간 자동 새로 고침)\n· 🔍 학생 보기: B3칸에서 이름을 고르세요\n· 노란 칸 = 원장님이 직접 고쳐도 되는 칸\n· 각 탭 제목 줄의 ▼ 필터로 원하는 학생만 볼 수 있어요');
}
