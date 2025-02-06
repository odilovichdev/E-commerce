from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from common.models import BaseModel
from ..managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin, BaseModel):
    first_name = models.CharField(max_length=255, verbose_name=_(
        "First Name"), null=True, blank=True)
    last_name = models.CharField(max_length=255, verbose_name=_(
        "Last Name"), null=True, blank=True)
    email = models.EmailField(verbose_name=_("Email"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name"]

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.first_name}"

    @property
    def get_fullname(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        db_table = "accounts"
