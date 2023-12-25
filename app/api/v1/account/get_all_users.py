from flask_restx import Resource

from app.models.API.users import UserSchema
from app.models.ORM import User


class Users(Resource):
    def get(self):
        users = User.query.all()
        return UserSchema().dump(users, many=True), 200
