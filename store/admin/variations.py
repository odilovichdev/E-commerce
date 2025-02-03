from django.contrib import admin
from store.models import Variation


@admin.register(Variation)
class VariationModelAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "variation_category",
        "variation_value",
        "is_active"
    )
    list_editable = ("is_active",)
    list_filter = (
        "product",
        "variation_category",
        "is_active"
    )
    search_fields = (
        "product__name",
    )
    autocomplete_fields = ("product",)
