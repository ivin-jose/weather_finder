from flask import Flask, render_template, flash, request, redirect, jsonify
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from datetime import datetime, date
import requests
# Flask Instance
app = Flask(__name__)

# The Secrete key
app.config['SECRET_KEY'] = "is my secret key"

@app.route('/', methods = ["POST","GET"])
def index():
	return render_template('index.html')


@app.route('/find_weather', methods=["POST", "GET"])
def find_weather():
	city = ''
	error_msg = ''
	general = ''
	temp = ''
	temperature = ''
	temp_kelvin = ''
	icon = ''
	if request.method == 'POST':
		city = request.form.get('city_name')
		daily_weather_url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid=";
		current_weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=";
		daily_weather_data = requests.get(daily_weather_url).json()
		current_weather_data = requests.get(current_weather_url).json()
		try:
			general = current_weather_data['weather'][0]['main']
			temp =  current_weather_data['main']['temp']
			temperature = round(temp - 273.15)
			icon_id =  current_weather_data['weather'][0]['icon']
			icon = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
		except:
			error_msg = "City not found"
	return render_template('index.html', city = city, error_msg = error_msg, temp = temperature,
		icon = icon, general = general, temp_kelvin = temp)