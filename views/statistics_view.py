from tkinter import Frame, Label
from controllers.statistics_fetcher import StatisticsFetcher

class StatisticsView(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.create_widgets()

    def create_widgets(self):
        fetcher = StatisticsFetcher()
        weekly_data = fetcher.get_weekly_statistics()

        Label(self, text="Estadísticas Semanales").grid(row=0, column=0)
        
        for i, row in enumerate(weekly_data.itertuples(), 1):
            Label(self, text=f"Día {i}: Nitrogen: {row.nitrogen}, Phosphorus: {row.phosphorus}, Oxygen: {row.oxygen}").grid(row=i, column=0)
