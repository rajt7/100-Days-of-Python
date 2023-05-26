import requests

parameters = {
    'lat': 21.170240,
    'lng': 72.831062,
    'formatted': 0
}

response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
data = response.json()
print(data)
