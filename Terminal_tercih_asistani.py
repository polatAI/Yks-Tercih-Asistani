import pandas as pd

class YksTercihBotu:
    def __init__(self, excel_dosyasi):
        """Sınıfı başlatır ve Excel dosyasını yükler."""
        self.excel_dosyasi = excel_dosyasi
        try:
            self.veri = pd.read_excel(excel_dosyasi)
            print("Excel dosyası başarıyla yüklendi.")
        except Exception as e:
            print(f"Excel dosyası yüklenirken bir hata oluştu: {e}")
            self.veri = None

    def arama_yap(self, sutun_adi, kriter):
        """Belirtilen sütunda arama yapar ve sonuçları bir txt dosyasına yazar."""
        if self.veri is None:
            print("Veri mevcut değil.")
            return

        try:
            # Sütunda arama yap
            eslesen_veriler = self.veri[self.veri[sutun_adi].astype(str).str.contains(kriter, case=False, na=False)]
            if not eslesen_veriler.empty:
                print(f"\n'{kriter}' için '{sutun_adi}' sütununda bulunan veriler:")
                print(eslesen_veriler)

                # Veriyi txt dosyasına yaz
                dosya_adi = f"{kriter}_veriler.txt"
                try:
                    with open(dosya_adi, "w", encoding="utf-8") as file:
                        file.write(f"'{kriter}' için '{sutun_adi}' sütununda bulunan veriler:\n\n")
                        for _, row in eslesen_veriler.iterrows():
                            file.write("\n".join([
                                f"PROGRAM KODU: {row.get('Program Kodu', 'N/A')}",
                                f"ÜNİVERSİTE TÜRÜ: {row.get('Üniversite Türü', 'N/A')}",
                                f"ÜNİVERSİTE ADI: {row.get('Üniversite Adı', 'N/A')}",
                                f"FAKÜLTE ADI: {row.get('Fakülte/Yüksekokul Adı', 'N/A')}",
                                f"PROGRAM ADI: {row.get('Program Adı', 'N/A')}",
                                f"PUAN TÜRÜ: {row.get('Puan Türü', 'N/A')}",
                                f"KONTEJAN SAYISI: {row.get('Kontenjan', 'N/A')}",
                                f"YERLEŞEN KİŞİ SAYISI: {row.get('Yerleşen', 'N/A')}",
                                f"TABAN PUAN: {row.get('En Küçük Puan', 'N/A')}",
                                f"TAVAN PUAN: {row.get('En Büyük Puan', 'N/A')}",
                                "---------------------------------------------------------------------------------------"
                            ]) + "\n")
                    print(f"Veriler '{dosya_adi}' dosyasına yazıldı.")
                except Exception as e:
                    print(f"Dosya yazılırken bir hata oluştu: {e}")
            else:
                print(f"\n'{kriter}' için '{sutun_adi}' sütununda sonuç bulunamadı.")
        except KeyError:
            print(f"Hata: '{sutun_adi}' veya gerekli diğer sütunlar bulunamadı.")

    def ozel_arama(self, kriterler):
        """Birden fazla kriterle arama yapar."""
        if self.veri is None:
            print("Veri mevcut değil.")
            return

        try:
            # Filtreleme işlemi
            filtre = self.veri
            for sutun, deger in kriterler.items():
                if deger:  # Eğer değer verilmişse filtre uygula
                    filtre = filtre[filtre[sutun].astype(str).str.contains(deger, case=False, na=False)]

            if not filtre.empty:
                print("\nBelirtilen kriterlere uygun veriler:")
                print(filtre)

                dosya_adi = "ozel_arama_sonuclari.txt"
                try:
                    with open(dosya_adi, "w", encoding="utf-8") as file:
                        file.write("Belirtilen kriterlere uygun veriler:\n\n")
                        for _, row in filtre.iterrows():
                            file.write("\n".join([
                                f"PROGRAM KODU: {row.get('Program Kodu', 'N/A')}",
                                f"ÜNİVERSİTE TÜRÜ: {row.get('Üniversite Türü', 'N/A')}",
                                f"ÜNİVERSİTE ADI: {row.get('Üniversite Adı', 'N/A')}",
                                f"FAKÜLTE ADI: {row.get('Fakülte/Yüksekokul Adı', 'N/A')}",
                                f"PROGRAM ADI: {row.get('Program Adı', 'N/A')}",
                                f"PUAN TÜRÜ: {row.get('Puan Türü', 'N/A')}",
                                f"KONTEJAN SAYISI: {row.get('Kontenjan', 'N/A')}",
                                f"YERLEŞEN KİŞİ SAYISI: {row.get('Yerleşen', 'N/A')}",
                                f"TABAN PUAN: {row.get('En Küçük Puan', 'N/A')}",
                                f"TAVAN PUAN: {row.get('En Büyük Puan', 'N/A')}",
                                "---------------------------------------------------------------------------------------"
                            ]) + "\n")
                    print(f"Veriler '{dosya_adi}' dosyasına yazıldı.")
                except Exception as e:
                    print(f"Dosya yazılırken bir hata oluştu: {e}")
            else:
                print("\nBelirtilen kriterlere uygun sonuç bulunamadı.")
        except Exception as e:
            print(f"Bir hata oluştu: {e}")

def menu():
    print("// YKS TERCİH ASİSTANI //\n")
    print("""VERİLERİMİZ 2023 YERLEŞTİRME SONUÇLARINDAN ALINMIŞTIR.
    
    ARAMA SEÇENEKLERİ:

    1- ÜNİVERSİTE TÜRÜ
    2- ÜNİVERSİTE ADI
    3- FAKÜLTE ADI
    4- PROGRAM ADI
    5- PUAN TÜRÜ (söz, ea, say)
    6- ÖZEL ARAMA
    Çıkış için 'Exit' yazınız.
    """)

# Excel dosyasının adını belirtin
dosya_adi = "Data//2024_uni_puanlari.xlsx"

# Sınıfı başlat
tercih_botu = YksTercihBotu(dosya_adi)

durum = True
while durum:
    menu()
    secim = input("Seçim yapınız: ").strip()

    if secim.lower() == "exit":
        print("Çıkış yapılıyor... İyi günler!")
        break

    elif secim == "1":
        print("\n1 - Vakıf Üniversiteleri\n2 - Devlet Üniversiteleri\n")
        secim2 = input("Seçiminiz: ").strip()

        if secim2 == "1":
            tercih_botu.arama_yap("Üniversite Türü", "Vakıf")
        elif secim2 == "2":
            tercih_botu.arama_yap("Üniversite Türü", "Devlet")
        else:
            print("Geçersiz seçim yaptınız. Lütfen tekrar deneyin.")

    elif secim == "2":
        uni_adi = input("Lütfen üniversite adını giriniz: ").strip()
        tercih_botu.arama_yap("Üniversite Adı", uni_adi)

    elif secim == "3":
        fakulte_adi = input("Lütfen fakülte adını giriniz: ").strip()
        tercih_botu.arama_yap("Fakülte/Yüksekokul Adı", fakulte_adi)

    elif secim == "4":
        bolum_adi = input("Lütfen bölüm adını giriniz: ").strip()
        tercih_botu.arama_yap("Program Adı", bolum_adi)

    elif secim == "5":
        puan_turu = input("Lütfen puan türünü giriniz (söz, ea, say): ").strip()
        tercih_botu.arama_yap("Puan Türü", puan_turu)

    elif secim == "6":
        print("ÖZEL ARAMA: Kriterleri boş bırakarak göz ardı edebilirsiniz.")
        kriterler = {
            "Üniversite Adı": input("Üniversite adı: ").strip(),
            "Fakülte/Yüksekokul Adı": input("Fakülte adı: ").strip(),
            "Program Adı": input("Bölüm adı: ").strip(),
            "Puan Türü": input("Puan türü: ").strip()
        }
        tercih_botu.ozel_arama(kriterler)

    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")
