from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets
from app.filters import *
from app.serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import pagination
from rest_framework.response import Response
# Create your views here.
from .models import *



class GroupPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 50
    queryset = Group.objects.all()
    filterset_class = Group
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



class FacultyViewSet(viewsets.ModelViewSet):
    queryset = Faculty.objects.all().order_by('-id')
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('-id')
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['name']
    filterset_fields = ('category', 'name')
    filterset_class = BookFilter
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
   
class GroupViewSet(viewsets.ModelViewSet):
    # queryset = Trade.objects.all().order_by('-id')
    objects = Group.objects.order_by('-id')
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = GroupPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ('name',)
    filterset_class = GroupFilter
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    
    