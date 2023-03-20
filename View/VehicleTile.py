"""
Filename    : VehicleTile.py
Description : Class for creating a tile for a vehicle object
"""

# Local imports
from fileLogging import logger
# Imports
import customtkinter as ctk
from PIL import Image

class VehicleTile(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master, width=600, height=650, corner_radius=5)
        self.grid_columnconfigure((0,1), weight=1)
        self.grid_columnconfigure((2,3), weight=0)
        self.grid_rowconfigure((0,1,2,3), weight=1)

        # Vehicle Image Frame
        self.imageFrame = ctk.CTkFrame(self)
        self.imageFrame.grid(row=0, column=0, columnspan=4, rowspan=1, sticky='new', padx=5, pady=(5,0))

        # Vehicle thumbnail
        self.civic = ctk.CTkImage(dark_image=Image.open("./civicHatch.png"), light_image=Image.open("./civicHatch.png"), size=(340, 250))

        self.image = ctk.CTkLabel(self.imageFrame, image=self.civic, text="")
        self.image.grid(row=0, column=0)

        # Vehicle Name Label
        self.vehicleLabel = ctk.CTkLabel(self, text="<Year> <Make> <Model> <Trim>", font=ctk.CTkFont(size=20, weight="bold"))
        self.vehicleLabel.grid(row=1, column=0, columnspan=2, padx=5, pady=0, sticky='new')
        """ Quick Info Labels """
        # Miles label
        self.milesLabel = ctk.CTkLabel(self, text="Miles: 999999", font=ctk.CTkFont(size=18))
        self.milesLabel.grid(row=2, column=0, padx=5, pady=0, sticky='new')
        # Recall Label
        self.recallLabel = ctk.CTkLabel(self, text="Recalls: 9999", font=ctk.CTkFont(size=18))
        self.recallLabel.grid(row=2, column=1, padx=5, pady=0, sticky='new')
        # Last Oil Change Label
        self.oilChangeLabel = ctk.CTkLabel(self, text="Last Oil Change: 12/12/9999", font=ctk.CTkFont(size=18))
        self.oilChangeLabel.grid(row=3, column=0, columnspan=2, sticky='new', padx=5, pady=0)

        logger().info(f"Added vehicle card")

