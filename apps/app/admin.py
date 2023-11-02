from django.contrib import admin

# Register your models here.

from .models import *

# class PaymentsAdmin(admin.ModelAdmin):
#     list_display = ["summa","date","finish","difference"]
#     list_per_page = 10
#     class Meta:
#         model = Payments
# admin.site.register(Payments, PaymentsAdmin)


class PaymentsInline(admin.TabularInline): 
    model = Payments
    fields = ["summa","date","finish",]
    # readonly_fields = ('difference',) 
admin.site.register(Payments)

@admin.register(Trade)
class TradeAdmin(admin.ModelAdmin):
    list_filter = ['price']
    inlines = [PaymentsInline, ]
    list_display = ["total"]
    list_per_page = 10
    
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

    
class ProductAdmin(admin.ModelAdmin):
    list_display = ["category","name",]
    list_per_page = 10
    search_fields = ('category', 'name',)
    class Meta:
        model = Product
admin.site.register(Product, ProductAdmin)


