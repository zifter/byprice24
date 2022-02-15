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


def test_product_data_port_in_url():
    item = ProductScrapingResult(
        url='https://www.funtastik.by:443/igrushki/konstruktory/myagkiy-konstruktor-38-detaley/',
        title='Мягкий конструктор Mommy Love, 38 деталей',
        main_category='buildingkit',
        description='test',
        price=18.53,
        price_currency='BYN',
    )

    data = ProductData(item)

    assert data.domain == 'www.funtastik.by'


def test_product_data_ad_params_in_url():
    item = ProductScrapingResult(
        url='https://www.funtastik.by:443/igrushki/konstruktory/konstruktor-lego-minecraft-21164-korallovyy-rif/?utm_source=yandex&yclid=601272390574470559&utm_medium=cpc&utm_campaign=dinamicheskie_smotreli_na_nashem_sajte_YAD_rsya&utm_term=&utm_content=%7Bcreative%7D%2F%7Bmatchtype%7D%2F%7Badposition%7D%2F%7Bdevice%7D%2F%7Bdevicemodel%7D',
        title='Мягкий конструктор Mommy Love, 38 деталей',
        main_category='buildingkit',
        description='test',
        price=18.53,
        price_currency='BYN',
    )

    data = ProductData(item)

    assert data.url == 'https://www.funtastik.by/igrushki/konstruktory/konstruktor-lego-minecraft-21164-korallovyy-rif/'
