import http.client
from collections import OrderedDict
from unittest.mock import Mock
from unittest.mock import patch

from django.test import TestCase
from search.mock_elastic import mocked_elastic_manager
from search.mock_elastic import mocked_empty_match_elastic
from search.mock_elastic import mocked_list_ok_elastic
from search.mock_elastic import mocked_not_full_pagintaion
from search.views import SearchProductViewSet


class ProductViewTestCase(TestCase):
    fixtures = ['test/marketplaces.yaml', 'test/products.yaml', 'test/product_pages.yaml', 'test/product_states.yaml', ]
    expected = {'count': 2,
                'next_page': 2,
                'previous_page': 0,
                'results': [
                    OrderedDict(
                        [('id', 1),
                         ('name', 'Acer Extensa 15 EX215-53G-7014 NX.EGCER.009'),
                         ('category', 'notebook'),
                         ('description', ''),
                         ('preview_url', None),
                         ('min_offer', OrderedDict([('price', '340.30'),
                                                    ('price_currency', 'BYN')])),
                         ('marketplaces_count_instock', 1)]),
                    OrderedDict(
                        [('id', 2),
                         ('name', 'Acer Extensa 15 EX215-52-54D6 NX.EG8ER.00V'),
                         ('category', 'notebook'),
                         ('description', ''),
                         ('preview_url', None),
                         ('min_offer', OrderedDict([('price', '580.30'),
                                                    ('price_currency', 'BYN')])),
                         ('marketplaces_count_instock', 1)])]}

    def setUp(self) -> None:
        self.patcher = patch('common.elastic.elastic.ElasticManager.__init__', mocked_elastic_manager)
        self.patcher.start()

    def tearDown(self) -> None:
        self.patcher.stop()

    @patch('common.elastic.elastic.ElasticManager.search_data', mocked_list_ok_elastic)
    @patch('common.shared_queue.get_flow_queue', (lambda: Mock())())
    def test_products_search_list_ok(self):
        response = self.client.get('/api/v1/search/products',
                                   data={'query': 'Acer'})
        self.assertEqual(len(response.data['results']), 2)

        self.assertEqual(response.data, self.expected)

    @patch('common.elastic.elastic.ElasticManager.search_data', mocked_list_ok_elastic)
    @patch('common.shared_queue.get_flow_queue', (lambda: Mock())())
    def test_get_product_full_search_ok(self):
        response = self.client.get('/api/v1/search/products',
                                   data={'query': 'Acer Extensa 15 EX215-53G-7014 NX.EGCER.009'})
        self.assertEqual(response.data, self.expected)

    @patch('common.elastic.elastic.ElasticManager.search_data', mocked_not_full_pagintaion)
    @patch('common.shared_queue.get_flow_queue', (lambda: Mock())())
    def test_pagination_not_full_page(self):
        SearchProductViewSet.page_size = 1
        response = self.client.get('/api/v1/search/products',
                                   data={'query': 'acer',
                                         'page': 2})
        self.assertEqual(response.data['count'], 2)
        self.assertEqual(len(response.data['results']), 1)

    @patch('common.elastic.elastic.ElasticManager.search_data', mocked_empty_match_elastic)
    @patch('common.shared_queue.get_flow_queue', (lambda: Mock())())
    def test_get_products_empty_list(self):
        response = self.client.get('/api/v1/search/products', data={'query': 'Apple'})
        self.assertEqual(response.data, {'count': 0,
                                         'next_page': 2,
                                         'previous_page': 0,
                                         'results': []})

    @patch('common.shared_queue.get_flow_queue', (lambda: Mock())())
    def test_fail_search_too_short_query(self):
        response = self.client.get('/api/v1/search/products', data={'query': 'A'})
        self.assertEqual(response.status_code, http.client.BAD_REQUEST)

    @patch('common.shared_queue.get_flow_queue', (lambda: Mock())())
    def test_fail_search_no_query(self):
        response = self.client.get('/api/v1/search/products')
        self.assertEqual(response.status_code, http.client.BAD_REQUEST)