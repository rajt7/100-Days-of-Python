# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import datetime, timedelta

# Getting the data from the Google Sheet
data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# Getting the Google sheet data
sheet_data = data_manager.get_data()

# Origin city is London
ORIGIN_CITY_IATA = "LON"

# Checking if IATA Code is present. If not, then updating the Google sheet with the respective
# IATA Codes from Kiwi Flight Search API.
if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row['iataCode'] = flight_search.get_destination_code(city_name=row['city'])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

# Setting the tomorrow and six month from today's dates
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6*30))

# for each city in the Google sheet getting the flight data from the flight API and comparing the
# price. If flight price lower than the price in sheet, then send the message to the user for a low
# price alert.
for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination['iataCode'],
        tomorrow.strftime('%d/%m/%Y'),
        six_month_from_today.strftime('%d/%m/%Y')
    )

    if flight is not None and flight.price < destination['lowestPrice']:
        notification_manager.send_message(price=flight.price, origin_city=flight.origin_city,
                                          origin_airport=flight.origin_airport,
                                          destination_city=flight.destination_city,
                                          destination_airport=flight.destination_airport,
                                          out_date=flight.out_date, return_date=flight.return_date)
