from app.extensions import db
from app.models.ORM.abs.base_model import BaseModel
from app.models.ORM.abs.column_types import Column


class Store(BaseModel):
    __tablename__ = 'stores'
    __tableargs__ = {
        'comment': 'Магазины пользователей'
    }

    store_id = Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    owner_id = Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    shop_name = Column(db.String(50), nullable=False)
    addition_date = Column(db.DateTime(), nullable=False, comment='Дата добавления магазина в систему')
    api_key_hash = Column(db.String(512), nullable=False, comment='Закешированный ключ API от магазина')
