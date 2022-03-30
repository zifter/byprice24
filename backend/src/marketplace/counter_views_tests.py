from unittest import TestCase

import fakeredis
from marketplace.counter_views import CounterViewsRedis


class CounterViewsTestCase(TestCase):
    fixtures = [
        'prod/categories.yaml',
        'test/marketplaces.yaml',
        'test/products.yaml',
        'test/product_pages.yaml',
        'test/product_states.yaml',
    ]

    def setUp(self):
        # Every test needs a client.
        self.client = fakeredis.FakeStrictRedis()

    def test_get_product_views_none(self):
        number_of_views = CounterViewsRedis(self.client, 2).get_product_views()
        self.assertEqual(number_of_views, 0)

    def test_increment_product_views(self):
        counter = CounterViewsRedis(self.client, 2)
        counter.create_initial_product_views()
        counter.increment_product_views()
        number_of_views = counter.get_product_views()
        self.assertEqual(number_of_views, 1)
