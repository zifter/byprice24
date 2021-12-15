from marketplace.fixtures.elastic import EMPTY_LIST_ELASTIC_FIXTURE
from marketplace.fixtures.elastic import EXACT_MATCH_ELASTIC_FIXTURE
from marketplace.fixtures.elastic import FULL_PAGINATION_FIXTURE
from marketplace.fixtures.elastic import LIST_MATCHES_ELASTIC_FIXTURE
from marketplace.fixtures.elastic import NOT_FULL_SCROLL_FIXTURE


def mock_es_creation(*args, **kwargs):
    return None


def mock_create(*args, **kwargs):
    return None


def mocked_list_ok_elastic(*args, **kwargs):
    return LIST_MATCHES_ELASTIC_FIXTURE


def mocked_exact_match_elastic(*args, **kwargs):
    return EXACT_MATCH_ELASTIC_FIXTURE


def mocked_empty_match_elastic(*args, **kwargs):
    return EMPTY_LIST_ELASTIC_FIXTURE


def mock_full_pagination(*args, **kwargs):
    return FULL_PAGINATION_FIXTURE


def mock_not_full_pagination(*args, **kwargs):
    return NOT_FULL_SCROLL_FIXTURE
