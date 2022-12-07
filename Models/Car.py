"""
    * VIN
    * Color
    * Make
    * Model
    * Year
    * Trim
    * Options (Object)
    * MaintHistory??? (Object)
    * User Manual????
    * Milage
    * Owners
    * AccidentHistory (Object)
"""


import json

class Car():
    # Check if vin is valid
    def __init__(self, vin:str):
        self.vin = vin
        self.data = self.__fetchData()
        self.make = self.data['Make']
        self.model = self.data['Model']
        self.year = self.data['ModelYear']
        self.trim = self.data['Trim']
        self.type = self.data['VehicleType']
        self.doors = self.data['Doors']

    def __fetchData(self):
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


if __name__=="__main__":
    car = Car("19XFL2H87NE023121")

    


