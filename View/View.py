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
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)

        # self.frame = MainFrame(self)
        self.inputFrame = ctk.CTkFrame(self)

        self.label = ctk.CTkLabel(master=self.inputFrame, text="AUTODEX", justify=ctk.LEFT)

        self.progress = ctk.CTkProgressBar(master=self.inputFrame)

        # Set frame dimensions to the screen dimensions
        screenWidth = self.winfo_screenwidth()
        screenHeight = self.winfo_screenheight()
        self.geometry(f"{screenWidth}x{screenHeight}")

        self.outputFrame = ctk.CTkFrame(self)
        self.outputLabel = ctk.CTkLabel(master=self.outputFrame, text="OUTPUT", justify=ctk.LEFT)

        self.switch = ctk.CTkSwitch(master=self.outputFrame)

        # self.style = self.widgetStyles()

        self.widgetGrid()

    def main(self):
        self.mainloop()
    
    def widgetGrid(self):
        sticky = {"sticky":"nswe"}
        
        self.inputFrame.grid(row=0, column=0, sticky='nsew', rowspan=2, columnspan=1)
        self.inputFrame.rowconfigure(0, weight=1)
        self.inputFrame.columnconfigure(1, weight=1)

        self.outputFrame.grid(row=0, column=1, sticky='nsew', rowspan=2, columnspan=3)

        self.progress.grid(row=0, column=1)
        self.label.grid(row=0, column=0, sticky='nw')

        self.outputLabel.grid(row=0, column=0, sticky='w')
        self.switch.grid(row=0, column=1)

    def widgetStyles(self) -> ttk.Style:
        theme = ttk.Style(self)
        # FRAME
        theme.configure('TFrame', background='#FAFAFA')
        # NOTEBOOK
        theme.configure('TNotebook', background='#686963')
        # BUTTON
        theme.configure('TButton', background='#904E55', foreground='#FAFAFA')
        theme.map('TButton', background=[('active', '#DB5461')])
        # LABEL
        theme.configure('TLabel', background='#FAFAFA', foreground='#686963')
        return theme

    """
    File menu
    """
    def createMenu(self):
        menubar = tk.Menu(self, background='#564E58', foreground="#E3F2FD")
        # File Menu
        fileMenu = tk.Menu(menubar, tearoff=0)
        fileMenu.add_command(label="Open", command=None)
        fileMenu.add_command(label="Print", command=None)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=fileMenu)
        # Edit Menu
        editMenu = tk.Menu(menubar, tearoff=0)
        editMenu.add_command(label="Undo", command=None)
        editMenu.add_command(label="Redo", command=None)
        editMenu.add_separator()
        editMenu.add_command(label="Find", command=None)
        menubar.add_cascade(label="Edit", menu=editMenu)
        # Help Menu

        self.config(menu=menubar)


