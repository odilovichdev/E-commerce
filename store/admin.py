from django.contrib import admin
from store.models import Product, ProductCategory


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = "name", "slug", "desc", "price", "category", "is_available"
    # exclude = ("slug",)
    readonly_fields = ("slug",)

    def get_fields(self, request, obj = None):
        fields = super().get_fields(request, obj)
        if obj:
            return fields 
        return [field for field in fields if field != "slug"]


@admin.register(ProductCategory)
class ProductCategoryModelAdmin(admin.ModelAdmin):
    list_display = ("name", )
