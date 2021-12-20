import logging
from typing import Optional

from django.db.models import QuerySet
from elasticsearch_dsl import Q
from marketplace.models import Product

from .documents import ProductDocument


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


def find_all_matches(query, page_size=20):
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
    search = ProductDocument.search().query(search_query).extra(size=page_size).highlight_options(order='score')
    qs: QuerySet = search.to_queryset()
    return qs
