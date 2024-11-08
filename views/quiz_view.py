from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QRadioButton, QPushButton, QMessageBox, QButtonGroup

class QuizView(QWidget):
    def __init__(self, quiz_controller):
        super().__init__()

        self.quiz_controller = quiz_controller
        self.current_question = 0
        self.score = 0

        self.setWindowTitle("Minijuego de Eutrofización")
        self.setGeometry(150, 150, 600, 400)

        self.layout = QVBoxLayout()

        # Pregunta
        self.question_label = QLabel("")
        self.layout.addWidget(self.question_label)

        # Opciones (botones de radio)
        self.radio_group = QButtonGroup(self)
        self.option1 = QRadioButton("")
        self.option2 = QRadioButton("")
        self.option3 = QRadioButton("")
        self.option4 = QRadioButton("")
        
        self.radio_group.addButton(self.option1)
        self.radio_group.addButton(self.option2)
        self.radio_group.addButton(self.option3)
        self.radio_group.addButton(self.option4)

        self.layout.addWidget(self.option1)
        self.layout.addWidget(self.option2)
        self.layout.addWidget(self.option3)
        self.layout.addWidget(self.option4)

        # Botón para la siguiente pregunta
        self.next_button = QPushButton("Siguiente pregunta")
        self.next_button.clicked.connect(self.check_answer)
        self.layout.addWidget(self.next_button)

        self.setLayout(self.layout)
        self.load_question()

    def load_question(self):
        """Carga la siguiente pregunta y opciones."""
        question, options = self.quiz_controller.get_question(self.current_question)
        self.question_label.setText(question)
        self.option1.setText(options[0])
        self.option2.setText(options[1])
        self.option3.setText(options[2])
        self.option4.setText(options[3])

    def check_answer(self):
        """Verifica la respuesta seleccionada."""
        selected_button = self.radio_group.checkedButton()
        if selected_button is None:
            QMessageBox.warning(self, "Advertencia", "Por favor, selecciona una opción.")
            return
        
        selected_option = selected_button.text()
        correct_answer = self.quiz_controller.get_answer(self.current_question)
        
        if selected_option == correct_answer:
            self.score += 1

        self.current_question += 1
        
        if self.current_question < len(self.quiz_controller.questions):
            self.load_question()
        else:
            self.show_score()

    def show_score(self):
        """Muestra el puntaje final."""
        QMessageBox.information(self, "Resultado", f"Has completado el juego. Tu puntaje es: {self.score}/{len(self.quiz_controller.questions)}")
        self.close()
