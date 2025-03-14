# YKS Tercih Asistanı

## Proje Açıklaması
YKS Tercih Asistanı, üniversite adaylarının tercih döneminde kullanabileceği bir araçtır. Python ile geliştirilmiş bu uygulama, 2023 yerleştirme sonuçlarından alınan verileri kullanarak tercih yapmayı kolaylaştırır. Kullanıcılar, istedikleri üniversite, fakülte, bölüm veya puan türüne göre arama yapabilirler.

Bu proje iki ana bileşenden oluşur:
1. **Terminal Uygulaması (`terminal_tercih_asistani.py`)**: Terminal üzerinden tercih sorgulamalarını yapmaya olanak tanır.
2. **Görsel Arayüzlü Uygulama (`ui_tercih_asistani.py`)**: Tkinter kullanılarak oluşturulmuş bir GUI içeren versiyondur.

## Gereksinimler
Projenin çalışması için aşağıdaki kütüphanelerin yüklü olması gerekmektedir:

```bash
pip install pandas openpyxl tkinter
```

> **Not:** `tkinter` Python'un standart kütüphanesinde bulunur, ancak bazı sistemlerde yüklenmiş olmayabilir.

## Kullanım
### 1. Terminal Versiyonu (`terminal_tercih_asistani.py`)
Terminal üzerinden çalıştırılabilir ve çeşitli kriterlere göre arama yapılabilir.

#### Çalıştırma:
```bash
python terminal_tercih_asistani.py
```

Kullanıcı, aşağıdaki seçeneklerden birini girerek arama yapabilir:
- Üniversite türü (Vakıf / Devlet)
- Üniversite adı
- Fakülte adı
- Program adı
- Puan türü (SÖZ, EA, SAY)
- Özel arama (Birden fazla kriter girilebilir)

Sonuçlar `txt` dosyası olarak kaydedilir.

### 2. Görsel Arayüzlü Versiyon (`ui_tercih_asistani.py`)
Kullanıcı dostu bir arayüze sahiptir ve daha kolay kullanım imkanı sunar.

#### Çalıştırma:
```bash
python ui_tercih_asistani.py
```

**Özellikler:**
- Kullanıcı Excel dosyasını seçerek verileri yükleyebilir.
- Farklı kriterlere göre arama yapabilir.
- Sonuçları `.txt` ve `.json` formatında kaydedebilir.

## Dosya Açıklamaları
- **`terminal_tercih_asistani.py`**: Terminal üzerinden çalışan tercih asistanı.
- **`ui_tercih_asistani.py`**: Tkinter tabanlı görsel arayüzü içeren tercih asistanı.
- **`2024_uni_puanlari.xlsx`**: 2024 yılı üniversite yerleştirme sonuçlarını içeren Excel dosyası.
- **`arama_sonuclari.txt` ve `arama_sonuclari.json`**: Yapılan sorguların kayıt edildiği dosyalar.

## Katkıda Bulunma
Projeye katkıda bulunmak isterseniz, pull request gönderebilir veya hataları bildirebilirsiniz.

## Lisans
Bu proje MIT lisansı ile lisanslanmıştır.

