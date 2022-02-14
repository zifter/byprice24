from crawler.structs import ProductData
from scraper.items import ProductScrapingResult


def test_product_data():
    item = ProductScrapingResult(
        url='https://21vek.by/mobile/x3pro8gb256gb_poco_01.html',
        main_category='mobile',
        title='Смартфон POCO X3 Pro 8GB/256GB (синий)',
        description='test',
        price=1049.0,
        price_currency='BYN',
        categories=['Смартфоны, ТВ и электроника', 'Смартфоны, аксессуары', 'Смартфоны']
    )

    data = ProductData(item)

    assert data.domain == '21vek.by'
