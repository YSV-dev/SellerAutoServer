from app.api.v1.account.auth import ns as auth_ns
from app.extensions import api_manager

namespaces = [auth_ns]

api_manager.add_api_region('account', 1, namespaces, 'Регион для работы с пользователями')
