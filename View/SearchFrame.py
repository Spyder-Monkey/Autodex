"""
Filename    : SearchFrame.py
Description : 
"""

import customtkinter as ctk

class SearchFrame(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master, corner_radius=5)

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2,3), weight=0)
        self.grid_rowconfigure((0,1,2), weight=1)

        # Search Bar
        self.searchBar = ctk.CTkEntry(self, placeholder_text='Search by VIN', height=50, font=ctk.CTkFont(size=16), corner_radius=5)
        self.searchBar.grid(row=0, column=0, padx=10, pady=10, columnspan=2, sticky='new')
        # Search Button
        self.searchButton = ctk.CTkButton(self, text='Search', command=lambda: self.searchForVehicle(self.searchBar.get()), height=50, font=ctk.CTkFont(size=16), corner_radius=5)
        self.searchButton.grid(row=0, column=3, padx=10, pady=10, sticky='new')

    def searchForVehicle(self, value):
        """
        Searches for the vehicle

        :param value: either the vin, make and/or model of a vehicle

        :return: True if one or more results were found, otherwise False
        """
        label = ctk.CTkLabel(self, text=value)
        label.grid(row=1, column=0)

        return True