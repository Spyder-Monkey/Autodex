"""
Filename    : autodex.py
Description : Main driver code for the AutoDex program
"""

import Controllers.cliController as cliController

def run():
    cliController.cliController().cmdloop()

if __name__=="__main__":
    run()