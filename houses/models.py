from django.db import models


class House(models.Model):
    year = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    description = models.TextField()
    imgUrl = models.TextField()
    price = models.IntegerField()
    levels = models.IntegerField()

    def __str__(self):
        return self.description