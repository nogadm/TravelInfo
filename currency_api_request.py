import requests

key = "cur_live_rOvleCWQhhHUClZPv4TLDy0dVSReFiAIKum78lra"


def convert_amount(from_currency, to_currency, amount_to_convert):
    # send an API request to currencyapi to get the conversion rate between the two currencies
    response = requests.get(f"https://api.currencyapi.com/v3/latest?apikey={key}&currencies={to_currency}&base_currency={from_currency}")
    conversion_dict = response.json()
    conversion_rate = conversion_dict['data'][to_currency]['value']

    # calculate converted amount
    converted_amount = amount_to_convert * conversion_rate

    # return message according to the desired amount to convert
    if amount_to_convert == 1:
        message = f"1{from_currency} is equal to {round(conversion_rate,2)}{to_currency}"
    else:
        message = f"{amount_to_convert}{from_currency} will cost you {round(converted_amount,2)}{to_currency}"
    return message


# print(convert_amount("ILS","USD", 100))