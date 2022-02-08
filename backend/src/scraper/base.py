import logging
from typing import Generator
from typing import Optional

from common.item_types import Category
from scraper.items import ProductScrapingResult
from scrapy.http import Request
from scrapy.http import Response
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.spiders import Spider


class CategoryRule(Rule):
    """
    Правило для парсинга в Crawler.

    Добавлен функционал возможности указания категории
    """

    def __init__(self, *args, category='', **kwargs):
        super().__init__(
            *args,
            follow=True,
            callback='parse_product',
            cb_kwargs={
                'category': category
            },
            **kwargs,
        )


class ParseProductBase():
    def parse_product(self, response: Response, category: Category
                      ) -> Generator[ProductScrapingResult, None, None]:
        logging.info('parse_item %s', response.url)

        result: ProductScrapingResult = self.parse_product_impl(response,
                                                                category)
        if result is None:
            return

        yield result

    def parse_product_impl(self, response: Response, category: Category
                           ) -> Optional[ProductScrapingResult]:
        raise NotImplementedError('must be overridden')


class CrawlSpiderBase(CrawlSpider, ParseProductBase):
    """
    Базовой CrawlSpider для большинства наших парсеров
    """

    def parse(self, response, **kwargs):
        raise NotImplementedError('method should not be called')


class SpiderBase(Spider, ParseProductBase):
    """
    Базовой Spider для некоторых наших парсеров
    """

    def start_requests(self) -> list[Request] | Generator[Request, None, None]:
        raise NotImplementedError('must be overridden')
