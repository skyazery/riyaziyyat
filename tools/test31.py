"""Yoxlama testi (3-1): 20 tapşırıq. Run: python3 tools/test31.py OUTDIR → OUTDIR/test_items.json"""
import sys
from testcommon import *

# A. Ədədlər (1000-ə qədər)
it('A', 'Üçrəqəmli ədədlər', 'Bloklara uyğun ədədi yazın.', 'Kvadrat – yüzlük, çubuq – onluq, kub – təklik.', '243',
   img=hto(2, 4, 3, 80), tokens=[N], answer=[243])
it('A', 'Ədədin yazılış formaları', 'Cəmə uyğun ədədi yazın.', 'Yüzlükləri, onluqları və təklikləri yan-yana yazın.', '608',
   tokens=[600, '+', 8, '=', N], answer=[608])
it('A', 'Müqayisə', 'Ən böyük ədədi seçin.', 'Əvvəl yüzlükləri müqayisə edin, bərabərdirsə onluqları.', '581',
   options=[chip('518', 60), chip('581', 60), chip('158', 60)], answer=1)
it('A', 'Yuvarlaqlaşdırma', 'Ədədi onluqlara qədər yuvarlaqlaşdırın.', 'Təkliklər 5 və ya çoxdursa, yuxarı yuvarlaqlaşdırın.', '350',
   tokens=[347, '≈', N], answer=[350])
# B. Toplama
it('B', 'Toplama', 'Cəmi tapın.', 'Yüzlükləri, onluqları və təklikləri ayrı-ayrı toplayın.', '587',
   tokens=[324, '+', 263, '=', N], answer=[587])
it('B', 'Yeni onluğun yaranması', 'Cəmi tapın.', '8 + 5 = 13: 1 onluğu onluqlara əlavə edin.', '473',
   tokens=[248, '+', 225, '=', N], answer=[473])
it('B', 'Yeni yüzlüyün yaranması', 'Cəmi tapın.', '7 + 6 = 13 onluq: 1 yüzlüyü yüzlüklərə əlavə edin.', '624',
   tokens=[372, '+', 252, '=', N], answer=[624])
it('B', 'Üç ədədin toplanması', 'Cəmi tapın.', 'Əvvəl 150 + 250 = 400 toplayın.', '520',
   tokens=[150, '+', 120, '+', 250, '=', N], answer=[520])
# C. Çıxma
it('C', 'Çıxma', 'Fərqi tapın.', 'Yüzlükləri, onluqları və təklikləri ayrı-ayrı çıxın.', '342',
   tokens=[586, '−', 244, '=', N], answer=[342])
it('C', 'Onluğun ayrılması', 'Fərqi tapın.', 'Təkliklər çatmır: 1 onluq ayırın. 12 − 7 = 5.', '235',
   tokens=[462, '−', 227, '=', N], answer=[235])
it('C', 'Yüzlüyün ayrılması', 'Fərqi tapın.', 'Onluqlar çatmır: 1 yüzlük ayırın. 13 − 8 = 5 onluq.', '355',
   tokens=[738, '−', 383, '=', N], answer=[355])
it('C', 'Məsələ', 'Kitabxanada 500 kitab var idi. 165 kitabı apardılar. Neçə kitab qaldı?', 'Çıxma əməli: 500 − 165.', '335',
   img=em('📚', 100), tokens=[500, '−', 165, '=', N], answer=[335])
# D. Vurma və bölmə
it('D', '6-ya və 7-yə vurma', 'Hasili tapın.', '7 · 6 = 6 · 7. Altı-altı sayın.', '42',
   tokens=[7, '·', 6, '=', N], answer=[42])
it('D', '8 və 9-a vurma', 'Hasili tapın.', '9 · 8 = 80 − 8.', '72',
   tokens=[9, '·', 8, '=', N], answer=[72])
it('D', 'Bölmə', 'Bölməni yerinə yetirin.', '7-ni neçəyə vuranda 56 alınır?', '8',
   tokens=[56, ':', 7, '=', N], answer=[8])
it('D', 'Məsələ', '36 qələmi 4 qutuya bərabər yığdılar. Hər qutuda neçə qələm var?', 'Bölmə əməli: 36 : 4.', '9',
   img=em('🖊️', 100), tokens=[36, ':', 4, '=', N], answer=[9])
# E. İfadələr və tənliklər
it('E', 'Məchulun tapılması', 'Məchul toplananı tapın.', 'Cəmdən məlum toplananı çıxın: 500 − 320.', '180',
   tokens=[320, '+', N, '=', 500], answer=[180])
it('E', 'Əməllər ardıcıllığı', 'İfadənin qiymətini hesablayın.', 'Əvvəlcə vurmanı yerinə yetirin: 4 · 5 = 20.', '50',
   tokens=[30, '+', 4, '·', 5, '=', N], answer=[50])
it('E', 'Dəyişəni olan ifadə', 'a = 6 olanda ifadənin qiymətini tapın.', 'a yerinə 6 yazın: 6 · 9.', '54',
   tokens=['a · 9', '=', N], answer=[54])
it('E', 'Tənlik', 'Tənliyi həll edin.', 'Məchul vuruğu tapmaq üçün hasili məlum vuruğa bölün: 48 : 6.', '8',
   tokens=['x · 6', '=', 48, ';', 'x', '=', N], answer=[8])

AREAS = [
    {'code': 'A', 'name': 'Ədədlər (1000-ə qədər)', 'topics': [92, 93, 94, 95], 'home': 'Qiymət etiketlərindəki üçrəqəmli ədədləri birlikdə oxuyun: neçə yüzlük, neçə onluq, neçə təklik var?'},
    {'code': 'B', 'name': 'Üçrəqəmli ədədlərin toplanması', 'topics': [96, 97, 98, 99, 100, 101], 'home': 'Alış-verişdə iki qiyməti alt-alta yazıb toplayın. Cavabı təqribi hesabla yoxlayın.'},
    {'code': 'C', 'name': 'Üçrəqəmli ədədlərin çıxılması', 'topics': [102, 103, 104, 105, 106, 107], 'home': '«Kitabda 320 səhifə var, 145-ni oxuduq. Nə qədər qaldı?» kimi suallar verin və cavabı toplama ilə yoxlayın.'},
    {'code': 'D', 'name': 'Vurma və bölmə', 'topics': [108, 109, 110, 111, 112], 'home': 'Vurma cədvəlini oyunla təkrar edin: 6, 7, 8 və 9-a vurma. Əşyaları bərabər paylayın – bu bölmədir.'},
    {'code': 'E', 'name': 'İfadələr və tənliklər', 'topics': [113, 114, 115, 116], 'home': '«Hansı ədədi 6-ya vuranda 42 olar?» kimi tapmacalar qurun. Əvvəl vurma, sonra toplama qaydasını xatırladın.'},
]
save_test(sys.argv[1], AREAS, '1-ci hissəsini')
