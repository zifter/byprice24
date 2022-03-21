import logging
from typing import Optional
from typing import Tuple

from django.db.models import QuerySet
from django_elasticsearch_dsl.search import Search
from elasticsearch_dsl import Q
from marketplace.models import Product

from .documents import ProductDocument
from .raw_queries import SELECT_PRODUCT_WITH_PAGES_AND_STATES
from .raw_queries import SELECT_PRODUCT_WITH_PAGES_AND_STATES_ORDER_BY_PRICE_ASC
from .raw_queries import SELECT_PRODUCT_WITH_PAGES_AND_STATES_ORDER_BY_PRICE_DESC


def threshold(title: str) -> float:
    return min(len(title) * 0.30, 5.0)  # magic


def find_closest_product(title: str) -> Optional[Product]:
    search_query = Q(
        'multi_match',
        query=title,
        fields=[
            'name',
            'description',
        ],
        fuzziness='auto',
    )

    search = ProductDocument.search().query(search_query).extra(size=5).highlight_options(order='score')
    qs: QuerySet = search.to_queryset()

    result: Optional[Product] = None
    hits = [hit for hit in search]

    logging.info('found %s', hits)
    if len(hits):
        hit = hits[0]

        title_threshold = threshold(title)
        logging.info('score %s, threshold %s', hit.meta.score, title_threshold)
        if hit.name == title or hit.meta.score > title_threshold:
            result = qs.first()

    return result


class ProductElasticSearch:
    @staticmethod
    def get(query: str, page: int, page_size: int) -> Search:
        search_query: dict = ProductElasticSearch.get_search_query(query)
        pagination_settings: dict = ProductElasticSearch.get_pagination_settings(page, page_size)

        search = ProductDocument.search().query(search_query).extra(**pagination_settings). \
            highlight_options(order='score')

        return search

    @staticmethod
    def get_search_query(query) -> dict:
        search_query = Q(
            'multi_match',
            query=query,
            fields=[
                'name',
                'description'
            ],
            fuzziness='auto',
            max_expansions=50,
            auto_generate_synonyms_phrase_query=True
        )
        return search_query

    @staticmethod
    def get_pagination_settings(page: int, page_size: int) -> dict:
        return dict(from_=page_size * (page - 1) if page > 1 else 0,
                    size=page_size)


class ProductSearch:
    ORDERING_SETTINGS = {
        'price_desc': SELECT_PRODUCT_WITH_PAGES_AND_STATES_ORDER_BY_PRICE_DESC,
        'price_asc': SELECT_PRODUCT_WITH_PAGES_AND_STATES_ORDER_BY_PRICE_ASC
    }

    def get_queryset(self, query: str, page: int, page_size: int, ordering: str) -> Tuple[QuerySet, int]:
        ids, count = self.get_ids_of_matched_products(query, page, page_size)
        if ids:
            raw_query = SELECT_PRODUCT_WITH_PAGES_AND_STATES
            if ordering in self.ORDERING_SETTINGS.keys():
                raw_query = self.ORDERING_SETTINGS[ordering]

            return Product.objects.raw(raw_query, [tuple(ids)]), count

        return Product.objects.none(), count

    def get_ids_of_matched_products(self, query: str, page: int, page_size: int) -> Tuple[list, int]:
        search = ProductElasticSearch.get(query, page, page_size)

        count = search.count()
        product_ids = []
        for product in search.execute():
            product_ids.append(product.meta.id)

        return product_ids, count


class ProductSearchAutocomplete:
    def get_queryset(self, query: str, page: int, page_size: int) -> QuerySet:
        return ProductElasticSearch.get(query, page, page_size).to_queryset()
