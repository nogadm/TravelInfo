from api.http_requests.request import Request
from api.http_requests.result import Result
from enums.ssh_keys_enums import SshKeysEnums
from enums.api_enums import ApiUrlsEnums


class CurrencyApi:
    """
    CurrencyApi class
    """

    def get_conversion_rate(self, from_currency, to_currency):
        """
        execute an API request to currencyapi to get the conversion rate between the two currencies
        :param from_currency: currency to convert from
        :param to_currency: currency to convert to
        :return: Result obj
        """
        try:
            request_data = {'apikey': SshKeysEnums.currency.value, 'currencies': to_currency,
                            'base_currency': from_currency}
            result = Request(url=ApiUrlsEnums.currency.value).get_request(data=request_data)

            if result.is_pass:
                response = result.return_value
                conversion_rate = response['data'][to_currency]['value']
                conversion_message = f"1{from_currency} is equal to {round(conversion_rate, 2)}{to_currency}"
                return Result(return_value=conversion_message)
            else:
                return Result(error_message=f"Error while trying to get currency information: {result.error_message}")
        except Exception as exp:
            return Result(error_message=str(exp))
