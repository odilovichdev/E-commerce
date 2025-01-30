from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.html import format_html
from store.models import Product, ProductCategory,  ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    max_num = 5


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "image",
        'stock',
        "desc", 
        "price", 
        "category", 
        "is_available"
        )
    list_filter = ("category", "is_available", "is_active")
    search_fields = ("name", "category__name")
    inlines = [ProductImageInline]
    # readonly_fields = ("image", )
    

    def image(self, obj):
        return format_html('<img src="{}" width="50" height="50"/>'.format(obj.image.url))
    
    image.short_description = "Images"


@admin.register(ProductCategory)
class ProductCategoryModelAdmin(admin.ModelAdmin):
    list_display = ("name", )

admin.site.unregister(Group)
admin.site.site_header = "eCommerce Admin"
admin.site.site_title = "eCommerce Admin Portal"
admin.site.index_title = "Welcome to eCommerce Admin Panel"
# admin.site.empty_value_display = "Mavjud Emas"
