import requests

API_KEY = 'fca_live_YIb84iC8QQz4Dc5VxtKhTkCIigQQ4MbdZiJJr7CE'
BASE_URL = f'https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}'

CURRENCIES  = ["USD", "CAD", "EUR", "AUD", "CNY", "IDR"]

def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try: 
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except Exception as e:
        print('Invalid Currency')
        return None
    
while True: 
    base = input("Enter the base currency (q for quit):").upper()

    if base == "Q":
        break

    data = convert_currency("USD")
    if not data:
        continue

    del data["USD"]
    for ticker, value in data.items():
        print(f"{ticker}: {value}")