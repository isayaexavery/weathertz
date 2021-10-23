import json

from flask import Blueprint, render_template, request
from .models import User, Regions, Forecast
from . import db

add_data = Blueprint('add_data', __name__)


@add_data.route('/add-first', methods=['GET', 'POST'])
def add_first():
    if request.method == 'POST':
        new_record = Regions(
            name=request.form.get('region').lower(),
            # name='arusha',
            lon=request.form.get('lon').lower(),
            lat=request.form.get('lat').lower(),
            id_weather=request.form.get('id_weather').lower(),
            description=request.form.get('description').lower(),
            icon=request.form.get('icon').lower(),
            temp=request.form.get('temp').lower(),
            temp_min=request.form.get('temp_min').lower(),
            temp_max=request.form.get('temp_max').lower(),
            pressure=request.form.get('pressure').lower(),
            humidity=request.form.get('humidity').lower(),
            wind_speed=request.form.get('speed').lower(),
            dt=request.form.get('datetime').lower(),
            sunrise=request.form.get('sunrise').lower(),
            sunset=request.form.get('sunset').lower(),
            # timezone=request.form.get('timezone').lower(),
        )

        db.session.add(new_record)
        db.session.commit()
        return render_template("add_data.html", message="Success")

    return render_template("add_data.html", message="Fail")


@add_data.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        region_name = request.form.get('region').lower()
        region_data = Regions.query.filter_by(name=region_name).first()
        if region_data is not None:

            region_data.lon = request.form.get('lon').lower()
            region_data.lat = request.form.get('lat').lower()
            region_data.id_weather = request.form.get('id_weather').lower()
            region_data.description = request.form.get('description').lower()
            region_data.icon = request.form.get('icon').lower()
            region_data.temp = request.form.get('temp').lower()
            region_data.temp_min = request.form.get('temp_min').lower()
            region_data.temp_max = request.form.get('temp_max').lower()
            region_data.pressure = request.form.get('pressure').lower()
            region_data.humidity = request.form.get('humidity').lower()
            region_data.wind_speed = request.form.get('speed').lower()
            region_data.dt = request.form.get('datetime').lower()
            region_data.sunrise = request.form.get('sunrise').lower()
            region_data.sunset = request.form.get('sunset').lower()

        # new_record = Regions(
        #     # name=request.form.get('region').lower(),
        #     name='arusha',
        #     lon=request.form.get('lon').lower(),
        #     lat=request.form.get('lat').lower(),
        #     id_weather=request.form.get('id_weather').lower(),
        #     description=request.form.get('description').lower(),
        #     icon=request.form.get('icon').lower(),
        #     temp=request.form.get('temp').lower(),
        #     temp_min=request.form.get('temp_min').lower(),
        #     temp_max=request.form.get('temp_max').lower(),
        #     pressure=request.form.get('pressure').lower(),
        #     humidity=request.form.get('humidity').lower(),
        #     wind_speed=request.form.get('speed').lower(),
        #     dt=request.form.get('datetime').lower(),
        #     sunrise=request.form.get('sunrise').lower(),
        #     sunset=request.form.get('sunset').lower(),
        #     # timezone=request.form.get('timezone').lower(),
        # )
        #
        # # db.session.add(new_record)
        # db.session.merge(new_record)
        db.session.add(region_data)
        db.session.commit()
        return render_template("add_data.html", message="Success")

    return render_template("add_data.html", message="Fail")

#
# @add_data.route('/add-temp', methods=['GET', 'POST'])
# def add_temp():
#     if request.method == 'POST':
#         new_record = Forecast(
#             region=request.form.get('region').lower(),
#             day_2=request.form.get('day2').lower(),
#             day_3=request.form.get('day3').lower(),
#             day_4=request.form.get('day4').lower(),
#             day_5=request.form.get('day5').lower(),
#             day_6=request.form.get('day6').lower(),
#             day_7=request.form.get('day7').lower(),
#             # timezone=request.form.get('timezone').lower(),
#         )
#
#         db.session.add(new_record)
#         # db.session.merge(new_record)
#         # db.session.add(region_data)
#         db.session.commit()
#         return render_template("add_temp.html", message="Success")
#
#     return render_template("add_temp.html", message="Fail")


# @add_data.route('/add', methods=['GET', 'POST'])
# def add_d():
#     if request.method == 'POST':
#
#
#         with open("data_details.json", "r") as data_file:
#             # reading old data
#             data = json.load(data_file)
#
#         name = request.form.get('region').lower()
#         lon = request.form.get('lon').lower()
#         lat = request.form.get('lat').lower()
#         id_weather = request.form.get('id_weather').lower()
#         description = request.form.get('description').lower()
#         icon = request.form.get('icon').lower()
#         temp = request.form.get('temp').lower()
#         temp_min = request.form.get('temp_min').lower()
#         temp_max = request.form.get('temp_max').lower()
#         pressure = request.form.get('pressure').lower()
#         humidity = request.form.get('humidity').lower()
#         wind_speed = request.form.get('speed').lower()
#         dt = request.form.get('datetime').lower()
#         sunrise = request.form.get('sunrise').lower()
#         sunset = request.form.get('sunset').lower()
#         # timezone=request.form.get('timezone').lower(),
#
#         data_details = {
#             name: {
#                 "lat": lat,
#                 "lon": lon,
#                 "day_1": {
#
#                         "dt": dt,
#                         "sunsrise": sunrise,
#                         "sunset": sunset,
#                         "temp": temp,
#                         "min": temp_min,
#                         "max": temp_max,
#                         "pressure": pressure,
#                         "humidity": humidity,
#                         "wind_speed": wind_speed,
#                         "main": "clouds",
#                         "description": description,
#                         "icon": icon
#
#
#                 },
#                 "day_2": {
#
#                     "dt": dt,
#                     "sunsrise": sunrise,
#                     "sunset": sunset,
#                     "temp": temp,
#                     "min": temp_min,
#                     "max": temp_max,
#                     "pressure": pressure,
#                     "humidity": humidity,
#                     "wind_speed": wind_speed,
#                     "main": "clouds",
#                     "description": description,
#                     "icon": icon
#
#                 }
#
#             }
#
#         }
#
#             # updating old data
#         data.update(data_details)
#
#         with open("data_details.json", "w") as data_file:
#             # saving all data old and new
#             json.dump(data, data_file, indent=4)
#
#         return "done"
#
#     return render_template("add_data.html", message="Fail")
