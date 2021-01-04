from rest_framework import serializers

from .models import Stocks


class StocksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stocks
        # fields = '__all__'
        fields = ('id',
                  'name',
                  'symbol',
                  'aimed_price',
                  'current_price',
                  'user_id')
