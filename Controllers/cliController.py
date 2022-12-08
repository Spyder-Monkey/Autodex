"""
Author      : Trevor Bender
Filename    : cliController.py
Description : 
"""

import cmd2

# Local Imports
import Models.Vehicle as Vehicle

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

    """
        * addCar
        * editCar
        * deleteCar
        
        * 
    """

    addVehicleParser = cmd2.Cmd2ArgumentParser(description="Add a new vehicle")
    addVehicleParser.add_argument('vin', help="Vehicle Identification Number")
    @cmd2.with_argparser(addVehicleParser)
    def do_addVehicle(self, arg):
        Vehicle.addVehicle(arg.vin)

    def do_editVehicle(self, arg):
        Vehicle.editVehicle()

    def do_deleteVehicle(self, arg):
        pass
    

    def do_exit(self, _):
        exit()

