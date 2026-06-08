import os
import json
import requests
from dotenv import load_dotenv
import sys

load_dotenv()

def fetch_stock_data(ticker):
    api_key = os.getenv("ALPHA_VANTAGE_API_KEY")

    if not api_key:
        raise ValueError("No API key, check .env! ")

    url = "https://www.alphavantage.co/query"
    params = {"function":"TIME_SERIES_DAILY", "symbol":ticker, "apikey" : api_key}

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        os.makedirs("data/raw", exist_ok=True)
        os.makedirs("data/bronze", exist_ok=True)
        os.makedirs("data/silver", exist_ok=True)
        os.makedirs("data/gold", exist_ok=True)
        with open(f"data/raw/{ticker.lower()}_raw.json", "w") as file:
            json.dump(data, file, indent=4)
    else:
        print(f"error {response.status_code}")
        
if __name__ == "__main__":
    user_ticker = sys.argv[1]
    print(f"running script, collecting data for {user_ticker}")
    fetch_stock_data(user_ticker)