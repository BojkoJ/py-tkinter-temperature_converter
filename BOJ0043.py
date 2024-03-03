import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

class UnitConverterApp(tk.Tk): # Definujeme třídu UnitConverterApp, která dědí z třídy Tk z modulu tkinter
    def __init__(self):  # Definujeme konstruktor třídy
        super().__init__()  # Voláme konstruktor nadřazené třídy

        self.title("Převaděč jednotek")
        self.resizable(False, False)

        self.converter_frame = tk.LabelFrame(self, text="Levý Frame")  # Vytváříme rámeček pro levou část aplikace
        self.converter_frame.pack(side="left", padx=10, pady=10, fill="y")

        self.direction_frame = tk.LabelFrame(self.converter_frame, text="Směr převodu")  # Vytváříme rámeček pro směr převodu
        self.direction_frame.pack(fill="x", padx=10, pady=(10, 5))

        self.radio_var = tk.StringVar(value="C_to_F")  # Vytváříme proměnnou pro uchování hodnoty vybraného směru převodu
        self.c_to_f_radio = tk.Radiobutton(self.direction_frame, text="C -> F", variable=self.radio_var, value="C_to_F")  # Vytváříme radio button pro převod z °C na °F
        self.c_to_f_radio.pack(anchor="w")

        self.f_to_c_radio = tk.Radiobutton(self.direction_frame, text="F -> C", variable=self.radio_var, value="F_to_C")  # Vytváříme radio button pro převod z °F na °C
        self.f_to_c_radio.pack(anchor="w")

        self.input_frame = tk.LabelFrame(self.converter_frame, text="Převod", padx=20, pady=50)  # Vytváříme rámeček pro vstupy
        self.input_frame.pack(fill="both", expand=True, padx=10, pady=5)

        self.input_label = tk.Label(self.input_frame, text="Vstup", pady=10)  # Vytváříme popisek pro vstup
        self.input_label.grid(row=0, column=0)

        self.input_entry = tk.Entry(self.input_frame)  # Vytváříme vstupní pole pro zadání hodnoty
        self.input_entry.grid(row=0, column=1, sticky="ew")

        self.output_label = tk.Label(self.input_frame, text="Výstup")  # Vytváříme popisek pro výstup
        self.output_label.grid(row=1, column=0)

        self.output_entry = tk.Entry(self.input_frame, state="readonly")  # Vytváříme výstupní pole pro zobrazení výsledku
        self.output_entry.grid(row=1, column=1, sticky="ew")

        self.convert_button = tk.Button(self.converter_frame, text="Převést", command=self.convert)  # Vytváříme tlačítko pro převod
        self.convert_button.pack(side="bottom", padx=10, pady=(5, 10))

        # Vytváříme label s podpisem
        self.bottom_label = tk.Label(self.converter_frame, text="Jan Bojko BOJ0043")
        self.bottom_label.pack(side="bottom", padx=10, pady=(5, 10))

        self.image_frame = tk.LabelFrame(self, text="Pravý frame")  # Vytváříme rámeček pro pravou část aplikace
        self.image_frame.pack(side="left", padx=10, pady=10, fill="both")

        scriptdir = os.path.dirname(os.path.abspath(__file__))  # Získáváme cestu k aktuálnímu adresáři skriptu
        imagepath = os.path.join(scriptdir, 'th_empty.png')  # Vytváříme cestu k obrázku

        if os.path.exists(imagepath):  # Pokud existuje soubor s obrázkem
            self.photo = ImageTk.PhotoImage(Image.open(imagepath))  # Otevřeme obrázek a vytvoříme z něj PhotoImage
            self.lbl_image = tk.Label(self.image_frame, image=self.photo)
            self.lbl_image.pack(padx=10, pady=10, fill="both", expand=True)
        else:
            print("Soubor obrázku nenalezen:", imagepath)  # Vypíšeme chybovou hlášku, pokud soubor neexistuje

    def convert(self):  # Metoda pro převod teploty
        try:
            temperature = float(self.input_entry.get())  # Získáváme hodnotu z vstupního pole a převádíme ji na desetinné číslo
            if self.radio_var.get() == "C_to_F":  # Pokud je vybrán převod z °C na °F
                result = (temperature * 9/5) + 32
            else:
                result = (temperature - 32) * 5/9

            self.output_entry.config(state="normal")  # Povolujeme úpravu výstupního pole
            self.output_entry.delete(0, tk.END)  # Smažeme obsah výstupního pole
            self.output_entry.insert(0, f"{result:.2f}")  # Vkládáme výsledek do výstupního pole s dvěma desetinnými místy
            self.output_entry.config(state="readonly")

            scriptdir = os.path.dirname(os.path.abspath(__file__)) # Image Handling - Stejné jako v konstruktoru
            imagepath = os.path.join(scriptdir, 'th.png')

            if os.path.exists(imagepath):
                self.photo = ImageTk.PhotoImage(Image.open(imagepath))
                self.lbl_image.config(image=self.photo)
            else:
                print("Soubor obrázku nenalezen:", imagepath)

        except ValueError:
            messagebox.showerror("Chyba", "Špatný vstup. Prosím uveďte validní číslo.")  # Zobrazíme chybovou hlášku, pokud je vstup neplatný

if __name__ == "__main__":
    app = UnitConverterApp()  # Vytváříme instanci třídy UnitConverterApp
    app.mainloop()
