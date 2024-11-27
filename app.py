import json
from flask import Flask, render_template, request
from data.travel import Travel
from api.weather import WeatherApi

app = Flask(__name__)

@app.route('/travel-info')
def index():
    return render_template('choose-destination.html')

@app.route('/info', methods=['POST'])
def display_info():
    src_city = request.form['sourceCities']
    dest_city = request.form['destinationCities']
    travel = Travel(src_city=src_city, dest_city=dest_city)

    destination_name = travel.get_full_destination_name()
    city_details = travel.full_city_details()
    weather = WeatherApi().get_weather_forcast(dest_city, str(request.form['arrivalDatePicker']), str(request.form['departureDatePicker'])).return_value

    return render_template('destination-info.html', destination_name=destination_name, city_details=json.dumps(city_details), weather=weather)

if __name__ == '__main__':
    app.run(debug=True)
