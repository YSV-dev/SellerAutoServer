from flask_restx import Namespace, Resource
from app.api.api_tools import API_Tools
from app.extensions import api_manager
from app.models.ORM.user import User

PATH: str = API_Tools.get_api_path(__name__)
ns = Namespace(PATH)

api_manager.add_namespace(ns)


@ns.route('/sign_up')
class SignUp(Resource):
    def post(self):
        return {"Hello": "RestX"}


# test
@ns.route('/getAllUsers')
class GetAllUsers(Resource):
    @ns.marshal_list_with(User.default_user_api_model)
    def get(self):
        return User.query.all()
