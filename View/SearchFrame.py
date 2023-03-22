"""
Filename    : SearchFrame.py
Description : 
"""

import customtkinter as ctk

class SearchFrame(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master, corner_radius=5)

        self.label = ctk.CTkLabel(self, text="Search")
        self.label.grid(row=0, column=0)