import os
import requests
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
TEQUILA_HEADERS = {
    "apikey": os.environ['TEQUILA_API_KEY']
}


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def get_destination_code(self, city_name):
        """ Get the destination IATA Code by using Tequila Flight Search API and returning it."""
        tequila_params = {
            "term": city_name
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query",
                                headers=TEQUILA_HEADERS,
                                params=tequila_params)
        code = response.json()['locations'][0]['code']
        return code

    # def get_flight(self, iata_code):
    #     flight_params = {
    #         "fly_from": "LON",
    #         "fly_to": iata_code,
    #         "date_from": "10/06/2023",
    #         "date_to": "10/12/2023",
    #         "curr": "GBP",
    #         "limit": 1
    #     }
    #
    #     response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search",
    #                             headers=TEQUILA_HEADERS,
    #                             params=flight_params)
    #
    #     flights = response.json()['data']
    #
    #     for flight in flights:
    #         destination_city = flight['cityTo']
    #         destination_price = flight['price']
    #         print(f"{destination_city}: £ {destination_price}")

    def check_flights(self, origin_city_code, destination_city_code, date_from, date_to):
        """ The function will check the flights from origin city to destination city from
            tomorrow to next six months and will return the flight details which is having the
             cheapest price. """

        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": date_from,
            "date_to": date_to,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "curr": "GBP",
            "max_stopovers": 0
        }

        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search",
                                headers=TEQUILA_HEADERS,
                                params=query)

        try:
            data = response.json()['data'][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}")
            return None

        flight_data = FlightData(
            price=data['price'],
            origin_city=data['route'][0]['cityFrom'],
            origin_airport=data['route'][0]['flyFrom'],
            destination_city=data['route'][0]['cityTo'],
            destination_airport=data['route'][0]['flyTo'],
            out_date=data['route'][0]['local_departure'].split('T')[0],
            return_date=data['route'][1]['local_departure'].split('T')[0]
        )

        print(f"{flight_data.destination_city}: £ {flight_data.price}")
        return flight_data
