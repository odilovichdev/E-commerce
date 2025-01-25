from django.contrib import admin
from store.models import Product, ProductCategory


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductCategory)
class ProductCategoryModelAdmin(admin.ModelAdmin):
    pass
