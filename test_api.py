import requests
import pandas as pd

response = requests.get("http://127.0.0.1:5000/expenses")

data = response.json()

df = pd.DataFrame(data)

print(df)