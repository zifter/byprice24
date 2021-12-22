from rest_framework import serializers


class ProductSearchSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    category = serializers.CharField()
    description = serializers.CharField()
    preview_url = serializers.CharField()
    min_offer = serializers.DecimalField(max_digits=10, decimal_places=2)
    min_offer_currency = serializers.CharField()
    marketplaces_count_instock = serializers.IntegerField()

    class Meta:
        fields = '__all__'

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['min_offer'] = dict(price=repr.pop('min_offer'),
                                 price_currency=repr.pop('min_offer_currency'))
        return repr


class ProductQuerySerializer(serializers.Serializer):
    query = serializers.CharField(min_length=3)
    page = serializers.IntegerField()
