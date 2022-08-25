from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    description_short = models.CharField(max_length=255, verbose_name="Короткое описание")
    description_long = models.TextField(verbose_name="Описание")
    coordinates_lng = models.FloatField(verbose_name="Долгота")
    coordinates_lat = models.FloatField(verbose_name="Широта")

    def __str__(self):
        return self.title


class Image(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(verbose_name="Картинка")
    place = models.ForeignKey(Place, on_delete=models.CASCADE, null=True)
    position = models.IntegerField(null=True, verbose_name="Позиция")

    def __str__(self):
        return self.title
