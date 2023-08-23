from flask import Flask, render_template, request

import city_details as cd
import weather_api_request as wa

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/info', methods=['POST'])
def calculate():
    src_city = request.form['sourceCities']
    dest_city = request.form['destinationCities']
    arrival_date = str(request.form['arrivalDatePicker'])
    departure_date = str(request.form['departureDatePicker'])
    dest_country = cd.find_country(dest_city)
    result = cd.full_city_details(src_city, dest_city)
    weather = wa.get_weather_forcast(dest_city, arrival_date, departure_date)
    return render_template('cityinfo.html', result=result, dest_country=dest_country, dest_city=dest_city,
                           weather=weather)


if __name__ == '__main__':
    app.run(debug=True)
