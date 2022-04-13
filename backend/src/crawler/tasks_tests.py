import pytest
from common.shared_queue import CrawlerTarget
from crawler.tasks import process_product
from crawler.tasks import scrape_target
from marketplace.models import Category
from marketplace.models import Marketplace
from scraper.items import ProductScrapingResult


@pytest.mark.django_db
def test_scrape_target_ok():
    target = CrawlerTarget(
        url='https://www.google.com',
        domain='www.amd.by',
        use_proxy=False,
        follow=False)

    scrape_target(target)


@pytest.mark.django_db
def test_process_scraping_result_ok():
    Marketplace.objects.get_or_create(domain='test.by')
    Category.objects.get_or_create(name='mobile')

    item = ProductScrapingResult(
        url='https://test.by/mobile/x3pro8gb256gb_poco_01.html',
        main_category='mobile',
        title='Смартфон POCO X3 Pro 8GB/256GB (синий)',
        description='test',
        price=1049.0,
        price_currency='BYN',
        categories=['Смартфоны, ТВ и электроника', 'Смартфоны, аксессуары', 'Смартфоны']
    )

    process_product(item)
