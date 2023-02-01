"""
Filename    : Engine.py
Description :
"""

import psycopg2
import boto3
import os
from dotenv import load_dotenv

load_dotenv('secrets.env')

ENDPOINT = os.getenv('ENDPOINT')
PORT = os.getenv('PORT')
USER = os.getenv('DBUSER')
PASS = os.getenv('DBPASS')
REGION = os.getenv('REGION')
DBNAME = os.getenv('DBNAME')

session = boto3.Session(profile_name="default")
client = session.client('rds')
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

        try:
            conn = psycopg2.connect(
                host=ENDPOINT, 
                port=PORT, 
                database=DBNAME,
                user=USER, 
                password=PASS, 
                sslrootcert='SSLCERTIFICATE'
            )
            conn.autocommit = True
            cur = conn.cursor()
            # Add engine to DB
            cur.execute(f"""INSERT INTO engine (model, horsepower, displacement, cylinders, configuration, drive_type, fuel_type)
                        SELECT %s, %s, %s, %s, %s, %s, %s
                        WHERE 
                        NOT EXISTS (SELECT model FROM engine WHERE model = %s)""", 
                        (self.model, self.horsePower, self.displacementL, self.cylinders, self.configuration, self.driveType, self.fuelType, self.model))
        except Exception as e:
            print(f"Connection failed due to: {e}")

    def __repr__(self) -> str:
        return f"{self.model}"