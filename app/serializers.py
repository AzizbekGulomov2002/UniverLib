from rest_framework import serializers
from .models import *
from rest_framework import fields

from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = "__all__"

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id","name","file"]
   
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["id","name",'faculty','desc']