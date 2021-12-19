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


class OfferSerializer(serializers.Serializer):
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    price_currency = serializers.CharField()


class ProductSearchSerializer(serializers.Serializer):
    id = serializers.IntegerField(source='_source.product.id')
    name = serializers.CharField(source='_source.product.name')
    category = serializers.CharField(source='_source.product.category')
    description = serializers.CharField(source='_source.product.description')
    preview_url = serializers.CharField(source='_source.product.preview_url')
    min_offer = OfferSerializer(source='_source.product_page.min_offer')
    marketplaces_count_instock = serializers.IntegerField(source='_source.product_page.marketplaces_count_instock')

    class Meta:
        fields = '__all__'


class ProductQuerySerializer(serializers.Serializer):
    query = serializers.CharField(min_length=3)
    page = serializers.IntegerField()


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
