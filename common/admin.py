from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Region, District

admin.site.unregister(Group)
admin.site.site_header = "eCommerce Admin"
admin.site.site_title = "eCommerce Admin Portal"
admin.site.index_title = "Welcome to eCommerce Admin Panel"
admin.site.empty_value_display = "Mavjud Emas"


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    list_per_page = 10



@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ("name", 'region')
    search_fields = ("name",)
    list_per_page = 10