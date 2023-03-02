import requests
import datetime as dt

today = dt.datetime.now()
date = today.today()
time = today.time()

# Currency that convartable
from_currency = input(
    "Enter in the currency you'd like to convert from: ").upper()

# Currency that Compare
to_currency = input(
    "Enter in the currency you'd like to convert to: ").upper()

# How much Money you have
amount = float(input("Enter int he amount of money: "))

response = requests.get(
    f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}")

output = f"""

{date:%A %B %d at %I:%M%p}       

{amount} {from_currency} is {response.json()['rates'][to_currency]} {to_currency}

"""

print(output)
