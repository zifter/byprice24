import django_rq
from rq import Queue

from .base import FlowQueueBase
from .base import ScrapingTarget
from .structs import QueryRequest

CRAWLER_FEED = 'crawler-feed'
CRAWLER_RESULT = 'crawler-result'
SEARCH_QUERY = 'search-query'


def crawler_feed() -> Queue:
    return Queue(name=CRAWLER_FEED, connection=django_rq.get_connection(CRAWLER_FEED))


def crawler_result() -> Queue:
    return Queue(name=CRAWLER_RESULT, connection=django_rq.get_connection(CRAWLER_RESULT))


def search_query() -> Queue:
    return Queue(name=SEARCH_QUERY, connection=django_rq.get_connection(SEARCH_QUERY))


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
