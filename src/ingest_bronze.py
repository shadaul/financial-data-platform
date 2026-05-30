import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

def fetch_stock_data():
    api_key = os.getenv("ALPHA_VANTAGE_API_KEY")

    if not api_key:
        raise ValueError("No API key, check .env! ")

    url = "https://www.alphavantage.co/query"
    params = {"function":"TIME_SERIES_DAILY", "symbol":"AAPL", "apikey" : api_key}

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        with open("data/raw/aapl_raw.json", "w") as file:
            json.dump(data, file, indent=4)
    else:
        print(f"error {response.status_code}")
        
if __name__ == "__main__":
    print("running script, collecting data")
    fetch_stock_data()