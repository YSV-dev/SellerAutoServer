from flask import Flask
from .extensions import api_manager, db, migrate, jwt
from app.api.v1.auth import ns
from .models import User
from .models.models_tools import ModelTools


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@127.0.0.1:3306/seller_auto'
    app.config["SQLALCHEMY_ECHO"] = True

    api_manager.init_app(app)
    db.init_app(app)
    jwt.init_app(app)

    # flask db migrate
    # flask db upgrade
    migrate.init_app(app, db)

    ModelTools.get_api_model(User)

    return app
