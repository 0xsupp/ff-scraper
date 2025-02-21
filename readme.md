# FF Scraper

This project performs **web scraping** on the `https://ff.io/`. The data is stored in an accumulating JSON file.

## 📌 Requirements

- Python 3.8 or later
- `pip` for dependency management

## 🔧 Installation

1. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Execution

To start the scraper:
```bash
python main.py
```
This will run every **5 minutes** and continuously append results to `recent_list.json`.

## 🛠 Configuration

You can modify these values inside `main.py`:
```python
URL = 'https://ff.io/'
FILE_PATH = 'recent_list.json'
```

## 📄 Output Format

The `recent_list.json` file will have the following format:
```json
[
    {
        "dir-com": "BTC",
        "dir-to": "USDT",
        "coin-value": "1500 USDT",
        "timestamp": "1740129932"
    },
    {
        "dir-com": "ETH",
        "dir-to": "USDC",
        "coin-value": "2000 USDC",
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

