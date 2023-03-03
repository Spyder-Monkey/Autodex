"""
Filename    : guiController.py
Description :
"""

# Local imports
import database as db
from View.View import View

class Controller:

    def __init__(self):
        self.view = View(self)

    def main(self):
        self.view.main()