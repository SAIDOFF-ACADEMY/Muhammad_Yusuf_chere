from django.db import models
from django.contrib.auth.models import AbstractUser
from shared.models import BaseModel


class CustomUser(AbstractUser, BaseModel):
    telegram_id = models.BigIntegerField(unique=True, null=True, blank=True)
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=150)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


# class UserContactApplication(BaseModel):
#     full_name = models.CharField(max_length=255)
#     phone = models.CharField(max_length=50, unique=True)
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.full_name
#
#     class Meta:
#         verbose_name = 'User Contact Application'
#         verbose_name_plural = 'User Contact Applications'
