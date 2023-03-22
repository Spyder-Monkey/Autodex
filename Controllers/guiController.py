"""
Filename    : guiController.py
Description : Controller for the GUI view
"""

# Local imports
from fileLogging import logger
# View Imports
from View.View import View
import View.SettingsFrame as SettingsFrame
import View.GarageFrame as GarageFrame
import View.ProfileFrame as ProfileFrame
import View.SearchFrame as SearchFrame

class Controller:

    def __init__(self):
        self.view = View(self)
        # Dictionary of individual frames
        self.frames = {}

        # Initialize each frame for easy switching between
        for F in (GarageFrame.GarageFrame, SettingsFrame.SettingsFrame, ProfileFrame.ProfileFrame, SearchFrame.SearchFrame):
            frame = F(self.view)

            self.frames[F] = frame

            frame.grid(row=0, column=1, columnspan=2, rowspan=4, padx=(5, 10), pady=10, sticky='nsew')

        self.showFrame(GarageFrame.GarageFrame)

    def showFrame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def main(self):
        self.view.main()
