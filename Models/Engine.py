"""
Filename    : Engine.py
Description :
"""

from fileLogging import logger
import database as db
class Engine():

    def __init__(self, data):
        self.model = data['EngineModel']
        self.configuration = data['EngineConfiguration']
        self.horsePower = data['EngineHP']
        self.cylinders = data['EngineCylinders']
        self.displacementL = data['DisplacementL']
        self.driveType = data['DriveType']
        self.fuelType = data['FuelTypePrimary']

        try:
            conn = db.connect()
            conn.autocommit = True
            cur = conn.cursor()
            # Add engine to DB
            cur.execute(f"""INSERT INTO engine (model, horsepower, displacement, cylinders, configuration, drive_type, fuel_type)
                        SELECT '{self.model}', {self.horsePower}, {self.displacementL}, {self.cylinders}, '{self.configuration}', '{self.driveType}', '{self.fuelType}'
                        WHERE 
                        NOT EXISTS (SELECT model FROM engine WHERE model = '{self.model}')""")
            # print(f"Engine {self.model}: {cur.statusmessage}")
            logger().info(f'[{self.model}]:{cur.statusmessage}')
        except Exception as e:
            logger().exception('')
            print(f"Could not connect to the database")

    def __repr__(self) -> str:
        return f"{self.model}"