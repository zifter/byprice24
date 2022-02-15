from functools import cache
from urllib.parse import urlparse

from common.paths import TEST_DATA_DIR
from scrapy.crawler import CrawlerRunner
from scrapy.http import Request
from scrapy.http import TextResponse
from scrapy.utils.project import get_project_settings

PAGES_DIR = TEST_DATA_DIR.joinpath('parsing', 'marketplaces')


@cache
def _get_crawler_runner() -> CrawlerRunner:
    runner = CrawlerRunner(get_project_settings())
    return runner


def get_spider_for_url(url):
    domain = urlparse(url).netloc
    return _get_crawler_runner().create_crawler(domain)._create_spider()


def assert_spider(url, test_file, expected):
    spider = get_spider_for_url(url)
    filepath = PAGES_DIR.joinpath(spider.name, test_file)

    fake_response = fake_response_from_file(filepath, url=url)
    results = list(spider.parse_product(fake_response, category=expected.main_category))

    assert len(results) == 1, f'result list len is {len(results)}, but expected 1'
    assert results[0] == expected, f'\n{results[0]}\n{expected}'


def fake_response_from_file(filepath, url=None):
    """
    Create a Scrapy fake HTTP response from a HTML file

    @param filepath: Absolute paths of response body.
    @param url: The URL of the response.

    returns: A scrapy HTTP response which can be used for unittesting.
    """
    with open(filepath) as f:
        return TextResponse(url=url,
                            request=Request(url=url),
                            body=f.read(),
                            encoding='utf-8')
