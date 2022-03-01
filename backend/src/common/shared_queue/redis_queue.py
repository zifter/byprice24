import os

from redis import Redis
from rq import Queue

from .base import FlowQueueBase
from .base import ScrapingTarget
from .structs import QueryRequest

CRAWLER_FEED = 'crawler-feed'
CRAWLER_RESULT = 'crawler-result'
SEARCH_QUERY = 'search-query'


def _connection():
    url = os.getenv('RQ_REDIS_URL', 'redis://localhost:6379/0')
    return Redis.from_url(url)


def crawler_feed() -> Queue:
    return Queue(name=CRAWLER_FEED, connection=_connection())


def crawler_result() -> Queue:
    return Queue(name=CRAWLER_RESULT, connection=_connection())


def search_query() -> Queue:
    return Queue(name=SEARCH_QUERY, connection=_connection())


class FlowQueueRedis(FlowQueueBase):
    def __init__(self, feed: Queue, result: Queue, query: Queue):
        super().__init__()

        self.feed = feed
        self.result = result
        self.query = query

    def scrape(self, target: ScrapingTarget):
        rq_job = self.feed.enqueue('crawler.tasks.scrape_target', target, job_timeout=-1, failure_ttl=-1)
        return rq_job.id

    def process_product(self, product):
        self.result.enqueue('crawler.tasks.process_product', product, job_timeout=30)

    def push_query(self, obj: QueryRequest):
        self.query.enqueue('search.tasks.push_query', obj, job_timeout=30)
