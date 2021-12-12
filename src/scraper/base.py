from typing import Generator

from scraper.items import ProductItem
from scrapy.http import Response
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule


class CategoryRule(Rule):
    def __init__(self, *args, category='', **kwargs):
        super().__init__(
            *args,
            follow=True,
            callback='parse_item',
            cb_kwargs={
                'category': category
            },
            **kwargs,
        )


class SpiderBase(CrawlSpider):
    def parse(self, response, **kwargs):
        raise NotImplementedError('method should not be called')

    def parse_item(self, response: Response, category: str) -> Generator[ProductItem, None, None]:
        raise NotImplementedError()
