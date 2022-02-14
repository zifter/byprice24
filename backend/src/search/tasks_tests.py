import pytest
from search.models import QueryHistory
from search.tasks import push_query


@pytest.mark.django_db
def test_push_query_into_postgres():
    params = dict(query='apple', number_found_products=25)
    obj = push_query(**params)
    assert obj == QueryHistory.objects.get(**params)
