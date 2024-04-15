from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Report(models.Model):
    author = models.ForeignKey(
        User,
        related_name='reports',
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )
    title = models.CharField('Отчет', max_length=250)
    text = models.TextField('Данные отчета')
    pub_date = models.DateTimeField(
        'Дата и время публикации',
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        ordering = ["-pub_date"]
        verbose_name = 'Отчёт'
        verbose_name_plural = 'Отчёты'

    def __str__(self):
        return self.title


class Param(models.Model):
    name = models.CharField('Название', max_length=254)
    slug = models.SlugField('Слаг', max_length=254)

    class Meta:
        verbose_name = 'Параметр'
        verbose_name_plural = 'Параметры'

    def __str__(self):
        return f'{self.name} - {self.slug}'


class Style(models.Model):
    name = models.CharField('Название', max_length=254)
    slug = models.SlugField('Слаг', max_length=254)

    class Meta:
        verbose_name = 'Стиль'
        verbose_name_plural = 'Стили'

    def __str__(self):
        return f'{self.name} - {self.slug}'


class Rule(models.Model):
    style = models.ForeignKey(
        Style,
        related_name='rules',
        on_delete=models.CASCADE,
        verbose_name='Стиль'
    )
    param = models.ForeignKey(
        Param,
        related_name='rules',
        on_delete=models.CASCADE,
        verbose_name='Параметр'
    )
    value = models.CharField('Значение', max_length=254)

    class Meta:
        verbose_name = 'Правило'
        verbose_name_plural = 'Правила'

    def __str__(self):
        return f'{self.style} - {self.param} - {self.value}'
