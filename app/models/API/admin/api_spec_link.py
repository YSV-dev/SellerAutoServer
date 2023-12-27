from flask_restx import fields

from app import api_manager


class ApiSpecLink:
    model = api_manager.api.model('Model', {
        'name': fields.String,
        'link': fields.String,
    })
