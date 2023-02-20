"""
Filename    : guiController.py
Description :
"""
import tkinter as tk
from tkinter import ttk

# Local imports
import database as db

def GUI():
    root = tk.Tk()
    frame = ttk.Frame(root, padding=10)
    frame.grid()
    ttk.Label(frame, text="Frame Testing").grid(column=0, row=0)
    ttk.Button(frame, text="Quit", command=root.destroy).grid(column=1, row=0)
    root.mainloop()
