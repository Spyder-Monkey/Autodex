"""
Filename    : Engine.py
Description :
"""
class Engine():
    def __init__(self, data):
        self.manufacturer = data['EngineManufacturer']
        self.model = data["EngineModel"]
        self.configuration = data['EngineConfiguration']
        self.fuelType = data['FuelTypePrimary']
        self.cycles = data['EngineCycles']
        self.cylinders = data['EngineCylinders']
        self.horsePower = data['EngineHP']
        self.displacementCC = data['DisplacementCC']
        self.displacementCI = data['DisplacementCI']
        self.displacementL = data['DisplacementL']
        self.kilowatts = data['EngineKW']

    def __repr__(self) -> str:
        return f"{self.manufacturer} {self.model}"