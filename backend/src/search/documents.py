from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from marketplace.models import Category
from marketplace.models import Product


@registry.register_document
class ProductDocument(Document):
    class Index:
        name = 'product'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = Product  # The model associated with this Document
        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'name',
            'description',
        ]


@registry.register_document
class CategoryDocument(Document):
    class Index:
        name = 'category'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = Category
        fields = [
            'name',
            'keywords',
        ]
