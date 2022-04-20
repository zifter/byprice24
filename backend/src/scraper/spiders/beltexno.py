from typing import Optional

from scraper.base import CategoryRule
from scraper.base import CrawlSpiderBase
from scraper.items import ProductScrapingResult
from scraper.mixin import StructuredDataMixin
from scrapy.http import Response


class Spider(CrawlSpiderBase, StructuredDataMixin):
    name: str = 'beltexno.by'
    allowed_domains = [
        'https://beltexno.by/',
    ]

    rules = (
        CategoryRule(allow='smartphone', category='mobile'),
        CategoryRule(allow='notebook', category='notebook'),
        CategoryRule(allow='planshets', category='tabletpc'),
        CategoryRule(allow='monitori-catalog', category='display'),
        CategoryRule(allow='pc', category='desktoppc'),
        CategoryRule(allow='tv', category='tv'),
    )

    def parse_product_impl(self, response: Response, category: str) -> Optional[ProductScrapingResult]:
        return self.extract_structured_data(response, category)