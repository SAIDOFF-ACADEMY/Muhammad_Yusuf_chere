from random import random

from django.db import models


def create_code(self):
    code = ''.join([str(random.randint(0, 100) % 10) for _ in range(4)])
    return code


class Customer(models.Model):
    tg_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100, unique=True)

    objects = models.Manager()


