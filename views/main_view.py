from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from controllers.eutrofizacion_calculator import EutrofizacionCalculator
from views.statistics_view import StatisticsView
from views.news_view import NewsView  # Importamos la nueva vista de noticias

class MainView(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Aplicación de Eutrofización")
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        # Campos de entrada
        self.nitrogen_label = QLabel("Nitrógeno:")
        self.nitrogen_input = QLineEdit()

        self.phosphorus_label = QLabel("Fósforo:")
        self.phosphorus_input = QLineEdit()

        self.oxygen_label = QLabel("Oxígeno:")
        self.oxygen_input = QLineEdit()

        # Botones para calcular y mostrar estadísticas
        self.calculate_button = QPushButton("Calcular")
        self.calculate_button.clicked.connect(self.calcular_eutrofizacion)

        self.statistics_button = QPushButton("Ver Estadísticas")
        self.statistics_button.clicked.connect(self.mostrar_estadisticas)

        # Botón para mostrar noticias
        self.news_button = QPushButton("Ver Noticias")
        self.news_button.clicked.connect(self.mostrar_noticias)

        # Agregar widgets al layout
        layout.addWidget(self.nitrogen_label)
        layout.addWidget(self.nitrogen_input)
        layout.addWidget(self.phosphorus_label)
        layout.addWidget(self.phosphorus_input)
        layout.addWidget(self.oxygen_label)
        layout.addWidget(self.oxygen_input)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.statistics_button)
        layout.addWidget(self.news_button)

        # Configurar layout principal
        self.setLayout(layout)

    def calcular_eutrofizacion(self):
        try:
            nitrogen = float(self.nitrogen_input.text())
            phosphorus = float(self.phosphorus_input.text())
            oxygen = float(self.oxygen_input.text())

            calculator = EutrofizacionCalculator(nitrogen, phosphorus, oxygen)
            resultado = calculator.calcular()

            QMessageBox.information(self, "Resultado", f"Índice de Eutrofización: {resultado:.2f}")
        except ValueError:
            QMessageBox.warning(self, "Error", "Por favor, ingresa valores numéricos válidos.")

    def mostrar_estadisticas(self):
        self.stats_window = StatisticsView()
        self.stats_window.show()

    def mostrar_noticias(self):
        self.news_window = NewsView()  # Creamos la ventana de noticias
        self.news_window.show()

