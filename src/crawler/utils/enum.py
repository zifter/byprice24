from crawler.utils.base import KeywordsEnum


class ProductCategoryEnum(KeywordsEnum):

    def __init__(self, *args):
        self._value_, self.keywords = args

    NOTEBOOK = 'notebook', ('ноутбуки', 'notebooks', 'notebook')
    SMARTPHONE = 'smartphone', ('смартфоны', 'smartphones', 'mobile', 'phone', 'мобильные телефоны')
