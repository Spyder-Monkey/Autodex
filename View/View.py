"""
Filename    : View.py
Description :
"""
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

# from MainFrame import MainFrame
from View.MainFrame import MainFrame
class View(ctk.CTk):

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title('Autodex')
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('blue')

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=2)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)
        # FRAMES
        self.inputFrame = ctk.CTkFrame(self)
        # self.inputFrame.pack(anchor=ctk.W)
        self.garageFrame = ctk.CTkFrame(self)
        # self.garageFrame.pack(anchor=ctk.NE, ipadx=10, ipady=10)
        self.outputFrame = ctk.CTkFrame(self)
        # self.outputFrame.pack(anchor=ctk.S)
        # LABELS
        self.label = ctk.CTkLabel(master=self.inputFrame, text="AUTODEX")
        # self.label.pack()
        self.garageLabel = ctk.CTkLabel(master=self.garageFrame, text="GARAGE", justify=ctk.LEFT)
        # self.garageLabel.pack()
        self.outputLabel = ctk.CTkLabel(master=self.outputFrame, text="OUTPUT", justify=ctk.LEFT)
        # self.outputLabel.pack()
        
        self.emptyLabel = ctk.CTkLabel(master=self.inputFrame)

        self.tabs = self.tabView()
        # self.tabs.enable_traversal()
        # self.tabs.pack()

        # Set frame dimensions to the screen dimensions
        screenWidth = self.winfo_screenwidth()
        screenHeight = self.winfo_screenheight()
        self.geometry(f"{screenWidth}x{screenHeight}")

        self.widgetGrid()

    def main(self):
        self.mainloop()
    
    def widgetGrid(self):
        sticky = {"sticky":"nswe"}
        
        self.inputFrame.grid(row=0, column=0, sticky='nsew', rowspan=2, columnspan=1)
        self.inputFrame.rowconfigure(0, weight=1)
        # self.inputFrame.rowconfigure(1, weight=2)
        # self.inputFrame.columnconfigure(0, weight=2)
        self.inputFrame.columnconfigure(1, weight=1)

        self.garageFrame.grid(row=0, column=1, sticky='nsew', rowspan=1, columnspan=3)

        self.outputFrame.grid(row=1, column=1, sticky='nsew', rowspan=1, columnspan=3)

        # self.label.grid(row=0, column=0, sticky='n')
        self.garageLabel.grid(row=0, column=0, sticky='w')
        self.outputLabel.grid(row=0, column=0, sticky='w')

        self.tabs.grid(row=0, column=0, sticky='nsew', rowspan=2, columnspan=2)

    def tabView(self):
        tab = ctk.CTkTabview(master=self.inputFrame)
        tab.add("Garage")
        tab.add("Search")
        tab.add("Add")

        return tab


