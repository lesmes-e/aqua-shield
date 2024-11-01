import sys
from PyQt5.QtWidgets import QApplication
from views.main_view import MainView

def load_stylesheet():
    with open("./styles.qss", "r") as f:
        return f.read()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Cargar y aplicar el archivo de estilos
    stylesheet = load_stylesheet()
    app.setStyleSheet(stylesheet)

    window = MainView()
    window.show()

    sys.exit(app.exec_())

