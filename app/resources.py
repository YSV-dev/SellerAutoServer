from flask_restx import Resource, Namespace

ns = Namespace("api")


@ns.route("/hello")
class Hello(Resource):
    def get(self):
        return {"Hello": "RestX"}

@ns.route('/sign_up')
class SignUp(Resource):
    def post(self):
        return {"Hello": "RestX"}
