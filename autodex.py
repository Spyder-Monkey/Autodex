"""
Filename    : autodex.py
Description : Main driver code for the AutoDex program
"""

import sys
# Local Imports
import Controllers.cliController as cliController
from Controllers.guiController import Controller

def run():
    if len(sys.argv) == 2 and sys.argv[1] == '--cli':
        cliController.cliController().cmdloop()
    else:
        Controller().main()

if __name__=="__main__":
    run()