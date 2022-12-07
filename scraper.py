import requests
import json


# Vin lookup
# https://vpic.nhtsa.dot.gov/decoder/Decoder

# <a class="btn btn-default" href="/decoder/Decoder/ExportToExcel?VIN=19XFL2H87NE023121">Export to Excel</a>

URL = 'https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVINValuesBatch/'

post_field = {'format': 'json', 'data':'19XFL2H87NE023121'}

r = requests.post(URL, data=post_field)

print(r.text)

