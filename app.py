from flask import Flask, render_template, request

import city_details as cd
from api.weather import WeatherApi

app = Flask(__name__)


@app.route('/travel-info')
def index():
    return render_template('choose-destination.html')


@app.route('/info', methods=['POST'])
def calculate():
    src_city = request.form['sourceCities']
    dest_city = request.form['destinationCities']
    arrival_date = str(request.form['arrivalDatePicker'])
    departure_date = str(request.form['departureDatePicker'])
    dest_country = cd.find_country(dest_city)
    result = cd.full_city_details(src_city, dest_city)
    weather = WeatherApi().get_weather_forcast(dest_city, arrival_date, departure_date).return_value
    # weather_icon = wa.weather_icon()
    # get info func
    return render_template('destination-info.html', result=result, dest_country=dest_country, dest_city=dest_city,
                           weather=weather, weather_icon=None)


if __name__ == '__main__':
    app.run(debug=True)
