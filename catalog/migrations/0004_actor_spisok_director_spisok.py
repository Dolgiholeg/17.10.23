# Generated by Django 4.2.5 on 2023-10-06 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_kino_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='spisok',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Фильмы в которых съиграл'),
        ),
        migrations.AddField(
            model_name='director',
            name='spisok',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Фильмы которые снял'),
        ),
    ]
