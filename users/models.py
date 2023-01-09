from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):  # we extend base user model and add user image
    image = models.ImageField(upload_to='user_images', null=True, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
