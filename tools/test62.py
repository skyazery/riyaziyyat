"""Yoxlama testi (6-2): 20 tapşırıq. Run: python3 tools/test62.py OUTDIR → OUTDIR/test_items.json"""
import sys
from testcommon import *
from kit56 import venn, trans, tri_h, circ, cyl

# A. Çoxluqlar
it('A', 'Çoxluğun elementləri', 'A = {1, 3, 5, 7, 9} çoxluğunun neçə elementi var?', 'Elementləri sayın.', '5', tokens=[N], answer=[5])
it('A', 'Kəsişmə', 'A = {2, 4, 6, 8}, B = {4, 8, 12}. A ∩ B kəsişməsinin neçə elementi var?', 'Ortaq elementlər: 4 və 8.', '2', tokens=[N], answer=[2])
it('A', 'Birləşmə', 'A = {2, 4, 6, 8}, B = {4, 8, 12}. A ∪ B birləşməsinin neçə elementi var?', '4 + 3 − 2.', '5', tokens=[N], answer=[5])
it('A', 'Eyler-Venn diaqramı', 'Diaqrama görə cəmi neçə şagird var?', 'Bütün hissələri toplayın.', '24',
   img=venn(10, 4, 7, 'Rəsm', 'Musiqi', 'heç biri: 3'), tokens=[N], answer=[24])
# B. İfadələr və tənliklər
it('B', 'Mötərizənin açılması', '−3(x − 4) = −3x + ? Boş xanaya uyğun ədədi yazın.', 'Mənfi ədədə vurduqda işarə dəyişir: −3 · (−4) = 12.', '12', tokens=['−3(x − 4) = −3x +', N], answer=[12])
it('B', 'Sadələşdirmə', 'İfadəni sadələşdirin: 6a − (2a − 5) = ?a + 5.', '6a − 2a + 5.', '4', tokens=['6a − (2a − 5) =', N, 'a + 5'], answer=[4])
it('B', 'Tənlik', 'Tənliyi həll edin: 5x − 3 = 2x + 12.', '5x − 2x = 12 + 3, 3x = 15.', '5', tokens=['5x − 3 = 2x + 12', 'x =', N], answer=[5])
it('B', 'Bərabərsizlik', '3x < 15 bərabərsizliyinin ən böyük natural həllini yazın.', 'x < 5.', '4', tokens=['3x < 15', '→', N], answer=[4])
# C. Üçbucaqlar
it('C', 'Median', 'AM medianıdır, BC = 18 sm. BM neçə santimetrdir?', 'Median tərəfi yarıya bölür.', '9', tokens=['BM =', N, 'sm'], answer=[9])
it('C', 'Paralel xətlər', 'a ∥ b. Sual işarəsi olan bucaq neçə dərəcədir?', 'Uyğun bucaqlar bərabərdir.', '70°',
   img=trans(70, {1: '70°', 5: '?'}), tokens=[N, '°'], answer=[70])
it('C', 'Bucaqların cəmi', 'Üçbucağın iki bucağı 45° və 75°-dir. Üçüncü bucağı tapın.', '180 − 45 − 75.', '60°', tokens=[N, '°'], answer=[60])
it('C', 'Üçbucaq bərabərsizliyi', 'Hansı parçalardan üçbucaq qurmaq olar?', 'Hər tərəf digər ikisinin cəmindən kiçik olmalıdır.', '4, 6, 8',
   options=[chip('2, 3, 6', 48), chip('4, 6, 8', 48), chip('1, 5, 7', 48)], answer=1)
# D. Sahə və həcm
it('D', 'Üçbucağın sahəsi', 'Oturacağı 12 sm, hündürlüyü 5 sm olan üçbucağın sahəsini tapın.', '12 · 5 : 2.', '30',
   img=tri_h('12 sm', '5 sm'), tokens=['S =', N, 'sm²'], answer=[30])
it('D', 'Rombun sahəsi', 'Rombun diaqonalları 10 sm və 8 sm-dir. Sahəsini tapın.', '10 · 8 : 2.', '40', tokens=['S =', N, 'sm²'], answer=[40])
it('D', 'Çevrənin uzunluğu', 'Radiusu 10 sm olan çevrənin uzunluğunu tapın (π ≈ 3,14).', '2 · 3,14 · 10.', '62,8',
   img=circ('r = 10 sm'), tokens=['C =', N, ',', N, 'sm'], answer=[62, 8])
it('D', 'Silindrin həcmi', 'Radiusu 1 sm, hündürlüyü 10 sm olan silindrin həcmini tapın (π ≈ 3,14).', '3,14 · 1 · 10.', '31,4',
   img=cyl('1 sm', '10 sm'), tokens=['V =', N, ',', N, 'sm³'], answer=[31, 4])
# E. Statistika və ehtimal
it('E', 'Moda', '4, 7, 7, 8, 7, 9 ədədlərinin modasını tapın.', 'Ən çox təkrarlanan ədəd.', '7', tokens=['Moda =', N], answer=[7])
it('E', 'Median', '3, 9, 5, 11, 7 ədədlərinin medianını tapın.', 'Sıraya düzün: 3, 5, 7, 9, 11.', '7', tokens=['Median =', N], answer=[7])
it('E', 'Ehtimal', 'Zəri atanda 5 düşməsinin ehtimalını tapın.', '6 nəticədən 1-i əlverişlidir.', '1/6', tokens=['P =', N, '/', N], answer=[1, 6])
it('E', 'Təsadüfi hadisə', 'Zəri atanda 0 düşməsi hansı hadisədir?', 'Zərdə 0 yoxdur.', 'mümkün olmayan',
   options=[chip('yəqin', 44), chip('təsadüfi', 44), chip('mümkün olmayan', 44)], answer=2)

AREAS = [
    {'code': 'A', 'name': 'Çoxluqlar', 'topics': list(range(267, 270)), 'home': 'Ailədə kimin çay, kimin kofe sevdiyini soruşub Eyler-Venn diaqramı çəkin.'},
    {'code': 'B', 'name': 'İfadələr və tənliklər', 'topics': list(range(270, 276)), 'home': 'Gündəlik məsələni tənliklə yazın: «Atanın yaşı oğlunun yaşından 3 dəfə çoxdur, cəmi 48-dir».'},
    {'code': 'C', 'name': 'Üçbucaqlar', 'topics': list(range(276, 281)), 'home': 'Kağızdan üçbucaq kəsib bucaqlarını qoparın və yan-yana qoyun: düz xətt (180°) alınır.'},
    {'code': 'D', 'name': 'Sahə və həcm', 'topics': list(range(281, 286)), 'home': 'Evdəki silindr şəkilli qabın (stəkan, qazan) radiusunu və hündürlüyünü ölçüb həcmini hesablayın.'},
    {'code': 'E', 'name': 'Statistika və ehtimal', 'topics': list(range(286, 290)), 'home': 'Zər və ya sikkə ilə 20 dəfə atış edin, nəticələri yazın və tezlik cədvəli qurun.'},
]
save_test(sys.argv[1], AREAS, '2-ci hissəsini', '6-cı')
