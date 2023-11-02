from django_filters import rest_framework as filters
from apps.app.models import *
from django.db.models import  fields
from apps.app.models import *
import django_filters
from django.db.models import F, Q, Sum, ExpressionWrapper



class ProductFilter(filters.FilterSet):
    class Meta:
        model = Product
        fields = ['category',]

class TradeFilter(django_filters.FilterSet):
    STATUS_CHOICES = (
        ("To'langan", "To'langan"),
        ('Qarzdorlik', 'Qarzdorlik'),
        ('Shartnoma yakunlangan', 'Shartnoma yakunlangan'),
    )
    client_name = django_filters.CharFilter(field_name='client_name', lookup_expr='icontains')
    client_num = django_filters.CharFilter(field_name='client_num', lookup_expr='icontains')
    imeika = django_filters.CharFilter(field_name='imeika', lookup_expr='icontains')
    next_pay = django_filters.CharFilter(field_name='next_pay', lookup_expr='icontains')
    status = django_filters.CharFilter(method='filter_status')

    # method='filter_status'

    def filter_status(self, queryset, name, value):
        today = timezone.localdate()
        queryset = queryset.annotate(
            total2=ExpressionWrapper(
                (F('price') + F('profit')),
                output_field=fields.FloatField()
            ),
            total_payments=Sum('payments__summa'),
            debt_f=F('total2') - F('total_payments')
        )
        for i in queryset:
            print(i.id, i.debt_f, i.next_pay)
        if value == "Shartnoma yakunlangan":
            return queryset.filter(debt_f=0)
        elif value == "Qarzdorlik":
            return queryset.filter(Q(Q(debt_f__gt=0) | Q(debt_f=None)) & Q(next_pay__lt=today))
        elif value == "To'langan":
            return queryset.filter(Q(Q(debt_f__gt=0) | Q(debt_f=None)) & Q(next_pay__gte=today))
        return queryset
    class Meta:
        model = Trade
        fields = ['client_name', 'dedline', 'start', 'status','product']
