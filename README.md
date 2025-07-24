# 💱 Currency Converter (Python CLI)

A simple command-line currency converter tool using the `forex-python` library. This script allows users to convert a specified amount from one currency to another using real-time exchange rates.

---

## 📦 Dependencies

Install the required package using pip:

```bash
pip install forex-python
```

---

## 🚀 How to Use

1. Run the script:

```bash
python currency_converter.py
```

2. Follow the prompts:

```
Currency Converter
Supported currencies: USD, EUR, GBP, JPY, INR, ...
Enter the currency code you want to convert from: USD
Enter the currency code you want to convert to: INR
Enter the amount in USD: 100
100 USD is equal to 8307.25 INR
```

---

## 🔧 Features

- Live currency conversion using real-time exchange rates
- Supports all major currencies (USD, EUR, GBP, JPY, INR, etc.)
- Input validation and error handling for unsupported codes

---

## 🧠 Example Supported Currencies

- `USD` – US Dollar  
- `EUR` – Euro  
- `INR` – Indian Rupee  
- `GBP` – British Pound  
- `JPY` – Japanese Yen  
- ...and many more (any currency supported by [forex-python](https://pypi.org/project/forex-python/))

---

## ⚠️ Notes

- Requires an internet connection to fetch live exchange rates.
- Ensure you enter valid ISO 4217 currency codes (e.g., `USD`, `INR`).
- API data is pulled from [ExchangeRate-API](https://www.exchangerate-api.com/) via `forex-python`.

---

## 📄 License

This project is free to use for personal or educational purposes.

