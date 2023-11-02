from rest_framework import serializers
from .models import *
from rest_framework import fields

from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id","category","name","desc"]
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['category'] = CategorySerializer(instance=instance.category).data
        return representation
    


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = ('id','pay_type','trade','summa', 'date', 'finish','desc')
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # representation['trade'] = TradeSerializer(instance=instance.trade).data
        return representation

class TradeSerializer(serializers.ModelSerializer):
    payments = PaymentsSerializer(many=True, read_only=True)
    class Meta:
        model = Trade
        fields = ('id',"type_pay",'client_num','client_name','client_passport','imeika','product','price','profit','dedline','start','next_pay','end',"total",'common_payment','debt_balance','payments','monthly_pay','status','pay_day','desc','calculate_dollar','calculate_sum')
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['product'] = ProductSerializer(instance=instance.product).data
        return representation




class AllTradeSerializer(serializers.ModelSerializer):
    payments = PaymentsSerializer(many=True, read_only=True)
    class Meta:
        model = Trade
        fields = ('id',"type_pay",'client_num','client_name','client_passport','imeika','product','price','profit','dedline','start','next_pay','end',"total",'common_payment','debt_balance','payments','monthly_pay','status','pay_day','desc','calculate_dollar','calculate_sum')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['product'] = ProductSerializer(instance=instance.product).data
        return representation



