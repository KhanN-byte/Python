'''

Weather Application 

Haris Khan

Uses OpenWeatherMapAPI

api_url = https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

'''

import argparse
import json
import sys
from pprint import pp
from configparser import ConfigParser
from urllib import parse, request, error

BASE_WEATHERAPI_URL = "http://api.openweathermap.org/data/2.5/weather"

def _get_api_key():
  """
      [openweather]
      api_key=<YOUR-OPENWEATHER-API-KEY>
  """
  config = ConfigParser()
  config.read("secrets.ini")
  return config["openweather"]["api_key"]
  

def get_userInput():
  
    parser = argparse.ArgumentParser(
        description="gets weather and temperature information for a city."
    )

    parser.add_argument(
        "city", nargs="+", type=str, help="enter the city name"
         #nargs="+" allow you to pass in a city name more then one word.
    )

    parser.add_argument(
        "-i",
        "--imperial",
        action = "store_true",
        help = "display the temperature in imperial units",
    )
    return parser.parse_args()

def create_WeatherCall(city_input, imperial=False):
    """
    Builds the URL for an API request to OpenWeather's weather API.

    Args:
        city_input (List[str]): Name of a city as collected by argparse
        imperial (bool): Whether or not to use imperial units for temperature

    Returns:
        str: URL formatted for a call to OpenWeather's city name endpoint
    """

    api_key = _get_api_key()
    city_name = " ".join(city_input)
    url_encoded_cityname = parse.quote_plus(city_name)
  
    if imperial:
      units = "imperial"
    else:
      units = "metric"
      
    url = (
      f"{BASE_WEATHERAPI_URL}?q={url_encoded_cityname}"
      f"&units={units}&appid={api_key}"
    )

    return url

def get_weather_json(url):
  """
      Makes an API request to a URL and returns the data as a Python object.

  Args:
      url (str): URL formatted for OpenWeather's city name endpoint

  Returns:
      dict: Weather information for a specific city
  """

  try:
    response = request.urlopen(url)
  except error.HTTPError as err:
    if err.code == 401: #unauthorized
        sys.exit("Access Denied. Check your API Key.")
    elif err.code == 404: # not found
      sys.exit("Can't find weather data for this city.")
    else: 
      sys.exit(f"Something went awry... ({err.code})")
      
  data = response.read()

  try:
    return json.loads(data)
  except json.JSONDecodeError:
    sys.exit("Server Error!")
    
  
if __name__ == "__main__":
  
    #get_userInput()
    user_input = get_userInput()
    queryUrl = create_WeatherCall(user_input.city, user_input.imperial)
    #print(user_input.city, user_input.imperial)
    #print(queryUrl)

    result = get_weather_json(queryUrl)
    pp(result)
    print("\n ====== Print just the section which shows the temperatures =====\n ")
    pp(result['main'])
  

