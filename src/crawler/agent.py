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
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor


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
                domain=scraping.marketplace.domain)

            self.queue.scrape(target)

            scraping.last_scraping = now
            scraping.save()

    def scrape(self, target: ScrapingTarget, spawn_process=False):
        logging.info('Scrape %s', target)

        spider = get_spider(target.spider_name)
        settings = {
            'start_urls': [
                'https://www.ilp.by/coffee'
            ],
            'allowed_domains': [
                target.domain
            ],
        }

        if spawn_process:
            process = CrawlerProcess(settings=get_project_settings())
            process.crawl(spider, **settings)
            process.start()  # the script will block here until all crawling jobs are finished
        else:
            runner = CrawlerRunner(get_project_settings())
            d = runner.crawl(spider, **settings)
            d.addBoth(lambda _: reactor.stop())
            reactor.run()

        return None

    def process_product(self, item: ProductItem):
        data = ProductData(item)
        logging.info('Process product %s', data)

        marketplace = Marketplace.objects.filter(domain=data.domain).get()

        product, created = Product.objects.get_or_create(
            name=data.name,
            category='',
            description='',
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
