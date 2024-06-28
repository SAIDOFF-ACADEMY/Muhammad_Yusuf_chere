from django.utils.translation import gettext_lazy as _
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated at'))

    class Meta:
        abstract = True


class Page(BaseModel):
    slug = models.SlugField(unique=True)
    title = RichTextUploadingField()
    content = RichTextUploadingField()

    def __str__(self):
        return self.title


class GalleryPhoto(BaseModel):
    photo = models.ImageField(upload_to="gallery/%Y/%m/%d/")


class Settings(BaseModel):
    contact_telegram = models.CharField(max_length=120)
    contact_phone = models.CharField(max_length=120)
    longitude = models.FloatField()
    latitude = models.FloatField()
    locations_text = models.TextField()
    working_horse_start = models.TimeField()
    working_horse_end = models.TimeField()
    telegram_bot = models.CharField(max_length=120)

    def __str__(self):
        return self.contact_phone
