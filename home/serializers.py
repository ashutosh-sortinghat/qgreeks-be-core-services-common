from rest_framework import serializers
from home.models import StockDetails, StockScreener


class StockDetailsSerializer(serializers.HyperlinkedModelSerializer):
    stock_id = serializers.ReadOnlyField()
    market_cap = serializers.DecimalField(max_digits=1000, decimal_places = 2)
    price = serializers.DecimalField(max_digits=1000, decimal_places=2)
    class Meta:
        model = StockDetails
        fields = "__all__"
        # exclude = ["stock_id", "id"]


class StockScreenerSerializer(serializers.HyperlinkedModelSerializer):
    stock_screener_id = serializers.ReadOnlyField()

    class Meta:
        model = StockScreener
        fields = "__all__"
        extra_kwargs = {
            'url': {'view_name': 'StockScreener-detail', 'lookup_field': 'stock_screener_id'},
            'users': {'lookup_field': 'stock_screener_id'}
        }
    
