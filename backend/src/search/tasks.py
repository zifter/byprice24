from common.shared_queue.structs import QueryRequest
from django_rq import job
from search.models import QueryHistory


@job
def push_query(obj: QueryRequest):
    return QueryHistory.objects.create(query=obj.query, number_found_products=obj.result_count, timestamp=obj.timestamp)
