from tkinter import Tk
from views.main_view import MainView

if __name__ == "__main__":
    root = Tk()  # Esta es la única instancia de Tk
    root.title("Aplicación de Eutrofización")
    root.geometry("600x400")  # Establecemos un tamaño más grande
    root.resizable(True, True)  # Hacemos la ventana redimensionable

    app = MainView(root)
    root.mainloop()  # Ejecutamos el bucle principal

