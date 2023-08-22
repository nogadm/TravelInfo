import requests

key = "cur_live_rOvleCWQhhHUClZPv4TLDy0dVSReFiAIKum78lra"


def find_conversion_rate(from_currency, to_currency):
    # send an API request to Exchange Rates API to get the conversion rate between the two currencies
    response = requests.get(f"https://api.6currencyapi.com/v3/latest?apikey={key}&currencies={from_currency}&base_currency={to_currency}")
    conversion_dict = response.json()
    conversion_rate = conversion_dict['data'][from_currency]['value']

    return conversion_rate


def convert_amount(from_currency, to_currency, amount_to_convert):
    # send an API request to Exchange Rates API to get the conversion rate between the two currencies
    response = requests.get(f"https://api.currencyapi.com/v3/latest?apikey={key}&currencies={from_currency}&base_currency={to_currency}")
    conversion_dict = response.json()
    conversion_rate = conversion_dict['data'][from_currency]['value']

    # calculate converted amount
    converted_amount = amount_to_convert * conversion_rate

    print(f"{amount_to_convert}{to_currency} will cost you {round(converted_amount,2)}{from_currency}")


convert_amount("ILS", "EUR", 500)