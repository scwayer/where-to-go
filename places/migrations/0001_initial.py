# Generated by Django 3.2.13 on 2022-06-09 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description_short', models.CharField(max_length=300)),
                ('description_long', models.TextField()),
                ('coordinates_lng', models.FloatField()),
                ('coordinates_lat', models.FloatField()),
            ],
        ),
    ]
