class QuizController:
    def __init__(self):
        self.questions = [
            {
                "question": "¿Qué es la eutrofización?",
                "options": [
                    "Un aumento de nutrientes en el agua",
                    "Un proceso de purificación natural del agua",
                    "La formación de sedimentos",
                    "La oxidación del agua"
                ],
                "answer": "Un aumento de nutrientes en el agua"
            },
            {
                "question": "¿Qué provoca la eutrofización?",
                "options": [
                    "La reducción de algas",
                    "El aumento de oxígeno en el agua",
                    "El crecimiento desmesurado de algas",
                    "La disminución de nutrientes en el agua"
                ],
                "answer": "El crecimiento desmesurado de algas"
            },
            {
                "question": "¿Cómo puede prevenirse la eutrofización?",
                "options": [
                    "Reduciendo el uso de fertilizantes",
                    "Aumentando el uso de pesticidas",
                    "Añadiendo más nutrientes al agua",
                    "No tiene prevención"
                ],
                "answer": "Reduciendo el uso de fertilizantes"
            }
        ]

    def get_question(self, index):
        """Devuelve la pregunta y las opciones en el índice dado."""
        question = self.questions[index]["question"]
        options = self.questions[index]["options"]
        return question, options

    def get_answer(self, index):
        """Devuelve la respuesta correcta para la pregunta en el índice dado."""
        return self.questions[index]["answer"]
