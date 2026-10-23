"""Builds 2-1/test.html from the 1-2 test page (same code, new items and labels).
Run: python3 build_test21.py TEST_ITEMS_JSON"""
import json, sys

ROOT = '/home/claude/riyaziyyat'
items = json.load(open(sys.argv[1]))
s = open(ROOT + '/1-2/test.html', encoding='utf-8').read()


def rep(a, b, n=1):
    global s
    c = s.count(a)
    assert c == n, (a, c)
    s = s.replace(a, b)


rep('<title>Riyaziyyat Yoxlama Testi · 2-ci hissə</title>', '<title>Riyaziyyat Yoxlama Testi · 2-ci sinif, 1-ci hissə</title>')
rep("<script>const KITAB='1-2';</script>", "<script>const KITAB='2-1';</script>")
rep('.bk-1-2{--bk1:#139067;--bk2:#3CCB8E;--bk3:#0B6A4B;--bkink:#139067}',
    '.bk-1-2{--bk1:#139067;--bk2:#3CCB8E;--bk3:#0B6A4B;--bkink:#139067}\n.bk-2-1{--bk1:#E8590C;--bk2:#FF922B;--bk3:#B8430A;--bkink:#D9480F}')
rep("h('div',{class:'card hdr bk bk-1-2'},h('div',{class:'part','aria-hidden':'true'},h('b',{},'2'),",
    "h('div',{class:'card hdr bk bk-2-1'},h('div',{class:'part','aria-hidden':'true'},h('b',{},'1'),")
rep("h('b',{},'1-ci sinif riyaziyyat'),h('i',{},'2-ci hissə')", "h('b',{},'2-ci sinif riyaziyyat'),h('i',{},'1-ci hissə')")
rep("h('span',{},'1-ci sinif · 2-ci hissə')", "h('span',{},'2-ci sinif · 1-ci hissə')")
rep("'Riyaziyyat · 1-ci sinif · 2-ci hissə – Yoxlama testi'", "'Riyaziyyat · 2-ci sinif · 1-ci hissə – Yoxlama testi'")
rep("const KEY='az-math-test-1-2-v1-'", "const KEY='az-math-test-2-1-v1-'")
a = s.index('const DATA = ')
b = s.index('\n', a)
s = s[:a] + 'const DATA = ' + json.dumps(items, ensure_ascii=False) + ';' + s[b:]
open(ROOT + '/2-1/test.html', 'w', encoding='utf-8').write(s)
print('test.html', len(s))
