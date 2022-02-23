from datetime import datetime

import pytest
from common.shared_queue.structs import QueryRequest
from search.models import QueryHistory
from search.tasks import push_query


@pytest.mark.django_db
def test_push_query_into_postgres():
    request = QueryRequest(
        query='apple',
        result_count=25,
        timestamp=datetime.now(),
    )
    obj = push_query(request)
    assert obj == QueryHistory.objects.get(query=request.query)
