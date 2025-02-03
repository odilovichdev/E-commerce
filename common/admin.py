from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Region, District

admin.site.unregister(Group)
admin.site.site_header = "eCommerce Admin"
admin.site.site_title = "eCommerce Admin Portal"
admin.site.index_title = "Welcome to eCommerce Admin Panel"
admin.site.empty_value_display = "Mavjud Emas"

admin.site.register(Region)
admin.site.register(District)
