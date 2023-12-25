from flask_restx import Namespace

from app.api.v1.account.auth.sign_up import SignUp
from app.api.v1.account.auth.sign_in import SignIn

ns = Namespace('/auth', description='авторизация пользователей')
ns.add_resource(SignUp, '/sign_up')
ns.add_resource(SignIn, '/sign_in')
