"""
Filename    : Vehicle.py
Description : Model of Vehicle objects and their associated methods
"""

from typing import List
import json
import requests
from bs4 import BeautifulSoup

import Models.Engine as Engine
import Models.Recall as Recall
import database as db

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

            try:
                conn = db.connect()
                conn.autocommit = True
                cur = conn.cursor()

                # Add body type to DB
                cur.execute(f"""INSERT INTO body (type)
                            select '{self.body}'
                            WHERE
                            NOT EXISTS (SELECT type FROM body WHERE type='{self.body}')""")

                # Add vehicle to DB                
                cur.execute(f"""INSERT INTO vehicle 
                            SELECT '{self.vin}', {self.year}, 'Black', {self.make}, {self.model}, (SELECT id FROM body WHERE type='{self.body}'), (SELECT id FROM engine WHERE model='{self.engine.model}')
                            WHERE
                            NOT EXISTS (SELECT vin FROM vehicle WHERE vin='{self.vin}')""")
                
                ##### PREVENTS SQL INJECTION ATTACKS https://www.psycopg.org/psycopg3/docs/basic/params.html
                # cur.execute(f"""SELECT (username, password) FROM users WHERE username=%s and password=%s""", (user, paswd))
                # results = cur.fetchall()
                # print(results)

            except Exception as e:
                print("Connection failed: {}".format(e))
        else:
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

def findVehicle(vin : str):
    """
        Searches vehicleIndex for the vin.

        :param vin: VIN to be searched for in vehicleIndex
        :returns: The index of the vehicle in vehicleIndex, otherwise -1
    """
    for i, v in enumerate(vehicleIndex):
        if v.vin == vin:
            return i
    return -1

def addVehicle(vin : str):
    """
    Adds a new vehicle to vehicleIndex if the vin does not already exist

    :param vin: VIN of the vehicle to be added
    """
    if len(vin) == 17 and findVehicle(vin) == -1:
        newVehicle = Vehicle(vin)
        vehicleIndex.append(newVehicle)

        print(f"\nAdded {newVehicle}")
    elif len(vin) != 17:
        print(f"\nVIN must be 17 characters long")
    else:
        print(f"\n{vin} already exists")


def deleteVehicle(vin : str):
    """
    Removes the vehicle with vin from vehicleIndex if it exists

    :param vin: VIN of the target vehicle
    """
    index = findVehicle(vin)
    if index > -1:
        vehicleIndex.pop(index)
    else:
        print(f'\n{vin} does not exist')

def editVehicle(vehicle : Vehicle, editOption : str):
    """
    Changes the value of a vehicle

    :param vehicle: The target vehicle
    :param editOption: What aspect to change
    """

    if editOption == 'Miles':
        vehicle.miles = input("(New miles)>> ")
    elif editOption == 'Color':
        vehicle.color = input("(New color)>> ")

#####################################################################################

vehicleIndex : List[Vehicle] = []


