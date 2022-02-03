import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 32.178196
MY_LONG = 34.907612
tolerance = 20


def send_email():
    my_email = "Test@gmail.com"
    password = "My_password"
    adders = "Test@gmail.com"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # secure the connection
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=adders,
                            msg=f"Subject:Lookup\n\n.")

    print("The mail was sent ........")


def check_iss_location():
    print("Checking.....")
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    print(f"Your current location: MY_LAT:{MY_LAT} , MY_LONG:{MY_LONG}")
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    print(f"Iss location: iss_latitude:{iss_latitude} , iss_longitude:{iss_longitude}")
    # Your position is within +5 or -5 degrees of the ISS position.

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = str(datetime.now()) # Or str(datetime.now().hour)
    current_hour = time_now.split(" ")[1].split(":")[0]

    if MY_LAT - tolerance <= iss_latitude <= MY_LAT + tolerance and MY_LONG - tolerance <= iss_longitude <= MY_LONG + tolerance:
        if int(current_hour) >= int(sunset):
            print("Send a mail ..... ")
            send_email()
        else:
            print("Still day time")
    else:
        print("The ISS location is far from your location !")


while True:
    check_iss_location()
    print("Wait 60 seconds = (")
    time.sleep(60)
# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
