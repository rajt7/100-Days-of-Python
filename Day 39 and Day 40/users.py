import os
import requests

SHEETY_USERS_ENDPOINT = "https://api.sheety.co/11307556d59027ee406d56b851a93512/flightDeals/users"
SHEETY_USERS_HEADERS = {
    "Authorization": f"Bearer {os.environ['SHEETY_TOKEN']}"
}


class User:

    def __init__(self):
        print("Welcome to the Raj's Flight Club.")
        print("We find the best flight deals and email you.")
        self.user_data = {}

    def get_user_data(self):
        response = requests.get(url=SHEETY_USERS_ENDPOINT, headers=SHEETY_USERS_HEADERS)
        response.raise_for_status()
        data = response.json()
        self.user_data = data['users']
        return self.user_data

    def register(self):
        first_name = input("What is your first name?\n")
        last_name = input("What is your last name?\n")
        email_id = input("What is your email?\n")
        verify_email_id = input("Type your email again.\n")

        if email_id == verify_email_id:
            new_user_data = {
                'user': {
                    'firstName': first_name,
                    'lastName': last_name,
                    'email': email_id
                }
            }

            response = requests.post(url=SHEETY_USERS_ENDPOINT, headers=SHEETY_USERS_HEADERS,
                                     json=new_user_data)

