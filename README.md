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

## 2-ci sinif, 2-ci hissə (`2-2/`)

- `2-2/index.html` – 22 mövzu (70–91), 220 şəkilli tapşırıq, səsli izah, səviyyə testi
- `2-2/test.html` – 20 tapşırıqlı yoxlama testi
- `2-2/muellim.html` – cavablar və qiymətləndirmə bələdçisi
- Mənbə: `tools/content22.py`, `tools/test22.py`, `tools/build_test22.py`, `tools/build_muellim22.py`
- macOS-da şəkillər üçün DejaVu şrifti və Noto emoji PNG-ləri `~/riyaziyyat-assets/` qovluğundadır (`draw.py` özü tapır, çatmayan emojini bir dəfə endirir)

## 3-cü sinif, 1-ci hissə (`3-1/`) və 2-ci hissə (`3-2/`)

- `3-1/index.html` – 25 mövzu (92–116), 250 şəkilli tapşırıq; `3-2/index.html` – 26 mövzu (117–142), 260 şəkilli tapşırıq
- `3-1/test.html`, `3-2/test.html` – 20 tapşırıqlı yoxlama testləri; `muellim.html` – cavablar və qiymətləndirmə
- Mənbə: `tools/bookgen.py` (ümumi çəkmə köməkçiləri), `tools/content31.py`, `tools/content32.py`, `tools/testcommon.py`, `tools/test31.py`, `tools/test32.py`, `tools/build_test3.py 3-1|3-2`, `tools/build_muellim3.py 3-1|3-2`

## Mətnlər və səslər

- Bütün tapşırıq mətnləri hörmətli formadadır (yazın, sayın, toxunun …). Yeni mətn əlavə edəndə `python3 tools/formal.py --apply` çevirir.
- Səslər: `python3 tools/tts_all.py` – çatışmayan səsləri yaradır (az-AZ-BanuNeural, +17Hz), `data/audio.json`-u yeniləyir, köhnə faylları silir. `--praise` tərif səslərini də yenidən yaradır. Lazım olan paketlər: `pip install edge-tts imageio-ffmpeg`.
