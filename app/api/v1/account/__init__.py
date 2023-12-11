from flask_restx import Namespace, Resource

from app.api.api_tools.api_tools import API_Tools
from app.api.v1.account.get_all_users import GetAllUsers
from app.extensions import api_manager

PATH: str = API_Tools.get_api_path(__name__)

ns = Namespace(PATH)
ns.add_resource(GetAllUsers, '/test')

api_manager.add_namespace(ns)


@ns.route('/sign_up')
class SignUp(Resource):
    def post(self):
        return {"Hello": "RestX"}


# test
# @ns.route('/getAllUsers')
# class GetAllUsers(Resource):
#     def get(self):
#         users = User.query.all()
#         return UserSchema.dump(users, many=True), 200
