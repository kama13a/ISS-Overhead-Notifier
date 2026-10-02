import os
from dotenv import load_dotenv
import requests
from datetime import datetime
import smtplib
import time

load_dotenv()


def check_and_notify():
    MY_LAT = 41.299496 # Your latitude
    MY_LONG = 69.240074 # Your longitude


    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])


    #Your position is within +5 or -5 degrees of the ISS position.


    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
        "tzid": "Asia/Tashkent",
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    hour = time_now.hour
    load_dotenv()


    my_email = os.environ["MY_EMAIL"]
    my_password = os.environ["MY_PASSWORD"]
    to_email = os.environ["TO_EMAIL"]




    #If the ISS is close to my current position
    if hour >= sunset or hour <= sunrise:
        dlon = abs(iss_longitude - MY_LONG)
        dlat = abs(iss_latitude - MY_LAT)
        if dlon <= 5 and dlat <= 5:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=my_password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=to_email,
                    msg = "Subject:Look up\n\nThe iss passing"
                )
                print("Email sent")
        else:
            print("ISS too far")
    else:
        print(f"Not dark. hour={hour}, sunset={sunset}, sunrise={sunrise}")
    # and it is currently dark
    # Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

if __name__ == "__main__":
    while True:
        try:
            check_and_notify()
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(60)
