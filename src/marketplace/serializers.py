from marketplace.models import Marketplace
from marketplace.models import Product
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
        return {
            'results': super().to_representation(instance)
        }


class ProductSearchSerializer(serializers.Serializer):
    query = serializers.CharField(min_length=3)
