from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
