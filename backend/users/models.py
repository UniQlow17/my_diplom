from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Кастомный класс пользователя.
    """

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)
    email = models.EmailField(unique=True)
    image = models.ImageField('Фото', upload_to='users_images/', blank=True)

    def __str__(self):
        return self.username
