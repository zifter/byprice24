from typing import Optional

from scraper.base import CategoryRule
from scraper.base import CrawlSpiderBase
from scraper.items import ProductScrapingResult
from scraper.mixin import StructuredDataMixin
from scrapy.http import Response


class Spider(CrawlSpiderBase, StructuredDataMixin):
    name: str = 'ram.by'
    allowed_domains = [
        'ram.by',
    ]

    rules = (
        CategoryRule(category='unknown'),
    )

    custom_settings = {
        'ROBOTSTXT_OBEY': False,
    }

    def parse_product_impl(self, response: Response, category: str) -> Optional[ProductScrapingResult]:
        return self.extract_structured_data(response, category)
