from flask import Flask, render_template, flash, request, redirect
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from datetime import datetime, date
# Flask Instance
app = Flask(__name__)

# The Secrete key
app.config['SECRET_KEY'] = "is my secret key"

@app.route('/')
def index():
	return render_template('index.html')