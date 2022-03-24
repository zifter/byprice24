import datetime
from unittest.mock import call
from unittest.mock import MagicMock

import pytz
from common.item_types import Availability
from common.shared_queue import FlowQueueBase
from common.shared_queue import ScrapingTarget
from crawler.agent import Agent
from crawler.models import CrawlerState
from django.core.management import call_command
from django.test import TestCase
from scraper.items import ProductScrapingResult


class AgentTestCase(TestCase):
    fixtures = [
        'prod/categories.yaml',
        'test/agent/markets.yaml'
    ]

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
                use_proxy=False,
                follow=True)),
            call(ScrapingTarget(
                url='https://www.ilp.by',
                domain='www.ilp.by',
                use_proxy=False,
                follow=True))])

    def test_schedule_by_cron(self):
        queue = FlowQueueBase()
        queue.scrape = MagicMock()
        agent = Agent(queue)
        agent.now = MagicMock()
        agent.now.return_value = datetime.datetime(2022, 1, 13, 2, 0, 0, tzinfo=pytz.UTC)
        vek21 = CrawlerState.objects.get(id=1)
        ilp = CrawlerState.objects.get(id=2)
        vek21.last_scraping = datetime.datetime(2022, 1, 12, 0, 0, 0, tzinfo=pytz.UTC)
        vek21.scraping_schedule = '0 0 * * 1 *'
        vek21.save()
        ilp.last_scraping = datetime.datetime(2022, 1, 12, 0, 0, 0, tzinfo=pytz.UTC)
        ilp.scraping_schedule = '0 0 * * * *'
        ilp.save()

        agent.schedule()

        queue.scrape.assert_has_calls([
            call(ScrapingTarget(
                url='https://www.ilp.by',
                domain='www.ilp.by',
                use_proxy=False,
                follow=True))])

    def test_schedule_no_scraping(self):
        queue = FlowQueueBase()
        queue.scrape = MagicMock()
        agent = Agent(queue)
        agent.now = MagicMock()
        agent.now.return_value = datetime.datetime(2022, 1, 13, 2, 0, 0, tzinfo=pytz.UTC)
        vek21 = CrawlerState.objects.get(id=1)
        ilp = CrawlerState.objects.get(id=2)
        vek21.last_scraping = datetime.datetime(2022, 1, 13, 0, 0, 0, tzinfo=pytz.UTC)
        vek21.save()
        ilp.last_scraping = datetime.datetime(2022, 1, 13, 0, 0, 0, tzinfo=pytz.UTC)
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
                use_proxy=False,
                follow=True))])

    def test_schedule_force(self):
        queue = FlowQueueBase()
        queue.scrape = MagicMock()
        agent = Agent(queue)
        agent.now = MagicMock()
        agent.now.return_value = datetime.datetime(2022, 1, 13, 2, 0, 0, tzinfo=pytz.UTC)
        vek21 = CrawlerState.objects.get(id=1)
        ilp = CrawlerState.objects.get(id=2)
        vek21.last_scraping = datetime.datetime(2022, 1, 13, 0, 0, 1, tzinfo=pytz.UTC)
        vek21.save()
        ilp.last_scraping = datetime.datetime(2022, 1, 13, 0, 0, 1, tzinfo=pytz.UTC)
        ilp.save()

        agent.schedule(force=True)

        queue.scrape.assert_has_calls([call(
            ScrapingTarget(
                url='https://www.21vek.by',
                domain='www.21vek.by',
                use_proxy=False,
                follow=True)),
            call(ScrapingTarget(
                url='https://www.ilp.by',
                domain='www.ilp.by',
                use_proxy=False,
                follow=True))])

    def test_schedule_productpage(self):
        queue = FlowQueueBase()
        queue.scrape = MagicMock()
        agent = Agent(queue)
        marketplace = 1

        agent.schedule(marketplace=marketplace,
                       url_page='https://www.ilp.by/notebook/acer/nxvller00q',
                       follow=False)

        queue.scrape.assert_has_calls([call(
            ScrapingTarget(
                url='https://www.ilp.by/notebook/acer/nxvller00q',
                domain='www.21vek.by',
                use_proxy=False,
                follow=False))])

    def test_process_product(self):
        mock = FlowQueueBase()
        agent = Agent(mock)

        item = ProductScrapingResult(
            url='https://www.21vek.by/mobile/x3pro8gb256gb_poco_01.html',
            title='Смартфон POCO X3 Pro 8GB/256GB (синий)',
            main_category='mobile',
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
