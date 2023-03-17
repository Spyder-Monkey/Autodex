"""
Filename    : View.py
Description : Main container file for the GUI view
"""
# Local imports
from fileLogging import logger
# View imports
import View.SideBarFrame as SideBarFrame

import customtkinter as ctk
class View(ctk.CTk):

    def __init__(self, controller):
        logger().info(f"Starting GUI")
        super().__init__()
        self.controller = controller
        self.title('Autodex')
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('green')

        logger().info(f"Appearance: {ctk.get_appearance_mode()}")
        # Creates a 4x4 grid layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2,3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # Left side bar frame
        self.sideBar = SideBarFrame.SideBarFrame(self)
        # Holds the toggle switch value for light/dark mode
        self.appearance = ctk.StringVar(value=ctk.get_appearance_mode())
        # Light/Dark mode toggle switch
        self.appearanceSwitch = ctk.CTkSwitch(self, text="Appearance", variable=self.appearance, onvalue="Dark", offvalue="Light", command=self.toggleAppearance)
        self.appearanceSwitch.grid(row=0, column=1, sticky='n')

        # Set frame dimensions to the screen dimensions
        screenWidth = self.winfo_screenwidth()
        screenHeight = self.winfo_screenheight()
        self.geometry(f"{screenWidth}x{screenHeight}")
        logger().info(f"Frame Width: {screenWidth}")
        logger().info(f"Frame Height: {screenHeight}")

        logger().info(f"Successfully started GUI")

    def toggleAppearance(self):
        """
        Used to change the appearance of the program
        """
        ctk.set_appearance_mode(self.appearance.get())
        logger().info(f"Appearance changed to {self.appearance.get()}")

    def main(self):
        self.mainloop()


