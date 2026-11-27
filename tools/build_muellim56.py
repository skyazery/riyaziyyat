"""Builds 5-1, 5-2, 6-1, 6-2 muellim.html (cavablar, səviyyə testi, yoxlama testi, qiymətləndirmə) in the same layout as 2-1/muellim.html.
Run: python3 tools/build_muellim56.py 5-1 TEST_ITEMS_JSON"""
import html, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BID = sys.argv[1]
B = ROOT + '/' + BID
PN = '1-ci hissə' if BID[-1] == '1' else '2-ci hissə'
PG = '1-ci hissəsi' if BID[-1] == '1' else '2-ci hissəsi'
GR = {'5': '5-ci', '6': '6-cı'}[BID[0]]
GRN = GR + ' sinfin'
LOGO, PREV, PREVT = {'5-1': ('📙', '../4-2/muellim.html', '← 4-cü sinif, 2-ci hissənin cavabları'),
                     '5-2': ('📗', '../5-1/muellim.html', '← 5-ci sinif, 1-ci hissənin cavabları'),
                     '6-1': ('📘', '../5-2/muellim.html', '← 5-ci sinif, 2-ci hissənin cavabları'),
                     '6-2': ('📕', '../6-1/muellim.html', '← 6-cı sinif, 1-ci hissənin cavabları')}[BID]
# Şagirdlər cədvəlində LV_START və LV_RETRY sütunları (Code.gs: 5-1 49–53, 5-2 54–58, 6-1 59–63, 6-2 64–68)
COLS = {'5-1': ('AY', 'BA'), '5-2': ('BD', 'BF'), '6-1': ('BI', 'BK'), '6-2': ('BN', 'BP')}[BID]
topics = json.load(open(B + '/data/topics.json'))['topics']
T = {t['n']: t for t in topics}
test = json.load(open(sys.argv[2]))
FIRST, LAST = topics[0]['n'], topics[-1]['n']
idx = open(B + '/index.html', encoding='utf-8').read()
sections = eval(re.search(r"sections:(\[\[.*?\]\])", idx).group(1))
lvq = eval(re.search(r"lvq:(\[\[\[.*?\]\]\])", idx).group(1))
e = html.escape

head = open(ROOT + '/2-1/muellim.html', encoding='utf-8').read()
head = head[:head.index('<body>')]
head = head.replace('<title>Müəllim üçün – 2-ci sinif riyaziyyat (1-ci hissə)</title>', '<title>Müəllim üçün – %s sinif riyaziyyat (%s)</title>' % (GR, PN))
assert GR + ' sinif' in head
out = [head, '<body><div class="wrap">',
       '<div class="card hdr"><div class="logo">%s</div><div class="brand"><b>Müəllim üçün</b><span>%s sinif riyaziyyat · %s · cavablar və qiymətləndirmə</span></div></div>' % (LOGO, GR, PN),
       '<p class="muted">Bu səhifə müəllim və valideynlər üçündür. Şagirdlərə <a href="../">əsas səhifənin</a> şəxsi linkini göndərin – %s %s həmin linklə açılır (səhifənin aşağısındakı kitab keçidləri). '
       '<a href="%s">%s</a></p>' % (GRN, PG, PREV, PREVT),
       '<h2>Mövzular üzrə cavablar</h2>']
for t in topics:
    lis = ''.join('<li><b>%d.</b> %s <span class="ans">→ %s</span></li>' % (k + 1, e(p['ins']), e(p['ans'])) for k, p in enumerate(t['problems']))
    out.append('<details class="card"><summary><b>Mövzu %d. %s</b></summary><p class="muted">%s</p><ol class="al">%s</ol></details>' % (t['n'], e(t['title']), e(t['concept']), lis))

rows = ''
for (name, a, b), qs in zip(sections, lvq):
    cells = '<br>'.join('Mövzu %d, tapşırıq %d – cavab: %s' % (n, i + 1, e(T[n]['problems'][i]['ans'])) for n, i in qs)
    rows += '<tr><td>%d. %s (Mövzu %d–%d)</td><td>%s</td></tr>' % (sections.index([name, a, b]) + 1, e(name), a, b, cells)
out.append('<div class="card"><h2>Səviyyə testi</h2><p class="muted">' + GRN + ' ' + PG.replace('hissəsi', 'hissəsini') + ' ilk dəfə açanda qısa səviyyə testi təklif olunur. Hər bölmədən 2 tapşırıq verilir; ikisi də düzdürsə növbəti bölməyə keçir. '
           'Səhv cavab olan kimi test bitir və şagird həmin bölmənin ilk mövzusundan başlayır. Əvvəlki mövzular həmişə açıqdır.</p>'
           '<div class="tw"><table><tr><th>Bölmə</th><th>Tapşırıqlar</th></tr>%s</table></div>'
           '<p class="home">📋 Müəllim cədvəlində (Şagirdlər) %s sütunu – bu hissənin başlanğıc mövzusu (%d–%d). Rəqəmi dəyişsəniz şagird o mövzudan başlayır, silsəniz testi yenidən edir. %s sütununu işarələsəniz testi bir dəfə də edə bilər.</p></div>' % (rows, COLS[0], FIRST, LAST, COLS[1]))

rows = ''.join('<tr><td>%d</td><td>%s</td><td>%s</td><td>%s</td></tr>' % (k + 1, it['area'], e(it['skill']), e(it['disp'])) for k, it in enumerate(test['items']))
out.append('<div class="card"><h2>Yoxlama testi – cavablar</h2><div class="tw"><table><tr><th>№</th><th>Sahə</th><th>Nə yoxlanır</th><th>Cavab</th></tr>%s</table></div></div>' % rows)

g = ['<div class="card"><h2>Qiymətləndirmə bələdçisi</h2><p class="muted">Test bitəndə şagirdin səhifəsində valideyn hesabatı avtomatik hazırlanır. Bu cədvəl həmin hesabatın meyarlarıdır.</p>']
for ar in test['areas']:
    tl = ', '.join(str(n) for n in ar['topics'])
    trs = ''
    for k, L in enumerate(test['levels']):
        bal = {0: '4', 1: '3', 2: '2', 3: '0–1'}[k]
        trs += '<tr><td>%s</td><td>%s</td><td>%s</td></tr>' % (bal, e(L['name']), e(L['text'].replace('{t}', tl)))
    g.append('<h3>%s. %s</h3><div class="tw"><table><tr><th>Bal</th><th>Səviyyə</th><th>Valideynə izah</th></tr>%s</table></div><p class="home">🏠 %s</p>' % (ar['code'], e(ar['name']), trs, e(ar['home'])))
ranges = ['18–20', '14–17', '10–13', '0–9']
trs = ''.join('<tr><td>%s</td><td>%s</td><td>%s</td></tr>' % (r, e(o['name']), e(o['text'])) for r, o in zip(ranges, test['overall']))
g.append('<h3>Ümumi nəticə</h3><div class="tw"><table><tr><th>Bal</th><th>Nəticə</th><th>Valideynə izah</th></tr>%s</table></div></div>' % trs)
out += g
out.append('</div></body></html>')
open(B + '/muellim.html', 'w', encoding='utf-8').write(''.join(out))
print('muellim.html ok')
