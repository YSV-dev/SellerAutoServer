from flask_restx import fields

from app.extensions import db, api_manager
from app.models.API.types.filed_types import DateField
from app.models.ORM.abs.base_model import BaseModel
from app.models.ORM.abs.column_types import NonApiColumn, Column


class User(BaseModel):
    __tablename__ = 'users'
    __tableargs__ = {
        'comment': 'Пользователи сервиса'
    }

    user_id = Column(db.Integer, primary_key=True, autoincrement=True)
    login = Column(db.String(255), unique=True)
    password_hash = NonApiColumn(db.String(512))
    email = Column(db.String(255), unique=True)
    first_name = Column(db.String(150))
    second_name = Column(db.String(150))
    middle_name = Column(db.String(150))
    birth_date = Column(db.DateTime())
    registration_date = Column(db.DateTime())
    last_login_date = Column(db.DateTime())
    last_action_date = Column(db.DateTime())

    stores = db.relationship('Store', backref='users', lazy=True)

    default_user_api_model = api_manager.model('User', {
        "user_id": fields.Integer,
        "login": fields.String,
        "first_name": fields.String,
        "last_name": fields.String,
        "middle_name": fields.String,
        "birth_date": DateField,
        "registration_date": DateField,
        "last_login_date": DateField,
        "last_action_date": DateField
    })

    def __repr__(self):
        return f'<User id={self.user_id} user_name={self.second_name + " " + self.first_name + " " + self.middle_name}>'

