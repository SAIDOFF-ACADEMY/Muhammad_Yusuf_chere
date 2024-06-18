from django.db import models
from users.models import User
from shared.models import BaseModel
from ckeditor_uploader.fields import RichTextUploadingField


class Product(BaseModel):
    name = models.CharField(max_length=100)
    content = RichTextUploadingField()
    price = models.BigIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Order(models.Model):

    class Status(models.TextChoices):
        CREATED = 'created'
        IN_PROGRESS = 'in_progres'
        ON_THE_WAY = 'on_the_way'
        DELIVERED = 'delivered'
        CANCELLED = 'cancelled'

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField()
    free_count = models.IntegerField(default=0)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    longitude = models.FloatField()
    latitude = models.FloatField()
    status = models.TextField(max_length=100, choices=Status)
    status_changed_at = models.DateTimeField(auto_now=True)
    product_price = models.BigIntegerField()
    total_price = models.BigIntegerField()
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin')

    def __str__(self):
        return f'Order by {self.customer}'

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class FreeProduct(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField()
    free_count = models.IntegerField()

    def __str__(self):
        return f'{self.product} - {self.count}'

    class Meta:
        verbose_name = 'Free Product'
        verbose_name_plural = 'Free Products'


class GalleryPhoto(BaseModel):
    photo = models.FileField(upload_to='photos')

    def __str__(self):
        return self.photo.name

    class Meta:
        verbose_name = 'Gallery Photo'
        verbose_name_plural = 'Gallery Photos'

