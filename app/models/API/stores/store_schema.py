from flask_marshmallow import sqla

from app.models.ORM import Store


class StoreSchema(sqla.SQLAlchemyAutoSchema):
    class Meta:
        model = Store
        exclude = ['api_key_hash']
