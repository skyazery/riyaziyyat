"""Yoxlama testi (4-1): 20 tapşırıq. Run: python3 tools/test41.py OUTDIR → OUTDIR/test_items.json"""
import sys
from testcommon import *

# A. Ədədlər (1 000 000-a qədər)
it('A', 'Çoxrəqəmli ədədlər', 'Cəmə uyğun ədədi yazın.', 'Hər mərtəbənin rəqəmini yan-yana yazın: 4 yüzminlik, 3 onminlik və s.', '435 207',
   tokens=['400 000', '+', '30 000', '+', '5 000', '+', 200, '+', 7, '=', N], answer=[435207])
it('A', 'Mərtəbələr', '712 635 ədədində 1 rəqəmi hansı mərtəbədədir?', 'Sağdan sayın: təklik, onluq, yüzlük, minlik, onminlik.', 'Onminliklər',
   options=[chip('Minliklər', 50), chip('Onminliklər', 50), chip('Yüzminliklər', 50)], answer=1)
it('A', 'Müqayisə', 'Ən böyük ədədi seçin.', 'Əvvəl rəqəmlərin sayını, sonra ən yüksək mərtəbəni müqayisə edin.', '181 321',
   options=[chip('22 105', 56), chip('181 321', 56), chip('99 999', 56)], answer=1)
it('A', 'Yuvarlaqlaşdırma', 'Ədədi minliklərə qədər yuvarlaqlaşdırın.', 'Yüzlüklər mərtəbəsindəki rəqəmə baxın: 7 ≥ 5, minlik 1 artır.', '19 000',
   tokens=['18 799', '≈', N], answer=[19000])
# B. Toplama və çıxma
it('B', 'Toplama', 'Cəmi tapın.', 'Alt-alta yazın və təkliklərdən başlayın.', '63 887',
   tokens=['54 184', '+', '9 703', '=', N], answer=[63887])
it('B', 'Çıxma', 'Fərqi tapın.', 'Sıfırlar olan yerdə soldakı mərtəbədən 1 vahid ayırın.', '1 248',
   tokens=['8 000', '−', '6 752', '=', N], answer=[1248])
it('B', 'Əvəzləmə üsulu', 'Cəmi asan yolla tapın.', '1 999-u 2 000-ə tamamlayın: 2 000 + 111.', '2 111',
   tokens=['1 999', '+', 112, '=', N], answer=[2111])
it('B', 'Məsələ', 'Everest 8 848 m, Marian çökəkliyi 11 034 m-dir. Ən uca zirvə ən dərin nöqtədən neçə metr hündürdür?', 'İki ədədi toplayın.', '19 882',
   img=em('🏔️', 100), tokens=['8 848', '+', '11 034', '=', N], answer=[19882])
# C. Vurma və bölmə
it('C', 'Birrəqəmli ədədə vurma', 'Hasili tapın.', 'Təkliklərdən başlayın, onluqları növbəti mərtəbəyə əlavə edin.', '25 266',
   tokens=['4 211', '·', 6, '=', N], answer=[25266])
it('C', 'Birrəqəmli ədədə bölmə', 'Qisməti tapın.', 'Minlikləri, yüzlükləri, onluqları və təklikləri ardıcıl bölün.', '1 346',
   tokens=['5 384', ':', 4, '=', N], answer=[1346])
it('C', 'İkirəqəmli ədədə vurma', 'Hasili tapın.', 'Natamam hasilləri toplayın: 125 · 3 + 125 · 20.', '2 875',
   tokens=[125, '·', 23, '=', N], answer=[2875])
it('C', 'İkirəqəmli ədədə bölmə', 'Qisməti tapın.', 'Qisməti təxmin edin və vurma ilə yoxlayın: 24 · 102.', '102',
   tokens=['2 448', ':', 24, '=', N], answer=[102])
# D. İfadələr və tənliklər
it('D', 'Əməllər ardıcıllığı', 'İfadənin qiymətini tapın.', 'Əvvəl mötərizə, sonra vurma və bölmə, sonra toplama.', '55',
   tokens=['(17 − 35 : 5)', '·', 4, '+', 15, '=', N], answer=[55])
it('D', 'Dəyişəni olan ifadə', 'a = 135 və b = 3 olanda ifadənin qiymətini tapın.', 'Hərflərin yerinə ədədləri yazın: 108 : 3 + 135.', '171',
   tokens=[108, ':', 'b', '+', 'a', '=', N], answer=[171])
it('D', 'Tənlik', 'Tənliyi həll edin.', 'Məchul bölünəni tapmaq üçün qisməti bölənə vurun.', '96',
   tokens=['d', ':', 8, '=', 12, ';', 'd', '=', N], answer=[96])
it('D', 'Qanunauyğunluq', 'Qaydanı tapın və növbəti ədədi yazın.', 'Hər ədəd 4-ə vurulur.', '192',
   tokens=['3,', '12,', '48,', N], answer=[192])
# E. Həndəsi fiqurlar
it('E', 'Çevrə', 'Çevrənin radiusu 7 sm-dir. Diametri neçə santimetrdir?', 'Diametr radiusdan 2 dəfə böyükdür.', '14',
   tokens=['d', '=', N, 'sm'], answer=[14])
it('E', 'Bucaq', 'Bu hansı bucaqdır?', '90°-dən böyük, 180°-dən kiçik bucaq kor bucaqdır.', 'Kor',
   img=angle_img(130, 220), options=[chip('İti', 56), chip('Düz', 56), chip('Kor', 56)], answer=2)
it('E', 'Koordinat şəbəkəsi', 'Kvadratın təpələri (1; 1), (4; 1), (4; 4) və (1; 4)-dür. Tərəfi neçə vahiddir?', '4 − 1 hesablayın.', '3',
   tokens=['a', '=', N], answer=[3])
it('E', 'Fəza fiqurları', 'Kubun neçə tili var?', 'Yuxarıda 4, aşağıda 4, yanlarda 4 til.', '12',
   img=cube_marked(160, False), tokens=[N], answer=[12])

AREAS = [
    {'code': 'A', 'name': 'Ədədlər (1 000 000-a qədər)', 'topics': [143, 144, 145], 'home': 'Qəzet və saytlardakı böyük ədədləri (əhali, məsafə) birlikdə oxuyun və minliklərə qədər yuvarlaqlaşdırın.'},
    {'code': 'B', 'name': 'Toplama və çıxma', 'topics': [146, 147, 148], 'home': 'Alış-veriş qəbzindəki məbləğləri alt-alta toplayın və qalığı hesablayın. Cavabı təqribi hesabla yoxlayın.'},
    {'code': 'C', 'name': 'Vurma və bölmə', 'topics': [149, 150, 151, 152, 153, 154, 160, 161, 162, 163], 'home': '«Bir qutuda 24 karandaş var, 15 qutuda neçədir?» kimi suallar verin. Bölməni vurma ilə yoxlamağı öyrədin.'},
    {'code': 'D', 'name': 'İfadələr və tənliklər', 'topics': [155, 156, 157, 158, 159], 'home': '«Hansı ədədi 8-ə böləndə 12 alınır?» kimi tapmacalar qurun. Əməllər ardıcıllığını misallarla xatırladın.'},
    {'code': 'E', 'name': 'Həndəsi fiqurlar', 'topics': [164, 165, 166, 167, 168, 169, 170], 'home': 'Evdə bucaqları (qapı, kitab) tapın: iti, düz, yoxsa kor? Qutunu açaraq onun açılışına baxın.'},
]
save_test(sys.argv[1], AREAS, '1-ci hissəsini', '4-cü')
