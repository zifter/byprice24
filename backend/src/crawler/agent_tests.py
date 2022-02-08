import datetime
from unittest.mock import MagicMock, call

import pytz

from common.item_types import Availability
from common.item_types import Category
from common.shared_queue import FlowQueueBase, ScrapingTarget
from crawler.agent import Agent
from django.core.management import call_command
from django.test import TestCase

from crawler.models import ScrapingState
from scraper.items import ProductScrapingResult


class AgentTestCase(TestCase):
    fixtures = ['test/agent/markets.yaml']

    @classmethod
    def setUpClass(cls):
        call_command('search_index', '--rebuild', '-f')

        super().setUpClass()

    def test_schedule_new_marketplaces(self):
        queue = FlowQueueBase()
        queue.scrape = MagicMock()
        agent = Agent(queue)

        agent.schedule()

        queue.scrape.assert_has_calls([call(
            ScrapingTarget(
                url='https://www.21vek.by',
                domain='www.21vek.by',
                use_proxy=False)),
            call(ScrapingTarget(
                url='https://www.ilp.by',
                domain='www.ilp.by',
                use_proxy=False))])

    def test_schedule_by_cron(self):
        queue = FlowQueueBase()
        queue.scrape = MagicMock()
        agent = Agent(queue)
        agent.now = MagicMock()
        agent.now.return_value = datetime.datetime(2022, 1, 13, 2, 0, 0, tzinfo=pytz.UTC)
        vek21 = ScrapingState.objects.get(id=1)
        ilp = ScrapingState.objects.get(id=2)
        vek21.last_scraping = datetime.datetime(2022, 1, 12, 0, 0, 0)
        vek21.scraping_schedule = "0 0 * * 1 *"
        vek21.save()
        ilp.last_scraping = datetime.datetime(2022, 1, 12, 0, 0, 0)
        ilp.scraping_schedule = "0 0 * * * *"
        ilp.save()

        agent.schedule()

        queue.scrape.assert_has_calls([
            call(ScrapingTarget(
                url='https://www.ilp.by',
                domain='www.ilp.by',
                use_proxy=False))])

    def test_schedule_no_scraping(self):
        queue = FlowQueueBase()
        queue.scrape = MagicMock()
        agent = Agent(queue)
        agent.now = MagicMock()
        agent.now.return_value = datetime.datetime(2022, 1, 13, 2, 0, 0, tzinfo=pytz.UTC)
        vek21 = ScrapingState.objects.get(id=1)
        ilp = ScrapingState.objects.get(id=2)
        vek21.last_scraping = datetime.datetime(2022, 1, 13, 0, 0, 0)
        vek21.save()
        ilp.last_scraping = datetime.datetime(2022, 1, 13, 0, 0, 0)
        ilp.save()

        agent.schedule()

        queue.scrape.assert_has_calls([])

    def test_schedule_marketplace(self):
        queue = FlowQueueBase()
        queue.scrape = MagicMock()
        agent = Agent(queue)
        marketplace = 1

        agent.schedule(marketplace=marketplace)

        queue.scrape.assert_has_calls([call(
            ScrapingTarget(
                url='https://www.21vek.by',
                domain='www.21vek.by',
                use_proxy=False))])

    def test_schedule_force(self):
        queue = FlowQueueBase()
        queue.scrape = MagicMock()
        agent = Agent(queue)
        agent.now = MagicMock()
        agent.now.return_value = datetime.datetime(2022, 1, 13, 2, 0, 0, tzinfo=pytz.UTC)
        vek21 = ScrapingState.objects.get(id=1)
        ilp = ScrapingState.objects.get(id=2)
        vek21.last_scraping = datetime.datetime(2022, 1, 13, 0, 0, 1)
        vek21.save()
        ilp.last_scraping = datetime.datetime(2022, 1, 13, 0, 0, 1)
        ilp.save()

        agent.schedule(force=True)

        queue.scrape.assert_has_calls([call(
            ScrapingTarget(
                url='https://www.21vek.by',
                domain='www.21vek.by',
                use_proxy=False)),
            call(ScrapingTarget(
                url='https://www.ilp.by',
                domain='www.ilp.by',
                use_proxy=False))])


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
            review_count=6,
            preview_url='https://static.21vek.by/img/galleries/6632/831/preview_b/x3pro8gb256gb_poco_01_60dd5ddb2379f.png',
            categories=['Смартфоны, ТВ и электроника', 'Смартфоны, аксессуары', 'Смартфоны']
        )

        agent.process_scraping_result(item)     # check adding new ProductState
        agent.process_scraping_result(item)     # check updating ProductState.last_check field
