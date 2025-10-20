"""
This will be an application that will remind the user to get up from their chair to move around, get some exercise in, or go have some food or simply take a break from the screens. 

"""

import schedule
import time
from plyer import notification
import requests


# --- CONFIG ---

LUNCH_TIME = "20:52"
WEATHER_API_KEY = "http://api.openweathermap.org/data/2.5/weather"
LOCATION = "LONGMONT, US"
WALK_THRESHOLD_TMP = 55 # Fahrenheit, weather must be above this temp for walk

# ---- FUNCTIONS ----

def stand_up():
    notification.notify(
        title = "Time to Stand Up",
        message = "Take a short break and stretch your legs!",
        timeout=10
    )


def lunch_break():

    notification.notify(
        title = "Lunch Break",
        message = "Time for some lunch, Take a proper break and refuel",
        timeout = 10
    )

def check_weather_and_walk():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={LOCATION}&appid={WEATHER_API_KEY}&units=imperial"
    response = requests.get(url).json()
    temp = response['main']['temp']
    weather_desc = response['weather'][0]['description']

    if temp >= WALK_THRESHOLD_TEMP and "rain" not in weather_desc.lower():
        notification.notify(
            title="Go for a Walk!",
            message=f"The weather is nice ({temp}°F, {weather_desc}). Time to get some fresh air!",
            timeout=10
        )
    else:
        print(f"Weather not ideal for a walk: {temp}°F, {weather_desc}")

# ---- SCHEDULE TASKS ----

schedule.every(1).hours.do(stand_up)
schedule.every().day.at(LUNCH_TIME).do(lunch_break)
schedule.every(6).hours.do(check_weather_and_walk)

# --- RUN LOOP ---

while True:
    schedule.run_pending()
    time.sleep(30)

