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
    options = serializers.HyperlinkedRelatedField(
        view_name='option-detail',
        lookup_field='stock_screener_id',
        many=True,
        read_only=True)
    
    class Meta:
        model = StockScreener
        fields = ["url", "stock_screener_id", "ticker", "options"]
        lookup_field = "stock_screener_id"
        # fields = ["etf"]  # "__all__"
