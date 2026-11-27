"""Səs üçün mətn: riyazi işarələri sözlə oxunan şəklə çevirir (4-cü sinif kitabları).
Ekranda görünən mətn və səs id-si dəyişmir; yalnız səsə verilən mətn dəyişir."""
import re

ONES = {'0': '', '1': 'bir', '2': 'iki', '3': 'üç', '4': 'dörd', '5': 'beş', '6': 'altı', '7': 'yeddi', '8': 'səkkiz', '9': 'doqquz'}
TENS = {'1': 'on', '2': 'iyirmi', '3': 'otuz', '4': 'qırx', '5': 'əlli', '6': 'altmış', '7': 'yetmiş', '8': 'səksən', '9': 'doxsan'}


def last_word(n):
    """ədədin oxunuşunun son sözü (şəkilçi seçmək üçün)"""
    s = str(int(n))
    if s == '0':
        return 'sıfır'
    if s.endswith('000'):
        return 'min'
    if s.endswith('00'):
        return 'yüz'
    if s[-1] != '0':
        return ONES[s[-1]]
    return TENS[s[-2]]


def back(word):
    for ch in reversed(word):
        if ch in 'aıou':
            return True
        if ch in 'eəiöü':
            return False
    return False


def loc(n):
    """yerlik hal: 4-də, 6-da"""
    w = last_word(n)
    return '%s-%s' % (n, 'da' if back(w) else 'də')


def frac(a, b):
    return '%s %s' % (loc(b), a)


def dat(n):
    """yönlük hal: 2-yə, 3-ə, 6-ya"""
    w = last_word(n)
    return '%s-%s%s' % (n, 'y' if w[-1] in 'aıoueəiöü' else '', 'a' if back(w) else 'ə')


UNIT = {'mm': 'millimetr', 'sm': 'santimetr', 'dm': 'desimetr', 'm': 'metr', 'km': 'kilometr'}
SUP = {'⁰': '0', '¹': '1', '²': '2', '³': '3', '⁴': '4', '⁵': '5', '⁶': '6', '⁷': '7', '⁸': '8', '⁹': '9'}


def front(suf):
    return suf.translate(str.maketrans('aıou', 'əiöü'))


def speakable(t):
    s = t
    s = s.replace('>, < və ya =', 'böyükdür, kiçikdir və ya bərabərdir işarəsini')
    # 5–6-cı sinif: vahidlərin kvadratı və kubu, qüvvət, modul, koordinatlar, nisbət
    s = re.sub(r'\b(mm|sm|dm|km|m)²', lambda m: 'kvadrat ' + UNIT[m.group(1)], s)
    s = re.sub(r'\b(mm|sm|dm|km|m)³', lambda m: 'kub ' + UNIT[m.group(1)], s)
    s = re.sub(r'([\d)a-z])([⁰¹²³⁴⁵⁶⁷⁸⁹]+)', lambda m: m.group(1) + ' üstü ' + ''.join(SUP[c] for c in m.group(2)), s)
    s = re.sub(r'\|([^|]+)\|', r'modul \1', s)
    s = re.sub(r'(ƏBOB|ƏKOB)\(', r'\1 ', s)
    s = re.sub(r'\((−?\d+); (−?\d+)\)', r' \1 və \2 ', s)
    if 'nisbət' in s or 'tənasüb' in s or 'miqyas' in s:
        s = re.sub(r'(?<![\d,])(\d+) : (?=\d)', lambda m: dat(m.group(1)) + ' ', s)
    s = re.sub(r'(\d+),(\d\d) manat(\w*)', lambda m: (('%s manat %s qəpik' % (m.group(1), int(m.group(2)))) if m.group(1) != '0' else '%d qəpik' % int(m.group(2))) + front(m.group(3)), s)
    s = re.sub(r'neçə km/saat(\w*)', lambda m: 'saatda neçə kilometr' + front(m.group(1)), s)
    s = re.sub(r'(\d+(?:,\d+)?)%(?:-(\w+))?', lambda m: m.group(1) + ' faiz' + front(re.sub(r'^[nsy](?=[aəıiouöüe])', '', m.group(2) or '')), s)  # 15%-i → 15 faizi
    s = re.sub(r'(\d+) km/saat(\w*)', lambda m: 'saatda %s kilometr' % m.group(1) + front(m.group(2)), s)
    s = re.sub(r'kv\. sm', 'kvadrat santimetr', s)
    s = re.sub(r'kv\. m\b', 'kvadrat metr', s)
    s = re.sub(r'\((\d+); (\d+)\)', r'\1 və \2', s)
    s = re.sub(r'\b0?(\d{1,2}):00\b', r'\1', s)
    s = re.sub(r'\b0?(\d{1,2}):(\d\d)\b', r'\1 \2', s)
    s = re.sub(r'(\d+) (\d+)/(\d+)', lambda m: '%s tam %s' % (m.group(1), frac(m.group(2), m.group(3))), s)
    s = re.sub(r'(\d+)/(\d+)', lambda m: frac(m.group(1), m.group(2)), s)
    s = re.sub(r'(\d+),(\d+)', lambda m: '%s tam %s %s' % (m.group(1), loc(10 ** len(m.group(2))), m.group(2).lstrip('0') or '0'), s)
    s = s.replace('°-', ' dərəcə').replace('°', ' dərəcə')
    s = s.replace(' · ', ' vur ').replace(' − ', ' çıx ').replace(' + ', ' üstəgəl ').replace(' = ', ' bərabərdir ')
    s = s.replace(' ≈ ', ' təqribən ').replace(' > ', ' böyükdür ').replace(' < ', ' kiçikdir ')
    s = re.sub(r'(?<=[\w)]) : (?=[\w(])', ' böl ', s)
    s = s.replace('−', 'mənfi ')
    s = s.replace('(', '').replace(')', '')
    return re.sub(r'\s+', ' ', s).strip()


if __name__ == '__main__':
    for x in ['2/3 = 4/6, 9/12 = 3/4.', 'Lalə tortun 2/6 hissəsini yedi.', '1 2/7 = 1 + 2/7', '2,5 > 1,9; 3,45 < 3,48', 'Dəftər 0,80 manatdır.', '1,20 manat',
              'Avtomobilin sürəti 60 km/saatdır.', 'neçə km/saatdır?', '90°-dir, 60°-lik', 'A (3; 2) nöqtəsi', 'Dərs 08:30-da', 'Saat 3:00-da', '48 kv. sm', '(17 − 35 : 5) · 4 + 15 = 55', 'Dairələrə >, < və ya = yazın.']:
        print(x, '→', speakable(x))
