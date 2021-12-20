from django.db.models import Prefetch
from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from marketplace.models import Product
from marketplace.models import ProductPage


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
        # related_models = [ProductPage, ProductState]

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'name',
            'description',
        ]

    def get_queryset(self):
        return super().get_queryset().prefetch_related(Prefetch('productpage_set',
                                                                queryset=ProductPage.objects.all(),
                                                                to_attr='product_pages'),
                                                       Prefetch('product_pages__productstate_set',
                                                                to_attr='product_state'))
