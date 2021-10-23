from . import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    user_name = db.Column(db.String(150))
    contribution = db.Column(db.Integer, default=0)
    profile_image = db.Column(db.Text, default="noImage")
    config = db.Column(db.Text)


class Regions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    lon = db.Column(db.Integer)
    lat = db.Column(db.Integer)
    id_weather = db.Column(db.Integer)
    description = db.Column(db.String(150))
    icon = db.Column(db.String(150))
    temp = db.Column(db.Integer)
    temp_min = db.Column(db.Integer)
    temp_max = db.Column(db.Integer)
    pressure = db.Column(db.Integer)
    humidity = db.Column(db.Integer)
    sea_level = db.Column(db.Integer)
    wind_speed = db.Column(db.Integer)
    dt = db.Column(db.Integer)
    sunrise = db.Column(db.Integer)
    sunset = db.Column(db.Integer)
    day_2 = db.Column(db.String(150))
    day_3 = db.Column(db.String(150))
    day_4 = db.Column(db.String(150))
    day_5 = db.Column(db.String(150))
    day_6 = db.Column(db.String(150))
    day_7 = db.Column(db.String(150))


class Forecast(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.String(150))
    day_2 = db.Column(db.Integer)
    day_3 = db.Column(db.Integer)
    day_4 = db.Column(db.Integer)
    day_5 = db.Column(db.Integer)
    day_6 = db.Column(db.Integer)
    day_7 = db.Column(db.Integer)

    # addd hourl data
