import requests
import os
from dotenv import load_dotenv

load_dotenv(override=True)
API_KEY = os.environ['OPEN_WEATHER_API_KEY']


URL = "https://api.openweathermap.org/data/2.8/onecall"

parameters = {
    "lat": 30.264980,
    "lon": -97.746597,
    "exclude": "current,minutely,daily",
    "appid": API_KEY
}

response = requests.get(url=URL, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
conditions = [int(hour_data["weather"][0]["id"]) for hour_data in weather_slice]

for condition in conditions:
    if condition < 700:
        print("Bring unmrella!")
        break
