"""
Filename    : View.py
Description :
"""
# Local imports
from fileLogging import logger
import View.SideBarFrame as SideBarFrame

import customtkinter as ctk
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

        # Left side bar frame
        self.sideBar = SideBarFrame.SideBarFrame(self)

        # Set frame dimensions to the screen dimensions
        screenWidth = self.winfo_screenwidth()
        screenHeight = self.winfo_screenheight()
        self.geometry(f"{screenWidth}x{screenHeight}")

    def main(self):
        self.mainloop()


