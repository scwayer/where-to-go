# Generated by Django 3.2.15 on 2022-08-25 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_image_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='position',
            field=models.IntegerField(null=True, verbose_name='Позиция'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='place',
            name='coordinates_lat',
            field=models.FloatField(verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='place',
            name='coordinates_lng',
            field=models.FloatField(verbose_name='Долгота'),
        ),
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='place',
            name='description_short',
            field=models.CharField(max_length=255, verbose_name='Короткое описание'),
        ),
        migrations.AlterField(
            model_name='place',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
    ]
