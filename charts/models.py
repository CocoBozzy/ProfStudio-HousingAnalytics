from django.db import models

# Create your models here.

class House(models.Model):
    state = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return "{}-{}".format(self.state, self.price)


