from django_filters import rest_framework as filters
from app.models import *
from django.db.models import  fields
from app.models import *
import django_filters


class BookFilter(filters.FilterSet):
    class Meta:
        model = Book
        fields = ['name',]


class GroupFilter(filters.FilterSet):
    class Meta:
        model = Group
        fields = ['name','faculty']
        

class FacultyFilter(filters.FilterSet):
    class Meta:
        model = Faculty
        fields = ['name']