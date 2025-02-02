from django.db import models
from django.utils.translation import gettext_lazy as _

from .accounts import CustomUser
from common.models import BaseModel, Region, District
from common.file_path_renamer import PathAndRename


user_avatar_path = PathAndRename("avatars/")


class Profile(BaseModel):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    avatar = models.ImageField(
        upload_to=user_avatar_path, blank=True, null=True,
        verbose_name=_("Avatar"))
    bio = models.TextField(blank=True, null=True, verbose_name=_("Bio"))
    birth_date = models.DateField(
        blank=True, null=True, verbose_name=_("Birth Date"))
    region = models.ForeignKey(
        Region, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_("Region"))
    district = models.ForeignKey(
        District, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_("District"))
    address = models.CharField(
        max_length=250, null=True, blank=True, verbose_name=_("Address"))

    def __str__(self):
        return f"{self.user.email} Profile"
    
    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")
        db_table = "profiles"
