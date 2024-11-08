from controllers.data_manager import save_new_entry

class EutrofizacionCalculator:
    def __init__(self, nitrogen, phosphorus, oxygen, location):
        self.nitrogen = nitrogen
        self.phosphorus = phosphorus
        self.oxygen = oxygen
        self.location = location  # Ubicación para guardar en los datos

    def calcular(self):
        # Fórmula simple para ilustrar el concepto
        indice_eutrofizacion = (self.nitrogen + self.phosphorus) / self.oxygen
        # Guarda el cálculo en el archivo CSV
        save_new_entry(self.location, self.nitrogen, self.phosphorus, self.oxygen)
        return indice_eutrofizacion

