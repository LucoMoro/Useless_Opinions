from django.db import models

# Create your models here.

class Item(models.Model):
    image = models.ImageField()
    name = models.CharField()
    description = models.CharField()
    price = models.FloatField()

    def __str__(self):
        return self.name
