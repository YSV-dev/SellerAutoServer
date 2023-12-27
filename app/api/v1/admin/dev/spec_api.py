import json

from flask_restx import Resource

from app import api_manager
from app.api.api_tools import api


class SpecApi(Resource):
    @api.doc(description='Получить список регионов API с ссылками')
    def get(self):
        return json.dumps(api_manager.get_all_api())
