import requests
import datetime as dt
import os
#nutrition API Info ----
APP_ID= os.environ["ENV_NIX_APPID"]
API_KEY= os.environ["ENV_NIX_APPKEY"]
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
#parameters for nutrition API call ----
exercise_input = input("Tell which exercise you did today?: ")
parameters = {
"query": exercise_input
}
#send API key and account info as a header ----
header = {
 "x-app-id": APP_ID,
  "x-app-key": API_KEY,
}
#Make an API call to the nutrition website ----
response = requests.post(url=exercise_endpoint, json=parameters, headers=header)
result = response.json()["exercises"]

Date = dt.datetime.now().strftime("%d/%m/%Y")
Time = dt.datetime.now().strftime("%H:%M:%S")

#sheety requires the post json data to be structured in a nested dictionary format
bearer_headers = {
"Authorization": "Bearer YOUR_TOKEN"
}
for each_exercise in result:
 data_to_post = {
  "my sheet":  {
   "date":Date,
   "time": Time,
   "exercise": each_exercise["user_input"],
   "duration":each_exercise["duration_min"],
   "calories":each_exercise["nf_calories"]
  }
 }
 print(data_to_post)
 #sheet_response = requests.post(url = "sheet_endpt", json = data_to_post, header = bearer_headers)
 #print(sheet_response.text)