"""
Filename    : GarageFrame.py
Description : 
"""
# Local imports
from fileLogging import logger

import View.VehicleTile as VehicleTile

import customtkinter as ctk



class GarageFrame(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master, corner_radius=5)
        self.grid(row=0, column=1, columnspan=2, rowspan=4, padx=(5, 10), pady=10, sticky='nsew')
        self.grid_columnconfigure((0,1,2,3), weight=1)
        # self.grid_columnconfigure((2,3), weight=0)
        self.grid_rowconfigure((0,1), weight=1)

        # self.testFrame = ctk.CTkFrame(master, corner_radius=5)
        # self.testFrame.grid(row=0, column=4, rowspan=4, padx=(5, 10), pady=10, sticky='nsew')


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

        # Vehicle info Heading label
        # self.header = ctk.CTkLabel(self, text="<Vehicle>", font=('Terminal', 25))
        # self.header.grid(row=0, column=0, padx=10, pady=10, sticky='nw')
        # # Vehicle image frame
        # self.vehicleImageFrame = ctk.CTkFrame(self, width=250, height=250, corner_radius=0)
        # self.vehicleImageFrame.grid(row=1, column=0, padx=10, pady=10, sticky='ne')

