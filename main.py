import sys
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction, QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from views.main_view import MainView

def load_stylesheet():
    with open("./styles.qss", "r") as f:
        return f.read()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Cargar y aplicar el archivo de estilos
    stylesheet = load_stylesheet()
    app.setStyleSheet(stylesheet)

    # Crear ventana principal
    window = MainView()

    # Establecer el icono de la ventana
    window.setWindowIcon(QIcon('./assets/icon.ico'))  # Cambia la ruta al archivo de tu icono

    # Poner la ventana en pantalla completa al inicio
    window.showFullScreen()  # Esto abre la ventana en modo pantalla completa

    # Función para salir del modo pantalla completa
    def toggle_fullscreen(event):
        if event.key() == Qt.Key_Escape:
            if window.isFullScreen():
                window.showNormal()  # Modo ventana normal
            else:
                window.showFullScreen()  # Modo pantalla completa

    window.keyPressEvent = toggle_fullscreen  # Asignar la función al evento de tecla

    # Crear el icono en la barra de tareas
    tray_icon = QSystemTrayIcon(QIcon('./assets/icon.ico'), parent=app)  # Icono de la barra de tareas
    tray_icon.setToolTip("Aplicación de Eutrofización")  # Texto que aparece al pasar el mouse sobre el icono

    # Crear el menú del icono en la barra de tareas
    tray_menu = QMenu()
    exit_action = QAction("Salir")
    exit_action.triggered.connect(app.quit)  # Cerrar la aplicación
    tray_menu.addAction(exit_action)

    tray_icon.setContextMenu(tray_menu)  # Añadir el menú al icono
    tray_icon.show()  # Mostrar el icono en la bandeja

    window.show()  # Mostrar la ventana principal

    sys.exit(app.exec_())
