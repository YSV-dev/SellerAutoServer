from abc import ABC


class ApiDevService(ABC):
    @staticmethod
    def get_api_spec_list() -> dict[str, str]:
        return {'ХУЙ': 'ХУЙ'}

