from flask_restx import Namespace

from app.api.v1.account import GetAllUsers
from app.models import API

path_array: list = __name__.split('.')

ns = Namespace(f'/{path_array[-1]}')
ns.add_resource(GetAllUsers, '/test')

API.add_namespace(ns)
