import os
import requests
from twilio.rest import Client


STOCK_PRICE_API = "https://www.alphavantage.co/query"
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "IBM",
    "interval": "5min",
    "apikey": os.environ['STOCK_API_KEY']
}

NEWS_API = "https://newsapi.org/v2/everything"
news_params = {
    "q": "ibm",
    "apiKey": os.environ['NEWS_API_KEY']
}

# Twilio API credentials
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

# Getting the data from the Stock API in JSON
stock_response = requests.get(url=STOCK_PRICE_API, params=stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()
print(stock_data)

# Getting the opening time and closing time of the data
opening_time_key = list(stock_data['Time Series (5min)'])[-1]
closing_time_key = list(stock_data['Time Series (5min)'])[0]

# Fetching the opening and closing price of the stock
opening_price = float(stock_data["Time Series (5min)"][opening_time_key]['1. open'])
closing_price = float(stock_data["Time Series (5min)"][closing_time_key]['4. close'])

# Calculating the percent change of the stock in a single day
percent_change = ((closing_price - opening_price) / opening_price) * 100
print("Percent change in price:", round(percent_change, 2))

# If the percent change is greater than 1 percent than fetch the news for that stock
if abs(percent_change) > 1:
    # Getting the news data
    news_response = requests.get(url=NEWS_API, params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()['articles'][:3]

    # Fetching the news headlines.
    news_titles = ''
    for i in range(len(news_data)):
        news_titles = news_titles + f'{i+1}. ' + news_data[i]["title"] + ' \n'

    # Drafting a message
    if percent_change > 0:
        message_to_send = f'Stock prices for tesla has shown {round(abs(percent_change), 2)} ' \
                          f'percent growth in a day. Here are the top 3 headlines for Tesla.\n' + \
                          news_titles
    else:
        message_to_send = f'Stock prices for tesla has shown {round(abs(percent_change), 2)} ' \
                          f'percent decrease in a day. Here are the top 3 headlines for Tesla.\n' \
                          + news_titles

    # Sending the message using Twilio
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body=message_to_send,
            from_='+13204417317',
            to='+919429797753'
        )
