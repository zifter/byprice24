from common.elastic.base import ElasticBase


def get_search_settings(query):
    return {
        'match': {
            'product.name': {
                'query': query,
                'fuzziness': 'AUTO',
                'max_expansions': 50,
                'auto_generate_synonyms_phrase_query': True
            }
        }
    }


class ElasticManager(ElasticBase):
    def __init__(self, index_name):
        super().__init__()
        self.index_name = index_name
        self.create_index_if_not_exists()

    def create_index_if_not_exists(self) -> bool:
        if not self.client.indices.exists(index=self.index_name):
            return self.client.indices.create(index=self.index_name)

    def insert_data(self, data: dict) -> dict:
        return self.client.index(index=self.index_name, document=data)

    def search_data(self, query) -> list:
        data = self.client.search(index=self.index_name, query=get_search_settings(query))
        return data['hits']['hits']
