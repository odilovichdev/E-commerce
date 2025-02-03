from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Region(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = _("Region")
        verbose_name_plural = _("Regions")
        db_table = "regions"


class District(models.Model):
    name = models.CharField(max_length=250)
    region = models.ForeignKey(
        Region, on_delete=models.CASCADE, related_name="district")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = _("District")
        verbose_name_plural = _("Districts")
        db_table = "districts"
