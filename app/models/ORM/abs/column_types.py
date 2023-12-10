from app.extensions import db


class NonApiColumn(db.Column):
    """
        Этот класс используется для обозначения полей модели,
        которые не будут автоматически включаться в модель API
    """
    pass


class Column(db.Column):
    """
        Этот класс используется для обозначения общих полей модели
    """
    pass
