from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from controllers.eutrofizacion_calculator import EutrofizacionCalculator
from views.statistics_view import StatisticsView
from views.news_view import NewsView  # Importamos la nueva vista de noticias
from views.education_view import EducationView
from views.quiz_view import QuizView
from controllers.quiz_controller import QuizController
from views.history_view import HistoryView
from PyQt5.QtCore import Qt
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
        # Botón para alternar pantalla completa
        self.fullscreen_button = QPushButton("Alternar Pantalla Completa", self)
        self.fullscreen_button.clicked.connect(self.toggle_fullscreen)
        self.fullscreen_button.setGeometry(10, 10, 200, 30)  # Posición y tamaño del botón
        # Botones para calcular y mostrar estadísticas
        self.calculate_button = QPushButton("Calcular")
        self.calculate_button.clicked.connect(self.calcular_eutrofizacion)

        self.statistics_button = QPushButton("Ver Estadísticas")
        self.statistics_button.clicked.connect(self.mostrar_estadisticas)

        # Botón para mostrar noticias
        self.news_button = QPushButton("Ver Noticias")
        self.news_button.clicked.connect(self.mostrar_noticias)
        
        # Crear botón para abrir la sección educativa
        self.education_button = QPushButton("Educación sobre la Eutrofización")
        self.education_button.clicked.connect(self.mostrar_educacion)
        layout.addWidget(self.education_button)

        self.quiz_button = QPushButton("Minijuego: Prueba tus conocimientos")
        self.quiz_button.clicked.connect(self.mostrar_quiz)
        layout.addWidget(self.quiz_button)

        # Botón para abrir el historial
        self.history_button = QPushButton("Ver Historial de Cálculos")
        self.history_button.clicked.connect(self.mostrar_historial)
        layout.addWidget(self.history_button)

        self.setLayout(layout)
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
            location = "Lago A" # Lugar
            calculator = EutrofizacionCalculator(nitrogen, phosphorus, oxygen, location=location)
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
    
    def mostrar_educacion(self):
        self.education_window = EducationView()  # Crear una nueva ventana de educación
        self.education_window.show()

    def mostrar_quiz(self):
        self.quiz_controller = QuizController()  # Inicializa el controlador del minijuego
        self.quiz_window = QuizView(self.quiz_controller)  # Crear la ventana del minijuego
        self.quiz_window.show()

    def mostrar_historial(self):
        """Muestra la ventana del historial de cálculos."""
        self.history_window = HistoryView()
        self.history_window.show()
        
    def toggle_fullscreen(self):
        if self.isFullScreen():
            self.showNormal()  # Cambia a modo ventana normal
        else:
            self.showFullScreen()  # Cambia a pantalla completa
