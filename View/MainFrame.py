from tkinter import ttk
from tkinter.messagebox import showinfo

class MainFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container, height=500)

        options = {'padx':10, 'pady':10}

        self.autodexLabel = ttk.Label(self, text="Autodex", foreground='#DB5461', font=('Arial', 36))
        self.autodexLabel.grid(row=0, column=0, sticky="nw", **options)

        self.label = ttk.Label(self, text="hello")
        self.label.grid(row=0, column=0)

        self.addVehicle = ttk.Button(self, text="Add Vehicle")
        self.addVehicle['command'] = self.buttonClicked
        # self.addVehicle.pack(**options)
        self.addVehicle.grid(row=5, column=0)

        self.testLabel = ttk.Label(self, text="TEST LABEL")
        self.testLabel.grid(row=3, column=0)

        # self.pack(**options)

    def buttonClicked(self):
        showinfo(title="Information", message="ADDED")