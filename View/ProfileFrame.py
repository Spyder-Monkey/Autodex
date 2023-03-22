"""
Filename    : ProfileFrame.py
Description :
"""

import customtkinter as ctk

# Local Imports
from fileLogging import logger


class ProfileFrame(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master, corner_radius=5)

        self.label = ctk.CTkLabel(self, text="Profile")
        self.label.grid(row=0, column=0)