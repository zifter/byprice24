import logging
from datetime import datetime
from datetime import timedelta
from typing import List

import pytz
from common.shared_queue import FlowQueueBase
from common.shared_queue import get_flow_queue
from common.shared_queue import ScrapingTarget
from crawler.models import ScrapingState
from crawler.structs import ProductData
from marketplace.models import Marketplace
from marketplace.models import Product
from marketplace.models import ProductPage
from marketplace.models import ProductState
from scraper.items import ProductItem
from scraper.utils import get_spider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from twisted.internet.defer import Deferred
from twisted.python.failure import Failure


class Agent:
    def __init__(self, queue: FlowQueueBase):
        self.queue = queue

    def schedule(self, marketplace=None, force=False):
        logging.info('Schedule marketplace %s, force %s', marketplace, force)
        now = datetime.now(tz=pytz.UTC)

        filter_args = {}
        if not force:
            day_before = now - timedelta(1)
            filter_args['last_scraping__lte'] = day_before

        if marketplace:
            filter_args['marketplace'] = marketplace

        objects: List[ScrapingState] = ScrapingState.objects.filter(**filter_args)

        for scraping in objects:
            target = ScrapingTarget(
                url='https://' + scraping.marketplace.domain,
                spider_name=scraping.spider_name,
                domain=scraping.marketplace.domain,
                use_proxy=scraping.use_proxy)

            self.queue.scrape(target)

            scraping.last_scraping = now
            scraping.save()

    def scrape(self, target: ScrapingTarget):
        logging.info('Scrape %s', target)

        spider = get_spider(target.spider_name)
        settings = {
            'start_urls': [
                target.url,
            ],
            'allowed_domains': [
                target.domain
            ],
            'use_proxy': [
                target.use_proxy
            ]
        }

        scrapy_failure = None
        process = CrawlerProcess(settings=get_project_settings())
        stats: Deferred = process.crawl(spider, **settings)

        def errback(failure: Failure):
            global scrapy_failure
            logging.error(failure)
            scrapy_failure = failure

        stats.addErrback(errback)

        process.start()  # the script will block here until all crawling jobs are finished

        if scrapy_failure:
            raise RuntimeError(scrapy_failure)

        return stats.result

    def process_product(self, item: ProductItem):
        data = ProductData(item)
        logging.info('Process product %s', data)

        marketplace = Marketplace.objects.filter(domain=data.domain).get()

        product, created = Product.objects.get_or_create(
            name=data.name,
            category='',
            description='',
            image_url=data.image_url,
        )

        page, created = ProductPage.objects.get_or_create(
            product=product,
            marketplace=marketplace,
            url=data.url,
        )

        _ = ProductState.objects.create(
            product_page=page,
            created=datetime.now(tz=pytz.UTC),
            price=data.price,
            price_currency=data.price_currency
        )


def get_agent() -> Agent:
    return Agent(get_flow_queue())
