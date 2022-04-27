import gc
import logging
from typing import Generator
from typing import Optional

from scraper.items import ProductScrapingResult
from scrapy.http import Request
from scrapy.http import Response
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, SitemapSpider
from scrapy.spiders import Rule
from scrapy.spiders import Spider


class CategoryRule(Rule):
    """
    Правило для парсинга в Crawler.

    Добавлен функционал возможности указания категории
    """

    def __init__(self, allow='', category='', follow=True, deny=(), **kwargs):
        self.allow = allow

        args = LinkExtractor(allow=(allow, ), deny=deny),
        super().__init__(
            *args,
            follow=follow,
            callback='parse_product',
            # process_links=process_links,
            cb_kwargs={
                'category': category
            },
            **kwargs,
        )


class ParseProductBase:

    def parse_product(self, response: Response, category: str = 'unknown'
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

    def __init__(self, *args, **kwargs):
        if not kwargs.get('follow', True):
            category = [rule.cb_kwargs['category'] for rule in self.rules
                        if rule.allow in kwargs['start_urls'][0]][0]

            self.rules = (CategoryRule(kwargs['start_urls'][0], category=category),)

        super().__init__(*args, **kwargs)

    def parse(self, response, **kwargs):
        raise NotImplementedError('method should not be called')


class SiteMapSpiderBase(ParseProductBase, AnySpiderMixin, SitemapSpider):
    """
    Базовой CrawlSpider для большинства наших парсеров
    """

    def __init__(self, *args, **kwargs):
        if not kwargs.get('follow', True):
            category = [rule.cb_kwargs['category'] for rule in self.sitemap_rules
                        if rule.allow in kwargs['start_urls'][0]][0]

            self.rules = (CategoryRule(kwargs['start_urls'][0], category=category),)

        super().__init__(*args, **kwargs)

    def parse(self, response, **kwargs):
        raise NotImplementedError('method should not be called')


class SpiderBase(ParseProductBase, AnySpiderMixin, Spider):
    """
    Базовой Spider для некоторых наших парсеров
    """

    def start_requests(self) -> list[Request] | Generator[Request, None, None]:
        raise NotImplementedError('must be overridden')