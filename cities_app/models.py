from django.db import models
from django.contrib.postgres.fields import ArrayField


class City(models.Model):
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50, blank=True)
    continent = models.CharField(max_length=50)
    description = models.TextField()
    top_3_attractions = ArrayField(models.CharField(max_length=50))
    image = models.TextField()  # some very long image URLs

    def __str__(self):
        return f'{self.city}, {self.country}'
