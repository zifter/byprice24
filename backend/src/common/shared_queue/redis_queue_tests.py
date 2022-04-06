from datetime import datetime

import pytz
from scraper.items import ProductScrapingResult

from . import get_flow_queue
from . import CrawlerTarget
from .structs import QueryRequest


def test_scrape_target_added():
    target = CrawlerTarget(
        url='https://www.google.com',
        domain='www.amd.by',
        use_proxy=False,
        follow=False)

    get_flow_queue().scrape(target)

    # TODO Add check


def test_process_product_added():
    item = ProductScrapingResult(
        url='https://test.by/mobile/x3pro8gb256gb_poco_01.html',
        main_category='mobile',
        title='Смартфон POCO X3 Pro 8GB/256GB (синий)',
        description='test',
        price=1049.0,
        price_currency='BYN',
        categories=['Смартфоны, ТВ и электроника', 'Смартфоны, аксессуары', 'Смартфоны']
    )
    get_flow_queue().process_product(item)

    # TODO Add check


def test_push_query_added():
    req = QueryRequest(query='apple', result_count=25, timestamp=datetime.now(tz=pytz.UTC))
    get_flow_queue().push_query(req)

    # TODO Add check
