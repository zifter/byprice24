from marketplace.models import Marketplace
from marketplace.models import Product
from marketplace.models import ProductPage
from marketplace.models import ProductState

marketplace = Marketplace(
    domain='www.test.by',
    description='too long',
    logo_url='https://test',
)

product = Product(
    name='iPone',
    category='electronic',
    description='??',
)

product_page = ProductPage(
    product=product,
    marketplace=marketplace,
    url='www.test.by/ipone',
)

product_state = ProductState(
    product_page=product_page,
    price=199,
    price_currency='BYN',
)


def test_marketplace_is_printable_ok():
    assert str(marketplace) == 'www.test.by'


def test_product_is_printable_ok():
    assert str(product) == 'iPone'


def test_product_page_is_printable_ok():
    assert str(product_page) == 'iPone [www.test.by]'


def test_product_state_is_printable_ok():
    assert str(product_state) == 'iPone [www.test.by] [199 BYN]'
