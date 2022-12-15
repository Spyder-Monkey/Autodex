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
import requests
from bs4 import BeautifulSoup

import Models.Engine as Engine
import Models.Recall as Recall

class Vehicle():
    def __init__(self, vin:str, miles:int=0):
        self.vin = vin
        self.data = self.__fetchVINData()
        self.make = self.data['Make']
        self.model = self.data['Model']
        self.year = self.data['ModelYear']
        self.trim = self.data['Trim']
        self.type = self.data['VehicleType']
        self.doors = self.data['Doors']
        # self.color = color
        self.miles = miles
        self.engine = Engine.Engine(self.data)
        self.recalls = self.__fetchRecallData()
        self.color = self.__fetchVehicleColor()

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

    def __fetchVehicleColor(self):
        import os
        from selenium import webdriver
        from selenium.webdriver.firefox.options import Options
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.common.keys import Keys

        # Get path to geckodriver executable        
        exePath = os.path.dirname(os.path.dirname(__file__))+"/geckodriver"

        # Set browser options
        options = Options()
        options.headless = True # Hide the GUI
        # Create a Firefox webdriver
        driver = webdriver.Firefox(executable_path=exePath, options=options)
        driver.get(f'https://www.vehiclehistory.com')
        # Find the search box on the web page
        searchBox = driver.find_element_by_css_selector('input[id="input-1"]')
        # Fill search box with vehicle VIN
        searchBox.send_keys(self.vin)
        # Press the enter key
        searchBox.send_keys(Keys.ENTER)
        # Wait for the div with class EquipmentDetails-item to load
        WebDriverWait(driver=driver, timeout=5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.EquipmentDetails-item'))
        )

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        # Exctract vehicle specs
        specs = soup.find('div', class_='VehicleSpecifications-section')
        titles = specs.find_all('div', class_='EquipmentDetails-title')
        values = specs.find_all('div', class_='EquipmentDetails-value')
        # Strip whitespace from strings and create a dictionary of title : value
        scrapedSpecs = {title.text.strip() : value.text.strip() for title, value in zip(titles, values)}

        print(scrapedSpecs)

        return scrapedSpecs

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

        print(recallList)


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
    :param color: Color of the vehicle
    """
    if len(vin) == 17 and findVehicle(vin) == -1:
        vehicleIndex.append(Vehicle(vin))
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


