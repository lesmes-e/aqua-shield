from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QMainWindow
import pandas as pd

class HistoryView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Historial de Calidad de Agua")
        self.setGeometry(200, 200, 600, 400)
        
        # Creación del QTableWidget donde mostrarás los datos
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(50, 50, 500, 300)  # Ajusta la geometría de la tabla
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(["Fecha", "Ubicación", "Nutrientes", "Crecimiento de Algas", "Oxígeno"])
        
        self.load_history()  # Cargar los datos del historial en la tabla

    def load_history(self):
        try:
            df = pd.read_csv("data/water_quality_data.csv")
            if df.empty:
                print("El archivo CSV está vacío.")
                return

            # Limpia la tabla antes de agregar nuevos datos
            self.tableWidget.setRowCount(0)

            # Cargar los datos en la tabla
            for index, row in df.iterrows():
                rowPosition = self.tableWidget.rowCount()
                self.tableWidget.insertRow(rowPosition)

                self.tableWidget.setItem(rowPosition, 0, QTableWidgetItem(row['date']))
                self.tableWidget.setItem(rowPosition, 1, QTableWidgetItem(row['location']))
                self.tableWidget.setItem(rowPosition, 2, QTableWidgetItem(str(row['nutrient_level'])))
                self.tableWidget.setItem(rowPosition, 3, QTableWidgetItem(str(row['algae_growth'])))
                self.tableWidget.setItem(rowPosition, 4, QTableWidgetItem(str(row['oxygen_level'])))

        except pd.errors.EmptyDataError:
            print("No hay datos en el archivo CSV.")
        except FileNotFoundError:
            print("Archivo no encontrado.")
