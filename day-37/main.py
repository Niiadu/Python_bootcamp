import requests
import datetime

# https://jsonviewer.stack.hu
# https://www.latlong.net
# https://pixe.la
# https://pandas.pydata.org/docs/reference/series.html#attributes

USERNAME = "niiadu"
TOKEN = "hsisndw723923hd"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}


# grapth_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# graph_config = {
#     "id": "graph1",
#     "name": "my coding grath",
#     "unit": "minutes",
#     "type": "float",
#     "color": "sora",
# }

pixel_post = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"


header = {
    "X-USER-TOKEN": TOKEN
}

# today = datetime.datetime(year=2023, month=11, day=21)
today = datetime.datetime.now()
print(today.strftime("%Y%m%d"))

# put_pixel = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime("%Y%m%d")}"
# delete_pixel = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime("%Y%m%d")}"


pixel_body = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many minutes did you code today? ")
}

response = requests.post(url=pixel_post, json=pixel_body, headers=header)
print(response.text)

# put_response = requests.delete(url=delete_pixel,  headers=header)
# print(put_response.text)