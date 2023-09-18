import requests
import pandas as pd


API_URL = "https://data.binance.com/api/v3/ticker/24hr"

response = requests.get(API_URL)

if response.status_code == 200:
    data = response.json()
else:
    print("Failed to retrieve the data from the API")
    exit()

df = pd.DataFrame(data)

csv_filename ="api_data.csv"
df.to_csv(csv_filename, index=False)
print(f"CSV dataset saved as {csv_filename}")
df = pd.read_csv("api_data.csv")
