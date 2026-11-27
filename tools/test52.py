"""Yoxlama testi (5-2): 20 tapşırıq. Run: python3 tools/test52.py OUTDIR → OUTDIR/test_items.json"""
import sys
from testcommon import *
from kit56 import ang, adj, cross, poly_l, rtri, prism3, pie, legend, bars

# A. İfadələr, tənliklər, bərabərsizliklər
it('A', 'İfadənin qiyməti', 'a = 6 olduqda 4a − 5 ifadəsinin qiymətini tapın.', '4 · 6 = 24, sonra 5 çıxın.', '19',
   tokens=['4a − 5', '=', N], answer=[19])
it('A', 'Sadələşdirmə', 'İfadəni sadələşdirin: 7x + 2x − 3x.', 'Əmsalları hesablayın: 7 + 2 − 3.', '6x',
   tokens=['7x + 2x − 3x', '=', N, 'x'], answer=[6])
it('A', 'Tənlik', 'Tənliyi həll edin: 4x + 9 = 37.', '4x = 37 − 9 = 28.', '7',
   tokens=['4x + 9 = 37', 'x =', N], answer=[7])
it('A', 'Bərabərsizlik', 'x < 5 bərabərsizliyinin neçə natural həlli var?', '1, 2, 3, 4.', '4',
   tokens=['x < 5', '→', N], answer=[4])
# B. Bucaqlar və xətlər
it('B', 'Tənbölən', 'Tənbölən 140°-li bucağı iki bərabər hissəyə bölür. Hər hissə neçə dərəcədir?', '140 : 2.', '70°',
   tokens=[N, '°'], answer=[70])
it('B', 'Qonşu bucaqlar', 'Qonşu bucaqlardan biri 65°-dir. Digəri neçə dərəcədir?', 'Qonşu bucaqların cəmi 180°-dir.', '115°',
   img=adj(65, '65°', '?'), tokens=[N, '°'], answer=[115])
it('B', 'Qarşılıqlı bucaqlar', 'İki düz xətt kəsişib. Sual işarəsi olan bucaq neçə dərəcədir?', 'Qarşılıqlı bucaqlar bərabərdir.', '50°',
   img=cross(50, ['50°', '', '?', '']), tokens=[N, '°'], answer=[50])
it('B', 'Üçbucağın növü', 'Tərəfləri 6 sm, 6 sm və 4 sm olan üçbucaq hansı üçbucaqdır?', 'İki tərəfi bərabərdir.', 'bərabəryanlı',
   options=[chip('bərabərtərəfli', 40), chip('bərabəryanlı', 40), chip('müxtəliftərəfli', 40)], answer=1)
# C. Sahə
it('C', 'Düzbucaqlı üçbucağın sahəsi', 'Katetləri 8 sm və 6 sm olan düzbucaqlı üçbucağın sahəsini tapın.', '8 · 6 : 2.', '24',
   img=rtri(8, 6, '8 sm', '6 sm', 30), tokens=['S =', N, 'sm²'], answer=[24])
it('C', 'Mürəkkəb fiqur', 'Fiqurun sahəsini tapın. Ölçülər santimetrlədir.', 'Böyük düzbucaqlıdan kəsilmiş kvadratı çıxın: 6 · 5 − 2 · 2.', '26',
   img=poly_l([(0, 0), (6, 0), (6, 3), (4, 3), (4, 5), (0, 5)], [(3, -0.6, '6'), (-0.7, 2.5, '5'), (5, 3.6, '2'), (6.7, 1.5, '3')], 32), tokens=['S =', N, 'sm²'], answer=[26])
it('C', 'Paralel tərəflər', 'Düzbucaqlıda neçə cüt paralel tərəf var?', 'Qarşı tərəflər paraleldir.', '2',
   tokens=[N], answer=[2])
it('C', 'Üçbucağın perimetri', 'Bərabərtərəfli üçbucağın tərəfi 8 sm-dir. Perimetrini tapın.', '8 · 3.', '24',
   tokens=['P =', N, 'sm'], answer=[24])
# D. Fəza fiqurları
it('D', 'Kubun səthi', 'Tili 4 sm olan kubun səthinin sahəsini tapın.', '6 · 4 · 4.', '96',
   tokens=['S =', N, 'sm²'], answer=[96])
it('D', 'Kuboidin həcmi', 'Ölçüləri 6 sm, 4 sm və 5 sm olan kuboidin həcmini tapın.', '6 · 4 · 5.', '120',
   tokens=['V =', N, 'sm³'], answer=[120])
it('D', 'Sahə vahidləri', '3 m² neçə dm²-dir?', '1 m² = 100 dm².', '300',
   tokens=['3 m² =', N, 'dm²'], answer=[300])
it('D', 'Həcm vahidləri', '4 litr neçə ml-dir?', '1 l = 1 000 ml.', '4 000',
   tokens=['4 l =', N, 'ml'], answer=[4000])
# E. Statistika
it('E', 'Ədədi orta', '6, 9 və 12 ədədlərinin ədədi ortasını tapın.', '(6 + 9 + 12) : 3.', '9',
   tokens=['Orta =', N], answer=[9])
it('E', 'Dairəvi diaqram', 'Sinifdə 20 şagird var. Diaqrama görə neçə şagird şahmatı seçib?', '20-nin 25%-i.', '5',
   img=hstack([pie([(0.25, (102, 187, 106), '25%'), (0.75, (66, 165, 245), '75%')], 200), legend([((102, 187, 106), 'Şahmat'), ((66, 165, 245), 'Futbol')], 30)], 16), tokens=[N, 'şagird'], answer=[5])
it('E', 'Sütunlu diaqram', 'Diaqrama görə çərşənbə axşamı neçə kitab oxunub?', 'Sütunun ucundan sola baxın.', '8',
   img=bars([(txt(d_, 26), v) for d_, v in [('B.e', 5), ('Ç.a', 8), ('Ç', 3)]], 10, 24, 60), tokens=[N], answer=[8])
it('E', 'Diaqram seçimi', 'Temperaturun dəyişməsini göstərmək üçün hansı diaqram daha uyğundur?', 'Dəyişmə – xətlə göstərilir.', 'xətti diaqram',
   options=[chip('dairəvi diaqram', 40), chip('xətti diaqram', 40)], answer=1)

AREAS = [
    {'code': 'A', 'name': 'İfadələr və tənliklər', 'topics': list(range(224, 230)), 'home': 'Gündəlik məsələləri tənliklə yazın: «Bir neçə alma aldıq, 3-nü yedik, 5 qaldı – əvvəl neçə idi?»'},
    {'code': 'B', 'name': 'Bucaqlar və xətlər', 'topics': [230, 231, 234, 235], 'home': 'Evdə paralel və perpendikulyar xətləri (pəncərə, kitab rəfi) tapın, saatın əqrəbləri ilə bucaq düzəldin.'},
    {'code': 'C', 'name': 'Sahə', 'topics': [232, 233], 'home': 'Otağın planını kağızda çəkib hissələrə bölün və sahəsini hesablayın.'},
    {'code': 'D', 'name': 'Fəza fiqurları', 'topics': list(range(236, 241)), 'home': 'Qutunun ölçülərini ölçüb həcmini tapın; mətbəxdə litr və mililitr işarələrinə baxın.'},
    {'code': 'E', 'name': 'Statistika', 'topics': list(range(241, 244)), 'home': 'Bir həftə ərzində ailədə oxunan səhifələri yazın, ədədi ortanı tapın və sütunlu diaqram çəkin.'},
]
save_test(sys.argv[1], AREAS, '2-ci hissəsini', '5-ci')
