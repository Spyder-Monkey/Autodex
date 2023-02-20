"""
Filename    : cliController.py
Description : 
"""

import pyfiglet
import sys
import cmd2
from pick import pick
import boto3
import os
from dotenv import load_dotenv

# Local Imports
import Models.Vehicle as Vehicle
import Models.Interface as Interface
from fileLogging import logger

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
        logger().info('Program Startup')
        del cmd2.Cmd.do_edit
        del cmd2.Cmd.do_history
        del cmd2.Cmd.do_macro
        del cmd2.Cmd.do_set
        del cmd2.Cmd.do_shell
        del cmd2.Cmd.do_shortcuts
        logger().info('Removed builtin commands')

    addVehicleParser = cmd2.Cmd2ArgumentParser(description="Add a new vehicle")
    addVehicleParser.add_argument('vin', help="Vehicle Identification Number (17 characters)")
    addVehicleParser.add_argument('miles', nargs=(0,1), type=int, help="Number of miles vehicle has driven")
    @cmd2.with_argparser(addVehicleParser)
    def do_addVehicle(self, arg):
        """
        Add a vehicle object
        """
        if len(arg.vin) != 17:
            logger().error('VIN should be 17 characters long')
            print("VIN should be 17 characters long")
            return
        
        Vehicle.addVehicle(arg.vin)

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

    def do_listEngines(self, _):
        """
        List all engines
        """
        Interface.listEngines()

    def do_listMakes(self, _):
        """
        List all makes stored in database
        """
        Interface.listMakes()

    listModelsParser = cmd2.Cmd2ArgumentParser(description="")
    listModelsParser.add_argument('make', help="Make to list all models of")
    @cmd2.with_argparser(listModelsParser)
    def do_listModels(self, arg):
        """
        List all models from the specified make
        """
        Interface.listModels(arg.make)

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
        logger().info("Exit Program")
        sys.exit()

