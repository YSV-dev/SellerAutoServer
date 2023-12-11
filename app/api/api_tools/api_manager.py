from flask_restx import Api


class ApiManager(object):
    def __init__(self, app=None):
        self.app = app
        self.__api_list: dict[str, Api] = {}

    def init_app(self, app):
        self.app = app
        for api in self.__api_list.values():
            api.init_app(self.app)

    def add_api(self, key: str, **kwargs) -> Api:
        if not key:
            raise ValueError('None key exception')

        # if not self.app:
        #     raise RuntimeError('App did`t initialized!')

        api = Api(**kwargs)

        if self.app:
            api.init_app(self.app)

        self.__api_list[key] = api
        return api

    def get_api(self, key: str) -> Api:
        return self.__api_list[key]
