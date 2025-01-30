from django.db import models
from django.utils.translation import gettext_lazy as _
from common.models import BaseModel
from store.models import Product
from store.managers import VariationManager, VariationCategoryChoice

class Variation(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name="variations")
    variation_category = models.CharField(max_length=255,
        choices=VariationCategoryChoice.choices, 
        verbose_name=_("Variation Category"))
    variation_value = models.CharField(max_length=255,
        verbose_name=_("Variation Value"))
    is_active = models.BooleanField(default=True)
    

    objects = VariationManager()

    def __str__(self):
        return self.variation_value


    class Meta:
        verbose_name = _("Variation")
        verbose_name_plural = _("Variations")
        db_table = "variations"
    