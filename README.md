# 1-ci sinif riyaziyyat – şəkilli və səsli tapşırıqlar

Gürcüstandakı azərbaycanlı uşaqlar üçün pulsuz riyaziyyat materialı (1-ci sinif, 1-ci və 2-ci hissə).

- **Şagirdlər üçün:** `index.html` – 28 mövzu, 280 şəkilli tapşırıq, səsli izah
- **Səviyyə testi:** `index.html#seviyye` – 2–12 sual, uşağın hansı mövzudan başlamalı olduğunu tapır
- **Yoxlama testi:** `test.html` – 20 tapşırıq və valideyn hesabatı
- **Müəllim üçün:** `muellim.html` – cavablar və qiymətləndirmə bələdçisi
- **Qeydiyyat (Riyaziyyat Dostu):** `qeydiyyat.html` – valideyn razılıq forması; göndərilən məlumat müəllim cədvəlinə (Qeydiyyat və Şagirdlər) avtomatik yazılır

## 2-ci hissə (`1-2/`)

- `1-2/index.html` – 21 mövzu (29–49), 210 şəkilli tapşırıq, səsli izah, səviyyə testi
- `1-2/test.html` – 20 tapşırıqlı yoxlama testi
- `1-2/muellim.html` – cavablar və qiymətləndirmə bələdçisi

## 2-ci sinif, 1-ci hissə (`2-1/`)

- `2-1/index.html` – 20 mövzu (50–69), 200 şəkilli tapşırıq, səsli izah, səviyyə testi
- `2-1/test.html` – 20 tapşırıqlı yoxlama testi
- `2-1/muellim.html` – cavablar və qiymətləndirmə bələdçisi
- Mənbə: `tools/content21.py`, `tools/draw2.py`, `tools/test21.py`, `tools/build_test21.py`, `tools/build_muellim21.py`, səslər: `tools/tts21.py` (az-AZ-BanuNeural, +17Hz)

Bütün hissələr eyni kodu işlədir: `app.js`, `app.css`, `sagird.js`. Kitabın ayarları səhifənin içindəki `BOOK` obyektindədir.
