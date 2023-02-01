"""
Filename    : Interface.py
Description : Functions for commands involving the interface
"""

import Models.Vehicle as Vehicle
from prettytable import PrettyTable, SINGLE_BORDER
# PSQL connection
import psycopg2
import boto3
import os

from dotenv import load_dotenv

load_dotenv('secrets.env')

ENDPOINT = os.getenv('ENDPOINT')
PORT = os.getenv('PORT')
USER = os.getenv('DBUSER')
PASS = os.getenv('DBPASS')
REGION = os.getenv('REGION')
DBNAME = os.getenv('DBNAME')

session = boto3.Session(profile_name="default")
client = session.client('rds')

def listVehicles():
    try:
        conn = psycopg2.connect(
            host = ENDPOINT,
            port = PORT,
            database = DBNAME,
            user = USER,
            password = PASS,
            sslrootcert = 'SSLCERTIFICATE'
        )
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
        conn = psycopg2.connect(
            host=ENDPOINT,
            port=PORT,
            database=DBNAME,
            user=USER,
            password=PASS,
            sslrootcert='SSLCERTIFICATE'
        )
        cur = conn.cursor()

        cur.execute(f"""SELECT vehicle.vin, vehicle.year, model.model_name, make.make_name, body.type, engine.model, engine.horsepower 
                        FROM vehicle 
                        JOIN model ON vehicle.model_id = model.id 
                        JOIN make ON vehicle.make_id = make.id
                        JOIN body ON vehicle.body_id = body.id 
                        JOIN engine ON vehicle.engine_id = engine.id 
                        WHERE vin=%s""", (vin))

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
        conn = psycopg2.connect(
            host=ENDPOINT,
            port=PORT,
            database=DBNAME,
            user=USER,
            password=PASS,
            sslrootcert='SSLCERTIFICATE'
        )
        cur = conn.cursor()

        cur.execute(f"""SELECT engine.model, engine.horsepower, engine.displacement, engine.cylinders, engine.configuration, engine.drive_type, engine.fuel_type
                    FROM engine 
                    WHERE engine.id = (SELECT vehicle.engine_id FROM vehicle WHERE vin=%s)""", (vin))
        
        results = cur.fetchone()

        table = PrettyTable()
        table.set_style(SINGLE_BORDER)
        table.field_names = ["Model", "Horsepower", "Displacement (L)", "Cylinders", "Configuration", "Drive Type", "Fuel"]
        table.add_row([results[0], results[1], results[2], results[3], results[4], results[5], results[6]])
        print(table)

    except Exception as e:
        print(f"Failed to connect: {e}")

def listRecalls(vehicle : Vehicle):
    if len(vehicle.recalls) > 0:
        table = PrettyTable()
        table.set_style(SINGLE_BORDER)
        table.title = vehicle
        table.field_names = ["Date", "Campaign", "Component", "Consequence"]

        for recall in vehicle.recalls:
            table.add_row([recall.reportReceiveDate, recall.campaignNum, recall.component, recall.consequence])
        print(table)