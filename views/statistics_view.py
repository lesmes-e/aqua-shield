from tkinter import Frame, Label
from tkinter import ttk
from controllers.statistics_fetcher import StatisticsFetcher

class StatisticsView(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack(fill="both", expand=True)
        self.create_widgets()

    def create_widgets(self):
        self.master.title("Estadísticas Semanales")
        self.master.geometry("500x300")

        fetcher = StatisticsFetcher()
        weekly_data = fetcher.get_weekly_statistics()

        stats_frame = ttk.LabelFrame(self, text="Estadísticas de Calidad de Agua", padding=(10, 10))
        stats_frame.pack(fill="both", padx=20, pady=20)

        Label(stats_frame, text="Estadísticas Semanales", font=("Helvetica", 14, "bold")).grid(row=0, column=0, padx=10, pady=10)

        for i, row in enumerate(weekly_data.itertuples(), 1):
            Label(stats_frame, text=f"Día {i}: Nitrógeno: {row.nitrogen}, Fósforo: {row.phosphorus}, Oxígeno: {row.oxygen}",
                  font=("Helvetica", 12)).grid(row=i, column=0, padx=10, pady=5)

