from forex_python.converter import CurrencyRates

def currency_converter():
    c = CurrencyRates()

    print("Currency Converter")
    print("Supported currencies: USD, EUR, GBP, JPY, INR, ...")
    
    from_currency = input("Enter the currency code you want to convert from: ").upper()
    to_currency = input("Enter the currency code you want to convert to: ").upper()
    
    amount = float(input(f"Enter the amount in {from_currency}: "))
    
    try:
        converted_amount = c.convert(from_currency, to_currency, amount)
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
    except:
        print("Error: Invalid currency codes or conversion rate not available.")

if __name__ == "__main__":
    currency_converter()
