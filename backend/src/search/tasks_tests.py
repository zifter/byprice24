import datetime

import pytest
from common.shared_queue.structs import QueryRequest
from search.models import QueryHistory
from search.tasks import push_query


@pytest.mark.django_db
def test_push_query_into_postgres():
    params_obj = QueryRequest(query='apple', result_count=25, timestamp=datetime.datetime.now())
    obj = push_query(params_obj)
    assert obj == QueryHistory.objects.get(query=params_obj.query,
                                           number_found_products=params_obj.result_count,
                                           timestamp=params_obj.timestamp)
