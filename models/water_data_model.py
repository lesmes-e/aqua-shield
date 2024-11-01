class WaterData:
    def __init__(self, nitrogen, phosphorus, oxygen):
        self.nitrogen = nitrogen
        self.phosphorus = phosphorus
        self.oxygen = oxygen

    def __repr__(self):
        return f"Nitrogen: {self.nitrogen}, Phosphorus: {self.phosphorus}, Oxygen: {self.oxygen}"
