"""
Filename    : Vehicle.py
Description : Model of Vehicle objects and their associated methods
"""


"""
    * Options (Object)
    * MaintHistory??? (Object)
    * User Manual????
    * Owners
    * AccidentHistory (Object)
"""

from typing import List
import json

import Models.Engine as Engine

class Vehicle():
    def __init__(self, vin:str, color:str, miles:int=0):
        self.vin = vin
        self.data = self.__fetchVINData()
        self.make = self.data['Make']
        self.model = self.data['Model']
        self.year = self.data['ModelYear']
        self.trim = self.data['Trim']
        self.type = self.data['VehicleType']
        self.doors = self.data['Doors']
        self.color = color
        self.miles = miles
        self.engine = Engine.Engine(self.data)
        self.recalls = self.__fetchRecallData()

    def __repr__(self) -> str:
        return f"{self.year} {self.make} {self.model} {self.trim} [{self.vin[-6:]}]"

    def __fetchVINData(self):
        """
            Uses the Department of Transportation's API to get the information of a vehicles VIN

            :returns: Dictionary of data associated with a VIN
        """
        import requests
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

        :returns: A list of dictionaries if a recall exists
        """
        import requests
        URL = f"https://api.nhtsa.gov/recalls/recallsByVehicle?make={self.make}&model={self.model}&modelYear={self.year}"
        # post_field = {'format':'json', 'make':self.make, 'model':self.model, 'modelYear':self.year}
        response = requests.get(URL)

        print(json.loads(response.text)['results'])

        return  json.loads(response.text)['results']

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

def addVehicle(vin : str, color : str):
    """
    Adds a new vehicle to vehicleIndex if the vin does not already exist

    :param vin: VIN of the vehicle to be added
    :param color: Color of the vehicle
    """
    if len(vin) == 17 and findVehicle(vin) == -1:
        vehicleIndex.append(Vehicle(vin, color))
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

def searchForRecalls(vehicle : Vehicle):
    pass

#####################################################################################

vehicleIndex : List[Vehicle] = []


