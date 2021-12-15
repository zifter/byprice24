from marketplace.models import Marketplace
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
