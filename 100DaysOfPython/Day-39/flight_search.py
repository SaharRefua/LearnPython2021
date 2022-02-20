import requests


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.all_cities = []
        self.city = ""

    def add_city(self, city):
        if city["iataCode"] == "":
            city["iataCode"] = "TRESTING"
        self.all_cities.append(city)
        # return self.all_cities
