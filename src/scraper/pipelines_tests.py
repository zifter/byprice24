import abc
import logging

from common import shared_queue
from common.shared_queue import FlowQueueBase
from scraper.items import ProductItem
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
    item = ProductItem(
        url='https://localhost/test',
    )
    assert pipeline.process_item(item, None) is None
