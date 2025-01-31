from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class UserAdmin(BaseUserAdmin):
    list_display = (
        "email", 
        "first_name", 
        "last_name", 
        "password", 
        "is_active",
        "is_staff",
        "is_superuser"
        )
    
    list_filter = ["email", "first_name", "is_active"]
    fieldsets = [
        (None, {"fields": [ "password"]}),
        ("Personal info", {"fields": ["email", "first_name", "last_name"]}),
        ("Permissions", {"fields": ["is_staff", "is_active", "is_superuser"]}),
    ]

    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "first_name","password1", "password2"],
            },
        ),
    ]

    ordering = "email",
    search_fields = ["email"]
    filter_horizontal = []
