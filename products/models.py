from django.db import models
from users.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Product(BaseModel):
    name = models.CharField(_('name'), max_length=100)
    content = RichTextUploadingField(_('content'))
    price = models.BigIntegerField()
    is_active = models.BooleanField(_('active'), default=True)

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


