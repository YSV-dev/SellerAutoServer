from flask import Blueprint, Flask
from flask_restx import Api, Namespace

"""
    Данные модуль содержит классы связанные с регистрацией адресов API
    по определенному стандарту
    
    Класс _ApiContainer - создан для хранения данных о структуре API адресов до инициализации приложения.
    Используется исключительно в этом модуле и более нет необходимости использовать его где-то ещё.
    
    Параметры:  api:        Api
                namespaces: list[Namespace]
                
    api - это созданный в ApiManager Api из flask_restx,
    namespace - созданый извне Namespace со всеми действиями для api
    
    ApiManager - класс генератор отдельных API для декомпозиции общего API на регионы, 
    что облегчает процесс разработки и тестирования.
    Страница swagger регистрируется в /docs адреса региона (/v1/account/docs)
    
    Не принимает параметров при инициализации
    
    Поля:
        _api_list: dict[str, _ApiContainer] = {}
        api: Api
        
        _api_list - лист контейнеров с данными API, который заполняется при выполнении метода add_api_region
        api - глобальный API, нужен для работы с декораторами вроде: @api_manager.api.doc().
              Не имеет своей страницы swagger.
        
    Методы:
        init_app - метод инициализации структуры API адресов, запускается в методе create_app стартового файла
        
        Параметры: 
            app: Flask 
            app - инстанс самого приложения
            
        
        _create_url - статический метод генерации url адреса по параметрам
        
        Параметры:
            version: int
            region: str
            
            version - версия API
            region  - регистрируемый регион
            
        Вывод:
            тип: str
            Строка формата f"/v{version}/{region}"
            
        
        add_api_region - метод добавления API регионов с конкретной структурой
            
        Параметры:
            region: str
            version: int
            namespaces: list[Namespace]
            for_desc: str = ''
            **kwargs
            
            region - раздел API
            version - версия API
            namespaces - подраздел API
            for_desc - описание раздела
            
        Вывод:
            тип: Api
            
        get_api_region - метод получения какого-то конкретного раздела API
        
        Параметры:
            version: int
            region: str
            
            version - версия API
            region - раздел
            
        Вывод:
            тип: Api
            
        get_all_api - получить список всех API с ключами и регионами
        
"""


class _ApiContainer:
    def __init__(self, api: Api, namespaces: list[Namespace]):
        self.api = api
        self.namespaces = namespaces


class ApiManager:
    def __init__(self):
        self.app = None

        self._api_container_list: dict[str, _ApiContainer] = {}

    def init_app(self, app: Flask):
        self.app = app

        for api_container in self._api_container_list.values():
            api = api_container.api

            for ns in api_container.namespaces:
                api.add_namespace(ns)

            blueprint: Blueprint = api.blueprint

            url_prefix = blueprint.name

            self.app.register_blueprint(blueprint, url_prefix=url_prefix)

    @staticmethod
    def _create_url(version: int, region: str) -> str:
        url: str = f"/v{version}/{region}"
        return url

    def add_api_region(self, region: str, version: int, namespaces: list[Namespace],
                       for_desc: str = '', **kwargs) -> Api:
        if not version:
            raise ValueError('Version must be specified')

        if version < 1:
            raise ValueError('Version cannot be specified below 1')

        if not region:
            raise ValueError('Region must be specified')

        formatted_version = '{:.1f}'.format(version)
        kwargs['version'] = formatted_version

        if not kwargs.get('title'):
            kwargs['title'] = f"{formatted_version}/{region}"

        url_prefix: str = self._create_url(version, region)

        kwargs['doc'] = f'/docs'

        if not kwargs.get('description'):
            kwargs['description'] = f"API version: {formatted_version}\nRegion: {region}\nFor: {for_desc}"

        blueprint = Blueprint(url_prefix, __name__)
        api: Api = Api(blueprint, **kwargs)

        api_res = _ApiContainer(api, namespaces)

        self._api_container_list[url_prefix] = api_res
        return api

    def get_api_region(self, version: int, region: str) -> Api:
        return self._api_container_list[self._create_url(version, region)].api

    def get_all_api(self) -> dict:
        result: dict[str, Api] = dict[str, Api]()
        for api_c in self._api_container_list:
            result[api_c] = self._api_container_list[api_c].api
        return result
