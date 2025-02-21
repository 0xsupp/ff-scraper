# FF Scraper

This project performs **web scraping** on the `https://ff.io/` website every 5 minutes to fetch recent transaction data, filtering only those with `USDC`, `USDT`, or `BTC` that exceed specific minimum values. The data is stored in an accumulating JSON file.

## 📌 Requirements

- Python 3.8 or later
- `pip` for dependency management

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/0xsupp/ff-scraper.git
   cd ff-scraper
   ```
2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Execution

To start the scraper:
```bash
python main.py
```
This will run every **`UPDATE` seconds** and continuously append results to `recent_list.json`.

## 🛠 Configuration

You can modify these values inside `main.py`:
```python
URL = 'https://ff.io/'
FILE_PATH = 'recent_list.json'
MIN_VALUES = {
    "USDT": 100,
    "USDC": 50,
    "BTC": 5000
}  # Minimum value per currency
UPDATE = 30  # Scraping interval in seconds
```

## 📄 Output Format

The `recent_list.json` file will have the following format:
```json
[
    {
        "dir-from": "BTC",
        "dir-to": "USDT",
        "coin-value": 5500,
        "timestamp": "1740129932"
    },
    {
        "dir-from": "USDC",
        "dir-to": "ETH",
        "coin-value": 200,
        "timestamp": "1740130045"
    }
]
```

## 📌 Dependencies

This project uses:
- `requests` for making HTTP requests
- `beautifulsoup4` for parsing HTML

## 📜 License

This project is licensed under the MIT License. 📝

