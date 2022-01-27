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


class ProductPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPage
        fields = '__all__'


class ProductStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductState
        fields = '__all__'
        ordering = ('created',)
