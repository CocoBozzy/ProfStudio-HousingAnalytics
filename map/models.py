from django.db import models


# Create your models here.
class SearchCriteria(models.Model):
    suburb = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.suburb}"
