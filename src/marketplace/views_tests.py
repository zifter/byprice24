import http.client
from collections import OrderedDict

from django.test import Client
from django.test import TestCase


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
    ])

    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_marketplaces_list_ok(self):
        response = self.client.get('/api/v1/marketplaces/')
        self.assertEqual(len(response.data), 1)

        self.assertEqual(response.data[0], MarketplaceViewTestCase.expected)

    def test_get_marketplace_ok(self):
        response = self.client.get('/api/v1/marketplaces/localhost')
        self.assertEqual(response.data, MarketplaceViewTestCase.expected)

    def test_get_marketplace_not_found(self):
        response = self.client.get('/api/v1/marketplaces/wrong-markeplace')
        self.assertEqual(response.status_code, http.client.NOT_FOUND)
