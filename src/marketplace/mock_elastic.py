from marketplace.fixtures.elastic import EMPTY_LIST_ELASTIC_FIXTURE
from marketplace.fixtures.elastic import LIST_MATCHES_ELASTIC_FIXTURE
from marketplace.fixtures.elastic import NOT_FULL_PAGINATION_ELASTIC_FIXTURE


def mocked_list_ok_elastic(*args, **kwargs):
    return LIST_MATCHES_ELASTIC_FIXTURE


def mocked_not_full_pagintaion(*args, **kwargs):
    return NOT_FULL_PAGINATION_ELASTIC_FIXTURE


def mocked_empty_match_elastic(*args, **kwargs):
    return EMPTY_LIST_ELASTIC_FIXTURE


def mocked_elastic_manager(*args, **kwargs):
    return None
