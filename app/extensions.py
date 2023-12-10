from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_restx import Api

api_manager = Api()
db = SQLAlchemy()
jwt = JWTManager()
migrate = Migrate()




