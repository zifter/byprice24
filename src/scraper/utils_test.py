from unittest import TestCase

from scraper.spiders.schema_org import SchemaOrgSpider
from scraper.utils import get_spider
from scraper.utils import get_spiders


class UtilsTestCase(TestCase):
    def test_get_spiders(self):
        spiders = get_spiders()
        self.assertGreater(len(spiders), 0)

    def test_get_schema_org(self):
        self.assertEqual(get_spider('schema.org'), SchemaOrgSpider)
