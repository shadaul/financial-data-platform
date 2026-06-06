import pandas as pd
import json
import sys

def clean_stock_data(ticker):
    with open(f"data/raw/{ticker.lower()}_raw.json", "r") as file:
        raw_data = json.load(file)
        time_series_dict = raw_data["Time Series (Daily)"]
        df = pd.DataFrame(time_series_dict)
        df = df.T
        df = df.rename(columns={"1. open": "open", "2. high": "high", "3. low": "low", "4. close": "close", "5. volume": "volume"})
        df =df.reset_index()
        df = df.rename(columns={"index": "date"})
        df["date"] = pd.to_datetime(df["date"])
        df[["open", "high", "low", "close", "volume"]] = df[["open", "high", "low", "close", "volume"]].astype(float)
        df.to_parquet(f"data/silver/{ticker.lower()}_silver.parquet")

if __name__ == "__main__":
    user_ticker = sys.argv[1]
    print(f"Here we are {user_ticker}")
    clean_stock_data(user_ticker.lower())