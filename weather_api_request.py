import requests
import pandas as pd

key = "a45ea9764ada4fa6b5675219232108"


def get_weather_forcast(city, start_date, end_date, degree_type):
    # find the date range between the first and last day
    date_range = pd.date_range(start=start_date, end=end_date)

    # dictionary that will contain data on each day in the range
    forcast = dict()

    # for each day in the range, send an API request to Weather API
    for date in date_range:
        date_str = date.strftime('%Y-%m-%d')
        response = requests.get(f"http://api.weatherapi.com/v1/future.json?key={key}&q={city}&dt={date_str}")
        date_weather_dict = response.json()

        if degree_type == "C":
            # get min temperature and max temperature in celsius
            min_temp = date_weather_dict["forecast"]["forecastday"][0]["day"]["mintemp_c"]
            max_temp = date_weather_dict["forecast"]["forecastday"][0]["day"]["maxtemp_c"]
        else:
            # get min temperature and max temperature in fahrenheit
            min_temp = date_weather_dict["forecast"]["forecastday"][0]["day"]["mintemp_f"]
            max_temp = date_weather_dict["forecast"]["forecastday"][0]["day"]["maxtemp_f"]

        # get sunrise time and sunset time
        sunrise = date_weather_dict["forecast"]["forecastday"][0]["astro"]["sunrise"]
        sunset = date_weather_dict["forecast"]["forecastday"][0]["astro"]["sunset"]

        # save details in dictionary
        forcast[date_str] = {"min_temp":min_temp, "max_temp":max_temp,
                             "sunrise":sunrise, "sunset":sunset}

    return forcast


print(get_weather_forcast("New York City", "2024-04-21", "2024-04-23", "C"))
