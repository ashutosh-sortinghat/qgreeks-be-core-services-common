from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta():
        model = StockDetails
        fields = "__all__"


# class MySerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100)
#     email = serializers.EmailField()
#     age = serializers.IntegerField(min_value=0)

class InsightStatsSerializer(serializers.Serializer):
    longitude = serializers.FloatField()
