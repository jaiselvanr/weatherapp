from flask import Flask, render_template, request
import requests
from datetime import datetime

app = Flask(__name__)
API_KEY = '187155cbcd8f493abd5d17c80edf98b4'

def get_weather_by_city(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def get_weather_by_coords(lat, lon):
    url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def get_forecast(lat, lon):
    url = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=current,minutely,hourly,alerts&appid={API_KEY}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

@app.template_filter('datetimeformat')
def datetimeformat(value, format='%a, %b %d'):
    return datetime.fromtimestamp(value).strftime(format)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    forecast_data = None

    if request.method == 'POST':
        city = request.form.get('city')
        lat = request.form.get('lat')
        lon = request.form.get('lon')

        if lat and lon:
            weather_json = get_weather_by_coords(lat, lon)
        elif city:
            weather_json = get_weather_by_city(city)
        else:
            return render_template('index.html', weather={'error': 'Please enter a city or use your location'})

        if weather_json:
            lat = weather_json['coord']['lat']
            lon = weather_json['coord']['lon']
            forecast_json = get_forecast(lat, lon)

            weather_data = {
                'city': weather_json['name'],
                'temperature': weather_json['main']['temp'],
                'description': weather_json['weather'][0]['description'],
                'icon': weather_json['weather'][0]['icon'],
            }

            if forecast_json:
                forecast_data = forecast_json['daily'][:7]

        else:
            weather_data = {'error': 'Weather data not found'}

    return render_template('index.html', weather=weather_data, forecast=forecast_data)

if __name__ == '__main__':
    app.run(debug=True,port=50011)
