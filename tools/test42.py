"""Yoxlama testi (4-2): 20 tapşırıq. Run: python3 tools/test42.py OUTDIR → OUTDIR/test_items.json"""
import sys
from testcommon import *

# A. Adi kəsrlər
it('A', 'Bərabər kəsrlər', 'Boş xanaya uyğun ədədi yazın: 3/4 = ?/12', 'Məxrəci 3-ə vurduq, surəti də 3-ə vurun.', '9',
   tokens=['3/4', '=', N, '/ 12'], answer=[9])
it('A', 'Kəsrlərin müqayisəsi', 'Ən böyük kəsri seçin.', 'Məxrəclər eynidirsə, surəti böyük olan kəsr böyükdür.', '7/10',
   options=[chip('3/10', 56), chip('7/10', 56), chip('5/10', 56)], answer=1)
it('A', 'Kəsrlərin toplanması', 'Hesablayın: 2/7 + 3/7 = ?/7', 'Surətləri toplayın, məxrəc dəyişmir.', '5',
   tokens=['2/7', '+', '3/7', '=', N, '/ 7'], answer=[5])
it('A', 'Qarışıq ədədlər', '1 3/4 qarışıq ədədini kəsr şəklində yazın: ?/4', '1 tam = 4/4. 4 + 3 = 7.', '7',
   tokens=['1 3/4', '=', N, '/ 4'], answer=[7])
# B. Onluq kəsrlər
it('B', 'Onluq kəsrlər', '2 3/10 ədədini onluq kəsr şəklində yazın.', 'Tam hissə 2, ondabirlər 3.', '2,3',
   tokens=['2 3/10', '=', N, ',', N], answer=[2, 3])
it('B', 'Onluq kəsrlərin müqayisəsi', 'Ən böyük ədədi seçin.', 'Tam hissələr bərabərdir, ondabirləri müqayisə edin.', '5,7',
   options=[chip('5,07', 56), chip('5,7', 56), chip('5,17', 56)], answer=1)
it('B', 'Onluq kəsrlərin toplanması', 'Cəmi tapın.', 'Vergülü vergülün altında yazın: 3,7 + 1,5.', '5,2',
   tokens=['3,7', '+', '1,5', '=', N, ',', N], answer=[5, 2])
it('B', 'Onluq kəsrlərin çıxılması', 'Fərqi tapın.', 'Ondabirlər çatmır: 1 tam ayırın.', '3,4',
   tokens=['5,2', '−', '1,8', '=', N, ',', N], answer=[3, 4])
# C. Pullar
it('C', 'Manat və qəpik', '2,50 manat neçə qəpikdir?', '1 manat = 100 qəpik: 200 + 50.', '250',
   tokens=['2,50 man', '=', N, 'qəp'], answer=[250])
it('C', 'Pullarla hesablama', 'Dəftər 1,20 manat, qələm 0,80 manatdır. Birlikdə neçə manatdır?', '20 qəpik + 80 qəpik = 1 manat.', '2',
   tokens=['1,20', '+', '0,80', '=', N, 'man'], answer=[2])
it('C', 'Qalıq', 'Lalə 10 manat verib 6,50 manatlıq kitab aldı. Ona neçə manat neçə qəpik qaytarıldı?', '10 manat − 6 manat 50 qəpik.', '3 manat 50 qəpik',
   tokens=[N, 'man', N, 'qəp'], answer=[3, 50])
it('C', 'Xərclər', 'İnternet hər ay 30 manatdır. 4 ayda neçə manat ödənilir?', 'Dəyişməyən xərci aylarla vurun.', '120',
   tokens=[30, '·', 4, '=', N], answer=[120])
# D. Ölçmə
it('D', 'Uzunluq', '2 km 500 m neçə metrdir?', '1 km = 1 000 m.', '2 500',
   tokens=['2 km', '500 m', '=', N, 'm'], answer=[2500])
it('D', 'Perimetr', 'Düzbucaqlının uzunluğu 12 sm, eni 5 sm-dir. Perimetri neçə santimetrdir?', '(12 + 5) · 2.', '34',
   tokens=['P', '=', N, 'sm'], answer=[34])
it('D', 'Sahə', 'Düzbucaqlının uzunluğu 7 sm, eni 5 sm-dir. Sahəsi neçə kvadrat santimetrdir?', 'Uzunluğu enə vurun.', '35',
   tokens=['S', '=', N, 'kv. sm'], answer=[35])
it('D', 'Sürət', 'Avtomobil saatda 60 km gedir. 3 saatda neçə kilometr gedər?', 'Yol = sürət · zaman.', '180',
   tokens=[60, '·', 3, '=', N, 'km'], answer=[180])
# E. Məlumatların təsviri
it('E', 'Piktoqram', 'Bir bilet şəkli 8 bileti göstərir. 5 şəkil neçə biletdir?', '8 · 5.', '40',
   img=hstack([em('🎫', 60)] * 5, 6), tokens=[8, '·', 5, '=', N], answer=[40])
it('E', 'Cədvəl', 'Cədvələ görə cəmi neçə çay sifariş olunub?', 'Şəkərli və şəkərsiz çayı toplayın.', '20',
   img=tab([['', 'Çay', 'Kofe'], ['Şəkərli', 12, 7], ['Şəkərsiz', 8, 5]], 34), tokens=[N], answer=[20])
it('E', 'Dairəvi diaqram', 'Sinifdə 24 şagird var. Onların yarısı futbolu seçib. Neçə şagird futbolu seçib?', 'Yarısı – 2-yə bölmək deməkdir.', '12',
   tokens=[24, ':', 2, '=', N], answer=[12])
it('E', 'Xətti diaqram', 'Diaqramda xətt yuxarı qalxırsa, bu nə deməkdir?', 'Nöqtə əvvəlkindən yuxarıdadırsa, qiymət artıb.', 'Artım',
   img=line_chart(['Yan', 'Fev', 'Mar', 'Apr', 'May'], [5, 10, 15, 20, 25], 30, 5, 520, 280, RED), options=[chip('Artım', 56), chip('Azalma', 56), chip('Dəyişmir', 56)], answer=0)

AREAS = [
    {'code': 'A', 'name': 'Adi kəsrlər', 'topics': [171, 172, 173, 174], 'home': 'Pitsanı və ya tortu bərabər hissələrə bölün: «Hissənin neçəsini yedik?» Kəsrləri bərabər hissələrlə göstərin.'},
    {'code': 'B', 'name': 'Onluq kəsrlər', 'topics': [175, 176, 177], 'home': 'Uşağın boyunu metrlə (1,32 m) ölçün, iki ölçünü müqayisə edin və fərqini tapın.'},
    {'code': 'C', 'name': 'Pullar', 'topics': [178, 179, 180], 'home': 'Alış-verişdə qiymətləri manat və qəpiklə oxuyun, qalığı uşağa hesablatdırın.'},
    {'code': 'D', 'name': 'Ölçmə', 'topics': [181, 182, 183, 184, 185, 186, 187], 'home': 'Otağın uzunluğunu və enini ölçüb sahəsini tapın. Yol gedəndə «Saatda 60 km ilə 2 saatda neçə km?» soruşun.'},
    {'code': 'E', 'name': 'Məlumatların təsviri', 'topics': [188, 189, 190], 'home': 'Həftə ərzində havanın temperaturunu qeyd edin və birlikdə sadə xətti diaqram çəkin.'},
]
save_test(sys.argv[1], AREAS, '2-ci hissəsini', '4-cü')
