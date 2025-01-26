# YKS Tercih Asistanı

YKS Tercih Asistanı, Türkiye'deki üniversite tercih sürecine yardımcı olmak için geliştirilmiş bir araçtır. Bu program, kullanıcıların 2023 YKS yerleştirme sonuçlarına dayalı olarak üniversite, fakülte ve program araması yapmasını sağlar. Ayrıca, özel kriterlerle detaylı aramalar yaparak doğru tercihleri belirlemede kolaylık sunar.

## Özellikler

### 1. **Excel Veri Yükleme**
- Program, 2023 YKS yerleştirme sonuçlarını içeren bir Excel dosyasını otomatik olarak yükler.
- Veri, "pandas" kütüphanesi ile işlenir.

### 2. **Arama Seçenekleri**
- **Üniversite Türü Arama:** Devlet veya vakıf üniversitelerini filtreleme.
- **Üniversite Adı Arama:** Belirli bir üniversiteyi arama.
- **Fakülte Adı Arama:** Belirli bir fakülteye veya yüksekokula yönelik sonuçları görüntüleme.
- **Program Adı Arama:** Bölüm bazında tercih yapma.
- **Puan Türü Arama:** Söz, EA veya sayısal puan türüne göre arama yapma.

### 3. **Özel Arama**
- Kullanıcı, birden fazla kriter girerek detaylı filtreleme yapabilir (örneğin: Üniversite Adı, Fakülte Adı, Program Adı, Puan Türü).

### 4. **Sonuçları Kaydetme**
- Arama sonuçları bir TXT dosyasına kaydedilerek daha sonra incelenebilir.
- Dosyada her bir satır program detaylarını içerecek şekilde düzenlenmiştir.

### 5. **Dinamik Menü**
- Kullanıcı dostu bir arayüz ile farklı arama seçenekleri sunar.
- Çıkış seçeneğiyle programdan kolayca çıkılabilir.

## Kullanım Talimatları

1. Program, Python ortamında çalıştırılabilir.
2. Projenin ana dizininde **"Data//2024_uni_puanlari.xlsx"** adında bir Excel dosyasının bulunduğundan emin olun.
3. Program çalıştırıldığında, aşağıdaki seçenekleri içeren bir menü görüntülenir:
    - Üniversite Türü (Vakıf/Devlet)
    - Üniversite Adı
    - Fakülte/Yüksekokul Adı
    - Program Adı
    - Puan Türü
    - Özel Arama
4. Menüdeki seçeneklerden birini seçerek tercihlerinize uygun arama yapabilirsiniz.
5. Arama sonuçları, ilgili bilgilerle birlikte ekrana yazdırılır ve bir dosyaya kaydedilir.

## Gereksinimler

- Python 3.7 veya daha üstü
- Pandas kütüphanesi (`pip install pandas`)
- openpyxl kütüphanesi (`pip install openpyxl`)

## Örnek Kullanım

### 1. Üniversite Türü Seçimi
- Menüden "1" seçildiğinde, kullanıcı "Vakıf" veya "Devlet" üniversitelerini filtreleyebilir.

### 2. Özel Arama
- Kullanıcı, birden fazla kriter belirterek detaylı arama yapabilir. Örneğin:
  - Üniversite Adı: "Boğaziçi Üniversitesi"
  - Fakülte Adı: "Mühendislik Fakültesi"
  - Program Adı: "Bilgisayar Mühendisliği"
  - Puan Türü: "Sayısal"

### 3. Sonuçların Kaydedilmesi
- "ozel_arama_sonuclari.txt" dosyasında arama sonuçları depolanır.

## Geliştirici Notları

Bu program, Python kullanıcılarına kolaylık sağlamak için tasarlanmıştır. Daha basit bir arayüz veya grafiksel bir kullanıcı arayüzü (GUI) eklemek isterseniz, `tkinter` veya `PyQt` gibi kütüphaneleri kullanabilirsiniz.

## Lisans

Bu proje açık kaynak kodludur ve dilediğiniz şekilde geliştirilebilir. Herhangi bir geri bildirim veya katkıda bulunmak için lütfen bizimle iletişime geçin.

