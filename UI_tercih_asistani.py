import pandas as pd
import json
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

class YksTercihBotu:
    def __init__(self, excel_dosyasi):
        self.excel_dosyasi = excel_dosyasi
        try:
            self.veri = pd.read_excel(excel_dosyasi)
            print("Excel dosyası başarıyla yüklendi.")
        except Exception as e:
            print(f"Excel dosyası yüklenirken bir hata oluştu: {e}")
            self.veri = None

    def arama_yap(self, kriterler):
        if self.veri is None:
            messagebox.showerror("Hata", "Veri mevcut değil.")
            return

        try:
            filtre = self.veri.copy()
            for sutun, kriter in kriterler.items():
                filtre = filtre[filtre[sutun].astype(str).str.contains(kriter, case=False, na=False)]

            if not filtre.empty:
                dosya_adi_txt = "arama_sonuclari.txt"
                dosya_adi_json = "arama_sonuclari.json"

                try:
                    filtre.to_csv(dosya_adi_txt, index=False, sep='\t', encoding="utf-8")
                    filtre.to_json(dosya_adi_json, orient='records', force_ascii=False, indent=4)
                    messagebox.showinfo("Başarılı", f"Sonuçlar kaydedildi: \n- {dosya_adi_txt}\n- {dosya_adi_json}")
                except Exception as e:
                    messagebox.showerror("Hata", f"Dosya yazılırken bir hata oluştu: {e}")
            else:
                messagebox.showinfo("Bilgi", "Hiçbir sonuç bulunamadı.")
        except Exception as e:
            messagebox.showerror("Hata", f"Arama sırasında bir hata oluştu: {e}")

class YksTercihGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("YKS Tercih Asistanı")

        self.bot = None

        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=20, padx=20)

        self.label = tk.Label(frame, text="Excel Dosyasını Seçin:")
        self.label.grid(row=0, column=0, padx=5, pady=5)

        self.file_entry = tk.Entry(frame, width=40)
        self.file_entry.grid(row=0, column=1, padx=5, pady=5)

        self.browse_button = tk.Button(frame, text="Gözat", command=self.browse_file)
        self.browse_button.grid(row=0, column=2, padx=5, pady=5)

        self.load_button = tk.Button(frame, text="Yükle", command=self.load_file)
        self.load_button.grid(row=0, column=3, padx=5, pady=5)

        self.criteria_frame = tk.LabelFrame(self.root, text="Arama Kriterleri")
        self.criteria_frame.pack(pady=10, padx=10, fill="both")

        self.criteria_widgets = []
        self.add_criteria_button = tk.Button(self.criteria_frame, text="Kriter Ekle", command=self.add_criteria)
        self.add_criteria_button.pack(pady=5)

        self.search_button = tk.Button(self.root, text="Ara", command=self.search)
        self.search_button.pack(pady=10)

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx"), ("All Files", "*.*")])
        self.file_entry.delete(0, tk.END)
        self.file_entry.insert(0, file_path)

    def load_file(self):
        file_path = self.file_entry.get()
        if not file_path:
            messagebox.showerror("Hata", "Lütfen bir dosya seçin.")
            return

        try:
            self.bot = YksTercihBotu(file_path)
            # Sütunları göster
            self.show_columns()
            messagebox.showinfo("Başarılı", "Excel dosyası başarıyla yüklendi.")
        except Exception as e:
            messagebox.showerror("Hata", f"Dosya yüklenirken bir hata oluştu: {e}")

    def show_columns(self):
        if self.bot:
            columns = list(self.bot.veri.columns)
            for widget in self.criteria_widgets:
                widget[0].destroy()
                widget[1].destroy()
            self.criteria_widgets.clear()

            for column in columns:
                row = tk.Frame(self.criteria_frame)
                row.pack(pady=2, padx=2)

                column_label = tk.Label(row, text=f"Sütun: {column}")
                column_label.pack(side=tk.LEFT, padx=5)

                value_entry = tk.Entry(row, width=20)
                value_entry.pack(side=tk.LEFT, padx=5)

                self.criteria_widgets.append((column, value_entry))

    def add_criteria(self):
        row = tk.Frame(self.criteria_frame)
        row.pack(pady=2, padx=2)

        column_label = tk.Label(row, text="Sütun Adı:")
        column_label.pack(side=tk.LEFT, padx=5)

        column_combo = ttk.Combobox(row, width=20)
        column_combo['values'] = [col for col in self.bot.veri.columns] if self.bot else []
        column_combo.pack(side=tk.LEFT, padx=5)

        value_label = tk.Label(row, text="Kriter:")
        value_label.pack(side=tk.LEFT, padx=5)

        value_entry = tk.Entry(row, width=20)
        value_entry.pack(side=tk.LEFT, padx=5)

        self.criteria_widgets.append((column_combo, value_entry))

    def search(self):
        if not self.bot:
            messagebox.showerror("Hata", "Önce bir Excel dosyası yükleyin.")
            return

        kriterler = {}
        for column_widget, value_entry in self.criteria_widgets:
            if isinstance(column_widget, ttk.Combobox):
                column = column_widget.get().strip()
            else:
                column = column_widget

            value = value_entry.get().strip()
            if column and value:
                kriterler[column] = value

        if kriterler:
            self.bot.arama_yap(kriterler)
        else:
            messagebox.showwarning("Uyarı", "Hiçbir kriter girilmedi.")

if __name__ == "__main__":
    root = tk.Tk()
    gui = YksTercihGUI(root)
    root.mainloop()
