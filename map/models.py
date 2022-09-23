from django.db import models


# Create your models here.

class SearchCriteria(models.Model):
    suburb = models.CharField(max_length=100)
    bedrooms = models.IntegerField(max_length=2)
    bathrooms = models.IntegerField(max_length=2)
    cars = models.IntegerField(max_length=2)

    def __str__(self):
        return f"{self.suburb}"
