import gc
import logging
from typing import Generator
from typing import Optional

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


class ParseProductBase:

    def parse_product(self, response: Response, category: str
                      ) -> Generator[ProductScrapingResult, None, None]:
        logging.info('parse_item %s', response.url)

        result: ProductScrapingResult = self.parse_product_impl(response,
                                                                category)
        if result is None:
            return

        yield result

        # try to reduce memory usage of scarpy
        gc.collect()

    def parse_product_impl(self, response: Response, category: str
                           ) -> Optional[ProductScrapingResult]:
        raise NotImplementedError('must be overridden')


class AnySpiderMixin:
    """
    Mixin для всех спайдеров
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # specify target url for debug purpose
        if hasattr(self, 'target_url') and hasattr(self, 'start_urls'):
            self.start_urls.append(self.target_url)


class CrawlSpiderBase(ParseProductBase, AnySpiderMixin, CrawlSpider):
    """
    Базовой CrawlSpider для большинства наших парсеров
    """

    def parse(self, response, **kwargs):
        raise NotImplementedError('method should not be called')


class SpiderBase(ParseProductBase, AnySpiderMixin, Spider):
    """
    Базовой Spider для некоторых наших парсеров
    """

    def start_requests(self) -> list[Request] | Generator[Request, None, None]:
        raise NotImplementedError('must be overridden')
