from django.db import models
from users.models import User
from shared.models import BaseModel
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import gettext_lazy as _


class Product(BaseModel):
    name = models.CharField(max_length=100)
    content = RichTextUploadingField()
    price = models.BigIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
        db_table = 'products'


class FreeProduct(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='free_products')
    count = models.IntegerField()
    free_count = models.IntegerField()

    def __str__(self):
        return f'{self.product} - {self.count}'

    class Meta:
        verbose_name = _('Free Product')
        verbose_name_plural = _('Free Products')
        db_table = 'free_products'


class GalleryPhoto(BaseModel):
    photo = models.FileField(upload_to='photos/%Y/%m/')

    def __str__(self):
        return self.photo.name

    class Meta:
        verbose_name = _('Gallery Photo')
        verbose_name_plural = _('Gallery Photos')
        db_table = 'gallery_photo'

