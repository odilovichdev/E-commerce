from django.db import models


class VariationCategoryChoice(models.TextChoices):
    COLOR = "color", "color"
    SIZE = "size", "size"


class VariationManager(models.Manager):
    def color(self):
        return super(VariationManager, self).filter(
            variation_category=VariationCategoryChoice.COLOR,
            is_active=True
        )

    def size(self):
        return super(VariationManager, self).filter(
            variation_category=VariationCategoryChoice.SIZE,
            is_active=True
        )
