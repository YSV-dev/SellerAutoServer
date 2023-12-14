from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_restx import Api
from flask_marshmallow import Marshmallow

blueprint = Blueprint('api', __name__)
blueprint2 = Blueprint('api2', __name__)

api_manager = Api(blueprint, title='API v1', description='base api', version="1.0", doc='/docs')
api_manager2 = Api(blueprint2, title='API v2', description='base api 2', version="2.0", doc='/docs')
#blueprint2 = Blueprint('api', __name__, url_prefix='/api/v2')
#api_manager2 = Api(blueprint, title='API v2',  doc="/api/v2", description='base api 2', version="2.0")
db = SQLAlchemy()
jwt = JWTManager()
migrate = Migrate()
ma = Marshmallow()




