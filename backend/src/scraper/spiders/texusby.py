from typing import Optional

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
        CategoryRule(LinkExtractor(allow=('mobilnye_telefony',)), category='mobile'),
        CategoryRule(LinkExtractor(allow=('noutbuki',)), category='notebook'),
        CategoryRule(LinkExtractor(allow=('planshety',)), category='tabletpc'),
        CategoryRule(LinkExtractor(allow=('monitory',)), category='display'),
        CategoryRule(LinkExtractor(allow=('kompyutery',)), category='desktoppc'),
        CategoryRule(LinkExtractor(allow=('televizory',)), category='tv'),
        CategoryRule(LinkExtractor(allow=('naushniki,garnitury',)), category='headphones'),
    )

    def parse_product_impl(self, response: Response, category: str) -> Optional[ProductScrapingResult]:
        return self.extract_structured_data(response, category)
