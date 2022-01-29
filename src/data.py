import io
import pandas as pd
import requests
import toml

def get_data(symbol: str,
             api_key: str | None = None,
             function: str = "TIME_SERIES_DAILY",
             compact: bool = True,
             datatype: str = "json"):
    if not api_key:
        secrets = toml.load("../secrets.toml")
        api_key = secrets["ALPHA_VANTAGE_API_KEY"]
    params = {
        "symbol": symbol,
        "apikey": api_key,
        "function": function,
        "outputsize": "compact" if compact else "full",
        "datatype": datatype,
    }
    url = "https://www.alphavantage.co/query?"
    response = requests.get(url, params=params)
    return response

def parse_df_from_api_csv(response):
    csv_obj = io.StringIO(response.text)
    df = pd.read_csv(csv_obj)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    # Reverse indices, they come backward from the API.
    df = df.reindex(index=df.index[::-1])
    df = df.reset_index(drop=True)
    return df