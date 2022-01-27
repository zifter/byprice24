from search.models import QueryHistory

query_history = QueryHistory(
    query='apple',
    number_found_products=25
)


def test_query_history_is_printable_ok():
    assert 'apple [25]' in str(query_history)
