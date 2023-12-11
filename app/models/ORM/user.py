from flask_restx import fields

from app.extensions import db, api_manager
from app.models.API.types.filed_types import DateField
from app.models.ORM.abs.base_model import BaseModel


class User(BaseModel):
    __tablename__ = 'users'
    __tableargs__ = {
        'comment': 'Пользователи сервиса'
    }

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    login = db.Column(db.String(255), unique=True)
    password_hash = db.Column(db.String(512))
    email = db.Column(db.String(255), unique=True)
    first_name = db.Column(db.String(150))
    second_name = db.Column(db.String(150))
    middle_name = db.Column(db.String(150))
    birth_date = db.Column(db.DateTime())
    registration_date = db.Column(db.DateTime())
    last_login_date = db.Column(db.DateTime())
    last_action_date = db.Column(db.DateTime())

    stores = db.relationship('Store', backref='users', lazy=True)

    def __repr__(self):
        return f'<User id={self.user_id} user_name={self.second_name + " " + self.first_name + " " + self.middle_name}>'

