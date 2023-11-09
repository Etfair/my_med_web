from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Пользователь"""
    username = None
    email = models.EmailField(verbose_name='почта', unique=True)

    is_active = models.BooleanField(default=True)
    rnd_key = models.IntegerField(default=0, verbose_name='ключ для верификации')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
