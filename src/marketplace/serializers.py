from datetime import datetime

from marketplace.models import Marketplace
from marketplace.models import Product
from marketplace.models import ProductPage
from marketplace.models import ProductState
from rest_framework import serializers


class MarketplaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marketplace
        fields = '__all__'


class ProductStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductState
        fields = '__all__'


class ProductPageSerializer(serializers.ModelSerializer):
    product_state = ProductStateSerializer(many=True)
    marketplace = MarketplaceSerializer()

    class Meta:
        model = ProductPage
        fields = ['marketplace', 'url', 'product_state']

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['product_state'] = sorted(response['product_state'],
                                           key=lambda x: datetime.strptime(x['created'], '%Y-%m-%dT%H:%M:%SZ'))
        response['product_state'] = response.get('product_state', [[]])[-1]
        return response


class ProductAvailabilitySerializer(serializers.ModelSerializer):
    product_pages = ProductPageSerializer(many=True, read_only=True, )

    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'description', 'preview_url', 'product_pages']

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['product_pages'] = sorted(response['product_pages'], key=lambda x: float(x['product_state']['price']))
        return response
