from typing import Optional

from scraper.base import CategoryRule
from scraper.base import CrawlSpiderBase
from scraper.items import ProductScrapingResult
from scraper.mixin import StructuredDataMixin
from scrapy.http import Response
from scrapy.linkextractors import LinkExtractor


class Spider(CrawlSpiderBase, StructuredDataMixin):
    name: str = 'www.21vek.by'
    allowed_domains = [
        'www.21vek.by',
    ]

    rules = (
        CategoryRule(LinkExtractor(allow=('mobile',)), category='mobile'),
        CategoryRule(LinkExtractor(allow=('notebooks',)), category='notebook'),
        CategoryRule(LinkExtractor(allow=('headphones',)), category='headphones'),
    )

    def parse_product_impl(self, response: Response, category: str) -> Optional[ProductScrapingResult]:
        return self.extract_structured_data(response, category)
