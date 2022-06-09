from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=100)
    description_short = models.CharField(max_length=300)
    description_long = models.TextField()
    coordinates_lng = models.FloatField()
    coordinates_lat = models.FloatField()

    def __str__(self):
        return self.title
