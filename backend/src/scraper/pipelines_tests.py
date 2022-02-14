import abc
import logging

from common import shared_queue
from common.shared_queue import FlowQueueBase
from scraper.items import ProductScrapingResult
from scraper.pipelines import ScraperPipeline


class Fake(FlowQueueBase):
    @abc.abstractmethod
    def process_product(self, product):
        logging.info(product)


def test_scraper_pipeline_process_ok(monkeypatch):
    def fake_queue():
        return Fake()

    monkeypatch.setattr(shared_queue, 'get_flow_queue', fake_queue)

    pipeline = ScraperPipeline()
    item = ProductScrapingResult(
        url='https://localhost/test',
        title='test',
        main_category='mobile',
        description='test',
        price=0.0,
        price_currency='BYN',
    )
    assert pipeline.process_item(item, None) is None
