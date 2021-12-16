from common.shared_queue.base import FlowQueueBase
from common.shared_queue.redis_queue import crawler_feed
from common.shared_queue.redis_queue import crawler_push_query
from common.shared_queue.redis_queue import crawler_result
from common.shared_queue.redis_queue import FlowQueueRedis
from common.shared_queue.structs import ScrapingTarget


def get_flow_queue() -> FlowQueueBase:
    return FlowQueueRedis(crawler_feed(), crawler_result(), crawler_push_query())


__all__ = [
    'FlowQueueBase',
    'ScrapingTarget',
    'get_flow_queue',
]
