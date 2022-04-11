from collections import namedtuple

CrawlerTarget = namedtuple('CrawlerTarget', ['url', 'domain', 'follow', 'use_proxy'])
QueryRequest = namedtuple('QueryRequest', ['query', 'result_count', 'timestamp'])
