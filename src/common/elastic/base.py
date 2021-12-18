import abc

from cms import settings
from elasticsearch import Elasticsearch


class ElasticBase:
    @abc.abstractmethod
    def __init__(self):
        url = settings.ELASTICSEARCH_DSL['default']['hosts']
        self.client = Elasticsearch(url)

    @abc.abstractmethod
    def create_index(self):
        pass

    @abc.abstractmethod
    def insert_data(self, data: dict):
        pass

    @abc.abstractmethod
    def search_data(self, query: str, page_size: int, page: int):
        pass
