import abc
import os

from elasticsearch import Elasticsearch


class ElasticBase:
    @abc.abstractmethod
    def __init__(self):
        self.client = Elasticsearch(os.getenv('ELASTIC_URL', 'http://localhost:9200'))

    @abc.abstractmethod
    def create_index(self):
        pass

    @abc.abstractmethod
    def insert_data(self, data: dict):
        pass

    @abc.abstractmethod
    def search_data(self, query: str, page_size: int, page: int):
        pass
