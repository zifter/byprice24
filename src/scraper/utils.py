from typing import Dict

from scrapy import Spider
from scrapy.http import Request
from scrapy.http import TextResponse

from .spiders.schema_org import SchemaOrgSpider


def get_spiders() -> Dict[str, Spider]:
    return {
        SchemaOrgSpider.name: SchemaOrgSpider,
    }


def get_spider(spider_class) -> Spider:
    return get_spiders().get(spider_class)


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
