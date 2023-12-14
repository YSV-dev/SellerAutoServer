from flask import Blueprint
from flask_restx import Api


class ApiManager(object):
    def __init__(self, app=None):
        self.app = app
        self._api_list: dict[str, Api] = {}

    def init_app(self, app):
        self.app = app
        for api in self._api_list.values():
            api.init_app(self.app)

    @staticmethod
    def _create_url(version: int, region: str) -> str:
        url: str = f"/v{version}/{region}"
        return url

    def add_api_region(self, region: str, version: int = 1, for_desc: str = '',  **kwargs) -> Api:
        if version < 1:
            raise ValueError('Version cannot be specified below 1')

        if not region:
            raise ValueError('Region must be specified')

        if not self.app:
            raise RuntimeError('App did`t initialized!')

        formatted_version = '{:.1f}'.format(version)
        kwargs['version'] = formatted_version

        if not kwargs['title']:
            kwargs['title'] = f"{formatted_version}/{region}"

        kwargs['doc'] = '/docs'

        if not kwargs['description']:
            kwargs['description'] = f"API version: {formatted_version}\nRegion: {region}\nFor: {for_desc}"

        url_prefix: str = self._create_url(version, region)

        blueprint = Blueprint(url_prefix, __name__)
        api = Api(blueprint, **kwargs)
        self.app.register_blueprint(blueprint, url_prefix=url_prefix)

        self._api_list[url_prefix] = api
        return api

    def get_api_region(self, version: int, region: str) -> Api:
        return self._api_list[self._create_url(version, region)]
