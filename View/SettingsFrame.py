"""
Filename    : SettingsFrame.py
Description :
"""

# local imports
from fileLogging import logger

import customtkinter as ctk

class SettingsFrame(ctk.CTkFrame):
    
    def __init__(self, master):
        super().__init__(master, corner_radius=5)
        self.grid(row=0, column=1, columnspan=2, rowspan=4, padx=(5, 10), pady=10, sticky='nsew')

        logger().info("Main View: Settings")

        self.appearance = ctk.StringVar(value=ctk.get_appearance_mode())


        self.label = ctk.CTkLabel(self, text="Settings")
        self.label.grid(row=0, column=0, padx=10, pady=10)

        self.appearanceToggle = ctk.CTkSwitch(self, variable=self.appearance, onvalue="Dark", offvalue="Light", command=self.toggleAppearance, text="")
        self.appearanceToggle.grid(row=1, column=0, padx=10, pady=10, sticky='w')

        """
            SETTINGS:
            * Dark/light mode
            * imperial -> metric
            * date format
            * 
        
        
        """

    def toggleAppearance(self):
        ctk.set_appearance_mode(self.appearance.get())
        logger().info(f"Changed appearance: {self.appearance.get()}")


