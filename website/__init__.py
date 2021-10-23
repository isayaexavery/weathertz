import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db = SQLAlchemy()
DB_NAME = "weather.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'SECRET_KEY'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .add_data import add_data
    from .from_openwether import open_weather

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(add_data, url_prefix='/')
    app.register_blueprint(open_weather, url_prefix='/')

    from .models import User
    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not os.path.exists('website/'+DB_NAME):
        db.create_all(app=app)
        print('Database created')
