"""Yoxlama testi (5-1): 20 tapşırıq. Run: python3 tools/test51.py OUTDIR → OUTDIR/test_items.json"""
import sys
from testcommon import *

# A. Natural ədədlər
it('A', 'Çoxrəqəmli ədədlər', 'Ədədi rəqəmlərlə yazın: üç milyon iki yüz min qırx.', 'Milyonlar, minliklər və təkliklər sinfini ayrıca yazın: 3 | 200 | 040.', '3 200 040',
   tokens=[N], answer=[3200040])
it('A', 'Yuvarlaqlaşdırma', '45 682 ədədini minliklərə qədər yuvarlaqlaşdırın.', 'Yüzlüklər rəqəmi 6-dır, 5-dən böyükdür: minliklər 1 artır.', '46 000',
   tokens=['45 682', '≈', N], answer=[46000])
it('A', 'Əməllərin ardıcıllığı', 'İfadənin qiymətini tapın: 60 − 4 · 3².', 'Əvvəl qüvvət, sonra vurma, sonra çıxma: 60 − 4 · 9.', '24',
   tokens=['60 − 4 · 3²', '=', N], answer=[24])
it('A', 'Bölənlər', 'Hansı ədəd 9-a bölünür?', 'Rəqəmlərin cəmi 9-a bölünməlidir.', '4 518',
   options=[chip('4 518', 56), chip('3 721', 56), chip('6 404', 56)], answer=0)
# B. Adi kəsrlər
it('B', 'Qarışıq ədəd', '17/5 kəsrini qarışıq ədəd şəklində yazın.', '17 : 5 = 3 (qalıq 2).', '3 2/5',
   tokens=['17/5', '=', N, N, '/ 5'], answer=[3, 2])
it('B', 'İxtisar', '18/24 kəsrini ixtisar edin.', 'Surət və məxrəci 6-ya bölün.', '3/4',
   tokens=['18/24', '=', N, '/', N], answer=[3, 4])
it('B', 'Kəsrlərin toplanması', 'Hesablayın: 1/4 + 2/3.', 'Ortaq məxrəc 12: 3/12 + 8/12.', '11/12',
   tokens=['1/4 + 2/3', '=', N, '/', N], answer=[11, 12])
it('B', 'Qarışıq ədədlərin çıxılması', 'Hesablayın: 5 1/3 − 2 2/3.', '5 1/3 = 4 4/3. 4 4/3 − 2 2/3 = 2 2/3.', '2 2/3',
   tokens=['5 1/3 − 2 2/3', '=', N, N, '/', N], answer=[2, 2, 3])
# C. Kəsrlərin vurulması və bölünməsi
it('C', 'Kəsrlərin vurulması', 'Hesablayın: 3/5 · 10/9.', 'Əvvəl ixtisar edin: 3 ilə 9-u, 5 ilə 10-u.', '2/3',
   tokens=['3/5 · 10/9', '=', N, '/', N], answer=[2, 3])
it('C', 'Kəsrlərin bölünməsi', 'Hesablayın: 5/6 : 5/12.', 'Bölənin tərs kəsrinə vurun: 5/6 · 12/5.', '2',
   tokens=['5/6 : 5/12', '=', N], answer=[2])
it('C', 'Ədədin hissəsi', '48 ədədinin 3/8 hissəsini tapın.', '48 : 8 · 3.', '18',
   tokens=['48', '·', '3/8', '=', N], answer=[18])
it('C', 'Hissəsinə görə ədəd', '2/7 hissəsi 10 olan ədədi tapın.', '10 : 2 · 7.', '35',
   tokens=['10', ':', '2/7', '=', N], answer=[35])
# D. Onluq kəsrlər
it('D', 'Onluq kəsrlərin müqayisəsi', 'Ən böyük ədədi seçin.', 'Tam hissələr bərabərdir, ondabirləri müqayisə edin.', '2,6',
   options=[chip('2,59', 56), chip('2,6', 56), chip('2,509', 56)], answer=1)
it('D', 'Onluq kəsrlərin toplanması', 'Hesablayın: 4,75 + 2,6.', 'Vergülü vergülün altında yazın.', '7,35',
   tokens=['4,75 + 2,6', '=', N, ',', N], answer=[7, 35])
it('D', 'Onluq kəsrlərin vurulması', 'Hesablayın: 1,2 · 0,5.', '12 · 5 = 60, vergüldən sonra 2 rəqəm: 0,60.', '0,6',
   tokens=['1,2 · 0,5', '=', N, ',', N], answer=[0, 6])
it('D', 'Onluq kəsrə bölmə', 'Hesablayın: 3,6 : 0,4.', 'Hər ikisində vergülü 1 rəqəm sağa keçirin: 36 : 4.', '9',
   tokens=['3,6 : 0,4', '=', N], answer=[9])
# E. Faiz
it('E', 'Faiz və kəsr', '3/5 kəsrini faizlə ifadə edin.', '3/5 = 60/100.', '60%',
   tokens=['3/5', '=', N, '%'], answer=[60])
it('E', 'Ədədin faizi', '250 ədədinin 20%-ni tapın.', '250 · 0,2.', '50',
   tokens=['20%', '·', '250', '=', N], answer=[50])
it('E', 'Faizinə görə ədəd', '30%-i 12 olan ədədi tapın.', '12 : 30 · 100.', '40',
   tokens=['30% → 12', '100% →', N], answer=[40])
it('E', 'Faizlə azaltma', 'Qiyməti 60 manat olan ayaqqabıya 25% endirim edildi. Yeni qiymət nə qədərdir?', '60-ın 25%-i 15 manatdır: 60 − 15.', '45',
   img=hstack([em('👟', 80), em('🏷️', 70)], 14), tokens=[N, 'manat'], answer=[45])

AREAS = [
    {'code': 'A', 'name': 'Natural ədədlər', 'topics': list(range(191, 199)), 'home': 'Qəzetdə və ya internetdə böyük ədədləri (əhali, məsafə) birlikdə oxuyun və minliklərə qədər yuvarlaqlaşdırın.'},
    {'code': 'B', 'name': 'Adi kəsrlər', 'topics': list(range(199, 204)), 'home': 'Yemək hazırlayanda reseptdəki 1/2, 3/4 stəkan kimi ölçüləri toplayın: «Cəmi neçə stəkan oldu?»'},
    {'code': 'C', 'name': 'Kəsrlərin vurulması və bölünməsi', 'topics': list(range(204, 209)), 'home': 'Uşaqdan soruşun: «24 konfetin 3/4 hissəsi neçədir?», «Pulunun yarısı 5 manatdırsa, nə qədər pulun var?»'},
    {'code': 'D', 'name': 'Onluq kəsrlər', 'topics': list(range(209, 220)), 'home': 'Mağazada qiymətləri (2,45 manat) toplayın və 3 dənəsinin qiymətini hesablatdırın.'},
    {'code': 'E', 'name': 'Faiz', 'topics': list(range(220, 224)), 'home': 'Endirim yazılarına baxın: «20% endirimlə bu neçə manat olar?»'},
]
save_test(sys.argv[1], AREAS, '1-ci hissəsini', '5-ci')
