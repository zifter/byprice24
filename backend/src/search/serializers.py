from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField


class OfferSerializer(serializers.Serializer):
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    price_currency = serializers.CharField()


class ProductSearchSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    category = serializers.CharField()
    category_tr = serializers.CharField()
    description = serializers.CharField()
    preview_url = serializers.CharField()
    marketplaces_count_instock = serializers.IntegerField()
    min_offer = SerializerMethodField()

    @extend_schema_field(OfferSerializer)
    def get_min_offer(self, obj):
        serializer = OfferSerializer(data=dict(price=obj.price, price_currency=obj.price_currency))
        serializer.is_valid(raise_exception=True)
        return serializer.data

    class Meta:
        fields = '__all__'


class ProductSearchQuerySerializer(serializers.Serializer):
    query = serializers.CharField(min_length=3)
    page = serializers.IntegerField()
    ordering = serializers.CharField(min_length=3, allow_null=True)


class ProductSearchResponse(serializers.Serializer):
    count = serializers.IntegerField()
    next_page = serializers.IntegerField()
    previous_page = serializers.IntegerField()
    results = ProductSearchSerializer(many=True)


class ProductSearchAutocompleteQuerySerializer(serializers.Serializer):
    query = serializers.CharField(min_length=3)


class ProductSearchAutocompleteSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    category = serializers.CharField()
    preview_url = serializers.CharField()

    class Meta:
        fields = '__all__'
