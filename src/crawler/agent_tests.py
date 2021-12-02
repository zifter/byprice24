from common.shared_queue import FlowQueueBase
from crawler.agent import Agent
from django.test import TestCase
from scraper.items import ProductItem


class AgentTestCase(TestCase):
    fixtures = ['prod/markets.yaml']

    def test_schedule(self):
        mock = FlowQueueBase()
        agent = Agent(mock)
        agent.schedule()

    def test_process_product(self):
        mock = FlowQueueBase()
        agent = Agent(mock)

        item = ProductItem(
            url='https://www.21vek.by/mobile/x3pro8gb256gb_poco_01.html',
            name='Смартфон POCO X3 Pro 8GB/256GB (синий)',
            price=1049.0,
            price_currency='BYN',
        )

        agent.process_product(item)
