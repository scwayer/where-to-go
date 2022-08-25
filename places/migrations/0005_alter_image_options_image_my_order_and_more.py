# Generated by Django 4.1 on 2022-08-25 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_auto_20220825_1825'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['my_order']},
        ),
        migrations.AddField(
            model_name='image',
            name='my_order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='image',
            name='position',
            field=models.PositiveIntegerField(null=True, verbose_name='Позиция'),
        ),
    ]