from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap  # Para manejar imágenes

class EducationView(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Educación sobre la Eutrofización")
        self.setGeometry(150, 150, 600, 400)

        layout = QVBoxLayout()

        # Título de la sección
        title = QLabel("¿Qué es la Eutrofización?")
        layout.addWidget(title)

        # Descripción educativa sobre la eutrofización
        description = QLabel("La eutrofización es un proceso causado por un exceso de nutrientes en cuerpos de agua, "
                             "lo que provoca el crecimiento desmesurado de algas y plantas acuáticas. Esto puede resultar "
                             "en la disminución de oxígeno en el agua, afectando la vida acuática y el ecosistema.")
        layout.addWidget(description)

        # Agregamos una imagen educativa
        image_label = QLabel(self)
        pixmap = QPixmap("ruta/a/la/imagen.jpg")  # Cambia la ruta a donde está la imagen en tu proyecto
        image_label.setPixmap(pixmap)
        image_label.setScaledContents(True)  # Esto hace que la imagen se ajuste al tamaño del label
        layout.addWidget(image_label)

        # Configuramos el layout
        self.setLayout(layout)
