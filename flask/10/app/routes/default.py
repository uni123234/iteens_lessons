from datetime import date, timedelta
import requests
from flask import Blueprint, render_template
from .weather import get_weather_data

bp = Blueprint("default", __name__)

@bp.route("/")
def index():
    mock_data = {}
    weather_data = {}
    for item in range(5):
        event_date = date.today() + timedelta(days=item)
        date_str = event_date.strftime("%d %B")
        mock_data[date_str] = []
        weather = get_weather_data(event_date.strftime("%Y-%m-%d"))
        weather_data[date_str] = weather
        for _ in range(3):
            event = requests.get("https://www.boredapi.com/api/activity/")
            mock_data[date_str].append(event.json().get("activity"))
    return render_template("main.html", data=mock_data, weather_data=weather_data)
