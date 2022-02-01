from common.category import get_category
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


class Category:
    MOBILE = get_category('mobile')
    NOTEBOOK = get_category('notebook')
    DISPLAY = get_category('display')
    DESKTOP = get_category('desktoppc')
    TV = get_category('tv')
    TABLET = get_category('tabletpc')
    HEADPHONE = get_category('headphones')
    LEGO = get_category('buildingkit')
    COSMETIC = get_category('face_makeup')  # TODO Remove me
    BOOK = get_category('books')
    SMART_GADGET = get_category('smartwatch')  # TODO Remove me
