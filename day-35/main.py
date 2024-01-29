import requests

weather_endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = "cf27321255bfcbd4a172b1e312b757a6"
parameter = {
    "lat": 5.621794,
    "lon": -0.225868,
    "appid": api_key
}

response = requests.get(weather_endpoint, params=parameter)
response.raise_for_status()
data = response.json()
print(data)