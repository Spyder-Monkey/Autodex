"""
Filename    : autodex.py
Description : Main driver code for the AutoDex program
"""

import sys

import Controllers.cliController as cliController
import Controllers.guiController as guiController

def run():
    if len(sys.argv) == 2 and sys.argv[1] == '--cli':
        cliController.cliController().cmdloop()
    else:
        guiController.GUI()
        
if __name__=="__main__":
    run()