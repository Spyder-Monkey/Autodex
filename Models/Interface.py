"""
Filename    : Interface.py
Description : Functions for commands involving the interface
"""

import Models.Vehicle as Vehicle
import database as db
from prettytable import PrettyTable, SINGLE_BORDER

def listVehicles():
    try:
        conn = db.connect()
        cur = conn.cursor()
        # Get vehicle and engine info
        cur.execute("""SELECT vehicle.vin, vehicle.year, model.model_name, make.make_name, body.type, engine.model, engine.horsepower
                    FROM vehicle
                    JOIN model ON vehicle.model_id = model.id
                    JOIN make ON vehicle.make_id = make.id
                    JOIN body ON vehicle.body_id = body.id
                    JOIN engine ON vehicle.engine_id = engine.id""")
        
        results = cur.fetchall()
        # Create table for output
        table = PrettyTable()
        table.set_style(SINGLE_BORDER)
        table.field_names = ["VIN", "Year", "Make", "Model", "Body", "Engine Model", "Horsepower"]
        # Add the rows to the table
        for row in results:
            table.add_row([row[0], row[1], row[3], row[2], row[4], row[5], row[6]])

        print(table)
    except Exception as e:
        print(f"Connection failed due to: {e}")

def listVehicle(vin : str):
    """
    List the contents of a specific vehicle

    :param vin: VIN of the target vehicle
    """

    try:
        conn = db.connect()
        cur = conn.cursor()

        cur.execute(f"""SELECT vehicle.vin, vehicle.year, model.model_name, make.make_name, body.type, engine.model, engine.horsepower 
                        FROM vehicle 
                        JOIN model ON vehicle.model_id = model.id 
                        JOIN make ON vehicle.make_id = make.id
                        JOIN body ON vehicle.body_id = body.id 
                        JOIN engine ON vehicle.engine_id = engine.id 
                        WHERE vin='{vin}'""")

        results = cur.fetchone()
        table = PrettyTable()
        table.title = results[0]
        table.set_style(SINGLE_BORDER)
        table.field_names = ["Make", "Model", "Year", "Body", "Engine", "Horsepower"]
        table.add_row([results[3], results[2], results[1], results[4], results[5], results[6]])
        print(table)
        
    except Exception as e:
        print("Connection failed due to: {}".format(e))

def listEngine(vin : str):
    try:
        conn = db.connect()
        cur = conn.cursor()

        cur.execute(f"""SELECT engine.model, engine.horsepower, engine.displacement, engine.cylinders, engine.configuration, engine.drive_type, engine.fuel_type
                    FROM engine 
                    WHERE engine.id = (SELECT vehicle.engine_id FROM vehicle WHERE vin='{vin}')""")
        
        results = cur.fetchone()

        table = PrettyTable()
        table.set_style(SINGLE_BORDER)
        table.title = vin.upper() + " ENGINE"
        table.field_names = ["Model", "Horsepower", "Displacement (L)", "Cylinders", "Configuration", "Drive Type", "Fuel"]
        table.add_row([results[0], results[1], results[2], results[3], results[4], results[5], results[6]])
        print(table)

    except Exception as e:
        print(f"Failed to connect: {e}")

def listEngines():
    try:
        conn = db.connect()
        cur = conn.cursor()

        cur.execute(f"""SELECT model, horsepower, displacement, cylinders, configuration, drive_type FROM engine""")
        results = cur.fetchall()

        table = PrettyTable()
        table.title = "ENGINES"
        table.set_style(SINGLE_BORDER)
        table.field_names = ["Model", "Horsepower", "Displacement (L)", "Cylinders", "Config", "Drive"]

        for result in results:
            table.add_row([result[0], result[1], result[2], result[3], result[4], result[5]])
        print(table)
    except Exception as e:
        print(f"Failed to connect due to: {e}")

def listMakes():
    try:
        conn = db.connect()
        cur = conn.cursor()

        cur.execute("""SELECT * FROM make""")
        results = cur.fetchall()

        table = PrettyTable()
        table.set_style(SINGLE_BORDER)
        table.title = "ALL MAKES"
        table.field_names = ["ID", "Make"]

        for result in results:
            table.add_row([result[0], result[1]])

        print(table)
    except Exception as e:
        print(f"Failed to connect to database: {e}")

def listModels(make : str):
    try:
        conn = db.connect()
        cur = conn.cursor()
        # Query to get the model id and name for the specified make
        cur.execute(f"""SELECT id, model_name FROM model WHERE make_name='{make.upper()}'""")
        results = cur.fetchall()
        # Create a table for output
        table = PrettyTable()
        table.set_style(SINGLE_BORDER)
        table.title = make.upper()
        table.field_names = ["Model ID", "Model"]
        # Add all models to table
        for result in results:
            table.add_row([result[0], result[1]])

        print(table)
    except Exception as e:
        print(f"Failed to connect to database: {e}")

def listRecalls(vehicle : Vehicle):
    if len(vehicle.recalls) > 0:
        table = PrettyTable()
        table.set_style(SINGLE_BORDER)
        table.title = vehicle
        table.field_names = ["Date", "Campaign", "Component", "Consequence"]

        for recall in vehicle.recalls:
            table.add_row([recall.reportReceiveDate, recall.campaignNum, recall.component, recall.consequence])
        print(table)