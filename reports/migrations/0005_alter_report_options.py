# Generated by Django 3.2 on 2024-04-11 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0004_auto_20240411_1056'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='report',
            options={'ordering': ['-pub_date'], 'verbose_name': 'Отчёт', 'verbose_name_plural': 'Отчёты'},
        ),
    ]