from django.db import models


class User(models.Model):
    name = models.CharField(max_length=10)
    password1 = models.CharField(max_length=12)

