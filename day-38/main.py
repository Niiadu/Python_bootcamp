import requests
import os
import datetime

APP_ID = "020659b4"
API_KEY = "e298196dc5239ffa38e087a5172a7ee2"
GENDER = "male"
HEIGHT = "190"
AGE = "27"


exercise_text = input("Tell me which exeercise you did: ")
today = datetime.datetime.now()

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/9cfa1a5b1e6fe00315efbf11e463676c/workoutTracking/workouts"

parameters = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}


body = {
    "query": exercise_text,
    "gender": GENDER,
    "height_cm": HEIGHT,
    "age": AGE,
}

response = requests.post(url=exercise_endpoint, headers=parameters, json=body)
response.raise_for_status()
response_exercises = response.json()["exercises"]
# text_input = input("Your exercise: ")
for index in response_exercises:
    print(index)
    workout_sheet = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%H:%M:%S"),
            "exercise": index["name"].title(),
            "duration": index["duration_min"],
            "calories": index["nf_calories"]
        }
    }

    response = requests.post(url=sheety_endpoint, json=workout_sheet, headers=parameters)
    print(response.text)