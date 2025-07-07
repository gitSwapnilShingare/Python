import requests
import pandas as pd
import logging
from datetime import datetime

# Setup Logger
logging.basicConfig(filename='crypto_fetcher.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# API URL
url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd,inr"

def fetch_crypto_prices():
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise error for bad responses
        data = response.json()

        # Transform to DataFrame
        df = pd.DataFrame(data).T  # .T to transpose: crypto as rows
        df['timestamp'] = datetime.now()

        # Save to CSV
        df.to_csv("crypto_prices.csv", mode='a', header=not pd.io.common.file_exists("crypto_prices.csv"))

        logging.info("Data fetched and saved successfully.")

    except Exception as e:
        logging.error(f"Error fetching data: {e}")

if __name__ == "__main__":
    fetch_crypto_prices()
