from scraper.middlewares import ScraperAPIMiddleware
from scrapy import Request


class FakeSpider:
    pass


def test_proxy_middleware_do_not_use():
    api = ScraperAPIMiddleware()
    request = Request('https://localhost')
    api.process_request(request, None)


def test_proxy_middleware_use_proxy():
    api = ScraperAPIMiddleware()
    request = Request('https://localhost')
    spider = FakeSpider()
    spider.use_proxy = True
    api.process_request(request, None)
