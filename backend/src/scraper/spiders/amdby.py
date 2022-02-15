from typing import Optional

from scraper.base import CategoryRule
from scraper.base import CrawlSpiderBase
from scraper.items import ProductScrapingResult
from scraper.mixin import StructuredDataMixin
from scrapy.http import Response
from scrapy.linkextractors import LinkExtractor


class Spider(CrawlSpiderBase, StructuredDataMixin):
    name: str = 'www.amd.by'
    allowed_domains = [
        'www.amd.by',
    ]

    rules = (
        CategoryRule(LinkExtractor(allow=('mobile', )), category='mobile'),
        CategoryRule(LinkExtractor(allow=('noutbuki',)), category='notebook'),
        CategoryRule(LinkExtractor(allow=('monitory',)), category='display'),
        CategoryRule(LinkExtractor(allow=('kompyutery',)), category='desktoppc'),
        CategoryRule(LinkExtractor(allow=('monobloki',)), category='desktoppc'),
        CategoryRule(LinkExtractor(allow=('televizory',)), category='tv'),
        CategoryRule(LinkExtractor(allow=('saundbary-i-domashnie-kinoteatry',)), category='tv'),
        CategoryRule(LinkExtractor(allow=('proektory',)), category='tv'),
        CategoryRule(LinkExtractor(allow=('proekcionnye-ekrany',)), category='tv'),
        CategoryRule(LinkExtractor(allow=('planshety',)), category='tabletpc'),
        CategoryRule(LinkExtractor(allow=('elektronnye-knigi',)), category='tabletpc'),
        CategoryRule(LinkExtractor(allow=('naushniki-i-garnitury',)), category='headphones'),
        CategoryRule(LinkExtractor(allow=('elektronnye-knigi',)), category='tabletpc'),
        CategoryRule(LinkExtractor(allow=('buildingkit',)), category='buildingkit'),
        # COSMETIC
        CategoryRule(LinkExtractor(allow=('umnye-chasy-i-braslety',)), category='smartwatch'),
        CategoryRule(LinkExtractor(allow=('smennye-remeshki-i-braslety',)), category='smartwatch'),
        CategoryRule(LinkExtractor(allow=('ochki-virtualnoi-realnosti',)), category='smartwatch'),
        CategoryRule(LinkExtractor(allow=('elektronnye-parogeneratory',)), category='smartwatch'),
    )

    def parse_product_impl(self, response: Response, category: str) -> Optional[ProductScrapingResult]:
        return self.extract_structured_data(response, category)
