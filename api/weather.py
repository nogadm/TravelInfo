import pandas as pd

from api.http_requests.request import Request
from api.http_requests.result import Result
from enums.ssh_keys_enums import SshKeysEnums
from enums.api_enums import ApiUrlsEnums


class WeatherApi:
    """
    WeatherApi class
    """

    def get_weather_forcast(self, city, start_date, end_date):
        """
        get weather forcast information to given city by range
        :param city: city
        :param start_date: start date of range
        :param end_date: end date of range
        :return: Result object
        """
        if end_date < start_date:
            return Result(error_message="Departure date is earlier than arrival date, please check the dates.")
        else:
            forecast = dict()
            date_range = pd.date_range(start=start_date, end=end_date)

            try:
                # for each day in the range, execute an API request to Weather API
                for date in date_range:
                    date_str = date.strftime('%Y-%m-%d')
                    request_data = {'key': SshKeysEnums.weather.value, 'q': city, 'dt': date_str}
                    result = Request(url=ApiUrlsEnums.weather.value).get_request(data=request_data)

                    if result.is_pass:
                        response = result.return_value["forecast"]["forecastday"][0]
                        response_day_data = response["day"]
                        response_astro_data = response["astro"]

                        # get minimum and maximum temperatures in celsius
                        min_temp_c = response_day_data["mintemp_c"]
                        max_temp_c = response_day_data["maxtemp_c"]

                        # get minimum and maximum temperatures in fahrenheit
                        min_temp_f = response_day_data["mintemp_f"]
                        max_temp_f = response_day_data["maxtemp_f"]

                        # get sunrise time and sunset time
                        sunrise = response_astro_data["sunrise"]
                        sunset = response_astro_data["sunset"]

                        # save details in dictionary
                        forecast[date_str] = {"min_temp_c": min_temp_c, "max_temp_c": max_temp_c,
                                              "min_temp_f": min_temp_f, "max_temp_f": max_temp_f,
                                              "sunrise": sunrise, "sunset": sunset}
                    else:
                        return Result(error_message=f"Error while trying to get weather forcast: "
                                                    f"{result.error_message}")
                return Result(return_value=forecast)
            except Exception as exp:
                return Result(error_message=str(exp))
