"""Builds 3-1/test.html or 3-2/test.html from the 2-2 test page (same code, new items and labels).
Run: python3 tools/build_test3.py 3-1 TEST_ITEMS_JSON   (then python3 tools/tts_all.py for the test audio)"""
import json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
bid, items = sys.argv[1], json.load(open(sys.argv[2]))
part = bid[-1]
pname = '1-ci hissə' if part == '1' else '2-ci hissə'
COL = {'3-1': '.bk-3-1{--bk1:#1098AD;--bk2:#3BC9DB;--bk3:#0B7285;--bkink:#0C8599}',
       '3-2': '.bk-3-2{--bk1:#D6336C;--bk2:#F06595;--bk3:#A61E4D;--bkink:#C2255C}'}[bid]
s = open(os.path.join(ROOT, '2-2', 'test.html'), encoding='utf-8').read()


def rep(a, b, n=1):
    global s
    c = s.count(a)
    assert c == n, (a, c)
    s = s.replace(a, b)


rep('<title>Riyaziyyat Yoxlama Testi · 2-ci sinif, 2-ci hissə</title>', '<title>Riyaziyyat Yoxlama Testi · 3-cü sinif, %s</title>' % pname)
rep("const KITAB='2-2'", "const KITAB='%s'" % bid)
rep('.bk-2-2{--bk1:#7048E8;--bk2:#9775FA;--bk3:#5032B8;--bkink:#6741D9}', COL)
rep("bk bk-2-2'},h('div',{class:'part','aria-hidden':'true'},h('b',{},'2'),", "bk bk-%s'},h('div',{class:'part','aria-hidden':'true'},h('b',{},'%s')," % (bid, part))
rep("h('b',{},'2-ci sinif riyaziyyat'),h('i',{},'2-ci hissə')", "h('b',{},'3-cü sinif riyaziyyat'),h('i',{},'%s')" % pname)
rep("h('span',{},'2-ci sinif · 2-ci hissə')", "h('span',{},'3-cü sinif · %s')" % pname)
rep("'Riyaziyyat · 2-ci sinif · 2-ci hissə – Yoxlama testi'", "'Riyaziyyat · 3-cü sinif · %s – Yoxlama testi'" % pname)
rep("const KEY='az-math-test-2-2-v1-'", "const KEY='az-math-test-%s-v1-'" % bid)
a = s.index('const DATA = ')
b = s.index('\n', a)
s = s[:a] + 'const DATA = ' + json.dumps(items, ensure_ascii=False) + ';' + s[b:]
assert '2-ci sinif' not in s.replace(json.dumps(items, ensure_ascii=False), '')
open(os.path.join(ROOT, bid, 'test.html'), 'w', encoding='utf-8').write(s)
print(bid, 'test.html', len(s))
