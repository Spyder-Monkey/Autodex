"""
Filename    : cliController.py
Description : 
"""

import pyfiglet
import sys
import cmd2
from pick import pick
import psycopg2
import boto3
import os
from dotenv import load_dotenv

# Local Imports
import Models.Vehicle as Vehicle
import Models.Interface as Interface

_intro_text = """\
{}
Type `help` for an overview `help <command>` for more details.
Type `exit` to quit.
"""

load_dotenv('secrets.env')

ENDPOINT = os.getenv('ENDPOINT')
PORT = os.getenv('PORT')
USER = os.getenv('DBUSER')
REGION = os.getenv('REGION')
DBNAME = os.getenv('DBNAME')

session = boto3.Session(profile_name="default")
client = session.client('rds')



class cliController(cmd2.Cmd):
    intro = _intro_text.format(pyfiglet.figlet_format("AutoDex"))
    prompt = ">> "

    def __init__(self):
        super().__init__(allow_cli_args=False)

    addVehicleParser = cmd2.Cmd2ArgumentParser(description="Add a new vehicle")
    addVehicleParser.add_argument('vin', help="Vehicle Identification Number (17 characters)")
    addVehicleParser.add_argument('miles', nargs=(0,1), type=int, help="Number of miles vehicle has driven")
    @cmd2.with_argparser(addVehicleParser)
    def do_addVehicle(self, arg):
        """
        Add a vehicle object
        """
        if len(arg.vin) != 17:
            print("VIN should be 17 characters long")
            return

        # if arg.miles:
        #     Vehicle.addVehicle(arg.vin, arg.miles)
        # else:
        
        Vehicle.addVehicle(arg.vin)

    def do_editVehicle(self, _):
        """
        Change a value of a vehicle object
        """
        vehicleOption, _ = pick(Vehicle.vehicleIndex, "Select a vehicle to edit:", indicator=">> ")
        editOption, _ = pick(['Miles', 'Color'], "What would you like to change?", indicator=">> ")
        Vehicle.editVehicle(vehicleOption, editOption)

    def do_deleteVehicle(self, _):
        """
        Remove a vehicle object
        """
        option, _ = pick(Vehicle.vehicleIndex, "Select a vehicle to delete:", indicator=">> ")
        Vehicle.deleteVehicle(option)

    def do_listVehicles(self, _):
        """
        List ALL vehicles
        """
        Interface.listVehicles()

    listVehicleParser = cmd2.Cmd2ArgumentParser(description="")
    listVehicleParser.add_argument('vin', help="Vehicle Identification Number (17) characters long")
    @cmd2.with_argparser(listVehicleParser)
    def do_listVehicle(self, arg):
        """
        List the specs of a specific vehicle
        """
        # option, _ = pick(Vehicle.vehicleIndex, "Select a vehicle:", indicator=">> ")
        Interface.listVehicle(arg.vin)

    @cmd2.with_argparser(listVehicleParser)
    def do_listEngine(self, arg):
        """
        List the engine specs of a specific vin
        """
        Interface.listEngine(arg.vin)

    def do_listMakes(self, _):
        """
        List all makes stored in database
        """
        Interface.listMakes()

    def do_listRecall(self, _):
        """
        List all recalls (past and present) on a vehicle
        """
        option, _ = pick(Vehicle.vehicleIndex, "Select a vehicle:", indicator=">> ")
        Interface.listRecalls(option)
    

    def do_exit(self, _):
        """
        Exit the program
        """
        sys.exit()

