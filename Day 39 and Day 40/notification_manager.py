import os
import smtplib
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

    def send_emails(self, receiver_mails, price, origin_city, origin_airport, destination_city,
                    destination_airport, out_date, return_date):
        sender = 'raj.mangukiya7070@gmail.com'
        receivers = receiver_mails

        message = f"Low price alert! Only £{price} to fly from {origin_city}-" \
                  f"{origin_airport} to {destination_city}-{destination_airport}," \
                  f"from {out_date} to {return_date}." \

        try:
            smp_obj = smtplib.SMTP('localhost')
            smp_obj.sendmail(from_addr=sender, to_addrs=receivers, msg=message)
        except smtplib.SMTPException:
            print("Error: unable to send mail")

