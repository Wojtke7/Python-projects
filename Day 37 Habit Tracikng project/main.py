import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

TOKEN = "eo3i5h2ou564f2t553tbfbo8r1u9r"
USERNAME = "wojtke7"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_conf = {
    "id": "graph1",
    "name": "Coding graph",
    "unit": "hours",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_conf, headers=headers)
# print(response.text)

pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

today = datetime.now()

pixel_update = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "4.5"
}

response = requests.post(url=pixel_update_endpoint, headers=headers, json=pixel_update)
print(response.text)


