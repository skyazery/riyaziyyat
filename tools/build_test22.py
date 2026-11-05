"""Builds 2-2/test.html from the 2-1 test page (same code, new items and labels).
Run: python3 tools/build_test22.py TEST_ITEMS_JSON   (then python3 tools/tts_all.py for the test audio)"""
import json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
items = json.load(open(sys.argv[1]))
s = open(os.path.join(ROOT, '2-1', 'test.html'), encoding='utf-8').read()


def rep(a, b, n=1):
    global s
    c = s.count(a)
    assert c == n, (a, c)
    s = s.replace(a, b)


rep('<title>Riyaziyyat Yoxlama Testi · 2-ci sinif, 1-ci hissə</title>', '<title>Riyaziyyat Yoxlama Testi · 2-ci sinif, 2-ci hissə</title>')
rep("const KITAB='2-1'", "const KITAB='2-2'")
rep('.bk-2-1{--bk1:#E8590C;--bk2:#FF922B;--bk3:#B8430A;--bkink:#D9480F}',
    '.bk-2-1{--bk1:#E8590C;--bk2:#FF922B;--bk3:#B8430A;--bkink:#D9480F}\n.bk-2-2{--bk1:#7048E8;--bk2:#9775FA;--bk3:#5032B8;--bkink:#6741D9}')
rep("bk bk-2-1'},h('div',{class:'part','aria-hidden':'true'},h('b',{},'1'),", "bk bk-2-2'},h('div',{class:'part','aria-hidden':'true'},h('b',{},'2'),")
rep("h('b',{},'2-ci sinif riyaziyyat'),h('i',{},'1-ci hissə')", "h('b',{},'2-ci sinif riyaziyyat'),h('i',{},'2-ci hissə')")
rep("h('span',{},'2-ci sinif · 1-ci hissə')", "h('span',{},'2-ci sinif · 2-ci hissə')")
rep("'Riyaziyyat · 2-ci sinif · 1-ci hissə – Yoxlama testi'", "'Riyaziyyat · 2-ci sinif · 2-ci hissə – Yoxlama testi'")
rep("const KEY='az-math-test-2-1-v1-'", "const KEY='az-math-test-2-2-v1-'")
a = s.index('const DATA = ')
b = s.index('\n', a)
s = s[:a] + 'const DATA = ' + json.dumps(items, ensure_ascii=False) + ';' + s[b:]
open(os.path.join(ROOT, '2-2', 'test.html'), 'w', encoding='utf-8').write(s)
print('test.html', len(s))
