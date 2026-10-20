/* Şagird idarəsi – şəxsi link və nəticələrin müəllim cədvəlinə göndərilməsi.
   API_URL: Google Apps Script "Web app" ünvanı (müəllim cədvəlində Deploy edəndən sonra yazılır). */
const API_URL = 'https://script.google.com/macros/s/AKfycbxjApYNtMnXK15asxzco_qI-H9a4pqpYvlgVbNtTl8XT1ex-wXyuVJ4zFy73eh4rWZ7/exec';

const SAGIRD_KEY = 'riyaziyyat-sagird';

/* Hansı kitab: səhifədə KITAB ('1-1' və ya '1-2') təyin olunubsa onu götürür */
function kitab() { try { if (typeof KITAB !== 'undefined' && KITAB) return KITAB; } catch (e) {} return '1-1'; }

/* URL-də ?s=KOD varsa onu yadda saxlayır, yoxdursa əvvəl yadda saxlananı qaytarır */
function sagirdKodu() {
  let c = null;
  try {
    const q = (new URLSearchParams(location.search).get('s') || '').trim().toUpperCase();
    if (/^[A-Z0-9]{6}$/.test(q)) c = q;
  } catch (e) {}
  if (c) { try { localStorage.setItem(SAGIRD_KEY, c); } catch (e) {} return c; }
  try { const s = localStorage.getItem(SAGIRD_KEY); if (s && /^[A-Z0-9]{6}$/.test(s)) return s; } catch (e) {}
  return null;
}

function sagirdAdiYaddas(code, name) {
  try { if (name) localStorage.setItem(SAGIRD_KEY + '-ad-' + code, name); return localStorage.getItem(SAGIRD_KEY + '-ad-' + code); } catch (e) { return null; }
}

async function sagirdMelumati(code) {
  const r = await fetch(API_URL + '?action=student&s=' + encodeURIComponent(code) + '&b=' + kitab(), { cache: 'no-store' });
  if (!r.ok) throw new Error('http ' + r.status);
  return r.json();
}

/* Səviyyə testinin nəticəsi: start – başlanğıc mövzu (kitabın son mövzusundan 1 çox = hamısını bilir), log – [mövzu, tapşırıq, düz(1)/səhv(0)] */
async function seviyyeGonder(code, start, log) {
  const r = await fetch(API_URL, { method: 'POST', body: JSON.stringify({ action: 'level', b: kitab(), s: code, start: start, log: log }) });
  if (!r.ok) throw new Error('http ' + r.status);
  return r.json();
}

async function testiGonder(code, ans, hints) {
  // text/plain: brauzer əlavə yoxlama sorğusu göndərmir
  const r = await fetch(API_URL, { method: 'POST', body: JSON.stringify({ action: 'submit', b: kitab(), s: code, ans: ans, hints: hints }) });
  if (!r.ok) throw new Error('http ' + r.status);
  return r.json();
}
