from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from user.models import User
from django.utils.translation import gettext_lazy as _
from common.models import BaseModel


class Product(BaseModel):
    name = models.CharField(max_length=100)
    content = RichTextUploadingField()
    price = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Mahsulot')
        verbose_name_plural = _('Mahsulotlar')


class FreeProduct(BaseModel):
    product = models.CharField(max_length=120)
    count = models.IntegerField()
    free_products = models.OneToOneField(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product
