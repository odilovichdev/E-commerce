from django.db import models

class VariationManager(models.Manager):
    def color(self):
        return super(VariationManager, self).filter(
            variation_category="color", is_active=True
        )
    
    def size(self):
        return super(VariationManager, self).filter(
            variation_category="size", is_active=True
        )