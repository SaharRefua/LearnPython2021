import requests

parameters = {
    "lat": 32.178196,
    "lon": 34.907612,

    "appid": "77d7cc42e3cfea820d8476202fd44b81",
    "exclude": "current,minutely,daily",

}


response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)

response.raise_for_status()
if response.status_code == 200:
    print(response.json())