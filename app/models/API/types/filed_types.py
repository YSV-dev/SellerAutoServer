from flask_restx import fields


class DateField(fields.Raw):
    def format(self, value):
        return value.strftime('%d-%m-%Y')
