import requests
import pandas as pd

response = requests.get("http://127.0.0.1:5000/expenses")
if response.status_code == 200:
    print("Expenses API passed")
else:
    print("Expenses API failed")

data = response.json()

df = pd.DataFrame(data)

print(df)

prediction_response = requests.get(
    "http://127.0.0.1:5000/expenses/predict")

if prediction_response.status_code == 200:
    print("Predicition Expenses API passed")
else:
    print("Predictions Expenses API failed")

print(prediction_response.json())