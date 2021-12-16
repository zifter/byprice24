from unittest.mock import patch

from common.item_types import Availability
from common.item_types import Category
from common.shared_queue import FlowQueueBase
from crawler.agent import Agent
from django.test import TestCase
from marketplace.mock_elastic import mocked_elastic_manager
from marketplace.mock_elastic import mocked_list_ok_elastic
from scraper.items import ProductScrapingResult


class AgentTestCase(TestCase):
    fixtures = ['prod/markets.yaml']

    def test_schedule(self):
        mock = FlowQueueBase()
        agent = Agent(mock)
        agent.schedule()

    @patch('common.elastic.elastic.ElasticManager.insert_data', mocked_list_ok_elastic)
    @patch('common.elastic.elastic.ElasticManager.__init__', mocked_elastic_manager)
    def test_process_product(self):
        mock = FlowQueueBase()
        agent = Agent(mock)

        item = ProductScrapingResult(
            url='https://www.21vek.by/mobile/x3pro8gb256gb_poco_01.html',
            title='Смартфон POCO X3 Pro 8GB/256GB (синий)',
            main_category=Category.MOBILE,
            description='test',
            price=1049.0,
            price_currency='BYN',
            availability=Availability.InStock,
            rating=5.0,
            review_count=4,
            preview_url='https://static.21vek.by/img/galleries/6632/831/preview_b/x3pro8gb256gb_poco_01_60dd5ddb2379f.png',
            categories=['Смартфоны, ТВ и электроника', 'Смартфоны, аксессуары', 'Смартфоны']
        )

        agent.process_product(item)
