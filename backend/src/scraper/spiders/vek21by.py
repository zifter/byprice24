from typing import Optional

from common.item_types import Category
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
        CategoryRule(LinkExtractor(allow=('mobile',)), category=Category.MOBILE),
        CategoryRule(LinkExtractor(allow=('notebooks',)), category=Category.NOTEBOOK),
        CategoryRule(LinkExtractor(allow=('headphones',)), category=Category.HEADPHONE),
    )

    def parse_product_impl(self, response: Response, category: Category) -> Optional[ProductScrapingResult]:
        return self.extract_structured_data(response, category)
