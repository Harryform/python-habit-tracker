import requests
from datetime import datetime

# log in info for requests

USERNAME = "harryform"
TOKEN = "lkasdnlaksdf"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": "graph1",
    "name": "Workout Graph",
    "unit": "Reps",
    "type": "int",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

# time and date for tracker input

today = datetime.now()

pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many reps did you do today? "),
}

# TODO create a full gui with buttons for this app. There should be 5 buttons and each gives the value 1 - 5
#  for amount of reps for that day

response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
print(response.text)

update_endpoint = f"{pixel_endpoint}/{today.strftime('%Y%m%d')}"

update_params = {
    "quantity": "3",
}
