from typing import Optional

from common.item_types import Category
from scraper.base import CategoryRule
from scraper.base import CrawlSpiderBase
from scraper.items import ProductScrapingResult
from scraper.mixin import StructuredDataMixin
from scrapy.http import Response
from scrapy.linkextractors import LinkExtractor


class Spider(CrawlSpiderBase, StructuredDataMixin):
    name: str = 'texus.by'
    allowed_domains = [
        'texus.by',
    ]

    rules = (
        CategoryRule(LinkExtractor(allow=('mobilnye_telefony',)), category=Category.MOBILE),
        CategoryRule(LinkExtractor(allow=('noutbuki',)), category=Category.NOTEBOOK),
        CategoryRule(LinkExtractor(allow=('planshety',)), category=Category.TABLET),
        CategoryRule(LinkExtractor(allow=('monitory',)), category=Category.DISPLAY),
        CategoryRule(LinkExtractor(allow=('kompyutery',)), category=Category.DESKTOP),
        CategoryRule(LinkExtractor(allow=('televizory',)), category=Category.TV),
        CategoryRule(LinkExtractor(allow=('naushniki,garnitury',)), category=Category.HEADPHONE),
    )

    def parse_product_impl(self, response: Response, category: Category) -> Optional[ProductScrapingResult]:
        return self.extract_structured_data(response, category)
