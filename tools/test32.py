"""Yoxlama testi (3-2): 20 tapşırıq. Run: python3 tools/test32.py OUTDIR → OUTDIR/test_items.json"""
import sys
from testcommon import *

EQUI = [(0, 1), (0.5, 0.13), (1, 1)]
RIGHT = [(0, 1), (0, 0.1), (1, 1)]
# A. Həndəsi fiqurlar
it('A', 'Paralel düz xətlər', 'Paralel düz xətləri seçin.', 'Paralel düz xətlər kəsişmir.', '2-ci şəkil',
   options=[lines_pair('cross', 150), lines_pair('parallel', 150), lines_pair('perp', 150)], answer=1)
it('A', 'Üçbucaqlar', 'Düzbucaqlı üçbucağı seçin.', 'Düz bucağın küncündə kiçik kvadrat işarəsi var.', '1-ci şəkil',
   options=[tri(RIGHT, size=130, right=1), tri(EQUI, size=130)], answer=0)
it('A', 'Simmetriya', 'Simmetrik şəkli seçin.', 'Qatlayanda iki hissə üst-üstə düşməlidir.', 'kəpənək',
   options=[sym('🦋', 120), sym('🐌', 120, False)], answer=0)
it('A', 'Fəza fiqurları', 'Kubun neçə üzü var?', 'Hər tərəfi sayın: üst, alt, ön, arxa, sağ, sol.', '6',
   img=solid('cube', 140), tokens=[N], answer=[6])
# B. Vurma və bölmə
it('B', 'İkirəqəmli ədədin vurulması', 'Hasili tapın.', '20 · 3 + 4 · 3 = 60 + 12.', '72',
   tokens=[24, '·', 3, '=', N], answer=[72])
it('B', 'Üçrəqəmli ədədin vurulması', 'Hasili tapın.', '200 · 3 + 10 · 3 + 2 · 3.', '636',
   tokens=[212, '·', 3, '=', N], answer=[636])
it('B', 'Qalıqlı bölmə', 'Qalıqlı bölməni yerinə yetirin: əvvəl qisməti, sonra qalığı yazın.', '4 · 5 = 20, 23 − 20 = 3.', '5 (q 3)',
   tokens=[23, ':', 4, '=', N, '(q', N, ')'], answer=[5, 3])
it('B', 'Bölmə', 'Bölməni yerinə yetirin.', 'Əvvəl yüzlükləri, sonra onluqları və təklikləri bölün.', '213',
   tokens=[639, ':', 3, '=', N], answer=[213])
# C. Kəsrlər
it('C', 'Kəsr', 'Rənglənmiş hissəni göstərən kəsri seçin.', 'Neçə bərabər hissə var? Neçəsi rənglənib?', '1/4',
   img=frac_circle(4, 1, 160), options=[frac_txt(1, 4, 60), frac_txt(1, 3, 60), frac_txt(4, 1, 60)], answer=0)
it('C', 'Ədədin hissəsi', '15-in üçdə biri neçədir?', '15-i 3 bərabər hissəyə bölün: 15 : 3.', '5',
   tokens=[15, ':', 3, '=', N], answer=[5])
it('C', 'Kəsrlərin müqayisəsi', 'Ən böyük kəsri seçin.', 'Məxrəclər bərabərdir: surəti böyük olan kəsr böyükdür.', '5/6',
   options=[frac_txt(2, 6, 60), frac_txt(5, 6, 60), frac_txt(3, 6, 60)], answer=1)
it('C', 'Ədədin hissəsi', 'Sinifdə 20 şagird var. Onların yarısı qızdır. Neçə qız var?', 'Yarısı – 2 bərabər hissədən biri: 20 : 2.', '10',
   img=hstack([em('👧', 80), em('👦', 80)], 20), tokens=[20, ':', 2, '=', N], answer=[10])
# D. Ədədlər, pullar və ölçmə
it('D', 'Dördrəqəmli ədədlər', 'Cəmə uyğun ədədi yazın.', 'Minlikləri, yüzlükləri, onluqları və təklikləri yan-yana yazın.', '3405',
   tokens=[3000, '+', 400, '+', 5, '=', N], answer=[3405])
it('D', 'Pullar', '3 manat 25 qəpik neçə qəpikdir?', '1 manat 100 qəpikdir: 300 + 25.', '325',
   tokens=['3 man 25 qəp', '=', N, 'qəp'], answer=[325])
it('D', 'Perimetr', 'Düzbucaqlının perimetrini tapın.', 'Bütün tərəfləri toplayın: 7 + 3 + 7 + 3.', '20',
   img=rect_sides(7, 3, '7 sm', '3 sm', 28), tokens=[N, 'sm'], answer=[20])
it('D', 'Kütlə', '2 kq 300 q neçə qramdır?', '1 kq 1000 qramdır: 2000 + 300.', '2300',
   tokens=['2 kq 300 q', '=', N, 'q'], answer=[2300])
# E. Məlumatlar və hadisələr
it('E', 'Rəqəmsal saat', 'Rəqəmsal saat neçəni göstərir? Saatı və dəqiqəni yazın.', 'İki nöqtədən əvvəl saat, sonra dəqiqə yazılır.', '14:20',
   img=digital('14:20', 64), tokens=[N, ':', N], answer=[14, 20])
it('E', 'Xətti diaqram', 'Diaqrama baxın. Çərşənbə günü neçə dərəcə olub?', 'Ç hərfinin üstündəki nöqtəyə baxın, sola – şkalaya gedin.', '15',
   img=line_chart(['B.e', 'Ç.a', 'Ç', 'C.a', 'C'], [10, 5, 15, 20, 10], 20, 5, 440, 260, RED), tokens=[N], answer=[15])
it('E', 'Hadisələr', 'Zər atılır. «7 düşəcək» – bu necədir?', 'Zərin üzlərində 1-dən 6-ya qədər nöqtə var.', 'Mümkün deyil',
   img=die(3, 110), options=[chip('Mümkün deyil', 40), chip('Çətin ki, olsun', 40), chip('Mütləq olacaq', 40)], answer=0)
it('E', 'Cədvəl', 'Cədvələ baxın. Cəmi neçə uşaq sorğuda iştirak edib?', 'Bütün ədədləri toplayın: 8 + 6 + 4.', '18',
   img=tab([['İdman', 'Uşaq'], ['Futbol', 8], ['Şahmat', 6], ['Üzgüçülük', 4]], 30), tokens=[N], answer=[18])

AREAS = [
    {'code': 'A', 'name': 'Həndəsi fiqurlar', 'topics': [117, 118, 119, 120, 121], 'home': 'Evdə paralel və kəsişən xətləri, simmetrik əşyaları, kub və silindr formalı qutuları birlikdə axtarın.'},
    {'code': 'B', 'name': 'Vurma və bölmə', 'topics': [122, 123, 124, 125, 126, 127, 128], 'home': '«Hər qutuda 24 konfet var, 3 qutuda neçə?» kimi məsələlər qurun. Konfetləri paylayıb qalığı birlikdə tapın.'},
    {'code': 'C', 'name': 'Kəsrlər', 'topics': [129, 130, 131], 'home': 'Pizzanı, almanı bərabər hissələrə bölün və hissələri kəsrlə adlandırın: yarısı, üçdə biri, dörddə biri.'},
    {'code': 'D', 'name': 'Ədədlər, pullar və ölçmə', 'topics': [132, 133, 134, 135, 136, 137, 138], 'home': 'Alış-verişdə manat və qəpikləri birlikdə sayın, mətbəxdə qram və millilitri oxuyun, otağın perimetrini ölçün.'},
    {'code': 'E', 'name': 'Məlumatlar və hadisələr', 'topics': [139, 140, 141, 142], 'home': 'Ailədə kiçik sorğu keçirin, cavabları cədvəldə yazın. Hava temperaturunu bir həftə qeyd edib diaqram çəkin.'},
]
save_test(sys.argv[1], AREAS, '2-ci hissəsini')
