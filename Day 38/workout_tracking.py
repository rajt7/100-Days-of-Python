import os
import requests
from datetime import datetime

# Setting teh parameters for Exercise data from NutritionX API
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "x-app-id": os.environ['APP_ID'],
    "x-app-key": os.environ['APP_KEY'],
    "content-type": "application/json"
}
exercise_config = {
    "query": input("Tell me what exercise you did today? "),
    "gender": "male",
    "weight_kg": 58.3,
    "height_cm": 170,
    "age": 22
}

# Posting the data from API by asking the user the workouts done in a string
exercise_response = requests.post(url=exercise_endpoint, headers=headers, json=exercise_config)
exercise_response.raise_for_status()
exercise_data = exercise_response.json()

# Setting the time and date as of current
current_date_time = datetime.now()
current_date = datetime.strftime(current_date_time, '%d/%m/%Y')
current_time = datetime.strftime(current_date_time, '%H:%M:%S')

# For each workout adding a specific row
for i in range(len(exercise_data['exercises'])):

    # Setting the parameters same as which are in Google Sheets
    date = current_date
    time = current_time
    exercise = exercise_data['exercises'][i]['name']
    duration = exercise_data['exercises'][i]['duration_min']
    calories = exercise_data['exercises'][i]['nf_calories']

    # Sheety API to post the data in a Google Sheets
    sheety_endpoint = f"https://api.sheety.co/{os.environ['SHEETY_USERNAME']}/myWorkouts/workouts"
    sheety_header = {
        "Authorization": os.environ['SHEETY_AUTH_ID'],
        'Content-Type': 'application/json'
    }

    # Creating a dictionary which is to be posted with the root key as the name of sheet
    workout_row_data = {
        'workout': {
            'date': current_date,
            'time': current_time,
            'exercise': exercise,
            'duration': duration,
            'calories': calories,
        }
    }

    # Posting the data
    workout_row = requests.post(url=sheety_endpoint, json=workout_row_data, headers=sheety_header)
    workout_row.raise_for_status()
