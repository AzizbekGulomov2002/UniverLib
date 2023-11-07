from django.contrib import admin
from .models import *


# class BookInline(admin.TabularInline): 
#     model = Book
#     fields = ["name","file"]
# admin.site.register(Book)


# class GroupAdmin(admin.ModelAdmin):
#     list_filter = ['name']
#     inlines = [BookInline, ]
#     list_display = ["name"]
#     list_per_page = 10
# @admin.register(Group)    
    
@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name',)


class BookInline(admin.TabularInline): 
    model = Book
    fields = ["name","file"]
    # readonly_fields = ('difference',) 
admin.site.register(Book)

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_filter = ['name']
    inlines = [BookInline, ]
    list_display = ["name"]
    list_per_page = 10
