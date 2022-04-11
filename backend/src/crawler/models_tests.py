from crawler.models import CrawlerState
from marketplace.models import Marketplace


def test_scraping_state_printable_ok():
    marketplace = Marketplace(
        domain='www.test.by',
    )
    state = CrawlerState(
        marketplace=marketplace,
    )

    assert str(state) == 'www.test.by [1970-01-01 00:00:00+00:00]'
