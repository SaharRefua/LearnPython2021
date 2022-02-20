import requests, datetime


class FlightData:
    def __init__(self):
        self.today = datetime.date.today()
        self.tomorrow = self.today + datetime.timedelta(days=1)
        self.start_date = self.tomorrow.strftime("%d/%m/%Y")  # dd/mm/YYYY
        self.date_to = self.tomorrow + datetime.timedelta(days=60)
        self.date_to = self.date_to.strftime("%d/%m/%Y")
        # This class is responsible for structuring the flight data.

    def find_flight(self, all_cities):
        sheet_endpoint = "https://tequila-api.kiwi.com/v2/search"
        header = {
            'apikey': "MN5pjvEz_ca818O8M1J0-x36jU7G-F1-"
        }

        for city in all_cities:
            parameters = {
                "fly_from": "LLBG",
                "fly_to": city["city"],
                "date_from": str(self.start_date),
                "date_to": str(self.date_to),
                "price_to": city["lowestPrice"],
                "nights_in_dst_from": 7,
                "nights_in_dst_to": 28,
                "flight_type": "round",
                "one_for_city": 1,
                "max_stopovers": 0

            }
            #"curr": "USD",
            response = requests.get(sheet_endpoint, headers=header, params=parameters)
            try:
                results = response.json()
                print(results)
            except IndexError:
                print(f"No flights found for {city['city']}.")
                return None

