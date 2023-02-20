"""
Filename    : Vehicle.py
Description : Model of Vehicle objects and their associated methods
"""

import json
import requests

import Models.Engine as Engine
import Models.Recall as Recall
import database as db
from fileLogging import logger

class Vehicle():
    def __init__(self, vin:str):
        self.vin = vin.upper()
        if len(self.vin) != 17:
            return
        self.data = self.__fetchVINData()
        if self.data['ErrorCode'] == "0":
            self.make = self.data['MakeID']
            self.model = self.data['ModelID']
            self.year = int(self.data['ModelYear'])
            self.body = self.data['BodyClass']
            self.trim = self.data['Trim']
            self.doors = self.data['Doors']
            self.engine = Engine.Engine(self.data)
        else:
            logger().error(f'Invalid VIN:{self.vin}')
            print("VIN error")

    def __repr__(self) -> str:
        return f"{self.year} {self.make} {self.model} {self.trim} [{self.vin[-6:]}]"

    def __fetchVINData(self):
        """
            Uses the Department of Transportation's API to get the information of a vehicles VIN

            https://vpic.nhtsa.dot.gov/api/


            :returns: Dictionary of data associated with a VIN
        """
        # URL to pull VIN info from
        URL = 'https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVINValuesBatch/'
        # Information used to pull information
        post_field = {'format': 'json', 'data':self.vin}
        # Pull vehicle information
        r = requests.post(URL, data=post_field)
        # Convert str to json
        vehicleData = json.loads(r.text)

        return vehicleData['Results'][0]

    def __fetchRecallData(self):
        """
        Uses the Department of Transportation's Recall API to search for current recalls on vehicle
        https://www.nhtsa.gov/nhtsa-datasets-and-apis
        
        :returns: A list of dictionaries if a recall exists
        """
        URL = f"https://api.nhtsa.gov/recalls/recallsByVehicle?make={self.make}&model={self.model}&modelYear={self.year}"
        # URL = "https://api.nhtsa.gov/recalls/recallsByVehicle?make=acura&model=rdx&modelYear=2012"
        response = requests.get(URL)

        data = json.loads(response.text)['results']
        recallList = []
        for dat in data:
            recallList.append(Recall.Recall(dat))

        return recallList

def addVehicle(vin: str):
    """
    Adds a new vehicle to vehicleIndex if the vin does not already exist

    :param vin: VIN of the vehicle to be added
    """
    try:
        conn = db.connect()
        cur = conn.cursor()
        conn.autocommit = True

        newVehicle = Vehicle(vin)

        cur.execute(f"""INSERT INTO body (type)
                            select '{newVehicle.body}'
                            WHERE
                            NOT EXISTS (SELECT type FROM body WHERE type='{newVehicle.body}')""")
        logger().info(f'Body:{cur.statusmessage}')

        cur.execute(f"""INSERT INTO vehicle 
                    SELECT '{newVehicle.vin}', {newVehicle.year}, {newVehicle.make}, {newVehicle.model}, (SELECT id FROM body WHERE type='{newVehicle.body}'), (SELECT id FROM engine WHERE model='{newVehicle.engine.model}')
                    WHERE
                    NOT EXISTS (SELECT vin FROM vehicle WHERE vin='{newVehicle.vin}')""")
        logger().info(f'[{vin}]:{cur.statusmessage}')
        print(f"\nAdded vehicle [{vin}]")

    except Exception as e:
        logger().exception('')
        print(f"Failed to connect to database: {e}")


    """
        * VIN already exists
        * VIN is too short
        * VIN is too long
        * VIN is invalid
    """


