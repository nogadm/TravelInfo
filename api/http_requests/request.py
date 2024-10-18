import requests

from api.http_requests.result import Result
from urllib.parse import urlencode


class Request:
    """
    Request class
    """

    def __init__(self, url: str):
        self.url = url

    def get_request(self, data: dict):
        """
        execute http GET request
        :param data: data to pass in the request body
        :return: Result object
        """
        response = requests.get(f'https://{self.url}?{urlencode(data)}')
        if response.status_code == 200:
            response_data = response.json()
            return Result(return_value=response_data)
        return Result(error_message=response.status_code)
