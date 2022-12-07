"""
Author      : Trevor Bender
Filename    : cliController.py
Description : 
"""

import cmd2

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


    def do_addCar(self, arg):
        pass

    def do_editCar(self, arg):
        pass

    def do_deleteCar(self, arg):
        pass
    

