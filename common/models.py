from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from shared.models import BaseModel
from django.utils.translation import gettext_lazy as _


class Settings(BaseModel):
    contact_telegram = models.CharField(max_length=120)
    contact_phone = models.CharField(max_length=30)
    longitude = models.BigIntegerField()
    latitude = models.BigIntegerField()
    location_text = models.TextField()
    working_hours_start = models.TimeField()
    working_hours_end = models.TimeField()
    telegram_bot = models.CharField(max_length=120)

    class Meta:
        verbose_name = _('Settings')
        verbose_name_plural = _("Settings")

    def __str__(self):
        return self.contact_telegram


class Page(BaseModel):
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, max_length=250)
    content = RichTextUploadingField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Page')
        verbose_name_plural = _("Pages")
