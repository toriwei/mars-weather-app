from flask import render_template
from app import app
import requests
import json

@app.route('/')
@app.route('/index')
def index():
    r = requests.get('https://api.nasa.gov/insight_weather/?api_key=xkULB89iqgimCCzD33SPByislVEhjaVbo714bJxN&feedtype=json&ver=1.0')
    
    return render_template('index.html', obj = json.loads(r.text), title = "Weather on Mars")
