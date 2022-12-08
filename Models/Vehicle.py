"""
    * VIN
    * Color
    * Options (Object)
    * MaintHistory??? (Object)
    * User Manual????
    * Milage
    * Owners
    * AccidentHistory (Object)
"""

from typing import List
import json

class Vehicle():
    def __init__(self, vin:str):
        self.vin = vin
        self.data = self.__fetchVINData()
        self.make = self.data['Make']
        self.model = self.data['Model']
        self.year = self.data['ModelYear']
        self.trim = self.data['Trim']
        self.type = self.data['VehicleType']
        self.doors = self.data['Doors']

    def __repr__(self) -> str:
        return f"{self.year} {self.make} {self.model} {self.trim} [{self.vin[-6:]}]"

    def __fetchVINData(self):
        """
            Uses the Department of Transportation's API to get the information of a vehicles VIN
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

def findVehicle(vin : str):
    for i, v in enumerate(vehicleIndex):
        if v.vin == vin:
            return i
    return -1

def addVehicle(vin : str):
    if findVehicle(vin) == -1:
        vehicleIndex.append(Vehicle(vin))
    else:
        print(f"\n{vin} already exists")


def deleteVehicle(vin : str):
    index = findVehicle(vin)
    if index > -1:
        vehicleIndex.pop(index)
    else:
        print(f'\n{vin} does not exist')

def editVehicle():
    """
    
    """
    from pick import pick
    # Get user selection of the vehicle to be changed
    title = "Choose a vehicle to edit: "
    vehicleOption, index = pick(vehicleIndex, title, indicator='>>')
    # Get user selection of what to change
    options = ['VIN', 'Make', 'Model', 'Year', 'Color']
    editOption, index = pick(options, "What would you like to change?", indicator='>>')

    if editOption is 'VIN':
        pass
    elif(editOption is 'Make'):
        pass
    elif editOption is 'Model':
        pass
    elif editOption is 'Year':
        pass
    elif editOption is 'Color':
        pass

    print(vehicleOption, editOption)

vehicleIndex : List[Vehicle] = []


