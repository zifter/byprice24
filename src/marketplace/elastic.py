from typing import List

from common.elastic.elastic import ElasticManager
from django.db.models import Prefetch
from marketplace.models import ProductPage

ELASTICSEARCH_PRODUCT_INDEX_NAME = 'product'


class ElasticProductLoader:
    @classmethod
    def load(cls, product):
        transformed_product = cls.transform(product)
        return ElasticManager(ELASTICSEARCH_PRODUCT_INDEX_NAME).insert_data(transformed_product)

    @classmethod
    def transform(cls, product) -> dict:
        return {
            'product': {
                'id': product.id,
                'name': product.name,
                'category': product.category,
                'description': product.description,
                'preview_url': product.preview_url},
            'product_page': {
                'marketplaces_count_instock': len(cls.get_offers(product)),
                'min_offer': min(cls.get_offers(product), key=lambda x: x['price'])
            }
        }

    @staticmethod
    def get_offers(product) -> List[dict, ]:
        price_offers = []
        product_pages = ProductPage.objects.filter(product=product).prefetch_related(
            Prefetch('productstate_set',
                     to_attr='product_state'))

        for page in product_pages:
            product_state = max(page.product_state, key=lambda x: x.created)
            price_offers.append(dict(price=float(product_state.price),
                                     price_currency=product_state.price_currency))

        return price_offers
