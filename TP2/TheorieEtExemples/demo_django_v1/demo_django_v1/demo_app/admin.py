from django.contrib import admin
from .models import Category, Product

admin.site.register(Category)
#admin.site.register(Product)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['code', 'name',]
    list_filter = ['category',]
    #ordering = ['name',]
    #readonly_fields = ['code']
    search_fields = ['code', 'name']
