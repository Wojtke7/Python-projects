from datetime import datetime
import os
import requests

sheet_url = "https://api.sheety.co/50ab9cbfa61830f47d54f41870031777/myWorkouts/workouts"
url = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    'Content-Type': 'application/json',
    'x-app-id': os.environ["APP_ID"],
    'x-app-key': os.environ["API_KEY"]
}

exercise = input("Tell me which exercise you did: ")

body = {
    "query": exercise
}

response = requests.post(url=url, headers=headers, json=body)
workout_data = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

sheet_header = {
    "Authorization": os.environ["BEARER_TOEKN"]
}

for exercise in workout_data["exercises"]:
    sheet_body = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    response_sheet = requests.post(sheet_url, headers=sheet_header, json=sheet_body)
    print(response_sheet.text)
