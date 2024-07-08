from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.translation import gettext_lazy


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Settings(BaseModel):
    objects = models.Manager()

    contact_telegram = models.CharField(max_length=120)
    contact_phone = models.CharField(max_length=30, null=True, blank=True)
    longitude = models.BigIntegerField()
    latitude = models.BigIntegerField()
    location_text = models.TextField(gettext_lazy('location_text'))
    working_hours_start = models.TimeField()
    working_hours_end = models.TimeField()
    telegram_bot = models.CharField(max_length=120)

    class Meta:
        verbose_name = gettext_lazy('Settings')
        verbose_name_plural = gettext_lazy("Settings")
        db_table = 'settings'

    def __str__(self):
        return "Settings"


class Page(BaseModel):
    title = models.CharField(gettext_lazy('title'), max_length=250)
    slug = models.SlugField(unique=True, max_length=250)
    content = RichTextUploadingField(gettext_lazy('content'))

    objects = models.Manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = gettext_lazy('Page')
        verbose_name_plural = gettext_lazy("Pages")
        db_table = 'pages'


class GalleryPhoto(BaseModel):
    photo = models.ImageField(upload_to='photos/%Y/%m/')

    objects = models.Manager()

    def __str__(self):
        return self.photo.name

    class Meta:
        verbose_name = gettext_lazy('Gallery Photo')
        verbose_name_plural = gettext_lazy('Gallery Photos')
        db_table = 'gallery_photo'

