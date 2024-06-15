from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Settings(models.Model):
    contact_telegram = models.CharField(max_length=120)
    contact_phone = models.CharField(max_length=30)
    longitude = models.BigIntegerField()
    latitude = models.BigIntegerField()
    location_text = models.TextField()
    working_hours_start = models.TimeField()
    working_hours_end = models.TimeField()
    telegram_bot = models.CharField(max_length=120)

    class Meta:
        verbose_name = 'Settings'
        verbose_name_plural = "Settings"


class Page(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, max_length=250)
    content = RichTextUploadingField()