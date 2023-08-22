from flask import Flask, render_template, request

import city_details
import weather_api_request as weather
import exchange_rates_api_request as er

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/info', methods=['POST'])
def calculate():
    # src_city = request.form['sourceCities']
    dest_city = request.form['destinationCities']
    arrival_date = request.form['arrivalDatePicker']
    departure_date = request.form['departureDatePicker']
    result = weather.get_weather_forcast(dest_city,str(arrival_date),str(departure_date))
    return render_template('cityinfo.html', result=result)

    # להכין עוד קובץ פייתון נפרד שמקבל - עיר מקור, עיר יעד, תאריך יציאה, תאריך חזרה
    # הקובץ הוא זה שיקרא לכל הפונקציות (חוץ מהתחזית אולי) ויחזיר בחזרה סטרינג אחד מסודר יפה


if __name__ == '__main__':
    app.run(debug=True)
