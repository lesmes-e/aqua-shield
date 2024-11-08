# controllers/statistics_fetcher.py

import pandas as pd

class StatisticsFetcher:
    def __init__(self):
        self.data_file = "data/water_quality_data.csv"
    
    def fetch_statistics(self):
        try:
            df = pd.read_csv(self.data_file)
            # Aquí procesas los datos y extraes las estadísticas
            return df.describe()  # Ejemplo de estadísticas
        except FileNotFoundError:
            return None

