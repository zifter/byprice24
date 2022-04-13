from marketplace.models import Marketplace
from marketplace.models import Product
from marketplace.models import ProductPage
from marketplace.models import ProductState
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from search.serializers import OfferSerializer


class MarketplaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marketplace
        fields = [
            'domain',
            'logo_url',
            'description',
            'delivery',
        ]


class ProductStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductState
        fields = [
            'created',
            'price',
            'price_currency',
            'rating',
            'review_count',
            'availability',
        ]
        ordering = ('created',)


class ProductPageSerializer(serializers.ModelSerializer):
    product_states = ProductStateSerializer(many=True)
    marketplace = MarketplaceSerializer()

    class Meta:
        model = ProductPage
        fields = ['marketplace', 'url', 'product_states', 'name']

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['product_states'] = sorted(response['product_states'], key=lambda x: x['created'])
        response['product_states'] = response.get('product_states', [[]])[-1]
        return response


class ProductDetailsSerializer(serializers.ModelSerializer):
    product_pages = ProductPageSerializer(many=True, read_only=True, )

    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'categories', 'description', 'preview_url', 'product_pages']

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['product_pages'] = sorted(response['product_pages'], key=lambda x: float(x['product_states']['price']))
        return response


class ProductsQuerySerializer(serializers.Serializer):
    id = serializers.IntegerField()


class ProductListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    category = serializers.CharField()
    preview_url = serializers.CharField()
    min_offer = SerializerMethodField()

    def get_min_offer(self, obj):
        serializer = OfferSerializer(data=dict(price=obj.price, price_currency=obj.price_currency))
        serializer.is_valid(raise_exception=True)
        return serializer.data

    class Meta:
        fields = '__all__'
