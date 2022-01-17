import logging
from datetime import datetime
from datetime import timedelta
from typing import List
from croniter import croniter

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
from scraper.items import ProductScrapingResult
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from search.logic import find_closest_product
from twisted.internet.defer import Deferred
from twisted.python.failure import Failure


class Agent:
    def __init__(self, queue: FlowQueueBase):
        self.queue = queue

    def schedule(self, marketplace=None, force=False):
        logging.info('Schedule marketplace [%s], force [%s]', marketplace, force)
        now = datetime.now(tz=pytz.UTC)

        filter_args = {}
        if not force:
            day_before = now - timedelta(1)
            filter_args['last_scraping__lte'] = day_before

        if marketplace:
            filter_args['marketplace'] = marketplace

        objects: List[ScrapingState] = ScrapingState.objects.filter(**filter_args).order_by('pk')

        for scraping in objects:
            logging.info(scraping.marketplace.domain)
            scraping_schedule = scraping.scraping_schedule
            next_scraping = croniter(scraping_schedule, now).get_next(datetime)

            target = ScrapingTarget(
                url='https://' + scraping.marketplace.domain,
                domain=scraping.marketplace.domain,
                use_proxy=scraping.use_proxy)

            if croniter.match(scraping_schedule, next_scraping):
                self.queue.scrape(target)


    def scrape(self, target: ScrapingTarget):
        logging.info('Scrape %s', target)

        settings = {
            'start_urls': [
                target.url,
            ],
            'use_proxy': [
                target.use_proxy
            ]
        }

        scrapy_failure = None
        process = CrawlerProcess(settings=get_project_settings())
        stats: Deferred = process.crawl(target.domain, **settings)

        def errback(failure: Failure):
            global scrapy_failure
            logging.error(failure)
            scrapy_failure = failure

        stats.addErrback(errback)

        process.start()  # the script will block here until all crawling jobs are finished

        if scrapy_failure:
            raise RuntimeError(scrapy_failure)

        return stats.result

    def process_scraping_result(self, item: ProductScrapingResult):
        data = ProductData(item)
        logging.info('Process product %s', data)

        marketplace = Marketplace.objects.filter(domain=data.domain).get()

        product = find_closest_product(data.result.title)

        if product is None:
            product, _ = Product.objects.get_or_create(
                name=data.result.title,
                category=data.result.main_category,
                description=data.result.description,
                preview_url=data.result.preview_url,
            )

        page, created = ProductPage.objects.get_or_create(
            product=product,
            marketplace=marketplace,
            url=data.result.url,
            name=data.result.title,
            description=data.result.description,
        )

        _ = ProductState.objects.create(
            product_page=page,
            created=data.result.timestamp,
            price=data.result.price,
            price_currency=data.result.price_currency,
            rating=data.result.rating,
            review_count=data.result.review_count,
            availability=data.result.availability,
        )


def get_agent() -> Agent:
    return Agent(get_flow_queue())
