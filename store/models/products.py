from django.db import models
from common.models import BaseModel
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import slugify

from common.file_path_renamer import PathAndRename


produc_prumbnail_path_and_rename = PathAndRename("products/trumbnail")
products_images_path_and_rename = PathAndRename("products/images")


class ProductCategory(BaseModel):
    name = models.CharField(max_length=250, verbose_name=_(
        "Name"), db_index=True, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Product Category")
        verbose_name_plural = _("Produc Categories")
        db_table = "produc_category"


class Product(BaseModel):
    name = models.CharField(max_length=255, verbose_name=_(
        "Name"), db_index=True, unique=True)
    slug = models.SlugField(max_length=255, unique=True,
                            blank=True, null=True)
    desc = models.TextField(verbose_name=_("Description"), null=True, blank=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name=_("Price"))

    category = models.ForeignKey(
        ProductCategory, on_delete=models.CASCADE, related_name="products")
    is_available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField(default=0, verbose_name=_("Stock"))
    image = models.ImageField(
        upload_to=produc_prumbnail_path_and_rename, blank=True, null=True)

    def __str__(self):
        return self.name
    
    @property
    def is_in_stock(self):
        return self.stock > 0

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        db_table = 'products'


class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to=products_images_path_and_rename)

    def __str__(self):
        return f"{self.product.name} image"
    
    class Meta:
        verbose_name = _("Product Image")
        verbose_name_plural = _("Product Images")
        db_table = "product_images"
