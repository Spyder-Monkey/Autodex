"""
Filename    : Engine.py
Description :
"""
class Engine():
    # def __init__(self, data):
    #     self.manufacturer = data['Engine Manufacturer']
    #     self.name = data['Engine Name']
    #     self.model = data["Engine Model"]
    #     self.configuration = data['Engine Configuration']
    #     self.fuelType = data['Fuel Type - Primary']
    #     self.cycles = data['Engine Stroke Cycles']
    #     self.cylinders = data['Engine Number of Cylinders']
    #     self.horsePower = data['Engine Brake (hp) From']
    #     self.displacementCC = data['Displacement (CC)']
    #     self.displacementCI = data['Displacement (CI)']
    #     self.displacementL = data['Displacement (L)']
    #     self.kilowatts = data['Engine Power (kW)']

    def __init__(self, data):
        self.model = data['EngineModel']
        self.configuration = data['EngineConfiguration']
        self.horsePower = data['EngineHP']
        self.cylinders = data['EngineCylinders']
        self.displacementL = data['DisplacementL']
        self.driveType = data['DriveType']
        self.fuelType = data['FuelTypePrimary']

    def __repr__(self) -> str:
        return f"{self.model}"