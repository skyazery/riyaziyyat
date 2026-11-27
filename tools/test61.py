"""Yoxlama testi (6-1): 20 tapşırıq. Run: python3 tools/test61.py OUTDIR → OUTDIR/test_items.json
Testin klaviaturasında mənfi düymə yoxdur: mənfi cavablı suallar seçim şəklindədir."""
import sys
from testcommon import *
from kit56 import cgrid, zline

# A. Qüvvət, sadə ədədlər, ƏBOB, ƏKOB
it('A', 'Qüvvət', 'Hesablayın: 3⁴.', '3 · 3 · 3 · 3.', '81', tokens=['3⁴', '=', N], answer=[81])
it('A', 'Sadə ədədlər', 'Hansı ədəd sadədir?', 'Sadə ədədin yalnız iki böləni var: 1 və özü.', '13',
   options=[chip('15', 56), chip('13', 56), chip('21', 56)], answer=1)
it('A', 'ƏBOB', 'ƏBOB(18, 24) neçədir?', 'Hər iki ədədi bölən ən böyük ədəd.', '6', tokens=['ƏBOB(18, 24)', '=', N], answer=[6])
it('A', 'ƏKOB', 'ƏKOB(6, 9) neçədir?', '6-ya və 9-a bölünən ən kiçik ədəd.', '18', tokens=['ƏKOB(6, 9)', '=', N], answer=[18])
# B. Nisbət, tənasüb, miqyas
it('B', 'Nisbətin ixtisarı', '20 : 35 nisbətini ixtisar edin.', 'Hər iki həddi 5-ə bölün.', '4 : 7', tokens=['20 : 35', '=', N, ':', N], answer=[4, 7])
it('B', 'Verilən nisbətdə bölmə', '45 ədədini 4 : 5 nisbətində bölün. Kiçik hissə neçədir?', '45 : 9 = 5, 4 · 5.', '20', tokens=[N], answer=[20])
it('B', 'Tənasüb', 'Tənasübdə x-i tapın: x : 6 = 10 : 15.', 'x · 15 = 6 · 10.', '4', tokens=['x : 6 = 10 : 15', 'x =', N], answer=[4])
it('B', 'Miqyas', 'Xəritənin miqyası 1 : 200 000-dir. Xəritədə 4 sm həqiqətdə neçə km-dir?', '1 sm = 2 km.', '8', tokens=[N, 'km'], answer=[8])
# C. Mütənasib asılılıq və faiz
it('C', 'Düz mütənasiblik', '3 kq alma 7,5 manatdır. 6 kq alma neçə manatdır?', 'Kütlə 2 dəfə artır – qiymət də.', '15', tokens=[N, 'manat'], answer=[15])
it('C', 'Tərs mütənasiblik', '6 fəhlə işi 4 günə görür. 3 fəhlə neçə günə görər?', 'Fəhlə 2 dəfə az – gün 2 dəfə çox.', '8', tokens=[N, 'gün'], answer=[8])
it('C', 'Nisbətin faizlə ifadəsi', '30 şagirddən 12-si qızdır. Qızlar neçə faizdir?', '12 : 30 = 0,4.', '40%', tokens=[N, '%'], answer=[40])
it('C', 'Dəyişmənin faizlə ifadəsi', 'Qiymət 40 manatdan 50 manata qalxdı. Neçə faiz artdı?', '10 : 40 = 0,25.', '25%', tokens=[N, '%'], answer=[25])
# D. Tam ədədlər
it('D', 'Müqayisə', 'Ən kiçik ədədi seçin.', 'Mütləq qiyməti böyük olan mənfi ədəd kiçikdir.', '−9',
   options=[chip('−2', 56), chip('−9', 56), chip('0', 56)], answer=1)
it('D', 'Mütləq qiymət', '|−14| neçədir?', 'Mütləq qiymət – sıfıra qədər məsafə.', '14', tokens=['|−14|', '=', N], answer=[14])
it('D', 'Toplama', 'Hesablayın: −8 + 15.', '15 − 8, böyüyün işarəsi müsbətdir.', '7', tokens=['−8 + 15', '=', N], answer=[7])
it('D', 'Vurma', '−6 · (−7) hasili neçədir?', 'Eyni işarəli ədədlərin hasili müsbətdir.', '42', tokens=['−6 · (−7)', '=', N], answer=[42])
# E. Koordinatlar
it('E', 'Nöqtənin koordinatları', 'A nöqtəsinin koordinatlarını seçin.', 'Əvvəl x (sağa-sola), sonra y (yuxarı-aşağı).', '(−3; 2)',
   img=cgrid(4, [(-3, 2, 'A')], 30), options=[chip('(−3; 2)', 48), chip('(2; −3)', 48), chip('(3; 2)', 48)], answer=0)
it('E', 'Rüblər', '(4; −1) nöqtəsi hansı rübdədir?', 'x müsbət, y mənfi – IV rüb.', 'IV',
   options=[chip('I', 56), chip('II', 56), chip('III', 56), chip('IV', 56)], answer=3)
it('E', 'Məsafə', 'A(−2; 3) və B(4; 3) nöqtələri arasındakı məsafəni tapın.', '|4 − (−2)| = 6.', '6', tokens=['AB =', N], answer=[6])
it('E', 'Simmetriya', 'B(5; 2) nöqtəsinə y oxuna nəzərən simmetrik nöqtəni seçin.', 'Absisin işarəsi dəyişir.', '(−5; 2)',
   options=[chip('(5; −2)', 48), chip('(−5; 2)', 48), chip('(−5; −2)', 48)], answer=1)

AREAS = [
    {'code': 'A', 'name': 'Qüvvət, ƏBOB və ƏKOB', 'topics': list(range(244, 248)), 'home': 'Konfet və ya meyvələri bərabər paketlərə bölərkən ƏBOB-u, iki avtobusun nə vaxt birlikdə gələcəyini hesablayarkən ƏKOB-u tapın.'},
    {'code': 'B', 'name': 'Nisbət və tənasüb', 'topics': list(range(248, 253)), 'home': 'Xəritədə iki şəhər arasındakı məsafəni xətkeşlə ölçüb miqyasa görə həqiqi məsafəni tapın.'},
    {'code': 'C', 'name': 'Mütənasiblik və faiz', 'topics': list(range(253, 257)), 'home': 'Reseptdəki ərzağı qonaqların sayına görə artırın; endirim yazılarında neçə faiz endirim olduğunu hesablayın.'},
    {'code': 'D', 'name': 'Tam ədədlər', 'topics': list(range(257, 264)), 'home': 'Hava proqnozunda mənfi temperaturları müqayisə edin: «Səhər −3°, günorta 5° – neçə dərəcə isindi?»'},
    {'code': 'E', 'name': 'Koordinat sistemi', 'topics': list(range(264, 267)), 'home': 'Dama taxtası və ya dəftər vərəqində koordinat oyunu oynayın: nöqtəni koordinatı ilə tapın.'},
]
save_test(sys.argv[1], AREAS, '1-ci hissəsini', '6-cı')
