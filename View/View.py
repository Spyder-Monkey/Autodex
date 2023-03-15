"""
Filename    : View.py
Description :
"""
import tkinter as tk
from tkinter import ttk

from fileLogging import logger

import customtkinter as ctk
from PIL import Image
class View(ctk.CTk):

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title('Autodex')
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('green')

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2,3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # LEFT SIDE BAR FRAME
        self.sidebarFrame = ctk.CTkFrame(self, width=350, corner_radius=0)
        self.sidebarFrame.grid(row=0, column=0, rowspan=4, sticky='nsew')
        self.sidebarFrame.grid_rowconfigure(5, weight=2)

        # LEFT SIDE BAR FRAME BUTTONS
        self.homeButton = ctk.CTkButton(self.sidebarFrame, image=ctk.CTkImage(light_image=Image.open("./icons/icons8-home-24-black.png"), dark_image=Image.open("./icons/icons8-home-24-white.png"), size=(30, 30)), fg_color=("gray86", "gray17"), text="", width=75)
        self.homeButton.grid(row=0, column=0, padx=10, pady=(10, 10))

        self.searchButton = ctk.CTkButton(self.sidebarFrame, image=ctk.CTkImage(light_image=Image.open("./icons/icons8-search-24-black.png"), dark_image=Image.open("./icons/icons8-search-24.png"), size=(30, 30)), fg_color=("gray86", "gray17"), text="", width=75)
        self.searchButton.grid(row=1, column=0, padx=10, pady=10)

        self.notificationButton = ctk.CTkButton(self.sidebarFrame, image=ctk.CTkImage(light_image=Image.open("./icons/icons8-notification-24-black.png"), dark_image=Image.open("./icons/icons8-notification-24.png"), size=(30, 30)), fg_color=("gray86", "gray17"), text="", width=75)
        self.notificationButton.grid(row=2, column=0, padx=10, pady=10)

        self.settingsButton = ctk.CTkButton(self.sidebarFrame, image=ctk.CTkImage(light_image=Image.open("./icons/icons8-settings-24-black.png"), dark_image=Image.open("./icons/icons8-settings-24.png"), size=(30, 30)), fg_color=("gray86", "gray17"), text="", width=75)
        self.settingsButton.grid(row=3, column=0, padx=10, pady=10)

        self.profileButton = ctk.CTkButton(self.sidebarFrame, image=ctk.CTkImage(light_image=Image.open("./icons/icons8-name-24-black.png"), dark_image=Image.open("./icons/icons8-name-24.png"), size=(30, 30)), fg_color=("gray86", "gray17"), text="", width=75)
        self.profileButton.grid(row=4, column=0, padx=10, pady=10)

        self.addNewButton = ctk.CTkButton(self.sidebarFrame, image=ctk.CTkImage(light_image=Image.open("./icons/icons8-add-new-26-black.png"), dark_image=Image.open("./icons/icons8-add-new-26.png"), size=(30, 30)), fg_color=("gray86", "gray17"), text="", width=75)
        self.addNewButton.grid(row=6, column=0, padx=10, pady=20)

        self.searchBar = ctk.CTkEntry(self, width=300, placeholder_text="Search...")
        self.searchBar.grid(row=0, column=1, columnspan=3, padx=20, pady=15, sticky='n')



        """
            ICONS:
                * garage?
                * car
                * filter
        """


        # Set frame dimensions to the screen dimensions
        screenWidth = self.winfo_screenwidth()
        screenHeight = self.winfo_screenheight()
        self.geometry(f"{screenWidth}x{screenHeight}")

    def main(self):
        self.mainloop()


