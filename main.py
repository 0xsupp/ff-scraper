import requests
from bs4 import BeautifulSoup
import time
import json

# Configuració
URL = 'https://ff.io/'
FILE_PATH = 'recent_list.json'
MIN_VALUE = 1000  # Valor mínim per filtrar

def extract_value(text):
    parts = text.split()
    if len(parts) == 2:
        try:
            value = float(parts[0])  # Convertim a número
            currency = parts[1].upper()  # Convertim a majúscules
            return value, currency
        except ValueError:
            return None, None
    return None, None

def scrape_recent_list():
    try:
        # Fa la petició a la pàgina
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

                    if value and currency:
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

                print(f"S'han afegit {len(filtered_items)} elements en {FILE_PATH}")
            else:
                print("No hi ha elements que compleixin el criteri.")
        else:
            print("No s'ha trobat la classe 'recent-list'.")

    except requests.exceptions.RequestException as e:
        print(f"Error en fer la petició: {e}")

if __name__ == "__main__":
    while True:
            scrape_recent_list()
            time.sleep(3)  
