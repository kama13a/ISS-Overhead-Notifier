import requests
from datetime import datetime
MY_LAT = 41.313034
MY_LNG = 69.279648

parameters = {
    "lat":MY_LAT,
    "lng":MY_LNG,
    "formatted":0,
}


response = requests.get("https://api.sunrise-sunset.org/v2", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["sunset"].split("T")[1].split(":")[0])
