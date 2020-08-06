from django.contrib.auth.models import AbstractUser
from django.db import models


class ShopUser(AbstractUser):
    avatar = models.ImageField(verbose_name='аватарка', upload_to='avatars', blank=True, null=True)
    age = models.PositiveSmallIntegerField(verbose_name='возраст', blank=True, null=True)

