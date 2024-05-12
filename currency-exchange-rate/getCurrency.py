"""
Haris Khan

Develop Currency-Exchange Python Code 

ExchangeRatesAPI

API Documentation: https://www.exchangerate-api.com/docs/standard-requests

"""

import json
import sys
from pprint import pp 
from urllib import error, request

api_key = '4b5d2a592355fd7ace6c31a1'
base_url = 'https://v6.exchangerate-api.com/v6/'

countryCode = input("Country currency to look at: \n")

exchangerateAPI = f"{base_url}{api_key}/latest/{countryCode}"

try:
  response = request.urlopen(exchangerateAPI)
except error.HTTPError as err:
  if err.code == 401: #unauthorized
      sys.exit("Access Denied. Check your API Key.")
  elif err.code == 404: # not found
    sys.exit("Can't find currency data for this country.")
  else: 
    sys.exit(f"Something went awry... ({err.code})")

data = response.read()

try:
  pp(json.loads(data))
except json.JSONDecodeError:
  sys.exit("Server Error!")