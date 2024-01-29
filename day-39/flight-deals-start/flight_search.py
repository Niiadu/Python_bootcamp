import requests

TEQUILLA_API = "bpHDLV-31-337sQQEd60kJxFU2oGja2a"
TEQUILLA_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"


response = requests.put(url=TEQUILLA_ENDPOINT, headers=headers, params=query)
code = response.json()["locations"][0]["code"]
print(code)
class FlightSearch:
    pass
    #This class is responsible for talking to the Flight Search API.

    # def get_destination_code(self,city_name):
    #     headers = {
    #         "apikey": TEQUILLA_API,
    #     }
    #
    #     query = {
    #         "term": city_name,
    #         "location_types": "city"
    #     }
    #     response = requests.put(url=TEQUILLA_ENDPOINT, headers=headers, params=query)
    #     code = response.json()["locations"][0]["code"]
    #     return code

    # def get_destination_code(self, city_name):
    #     code = "TESTING"
    #     return code

# FlightSearch().get_destination_code("Paris")



