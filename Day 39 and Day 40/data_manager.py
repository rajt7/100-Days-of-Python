import os
import requests

SHEETY_ENDPOINT = "https://api.sheety.co/11307556d59027ee406d56b851a93512/flightDeals/prices"
SHEETY_HEADERS = {
            "Authorization": f"Bearer {os.environ['SHEETY_TOKEN']}"
        }


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_data(self):
        """ Get the data from the Google sheet. """
        response = requests.get(url=SHEETY_ENDPOINT, headers=SHEETY_HEADERS)
        response.raise_for_status()
        data = response.json()
        self.destination_data = data['prices']
        return self.destination_data

    def update_destination_codes(self):
        """ Updating the Google sheet with the IATA Code. """
        for data in self.destination_data:
            new_data = {
                'price': {
                    'iataCode': data['iataCode']
                }
            }
            response = requests.put(url=f"{SHEETY_ENDPOINT}/{data['id']}",
                                    headers=SHEETY_HEADERS,
                                    json=new_data)
