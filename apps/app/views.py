from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets
from apps.app.filters import ProductFilter, TradeFilter
from apps.app.serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import pagination
from rest_framework.response import Response
# Create your views here.
from .models import *

from rest_framework.views import APIView
from rest_framework.response import Response

class TradePagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 50
    queryset = Trade.objects.all()
    filterset_class = Trade
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response({
            'page_size': self.page_size,
            'total_objects': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'current_page_number': self.page.number,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data,
        })



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('-id')
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-id')
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['name']
    filterset_fields = ('category', 'name')
    filterset_class = ProductFilter
    permission_classes = [IsAuthenticatedOrReadOnly]
    # pagination_class = ProductPagination
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
   
class TradeViewSet(viewsets.ModelViewSet):
    # queryset = Trade.objects.all().order_by('-id')
    objects = Trade.objects.order_by('-id')
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = TradePagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ('imeika','client_num','client_name','price','dedline','client_passport','start')
    filterset_fields = ('status', )
    filterset_class = TradeFilter
    queryset = Trade.objects.all()
    serializer_class = TradeSerializer
    
    
class AllTradeViewSet(viewsets.ModelViewSet):
    objects = Trade.objects.order_by('-id')
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ('imeika','client_num','client_name','price','dedline','client_passport','start')
    filterset_fields = ('status', )
    filterset_class = TradeFilter
    queryset = Trade.objects.all()
    serializer_class = AllTradeSerializer
    
# class TradeAPIView(APIView):
#     def get(self, request, id):
#         trade = Trade.objects.get(id=id)
#         payments = trade.trades_clients.all()
#         serializer = TradeSerializer(trade, context={'payments':payments})
#         return Response(status=status.HTTP_200_OK)


class PaymentsViewSet(viewsets.ModelViewSet):
    objects = Trade.objects.order_by('-id')
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer