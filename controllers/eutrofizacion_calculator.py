class EutrofizacionCalculator:
    def __init__(self, nitrogen, phosphorus, oxygen):
        self.nitrogen = nitrogen
        self.phosphorus = phosphorus
        self.oxygen = oxygen

    def calcular(self):
        # Fórmula simple para ilustrar el concepto
        indice_eutrofizacion = (self.nitrogen + self.phosphorus) / self.oxygen
        return indice_eutrofizacion
