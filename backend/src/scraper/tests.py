import pytest
from common.item_types import Availability
from common.item_types import Category
from scraper.items import ProductScrapingResult
from scraper.testing_utils import assert_spider


test_data = {
    'texus.by': [
        ('mobilnyy_telefon_bq_dream_32mb_32mb_tyemno_siniy_discount.html',
         ProductScrapingResult(
             url='https://texus.by/catalog/mobilnye_telefony/mobilnyy_telefon_bq_dream_32mb_32mb_tyemno_siniy/',
             title='Мобильный телефон BQ Dream 32Mb/32Mb тёмно-синий Код 203905',
             description='2.4"TFT (240x320) Защита от царапин: Есть / Поддержка: 2 SIM, SIM: Стандартная / 32Mb / 32Mb / Есть / USB:micro USB / Аудиовых: Есть / 800 мАч / тёмно-синий / пластик/ 106 г',
             price=80.50,
             price_currency='BYN',
             availability=Availability.InStock,
             preview_url='https://texus.by/upload/Sh/imageCache/220/632/6083bb29b3ca0314102aa8ce788a6a97.jpeg',
             rating=0.0,
             review_count=0,
             main_category=Category.MOBILE,
             categories=[],
         )
         ),
        ('mobilnyy_telefon_xiaomi_redmi_9a_2gb_32gb_zelyenyy.html',
         ProductScrapingResult(
             url='https://texus.by/catalog/mobilnye_telefony/mobilnyy_telefon_xiaomi_redmi_9a_2gb_32gb_zelyenyy/',
             title='Мобильный телефон Xiaomi Redmi 9a 2Gb/32Gb зелёный Код 171069',
             description='6.53"IPS (720x1600) / Поддержка: 2 SIM / Android 10.0 / MediaTek Helio G252000 МГц Кол-во ядер: 8 / 2Gb / 32Gb / GPS/A-GPS: Есть / Wi-Fi: Есть / Есть / USB:micro USB / Аудиовых: Есть / 5 000 мАч / зелёный/ 194 г',
             price=299.00,
             price_currency='BYN',
             availability=Availability.InStock,
             preview_url='https://texus.by/upload/Sh/imageCache/dd5/18e/0f0fcc05b510be63d3a875750b1bc0f8.jpeg',
             rating=0.0,
             review_count=0,
             main_category=Category.MOBILE,
             categories=[],
         )
         ),
        ('monitor_21_5_acer_kg221qabmix_um_wx1ee_a01.html',
         ProductScrapingResult(
             url='https://texus.by/catalog/monitory/monitor_21_5_acer_kg221qabmix_um_wx1ee_a01/',
             title='Монитор 21.5" Acer KG221QAbmix (UM.WX1EE.A01) Код 205210',
             description='21.5" (1920х1080) 16:9 TN+Film / Отклик: 1 мс / 16.7 млн / Угол обзора верт: 65°/гориз: 90° / Ярк: 200 кд/м2 / Контр: 600:1 / DC:(10 000 000 :1); / HDMI: Нет / DVI: Нет / VGA: 1 / USB 3.1: нет / USB 3.1: нет / USB Type C: нет / Черный / Крепл. к сте',
             price=417.00,
             price_currency='BYN',
             availability=Availability.InStock,
             preview_url='https://texus.by/upload/Sh/imageCache/913/a54/d4b69d8bbd8154250d33656d0a9e1583.jpeg',
             rating=0.0,
             review_count=0,
             main_category=Category.MOBILE,
             categories=[],
         )
         ),
    ]
}


def test_spider_ilpby():
    url = 'https://www.ilp.by/notebook/apple/mxk32'
    expected = ProductScrapingResult(
        url=url,
        title='Apple MacBook Pro 13" Touch Bar 2020 MXK32',
        main_category=Category.NOTEBOOK,
        description='13.3" 2560 x 1600 IPS, Intel Core i5 8257U 1400 МГц, 8 ГБ, SSD 256 ГБ, граф. адаптер: встроенный, Mac OS, цвет крышки серый',
        price=3440.0,
        price_currency='BYN',
        availability=Availability.InStock,
        preview_url='https://cdn.dataimgstore.com/preview/64/3/2626323/y9uMMTST0z.jpeg',
        rating=0.0,
        review_count=0,
        categories=[
            'Ноутбуки'
        ],
    )

    assert_spider(url, 'macbook.html', expected)


def test_spider_21vek_by():
    url = 'https://www.21vek.by/mobile/x3pro8gb256gb_poco_01.html'
    expected = ProductScrapingResult(
        url=url,
        title='Смартфон POCO X3 Pro 8GB/256GB (синий)',
        description='Смартфон POCO X3 Pro 8GB/256GB (синий) по доступной цене в интернет-магазине 21vek.by. POCO X3 Pro 8GB/256GB (синий)  Смартфон  2 SIM-карты  купить в Минске, Гомеле, Витебске, Могилеве, Бресте, Гродно с фото и описанием — доставка по Беларуси',
        price=1049.0,
        price_currency='BYN',
        availability=Availability.InStock,
        preview_url='https://static.21vek.by/img/galleries/6632/831/preview_b/x3pro8gb256gb_poco_01_60dd5ddb2379f.png',
        rating=5.0,
        review_count=4,
        main_category=Category.MOBILE,
        categories=[
            'Смартфоны, ТВ и электроника',
            'Смартфоны, аксессуары',
            'Смартфоны',
        ],
    )

    assert_spider(url, 'poco-pro-x3.html', expected)


def test_spider_amd_by():
    url = 'https://www.amd.by/mobile/poco-x3-pro-6gb128gb-mezhdunarodnaya-versiya-bronzovyi/'
    expected = ProductScrapingResult(
        url=url,
        title='Смартфон POCO X3 Pro 6GB/128GB международная версия (бронзовый)',
        description='Android, экран 6.67" IPS (1080x2400), Qualcomm Snapdragon 860, ОЗУ 6 ГБ, флэш-память 128 ГБ, карты памяти, камера 48 Мп, аккумулятор 5160 мАч, 2 SIM',
        price=873.63,
        price_currency='BYN',
        availability=Availability.InStock,
        preview_url='https://www.amd.by/image/cache/catalog/products/628688/1633610376-500x500.jpg',
        main_category=Category.MOBILE,
        categories=[],
    )

    assert_spider(url, 'poco-pro-x3.html', expected)


def test_funtastik_by():
    url = 'https://www.funtastik.by/igrushki/konstruktory/konstruktor-lego-super-mario-71360-priklyucheniya-vmeste-s-mario-startovyy-nabor/'
    expected = ProductScrapingResult(
        url=url,
        title='Конструктор LEGO City 60297: Разрушительный трюковый мотоцикл',
        description='Конструктор LEGO City 60297: Разрушительный трюковый мотоцикл\nОсобенности:\n- мотоцикл с маховиком;\n- 1 минифигурка в комплекте;\n- набор можно объединять с другими наборами LEGO City.\nРазмер мотоцикла в собранном виде: 6х2х3 см.\nМатериал: пластмасса.\nВ наборе: 12 деталей, 1 минифигурка, инструкция.',
        price=19.61,
        price_currency='BYN',
        availability=Availability.InStock,
        preview_url='https://www.funtastik.by/upload/resize_cache/iblock/2f8/720_720_040cd750bba9870f18aada2478b24840a/2f8c4ef8be4aa902ed0659f02b29607f.jpg',
        main_category=Category.LEGO,
        categories=[],
    )
    assert_spider(url, 'lego-city.html', expected)


def test_spider_ozon_ru():
    url = 'https://www.ozon.ru/product/smartfon-infinix-hot-10-lite-2-32gb-chernyy-272831176/?sh=pcJtVKpF'
    expected = ProductScrapingResult(
        url=url,
        title='Смартфон Infinix HOT 10 Lite 2/32GB, черный',
        description='',
        price=7999.0,
        price_currency='RUB',
        availability=Availability.InStock,
        preview_url='https://cdn1.ozone.ru/s3/multimedia-1/6087434965.jpg',
        main_category=Category.MOBILE,
        rating=4.9,
        review_count=7,
        categories=['Электроника', 'Телефоны и смарт-часы'],
    )

    assert_spider(url, 'Infinix-HOT-10-Lite.html', expected)


@pytest.mark.parametrize('test_html,expected', test_data['texus.by'])
def test_texus_by(test_html, expected):
    assert_spider(expected.url, test_html, expected)
