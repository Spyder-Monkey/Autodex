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
    if len(Vehicle.vehicleIndex) > 0:
        table = PrettyTable()
        table.set_style(SINGLE_BORDER)
        table.field_names = ["VIN", "Year", "Make", "Model", "Trim", "Color", "Miles", "Engine Model", "Recalls"]
        for vehicle in Vehicle.vehicleIndex:
           
            table.add_row([vehicle.vin, vehicle.year, vehicle.make, vehicle.model, vehicle.trim, vehicle.color, vehicle.miles, vehicle.engine.model, len(vehicle.recalls)])
        print(table)
    else:
        print(f'\nNo vehicles have been added')

def listVehicle(vin : str):
    """
    List the contents of a specific vehicle

    :param vehicle: target Vehicle object
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

        cur.execute(f"""SELECT * FROM vehicle WHERE vin='{vin}'""")
        results = cur.fetchone()
        
        table = PrettyTable(header=False)
        table.set_style(SINGLE_BORDER)
        table.add_column("", ["Make", "Model", "Year", "Color", "Body", "Engine"])
        table.add_column("", [results[3], results[4], results[1], results[2], results[5], results[6]])
        print(table)
    except Exception as e:
        print("Connection failed due to: {}".format(e))

    # table = PrettyTable(header=False)
    # table.set_style(SINGLE_BORDER)
    # table.add_column("", ["Make", "Model", "Year", "Trim", "Color", "Miles"])
    # table.add_column("", [vehicle.make, vehicle.model, vehicle.year, vehicle.trim, vehicle.color, vehicle.miles])

    # print(table)

def listRecalls(vehicle : Vehicle):
    if len(vehicle.recalls) > 0:
        table = PrettyTable()
        table.set_style(SINGLE_BORDER)
        table.title = vehicle
        table.field_names = ["Date", "Campaign", "Component", "Consequence"]

        for recall in vehicle.recalls:
            table.add_row([recall.reportReceiveDate, recall.campaignNum, recall.component, recall.consequence])
        print(table)