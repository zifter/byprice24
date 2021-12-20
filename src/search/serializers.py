from rest_framework import serializers


class OfferSerializer(serializers.Serializer):
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    price_currency = serializers.CharField()


class ProductSearchSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    category = serializers.CharField()
    description = serializers.CharField()
    preview_url = serializers.CharField()
    # min_offer = OfferSerializer(source='_source.product_page.min_offer')
    # marketplaces_count_instock = serializers.IntegerField(source='_source.product_page.marketplaces_count_instock')

    class Meta:
        fields = '__all__'


class ProductQuerySerializer(serializers.Serializer):
    query = serializers.CharField(min_length=3)
    page = serializers.IntegerField()
