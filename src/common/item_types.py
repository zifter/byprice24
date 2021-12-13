from common.enums import ExtendedEnum


# https://schema.org/ItemAvailability
class Availability(ExtendedEnum):
    BackOrder = 'BackOrder'
    Discontinued = 'Discontinued'
    InStock = 'InStock'
    InStoreOnly = 'InStoreOnly'
    LimitedAvailability = 'LimitedAvailability'
    OnlineOnly = 'OnlineOnly'
    OutOfStock = 'OutOfStock'
    PreOrder = 'PreOrder'
    PreSale = 'PreSale'
    SoldOut = 'SoldOut'


class Category(ExtendedEnum):
    SMARTPHONE = 'Smartphone'
    NOTEBOOK = 'Notebook'
    MONITOR = 'Monitor'
    DESKTOP = 'Desktop'
    TV = 'TV'
    TABLET = 'Tablet'
    HEADPHONE = 'Headphones'
    LEGO = 'ConstructionSet'
    COSMETIC = 'Cosmetic'
    BOOK = 'Book'
    SMART_ACCESSORY = 'SmartAccessory'
