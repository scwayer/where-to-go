# Generated by Django 4.1 on 2022-08-25 20:02

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_place_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='content',
        ),
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(default='', verbose_name='Описание'),
        ),
    ]
