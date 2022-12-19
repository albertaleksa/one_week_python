import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 30.267153
MY_LONG = -97.743057
PLACEHOLDER = "[NAME]"
MY_EMAIL = "albert.aleksa.by@gmail.com"
MY_PASSWORD = "cxmvdmkzhurxlakm"


def get_iss_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_position = (iss_latitude, iss_longitude)

    return iss_position


def is_iss_close_to_me():
    iss_position = get_iss_position()
    print(iss_position)
    if MY_LAT - 5 < iss_position[0] < MY_LAT + 5 and MY_LONG - 5 < iss_position[1] < MY_LONG + 5:
        return True
    return False


def is_night():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()

    data = response.json()
    sunrise_hour = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) - 6
    sunset_hour = int(data["results"]["sunset"].split("T")[1].split(":")[0]) - 6

    time_now_hour = datetime.now().hour

    if time_now_hour >= sunset_hour or time_now_hour <= sunrise_hour:
        return True
    return False


def send_email():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up\n\nThe ISS is above you in the sky."
        )


if __name__ == '__main__':
    while True:
        time.sleep(60)
        if is_iss_close_to_me() and is_night():
            send_email()
