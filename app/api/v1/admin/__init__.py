from flask_restx import Api

from app.api.v1.admin.dev import ns as dev_ns
from app.extensions import api_manager

namespaces = [dev_ns]

admin_api: Api = api_manager.add_api_region('admin', 1, namespaces, 'Регион для администраторов')