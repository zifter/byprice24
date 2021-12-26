import http.client
from collections import OrderedDict
from unittest.mock import Mock
from unittest.mock import patch

from django.test import TestCase


class ProductViewTestCase(TestCase):
    fixtures = ['test/marketplaces.yaml', 'test/products.yaml', 'test/product_pages.yaml', 'test/product_states.yaml', ]
    expected = {'count': 2,
                'next_page': 2,
                'previous_page': 0,
                'results': [
                    OrderedDict([('id', 2),
                                 ('name', 'Acer Extensa 15 EX215-53G-7014 NX.EGCER.009'),
                                 ('category', 'notebook'),
                                 ('description', ''),
                                 ('preview_url', None),
                                 ('marketplaces_count_instock', 2),
                                 ('min_offer', {'price': '340.30', 'price_currency': 'BYN'})]),
                    OrderedDict([('id', 3),
                                 ('name', 'Acer Extensa 15 EX215-54-348Z NX.EGJER.00M'),
                                 ('category', 'notebook'),
                                 ('description', ''),
                                 ('preview_url', None),
                                 ('marketplaces_count_instock', 1),
                                 ('min_offer', {'price': '580.30', 'price_currency': 'BYN'})])]}

    @patch('common.shared_queue.get_flow_queue', (lambda: Mock())())
    def test_products_search_list_ok(self):
        response = self.client.get('/api/v1/search/products',
                                   data={'query': 'Acer'})
        self.assertEqual(len(response.data['results']), 2)
        self.assertEqual(response.data, self.expected)

    @patch('common.shared_queue.get_flow_queue', (lambda: Mock())())
    def test_pagination_not_full_page(self):
        response = self.client.get('/api/v1/search/products',
                                   data={'query': 'acer',
                                         'page': 1})
        self.assertEqual(response.data['count'], 2)
        self.assertEqual(len(response.data['results']), 2)

    @patch('common.shared_queue.get_flow_queue', (lambda: Mock())())
    def test_pagination_empty(self):
        response = self.client.get('/api/v1/search/products',
                                   data={'query': 'acer',
                                         'page': 2})
        self.assertEqual(response.data['count'], 2)
        self.assertEqual(len(response.data['results']), 0)

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
