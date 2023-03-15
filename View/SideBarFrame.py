"""
Filename    : SideBarFrame.py
Description : Contains the visuals for the side bar in the GUI
"""
import customtkinter as ctk
from PIL import Image

class SideBarFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=350, corner_radius=0)
        self.grid(row=0, column=0, rowspan=4, sticky='nsew')

        self.grid_rowconfigure(5, weight=2)

        # Home Button
        self.homeButton = ctk.CTkButton(self, image=ctk.CTkImage(light_image=Image.open("./icons/icons8-home-24-black.png"), dark_image=Image.open("./icons/icons8-home-24-white.png"), size=(30, 30)), fg_color=("gray86", "gray17"), text="", width=75)
        self.homeButton.grid(row=0, column=0, padx=10, pady=(10, 10))
        # Search Button
        self.searchButton = ctk.CTkButton(self, image=ctk.CTkImage(light_image=Image.open("./icons/icons8-search-24-black.png"), dark_image=Image.open("./icons/icons8-search-24.png"), size=(30, 30)), fg_color=("gray86", "gray17"), text="", width=75)
        self.searchButton.grid(row=1, column=0, padx=10, pady=10)
        # Notification Button
        self.notificationButton = ctk.CTkButton(self, image=ctk.CTkImage(light_image=Image.open("./icons/icons8-notification-24-black.png"), dark_image=Image.open("./icons/icons8-notification-24.png"), size=(30, 30)), fg_color=("gray86", "gray17"), text="", width=75)
        self.notificationButton.grid(row=2, column=0, padx=10, pady=10)
        # Settings Button
        self.settingsButton = ctk.CTkButton(self, image=ctk.CTkImage(light_image=Image.open("./icons/icons8-settings-24-black.png"), dark_image=Image.open("./icons/icons8-settings-24.png"), size=(30, 30)), fg_color=("gray86", "gray17"), text="", width=75)
        self.settingsButton.grid(row=3, column=0, padx=10, pady=10)
        # Profile Button
        self.profileButton = ctk.CTkButton(self, image=ctk.CTkImage(light_image=Image.open("./icons/icons8-name-24-black.png"), dark_image=Image.open("./icons/icons8-name-24.png"), size=(30, 30)), fg_color=("gray86", "gray17"), text="", width=75)
        self.profileButton.grid(row=4, column=0, padx=10, pady=10)
        # Add New Vehicle Button
        self.addNewButton = ctk.CTkButton(self, image=ctk.CTkImage(light_image=Image.open("./icons/icons8-add-new-26-black.png"), dark_image=Image.open("./icons/icons8-add-new-26.png"), size=(30, 30)), fg_color=("gray86", "gray17"), text="", width=75)
        self.addNewButton.grid(row=6, column=0, padx=10, pady=20)