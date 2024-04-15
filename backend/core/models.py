from django.db import models


class Feedback(models.Model):
    """
    Класс отвечающий за отзывы.
    """

    username = models.CharField('Никнейм', max_length=255)
    text = models.TextField('Отзыв')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
