from flask_restx import Resource

from app import api_manager


class SignIn(Resource):
    @api_manager.api.doc(description='Вход в учётную запись')
    def post(self):
        return {}