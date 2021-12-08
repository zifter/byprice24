from typing import List

from marketplace.models import Marketplace
from marketplace.models import Product
from rest_framework import serializers


class MarketplaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marketplace
        fields = '__all__'


class ProductSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        product_offers = self.get_offers(instance)
        return {'marketplaces_count_instock': len(instance.product_pages),
                'min_offer': min(product_offers, key=lambda x: x['price']),
                **super().to_representation(instance)}

    @staticmethod
    def get_offers(instance) -> List[dict, ]:
        price_offers = []
        product_pages = instance.product_pages

        for page in product_pages:
            product_state = max(page.product_state, key=lambda x: x.created)
            price_offers.append(dict(price=float(product_state.price),
                                     price_currency=product_state.price_currency))

        return price_offers


class ProductQuerySerializer(serializers.Serializer):
    query = serializers.CharField(min_length=3)
