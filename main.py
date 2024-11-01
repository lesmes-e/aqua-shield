import sys
from PyQt5.QtWidgets import QApplication
from views.main_view import MainView

if __name__ == "__main__":
    app = QApplication(sys.argv)  # Instancia de la aplicación Qt
    window = MainView()  # Creamos la vista principal
    window.show()  # Mostramos la ventana principal
    sys.exit(app.exec_())  # Iniciamos el bucle de eventos de Qt

