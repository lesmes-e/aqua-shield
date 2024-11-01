from tkinter import Frame, Label, Entry, Button
from controllers.eutrofizacion_calculator import EutrofizacionCalculator
from views.statistics_view import StatisticsView

class MainView(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.create_widgets()

    def create_widgets(self):
        Label(self, text="Nitrogeno:").grid(row=0)
        Label(self, text="Fosforo:").grid(row=1)
        Label(self, text="Oxigeno:").grid(row=2)

        self.nitrogen = Entry(self)
        self.phosphorus = Entry(self)
        self.oxygen = Entry(self)

        self.nitrogen.grid(row=0, column=1)
        self.phosphorus.grid(row=1, column=1)
        self.oxygen.grid(row=2, column=1)

        Button(self, text="Calcular", command=self.calcular_eutrofizacion).grid(row=3, column=1)
        Button(self, text="Ver Estadísticas", command=self.mostrar_estadisticas).grid(row=4, column=1)

    def calcular_eutrofizacion(self):
        nitrogen = float(self.nitrogen.get())
        phosphorus = float(self.phosphorus.get())
        oxygen = float(self.oxygen.get())

        calculator = EutrofizacionCalculator(nitrogen, phosphorus, oxygen)
        resultado = calculator.calcular()

        Label(self, text=f"Índice de Eutrofización: {resultado:.2f}").grid(row=5, column=1)

    def mostrar_estadisticas(self):
        new_window = Toplevel(self) # type: ignore
        StatisticsView(new_window)
