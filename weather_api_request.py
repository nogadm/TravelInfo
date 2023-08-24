import base64
import requests
import pandas as pd

key = "a45ea9764ada4fa6b5675219232108"


def get_weather_forcast(city, start_date, end_date):
    # find the date range between the first and last day
    date_range = pd.date_range(start=start_date, end=end_date)
    # dictionary that will contain data on each day in the range
    forecast = dict()

    if end_date < start_date:
        forecast["Departure date is earlier than arrival date, please check the dates."] = ""
    else:
        # for each day in the range, send an API request to Weather API
        for date in date_range:
            date_str = date.strftime('%Y-%m-%d')
            response = requests.get(f"http://api.weatherapi.com/v1/future.json?key={key}&q={city}&dt={date_str}")
            date_weather_dict = response.json()

            # get min temperature and max temperature in celsius
            min_temp_c = date_weather_dict["forecast"]["forecastday"][0]["day"]["mintemp_c"]
            max_temp_c = date_weather_dict["forecast"]["forecastday"][0]["day"]["maxtemp_c"]

            # get min temperature and max temperature in fahrenheit
            min_temp_f = date_weather_dict["forecast"]["forecastday"][0]["day"]["mintemp_f"]
            max_temp_f = date_weather_dict["forecast"]["forecastday"][0]["day"]["maxtemp_f"]

            # get sunrise time and sunset time
            sunrise = date_weather_dict["forecast"]["forecastday"][0]["astro"]["sunrise"]
            sunset = date_weather_dict["forecast"]["forecastday"][0]["astro"]["sunset"]

            # save details in dictionary
            forecast[date_str] = {"min_temp_c":min_temp_c, "max_temp_c":max_temp_c,
                                 "min_temp_f": min_temp_f, "max_temp_f": max_temp_f,
                                 "sunrise":sunrise, "sunset":sunset}
    return forecast


def weather_icon():
    with open('icons/weather.png', 'rb') as f:
        image = f.read()
        encoded_image = base64.b64encode(image).decode('utf-8')
        return encoded_image
