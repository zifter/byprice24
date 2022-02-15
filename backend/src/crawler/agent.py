import logging
from datetime import datetime
from typing import List

import pytz
from common.shared_queue import FlowQueueBase
from common.shared_queue import get_flow_queue
from common.shared_queue import ScrapingTarget
from crawler.models import ScrapingState
from crawler.structs import ProductData
from croniter import croniter
from marketplace.models import Marketplace
from marketplace.models import Product
from marketplace.models import ProductPage
from marketplace.models import ProductState
from scraper.items import ProductScrapingResult
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from twisted.internet.defer import Deferred
from twisted.python.failure import Failure


class Agent:
    def __init__(self, queue: FlowQueueBase):
        self.queue = queue

    def now(self):
        return datetime.now(tz=pytz.UTC)

    def schedule(self, marketplace=None, force=False) -> List[str]:
        logging.info('Schedule marketplace [%s], force [%s]', marketplace, force)
        now = self.now()

        filter_args = {}
        if marketplace:
            filter_args['marketplace'] = marketplace

        objects: List[ScrapingState] = ScrapingState.objects.filter(**filter_args).order_by('pk')

        job_ids = []

        for scraping in objects:
            logging.info(scraping.marketplace.domain)
            scraping_schedule = scraping.scraping_schedule
            next_scraping = croniter(scraping_schedule, scraping.last_scraping).get_next(datetime)

            target = ScrapingTarget(
                url='https://' + scraping.marketplace.domain,
                domain=scraping.marketplace.domain,
                use_proxy=scraping.use_proxy)

            if force or next_scraping <= now:
                job_ids.append(self.queue.scrape(target))
                scraping.last_scraping = now
                scraping.save()

        return job_ids

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
        product = data.closest_product()

        if product is None:
            product, _ = Product.objects.get_or_create(
                name=data._result.title,
                category=data.category(),
                description=data._result.description,
                preview_url=data._result.preview_url,
            )

        page, _ = ProductPage.objects.get_or_create(
            product=product,
            marketplace=marketplace,
            url=data.url,
            name=data._result.title,
            description=data._result.description,
        )

        def models_has_equal_fields(model_1, model_2, *fields):
            is_equal = True
            for field in fields:
                if model_1.__getattribute__(field) != model_2.__getattribute__(field):
                    is_equal = False
                    break
            return is_equal

        last_product_state = ProductState.objects.filter(product_page=page).last()
        new_product_state = ProductState.objects.model(
            product_page=page,
            created=data._result.timestamp,
            last_check=data._result.timestamp,
            price=data._result.price,
            price_currency=data._result.price_currency,
            rating=data._result.rating,
            review_count=data._result.review_count,
            availability=data._result.availability,
        )
        if not last_product_state or not models_has_equal_fields(
                last_product_state,
                new_product_state,
                'price', 'price_currency', 'rating', 'review_count', 'availability'):
            new_product_state.save(force_insert=True, using=ProductState.objects.db)
        else:
            setattr(last_product_state, 'last_check', data._result.timestamp)
            last_product_state.save(using=ProductState.objects.db)


def get_agent() -> Agent:
    return Agent(get_flow_queue())
