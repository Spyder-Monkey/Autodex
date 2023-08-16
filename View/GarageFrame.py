"""
Filename    : GarageFrame.py
Description : 
"""
# Local imports
from fileLogging import logger
import View.VehicleTile as VehicleTile
# Imports
import customtkinter as ctk

class GarageFrame(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master, corner_radius=5)
        self.grid_columnconfigure((0,1,2,3), weight=1)
        self.grid_rowconfigure((0,1), weight=1)
        logger().info("Main View: Garage")


        self.tile = VehicleTile.VehicleTile(self)
        self.tile.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

        self.tileTwo = VehicleTile.VehicleTile(self)
        self.tileTwo.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')

        self.tileThree = VehicleTile.VehicleTile(self)
        self.tileThree.grid(row=0, column=2, padx=10, pady=10, sticky='nsew')

        self.tileFour = VehicleTile.VehicleTile(self)
        self.tileFour.grid(row=0, column=3, padx=10, pady=10, sticky='nsew')

        self.tileFive = VehicleTile.VehicleTile(self)
        self.tileFive.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

