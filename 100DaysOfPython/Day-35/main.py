import requests
# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ.get("OWM_API_KEY")
auth_token = os.environ.get("token")

print(account_sid, auth_token)
parameters = {
    "lat": 32.178196,
    "lon": 34.907612,
    "appid": "77d7cc42e3cfea820d8476202fd44b81",
    "exclude": "current,minutely,daily",
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
if response.status_code == 200:
    data = response.json()
    weather = data['hourly']
    x = 0
    while x < 12:
        hourly_weather = weather[x]["weather"]
        weather_id = hourly_weather[0]["id"]
        print(weather_id)
        if weather_id < 700:
            print("Bring an umbrella.")
            client = Client(account_sid, auth_token)

            message = client.messages \
                .create(
                body="It's going to rain today. Remember to bring an umbrella.",
                from_='+19034851279',
                to='+9720524879755'
                # to='+972523692124'
            )
            print(message.status)
            break
        x += 1
