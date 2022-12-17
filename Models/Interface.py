"""
Filename    : Interface.py
Description : Functions for commands involving the interface
"""

import Models.Vehicle as Vehicle
from prettytable import PrettyTable, SINGLE_BORDER

def listVehicles():
    if len(Vehicle.vehicleIndex) > 0:
        table = PrettyTable()
        table.set_style(SINGLE_BORDER)
        table.field_names = ["VIN", "Year", "Make", "Model", "Trim", "Color", "Miles", "Engine Model", "Recalls"]
        for vehicle in Vehicle.vehicleIndex:
           
            table.add_row([vehicle.vin, vehicle.year, vehicle.make, vehicle.model, vehicle.trim, vehicle.color, vehicle.miles, vehicle.engine.model, len(vehicle.recalls)])
        print(table)
    else:
        print(f'\nNo vehicles have been added')

def listVehicle(vehicle : Vehicle):
    """
    List the contents of a specific vehicle

    :param vehicle: target Vehicle object
    """

    table = PrettyTable(header=False)
    table.set_style(SINGLE_BORDER)
    table.add_column("", ["Make", "Model", "Year", "Trim", "Color", "Miles"])
    table.add_column("", [vehicle.make, vehicle.model, vehicle.year, vehicle.trim, vehicle.color, vehicle.miles])

    print(table)

def listRecalls(vehicle : Vehicle):
    if len(vehicle.recalls) > 0:
        table = PrettyTable()
        table.set_style(SINGLE_BORDER)
        table.title = vehicle
        table.field_names = ["Date", "Campaign", "Component", "Consequence"]

        for recall in vehicle.recalls:
            table.add_row([recall.reportReceiveDate, recall.campaignNum, recall.component, recall.consequence])
        print(table)