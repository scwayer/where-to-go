from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    description_short = models.CharField(max_length=255, verbose_name="Короткое описание")
    description_long = HTMLField(default="", verbose_name="Описание")
    coordinates_lng = models.FloatField(verbose_name="Долгота")
    coordinates_lat = models.FloatField(verbose_name="Широта")

    def __str__(self):
        return self.title


class Image(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(verbose_name="Картинка")
    place = models.ForeignKey(Place, on_delete=models.CASCADE, null=True)
    position = models.PositiveIntegerField(null=True, verbose_name="Позиция")
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)

    def __str__(self):
        return f"{self.my_order} {self.title}"

    class Meta:
        ordering = ["my_order"]