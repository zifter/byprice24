import os

from redis import Redis
from rq import Queue

from .base import FlowQueueBase
from .base import ScrapingTarget

CRAWLER_FEED = 'crawler-feed'
CRAWLER_RESULT = 'crawler-result'
CRAWLER_PUSH_QUERY = 'crawler-push-query'


def crawler_feed() -> Queue:
    url = os.getenv('RQ_REDIS_URL', 'redis://localhost:6379/0')
    redis = Redis.from_url(url)
    return Queue(name=CRAWLER_FEED, connection=redis)


def crawler_result() -> Queue:
    url = os.getenv('RQ_REDIS_URL', 'redis://localhost:6379/0')
    redis = Redis.from_url(url)
    return Queue(name=CRAWLER_RESULT, connection=redis)


def crawler_push_query() -> Queue:
    url = os.getenv('RQ_REDIS_URL', 'redis://localhost:6379/0')
    redis = Redis.from_url(url)
    return Queue(name=CRAWLER_PUSH_QUERY, connection=redis)


class FlowQueueRedis(FlowQueueBase):
    def __init__(self, feed: Queue, result: Queue, push_query: Queue):
        super().__init__()

        self.feed = feed
        self.result = result
        self.query = push_query

    def scrape(self, target: ScrapingTarget):
        self.feed.enqueue('crawler.tasks.scrape_target', target, job_timeout=-1)

    def process_product(self, product):
        self.result.enqueue('crawler.tasks.process_product', product, job_timeout=30)

    def push_query(self, query: str):
        self.query.enqueue('crawler.tasks.push_query', query, job_timeout=1)
