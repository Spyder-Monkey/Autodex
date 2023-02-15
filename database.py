import os
import psycopg2
import boto3
from fileLogging import logger

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

def connect():
    logger().info('Connected to database')
    return psycopg2.connect(
        host = ENDPOINT,
        port = PORT,
        database = DBNAME,
        user = USER,
        password = PASS,
        sslrootcert = 'SSLCERTIFICATE'
    )
