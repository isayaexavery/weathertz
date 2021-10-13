import requests
import math
from flask import Blueprint, render_template, request
from .models import User, Regions, Forecast
from . import db
from flask.helpers import url_for
from werkzeug.utils import redirect
from datetime import date
import time
import os
from dotenv import load_dotenv
load_dotenv()


views = Blueprint('views', __name__)

OWN_Endpoint = os.environ.get("OWM_Endpoint")
API_KEY = os.getenv("API_KEY")


@views.route("/", methods=['GET', 'POST'])
def home():
    # default region
    region = "dodoma"
    if request.method == 'POST':
        region = request.form.get('region').lower()

    region_details = Regions.query.filter_by(name=region).first()

    lat = region_details.lat
    lon = region_details.lon
    weather_params = {
        "lat": lat,
        "lon": lon,
        "appid": API_KEY,
        "exclude": "current,minutely,hourly",
        "units": "metric",

    }
    response = requests.get(OWN_Endpoint, params=weather_params)
    response.raise_for_status()
    weather_data = response.json()
    weather_slice = weather_data["daily"][:1][0]  # today
    weather_slice_2 = weather_data["daily"][1:2][0]  # tommorrow

    dt = time.strftime('%A, %d %b', time.localtime(weather_slice["dt"]))
    dt_tomorrow = time.strftime('%A, %d %b', time.localtime(weather_slice_2["dt"]))

    sunrise_today = time.strftime('%H%M', time.localtime(weather_slice["sunrise"]))
    sunset_today = time.strftime('%H%M ', time.localtime(weather_slice["sunset"]))
    sunrise_tom = time.strftime('%H%M', time.localtime(weather_slice_2["sunrise"]))
    sunset_tom = time.strftime('%H%M ', time.localtime(weather_slice_2["sunset"]))

    all_regions = Regions.query.filter_by()

    return render_template("home.html", weather_data=weather_slice, weather_tom=weather_slice_2,
                           region=region, datetime=dt, datetime_tom=dt_tomorrow,
                           sunrise=sunrise_today, sunset=sunset_today, sunrise_tom=sunrise_tom, sunset_tom=sunset_tom,
                           all_regions=all_regions
                           )


@views.route("/search", methods=['GET', 'POST'])
def search():

    if request.method == 'POST':
        region = request.form.get('region').lower()
        regions_search = Regions.query.filter(Regions.name.like('%'+region+'%')).all()

        return render_template("search.html", details=regions_search)

    return redirect(url_for('views.home'))


@views.route("/contact")
def contact():
    all_regions = Regions.query.filter_by()
    return render_template("contact.html", all_regions=all_regions)
