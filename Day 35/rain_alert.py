import requests

api_key = "60dd988978eeef4171304e5dd06813a6"

weather_params = {
    'lat': 21.170240,
    'lon': 72.831062,
    'appid': api_key
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/weather",
                        params=weather_params)

print(response.json())
