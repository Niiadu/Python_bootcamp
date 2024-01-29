import requests
from data_manager import DataManager

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

# APP_ID = "020659b4"
# API_KEY = "e298196dc5239ffa38e087a5172a7ee2"
#
# 
# sheety_api = "https://api.sheety.co/9cfa1a5b1e6fe00315efbf11e463676c/flightDeals/prices"
#
# headers = {
#     "x-app-id": APP_ID,
#     "x-app-key": API_KEY,
# }

data_manager = DataManager()
sheet_data = data_manager.get_data_sheet()

if sheet_data[0]["iataCode"] == "TESTING":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(f"sheet data\n {sheet_data}")

    data_manager.send_data_to_sheet()