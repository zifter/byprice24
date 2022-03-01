from typing import Optional

from scraper.base import CategoryRule
from scraper.base import CrawlSpiderBase
from scraper.items import ProductScrapingResult
from scraper.mixin import StructuredDataMixin
from scrapy.http import Response


class Spider(CrawlSpiderBase, StructuredDataMixin):
    name: str = 'www.amd.by'
    allowed_domains = [
        'www.amd.by',
    ]

    rules = (
        CategoryRule(allow='mobile', category='mobile'),
        CategoryRule(allow='noutbuki', category='notebook'),
        CategoryRule(allow='monitory', category='display'),
        CategoryRule(allow='kompyutery', category='desktoppc'),
        CategoryRule(allow='monobloki', category='desktoppc'),
        CategoryRule(allow='televizory', category='tv'),
        CategoryRule(allow='saundbary-i-domashnie-kinoteatry', category='tv'),
        CategoryRule(allow='proektory', category='tv'),
        CategoryRule(allow='proekcionnye-ekrany', category='tv'),
        CategoryRule(allow='planshety', category='tabletpc'),
        CategoryRule(allow='elektronnye-knigi', category='tabletpc'),
        CategoryRule(allow='naushniki-i-garnitury', category='headphones'),
        CategoryRule(allow='elektronnye-knigi', category='tabletpc'),
        CategoryRule(allow='buildingkit', category='buildingkit'),
        # COSMETIC
        CategoryRule(allow='umnye-chasy-i-braslety', category='smartwatch'),
        CategoryRule(allow='smennye-remeshki-i-braslety', category='smartwatch'),
        CategoryRule(allow='ochki-virtualnoi-realnosti', category='smartwatch'),
        CategoryRule(allow='elektronnye-parogeneratory', category='smartwatch'),
    )

    def parse_product_impl(self, response: Response, category: str) -> Optional[ProductScrapingResult]:
        return self.extract_structured_data(response, category)
