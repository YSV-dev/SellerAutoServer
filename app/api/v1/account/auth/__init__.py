from flask_restx import Namespace

from app.api.v1.account.auth.sign_up import SignUp

ns = Namespace('/auth')
ns.add_resource(SignUp, '/sign_up')
