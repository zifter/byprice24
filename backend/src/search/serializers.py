from rest_framework import serializers
from rest_framework.fields import SerializerMethodField


class OfferSerializer(serializers.Serializer):
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    price_currency = serializers.CharField()


class ProductSearchSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    category = serializers.CharField()
    description = serializers.CharField()
    preview_url = serializers.CharField()
    marketplaces_count_instock = serializers.IntegerField()
    min_offer = SerializerMethodField()

    def get_min_offer(self, obj):
        serializer = OfferSerializer(data=dict(price=obj.price, price_currency=obj.price_currency))
        serializer.is_valid(raise_exception=True)
        return serializer.data

    class Meta:
        fields = '__all__'


class ProductQuerySerializer(serializers.Serializer):
    query = serializers.CharField(min_length=3)
    page = serializers.IntegerField()
    ordering = serializers.CharField(min_length=3, allow_null=True)
