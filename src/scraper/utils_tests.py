from scraper.spiders.schema_org import SchemaOrgSpider
from scraper.utils import get_spider
from scraper.utils import get_spiders


def test_get_spiders():
    spiders = get_spiders()
    assert len(spiders) > 0


def test_get_schema_org():
    assert get_spider('schema.org') == SchemaOrgSpider
