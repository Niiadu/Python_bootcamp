import requests
import pprint

APP_ID = "020659b4"
API_KEY = "e298196dc5239ffa38e087a5172a7ee2"

sheety_api = "https://api.sheety.co/9cfa1a5b1e6fe00315efbf11e463676c/flightDeals/prices"



class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_data_sheet(self):
        response = requests.get(url=sheety_api)
        data = response.json()
        # pprint.pprint(data)
        self.destination_data = data["prices"]
        return self.destination_data

    def send_data_to_sheet(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": ""
                }
            }
            response = requests.put(
                url=f"{sheety_api}/{city["id"]}",
                json=new_data
            )

            print(response.text)




