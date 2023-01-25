import psycopg2
import sys
import boto3
import os

ENDPOINT = "autodex.cbvteipevqwf.us-east-1.rds.amazonaws.com"
PORT = "5432"
USER = "tbends"
REGION = "us-east-1"
DBNAME = "Autodex"
os.environ['LIBMYSQL_ENABLE_CLEARTEXT_PLUGIN'] = '1'

session = boto3.Session(profile_name='default')
client = session.client('rds')

token = client.generate_db_auth_token(DBHostname=ENDPOINT, Port=PORT, DBUsername=USER, Region=REGION)

try:
    conn = psycopg2.connect(host=ENDPOINT, database=DBNAME, user=USER, password=token, ssl_ca='SSLCERTIFICATE')
    cur = conn.cursor()
    cur.execute("""SELECT now()""")
    query_results = cur.fetchall()
    print(query_results)
except Exception as e:
    print("Database connection failed due to {}".format(e))