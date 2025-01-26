from django.contrib import admin
from store.models import Product, ProductCategory


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = "name", "slug", "desc", "price", "category", "is_available"
    # exclude = ("slug",)
    readonly_fields = ("slug",)


@admin.register(ProductCategory)
class ProductCategoryModelAdmin(admin.ModelAdmin):
    list_display = ("name", )
