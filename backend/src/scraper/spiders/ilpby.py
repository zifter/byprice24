from typing import Optional

from scraper.base import CategoryRule
from scraper.base import CrawlSpiderBase
from scraper.items import ProductScrapingResult
from scraper.mixin import StructuredDataMixin
from scrapy.http import Response
from scrapy.linkextractors import LinkExtractor


class Spider(CrawlSpiderBase, StructuredDataMixin):
    name: str = 'www.ilp.by'
    allowed_domains = [
        'www.ilp.by',
    ]

    rules = (
        CategoryRule(LinkExtractor(allow=('notebook', )), category='notebook'),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def parse_product_impl(self, response: Response, category: str) -> Optional[ProductScrapingResult]:
        return self.extract_structured_data(response, category)
