import Models.Vehicle as Vehicle
from prettytable import PrettyTable

def listVehicles():
    if len(Vehicle.vehicleIndex) > 0:
        table = PrettyTable()
        table.field_names = ["Year", "Make", "Model", "Trim", "Color", "Miles", "VIN"]
        for vehicle in Vehicle.vehicleIndex:
           
            table.add_row([vehicle.year, vehicle.make, vehicle.model, vehicle.trim, vehicle.color, vehicle.miles, vehicle.vin[-6:]])
        print(table)
    else:
        print(f'\nNo vehicles have been added')

def listVehicle(vehicle : Vehicle):
    """
    List the contents of a specific vehicle

    :param vin: VIN of the target vehicle
    """

    


    print("Vehicle:\n")
    print(f"\tMake: {vehicle.make}")
    print(f"\tModel: {vehicle.model}")
    print(f"\tYear: {vehicle.year}")
    print(f"\tTrim: {vehicle.trim}")
    print(f"\tColor: {vehicle.color}")
    print(f"\tMiles: {vehicle.miles}")