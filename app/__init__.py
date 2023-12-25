from datetime import timedelta

from flask import Flask

from .admin_tools.sqlalchemy_data_model_visualizer import generate_data_model_diagram, add_web_font_and_interactivity
from .extensions import api_manager, db, migrate, jwt, ma
from app.api.v1 import *
from .models.ORM import User, Store


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@127.0.0.1:3306/seller_auto'
    app.config["SQLALCHEMY_ECHO"] = True

    app.config['JWT_SECRET_KEY'] = 'asu72fa8a7bcyqcnu298cu12n7cynn8o'
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)

    # models = [User, Store]
    # output_file_name = 'my_data_model_diagram'
    # generate_data_model_diagram(models, output_file_name)
    # add_web_font_and_interactivity('my_data_model_diagram.svg', 'my_interactive_data_model_diagram.svg')

    db.init_app(app)
    jwt.init_app(app)
    ma.init_app(app)

    # flask db migrate
    # flask db upgrade
    migrate.init_app(app, db)

    api_manager.init_app(app)

    return app
