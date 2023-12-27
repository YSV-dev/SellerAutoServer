from flask_restx import Resource
from app.api.api_tools import api


class SignIn(Resource):
    @api.doc(description='Вход в учётную запись')
    def post(self):
        return {}