import requests

# # ISS location !
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# print(response.status_code)
# print(response.json())
# longitude = response["iss_position"]["longitude"]
# latitude = response["iss_position"]["latitude"]
# iss_position = (longitude, latitude)
# print(iss_position)
Latitude = 40.760204
Longitude = -73.984421

parameters = {
    "lat": Latitude,
    "lng": Longitude,
    "formatted": 0,
}
response = requests.get("https://api.sunrise-sunset.org/json?", params=parameters)
response.raise_for_status()
response.raise_for_status()
data = response.json()
print(data)
sunrise = data["results"]["sunrise"]
print(sunrise)


