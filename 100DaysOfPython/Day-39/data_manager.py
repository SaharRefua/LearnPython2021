import requests
from pprint import pprint


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.get_all_data()

    def get_all_data(self):
        APP_ID = "6a98755a"
        API_KEY = "f842b33e07e1cab4c749a02d30cf566f"
        sheet_endpoint = "https://api.sheety.co/04049eba40c092db9ad7d0fe1086155f/flightDeals/prices"
        headers = {
            "x-app-id": APP_ID,
            "x-app-key": API_KEY,
        }

        response = requests.get(sheet_endpoint, headers=headers)
        result = response.json()
        # print(result)
        # pprint(result)
        return result

    def get_iataCode(self, city):
        sheet_endpoint = "https://tequila-api.kiwi.com/locations/query"
        headers = {
            "apikey": "MN5pjvEz_ca818O8M1J0-x36jU7G-F1-"
        }

        parameters = {

            "term": city["city"],
            "location_types": "city"

        }

        response = requests.get(sheet_endpoint, headers=headers, params=parameters)
        response.raise_for_status()
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def update_data_sheet(self, all_cities):
        APP_ID = "6a98755a"
        API_KEY = "f842b33e07e1cab4c749a02d30cf566f"
        sheet_endpoint = "https://api.sheety.co/04049eba40c092db9ad7d0fe1086155f/flightDeals/prices/"  # [Object ID]"
        headers = {
            "x-app-id": APP_ID,
            "x-app-key": API_KEY,
        }

        for city in all_cities:
            city["iataCode"] = self.get_iataCode(city)
            data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }

            response = requests.put(f"{sheet_endpoint}/{city['id']}", headers=headers, json=data)
            response.raise_for_status()
            result = response.json()
