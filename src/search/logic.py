import logging
from typing import Optional

from django.db.models import QuerySet
from django_elasticsearch_dsl.search import Search
from elasticsearch_dsl import Q
from marketplace.models import Product

from .documents import ProductDocument
from .raw_queries import SELECT_PRODUCT_WITH_PAGES_AND_STATES


def threshold(title: str) -> float:
    return min(len(title) * 0.30, 5.0)  # magic


def get_search_query(query):
    return


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
            result = list(qs)[0]

    return result


class SearchProduct:
    def __init__(self, query: str, page: int, page_size: int):
        self.query = query
        self.page = page
        self.page_size = page_size

        self._count = 0

    def get_queryset(self) -> QuerySet:
        ids = self.get_ids_of_matched_products()
        if ids:
            queryset = Product.objects.raw(SELECT_PRODUCT_WITH_PAGES_AND_STATES, [tuple(ids)])
            return queryset
        return Product.objects.none()

    def get_ids_of_matched_products(self) -> list:
        search = self.find_all_matches()

        product_ids = []
        for product in search.execute():
            product_ids.append(product.meta.id)
        return product_ids

    def find_all_matches(self) -> Search:
        search_query: dict = self.get_search_query()
        pagination_settings: dict = self.get_pagination_settings()

        search = ProductDocument.search().query(search_query).extra(**pagination_settings). \
            highlight_options(order='score')

        self.count = search.count()
        return search

    def get_search_query(self) -> dict:
        search_query = Q(
            'multi_match',
            query=self.query,
            fields=[
                'name',
                'description'
            ],
            fuzziness='auto',
            max_expansions=50,
            auto_generate_synonyms_phrase_query=True
        )
        return search_query

    def get_pagination_settings(self) -> dict:
        return dict(from_=self.page_size * self.page if self.page > 1 else 0,
                    size=self.page_size)

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = int(value)

    @count.getter
    def count(self):
        return self._count
