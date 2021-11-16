import os

from redis import Redis
from rq import Queue

from .base import FlowQueueBase
from .base import ScrapingTarget


CRAWLER_FEED = 'crawler-feed'
CRAWLER_RESULT = 'crawler-result'


def crawler_feed() -> Queue:
    url = os.getenv('RQ_REDIS_URL', 'redis://localhost:6379/0')
    redis = Redis.from_url(url)
    return Queue(name=CRAWLER_FEED, connection=redis)


def crawler_result() -> Queue:
    url = os.getenv('RQ_REDIS_URL', 'redis://localhost:6379/0')
    redis = Redis.from_url(url)
    return Queue(name=CRAWLER_RESULT, connection=redis)


class FlowQueueRedis(FlowQueueBase):
    def __init__(self, feed: Queue, result: Queue):
        super().__init__()

        self.feed = feed
        self.result = result

    def scrape(self, target: ScrapingTarget):
        self.feed.enqueue('crawler.tasks.scrape_target', target, job_timeout=-1)

    def process_product(self, product):
        self.result.enqueue('crawler.tasks.process_product', product, job_timeout=30)
