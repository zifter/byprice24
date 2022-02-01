from typing import Optional

from common.item_types import Category
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
        CategoryRule(LinkExtractor(allow=('mobile', )), category=Category.MOBILE),
        CategoryRule(LinkExtractor(allow=('noutbuki',)), category=Category.NOTEBOOK),
        CategoryRule(LinkExtractor(allow=('monitory',)), category=Category.DISPLAY),
        CategoryRule(LinkExtractor(allow=('kompyutery',)), category=Category.DESKTOP),
        CategoryRule(LinkExtractor(allow=('monobloki',)), category=Category.DESKTOP),
        CategoryRule(LinkExtractor(allow=('televizory',)), category=Category.TV),
        CategoryRule(LinkExtractor(allow=('saundbary-i-domashnie-kinoteatry',)), category=Category.TV),
        CategoryRule(LinkExtractor(allow=('proektory',)), category=Category.TV),
        CategoryRule(LinkExtractor(allow=('proekcionnye-ekrany',)), category=Category.TV),
        CategoryRule(LinkExtractor(allow=('planshety',)), category=Category.TABLET),
        CategoryRule(LinkExtractor(allow=('elektronnye-knigi',)), category=Category.TABLET),
        CategoryRule(LinkExtractor(allow=('naushniki-i-garnitury',)), category=Category.HEADPHONE),
        CategoryRule(LinkExtractor(allow=('elektronnye-knigi',)), category=Category.TABLET),
        CategoryRule(LinkExtractor(allow=('buildingkit',)), category=Category.LEGO),
        # COSMETIC
        CategoryRule(LinkExtractor(allow=('umnye-chasy-i-braslety',)), category=Category.SMART_GADGET),
        CategoryRule(LinkExtractor(allow=('smennye-remeshki-i-braslety',)), category=Category.SMART_GADGET),
        CategoryRule(LinkExtractor(allow=('ochki-virtualnoi-realnosti',)), category=Category.SMART_GADGET),
        CategoryRule(LinkExtractor(allow=('elektronnye-parogeneratory',)), category=Category.SMART_GADGET),
    )

    def parse_product_impl(self, response: Response, category: Category) -> Optional[ProductScrapingResult]:
        return self.extract_structured_data(response, category)
