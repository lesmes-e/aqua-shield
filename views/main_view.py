from tkinter import Frame, Label, Entry, Button, Toplevel
from tkinter import ttk
from controllers.eutrofizacion_calculator import EutrofizacionCalculator
from views.statistics_view import StatisticsView

class MainView(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master  # Reutilizamos la ventana principal que es 'master'
        self.pack(fill="both", expand=True)
        self.create_widgets()

    def create_widgets(self):
        # Configuramos la interfaz como antes
        input_frame = ttk.LabelFrame(self, text="Datos de Eutrofización", padding=(10, 10))
        input_frame.pack(fill="x", padx=20, pady=20)

        ttk.Label(input_frame, text="Nitrógeno:", font=("Helvetica", 12)).grid(row=0, column=0, padx=10, pady=10)
        ttk.Label(input_frame, text="Fósforo:", font=("Helvetica", 12)).grid(row=1, column=0, padx=10, pady=10)
        ttk.Label(input_frame, text="Oxígeno:", font=("Helvetica", 12)).grid(row=2, column=0, padx=10, pady=10)

        self.nitrogen = ttk.Entry(input_frame, font=("Helvetica", 12))
        self.phosphorus = ttk.Entry(input_frame, font=("Helvetica", 12))
        self.oxygen = ttk.Entry(input_frame, font=("Helvetica", 12))

        self.nitrogen.grid(row=0, column=1, padx=10, pady=10)
        self.phosphorus.grid(row=1, column=1, padx=10, pady=10)
        self.oxygen.grid(row=2, column=1, padx=10, pady=10)

        ttk.Button(input_frame, text="Calcular", command=self.calcular_eutrofizacion).grid(row=3, column=1, padx=10, pady=10, sticky="ew")
        ttk.Button(input_frame, text="Ver Estadísticas", command=self.mostrar_estadisticas).grid(row=4, column=1, padx=10, pady=10, sticky="ew")

        self.result_frame = ttk.LabelFrame(self, text="Resultado", padding=(10, 10))
        self.result_frame.pack(fill="x", padx=20, pady=20)

        self.result_label = ttk.Label(self.result_frame, text="Índice de Eutrofización: ", font=("Helvetica", 12))
        self.result_label.pack()

    def calcular_eutrofizacion(self):
        try:
            nitrogen = float(self.nitrogen.get())
            phosphorus = float(self.phosphorus.get())
            oxygen = float(self.oxygen.get())

            calculator = EutrofizacionCalculator(nitrogen, phosphorus, oxygen)
            resultado = calculator.calcular()

            self.result_label.config(text=f"Índice de Eutrofización: {resultado:.2f}", foreground="green")
        except ValueError:
            self.result_label.config(text="Por favor, ingresa valores numéricos válidos.", foreground="red")

    def mostrar_estadisticas(self):
        new_window = Toplevel(self)  # Toplevel crea una nueva ventana sin interferir con la principal
        StatisticsView(new_window)

