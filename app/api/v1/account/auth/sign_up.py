from flask_restx import Resource


class SignUp(Resource):
    def post(self):
        return {"Hello": "RestX"}
