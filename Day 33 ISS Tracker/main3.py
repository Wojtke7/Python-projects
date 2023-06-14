import requests
from datetime import datetime
import smtplib
import time

testing_mail = "wojciechmarcela7@gmail.com"
testing_password = "rxttlfneryuuujiw"

MY_LAT = 50.184820
MY_LONG = 19.482790
FORMAT = 0


def check_pos():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    print(f"Iss longitude :{iss_longitude}\nIss latitude: {iss_latitude}\nMy long: {MY_LONG}\nMy lat:{MY_LAT}" )

    if abs(MY_LAT - iss_latitude) <= 5 and abs(MY_LONG - iss_longitude) <= 5:
        return True
    else:
        return False


def check_daytime():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": FORMAT,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()
    curr_hour = time_now.hour

    print(f"Sunrise: {sunrise}, sunset: {sunset}\nCurr hour: {curr_hour}")

    if sunset <= curr_hour <= 24:
        return True
    elif 0 <= curr_hour <= sunrise:
        return True
    else:
        return False


while True:
    if check_pos() and check_daytime():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=testing_mail, password=testing_password)
            connection.sendmail(from_addr=testing_mail, to_addrs="madridistazduszy@gmail.com",
                                msg=f"Subject:Hey you!\n\n "
                                    f"Look up!")
    time.sleep(60)

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
