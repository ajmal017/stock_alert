from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Stocks
from .serializers import StocksSerializer

#
# @api_view(['GET'])
# def index(request):
#     return Response("Hello, world. You're at the polls index.")
#
# @api_view(['GET'])
# def stocksList(request):
#     stocks = Stocks.objects.all()
#     serializer = StocksSerializer(stocks, many=True)
#     return Response(serializer.data)


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stocks.objects.all().order_by('name')
    serializer_class = StocksSerializer