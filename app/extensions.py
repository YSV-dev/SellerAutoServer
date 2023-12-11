from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_restx import Api
from flask_marshmallow import Marshmallow

api_manager = Api(title='API v1',  prefix="/api/v1", doc="/api/v1", description='base api', version="1.0")
db = SQLAlchemy()
jwt = JWTManager()
migrate = Migrate()
ma = Marshmallow()




