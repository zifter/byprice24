from collections import namedtuple

ScrapingTarget = namedtuple('ScrapingTarget', ['url', 'domain', 'use_proxy'])
QueryRequest = namedtuple('QueryRequest', ['query', 'result_count', 'timestamp'])
