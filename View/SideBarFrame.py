"""
Filename    : SideBarFrame.py
Description : Contains the visuals for the side bar in the GUI
"""
import customtkinter as ctk
from PIL import Image

from fileLogging import logger
import View.SettingsFrame as SettingsFrame
import View.GarageFrame as GarageFrame

class SideBarFrame(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, width=350, corner_radius=5)
        logger().info(f"Creating side bar frame")
        self.grid(row=0, column=0, rowspan=4, padx=(10, 5), pady=10, sticky='nsew')

        self.grid_rowconfigure(5, weight=2)
        logger().info(f"Adding button icons")
        # Home Button
        self.homeButton = ctk.CTkButton(self, image=ctk.CTkImage(light_image=Image.open("./icons/icons8-home-24-black.png"), dark_image=Image.open("./icons/icons8-home-24-white.png"), size=(30, 30)), fg_color=("gray86", "gray17"), text="", width=75, hover_color="#F5D547", command=lambda: controller.showFrame(GarageFrame.GarageFrame))
        self.homeButton.grid(row=0, column=0, padx=10, pady=(10, 10))
        # Search Button
        self.searchButton = ctk.CTkButton(self, image=ctk.CTkImage(light_image=Image.open("./icons/icons8-search-24-black.png"), dark_image=Image.open("./icons/icons8-search-24.png"), size=(30, 30)), fg_color=("gray86", "gray17"), text="", width=75)
        self.searchButton.grid(row=1, column=0, padx=10, pady=10)
        # Notification Button
        self.notificationButton = ctk.CTkButton(self, image=ctk.CTkImage(light_image=Image.open("./icons/icons8-notification-24-black.png"), dark_image=Image.open("./icons/icons8-notification-24.png"), size=(30, 30)), fg_color=("gray86", "gray17"), text="", width=75)
        self.notificationButton.grid(row=2, column=0, padx=10, pady=10)
        # Settings Button
        self.settingsButton = ctk.CTkButton(self, image=ctk.CTkImage(light_image=Image.open("./icons/icons8-settings-24-black.png"), dark_image=Image.open("./icons/icons8-settings-24.png"), size=(30, 30)), fg_color=("gray86", "gray17"), text="", width=75, command=lambda: controller.showFrame(SettingsFrame.SettingsFrame))
        self.settingsButton.grid(row=3, column=0, padx=10, pady=10)
        # Profile Button
        self.profileButton = ctk.CTkButton(self, image=ctk.CTkImage(light_image=Image.open("./icons/icons8-name-24-black.png"), dark_image=Image.open("./icons/icons8-name-24.png"), size=(30, 30)), fg_color=("gray86", "gray17"), text="", width=75)
        self.profileButton.grid(row=4, column=0, padx=10, pady=10)
        # Add New Vehicle Button
        self.addNewButton = ctk.CTkButton(self, image=ctk.CTkImage(light_image=Image.open("./icons/icons8-add-new-26-black.png"), dark_image=Image.open("./icons/icons8-add-new-26.png"), size=(30, 30)), fg_color=("gray86", "gray17"), text="", width=75)
        self.addNewButton.grid(row=6, column=0, padx=10, pady=20)

        # Test logo icon
        # self.autoIcon = ctk.CTkButton(self, image=ctk.CTkImage(dark_image=Image.open("./icons/Method Draw Image(4).png"), size=(30, 30)), fg_color=("gray86", "gray17"), text="", width=75)
        # self.autoIcon.grid(row=7, column=0, padx=10, pady=20)

        logger().info(f"Successfully created side bar frame")

        