from app.models.ORM.abs.base_model import BaseModel


class ModelTools:
    @staticmethod
    def get_api_model(model: type):
        if not issubclass(model, BaseModel):
            raise TypeError("Class is not Model")
'''
            for attr in model.__dict__.items():
            attr_name = attr[0]
            attr_type = type(attr[1])
            if attr_name.startswith('__'):
                continue
            if issubclass(db.Column, Column):
                print(" (+) ", end="")
            else:
                print(" (-) ", end="")
            print(f"{str(attr_name)} {str(attr_type)}")

            print(attr_type.__mro__)
            print('-----------------------')
            print(Column.__mro__)
            break
'''

