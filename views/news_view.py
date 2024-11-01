from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout

class NewsView(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Noticias sobre Eutrofización")
        self.setGeometry(150, 150, 600, 400)

        layout = QVBoxLayout()

        # Etiqueta principal de noticias
        title = QLabel("Impacto de la Eutrofización en el Medio Ambiente")
        layout.addWidget(title)

        # Noticias estáticas, en el futuro podrían provenir de una API o archivo externo
        noticia_1 = QLabel("Noticia 1: La eutrofización en los lagos ha aumentado un 15% en los últimos 5 años.")
        noticia_2 = QLabel("Noticia 2: Comunidades costeras reportan una disminución significativa de especies marinas.")
        noticia_3 = QLabel("Noticia 3: Nuevas políticas buscan mitigar el impacto del exceso de nutrientes en el agua.")

        # Añadimos las noticias al layout
        layout.addWidget(noticia_1)
        layout.addWidget(noticia_2)
        layout.addWidget(noticia_3)

        # Configuramos el layout
        self.setLayout(layout)
