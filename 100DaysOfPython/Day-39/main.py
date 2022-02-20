# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData

FD = FlightData()
DM = DataManager()
FS = FlightSearch()
sheet_data = DM.get_all_data()
sheet_data_prices = sheet_data["prices"]
for city in sheet_data_prices:
    FS.add_city(city)
# print(sheet_data_prices)
all_cities = FS.all_cities
# DM.update_data_sheet(all_cities)

FD.find_flight(all_cities)

# <script>document.getElementsByTagName("h1")[0].style.fontSize = "6vw"; </script>
# <style media="screen">
# body {
#   font-family: system-ui;
#   background: #f06d06;
#   color: white;
#   text-align: center;
#   }
# </style>
