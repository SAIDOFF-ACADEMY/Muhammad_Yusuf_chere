from django.db import models
from django.contrib.auth.models import AbstractUser
from shared.models import BaseModel
from django.utils.translation import gettext_lazy as _


class User(AbstractUser, BaseModel):
    telegram_id = models.BigIntegerField(unique=True, null=True, blank=True)
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    lang = models.CharField(max_length=2, choices=(('uz', 'Uzbek'), ('ru', "Russia")), default='uz')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        db_table = 'users'

    username = None
    first_name = None
    last_name = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class UserContactApplication(BaseModel):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=50, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _('User Contact Application')
        verbose_name_plural = _('User Contact Applications')
        db_table = 'user_contact_application'
