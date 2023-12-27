from flask_restx import Namespace

from app.api.v1.admin.dev.spec_api import SpecApi

ns = Namespace('/dev', description='Раздел API для разработки.')
ns.add_resource(SpecApi, '/spec_api_list')
