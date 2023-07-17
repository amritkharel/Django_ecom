from django.db import models

class Items(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=1000)
    avalability = models.IntegerField(default=0)