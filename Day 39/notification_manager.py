import os
from twilio.rest import Client

# Twilio API credentials
TWILIO_SID = os.environ['TWILIO_ACCOUNT_SID']
TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
TWILIO_VIRTUAL_NUMBER = os.environ['TWILIO_VIRTUAL_NUMBER']
TWILIO_VERIFIED_NUMBER = os.environ['TWILIO_VERIFIED_NUMBER']

class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_message(self, price, origin_city, origin_airport, destination_city,
                     destination_airport, out_date, return_date):
        message_body = f"Low price alert! Only £{price} to fly from {origin_city}-" \
                       f"{origin_airport} to {destination_city}-{destination_airport}," \
                       f"from {out_date} to {return_date}." \

        message = self.client.messages.create(
                body=message_body,
                from_=TWILIO_VIRTUAL_NUMBER,
                to=TWILIO_VERIFIED_NUMBER
            )

        print(message.sid)
