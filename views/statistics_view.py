from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from controllers.statistics_fetcher import StatisticsFetcher

class StatisticsView(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Estadísticas Semanales")
        self.setGeometry(150, 150, 500, 300)

        layout = QVBoxLayout()

        fetcher = StatisticsFetcher()
        weekly_data = fetcher.get_weekly_statistics()

        # Creamos los widgets para mostrar las estadísticas
        stats_label = QLabel("Estadísticas de Calidad de Agua")
        layout.addWidget(stats_label)

        for i, row in enumerate(weekly_data.itertuples(), 1):
            stat_label = QLabel(f"Día {i}: Nitrógeno: {row.nitrogen}, Fósforo: {row.phosphorus}, Oxígeno: {row.oxygen}")
            layout.addWidget(stat_label)

        # Configuramos el layout
        self.setLayout(layout)

