from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import CustomUser, Profile


@admin.register(CustomUser)
class UserAdmin(BaseUserAdmin):
    list_display = (
        "email",
        "first_name",
        "last_name",
        "is_active",
        "is_staff",
        "is_superuser"
    )

    list_filter = ["email", "first_name", "is_active"]
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login",)}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "usable_password", "password", "password2"),
            },
        ),
    )

    ordering = "email",
    search_fields = ["email"]
    filter_horizontal = (
        "groups",
        "user_permissions",
    )





@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "avatar",
        "bio",
        "birth_date",
        "region",
        "district",
        "address"
    )
    list_filter = (
        "region",
        "district"
    )
    search_fields = ("user__first_name",)
    autocomplete_fields = ["user", "region", "district"]
