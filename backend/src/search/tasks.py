from django_rq import job
from search.models import QueryHistory


@job
def push_query(query: str, number_found_products: int):
    return QueryHistory.objects.create(query=query.lower(), number_found_products=number_found_products)
