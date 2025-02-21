import requests
from bs4 import BeautifulSoup
import time
import json

# Configuration
URL = 'https://ff.io/'
FILE_PATH = 'recent_list.json'
MIN_VALUES = {
    "USDT": 100,
    "USDC": 50,
    "BTC": 5000
}  # Minimum values per currency
UPDATE = 30  # Interval in seconds

def extract_value(text):
    """Extracts the numerical value and currency from the given text."""
    parts = text.split()
    if len(parts) == 2:
        try:
            value = float(parts[0])  # Convert to a number
            currency = parts[1].upper()  # Convert to uppercase
            return value, currency
        except ValueError:
            return None, None
    return None, None

def scrape_recent_list():
    """Scrapes the website and extracts relevant transaction data."""
    try:
        # Send a request to the page
        response = requests.get(URL)
        response.raise_for_status() 
        soup = BeautifulSoup(response.text, 'html.parser')

        recent_list = soup.find(class_='recent-list')

        if recent_list:
            items = recent_list.find_all('li')  

            filtered_items = []
            for item in items:
                dir_from = item.find(class_='dir-from')
                dir_to = item.find(class_='dir-to')
                coin_value_tag = item.find(class_='coin-value')
                time_tag = item.find('time')  

                timestamp = time_tag['timestamp'] if time_tag and 'timestamp' in time_tag.attrs else None

                if coin_value_tag:
                    value, currency = extract_value(coin_value_tag.get_text(strip=True))

                    # Check if `dir-from` exists in the dictionary and if the value exceeds the minimum threshold
                    if currency in MIN_VALUES and value > MIN_VALUES[currency]:
                        item_data = {}

                        if dir_from:
                            item_data['dir-from'] = currency
                        if dir_to:
                            item_data['dir-to'] = dir_to.get_text(strip=True)
                        if timestamp:
                            item_data['timestamp'] = timestamp  

                        item_data['coin-value'] = value

                        filtered_items.append(item_data)

            if filtered_items:
                try:
                    with open(FILE_PATH, 'r', encoding='utf-8') as file:
                        existing_data = json.load(file)
                except (FileNotFoundError, json.JSONDecodeError):
                    existing_data = []

                existing_data.extend(filtered_items)

                with open(FILE_PATH, 'w', encoding='utf-8') as file:
                    json.dump(existing_data, file, ensure_ascii=False, indent=4)

                print(f"Added {len(filtered_items)} items to {FILE_PATH}")
            else:
                print("No items match the criteria.")
        else:
            print("Class 'recent-list' not found.")

    except requests.exceptions.RequestException as e:
        print(f"Error while making the request: {e}")

if __name__ == "__main__":
    while True:
        scrape_recent_list()
        time.sleep(UPDATE)  
