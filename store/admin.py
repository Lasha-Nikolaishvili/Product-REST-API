from django.contrib import admin
from store.models import Product, ProductCategory


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'stock']
    list_filter = ['price', 'stock']
    search_fields = ['name']
    list_per_page = 10


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category']
    list_per_page = 10
