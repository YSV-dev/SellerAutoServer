from flask import Flask
from .extensions import api_manager, db, migrate, jwt, ma, blueprint, blueprint2  # , api_manager2
from app.api import *


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@127.0.0.1:3306/seller_auto'
    app.config["SQLALCHEMY_ECHO"] = True

    #db.init_app(app)
    jwt.init_app(app)
    ma.init_app(app)

    # flask db migrate
    # flask db upgrade
    migrate.init_app(app, db)

    app.register_blueprint(blueprint, url_prefix='/v1')
    app.register_blueprint(blueprint2, url_prefix='/v2')
    #api_manager.init_app(app)

    #api_manager2.init_app(app)

    return app
