from django.db import models
from users.models import CustomUser
from ckeditor_uploader.fields import RichTextUploadingField

CREATED, IN_PROGRESS, ON_THE_WAY, DELIVERED, CANCELLED = (
    'created', 'in_progres', 'on_the_way', 'delivered', 'cancelled')


class Product(models.Model):
    name_uz = models.CharField(max_length=100)
    name_ru = models.CharField(max_length=100)
    content_uz = RichTextUploadingField()
    content_ru = RichTextUploadingField()
    price = models.BigIntegerField()

    def __str__(self):
        return self.name_uz

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Order(models.Model):
    StatusOrder = (
        (CREATED, CREATED),
        (IN_PROGRESS, IN_PROGRESS),
        (ON_THE_WAY, ON_THE_WAY),
        (DELIVERED, DELIVERED),
        (CANCELLED, CANCELLED),
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField()
    free_count = models.IntegerField(default=0)
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='orders')
    longitude = models.FloatField()
    latitude = models.FloatField()
    status = models.CharField(max_length=100, choices=StatusOrder)
    status_changed_at = models.DateTimeField(auto_now=True)
    product_price = models.BigIntegerField()
    total_price = models.BigIntegerField()
    admin = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='admin')

    def __str__(self):
        return f'Order by {self.customer}'

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class FreeProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField()
    free_count = models.IntegerField()

    def __str__(self):
        return f'{self.product} - {self.count}'

    class Meta:
        verbose_name = 'Free Product'
        verbose_name_plural = 'Free Products'


class GalleryPhoto(models.Model):
    photo = models.FileField(upload_to='photos')

    def __str__(self):
        return self.photo.name

    class Meta:
        verbose_name = 'Gallery Photo'
        verbose_name_plural = 'Gallery Photos'

