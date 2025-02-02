from django.contrib import admin
from django.utils.html import format_html
from store.models import Product, ProductCategory,  ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    max_num = 5


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = (
        "image_tags",
        "name",
        'stock',
        "price", 
        "category", 
        "is_available"
        )
    list_filter = ("category", "is_available", "is_active")
    search_fields = ("name", "category__name")
    inlines = [ProductImageInline]
    prepopulated_fields = {"slug": ("name",)}
    

    def image_tags(self, obj):
        return format_html('<img src="{}" width="100" height="100"/>'.format(obj.image.url))
    
    image_tags.short_description = "Images"


@admin.register(ProductCategory)
class ProductCategoryModelAdmin(admin.ModelAdmin):
    list_display = ("name", )


