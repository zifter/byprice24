import http.client
from collections import OrderedDict
from unittest.mock import patch

from django.test import Client
from django.test import TestCase
from marketplace.mock_elastic import mock_full_pagination
from marketplace.mock_elastic import mock_not_full_pagination
from marketplace.mock_elastic import mocked_empty_match_elastic
from marketplace.mock_elastic import mocked_exact_match_elastic
from marketplace.mock_elastic import mocked_list_ok_elastic


class MarketplaceViewEmptyTestCase(TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_api_empty_list(self):
        response = self.client.get('/api/v1/marketplaces/')
        self.assertEqual(len(response.data), 0)


class MarketplaceViewTestCase(TestCase):
    fixtures = ['marketplaces_test.yaml', ]

    expected = OrderedDict([
        ('id', 1),
        ('domain', 'localhost'),
        ('description', ''),
        ('rating', 0),
        ('image_logo_url', 'https://www.test.by/')
    ])

    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_marketplaces_list_ok(self):
        response = self.client.get('/api/v1/marketplaces/')
        self.assertEqual(len(response.data), 2)

        self.assertEqual(response.data[0], MarketplaceViewTestCase.expected)

    def test_get_marketplace_ok(self):
        response = self.client.get('/api/v1/marketplaces/localhost')
        self.assertEqual(response.data, MarketplaceViewTestCase.expected)

    def test_get_marketplace_not_found(self):
        response = self.client.get('/api/v1/marketplaces/wrong-markeplace')
        self.assertEqual(response.status_code, http.client.NOT_FOUND)


class ProductViewTestCase(TestCase):
    fixtures = ['marketplaces_test.yaml', 'products_test.yaml', 'product_pages_test.yaml', 'product_states_test.yaml', ]
    expected = {'count': 2,
                'next': 2,
                'previous': 0,
                'results': [
                    OrderedDict(
                        [('id', 2),
                         ('name', 'Acer Extensa 15 EX215-53G-7014 NX.EGCER.009'),
                         ('category', 'notebook'),
                         ('description', ''),
                         ('preview_url', None),
                         ('min_offer', OrderedDict([('price', '340.30'),
                                                    ('price_currency', 'BYN')])),
                         ('marketplaces_count_instock', 2)]),
                    OrderedDict([('id', 3),
                                 ('name', 'Acer Extensa 15 EX215-52-54D6 NX.EG8ER.00V'),
                                 ('category', 'notebook'),
                                 ('description', ''),
                                 ('preview_url', None),
                                 ('min_offer', OrderedDict([('price', '580.30'),
                                                            ('price_currency', 'BYN')])),
                                 ('marketplaces_count_instock', 1)])]}

    @patch('elasticsearch.Elasticsearch.search', mocked_list_ok_elastic)
    def test_products_startswith_search_list_ok(self):
        response = self.client.get('/api/v1/search/products',
                                   data={'query': 'Acer'})
        self.assertEqual(len(response.data['results']), 2)

        self.assertEqual(response.data, self.expected)

    @patch('elasticsearch.Elasticsearch.search', mocked_exact_match_elastic)
    def test_get_product_full_search_ok(self):
        response = self.client.get('/api/v1/search/products',
                                   data={'query': 'Acer Extensa 15 EX215-53G-7014 NX.EGCER.009'})
        self.assertEqual(response.data['results'], [self.expected['results'][0]])

    @patch('elasticsearch.Elasticsearch.search', mock_full_pagination)
    def test_pagination_full_page(self):
        response = self.client.get('/api/v1/search/products',
                                   data={'query': 'Samsung',
                                         'page': 1})
        self.assertEqual(response.data['count'], 20)
        self.assertEqual(len(response.data['results']), 20)

    @patch('elasticsearch.Elasticsearch.scroll', mock_not_full_pagination)
    @patch('elasticsearch.Elasticsearch.search', mock_full_pagination)
    def test_pagination_not_full_page(self):
        response = self.client.get('/api/v1/search/products',
                                   data={'query': 'acer',
                                         'page': 2})
        self.assertEqual(len(response.data['results']), 2)

    @patch('elasticsearch.Elasticsearch.search', mocked_empty_match_elastic)
    def test_get_products_empty_list(self):
        response = self.client.get('/api/v1/search/products', data={'query': 'Apple'})
        self.assertEqual(response.data, {'count': 0,
                                         'next': 2,
                                         'previous': 0, 'results': []}
                         )

    @patch('elasticsearch.Elasticsearch.search', mocked_list_ok_elastic)
    def test_fail_search_too_short_query(self):
        response = self.client.get('/api/v1/search/products', data={'query': 'A'})
        self.assertEqual(response.status_code, http.client.BAD_REQUEST)

    def test_fail_search_no_query(self):
        response = self.client.get('/api/v1/search/products')
        self.assertEqual(response.status_code, http.client.BAD_REQUEST)
