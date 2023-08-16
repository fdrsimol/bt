import json
import os
import tkinter as tk
from tkinter import ttk
from datetime import datetime

class FootballBettingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Cuotas de Fútbol")
        self.matches = []

        self.load_data()
        self.create_ui()

    def load_data(self):
        if os.path.exists("matches.json"):
            with open("matches.json", "r") as file:
                self.matches = json.load(file)

    def save_data(self):
        with open("matches.json", "w") as file:
            json.dump(self.matches, file, indent=4)

    def create_ui(self):
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack()

        self.add_tab()

      

    def add_tab(self):
        add_frame = tk.Frame(self.notebook)
        self.notebook.add(add_frame, text="Agregar Partido")

        tk.Label(add_frame, text="Nombre del Partido:").grid(row=0, column=0)
        self.partido_entry = tk.Entry(add_frame)
        self.partido_entry.grid(row=0, column=1)

        tk.Label(add_frame, text="Fecha (dd/mm/aaaa):").grid(row=1, column=0)
        self.fecha_entry = tk.Entry(add_frame)
        self.fecha_entry.grid(row=1, column=1)

        tk.Label(add_frame, text="Hora (hh:mm):").grid(row=2, column=0)
        self.hora_entry = tk.Entry(add_frame)
        self.hora_entry.grid(row=2, column=1)

        tk.Label(add_frame, text="Local:").grid(row=3, column=0)
        self.local_entry = tk.Entry(add_frame)
        self.local_entry.grid(row=3, column=1)

        tk.Label(add_frame, text="Empate:").grid(row=4, column=0)
        self.empate_entry = tk.Entry(add_frame)
        self.empate_entry.grid(row=4, column=1)

        tk.Label(add_frame, text="Visita:").grid(row=5, column=0)
        self.visita_entry = tk.Entry(add_frame)
        self.visita_entry.grid(row=5, column=1)

        tk.Label(add_frame, text="Más de 0.5:").grid(row=6, column=0)
        self.more_than_05_entry = tk.Entry(add_frame)
        self.more_than_05_entry.grid(row=6, column=1)

        tk.Label(add_frame, text="Más de 1.5:").grid(row=7, column=0)
        self.more_than_15_entry = tk.Entry(add_frame)
        self.more_than_15_entry.grid(row=7, column=1)

        tk.Label(add_frame, text="Más de 2.5:").grid(row=8, column=0)
        self.more_than_25_entry = tk.Entry(add_frame)
        self.more_than_25_entry.grid(row=8, column=1)

        tk.Label(add_frame, text="Más de 3.5:").grid(row=9, column=0)
        self.more_than_35_entry = tk.Entry(add_frame)
        self.more_than_35_entry.grid(row=9, column=1)

        tk.Label(add_frame, text="Más de 4.5:").grid(row=10, column=0)
        self.more_than_45_entry = tk.Entry(add_frame)
        self.more_than_45_entry.grid(row=10, column=1)

        
        tk.Label(add_frame, text="Menos de 0.5:").grid(row=11, column=0)
        self.less_than_05_entry = tk.Entry(add_frame)
        self.less_than_05_entry.grid(row=11, column=1)


        tk.Label(add_frame, text="Menos de 1.5:").grid(row=12, column=0)
        self.less_than_15_entry = tk.Entry(add_frame)
        self.less_than_15_entry.grid(row=12, column=1)

        tk.Label(add_frame, text="Menos de 2.5:").grid(row=13, column=0)
        self.less_than_25_entry = tk.Entry(add_frame)
        self.less_than_25_entry.grid(row=13, column=1)

        tk.Label(add_frame, text="Menos de 3.5:").grid(row=14, column=0)
        self.less_than_35_entry = tk.Entry(add_frame)
        self.less_than_35_entry.grid(row=14, column=1)

        tk.Label(add_frame, text="Menos de 4.5:").grid(row=15, column=0)
        self.less_than_45_entry = tk.Entry(add_frame)
        self.less_than_45_entry.grid(row=15, column=1)
        
        tk.Label(add_frame, text="Menos de 0.5 visita:").grid(row=16, column=0)
        self.less_than_05_visita_entry = tk.Entry(add_frame)
        self.less_than_05_visita_entry.grid(row=16, column=1)

        # ... (other fields)

        tk.Label(add_frame, text="Más de 11.5 esquina:").grid(row=17, column=0)
        self.more_than_115_corner_entry = tk.Entry(add_frame)
        self.more_than_115_corner_entry.grid(row=17, column=1)

        tk.Label(add_frame, text="Menos de 4.5 esquina:").grid(row=18, column=0)
        self.less_than_45_corner_entry = tk.Entry(add_frame)
        self.less_than_45_corner_entry.grid(row=18, column=1)

        tk.Label(add_frame, text="Más de 0.5 local:").grid(row=19, column=0)
        self.more_than_05_local_entry = tk.Entry(add_frame)
        self.more_than_05_local_entry.grid(row=19, column=1)

        tk.Label(add_frame, text="Más de 1.5 local:").grid(row=21, column=0)
        self.more_than_15_local_entry = tk.Entry(add_frame)
        self.more_than_15_local_entry.grid(row=21, column=1)

        tk.Label(add_frame, text="Más de 2.5 local:").grid(row=22, column=0)
        self.more_than_25_local_entry = tk.Entry(add_frame)
        self.more_than_25_local_entry.grid(row=22, column=1)

        tk.Label(add_frame, text="Más de 3.5 local:").grid(row=23, column=0)
        self.more_than_35_local_entry = tk.Entry(add_frame)
        self.more_than_35_local_entry.grid(row=23, column=1)

        tk.Label(add_frame, text="Menos de 0.5 local:").grid(row=24, column=0)
        self.less_than_05_local_entry = tk.Entry(add_frame)
        self.less_than_05_local_entry.grid(row=24, column=1)

        tk.Label(add_frame, text="Menos de 1.5 local:").grid(row=25, column=0)
        self.less_than_15_local_entry = tk.Entry(add_frame)
        self.less_than_15_local_entry.grid(row=25, column=1)

        tk.Label(add_frame, text="Menos de 2.5 local:").grid(row=26, column=0)
        self.less_than_25_local_entry = tk.Entry(add_frame)
        self.less_than_25_local_entry.grid(row=26, column=1)

        tk.Label(add_frame, text="Menos de 3.5 local:").grid(row=27, column=0)
        self.less_than_35_local_entry = tk.Entry(add_frame)
        self.less_than_35_local_entry.grid(row=27, column=1)

        tk.Label(add_frame, text="1X:").grid(row=28, column=0)
        self.x1_entry = tk.Entry(add_frame)
        self.x1_entry.grid(row=28, column=1)

        tk.Label(add_frame, text="12:").grid(row=29, column=0)
        self.x2_entry = tk.Entry(add_frame)
        self.x2_entry.grid(row=29, column=1)

        tk.Label(add_frame, text="X2:").grid(row=30, column=0)
        self.x2_entry = tk.Entry(add_frame)
        self.x2_entry.grid(row=30, column=1)

        tk.Label(add_frame, text="Si:").grid(row=31, column=0)
        self.si_entry = tk.Entry(add_frame)
        self.si_entry.grid(row=31, column=1)

        tk.Label(add_frame, text="No:").grid(row=32, column=0)
        self.no_entry = tk.Entry(add_frame)
        self.no_entry.grid(row=32, column=1)
        tk.Label(add_frame, text="Más de 0.5 visita:").grid(row=33, column=0)
        self.more_than_05_visita_entry = tk.Entry(add_frame)
        self.more_than_05_visita_entry.grid(row=33, column=1)

        tk.Label(add_frame, text="Más de 1.5 visita:").grid(row=34, column=0)
        self.more_than_15_visita_entry = tk.Entry(add_frame)
        self.more_than_15_visita_entry.grid(row=34, column=1)

        tk.Label(add_frame, text="Más de 2.5 visita:").grid(row=35, column=0)
        self.more_than_25_visita_entry = tk.Entry(add_frame)
        self.more_than_25_visita_entry.grid(row=35, column=1)

        tk.Label(add_frame, text="Más de 3.5 visita:").grid(row=36, column=0)
        self.more_than_35_visita_entry = tk.Entry(add_frame)
        self.more_than_35_visita_entry.grid(row=36, column=1) 
        tk.Label(add_frame, text="Menos de 0.5 visita:").grid(row=37, column=0)
        self.less_than_05_visita_entry = tk.Entry(add_frame)
        self.less_than_05_visita_entry.grid(row=37, column=1)

        tk.Label(add_frame, text="Menos de 1.5 visita:").grid(row=38, column=0)
        self.less_than_15_visita_entry = tk.Entry(add_frame)
        self.less_than_15_visita_entry.grid(row=38, column=1)

        tk.Label(add_frame, text="Menos de 2.5 visita:").grid(row=39, column=0)
        self.less_than_25_visita_entry = tk.Entry(add_frame)
        self.less_than_25_visita_entry.grid(row=39, column=1)

        tk.Label(add_frame, text="Menos de 3.5 visita:").grid(row=40, column=0)
        self.less_than_35_visita_entry = tk.Entry(add_frame)
        self.less_than_35_visita_entry.grid(row=40, column=1)

        tk.Label(add_frame, text="Más de 4.5 esquina:").grid(row=41, column=0)
        self.more_than_45_corner_entry = tk.Entry(add_frame)
        self.more_than_45_corner_entry.grid(row=41, column=1)

        tk.Label(add_frame, text="Más de 5.5 esquina:").grid(row=42, column=0)
        self.more_than_55_corner_entry = tk.Entry(add_frame)
        self.more_than_55_corner_entry.grid(row=42, column=1)

        tk.Label(add_frame, text="Más de 6.5 esquina:").grid(row=43, column=0)
        self.more_than_65_corner_entry = tk.Entry(add_frame)
        self.more_than_65_corner_entry.grid(row=43, column=1)

        tk.Label(add_frame, text="Menos de 11.5 esquina:").grid(row=44, column=0)
        self.less_than_115_corner_entry = tk.Entry(add_frame)
        self.less_than_115_corner_entry.grid(row=44, column=1)   
        add_button = tk.Button(add_frame, text="Agregar Partido", command=self.add_match)
        add_button.grid(row=50, columnspan=2) 

    def add_match(self):
        partido = self.partido_entry.get()
        fecha_str = self.fecha_entry.get()
        hora_str = self.hora_entry.get()
        local = float(self.local_entry.get())
        empate = float(self.empate_entry.get())
        visita = float(self.visita_entry.get())
        more_than_05 = float(self.more_than_05_entry.get())
        more_than_15 = float(self.more_than_15_entry.get())
        more_than_25 = float(self.more_than_25_entry.get())
        more_than_35 = float(self.more_than_35_entry.get())
        more_than_45 = float(self.more_than_45_entry.get())
        less_than_15 = float(self.less_than_15_entry.get())
        less_than_25 = float(self.less_than_25_entry.get())
        less_than_35 = float(self.less_than_35_entry.get())
        less_than_45 = float(self.less_than_45_entry.get())
        x1 = float(self.x1_entry.get())
        x2 = float(self.x2_entry.get())
        si = float(self.si_entry.get())
        no = float(self.no_entry.get())
        more_than_05_local = float(self.more_than_05_local_entry.get())
        more_than_15_local = float(self.more_than_15_local_entry.get())
        more_than_25_local = float(self.more_than_25_local_entry.get())
        more_than_35_local = float(self.more_than_35_local_entry.get())
        less_than_05_local = float(self.less_than_05_local_entry.get())
        less_than_15_local = float(self.less_than_15_local_entry.get())
        less_than_25_local = float(self.less_than_25_local_entry.get())
        less_than_35_local = float(self.less_than_35_local_entry.get())
        more_than_05_visita = float(self.more_than_05_visita_entry.get())
        more_than_15_visita = float(self.more_than_15_visita_entry.get())
        more_than_25_visita = float(self.more_than_25_visita_entry.get())
        more_than_35_visita = float(self.more_than_35_visita_entry.get())
        less_than_05_visita = float(self.less_than_05_visita_entry.get())
        less_than_15_visita = float(self.less_than_15_visita_entry.get())
        less_than_25_visita = float(self.less_than_25_visita_entry.get())
        less_than_35_visita = float(self.less_than_35_visita_entry.get())
        more_than_45_corner = float(self.more_than_45_corner_entry.get())
        more_than_55_corner = float(self.more_than_55_corner_entry.get())
        more_than_65_corner = float(self.more_than_65_corner_entry.get())
        
        more_than_115_corner = float(self.more_than_115_corner_entry.get())
        less_than_45_corner = float(self.less_than_45_corner_entry.get())
        
        less_than_115_corner = float(self.less_than_115_corner_entry.get())
        

        fecha = datetime.strptime(fecha_str, "%d/%m/%Y").strftime("%Y-%m-%d")
        hora = datetime.strptime(hora_str, "%H:%M").strftime("%H:%M")

        match_data = {
            "partido": partido,
            "fecha": fecha + " " + hora,
            "local": local,
            "empate": empate,
            "visita": visita,
            "más de 0.5": more_than_05,
            "más de 1.5": more_than_15,
            "más de 2.5": more_than_25,
            "más de 3.5": more_than_35,
            "más de 4.5": more_than_45,
            "menos de 1.5": less_than_15,
            "menos de 2.5": less_than_25,
            "menos de 3.5": less_than_35,
            "menos de 4.5": less_than_45,
            "1X": x1,
            "12": x2,
            "X2": x2,
            "Si": si,
            "No": no,
            "más de 0.5 local": more_than_05_local,
            "más de 1.5 local": more_than_15_local,
            "más de 2.5 local": more_than_25_local,
            "más de 3.5 local": more_than_35_local,
            "menos de 0.5 local": less_than_05_local,
            "menos de 1.5 local": less_than_15_local,
            "menos de 2.5 local": less_than_25_local,
            "menos de 3.5 local": less_than_35_local,
            "más de 0.5 visita": more_than_05_visita,
            "más de 1.5 visita": more_than_15_visita,
            "más de 2.5 visita": more_than_25_visita,
            "más de 3.5 visita": more_than_35_visita,
            "menos de 0.5 visita": less_than_05_visita,
            "menos de 1.5 visita": less_than_15_visita,
            "menos de 2.5 visita": less_than_25_visita,
            "menos de 3.5 visita": less_than_35_visita,
            "más de 4.5 esquina": more_than_45_corner,
            "más de 5.5 esquina": more_than_55_corner,
            "más de 6.5 esquina": more_than_65_corner,
            "más de 11.5 esquina": more_than_115_corner,
            "menos de 4.5 esquina": less_than_45_corner,
            "menos de 11.5 esquina": less_than_115_corner,
            # Add other fields here
            # ...
        }

        self.matches.append(match_data)
        self.save_data()

        # Clear the entry fields after adding
        self.partido_entry.delete(0, tk.END)
        self.fecha_entry.delete(0, tk.END)
        self.hora_entry.delete(0, tk.END)
        self.local_entry.delete(0, tk.END)
        self.empate_entry.delete(0, tk.END)
        self.visita_entry.delete(0, tk.END)
        self.more_than_05_entry.delete(0, tk.END)
        self.more_than_15_entry.delete(0, tk.END)
        self.more_than_25_entry.delete(0, tk.END)
        self.more_than_35_entry.delete(0, tk.END)
        self.more_than_45_entry.delete(0, tk.END)
        self.less_than_15_entry.delete(0, tk.END)
        self.less_than_25_entry.delete(0, tk.END)
        self.less_than_35_entry.delete(0, tk.END)
        self.less_than_45_entry.delete(0, tk.END)
        self.x1_entry.delete(0, tk.END)
        self.x2_entry.delete(0, tk.END)
        self.si_entry.delete(0, tk.END)
        self.no_entry.delete(0, tk.END)
        self.more_than_05_local_entry.delete(0, tk.END)
        self.more_than_15_local_entry.delete(0, tk.END)
        self.more_than_25_local_entry.delete(0, tk.END)
        self.more_than_35_local_entry.delete(0, tk.END)
        self.less_than_05_local_entry.delete(0, tk.END)
        self.less_than_15_local_entry.delete(0, tk.END)
        self.less_than_25_local_entry.delete(0, tk.END)
        self.less_than_35_local_entry.delete(0, tk.END)
        self.more_than_05_visita_entry.delete(0, tk.END)
        self.more_than_15_visita_entry.delete(0, tk.END)
        self.more_than_25_visita_entry.delete(0, tk.END)
        self.more_than_35_visita_entry.delete(0, tk.END)
        self.less_than_05_visita_entry.delete(0, tk.END)
        self.less_than_15_visita_entry.delete(0, tk.END)
        self.less_than_25_visita_entry.delete(0, tk.END)
        self.less_than_35_visita_entry.delete(0, tk.END)
        self.more_than_45_corner_entry.delete(0, tk.END)
        self.more_than_55_corner_entry.delete(0, tk.END)
        self.more_than_65_corner_entry.delete(0, tk.END)
        self.more_than_115_corner_entry.delete(0, tk.END)
        self.less_than_45_corner_entry.delete(0, tk.END)
        self.less_than_115_corner_entry.delete(0, tk.END)
        # Clear other fields
        # ...

    # ... (same as before)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = FootballBettingApp(root)
    app.run()


