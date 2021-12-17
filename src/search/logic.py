from typing import Optional

from django.db.models import QuerySet
from elasticsearch_dsl import Q
from marketplace.models import Product

from .documents import ProductDocument


def threshold(title: str) -> float:
    return min(len(title) * 0.35, 6.0)  # magic


def find_nearest_product(title: str) -> Optional[Product]:
    q = Q(
        'multi_match',
        query=title,
        fields=[
            'name',
            'description',
        ],
        fuzziness='auto',
    )

    search = ProductDocument.search().query(q).extra(size=1).highlight_options(order='score')
    qs: QuerySet = search.to_queryset()

    result: Optional[Product] = None
    hits = [hit for hit in search]
    if len(hits):
        hit = hits[0]
        if hit.name == title or hit.meta.score > threshold(title):
            result = list(qs)[0]

    return result
