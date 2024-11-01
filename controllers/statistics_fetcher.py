import pandas as pd

class StatisticsFetcher:
    def __init__(self, data_path="data/water_quality_data.csv"):
        self.data_path = data_path

    def get_weekly_statistics(self):
        data = pd.read_csv(self.data_path)
        # Lógica para obtener estadísticas de la semana en curso
        weekly_data = data.tail(7)
        return weekly_data
