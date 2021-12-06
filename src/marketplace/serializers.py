from typing import List

from marketplace.models import Marketplace
from marketplace.models import Product
from marketplace.models import ProductPage
from marketplace.models import ProductState
from rest_framework import serializers


class MarketplaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marketplace
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        product_offers = self.get_offers(instance)
        return {'marketplaces_count_instock': len(ProductPage.objects.filter(product=instance)),
                'min_offer': min(product_offers, key=lambda x: x['price']),
                **super().to_representation(instance)}

    @staticmethod
    def get_offers(instance) -> List[dict, ]:
        price_offers = []
        product_pages = ProductPage.objects.filter(product=instance)

        for page in product_pages:
            product_state = ProductState.objects.filter(product_page=page).order_by('-created').first()
            price_offers.append(dict(price=float(product_state.price),
                                     price_currency=product_state.price_currency))

        return price_offers


class ProductSearchSerializer(serializers.Serializer):
    query = serializers.CharField(min_length=3)
