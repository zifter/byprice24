from common.item_types import Availability
from common.item_types import Category
from common.shared_queue import FlowQueueBase
from crawler.agent import Agent
from django.core.management import call_command
from django.test import TestCase
from scraper.items import ProductScrapingResult


class AgentTestCase(TestCase):
    fixtures = ['prod/markets.yaml']

    @classmethod
    def setUpClass(cls):
        call_command('search_index', '--rebuild', '-f')

        super().setUpClass()

    def test_schedule(self):
        mock = FlowQueueBase()
        agent = Agent(mock)
        agent.schedule()

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
