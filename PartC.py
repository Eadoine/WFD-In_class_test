from django.db import models

class SalesPerson(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()