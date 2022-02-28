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
        CategoryRule('mobile', category='mobile'),
        CategoryRule('noutbuki', category='notebook'),
        CategoryRule('monitory', category='display'),
        CategoryRule('kompyutery', category='desktoppc'),
        CategoryRule('monobloki', category='desktoppc'),
        CategoryRule('televizory', category='tv'),
        CategoryRule('saundbary-i-domashnie-kinoteatry', category='tv'),
        CategoryRule('proektory', category='tv'),
        CategoryRule('proekcionnye-ekrany', category='tv'),
        CategoryRule('planshety', category='tabletpc'),
        CategoryRule('elektronnye-knigi', category='tabletpc'),
        CategoryRule('naushniki-i-garnitury', category='headphones'),
        CategoryRule('elektronnye-knigi', category='tabletpc'),
        CategoryRule('buildingkit', category='buildingkit'),
        # COSMETIC
        CategoryRule('umnye-chasy-i-braslety', category='smartwatch'),
        CategoryRule('smennye-remeshki-i-braslety', category='smartwatch'),
        CategoryRule('ochki-virtualnoi-realnosti', category='smartwatch'),
        CategoryRule('elektronnye-parogeneratory', category='smartwatch'),
    )

    def parse_product_impl(self, response: Response, category: str) -> Optional[ProductScrapingResult]:
        return self.extract_structured_data(response, category)
