from app.extensions import db
from app.models.ORM.abs.base_model import BaseModel


class Store(BaseModel):
    __tablename__ = 'stores'
    __tableargs__ = {
        'comment': 'Магазины пользователей'
    }

    store_id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    shop_name = db.Column(db.String(50), nullable=False)
    addition_date = db.Column(db.DateTime(), nullable=False, comment='Дата добавления магазина в систему')
    api_key_hash = db.Column(db.String(512), nullable=False, comment='Закешированный ключ API от магазина')
