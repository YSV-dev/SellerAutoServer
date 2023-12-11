from flask_marshmallow import sqla

from app.models.ORM import User


class UserSchema(sqla.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        exclude = ['password_hash']
