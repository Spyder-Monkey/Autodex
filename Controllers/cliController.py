"""
Filename    : cliController.py
Description : 
"""

import pyfiglet
import sys
import cmd2
from pick import pick

# Local Imports
import Models.Vehicle as Vehicle
import Models.Interface as Interface

_intro_text = """\
{}
Type `help` for an overview `help <command>` for more details.
Type `exit` to quit.
"""

class cliController(cmd2.Cmd):
    intro = _intro_text.format("AutoDex")
    prompt = ">> "

    def __init__(self):
        super().__init__(allow_cli_args=False)

    addVehicleParser = cmd2.Cmd2ArgumentParser(description="Add a new vehicle")
    addVehicleParser.add_argument('vin', help="Vehicle Identification Number (17 characters)")
    @cmd2.with_argparser(addVehicleParser)
    def do_addVehicle(self, arg):
        Vehicle.addVehicle(arg.vin)

    def do_editVehicle(self, _):
        vehicleOption, _ = pick(Vehicle.vehicleIndex, "Select a vehicle to edit:", indicator=">> ")
        editOption, _ = pick(['Miles', 'Color'], "What would you like to change?", indicator=">> ")
        Vehicle.editVehicle(vehicleOption, editOption)

    def do_deleteVehicle(self, arg):
        pass

    def do_listVehicles(self, _):
        Interface.listVehicles()

    def do_listVehicle(self, _):
        option, _ = pick(Vehicle.vehicleIndex, "Select a vehicle:", indicator=">> ")
        Interface.listVehicle(option)

    def do_listRecall(self, _):
        option, _ = pick(Vehicle.vehicleIndex, "Select a vehicle:", indicator=">> ")
        Interface.listRecalls(option)
    

    def do_exit(self, _):
        sys.exit()

