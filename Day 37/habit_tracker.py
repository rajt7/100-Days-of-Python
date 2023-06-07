import requests

TOKEN = "abvila94r8nfoavn"
USERNAME = "rajt7"

pixela_endpoint = "https://pixe.la/v1/users"

pixela_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=pixela_params)
# print(response.text)

headers = {
    "X-USER-TOKEN": TOKEN
}
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Coding",
    "unit": "minutes",
    "type": "int",
    "color": "sora"
}

pixel_endpoint = f"{graph_endpoint}/{graph_config['id']}"
pixel_config = {
    "date": "20230602",
    "quantity": "90"
}

update_pixel_endpoint = f"{pixel_endpoint}/20230602"
update_pixel_config = {
    "quantity": "150"
}

graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
pixel_response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
update_pixel_response = requests.put(url=update_pixel_endpoint, json=update_pixel_config,
                                     headers=headers)

print(update_pixel_response.text)

