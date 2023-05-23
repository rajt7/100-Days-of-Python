travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities_visited": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"]
    }
]

def add_new_country(country, visits, cities_visited):
    dict = {}
    dict["country"] = country
    dict["visits"] = visits
    dict["cities_visited"] = cities_visited
    travel_log.append(dict)

add_new_country("Russia", 15, ["Moscow", "Saint Petersburg"])
print(travel_log)